# Cruzamento: diagnóstico de margem da Pillar x meta de 28% da Viabiliza Consultoria

**Cliente:** Construmais
**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra
**Status:** v1, sujeito a refinamento
**Gatilho da análise:** Relatório Executivo de Gestão Econômico-Financeira da Viabiliza Consultoria (fornecedor externo do cliente, não é a Pillar), cobrindo jan-jun/2026, recebido pelo Tony. A Pillar não leu o PDF original, os números da Viabiliza usados aqui vêm do resumo repassado no pedido desta análise, não de leitura direta do documento.
**Fontes internas usadas:** `outputs/_diagnosticos/inteligencia-dados/diagnostico-estoque.md` (4 períodos de Curva ABC, mai/2025 a jun/2026, e auditoria de cadastro do snapshot de 03/08/2026), `outputs/_diagnosticos/inteligencia-dados/diagnostico-giro-estoque.md` (classificação de giro por bucket, mesmo snapshot), `CLIENTE.md` (seção Pilar 1).

## Como ler este arquivo

Esta não é uma nova seção de período dos diagnósticos cumulativos: não processei relatório novo de ERP nesta rodada, cruzei o que já estava diagnosticado com a meta trazida de fora pela Viabiliza. Por isso vira análise pontual, não entra em `diagnostico-curva-abc.md` nem em `diagnostico-giro-estoque.md`.

**Antes de qualquer recomendação, um alerta importante:** ao cruzar os dois relatórios encontrei mais de uma discrepância de número entre o que foi resumido da Viabiliza, o que já está registrado no `CLIENTE.md` e o que os diagnósticos internos da Pillar realmente sustentam hoje. Reporto cada uma abaixo em vez de escolher um número silenciosamente, seguindo a regra de não inventar dado.

---

## 1. A margem de 21,8% da Viabiliza não é a mesma métrica que a margem que a Pillar calcula

Isso precisa ficar claro antes de qualquer cruzamento por categoria.

- **O que a Pillar calcula:** margem bruta sobre venda por SKU, direto da Curva ABC do ERP Pontual: (Preço - Custo) / Preço. É essencialmente a mesma conta que (Receita - CMV) / Receita.
- **O que a Viabiliza calcula:** margem de contribuição, que parte da mesma Receita e do mesmo CMV, mas desconta também outros custos variáveis (impostos sobre venda, comissão, frete, taxa de cartão, entre outros que o resumo recebido não detalha por categoria).

Juntando os dois períodos de Curva ABC que cobrem jan-jun/2026 (jan-mar/2026: faturamento R$ 598.882,79, margem R$ 270.339,16, 45,14%; abr-jun/2026: faturamento R$ 650.821,13, margem R$ 254.933,69, 39,17%), a margem bruta ponderada da Pillar para o semestre fica em **42,0%** (R$ 525.272,85 de margem sobre R$ 1.249.703,92 de faturamento, soma direta dos dois períodos já publicados no diagnóstico).

A DRE da Viabiliza pro mesmo semestre mostra Receita Bruta R$ 1.443.700, CMV R$ 861.760 (59,7% da receita). Isso dá uma margem bruta (Receita - CMV) / Receita de **40,3%**, próxima dos 42,0% calculados pela Pillar (diferença de 1,7 ponto, dentro do esperado considerando que a base de receita também não bate exatamente, ver item 2 abaixo). Ou seja: **o CMV/margem bruta dos dois lados são consistentes entre si.**

O problema não está no CMV. Está no salto de 40,3% (margem bruta) pra 21,8% (margem de contribuição): R$ 311.720 de custo variável adicional no semestre (R$ 581.940 de margem bruta menos R$ 270.220 de margem de contribuição), cerca de 21,6% da receita bruta, que a Pillar **não tem visibilidade nenhuma** por categoria, porque não está em nenhum campo do ERP que os relatórios de Curva ABC ou de estoque trazem.

**Consequência prática:** a Pillar não consegue decompor os 6,2 pontos que faltam pra sair de 21,8% pra 28% diretamente pela margem de contribuição por categoria, porque não tem o dado de impostos/comissão/frete por categoria. O que dá pra fazer, e é o que a Viabiliza pediu ("revisão de precificação e mix"), é atacar o lado que a Pillar enxerga: a margem bruta de mercadoria por categoria/SKU. **Supondo que os outros custos variáveis (impostos, comissão, frete) se mantenham proporcionais à receita** (premissa a confirmar com a Viabiliza ou o Tony, não é fato verificado), subir a margem bruta ponderada da loja em 6,2 pontos, de ~42,0% pra ~48,2%, teria o efeito equivalente de levar a margem de contribuição de 21,8% pra 28%. Esse é o número que orienta as recomendações abaixo.

## 2. Discrepâncias de dado encontradas (não escolhi um número, reporto os dois)

