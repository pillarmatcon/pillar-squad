# Atividade: Curva ABC do Estoque

Classificar cada produto pelo peso real que ele tem no negócio (faturamento e margem), a partir das vendas registradas no ERP, e usar essa classificação como lente para ler o estoque. A curva em si é feita com base nas vendas, nunca na quantidade parada em prateleira. É a base de tudo: sem saber o que é A, B ou C, qualquer decisão de compra, exposição ou campanha vira chute.

## Duas coisas diferentes: curva e leitura de estoque

- **A curva ABC usa vendas, não estoque.** O critério de corte (A ≈80%, B ≈15%, C ≈5%) é sempre sobre faturamento e margem gerados no período, nunca sobre quantidade em estoque. Um item pode ter estoque baixo e ainda ser A (porque vende muito), ou estoque alto e ser C (porque não vende).
- **O estoque é lido depois, à luz da curva, mas em atividade própria.** Uma vez classificados os produtos por venda, giro, capital parado e risco de ruptura são calculados na atividade `2 - Giro de Estoque e Margem`, nunca aqui. Esta atividade entrega o "o que vende e quanto vale"; a leitura de estoque em cima disso é sempre da atividade seguinte.
- **O relatório de Curva ABC já traz o "Grupo Z"** (ou nomenclatura equivalente do ERP do cliente): os SKUs sem nenhuma venda no período coberto. É matéria-prima pra giro parado e estoque parado, mas essa leitura em si é documentada em `2 - Giro de Estoque e Margem/`, não no diagnóstico desta atividade. Só cito a origem (relatório, período, Grupo Z) quando a atividade 2 usar esse dado.

## Por que importa pra performance

Loja de material de construção costuma ter centenas de SKUs, mas uma fração pequena deles concentra a maior parte do faturamento. Sem a curva feita, o dono trata os itens A (os que sustentam o caixa) com a mesma atenção dos itens C (os que ocupam prateleira e capital parado). Isso custa duas coisas ao mesmo tempo: falta do produto que mais vende (ruptura de estoque no item A, oportunidade de faturamento perdida) e capital preso em item que quase não gira (item C parado). A curva ABC corrige as duas em um único diagnóstico.

## Como executar

1. Pedir ao cliente a exportação do relatório de estoque/vendas do ERP (Curva ABC pronta, ou vendas por SKU no período).
2. Se a fonte for PDF do sistema Pontual Tecnologia, rodar antes o `SKILL.md` desta mesma pasta (script `pillar_padroniza_curva_abc.py`) pra converter em XLSX padronizado.
3. `@inteligencia-dados` classifica os produtos em A (≈80% do faturamento), B (≈15%) e C (≈5% restante), usando sempre dado de venda, documentando o critério de corte usado.
4. Cruzar a classificação por faturamento com a classificação por margem bruta, pois nem todo item A em faturamento é A em margem.
5. Entregar o diagnóstico com a participação de cada categoria de produto (básico, elétrica, hidráulica, pintura, acabamento, ferramentas) na curva.
6. Passar a classificação (e o Grupo Z, se o relatório trouxer) pra atividade `2 - Giro de Estoque e Margem`, que calcula giro, capital parado e risco de ruptura em cima dela.

## Cadência recomendada

Mensal para clientes com movimento intenso; trimestral é o mínimo aceitável para não perder a fotografia do negócio desatualizada. Recalcular sempre que o cliente trouxer um relatório novo, mesmo fora do ciclo.

## Indicadores de sucesso

- % do faturamento concentrado nos itens A (referência de saúde: 70 a 85%)
- Grupo A, B e C bem definidos e estáveis entre períodos (se o corte muda muito de um período pro outro sem motivo de negócio, vale revisar o critério)

Indicadores de giro, capital parado e risco de ruptura ficam em `2 - Giro de Estoque e Margem/_atividade.md`, calculados sobre esta classificação.

## Squad responsável

`@inteligencia-dados` executa. Exige relatório real de ERP anexado, nunca estima número sem fonte (Pilar 1 do Método Viga Mestra).

## Operação enxuta

Uma curva ABC bem feita substitui reunião de "achismo" sobre o que comprar. É a atividade de maior alavancagem do Pilar 1: baixo esforço de execução (um relatório, uma rodada de classificação), alto impacto na decisão de compra e campanha dos meses seguintes.

## Tarefas desta atividade

1. **Padronização do relatório de origem** (quando PDF Pontual): converter pra XLSX antes de qualquer leitura, script determinístico, zero custo de IA na conversão. Ferramenta pronta nesta pasta: `SKILL.md` + `pillar_padroniza_curva_abc.py`.
2. **Classificação ABC por faturamento**: ordenar produtos por receita de venda, aplicar corte 80/15/5, documentar o critério.
3. **Classificação ABC por margem**: repetir o corte usando margem bruta em vez de faturamento, e apontar onde as duas classificações divergem.
4. **Leitura de participação por categoria**: consolidar a curva por categoria de produto, não só por SKU individual, pra virar leitura executiva pro dono da loja.

Leitura de giro, capital parado, risco de ruptura e giro parado (a partir desta classificação e do Grupo Z do relatório, se houver) é tarefa de `2 - Giro de Estoque e Margem/_atividade.md`, não desta atividade.

As tarefas 2 a 4 ainda não têm arquivo `.md` de script pronto. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.
