# Diagnóstico de Estoque e Giro para Construmais

> **⚠️ ARQUIVO SUPERADO (nota de 2026-07-25).** A fonte da verdade atual do Pilar 1 é `outputs/1 - Inteligência de Dados/1 - Curva ABC do Estoque/diagnostico-estoque.md` (diagnóstico cumulativo por período, produzido com a ferramenta determinística de padronização de Curva ABC). Este arquivo fica preservado como registro da análise de 23/07/2026: os totais de 14 meses foram reconciliados entre as duas análises (faturamento R$ 3.081.818,22, margem 39,27%), e o estoque parado de referência foi recalculado em 25/07 (R$ 295.126,57 em 1.695 produtos, ver Histórico do CLIENTE.md, 23ª atualização). Não usar os números daqui pra decisão nova sem conferir o diagnóstico atual.

**Fonte dos dados:** análise direta dos 5 arquivos originais exportados do ERP (Pontual Tecnologia), sem uso de resumo de conversa anterior: `Curva ABC parte 1.pdf` (45 páginas, período 01/05/2025 a 31/10/2025), `Curva ABC parte 2.pdf` (41 páginas, 01/11/2025 a 31/12/2025), `Curva ABC parte 3.pdf` (41 páginas, 01/01/2026 a 31/03/2026), `Curva ABC parte 4.pdf` (41 páginas, 01/04/2026 a 30/06/2026) e `Estoque ETL.xlsx` (aba "Estoque", 15.228 linhas de produto, mais uma aba "Dina" não analisada em detalhe por não ser fonte primária de estoque). Os 168 páginas de PDF foram lidas por completo, na íntegra, célula a célula, com script próprio de extração (não houve leitura parcial nem amostragem).

**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra

**Status:** v1, sujeito a refinamento. Esta versão substitui por completo a anterior, que era uma compilação de resumos de conversas antigas. Os números abaixo vêm de leitura direta dos arquivos brutos, célula a célula, com o método de extração documentado em cada seção.

## Nota de metodologia (leia antes de usar os números)

Os PDFs de Curva ABC não são texto simples: são relatórios tabulares densos, e a ferramenta de extração de texto (pdftotext, modo tabela) tem duas limitações que afetam a precisão de alguns números:

1. **Parte 1** não traz colunas de categoria de produto (Grupo/Sub-grupo), só código, produto e os números de giro/margem. As Partes 2, 3 e 4 trazem essas colunas. Por isso, a categorização de produto usada neste diagnóstico vem do cadastro atual da planilha `Estoque ETL.xlsx` (coluna "Grupo"), cruzado por código com os números de venda da Curva ABC, e não da Parte 1 isolada.
2. A soma linha a linha dos valores de venda extraídos de cada PDF fica entre 96,5% e 98,8% do total oficial impresso no rodapé de cada relatório (ex: Parte 1 imprime "Total Geral: 882.458,27 ... 1.377.269,74 ... 35,93" ao final, que é o número de referência usado). A diferença vem de um pequeno número de linhas (por volta de 19 por parte, de um total de mais de 15 mil) com unidade de medida não padrão (ex: "5/8", "3PCS") que o script não conseguiu separar com segurança. Nesses casos, o **total oficial impresso no rodapé do relatório é a fonte usada no resumo executivo**, e a soma linha a linha é usada só para as quebras por categoria e os rankings, com a ressalva de cobertura declarada.
3. Uma única linha da Parte 1 (código 48, TIJOLO C/8 FUROS 09X19X19) teve o valor de venda corrompido pela extração: o texto "Venda Total" apareceu como "Venda Tota1l" com um dígito "1" absorvido pela palavra, fazendo o número perder R$ 100.000 (aparecia R$ 22.202,00 em vez de R$ 122.202,00). Isso foi identificado porque a soma de todas as linhas só batia com o total oficial do rodapé depois dessa correção pontual, e o valor corrigido reconcilia margem, custo e venda com precisão de centavos. Não há evidência de outras linhas com esse problema (a soma bateu exatamente após esse ajuste único).

## Resumo executivo

