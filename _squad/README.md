# Squad Pillar MatCon: Agentes para Operação da Agência

> **O que é:** Squad completo de 7 agentes, 1 orquestrador + 6 especialistas, que cobrem as funções operacionais centrais da Pillar no atendimento a clientes de material de construção (MatCon).
> **Para que serve:** Uso real no dia a dia da Pillar com clientes próprios.
> **Onde roda:** Claude Desktop (modo Chat ou modo Code).

---

## Como funciona

Você dá um único briefing ao `@orquestrador`. Ele executa os agentes especialistas em sequência e entrega tudo em uma conversa só:

```
@orquestrador [briefing do cliente]

→ Agente 06 lê relatório de ERP e produz diagnóstico de estoque/giro (só se houver relatório anexado)
→ Agente 01 produz plano de tráfego
→ Agente 02 usa o plano para escrever copy
→ Agente 03 usa a copy para gerar o criativo (Story + Post) HTML
→ Agente 04 usa briefing + copy para construir a LP HTML
→ Agente 05 usa as metas do plano para preencher o dashboard
→ Orquestrador consolida tudo + entrega checklist de publicação
```

Também é possível chamar cada agente individualmente para tarefas pontuais.

---

## Os 7 agentes

| # | Agente | Função | Saída típica |
|---|--------|--------|--------------|
| 00 | **Orquestrador** | Recebe o briefing e executa os agentes especialistas em sequência | Squad completo entregue numa única conversa |
| 01 | **Tráfego** | Estrutura campanha Meta + Google, audita contas, define budget e UTMs | Plano de campanha + benchmarks + UTMs + cronograma |
| 02 | **Copy** | Escreve anúncios, headlines, emails, scripts, sequências de follow-up e playbook de atendimento/orçamento | 10 headlines + 3 anúncios (direta/PAS/prova) + email + script + playbook de vendedor |
| 03 | **Design/Criativos** | Gera criativo HTML a partir de 1 foto real, em Story (1080×1920) + Post (1080×1350), nas cores do cliente | Criativo HTML exportável para PNG |
| 04 | **Páginas** | Cria landing page HTML completa, captura, vendas, obrigado, agendamento, e proposta comercial para prospect | LP responsiva com Pixel, GA4, SEO, Open Graph, ou proposta HTML com a marca da Pillar |
| 05 | **Relatório/Dashboard** | Gera relatório semanal e dashboard HTML com KPIs visuais de campanha | Dashboard HTML com análise + próximas ações + ROI |
| 06 | **Inteligência de Dados** | Lê relatório de ERP (Curva ABC, estoque, vendas) e produz diagnóstico de giro, margem, estoque parado e produtos isca | Diagnóstico estruturado, insumo para copy (kits), dashboard (KPI de estoque) e proposta |

---

## Estrutura de pastas