| Métrica | Valor citado no pedido desta análise | Valor mais recente nos diagnósticos da Pillar | O que aconteceu |
|---|---|---|---|
| Estoque parado (R$) | R$ 320.903,02, 1.682 itens (fonte: `CLIENTE.md`, cálculo de 23/07/2026) | R$ 373.769,46, 1.732 SKUs (`diagnostico-estoque.md`, snapshot 03/08/2026) **ou** R$ 351.523,17, 1.733 SKUs (`diagnostico-giro-estoque.md`, mesmo snapshot, com uma correção de custo a mais aplicada) | O número foi recalculado 3 vezes desde 23/07: primeiro por reconciliação (R$ 295.126,57 em 25/07), depois por um snapshot de estoque novo (R$ 373.769,46 em 03/08), depois com a correção do item "Sacolas 30x40" aplicada só no `diagnostico-giro-estoque.md` (R$ 351.523,17). O `diagnostico-estoque.md` ainda não foi atualizado com essa última correção. R$ 320.903,02 está desatualizado nos três recálculos seguintes |
| Margem acima de 1.000% (itens) | 27 itens | 24 itens (`diagnostico-estoque.md`, auditoria de 03/08/2026, "era 27 em 23/07/2026") | Contagem revisada, 3 itens saíram da lista entre uma rodada e outra, motivo não detalhado na fonte |
| Margem negativa (itens) | 199 itens | 198 itens (`diagnostico-estoque.md`, "era 199... estável") | Variação mínima, tratada como estável na própria fonte |
| Inconsistência preço x custo/margem | 147 itens, tolerância de R$ 2 | **Origem localizada em 2026-09-18:** `outputs/07-2026/Analises/23-diagnostico-estoque.md`, linha 175, snapshot de 23/07/2026. Vem da coluna "Precificação" já embutida no próprio `Estoque ETL.xlsx` do cliente (checagem booleana com tolerância de R$ 2 entre preço cadastrado e o preço que custo+margem indicariam). É diferente do achado "387 itens, tolerância de 2 pontos percentuais" dos diagnósticos de 03/08/2026 em diante, que é outra métrica (% Margem cadastrado x recalculado), não substitui os 147 | Os dois achados são reais e coexistem, cada um mede uma inconsistência diferente. Os 147 não foram carregados pros diagnósticos cumulativos mais recentes (`diagnostico-estoque.md`/`diagnostico-giro-estoque.md`), ficaram só no relatório pontual de 23/07/2026. Vale considerar incorporar essa checagem de novo na próxima rodada de atualização do diagnóstico cumulativo |
| Participação por categoria (14 meses) | Material Básico 42,21%, Hidráulica 10,10%, Pintura 8,42% | Não está como total de 14 meses em nenhum dos dois diagnósticos, só por período trimestral/bimestral: Material Básico varia de 41,7% a 44,8% conforme o trimestre, Hidráulica de 5,8% a 10,8%, Pintura de 7,5% a 10,7% | Os números de 14 meses citados vêm do `CLIENTE.md` (seção Pilar 1), não foram recalculados nem republicados nos diagnósticos de período. Estão dentro da faixa que os 4 períodos sustentam, mas não é um valor que eu consegui conferir direto numa tabela de 14 meses |
| Faturamento jan-jun/2026 | R$ 1.443.700 (DRE Viabiliza, Receita Bruta) | R$ 1.249.703,92 (soma de jan-mar + abr-jun/2026, Curva ABC) | **Resolvido em 2026-09-18, via time interno da Pillar:** são recortes de período diferentes. A Viabiliza usa relatório do ERP mais atualizado que o extrato de Curva ABC que a Pillar processou pro mesmo intervalo nominal. Não é erro de cálculo nem de fonte, os R$ 193.996,08 de diferença não precisam de investigação adicional nem de pergunta ao Tony/Viabiliza |

Uso os valores mais recentes dos diagnósticos da Pillar no resto desta análise (198 margem negativa, 24 margem >1.000%, R$ 351.523,17 de estoque parado com o critério mais estrito), e trato os 147 itens de inconsistência preço x custo como número pendente de origem, não como base de ação.

## 3. Onde a margem bruta de mercadoria está mais fraca hoje (o que dá pra atacar via precificação/mix)

Os diagnósticos da Pillar não têm uma tabela de margem % por categoria (só participação de faturamento por categoria e margem % item a item nos rankings de giro e margem). O que dá pra afirmar com o que já foi calculado:

**Material Básico é ao mesmo tempo a maior categoria em faturamento (41,7% a 44,8% do total conforme o trimestre) e a categoria onde vive o principal item de margem estruturalmente baixa da loja: cimento.**

