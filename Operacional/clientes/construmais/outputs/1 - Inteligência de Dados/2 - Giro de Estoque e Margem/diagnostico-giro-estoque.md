# Diagnóstico de Giro de Estoque e Margem para Construmais
**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra, atividade "Giro de Estoque e Margem"
**Como ler este arquivo:** histórico cumulativo, uma seção por período/snapshot coberto por relatório de estoque do cliente, do mais recente (topo) para o mais antigo (final), independente da ordem em que os relatórios foram processados.

**Nota de migração estrutural (12/08/2026):** este arquivo nasceu da separação do antigo `diagnostico-estoque.md` (formato legado, um arquivo único) em dois diagnósticos, conforme o critério de "Formato de output" em `_squad/06-inteligencia-dados/SKILL.md`. Este arquivo concentra as leituras de estoque parado e auditoria de cadastro: o snapshot de estoque de 03/08/2026 (que já vinha nesse formato) e as 4 subseções "Estoque parado" que existiam dentro de cada período de Curva ABC (fonte: Grupo Z de cada relatório), agora como entradas próprias. As leituras de venda (faturamento, margem, participação por categoria, giro, produtos isca, kits) seguem em `../1 - Curva ABC do Estoque/diagnostico-curva-abc.md`. Nenhum número foi recalculado nesta migração, é reorganização estrutural de conteúdo já apurado.

**Nota de reconciliação do estoque parado (25/07/2026):** o "Estoque parado corrigido" na tabela abaixo, um valor por período, é o que dava pra calcular só com os 4 PDFs de Curva ABC, e tem uma limitação importante: os 4 relatórios foram todos gerados na mesma semana (27/06 a 03/07/2026), então o campo de estoque de cada um reflete o estoque de **quando o relatório foi emitido**, não do fim do período de venda que ele cobre. Ou seja, a "evolução" desse número entre períodos reflete principalmente quais produtos entram ou saem da lista conforme a janela de venda comparada muda, não uma trajetória real de estoque acumulando ao longo de 14 meses. Depois de receber `Estoque em 27-06-26.xls` (exportação original do sistema, com estoque de todos os 15.228 produtos numa única data certa), cruzei esse arquivo com a venda somada dos 4 relatórios de Curva ABC e cheguei no número correto de estoque parado real: **1.695 produtos sem nenhuma venda registrada nos 14 meses inteiros (mai/2025 a jun/2026), R$ 295.126,57 a custo** (já com a correção do colorante aplicada). Esse número bate próximo do R$ 320.903,02 do diagnóstico de 23/07 (diferença de ~8%, provavelmente porque aquela análise também corrigiu outros itens de custo além do colorante).

**Nota de atualização de estoque (03/08/2026), substitui a referência acima:** novo snapshot de estoque (`Produto em 03-08-26.htm`, exportação direta do sistema Pontual, 15.369 SKUs) cruzado com a mesma venda somada dos 4 períodos de Curva ABC. Estoque parado real atualizado: **1.732 produtos, R$ 373.769,46 a custo** (alta de R$ 78.642,89 / +26,6% em valor frente ao R$ 295.126,57 de 25/07/2026, com apenas 37 SKUs a mais no grupo parado, +2,2%, ou seja o valor médio por item parado subiu mais que a quantidade de itens). Esse novo relatório trouxe também **2 outliers críticos de cadastro não vistos antes**, com quantidade ou custo em forte desacordo com os pares da própria linha de produto (`CABO FLEX 2.5MM AZ PC COBRECOM`, código 7153, quantidade 79.263,9 PC contra pares entre 0 e 635 MT/PC da mesma linha; `MANGUEIRA CORRUGADA 20MM AM - KRONA`, código 7874, quantidade e custo fora do padrão). Já excluídos do número acima, ver seção "Período/Snapshot: 03/08/2026" abaixo para o detalhe completo. **Use R$ 373.769,46 como referência de estoque parado do negócio a partir de agora**, não os valores por período/snapshot da tabela abaixo (mantidos só pra referência histórica) nem o R$ 295.126,57 de 25/07 (desatualizado, mas preservado acima por transparência do histórico).

## Visão geral acumulada (mai/2025 a jun/2026, 5 períodos/snapshots processados)
*(atualizar este bloco a cada novo período/snapshot processado, não é seção fixa)*

| Período/Snapshot | Fonte | Estoque parado corrigido | SKUs parados | Giro médio / Quadrante predominante |
|---|---|---|---|---|
| 03/08/2026 (snapshot) | `Produto em 03-08-26.htm` | R$ 373.769,46 | 1.732 | n/d, ver nota abaixo |
| 01/04/2026 a 30/06/2026 (Grupo Z) | `Curva ABC parte 4.pdf` | R$ 469.329,89 | 2.865 | n/d, ver nota abaixo |
| 01/01/2026 a 31/03/2026 (Grupo Z) | `Curva ABC parte 3.pdf` | R$ 491.900,30 | 2.987 | n/d, ver nota abaixo |
| 01/11/2025 a 31/12/2025 (Grupo Z) | `Curva ABC parte 2.pdf` | R$ 467.599,36 | 3.381 | n/d, ver nota abaixo |
| 01/05/2025 a 31/10/2025 (Grupo Z) | `Curva ABC parte 1.pdf` | R$ 424.367,42 | 2.661 | n/d, ver nota abaixo |