- **Faturamento total do período analisado (14 meses, 01/05/2025 a 30/06/2026):** R$ 3.081.818,22 (soma dos 4 totais oficiais impressos nos relatórios, não uma soma linha a linha)
- **Custo total do período:** R$ 1.871.502,08
- **Margem bruta agregada:** R$ 1.210.316,14 (39,27% sobre a venda)
- **Média mensal de faturamento:** R$ 220.129,87
- **Catálogo ativo no cadastro:** 15.228 SKUs distintos (linhas da aba "Estoque"), consistente com a contagem de códigos únicos vista nos 4 relatórios de Curva ABC (entre 15.156 e 15.195 por período, pequena variação porque produtos entram e saem do catálogo entre um período e outro)
- **Curva ABC (participação no faturamento, calculada separadamente em cada um dos 4 períodos):** Classe A entre 56,7% e 60,2% do faturamento, Classe B entre 24,7% e 27,1%, Classe C entre 15,1% e 16,2%. A composição é notavelmente estável nos 4 períodos, o retrato mais recente (Parte 4, abril a junho de 2026) é A 59,2% / B 25,4% / C 15,4%.
- **Limitações da fonte:** (1) o sistema Pontual Tecnologia exporta por período fechado escolhido na hora de gerar o relatório, não por corte mensal contínuo nativo, os 14 meses vêm de 4 exportações separadas; (2) a Parte 1 não tem coluna de categoria de produto (ver nota de metodologia); (3) a soma linha a linha cobre entre 96,5% e 98,8% do faturamento oficial por período, o restante não some, é atribuído a um pequeno número de linhas com unidade de medida atípica que o parser não conseguiu separar com segurança.

## Comparação com o diagnóstico anterior (o que bate, o que não bate)

O diagnóstico de 2026-07 anterior foi montado a partir de resumos de conversa, não do arquivo. Com acesso direto aos 5 arquivos, o resultado é o seguinte:

### Confirmado com exatidão
| Item | Valor anterior | Valor confirmado agora |
|---|---|---|
| Faturamento total 14 meses | R$ 3.081.818 | R$ 3.081.818,22 |
| Curva ABC (A/B/C) | 59,9% / 25,1% / 15,0% | 56,7 a 60,2% / 24,7 a 27,1% / 15,1 a 16,2% (varia por período, dentro da faixa citada) |
| Fornecedor cadastrado como a própria loja | 57 itens | 57 itens |
| Quantidade de estoque negativa | 17 itens | 17 itens |
| Preço de venda zerado com estoque ativo | 4 itens | 4 itens |
| Margem acima de 1.000% | 27 itens | 27 itens |
| Margem negativa | 199 itens | 199 itens |
| Categoria/grupo corrompido | cerca de 35% da base, 5.257 itens | 34,52% da base, 5.257 itens (exato) |
| Participação de Material Básico | 43% | 42,21% |
| Kit Alvenaria (tijolo + argamassa) | margem sobe de 33,8% para 34,49% | confirmado com cálculo direto: 33,82% para 34,49% |
| Kit Estrutura (cimento + gesso + bloco) | margem sobe de 14,4% para 16,16% | confirmado com cálculo direto: 14,39% para 16,16% |

### Próximo, mas não exato
| Item | Valor anterior | Valor confirmado agora | Observação |
|---|---|---|---|
| Custo final menor que custo inicial | 103 itens | 104 itens | diferença de 1 item, dentro da margem de um caso de fronteira |
| Custo zerado com vendas ativas | 2 itens | 1 item | só encontrei 1 código (1813, BORRACHA SILICONIZADA) com custo final zerado e venda registrada na Curva ABC nos 14 meses |
| Produto duplicado com código diferente | 20 itens | 10 grupos de nome idêntico, 24 códigos no total | metodologia provavelmente diferente (contagem de "itens extras" vs total de códigos envolvidos) |