| Produto | Margem % por período (mai-out/25 · nov-dez/25 · jan-mar/26 · abr-jun/26) |
|---|---|
| Cimento Montes Claros CPII F 32 50kg | 22,4% (corrigida) · 22,0% · 22,8% · 22,4% |
| Cimento Poty CPII Z 32 50kg | 24,65% · 18,2% · 21,1% · 21,7% |

Esses dois SKUs aparecem como produto isca validado nos 4 períodos processados, sem exceção (giro alto, margem consistentemente entre 18% e 25%, nunca acima disso em nenhum dos 4 recortes). No mesmo grupo de fase de obra (fundação/alvenaria), os agregados vendidos junto (areia, pedra britada) rodam bem mais alto:

| Produto | Margem % por período |
|---|---|
| Areia Fina | 51,7%(estimado) · 50,9% · 51,5% · 52,6% |
| Pedra Britada 1 (19) | 52,0% · 58,6% · não apareceu no top 5 do período · 52,6% |

O padrão se repete em todos os 4 períodos sem exceção: cimento puxa faturamento e é âncora de tráfego, agregados carregam a margem. Isso já sustenta o Kit Fundação e Alvenaria (cimento + areia + pedra + tijolo), validado nos 4 períodos e já registrado em `outputs/07-2026/Analises/24-estrategia-kits-e-vendas.md`.

**Isso não significa que o cimento deva subir de preço.** Ele é produto isca de propósito, decisão do cliente conforme já registrado em `CLIENTE.md`. A alavanca de precificação mais direta que os dados sustentam é: reforçar o cross-sell do cimento pros itens de margem alta da mesma fase de obra (kit já validado), em vez de mexer no preço do isca.

**Lacuna importante:** não tenho, em nenhum dos dois diagnósticos, margem % agregada por categoria pra Hidráulica, Pintura ou qualquer categoria fora de Material Básico. Os rankings de "top produtos por margem bruta absoluta" de todos os 4 períodos são dominados por itens de Material Básico (cimento, areia, pedra, tijolo), então não sei se Hidráulica e Pintura, juntas 18,5% a 21,6% do faturamento por trimestre, têm margem melhor ou pior que a média da loja. Recalcular isso exigiria abrir as planilhas padronizadas de Curva ABC (`07-2026/Arquivos/25-inteligencia-dados-curva-abc-padronizada_*.xlsx`) e agregar margem por categoria diretamente, o que não fiz nesta rodada porque não foi pedido um novo processamento de período, e envolveria recalcular ~15 mil linhas por arquivo. Fica como próximo passo, ver seção 5.

**Outro fator estrutural que dilui a margem agregada, não é um item específico:** o Grupo A concentra só 59,87% a 59,98% do faturamento nos 4 períodos, abaixo da faixa saudável de referência do método (70% a 85%), estável nos 4 recortes. Isso quer dizer que uma fatia maior do que o ideal do faturamento passa por uma cauda longa de itens B e C, cuja margem individual não está mapeada em conjunto. Concentrar mais faturamento nos itens A (via mix, não via desconto) tende a puxar a margem média pra cima, mas isso não é uma ação de precificação item a item, é mais uma leitura de composição de venda.

## 4. Os 24 itens de margem acima de 1.000% e os 198 de margem negativa: sinalizar, não usar como alavanca de preço

Conforme pedido, trato os dois blocos como possível erro de cadastro a corrigir no ERP, não como oportunidade de correção de preço real:

- **24 itens com markup acima de 1.000%:** a maioria tem quantidade em estoque zero (sem exposição financeira hoje), e nos casos com par direto na mesma linha de produto (ex: Cabo Rígido 10mm, Cordão Paralelo, Abraçadeira Nylon), o benchmark aponta erro de dígito no custo cadastrado (falta um ou dois zeros), não markup real. Detalhe completo, item a item, em `diagnostico-estoque.md`, seção "Detalhamento da auditoria de qualidade do cadastro, por categoria de erro".
- **198 itens com margem negativa:** 190 têm quantidade zero ou negativa, sem exposição financeira real hoje. Os 8 itens com estoque ativo somam R$ 951,20 de perda potencial se vendidos ao preço cadastrado, valor baixo frente ao faturamento da loja.

Nenhum dos dois blocos entra na conta de "onde subir margem via precificação real", porque não representa preço de venda genuíno hoje, representa erro de cadastro. Ação recomendada é corrigir o ERP, não redefinir preço de venda.

## 5. Estoque parado: R$ 320,9 mil citado está defasado, use R$ 351.523,17 como referência e ataque em 2 blocos

Usando o valor mais recente e mais corrigido (`diagnostico-giro-estoque.md`, bucket "Nunca vendeu, 14 meses completos", R$ 351.523,17 em 1.733 SKUs), a recomendação de ação comercial (fora do escopo de reestruturação de dívida, dentro do escopo da Pillar) segue o que o próprio diagnóstico de giro já separou:

