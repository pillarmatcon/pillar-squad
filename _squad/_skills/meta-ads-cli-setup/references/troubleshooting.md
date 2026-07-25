# Troubleshooting · Meta Ads CLI Setup

Catálogo de erros comuns no caminho **zero → primeira chamada funcional**. Organizado por fase e sistema operacional (🍎 macOS, 🐧 Linux, 🪟 Windows). Cada erro tem: **sintoma exato** → **causa raiz** → **fix passo a passo** → **como validar que resolveu**.

---

## Problemas do modo guiado (Claude Code rodando comandos)

### Popup "Allow this Bash command?" do Claude Code

**Sintoma:** Toda vez que o agente tenta rodar um comando novo, aparece um popup pedindo aprovação.

**Causa:** Proteção de segurança do Claude Desktop. Padrões de comando novos exigem aprovação explícita.

**Fix recomendado:**
1. Quando aparecer, clique em **"Allow for this session"** (não só "Allow"), assim libera o padrão pra essa sessão inteira.
2. Após a Fase 5, o `settings.local.json` pré-autoriza os comandos `meta` permanentemente, popups param.

**Se quiser pré-autorizar mais cedo:** o agente pode criar um `.claude/settings.local.json` mínimo logo na Fase 1 com pré-aprovação só pra `uv tool install`, `meta --version`, `meta ads --help`. Mas isso aumenta superfície de risco, recomendo só fazer se o usuário ficar muito incomodado.

---

### Clipboard vazio ou token inválido após Fase 3

**Sintoma:** Validação da Fase 3 retorna:
- `Token length: 0` → clipboard tava vazio
- `Token length: 5` ou outro número muito pequeno → copiou outra coisa por engano (URL, nome, etc.)
- `Token length: > 300` → copiou texto extra junto (algum espaço, caractere invisível)

**Causa:** O Ctrl+C / Cmd+C não pegou o token completo, ou o usuário copiou outra coisa entre o Passo 2.6 e a Fase 3.

**Fix:**