### Não se sustentou / contradiz a análise direta
| Item | Valor anterior | Valor da análise direta | O que aconteceu |
|---|---|---|---|
| Faturamento do recorte de 6 meses (01/05 a 31/10/2025) | R$ 732.186,81 | **R$ 1.377.269,74** | número impresso no próprio rodapé da Parte 1 do relatório, não bate com o valor citado antes |
| Faturamento do recorte de 2 meses (01/11 a 31/12/2025) | R$ 341.258,40 | **R$ 454.844,56** | número impresso no próprio rodapé da Parte 2, também não bate |
| Custo total de estoque | "aproximadamente R$ 550 mil" | **R$ 900.940,38** | soma direta da coluna "Custo Total" da planilha Estoque, valor bem mais alto |
| Potencial de venda do estoque atual | "mais de R$ 1 milhão" | **R$ 1.879.478,79** | soma direta da coluna "PV Total" da planilha |
| Suspeita de superfaturamento, 18 casos, R$ 754.497 | 18 casos confirmados, R$ 754.497 | não consegui reproduzir esse recorte específico | ver seção de auditoria abaixo, o método exato usado para chegar a "18 casos confirmados" não está documentado nos 5 arquivos que analisei, então não posso confirmar nem descartar esse número, só reproduzir o caso isolado citado (o colorante) com uma métrica diferente |
| Outliers de custo acima de 6x a mediana de pares | 134 outliers | 1.579 outliers | meu agrupamento de "produtos parecidos" foi por categoria + unidade de medida (o único par de colunas disponível na planilha), que é mais largo que o critério original (provavelmente por subcategoria/família de produto, que não está disponível de forma limpa nos arquivos que recebi); ver seção de auditoria |
| Estoque parado (+6 meses sem saída) | "não encontrado" | **1.682 itens, R$ 320.903,02 a custo (35,6% do custo total em estoque)** | agora dá para calcular, ver seção Estoque abaixo, com uma ressalva importante sobre o que a planilha realmente mede |

## Participação por categoria (14 meses)

Categoria = cadastro atual da coluna "Grupo" da planilha `Estoque ETL.xlsx`, cruzado por código de produto com o valor de venda de cada período da Curva ABC. Isso é uma foto atual do agrupamento (não peço para o sistema recalcular categoria retroativa por período), mas cobre os 14 meses inteiros de faturamento porque o cruzamento é feito por código, não por relatório.

| Categoria | Faturamento (14 meses) | % do total analisado | Margem bruta média |
|---|---|---|---|
| Material Básico (cimento, areia, tijolo, pedra, telha, aço) | R$ 1.285.654,45 | 42,21% | 35,88% |
| Hidráulica | R$ 307.641,55 | 10,10% | 46,06% |
| Pintura | R$ 256.518,19 | 8,42% | 36,37% |
| Impermeabilizantes | R$ 168.083,59 | 5,52% | 41,66% |
| Material Elétrico | R$ 164.016,83 | 5,38% | 31,73% |
| Ferramentas | R$ 157.405,62 | 5,17% | 46,20% |
| Ferragem | R$ 151.093,13 | 4,96% | 49,27% |
| Cobertura (telhas) | R$ 144.109,70 | 4,73% | 43,09% |
| Argamassas e Rejunte | R$ 131.297,65 | 4,31% | 38,82% |
| Metais | R$ 61.610,61 | 2,02% | 44,14% |
| Utilidades e Jardim | R$ 58.336,77 | 1,92% | 42,50% |
| Louças Sanitárias | R$ 24.170,55 | 0,79% | 38,13% |
| Cerâmica | R$ 22.059,63 | 0,72% | 37,95% |
| Esquadrias | R$ 17.046,59 | 0,56% | 42,02% |
| Categoria ilegível no cadastro ("MD-MD-MD-...") | R$ 13.961,81 | 0,46% | 48,69% |
| Demais categorias (iluminação, automotivo, refrigeração, piscina, armários etc.) | R$ 40.219,42 | 1,32% | variável |
| Sem código correspondente no cadastro de estoque | R$ 24.369,55 | 0,80% | não aplicável |

Material Básico, Hidráulica e Pintura somam 60,7% do faturamento em 14 meses. Vale notar: apesar de a categoria corrompida ("MD-MD-MD-...") atingir 34,5% da CONTAGEM de SKUs do catálogo, ela responde por só 0,46% do FATURAMENTO, porque a maior parte dos itens com essa corrupção de cadastro tem pouco ou nenhum movimento de venda (isso aparece de novo na seção de estoque parado abaixo). Isso não torna o problema de cadastro menos real, só limita o impacto financeiro imediato dele na leitura por categoria.

## Top produtos por giro (quantidade vendida, 14 meses)

