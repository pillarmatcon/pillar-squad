# Atividade: Giro de Estoque e Margem

Cruzar dois números que sozinhos enganam: giro (quão rápido o produto vende) e margem (quanto sobra em cada venda). Um item pode girar rápido e dar pouco lucro, ou girar devagar e ser essencial pra margem. A leitura só fica útil quando os dois são vistos juntos.

## Por que importa pra performance

Dinheiro parado em estoque é dinheiro que a loja não tem em caixa. Quando ninguém mede giro por categoria, o padrão de compra vira reposição no automático, comprando de novo o que sempre foi comprado, sem checar se aquele item ainda merece espaço de prateleira e capital de giro. Cruzar com margem evita o erro oposto: cortar um item de giro baixo que na verdade sustenta boa parte do lucro.

**Uso direto em decisão de mídia.** Esta atividade não é só leitura financeira, é insumo direto pro `@gestor-trafego`/`@copywriter` decidirem o que anunciar: (1) **risco de ruptura**, item de giro alto com estoque baixo ou caindo não deve entrar em campanha nova sem reforço de compra confirmado, ou tem o orçamento reduzido até repor, anunciar o que vai faltar queima verba e frustra cliente; (2) **giro parado**, item com estoque alto e saída lenta é candidato a virar foco de campanha ou promoção pra desovar, a mídia empurra o que não sai sozinho. As duas leituras dependem de cruzar venda (Curva ABC) com estoque, por isso um input central desta atividade é o "Grupo Z" que já vem dentro do relatório de Curva ABC (SKUs sem venda no período), complementado por snapshot de estoque separado quando o cliente mandar um.

## Como executar

1. Calcular giro por SKU/categoria: quantidade vendida no período dividida pelo estoque médio do mesmo período. Cruza a classificação ABC (vinda de `1 - Curva ABC do Estoque`) com o estoque físico de cada produto.
2. Calcular margem bruta (%) e margem bruta absoluta (R$) por SKU/categoria.
3. Montar a matriz giro x margem em 4 quadrantes: alto giro/alta margem (estrela, priorizar), alto giro/baixa margem (produto isca, ver atividade própria), baixo giro/alta margem (manter, é reserva de lucro), baixo giro/baixa margem (candidato a liquidar ou descontinuar).
4. Identificar estoque parado: produto sem saída há mais de 6 meses (ou o período que o cliente definir), com valor financeiro parado a custo. Usa o "Grupo Z" do relatório de Curva ABC como base, refinado por snapshot de estoque separado quando existir (quantidade e custo mais atuais).
5. Sinalizar risco de ruptura: item A ou B (da curva) com giro alto e estoque baixo ou em queda, pronto pra virar alerta antes de entrar ou continuar em campanha.
6. Sinalizar giro parado como oportunidade de mídia: item de estoque alto e saída lenta, candidato a campanha/promoção de desova, handoff explícito pro `@copywriter`/`@gestor-trafego`.
7. Recomendar ação por quadrante, sem decidir preço ou promoção sozinho, essa decisão é do `@copywriter`/`@gestor-trafego` ou do cliente.

## Cadência recomendada

Mensal, alinhada com o fechamento do ERP do cliente. Estoque parado pode ser revisado a cada 2 meses, o quadro muda pouco em ciclos mais curtos.

## Indicadores de sucesso

- R$ parado em estoque de baixo giro (tendência: caindo mês a mês)
- Giro médio dos itens A da curva ABC
- Nº de itens movidos do quadrante "baixo giro/baixa margem" para liquidação ou descontinuação
- Nº de itens A/B sinalizados com risco de ruptura antes de entrar em campanha (referência: zero campanha nova rodando sobre item sem esse checklist)
- Nº de itens de giro parado que viraram campanha/promoção de desova

## Squad responsável

`@inteligencia-dados` executa e documenta o critério de agrupamento usado. Resultado alimenta `@analista-dados` (KPI de dashboard) e `@copywriter`/`@gestor-trafego` (decisão de que anunciar, risco de ruptura antes de subir campanha e giro parado como foco de promoção).

## Operação enxuta

Não é necessário recalcular giro produto a produto toda semana, isso é ruído. O ganho real vem de rodar a matriz uma vez por mês e agir nos poucos itens que mudaram de quadrante, não em recalcular tudo com frequência desnecessária.

## Tarefas desta atividade

1. **Cálculo de giro por SKU/categoria**: quantidade vendida ÷ estoque médio no período.
2. **Cruzamento giro x margem (matriz 2x2)**: classificar cada categoria nos 4 quadrantes e documentar a leitura.
3. **Identificação de estoque parado**: produtos sem saída há mais de 6 meses, com valor financeiro parado a custo, usando o Grupo Z da Curva ABC como base.
4. **Sinalização de risco de ruptura**: itens A/B com giro alto e estoque baixo/caindo, handoff pro `@gestor-trafego`/`@copywriter` antes de subir ou manter campanha.
5. **Sinalização de giro parado como oportunidade de mídia**: itens de estoque alto e saída lenta, handoff pro `@copywriter`/`@gestor-trafego` como candidato a campanha de desova.
6. **Recomendação de ação por quadrante**: liquidar, manter, priorizar ou investigar, sem decidir preço final.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.
