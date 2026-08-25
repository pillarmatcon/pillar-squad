# Workspace Pillar MatCon

Esta pasta é o **workspace permanente** de uma agência de marketing digital que usa o Squad da Pillar.

## Estrutura

- `.claude/` - esta pasta. Instruções globais (este arquivo) + 7 agentes registrados. Fica sempre na raiz de `Pillar/`: é daqui que o Claude Code carrega o CLAUDE.md e os agentes ao iniciar uma sessão na raiz do workspace. Mover essa pasta quebraria o carregamento automático.
- `orquestracao-multi-ia/` - infraestrutura dos workers externos (DeepSeek ativo; OpenAI e Gemini pausados por custo) usados pelos subagents `roteador`/`revisor-qa` pra trabalho pesado em massa. Não é conteúdo do squad nem entrega de cliente. Ver `orquestracao-multi-ia/README.md`.
- `_squad/` - arquivos de referência do squad (SKILLs, templates HTML, regras compartilhadas, **Humanizer**, **skill embutida de Meta Ads CLI em modo guiado total**, **identidade da própria agência** em `_squad/_shared/identidade-agencia.md`, **logo da Pillar** em `_squad/_shared/marca-pillar/`, **Método Viga Mestra** (metodologia proprietária, 5 pilares, racional completo) em `_squad/_shared/metodo-viga-mestra.md`, **template de tarefa reutilizável** em `_squad/_shared/template-tarefa.md`).

### `Operacional/` - execução com cliente já fechado

- `Operacional/Método Viga Mestra/` - biblioteca de playbooks genéricos da metodologia, tudo em um único arquivo `_metodo.md` (os 5 pilares, cada atividade e as tarefas já documentadas). Todo conteúdo aqui é template, com `[placeholders]` no lugar de dado de cliente. A versão real preenchida pra um cliente específico vai em `Operacional/clientes/<nome>/outputs/`, nunca aqui. Exceção: `Ferramenta Curva ABC/` guarda uma ferramenta pronta (não-template, não é playbook), o script `pillar_padroniza_curva_abc.py` + `SKILL.md`, que converte PDF de Curva ABC do sistema Pontual Tecnologia em XLSX padronizado, zero IA na conversão.
- `Operacional/clientes/` - uma subpasta por cliente fechado. Cada cliente tem `CLIENTE.md`, `outputs/` e `historico/`.

### `Comercial/` - prospecção, cliente ainda não fechado

- `Comercial/propostas/` - uma subpasta por prospect (cliente em potencial, ainda não fechado). Identidade visual usada é sempre a da Pillar, nunca a do prospect. Ver `Comercial/propostas/README.md`.
- `Comercial/site-pillar/` - site institucional da própria Pillar (HTML/CSS/JS). Não é proposta de prospect: usa a identidade de `_squad/_shared/identidade-agencia.md`.
- `Comercial/materiais-prospeccao/` - criativos de aquisição de cliente da própria Pillar (não ligados a um prospect específico), produzidos pelo agente `designer`.

## Como invocar os agentes

Não existe sintaxe `@nome` ou `/nome` no Claude Code (isso não é um mecanismo real da ferramenta). Para acionar um agente específico, basta nomeá-lo no pedido em linguagem natural, por exemplo "peça ao gestor-trafego para montar um plano de tráfego pra Construmais". Isso aciona só aquele agente diretamente, sem passar pelo orquestrador.

Use o orquestrador apenas quando o pedido envolver vários agentes em sequência (ex: onboarding completo de um cliente novo, cobrindo vários pilares do método de uma vez). Para pedir uma tarefa isolada de um único especialista, chame-o direto pelo nome.

- `orquestrador` - coordena todos os agentes em sequência
- `gestor-trafego` - plano de tráfego pago (Meta, Google, TikTok). **Upgrade opcional via Meta Ads CLI: o agente executa o setup completo sozinho via Bash tool, usuário não toca no terminal. Funciona em Mac, Linux e Windows.**
- `copywriter` - headlines, anúncios, e-mails, scripts, e playbook de atendimento/follow-up de orçamento (Pilar Vendedor de Elite)
- `webdesigner` - landing pages HTML para clientes, e propostas comerciais HTML para prospects (`Comercial/propostas/`)
- `analista-dados` - dashboards e relatórios de performance de campanha
- `inteligencia-dados` - lê relatório de ERP (Curva ABC, estoque, vendas por categoria) e produz diagnóstico de giro, margem, estoque parado e produtos isca (Pilar 1 do Método Viga Mestra)
- `designer` - criativo de aquisição de cliente da própria Pillar (Story + Post), captando dono de loja de MatCon como lead da agência. Identidade Pillar e público fixos no template; headline e bullets sempre vêm do `copywriter`. Não atende cliente final.

## Workflow padrão