| # | Produto | Categoria | Qtde. vendida | Margem % | Faturamento gerado |
|---|---|---|---|---|---|
| 1 | Tijolo C/8 Furos 09x19x19 | Material Básico | 282.430 un | 33,8% | R$ 272.677,10 |
| 2 | Telha Canal Tipo Russa 2ª | Cobertura | 22.085 un | 52,7% | R$ 28.785,27 |
| 3 | Parafuso Auto Broc Zinc 12x1 Jomarca | Ferragem | 13.027 un | 52,0% | R$ 6.016,20 |
| 4 | Telha Canal Tipo Russa 1ª | Cobertura | 11.089 un | 65,0% | R$ 15.890,24 |
| 5 | Bucha Nylon 08 Fixaforte | Ferragem | 4.133 un | 67,0% | R$ 1.036,61 |
| 6 | Cimento Montes Claros CPII F 32 ACPY 50kg | Material Básico | 3.700 sc | 14,4% | R$ 172.398,23 |
| 7 | Bucha Nylon 06 Fixaforte | Ferragem | 2.217 un | 60,0% | R$ 333,00 |
| 8 | Argamassa Cola Forte AC-II 15kg Polimassa | Argamassas e Rejunte | 2.099 un | 38,1% | R$ 49.977,21 |
| 9 | Telha Canal Tipo Carnaúba 1ª | Cobertura | 2.000 un | 24,2% | R$ 2.400,00 |
| 10 | Bucha Nylon 10 Fixaforte | Ferragem | 1.945 un | 62,0% | R$ 972,99 |
| 11 | Gesso Composto 1kg Itatiunga | Material Básico | 1.880 kg | 45,2% | R$ 4.701,93 |
| 12 | Bloco P/Laje 30x07x20 | Material Básico | 1.819 un | 52,9% | R$ 4.583,48 |
| 13 | Arruela Lisa Zinc 3/16 Jomarca | Ferragem | 1.779 un | 65,5% | R$ 282,59 |
| 14 | Parafuso PH CB Chata BC 4.0x20 Jomarca | Ferragem | 1.638 un | 75,2% | R$ 246,91 |
| 15 | Parafuso PH CB Chata BC 4.0x40 Jomarca | Ferragem | 1.553 un | 63,4% | R$ 310,79 |

Limitação encontrada: o cimento CP II Z 32 Cimpor e o cimento CP II F 40 Zebu aparecem cada um cadastrado em 4 códigos diferentes (provavelmente por lote de compra). Isso faz o giro de cada código individual aparecer menor do que o giro real do produto consolidado, então o ranking acima provavelmente subestima a posição desses dois cimentos frente ao Cimento Montes Claros, que está em um código só. Não corrigi isso automaticamente porque juntar códigos por nome de forma confiável em toda a base de 15 mil itens exigiria uma regra de normalização de nome que não tive como validar linha a linha no tempo disponível.

## Top produtos por margem bruta absoluta (R$, 14 meses)

| # | Produto | Categoria | Margem em R$ | Margem % | Faturamento |
|---|---|---|---|---|---|
| 1 | Tijolo C/8 Furos 09x19x19 | Material Básico | R$ 92.217,30 | 33,8% | R$ 272.677,10 |
| 2 | Areia Fina | Material Básico | R$ 52.338,76 | 27,8% | R$ 188.053,88 |
| 3 | Pedra Britada 1 (19) | Material Básico | R$ 38.612,86 | 53,4% | R$ 72.332,69 |
| 4 | Areia Média | Material Básico | R$ 27.861,36 | 46,5% | R$ 59.849,14 |
| 5 | Pedra Calcária | Material Básico | R$ 25.633,61 | 53,9% | R$ 47.545,00 |
| 6 | Pedra Britada 0 (Cascalhinho) | Material Básico | R$ 25.114,69 | 51,9% | R$ 48.367,61 |
| 7 | Cimento Montes Claros CPII F 32 ACPY 50kg | Material Básico | R$ 24.814,36 | 14,4% | R$ 172.398,23 |
| 8 | Areia Grossa Lavada | Material Básico | R$ 20.579,00 | 38,1% | R$ 54.034,98 |
| 9 | Argamassa Cola Forte AC-II 15kg Polimassa | Argamassas e Rejunte | R$ 19.062,50 | 38,1% | R$ 49.977,21 |
| 10 | Telha Canal Tipo Russa 2ª | Cobertura | R$ 15.166,12 | 52,7% | R$ 28.785,27 |
| 11 | Treliça Premoldada TG8 SL 6/3 x 4/4.2mm | Material Básico | R$ 14.014,10 | 54,3% | R$ 25.819,60 |
| 12 | Telha Brasilit Fibrotex 2.44x1.10x5mm | Cobertura | R$ 12.140,52 | 37,5% | R$ 32.380,00 |
| 13 | Cimento Poty CPII Z 32 Todas as Obras 50kg | Material Básico | R$ 11.251,11 | 22,7% | R$ 49.597,65 |
| 14 | Telha Canal Tipo Russa 1ª | Cobertura | R$ 10.328,38 | 65,0% | R$ 15.890,24 |
| 15 | Pilar de Ferro | Material Básico | R$ 10.245,24 | 49,7% | R$ 20.628,00 |

