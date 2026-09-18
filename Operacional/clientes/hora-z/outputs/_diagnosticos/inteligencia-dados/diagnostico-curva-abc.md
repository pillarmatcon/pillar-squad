# Diagnóstico de Curva ABC para Hora Z
**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra, atividade "Curva ABC do Estoque"
**Como ler este arquivo:** histórico cumulativo, uma seção por período coberto por relatório de vendas do cliente, do mais recente (topo) para o mais antigo (final), independente da ordem em que os relatórios foram processados.

## Visão geral acumulada

| Período/snapshot | Faturamento | Faturamento sem outliers | Margem % média (cruzado c/ estoque) | Concentração do grupo A (por faturamento) |
|---|---|---|---|---|
| Acumulado até 15/09/2026 | R$ 521.254,92 | R$ 291.831,91 | 44,3% (mediana, 295 SKUs cruzados) | 173 SKUs, 79,9% do faturamento sem outliers |

Primeira rodada de diagnóstico do cliente, sem período anterior para comparar tendência. Duas leituras já dão pra fixar: a loja tem uma cauda de SKU (1187 produtos vendidos no acumulado) mas a concentração de valor está em poucos itens (173 SKUs respondem por quase 80% do faturamento), e dois lançamentos isolados de "Plataforma" distorcem qualquer leitura de faturamento total se não forem tratados à parte.

**Correção de metodologia em 18/09/2026:** a rodada anterior desta seção usava a classificação ABC por quantidade vendida (a que veio pronta do relatório do cliente) como se fosse "a" Curva ABC. Isso estava errado: Curva ABC classifica por faturamento, não por quantidade. O que era chamado de Curva ABC virou "indicador de giro por quantidade / produto isca" (ainda útil, só não é Curva ABC), e a classificação por faturamento, recalculada abaixo, passa a ser a Curva ABC oficial do arquivo. O conteúdo da seção de período abaixo foi reescrito para refletir isso, mesmo período e mesma fonte de dados, sem duplicar seção.

---

## Período: acumulado até 15/09/2026 (período não declarado pela fonte)
**Fonte dos dados:** `Curva_Abc.xlsx`, aba "Curva ABC de Produtos por quantidade", recebido do cliente em 15/09/2026, processado em 09-2026
**Planilha(s):** `09-2026/Arquivos/15-inteligencia-dados-curva-abc-padronizada_acumulado-ate-2026-09-15.xlsx` (atualizada em 18/09/2026 com abas novas: "Curva ABC por faturamento", "Comparativo qtd x faturamento", "Top 15 faturamento c. margem", "Margem por categoria (cruz. completo)" e "Margem completa cruzada (263 SKUs)", substituindo a antiga "Top 30 margem")
**Status:** v1, sujeito a refinamento

### Resumo executivo

