# Validação de Margem do Programa de Parceria com Profissionais: Construmais

**Briefing usado:** pedido do plano `outputs/09-2026/Analises/11-plano-obra-integral-plano-estrategico-parceria-profissionais.md` (seções 1, 3.3, 4.1 e 6), diagnóstico cumulativo `outputs/_diagnosticos/inteligencia-dados/diagnostico-estoque.md` (4 períodos de Curva ABC, mai/2025 a jun/2026, e snapshot de estoque de 03/08/2026), `CLIENTE.md` (margem agregada 39,27%, ticket médio até R$ 300, contrato Pilar 1 no Anexo I). Atividade do método: Pilar 1, Inteligência de Dados, dando suporte à Atividade 5.4 do Pilar 5.

**Status:** v1, sujeito a refinamento. Nenhum percentual aqui é recomendação fechada, é insumo para o Tony decidir (ver seção 6 do plano de parceria).

---

## Tarefa 1: cruzamento de compradores recorrentes por ofício

### Resultado: bloqueada

Conferi a estrutura completa dos 6 arquivos de ERP disponíveis no repositório do cliente antes de concluir:

| Arquivo | Abas | Colunas |
|---|---|---|
| `07-2026/Arquivos/25-inteligencia-dados-curva-abc-padronizada_*.xlsx` (4 arquivos, um por período) | 1 aba única, "Curva ABC padronizada" | `codigo, produto, grupo_abc, unidade, qtd_atual, qtd_vendida, custo_unit, custo_total, preco_venda_medio, venda_total, margem_bruta_pct` |
| `08-2026/Arquivos/03-inteligencia-dados-estoque-auditado_2026-08-03.xlsx` | Estoque padronizado, Estoque parado (ajustado), Outliers críticos | `codigo, produto, fabricante, unid_estoque, qtde, custo_inicial, custo_final, pct_margem, preco, categoria_mapeada, existe_no_historico, qtd_vendida_historico, flag_estoque_parado, flag_outlier_critico, valor_custo` |
| `08-2026/Arquivos/26-inteligencia-dados-giro-estoque-por-bucket_2026-08-03.xlsx` | Ranking por valor de estoque, Resumo por bucket, Ativo imobilizado, Outliers críticos | `codigo, produto, categoria, fornecedor, qtde, custo_unit_usado, valor_estoque_ajustado, preco, margem_cadastrada_pct, bucket_giro, dias_sem_venda_minimo, ultimo_periodo_com_venda, notas` |

Confirmo: **nenhum dos 6 arquivos tem granularidade de cliente.** Todos são vendas ou estoque agregados por SKU (produto), não por comprador. Não existe coluna de CPF/CNPJ, nome de cliente, número de cupom/nota ou data de venda individual em nenhuma das 9 abas conferidas. Isso bate com o que o `CLIENTE.md` já registra (Pilar 1: "sistema Pontual Tecnologia... dados de cliente cadastrados: nome, celular, e-mail, endereço, CPF", mas os relatórios que a Pillar recebeu até agora não trazem esse campo cruzado com a venda).

Não tenho como montar a lista nominal de profissionais recorrentes por ofício nem a distribuição de volume que define o corte do Nível Ouro (seções 3.3 e 4.1 do plano) sem um relatório novo. Não vou aproximar isso com os dados de SKU que tenho (não dá para inferir "quem comprou" a partir de "o que vendeu no agregado"), conforme Regra 9 de `_shared/regras-globais.md`.

### O que pedir ao Tony (relatório do Pontual Tecnologia)

Pedir ao Tony (ou diretamente ao suporte Pontual) uma exportação de **vendas por cliente**, período de 12 meses (para cobrir sazonalidade de obra), com as colunas mínimas:

