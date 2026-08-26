#!/usr/bin/env python3
"""
Worker DeepSeek — trabalho pesado em massa (classificação, extração, resumo).

Uso:
  python orquestracao-multi-ia/workers/deepseek_bulk.py \
    --entrada orquestracao-multi-ia/tasks/produtos.jsonl \
    --system orquestracao-multi-ia/prompts/classificar_produto.txt \
    --saida orquestracao-multi-ia/outputs/produtos_classificados.jsonl

Regras de economia:
  - O system prompt fica em arquivo e é enviado IDÊNTICO em toda chamada
    (byte a byte) para maximizar cache hit (~97% de desconto no input).
  - Rodar durante o dia em Brasília = horário off-peak da DeepSeek (metade do preço).
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

from openai import OpenAI

BASE_URL = "https://api.deepseek.com"
MODEL = os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-flash")

# Preços off-peak V4-Flash (USD por 1M tokens) — atualizar se a DeepSeek mudar
PRECO_INPUT_MISS = 0.22
PRECO_INPUT_HIT = 0.007
PRECO_OUTPUT = 0.66


def chamar(client: OpenAI, system_prompt: str, item: str, max_retries: int = 3):
    for tentativa in range(max_retries):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": item},
                ],
                temperature=0.2,
            )
            return resp
        except Exception as exc:
            if tentativa == max_retries - 1:
                raise
            espera = 2 ** tentativa
            print(f"  [retry] {exc} — aguardando {espera}s", file=sys.stderr)
            time.sleep(espera)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", required=True, help="Arquivo com 1 item por linha (txt ou jsonl)")
    ap.add_argument("--system", required=True, help="Arquivo com o system prompt (fixo, para cache)")
    ap.add_argument("--saida", required=True, help="Arquivo jsonl de saída")
    args = ap.parse_args()

    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        sys.exit("ERRO: defina DEEPSEEK_API_KEY como variável de ambiente")

    client = OpenAI(api_key=api_key, base_url=BASE_URL)
    system_prompt = Path(args.system).read_text(encoding="utf-8")
    itens = [l.strip() for l in Path(args.entrada).read_text(encoding="utf-8").splitlines() if l.strip()]

    tokens = {"hit": 0, "miss": 0, "out": 0}
    saida = Path(args.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)

    # Saída incremental: se o job cair no meio, retoma de onde parou
    ja_feitos = 0
    if saida.exists():
        ja_feitos = sum(1 for _ in saida.open(encoding="utf-8"))
        print(f"Retomando: {ja_feitos} itens já processados")

    with saida.open("a", encoding="utf-8") as f:
        for i, item in enumerate(itens):
            if i < ja_feitos:
                continue
            resp = chamar(client, system_prompt, item)
            resultado = resp.choices[0].message.content
            u = resp.usage
            tokens["hit"] += getattr(u, "prompt_cache_hit_tokens", 0) or 0
            tokens["miss"] += getattr(u, "prompt_cache_miss_tokens", u.prompt_tokens) or 0
            tokens["out"] += u.completion_tokens
            f.write(json.dumps({"entrada": item, "resultado": resultado}, ensure_ascii=False) + "\n")
            f.flush()
            if (i + 1) % 25 == 0:
                print(f"  {i + 1}/{len(itens)} itens")

    custo = (
        tokens["miss"] / 1e6 * PRECO_INPUT_MISS
        + tokens["hit"] / 1e6 * PRECO_INPUT_HIT
        + tokens["out"] / 1e6 * PRECO_OUTPUT
    )
    print(f"\nConcluído: {len(itens)} itens -> {saida}")
    print(f"Tokens: {tokens} | Custo estimado (off-peak): US$ {custo:.4f}")


if __name__ == "__main__":
    main()
