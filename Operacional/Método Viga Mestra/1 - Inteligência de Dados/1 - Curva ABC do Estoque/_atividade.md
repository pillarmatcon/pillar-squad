# Atividade: Curva ABC do Estoque

Classificar cada produto do estoque pelo peso real que ele tem no negócio (faturamento e margem), a partir do relatório de ERP que o cliente exporta. É a base de tudo: sem saber o que é A, B ou C, qualquer decisão de compra, exposição ou campanha vira chute.

## Por que importa pra performance

Loja de material de construção costuma ter centenas de SKUs, mas uma fração pequena deles concentra a maior parte do faturamento. Sem a curva feita, o dono trata os itens A (os que sustentam o caixa) com a mesma atenção dos itens C (os que ocupam prateleira e capital parado). Isso custa duas coisas ao mesmo tempo: falta do produto que mais vende (ruptura de estoque no item A) e capital preso em item que quase não gira (item C parado). A curva ABC corrige as duas em um único diagnóstico.

## Como executar

1. Pedir ao cliente a exportação do relatório de estoque/vendas do ERP (Curva ABC pronta, ou vendas por SKU no período).
2. Se a fonte for PDF do sistema Pontual Tecnologia, rodar antes o `SKILL.md` desta mesma pasta (script `pillar_padroniza_curva_abc.py`) pra converter em XLSX padronizado.
3. `@inteligencia-dados` classifica os produtos em A (≈80% do faturamento), B (≈15%) e C (≈5% restante), documentando o critério de corte usado.
4. Cruzar a classificação por faturamento com a classificação por margem bruta, pois nem todo item A em faturamento é A em margem.
5. Entregar o diagnóstico com a participação de cada categoria de produto (básico, elétrica, hidráulica, pintura, acabamento, ferramentas) na curva.

## Cadência recomendada

Mensal para clientes com movimento intenso; trimestral é o mínimo aceitável para não perder a fotografia do negócio desatualizada. Recalcular sempre que o cliente trouxer um relatório novo, mesmo fora do ciclo.

## Indicadores de sucesso

- % do faturamento concentrado nos itens A (referência de saúde: 70 a 85%)
- Nº de itens A sem ruptura de estoque no período
- R$ parado em itens C identificados

## Squad responsável

`@inteligencia-dados` executa. Exige relatório real de ERP anexado, nunca estima número sem fonte (Pilar 1 do Método Viga Mestra).

## Operação enxuta

Uma curva ABC bem feita substitui reunião de "achismo" sobre o que comprar. É a atividade de maior alavancagem do Pilar 1: baixo esforço de execução (um relatório, uma rodada de classificação), alto impacto na decisão de compra e campanha dos meses seguintes.

## Tarefas desta atividade

1. **Padronização do relatório de origem** (quando PDF Pontual): converter pra XLSX antes de qualquer leitura, script determinístico, zero custo de IA na conversão. Ferramenta pronta nesta pasta: `SKILL.md` + `pillar_padroniza_curva_abc.py`.
2. **Classificação ABC por faturamento**: ordenar produtos por receita, aplicar corte 80/15/5, documentar o critério.
3. **Classificação ABC por margem**: repetir o corte usando margem bruta em vez de faturamento, e apontar onde as duas classificações divergem.
4. **Leitura de participação por categoria**: consolidar a curva por categoria de produto, não só por SKU individual, pra virar leitura executiva pro dono da loja.

As tarefas 2 a 4 ainda não têm arquivo `.md` de script pronto. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.
