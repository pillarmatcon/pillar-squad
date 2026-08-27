# Diagnóstico de Estoque e Giro para Construmais
**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra
**Como ler este arquivo:** histórico cumulativo, uma seção por período coberto por relatório do cliente, do mais recente (topo) para o mais antigo (final), independente da ordem em que os relatórios foram processados.

**Nota de divisão do arquivo (26/08/2026):** o `_squad/06-inteligencia-dados/SKILL.md` atual separa Curva ABC e Giro de Estoque/Margem em dois arquivos (`diagnostico-curva-abc.md` e `diagnostico-giro-estoque.md`), mas este arquivo combinado é anterior a essa divisão e ainda não foi migrado. A partir de 26/08/2026, análises novas de giro/estoque (classificação por bucket de dias sem venda, matriz giro x margem etc.) passam a entrar em `diagnostico-giro-estoque.md`, criado nesta data. Este arquivo (`diagnostico-estoque.md`) segue sendo a fonte de verdade de tudo que já estava aqui (4 períodos de Curva ABC, auditoria de cadastro e outliers do snapshot de 03/08/2026) até uma migração completa pra estrutura dividida, que fica proposta como tarefa separada, sem data definida ainda.

**Nota de revisão (25/07/2026):** a versão anterior deste arquivo (mesma data) foi calculada com um bug no script de padronização, que descartava silenciosamente os 2 primeiros produtos de cada página do PDF nas partes 2, 3 e 4 (perda de ~15% do catálogo e ~12% do faturamento nesses períodos, a parte 1 não era afetada). O bug foi corrigido (`pillar_padroniza_curva_abc.py`, cobertura agora conferida automaticamente contra o "Total Geral" oficial impresso em cada relatório, 100% de cobertura nos 4 períodos) e as planilhas de origem foram regeradas. **Os números abaixo são os corretos.** Como efeito colateral bom: o faturamento e a margem agregada dos 14 meses agora batem exatamente com o diagnóstico anterior de 23/07 (`outputs/07-2026/Analises/23-diagnostico-estoque.md`), o que resolve a contradição registrada no Histórico do `CLIENTE.md`.

**Nota de reconciliação do estoque parado (25/07/2026):** o "Estoque parado corrigido" na tabela abaixo, um valor por período, é o que dava pra calcular só com os 4 PDFs de Curva ABC, e tem uma limitação importante: os 4 relatórios foram todos gerados na mesma semana (27/06 a 03/07/2026), então o campo de estoque de cada um reflete o estoque de **quando o relatório foi emitido**, não do fim do período de venda que ele cobre. Ou seja, a "evolução" desse número entre períodos reflete principalmente quais produtos entram ou saem da lista conforme a janela de venda comparada muda, não uma trajetória real de estoque acumulando ao longo de 14 meses. Depois de receber `Estoque em 27-06-26.xls` (exportação original do sistema, com estoque de todos os 15.228 produtos numa única data certa), cruzei esse arquivo com a venda somada dos 4 relatórios de Curva ABC e cheguei no número correto de estoque parado real: **1.695 produtos sem nenhuma venda registrada nos 14 meses inteiros (mai/2025 a jun/2026), R$ 295.126,57 a custo** (já com a correção do colorante aplicada). Esse número bate próximo do R$ 320.903,02 do diagnóstico de 23/07 (diferença de ~8%, provavelmente porque aquela análise também corrigiu outros itens de custo além do colorante).

**Nota de atualização de estoque (03/08/2026), substitui a referência acima:** novo snapshot de estoque (`Produto em 03-08-26.htm`, exportação direta do sistema Pontual, 15.369 SKUs) cruzado com a mesma venda somada dos 4 períodos de Curva ABC. Estoque parado real atualizado: **1.732 produtos, R$ 373.769,46 a custo** (alta de R$ 78.642,89 / +26,6% em valor frente ao R$ 295.126,57 de 25/07/2026, com apenas 37 SKUs a mais no grupo parado, +2,2%, ou seja o valor médio por item parado subiu mais que a quantidade de itens). Esse novo relatório trouxe também **2 outliers críticos de cadastro não vistos antes**, com quantidade ou custo em forte desacordo com os pares da própria linha de produto (`CABO FLEX 2.5MM AZ PC COBRECOM`, código 7153, quantidade 79.263,9 PC contra pares entre 0 e 635 MT/PC da mesma linha; `MANGUEIRA CORRUGADA 20MM AM - KRONA`, código 7874, quantidade e custo fora do padrão). Já excluídos do número acima, ver seção "Atualização de Estoque: 03/08/2026" abaixo para o detalhe completo. **Use R$ 373.769,46 como referência de estoque parado do negócio a partir de agora**, não os valores por período da tabela abaixo (mantidos só pra referência histórica) nem o R$ 295.126,57 de 25/07 (desatualizado, mas preservado acima por transparência do histórico).

**Nota de confirmação do Tony (26/08/2026):** o Tony confirmou verbalmente a natureza de 7 itens que apareciam nas listas de estoque parado ou de achados pendentes de confirmação (ver detalhe cruzado nas seções "Maiores itens parados individuais" e "Achados extras confirmados nesta rodada" abaixo). Ainda não houve reprocessamento de dado, só registro da confirmação qualitativa:
- **Cumeeira:** vendida por encomenda, não é estoque parado real (item não deveria ser lido como giro zero problemático)
- **Vareta (Solda Oxi):** gira muito pouco, confirma que é slow-mover genuíno, não erro de leitura
- **Sacolas:** usadas para ensacar areia e brita (uso interno/operacional da loja, não item de revenda com markup normal)
- **Tubo (PVC Rosca):** produto de giro baixo, confirmado pelo Tony. Removido da lista de pendências de confirmação (ver "Achados extras confirmados nesta rodada" abaixo)
- **Metalon 30x20:** estoque zerado, é furo de estoque (perda/discrepância, não erro de cadastro) — item novo, ainda sem código/valor cruzado neste diagnóstico
- **Torneira:** é furo de estoque (mesma natureza do Metalon) — item novo, ainda sem código/valor cruzado neste diagnóstico
- **Tela:** temos em estoque, material de baixo giro — item novo, ainda sem código/valor cruzado neste diagnóstico

## Visão geral acumulada (mai/2025 a jun/2026, 4 períodos processados)
*(atualizar este bloco a cada novo período processado, não é seção fixa)*

| Período | Meses | Faturamento | Média mensal | Margem % | Grupo A (% fat.) | Estoque parado (snapshot do período, ver nota acima) |
|---|---|---|---|---|---|---|
| 01/05/2025 a 31/10/2025 | 6 | R$ 1.377.269,74 | R$ 229.544,96 | 35,93% | 59,87% (66 SKUs) | R$ 424.367,42 |
| 01/11/2025 a 31/12/2025 | 2 | R$ 454.844,56 | R$ 227.422,28 | 41,82% | 59,97% (35 SKUs) | R$ 467.599,36 |
| 01/01/2026 a 31/03/2026 | 3 | R$ 598.882,79 | R$ 199.627,60 | 45,14% | 59,89% (63 SKUs) | R$ 491.900,30 |
| 01/04/2026 a 30/06/2026 | 3 | R$ 650.821,13 | R$ 216.940,38 | 39,17% | 59,98% (48 SKUs) | R$ 469.329,89 |
| **Total / média 14 meses** | 14 | **R$ 3.081.818,22** | **R$ 220.129,87** | **39,27%** | ~59,9% (estável) | **R$ 373.769,46 (real, 1.732 SKUs, snapshot 03/08/2026, ver nota)** |

O total de 14 meses bate exato com o diagnóstico de 23/07 (R$ 3.081.818,22, margem 39,27%), única vez em que essa reconciliação foi possível porque os dois usaram a mesma fonte (os 4 PDFs originais), só que com scripts diferentes. Faturamento, margem e giro não foram recalculados desde jun/2026: o relatório mais recente recebido (03/08/2026) é um snapshot de estoque, sem dado de venda, ver seção "Atualização de Estoque: 03/08/2026" abaixo.

Seis leituras que só aparecem quando os períodos e snapshots são vistos juntos:

1. **Faturamento mensal médio ficou estável entre o 1º e o 2º período** (R$ 229,5 mil → R$ 227,4 mil, -0,9%), **caiu de forma real só no 3º período** (R$ 227,4 mil → R$ 199,6 mil, -12,2%) **e recuperou no período mais recente** (R$ 199,6 mil → R$ 216,9 mil, +8,7%). Não é uma tendência de queda contínua, é um trimestre mais fraco isolado (jan-mar/2026) seguido de recuperação parcial.
2. **Margem subiu período a período até o pico em jan-mar/2026** (35,93% → 41,82% → 45,14%) **e caiu 5,97 pontos no trimestre mais recente** (45,14% → 39,17%). É a maior queda de margem entre dois períodos de todo o histórico, vale investigar.
3. **Grupo A concentra 59,87% a 59,98% do faturamento nos 4 períodos, uma estabilidade notável** (variação de menos de 0,2 ponto percentual entre o período mais alto e o mais baixo), sempre abaixo da faixa saudável de referência do método (70 a 85%). Não é oscilação, é um padrão estrutural muito consistente da loja: o negócio depende de uma base de produtos mais larga do que o ideal pra sustentar o faturamento.
4. **Cimento Montes Claros e Cimento Poty são produto isca nos 4 períodos, sem exceção**, e seguem com custo/preço/margem cadastrados estáveis no snapshot de 03/08/2026 (ver seção mais recente). Nenhum outro item se repete como isca validado em todas as janelas. É a base mais sólida pro Kit Fundação e Alvenaria sugerido abaixo.
5. **Estoque parado real atualizado em 03/08/2026: R$ 373.769,46 em 1.732 produtos** (era R$ 295.126,57 em 1.695 produtos em 25/07/2026, alta de 26,6% em valor com só 2,2% mais itens, ver nota de atualização acima). Os valores "por período" na tabela acima não devem ser lidos como uma tendência de crescimento ou queda, pelo motivo explicado na nota de reconciliação de 25/07.
6. **2 itens do relatório de 03/08/2026 têm quantidade ou custo em forte desacordo com os pares da própria linha de produto** (cabo flex e mangueira corrugada, ver seção mais recente), somando R$ 17,46 milhões que já foram excluídos de todos os números acima. Pendente de confirmação do Tony antes de tratar como estoque real, ver auditoria completa abaixo.