Material Básico domina os dois rankings (giro e margem absoluta), o que é esperado no nicho, mas concentra risco: se o preço de cimento/areia/pedra tiver qualquer distorção de cadastro (ver auditoria abaixo), o impacto financeiro é desproporcional ao resto do catálogo.

## Estoque

- **Custo total do estoque atual (soma da coluna "Custo Total" da planilha, todos os 15.228 códigos):** R$ 900.940,38
- **Potencial de venda do estoque atual pelo preço correto calculado (soma da coluna "PV Total"):** R$ 1.879.478,79
- **Itens do catálogo com saldo em estoque maior que zero:** 4.797 de 15.228 (os demais 10.431 códigos existem no cadastro mas estão com saldo zerado)

### Estoque parado (14 meses sem nenhuma venda registrada, com saldo em estoque positivo)

- **1.682 itens**, valendo **R$ 320.903,02 a custo**, o equivalente a **35,6% de todo o custo de estoque atual**
- Critério usado: código sem nenhuma unidade vendida em nenhum dos 4 relatórios de Curva ABC (ou seja, sem venda nos 14 meses completos, não só 6 meses) e com saldo em estoque maior que zero na planilha `Estoque ETL.xlsx`

Maiores casos por valor parado:
| Código | Produto | Qtde em estoque | Custo unitário | Valor parado | Categoria |
|---|---|---|---|---|---|
| 3746 | Vareta Solda Oxi 1.59mm Gerdau | 7.329 | R$ 10,20 | R$ 74.755,80 | categoria ilegível no cadastro |
| 14160 | Triciclo Tuka TK1200W | 1 | R$ 26.000,40 | R$ 26.000,40 | Ativo Imobilizado (não é mercadoria de revenda) |
| 11022 | Sacolas 30x40 Impressas | 2.005 | R$ 11,66 | R$ 23.378,30 | Material de Uso e Consumo |
| 11024 | Sacola Reciclada VD 60x80 | 1.015 | R$ 11,50 | R$ 11.672,50 | Material de Uso e Consumo |
| 3214 | Tubo PVC Rosca 1 Pol Tigre | 999,8 | R$ 8,06 | R$ 8.058,39 | categoria ilegível no cadastro |

Por categoria, o valor parado se concentra em: categoria ilegível no cadastro (R$ 101.355,45), Material de Uso e Consumo (R$ 55.520,24), Ativo Imobilizado (R$ 28.499,40, atenção: isso inclui bens como notebook e triciclo, não mercadoria de revenda, então esse valor não deveria entrar na leitura de "estoque parado para vender"), Pintura (R$ 23.265,94), Ferragem (R$ 23.083,11) e Ferramentas (R$ 18.899,63).

**Limitação importante:** a planilha `Estoque ETL.xlsx` não tem campo de "data da última venda". O campo de data que existe (coluna "Dt. Compra") é a data da última COMPRA do produto ao fornecedor, não da última venda ao cliente. O número de estoque parado acima não usa essa coluna de data, usa o cruzamento direto com a quantidade vendida de cada um dos 4 relatórios de Curva ABC (uma venda de 1 unidade sequer nos 14 meses já tira o item dessa lista). Isso é mais confiável do que usar a data de compra como proxy, mas ainda assim é um cálculo por ausência de venda no período coberto, não uma data exata de última movimentação.

## Auditoria de qualidade de dado (`Estoque ETL.xlsx`)

A própria planilha já vem com uma camada de ETL embutida (colunas calculadas: "Preço Correto", "Precificação" com checagem booleana de tolerância de R$ 2, "Custo Total", "PV Total"), sinal de que já houve trabalho de auditoria anterior sobre esse arquivo. Os achados abaixo repetem essa auditoria de forma independente, direto da planilha.

