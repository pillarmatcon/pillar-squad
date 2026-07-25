# Guia de Hospedagem

> **Para quem é:** você, quando precisa subir uma landing page de cliente e ainda não tem hospedagem própria. Esse guia mostra o caminho mais simples, mais barato e mais rápido.
> **Quem usa:** os agentes 04-Páginas e 03-Design/Criativos recomendam essa rota como padrão.

---

## Resposta direta

**Cloudflare Pages.** Gratuito, sem cartão, drag-and-drop, sai no ar em 60 segundos. URL pública grátis (`nome-do-projeto.pages.dev`). Permite domínio próprio depois sem custo de hospedagem.

Se você seguir esse guia, em 15 minutos a LP do cliente está no ar com URL pública e SSL automático. Sem servidor, sem mensalidade.

---

## Comparativo das opções gratuitas

| Plataforma | Setup inicial | Domínio grátis | Domínio próprio | SSL | Edge global | Limite gratuito | Recomendação |
|---|---|---|---|---|---|---|---|
| **Cloudflare Pages** | 2 min | `*.pages.dev` | Grátis (DNS Cloudflare) | Automático | Sim, 250+ cidades | 500 builds/mês, banda ilimitada | **Padrão recomendado** |
| Vercel | 3 min | `*.vercel.app` | Grátis | Automático | Sim | 100GB banda/mês | Bom alternativo |
| Netlify | 3 min | `*.netlify.app` | Grátis | Automático | Sim | 100GB banda/mês | Bom alternativo |
| GitHub Pages | 5 min (precisa conta GitHub) | `*.github.io` | Grátis | Automático | Sim (CDN básico) | 100GB banda/mês | Bom para quem já usa GitHub |
| Hospedagem cPanel/FTP | Variável | Não | Sim (custo do registrador) | Manual | Não | Conforme plano | Só se cliente já tem |

**Razão de Cloudflare Pages ser #1:** banda ilimitada no plano gratuito (Vercel e Netlify cobram acima de 100GB), edge global mais amplo, integração nativa com domínio Cloudflare.

---

## Passo a passo: subir LP do cliente em Cloudflare Pages

### O que você precisa antes de começar

- Arquivo HTML produzido pelo agente 04-Páginas (.html único)
- Imagens da página (logo, hero, depoimentos), todas em uma pasta
- Conta Google ou GitHub (para criar conta Cloudflare em 30 segundos)

### Passos

**1. Criar conta no Cloudflare (1 minuto)**