---

## Atualização de Estoque: 03/08/2026 (snapshot, fora do ciclo de Curva ABC)
**Fonte dos dados:** `Produto em 03-08-26.htm` (sistema Pontual Tecnologia, exportação HTML de tabela de produto), processado em 08-2026
**Planilha:** `08-2026/Arquivos/03-inteligencia-dados-estoque-auditado_2026-08-03.xlsx` (abas: Estoque padronizado, Estoque parado (ajustado), Outliers críticos)
**Status:** v1, sujeito a refinamento
**Tipo de relatório:** diferente dos 4 períodos abaixo. É um snapshot de produto/estoque (quantidade, custo, preço e margem cadastrados numa data única), não uma Curva ABC de vendas. Confirmado pela estrutura do arquivo (colunas Código, Dt. Compra, Produto, Fabricante, Unid. Estoque, Qtde., Custo inicial, % ICMS/IPI/ST/FRETE/OUTROS, Custo Final, % Margem, Preço, NCM, Código de Barras, Fornecedor, Qtde. última compra): não tem quantidade vendida nem faturamento, então **não atualiza giro nem participação por categoria de faturamento nesta rodada**. Formato HTML, não PDF, então não passa pela ferramenta de padronização de Curva ABC (`Operacional/Método Viga Mestra/1 - Inteligência de Dados/1 - Curva ABC do Estoque/SKILL.md`), que é específica pra PDF de Curva ABC; processado com parser próprio (regex determinístico, zero IA na extração).

### Resumo executivo
- Catálogo no relatório: **15.369 SKUs** (contra 15.254 SKUs distintos no histórico dos 4 períodos de Curva ABC, mai/2025 a jun/2026: 115 SKUs novos, sem histórico de venda pra avaliar)
- Valor de estoque a custo, leitura bruta (direto do relatório, todos os itens com saldo positivo): **R$ 19.111.367,72** em 4.848 SKUs
- **2 itens sozinhos respondem por R$ 17.456.023,32 (91,3%) desse valor bruto**, com quantidade/custo em forte desacordo com os pares da própria linha de produto. Somado a um terceiro item recorrente (colorante, já conhecido desde 23/07), os 3 outliers somam **R$ 18.176.265,52 (95,1%) do valor bruto total**
- **Valor de estoque a custo, leitura ajustada (excluindo os 3 outliers): R$ 935.102,19**, crescimento de R$ 34.161,81 (+3,79%) frente aos R$ 900.940,38 registrados em 25/07/2026 (`Estoque em 27-06-26.xls`), variação plausível para 5 semanas de operação
- Estoque parado atualizado (sem venda nos 4 períodos históricos, ajustado): **R$ 373.769,46 em 1.732 SKUs** (detalhe na seção própria abaixo)
- Nenhum dado de faturamento, giro ou participação por categoria de venda foi recalculado nesta rodada, esse relatório não traz essa informação

### Limitações da fonte de dados
1. **Sem dado de venda/faturamento.** Este relatório só traz estoque, custo e preço cadastrados. Giro (quantidade vendida) e participação por categoria de faturamento continuam sendo os do período 01/04/2026 a 30/06/2026 (ver seção abaixo), não foram atualizados.
2. **Sem coluna de categoria própria.** Ao contrário do `Estoque ETL.xlsx` usado em 23/07, este relatório não tem campo de categoria/grupo. Mapeei a categoria por cruzamento do `codigo` com o campo `grupo_produto` da Curva ABC mais recente (abr-jun/2026), cobrindo 15.217 dos 15.369 SKUs (99,0%). Os 152 SKUs sem categoria mapeada (0,99% dos itens, R$ 7.856,01 do valor bruto de estoque) são majoritariamente SKUs novos, criados depois de jun/2026.
3. **Categoria corrompida no cadastro do cliente, mesmo problema já reportado em 25/07/2026.** Via o cruzamento acima, 5.254 SKUs do relatório atual mapeiam para a categoria corrompida "MD-MD-MD-MD-MD-...". Segue pendente de correção no ERP do cliente.
4. **2 outliers críticos de cadastro identificados nesta rodada, não vistos nos relatórios anteriores** (ver auditoria abaixo). Excluídos de todos os totais "ajustados" deste diagnóstico até confirmação do Tony.

### Auditoria de qualidade do cadastro (15.369 SKUs)
| Achado | Quantidade | Observação |
|---|---|---|
| Fornecedor cadastrado como a própria loja | 59 | Era 57 em 23/07/2026 (`Estoque ETL.xlsx`) |
| Quantidade em estoque negativa | 42 itens, R$ -18.713,82 a custo | Era 17 itens, R$ -139.191,14 em 23/07/2026. Maior caso: Tijolo c/8 furos, -11.320 un, R$ -9.056,00 |
| Preço de venda zerado com estoque ativo (qtde > 0) | 4 | Mesmos 4 de 23/07/2026: itens de mobiliário/exposição de loja (gôndola, expositor), não mercadoria de revenda |
| Custo final zerado com estoque ativo (qtde > 0) | 7 | Métrica nova (23/07 media "custo zerado com venda ativa", 1 item, critério diferente por falta de dado de venda) |
| Margem (markup sobre custo) acima de 1.000% | 24 | Era 27 em 23/07/2026 |
| Margem (markup sobre custo) negativa | 198 | Era 199 em 23/07/2026, estável |
| Custo final menor que custo inicial | 956 | 91,8% (878 itens) com diferença ≤ 5%, plausível efeito de imposto/desconto sobre o custo. 29 itens com diferença > 30%, quase todos por custo final zerado (já contam na linha acima) |
| Nome de produto duplicado em código diferente | 8 grupos, 20 códigos | Era 10 grupos, 24 códigos em 23/07/2026. Inclui 2 tipos de cimento cadastrados em 4 códigos cada (`CP II F 40 ZEBU`, `CP II-Z-32 CIMPOR`), provavelmente lotes/entradas diferentes do mesmo produto |
| Inconsistência entre % Margem cadastrado e o recálculo (Preço-Custo Final)/Custo Final, tolerância 2 pontos percentuais | 387 | Métrica nova nesta rodada (tolerância não usada antes) |
| Sem data de compra cadastrada | 5.979 | Métrica nova nesta rodada, 38,9% do catálogo |

Nota sobre o campo "% Margem" deste relatório: é **markup sobre custo** ((Preço - Custo Final) / Custo Final × 100), cadastrado pelo próprio sistema Pontual. Não é o mesmo cálculo de "margem bruta % sobre venda" usado nas seções de Curva ABC abaixo (que é sobre faturamento real). Os dois não devem ser comparados diretamente.

### Detalhamento da auditoria de qualidade do cadastro, por categoria de erro (refinamento de 11/08/2026)
Aprofundamento da tabela acima, produto a produto, gerado direto da aba "Estoque padronizado" do arquivo `08-2026/Arquivos/03-inteligencia-dados-estoque-auditado_2026-08-03.xlsx` (15.369 SKUs). Os totais por categoria já publicados na tabela acima não mudam, este bloco só detalha os casos mais relevantes de cada um, priorizados por impacto financeiro e por quão implausível é o valor cadastrado. Não é uma listagem exaustiva (a coluna "Quantidade" da tabela acima segue sendo a contagem oficial de cada achado).

Para os casos de custo, preço ou margem suspeitos, apliquei a mesma metodologia já usada nos 3 outliers críticos (seção abaixo): busquei produtos da mesma linha (mesmo nome base, mesma marca quando possível, mesma unidade de estoque) dentro do próprio relatório, antes de estimar um valor correto. Casos que são puramente estruturais (fornecedor, nome duplicado, quantidade negativa) não têm "valor correto" a estimar por benchmark, só reporto o valor cadastrado e o problema.

**1. Fornecedor cadastrado como a própria loja (59 itens na tabela oficial)**
Busca direta pelo texto exato do fornecedor "CONSTRUMAIS MATERIAL DE CONSTRUCAO" encontrou 57 dos 59 registrados na contagem oficial (pequena diferença provavelmente por variação de grafia não capturada pela busca exata, não investigada a fundo). Impacto financeiro é baixo: só 4 dos 57 têm estoque ativo (qtde > 0), somando R$ 88,32 a custo. Não é erro de valor, é erro de cadastro (a loja aparece como fornecedora de si mesma, provavelmente entrada de ajuste de estoque ou devolução lançada errado).

| Código | Produto | Campo suspeito | Valor cadastrado | Observação |
|---|---|---|---|---|
| 6528 | COMANDO ARTICULAVEL LADO ESQUERDO ANTIQUE ISERO | Fornecedor | CONSTRUMAIS MATERIAL DE CONSTRUCAO | Qtde 4, custo R$ 10,00, valor R$ 40,00. Maior caso por valor |
| 7736 | LUMINARIA QUADRADA LED SOBREPOR 12W-6000K INITIAL | Fornecedor | CONSTRUMAIS MATERIAL DE CONSTRUCAO | Qtde 1, custo R$ 23,00 |
| 8328 | PONTEIRA EXT PVC 5/8 PT 1025002001 CRIATIV | Fornecedor | CONSTRUMAIS MATERIAL DE CONSTRUCAO | Qtde 130, custo R$ 0,13, valor R$ 16,90 |
| 1702 | MEC P/CX DESCARGA C15/C17 K15 ASTRA | Fornecedor | CONSTRUMAIS MATERIAL DE CONSTRUCAO | Qtde 1, custo R$ 8,42 |
| Demais 53 itens | Diversos | Fornecedor | CONSTRUMAIS MATERIAL DE CONSTRUCAO | Todos com qtde = 0, sem exposição financeira. Ver planilha para lista completa |

**2. Quantidade em estoque negativa (42 itens, R$ -18.713,82 a custo na tabela oficial)**
Fisicamente impossível (não existe estoque negativo). Não dá pra benchmarkar "quantidade correta" com os pares, o problema é a entrada de saída/venda sem entrada de compra correspondente no sistema, não um valor de custo errado. Top 10 por valor negativo:

