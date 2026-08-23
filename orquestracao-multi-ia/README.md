# Orquestração multi-IA

Claude Code orquestra; os workers executam. Tudo isolado nesta pasta (`orquestracao-multi-ia/`) pra não misturar com o conteúdo do squad.

**Status atual: só DeepSeek está ativo.** GPT (OpenAI) e Gemini foram pausados por custo — ver nota em `.claude/agents/roteador.md`. O roteador só despacha trabalho pesado em massa pro DeepSeek; texto criativo e imagem seguem pelos agents `copywriter`/`designer` do squad normalmente, sem custo de API externa.

Comandos abaixo assumem que você está na raiz do workspace (`Pillar/`), não dentro desta pasta.

## Setup (uma vez)

```bash
pip install -r orquestracao-multi-ia/requirements.txt
cp orquestracao-multi-ia/.env.example orquestracao-multi-ia/.env   # preencha DEEPSEEK_API_KEY (GPT e Gemini ficam em branco por enquanto)
```

Chave: DeepSeek em platform.deepseek.com (5M tokens grátis no cadastro). Gemini (aistudio.google.com) e OpenAI (platform.openai.com) ficam disponíveis pra reativar depois, se o custo fizer sentido.

## Teste de fumaça (sem Claude, direto no terminal)

```bash
# Bulk — único worker ativo hoje
python orquestracao-multi-ia/workers/deepseek_bulk.py --entrada orquestracao-multi-ia/tasks/teste.txt \
  --system orquestracao-multi-ia/prompts/tom_de_voz_pillar.txt --saida orquestracao-multi-ia/outputs/teste/bulk.jsonl
```

Já validado: 3 itens, custo real US$ 0,0046. Ver `tasks/teste.txt` / `outputs/teste/bulk.jsonl`.

Os testes de texto (GPT) e imagem (Gemini) abaixo só valem se/quando esses workers forem reativados:

```bash
# Texto (pausado)
python orquestracao-multi-ia/workers/openai_texto.py --prompt "Legenda para post de cimento CP-II em promoção, CTA WhatsApp" \
  --system orquestracao-multi-ia/prompts/tom_de_voz_pillar.txt --n 2 --saida orquestracao-multi-ia/outputs/teste/legendas.md

# Imagem (pausado)
python orquestracao-multi-ia/workers/gemini_imagem.py --prompt "Foto publicitária de sacos de cimento empilhados em loja de material de construção brasileira, iluminação natural" \
  --saida orquestracao-multi-ia/outputs/teste/ --n 1
```

## Uso via Claude Code (fluxo real)

1. Crie a tarefa: um `.md` em `orquestracao-multi-ia/tasks/` (modelo em `tasks/exemplo-post-construmais.md`).
2. No Claude Code: "processe a tarefa orquestracao-multi-ia/tasks/exemplo-post-construmais.md" — o subagent **roteador** despacha para os workers e o **revisor-qa** valida e abre o PR.
3. Você revisa e aprova o PR. Ponto final humano preservado.

## Regras de custo embutidas

- DeepSeek: system prompt sempre em arquivo e idêntico entre chamadas -> cache hit (input ~97% mais barato). Rodar jobs pesados durante o dia em Brasília (off-peak da DeepSeek = metade do preço; o pico deles cai ~22h–01h e 03h–07h no horário de Brasília).
- Trabalho mecânico (padronização, cálculo) nunca passa por IA — Python puro.
- O Claude só lê resumos/amostras dos outputs, nunca arquivos bulk inteiros.
- `deepseek_bulk.py` imprime custo estimado ao final e retoma jobs interrompidos sem reprocessar.

## Verifique antes de reativar GPT/Gemini

- Nome do modelo de imagem: `gemini-2.5-flash-image` (Nano Banana) é legado — a Google recomenda migrar. Padrão atualizado pra `gemini-3.1-flash-lite-image` (mais barato, 1K, suporta 3:4 nativamente). Existem também `gemini-3.1-flash-image` (mais versátil, até 4K) e `gemini-3-pro-image` (qualidade premium), se a Lite não bastar — troque em `GEMINI_IMAGE_MODEL` no `.env`.
- Modelo de texto OpenAI: padrão `gpt-5-mini`; troque em `OPENAI_MODEL` se quiser outro.
- Preços no topo de `deepseek_bulk.py` (usados só na estimativa impressa).