1. Leia `Operacional/clientes/<nome>/CLIENTE.md`
2. Leia o SKILL.md em `_squad/<pasta>/SKILL.md`
3. Leia `_squad/_shared/nichos.md`, `briefing-template.md`, `regras-globais.md`
4. Para copywriter, webdesigner e designer: leia também `_squad/_shared/humanizer.md`
5. Para gestor-trafego em pedidos com conta real: detecte CLI (`meta --version`) e ofereça onboarding via `_squad/01-gestor-trafego/cli-onboarding.md` se necessário (modo guiado total)
6. Para analista-dados (rodapé `{{NOME_AGENCIA}}` do dashboard) ou qualquer material que carregue a identidade da própria agência (proposta comercial, material institucional): leia também `_squad/_shared/identidade-agencia.md` no lugar do `CLIENTE.md`. Isso nunca substitui a marca do cliente em LP, copy, anúncio ou criativo.
7. Para inteligencia-dados: exige pelo menos um relatório real de ERP (estoque, Curva ABC, vendas por categoria) anexado ou referenciado. Sem isso, para e pede a exportação. Se a fonte for PDF de Curva ABC do sistema Pontual Tecnologia, roda antes a ferramenta em `Operacional/Método Viga Mestra/Ferramenta Curva ABC/SKILL.md` (converte pra XLSX padronizado, script determinístico, sem gasto de IA na conversão em si).
7b. Para qualquer agente: se o pedido corresponde a uma atividade do Método Viga Mestra, cheque antes se existe a seção correspondente (Pilar > Atividade) em `Operacional/Método Viga Mestra/_metodo.md` e siga-a. Se durante a execução nascer um processo genérico novo (reutilizável pra qualquer cliente MatCon), proponha salvar a versão template lá, seguindo `_squad/_shared/template-tarefa.md` (placeholders no lugar de dado real).
8. Execute
9. Rode Humanizer nas saídas textuais
10. Salve em `Operacional/clientes/<nome>/outputs/` (cliente fechado) ou `Comercial/propostas/<nome-prospect>/` (prospect, ver item 6). Estrutura por mês de execução, não por pilar: `outputs/<MM-YYYY>/<Analises|Arquivos>/<DD>-<pilar>-<descritor>.<ext>`, onde `<MM-YYYY>`/`<DD>` é o mês e o dia em que a entrega foi gerada (não o período que o dado cobre) e `<pilar>` é o slug do pilar do Método Viga Mestra que ela atende: `inteligencia-dados`, `dominio-territorial`, `combo-de-produtos`, `vendedor-de-elite`, `plano-obra-integral`. Dentro de cada mês, `Analises/` leva os `.md` (demanda que acionou um agente pra analisar, diagnosticar ou criar estratégia/copy/playbook) e `Arquivos/` leva o resto (planilha tratada, HTML, imagem), o material de consulta/dado que o usuário pode conferir separado. Entrega pontual fora do método omite o `<pilar>`: `outputs/<MM-YYYY>/<Analises|Arquivos>/<DD>-<descritor>.<ext>`. Arquivo cumulativo (diagnóstico que cresce por rodada, nunca sobrescrito) foge dessa regra e fica em `outputs/_diagnosticos/<pilar>/<nome-arquivo>.md`, fora de qualquer pasta de mês e sem divisão Analises/Arquivos. Detalhes do `inteligencia-dados`: Curva ABC e Giro de Estoque e Margem continuam sendo análises diferentes que nunca dividem arquivo, mas a distinção agora fica no nome do arquivo (ex: `25-inteligencia-dados-curva-abc-padronizada_<periodo>.xlsx`, que vai em `Arquivos/`) e em diagnósticos cumulativos separados dentro de `_diagnosticos/inteligencia-dados/` (`diagnostico-curva-abc.md` e `diagnostico-giro-estoque.md`, ver "Formato de output" em `_squad/06-inteligencia-dados/SKILL.md`). Entrega com arquivo de apoio que precisa ficar fisicamente ao lado dela pra funcionar (ex: site HTML autocontido que depende de uma pasta `assets/`) mantém os dois dentro de `Arquivos/`, exceção por necessidade técnica, não a regra geral
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

- `_squad/_skills/meta-ads-cli-setup/` - skill checkpointed em **modo guiado total**. O agente executa todos os comandos via Bash tool, usuário não toca no terminal. Suporta macOS, Linux e Windows (PowerShell). O `gestor-trafego` invoca quando o usuário aceita o upgrade.
- `Operacional/Método Viga Mestra/Ferramenta Curva ABC/SKILL.md` - converte PDF de Curva ABC (sistema Pontual Tecnologia) em XLSX padronizado via script Python determinístico (regex/posição de coluna + pandas, zero chamada de IA na conversão). O `inteligencia-dados` invoca automaticamente antes do diagnóstico quando a fonte é esse tipo de PDF. Fica dentro de `Operacional/Método Viga Mestra/` em vez de `_squad/_skills/`, porque é a ferramenta operacional dessa atividade específica (Pilar 1), não um setup genérico de conta.

## Clientes ativos

- `Operacional/clientes/construmais/` - Material de construção em João Pessoa/PB
- `Operacional/clientes/_TEMPLATE/` - Template para criar novo cliente

## Propostas comerciais (prospects)

- `Comercial/propostas/` - uma subpasta por prospect. Ver `Comercial/propostas/README.md` para estrutura e workflow.