| Código | Produto | Campo suspeito | Valor cadastrado | Divergência (R$) | Observação |
|---|---|---|---|---|---|
| 48 | TIJOLO C/8 FUROS 09X19X19 | Quantidade | -11.320 un | R$ -9.056,00 | Já citado na tabela oficial como maior caso. Item de giro altíssimo (ver Curva ABC abaixo), provável saída lançada sem a entrada de compra correspondente |
| 2796 | LAJE PREMOLDADA EM TRELICA TG-8 | Quantidade | -93 un | R$ -4.092,00 | |
| 7459 | PISO INTERTRAVADO NATURAL 10X20X6CM 25MPA | Quantidade | -30 un | R$ -1.290,00 | |
| 118 | PEDRA RACHINHA FRIA IRREGULAR | Quantidade | -59 un | R$ -1.062,00 | |
| 8626 | LAVATORIO INOX COLETIVO 1MT C/BANCADA P/2 TORNEIRAS | Quantidade | -1 un | R$ -825,60 | |
| 16261 | COLUNA FERRO 3/8 10.00MM 08X20 C/04 FERROS | Quantidade | -18 un | R$ -540,00 | Sem categoria mapeada |
| 16262 | COLUNA FERRO 1/2 12.50MM 10X30 C/06 FERROS | Quantidade | -6 un | R$ -420,00 | Sem categoria mapeada |
| 7204 | PISO PREMOLDADO 40X40 M2 | Quantidade | -18 un | R$ -396,00 | |
| 5976 | CUBA EMB OVAL LOUCA 37.50X48.50 L37.17 BR DECA | Quantidade | -2 un | R$ -279,80 | |
| 4215 | FORRA ADUELA SUCUPIRA 2.10X0.90 | Quantidade | -1 un | R$ -150,00 | |

**3. Preço de venda zerado com estoque ativo (4 itens, todos já conhecidos)**
| Código | Produto | Campo suspeito | Valor cadastrado | Observação |
|---|---|---|---|---|
| 9367 | Conj. Com. Desmontado-Gondola | Preço | R$ 0,00 | Mobiliário/exposição de loja, não é mercadoria de revenda. Custo R$ 0,00 também (ver categoria 4) |
| 9504 | Expositor Aramado Ilha ASTRA | Preço | R$ 0,00 | Mesma natureza (exposição) |
| 9449 | EXPOSITOR MULTIFUNCIONAL GR ATLAS | Preço | R$ 0,00 | Mesma natureza (exposição) |
| 9463 | GONDOLA EXPOSITORA MOVEL CAIXA C/1 PECA | Preço | R$ 0,00 | Custo cadastrado R$ 856,64, é o único dos 4 com custo positivo. Também aparece na categoria "margem negativa" abaixo pelo mesmo motivo |

**4. Custo final zerado com estoque ativo (7 itens)**
| Código | Produto | Campo suspeito | Valor cadastrado | Observação |
|---|---|---|---|---|
| 4577 | ARRUELA PRESSAO MEDIA ZINC 3/16 BELENUS | Custo final | R$ 0,00 | Qtde 83, preço R$ 0,10 cadastrado, sem custo pra calcular margem |
| 11871 | ENXADA ACO 2.5LB EST CONST S/CB 77220/254 TRAMONTINA | Custo final | R$ 0,00 | Qtde 2, preço R$ 45,00. Custo inicial cadastrado era R$ 28,64, então o valor correto provavelmente é próximo disso, não R$ 0,00 (ver também categoria 7 abaixo) |
| 1813 | BORRACHA SILICONIZADA | Custo final | R$ 0,00 | Qtde 10, preço R$ 2,00 |
| 7300 | ABRACADEIRA NYLON PT 200X3.50 ENERBRAS | Custo final | R$ 0,00 | Qtde 0,22, preço R$ 0,20. Baixíssimo impacto |
| 9367, 9504, 9449 | Itens de mobiliário/exposição já citados na categoria 3 | Custo final | R$ 0,00 | Mesma natureza, não é mercadoria de revenda |

**5. Margem (markup sobre custo) acima de 1.000% (24 itens, 1 já conhecido: código 7874, mangueira corrugada, ver seção de outliers críticos abaixo)**
Dos 23 restantes, a maioria tem qtde = 0 (sem exposição financeira hoje, mas cadastro errado por igual). Nos casos com par direto na mesma linha, o benchmark aponta forte para erro de custo (valor perdeu dígitos ou casas decimais), não de preço:

| Código | Produto | Campo suspeito | Valor cadastrado | Benchmark de pares (mesma linha) | Estimativa | Divergência |
|---|---|---|---|---|---|---|
| 3214 | TUBO PVC ROSCA 1 POL TIGRE | Custo final ou preço (não conclusivo) | Custo R$ 8,06, preço R$ 96,00, markup 1.091% | Outros "Tubo PVC Rosca" Tigre/Krona no relatório têm markup entre 66% e 102% (1/2 Tigre: custo R$ 69,98/preço R$ 125; 3/4 Tigre: R$ 13,84/R$ 28; 1.1/2 Tigre: R$ 108,16/R$ 180; 2 pol Tigre: R$ 162,23/R$ 270; 1/2 Krona: R$ 7,29/R$ 14). É a única peça de 1 polegada da linha, então não há um par exato do mesmo diâmetro pra comparar direto | Duas hipóteses possíveis, benchmark não resolve qual: (a) se o preço R$ 96,00 estiver certo, o custo correto ficaria entre R$ 48 e R$ 60 (markup de 60 a 100% igual aos pares); (b) se o custo R$ 8,06 estiver certo, o preço correto ficaria entre R$ 13 e R$ 16. A quantidade em estoque (999,83 PC) também é muito maior que qualquer par da mesma linha (0 a 6 PC), o que sugere que pode haver também um problema de quantidade lançada, não só de preço/custo | Estoque a custo hoje: R$ 8.058,63 (999,83 x R$ 8,06). Se a hipótese (a) estiver certa, o valor real seria R$ 48.000 a R$ 60.000, quase 6 a 7 vezes mais |
| 9813 | CABO RIGIDO 10.0MM AZ 1KVA SIL | Custo final | R$ 9,06 (preço R$ 1.350,00, markup 14.801%) | Mesmo item, cor diferente: CABO RIGIDO 10.0MM PT 1KVA SIL (código 7189), custo R$ 918,00, preço R$ 1.350,00 (idêntico), markup 47,06% | Custo correto provavelmente próximo de R$ 918,00. Padrão sugere erro de digitação (R$ 9,06 em vez de R$ 906,00, faltam 2 zeros) | Qtde em estoque = 0, sem exposição financeira hoje, mas cadastro errado |
| 3533 | CORDAO PARALELO 2X1.00MM COBRECOM | Custo final | R$ 1,67 (preço R$ 240,00, markup 14.271%) | Outros "Cordão Paralelo" Cobrecom vendidos em PC (rolo), por bitola: 0,50mm R$ 93,08/R$ 140; 0,75mm R$ 132,13/R$ 195; 1,50mm R$ 232,19/R$ 340. Interpolando pela bitola, 1,00mm ficaria na faixa R$ 150 a R$ 180 de custo | Custo correto estimado entre R$ 150,00 e R$ 180,00, não R$ 1,67. Preço R$ 240,00 está coerente com o padrão da linha (markup de 33 a 55% nos pares em PC) | Qtde 98,9892 PC, valor a custo hoje R$ 165,31. Se corrigido, valor passaria para algo entre R$ 14.848 e R$ 17.818, também bem mais alto |
| 11906 | ABRACADEIRA NYLON PT 140X3,50 FOXLUX | Custo final ou preço | R$ 0,09 (preço R$ 17,00, markup 19.174%) | Mesma linha, mesma marca: ABRACADEIRA NYLON PT 140X2,50 FOXLUX (custo R$ 0,07/preço R$ 0,15) e ABRACADEIRA NYLON BR 140X3.50 FOXLUX (custo R$ 0,06/preço R$ 0,15) | Preço correto provavelmente R$ 0,15 a R$ 0,20, não R$ 17,00 (custo R$ 0,09 está coerente com a linha) | Qtde 7,02, valor de venda potencial cadastrado hoje R$ 119,34, valor real estimado R$ 1,05 a R$ 1,40 |
| 2190 | ABRACADEIRA NYLON PT 80X2.50 BRASFORT | Custo final | R$ 0,02 (preço R$ 5,00, markup 24.900%) | Mesmo produto, cor branca: ABRACADEIRA NYLON BR 80X2.50 BRASFORT (código 3317), custo R$ 2,19, preço R$ 5,00 (idêntico). O próprio campo "custo inicial" deste item já registra R$ 2,36, também compatível | Custo correto provavelmente entre R$ 2,19 e R$ 2,36, não R$ 0,02. Caso claro de custo final zerado por engano, o custo inicial da própria linha confirma a faixa | Qtde 0, sem exposição financeira hoje |
| 13591 | DOBRADICA PRESSAO 26MM CURVA C/CALCO METAL ALBRAS | Custo final | R$ 0,03 (preço R$ 4,00, markup 12.479%) | Mesma marca, variante plástica: DOBRADICA PRESSAO 26MM CURVA PLASTICA ALBRAS (código 13588), custo R$ 2,31, preço R$ 5,00. Outras dobradiças de pressão 26mm curva no catálogo (Jomarca, Power, Bendoor): custo entre R$ 1,11 e R$ 2,72 | Custo correto estimado entre R$ 1,96 e R$ 2,72, ponto médio próximo de R$ 2,30 | Qtde 1, valor a custo hoje R$ 0,03, valor real estimado R$ 2,30 |
| 9002 | MADEIRA SERRADA DE PINUS | Preço | R$ 3.214,29 (custo R$ 10,60, markup 30.223%) | Nenhum outro "Madeira Serrada" no relatório pra comparar. Preço muito acima de qualquer produto de madeira do catálogo | Não estimo valor correto por falta de comparável interno. Sinalizo como implausível e recomendo checagem direta com o Tony antes de pesquisar preço de mercado | Qtde 0, sem exposição financeira hoje |
| 9876 | ESPACADOR NIVELADOR PISO 2MM KALA | Preço | R$ 30,00 (custo R$ 0,11, markup 27.173%) | Mesma marca, espessura diferente: ESPACADOR NIVELADOR PISO 1MM KALA (código 7380), custo R$ 0,11 (idêntico), preço R$ 0,30 | Preço correto provavelmente R$ 0,30, não R$ 30,00 (aparenta ser um zero a mais digitado) | Qtde 0, sem exposição financeira hoje |

