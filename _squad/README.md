# Squad AgêncIA 100k: Agentes para Operação de Agência

> **O que é:** Squad completo de 6 agentes especialistas, 1 orquestrador + 5 executores, que cobrem todas as funções operacionais centrais de uma agência de marketing digital, para qualquer nicho.
> **Para que serve:** Demonstração ao vivo na Aula 4 do evento AgêncIA 100k e entrega real para os alunos usarem com clientes próprios.
> **Onde roda:** Claude Desktop (modo Chat ou modo Code).

---

## Como funciona

O dono da agência dá um único briefing ao `@orquestrador`. Ele executa os 5 agentes em sequência e entrega tudo em uma conversa só:

```
@orquestrador [briefing do cliente]

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
| 00 | **Orquestrador** | Recebe o briefing e executa os 5 agentes em sequência | Squad completo entregue numa única conversa |
| 01 | **Tráfego** | Estrutura campanha Meta + Google, audita contas, define budget e UTMs | Plano de campanha + benchmarks + UTMs + cronograma |
| 02 | **Copy** | Escreve anúncios, headlines, emails, scripts, sequências de follow-up e playbook de atendimento/orçamento | 10 headlines + 3 anúncios (direta/PAS/prova) + email + script + playbook de vendedor |
| 03 | **Design/Criativos** | Gera criativo HTML a partir de 1 foto real, em Story (1080×1920) + Post (1080×1350), nas cores do cliente | Criativo HTML exportável para PNG |
| 04 | **Páginas** | Cria landing page HTML completa, captura, vendas, obrigado, agendamento, e proposta comercial para prospect | LP responsiva com Pixel, GA4, SEO, Open Graph, ou proposta HTML com a marca da Pillar |
| 05 | **Relatório/Dashboard** | Gera relatório semanal e dashboard HTML com KPIs visuais de campanha | Dashboard HTML com análise + próximas ações + ROI |
| 06 | **Inteligência de Dados** | Lê relatório de ERP (Curva ABC, estoque, vendas) e produz diagnóstico de giro, margem, estoque parado e produtos isca | Diagnóstico estruturado, insumo para copy (kits), dashboard (KPI de estoque) e proposta |

---

## Estrutura de pastas

```
AGENTES/
├── README.md                              ← este arquivo
│
├── 00-orquestrador/
│   ├── SKILL.md                           ← instruções do orquestrador
│   ├── briefing-orquestrador.md           ← template de briefing (completo + express)
│   └── mindmap-squad.html                 ← visualização do fluxo do squad
│
├── _shared/                               ← fundação consultada por TODOS os agentes
│   ├── nichos.md                          ← framework de mapeamento universal de nicho
│   ├── briefing-template.md               ← template de briefing do cliente
│   ├── regras-globais.md                  ← regras de copy, execução, anti-IA, compliance
│   └── hospedagem-guia.md                 ← como hospedar LP no Cloudflare Pages (gratuito)
│
├── 01-gestor-trafego/
│   ├── SKILL.md                           ← instruções completas do agente
│   ├── estruturas-de-campanha.md          ← 7 estruturas prontas com nomeação padrão
│   ├── diagnostico-de-conta.md            ← funil de diagnóstico sequencial
│   ├── benchmarks.md                      ← CPL/CPA/ROAS por 9 nichos + fórmulas
│   └── exemplo-demo.md                    ← Clínica Vital completo (Meta + Google)
│
├── 02-copywriter/
│   ├── SKILL.md
│   ├── frameworks.md                      ← AIDA, PAS, PROTTO, 4Ps + quando usar cada
│   ├── biblioteca-headlines.md            ← headlines testadas por objetivo
│   └── exemplo-demo.md
│
├── 03-designer-criativos/
│   ├── SKILL.md
│   ├── templates-html/
│   │   ├── educativo.html                 ← template de insight educativo (Story + Post)
│   │   ├── oferta.html                    ← template de promoção/oferta (Story + Post)
│   │   └── prova.html                     ← template de prova social / resultado (Story + Post)
│   ├── exportar-png.md                    ← como gerar PNG via Chrome DevTools (sem instalar nada)
│   └── exemplo-demo.md
│
├── 04-webdesigner/
│   ├── SKILL.md
│   ├── estrutura-lp.md                    ← seções obrigatórias e ordem
│   ├── templates-html/
│   │   ├── captura.html                   ← LP de captura de leads
│   │   ├── vendas.html                    ← LP de vendas
│   │   └── obrigado.html                  ← página pós-conversão
│   └── exemplo-demo.md
│
├── 05-analista-dados/
│   ├── SKILL.md
│   ├── kpis-por-nicho.md                  ← KPIs primários e secundários por negócio
│   ├── template-dashboard.html            ← base com KPI cards + tabela de criativos + análise
│   └── exemplo-demo.md                    ← Clínica Vital semana 1 (CPL R$23,73, ROI 928%)
│
└── 06-inteligencia-dados/
    └── SKILL.md                            ← lê ERP (Curva ABC, estoque), Pilar 1 do Método Viga Mestra
