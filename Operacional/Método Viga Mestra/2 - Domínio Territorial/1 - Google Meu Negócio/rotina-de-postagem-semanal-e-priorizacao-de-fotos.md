## 1. Cadência de postagem

1 post nativo por semana no perfil (Novidade ou Produto), alternando produto de giro alto com dica prática de obra. O Google prioriza perfil ativo no algoritmo de busca local, perfil parado perde posição mesmo com nota alta.

**Tipos de post disponíveis no Google Business Profile:**
- **Novidade:** informativo, sem data de validade, uso mais livre.
- **Produto:** ficha de produto com nome, foto, preço opcional, descrição curta. É o tipo que mais aproveita o banco de fotos priorizado na seção 3.
- **Oferta:** exige data de início/fim e condição real e vigente. Só usar se a promoção for política confirmada da loja, nunca com preço ou prazo supostos.
- **Evento:** data específica (ex: aniversário da loja, feira, mutirão).

---

## 2. Repositório de fotos e agendamento manual (operação enxuta)

**Situação real hoje:** o Google Business Profile não tem um recurso nativo de "agendar post pra data futura" no fluxo padrão de conta gratuita. Toda publicação de post/foto é imediata no momento em que alguém do time sobe o conteúdo. Por isso, "publicar 8 fotos ao longo de 8 semanas" na prática vira uma fila manual com lembrete, não uma automação de fato, a menos que se pague uma ferramenta terceira (ver seção 4).

**Como organizar a fila, dado um repositório de N fotos:**
1. Cada foto do repositório recebe um número de ordem de publicação, definido pela priorização da seção 3 (nunca pela ordem em que a foto chegou na pasta).
2. Uma planilha ou lista de controle registra: nº da semana, nome do arquivo, produto/tema, status (pendente / publicada), data de publicação.
3. Toda semana (mesma rotina que já cobre resposta de avaliação), o responsável pega a próxima foto pendente da fila, sobe como post de Produto ou Novidade, marca como publicada.
4. Quando o repositório de N fotos acaba, reponhe com fotos novas seguindo o mesmo critério de prioridade, não deixa a fila zerar sem próximo lote definido.

**Por que não construir automação via API agora:** o Google restringe o acesso de escrita da Business Profile API (posts, fotos) a parceiros aprovados via processo de solicitação, não é self-service. Pra uma agência do porte da Pillar, atendendo o volume de clientes de hoje, o custo de aprovação, manutenção e risco de a API mudar não se paga frente a uma tarefa de poucos minutos por semana. Reavaliar isso só se o número de clientes que exigem essa rotina crescer o suficiente pra justificar o investimento.

---

## 3. Priorização de fotos e produtos (ligação com Curva ABC)

Ordem de prioridade pra decidir qual foto/produto entra na fila antes do outro, do mais forte pro mais fraco:

1. **Produto que o cliente pediu explicitamente pra divulgar mais** (ex: uma linha de alto ticket que o dono quer posicionar, tipo um sistema de mistura de tinta personalizada). Entra na fila mesmo que o giro ainda não seja alto, porque é decisão comercial do cliente, não só dado de estoque. Alternar com os itens abaixo, não ocupar todas as semanas só com esse produto.
2. **Produtos Classe A da Curva ABC** (maior faturamento), especialmente os de maior giro dentro da Classe A. São o que mais sustenta a loja e o que mais gente já procura por nome.
3. **Produtos de maior margem** dentro das classes A/B, quando não coincidirem com os do item 2. Puxa produto rentável pra visibilidade, não só volume.
4. **Produtos "isca"** identificados no diagnóstico de estoque (Pilar 1, Inteligência de Dados). Item de giro alto e ticket baixo que atrai fluxo de gente pra loja, mesmo sem ser o de maior margem.
5. **Institucional/reforço de marca** (fachada, equipe, tempo de mercado, bastidor da loja), pra intercalar entre os posts de produto e não deixar o perfil parecer catálogo puro.

**Fonte do dado:** diagnóstico de estoque e Curva ABC do cliente (`outputs/1 - Inteligência de Dados/1 - Curva ABC do Estoque/diagnostico-estoque.md` ou equivalente). Nunca estimar giro, faturamento ou margem de cabeça, sempre puxar do diagnóstico real mais recente daquele cliente.

**Regra de mistura:** numa fila de 8 fotos, por exemplo, uma distribuição saudável é algo como 2 produtos pedidos pelo cliente, 3 Classe A/giro alto, 1 de margem, 1 isca, 1 institucional. Ajustar a proporção conforme o que o diagnóstico de estoque daquele cliente específico mostrar como prioridade real.

---

## 4. Se o cliente ou a agência quiser automação de verdade (upsell futuro, não operação padrão)

Existem ferramentas terceiras de agendamento de redes sociais que já têm parceria aprovada com o Google e permitem programar post/foto do Business Profile com data futura pelo próprio painel delas (categoria de produto: social media schedulers com suporte a Google Business Profile). Antes de recomendar uma ferramenta específica a um cliente, confirmar preço, limites de conta e recursos atuais direto no site do fornecedor, porque essas ferramentas mudam plano e funcionalidade com frequência e não há dado confiável fixo pra citar aqui. Tratar como upsell de operação a ser avaliado caso a caso, não como parte do serviço padrão da Pillar hoje.

---

## Boas práticas gerais (valem pra rotina inteira)

- Nunca subir foto de banco de imagem no lugar de foto real do produto/loja, isso já é regra do checklist de otimização (`checklist-otimizacao-de-perfil.md`).
- Post de Oferta exige condição real e vigente, nunca preço ou prazo suposto.
- Se a fila de fotos ficar sem próximo item definido, isso é sinal de alerta pra pedir mais fotos ao cliente antes que a rotina semanal quebre por falta de material.