Nota sobre a coluna "Giro médio / Quadrante predominante": a matriz giro x margem (4 quadrantes) ainda não foi calculada pra nenhum período/snapshot. Exige cruzar quantidade vendida por SKU com o estoque na mesma janela, trabalho não feito até agora (os 4 Grupo Z acima só têm o dado de "sem venda no período", não giro positivo por SKU; o snapshot de 03/08 tem estoque, custo e preço mas não venda). Registrado como limitação, não como dado zerado.

Leituras que só aparecem comparando períodos e snapshots:

1. **Estoque parado real atualizado em 03/08/2026: R$ 373.769,46 em 1.732 produtos** (era R$ 295.126,57 em 1.695 produtos em 25/07/2026, alta de 26,6% em valor com só 2,2% mais itens, ver nota de atualização acima).
2. **Os 4 valores "por período" (Grupo Z) da tabela acima não devem ser lidos como uma tendência real de estoque acumulando ao longo do tempo.** Os 4 relatórios de Curva ABC de origem foram todos emitidos na mesma semana (27/06 a 03/07/2026), então o campo de estoque de cada um reflete o estoque de quando o relatório foi emitido, não do fim do período de venda que ele cobre (ver nota de reconciliação de 25/07 acima). A oscilação entre eles (R$ 424,4 mil → R$ 467,6 mil → R$ 491,9 mil → R$ 469,3 mil) reflete principalmente quais produtos entram ou saem da lista de "sem venda" conforme a janela de venda comparada muda, não estoque parado se acumulando mês a mês.
3. **2 itens do relatório de 03/08/2026 têm quantidade ou custo em forte desacordo com os pares da própria linha de produto** (cabo flex e mangueira corrugada, ver seção "Período/Snapshot: 03/08/2026" abaixo), somando R$ 17,46 milhões que já foram excluídos de todos os números acima. Pendente de confirmação do Tony antes de tratar como estoque real.

---

## Período/Snapshot: 03/08/2026 (snapshot, fora do ciclo de Curva ABC)
**Fonte dos dados:** `Produto em 03-08-26.htm` (sistema Pontual Tecnologia, exportação HTML de tabela de produto), processado em 08-2026
**Planilha:** `08-2026/estoque-auditado_2026-08-03.xlsx` (abas: Estoque padronizado, Estoque parado (ajustado), Outliers críticos) + `08-2026/top-relevantes-parados_2026-08-03.xlsx` (abas: Top por valor de custo, Top por potencial de venda, listas completas por concentração de valor, ver critério na seção "Estoque parado atualizado" abaixo)
**Status:** v1, sujeito a refinamento
**Tipo de relatório:** diferente das entradas de Grupo Z abaixo. É um snapshot de produto/estoque (quantidade, custo, preço e margem cadastrados numa data única), não uma Curva ABC de vendas. Confirmado pela estrutura do arquivo (colunas Código, Dt. Compra, Produto, Fabricante, Unid. Estoque, Qtde., Custo inicial, % ICMS/IPI/ST/FRETE/OUTROS, Custo Final, % Margem, Preço, NCM, Código de Barras, Fornecedor, Qtde. última compra): não tem quantidade vendida nem faturamento, então **não atualiza giro nem participação por categoria de faturamento nesta rodada**. Formato HTML, não PDF, então não passa pela ferramenta de padronização de Curva ABC (`Operacional/Método Viga Mestra/1 - Inteligência de Dados/1 - Curva ABC do Estoque/SKILL.md`), que é específica pra PDF de Curva ABC; processado com parser próprio (regex determinístico, zero IA na extração).
**Ver também:** faturamento, margem e giro por SKU dos 4 períodos de venda cobertos pelo histórico deste cliente estão em `../1 - Curva ABC do Estoque/diagnostico-curva-abc.md`.

### Resumo executivo
- Catálogo no relatório: **15.369 SKUs** (contra 15.254 SKUs distintos no histórico dos 4 períodos de Curva ABC, mai/2025 a jun/2026: 115 SKUs novos, sem histórico de venda pra avaliar)
- Valor de estoque a custo, leitura bruta (direto do relatório, todos os itens com saldo positivo): **R$ 19.111.367,72** em 4.848 SKUs
- **2 itens sozinhos respondem por R$ 17.456.023,32 (91,3%) desse valor bruto**, com quantidade/custo em forte desacordo com os pares da própria linha de produto. Somado a um terceiro item recorrente (colorante, já conhecido desde 23/07), os 3 outliers somam **R$ 18.176.265,52 (95,1%) do valor bruto total**
- **Valor de estoque a custo, leitura ajustada (excluindo os 3 outliers): R$ 935.102,19**, crescimento de R$ 34.161,81 (+3,79%) frente aos R$ 900.940,38 registrados em 25/07/2026 (`Estoque em 27-06-26.xls`), variação plausível para 5 semanas de operação
- Estoque parado atualizado (sem venda nos 4 períodos históricos, ajustado): **R$ 373.769,46 em 1.732 SKUs** (detalhe na seção própria abaixo)
- Nenhum dado de faturamento, giro ou participação por categoria de venda foi recalculado nesta rodada, esse relatório não traz essa informação

