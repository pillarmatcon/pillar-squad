#!/usr/bin/env python3
"""
Worker Gemini (Nano Banana) — geração de imagens 3:4 para posts.

Uso:
  python workers/gemini_imagem.py \
    --prompt-arquivo prompts/post_cimento.txt \
    --saida outputs/construmais/post_012/ \
    --n 2

Cada execução salva imagem_01.png, imagem_02.png... na pasta de saída,
mais um meta.json com o prompt usado (auditabilidade).
"""
import argparse
import json
import os
import sys
from pathlib import Path

from google import genai
from google.genai import types

MODEL = os.environ.get("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image")


def gerar(client: genai.Client, prompt: str):
    try:
        config = types.GenerateContentConfig(
            image_config=types.ImageConfig(aspect_ratio="3:4")
        )
        resp = client.models.generate_content(model=MODEL, contents=prompt, config=config)
    except (AttributeError, TypeError):
        # SDK sem ImageConfig: pede o 3:4 no próprio prompt
        resp = client.models.generate_content(
            model=MODEL, contents=prompt + "\n\nFormato: retrato 3:4 (vertical)."
        )
    imagens = []
    for part in resp.candidates[0].content.parts:
        if getattr(part, "inline_data", None) and part.inline_data.data:
            imagens.append(part.inline_data.data)
    return imagens


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt-arquivo", help="Arquivo .txt com o prompt da imagem")
    ap.add_argument("--prompt", help="Prompt direto na linha de comando")
    ap.add_argument("--saida", required=True, help="Pasta de saída")
    ap.add_argument("--n", type=int, default=2, help="Quantas imagens gerar (padrão: 2)")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("ERRO: defina GEMINI_API_KEY no .env / ambiente")
    if not (args.prompt or args.prompt_arquivo):
        sys.exit("ERRO: informe --prompt ou --prompt-arquivo")

    prompt = args.prompt or Path(args.prompt_arquivo).read_text(encoding="utf-8")
    client = genai.Client(api_key=api_key)
    pasta = Path(args.saida)
    pasta.mkdir(parents=True, exist_ok=True)

    salvas = []
    contador = 1
    tentativas = 0
    while len(salvas) < args.n and tentativas < args.n * 2:
        tentativas += 1
        for data in gerar(client, prompt):
            destino = pasta / f"imagem_{contador:02d}.png"
            destino.write_bytes(data)
            salvas.append(str(destino))
            contador += 1
            if len(salvas) >= args.n:
                break

    (pasta / "meta.json").write_text(
        json.dumps({"modelo": MODEL, "prompt": prompt, "imagens": salvas}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    if not salvas:
        sys.exit("ERRO: nenhuma imagem retornada (verifique modelo/quota)")
    print(f"OK: {len(salvas)} imagem(ns) em {pasta}")


if __name__ == "__main__":
    main()
