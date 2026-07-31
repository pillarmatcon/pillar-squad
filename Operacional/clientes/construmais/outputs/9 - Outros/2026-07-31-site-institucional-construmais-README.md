# Site institucional Construmais (single-page) — README de entrega

**Briefing usado:** pedido direto no chat, 2026-07-31. Objetivo era reconstruir, em HTML puro editável, a estrutura de seções de uma página hoje publicada em `https://pillar.pages.net.br/construmais` (GreatPages), cujo conteúdo é 100% placeholder genérico de marcenaria/madeira, sem relação com a Construmais. Confirmado com o usuário que o pedido é reaproveitar só o **esqueleto de seções**, preenchido com dado real da Construmais (`Operacional/clientes/construmais/CLIENTE.md`).

**Arquivos desta entrega:**
```
outputs/9 - Outros/2026-07-31-site-institucional-construmais.html   (o site)
outputs/9 - Outros/2026-07-31-site-institucional-construmais-README.md   (este arquivo)
outputs/9 - Outros/assets/logo-construmais.png       (logo real, cópia integral)
outputs/9 - Outros/assets/logo-construmais.webp      (logo, versão otimizada 800x450 usada no hero)
outputs/9 - Outros/assets/mascote-construmais.png    (mascote real, cópia integral)
outputs/9 - Outros/assets/mascote-construmais.webp   (mascote, versão otimizada 900x1593 usada na seção Sobre)
outputs/9 - Outros/assets/og-image-construmais.png   (imagem 1200x630 gerada a partir do logo real, para Open Graph)
```
O HTML é autocontido (CSS inline no `<head>`, JS vanilla no rodapé) e só depende da pasta `assets/` ao lado dele. Abra o `.html` direto no navegador para conferir.

---

## O que está pronto

- **Estrutura completa das 7 seções pedidas:** nav fixo (Início, Departamentos, Sobre, Depoimentos, Atendimento + botão "Solicitar Orçamento"), hero com selo "CONSTRUMAIS • DESDE 2011" e CTA "ORÇAMENTO ➝" pro WhatsApp, 4 cards de Departamentos (Material Básico em destaque + Elétrica, Hidráulica, Tintas e Acabamento), seção Sobre com o diferencial real (sacaria própria de 20kg + sistema tintométrico de 5.000 cores) e os 2 números reais (+15 anos, nota 4,6/108 avaliações), seção de Depoimentos com as 3 avaliações reais do Google, seção de Atendimento com CTA final, e rodapé completo (navegação, contato, endereço, horário, redes sociais, links legais).
- **100% dado real, zero placeholder genérico de marcenaria.** Todo texto vem do briefing e do `CLIENTE.md`.
- **Identidade visual real aplicada:** paleta exata (`#EE2526` vermelho, `#F4D000` amarelo, laranja só como acento, nunca dominante), logo e mascote reais da Construmais (arquivos copiados para `assets/`, não linkam o caminho original do workspace), wordmark aproximado em Poppins ExtraBold itálico leve.
- **Sem foto de fachada/produto/interior inventada.** Onde não existe banco de fotos real, usei o logo, o mascote e ícones SVG curados à mão (nenhum emoji).
- **Mobile-first, acessível:** navegação funciona mesmo com JavaScript desativado (menu aparece empilhado por padrão; o hambúrguer só assume o controle quando o JS carrega), skip link pro conteúdo, hierarquia `h1` único → `h2` por seção → `h3` nos cards, contraste checado manualmente em cada combinação de cor de texto/fundo da paleta (o vermelho puro da marca só carrega texto grande/negrito ou fica em botão com cor de fundo diferente, exatamente pra passar no WCAG AA em qualquer tamanho de fonte).
- **Imagens otimizadas:** logo e mascote convertidos e redimensionados para WebP (de 450KB/1,17MB para 17KB/110KB), com `width`/`height` corretos (evita layout shift) e `loading="lazy"` no mascote (abaixo da dobra).
- **SEO + Open Graph + Twitter Card + Schema.org completos**, usando `HardwareStore` (tipo do schema.org específico pra loja de material de construção, mais preciso que o `LocalBusiness` genérico), com endereço, horário, telefone e a nota real do Google (4,6/108) embutidos no JSON-LD.
- **Meta Pixel + GA4 instalados** com placeholder (`META_PIXEL_ID_AQUI`, `GA4_ID_AQUI`), incluindo evento de clique (`Contact` / `generate_lead`) nos 3 botões de WhatsApp/orçamento da página.
- **Compliance aplicado:** nenhuma menção a frete grátis, desconto, parcelamento ou prazo de entrega (o cliente relatou frete cobrado como ponto de atrito, não cortesia, e nenhuma dessas condições é política confirmada).
- **Humanizer aplicado** em todo o texto (headline, sobre, depoimentos, CTAs, rodapé). Ver assinatura no fim deste README.