**Principais achados (o que muda decisão):**
1. **O estoque parado é fortemente concentrado.** 103 produtos, 5,9% dos 1.732 itens parados, respondem por 70% do valor a custo parado (R$ 261.795,55 de R$ 373.769,46). Os 1.629 produtos restantes (cauda longa) somam só R$ 111.973,91, pouco relevantes um a um pra decisão de liquidar.
2. **O maior item parado em valor não é "estoque velho".** Cumeeira Zincalum 0,43 (R$ 77.948,00 a custo, 20,9% de todo o valor parado ajustado) só entrou no catálogo em jan/2026, cruzando com os 4 relatórios de Curva ABC. Está parado há cerca de 7 meses, não 14 meses ou mais como a maioria da lista. Vale checar com o Tony se é item recém comprado que não girou, ou erro de lançamento de entrada.
3. **O potencial de venda do estoque parado, se tudo fosse vendido ao preço cadastrado, é R$ 729.454,20, quase o dobro do valor a custo (R$ 373.769,46).** Mas o segundo maior item desse ranking, Tubo PVC Rosca 1 Pol Tigre (R$ 95.983,68 de potencial), tem markup cadastrado de 1.091% sobre o custo, um dos 24 itens já sinalizados na auditoria com margem acima de 1.000%. Esse valor específico deve ser tratado com reserva até confirmação de cadastro, não como fato.
4. **A maioria dos itens parados não tem como saber o tempo exato sem venda, só um piso.** 1.720 dos 1.732 produtos (99,3%) já existiam no primeiro relatório de Curva ABC (mai/2025) e nunca tiveram venda registrada nos 14 meses seguintes, então o "tempo sem venda" real pode ser maior que 14 meses, mas não dá pra confirmar por quanto. Só 12 produtos (0,7%) entraram no catálogo depois (jan/2026), esses têm piso mais curto, cerca de 7 meses.

### Limitações da fonte de dados
1. **Sem dado de venda/faturamento.** Este relatório só traz estoque, custo e preço cadastrados. Giro (quantidade vendida) e participação por categoria de faturamento continuam sendo os documentados por período em `diagnostico-curva-abc.md`, não foram atualizados nesta rodada.
2. **Sem coluna de categoria própria.** Ao contrário do `Estoque ETL.xlsx` usado em 23/07, este relatório não tem campo de categoria/grupo. Mapeei a categoria por cruzamento do `codigo` com o campo `grupo_produto` da Curva ABC mais recente (abr-jun/2026), cobrindo 15.217 dos 15.369 SKUs (99,0%). Os 152 SKUs sem categoria mapeada (0,99% dos itens, R$ 7.856,01 do valor bruto de estoque) são majoritariamente SKUs novos, criados depois de jun/2026.
3. **Categoria corrompida no cadastro do cliente, mesmo problema já reportado em 25/07/2026.** Via o cruzamento acima, 5.254 SKUs do relatório atual mapeiam para a categoria corrompida "MD-MD-MD-MD-MD-...". Segue pendente de correção no ERP do cliente.
4. **2 outliers críticos de cadastro identificados nesta rodada, não vistos nos relatórios anteriores** (ver auditoria abaixo). Excluídos de todos os totais "ajustados" deste diagnóstico até confirmação do Tony.
5. **Tempo sem venda por SKU parado é um piso, não uma data exata, e varia entre os itens.** O sistema do cliente não tem campo de data de última venda, só ausência de venda nos relatórios de Curva ABC (limitação já registrada nas atualizações anteriores). Nesta rodada, cruzei o código de cada um dos 1.732 produtos parados com os 4 arquivos originais de Curva ABC (não só o flag agregado da planilha de estoque) pra identificar em qual período cada SKU aparece pela primeira vez. 1.720 SKUs já existiam desde o primeiro período (mai-out/2025), então cobrem os 14 meses inteiros da série sem nenhuma venda, mas sem dado de venda anterior a mai/2025 nem posterior a jun/2026 (o piso real pode ser maior). 12 SKUs só aparecem a partir do período jan-mar/2026 (mesmo conjunto dos 26 SKUs novos identificados no catálogo geral), esses têm piso mais curto, cerca de 7 meses, e não devem ser somados ao grupo de 14+ meses.

*As seções abaixo são o detalhamento analítico, produto a produto, para consulta durante a reunião. O resumo acima já traz o que muda a decisão.*

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

Nota sobre o campo "% Margem" deste relatório: é **markup sobre custo** ((Preço - Custo Final) / Custo Final × 100), cadastrado pelo próprio sistema Pontual. Não é o mesmo cálculo de "margem bruta % sobre venda" usado em `diagnostico-curva-abc.md` (que é sobre faturamento real). Os dois não devem ser comparados diretamente.

