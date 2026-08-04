# Diagnóstico de Estoque e Giro para Construmais
**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra
**Como ler este arquivo:** histórico cumulativo, uma seção por período coberto por relatório do cliente, do mais recente (topo) para o mais antigo (final), independente da ordem em que os relatórios foram processados.

**Nota de revisão (25/07/2026):** a versão anterior deste arquivo (mesma data) foi calculada com um bug no script de padronização, que descartava silenciosamente os 2 primeiros produtos de cada página do PDF nas partes 2, 3 e 4 (perda de ~15% do catálogo e ~12% do faturamento nesses períodos, a parte 1 não era afetada). O bug foi corrigido (`pillar_padroniza_curva_abc.py`, cobertura agora conferida automaticamente contra o "Total Geral" oficial impresso em cada relatório, 100% de cobertura nos 4 períodos) e as planilhas de origem foram regeradas. **Os números abaixo são os corretos.** Como efeito colateral bom: o faturamento e a margem agregada dos 14 meses agora batem exatamente com o diagnóstico anterior de 23/07 (`outputs/2026-07-diagnostico-estoque.md`), o que resolve a contradição registrada no Histórico do `CLIENTE.md`.

**Nota de reconciliação do estoque parado (25/07/2026):** o "Estoque parado corrigido" na tabela abaixo, um valor por período, é o que dava pra calcular só com os 4 PDFs de Curva ABC, e tem uma limitação importante: os 4 relatórios foram todos gerados na mesma semana (27/06 a 03/07/2026), então o campo de estoque de cada um reflete o estoque de **quando o relatório foi emitido**, não do fim do período de venda que ele cobre. Ou seja, a "evolução" desse número entre períodos reflete principalmente quais produtos entram ou saem da lista conforme a janela de venda comparada muda, não uma trajetória real de estoque acumulando ao longo de 14 meses. Depois de receber `Estoque em 27-06-26.xls` (exportação original do sistema, com estoque de todos os 15.228 produtos numa única data certa), cruzei esse arquivo com a venda somada dos 4 relatórios de Curva ABC e cheguei no número correto de estoque parado real: **1.695 produtos sem nenhuma venda registrada nos 14 meses inteiros (mai/2025 a jun/2026), R$ 295.126,57 a custo** (já com a correção do colorante aplicada). Esse número bate próximo do R$ 320.903,02 do diagnóstico de 23/07 (diferença de ~8%, provavelmente porque aquela análise também corrigiu outros itens de custo além do colorante).

**Nota de atualização de estoque (03/08/2026), substitui a referência acima:** novo snapshot de estoque (`Produto em 03-08-26.htm`, exportação direta do sistema Pontual, 15.369 SKUs) cruzado com a mesma venda somada dos 4 períodos de Curva ABC. Estoque parado real atualizado: **1.732 produtos, R$ 373.769,46 a custo** (alta de R$ 78.642,89 / +26,6% em valor frente ao R$ 295.126,57 de 25/07/2026, com apenas 37 SKUs a mais no grupo parado, +2,2%, ou seja o valor médio por item parado subiu mais que a quantidade de itens). Esse novo relatório trouxe também **2 outliers críticos de cadastro não vistos antes**, com quantidade ou custo em forte desacordo com os pares da própria linha de produto (`CABO FLEX 2.5MM AZ PC COBRECOM`, código 7153, quantidade 79.263,9 PC contra pares entre 0 e 635 MT/PC da mesma linha; `MANGUEIRA CORRUGADA 20MM AM - KRONA`, código 7874, quantidade e custo fora do padrão). Já excluídos do número acima, ver seção "Atualização de Estoque: 03/08/2026" abaixo para o detalhe completo. **Use R$ 373.769,46 como referência de estoque parado do negócio a partir de agora**, não os valores por período da tabela abaixo (mantidos só pra referência histórica) nem o R$ 295.126,57 de 25/07 (desatualizado, mas preservado acima por transparência do histórico).

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
**Planilha:** `08-2026/estoque-auditado_2026-08-03.xlsx` (abas: Estoque padronizado, Estoque parado (ajustado), Outliers críticos)
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

Total ajustado: R$ 935.102,19. Valor potencial de venda (qtde × preço, mesmos itens, exclui os 3 outliers): não calculado nesta seção, pois herda a mesma distorção dos outliers e exigiria o mesmo tratamento, ver planilha `08-2026/estoque-auditado_2026-08-03.xlsx` para o dado bruto por SKU.

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

Vareta Solda Oxi e Cumeeira Zincalum já apareciam como maiores itens parados individuais nos períodos de nov-dez/2025 e jan-mar/2026 respectivamente (ver seções abaixo), confirma que são itens realmente parados de longa data, não erro de leitura pontual.

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
**Planilha:** `07-2026/curva-abc-padronizada_2026-04-01_a_2026-06-30.xlsx`
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
**Planilha:** `07-2026/curva-abc-padronizada_2026-01-01_a_2026-03-31.xlsx`
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
**Planilha:** `07-2026/curva-abc-padronizada_2025-11-01_a_2025-12-31.xlsx`
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
**Planilha:** `07-2026/curva-abc-padronizada_2025-05-01_a_2025-10-31.xlsx`
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
