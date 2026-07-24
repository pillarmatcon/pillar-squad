# Workspace Pillar MatCon

Esta pasta é o **workspace permanente** de uma agência de marketing digital que usa o Squad da Pillar.

## Estrutura

- `_squad/` - arquivos de referência do squad (SKILLs, templates HTML, regras compartilhadas, **Humanizer**, **skill embutida de Meta Ads CLI em modo guiado total**, **identidade da própria agência** em `_squad/_shared/identidade-agencia.md`, **logo da Pillar** em `_squad/_shared/marca-pillar/`, **Método Viga Mestra** (metodologia proprietária, 5 pilares) em `_squad/_shared/metodo-viga-mestra.md`).
- `clientes/` - uma subpasta por cliente fechado. Cada cliente tem `CLIENTE.md`, `outputs/` e `historico/`.
- `propostas/` - uma subpasta por prospect (cliente em potencial, ainda não fechado). Identidade visual usada é sempre a da Pillar, nunca a do prospect. Ver `propostas/README.md`.
- `.claude/` - esta pasta. Instruções globais + 7 agentes registrados.

## Como invocar os agentes

Via `@nome` ou `/nome` em qualquer conversa neste workspace:

- `@orquestrador` - coordena todos os agentes em sequência
- `@gestor-trafego` - plano de tráfego pago (Meta, Google, TikTok). **Upgrade opcional via Meta Ads CLI: o agente executa o setup completo sozinho via Bash tool, usuário não toca no terminal. Funciona em Mac, Linux e Windows.**
- `@copywriter` - headlines, anúncios, e-mails, scripts, e playbook de atendimento/follow-up de orçamento (Pilar Vendedor de Elite)
- `@designer-criativos` - criativos HTML para Instagram, 1 foto real em Story (1080×1920) + Post (1080×1350)
- `@webdesigner` - landing pages HTML para clientes, e propostas comerciais HTML para prospects (`propostas/`)
- `@analista-dados` - dashboards e relatórios de performance de campanha
- `@inteligencia-dados` - lê relatório de ERP (Curva ABC, estoque, vendas por categoria) e produz diagnóstico de giro, margem, estoque parado e produtos isca (Pilar 1 do Método Viga Mestra)

## Workflow padrão

1. Leia `clientes/<nome>/CLIENTE.md`
2. Leia o SKILL.md em `_squad/<pasta>/SKILL.md`
3. Leia `_squad/_shared/nichos.md`, `briefing-template.md`, `regras-globais.md`
4. Para copywriter, designer-criativos e webdesigner: leia também `_squad/_shared/humanizer.md`
5. Para gestor-trafego em pedidos com conta real: detecte CLI (`meta --version`) e ofereça onboarding via `_squad/01-gestor-trafego/cli-onboarding.md` se necessário (modo guiado total)
6. Para analista-dados (rodapé `{{NOME_AGENCIA}}` do dashboard) ou qualquer material que carregue a identidade da própria agência (proposta comercial, material institucional): leia também `_squad/_shared/identidade-agencia.md` no lugar do `CLIENTE.md`. Isso nunca substitui a marca do cliente em LP, copy, anúncio ou criativo.
7. Para inteligencia-dados: exige pelo menos um relatório real de ERP (estoque, Curva ABC, vendas por categoria) anexado ou referenciado. Sem isso, para e pede a exportação.
8. Execute
9. Rode Humanizer nas saídas textuais
10. Salve em `clientes/<nome>/outputs/` (cliente fechado) ou `propostas/<nome-prospect>/` (prospect, ver item 6)
11. Proponha a linha de atualização do Histórico de `clientes/<nome>/CLIENTE.md` e peça confirmação antes de gravar (Regra 23 de `_squad/_shared/regras-globais.md`). Não se aplica a `propostas/`, que não tem CLIENTE.md

## Regras globais

- Nunca invente dados - pergunte ao usuário
- Sempre em português brasileiro
- Sem marketês, sem travessão (ver `_squad/_shared/regras-globais.md`)
- Sem cara de IA - aplicar `_squad/_shared/humanizer.md` antes de entrega textual
- Comandos write em conta real: confirmação textual explícita (Regra 22)
- Token nunca passa pelo chat - só via clipboard (Fase 3 do meta-ads-cli-setup)
- Compliance por nicho automático

## Skill embutida

`_squad/_skills/meta-ads-cli-setup/` - skill checkpointed em **modo guiado total**. O agente executa todos os comandos via Bash tool, usuário não toca no terminal. Suporta macOS, Linux e Windows (PowerShell). O `@gestor-trafego` invoca quando o aluno aceita o upgrade.

## Clientes ativos

- `clientes/construmais/` - Material de construção em João Pessoa/PB
- `clientes/_TEMPLATE/` - Template para criar novo cliente

## Propostas comerciais (prospects)

- `propostas/` - uma subpasta por prospect. Ver `propostas/README.md` para estrutura e workflow.
