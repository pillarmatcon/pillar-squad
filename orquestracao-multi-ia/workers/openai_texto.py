#!/usr/bin/env python3
"""
Worker OpenAI (GPT) — copy criativa: legendas, e-mails, variações de texto.

Uso:
  python orquestracao-multi-ia/workers/openai_texto.py \
    --prompt-arquivo orquestracao-multi-ia/prompts/legenda_post.txt \
    --system orquestracao-multi-ia/prompts/tom_de_voz_pillar.txt \
    --n 3 \
    --saida orquestracao-multi-ia/outputs/construmais/post_012/legendas.md
"""
import argparse
import os
import sys
from pathlib import Path

from openai import OpenAI

MODEL = os.environ.get("OPENAI_MODEL", "gpt-5-mini")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt-arquivo", help="Arquivo .txt com o pedido")
    ap.add_argument("--prompt", help="Pedido direto na linha de comando")
    ap.add_argument("--system", help="Arquivo com tom de voz / diretrizes da marca")
    ap.add_argument("--n", type=int, default=1, help="Quantas variantes gerar")
    ap.add_argument("--saida", required=True, help="Arquivo .md de saída")
    args = ap.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit("ERRO: defina OPENAI_API_KEY como variável de ambiente")
    if not (args.prompt or args.prompt_arquivo):
        sys.exit("ERRO: informe --prompt ou --prompt-arquivo")

    prompt = args.prompt or Path(args.prompt_arquivo).read_text(encoding="utf-8")
    system = Path(args.system).read_text(encoding="utf-8") if args.system else "Você é redator sênior da Pillar, agência de marketing para lojas de material de construção."

    client = OpenAI(api_key=api_key)
    variantes = []
    for i in range(args.n):
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            temperature=0.9,
        )
        variantes.append(resp.choices[0].message.content.strip())

    saida = Path(args.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    corpo = "\n\n---\n\n".join(f"## Variante {i + 1}\n\n{v}" for i, v in enumerate(variantes))
    saida.write_text(corpo + "\n", encoding="utf-8")
    print(f"OK: {args.n} variante(s) em {saida}")


if __name__ == "__main__":
    main()
