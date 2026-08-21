# Orquestração multi-IA — pillar-squad

Claude Code orquestra; os workers executam. Copie estas pastas para a raiz do repositório `calillegit/pillar-squad` (mesclando `.claude/` com a existente).

## Setup (uma vez)

```bash
pip install openai google-genai
cp .env.example .env   # preencha as 3 chaves
echo ".env" >> .gitignore
```

Chaves: DeepSeek em platform.deepseek.com (5M tokens grátis no cadastro), Gemini em aistudio.google.com, OpenAI em platform.openai.com.

## Teste de fumaça (sem Claude, direto no terminal)

```bash
# Texto
python workers/openai_texto.py --prompt "Legenda para post de cimento CP-II em promoção, CTA WhatsApp" \
  --system prompts/tom_de_voz_pillar.txt --n 2 --saida outputs/teste/legendas.md

# Imagem
python workers/gemini_imagem.py --prompt "Foto publicitária de sacos de cimento empilhados em loja de material de construção brasileira, iluminação natural" \
  --saida outputs/teste/ --n 1

# Bulk (crie um jsonl com 3 linhas de teste antes)
python workers/deepseek_bulk.py --entrada tasks/teste.txt \
  --system prompts/tom_de_voz_pillar.txt --saida outputs/teste/bulk.jsonl
```

## Uso via Claude Code (fluxo real)

1. Crie a tarefa: um `.md` em `tasks/` (modelo em `tasks/exemplo-post-construmais.md`).
2. No Claude Code: "processe a tarefa tasks/exemplo-post-construmais.md" — o subagent **roteador** despacha para os workers e o **revisor-qa** valida e abre o PR.
3. Você revisa e aprova o PR. Ponto final humano preservado.

## Regras de custo embutidas

- DeepSeek: system prompt sempre em arquivo e idêntico entre chamadas -> cache hit (input ~97% mais barato). Rodar jobs pesados durante o dia em Brasília (off-peak da DeepSeek = metade do preço; o pico deles cai ~22h–01h e 03h–07h no horário de Brasília).
- Trabalho mecânico (padronização, cálculo) nunca passa por IA — Python puro.
- O Claude só lê resumos/amostras dos outputs, nunca arquivos bulk inteiros.
- `deepseek_bulk.py` imprime custo estimado ao final e retoma jobs interrompidos sem reprocessar.

## Verifique antes do primeiro uso real

- Nome do modelo de imagem: o padrão está `gemini-2.5-flash-image` (Nano Banana). Se a Google tiver renomeado, ajuste `GEMINI_IMAGE_MODEL` no `.env`.
- Modelo de texto OpenAI: padrão `gpt-5-mini`; troque em `OPENAI_MODEL` se quiser outro.
- Preços no topo de `deepseek_bulk.py` (usados só na estimativa impressa).