1. **Volte pro painel da Meta** (https://business.facebook.com/settings/system-users → seu System User → Tokens).

2. Se o token ainda aparece (raro, geralmente some depois de gerado):
   - Clique no botão "Copiar" ao lado do token (não Ctrl+C manual, botão de cópia da UI)
   - Não copie mais nada até voltar pro Claude Code
   - Avise o agente: `repete a fase 3`
   - Agente re-executa o comando de leitura do clipboard

3. Se o token sumiu da tela (caso normal, só aparece 1 vez):
   - Não dá pra recuperar. Gera token novo:
     - System User → **Gerar novo token** → mesmos escopos da Fase 2.6
     - Botão **Copiar** ao lado do novo token
     - Avise o agente: `repete a fase 3 com token novo`

**Valida:** Após re-rodar, a validação deve mostrar:
```
Token prefix: EAA... (começa com EAA, EAAJ, EAAG)
Token length: 195-220 chars
```

---

### Clipboard sem permissão (Linux/WSL)

**Sintoma:** Em Linux ou WSL2, o comando `xclip` retorna erro tipo:
- `Can't open display`
- `xclip: command not found`

**Causa:** xclip não instalado, ou rodando em ambiente sem display X11 (WSL sem WSLg, servidor headless).

**Fix:**
```bash
# Ubuntu/Debian
sudo apt install xclip xsel

# Ou usar xsel se já estiver instalado
xsel --clipboard --output
```

**No WSL2 sem WSLg:** o clipboard do Windows é acessível via:
```bash
# Lê clipboard do Windows host
powershell.exe -c "Get-Clipboard" | tr -d '\r'
```

Avise o agente que está em WSL pra ele usar esse caminho alternativo na Fase 3.

---

## Fase 0: Pré-requisitos

### 🍎🐧 `python3: command not found`

**Causa:** macOS antigo sem Python ou shell com PATH zoado.

**Fix (macOS):**
```bash
brew install python@3.12
echo 'export PATH="/opt/homebrew/opt/python@3.12/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Fix (Ubuntu/Debian):**
```bash
sudo apt update && sudo apt install python3.12 python3.12-venv
```

**Valida:** `python3 --version` retorna `Python 3.12.x`.

---

### 🪟 `python : The term 'python' is not recognized` (Windows)

**Causa:** Python não instalado ou instalado sem marcar "Add Python to PATH".

**Fix:**
```powershell
# Opção A - winget (recomendado)
winget install Python.Python.3.12

# Opção B - baixar instalador do python.org
# IMPORTANTE: na primeira tela do instalador, MARCAR a caixa
# "Add python.exe to PATH" antes de clicar Install.

# Reabrir o PowerShell pra recarregar o PATH
```

**Valida:** `python --version` retorna `Python 3.12.x`. Se ainda não funcionar, tentar `py --version` (Python Launcher).

---

### 🪟 `Get-Command : The term 'uv' is not recognized` (Windows)

**Causa:** uv instalado mas o PATH ainda não foi recarregado, ou bloqueio do antivírus durante instalação.

**Fix:**
```powershell
# Verificar se uv foi instalado
Test-Path "$env:USERPROFILE\.local\bin\uv.exe"

# Se sim, recarregar PATH manualmente
$env:Path += ";$env:USERPROFILE\.local\bin"

# Se a verificação acima retornar False, reinstalar
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Reabrir o PowerShell depois
```

**Valida:** `uv --version` retorna um número.

---

### Python < 3.12

**Causa:** versão antiga (3.9, 3.10, 3.11 não atendem requisito da Ads CLI).

**Fix (recomendado, usando uv):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.12
```

**Valida:** `uv run python --version` retorna `3.12.x`.

---

## Fase 1: Install da CLI

### `command not found: meta` depois de instalar

**Causa:** binário foi instalado em `~/.local/bin` (pip --user) ou `~/.cargo/bin` (uv) e o PATH não inclui isso.

**Fix:**
```bash
# Descobrir onde foi instalado
which meta || find ~ -name "meta" -type f 2>/dev/null | head -5

# Adicionar ao PATH (zsh)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Valida:** `which meta` retorna um caminho válido.

---

### `error: externally-managed-environment` no pip

**Causa:** macOS com Python via Homebrew bloqueia pip global (PEP 668).

**Fix:**
```bash
# Trocar pra uv (recomendado)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install meta-ads
```

**Valida:** `meta ads --help` funciona.

---

### Conflito de pacote: outro `meta` instalado

**Sintoma:** `meta --help` mostra ajuda de outro tool (ex: meta-ai, meta-llama).

**Fix:**
```bash
# Identificar o conflito
which -a meta

# Desinstalar conflitante (exemplo)
pip3 uninstall meta meta-ai meta-llama

# Reinstalar via uv (isola)
uv tool install meta-ads
```

**Valida:** `meta ads --help` mostra subcomandos `campaign`, `adset`, `ad`, `insights`.

---

## Fase 2: App + System User

### "Não vejo opção 'Usuários do sistema' no Business Manager"

**Causa:** usuário está logado em conta pessoal do Facebook, não no Business Manager. OU não é admin do BM.

**Fix:**
1. Confirmar URL: deve ser `business.facebook.com/settings/system-users`
2. Se redirecionar pra `business.facebook.com/overview`, é porque não tem BM associado
3. Criar BM novo em `business.facebook.com/overview` se for o caso
4. Se BM existe mas opção não aparece: pedir ao admin do BM pra elevar permissão

---

### "Gerei o token mas a CLI retorna `Invalid OAuth access token`"

**Causa #1:** Token foi gerado mas escopos faltando.

**Fix:** voltar em business.facebook.com → System User → Gerar novo token → confirmar EXATAMENTE estes escopos:
- `ads_management`
- `ads_read`
- `business_management`
- `pages_read_engagement`
- `read_insights`

**Causa #2:** Token foi de usuário comum, não System User.

**Fix:** Token de System User começa igual a token comum (`EAA...`), mas o caminho de criação é diferente:
- ❌ ERRADO: `developers.facebook.com → App → Tools → Graph API Explorer → Generate Token`
- ✅ CERTO: `business.facebook.com → Configurações → Usuários do sistema → [seu user] → Gerar novo token`

**Valida:** Token de System User tem validade **"Nunca"** quando você gera. Se a opção não apareceu, foi pelo caminho errado.

---

### "Atribuí a conta mas continua dando erro 200 (Permissions)"

**Causa:** Permissão atribuída mas com nível baixo demais.

**Fix:**
1. Ir em System User → Ativos atribuídos → conta de anúncios
2. Confirmar que **TODAS** as caixas estão marcadas em "Gerenciar campanhas" (não só "Visualizar performance")
3. Salvar
4. Pode levar 1-2 min pra propagar

---

## Fase 3: Guardar o token

### 🍎🐧 `echo $ACCESS_TOKEN` retorna vazio

**Causa #1:** Não rodou `source ~/.zshrc` depois de editar.

**Fix:**
```bash
source ~/.zshrc
echo "${ACCESS_TOKEN:0:10}..."
```

**Causa #2:** Editou o arquivo errado (`.bashrc` no macOS quando shell é zsh, ou vice-versa).

**Fix:**
```bash
echo $SHELL  # /bin/zsh → ~/.zshrc | /bin/bash → ~/.bashrc
```

**Causa #3:** Você usou prefixo `META_ADS_` (sugestão antiga da skill). A CLI espera `ACCESS_TOKEN`, `AD_ACCOUNT_ID`, `BUSINESS_ID` **sem prefixo**.

**Causa #4:** Linha tem aspas erradas ou espaços.

```bash
# ✅ CERTO
export ACCESS_TOKEN="EAA..."

# ❌ ERRADO (espaço antes/depois do =)
export ACCESS_TOKEN = "EAA..."

# ❌ ERRADO (sem aspas, token tem caractere especial)
export ACCESS_TOKEN=EAA...
```

---

### "Colei o token no chat por engano"

**Plano de contenção:**

1. **Revogar imediatamente:**
   - https://business.facebook.com → Configurações → Usuários do sistema
   - Clicar no seu System User
   - Aba **Tokens** → encontrar o token comprometido → **Revogar**

2. **Gerar novo token** (Fase 2.6 do SKILL.md)

3. **Refazer Fase 3** colocando o novo token só em variável de ambiente (`~/.zshrc` no Mac/Linux, ou `[Environment]::SetEnvironmentVariable` no Windows)

4. **Não delete a conversa:** isso não apaga o transcript no histórico do Claude Code. Revogação é a única defesa.

---

### 🪟 `$env:ACCESS_TOKEN` retorna vazio (Windows)

**Causa #1:** Você setou a variável com `[Environment]::SetEnvironmentVariable(...)` mas ainda não recarregou na sessão atual.

**Fix:**
```powershell
$env:ACCESS_TOKEN  = [Environment]::GetEnvironmentVariable("ACCESS_TOKEN",  "User")
$env:AD_ACCOUNT_ID = [Environment]::GetEnvironmentVariable("AD_ACCOUNT_ID", "User")
$env:BUSINESS_ID   = [Environment]::GetEnvironmentVariable("BUSINESS_ID",   "User")
"$($env:ACCESS_TOKEN.Substring(0,10))..."
```

**Causa #2:** Você setou no escopo errado (`Machine` em vez de `User`, ou `Process` que só dura a sessão).

**Verificar todos os escopos:**
```powershell
"User:    $([Environment]::GetEnvironmentVariable('ACCESS_TOKEN','User').Length) chars"
"Machine: $([Environment]::GetEnvironmentVariable('ACCESS_TOKEN','Machine').Length) chars"
"Process: $([Environment]::GetEnvironmentVariable('ACCESS_TOKEN','Process').Length) chars"
```

Se o tamanho aparecer em `Machine` mas não em `User`, mover pro escopo certo:
```powershell
$tk = [Environment]::GetEnvironmentVariable("ACCESS_TOKEN", "Machine")
[Environment]::SetEnvironmentVariable("ACCESS_TOKEN", $tk, "User")
[Environment]::SetEnvironmentVariable("ACCESS_TOKEN", $null, "Machine")  # limpar do Machine
$tk = $null
```

---

### 🪟 PowerShell bloqueado: "running scripts is disabled on this system"

**Sintoma:** ao rodar o instalador do uv ou qualquer script `.ps1`, você vê:
```
File ... cannot be loaded because running scripts is disabled on this system.
For more information, see about_Execution_Policies
```

**Causa:** política de execução do PowerShell está restritiva (default em alguns Windows corporativos).

**Fix temporário (só pra sessão atual):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
# Depois rodar o comando que travou
```

**Fix permanente (recomendado pra uso normal):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Aceitar com "Y"
```

`RemoteSigned` permite rodar scripts locais e exige assinatura só pra scripts baixados.

---

### 🪟 Antivírus / SmartScreen bloqueia o `meta.exe`

**Sintoma:** ao rodar `meta ads --help` pela primeira vez, Windows Defender SmartScreen avisa "Windows protected your PC".

**Causa:** o `meta.exe` não tem assinatura conhecida pelo Defender ainda. Falso positivo comum em CLIs novas.

**Fix:**
1. No popup do SmartScreen, clicar **"More info"** → **"Run anyway"**
2. Se ainda travar, adicionar exclusão:
   - Configurações → Privacidade e segurança → Segurança do Windows → Proteção contra vírus e ameaças
   - Gerenciar configurações → Adicionar ou remover exclusões
   - Adicionar pasta: `%USERPROFILE%\.local\bin`

**Valida:** `meta ads --help` roda sem popup.

---

## Fase 4: Validação

### `Error: No such option '--output'.`

**Causa:** `--output json` é flag **global do `meta`**, vai ANTES do subcomando, não depois. Confirmado em teste real com `meta-ads 1.0.1`.

**Fix:**
```bash
# ❌ ERRADO
meta ads campaign list --output json

# ✅ CERTO
meta --output json ads campaign list
```

### `Error: No ad account configured.`

**Causa:** `AD_ACCOUNT_ID` não está exportado ou shell não foi recarregado.

**Fix:**
```bash
source ~/.zshrc
echo "$AD_ACCOUNT_ID"   # deve retornar act_XXXXX

# ou passar inline na chamada:
meta --ad-account-id act_XXXXX --output json ads campaign list
```

### `OAuthException: Invalid OAuth access token - Cannot parse access token`

Token corrompido (espaço, quebra de linha, aspas extras no `~/.zshrc`).

**Fix:**
```bash
# Confirmar formato (deve ser uma única linha, sem quebras)
grep ACCESS_TOKEN ~/.zshrc
```

Reabrir `~/.zshrc`, garantir linha única, salvar, `source`, retestar.

---

### `(#100) Tried accessing nonexisting field`

`AD_ACCOUNT_ID` está sem o prefixo `act_`.

**Fix:**
```bash
# ❌ ERRADO
export AD_ACCOUNT_ID="1234567890"

# ✅ CERTO
export AD_ACCOUNT_ID="act_1234567890"
```

---

### `(#17) User request limit reached`

Rate limit da Marketing API. Cada token tem orçamento horário de chamadas.

**Fix imediato:** esperar 1h.

**Fix de longo prazo:**
```bash
# Usar --limit pra reduzir tamanho das respostas
meta ads campaign list --limit 25 --output json

# Usar --fields pra pegar só o que precisa
meta ads insights get --fields impressions,spend --output json
```

---

### `(#190) Error validating access token: Session has expired`

**Causa:** Token de usuário comum (expira em 60 dias). Não é System User.

**Fix:** Refazer toda Fase 2 como System User. **Não dá pra "renovar", precisa migrar pra System User.**

---

### `Could not resolve host: graph.facebook.com`

Problema de rede local. Não é da CLI.

**Fix:**
```bash
# Testar conectividade
curl -I https://graph.facebook.com/v19.0/

# Se falhar: VPN, firewall corporativo, DNS, ou Meta com instabilidade
# Checar status: https://metastatus.com
```

---

## Fase 5: Claude Code

### "Claude Code pede confirmação pra cada `meta ads campaign list`"

**Causa:** Permissão não foi adicionada em `.claude/settings.local.json`.

**Fix:** colar no `.claude/settings.local.json` do projeto:
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
      "Bash(source ~/.zshrc:*)"
    ]
  }
}
```

Reabrir o Claude Code.

---

### "Claude Code executou um `delete` sem pedir confirmação"

**Causa #1:** Permissão muito ampla. Tem `Bash(meta ads:*)` em vez de allowlist específica.

**Fix:** apertar o escopo no `.claude/settings.local.json`, só read-only no allow. Writes precisam disparar prompt.

**Causa #2:** CLAUDE.md sem regra explícita.

**Fix:** colar o bloco de `references/claude-md-template.md` no CLAUDE.md do projeto.

---

## Checklist final

Antes de fechar a sessão de setup, confirmar:

- [ ] `meta ads --help` funciona
- [ ] `echo "${ACCESS_TOKEN:0:10}..."` mostra prefixo (não vazio)
- [ ] `meta --output json ads campaign list` retorna sem erro (texto `No results.` em conta nova é ok)
- [ ] `meta --output json ads insights get --date-preset last_7d` retorna `{"data":[...]}` ou `{"data":[]}`
- [ ] `meta --output json ads adaccount get` retorna o JSON real da conta
- [ ] `.claude/settings.local.json` tem allowlist de read-only
- [ ] CLAUDE.md tem regras de write/PAUSED/json
- [ ] Token está APENAS em `~/.zshrc`, em nenhum outro lugar (nem .env do projeto, nem CLAUDE.md, nem chat)