- Faturamento total no relatório: R$ 521.254,92, em 1.187 SKUs distintos.
- Este relatório não declara o período coberto (sem data de início/fim no cabeçalho, diferente do padrão do sistema Pontual Tecnologia). Tratei como snapshot acumulado até a data de extração/recebimento do arquivo (15/09/2026), por ser a leitura mais honesta possível sem inventar corte de datas. **Preciso que o cliente confirme qual é o período real coberto** (desde a abertura da loja, desde a troca de ERP, últimos 12 meses etc.), porque isso muda completamente a leitura de "faturamento mensal médio" e de tendência.
- **Curva ABC oficial: classificação por faturamento, não por quantidade.** O relatório do cliente vem com uma classificação ABC pronta baseada em quantidade vendida (nome da aba original: "Curva ABC de Produtos por quantidade"). Na rodada anterior deste diagnóstico, tratei essa classificação como se fosse "a" Curva ABC, o que é um erro de metodologia: Curva ABC de verdade classifica por faturamento. Corrigido nesta atualização (18/09/2026): recalculei a Curva ABC ordenando os 1.185 SKUs (sem os 2 outliers de "Plataforma", ver abaixo) por valor faturado desc., com corte A até 80% do faturamento acumulado, B de 80% a 95%, C de 95% a 100%. A classificação por quantidade continua no arquivo, mas rotulada como "indicador de giro por quantidade / produto isca", que é o que ela realmente mede.
- **Dois lançamentos distorcem o faturamento bruto**: "Plataforma -Z-45/25J RT" (R$ 133.748,71) e "114887 - Plataforma - Z-3422 DC" (R$ 95.674,30), juntos R$ 229.423,01, quase 44% do total faturado do relatório inteiro. Cada um aparece uma única vez, com código fora do padrão usado no resto do catálogo. Não tenho como saber pela planilha se é venda de equipamento, aluguel registrado como venda ou lançamento incorreto. Tanto a participação por categoria quanto a nova Curva ABC por faturamento abaixo excluem esses dois lançamentos. **Peço para o cliente confirmar a natureza dessas duas vendas antes de usar este relatório para decidir orçamento de mídia por categoria.**
- Categorização por palavra-chave na descrição do produto (taxonomia MatCon de `_squad/_shared/nichos.md`, fallback porque o relatório não traz categoria própria), critério auditável documentado na seção seguinte. 95 dos 1.187 SKUs (8%) não bateram com nenhuma palavra-chave e ficaram como "não classificado", a maioria peças de fixação e itens com nome abreviado demais para reconhecer com segurança.
- Sem "Grupo Z" (produtos sem venda) neste relatório: a Curva ABC do sistema desse cliente só lista quem vendeu, não existe faixa de classificação para quem não vendeu. Uso o relatório de Estoque, cruzado com este, para aproximar quem não vendeu no período, ver `diagnostico-giro-estoque.md`.
- **Cobertura de margem ampliada.** A rodada anterior cruzava Curva ABC com Estoque para calcular margem, mas só expunha os 30 SKUs de maior margem numa aba própria. Refeito o cruzamento completo por código: dos 295 SKUs presentes nos dois relatórios, 263 têm custo maior que zero e menor ou igual ao preço de venda (margem confiável), 18 têm custo zerado no cadastro e 14 têm outlier de cadastro (custo maior que o preço de venda, ver auditoria em `diagnostico-giro-estoque.md`). A cobertura de margem por faturamento (não por contagem de SKU) varia bastante por categoria, documentada na seção "Margem por categoria" abaixo, sem inventar margem para quem não tem custo cruzável.

### Critério de categorização

Correspondência de palavra-chave na descrição do produto (nome em maiúsculas, busca por termo/regex), testada em ordem de prioridade: elétrica e hidráulica primeiro (termos mais específicos), depois pintura, ferramentas, acabamento e básico. Duas categorias fora da taxonomia padrão de 6 grupos foram necessárias porque apareceram no catálogo real: **EPI/segurança** (calçado, óculos, protetor auditivo, colete) e **bazar/diversos** (celular, perfume, air fryer, itens claramente fora do escopo de material de construção, provavelmente revenda paralela ou cadastro incorreto de fornecedor). Uma categoria **serviço** também foi separada (taxa de entrega), porque não é produto físico. O critério completo (lista de termos por categoria) está documentado no script de processamento e pode ser auditado e contestado pelo cliente linha a linha na planilha categorizada.

### Participação por categoria

Cálculo sem os 2 lançamentos de "Plataforma" (ver Resumo executivo). Base: R$ 291.831,91 em 1.185 SKUs.

| Categoria | Faturamento | % do total | SKUs |
|---|---|---|---|
| Básico (cimento, tijolo, bloco, ferro, fixação) | R$ 145.326,68 | 49,8% | 238 |
| Acabamento | R$ 35.804,53 | 12,3% | 60 |
| Hidráulica | R$ 25.995,10 | 8,9% | 342 |
| Pintura | R$ 21.534,66 | 7,4% | 122 |
| Não classificado | R$ 19.468,78 | 6,7% | 93 |
| Ferramentas | R$ 15.232,33 | 5,2% | 169 |
| Elétrica | R$ 13.543,89 | 4,6% | 109 |
| Bazar/diversos | R$ 6.652,17 | 2,3% | 12 |
| EPI/segurança | R$ 4.194,55 | 1,4% | 28 |
| Serviço (taxa de entrega) | R$ 4.079,22 | 1,4% | 12 |