## O que precisa ser trocado antes de subir

1. **Pixel Meta ID e GA4 ID.** Hoje `META_PIXEL_ID_AQUI` e `GA4_ID_AQUI` no HTML (linhas perto do fim do arquivo). Ambos aparecem como `[PREENCHER]` no `CLIENTE.md`, seção Tracking. Sem isso, a página carrega normalmente mas não manda dado nenhum pro Meta Ads nem pro Google Analytics.
2. **Confirmar domínio de publicação.** O `canonical`, `og:url` e o schema.org apontam pra `construmaisjp.com.br`, que é o domínio já registrado no `CLIENTE.md`. **Atenção:** esse domínio hoje hospeda o site institucional feito pela Anova Agência (já existe, com fachada, foto do Tony e galeria real). Confirme com o Tony antes de publicar este arquivo por cima do site atual, pra não perder o que já está no ar sem necessidade.
3. **Páginas de Política de Privacidade, Termos de Uso e Cookies.** O rodapé já linka pra `/politica-de-privacidade`, `/termos-de-uso` e `/cookies`, mas essas páginas ainda não existem (a loja não tem esse conteúdo hoje). Não inventei texto de política nenhum, só deixei o link apontado pra onde a página deveria morar quando for criada.
4. **Favicon.** Hoje usa o `logo-construmais.png` inteiro (retangular, fundo vermelho) como ícone de aba, o que funciona mas não é ideal (o ícone vai aparecer meio "espremido" numa aba de navegador). Recomendo gerar um favicon quadrado (recorte só do "C" da casinha do logo) quando tiver tempo de design disponível.

## Pendências que ficam registradas, mas não bloqueiam a entrega

- Meta description ficou com ~170 caracteres (levemente acima do ideal de 150-160). Não é erro, só um ajuste fino de SEO pra uma próxima rodada.
- `og:image` aponta pra `https://construmaisjp.com.br/assets/og-image-construmais.png`: a imagem já existe e está na pasta `assets/`, mas só vai aparecer corretamente em preview de link (WhatsApp, Instagram, etc.) depois que o arquivo estiver hospedado nesse caminho exato.
- Página não tem formulário de captura (só CTA de WhatsApp/telefone), porque a estrutura pedida foi a de site institucional, não a de landing page de captura. Se quiser um formulário embutido além do WhatsApp, é um pedido separado.
- Sem foto real de fachada, interior ou produto da loja (não existe banco de fotos no workspace ainda, confirmado no `CLIENTE.md`, seção Presença Digital). Quando o Tony enviar o acervo, dá pra substituir o mascote/logo por foto real em pontos estratégicos (hero, seção Sobre).

## Próximos passos

1. Confirmar com o Tony se este arquivo substitui o site atual em `construmaisjp.com.br` ou se fica em outro subdomínio/URL por enquanto.
2. Preencher Pixel Meta ID e GA4 ID assim que existirem (ver `CLIENTE.md`).
3. Publicar em hospedagem estática (recomendação abaixo).
4. Validar o texto final com o Tony antes de publicar (headline, sobre, depoimentos), já que o dado é real mas a redação é da Pillar.

## Hospedagem recomendada

**Cloudflare Pages**, gratuita, sem cartão, arrastar e soltar, no ar em 60 segundos.
1. Criar conta em [cloudflare.com](https://cloudflare.com)
2. Workers & Pages → Create application → Pages → Upload assets
3. Arrastar a pasta `9 - Outros` inteira (o `.html` e a subpasta `assets/` juntos, mantendo a estrutura)
4. O site fica no ar com URL `*.pages.dev`
5. Pra domínio próprio (`construmaisjp.com.br`): aba Custom Domains, seguir instruções de DNS

Guia completo em `_squad/_shared/hospedagem-guia.md`. Custo esperado: R$ 0 (URL `*.pages.dev`) ou já coberto, já que o domínio `construmaisjp.com.br` já existe.

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