**6. Margem (markup sobre custo) negativa (198 itens, achado já publicado)**
190 dos 198 têm qtde = 0 ou negativa, sem exposição financeira real hoje (cadastro errado, mas não afeta o caixa enquanto não repuser estoque). Os 8 itens com estoque ativo somam R$ 951,20 de perda potencial (qtde x (custo final - preço), o quanto a loja perderia se vendesse hoje ao preço cadastrado):

| Código | Produto | Campo suspeito | Valor cadastrado | Divergência | Observação |
|---|---|---|---|---|---|
| 9463 | GONDOLA EXPOSITORA MOVEL CAIXA C/1 PECA | Preço | Custo R$ 856,64, preço R$ 0,00 | Perda potencial R$ 856,64 | Já citado na categoria 3, mobiliário de exposição, não mercadoria de revenda |
| 7107 | PARAFUSO MOVEIS MADEIRA SOFT 13 DS 7X90 PS BC CISER | Custo ou preço | Custo R$ 4,29, preço R$ 0,70, qtde 21 | Perda potencial R$ 75,39 | Sem par direto de mesma bitola/marca no relatório pra benchmark, baixa materialidade |
| 11324 | BUCHA NYLON 12 GESSO C/ ANEL RIBEIRO | Custo ou preço | Custo R$ 1,13, preço R$ 1,00, qtde 69 | Perda potencial R$ 8,97 | Divergência pequena (11,8%), pode ser arredondamento de preço promocional, não necessariamente erro de cadastro |
| 9363 | TEL CEL SAMS GLX A205G PTO-SP | Preço | Custo R$ 855,68, preço R$ 850,00 | Perda potencial R$ 5,68 | Item fora do mix típico da loja (celular usado, provável troca ou entrada atípica), não é material de construção |
| 7112 | REBITE ALUM 3.2X06MM CISER | Custo ou preço | Custo R$ 0,36, preço R$ 0,05, qtde 7 | Perda potencial R$ 2,17 | Baixa materialidade |
| 7090 | PARAFUSO PH CB CHATA RI ZINC 2.9X16 CISER | Custo ou preço | Custo R$ 0,33, preço R$ 0,10, qtde 5 | Perda potencial R$ 1,15 | Baixa materialidade |
| 6990 | ESPACADOR NIVELADOR PISO 1MM MOLDIMPLAS | Custo ou preço | Custo R$ 0,63, preço R$ 0,25, qtde 2 | Perda potencial R$ 0,76 | Comparado com a linha Kala/Roma de mesmo produto (custo R$ 0,11 a R$ 6,17 conforme embalagem), a faixa é muito variável pra apontar um valor único, baixa materialidade |
| 7089 | PARAFUSO PH CB CHATA RI ZINC 2.9X13 CISER | Custo ou preço | Custo R$ 0,32, preço R$ 0,10, qtde 2 | Perda potencial R$ 0,44 | Baixa materialidade |

**7. Custo final menor que custo inicial, diferença acima de 30% (29 itens dos 956 totais, achado já publicado)**
Só 4 desses 29 têm estoque ativo (qtde > 0), os outros 25 são catálogo zerado:

| Código | Produto | Campo suspeito | Custo inicial | Custo final | Divergência | Observação |
|---|---|---|---|---|---|---|
| 7255 | CABO FLEX PP 2X4.00MM MT COBRECOM | Custo final | R$ 7,60 | R$ 0,01 | -99,9% | Mesmo item já detalhado na categoria 5 (margem >1.000%). Par direto: CABO FLEX PP 2X4.00MM MT MEGATROM, custo R$ 9,35. Custo correto provavelmente próximo de R$ 9,00 a R$ 10,00, coerente também com o custo inicial de R$ 7,60 |
| 9487 | BARRAMENTO NEUTRO/TERRA DIN OU NEMA MECTRO | Custo final | R$ 6,16 | R$ 4,00 | -35,1% | Qtde 1, valor R$ 4,00. Diferença mais moderada que os outros casos, pode ser desconto real de compra, não necessariamente erro |
| 11871 | ENXADA ACO 2.5LB EST CONST S/CB 77220/254 TRAMONTINA | Custo final | R$ 28,64 | R$ 0,00 | -100,0% | Qtde 2. Também aparece na categoria 4 (custo zerado). Custo correto provavelmente próximo do custo inicial, R$ 28,64 |
| 7300 | ABRACADEIRA NYLON PT 200X3.50 ENERBRAS | Custo final | R$ 0,08 | R$ 0,00 | -100,0% | Qtde 0,22, valor irrisório |

**8. Nome de produto duplicado em código diferente (8 grupos, 20 códigos, achado já publicado)**
| Categoria do erro | Produto | Códigos | Observação |
|---|---|---|---|
| Nome duplicado | CP II F 40 ZEBU SACO 50KG | 6033, 6035, 6037, 6039 | Custo idêntico nos 4 (R$ 15,49), qtde 0 em todos. Provavelmente lotes/entradas diferentes do mesmo cimento, já citado na tabela oficial |
| Nome duplicado | CP II-Z-32 CIMPOR USO GERAL SACO 50KG | 6032, 6034, 6036, 6038 | Custo idêntico nos 4 (R$ 15,20), qtde 0 em todos |
| Nome duplicado | CP II F 40 ZEBU SACO 50KG (2 códigos) | 1696, 6406 | BASCULANTE ALUMINIO 0.40X0.60, custo idêntico (R$ 37,70) |
| Nome duplicado | BOTA BORRACHA PT SOLA AMARELA CANO MEDIO 4 | 10290, 6360 | Custo idêntico (R$ 20,93) |
| Nome duplicado | BROCA CONCRETO SDS PLUS 08MMX210MM IRWIN | 4630, 7053 | Custos diferentes entre os 2 códigos (R$ 13,74 e R$ 5,91), maior divergência dos 8 grupos, vale checar se são lotes de fornecedores diferentes ou erro de cadastro em um dos 2 |
| Nome duplicado | PAREDEX VINIL ACRILICA CONCRETO 3.6L | 4878, 7703 | Custos diferentes (R$ 16,95 e R$ 22,45) |
| Nome duplicado | POP ACRILICO CONCRETO INT/EXT GL 3.6L | 5582, 8362 | Custos diferentes (R$ 18,29 e R$ 22,53) |
| Nome duplicado | VALVULA PIA AMER MET CROM 3.1/2 X7/8 1623 | 10429, 10795 | Custos diferentes (R$ 17,13 e R$ 11,92) |

**9. Inconsistência entre % Margem cadastrado e o recálculo (Preço-Custo Final)/Custo Final, tolerância 2 pontos percentuais (387 itens, 2 já conhecidos: mangueira corrugada código 7874 e colorante código 11073, ver seção de outliers críticos abaixo)**
Dos 385 restantes, a soma de valor a custo é R$ 40.900,03. É a categoria com o achado extra mais relevante desta rodada: o caso das sacolas trazido no início desta análise.

| Código | Produto | Campo suspeito | Valor cadastrado | Benchmark de pares (mesma linha) | Estimativa | Divergência |
|---|---|---|---|---|---|---|
| 11022 | SACOLAS 30X40 IMP | Custo final (não o preço) | Custo R$ 11,66, preço R$ 0,20 (mesma unidade UN nos dois casos) | O item irmão direto na mesma família de nome e mesma unidade (UN) é SACOLAS 40X50 IMP (código 11023), custo R$ 0,15, preço R$ 0,40. A família "Sacola Reciclada" tem custo R$ 11 a R$ 16, mas é vendida por KG, não por UN, então não é o par correto aqui | O benchmark aponta o oposto da hipótese inicial: não é o preço que está baixo demais, é o **custo** que está alto demais. Custo correto provavelmente entre R$ 0,15 e R$ 0,30 por unidade (mesma ordem de grandeza do irmão 40x50), não R$ 11,66. Ao custo correto, o preço R$ 0,20 fica plausível (markup positivo pequeno, coerente com sacola de baixo valor) | Qtde 2.005 un, valor a custo hoje R$ 23.378,30 (já contabilizado como um dos maiores itens de estoque parado no relatório). Se corrigido, o valor cairia para algo entre R$ 300 e R$ 600, uma diferença de mais de R$ 22.000 |
| 11225 | SACO DE AREIA IMPRESSO 40x60 | Nenhum campo individual, inconsistência pequena (2,2 pontos percentuais) | Custo R$ 0,68, preço R$ 2,00, margem cadastrada 196,3% x recalculada 194,1% | Não é um erro relevante, a diferença de 2,2 pontos é só arredondamento no campo de margem cadastrado, não um erro de custo ou preço | Não precisa correção, valores plausíveis para a linha de embalagem de material básico ensacado | Qtde 8.138 un, valor a custo R$ 5.533,84. Maior item desta categoria por valor, mas sem erro real |
| 11603 | SACOLA CAMISETA IMPRESSO/ALTA 70 x 90 x 0,03 | Custo ou preço | Custo R$ 0,57, preço R$ 0,30 (margem negativa, -47,4%) | Outras sacolas camiseta impressas do catálogo (50x70): custo R$ 0,32, preço R$ 0,11, também com margem negativa. Padrão se repete nos 2 tamanhos, sugere erro sistemático na linha "Sacola Camiseta Impresso/Alta", não caso isolado | Sem comparável de margem positiva na mesma linha pra estimar valor correto, recomendo checar com o Tony se o preço de venda dessas sacolas está cadastrado errado (parece ter sido invertido com o custo em algum momento) | Qtde 2.000, valor a custo R$ 1.140,00 |
| 11602 | SACOLA CAMISETA IMPRESSO/ALTA 50 x 70 x 0,03 | Custo ou preço | Custo R$ 0,32, preço R$ 0,11 (margem negativa, -65,6%) | Mesmo padrão do item acima (70x90), mesma linha | Mesma recomendação: checar se preço e custo foram invertidos na linha toda de sacola camiseta impressa | Qtde 3.000, valor a custo R$ 960,00 |
| 10030 | ETIQ. ADESIVA 32 X 25 X 3 CAR MM RL C/ 27 MTS TP | Custo ou preço | Custo R$ 25,00, preço R$ 15,00 (margem negativa, -40,0%) | Sem outro produto de etiqueta adesiva no relatório pra comparar | Sem benchmark interno, recomendo checagem direta com o Tony | Qtde 18, valor a custo R$ 450,00 |
| 10842 | EXPOSITOR DE ESPELHOS LINHA FLORA | Custo ou preço | Custo R$ 312,73, preço R$ 297,84 (margem negativa, -4,8%) | Item de mobiliário/exposição, mesma natureza dos itens já excluídos por não serem mercadoria de revenda | Divergência pequena (4,8%), provavelmente não é erro de cadastro, é margem realmente apertada nesse item específico | Qtde 1, valor a custo R$ 312,73 |
| 10810 | COPO DESCARTAVEL 180ML PRATIK | Custo ou preço | Custo R$ 5,20, preço R$ 4,37 (margem negativa, -16,0%) | Sem outro "copo descartável" no relatório pra comparar | Sem benchmark interno, recomendo checagem direta | Qtde 50, valor a custo R$ 260,00 |