- Acessar [cloudflare.com](https://cloudflare.com)
- Clicar em "Sign Up", usar seu email
- Confirmar email
- Não precisa cartão de crédito

**2. Criar projeto Pages (2 minutos)**

- No painel Cloudflare, menu lateral: "Workers & Pages"
- Botão "Create application"
- Aba "Pages"
- Botão "Upload assets"
- Nome do projeto: `nome-do-cliente-lp` (ex: `construmais-lp`)
- Botão "Create project"

**3. Upload dos arquivos (1 minuto)**

- Arrastar a pasta inteira (HTML + imagens + favicon) para a área de upload
- Aguardar upload completar (5 a 30 segundos dependendo do tamanho)
- Botão "Deploy site"

**4. Pronto. URL pública criada**

- Cloudflare gera URL automática: `https://construmais-lp.pages.dev`
- Abrir essa URL no navegador, verificar que a página carregou
- SSL automático já ativo
- Edge global já ativo (página rápida em qualquer parte do mundo)

### Tempo total: 4 a 6 minutos do zero ao ar

---

## Conectar domínio próprio (opcional, mas recomendado)

A URL `*.pages.dev` funciona, mas converte menos do que domínio próprio. Cliente paga R$ 40/ano por um `.com.br` e isso vale.

### Se o cliente já tem domínio

**1. No Cloudflare Pages, ir no projeto criado**
- Aba "Custom domains"
- "Set up a custom domain"
- Digitar o domínio: `lp.cliente.com.br` ou `cliente.com.br`

**2. Cloudflare mostra o registro DNS necessário**
- Geralmente um CNAME apontando para `nome-projeto.pages.dev`
- Ou um A record + AAAA record

**3. No painel do domínio do cliente (Registro.br, GoDaddy, etc), criar o registro DNS**
- Tipo: CNAME
- Nome: `lp` (subdomínio) ou `@` (domínio raiz)
- Valor: o que Cloudflare informou
- TTL: automático ou 3600

**4. Aguardar propagação DNS**
- Geralmente em 5 a 30 minutos
- Pode levar até 24h em casos raros
- Cloudflare valida e ativa SSL automaticamente

### Se o cliente não tem domínio

Comprar é simples e barato:

**Para domínios .com.br (recomendado para negócio brasileiro):**
- Acessar [registro.br](https://registro.br)
- Pesquisar disponibilidade
- Custo: ~R$ 40/ano
- Pagamento: boleto ou cartão
- Liberação: imediata após pagamento (boleto leva 1-2 dias)

**Para domínios .com (recomendado se vai vender pra fora do Brasil):**
- Cloudflare Registrar (mais barato, ~US$ 10/ano)
- Ou NameCheap (~US$ 12/ano)
- Ou Registro.br também tem .com (mais caro)

**Dica do guia:** se você tem vários clientes, considerar transferir todos os domínios para Cloudflare Registrar (preço de custo, sem markup) e gerenciar tudo num painel só.

---

## Alternativas se Cloudflare Pages não couber

### Vercel
**Quando preferir:** se você já usa Next.js ou Vue em outros projetos. Vercel é mais integrado com esses frameworks.

**Setup:** mesmo princípio. Conta gratuita, drag-and-drop em [vercel.com/new](https://vercel.com/new), URL `*.vercel.app`, conexão com domínio próprio em 3 cliques.

**Limite:** 100GB banda/mês. Para LP de tráfego pago, geralmente não chega.

### Netlify
**Quando preferir:** se você gosta de UI mais "marketing-friendly" (alguns acham mais bonito).

**Setup:** [netlify.com](https://netlify.com), drag-and-drop em [app.netlify.com/drop](https://app.netlify.com/drop), URL `*.netlify.app`.

**Limite:** 100GB banda/mês.

### GitHub Pages
**Quando preferir:** se você já tem GitHub ativo e quer versionar a LP em git desde o começo.

**Setup:** criar repo público, fazer push do HTML, ativar Pages nas Settings, URL `usuario.github.io/repo`.

**Limite:** 100GB banda/mês, 1GB de armazenamento.

**Atenção:** o repositório precisa ser **público** no plano gratuito (privado requer GitHub Pro). Se a LP tem dado sensível na URL ou no código, prefira Cloudflare Pages.

---

## Plataformas que NÃO recomendo

### WordPress (com hospedagem própria)
**Por que não:** custa entre R$ 10 e R$ 50/mês. Lento sem otimização. Atualização constante de plugin/tema. Vulnerabilidade de segurança comum. Não vale o trabalho pra hospedar 1 LP.

**Quando faz sentido:** site institucional do cliente com 10+ páginas, blog ativo, e-commerce com plugin específico.

### Wix, Squarespace, Webflow Free
**Por que não:** plano gratuito mostra branding deles na página (mata credibilidade). Plano pago custa US$ 12-30/mês. Limitação séria de customização técnica (CSS, JS). Performance pior que HTML puro hospedado em Cloudflare.

**Quando faz sentido:** cliente exige editar sozinho sem mexer em código.

### Hostgator, GoDaddy Hosting, Locaweb (hospedagem compartilhada brasileira)
**Por que não:** cobram R$ 10 a R$ 30/mês. Performance ruim (servidor compartilhado lento). cPanel desnecessário pra LP. SSL manual. Backup manual.

**Quando faz sentido:** cliente já tem essa hospedagem e quer aproveitar (não vale migrar só pra LP, mas se já tem, usa).

### LeadLovers, Klickpages, GreatPages, Builderall (plataformas de "leads")
**Por que não:** custam R$ 100 a R$ 500/mês. Travam você na ferramenta (LP fica lá, se cancela, perde). Performance ruim (LP renderizada via builder próprio). Limitação séria de customização.

**Quando faz sentido:** se você já paga por uma dessas pra outras funções (envio de email, CRM) e quer hospedar a LP no mesmo lugar pra simplificar. Mesmo assim, geralmente é mais barato manter o builder pra email/CRM e a LP em Cloudflare Pages.

---

## Custo total recomendado para subir LP de cliente

**Setup mínimo (recomendado):**
- Hospedagem (Cloudflare Pages): R$ 0
- Domínio (.com.br, opcional mas recomendado): R$ 40/ano
- SSL: R$ 0 (incluído)
- CDN/edge: R$ 0 (incluído)

**Total:** R$ 40/ano por cliente, ou R$ 0 se usar URL `*.pages.dev`.

Para comparar: hospedagem WordPress + domínio + plugin de cache + SSL premium custaria R$ 60 a R$ 100/mês. Cloudflare Pages dá o mesmo resultado por 1/30 do preço.

---

## Como o agente apresenta isso pra você

Os agentes 04-Páginas e 03-Design/Criativos, ao entregar uma página/criativo, sempre incluem:

> **Hospedagem recomendada:** Cloudflare Pages (gratuita).
> 1. Criar conta em [cloudflare.com](https://cloudflare.com), 30 segundos
> 2. Workers & Pages → Create application → Pages → Upload assets
> 3. Arrastar a pasta com seu HTML + imagens
> 4. Sua LP fica no ar em 60 segundos com URL `*.pages.dev`
> 5. Para domínio próprio: aba Custom Domains → seguir instruções de DNS
>
> Guia completo em `_shared/hospedagem-guia.md` no projeto.

E sinaliza pendência: confirmar com o cliente se o domínio dele já está no Cloudflare (DNS) ou em outro registrar.

---

## Casos especiais

### Cliente exige hospedagem própria dele (cPanel, GoDaddy, Locaweb)

Você faz upload do HTML via FTP no diretório `public_html` ou `www`. Se já tem SSL, ok. Se não tem, instalar Let's Encrypt grátis pelo cPanel (botão "Vamos criptografar" ou similar).

### Cliente usa Go High Level (GHL) e quer hospedar lá

Possível, mas com limitações. O agente 04-Páginas tem nota específica sobre GHL: o HTML precisa ser inserido como "Custom Code" no GHL builder, com ajuste fino de CSS reset. Performance é pior que Cloudflare Pages, mas integração com CRM do GHL fica mais simples.

### LP precisa de backend (gravar dados, processar pagamento, autenticação)

Cloudflare Pages cobre o frontend. Backend usa:
- Cloudflare Workers (gratuito até 100k requests/dia)
- Formspree/FormSubmit (gratuito até 50 submissions/mês)
- Hotmart/Kiwify (checkout completo gratuito)
- Zapier/Make webhook (gratuito até 100 tasks/mês)

Para LP de captura simples, Formspree ou webhook do CRM do cliente já resolvem.

---

## Resumo executivo (3 linhas)

1. **Default:** Cloudflare Pages, gratuito, drag-and-drop, no ar em 60s
2. **Domínio próprio:** Registro.br para `.com.br` (R$ 40/ano), Cloudflare Registrar para `.com`
3. **Não usar:** Wix, Squarespace, hospedagem WordPress só pra LP, plataformas tipo LeadLovers só pra hospedar