| Coluna | Por quê |
|---|---|
| CPF ou CNPJ do cliente | Identificador único de comprador, chave para calcular recorrência |
| Nome do cliente | Para a lista nominal pedida no plano |
| Telefone/WhatsApp cadastrado | Para o cadastro do programa (Fase 0 do plano) |
| Data da venda | Para calcular frequência de compra e volume trimestral |
| Número do cupom/nota fiscal | Para agrupar itens da mesma compra (mix por cupom) |
| Código do SKU | Para cruzar com a categorização já usada nos diagnósticos de Curva ABC |
| Quantidade vendida | Para o cálculo de volume |
| Valor unitário e valor total do item | Para o cálculo de faturamento por cliente |
| Categoria/grupo do produto (se disponível no cadastro) | Para o mix por categoria (ex: quanto de Material Básico um comprador leva) |

Com esse relatório dá para calcular, por CPF: frequência de compra no período, valor total comprado, mix por categoria (indício de ofício: quem compra sobretudo Material Básico tende a ser pedreiro/mestre de obra, quem compra Pintura tende a ser pintor, etc., mas o ofício em si só fica confirmado com cadastro manual no balcão, que já está previsto na Fase 0 do plano), e a distribuição de volume trimestral que embasa o corte do Nível Ouro pedido em 3.3.

Enquanto esse relatório não chega, a Fase 0 do plano ("cruzar no ERP quem já é comprador recorrente... sair com lista nominal por ofício") não tem como ser cumprida pelo `@inteligencia-dados`. A alternativa operacional que o próprio plano já prevê (seção 4.2, Fase 1) é o cadastro manual no balcão pelos 2 vendedores, que não depende deste relatório e pode começar em paralelo.

---

## Tarefa 2: validação de margem do benefício proposto

### Fonte e critério de qualidade do dado

Usei as 4 planilhas de Curva ABC padronizada (mai/2025 a jun/2026, 14 meses), a mesma fonte do diagnóstico cumulativo. Segui o diagnóstico para descartar linhas com custo comprovadamente errado (limitação 2 do período mai-out/2025) e encontrei **mais um caso não documentado antes**, tratado com a mesma metodologia de benchmark contra os outros períodos (princípio 3 do SKILL de Inteligência de Dados).

### 2.0. Linhas descartadas e por quê

| Item | Período descartado | Motivo |
|---|---|---|
| Cimento Montes Claros | mai-out/2025 | Limitação 2 já documentada no diagnóstico cumulativo: margem bruta cadastrada de -2,01% neste período contra 22,0% a 22,8% nos outros 3. Erro de custo confirmado, não reflete a realidade. |
| Areia fina | mai-out/2025 | Mesma limitação 2: margem -0,84% neste período contra 50,9% a 52,6% nos outros 3. |
| Cabo flex 2,5mm (PT PC Megatron, código 1320, usado como representativo da linha) | mai-out/2025 | Mesma limitação 2: margem -1.285,65% neste período contra 37,5% a 47,1% nos outros 3. |
| **Tijolo c/8 furos (código 48)** | **jan-mar/2026** | **Achado novo desta análise, fora da limitação 2 do diagnóstico cumulativo.** Custo unitário cai para R$ 0,43 nesse período, 38% abaixo da média dos outros 3 (R$ 0,69 a R$ 0,75), com o preço de venda estável (R$ 0,97), gerando margem de 55,66%, destoante do padrão de 25% a 30% do resto do histórico. Mesmo padrão de erro de custo cadastrado já visto em dezenas de outros SKUs na auditoria de estoque de 03/08/2026. Recomendo reportar ao Tony junto com os demais achados de cadastro pendentes. |

Todos os consolidados abaixo usam só os períodos não descartados de cada item (3 de 4 para os 4 casos acima, 4 de 4 para os demais).

### 2.a. Margem bruta % por SKU, por período e consolidada

Consolidado = margem bruta em R$ somada dos períodos válidos, dividida pela venda total somada dos mesmos períodos (média ponderada por venda, não média simples dos percentuais).

