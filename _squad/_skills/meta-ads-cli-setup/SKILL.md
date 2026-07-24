---
name: meta-ads-cli-setup
description: >
  Use esta skill sempre que o usuário quiser conectar, instalar,
  configurar, autenticar ou debugar o setup inicial da Ads CLI
  oficial da Meta (lançada em 29/04/2026) dentro do Claude Code.
  Trigger para: "conectar meta ads", "configurar ads cli",
  "setup meta ads", "instalar meta ads cli", "ads cli", "meta ads
  no claude code", "system user meta", "access token meta ads",
  "conectar facebook ads", "autenticar marketing api", "primeiro
  relatório meta ads", "criar primeiro relatório de campanha",
  "começar com meta ads", "meta ads não funciona", "token expirado
  meta", "ad account id meta", "business id meta", "marketing api
  token". Esta skill leva do zero (nada instalado) até a primeira
  chamada `meta ads` funcional. Cobre macOS, Linux e Windows
  (PowerShell). MODO GUIADO TOTAL: o agente roda todos os comandos
  diretamente via Bash tool do Claude Code. O usuário não precisa
  abrir terminal nem digitar comando, só clicar na UI da Meta e
  apertar Ctrl+C pra copiar o token (que é lido do clipboard sem
  passar pelo chat). É skill CHECKPOINTED: confirma com o usuário
  no fim de cada fase antes de avançar. Foca no setup inicial
  seguro, não cobre automação avançada. Depois do setup, usa os
  comandos do cheatsheet pra montar workflows.
---

# Meta Ads CLI · Setup guiado dentro do Claude Code (zero → primeira chamada)

Skill **checkpointed + modo guiado total**: o agente executa todos os comandos via Bash tool. O usuário não digita nada no terminal. Cada fase só avança quando o usuário valida. Tudo em português BR, tom direto.

> **Para o agente (não mostrar pro usuário):** sua filosofia aqui é "EU rodo, VOCÊ verifica". Em cada fase, você executa via Bash tool, mostra a saída relevante, interpreta o que aconteceu, e pergunta se pode seguir. Nunca peça pro usuário sair pro terminal pra rodar algo, exceto Fase 2 (UI Meta, que exige clique humano).

---

## 🛡️ REGRAS INVIOLÁVEIS (ler antes de qualquer fase)

1. **NUNCA peça nem aceite o token no chat.** Se o usuário colar um token (qualquer string começando com `EAA…` ou similar) na conversa:
   - Pare imediatamente.
   - Alerte: "⚠️ Você colou um token no chat. Considere ele comprometido. Vá em https://business.facebook.com/settings/system-users → System User → Revogar token → Gerar novo. Vamos refazer a Fase 3 com o token novo, lendo do clipboard sem passar pelo chat."
   - Não prossiga até confirmar a revogação.

2. **Token vai do clipboard direto pra env var.** Na Fase 3, você lê o token do clipboard do usuário (`pbpaste` no Mac, `Get-Clipboard` no Windows, `xclip -o` no Linux) e exporta a env var **sem o token aparecer em nenhum comando visível**. Token nunca em arquivo do projeto, nunca em CLAUDE.md, nunca em código versionado.

3. **Comandos de write são opt-in explícito.** `meta ads campaign create`, `update`, `delete`, `pause`, `resume`, sempre pedir confirmação textual antes de executar. Recursos novos nascem em `status=PAUSED`.

4. **Sempre `meta --output json ads ...`** quando você for parsear a saída. `--output` é flag **global do `meta`**, vai ANTES do subcomando.

5. **Phased, não automatizado.** No fim de cada fase, perguntar: "Posso seguir pra Fase X+1?" Não emende fases.

6. **Você roda. O usuário observa.** Salvo a Fase 2 (UI Meta, inescapável), nenhuma fase pede pro usuário sair pro terminal. Se você se pegar dizendo "agora você roda X", pare e refaça: VOCÊ roda X via Bash tool.