Leitura: quase metade do faturamento vem de material básico de estrutura e alvenaria, esperado pra uma loja de material de construção com perfil de obra (não só reforma de acabamento). Hidráulica tem o maior número de SKUs distintos (342) mas participação de faturamento proporcionalmente baixa (8,9%), sinal de catálogo pulverizado em peças de conexão de ticket baixo. Vale o cliente confirmar se essa divisão bate com a divisão real dos departamentos da loja física.

### Classificação ABC (por faturamento), oficial

Recalculada em 18/09/2026. Base: R$ 291.831,91 em 1.185 SKUs (sem os 2 outliers de "Plataforma"). Ordenação por valor faturado desc., corte A até 80% do faturamento acumulado, B de 80% a 95%, C de 95% a 100%.

| Classe | SKUs | % dos SKUs | Faturamento | % do faturamento |
|---|---|---|---|---|
| A | 173 | 14,6% | R$ 233.311,13 | 79,9% |
| B | 369 | 31,1% | R$ 43.883,16 | 15,0% |
| C | 643 | 54,3% | R$ 14.637,62 | 5,0% |

Leitura: 173 SKUs (14,6% do catálogo vendido) respondem por quase 80% do faturamento. A classe C, com mais da metade dos SKUs, responde por só 5% do valor. É a leitura Pareto clássica de Curva ABC, bem diferente da leitura por quantidade (ver comparativo abaixo), que tinha só 1 SKU em classe A.

### Indicador de giro por quantidade / produto isca (não é Curva ABC)

Esta é a classificação que veio pronta no relatório do cliente, batizada na fonte como "Curva ABC de Produtos por quantidade". Continua útil (identifica giro alto/produto isca), mas não é Curva ABC: o corte é por volume de unidades vendidas, não por faturamento.

| Classe | SKUs | % do volume (quantidade) | % do faturamento (sem outliers) |
|---|---|---|---|
| A | 1 | 22,0% | 2,2% |
| B | 70 | 57,9% | 29,9% |
| C | 1.114 | 20,1% (após remover 2 outliers de C) | 67,8% |

O único SKU da classe A por quantidade é um tijolo cerâmico de R$ 0,95 a unidade (código 22114), responsável por 21,96% de tudo que saiu da loja em unidades, mas só 2,2% do valor faturado. Esse mesmo tijolo também é classe A por faturamento (rank 6 de valor), então aqui as duas leituras coincidem, mas isso não é a regra, ver comparativo abaixo.

### Comparativo: indicador de giro (quantidade) x Curva ABC (faturamento)

Mesma base de SKUs, mostrando como a classe muda dependendo do critério. Lista completa na aba "Comparativo qtd x faturamento" da planilha.

| Código | Produto | Categoria | Quantidade | Indicador giro (classe qtd) | Faturamento | Classe ABC (faturamento) | Leitura |
|---|---|---|---|---|---|---|---|
| PRD00045 | Cimento Supremo 50kg | Básico | 704 | B | R$ 27.868,00 | A | Giro moderado, mas maior faturamento do catálogo: ticket alto, não volume, que fatura |
| 22114 | Tijolo 6 furos 09x14x24 Lorenzetti | Básico | 6.860 | A | R$ 6.452,00 | A | Maior giro em unidades e também classe A em faturamento, as duas leituras coincidem |
| 20250 | Tijolo 6 furos 09x14x29 Lorenzetti | Básico | 4.170 | B | R$ 4.229,00 | A | Giro moderado (classe B), mas puxa classe A de faturamento pelo volume de unidades |
| 21356 | Bloco concreto normal 14x19x39 | Básico | 1.470 | B | R$ 5.248,80 | A | Giro moderado, mas ticket por lote alto o suficiente pra puxar classe A de faturamento |
| 21070 | Vermelho segurança epóxi piso 2,88L Farben | Acabamento | 16 | C | R$ 8.638,46 | A | Giro baixíssimo em quantidade, mas ticket alto o bastante pra ser 2º maior faturamento |
| 21445 | Epóxi piso branco Farben 2,8L | Acabamento | 24 | C | R$ 7.873,06 | A | Mesmo padrão: baixo giro, alto ticket, classe A de faturamento |
| 1589 | Bucha plástica tijolo oco 06mm (1000) cinza | Básico | 460 | B | R$ 46,00 | C | Giro relativamente alto em unidades, mas valor unitário tão baixo que cai pra classe C |

