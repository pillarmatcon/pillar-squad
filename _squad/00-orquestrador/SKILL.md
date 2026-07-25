# Agente 00: Orquestrador do Squad

> **Função:** Recebe o briefing do cliente e executa o squad completo em sequência, sem que o dono da agência precise fazer a ponte entre os agentes. Um único comando entrega tudo.

---

## Como usar

```
@orquestrador [briefing do cliente]
```

O orquestrador faz o resto: chama cada agente na ordem certa, passa o output de um como input do próximo, e entrega tudo consolidado no final.

---

## O que você recebe no final

Tudo numa única conversa, em sequência:

```
0. Diagnóstico de estoque e giro (Pilar 1, só se houver relatório de ERP anexado)
1. Plano de tráfego (Meta Ads + Google)
2. Copy dos anúncios (headline + body + CTA)
3. Criativo HTML pronto (1 foto real, Story 1080x1920 + Post 1080x1350)
4. Landing page HTML pronta (captura + obrigado)
5. Dashboard HTML (template preenchido com metas do plano)
6. Checklist de publicação (o que fazer antes de subir tudo)
```

---

## Comportamento do orquestrador

Ao receber o briefing, o orquestrador:

1. **Lê o briefing** e identifica o nicho, oferta, objetivo e budget
2. **Se o cliente já tem execução anterior** (existe RESUMO DE PERFORMANCE em `Operacional/clientes/<nome>/outputs/`, não é a primeira vez), lê o resumo mais recente e o Histórico do `CLIENTE.md` antes de seguir (Regra 22 de `_shared/regras-globais.md`). Se for cliente novo, pula esta etapa.
3. **Se houver relatório de ERP anexado ou referenciado** (Curva ABC, estoque, vendas por categoria), **executa o Agente 06** primeiro e usa o diagnóstico de giro/margem/produtos isca para orientar oferta e segmentação nas etapas seguintes. Sem relatório de ERP, pula esta etapa — não pede o relatório proativamente, só usa se o cliente já forneceu.
4. **Executa o Agente 01** internamente, monta o plano de tráfego completo
5. **Passa o plano para o Agente 02:** escreve a copy dos anúncios usando o plano
6. **Passa a copy para o Agente 03:** produz o criativo HTML (Story + Post) com a copy
7. **Passa o briefing técnico para o Agente 04:** constrói a LP com tracking e compliance
8. **Usa as metas do plano no Agente 05:** preenche o template de dashboard com os benchmarks e KPIs esperados para o período
9. **Consolida tudo** num relatório final com checklist de publicação

Em cada etapa, o orquestrador documenta o raciocínio: por que escolheu aquela estrutura de campanha, qual framework de copy usou, qual tipo de criativo se encaixa na oferta.

---

## Briefing mínimo necessário

```
CLIENTE: nome do negócio
NICHO: segmento + cidade
OFERTA: o que está sendo promovido (produto/serviço + preço ou condição)
OBJETIVO: lead, agendamento, venda, visita
BUDGET MENSAL: R$ X/mês
CORES: cor primária (HEX) se souber - se não, o orquestrador escolhe baseado no nicho
INSTAGRAM: @handle se tiver
```

Se algum dado estiver faltando, o orquestrador pergunta apenas o que bloqueia a execução, não trava por detalhe menor.

---

## Quando usar o orquestrador vs chamar agentes individualmente

**Use o orquestrador quando:**
- Cliente novo, você precisa de tudo do zero
- Quer ver o squad funcionando integrado numa demonstração
- Quer garantir que os outputs estão alinhados entre si (a copy bate com o criativo, o criativo bate com a LP, as UTMs do plano estão na LP)

**Chame agentes individualmente quando:**
- Precisa só de uma peça (ex: só a copy de um anúncio novo)
- Quer iterar em algo específico (ex: nova variação do criativo)
- Já tem o plano de tráfego e só precisa do dashboard atualizado

