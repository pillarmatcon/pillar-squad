# Workspace Pillar MatCon

Esta pasta é o **workspace permanente** de uma agência de marketing digital que usa o Squad da Pillar.

## Estrutura

- `.claude/` - esta pasta. Instruções globais (este arquivo) + 7 agentes registrados. Fica sempre na raiz de `Pillar/`: é daqui que o Claude Code carrega o CLAUDE.md e os agentes ao iniciar uma sessão na raiz do workspace. Mover essa pasta quebraria o carregamento automático.
- `_squad/` - arquivos de referência do squad (SKILLs, templates HTML, regras compartilhadas, **Humanizer**, **skill embutida de Meta Ads CLI em modo guiado total**, **identidade da própria agência** em `_squad/_shared/identidade-agencia.md`, **logo da Pillar** em `_squad/_shared/marca-pillar/`, **Método Viga Mestra** (metodologia proprietária, 5 pilares, racional completo) em `_squad/_shared/metodo-viga-mestra.md`, **template de tarefa reutilizável** em `_squad/_shared/template-tarefa.md`).

### `Operacional/` - execução com cliente já fechado

- `Operacional/Método Viga Mestra/` - biblioteca de playbooks genéricos da metodologia, organizada em `Pilar > Atividade > Tarefa` (ver `Operacional/Método Viga Mestra/_metodo.md`). Todo conteúdo aqui é template, com `[placeholders]` no lugar de dado de cliente. A versão real preenchida pra um cliente específico vai em `Operacional/clientes/<nome>/outputs/`, nunca aqui. Exceção: a tarefa `1 - Inteligência de Dados/1 - Curva ABC do Estoque/` guarda também uma ferramenta pronta (não-template), o script `pillar_padroniza_curva_abc.py` + `SKILL.md`, que converte PDF de Curva ABC do sistema Pontual Tecnologia em XLSX padronizado, zero IA na conversão.
- `Operacional/clientes/` - uma subpasta por cliente fechado. Cada cliente tem `CLIENTE.md`, `outputs/` e `historico/`.

### `Comercial/` - prospecção, cliente ainda não fechado

- `Comercial/propostas/` - uma subpasta por prospect (cliente em potencial, ainda não fechado). Identidade visual usada é sempre a da Pillar, nunca a do prospect. Ver `Comercial/propostas/README.md`.

## Como invocar os agentes

Via `@nome` ou `/nome` em qualquer conversa neste workspace:

- `@orquestrador` - coordena todos os agentes em sequência
- `@gestor-trafego` - plano de tráfego pago (Meta, Google, TikTok). **Upgrade opcional via Meta Ads CLI: o agente executa o setup completo sozinho via Bash tool, usuário não toca no terminal. Funciona em Mac, Linux e Windows.**
- `@copywriter` - headlines, anúncios, e-mails, scripts, e playbook de atendimento/follow-up de orçamento (Pilar Vendedor de Elite)
- `@designer-criativos` - criativos HTML para Instagram, 1 foto real em Story (1080×1920) + Post (1080×1350)
- `@webdesigner` - landing pages HTML para clientes, e propostas comerciais HTML para prospects (`Comercial/propostas/`)
- `@analista-dados` - dashboards e relatórios de performance de campanha
- `@inteligencia-dados` - lê relatório de ERP (Curva ABC, estoque, vendas por categoria) e produz diagnóstico de giro, margem, estoque parado e produtos isca (Pilar 1 do Método Viga Mestra)

## Workflow padrão

1. Leia `Operacional/clientes/<nome>/CLIENTE.md`
2. Leia o SKILL.md em `_squad/<pasta>/SKILL.md`
3. Leia `_squad/_shared/nichos.md`, `briefing-template.md`, `regras-globais.md`
4. Para copywriter, designer-criativos e webdesigner: leia também `_squad/_shared/humanizer.md`
5. Para gestor-trafego em pedidos com conta real: detecte CLI (`meta --version`) e ofereça onboarding via `_squad/01-gestor-trafego/cli-onboarding.md` se necessário (modo guiado total)
6. Para analista-dados (rodapé `{{NOME_AGENCIA}}` do dashboard) ou qualquer material que carregue a identidade da própria agência (proposta comercial, material institucional): leia também `_squad/_shared/identidade-agencia.md` no lugar do `CLIENTE.md`. Isso nunca substitui a marca do cliente em LP, copy, anúncio ou criativo.
7. Para inteligencia-dados: exige pelo menos um relatório real de ERP (estoque, Curva ABC, vendas por categoria) anexado ou referenciado. Sem isso, para e pede a exportação. Se a fonte for PDF de Curva ABC do sistema Pontual Tecnologia, roda antes a ferramenta em `Operacional/Método Viga Mestra/1 - Inteligência de Dados/1 - Curva ABC do Estoque/SKILL.md` (converte pra XLSX padronizado, script determinístico, sem gasto de IA na conversão em si).
8. Execute
9. Rode Humanizer nas saídas textuais
10. Salve em `Operacional/clientes/<nome>/outputs/` (cliente fechado) ou `Comercial/propostas/<nome-prospect>/` (prospect, ver item 6). Exceção: `@inteligencia-dados` salva em `outputs/<Pilar>/<Atividade>/`, espelhando a estrutura de `Operacional/Método Viga Mestra/`: planilhas por período dentro de subpastas `<MM-YYYY>` (mês de execução), e um único `diagnostico-estoque.md` cumulativo na raiz da atividade, que cresce por período em vez de ser sobrescrito (ver "Formato de output" em `_squad/06-inteligencia-dados/SKILL.md`)
11. Proponha a linha de atualização do Histórico de `Operacional/clientes/<nome>/CLIENTE.md` e peça confirmação antes de gravar (Regra 21 de `_squad/_shared/regras-globais.md`). Não se aplica a `Comercial/propostas/`, que não tem CLIENTE.md

## Regras globais

- Nunca invente dados - pergunte ao usuário
- Sempre em português brasileiro
- Sem marketês, sem travessão (ver `_squad/_shared/regras-globais.md`)
- Sem cara de IA - aplicar `_squad/_shared/humanizer.md` antes de entrega textual
- Comandos write em conta real: confirmação textual explícita (Regra 20)
- Token nunca passa pelo chat - só via clipboard (Fase 3 do meta-ads-cli-setup)
- Compliance por nicho automático

## Skills embutidas

- `_squad/_skills/meta-ads-cli-setup/` - skill checkpointed em **modo guiado total**. O agente executa todos os comandos via Bash tool, usuário não toca no terminal. Suporta macOS, Linux e Windows (PowerShell). O `@gestor-trafego` invoca quando o aluno aceita o upgrade.
- `Operacional/Método Viga Mestra/1 - Inteligência de Dados/1 - Curva ABC do Estoque/SKILL.md` - converte PDF de Curva ABC (sistema Pontual Tecnologia) em XLSX padronizado via script Python determinístico (regex/posição de coluna + pandas, zero chamada de IA na conversão). O `@inteligencia-dados` invoca automaticamente antes do diagnóstico quando a fonte é esse tipo de PDF. Fica junto da tarefa correspondente do Método Viga Mestra em vez de `_squad/_skills/`, porque é a ferramenta operacional dessa tarefa específica, não um setup genérico de conta.

## Clientes ativos

- `Operacional/clientes/construmais/` - Material de construção em João Pessoa/PB
- `Operacional/clientes/_TEMPLATE/` - Template para criar novo cliente

## Propostas comerciais (prospects)

- `Comercial/propostas/` - uma subpasta por prospect. Ver `Comercial/propostas/README.md` para estrutura e workflow.