### Outliers críticos identificados (pendente de confirmação do cliente)
| Código | Produto | Campo suspeito | Valor cadastrado | Benchmark de pares (mesma linha) | Estimativa | Impacto no valor de estoque |
|---|---|---|---|---|---|---|
| 7153 | CABO FLEX 2.5MM AZ PC COBRECOM | Quantidade | 79.263,90 PC | Outras cores da mesma linha "PC COBRECOM" (vermelho, verde, amarelo, preto): estoque entre 0 e 0,035 PC. Outras marcas de cabo flex 2,5mm no catálogo: estoque entre 0 e 635 MT | Quantidade real provavelmente entre 0 e poucas centenas de unidades, não 79 mil. Não estimo um número exato, é caso de erro de lançamento (unidade ou dígito a mais), não de custo errado | R$ 14.161.290,32 (74,1% do valor bruto de estoque) |
| 7874 | MANGUEIRA CORRUGADA 20MM AM - KRONA | Quantidade e custo | 164.736.600 MT, custo R$ 0,02/MT | Mangueira corrugada 20mm de outras marcas: estoque entre 32 e 239 MT, custo entre R$ 0,91 e R$ 1,22/MT | Quantidade real provavelmente na mesma ordem de grandeza dos pares (dezenas a poucas centenas de MT), custo também provavelmente mais próximo de R$ 0,90 a R$ 1,20/MT | R$ 3.294.733,00 (17,2% do valor bruto de estoque) |
| 11073 | COLORANTE ICORES BA AMARELO P0411 0.9L | Custo final | R$ 158,67/ML | Outros 9 colorantes da mesma linha (Icores BA, 0,9L, unidade ML): custo entre R$ 0,09 e R$ 0,23/ML, mediana R$ 0,13/ML | R$ 0,13 a R$ 0,18/ML (mesma faixa já usada nos 4 períodos de Curva ABC, ver `diagnostico-curva-abc.md`). **Mesmo item já reportado ao Tony em 23/07/2026 e confirmado como erro de cadastro, segue sem correção no ERP em 03/08/2026** | R$ 720.244,40 (3,8% do valor bruto de estoque) |

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
- **Valor potencial de venda do estoque parado ajustado (qtde × preço cadastrado, mesmos 1.732 SKUs): R$ 729.454,20** (dado novo desta rodada, não calculado nas atualizações anteriores). Ver ressalva do item Tubo PVC Rosca 1 Pol Tigre na tabela "por potencial de venda" abaixo antes de tratar esse total como confirmado.
- Comparação com 25/07/2026 (`Estoque em 27-06-26.xls`): R$ 295.126,57 em 1.695 SKUs → R$ 373.769,46 em 1.732 SKUs (alta de R$ 78.642,89, +26,6% em valor, com só +37 SKUs, +2,2%, ou seja o valor médio por item parado subiu bem mais que a quantidade de itens parados)
- 68 SKUs novos (sem histórico de venda nos 4 períodos, criados depois de jun/2026) têm estoque positivo hoje e não entram no cálculo de parado por falta de janela de avaliação: R$ 7.254,58 a custo

**Correção a um apontamento da rodada anterior:** a nota de 25/07/2026 dizia que "Vareta Solda Oxi e Cumeeira Zincalum já apareciam como maiores itens parados individuais nos períodos de nov-dez/2025 e jan-mar/2026 respectivamente, confirma que são itens realmente parados de longa data". Isso segue verdadeiro pra Vareta Solda Oxi (código 3746, presente desde o primeiro relatório de Curva ABC, mai-out/2025, sem venda há 14+ meses). Não é verdade pra Cumeeira Zincalum (código 1986): o cruzamento desta rodada mostra que esse código só passou a existir no catálogo a partir do relatório de jan-mar/2026, então está parado há cerca de 7 meses, não 14+. O fato de ele aparecer como "maior item individual" já no período jan-mar/2026 (primeira vez que existe no catálogo) e não em nov-dez/2025 é consistente com essa conclusão, não uma contradição, mas a leitura de "parado de longa data" estava errada pra esse item específico. Ver "Principais achados" no topo desta seção.

**Cobertura das listas abaixo (critério de concentração de valor, princípio 8 do SKILL.md):** a tabela "Top produtos parados" e a "por valor de custo" cobrem 103 produtos = 70,0% do valor a custo parado (R$ 261.795,55 de R$ 373.769,46). Os 1.629 SKUs restantes (cauda longa) somam R$ 111.973,91 (30,0%), consolidados sem detalhamento linha a linha por não mudarem a decisão individualmente. A tabela "por potencial de venda" usa o mesmo critério aplicado à dimensão de valor potencial: 76 produtos = 70,0% (R$ 510.879,96 de R$ 729.454,20), cauda longa de 1.656 SKUs somando R$ 218.574,24 (30,0%). Listas completas nas duas abas de `08-2026/top-relevantes-parados_2026-08-03.xlsx`.

#### Top produtos parados
Amostra dos 20 maiores itens por valor a custo, ordenados do maior pro menor (lista completa de 103 produtos, 70% do valor a custo parado, na aba "Top por valor de custo" da planilha derivada):