Este é o achado que justifica não tratar giro por quantidade como Curva ABC: cimento e as tintas epóxi Farben são os principais itens de faturamento da loja, mas não aparecem no topo do ranking de giro por quantidade. Ao mesmo tempo, itens de giro alto em unidades (buchas, parafusos, 21 SKUs no total com esse padrão) somam pouco em faturamento e ficam em classe C. São leituras diferentes e complementares, não a mesma coisa com nome trocado.

### Top produtos por faturamento (Curva ABC oficial)

Margem calculada quando o SKU aparece no relatório de Estoque com custo maior que zero e menor ou igual ao preço de venda. Lista completa das 1.185 linhas na aba "Curva ABC por faturamento" da planilha; top 15 com margem também na aba "Top 15 faturamento c. margem".

| # | Código | Produto | Categoria | Classe ABC (fat.) | Faturamento | Quantidade | Margem % |
|---|---|---|---|---|---|---|---|
| 1 | PRD00045 | Cimento Supremo 50kg | Básico | A | R$ 27.868,00 | 704 | 16,8% |
| 2 | 21070 | Vermelho segurança epóxi piso 2,88L Farben | Acabamento | A | R$ 8.638,46 | 16 | 0,3% (custo R$ 261,69 x preço R$ 262,41, confirmar com o cliente, margem quase zero) |
| 3 | 21445 | Epóxi piso branco Farben 2,8L | Acabamento | A | R$ 7.873,06 | 24 | sem cruzamento (não consta no relatório de Estoque recebido) |
| 4 | 22446 | Argamassa Superkola 3Mais cinza 20kg | Básico | A | R$ 7.166,12 | 290 | 37,9% |
| 5 | PRD00040 | Ar condicionado 9.000 BTU Inverter Frio TCL | Não classificado | A | R$ 6.600,00 | 3 | sem cruzamento |
| 6 | 22114 | Tijolo 6 furos 09x14x24 Lorenzetti | Básico | A | R$ 6.452,00 | 6.860 | 36,8% |
| 7 | 21437 | Catalisador epóxi p/piso 0,72L Farben | Acabamento | A | R$ 5.495,40 | 51 | sem cruzamento |
| 8 | 20861 | Areia fina cinza 1m³ | Básico | A | R$ 5.440,07 | 25,5 | sem cruzamento |
| 9 | 21356 | Bloco concreto normal 14x19x39 | Básico | A | R$ 5.248,80 | 1.470 | sem cruzamento |
| 10 | 20492 | Fundo preparador parede 18L Alessi | Pintura | A | R$ 4.312,00 | 16 | sem cruzamento |
| 11 | 20250 | Tijolo 6 furos 09x14x29 Lorenzetti | Básico | A | R$ 4.229,00 | 4.170 | 34,1% |
| 12 | PRD00079 | Areia com brita 00, 1m³ | Básico | A | R$ 3.914,77 | 20 | sem cruzamento |
| 13 | 20252 | Refletor Slim LED 200 120 6500K Autovolt | Elétrica | A | R$ 3.747,00 | 30 | sem cruzamento |
| 14 | 101010 | Ferro 3/8 (12 metros) 10mm | Básico | A | R$ 3.449,59 | 61 | 28,5% |
| 15 | 20912 | Ferro 5/16 (12 metros) 8mm | Básico | A | R$ 3.205,40 | 86 | 27,0% |

Leitura: o topo de faturamento é dominado por cimento e pelos itens de acabamento de ticket alto (tintas epóxi Farben para piso industrial), não pelos itens de maior giro em unidades (tijolo e bloco, que aparecem mas mais abaixo no ranking de valor). "Sem cruzamento" significa que o SKU não consta no relatório de Estoque recebido (443 SKUs), não que a margem seja zero, é ausência de dado, não dado ruim. O item 21070 tem margem calculável mas praticamente zero (R$ 0,72 de diferença entre custo e preço em um item de R$ 262), vale o cliente confirmar se o custo ou o preço cadastrado estão corretos antes de considerar esse item rentável.

### Margem por categoria (cruzamento completo)