| Achado | Quantidade | Observação |
|---|---|---|
| Fornecedor cadastrado como a própria loja ("CONSTRUMAIS MATERIAL DE CONSTRUCAO") | 57 itens | confirmado, nome exato do fornecedor encontrado na planilha |
| Quantidade de estoque negativa | 17 itens | valor financeiro (qtde x custo) somado: negativo em R$ 139.191,14 |
| Preço de venda zerado com estoque ativo (saldo > 0) | 4 itens | valor de estoque nessas condições: R$ 856,64 a custo |
| Custo final zerado com venda ativa nos 14 meses | 1 item | código 1813, Borracha Siliconizada, vendeu 1 unidade no período com custo final cadastrado em zero |
| Margem acima de 1.000% | 27 itens | |
| Margem negativa | 199 itens | |
| Custo final menor que custo inicial | 104 itens | tecnicamente inconsistente: custo final deveria ser igual ou maior que o inicial (soma impostos e frete), nunca menor |
| Categoria/grupo corrompido (texto "MD-MD-MD-..." no lugar do nome da categoria) | 5.257 itens | 34,52% da base, confirmado como problema real no arquivo fonte (não é artefato de leitura de PDF, foi verificado direto na planilha Excel) |
| Produto com nome idêntico cadastrado em código diferente | 10 grupos, 24 códigos no total | inclui 2 casos de cimento (CP II Z 32 Cimpor em 4 códigos, CP II F 40 Zebu em 4 códigos), que também afeta o ranking de giro acima |
| Inconsistência entre preço cadastrado e o preço que custo+margem indicariam (coluna "Precificação" da própria planilha, tolerância de R$ 2) | 147 itens | achado adicional, não estava no diagnóstico anterior, vem de uma checagem que já existia dentro do próprio arquivo do cliente |

### Suspeita de superfaturamento (custo muito acima do esperado)

O diagnóstico anterior citava "18 casos confirmados, R$ 754.497 de sobrevalorização, maior caso um colorante a 1.075x o custo implícito" e "134 outliers acima de 6x a mediana de pares por um segundo método". Não encontrei, nos 5 arquivos analisados, a metodologia exata usada para chegar a esses dois números (não há um campo ou aba que marque "caso confirmado" nem o critério de corte usado para os 18 casos). Por isso, não posso confirmar nem descartar R$ 754.497 ou os 18 casos: não é possível calcular isso com o dado disponível, sem a metodologia original.

O que consigo confirmar de forma independente:

- **O caso do colorante existe e é localizável:** código 11073, "Colorante Icores BA Amarelo P0411 0.9L". A planilha tem Custo Inicial de R$ 131,13 e Custo Final (depois de impostos/frete) de R$ 0,16, uma queda de custo de cerca de 827 vezes entre as duas colunas, quando o normal é o custo final ser igual ou levemente maior que o inicial (nunca centenas de vezes menor). É quase certo que R$ 131,13 é um erro de cadastro nesse produto especificamente (decimal errado, ou custo de lote inteiro lançado como se fosse custo unitário). O número exato de "1.075x" citado antes não bateu com o meu cálculo de "827x", possivelmente por uma forma diferente de calcular "custo implícito", mas o produto e a direção do problema são os mesmos.
- **Rodando meu próprio método (mediana de custo por categoria + unidade de medida, o mesmo tipo de comparação "produtos parecidos" descrito antes), encontrei 1.579 códigos com custo final 6 vezes ou mais acima da mediana dos pares**, valendo cerca de R$ 113.173,52 de possível sobrevalorização de estoque (considerando só os itens com saldo positivo em estoque). Esse número é bem maior que os 134 citados antes porque meu agrupamento por "categoria + unidade de medida" é mais largo que um agrupamento por subcategoria ou família de produto (que existiria nas colunas "Sub. Grupo", "Linha" e "Família" dos relatórios de Curva ABC Partes 2 a 4, mas essas colunas vêm com quebra de linha e corrupção de texto que não deu para reconstruir com segurança linha a linha, ver nota de metodologia no topo). Isso quer dizer que uma fração relevante dos 1.579 é provavelmente falso positivo (produtos genuinamente mais caros dentro da mesma categoria ampla, não erro de cadastro).

Os 15 piores casos por essa métrica (para verificação manual, não tratar como confirmado sem checagem item a item):