| Produto | Categoria | Tempo sem venda | Qtd em estoque | Custo unitário | Valor total a custo | Preço de venda unitário | Valor potencial de venda |
|---|---|---|---|---|---|---|---|
| Cumeeira Zincalum 0,43 | Material Básico | ~7 meses | 2.998 UN | R$ 26,00 | R$ 77.948,00 | R$ 41,00 | R$ 122.918,00 |
| Vareta Solda Oxi 1,59mm Gerdau | (categoria corrompida) | ≥14 meses | 7.329 UN | R$ 10,20 | R$ 74.755,80 | R$ 25,00 | R$ 183.225,00 |
| Sacolas 30x40 Imp | Material de Uso e Consumo | ≥14 meses | 2.005 UN | R$ 11,66 | R$ 23.378,30 | R$ 0,20 | R$ 401,00 |
| Sacola Recicladas VD 60x80 | Material de Uso e Consumo | ≥14 meses | 1.015 KG | R$ 11,50 | R$ 11.672,50 | R$ 20,00 | R$ 20.300,00 |
| Tubo PVC Rosca 1 pol Tigre | (categoria corrompida) | ≥14 meses | 999,83 PC | R$ 8,06 | R$ 8.058,63 | R$ 96,00 | R$ 95.983,68 |
| Metalon Galv 30mm x 20mm 1.25mm Ch 18 | Material Básico | ≥14 meses | 47,20 PC | R$ 62,36 | R$ 2.943,39 | R$ 95,00 | R$ 4.484,00 |
| Torneira Met Filtro Abs BM 2172 C40 CR Imperatriz Metais | (categoria corrompida) | ≥14 meses | 27 UN | R$ 96,28 | R$ 2.599,56 | R$ 160,00 | R$ 4.320,00 |
| Tela Alambrado Practica Fio 2.400mm 5x15 Alt 1.57mt Belgo | Material Básico | ≥14 meses | 50 MT | R$ 42,60 | R$ 2.130,00 | R$ 80,00 | R$ 4.000,00 |
| Bob. Termica 80 x 40 mts Personalizada | Material de Uso e Consumo | ≥14 meses | 630 UN | R$ 2,83 | R$ 1.782,90 | R$ 2,85 | R$ 1.795,50 |
| Bacia p/Caixa Acopl Izy Conforto BR Deca | Louças Sanitárias | ≥14 meses | 3 UN | R$ 527,27 | R$ 1.581,81 | R$ 770,00 | R$ 2.310,00 |
| Colorante Icores BA Az Intenso P0441 0.9L | Pintura | ≥14 meses | 6.708,31 MLS | R$ 0,23 | R$ 1.542,91 | R$ 0,37 | R$ 2.482,07 |
| Porcelanato Bali Polido 61x61 CX 1.88M2 Tipo A Cercamp | Cerâmica | ≥14 meses | 30,08 M2 | R$ 48,84 | R$ 1.469,11 | R$ 70,00 | R$ 2.105,60 |
| Kit Aço Cacau 40 Cozimax | Armários, Gabinetes | ≥14 meses | 4 UN | R$ 342,51 | R$ 1.370,04 | R$ 400,00 | R$ 1.600,00 |
| Boné Personalizado Construmais | Material de Uso e Consumo | ≥14 meses | 50 UN | R$ 25,00 | R$ 1.250,00 | R$ 42,50 | R$ 2.125,00 |
| Papel Report Pr.A4 500F GR75 | Utilidades e Jardim | ≥14 meses | 46 UN | R$ 27,05 | R$ 1.244,30 | R$ 34,00 | R$ 1.564,00 |
| Sacola Camiseta Impresso/Alta 70x90x0,03 | Material de Uso e Consumo | ≥14 meses | 2.000 UN | R$ 0,57 | R$ 1.140,00 | R$ 0,30 | R$ 600,00 |
| Porta Semi Oca Mogno 2.10x0.60x30mm Alpha | Esquadrias | ≥14 meses | 10 UN | R$ 99,90 | R$ 999,00 | R$ 170,00 | R$ 1.700,00 |
| Icores Delanil Fosco Base P 16L | Pintura | ≥14 meses | 4 UN | R$ 245,59 | R$ 982,36 | R$ 370,00 | R$ 1.480,00 |
| Sacola Camiseta Impresso/Alta 50x70x0,03 | Material de Uso e Consumo | ≥14 meses | 3.000 UN | R$ 0,32 | R$ 960,00 | R$ 0,11 | R$ 330,00 |
| Saco Reciclado Impresso Transparente 43x70 KG | Material de Uso e Consumo | ≥14 meses | 50 KG | R$ 18,00 | R$ 900,00 | R$ 23,40 | R$ 1.170,00 |

Legenda de "Tempo sem venda": "≥14 meses" = SKU já existia no primeiro relatório de Curva ABC (mai-out/2025) e não teve nenhuma venda registrada nos 4 períodos seguintes (piso, não data exata). "~7 meses" = SKU só passou a existir no catálogo a partir do relatório de jan-mar/2026, sem venda desde então.

#### Top produtos parados por valor de custo (maior capital imobilizado)
Mesmo critério de ordenação da tabela acima (valor a custo, a pergunta "onde está o capital parado"), versão compacta com 10 linhas pra consulta rápida. A lista completa de 103 produtos (mesma cobertura de 70%) está na aba "Top por valor de custo" de `top-relevantes-parados_2026-08-03.xlsx`, idêntica à base da tabela "Top produtos parados" acima.