Cruzamento completo Curva ABC x Estoque por código: todos os 295 SKUs presentes nos dois relatórios, não só os 30 de maior margem. Cobertura = % do faturamento da categoria com margem calculável (custo maior que zero e menor ou igual ao preço). Margem ponderada = margem % ponderada pelo faturamento dos SKUs com margem calculável.

| Categoria | Faturamento | % do total | SKUs cruzados | SKUs com margem calculável | Cobertura (% do faturamento) | Margem % ponderada |
|---|---|---|---|---|---|---|
| Básico | R$ 145.326,68 | 49,8% | 67 | 55 | 46,1% | 29,9% |
| Acabamento | R$ 35.804,53 | 12,3% | 14 | 13 | 30,3% | 6,8% |
| Hidráulica | R$ 25.995,10 | 8,9% | 84 | 79 | 32,5% | 41,1% |
| Pintura | R$ 21.534,66 | 7,4% | 31 | 26 | 18,2% | 42,4% |
| Não classificado | R$ 19.468,78 | 6,7% | 29 | 28 | 17,4% | 50,4% |
| Ferramentas | R$ 15.232,33 | 5,2% | 46 | 40 | 23,7% | 43,2% |
| Elétrica | R$ 13.543,89 | 4,6% | 17 | 16 | 7,7% | 48,9% |
| Bazar/diversos | R$ 6.652,17 | 2,3% | 1 | 1 | 0,4% | 38,6% |
| EPI/segurança | R$ 4.194,55 | 1,4% | 6 | 5 | 2,8% | 41,5% |
| Serviço | R$ 4.079,22 | 1,4% | 0 | 0 | 0,0% | N/D |

**Cobertura é baixa na maioria das categorias, de 0,4% (Bazar/diversos, categoria de 1 SKU só) a 46,1% (Básico), essa é a limitação real desta rodada, não escondo isso.** A maioria dos SKUs que vendeu no acumulado não está mais (ou nunca esteve, com esse código) no snapshot de estoque atual, então a margem ponderada acima reflete só a fatia cruzável de cada categoria, não a categoria inteira. Acabamento é o caso mais visível: a margem ponderada de 6,8% parece baixa para uma categoria de ticket alto, mas isso é puxado quase inteiramente por um único item (Vermelho segurança epóxi piso, R$ 8.638 de faturamento e margem de 0,3%), que domina os R$ 10.850 de faturamento cruzável da categoria. Não acrescento margem estimada para os SKUs sem custo cruzável, eles ficam de fora da média, não entram como zero nem como suposição.

**5 principais produtos por faturamento em cada categoria, pra dar contexto (todos classe A):**
- **Básico:** Cimento Supremo 50kg (R$ 27.868), Argamassa Superkola 3Mais 20kg (R$ 7.166), Tijolo 6 furos 09x14x24 (R$ 6.452), Areia fina cinza 1m³ (R$ 5.440), Bloco concreto normal 14x19x39 (R$ 5.249).
- **Acabamento:** Vermelho segurança epóxi piso 2,88L Farben (R$ 8.638), Epóxi piso branco Farben 2,8L (R$ 7.873), Catalisador epóxi p/piso 0,72L Farben (R$ 5.495), Porta interna lisa (R$ 2.309), Amarelo segurança epóxi piso 2,8L (R$ 1.587).
- **Hidráulica:** Tubo esgoto 100mm 6m (R$ 2.260), Torneira Prima eletrônica 5500W (R$ 984), Tubo concreto 30x100 (R$ 980), Tubo esgoto 50mm 6m (R$ 586), Ducha ND eletrônica 7700W (R$ 524).
- **Pintura:** Fundo preparador parede 18L Alessi (R$ 4.312), Tinta acrílica fosco econômico 15L Eucatex (R$ 1.800), Tinta amarelo segurança piso (R$ 1.614), Fita crepe amarela 18x40 automotiva (R$ 1.293), Tinta acrílica preto semibrilho (R$ 1.179).

### Produtos isca / âncora identificados