### Achados extras confirmados nesta rodada (fora da lista de outliers críticos originais)
1. **Tubo PVC Rosca 1 pol Tigre (código 3214):** o benchmark contra os outros "Tubo PVC Rosca" da mesma marca não resolvia sozinho se o problema era o custo (R$ 8,06), o preço (R$ 96,00) ou a quantidade (999,83 PC, muito acima de qualquer par da linha, que vão de 0 a 6 PC). **Confirmado pelo Tony em 26/08/2026: é um produto de giro baixo**, consistente com pouca movimentação. Removido da lista de pendências de confirmação.
2. **Sacolas 30x40 Imp (código 11022):** o benchmark contra o item irmão direto (Sacolas 40x50 Imp, mesma família, mesma unidade) invertia a hipótese inicial, apontando o custo cadastrado (R$ 11,66) como muito acima do padrão da linha (o irmão custa R$ 0,15). **Confirmado pelo Tony em 26/08/2026: essas sacolas são usadas para ensacar areia e brita** (uso interno/operacional da loja, não item de revenda padrão), o que explica a linha de preço/margem fora do padrão de sacola de revenda. Removido da lista de pendências de confirmação.

### Outliers críticos identificados (pendente de confirmação do cliente)
| Código | Produto | Campo suspeito | Valor cadastrado | Benchmark de pares (mesma linha) | Estimativa | Impacto no valor de estoque |
|---|---|---|---|---|---|---|
| 7153 | CABO FLEX 2.5MM AZ PC COBRECOM | Quantidade | 79.263,90 PC | Outras cores da mesma linha "PC COBRECOM" (vermelho, verde, amarelo, preto): estoque entre 0 e 0,035 PC. Outras marcas de cabo flex 2,5mm no catálogo: estoque entre 0 e 635 MT | Quantidade real provavelmente entre 0 e poucas centenas de unidades, não 79 mil. Não estimo um número exato, é caso de erro de lançamento (unidade ou dígito a mais), não de custo errado | R$ 14.161.290,32 (74,1% do valor bruto de estoque) |
| 7874 | MANGUEIRA CORRUGADA 20MM AM - KRONA | Quantidade e custo | 164.736.600 MT, custo R$ 0,02/MT | Mangueira corrugada 20mm de outras marcas: estoque entre 32 e 239 MT, custo entre R$ 0,91 e R$ 1,22/MT | Quantidade real provavelmente na mesma ordem de grandeza dos pares (dezenas a poucas centenas de MT), custo também provavelmente mais próximo de R$ 0,90 a R$ 1,20/MT | R$ 3.294.733,00 (17,2% do valor bruto de estoque) |
| 11073 | COLORANTE ICORES BA AMARELO P0411 0.9L | Custo final | R$ 158,67/ML | Outros 9 colorantes da mesma linha (Icores BA, 0,9L, unidade ML): custo entre R$ 0,09 e R$ 0,23/ML, mediana R$ 0,13/ML | R$ 0,13 a R$ 0,18/ML (mesma faixa já usada nos 4 períodos de Curva ABC abaixo). **Mesmo item já reportado ao Tony em 23/07/2026 e confirmado como erro de cadastro, segue sem correção no ERP em 03/08/2026** | R$ 720.244,40 (3,8% do valor bruto de estoque) |

Juntos, os 3 itens somam **R$ 18.176.265,52, 95,1% do valor de estoque bruto do relatório**. Nenhum dos 3 foi tratado como fato: os valores "ajustados" deste diagnóstico excluem os 3, e a estimativa de faixa correta é só isso, uma estimativa auditável, que o Tony precisa confirmar ou corrigir. Os itens 7153 e 7874 são achados novos desta rodada, nunca reportados antes.

### Estoque atual (valor a custo)
| Categoria | Valor de estoque (ajustado, exclui outliers) | % do total |
|---|---|---|
| Material Básico | R$ 295.474,92 | 31,9% |
| (categoria corrompida "MD-MD-MD...") | R$ 108.384,93 | 11,7% |
| Hidráulica | R$ 70.065,80 | 7,6% |
| Ferragem | R$ 63.146,25 | 6,8% |
| Material de Uso e Consumo | R$ 61.109,38 | 6,6% |
| Pintura | R$ 59.404,22 | 6,4% |
| Material Elétrico | R$ 53.433,61 | 5,8% |
| Ferramentas | R$ 52.285,17 | 5,6% |
| Utilidades e Jardim | R$ 29.065,59 | 3,1% |
| Cobertura | R$ 28.826,79 | 3,1% |
| Ativo Imobilizado | R$ 28.499,40 | 3,1% |
| Demais categorias (11, cada uma abaixo de 2%) | R$ 49.598,12 | 5,3% |
| Sem categoria mapeada | R$ 7.856,01 | 0,8% |

Total ajustado: R$ 935.102,19. Valor potencial de venda (qtde × preço, mesmos itens, exclui os 3 outliers): não calculado nesta seção, pois herda a mesma distorção dos outliers e exigiria o mesmo tratamento, ver planilha `08-2026/Arquivos/03-inteligencia-dados-estoque-auditado_2026-08-03.xlsx` para o dado bruto por SKU.

### Estoque parado atualizado
- Valor financeiro parado a custo, bruto (direto do relatório): R$ 15.255.302,32, em 1.734 SKUs
- **Valor ajustado (excluindo os outliers 7153 e 11073, que respondem por R$ 14.881.532,87 do valor parado bruto): R$ 373.769,46, em 1.732 SKUs**
- Comparação com 25/07/2026 (`Estoque em 27-06-26.xls`): R$ 295.126,57 em 1.695 SKUs → R$ 373.769,46 em 1.732 SKUs (alta de R$ 78.642,89, +26,6% em valor, com só +37 SKUs, +2,2%, ou seja o valor médio por item parado subiu bem mais que a quantidade de itens parados)
- 68 SKUs novos (sem histórico de venda nos 4 períodos, criados depois de jun/2026) têm estoque positivo hoje e não entram no cálculo de parado por falta de janela de avaliação: R$ 7.254,58 a custo

Maiores itens parados individuais, exceto os outliers já tratados à parte:
| Produto | Qtde. | Custo final | Valor a custo | Categoria |
|---|---|---|---|---|
| Cumeeira Zincalum 0,43 | 2.998 un | R$ 26,00 | R$ 77.948,00 | Material Básico |
| Vareta Solda Oxi 1,59mm Gerdau | 7.329 un | R$ 10,20 | R$ 74.755,80 | (categoria corrompida) |
| Sacolas 30x40 Imp | 2.005 un | R$ 11,66 | R$ 23.378,30 | Material de Uso e Consumo |
| Sacola Recicladas VD 60x80 | 1.015 kg | R$ 11,50 | R$ 11.672,50 | Material de Uso e Consumo |
| Tubo PVC Rosca 1 pol Tigre | 999,83 pc | R$ 8,06 | R$ 8.058,63 | (categoria corrompida) |

Vareta Solda Oxi e Cumeeira Zincalum já apareciam como maiores itens parados individuais nos períodos de nov-dez/2025 e jan-mar/2026 respectivamente (ver seções abaixo), confirma que são itens realmente parados de longa data, não erro de leitura pontual. **Confirmado pelo Tony em 26/08/2026:** Cumeeira é vendida por encomenda (não deveria ser lida como estoque morto real, giro zero é esperado pra esse tipo de venda); Vareta gira muito pouco (slow-mover genuíno, não erro de leitura).

Estoque parado por categoria (ajustado, exclui outliers): categoria corrompida "MD-MD-MD..." concentra 27,4% do valor parado ajustado (R$ 102.131,64), seguida de Material Básico (22,5%, R$ 83.968,25) e Material de Uso e Consumo (14,6%, R$ 54.545,54). Ver planilha para o detalhe completo por SKU.

### Produtos isca / âncora, checagem de cadastro
Sem dado de venda nesta rodada, não é possível reconfirmar giro. Checagem só de preço/custo/margem cadastrados:
- **Cimento Montes Claros CPII F 32 50kg** (código 8992): 27,5 sc em estoque, custo R$ 37,90, preço R$ 51,00, markup cadastrado 34,56%
- **Cimento Poty CPII Z 32 50kg** (código 7972): 174 sc em estoque, custo R$ 38,22, preço R$ 51,00, markup cadastrado 33,44%

Preço e custo seguem na mesma faixa dos períodos anteriores, sem sinal de descontinuação (estoque positivo nos dois). O markup cadastrado (33-35%) não é diretamente comparável à margem sobre venda dos períodos de Curva ABC (21-22%, ver seções abaixo), são cálculos diferentes (markup sobre custo vs margem sobre faturamento real). Reconfirmação de giro depende de um novo export de Curva ABC (jul/ago 2026).

### Comparação com o snapshot anterior (`Estoque em 27-06-26.xls`, 27/06/2026)
- Valor de estoque a custo (ajustado): R$ 900.940,38 → R$ 935.102,19 (alta de 3,79% em 5 semanas)
- Estoque parado (ajustado): R$ 295.126,57 em 1.695 SKUs → R$ 373.769,46 em 1.732 SKUs (alta de 26,6% em valor, 2,2% em SKUs, o valor médio por item parado cresceu mais que a contagem)
- Catálogo: cresceu de 15.228 para 15.369 SKUs cadastrados (a base de comparação de "novos" usada nesta seção, 15.254 SKUs, vem da Curva ABC, não do `Estoque ETL.xlsx`, por isso os números não batem exatos entre si)
- 2 outliers críticos novos identificados nesta rodada (cabo flex e mangueira), não presentes com essa magnitude nos relatórios anteriores

