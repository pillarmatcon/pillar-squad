# Método Viga Mestra

> Metodologia proprietária da Pillar. Aplicada a todo cliente e prospect de loja de material de construção (MatCon), que é o único nicho que a Pillar atende (ver `_shared/nichos.md`). Referenciada em `_shared/identidade-agencia.md` como a metodologia própria da agência.

## Os 5 pilares

### 1. Inteligência de Dados

- **Problema que resolve:** dinheiro preso em estoque parado e perda de venda por falta de produto.
- **Resultado que busca:** estoque que vira caixa rápido e compra baseada em demanda real.
- **Exemplos tangíveis de execução:**
  1. Análise da curva ABC do estoque
  2. Mapeamento do giro do estoque e margem
  3. Identificação de produtos "isca" para geração de fluxo de caixa

### 2. Domínio Territorial

- **Problema que resolve:** verba de anúncio jogada fora com quem está longe ou é só "curioso".
- **Resultado que busca:** ser a primeira opção (top of mind) num raio de entrega lucrativo.
- **Exemplos tangíveis de execução:**
  1. Otimização do perfil no Google para ser a primeira opção na vizinhança
  2. Anúncios geolocalizados blindando apenas o raio de entrega lucrativo
  3. Captura de buscas em alta por produtos

### 3. Combo de Produtos

- **Problema que resolve:** vender só o "grosso" (com margem baixa) e perder o acessório pro vizinho.
- **Resultado que busca:** aumento do ticket médio transformando produtos em soluções completas.
- **Exemplos tangíveis de execução:**
  1. Montagem de kits inteligentes por fase da obra (fundação ao acabamento)
  2. Checklists de venda adicional para o cliente não esquecer o acessório
  3. Estratégia de precificação isca para puxar o mix de alta margem

### 4. Vendedor de Elite

- **Problema que resolve:** atendimento lento, orçamentos "frios" e falta de acompanhamento (follow-up).
- **Resultado que busca:** padronizar o atendimento, acelerar o tempo de resposta e aumentar a taxa de conversão.
- **Exemplos tangíveis de execução:**
  1. Implementação de rotina de resposta ultrarrápida (máximo 15 minutos)
  2. Playbook de scripts persuasivos focado em fechamento de orçamentos
  3. Régua de follow-up sistematizada para não deixar o orçamento esfriar

### 5. Plano Obra Integral

- **Problema que resolve:** o cliente compra o cimento, mas faz o acabamento em outra loja.
- **Resultado que busca:** fidelizar o cliente em todas as etapas da obra (LTV máximo).
- **Exemplos tangíveis de execução:**
  1. Rastreamento da jornada do cliente da fundação até o acabamento
  2. Mecanismo de bônus/cashback para garantir a recompra do material fino
  3. Cronograma de ofertas preditivas conforme o avanço físico da obra

## Qual agente do squad executa cada pilar

| Pilar | Agente(s) que mais aplica | Por quê |
|---|---|---|
| 1. Inteligência de Dados | `@inteligencia-dados` | Lê relatório de ERP (Curva ABC, estoque) e produz diagnóstico de giro, margem, estoque parado e produtos isca. Resultado alimenta `@analista-dados` (KPI de dashboard), `@copywriter` (kits do Pilar 3) e `@webdesigner` (diagnóstico de proposta) |
| 2. Domínio Territorial | `@gestor-trafego` | Geolocalização, raio de entrega e otimização de perfil no Google são estrutura de campanha |
| 3. Combo de Produtos | `@copywriter` + `@gestor-trafego` | Kit e precificação isca viram oferta, ângulo de copy e criativo. Candidatos a kit vêm do diagnóstico do `@inteligencia-dados` |
| 4. Vendedor de Elite | `@copywriter` | Script de resposta ultrarrápida, playbook de fechamento de orçamento e régua de follow-up (ver "Playbook de vendedor" em `_squad/02-copywriter/SKILL.md`) |
| 5. Plano Obra Integral | `@analista-dados` + `@copywriter` | LTV e jornada viram KPI de retenção; cronograma de ofertas preditivas vira sequência de e-mail/WhatsApp |

## Onde este documento é usado

- **Proposta comercial** (`_squad/04-webdesigner/templates-html/proposta-comercial.html`): os placeholders `{{PILAR_1_NOME}}` a `{{PILAR_3_DESCRICAO}}` usam por padrão os 3 pilares mais relevantes para o diagnóstico daquele prospect específico, escolhidos entre os 5 acima. Se o usuário não indicar quais, o agente pergunta qual dos 5 pilares tem mais aderência ao caso antes de escolher sozinho.
- **Plano de tráfego, copy e dashboard** de qualquer cliente MatCon: os agentes consultam este arquivo para alinhar diagnóstico e ângulo de comunicação com a metodologia oficial da Pillar, em vez de reinventar enquadramento a cada cliente.

## Regra

Este método é específico da Pillar e do nicho MatCon. Não usar os 5 pilares como framework genérico para outros nichos caso a agência um dia atenda outro tipo de cliente. Nesse cenário, o método precisaria ser adaptado ou substituído, não aplicado por analogia.
