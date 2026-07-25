# Atividade: Giro de Estoque e Margem

Cruzar dois números que sozinhos enganam: giro (quão rápido o produto vende) e margem (quanto sobra em cada venda). Um item pode girar rápido e dar pouco lucro, ou girar devagar e ser essencial pra margem. A leitura só fica útil quando os dois são vistos juntos.

## Por que importa pra performance

Dinheiro parado em estoque é dinheiro que a loja não tem em caixa. Quando ninguém mede giro por categoria, o padrão de compra vira reposição no automático, comprando de novo o que sempre foi comprado, sem checar se aquele item ainda merece espaço de prateleira e capital de giro. Cruzar com margem evita o erro oposto: cortar um item de giro baixo que na verdade sustenta boa parte do lucro.

## Como executar

1. Calcular giro por SKU/categoria: quantidade vendida no período dividida pelo estoque médio do mesmo período.
2. Calcular margem bruta (%) e margem bruta absoluta (R$) por SKU/categoria.
3. Montar a matriz giro x margem em 4 quadrantes: alto giro/alta margem (estrela, priorizar), alto giro/baixa margem (produto isca, ver atividade própria), baixo giro/alta margem (manter, é reserva de lucro), baixo giro/baixa margem (candidato a liquidar ou descontinuar).
4. Identificar estoque parado: produto sem saída há mais de 6 meses (ou o período que o cliente definir), com valor financeiro parado a custo.
5. Recomendar ação por quadrante, sem decidir preço ou promoção sozinho, essa decisão é do `@copywriter`/`@gestor-trafego` ou do cliente.

## Cadência recomendada

Mensal, alinhada com o fechamento do ERP do cliente. Estoque parado pode ser revisado a cada 2 meses, o quadro muda pouco em ciclos mais curtos.

## Indicadores de sucesso

- R$ parado em estoque de baixo giro (tendência: caindo mês a mês)
- Giro médio dos itens A da curva ABC
- Nº de itens movidos do quadrante "baixo giro/baixa margem" para liquidação ou descontinuação

## Squad responsável

`@inteligencia-dados` executa e documenta o critério de agrupamento usado. Resultado alimenta `@analista-dados` (KPI de dashboard) e `@copywriter`/`@gestor-trafego` (decisão de ação sobre o estoque parado).

## Operação enxuta

Não é necessário recalcular giro produto a produto toda semana, isso é ruído. O ganho real vem de rodar a matriz uma vez por mês e agir nos poucos itens que mudaram de quadrante, não em recalcular tudo com frequência desnecessária.

## Tarefas desta atividade

1. **Cálculo de giro por SKU/categoria**: quantidade vendida ÷ estoque médio no período.
2. **Cruzamento giro x margem (matriz 2x2)**: classificar cada categoria nos 4 quadrantes e documentar a leitura.
3. **Identificação de estoque parado**: produtos sem saída há mais de 6 meses, com valor financeiro parado a custo.
4. **Recomendação de ação por quadrante**: liquidar, manter, priorizar ou investigar, sem decidir preço final.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `Claude/_squad/_shared/template-tarefa.md`.