Cimento e tijolo são classe A tanto no indicador de giro por quantidade quanto na Curva ABC por faturamento (à exceção do cimento, que só é A por faturamento, ver comparativo acima), com margem baixa em termos percentuais (16,8% no cimento, 34-37% no tijolo, abaixo da mediana de 44,3% do catálogo cruzado). É o padrão clássico de produto isca de MatCon: material estrutural de consumo constante em qualquer obra, que traz o profissional e o consumidor final até a loja, mesmo com margem apertada.

- **Cimento Supremo 50kg**: 704 unidades vendidas, margem de 16,8% (a mais baixa entre os itens de giro alto cruzados). Item de entrada, provável gerador de fluxo, mas exige volume alto pra compensar.
- **Tijolo 6 furos (24 e 29)**: os dois SKUs de maior giro absoluto do catálogo (6.860 e 4.170 unidades), margem na faixa de 34-37%. Estoque atual confortável nos dois (2.514 e 2.598 unidades), sem risco de ruptura no momento (ver `diagnostico-giro-estoque.md`).
- **Ferro 3/8 e 5/16 (vergalhão)**: giro moderado (61 e 86 unidades), margem 27-28%, mas com estoque baixo (9-10 unidades cada). Aparecem também na lista de risco de ruptura do outro diagnóstico.

A decisão de usar esses itens como isca de campanha ou de vitrine é do `@copywriter`/`@gestor-trafego` e do cliente. Aqui só identifico o padrão de giro e margem.

### Candidatos a kit (handoff para @copywriter, Pilar 3)

Duas combinações nascem direto do cruzamento giro x margem, ambas na fase de estrutura/alvenaria da obra:

1. **Cimento + argamassa de assentamento/reboco.** Cimento Supremo 50kg (isca, margem 16,8%) puxa o cliente até a loja; argamassa (massa reboco cinza 20kg, margem 56,5%, ou Extrakolla 2, margem 42,2%) é o item de margem mais alta comprado na mesma etapa de obra. Kit sugerido: "cimento + argamassa" pra quem está em fase de alvenaria/reboco.
2. **Tijolo/bloco + argamassa de assentamento.** Mesmo racional: tijolo 6 furos ou bloco de concreto (giro altíssimo, margem moderada) combinado com argamassa colante de margem mais alta.

Não incluí ferro/estribo no kit porque os SKUs de estribo do relatório (`PRD00016`, `21809`) aparecem na auditoria de outliers de cadastro (custo maior que o preço de venda ou custo muito acima do padrão da família), então a margem real desses itens está incerta até o cliente corrigir o cadastro (ver `diagnostico-giro-estoque.md`).

Decisão final de composição, precificação e comunicação do kit é do `@copywriter`, aqui só aponto a oportunidade.

### Comparação com o período anterior

Primeira seção deste diagnóstico, sem período anterior pra comparar.

### Próximos passos

1. Confirmar com o cliente qual é o período real coberto pela Curva ABC (desde quando o sistema acumula esses dados).
2. Confirmar a natureza dos dois lançamentos "Plataforma" (R$ 229.423,01 somados) antes de usar faturamento total ou participação por categoria em qualquer decisão de mídia.
3. Encaminhar os 2 candidatos a kit e a lista de produtos isca para o `@copywriter` avaliar composição e copy (Pilar 3, Combo de Produtos).
4. `@analista-dados` usa faturamento por categoria e margem como KPI de dashboard quando o cliente tiver conta de mídia ativa.
5. Confirmar com o cliente se a categorização por palavra-chave usada aqui bate com a divisão real de departamentos da loja, principalmente os 93 SKUs (6,7% do faturamento sem outliers) que ficaram como "não classificado".
6. Corrigir no ERP os itens de cadastro com problema listados na auditoria de outliers do `diagnostico-giro-estoque.md` antes de fechar qualquer kit ou campanha com margem calculada.
7. Confirmar com o cliente o custo/preço do item Vermelho segurança epóxi piso Farben (código 21070, R$ 261,69 de custo x R$ 262,41 de preço, margem de 0,3%), 2º maior item de faturamento da loja com margem praticamente zero.
8. Ampliar a cobertura de margem por categoria (hoje entre 17% e 46% do faturamento por categoria) pedindo ao cliente um relatório de estoque mais recente ou mais completo, que cubra mais SKUs vendidos no acumulado.

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