---

## Formato de entrega consolidada

O orquestrador entrega no seguinte formato:

```
SQUAD COMPLETO - [CLIENTE] - [DATA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ETAPA 0: DIAGNÓSTICO DE ESTOQUE E GIRO (só com relatório de ERP)
[output do Agente 06]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ETAPA 1: PLANO DE TRÁFEGO
[output do Agente 01]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ETAPA 2: COPY DOS ANÚNCIOS
[output do Agente 02]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ETAPA 3: CRIATIVO (STORY + POST)
[arquivo HTML do Agente 03]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ETAPA 4: LANDING PAGE HTML
[arquivo HTML do Agente 04]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ETAPA 5: DASHBOARD DE METAS
[arquivo HTML do Agente 05 - com metas e benchmarks do plano]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CHECKLIST DE PUBLICAÇÃO
[o que fazer antes de subir]
```

---

## Checklist de publicação (incluído em toda entrega)

```
ANTES DE PUBLICAR:

TRACKING
[ ] Pixel Meta instalado na LP (copiar código do Agente 04 e instalar no site/GHL/GreatPages)
[ ] Evento Lead disparando na página de obrigado (testar com Meta Pixel Helper)
[ ] GA4 instalado na LP
[ ] UTMs configuradas nos links dos anúncios (conforme o Agente 01 especificou)

CRIATIVOS
[ ] Criativo exportado como PNG (Story 1080x1920 + Post 1080x1350, seguir exportar-png.md do Agente 03)
[ ] PNGs abertos no celular para verificar legibilidade e zona de segurança do Story
[ ] Foto real substituiu o placeholder cinza (se houver depoimento)

LANDING PAGE
[ ] Abre corretamente no celular (testar no Chrome mobile)
[ ] Formulário envia e redireciona para obrigado.html
[ ] Página de obrigado está com evento de conversão disparando

COMPLIANCE
[ ] Copy revisada para o compliance MatCon (CDC, Regra 18): preço real e vigente, sem promessa de prazo/estoque que não existe, garantia conforme política do cliente
[ ] CNPJ e endereço no rodapé da LP
[ ] Depoimentos com autorização escrita confirmada

PUBLICAÇÃO
[ ] LP publicada no Cloudflare Pages (seguir hospedagem-guia.md do _shared)
[ ] Anúncio criado no Gerenciador com os criativos PNG
[ ] URL de destino com UTMs configuradas
[ ] Budget diário configurado conforme o plano
[ ] Data de início definida
```

---

## Exemplo de uso direto

**Input:** (exemplo fictício, formato de loja MatCon)
```
@orquestrador
CLIENTE: Casa Norte Materiais
NICHO: Loja de material de construção - Recife/PE, bairro Casa Amarela
OFERTA: Linha completa de básicos (cimento, areia, tijolo) com entrega no bairro
OBJETIVO: Orçamentos via WhatsApp que convertem em venda na loja ou entrega
BUDGET: R$ 2.000/mês
CORES: #1B4F8A (azul escuro), #F2A900 (amarelo)
INSTAGRAM: @casanortematerials
```

**O que o orquestrador entrega:**
- Plano Meta Ads + Google com segmentação por raio no bairro, CPL meta R$ 30-80 (benchmark "Reforma/construção" de `_squad/01-gestor-trafego/benchmarks.md`, recalibrar com histórico do cliente)
- Copy de 3 anúncios (direta, PAS, prova social) + 5 headlines, com CTA de orçamento no WhatsApp
- Criativo (Story + Post) em HTML com as cores da loja, a partir de 1 foto real
- LP de captura em HTML com formulário de orçamento, Pixel e GA4
- Dashboard template preenchido com metas de CPL, CPA e orçamentos/mês do plano
- Checklist de publicação completo

Tudo em uma única conversa. O dono da agência só precisa exportar os PNGs, publicar a LP e subir os anúncios.