| Código | Produto | Custo cadastrado | Mediana dos pares (mesma categoria+unidade) | Quantas vezes acima |
|---|---|---|---|---|
| 15657 | Sikasil-728 SL Charcoal Gray Tambor 270kg | R$ 31.537,94 | R$ 13,16 | 2.396x |
| 15990 | Motobomba Centrífuga ME-BR 24150 15T 60 4V SC | R$ 15.700,00 | R$ 11,92 | 1.317x |
| 14716 | Fechadura WC 513 Premium 55 Roseta Inox 308 L | R$ 2.384,00 | R$ 2,13 | 1.122x |
| 14888 | BAP Neo Push Dupla F H/V 1MT PT W4100D-HV-PT | R$ 905,48 | R$ 2,13 | 426x |
| 15365 | Nobreak 2000VA Biv SMS | R$ 2.985,60 | R$ 7,83 | 381x |
| 12112 | Bomba Submersa 2.1-TSR-19 1.1/2CV 220V | R$ 3.462,84 | R$ 12,55 | 276x |
| 12113 | Bomba Submersa 3.2-TSR-20 2.0CV 380V | R$ 3.132,32 | R$ 12,55 | 250x |

Nos três primeiros casos (Sikasil, Motobomba, Fechadura), a explicação mais provável não é fraude nem erro grosseiro, é que a mediana de comparação (produtos baratos tipo parafuso e arruela, que também são "Ferragem, unidade UN" ou "Impermeabilizantes, unidade UN") é baixa demais para servir de referência a um produto de nicho caro (tambor de selante industrial de 270kg, motobomba, fechadura premium). Recomendo tratar esses casos específicos como candidatos a falso positivo até checagem manual, e priorizar a checagem manual pelo caso do colorante (código 11073), que é o único onde a distorção de custo já foi confirmada por duas colunas da própria planilha (Custo Inicial x Custo Final), não por comparação externa.

## Produtos isca / âncora identificados

- **Tijolo C/8 Furos 09x19x19:** giro disparadamente o maior do catálogo (282.430 unidades em 14 meses, o segundo colocado vende 22.085), margem de 33,8%, a mais baixa entre os itens de giro alto que não são cimento. Âncora natural de tráfego de loja.
- **Cimento Montes Claros CPII F 32:** giro alto (3.700 sacos) com a pior margem entre os produtos de maior giro (14,4%), o caso mais claro de "isca" clássico do nicho (venda alta, margem mínima, produto que qualquer obra precisa comprar).
- **Cimento Poty CPII Z 32:** mesmo padrão do Cimento Montes Claros, margem de 22,7%, giro menor (1.112 sacos).

## Candidatos a kit (handoff para @copywriter, Pilar 3)

**Correção (2026-07-23):** a linha "Alvenaria" abaixo tinha um erro de domínio técnico identificado depois desta versão: Argamassa Cola Forte AC-II 15kg é argamassa colante para assentar piso/cerâmica (norma ABNT NBR 14081), não serve para assentar tijolo. O pareamento correto do Kit Alvenaria é Tijolo + Areia Fina (traço de cimento e areia), e a Argamassa AC-II vai para o Kit Revestimento, pareada com piso cerâmico. Ver a versão corrigida e expandida (10 kits por fase de obra) em `outputs/2026-07-estrategia-kits-e-vendas.md`, que substitui a tabela abaixo como referência de composição de kit. Margem combinada do kit Alvenaria recalculada abaixo com Areia Fina no lugar da AC-II.

Efeito de margem calculado diretamente a partir dos números confirmados acima (soma da margem em R$ dos produtos do kit dividida pela soma do faturamento dos mesmos produtos), não estimado.

