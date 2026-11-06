# Nó de follow-up da Suri (Construmais): notas de configuração

**Pedido:** prompt para o nó de follow-up, acionado quando o cliente para de responder no começo, no meio ou no fim da conversa (06/11/2026).
**Pilar:** 4, Vendedor de Elite (Atividade 4.3, Régua de Follow-up).
**Prompt para colar na Suri:** `outputs/11-2026/Arquivos/06-vendedor-de-elite-prompt-no-followup-suri.txt`
**Status:** v1, sem teste na plataforma. Este README é interno, não vai para a Suri.

## Como o prompt funciona

1. Decide se deve escrever. Em seis situações responde `NAO_ENVIAR` (cliente recusou, está irritado, já está com vendedor humano, a bola está com a loja, 3 tentativas esgotadas, despedida natural).
2. Classifica a fase em que a conversa parou: início, meio ou fim.
3. Escolhe um objetivo por tentativa (retomar, facilitar, encerrar) e escreve uma mensagem única de até 280 caracteres.
4. Tentativa 3 é sempre a despedida, sem pergunta. Depois dela o nó não roda de novo na mesma conversa.

As regras de limite seguem o arquivo 11 da base de conhecimento (sem preço, estoque, prazo, frete, pagamento ou desconto) e o compliance do `CLIENTE.md` (sem urgência falsa, sem frete grátis).

## O que configurar fora do prompt, na Suri

- **Gatilho e intervalo.** Proposta de partida: tentativa 1 após cerca de 2 horas úteis, tentativa 2 no dia seguinte, tentativa 3 no terceiro dia. A régua padrão do método (D1, D3, D7, D15) foi pensada para orçamento enviado por vendedor. Este nó é do assistente, com conversa mais curta, então 3 tentativas bastam. Ajustar depois de ver a taxa de resposta por etapa.
- **Só em horário de funcionamento.** Seg a sex 7h30 às 17h30, sábado 7h30 às 16h, domingo fechado. Follow-up às 22h ou no domingo tende a irritar e a reduzir resposta.
- **Janela de 24 horas do WhatsApp.** Se o número do assistente estiver na API oficial, mensagem livre só vale até 24h após a última mensagem do cliente. Tentativas fora dessa janela exigem template aprovado pela Meta. Hoje o número oficial é (83) 9 8855-5601 e o de teste com IA é (83) 9 9847-1242. Precisa confirmar em qual número o assistente roda e se a Suri troca para template sozinha.
- **Transbordo.** Desligar o nó quando o atendimento passa para humano, ou garantir que `{{transbordo_feito}}` chegue preenchido. Sem isso o assistente e o vendedor cobram o cliente ao mesmo tempo.
- **Variáveis.** Os nomes em `{{chaves}}` são genéricos. Trocar pelos reais da Suri. Se alguma não existir, o prompt funciona sem ela, mas perde precisão (a mais importante é `numero_tentativa`).
- **Tratamento do `NAO_ENVIAR`.** Conferir se a Suri não manda essa palavra ao cliente. Se mandar, trocar por um campo de saída vazio ou por uma condição antes do envio.
- **Pausa se o cliente responder.** Qualquer resposta do cliente cancela as tentativas pendentes e devolve a conversa ao fluxo normal.

## Pendências

1. Tony não confirmou formas de pagamento, frete e prazo. Por isso nenhum follow-up usa esses temas como gancho.
2. Fora do horário, o prompt evita prometer retorno. Se o Tony definir uma regra (ex.: retorno em até X minutos no horário comercial), incluir no prompt.
3. Medir após 2 semanas: taxa de resposta por tentativa e fase, e quantas conversas voltaram a virar orçamento. Com esses números dá para calibrar intervalos e texto.
