# Onboarding da Meta Ads CLI (oferta condicional)

> **Uso:** consultado pelo `@gestor-trafego` quando o aluno pede algo que se beneficia de dados reais da conta Meta (diagnóstico, relatório, execução de plano) **e** a CLI ainda não está disponível no ambiente.

---

## Quando oferecer

O agente verifica a disponibilidade da CLI com:

```bash
meta --version
```

- Se retornar versão (ex: `meta 1.0.1`) → **não ofereça onboarding**. Vai direto pro Nível 2 (leitura) ou Nível 3 (execução com confirmação).
- Se retornar `command not found` → **ofereça as 2 opções abaixo**.

Não ofereça onboarding em pedidos que não dependem de dados reais (ex: aluno só quer plano de tráfego do zero, sem conta existente). Nesses casos, modo padrão (markdown) é suficiente.

---

## Script de apresentação ao aluno

Quando precisar oferecer, use este texto verbatim (adaptado ao contexto do pedido):

```
Pra fazer {DIAGNÓSTICO | RELATÓRIO | EXECUÇÃO} de verdade, eu tenho 2 caminhos:

  [1] MODO MANUAL - você exporta o CSV do Meta Ads e cola aqui.
      Eu analiso e devolvo as recomendações em markdown.
      Você executa os ajustes manualmente no Gerenciador de Anúncios.
      Tempo: 5 min você + 5 min eu = 10 min por iteração.

  [2] MODO CLI - a gente faz um setup técnico uma vez só (~1h)
      que conecta a Ads CLI oficial da Meta ao Claude Code.
      Depois disso, EU PUXO OS DADOS DIRETO DA API e ainda posso
      EXECUTAR ajustes na sua conta (com sua confirmação textual
      em cada operação, e tudo nasce em PAUSED).
      Tempo no dia a dia: 2 min você + 1 min eu = 3 min por iteração.

  Qual prefere agora?
```

Aguarde a escolha.

---

## Se o aluno escolher [1] MANUAL

Continue como sempre fez:
1. Peça o CSV ou os números relevantes
2. Analise
3. Entregue recomendações em markdown
4. Aluno executa manualmente

Não insista no upgrade. Termine a tarefa.

---

## Se o aluno escolher [2] CLI

1. **Anuncie a transição:**

```
Beleza. Vou ativar agora o protocolo de setup da Meta Ads CLI.
São 6 fases checkpointed (você confirma cada uma antes da próxima).
Estimativa total: 45 min a 1h15 dependendo de quanto a Meta vai
te embromar na criação do App.

Quando terminar, eu volto pra sua pergunta original sobre
{DIAGNÓSTICO | RELATÓRIO | EXECUÇÃO} da conta da {CLIENTE} com
dados reais.

Confirmando, vou começar pela Fase 0 (pré-requisitos).
```

2. **Leia e siga integralmente** `_squad/_skills/meta-ads-cli-setup/SKILL.md`. Esse arquivo é uma skill completa e checkpointed, ele toma conta do onboarding por 6 fases (0 → 5).

3. **Durante o onboarding, mantenha-se em personagem da skill** `meta-ads-cli-setup`. Não saia de fase sem confirmação.

4. **Regras de segurança da skill são INVIOLÁVEIS** (ver `_squad/_skills/meta-ads-cli-setup/SKILL.md`, seção "REGRAS INVIOLÁVEIS"):
   - Token nunca passa pelo chat
   - Tudo em env vars no shell
   - Comandos write são opt-in explícito

5. **Quando a Fase 5 terminar** (CLI integrada com Claude Code), anuncie:

```
✓ Setup completo. CLI disponível e validada.

Voltando à sua pergunta original: você queria {RESUMO DO QUE PEDIU}
pra {CLIENTE}. Posso seguir agora com dados reais da conta?
```

Aguarde a confirmação e retome a task original, agora com acesso a comandos read-only da CLI (ver `_skills/meta-ads-cli-setup/references/comandos-cheatsheet.md`).

---

## Se a CLI fica disponível em meio à conversa

(Aluno fez o setup em paralelo, ou já tinha mas você não detectou de primeira)

Quando a `meta --version` passar a responder, anuncie:

```
✓ Detectei que a Meta Ads CLI está disponível. A partir de agora
posso usar dados reais da conta no diagnóstico. Próxima pergunta
sua eu já uso a CLI.
```

E siga usando comandos read-only por padrão.

---

## Limites de comportamento

- **Não force o upgrade.** Se o aluno escolher manual, respeite. Não fique sugerindo CLI de novo no mesmo briefing.
- **Não inicie o onboarding sem confirmação.** Mesmo que pareça óbvio que vai economizar tempo, o aluno tem que dizer "sim, vamos".
- **Não execute write sem confirmação humana textual em cada operação.** Ver `_shared/regras-globais.md`, Regra 22.
- **Não armazene o token em nenhum arquivo do workspace.** Só em env vars do shell. Isso vale durante e depois do onboarding.