**Bloco 1, já confirmado como não problemático (R$ 161.213,56, 45,9% do "nunca vendeu"):** Cumeeira Zincalum (venda por encomenda), Vareta Solda Oxi (slow-mover genuíno confirmado pelo Tony), Sacolas 30x40 (uso interno, não revenda), Tubo PVC Rosca (giro baixo confirmado, mas com pendência de cadastro à parte). **Não entra em campanha de liquidação.**

**Bloco 2, candidato real a ação comercial (R$ 190.309,61 + R$ 99.010,99 = R$ 289.320,60 a custo):**
- R$ 190.309,61 (54,1% do "nunca vendeu"): sem nota qualitativa do Tony ainda, candidato a checagem item a item por valor (priorizado pela planilha `08-2026/Arquivos/26-inteligencia-dados-giro-estoque-por-bucket_2026-08-03.xlsx`) e, pros itens que não tiverem explicação de negócio (tipo Cumeeira/Vareta), candidato a campanha de liquidação/desova.
- R$ 99.010,99 (buckets "121 a 150 dias" e "acima de 180 dias"): giro mais recente que zero, mas já caindo, candidato a campanha de giro antes de virar estoque parado de fato.

Recomendação objetiva: tratar os R$ 289.320,60 como o pool de capital empatado que dá pra converter em caixa via ação comercial (campanha de desova, kit de saída, desconto pontual) nos próximos 60 a 90 dias, em vez dos R$ 373.769,46 (ou R$ 320.903,02) citados antes, que misturam itens já confirmados como giro zero esperado com itens que ainda não tiveram checagem. A decisão de preço/desconto da campanha continua sendo do `@gestor-trafego`/`@copywriter` ou do cliente, não da Inteligência de Dados.

## 6. O que falta pra fechar o cruzamento completo até categoria/classe ABC com a meta de 28%

Listo em vez de estimar, conforme pedido:

1. **Breakdown de custo variável além do CMV (impostos, comissão, frete, taxa de cartão) por categoria ou ao menos em nível agregado mensal.** Sem isso não dá pra saber se os 21,6% de receita que separam margem bruta de margem de contribuição pesam igual em todas as categorias ou se concentram nalguma (ex: frete pesa mais em material básico ensacado/agregado, que tem mais volume/peso por venda).
2. **Margem % agregada por categoria (Hidráulica, Pintura, Elétrica, Ferragem etc.), não só participação de faturamento.** Exigiria abrir as 4 planilhas padronizadas de Curva ABC e agregar margem por categoria linha a linha, tarefa de recálculo que não estava no escopo desta análise pontual.
3. ~~Origem do número "147 itens, tolerância R$ 2"~~. **Resolvido em 2026-09-18**, ver item 2 acima: vem de `23-diagnostico-estoque.md`, checagem embutida na planilha do cliente.
4. ~~Reconciliação da diferença de R$ 193.996,08 entre a Receita Bruta da DRE da Viabiliza e o faturamento somado da Curva ABC~~. **Resolvido em 2026-09-18**, ver item 2 acima: são recortes de período diferentes, a Viabiliza usa relatório de ERP mais atualizado.
5. **Confirmação da premissa usada na seção 1** (outros custos variáveis proporcionais à receita entre categorias), direto com a Viabiliza ou com o Tony, antes de tratar o alvo de "margem bruta ~48,2%" como equivalente confiável da meta de margem de contribuição de 28%. Segue em aberto.

## Próximos passos

1. Enviar este cruzamento ao Tony e propor perguntar à Viabiliza o item 1 da seção 6 (o que compõe o custo variável entre margem bruta e margem de contribuição, e se dá pra abrir por categoria de produto), sem isso a meta de 28% não tem como ser decomposta por categoria com confiabilidade.
2. Se o cliente confirmar a premissa da seção 1, o próximo passo natural é recalcular margem % por categoria direto das 4 planilhas de Curva ABC (item 2 da seção 6), pra saber se Hidráulica e Pintura ajudam ou atrapalham a margem agregada, hoje é ponto cego.
3. `@copywriter`/`@gestor-trafego` podem usar o Bloco 2 da seção 5 (R$ 289.320,60) como base de campanha de giro/desova nos próximos 60-90 dias.
4. Cobrar de novo a correção dos outliers críticos já pendentes no ERP (colorante código 11073, cabo flex código 7153, mangueira código 7874), que seguem inflando valor de estoque bruto mesmo não entrando nos totais ajustados.
5. Considerar reincorporar a checagem "Precificação, tolerância R$ 2" (147 itens em 23/07/2026) na próxima atualização do diagnóstico cumulativo de estoque, hoje ela só existe no relatório pontual mais antigo.

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