```
_squad/
├── README.md                              ← este arquivo
│
├── 00-orquestrador/
│   ├── SKILL.md                           ← instruções do orquestrador
│   └── briefing-orquestrador.md           ← template de briefing (completo + express)
│
├── _shared/                               ← fundação consultada por TODOS os agentes
│   ├── nichos.md                          ← perfil MatCon + framework de fallback para nicho novo
│   ├── briefing-template.md               ← template de briefing do cliente
│   ├── regras-globais.md                  ← regras de copy, execução, anti-IA, compliance
│   ├── identidade-agencia.md              ← kit de marca da própria Pillar
│   ├── metodo-viga-mestra.md              ← metodologia proprietária, 5 pilares
│   ├── humanizer.md                       ← protocolo anti-cara-de-IA no texto
│   ├── hospedagem-guia.md                 ← como hospedar LP no Cloudflare Pages (gratuito)
│   └── marca-pillar/                      ← logo e ativos visuais da Pillar
│
├── 01-gestor-trafego/
│   ├── SKILL.md                           ← instruções completas do agente
│   ├── cli-onboarding.md                  ← oferta de upgrade para Meta Ads CLI
│   ├── estruturas-de-campanha.md          ← estruturas prontas com nomeação padrão
│   ├── diagnostico-de-conta.md            ← funil de diagnóstico sequencial
│   └── benchmarks.md                      ← CPL/CPA/ROAS de referência (foco MatCon) + fórmulas
│
├── 02-copywriter/
│   ├── SKILL.md
│   ├── frameworks.md                      ← AIDA, PAS, PROTTO, 4Ps + quando usar cada
│   └── biblioteca-headlines.md            ← headlines testadas por objetivo, ângulos MatCon
│
├── 03-designer-criativos/
│   ├── SKILL.md
│   ├── templates-html/
│   │   ├── educativo.html                 ← template de insight educativo (Story + Post)
│   │   ├── oferta.html                    ← template de promoção/oferta (Story + Post)
│   │   └── prova.html                     ← template de prova social / resultado (Story + Post)
│   └── exportar-png.md                    ← como gerar PNG via Chrome DevTools (sem instalar nada)
│
├── 04-webdesigner/
│   ├── SKILL.md
│   ├── estrutura-lp.md                    ← seções obrigatórias e ordem
│   └── templates-html/
│       ├── captura.html                   ← LP de captura de leads
│       ├── vendas.html                    ← LP de vendas
│       ├── obrigado.html                  ← página pós-conversão
│       └── proposta-comercial.html        ← proposta HTML com a marca da Pillar, para prospect
│
├── 05-analista-dados/
│   ├── SKILL.md
│   ├── kpis-por-nicho.md                  ← KPIs primários e secundários (foco varejo/MatCon)
│   └── template-dashboard.html            ← base com KPI cards + tabela de criativos + análise
│
├── 06-inteligencia-dados/
│   └── SKILL.md                           ← lê ERP (Curva ABC, estoque), Pilar 1 do Método Viga Mestra
│
└── _skills/
    └── meta-ads-cli-setup/                ← setup guiado da Meta Ads CLI (opcional, modo guiado total)
```

---

## Como usar

### Opção 1: Modo Code (recomendado, é como este workspace roda)

1. Abrir a pasta do workspace no Claude Code
2. O `.claude/CLAUDE.md` define o comportamento base
3. Cada `SKILL.md` vira um agente disponível via `@nome-do-agente`
4. Os outputs (HTML de LP, dashboard, criativo) são salvos diretamente na máquina
5. Testar com: `@orquestrador CLIENTE: [nome] NICHO: material de construção - [cidade] OFERTA: [o que é] OBJETIVO: [lead/agendamento/venda] BUDGET: R$ X/mês`

### Opção 2: Agente individual (para tarefas pontuais)

- Só precisa de copy nova? Chame `@copywriter`
- Só precisa de nova variação do criativo? Chame `@designer-criativos`
- Já tem plano de tráfego e só quer atualizar o dashboard? Chame `@analista-dados`
- Recebeu relatório de estoque/Curva ABC do cliente? Chame `@inteligencia-dados`

---

## Filosofia do squad

1. **Focado em MatCon.** A Pillar atende hoje só loja de material de construção. `_shared/nichos.md` traz o perfil completo desse nicho como padrão, com um framework de fallback (6 dimensões + 5 perguntas) só para o dia em que aparecer um cliente fora dele.
2. **Autocontido.** Cada agente roda sem depender de plugins ou integrações externas. Os arquivos da pasta são tudo que ele precisa.
3. **Briefing antes de execução.** Nenhum agente produz nada sem briefing mínimo. Sem chute, sem invenção.
4. **Output orientado a uso real.** Toda saída indica claramente o que é v1 vs pronto para publicar, e o que falta validar com o cliente.
5. **Compliance embutido.** O compliance padrão hoje é o do CDC (nicho MatCon, ver `_shared/regras-globais.md`). Se a Pillar atender fora do nicho um dia, a regulamentação daquele setor precisa ser mapeada antes de publicar.