| Produto | Categoria | Tempo sem venda | Qtd em estoque | Valor total a custo |
|---|---|---|---|---|
| Cumeeira Zincalum 0,43 | Material Básico | ~7 meses | 2.998 UN | R$ 77.948,00 |
| Vareta Solda Oxi 1,59mm Gerdau | (categoria corrompida) | ≥14 meses | 7.329 UN | R$ 74.755,80 |
| Sacolas 30x40 Imp | Material de Uso e Consumo | ≥14 meses | 2.005 UN | R$ 23.378,30 |
| Sacola Recicladas VD 60x80 | Material de Uso e Consumo | ≥14 meses | 1.015 KG | R$ 11.672,50 |
| Tubo PVC Rosca 1 pol Tigre | (categoria corrompida) | ≥14 meses | 999,83 PC | R$ 8.058,63 |
| Metalon Galv 30mm x 20mm 1.25mm Ch 18 | Material Básico | ≥14 meses | 47,20 PC | R$ 2.943,39 |
| Torneira Met Filtro Abs BM 2172 C40 CR Imperatriz Metais | (categoria corrompida) | ≥14 meses | 27 UN | R$ 2.599,56 |
| Tela Alambrado Practica Fio 2.400mm 5x15 Alt 1.57mt Belgo | Material Básico | ≥14 meses | 50 MT | R$ 2.130,00 |
| Bob. Termica 80 x 40 mts Personalizada | Material de Uso e Consumo | ≥14 meses | 630 UN | R$ 1.782,90 |
| Bacia p/Caixa Acopl Izy Conforto BR Deca | Louças Sanitárias | ≥14 meses | 3 UN | R$ 1.581,81 |

#### Top produtos parados por potencial de venda
Ordenado por valor potencial de venda (qtde × preço cadastrado), critério diferente do custo, muda a ordem porque markup varia por item. Amostra de 15 (lista completa de 76 produtos, 70% do valor potencial de venda, na aba "Top por potencial de venda" da planilha derivada):

| Produto | Categoria | Tempo sem venda | Qtd em estoque | Preço de venda unitário | Valor potencial de venda |
|---|---|---|---|---|---|
| Vareta Solda Oxi 1,59mm Gerdau | (categoria corrompida) | ≥14 meses | 7.329 UN | R$ 25,00 | R$ 183.225,00 |
| Cumeeira Zincalum 0,43 | Material Básico | ~7 meses | 2.998 UN | R$ 41,00 | R$ 122.918,00 |
| Tubo PVC Rosca 1 pol Tigre | (categoria corrompida) | ≥14 meses | 999,83 PC | R$ 96,00 | R$ 95.983,68 |
| Sacola Recicladas VD 60x80 | Material de Uso e Consumo | ≥14 meses | 1.015 KG | R$ 20,00 | R$ 20.300,00 |
| Metalon Galv 30mm x 20mm 1.25mm Ch 18 | Material Básico | ≥14 meses | 47,20 PC | R$ 95,00 | R$ 4.484,00 |
| Torneira Met Filtro Abs BM 2172 C40 CR Imperatriz Metais | (categoria corrompida) | ≥14 meses | 27 UN | R$ 160,00 | R$ 4.320,00 |
| Tela Alambrado Practica Fio 2.400mm 5x15 Alt 1.57mt Belgo | Material Básico | ≥14 meses | 50 MT | R$ 80,00 | R$ 4.000,00 |
| Colorante Icores BA Az Intenso P0441 0.9L | Pintura | ≥14 meses | 6.708,31 MLS | R$ 0,37 | R$ 2.482,07 |
| Bacia p/Caixa Acopl Izy Conforto BR Deca | Louças Sanitárias | ≥14 meses | 3 UN | R$ 770,00 | R$ 2.310,00 |
| Boné Personalizado Construmais | Material de Uso e Consumo | ≥14 meses | 50 UN | R$ 42,50 | R$ 2.125,00 |
| Porcelanato Bali Polido 61x61 CX 1.88M2 Tipo A Cercamp | Cerâmica | ≥14 meses | 30,08 M2 | R$ 70,00 | R$ 2.105,60 |
| Sacolas 40x50 Imp. | Material de Uso e Consumo | ≥14 meses | 5.000 UN | R$ 0,40 | R$ 2.000,00 |
| Bob. Termica 80 x 40 mts Personalizada | Material de Uso e Consumo | ≥14 meses | 630 UN | R$ 2,85 | R$ 1.795,50 |
| Porta Semi Oca Mogno 2.10x0.60x30mm Alpha | Esquadrias | ≥14 meses | 10 UN | R$ 170,00 | R$ 1.700,00 |
| Kit Aço Cacau 40 Cozimax | Armários, Gabinetes | ≥14 meses | 4 UN | R$ 400,00 | R$ 1.600,00 |