### Próximos passos
1. **Confirmar com o Tony os 2 outliers novos** (código 7153, Cabo Flex, quantidade 79.263,9 PC; código 7874, Mangueira Corrugada Krona, quantidade 164.736.600 MT e custo R$ 0,02/MT) antes de tratar como estoque real. Corrigir no ERP.
2. **Cobrar novamente a correção do colorante** (código 11073, pendente desde 23/07/2026, ainda não corrigido em 03/08/2026)
3. **Solicitar novo export de Curva ABC** (PDF, jul/ago 2026) pra atualizar giro, faturamento e participação por categoria de venda, este relatório não traz esse dado
4. Reportar de novo a categoria corrompida no cadastro (5.254 SKUs "MD-MD-MD...", pendência desde 25/07/2026, segue sem correção)
5. `@analista-dados` pode usar o estoque parado atualizado (R$ 373.769,46) como KPI de dashboard no lugar do valor de 25/07/2026

---

## Período: 01/04/2026 a 30/06/2026
**Fonte dos dados:** `Curva ABC parte 4.pdf` (sistema Pontual Tecnologia), processado em 07-2026
**Planilha:** `07-2026/Arquivos/25-inteligencia-dados-curva-abc-padronizada_2026-04-01_a_2026-06-30.xlsx`
**Status:** v1, sujeito a refinamento

### Resumo executivo
- Faturamento do período (2° trimestre 2026): **R$ 650.821,13** (conferido contra o Total Geral oficial do relatório, cobertura 100%), em 2.464 SKUs com venda registrada (grupos A+B+C)
- Margem bruta total: **R$ 254.933,69 (39,17% sobre a venda)**, caiu 5,97 pontos em relação ao período anterior, a maior queda entre dois períodos do histórico
- Concentração: grupo A responde por **59,98%** do faturamento com apenas **48 SKUs**, quarto período seguido abaixo da faixa saudável de referência do método (70 a 85%), padrão estrutural muito estável (ver visão geral acumulada)
- Estoque parado identificado (sem nenhuma venda neste trimestre, com saldo em estoque): **≈ R$ 469.329,89 a custo** (corrigido), em 2.865 SKUs. Teve leve queda frente ao período anterior (ver comparação abaixo)
- Este foi o primeiro dos 4 arquivos do cliente a ser processado (parte 4 de 4). Os outros 3 já foram processados e entraram neste diagnóstico, ver seções abaixo e a visão geral acumulada no topo do arquivo.

### Limitações da fonte de dados
1. **Erro de cadastro confirmado em `COLORANTE ICORES BA AMARELO P0411 0.9L` (código 11073).** No relatório bruto, esse item aparece com custo de R$ 158,67, e como a quantidade em estoque é grande (4.555,26, na unidade ML do próprio ERP, não frasco), isso gerava sozinho R$ 722.783,10 de estoque parado. Esse é o mesmo apontamento que a Pillar já tinha feito com o Tony, que confirmou o erro de cadastro.
   - **Benchmark usado:** os outros 9 colorantes da mesma linha no relatório (Icores BA, mesmo frasco 0,9L, mesma unidade ML: verde, vermelho óxido, âmbar óxido, vermelho, azul intenso, azul, branco, laranja, rosa) têm custo entre R$ 0,09 e R$ 0,23 por ml, mediana R$ 0,13/ml. O preço de venda médio do item com erro (R$ 0,29/ml) está dentro do padrão normal de venda da linha, o que confirma que só o custo cadastrado está errado, não a quantidade nem o preço de venda.
   - **Valor correto estimado:** entre R$ 0,13/ml (mediana da linha) e R$ 0,18/ml (aplicando o markup médio de ~1,6x que a linha usa entre custo e venda sobre o preço de venda real do item), ponto médio usado nos cálculos: R$ 0,15/ml, não R$ 158,67. Isso equivale a um estoque parado real desse item de R$ 683,29, não R$ 722.783,10.
   - Recomendo corrigir o `custo_unit` desse SKU no ERP para essa faixa, e usar o valor de estoque parado corrigido (R$ 469.329,89) como referência daqui pra frente, não o valor bruto do relatório.
2. **`Lona Plástica 4m` e `Tintométrico` têm margem negativa neste período (-143,9% e -43,0%), confirmados como erro de cadastro, não isca.** Benchmark contra os outros 3 períodos: Lona Plástica teve margem 63,25% (nov-dez/25) e 64,25% (jan-mar/26), margem real estimada ≈ 63,8%. Tintométrico teve margem 99,21% em mai-out/2025 e 99,20% em jan-mar/2026, margem real estimada ≈ 99%, faz sentido pra um item de serviço de tingimento (quase todo o valor de venda é margem). Removidos da lista de produtos isca abaixo.
3. **Categoria corrompida no cadastro do cliente (confirmado, não é falha de extração do PDF).** 5.254 SKUs (majoritariamente sem venda no período, R$ 2.385,39 de faturamento no total, irrelevante para o resultado financeiro) têm o campo de categoria gravado como "MD-MD-MD-MD-MD-...". Achei o mesmo texto corrompido no arquivo `Estoque em 27-06-26.xls`, exportado direto do sistema Pontual (Excel, não PDF, sem passar por extração nenhuma), confirmando que é um problema real de cadastro no ERP do cliente, não um artefato de leitura da ferramenta da Pillar. Não interpretei nem inventei categoria pra esses itens, eles ficam fora da tabela de participação por categoria abaixo. Vale reportar ao Tony como pendência de correção de cadastro no sistema.
4. **Grupo "Z" do relatório (12.790 SKUs) não teve nenhuma venda no período**, faturamento R$ 0,00. Inclui tanto item comercial parado quanto ativo imobilizado da empresa (veículo, computador, triciclo, celular, 13 itens), que retirei do cálculo de estoque parado por não ser mercadoria de revenda.
5. **Este relatório cobre só um trimestre.** Giro, margem e classificação ABC (A/B/C, já vem calculada pelo próprio sistema do cliente) refletem só esses 3 meses.

### Participação por categoria
(SKUs com venda no período, categoria correta only, exclui os 5.254 com categoria corrompida no cadastro, descrito acima)

| Categoria | Faturamento | % do total |
|---|---|---|
| Material Básico | R$ 290.902,33 | 44,7% |
| Hidráulica | R$ 70.122,75 | 10,8% |
| Pintura | R$ 69.739,78 | 10,7% |
| Cobertura | R$ 35.326,83 | 5,4% |
| Material Elétrico | R$ 30.732,49 | 4,7% |
| Ferramentas | R$ 26.828,08 | 4,1% |
| Impermeabilizantes | R$ 23.163,59 | 3,6% |
| Ferragem | R$ 22.489,69 | 3,5% |
| Argamassas e Rejunte | R$ 16.435,53 | 2,5% |
| Metais | R$ 14.030,18 | 2,2% |

Material Básico sozinho é quase metade do faturamento do trimestre. É onde está o grosso do negócio e também onde estão os itens isca (ver abaixo).

### Top produtos por giro (quantidade vendida)
| Produto | Grupo ABC | Qtd. vendida | Faturamento | Margem % |
|---|---|---|---|---|
| Tijolo c/8 furos 09x19x19 | A | 45.296 un | R$ 45.305,49 | 25,0% |
| Telha canal tipo russa 1a. | A | 3.588 un | R$ 5.117,00 | 50,2% |
| Telha canal tipo russa 2a. | A | 1.700 un | R$ 2.380,00 | 33,6% |
| Registro gaveta met 1502 4pol semi ind Deca | A | 1.381 un | R$ 4.800,00 | 42,5% |
| Cimento Montes Claros CPII F 32 50kg | A | 987,6 sc | R$ 50.782,93 | 22,4% |

Abaixo dessas, o giro é dominado por itens de ferragem de baixo ticket (buchas, parafusos, arruelas, abraçadeiras), volume alto mas contribuição de faturamento pequena, típico item de acompanhamento de venda, não de resultado.

### Top produtos por margem bruta absoluta
| Produto | Faturamento | Margem R$ | Margem % |
|---|---|---|---|
| Areia fina | R$ 37.261,76 | R$ 19.604,96 | 52,6% |
| Pedra britada 1 (19) | R$ 23.203,17 | R$ 12.212,35 | 52,6% |
| Cimento Montes Claros CPII F 32 50kg | R$ 50.782,93 | R$ 11.369,41 | 22,4% |
| Tijolo c/8 furos 09x19x19 | R$ 45.305,49 | R$ 11.333,49 | 25,0% |
| Areia média | R$ 15.893,36 | R$ 7.477,80 | 47,1% |
| Pedra calcária | R$ 10.800,00 | R$ 5.279,76 | 48,9% |
| Areia grossa lavada | R$ 8.800,62 | R$ 4.808,22 | 54,6% |
| Pedra britada 0 (cascalhinho) | R$ 9.320,00 | R$ 4.789,92 | 51,4% |

Padrão claro: agregados (areia, pedra, brita) têm margem % alta (50 a 55%) mas dependem do cimento e do tijolo pra puxar venda. Cimento e tijolo têm margem % baixa (22 a 25%) mas concentram o volume. É o par clássico isca + margem alta do mesmo momento de obra (fundação e alvenaria), validado em todos os 4 períodos processados.

### Estoque parado (sem venda no período, com saldo em estoque)
- Valor financeiro parado a custo, **já corrigido pelo erro de cadastro da limitação 1**: **≈ R$ 469.329,89**, em 2.865 SKUs
- Valor bruto do relatório, sem a correção (não usar como referência): R$ 1.191.429,70

### Produtos isca / âncora identificados
- **Cimento Montes Claros CPII F 32 50kg**: 987,6 sacos vendidos, R$ 50.782,93 de faturamento, margem 22,4%. Quarto período seguido no mesmo padrão de isca (ver visão geral acumulada).
- **Cimento Poty CPII Z 32 50kg**: 326 sacos, R$ 16.779,99, margem 21,7%. Mesmo padrão.
- Lona Plástica e Tintométrico, que apareciam nesse filtro com margem negativa, foram removidos da lista, ver limitação 2 (erro de cadastro confirmado, não isca).

### Candidatos a kit (handoff para @copywriter, Pilar 3)
- **Kit Fundação e Alvenaria**: cimento (Montes Claros ou Poty, produto âncora de giro) + areia fina/média + pedra britada 1 + tijolo c/8 furos. Validado nos 4 períodos processados (mai/2025 a jun/2026), não é padrão de um trimestre isolado. Kit reduz esforço de venda avulsa e empurra o item de maior margem (areia, brita) junto com o item que já puxa cliente (cimento, tijolo).

