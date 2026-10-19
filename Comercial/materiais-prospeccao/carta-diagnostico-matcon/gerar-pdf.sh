#!/usr/bin/env bash
# Gera o PDF de uma carta a partir do HTML.
# Uso: ./gerar-pdf.sh caminho/da/carta.html [saida.pdf]
# Precisa de Chrome, Chromium ou Edge instalado e de internet (as fontes vêm do Google Fonts).
set -euo pipefail
html="${1:?Informe o HTML da carta}"
out="${2:-${html%.html}.pdf}"
for b in google-chrome google-chrome-stable chromium chromium-browser chrome microsoft-edge \
         "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
         "/opt/pw-browsers/chromium"; do
  if command -v "$b" >/dev/null 2>&1 || [ -x "$b" ]; then browser="$b"; break; fi
done
[ -n "${browser:-}" ] || { echo "Chrome/Chromium não encontrado. Abra o HTML no navegador e use Ctrl+P > Salvar como PDF (margens: nenhuma, gráficos de plano de fundo: ligado)."; exit 1; }
"$browser" --headless --no-sandbox --disable-gpu --virtual-time-budget=8000 --no-pdf-header-footer \
  --print-to-pdf="$out" "file://$(cd "$(dirname "$html")" && pwd)/$(basename "$html")" >/dev/null 2>&1
echo "PDF gerado: $out"