| Kit | Composição | Margem isolada do âncora | Margem combinada do kit | Efeito |
|---|---|---|---|---|
| Alvenaria (composição corrigida) | Tijolo C/8 Furos + Areia Fina | 33,82% | 31,38% | -2,44 pontos percentuais (queda, não ganho) |
| Estrutura/Fundação | Cimento Montes Claros (âncora de giro, pior margem do top 15) + Gesso Composto 1kg + Bloco P/Laje 30x07x20 | 14,39% | 16,16% | +1,77 ponto percentual |
| Impermeabilização | Cimento Montes Claros (âncora) + Vedalit 900ml Vedacit (impermeabilizante de margem 41,58%) | 14,39% | 15,14% | +0,75 ponto percentual |
| Revestimento | Argamassa Cola Forte AC-II 15kg (âncora, pareamento correto) + Rejunte Flex Cinza Platina 1kg Polimassa (margem 40,48%) | 38,14% | 38,29% | +0,15 ponto percentual (ganho pequeno porque a argamassa já tem margem razoável sozinha) |
| Pintura | Tinta Pó C/10kg CH-1 Cal Megão (margem 34,46%) + Lixa Massa G120 A257 Norton (margem 66,79%) | 34,46% | 38,48% | +4,02 pontos percentuais (o kit com maior ganho de margem entre os cinco calculados) |

Não encontrei, nos 5 arquivos analisados, um produto de "cola/adesivo para tubo PVC" cadastrado com esse nome (o cruzamento sugerido pelo próprio cliente, joelho + tubo + cola, ver `CLIENTE.md`), então não montei esse kit com número de margem real. O `@copywriter` ou o cliente podem indicar o código exato desse produto no cadastro para eu completar esse kit depois.

**Nota sobre o Kit Alvenaria corrigido:** ao contrário dos outros quatro kits, o pareamento tecnicamente correto (Tijolo + Areia Fina) reduz a margem percentual combinada em vez de aumentar, porque a Areia Fina tem margem própria (27,8%) menor que o Tijolo (33,8%). Cálculo: margem R$ do Tijolo (R$ 92.217,30) mais margem R$ da Areia Fina (R$ 52.338,76), dividido pela soma do faturamento dos dois (R$ 272.677,10 + R$ 188.053,88 = R$ 460.730,98), resulta em 31,38%. Isso não invalida o kit como estratégia comercial (Tijolo e Areia Fina são comprados juntos na prática, para o mesmo traço de assentamento), só significa que o argumento de venda desse kit específico não é "aumenta a margem", e sim "é o par de produtos que a obra precisa comprar junto de qualquer forma, então captura ticket que já existe" (diferente do Kit Alvenaria com AC-II, que era tecnicamente errado mas coincidentemente mostrava ganho de margem).

## Próximos passos

1. Resolver a auditoria de cadastro antes de qualquer decisão de precificação ou kit se apoiar em margem por categoria: prioridade para os 104 casos de custo final menor que custo inicial e para os 5.257 itens de categoria corrompida (mesmo respondendo por só 0,46% do faturamento, atrapalham qualquer relatório futuro por categoria).
2. Verificar manualmente o caso do colorante (código 11073) e os 7 outliers extremos listados na seção de superfaturamento, idealmente com o Tony confirmando se o custo inicial de R$ 131,13 é erro de digitação ou tem alguma explicação (lote, câmbio, unidade de compra diferente da unidade de venda).
3. Reportar ao Tony a divergência encontrada nos números de faturamento por recorte de 6 e 2 meses (R$ 732.186,81 e R$ 341.258,40 citados antes, contra R$ 1.377.269,74 e R$ 454.844,56 confirmados agora direto do rodapé dos relatórios), para entender se a fonte anterior usava outro filtro (ex: só uma categoria, ou só uma classe da Curva ABC) e evitar retrabalho de quem usar o número errado.
4. `@analista-dados` pode usar o estoque parado (R$ 320.903,02, 1.682 itens) e o giro/margem por categoria como KPI de dashboard quando o cliente autorizar acompanhamento contínuo.
5. `@copywriter` pode usar os 5 kits calculados (Alvenaria, Estrutura/Fundação, Impermeabilização, Revestimento, Pintura) para copy de oferta do Pilar 3, lembrando que Pilar 3 não é item formal do Anexo I com a Construmais hoje (ver `CLIENTE.md`, seção Contrato com a Pillar; o trabalho em si já é entregue, só a formalização contratual como upsell depende do Tony), confirmar com o cliente antes de produzir peça paga em mídia.
6. Pedir ao Tony (ou ao suporte da Pontual Tecnologia) um campo de "data da última venda" por produto, se existir no sistema mas não sair nesse formato de exportação, para no futuro calcular estoque parado por tempo real sem depender de cruzar 4 relatórios de período fechado.
7. Confirmar com o cliente o código do produto usado como cola/adesivo para tubo PVC, para completar o kit sugerido por ele mesmo (joelho + tubo + cola) com número de margem real.