### Comparação com o período anterior (jan-mar/2026)
- Faturamento mensal médio: R$ 199.627,60 → R$ 216.940,38 (subiu 8,7%, recuperação parcial após o trimestre mais fraco do histórico)
- Margem: 45,14% → 39,17% (caiu 5,97 pontos percentuais, maior queda entre dois períodos do histórico)
- Grupo A: 59,89% → 59,98% (estável)
- Estoque parado corrigido: R$ 491.900,30 → R$ 469.329,89 (queda de 4,6%)

### Próximos passos
1. Corrigir no ERP o `custo_unit` de `COLORANTE ICORES BA AMARELO P0411 0.9L` (código 11073) para a faixa R$ 0,13 a R$ 0,18/ml, erro já confirmado com o Tony (limitação 1)
2. Investigar com o Tony por que a margem caiu 5,97 pontos neste trimestre, maior queda do histórico
3. Enviar este diagnóstico para `@copywriter` avaliar o Kit Fundação e Alvenaria, agora validado em 4 períodos seguidos
4. `@analista-dados` pode usar faturamento, margem e estoque parado (R$ 295.126,57, valor real reconciliado, ver nota no topo do arquivo) como KPI de dashboard, histórico completo mai/2025 a jun/2026 já consolidado e reconciliado com o diagnóstico de 23/07
5. Reportar ao Tony a categoria corrompida no cadastro do sistema (5.254 SKUs com "MD-MD-MD-..." no campo Grupo, confirmado no arquivo `Estoque em 27-06-26.xls` também, não é problema de leitura da Pillar) como pendência de correção de cadastro
6. Confirmar com o cliente se a categorização usada (campo do próprio relatório Pontual) bate com a divisão real da loja

---

## Período: 01/01/2026 a 31/03/2026
**Fonte dos dados:** `Curva ABC parte 3.pdf` (sistema Pontual Tecnologia), processado em 07-2026
**Planilha:** `07-2026/Arquivos/25-inteligencia-dados-curva-abc-padronizada_2026-01-01_a_2026-03-31.xlsx`
**Status:** v1, sujeito a refinamento

### Resumo executivo
- Faturamento do período (3 meses, jan-mar/2026): **R$ 598.882,79** (conferido contra o Total Geral oficial, cobertura 100%), em 2.540 SKUs com venda registrada
- Margem bruta total: **R$ 270.339,16 (45,14% sobre a venda)**, a maior margem % dos 4 períodos
- Grupo A responde por 59,89% do faturamento em 63 SKUs
- Estoque parado corrigido (ver limitação 1): **≈ R$ 491.900,30**, em 2.987 SKUs, o maior valor dos 4 períodos
- O mais fraco dos 4 períodos em faturamento mensal médio (R$ 199.627,60/mês), ver visão geral acumulada

### Limitações da fonte de dados
1. **Mesmo erro de cadastro do `COLORANTE ICORES BA AMARELO P0411 0.9L`** (código 11073, benchmark detalhado no período de abr-jun/2026 acima). Valor bruto do relatório R$ 1.214.000,11, valor corrigido usando R$ 0,15/ml: **R$ 491.900,30**.
2. **Ativo imobilizado**: 13 itens excluídos da análise comercial.
3. **Categoria corrompida no cadastro do cliente** (confirmado como erro real do ERP, não da extração do PDF, ver detalhe no período de abr-jun/2026 acima): 5.254 SKUs, faturamento R$ 3.295,32, fora da tabela abaixo.
4. Neste período não apareceu nenhum item com margem negativa implausível entre os candidatos a isca, ao contrário dos dois períodos mais antigos (ver seções abaixo).

### Participação por categoria
| Categoria | Faturamento | % do total |
|---|---|---|
| Material Básico | R$ 268.434,71 | 44,8% |
| Hidráulica | R$ 54.907,92 | 9,2% |
| Pintura | R$ 45.048,31 | 7,5% |
| Material Elétrico | R$ 40.759,43 | 6,8% |
| Cobertura | R$ 32.341,54 | 5,4% |
| Ferramentas | R$ 31.329,46 | 5,2% |
| Argamassas e Rejunte | R$ 28.115,56 | 4,7% |
| Ferragem | R$ 23.159,15 | 3,9% |

### Top produtos por giro (quantidade vendida)
| Produto | Grupo ABC | Qtd. vendida | Faturamento | Margem % |
|---|---|---|---|---|
| Tijolo c/8 furos 09x19x19 | A | 62.307 un | R$ 60.417,61 | 55,7% |
| Telha canal tipo russa 2a. | A | 6.158 un | R$ 8.162,85 | 66,8% |
| Telha canal tipo russa 1a. | A | 1.480 un | R$ 2.344,00 | 93,1% |
| Cimento Montes Claros CPII F 32 50kg | A | 927,9 sc | R$ 44.638,73 | 22,8% |
| Argamassa Cola Forte AC-II 15kg | A | 644 un | R$ 15.512,30 | 39,0% |

### Top produtos por margem bruta absoluta
| Produto | Faturamento | Margem R$ | Margem % |
|---|---|---|---|
| Tijolo c/8 furos 09x19x19 | R$ 60.417,61 | R$ 33.625,60 | 55,7% |
| Areia fina | R$ 37.716,21 | R$ 19.424,36 | 51,5% |
| Cimento Montes Claros CPII F 32 50kg | R$ 44.638,73 | R$ 10.175,41 | 22,8% |
| Pedra calcária | R$ 13.670,00 | R$ 7.653,03 | 56,0% |
| Pedra britada 0 (cascalhinho) | R$ 13.110,00 | R$ 6.978,44 | 53,2% |

### Estoque parado (sem venda no período, com saldo em estoque)
- Valor financeiro parado a custo, **já corrigido**: **≈ R$ 491.900,30**, em 2.987 SKUs
- Valor bruto do relatório: R$ 1.214.000,11
- Maior item individual, fora o colorante: Cumeeira Zincalum 0,43, 2.998 un a R$ 26,00, R$ 77.948,00

### Produtos isca / âncora identificados
- **Cimento Montes Claros CPII F 32 50kg**: margem 22,8%, terceiro período seguido no mesmo padrão
- **Cimento Poty CPII Z 32 50kg**: margem 21,1%

### Candidatos a kit (handoff para @copywriter, Pilar 3)
- **Kit Fundação e Alvenaria**: mesmo padrão validado, agora em 3 dos 4 períodos processados

### Comparação com o período anterior (nov-dez/2025)
- Faturamento mensal médio: R$ 227.422,28 → R$ 199.627,60 (queda de 12,2%, o trimestre mais fraco do histórico)
- Margem: 41,82% → 45,14% (subiu 3,32 pontos percentuais, melhor margem do histórico)
- Grupo A: 59,97% → 59,89% (estável)
- Estoque parado corrigido: R$ 467.599,36 → R$ 491.900,30 (subiu 5,2%)

### Próximos passos
1. Entender com o Tony por que jan-mar/2026 foi o trimestre mais fraco em faturamento mensal médio do histórico, mesmo tendo a melhor margem
2. Manter observação da melhora de margem, entender se é mix de produto (mais itens de alta margem vendidos) ou reajuste de preço

---

## Período: 01/11/2025 a 31/12/2025
**Fonte dos dados:** `Curva ABC parte 2.pdf` (sistema Pontual Tecnologia), processado em 07-2026
**Planilha:** `07-2026/Arquivos/25-inteligencia-dados-curva-abc-padronizada_2025-11-01_a_2025-12-31.xlsx`
**Status:** v1, sujeito a refinamento

### Resumo executivo
- Faturamento do período (2 meses, nov-dez/2025): **R$ 454.844,56** (conferido contra o Total Geral oficial, cobertura 100%), em 2.088 SKUs com venda registrada
- Margem bruta total: **R$ 190.231,82 (41,82% sobre a venda)**
- Grupo A responde por 59,97% do faturamento em apenas 35 SKUs
- Estoque parado corrigido (ver limitação 1): **≈ R$ 467.599,36**, em 3.381 SKUs

### Limitações da fonte de dados
1. **Mesmo erro de cadastro do `COLORANTE ICORES BA AMARELO P0411 0.9L`** (código 11073, custo cadastrado R$ 158,67/ml, benchmark detalhado no período de abr-jun/2026 acima). Valor bruto do relatório R$ 1.195.222,01, valor corrigido usando R$ 0,15/ml: **R$ 467.599,36**.
2. **`Mangueira Corrugada 25mm` aparece com margem -193,12%** neste período. Benchmark contra jan-mar/2026 (41,00%) e abr-jun/2026 (41,26%) indica margem real ≈ 41,1%, não isca, erro de custo cadastrado pontual deste período.
3. **Ativo imobilizado**: 13 itens excluídos da análise comercial.
4. **Categoria corrompida no cadastro do cliente** (confirmado como erro real do ERP, não da extração do PDF, ver detalhe no período de abr-jun/2026 acima): 5.256 SKUs, faturamento R$ 1.684,76, fora da tabela de participação por categoria abaixo.

### Participação por categoria
| Categoria | Faturamento | % do total |
|---|---|---|
| Material Básico | R$ 189.465,67 | 41,7% |
| Ferragem | R$ 48.359,08 | 10,6% |
| Pintura | R$ 44.372,15 | 9,8% |
| Impermeabilizantes | R$ 37.046,64 | 8,1% |
| Ferramentas | R$ 26.625,75 | 5,9% |
| Hidráulica | R$ 26.326,25 | 5,8% |
| Material Elétrico | R$ 24.043,73 | 5,3% |
| Cobertura | R$ 16.542,94 | 3,6% |
| Argamassas e Rejunte | R$ 15.246,58 | 3,4% |

### Top produtos por giro (quantidade vendida)
| Produto | Grupo ABC | Qtd. vendida | Faturamento | Margem % |
|---|---|---|---|---|
| Tijolo c/8 furos 09x19x19 | A | 46.742 un | R$ 44.752,00 | 30,0% |
| Telha canal tipo russa 2a. | A | 8.911 un | R$ 11.284,07 | 32,9% |
| Parafuso auto broc zinc 12x1 | A | 8.000 un | R$ 4.000,00 | 58,0% |
| Cimento Montes Claros CPII F 32 50kg | A | 432,2 sc | R$ 20.048,27 | 22,0% |