**Ressalva sobre o 3º colocado (Tubo PVC Rosca 1 pol Tigre):** markup cadastrado de 1.091% sobre o custo (custo R$ 8,06, preço R$ 96,00), um dos 24 itens já sinalizados na "Auditoria de qualidade do cadastro" acima com margem acima de 1.000%. Não é um dos 3 outliers críticos já excluídos (não teve benchmark de linha feito ainda), mas o valor de potencial de venda desse item específico (R$ 95.983,68, 13,2% do potencial total da lista de 70%) deve ser tratado com reserva até o Tony confirmar se o preço ou o custo cadastrado estão corretos.

Estoque parado por categoria (ajustado, exclui outliers): categoria corrompida "MD-MD-MD..." concentra 27,4% do valor parado ajustado (R$ 102.131,64), seguida de Material Básico (22,5%, R$ 83.968,25) e Material de Uso e Consumo (14,6%, R$ 54.545,54). Ver planilha para o detalhe completo por SKU.

### Produtos isca / âncora, checagem de cadastro
Sem dado de venda nesta rodada, não é possível reconfirmar giro. Checagem só de preço/custo/margem cadastrados:
- **Cimento Montes Claros CPII F 32 50kg** (código 8992): 27,5 sc em estoque, custo R$ 37,90, preço R$ 51,00, markup cadastrado 34,56%
- **Cimento Poty CPII Z 32 50kg** (código 7972): 174 sc em estoque, custo R$ 38,22, preço R$ 51,00, markup cadastrado 33,44%

Preço e custo seguem na mesma faixa dos períodos anteriores, sem sinal de descontinuação (estoque positivo nos dois). O markup cadastrado (33-35%) não é diretamente comparável à margem sobre venda dos períodos de Curva ABC (21-22%, ver `diagnostico-curva-abc.md`), são cálculos diferentes (markup sobre custo vs margem sobre faturamento real). Reconfirmação de giro depende de um novo export de Curva ABC (jul/ago 2026).

### Comparação com o snapshot anterior (`Estoque em 27-06-26.xls`, 27/06/2026)
- Valor de estoque a custo (ajustado): R$ 900.940,38 → R$ 935.102,19 (alta de 3,79% em 5 semanas)
- Estoque parado (ajustado): R$ 295.126,57 em 1.695 SKUs → R$ 373.769,46 em 1.732 SKUs (alta de 26,6% em valor, 2,2% em SKUs, o valor médio por item parado cresceu mais que a contagem)
- Catálogo: cresceu de 15.228 para 15.369 SKUs cadastrados (a base de comparação de "novos" usada nesta seção, 15.254 SKUs, vem da Curva ABC, não do `Estoque ETL.xlsx`, por isso os números não batem exatos entre si)
- 2 outliers críticos novos identificados nesta rodada (cabo flex e mangueira), não presentes com essa magnitude nos relatórios anteriores

### Próximos passos
1. **Confirmar com o Tony os 2 outliers novos** (código 7153, Cabo Flex, quantidade 79.263,9 PC; código 7874, Mangueira Corrugada Krona, quantidade 164.736.600 MT e custo R$ 0,02/MT) antes de tratar como estoque real. Corrigir no ERP.
2. **Cobrar novamente a correção do colorante** (código 11073, pendente desde 23/07/2026, ainda não corrigido em 03/08/2026)
3. **Solicitar novo export de Curva ABC** (PDF, jul/ago 2026) pra atualizar giro, faturamento e participação por categoria de venda, este relatório não traz esse dado (handoff pra `diagnostico-curva-abc.md`)
4. Reportar de novo a categoria corrompida no cadastro (5.254 SKUs "MD-MD-MD...", pendência desde 25/07/2026, segue sem correção)
5. `@analista-dados` pode usar o estoque parado atualizado (R$ 373.769,46) como KPI de dashboard no lugar do valor de 25/07/2026
6. **Confirmar com o Tony o caso da Cumeeira Zincalum 0,43** (código 1986, maior item parado em valor, R$ 77.948,00): item entrou no catálogo em jan/2026 e nunca vendeu, checar se é excesso de compra recente ou erro de lançamento de entrada, antes de tratar como candidato padrão de liquidação de "estoque velho"
7. **Confirmar cadastro do Tubo PVC Rosca 1 Pol Tigre** (código 3214, markup cadastrado 1.091% sobre o custo): checar se o preço de R$ 96,00 ou o custo de R$ 8,06 estão corretos antes de usar o valor potencial de venda desse item (R$ 95.983,68) em qualquer decisão

---

## Período/Snapshot: 01/04/2026 a 30/06/2026 (Grupo Z da Curva ABC)
**Fonte dos dados:** Grupo Z de `Curva ABC parte 4.pdf` (sistema Pontual Tecnologia, SKUs sem nenhuma venda no período), processado em 07-2026. Faturamento, margem e giro do mesmo relatório: ver `../1 - Curva ABC do Estoque/diagnostico-curva-abc.md`, seção "Período: 01/04/2026 a 30/06/2026".
**Planilha(s):** `../1 - Curva ABC do Estoque/07-2026/curva-abc-padronizada_2026-04-01_a_2026-06-30.xlsx` (mesma planilha da Curva ABC, SKUs do Grupo Z sem venda no período)
**Status:** v1, sujeito a refinamento