| Item | mai-out/25 | nov-dez/25 | jan-mar/26 | abr-jun/26 | **Consolidado (períodos válidos)** |
|---|---|---|---|---|---|
| Cimento Montes Claros | ~~-2,01%~~ descartado | 22,02% | 22,80% | 22,39% | **22,48%** |
| Cimento Poty | 24,65% | 18,21% | 21,05% | 21,74% | **22,68%** |
| Tijolo c/8 furos | 27,68% | 30,02% | ~~55,66%~~ descartado | 25,02% | **27,61%** |
| Areia fina | ~~-0,84%~~ descartado | 50,93% | 51,50% | 52,61% | **51,75%** |
| Areia média | 45,70% | 45,89% | 47,80% | 47,05% | **46,55%** |
| Areia grossa lavada | 28,82% | 48,51% | 38,90% | 54,63% | **38,08%** |
| Pedra britada 0 (cascalhinho) | 49,53% | 58,34% | 53,23% | 51,39% | **51,92%** |
| Pedra britada 1 (19) | 52,03% | 58,55% | 54,49% | 52,63% | **53,38%** |
| Pedra calcária | 54,81% | 55,55% | 55,98% | 48,89% | **53,91%** |
| Tubo PVC Esg 200mm (Corplastik/Krona) | 46,04% / 38,90% | sem venda | sem venda | sem venda | Só vendeu no 1º período (ver nota abaixo) |
| Joelho 45 PVC Esg 200mm (3 marcas) | 54,38% a 75,75% | sem venda | sem venda | sem venda | Só vendeu no 1º período |
| Luva PVC Esg 200mm (3 marcas) | 42,37% a 63,94% | sem venda | sem venda | sem venda | Só vendeu no 1º período |
| Cabo flex 2,5mm (representativo, cód. 1320) | ~~-1.285,65%~~ descartado | 39,00%* | 37,49% | 47,09% | **40,37%** |
| Bloco p/Laje 30x07x20 | 54,56% | 54,08% | 54,63% | 41,60% | **52,91%** |
| Telha Canal Russa 1ª | 65,71% | 90,70% | 93,05% | 50,21% | **64,99%** |
| Telha Canal Russa 2ª | 74,79% | 32,88% | 66,81% | 33,57% | **52,69%** |
| Argamassa Cola Forte AC-II 15kg | 38,49% | 36,66% | 39,01% | 34,50% | **38,14%** |

\* nov-dez/25 teve só 1 unidade vendida do código 1320 (venda R$ 3,00), volume baixo demais para confiar isoladamente, mas dentro da faixa dos outros períodos.

Nota sobre a linha PVC 200mm: os 3 grupos (tubo, joelho, luva) só tiveram venda registrada no período mai-out/2025 (6 meses); nos 3 períodos seguintes (8 meses) ficaram no Grupo Z, sem nenhuma saída. É giro muito baixo e esporádico, não confirmado ainda com o Tony (diferente do caso do "Tubo PVC Rosca 1 pol", já confirmado como baixo giro em 26/08/2026). Vale reportar como pendência de confirmação.

Não localizei um item chamado exatamente **"Massa PVA"** no catálogo. Os candidatos mais próximos são "Massa Corrida BD" (várias marcas, revestimento à base de PVA, margem entre 31,8% e 39,6% nos exemplos do período mai-out/2025) e "Cola Branca PVA Itafix" (adesivo, não revestimento, margem 45,5% a 46,2%). Não assumi qual dos dois o plano tinha em mente. Fica como pergunta ao Tony antes de incluir esse item na régua de agregados.

### 2.b. Simulação do custo do crédito, cesta de obra de alvenaria

**Como cheguei na cesta:** não consigo derivar a proporção de compra de um profissional individual (Tarefa 1 bloqueada). Usei a proporção agregada real de venda da loja no trimestre mais recente (abr-jun/2026): a cada 1 saco de cimento vendido (Montes Claros + Poty somados), a loja vende em média 34,48 tijolos, 0,3177 m³ de areia (fina+média+grossa somadas) e 0,0931 m³ de brita (0+1 somadas). É dado real dos relatórios, mas é a mistura de todos os compradores do trimestre (consumidor final e profissional juntos), não comprovadamente o padrão de compra de um profissional específico. Escalei para uma base de 20 sacos de cimento, o mesmo tamanho de referência já usado no plano (seção 1), usando cimento Montes Claros, tijolo, areia fina (o par que o `CLIENTE.md` já valida como composição correta do Kit Alvenaria) e brita 1, com preço e custo do período mais recente (abr-jun/2026):

