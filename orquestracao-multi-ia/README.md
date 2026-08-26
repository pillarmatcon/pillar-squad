# Orquestração multi-IA

Claude Code orquestra; o worker executa. Tudo isolado nesta pasta (`orquestracao-multi-ia/`) pra não misturar com o conteúdo do squad.

**Só DeepSeek é usado.** O roteador despacha trabalho pesado em massa (classificação/extração/parsing de muitos itens) pro DeepSeek; texto criativo e imagem seguem pelos agents `copywriter`/`designer` do squad normalmente, sem custo de API externa.

Comandos abaixo assumem que você está na raiz do workspace (`Pillar/`), não dentro desta pasta.

## Setup (uma vez)

```bash
pip install -r orquestracao-multi-ia/requirements.txt
```

O worker lê a chave só via variável de ambiente do sistema (`os.environ`) — não existe `.env` de fato, o script não carrega esse arquivo (sem `python-dotenv` instalado). Defina `DEEPSEEK_API_KEY` como variável de ambiente do Windows (escopo User) e ela fica disponível pra qualquer sessão nova neste computador, sem precisar tocar em arquivo nenhum. `.env.example` serve só de referência do nome de variável esperado, não é pra copiar/preencher.

Chave: DeepSeek em platform.deepseek.com (5M tokens grátis no cadastro).

## Teste de fumaça (sem Claude, direto no terminal)

```bash
python orquestracao-multi-ia/workers/deepseek_bulk.py --entrada orquestracao-multi-ia/tasks/teste.txt \
  --system orquestracao-multi-ia/prompts/tom_de_voz_pillar.txt --saida orquestracao-multi-ia/outputs/teste/bulk.jsonl
```

Já validado: 3 itens, custo real US$ 0,0046. Ver `tasks/teste.txt` / `outputs/teste/bulk.jsonl`.

## Uso via Claude Code (fluxo real)

1. Crie a tarefa: um `.md` em `orquestracao-multi-ia/tasks/` (modelo em `tasks/exemplo-classificacao-produtos.md`).
2. No Claude Code: "processe a tarefa orquestracao-multi-ia/tasks/exemplo-classificacao-produtos.md" — o subagent **roteador** despacha para o worker e o **revisor-qa** valida e abre o PR.
3. Você revisa e aprova o PR. Ponto final humano preservado.

## Regras de custo embutidas

- System prompt sempre em arquivo e idêntico entre chamadas -> cache hit (input ~97% mais barato). Rodar jobs pesados durante o dia em Brasília (off-peak da DeepSeek = metade do preço; o pico deles cai ~22h–01h e 03h–07h no horário de Brasília).
- Trabalho mecânico (padronização, cálculo) nunca passa por IA — Python puro.
- O Claude só lê resumos/amostras dos outputs, nunca arquivos bulk inteiros.
- `deepseek_bulk.py` imprime custo estimado ao final e retoma jobs interrompidos sem reprocessar.
- Preços no topo de `deepseek_bulk.py` (usados só na estimativa impressa).