### Estoque parado (sem venda no período, com saldo em estoque)
- Valor financeiro parado a custo, já corrigido pelo erro de cadastro do colorante (código 11073, ver `diagnostico-curva-abc.md`, mesmo período, limitação 1): **≈ R$ 469.329,89**, em 2.865 SKUs
- Valor bruto do relatório, sem a correção (não usar como referência): R$ 1.191.429,70

### Comparação com o período/snapshot anterior (01/01/2026 a 31/03/2026)
- Estoque parado corrigido: R$ 491.900,30 → R$ 469.329,89 (queda de 4,6%)

---

## Período/Snapshot: 01/01/2026 a 31/03/2026 (Grupo Z da Curva ABC)
**Fonte dos dados:** Grupo Z de `Curva ABC parte 3.pdf` (sistema Pontual Tecnologia, SKUs sem nenhuma venda no período), processado em 07-2026. Faturamento, margem e giro do mesmo relatório: ver `../1 - Curva ABC do Estoque/diagnostico-curva-abc.md`, seção "Período: 01/01/2026 a 31/03/2026".
**Planilha(s):** `../1 - Curva ABC do Estoque/07-2026/curva-abc-padronizada_2026-01-01_a_2026-03-31.xlsx` (mesma planilha da Curva ABC, SKUs do Grupo Z sem venda no período)
**Status:** v1, sujeito a refinamento

### Estoque parado (sem venda no período, com saldo em estoque)
- Valor financeiro parado a custo, já corrigido: **≈ R$ 491.900,30**, em 2.987 SKUs
- Valor bruto do relatório: R$ 1.214.000,11
- Maior item individual, fora o colorante: Cumeeira Zincalum 0,43, 2.998 un a R$ 26,00, R$ 77.948,00

### Comparação com o período/snapshot anterior (01/11/2025 a 31/12/2025)
- Estoque parado corrigido: R$ 467.599,36 → R$ 491.900,30 (subiu 5,2%)

---

## Período/Snapshot: 01/11/2025 a 31/12/2025 (Grupo Z da Curva ABC)
**Fonte dos dados:** Grupo Z de `Curva ABC parte 2.pdf` (sistema Pontual Tecnologia, SKUs sem nenhuma venda no período), processado em 07-2026. Faturamento, margem e giro do mesmo relatório: ver `../1 - Curva ABC do Estoque/diagnostico-curva-abc.md`, seção "Período: 01/11/2025 a 31/12/2025".
**Planilha(s):** `../1 - Curva ABC do Estoque/07-2026/curva-abc-padronizada_2025-11-01_a_2025-12-31.xlsx` (mesma planilha da Curva ABC, SKUs do Grupo Z sem venda no período)
**Status:** v1, sujeito a refinamento

### Estoque parado (sem venda no período, com saldo em estoque)
- Valor financeiro parado a custo, já corrigido: **≈ R$ 467.599,36**, em 3.381 SKUs
- Valor bruto do relatório: R$ 1.195.222,01
- Maior item individual, fora o colorante: Vareta Solda Oxi 1,59mm Gerdau, 7.329 un, R$ 74.755,80

### Comparação com o período/snapshot anterior (01/05/2025 a 31/10/2025)
- Estoque parado corrigido: R$ 424.367,42 → R$ 467.599,36 (subiu 10,2%)

### Próximos passos
1. Entender por que o estoque parado corrigido subiu 10,2% frente ao período anterior (item de acompanhamento herdado de `diagnostico-curva-abc.md` na migração estrutural de 12/08/2026, ainda em aberto)

---

## Período/Snapshot: 01/05/2025 a 31/10/2025 (Grupo Z da Curva ABC)
**Fonte dos dados:** Grupo Z de `Curva ABC parte 1.pdf` (sistema Pontual Tecnologia, SKUs sem nenhuma venda no período), processado em 07-2026. Faturamento, margem e giro do mesmo relatório: ver `../1 - Curva ABC do Estoque/diagnostico-curva-abc.md`, seção "Período: 01/05/2025 a 31/10/2025".
**Planilha(s):** `../1 - Curva ABC do Estoque/07-2026/curva-abc-padronizada_2025-05-01_a_2025-10-31.xlsx` (mesma planilha da Curva ABC, SKUs do Grupo Z sem venda no período)
**Status:** v1, sujeito a refinamento

### Estoque parado (sem venda no período, com saldo em estoque)
- Valor financeiro parado a custo, já corrigido pelo erro de cadastro do colorante (código 11073): **≈ R$ 424.367,42**, em 2.661 SKUs
- Valor bruto do relatório, sem a correção (não usar como referência): R$ 1.153.904,99
- Maior item individual, fora o colorante já corrigido: Vareta Solda Oxi 1,59mm Gerdau, 7.329 un a R$ 10,20, R$ 74.755,80
- Limitação: este PDF veio em "formato simples", sem colunas de categoria. O filtro de estoque parado não teve como excluir ativo imobilizado por categoria da mesma forma que nos outros 3 períodos, usou só grupo Z + estoque positivo (ver `diagnostico-curva-abc.md`, mesmo período, limitação 4).

Período mais antigo do histórico processado até agora, não há período/snapshot anterior pra comparar.