| Item | Qtd. | Preço unit. | Custo unit. | Venda (R$) | Custo (R$) | Margem (R$) | Margem % |
|---|---|---|---|---|---|---|---|
| Cimento Montes Claros | 20 sc | R$ 51,42 | R$ 39,91 | 1.028,40 | 798,20 | 230,20 | 22,38% |
| Tijolo c/8 furos | 690 un | R$ 1,00 | R$ 0,75 | 689,67 | 517,25 | 172,42 | 25,00% |
| Areia fina | 6,35 m³ | R$ 154,29 | R$ 73,11 | 980,39 | 464,55 | 515,83 | 52,62% |
| Pedra britada 1 | 1,86 m³ | R$ 257,33 | R$ 121,89 | 479,10 | 226,94 | 252,16 | 52,63% |
| **Total da cesta** | | | | **3.177,55** | **2.006,94** | **1.170,61** | **36,84%** |

A margem da cesta (36,84%) fica abaixo da margem agregada da loja inteira (39,27%), porque cimento e tijolo, os dois itens de menor margem, pesam mais em volume de venda nessa cesta do que no mix completo da loja.

**Custo do crédito de 2% e 3%, resgatado em item de margem alta (não em cimento/tijolo):**

O crédito não é descontado em dinheiro, é resgatado em produto. O custo real para a loja é o custo do item resgatado, não o valor de face do crédito. Usando areia fina como item de resgate (agregado permitido pela régua da seção 3.3 do plano, custo/preço = 47,38% no período mais recente):

| Crédito sobre a cesta | Valor de face | Custo real do crédito para a loja (resgatado em areia fina) | Margem líquida da cesta (R$) | Margem líquida (% sobre a venda da cesta) |
|---|---|---|---|---|
| 2% | R$ 63,55 | R$ 30,11 | R$ 1.140,50 | 35,89% |
| 3% | R$ 95,33 | R$ 45,17 | R$ 1.125,44 | 35,42% |

A conta: crédito de 2% sobre R$ 3.177,55 = R$ 63,55 de face. Se a loja pagasse isso em dinheiro, custaria R$ 63,55. Como é resgatado em areia fina (que custa à loja 47,38% do que ela vende), o custo real cai para R$ 63,55 × 0,4738 = R$ 30,11, menos da metade do valor de face. O mesmo raciocínio vale para 3%: R$ 95,33 de face custam R$ 45,17 de fato.

Em ambos os cenários, a margem líquida da cesta (35,89% e 35,42%) continua acima de 30% mesmo depois do crédito, e a diferença de custo entre 2% e 3% é de só R$ 15,06 por cesta desse tamanho (R$ 30,11 vs R$ 45,17).

### 2.c. Margem residual da tabela de preço profissional, descontos de 3%, 5% e 8%

Base: preço e custo do período mais recente (abr-jun/2026), sem crédito, é desconto direto no preço de tabela.

| Item | Margem atual | -3% | -5% | -8% |
|---|---|---|---|---|
| Cimento Montes Claros | 22,38% | 19,98% | 18,30% | **15,64%** |
| Cimento Poty | 21,74% | 19,32% | 17,62% | **14,94%** |
| Tijolo c/8 furos | 25,00% | 22,68% | 21,05% | 18,48% |
| Areia fina | 52,62% | 51,15% | 50,12% | 48,49% |
| Pedra britada 1 | 52,63% | 51,17% | 50,14% | 48,51% |
| Pedra britada 0 | 51,39% | 49,89% | 48,84% | 47,17% |

