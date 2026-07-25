# Atividade: Curva ABC do Estoque

Classificar cada produto pelo peso real que ele tem no negócio (faturamento e margem), a partir das vendas registradas no ERP, e usar essa classificação como lente para ler o estoque. A curva em si é feita com base nas vendas, nunca na quantidade parada em prateleira. É a base de tudo: sem saber o que é A, B ou C, qualquer decisão de compra, exposição ou campanha vira chute.

## Duas coisas diferentes: curva e leitura de estoque

- **A curva ABC usa vendas, não estoque.** O critério de corte (A ≈80%, B ≈15%, C ≈5%) é sempre sobre faturamento e margem gerados no período, nunca sobre quantidade em estoque. Um item pode ter estoque baixo e ainda ser A (porque vende muito), ou estoque alto e ser C (porque não vende).
- **O estoque é lido depois, à luz da curva.** Uma vez classificados os produtos por venda, aplicamos três leituras sobre o estoque físico de cada um: giro (velocidade com que o produto sai da prateleira), capital parado (R$ imobilizado em produto que não gira) e oportunidade de faturamento (item que vende bem mas está com estoque baixo ou em ruptura, faturamento que a loja está deixando na mesa).

## Por que importa pra performance

Loja de material de construção costuma ter centenas de SKUs, mas uma fração pequena deles concentra a maior parte do faturamento. Sem a curva feita, o dono trata os itens A (os que sustentam o caixa) com a mesma atenção dos itens C (os que ocupam prateleira e capital parado). Isso custa duas coisas ao mesmo tempo: falta do produto que mais vende (ruptura de estoque no item A, oportunidade de faturamento perdida) e capital preso em item que quase não gira (item C parado). A curva ABC corrige as duas em um único diagnóstico.

## Como executar

1. Pedir ao cliente a exportação do relatório de estoque/vendas do ERP (Curva ABC pronta, ou vendas por SKU no período).
2. Se a fonte for PDF do sistema Pontual Tecnologia, rodar antes o `SKILL.md` desta mesma pasta (script `pillar_padroniza_curva_abc.py`) pra converter em XLSX padronizado.
3. `@inteligencia-dados` classifica os produtos em A (≈80% do faturamento), B (≈15%) e C (≈5% restante), usando sempre dado de venda, documentando o critério de corte usado.
4. Cruzar a classificação por faturamento com a classificação por margem bruta, pois nem todo item A em faturamento é A em margem.
5. Sobre essa classificação, ler o estoque físico de cada produto: calcular giro, apontar capital parado (R$ em itens de giro baixo, sobretudo C) e identificar oportunidade de faturamento (itens A ou B com estoque baixo ou em ruptura).
6. Entregar o diagnóstico com a participação de cada categoria de produto (básico, elétrica, hidráulica, pintura, acabamento, ferramentas) na curva.

## Cadência recomendada

Mensal para clientes com movimento intenso; trimestral é o mínimo aceitável para não perder a fotografia do negócio desatualizada. Recalcular sempre que o cliente trouxer um relatório novo, mesmo fora do ciclo.

## Indicadores de sucesso

- % do faturamento concentrado nos itens A (referência de saúde: 70 a 85%)
- Giro médio dos itens A, B e C (referência: giro cai de A pra C; se não cair, o critério de corte está errado)
- R$ de capital parado identificado em itens C
- Nº de itens A ou B com oportunidade de faturamento (estoque baixo ou ruptura) sinalizados pro cliente

## Squad responsável

`@inteligencia-dados` executa. Exige relatório real de ERP anexado, nunca estima número sem fonte (Pilar 1 do Método Viga Mestra).

## Operação enxuta

Uma curva ABC bem feita substitui reunião de "achismo" sobre o que comprar. É a atividade de maior alavancagem do Pilar 1: baixo esforço de execução (um relatório, uma rodada de classificação), alto impacto na decisão de compra e campanha dos meses seguintes.

## Tarefas desta atividade

1. **Padronização do relatório de origem** (quando PDF Pontual): converter pra XLSX antes de qualquer leitura, script determinístico, zero custo de IA na conversão. Ferramenta pronta nesta pasta: `SKILL.md` + `pillar_padroniza_curva_abc.py`.
2. **Classificação ABC por faturamento**: ordenar produtos por receita de venda, aplicar corte 80/15/5, documentar o critério.
3. **Classificação ABC por margem**: repetir o corte usando margem bruta em vez de faturamento, e apontar onde as duas classificações divergem.
4. **Leitura de estoque por giro, capital parado e oportunidade de faturamento**: aplicada sobre a classificação já feita, calcula giro por produto, aponta R$ parado em itens de giro baixo e sinaliza item A/B com risco de ruptura.
5. **Leitura de participação por categoria**: consolidar a curva por categoria de produto, não só por SKU individual, pra virar leitura executiva pro dono da loja.

As tarefas 2 a 5 ainda não têm arquivo `.md` de script pronto. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.