---

## Disparo da skill

Ao ser ativada, sempre começar com:

```
Skill `meta-ads-cli-setup` ativa.

Vou te guiar do zero até a primeira chamada funcional da Ads CLI da
Meta dentro do Claude Code. EU vou rodar todos os comandos - você
não precisa abrir terminal nem digitar comando. Suas tarefas:

  - Aprovar comandos quando o Claude Code pedir (você clica "Allow")
  - Clicar 7-8 vezes no painel da Meta (Fase 2 - eu te guio)
  - Apertar Ctrl+C UMA vez pra copiar o token (eu leio do clipboard)
  - Me confirmar quando avançar de fase

São 6 fases (0 → 5). Antes de começar:

  Qual é o seu sistema?

    [M] macOS
    [L] Linux
    [W] Windows (PowerShell)

  Em qual fase você está?

    [0] Pré-requisitos - nada instalado ainda
    [1] CLI - já tem Python+uv, falta `meta-ads`
    [2] Painel Meta - CLI instalada, falta criar token
    [3] Guardar token - token criado, falta exportar
    [4] Validar conexão - variáveis exportadas, falta testar
    [5] Plugar no Claude Code - CLI funcionando, falta permissões
```

Aguardar a resposta. Não pular fases.

---

## Fase 0: Pré-requisitos (agente verifica e instala)

**Objetivo:** garantir Python 3.12+ e `uv` no computador. Você (agente) verifica e instala o que faltar.

### Passos do agente