### Top produtos por margem bruta absoluta
| Produto | Faturamento | Margem R$ | Margem % |
|---|---|---|---|
| Areia fina | R$ 27.548,26 | R$ 14.030,59 | 50,9% |
| Tijolo c/8 furos 09x19x19 | R$ 44.752,00 | R$ 13.434,86 | 30,0% |
| Cerca concertina 45cm | R$ 22.575,09 | R$ 9.160,61 | 40,6% |
| Cimento asfalto oxidado Betoxi | R$ 19.040,00 | R$ 6.904,38 | 36,3% |
| Pedra britada 1 (19) | R$ 8.577,58 | R$ 5.022,58 | 58,6% |

### Estoque parado (sem venda no período, com saldo em estoque)
- Valor financeiro parado a custo, **já corrigido**: **≈ R$ 467.599,36**, em 3.381 SKUs
- Valor bruto do relatório: R$ 1.195.222,01
- Maior item individual, fora o colorante: Vareta Solda Oxi 1,59mm Gerdau, 7.329 un, R$ 74.755,80

### Produtos isca / âncora identificados
- **Cimento Montes Claros CPII F 32 50kg**: margem 22,0%, mesmo padrão dos demais períodos
- **Cimento Poty CPII Z 32 50kg**: margem 18,2%

### Candidatos a kit (handoff para @copywriter, Pilar 3)
- **Kit Fundação e Alvenaria**: mesmo padrão validado nos outros 3 períodos (cimento + areia + pedra britada + tijolo)

### Comparação com o período anterior (mai-out/2025)
- Faturamento mensal médio: R$ 229.544,96 → R$ 227.422,28 (queda de 0,9%, praticamente estável)
- Margem: 35,93% → 41,82% (subiu 5,89 pontos percentuais)
- Grupo A: 59,87% → 59,97% (estável)
- Estoque parado corrigido: R$ 424.367,42 → R$ 467.599,36 (subiu 10,2%)

### Próximos passos
1. Investigar a causa da margem negativa da Mangueira Corrugada neste período (limitação 2)
2. Entender por que o estoque parado corrigido subiu 10,2% frente ao período anterior

---

## Período: 01/05/2025 a 31/10/2025
**Fonte dos dados:** `Curva ABC parte 1.pdf` (sistema Pontual Tecnologia), processado em 07-2026
**Planilha:** `07-2026/Arquivos/25-inteligencia-dados-curva-abc-padronizada_2025-05-01_a_2025-10-31.xlsx`
**Status:** v1, sujeito a refinamento

### Resumo executivo
- Faturamento do período (6 meses, mai a out/2025): **R$ 1.377.269,74** (bate exato com o Total Geral oficial do relatório), em 3.421 SKUs com venda registrada (grupos A+B+C)
- Margem bruta total: **R$ 494.811,46 (35,93% sobre a venda)**
- Grupo A responde por 59,87% do faturamento em apenas 66 SKUs
- Estoque parado corrigido (ver limitação 1): **≈ R$ 424.367,42**, em 2.661 SKUs
- Este PDF veio em "formato simples" (o outro layout que a ferramenta de padronização reconhece), sem as colunas de categoria (Grupo/Sub-Grupo/Linha/Família) que os outros 3 relatórios trazem. Por isso este período não tem tabela de participação por categoria. Esse formato não teve o bug de extração que afetou os outros 3 períodos (ver nota de revisão no topo do arquivo), os números deste período nunca precisaram ser corrigidos.
- Período mais antigo do histórico processado até agora, não há período anterior pra comparar.

### Limitações da fonte de dados
1. **Erro de cadastro conhecido em `COLORANTE ICORES BA AMARELO P0411 0.9L` (código 11073), mesmo item identificado no período de abr-jun/2026 (acima) e confirmado pelo Tony.** Custo cadastrado R$ 158,67/ml contra R$ 0,09 a R$ 0,23/ml dos outros 9 colorantes da mesma linha (benchmark detalhado no período de abr-jun/2026, mais acima neste arquivo). Uso a mesma estimativa de custo correto, R$ 0,13 a R$ 0,18/ml (ponto médio R$ 0,15/ml), pra corrigir o estoque parado deste período: valor bruto do relatório R$ 1.153.904,99, valor corrigido **R$ 424.367,42**.
2. **Vários itens deste período específico aparecem com margem fortemente negativa e implausível** (Cabo Flex 2,5mm -1285,65%, Cabo Flex 1,5mm -2119,15%, Lixa Massa G220 -8028,93%, Fita Multiuso Adesiva -91,44%, Lona Plástica -68,61%, Cimento Montes Claros -2,01%, Areia Fina -0,84%). Apliquei o benchmark contra os outros 3 períodos já processados (mesmo produto, custo em janela diferente) e todos voltam a margem normal fora deste período:

   | Produto | Margem neste período | Margem nos outros períodos | Margem real estimada |
   |---|---|---|---|
   | Cimento Montes Claros CPII F 32 | -2,01% | 22,02% (nov-dez/25) · 22,80% (jan-mar/26) · 22,39% (abr-jun/26) | ≈ 22,4% |
   | Areia Fina | -0,84% | 50,93% (nov-dez/25) · 51,50% (jan-mar/26) · 52,61% (abr-jun/26) | ≈ 51,7% |
   | Cabo Flex 2,5mm | -1285,65% | 39,00% (nov-dez/25) · 37,49% (jan-mar/26) · 47,09% (abr-jun/26) | ≈ 41,2% |
   | Cabo Flex 1,5mm | -2119,15% | 45,00% (nov-dez/25) · 38,60% (jan-mar/26) | ≈ 41,8% |
   | Fita Multiuso Adesiva | -91,44% | 53,08% (nov-dez/25) | ≈ 53,1% |
   | Lona Plástica 4m | -68,61% | 63,25% (nov-dez/25) · 64,25% (jan-mar/26) | ≈ 63,8% |
   | Lixa Massa G220 | -8028,93% | 55,00% (nov-dez/25) · 53,67% (jan-mar/26) · 57,31% (abr-jun/26) | ≈ 55,3% |

   Padrão consistente: só este período tem esses valores fora da curva, e o preço de venda desses itens está normal (é o custo cadastrado que destoa). Provável lote de entrada com custo lançado errado nesse relatório específico. Não tratei nenhum desses itens como isca (a margem real é alta), removi da lista de candidatos abaixo.
3. **Ativo imobilizado e SKUs sem movimento** ficam no grupo Z do relatório, mesmo critério de exclusão usado nos demais períodos.
4. **Sem colunas de categoria neste PDF** (formato simples), então não dá pra montar a tabela de participação por categoria nem separar "ativo imobilizado" da mesma forma que nos outros 3 períodos. O filtro de estoque parado abaixo não teve como excluir ativo imobilizado por categoria (usei só grupo Z + estoque positivo).

### Top produtos por giro (quantidade vendida)
| Produto | Grupo ABC | Qtd. vendida | Faturamento | Margem % |
|---|---|---|---|---|
| Tijolo c/8 furos 09x19x19 | A | 128.085 un | R$ 122.202,00 | 27,7% |
| Telha canal tipo russa 1a. | A | 5.911 un | R$ 8.275,40 | 65,7% |
| Telha canal tipo russa 2a. | A | 5.316 un | R$ 6.958,35 | 74,8% |
| Cimento Montes Claros CPII F 32 50kg | A | 1.352,4 sc | R$ 56.928,30 | 22,4% (corrigida, ver limitação 2) |
| Argamassa Cola Forte AC-II 15kg | A | 1.053 un | R$ 25.046,98 | 38,5% |

### Top produtos por margem bruta absoluta
| Produto | Faturamento | Margem R$ | Margem % |
|---|---|---|---|
| Tijolo c/8 furos 09x19x19 | R$ 122.202,00 | R$ 33.823,35 | 27,7% |
| Pedra britada 1 (19) | R$ 29.242,27 | R$ 15.215,72 | 52,0% |
| Pilar de ferro | R$ 20.628,00 | R$ 10.245,24 | 49,7% |
| Pedra britada 0 (cascalhinho) | R$ 20.271,53 | R$ 10.040,86 | 49,5% |
| Argamassa Cola Forte AC-II 15kg | R$ 25.046,98 | R$ 9.641,59 | 38,5% |
| Areia média | R$ 20.500,39 | R$ 9.368,87 | 45,7% |
| Pedra calcária | R$ 15.875,00 | R$ 8.700,98 | 54,8% |

### Estoque parado (sem venda no período, com saldo em estoque)
- Valor financeiro parado a custo, **já corrigido pelo erro de cadastro da limitação 1**: **≈ R$ 424.367,42**, em 2.661 SKUs
- Valor bruto do relatório, sem a correção (não usar como referência): R$ 1.153.904,99
- Maior item individual, fora o colorante já corrigido: Vareta Solda Oxi 1,59mm Gerdau, 7.329 un a R$ 10,20, R$ 74.755,80

### Produtos isca / âncora identificados
- **Cimento Montes Claros CPII F 32 50kg**: 1.352,4 sacos vendidos, R$ 56.928,30 de faturamento, margem real ≈ 22,4% (corrigida, limitação 2). Maior giro em valor do período com margem abaixo da média.
- **Cimento Poty CPII Z 32 50kg**: margem 24,65%, mesmo perfil, presente também nos outros 3 períodos.
- **Telha Canal Tipo Carnaúba 1ª**: 2.000 un, margem 24,17%, giro alto e margem no limite do corte de isca (<25%), aparece só neste período, vale observar se repete.

### Candidatos a kit (handoff para @copywriter, Pilar 3)
- **Kit Fundação e Alvenaria**: cimento (âncora de giro) + pedra britada + areia média + tijolo. Mesmo padrão dos demais períodos (ver visão geral acumulada), os 4 itens de maior margem absoluta pertencem à fase de fundação/alvenaria.

### Próximos passos
1. Nenhuma ação de cadastro necessária além da já registrada no período de abr-jun/2026 (limitação 1), o erro do colorante é o mesmo item, já em correção
2. Investigar com o Tony se o lote de custo errado da limitação 2 (cabo flex, lixa, fita, lona, cimento, areia) teve algum evento em comum (troca de sistema, importação de nota fiscal em lote, migração de dado)
3. Confirmar se Telha Canal Tipo Carnaúba 1ª deve entrar na lista de produtos isca de forma permanente ou foi pontual deste período
