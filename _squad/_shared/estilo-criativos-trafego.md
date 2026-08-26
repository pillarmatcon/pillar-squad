# Guia de Estilo: Criativos de Tráfego Pago Pillar

Referência visual pra gerar criativos de aquisição de cliente da própria Pillar (peças que miram dono de loja de MatCon, formato Story/Post) em qualquer ferramenta: Ad Creative AI, Midjourney, Canva, DALL-E, etc. Objetivo é manter o mesmo estilo entre criativos diferentes, sem redescrever do zero em cada geração.

Não confundir com identidade de cliente: essas peças carregam a marca da Pillar (`_shared/identidade-agencia.md`), não a do cliente final. Pra criativo de campanha de um cliente real (ex: Construmais), a marca usada é a do cliente, não este guia.

## Padrão identificado (baseado nas peças que já performaram)

- **Logo Pillar** sempre visível, canto superior (esquerdo ou direito), nunca escondido atrás de elemento.
- **Fundo:** foto realista de ambiente de loja de material de construção (corredor, prateleira, balcão de atendimento, sacaria empilhada, pátio) ou fundo sólido azul-marinho liso. Nunca ilustração, nunca stock genérico fora do nicho.
- **Headline:** grande, caixa alta, negrito, topo da peça. Sobre foto, sempre com fundo sólido semi-opaco atrás do texto (garante contraste e legibilidade em qualquer parte da imagem).
- **Hierarquia de texto:** headline de impacto → subtítulo/benefício (1 a 2 linhas) → menção ao Método Viga Mestra (opcional, reforça autoridade) → CTA.
- **CTA:** texto "CLIQUE EM SAIBA MAIS" em negrito solto no layout, ou botão pill (cantos arredondados) laranja sólido com "Saiba mais". Nunca os dois ao mesmo tempo na mesma peça.
- **Paleta:** laranja `#f97316` como cor de destaque e ação, azul-marinho `#0f172a` como base séria/profissional, branco `#f8fafc` para contraste e respiro. Cinza-ardósia `#64748b` só em elemento de apoio, nunca em texto principal.
- **Tipografia:** sans-serif bold (Barlow) é o padrão. Uma variação serifada apareceu numa peça isolada (efeito "editorial/premium") — usar como exceção pontual, não como novo padrão, a menos que o usuário peça explicitamente.
- **Prova social / autoridade:** ícones de Google Ads e Meta Ads quando o ângulo da peça é sobre tráfego pago em si. Lista de benefícios com check mark laranja quando o ângulo é resultado (giro de estoque, ticket médio, blindagem de orçamento).

## Prompt-base reutilizável

Cole isto como ponto de partida em qualquer ferramenta de geração, antes da instrução específica de cada peça:

```
Estilo visual Pillar (agência de marketing para lojas de material de construção):
- Formato: Story vertical 1080x1920 ou Post 1080x1350
- Fundo: foto realista de loja de material de construção (corredor, prateleira, balcão de atendimento, sacaria de cimento) OU fundo sólido azul-marinho #0f172a
- Logo "Pillar" em laranja, canto superior da peça
- Headline grande, caixa alta, negrito, com fundo sólido semi-opaco atrás quando sobreposta a foto, pra garantir contraste
- Hierarquia: headline de impacto no topo, subtítulo de benefício logo abaixo, CTA no terço inferior
- Paleta: laranja #f97316 (destaque e ação), azul-marinho #0f172a (base/texto), branco #f8fafc (contraste)
- Tipografia sans-serif bold (Barlow)
- CTA: "CLIQUE EM SAIBA MAIS" em negrito OU botão pill laranja "Saiba mais" (nunca os dois juntos)
- Tom visual: sóbrio e profissional, com o laranja trazendo energia pontual. Sem cara de estoque genérico, sem clichê de agência.
```

Depois desse bloco, entra a instrução específica: o ângulo da peça (ex: "foco em blindar orçamento contra concorrência", "foco em treinar equipe como consultora de obra"), a headline e os bullets (sempre vindos do `copywriter`, ver `_squad/03-designer/SKILL.md`).

## Como usar por ferramenta

- **Ad Creative AI (ou similar com upload de referência):** anexar 1 a 2 peças anteriores como referência de estilo, colar o prompt-base acima como instrução de composição, e só depois descrever o ângulo/copy da peça nova.
- **Ferramentas só de texto (Midjourney, DALL-E):** o prompt-base já cobre o que uma referência de imagem faria. Ajustar a descrição do fundo pro cenário específico da peça (ex: "balcão com cliente sendo atendido" vs "prateleira de ferramentas").
- **Canva ou edição manual:** usar o prompt-base como checklist de composição em vez de prompt de IA.

## Quando propor atualizar este guia

Se uma peça nova estabelecer um padrão visual diferente do descrito aqui (nova paleta, nova composição, novo elemento recorrente) e performar bem, propor atualização deste arquivo antes de reutilizar o padrão novo em outra peça, pra manter o guia como fonte única da verdade.