```

---

## Como usar

### Opção 1: Modo Code (recomendado, é como este workspace roda)

1. Abrir a pasta do workspace no Claude Code
2. O `.claude/CLAUDE.md` define o comportamento base
3. Cada `SKILL.md` vira um agente disponível via `@nome-do-agente`
4. Os outputs (HTML de LP, dashboard, criativo) são salvos diretamente na máquina
5. Testar com: `@orquestrador CLIENTE: [nome] NICHO: [segmento] - [cidade] OFERTA: [o que é] OBJETIVO: [lead/agendamento/venda] BUDGET: R$ X/mês`

### Opção 2: Agente individual (para tarefas pontuais)

- Só precisa de copy nova? Chame `@copy`
- Só precisa de nova variação do criativo? Chame `@designer-criativos`
- Já tem plano de tráfego e só quer atualizar o dashboard? Chame `@analista-dados`

---

## Roteiro da Aula 4: Demo ao vivo

**Tempo total:** 12 a 15 minutos (demonstração completa com orquestrador)

1. **Apresentar o caso** (2 min): Clínica Vital ou cliente do aluno. Mostrar o briefing express na tela, 7 campos, 1 minuto para preencher.
2. **Invocar o orquestrador** (1 min): colar `@orquestrador [briefing]`. Claude começa a executar.
3. **Acompanhar o Agente 01** (2 min): mostrar o plano de tráfego saindo com CPL máximo calculado, estrutura de campanha, UTMs.
4. **Acompanhar o Agente 02** (2 min): mostrar as headlines + anúncios usando os ângulos do plano.
5. **Acompanhar o Agente 03** (2 min): criativo HTML gerado (Story + Post). Explicar como exportar para PNG.
6. **Acompanhar o Agente 04** (2 min): LP HTML pronta. Abrir no browser. Mostrar Pixel + formulário.
7. **Acompanhar o Agente 05** (2 min): dashboard preenchido com as metas do plano. Abrir no browser. Mostrar como salvar em PDF.
8. **Fechar o ciclo** (1 min): "Isso é o trabalho de uma semana inteira de uma equipe. Você fez em uma conversa."

---

## Filosofia do squad

1. **Multinicho por design.** Não há "agente para clínica" nem "agente para restaurante". O `_shared/nichos.md` mapeia qualquer cliente em 5 perguntas.
2. **Autocontido.** Cada agente roda sem depender de plugins ou integrações externas. Os arquivos da pasta são tudo que ele precisa.
3. **Briefing antes de execução.** Nenhum agente produz nada sem briefing mínimo. Sem chute, sem invenção.
4. **Output orientado a uso real.** Toda saída indica claramente o que é v1 vs pronto para publicar, e o que falta validar com o cliente.
5. **Compliance embutido.** Saúde não promete resultado clínico, advogado não capta ativamente, financeiro não promete retorno. O squad bloqueia automaticamente por nicho.

---

## Status do projeto

| Componente | Status |
|---|---|
| `_shared/` (4 arquivos) | Pronto |
| Agente 00-Orquestrador | Pronto |
| Agente 01-Tráfego (5 arquivos) | Pronto |
| Agente 02-Copy (4 arquivos) | Pronto |
| Agente 03-Design/Criativos (6 arquivos) | Pronto |
| Agente 04-Páginas (6 arquivos) | Pronto |
| Agente 05-Relatório/Dashboard (4 arquivos) | Pronto |
| `mindmap-squad.html` | Pronto |

**Total: 30 arquivos entregues.** Squad completo, pronto para ensinar na Aula 4.
