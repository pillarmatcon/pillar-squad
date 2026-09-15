# Diagnóstico de Curva ABC para Hora Z
**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra, atividade "Curva ABC do Estoque"
**Como ler este arquivo:** histórico cumulativo, uma seção por período coberto por relatório de vendas do cliente, do mais recente (topo) para o mais antigo (final), independente da ordem em que os relatórios foram processados.

## Visão geral acumulada

| Período/snapshot | Faturamento | Faturamento sem outliers | Margem % média (cruzado c/ estoque) | Concentração do grupo A |
|---|---|---|---|---|
| Acumulado até 15/09/2026 | R$ 521.254,92 | R$ 291.831,91 | 44,3% (mediana, 295 SKUs cruzados) | 1 SKU (tijolo 6 furos 24), 1,2% do valor bruto |

Primeira rodada de diagnóstico do cliente, sem período anterior para comparar tendência. Duas leituras já dão pra fixar: a loja tem uma cauda de SKU (1187 produtos vendidos no acumulado) mas a concentração de volume está em poucos itens estruturais (tijolo, bloco, cimento, ferro), e dois lançamentos isolados de "Plataforma" distorcem qualquer leitura de faturamento total se não forem tratados à parte.

---

## Período: acumulado até 15/09/2026 (período não declarado pela fonte)
**Fonte dos dados:** `Curva_Abc.xlsx`, aba "Curva ABC de Produtos por quantidade", recebido do cliente em 15/09/2026, processado em 09-2026
**Planilha(s):** `09-2026/Arquivos/15-inteligencia-dados-curva-abc-padronizada_acumulado-ate-2026-09-15.xlsx`
**Status:** v1, sujeito a refinamento

### Resumo executivo

- Faturamento total no relatório: R$ 521.254,92, em 1.187 SKUs distintos.
- Este relatório não declara o período coberto (sem data de início/fim no cabeçalho, diferente do padrão do sistema Pontual Tecnologia). Tratei como snapshot acumulado até a data de extração/recebimento do arquivo (15/09/2026), por ser a leitura mais honesta possível sem inventar corte de datas. **Preciso que o cliente confirme qual é o período real coberto** (desde a abertura da loja, desde a troca de ERP, últimos 12 meses etc.), porque isso muda completamente a leitura de "faturamento mensal médio" e de tendência.
- **A classificação ABC deste relatório é por quantidade vendida, não por faturamento.** Isso já vem explícito no nome da aba do arquivo original ("Curva ABC de Produtos por quantidade") e o efeito aparece direto no resultado: o único SKU da classe A é um tijolo cerâmico de R$ 0,95 a unidade, responsável por 21,96% de tudo que saiu da loja em unidades, mas só 1,24% do valor faturado bruto. Não misturar com uma curva ABC por valor, que teria classe A dominada pelos itens de ticket mais alto.
- **Dois lançamentos distorcem o faturamento bruto**: "Plataforma -Z-45/25J RT" (R$ 133.748,71) e "114887 - Plataforma - Z-3422 DC" (R$ 95.674,30), juntos R$ 229.423,01, quase 44% do total faturado do relatório inteiro. Cada um aparece uma única vez, com código fora do padrão usado no resto do catálogo. Não tenho como saber pela planilha se é venda de equipamento, aluguel registrado como venda ou lançamento incorreto. Todos os números de participação por categoria abaixo estão calculados com e sem esses dois lançamentos, e a leitura "sem outliers" é a que uso pra falar de mix de produto da loja. **Peço para o cliente confirmar a natureza dessas duas vendas antes de usar este relatório para decidir orçamento de mídia por categoria.**
- Categorização por palavra-chave na descrição do produto (taxonomia MatCon de `_squad/_shared/nichos.md`, fallback porque o relatório não traz categoria própria), critério auditável documentado na seção seguinte. 95 dos 1.187 SKUs (8%) não bateram com nenhuma palavra-chave e ficaram como "não classificado", a maioria peças de fixação e itens com nome abreviado demais para reconhecer com segurança.
- Sem "Grupo Z" (produtos sem venda) neste relatório: a Curva ABC do sistema desse cliente só lista quem vendeu, não existe faixa de classificação para quem não vendeu. Uso o relatório de Estoque, cruzado com este, para aproximar quem não vendeu no período, ver `diagnostico-giro-estoque.md`.

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

### Classificação ABC (por quantidade) e o que ela representa em valor