1. **Verificar Python via Bash tool:**

   🍎🐧 Mac/Linux: `python3 --version 2>&1`
   🪟 Windows: `python --version 2>&1` (se falhar, tente `py --version`)

   - Se >= 3.12: ok, anuncie `✓ Python 3.12+ detectado`
   - Se < 3.12 ou não encontrado: anuncie e instale automaticamente:
     - 🍎 macOS: `brew install python@3.12` (se não tem brew, instale primeiro: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`)
     - 🐧 Ubuntu/Debian: `sudo apt update && sudo apt install -y python3.12 python3.12-venv` (peça senha do sudo via confirmação)
     - 🪟 Windows: `winget install -e --id Python.Python.3.12` (sem prompt)

2. **Verificar `uv`:**

   `uv --version 2>&1`

   - Se ok: anuncie `✓ uv detectado`
   - Se não: instale automaticamente:
     - 🍎🐧 Mac/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
     - 🪟 Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - **IMPORTANTE no Windows:** depois de instalar, recarregue o PATH na sessão atual:
     ```powershell
     $env:Path += ";$env:USERPROFILE\.local\bin"
     ```
   - Valide com novo `uv --version`.

3. **Confirmar acesso admin ao Meta Business Manager** (essa parte exige confirmação do usuário, pois é fora do computador):

   Pergunte:
   > "Pra ir pra Fase 2 eu vou precisar que você seja admin do Business Manager da conta de anúncios que quer gerenciar. Você é? (Sim/Não, se não souber, abra https://business.facebook.com/settings/people e veja se aparece "Acesso total" ao lado do seu nome)"

### Validação da Fase 0

Você (agente) mostra resumo:
```
✓ Python 3.12.x detectado
✓ uv detectado
✓ Usuário confirmou acesso admin ao Business Manager X
```

### Checkpoint

> "Fase 0 ok. Posso seguir pra Fase 1 (instalar a CLI)?"

---

## Fase 1: Instalar a Ads CLI (agente instala)

**Objetivo:** ter `meta ads --help` funcionando. Você executa.

### Passos do agente

1. **Instalar via uv:**
   ```
   uv tool install meta-ads
   ```

2. **No Windows, garantir PATH na sessão atual:**
   ```powershell
   $env:Path += ";$env:USERPROFILE\.local\bin"
   ```

3. **Validar:**
   ```
   meta ads --version
   meta ads --help
   ```

   Se não funcionar:
   - 🍎🐧 Mac/Linux: rode `which meta`. Se não estiver no PATH, adicione `$HOME/.local/bin` ao PATH e instrua o usuário a reabrir o Claude Code uma vez (pra recarregar PATH em sessões futuras).
   - 🪟 Windows: rode `Get-Command meta -ErrorAction SilentlyContinue`. Se vazio, rode `uv tool update-shell` e instrua a reabrir o Claude Code.

### Validação da Fase 1

```
✓ meta ads instalado (versão X.Y.Z)
✓ Subcomandos disponíveis: campaign, adset, ad, creative, insights
```

### Checkpoint

> "Fase 1 ok, CLI instalada. Posso seguir pra Fase 2 (criar App + System User no painel da Meta)?"

---

## Fase 2: Criar App + System User no Meta (usuário no navegador, agente guia)

**Esta é a única fase que exige cliques humanos.** Você abre as URLs no navegador automaticamente e guia passo a passo. O usuário não sai do Claude Code, abre só a aba do navegador ao lado.

### Abertura

Anuncie:

> "A Meta exige criar o App e o token clicando manualmente no painel deles. Vou abrir 2 abas pra você e te guiar passo a passo. Você não precisa copiar comando nenhum, só clicar e me avisar quando terminar cada parte."

### Passo 2.0: Agente abre as URLs

🍎 Mac:
```bash
open "https://developers.facebook.com/apps"
open "https://business.facebook.com/settings/system-users"
```

🐧 Linux:
```bash
xdg-open "https://developers.facebook.com/apps" 2>/dev/null
xdg-open "https://business.facebook.com/settings/system-users" 2>/dev/null
```

🪟 Windows:
```powershell
Start-Process "https://developers.facebook.com/apps"
Start-Process "https://business.facebook.com/settings/system-users"
```

### Passo 2.1: Criar o App (usuário clica, agente espera)

Mensagem ao usuário:

> "Na aba **developers.facebook.com/apps** que abri:
> 1. Clique em **Criar app** (canto superior direito)
> 2. **Caso de uso:** escolha **Other** → **Continue**
> 3. **Tipo:** **Business** → **Next**
> 4. **Nome do app:** algo simples tipo `Agencia_Claude_2026` → **Create**
> 5. Quando carregar o dashboard do app, **me passa o App ID** (fica no topo da página).
>
> O App ID parece com `1234567890123456` (15-16 dígitos). Pode digitar aqui, não é segredo."

Aguarde. Quando o usuário passar o App ID, anote internamente como `APP_ID`.

### Passo 2.2: Confirmar caso de uso "API de Marketing"

> "Ainda no painel do app:
> 1. Sidebar esquerda → **Casos de uso**
> 2. Confirme que aparece o card **'Criar e gerenciar anúncios com a API de Marketing'**
>
> Se aparecer, me avisa só com 'ok'. Se não aparecer (raro), me avisa também, vou te dar workaround."

### Passo 2.3: Criar o System User

> "Agora vai pra outra aba: **business.facebook.com/settings/system-users**
> 1. Botão **Adicionar** (azul, canto direito)
> 2. **Nome:** `claude_code_ads` (ou outro nome simples)
> 3. **Função:** **Funcionário** ⚠️ (não Admin, explico no fim)
> 4. **Criar usuário do sistema**
>
> Me confirma quando ele aparecer na lista."

> ⚠️ **Por que Funcionário e não Admin:** muitos BMs têm limite de 1 Admin (já ocupado por WhatsApp BOT, Conversions API, etc.). Funcionário é suficiente pra Ads CLI, explicado na legacy v1.

### Passo 2.4: Atribuir conta de anúncios ao System User

> "Agora você vai dar permissão de gerenciar campanhas pra esse System User:
> 1. Clique no System User que acabou de criar
> 2. Botão **Adicionar ativos** → **Contas de anúncios**
> 3. Selecione a conta de anúncios do cliente que vamos gerenciar
> 4. Marque **TODAS** as caixas de permissão (gerenciar campanhas, ver desempenho, etc.)
> 5. **Salvar alterações**
>
> Me avisa quando terminar."

### Passo 2.5: Atribuir o App ao System User

> "Mesmo System User:
> 1. **Adicionar ativos** de novo → **Apps**
> 2. Selecione o app que você criou no Passo 2.1
> 3. Marque **Desenvolver app**
> 4. **Salvar alterações**"

### Passo 2.6: Gerar o token (PARTE CRÍTICA)

> "Última parte, e a mais importante. Ainda no System User:
> 1. Botão **Gerar novo token**
> 2. Selecione o **app** que você criou
> 3. **Validade do token:** **Nunca**
> 4. **Escopos:** use a busca pra encontrar e marcar EXATAMENTE estes 4:
>   , `ads_management`
>   , `ads_read`
>   , `business_management`
>   , `pages_read_engagement`
> 5. Clique **Gerar token**
> 6. **PARE.** O token vai aparecer numa caixa. **NÃO copia ainda.**
>
> Me avisa quando estiver vendo a caixa com o token."

Aguarde o usuário confirmar.

> "Beleza. Agora, atenção total:
> 1. Clique no botão **Copiar** ao lado do token (ou selecione tudo e Ctrl+C / Cmd+C)
> 2. Me avisa com a palavra `COPIEI`, vou ler direto do seu clipboard.
> 3. ⚠️ **NÃO COLE O TOKEN AQUI NO CHAT.** Se colar, eu vou parar a skill e a gente vai ter que gerar token novo."

Aguarde a confirmação `COPIEI` (ou similar). Vá pra Fase 3.

### Coletar também (sem ser segredo)

Pergunte ao usuário:

> "Antes de prosseguir, me passa também:
>
> 1. **AD_ACCOUNT_ID:** abre https://business.facebook.com/settings/ad-accounts, clica na conta, copia o ID que aparece (formato: `act_1234567890`)
> 2. **BUSINESS_ID:** abre https://business.facebook.com/settings/info, copia o **ID do negócio** (formato: 15-16 dígitos)
>
> Pode digitar os dois aqui, não são segredos."

### Checkpoint

> "Fase 2 ok? Você tem (a) `COPIEI` confirmado pro token, (b) AD_ACCOUNT_ID, (c) BUSINESS_ID? Posso seguir pra Fase 3?"

---

## Fase 3: Guardar o token via clipboard (agente lê, NUNCA o usuário cola)

**Objetivo:** transferir token do clipboard pra env var permanente, sem o token aparecer em comando visível. Você (agente) executa.

### ⚠️ Protocolo de segurança

O agente roda comandos que **lêem do clipboard direto pra env var**. O token nunca aparece como string literal em nenhum comando, nem no Bash visible output, nem no transcript.

### Passos do agente: 🍎 macOS

1. **Ler token do clipboard pra env var permanente:**
   ```bash
   echo "# === Meta Ads CLI ===" >> ~/.zshrc
   echo "export ACCESS_TOKEN=\"$(pbpaste)\"" >> ~/.zshrc
   echo "export AD_ACCOUNT_ID=\"act_VALUE\"" >> ~/.zshrc
   echo "export BUSINESS_ID=\"VALUE\"" >> ~/.zshrc
   ```
   Substitua `act_VALUE` e `VALUE` pelos IDs que o usuário forneceu na Fase 2.

2. **Recarregar pra sessão atual:**
   ```bash
   source ~/.zshrc
   ```

3. **Validar SEM imprimir o token:**
   ```bash
   echo "Token prefix: ${ACCESS_TOKEN:0:10}..."
   echo "Token length: ${#ACCESS_TOKEN}"
   echo "Token sufixo: ...${ACCESS_TOKEN: -4}"
   echo "Account: $AD_ACCOUNT_ID"
   echo "Business: $BUSINESS_ID"
   ```

### Passos do agente: 🐧 Linux

Idêntico ao macOS, mas:
- Se shell for bash: usar `~/.bashrc` em vez de `~/.zshrc`
- Comando do clipboard: `$(xclip -selection clipboard -o)` (se `xclip` não estiver instalado, instale via `sudo apt install xclip`)

```bash
echo "# === Meta Ads CLI ===" >> ~/.bashrc
echo "export ACCESS_TOKEN=\"$(xclip -selection clipboard -o)\"" >> ~/.bashrc
echo "export AD_ACCOUNT_ID=\"act_VALUE\"" >> ~/.bashrc
echo "export BUSINESS_ID=\"VALUE\"" >> ~/.bashrc
source ~/.bashrc
```

### Passos do agente: 🪟 Windows (PowerShell)

1. **Ler clipboard e salvar como env var permanente (escopo User):**
   ```powershell
   $token = Get-Clipboard
   [Environment]::SetEnvironmentVariable("ACCESS_TOKEN", $token, "User")
   [Environment]::SetEnvironmentVariable("AD_ACCOUNT_ID", "act_VALUE", "User")
   [Environment]::SetEnvironmentVariable("BUSINESS_ID", "VALUE", "User")
   $token = $null  # limpa variável temporária da sessão
   ```

2. **Recarregar sessão atual:**
   ```powershell
   $env:ACCESS_TOKEN  = [Environment]::GetEnvironmentVariable("ACCESS_TOKEN",  "User")
   $env:AD_ACCOUNT_ID = [Environment]::GetEnvironmentVariable("AD_ACCOUNT_ID", "User")
   $env:BUSINESS_ID   = [Environment]::GetEnvironmentVariable("BUSINESS_ID",   "User")
   ```

3. **Validar SEM imprimir o token:**
   ```powershell
   "Token prefix: $($env:ACCESS_TOKEN.Substring(0,10))..."
   "Token length: $($env:ACCESS_TOKEN.Length)"
   "Token sufixo: ...$($env:ACCESS_TOKEN.Substring($env:ACCESS_TOKEN.Length-4))"
   "Account: $env:AD_ACCOUNT_ID"
   "Business: $env:BUSINESS_ID"
   ```

### Validação esperada (todos os SOs)

Saída deve ser tipo:
```
Token prefix: EAAJ4yzABC...
Token length: 195    (típico: 195-220 chars)
Token sufixo: ...x1Y2
Account: act_1234567890
Business: 9876543210
```

Se o token vier vazio ou com tamanho estranho, o clipboard não tinha o token. Peça pro usuário copiar de novo e rode o comando outra vez.

### Se o usuário colar o token no chat por engano

Disparar imediatamente:

> ⚠️ **Você colou o token na conversa.** O transcript da nossa sessão pode ser armazenado. Considere o token comprometido.
>
> **Plano:**
> 1. Vou abrir o painel pra você revogar o token agora
> 2. Você gera um novo token (refazendo a parte 2.6 da Fase 2)
> 3. Volta aqui e a gente refaz a Fase 3 com clipboard

E rode `open https://business.facebook.com/settings/system-users` (ou equivalente do SO). Não prossiga até confirmar revogação.

### Checkpoint

> "Fase 3 ok. A validação mostrou prefixo do token + account + business sem expor o token completo? Posso seguir pra Fase 4 (validar conexão real com a API da Meta)?"

---

## Fase 4: Validar conexão (agente roda, mostra relatório bonito)

**Objetivo:** primeira chamada real à API da Meta. Você (agente) executa e formata o resultado pro usuário.

### Passos do agente

1. **Testar conexão básica (read-only):**
   ```bash
   meta --output json ads adaccount get
   ```

   Parsear a saída e mostrar ao usuário em formato amigável:
   ```
   ✓ Conexão validada com a Meta API:
     Conta:     Nome da Conta Aqui
     ID:        act_1234567890
     Status:    ACTIVE
     Moeda:     BRL
     Timezone:  America/Sao_Paulo
     Gasto:     R$ X.XXX,XX
   ```

2. **Listar campanhas:**
   ```bash
   meta --output json ads campaign list --limit 10
   ```

   - Se retornar JSON com array de campanhas: mostre quantas existem + 3 primeiras (nome + status + budget)
   - Se retornar `[]` ou `No results`: anuncie "✓ Conexão ok. Conta sem campanhas ativas no momento, normal pra conta nova."

3. **Testar insights:**
   ```bash
   meta --output json ads insights get --date-preset last_7d --fields impressions,spend,ctr,cpc
   ```

   - Se vier `{"data":[...]}`: mostre métricas resumidas
   - Se vier `{"data":[]}`: "✓ Conexão ok. Sem dados nos últimos 7 dias."

### Mapa de troubleshooting (você diagnostica e fixa sozinho)

| Erro retornado | Causa | Você (agente) faz |
|---|---|---|
| `Error: No such option '--output'.` | Você pôs `--output json` depois do subcomando | Rode de novo na ordem certa: `meta --output json ads ...` |
| `Error: No ad account configured.` | `AD_ACCOUNT_ID` não exportado ou sessão não recarregada | Re-rode os comandos de recarga da Fase 3 |
| `OAuthException: Invalid OAuth access token` | Token errado / vazio / sessão não recarregada | Verifique com `echo "len: ${#ACCESS_TOKEN}"` ou `$env:ACCESS_TOKEN.Length`. Se vazio, refaça Fase 3 |
| `(#100) Tried accessing nonexisting field` | `AD_ACCOUNT_ID` sem prefixo `act_` | Re-salve a var com `act_` no começo |
| `(#200) Permissions error` | Escopo faltando ou System User sem permissão na conta | Volte pra Fase 2.4 e 2.6, refaça |
| `(#17) User request limit reached` | Rate limit Meta | Espere 1h ou use `--limit 25` |
| `(#190) Session has expired` | Token de user comum (60d), não System User | Refaça Fase 2.3-2.6 como System User Funcionário |

Detalhes em `references/troubleshooting.md`.

### Checkpoint

> "Fase 4 ok? Conexão validada com a API da Meta? Posso seguir pra Fase 5 (plugar a CLI no Claude Code com permissões seguras)?"

---

## Fase 5: Integrar com o Claude Code (agente cria configs)

**Objetivo:** configurar `.claude/settings.local.json` no projeto atual pra que o Claude Code possa rodar comandos `meta` read-only sem pedir permissão a cada vez. Você (agente) faz tudo via Write tool.

### Passo 5.1: Detectar o projeto atual

Pergunte ao usuário:

> "Você está em qual pasta do Claude Code? Geralmente é o workspace `agencia/` do Squad ou uma pasta específica de cliente (`agencia/clientes/<nome>/`). Me confirma o caminho completo."

Ou rode `pwd` (Mac/Linux) ou `Get-Location` (Windows) pra detectar automaticamente.

### Passo 5.2: Criar/atualizar `.claude/settings.local.json`

Use a ferramenta Write/Edit do Claude Code pra criar o arquivo no projeto.

🍎🐧 **Conteúdo (Mac/Linux):**
```json
{
  "permissions": {
    "allow": [
      "Bash(meta --output json ads campaign list:*)",
      "Bash(meta --output json ads adset list:*)",
      "Bash(meta --output json ads ad list:*)",
      "Bash(meta --output json ads creative list:*)",
      "Bash(meta --output json ads insights get:*)",
      "Bash(meta --output json ads adaccount get:*)",
      "Bash(meta ads campaign list:*)",
      "Bash(meta ads insights get:*)",
      "Bash(source ~/.zshrc:*)",
      "Bash(source ~/.bashrc:*)"
    ]
  }
}
```

🪟 **Conteúdo (Windows):**
```json
{
  "permissions": {
    "allow": [
      "Bash(meta --output json ads campaign list:*)",
      "Bash(meta --output json ads adset list:*)",
      "Bash(meta --output json ads ad list:*)",
      "Bash(meta --output json ads creative list:*)",
      "Bash(meta --output json ads insights get:*)",
      "Bash(meta --output json ads adaccount get:*)",
      "Bash(meta ads campaign list:*)",
      "Bash(meta ads insights get:*)"
    ]
  }
}
```

> **Por que não `Bash(meta ads:*)` ou `Bash(meta:*)`?** Porque incluiria `meta ads campaign delete` sem confirmação. Whitelist apenas read-only.

Se o `.claude/settings.local.json` já existir, **mergee** os campos do `permissions.allow` (não sobrescreva o arquivo inteiro).

### Passo 5.3: Atualizar CLAUDE.md do projeto (opcional, mas recomendado)

Pergunte:

> "Quer que eu adicione um bloco no `CLAUDE.md` do projeto explicando que ele agora tem acesso à Meta Ads CLI? Isso ajuda em sessões futuras."

Se sim, use o template em `references/claude-md-template.md` e adicione/mergee no `CLAUDE.md` do projeto via Write/Edit tool.

### Passo 5.4: Primeiro workflow de exemplo

Anuncie:

> "Setup completo. Vou rodar um relatório de exemplo pra você ver funcionando:"

Execute:
```bash
meta --output json ads campaign list --limit 5
meta --output json ads insights get --date-preset last_7d --fields campaign_name,impressions,spend,ctr,cpc
```

Parseie a saída e devolva pro usuário um relatório em markdown bonitinho:

```
## Relatório dos últimos 7 dias

| Campanha | Impressões | Gasto | CTR | CPC |
|---|---|---|---|---|
| ... | ... | R$ ... | ...% | R$ ... |
```

### Checkpoint final

> "✓ Setup completo. CLI da Meta plugada no Claude Code deste projeto.
>
> Daqui em diante:
>, Pra **relatórios**: peça e eu rodo (`@gestor-trafego` ou direto)
>, Pra **executar** mudanças na conta (criar campanha, pausar, etc.): peça explicitamente, eu vou pedir confirmação textual e tudo nasce em PAUSED
>, **Token expira nunca** (System User). Se um dia parar de funcionar, volta aqui que a gente refaz a Fase 4
>
> Bora começar?"

---

## Recursos bundleados (referências internas)

Ler sob demanda quando a fase pedir:

- `references/troubleshooting.md`, catálogo de erros + fix
- `references/comandos-cheatsheet.md`, comandos `meta ads` mais usados (read + write)
- `references/claude-md-template.md`, bloco pra colar no CLAUDE.md do projeto

---

## Notas pra agentes do squad que invocam essa skill

Se você é o `@gestor-trafego` (ou outro agente do Squad AgêncIA 100k) e o aluno aceitou o upgrade via `cli-onboarding.md`:

1. Anuncie a transição uma vez
2. Siga este SKILL.md fielmente, fase a fase
3. Quando terminar a Fase 5, **volte pra a task original** do aluno (diagnóstico, plano, execução), agora com acesso a comandos `meta` reais.
4. Em comandos write subsequentes (Nível 3 do gestor-trafego), aplique a Regra 22 de `_shared/regras-globais.md`.

---

## Versão

- **v2 (modo guiado total):** este arquivo. Agente executa via Bash tool, usuário não toca no terminal. Token via clipboard.
- **v1 (modo manual):** preservado em `SKILL.legacy-v1-manual.md`, versão original onde o usuário copia/cola comandos. Mantido pra referência caso alguém prefira esse fluxo.