Nenhum dos 6 itens fica com margem negativa nos 3 cenários testados (-3%, -5%, -8%), mas o cimento é o único grupo que cruza o piso de 15% da pergunta: **Cimento Poty fica abaixo de 15% (14,94%) a -8% de desconto**, e Cimento Montes Claros fica bem perto do piso (15,64%) no mesmo cenário. Já a -5%, os dois cimentos ficam entre 17,6% e 18,3%, ainda com alguma folga. O tijolo nunca cai abaixo de 18% nos cenários testados. Os agregados (areia, brita) seguem confortáveis nos 3 cenários, sempre acima de 47%, porque a margem % deles é alta o bastante para absorver um desconto de preço de tabela sem comprometer a operação.

### 2.d. Conclusão objetiva

- **Cimento (Montes Claros e Poty) é o item que menos suporta desconto direto de tabela.** Com margem atual de 21,7% a 22,4%, um desconto de -8% no preço de tabela profissional já derruba a margem para a faixa de 15%, no limite ou abaixo do piso de referência usado nesta análise. -5% ainda deixa alguma folga (17,6% a 18,3%).
- **Tijolo tem folga um pouco maior** (25% de margem atual), suporta -8% sem cruzar 15%, mas ainda assim é o segundo item mais sensível.
- **Areia e brita suportam desconto direto com folga confortável** nos 3 cenários testados (sempre acima de 47%), inclusive a -8%, porque partem de margem bruta na faixa de 51% a 55%.
- **Sobre o crédito de 2% versus 3% (Nível Ouro):** os dois ficam abaixo da margem agregada da loja (39,27%) mesmo depois de descontado o custo real do crédito, porque o benefício é resgatado em item de margem alta, não em dinheiro. A diferença de custo entre as duas faixas é pequena em termos absolutos (cerca de R$ 15 a mais por cada R$ 3.177,55 de cesta comprada no crédito de 3% frente ao de 2%), mas em escala (aplicado a todo o volume trimestral de profissionais cadastrados) essa diferença cresce proporcionalmente. Com a informação disponível hoje, **2% parece a faixa com mais folga** por ficar mais perto do meio da margem agregada da loja depois do desconto, mas **3% também não compromete a margem da cesta simulada** (fica em 35,42% líquido, ainda saudável). A decisão final do percentual, como o próprio plano registra na seção 6, é do Tony.

---

## Próximos passos

1. **Tarefa 1 (bloqueada):** pedir ao Tony (ou diretamente ao suporte Pontual Tecnologia) o relatório de vendas por cliente, 12 meses, com as colunas listadas na seção da Tarefa 1. Sem isso, a lista nominal por ofício e o corte de volume do Nível Ouro não têm como ser calculados a partir do ERP.
2. **Enquanto isso, o cadastro manual do balcão (Fase 0 e 1 do plano) pode seguir em paralelo**, sem depender deste relatório.
3. **Reportar ao Tony o novo achado de custo cadastrado no Tijolo c/8 furos em jan-mar/2026** (seção 2.0), junto com os demais achados de cadastro já pendentes no diagnóstico cumulativo.
4. **Confirmar com o Tony o que é "Massa PVA"** no plano (Massa Corrida BD ou Cola Branca PVA), antes de incluir esse item na régua de agregados resgatáveis.
5. **Confirmar com o Tony se a linha PVC 200mm (tubo/joelho/luva) é giro baixo esperado** (mesmo padrão já confirmado para outros itens hidráulicos) ou se há problema de cadastro/ruptura, já que não vendeu nada nos últimos 8 meses de histórico.
6. Levar as tabelas de 2.a a 2.d para a decisão do Tony na seção 3.8 do plano (itens 1 e 2: tabela de preço profissional e percentual de crédito trimestral).
7. Quando o relatório de vendas por cliente existir, repetir a Tarefa 1 e cruzar com os achados desta Tarefa 2 para validar se o mix de compra dos profissionais reais bate com a proporção agregada usada na cesta ilustrativa da seção 2.b.

**Planilha de apoio:** `outputs/09-2026/Arquivos/11-inteligencia-dados-validacao-margem-parceria.xlsx` (abas: Margem por SKU e período, Consolidado por item, Linhas descartadas, Cesta alvenaria e crédito, Simulação crédito 2-3%, Tabela preço profissional).

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