| Classe | SKUs | % do volume (quantidade) | % do faturamento (sem outliers) |
|---|---|---|---|
| A | 1 | 22,0% | 2,2% |
| B | 70 | 57,9% | 29,9% |
| C | 1.114 | 20,1% (após remover 2 outliers de C) | 67,8% |

A classe C concentra 1.114 dos 1.187 SKUs (94%) mas ainda assim responde por mais de dois terços do faturamento sem os outliers, o que é típico de loja com catálogo de cauda longa (muita peça avulsa de valor unitário maior, hidráulica e acabamento, cada uma vendendo pouca quantidade).

### Top produtos por giro (quantidade faturada)

| Código | Produto | Categoria | Classe | Quantidade | Faturamento |
|---|---|---|---|---|---|
| 22114 | Tijolo 6 furos 09x14x24 cerâmico Lorenzetti | Básico | A | 6.860 | R$ 6.452,00 |
| 20250 | Tijolo 6 furos 09x14x29 cerâmico Lorenzetti | Básico | B | 4.170 | R$ 4.229,00 |
| 21356 | Bloco concreto normal 14x19x39 | Básico | B | 1.470 | R$ 5.248,80 |
| 22501 | Tijolo de vedação 6 furos 09x14x24 | Básico | B | 838 | R$ 754,20 |
| PRD00017 | Estribo de aço 07x14cm | Básico | B | 804 | R$ 945,10 |
| PRD00045 | Cimento Supremo 50kg | Básico | B | 704 | R$ 27.868,00 |
| 1590 | Bucha plástica tijolo oco 08mm (1000) branca | Básico | B | 532 | R$ 133,00 |
| 1589 | Bucha plástica tijolo oco 06mm (1000) cinza | Básico | B | 460 | R$ 46,00 |
| 22257 | Estribo de aço 07x20cm | Básico | B | 450 | R$ 602,50 |
| 1591 | Bucha plástica tijolo oco 08mm (1000) cinza | Básico | B | 427 | R$ 64,05 |
| 21384 | Bloco estrutural 14x19x39 | Básico | B | 415 | R$ 1.737,00 |
| 4436 | Cabo de aço plastificado 3/32" 2,40mm | Básico | B | 400 | R$ 1.040,00 |

Lista completa dos 1.187 SKUs, ordenada por giro, na aba "Top 30 giro" e na aba principal da planilha padronizada.

### Top produtos por margem bruta absoluta

Cálculo cruzado com o relatório de Estoque: margem unitária pelo custo mais recente cadastrado x quantidade faturada no acumulado. Cobre só os 295 SKUs presentes nos dois relatórios (dos 1.187 da Curva ABC), é estimativa (usa o custo mais atual, não o custo real de cada venda no momento em que ocorreu).

| Código | Produto | Categoria | Quantidade | Margem % | Margem bruta estimada |
|---|---|---|---|---|---|
| PRD00045 | Cimento Supremo 50kg | Básico | 704 | 16,8% | R$ 4.692,86 |
| 22446 | Argamassa Superkola 3Mais cinza 20kg | Básico | 290 | 37,9% | R$ 3.068,20 |
| 22114 | Tijolo 6 furos 09x14x24 | Básico | 6.860 | 36,8% | R$ 2.401,00 |
| 12010 | Argamassa massa reboco cinza 20kg | Básico | 138 | 56,5% | R$ 1.708,16 |
| 20250 | Tijolo 6 furos 09x14x29 | Básico | 4.170 | 34,1% | R$ 1.564,58 |
| 22445 | Argamassa Extrakolla 2 cinza 20kg | Básico | 143 | 42,2% | R$ 1.358,50 |
| 101010 | Ferro 3/8 (12 metros) 10mm | Básico | 61 | 28,5% | R$ 1.042,49 |
| 20912 | Ferro 5/16 (12 metros) 8mm | Básico | 86 | 27,0% | R$ 946,00 |
| 21452 | Tubo esgoto 100mm 6m | Hidráulica | 26 | 33,5% | R$ 774,31 |
| 21435 | Fita crepe amarela 18x40 automotiva | Pintura | 167 | 38,7% | R$ 549,43 |

Lista completa dos 295 SKUs cruzados na aba "Top 30 margem (cruzado c. estoque)" da planilha.

### Produtos isca / âncora identificados

Cimento e tijolo aparecem nas duas pontas: giro altíssimo, margem baixa em termos percentuais (16,8% no cimento, 34-37% no tijolo, abaixo da mediana de 44,3% do catálogo cruzado). É o padrão clássico de produto isca de MatCon: material estrutural de consumo constante em qualquer obra, que traz o profissional e o consumidor final até a loja, mesmo com margem apertada.

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

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
