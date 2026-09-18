# Diagnóstico de Giro de Estoque e Margem para Hora Z
**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra, atividade "Giro de Estoque e Margem"
**Como ler este arquivo:** histórico cumulativo, uma seção por período/snapshot coberto por relatório de estoque do cliente, do mais recente (topo) para o mais antigo (final), independente da ordem em que os relatórios foram processados.

## Visão geral acumulada

| Período/snapshot | Estoque parado corrigido | Giro médio (mediana) | Quadrante predominante |
|---|---|---|---|
| Snapshot 15/09/2026 | R$ 6.293,29 (148 SKUs, proxy por ausência de venda) | 4 unidades (mediana, 295 SKUs cruzados) | Estrela (85 de 295 SKUs cruzados) |

Primeira rodada, sem snapshot anterior para comparar evolução de estoque parado ou mudança de quadrante.

**Correção em 18/09/2026:** o cliente apontou que o `diagnostico-curva-abc.md` estava tratando classificação por quantidade como Curva ABC, erro de metodologia (Curva ABC classifica por faturamento). Essa correção não muda a matriz giro x margem nem o proxy de estoque parado deste arquivo, que já usavam giro em quantidade de forma correta e rotulada como tal. O que foi revisado aqui: valor em estoque por produto (agora com visão sem outliers de cadastro), maiores quantidades em estoque (seção nova) e estoque parado (agora ordenado por antiguidade da última compra, não por valor). Ver seção de período abaixo para o detalhe.

**Segunda correção em 18/09/2026:** o cliente viu a correção anterior (custo da compra mais recente escolhido como proxy único para os 86 SKUs com mais de um fornecedor) e pediu mudança de estrutura, não mais uma nota de rodapé. A partir desta rodada nenhuma tabela deste arquivo escolhe um custo vencedor para esses 86 SKUs: quantidade, categoria e produto continuam agrupados por código, isso já estava certo. Custo e margem passam a aparecer lado a lado (cenário de custo mínimo e cenário de custo máximo já pagos) nas quatro tabelas em que a margem ou o valor a custo pesa na leitura: valor em estoque por produto, estoque por categoria, estoque parado e matriz giro x margem. Detalhe de cada tabela na seção de período abaixo.

---

## Período/Snapshot: 15/09/2026 (snapshot único de estoque)
**Fonte dos dados:** `Estoque.xlsx`, aba "Produtos por Fornecedor", recebido do cliente em 15/09/2026, processado em 09-2026. Cruzado com `Curva_Abc.xlsx` (mesma data de recebimento) para leitura de giro.
**Planilha(s):** `09-2026/Arquivos/15-inteligencia-dados-estoque-giro-margem_snapshot-2026-09-15.xlsx` (atualizada em 18/09/2026 com abas novas: "Estoque por categoria (bruto e s outliers)", "Top produtos valor estoque" e "Maiores quantidades em estoque"; aba "Estoque parado" reordenada por antiguidade da última compra; segunda atualização no mesmo dia: abas "Top produtos valor estoque", "Matriz giro x margem", "Estoque parado" e "Estoque por categoria (bruto e s outliers)" ganharam colunas de custo/margem mínimo e máximo para os SKUs com mais de um fornecedor, sem custo único escolhido)
**Status:** v1, sujeito a refinamento

### Resumo executivo

- Valor total em estoque a custo: R$ 40.661,03, em 443 SKUs únicos.
- O relatório de estoque não declara data de corte explícita. Usei a data de hoje (15/09/2026) como data do snapshot, conforme instrução do cliente.
- **Limitação principal desta rodada: não há data de última venda por SKU em nenhum dos dois relatórios recebidos**, só data de última compra (quando fornecedor comprou o produto, não quando o cliente final comprou). Isso impede aplicar a definição padrão de estoque parado ("sem saída há 6 ou mais meses"). Na falta dela, usei um proxy: SKU que está no snapshot de estoque e não aparece em nenhuma linha da Curva ABC recebida (que cobre um acumulado, período não declarado, ver `diagnostico-curva-abc.md`). Isso aproxima "sem venda no período coberto", não "sem venda há X meses". Recomendo pedir ao ERP um relatório com data de última venda por SKU pra refinar isso na próxima rodada.
- O relatório de estoque original ("Produtos por Fornecedor") lista 544 linhas para 443 SKUs únicos: 86 códigos aparecem em mais de uma linha (101 linhas extras ao todo, um código com até 5 linhas) porque já foram comprados de mais de um fornecedor ao longo do tempo. Estoque disponível e preço de venda são idênticos entre as linhas duplicadas do mesmo código (confirmado: nenhum dos 86 tem estoque disponível diferente entre as linhas, a quantidade física não está duplicada), só custo, fornecedor e data de compra variam. Quantidade, categoria e descrição continuam agrupadas por produto, 1 linha por código, isso não muda nesta rodada.
- **Mudança de estrutura pedida pelo cliente em 18/09/2026, depois de ver a rodada anterior (custo da compra mais recente escolhido como proxy único para os 86 códigos com mais de um fornecedor): a partir de agora não escolho mais um custo vencedor para esses 86 códigos.** Nas quatro tabelas em que custo ou margem influencia o número final (valor em estoque por produto, estoque por categoria, estoque parado e matriz giro x margem), esses 86 códigos ganharam o custo mínimo e o custo máximo já pagos lado a lado, no lugar de uma escolha única. Exemplo: Cimento Supremo 50kg (código PRD00045) tem 95 unidades nas duas linhas, custo de R$ 36,90 (Becker, 11/06/2026) e R$ 33,00 (Agremix, 09/09/2026). A tabela de valor em estoque agora mostra R$ 3.135,00 (cenário R$ 33,00) e R$ 3.505,50 (cenário R$ 36,90) lado a lado, sem escolher qual vale para a reunião. Na matriz giro x margem, onde não cabia duplicar todas as colunas, a tabela ganhou uma coluna de margem mínima, uma de margem máxima e um sinalizador de quando o quadrante (Estrela, Isca, Reserva de lucro, Candidato a liquidar) muda dependendo do custo confirmado, ver seção própria abaixo. Os 86 códigos somam R$ 11.694,48 de valor em estoque pelo custo mais recente (28,8% do valor bruto total, R$ 40.661,03), variando entre R$ 10.505,96 (se todos usassem o custo mínimo já pago) e R$ 16.658,94 (se todos usassem o máximo), diferença de R$ 6.152,98, a mesma faixa já levantada na rodada anterior. Dois desses 86 códigos (Cabo de aço plastificado 3/32", código 4436, e Desempenadeira lisa CB plástico, código 22922) também estão na auditoria de outliers de cadastro abaixo: além do custo variar entre fornecedores, a compra mais recente de cada um tem custo maior que o preço de venda, um problema em cima do outro. Lista completa dos 86 códigos com custo mínimo, máximo e o mais recente segue na aba "Sensibilidade custo fornecedor" da planilha, sem mudança nesta rodada.
- 148 dos 443 SKUs do estoque atual (33%) não têm nenhuma venda registrada na Curva ABC recebida, valor financeiro parado a custo de R$ 6.293,29 (15,5% do valor total em estoque). Destes, 8 SKUs (5,4%) não têm data de última compra preenchida no relatório, ficam sem posição de antiguidade na régua de estoque parado abaixo.
- Auditoria de cadastro encontrou 49 SKUs com valor de custo fora do padrão: 33 com custo zerado e 16 com custo cadastrado acima do próprio preço de venda (prejuízo no cadastro, não necessariamente prejuízo real na venda). Detalhe na seção própria abaixo.
- **Correção em 18/09/2026, apontada pelo cliente:** o "top valor em estoque" da rodada anterior não isolava os itens com outlier de cadastro, então o ranking bruto ficava inflado por 2 itens com custo claramente errado (bucha plástica c/ anel concreto 8mm, código 22483, e estribo Flexfer, código PRD00016). Adicionei a visão "sem outliers" logo abaixo, mesmo tratamento já dado ao faturamento com os lançamentos "Plataforma" no outro diagnóstico.

### Giro por SKU/categoria

Categorização do estoque pelo mesmo critério de palavra-chave usado na Curva ABC (ver `diagnostico-curva-abc.md`), aplicada de forma independente sobre a descrição de cada SKU do relatório de estoque:

| Categoria | SKUs em estoque | Valor em estoque a custo |
|---|---|---|
| Básico | 82 | R$ 20.890,00 |
| Hidráulica | 105 | R$ 6.158,68 |
| Ferramentas | 81 | R$ 3.570,11 |
| Não classificado | 67 | R$ 2.990,60 |
| Pintura | 40 | R$ 2.886,51 |
| Elétrica | 29 | R$ 1.782,90 |
| Acabamento | 20 | R$ 1.604,65 |
| EPI/segurança | 18 | R$ 761,91 |
| Bazar/diversos | 1 | R$ 15,66 |

Básico concentra mais da metade do valor em estoque a custo (51,4% dos R$ 40.661,03), coerente com o achado da Curva ABC: cimento, tijolo, bloco e ferro puxam tanto o giro quanto o capital parado em estoque. 67 dos 443 SKUs do estoque (15%) ficaram sem categoria reconhecida pelo critério de palavra-chave, em geral por nome abreviado ou peça de fixação genérica (parafuso, arruela sem contexto). Detalhe SKU a SKU na aba "Estoque categorizado" da planilha, coluna "Categoria (inferida)" combinada com "Valor em estoque a custo".

**Valor em estoque por categoria, bruto x sem outliers de cadastro (novo em 18/09/2026):** o valor bruto acima inclui 16 SKUs com outlier de cadastro (custo cadastrado acima do preço de venda, ver "Auditoria de qualidade do cadastro" abaixo), que inflam principalmente a categoria Básico. Aba "Estoque por categoria (bruto e s outliers)" da planilha.

| Categoria | Valor bruto | SKUs (sem outliers) | Valor sem outliers |
|---|---|---|---|
| Básico | R$ 20.890,00 | 74 | R$ 10.934,68 |
| Hidráulica | R$ 6.158,68 | 104 | R$ 6.140,38 |
| Ferramentas | R$ 3.570,11 | 78 | R$ 2.807,96 |
| Não classificado | R$ 2.990,60 | 67 | R$ 2.990,60 |
| Pintura | R$ 2.886,51 | 38 | R$ 1.578,53 |
| Elétrica | R$ 1.782,90 | 28 | R$ 1.640,40 |
| Acabamento | R$ 1.604,65 | 19 | R$ 1.604,65 |
| EPI/segurança | R$ 761,91 | 18 | R$ 761,91 |
| Bazar/diversos | R$ 15,66 | 1 | R$ 15,66 |
| **Total** | **R$ 40.661,03** | **427** | **R$ 28.474,77** |

Básico perde quase metade do valor bruto (de R$ 20.890 para R$ 10.934,68) só por causa de 4 itens com custo mal cadastrado. Essa é a leitura que uso pra falar de capital parado por categoria daqui pra frente, o valor bruto por categoria fica documentado mas não é a base de decisão.

**Sensibilidade de custo por múltiplos fornecedores, por categoria (novo em 18/09/2026):** os 86 códigos com mais de um fornecedor se espalham por 8 das 9 categorias de estoque (só Bazar/diversos, categoria de 1 SKU só, fica de fora). A tabela usa custo mínimo e máximo já pagos só desses 86 códigos, o resto da categoria continua pelo custo mais recente já mostrado acima. Aba "Estoque por categoria (bruto e s outliers)" da planilha, colunas F a H.

| Categoria | SKUs c/ múltiplos fornecedores | Valor desses SKUs (custo mín.) | Valor desses SKUs (custo máx.) |
|---|---|---|---|
| Básico | 20 | R$ 7.465,94 | R$ 10.667,13 |
| Hidráulica | 28 | R$ 1.576,11 | R$ 2.211,68 |
| Ferramentas | 10 | R$ 204,19 | R$ 1.963,75 |
| Não classificado | 10 | R$ 367,72 | R$ 520,52 |
| Pintura | 9 | R$ 378,97 | R$ 568,73 |
| EPI/segurança | 3 | R$ 52,74 | R$ 159,75 |
| Acabamento | 3 | R$ 390,43 | R$ 452,27 |
| Elétrica | 3 | R$ 69,86 | R$ 115,10 |

Básico concentra a maior parte da ambiguidade em valor absoluto (R$ 3.201,18 de diferença entre os dois cenários), mas Ferramentas tem a maior variação proporcional: os 10 SKUs afetados quase decuplicam de valor entre o custo mínimo e o máximo (R$ 204,19 a R$ 1.963,75), puxado por poucos itens com histórico de custo bem disperso. Isso não muda o total "sem outliers" da tabela acima (R$ 28.474,77), que continua pelo custo mais recente, é uma leitura complementar para mostrar onde a decisão de qual custo usar pesa mais por categoria.

### Valor em estoque por produto, top produtos (novo em 18/09/2026)

O ranking bruto por valor em estoque tem pelo menos 2 itens com outlier de cadastro (custo acima do preço de venda) entre os 3 primeiros lugares. Não apresento o "top valor em estoque" sem tratar isso: a tabela abaixo mostra o bruto com a coluna de outlier sinalizada, seguida do top 15 recalculado sem esses itens. Lista completa (top 20 bruto + top 15 sem outliers) na aba "Top produtos valor estoque" da planilha.

| Código | Produto | Categoria | Custo | Estoque | Valor em estoque | Outlier de cadastro |
|---|---|---|---|---|---|---|
| 22483 | Bucha plástica c/ anel concreto 8mm | Básico | R$ 11,25 | 478 | R$ 5.377,50 | **SIM, custo maior que preço de venda (R$ 0,05)** |
| PRD00045 | Cimento Supremo 50kg | Básico | R$ 33,00 | 95 | R$ 3.135,00 | não |
| PRD00016 | Estribo Flexfer 10x16 4,2mm | Básico | R$ 60,00 | 42 | R$ 2.520,00 | **SIM, custo maior que preço de venda (R$ 1,20)** |
| 20250 | Tijolo 6 furos 09x14x29 Lorenzetti | Básico | R$ 0,72 | 2.598 | R$ 1.883,03 | não |
| 22114 | Tijolo 6 furos 09x14x24 Lorenzetti | Básico | R$ 0,60 | 2.514 | R$ 1.508,40 | não |
| 16420 | Corante base d'água 50ml xadrez preto | Pintura | R$ 50,02 | 24 | R$ 1.200,48 | **SIM, custo maior que preço de venda (R$ 7,50)** |

**Top 15 recalculado sem os outliers de cadastro:**

Coluna nova em 18/09/2026: "Valor em estoque" mostra o custo mais recente (como antes), e "Custo mín. a máx." mostra a faixa completa só para os produtos com mais de um fornecedor cadastrado, sem escolher qual dos dois vale. Produto com uma linha só de compra fica sem essa coluna preenchida, não há ambiguidade a mostrar.

| # | Código | Produto | Categoria | Valor em estoque | Custo mín. a máx. (múltiplos fornecedores) |
|---|---|---|---|---|---|
| 1 | PRD00045 | Cimento Supremo 50kg | Básico | R$ 3.135,00 | R$ 3.135,00 a R$ 3.505,50 (2 fornecedores) |
| 2 | 20250 | Tijolo 6 furos 09x14x29 Lorenzetti | Básico | R$ 1.883,03 | R$ 1.883,03 a R$ 2.779,86 (2 fornecedores) |
| 3 | 22114 | Tijolo 6 furos 09x14x24 Lorenzetti | Básico | R$ 1.508,40 | R$ 1.508,40 a R$ 2.436,07 (4 fornecedores) |
| 4 | 21452 | Tubo esgoto 100mm 6m | Hidráulica | R$ 709,43 | R$ 707,02 a R$ 719,90 (3 fornecedores) |
| 5 | 20708 | Pó de brita 5m³ | Básico | R$ 534,40 | |
| 6 | 22445 | Argamassa Extrakolla 2 cinza 20kg | Básico | R$ 507,00 | |
| 7 | 22446 | Argamassa Superkola 3Mais cinza 20kg | Básico | R$ 415,68 | |
| 8 | 506709 | Ventilador parede VOP Premium 60cm preto bivolt | Elétrica | R$ 399,96 | |
| 9 | 101010 | Ferro 3/8 (12 metros) 10mm | Básico | R$ 386,10 | |
| 10 | 20702 | Cabo flexível Corfio 4,0mm 750V preto | Elétrica | R$ 348,96 | |
| 11 | 21449 | Tubo esgoto 40mm 6m | Hidráulica | R$ 325,63 | |
| 12 | 21451 | Tubo esgoto 75mm 6m | Hidráulica | R$ 317,87 | |
| 13 | 22468 | Lona preta 4x100 75 micras | Não classificado | R$ 317,30 | |
| 14 | 22646 | Tubo esgoto 150mm 6m | Hidráulica | R$ 308,67 | |
| 15 | 20912 | Ferro 5/16 (12 metros) 8mm | Básico | R$ 298,00 | R$ 298,00 a R$ 339,50 (2 fornecedores) |

5 dos 15 produtos deste top têm mais de um fornecedor cadastrado, os mesmos 5 que já apareciam no top 20 bruto acima (nenhum deles é outlier de cadastro, por isso repetem nos dois rankings). Tijolo 6 furos 09x14x24 (código 22114) é o caso mais extremo: 4 fornecedores diferentes, valor em estoque variando de R$ 1.508,40 a R$ 2.436,07, uma diferença de R$ 927,67 sozinho. Nota: 20708 (Pó de brita 5m³) tinha o preço de venda cadastrado como R$ 0,00 no relatório, então não entra no cálculo de outlier de cadastro por custo maior que preço (a comparação exige preço maior que zero), mas o preço zerado por si só é uma falha de cadastro que impede vender esse item corretamente no sistema, vale o cliente confirmar.

### Maiores quantidades em estoque, unidades (novo em 18/09/2026)

Top produtos por quantidade física, independente do valor. Mostra onde está o volume de peças miúdas (parafuso, bucha), que não aparece nos rankings de valor mas ocupa espaço físico e representa capital de giro em volume. Lista completa (top 20) na aba "Maiores quantidades em estoque" da planilha.

| # | Código | Produto | Categoria | Quantidade | Valor em estoque |
|---|---|---|---|---|---|
| 1 | 20250 | Tijolo 6 furos 09x14x29 Lorenzetti | Básico | 2.598 | R$ 1.883,03 |
| 2 | 22114 | Tijolo 6 furos 09x14x24 Lorenzetti | Básico | 2.514 | R$ 1.508,40 |
| 3 | 22553 | Parafuso chipboard CH PH 4,0x50mm | Básico | 1.504 | R$ 114,24 |
| 4 | 1592 | Bucha plástica tijolo oco 10mm (500) branca | Básico | 1.414 | R$ 752,45 (outlier de cadastro) |
| 5 | 22294 | Bucha 06 | Básico | 910 | R$ 12,93 |
| 6 | 20480 | Parafuso drywall forro 4,2x13mm | Básico | 500 | R$ 19,49 |
| 7 | 20895 | Parafuso chip 4,5x40 amarelo | Básico | 500 | R$ 37,98 |
| 8 | 20374 | Parafuso chip 5,0x40 amarelo | Básico | 486 | R$ 46,85 |
| 9 | 22483 | Bucha plástica c/ anel concreto 8mm | Básico | 478 | R$ 5.377,50 (outlier de cadastro) |
| 10 | 22748 | Parafuso chip 4,5x45 amarelo | Básico | 300 | R$ 28,78 |

Além do tijolo (que já é âncora conhecido), o volume físico de estoque está concentrado em parafuso e bucha de valor unitário baixo, itens que praticamente não aparecem em nenhum ranking de valor ou margem, mas ocupam prateleira e representam capital de giro somado. Dois dos itens desta lista (1592 e 22483) são os mesmos outliers de cadastro já identificados acima, o volume alto some junto com o valor quando o custo é corrigido.

### Matriz giro x margem (4 quadrantes)

Cálculo restrito aos 295 SKUs presentes nos dois relatórios (giro vem da Curva ABC, margem vem do Estoque). Limiar de corte: mediana do próprio grupo cruzado, giro igual ou acima de 4 unidades vendidas no acumulado é "alto giro", margem igual ou acima de 44,3% é "alta margem".

| Quadrante | SKUs | Valor em estoque a custo |
|---|---|---|
| Estrela (alto giro, alta margem) | 85 | R$ 2.942,70 |
| Isca (alto giro, baixa margem) | 78 | R$ 24.446,22 |
| Reserva de lucro (baixo giro, alta margem) | 62 | R$ 1.603,65 |
| Candidato a liquidar (baixo giro, baixa margem) | 70 | R$ 5.375,16 |

O quadrante isca concentra quase 60% do valor em estoque a custo entre os SKUs cruzados, coerente com o achado do `diagnostico-curva-abc.md`: cimento, tijolo e argamassas de giro alto exigem capital parado em volume mesmo com margem percentual apertada. O quadrante candidato a liquidar (R$ 5.375,16) é o primeiro lugar a olhar pra liberar caixa sem mexer em item que ainda gira bem.

**5 principais produtos por valor em estoque em cada quadrante, pra dar contexto:**
- **Isca:** Bucha plástica c/ anel concreto 8mm (código 22483, R$ 5.377,50), Cimento Supremo 50kg (R$ 3.135), Estribo Flexfer 10x16 (código PRD00016, R$ 2.520), Tijolo 6 furos 09x14x29 (R$ 1.883), Tijolo 6 furos 09x14x24 (R$ 1.508). **Atenção:** os 2 primeiros itens (22483 e PRD00016) são os mesmos outliers de cadastro custo maior que preço já identificados na auditoria abaixo, a margem negativa que os classificou como "isca" nesta matriz é efeito do erro de cadastro, não leitura real de margem baixa. Cimento e os dois tijolos são os itens isca de verdade deste quadrante, mas os três também têm mais de um fornecedor cadastrado, ver classificação provisória logo abaixo.
- **Estrela:** Lona preta 4x100 75 micras (R$ 317), Canaleta adesiva com divisória (R$ 237), PU 40 branco 380g (R$ 175), Enxada olho oval 19cm (R$ 96), Eletroduto corrugado 25mm (R$ 87).
- **Candidato a liquidar:** Pó de brita 5m³ (R$ 534, sem margem calculável, preço de venda zerado no cadastro), Tubo esgoto 40mm 6m (R$ 326), Tubo esgoto 75mm 6m (R$ 318), Tubo esgoto 150mm 6m (R$ 309), Verniz marítimo 3,6L Alessi (R$ 174).
- **Reserva de lucro:** Silicone 400g base d'água Unipega (R$ 193), Linha pedreiro 100m (R$ 128), Parafuso chipboard 4,0x50mm (R$ 114), Mão francesa 38,5x23,5cm branco (R$ 93), Luva de correr soldável 25mm (R$ 74).

### Classificação provisória por múltiplos fornecedores (novo em 18/09/2026)

Dos 295 SKUs cruzados nesta matriz, 77 são códigos com mais de um fornecedor cadastrado (dos 86 do estoque inteiro, os outros 9 caem em estoque parado abaixo, sem giro registrado, então não entram aqui: 77 + 9 = 86, cobre todos). A coluna "Margem %" da tabela principal usa o custo da compra mais recente, igual às demais tabelas deste diagnóstico. Para esses 77, a aba "Matriz giro x margem" da planilha ganhou colunas "Margem % (custo mín.)", "Margem % (custo máx.)", "Quadrante (custo mín.)", "Quadrante (custo máx.)" e "Classificação provisória", recalculando a margem nos dois cenários de custo já pagos.

Em 37 desses 77 (48%), a margem cruza a linha de corte de 44,3% dependendo do custo usado, ou seja, o quadrante (Estrela, Isca, Reserva de lucro ou Candidato a liquidar) desses 37 produtos específicos é provisório até o cliente confirmar qual custo vale. Não reclassifiquei nenhum deles, a tabela principal continua com o quadrante calculado pelo custo mais recente, só sinalizo onde essa classificação pode mudar de lado. Os 8 casos de maior valor em estoque entre os 37:

| Código | Produto | Categoria | Quadrante atual (custo mais recente) | Margem % (custo mín.) | Margem % (custo máx.) | Estoque disponível |
|---|---|---|---|---|---|---|
| 22686 | Carrinho de carga 45L Minasul | Ferramentas | Isca | 100,0% | 38,1% | 3 |
| 4436 | Cabo de aço plastificado 3/32" | Básico | Isca* | 64,6% | -250,0%* | 100 |
| 20734 | Torneira jardim megajato 1/2" amarela | Hidráulica | Isca | 100,0% | 43,2% | 93 |
| 1212 | Prego polido 17x27 1kg com cabeça | Básico | Isca | 50,0% | 42,0% | 10 |
| **12010** | **Argamassa massa reboco cinza 20kg** | **Básico** | **Estrela** | **56,5%** | **24,2%** | **9** |
| 22583 | Torneira de boia p/ cx d'água alta vazão 1/2 e 3/4" Cipla | Hidráulica | Candidato a liquidar | 100,0% | 43,3% | 2 |
| 21454 | Tubo soldável 25mm 6m | Hidráulica | Isca | 49,1% | 40,0% | 5 |
| 22146 | Trincha branca "396" 3.0" | Pintura | Isca | 74,6% | 36,9% | 6 |

*Cabo de aço plastificado (4436) é o mesmo código já citado na auditoria de outliers de cadastro (custo da compra mais recente maior que o preço de venda), por isso a margem "atual" já sai negativa (-24%) e o cenário de custo máximo fica ainda mais distorcido (-250%). Não é erro de cálculo desta planilha, é o efeito de somar dois problemas de cadastro no mesmo SKU: fornecedor múltiplo e custo maior que preço.

**O caso que mais importa pra decisão de negócio é a Argamassa massa reboco cinza 20kg (código 12010).** Ela é citada em `diagnostico-curva-abc.md` como o item de margem mais alta (56,5%) pra combinar com o Cimento Supremo no kit "cimento + argamassa" (Pilar 3, Combo de Produtos). Essa margem de 56,5% usa o custo mais recente (R$ 9,52, fornecedor Inkor). Mas esse mesmo SKU já foi comprado por R$ 16,59 de outro fornecedor, o que derrubaria a margem para 24,2%, abaixo da mediana do catálogo (44,3%) e do outro lado da linha que separa "alta" de "baixa" margem. Ou seja: dependendo de qual custo o cliente confirmar como válido, a Argamassa massa reboco deixa de ser Estrela e vira Isca, e o racional do kit ("cimento isca + argamassa de margem alta") perde parte do sustento. Recomendo confirmar o custo real desse item antes de fechar a composição ou a comunicação do kit com o cliente. Não altero a classificação nem o kit sugerido aqui, só sinalizo a pendência.

Os outros 40 SKUs multi-fornecedor cruzados na matriz (77 menos os 37 acima) têm margem mínima e máxima do mesmo lado da linha de corte: o número exato de margem muda com o custo, mas o quadrante (Estrela, Isca, Reserva de lucro ou Candidato a liquidar) fica estável nos dois cenários. Lista completa dos 77, com as duas margens e os dois quadrantes lado a lado, na aba "Matriz giro x margem" da planilha.

### Estoque parado (proxy: sem venda no período coberto pela Curva ABC)

- Valor financeiro parado a custo: R$ 6.293,29, em 148 SKUs.
- Maior concentração em valor por categoria: Não classificado (R$ 1.648,01, 38 SKUs), Ferramentas (R$ 1.063,56, 35 SKUs), Hidráulica (R$ 997,41, 21 SKUs), Elétrica (R$ 953,83, 12 SKUs). **Correção em 18/09/2026:** a rodada anterior citava "Elétrica, seguida por Ferramentas e Hidráulica" como maior concentração, baseado só nos 2 itens de maior valor individual. Recalculando a soma por categoria, Não classificado lidera (por ter mais SKUs parados, mesmo de ticket baixo cada), seguido por Ferramentas e Hidráulica. Elétrica cai para 4º lugar.

**Top 10 por valor parado (referência rápida):**

| Código | Produto | Categoria | Estoque disponível | Valor parado a custo | Data última compra |
|---|---|---|---|---|---|
| 506709 | Ventilador parede VOP Premium 60cm preto bivolt | Elétrica | 2 | R$ 399,96 | 13/03/2026 |
| 20702 | Cabo flexível Corfio 4,0mm 750V preto | Elétrica | 100 | R$ 348,96 | 26/06/2026 |
| 22955 | Piscina Fast Set 2.300L | Não classificado | 1 | R$ 241,33 | 22/12/2025 |
| 20591 | Ducha Lorenzetti Comfort 220V 7500W | Hidráulica | 2 | R$ 182,16 | 13/07/2026 |
| 22948 | Piscina Fast Set 1000L | Não classificado | 1 | R$ 157,18 | 22/12/2025 |
| 22935 | Jogo brocas/talhadeira SDS Plus 13 peças | Não classificado | 1 | R$ 157,16 | 22/12/2025 |
| 22933 | Jogo broca bits 110 peças | Ferramentas | 1 | R$ 155,00 | 22/12/2025 |
| 22917 | Pulverizador plástico costal manual 20L | Não classificado | 1 | R$ 141,47 | 22/12/2025 |
| 1896 | Mangueira nível cristal 5/16x1,3mm, metro | Hidráulica | 100 | R$ 137,40 | 29/07/2026 |
| 1040 | Broca encaixe SDS Plus 7x210mm blister | Ferramentas | 15 | R$ 130,50 | 09/09/2026 |

**Estoque parado ordenado por antiguidade da última compra (novo em 18/09/2026), do mais antigo pro mais recente.** "Data da última compra" é quando a loja comprou do fornecedor, não quando o cliente final comprou, não é régua de tempo parado por venda de verdade (6 ou mais meses sem venda), é a leitura mais honesta possível com o dado disponível. 8 dos 148 SKUs (5,4%) não têm essa data preenchida no relatório de Estoque, ficam sem posição de antiguidade. Data mais antiga encontrada: 22/12/2025 (23 SKUs compartilham essa data, provável lote de reposição único há 9 meses); data mais recente entre os parados: 11/09/2026. Lista completa das 148 linhas, já ordenada, na aba "Estoque parado" da planilha.

| Código | Produto | Categoria | Data última compra | Estoque disponível | Valor parado a custo |
|---|---|---|---|---|---|
| 22930 | Desempenadeira plástica dentada 12x26 monobloco | Ferramentas | 22/12/2025 | 1 | R$ 10,99 |
| 22950 | Jogo brocas chatas 7 peças 1/4-1" | Não classificado | 22/12/2025 | 1 | R$ 31,43 |
| 22917 | Pulverizador plástico costal manual 20L | Não classificado | 22/12/2025 | 1 | R$ 141,47 |
| 22933 | Jogo broca bits 110 peças | Ferramentas | 22/12/2025 | 1 | R$ 155,00 |
| 22920 | Disco diamantado porcelanato/cerâmica 110x20mm | Ferramentas | 22/12/2025 | 1 | R$ 13,91 |
| 22935 | Jogo brocas/talhadeira SDS Plus 13 peças | Não classificado | 22/12/2025 | 1 | R$ 157,16 |
| 22948 | Piscina Fast Set 1000L | Não classificado | 22/12/2025 | 1 | R$ 157,18 |
| 22955 | Piscina Fast Set 2.300L | Não classificado | 22/12/2025 | 1 | R$ 241,33 |

(mais 15 itens com a mesma data de 22/12/2025, total de 23 SKUs nesse lote; lista completa na planilha). Estes 23 itens são os candidatos mais fortes a estoque parado de verdade (compra mais antiga entre os 148 sem venda no acumulado), valem confirmação com o cliente antes de qualquer decisão de baixa ou liquidação.

Repito a limitação: isso é "sem venda no acumulado coberto pela Curva ABC", não "sem venda há 6 ou mais meses". Um item pode não estar aqui parado há muito tempo, só não ter vendido no recorte deste relatório específico. Cliente confirma se o proxy é aceitável ou se vale pedir relatório de última venda por SKU, o que também resolveria a falta de régua de tempo parado por venda de verdade.

**Múltiplos fornecedores entre os SKUs parados (novo em 18/09/2026):** 9 dos 148 SKUs parados também têm mais de um fornecedor cadastrado. A aba "Estoque parado" da planilha ganhou as colunas "Custo mín.", "Custo máx.", "Valor parado (custo mín.)" e "Valor parado (custo máx.)" pra esses 9, sem escolher qual custo vale:

| Código | Produto | Categoria | Valor parado (custo usado) | Valor parado (custo mín.) | Valor parado (custo máx.) |
|---|---|---|---|---|---|
| 22943 | Cilindro gás mapp pro 400gr | Não classificado | R$ 37,42 | R$ 37,42 | R$ 86,42 |
| 22932 | Fita dupla face 25mmx2m externo | Não classificado | R$ 14,80 | R$ 14,80 | R$ 29,20 |
| 20674 | Sapato monodensidade s/bico cano baixo nº43 | Hidráulica | R$ 62,88 | R$ 62,88 | R$ 62,88 |
| 22682 | Registro de esfera máquina de lavar 1/2"x3/4" Fertak | Hidráulica | R$ 43,32 | R$ 43,32 | R$ 57,65 |
| 22922 | Desempenadeira lisa CB plástico 12x25,5cm | Ferramentas | R$ 34,84 | R$ 26,42 | R$ 34,84 |
| 21145 | Pilha alcalina AAA c/02 und Eletronic | Elétrica | R$ 17,60 | R$ 17,60 | R$ 32,90 |
| 21152 | Trena emborrachada 10m x 25mm Thompson | Ferramentas | R$ 41,54 | R$ 0,00 | R$ 41,54 |
| 20357 | Válvula click 1.1/4" corpo plástico tampa inox | Hidráulica | R$ 0,00 | R$ 0,00 | R$ 53,72 |
| 22068 | Cruzeta/espaçador 5,00mm c/100 | Básico | R$ 5,22 | R$ 5,22 | R$ 5,28 |

Dois casos merecem atenção além da faixa em si. A Trena emborrachada (código 21152) tem uma compra histórica registrada a custo zero, provável erro de cadastro daquela nota, não item recebido de graça: o custo mais recente (R$ 20,77 a unidade) é o número mais confiável dos dois. E a Válvula click (código 20357) está entrando no total de estoque parado (R$ 6.293,29) como R$ 0,00 porque a compra mais recente dela também está cadastrada a custo zero: pelo outro fornecedor, o valor parado desse item seria R$ 53,72, não R$ 0,00. Isso não muda o total geral de forma relevante (a diferença é pequena), mas mostra que o proxy "custo mais recente" às vezes pega uma linha com erro de cadastro em vez da mais confiável, exatamente o tipo de caso que a mudança de estrutura desta rodada existe para deixar visível em vez de esconder atrás de uma escolha automática.

### Risco de ruptura

SKU de classe A ou B do indicador de giro por quantidade (ver `diagnostico-curva-abc.md`, esta classificação NÃO é a Curva ABC oficial por faturamento) com estoque atual de 10 unidades ou menos:

| Código | Produto | Categoria | Indicador giro (classe qtd) | Giro (qtd. faturada) | Estoque disponível |
|---|---|---|---|---|---|
| 21603 | Telha cerâmica esmaltada | Acabamento | B | 150 | 0 |
| 21435 | Fita crepe amarela 18x40 automotiva | Pintura | B | 167 | 7 |
| 12010 | Argamassa massa reboco cinza 20kg | Básico | B | 138 | 9 |
| 101010 | Ferro 3/8 (12 metros) 10mm | Básico | B | 61 | 9 |
| 20912 | Ferro 5/16 (12 metros) 8mm | Básico | B | 86 | 10 |

A Telha cerâmica esmaltada já está com estoque zerado e teve 150 unidades vendidas no acumulado (classe B), ruptura em curso, não é mais risco futuro. Este item também aparece na auditoria de outliers abaixo (custo cadastrado acima do preço de venda), então antes de repor vale corrigir o cadastro de custo pra não comprar de novo com margem errada no sistema.

Critério provisório: sem o período real da Curva ABC declarado, não dá pra calcular dias de cobertura de estoque (giro diário x estoque atual), só o corte simples "estoque baixo + já vendeu bastante". Refinar quando o cliente confirmar o período.

O Ferro 5/16 (código 20912) desta lista também é um dos 86 códigos com mais de um fornecedor, mas essa classificação de risco de ruptura não depende de margem, só de giro e estoque disponível, então não muda com o custo. A ambiguidade de custo desse item só importa para o valor em estoque e a margem dele, tratados nas outras seções.

### Auditoria de qualidade do cadastro

49 SKUs com valor de custo fora do padrão, dois tipos:

**Custo cadastrado acima do preço de venda (16 itens).** Indica erro de cadastro (unidade de compra diferente da unidade de venda, custo de lote lançado como custo unitário, ou revisão de preço de venda que não acompanhou o custo). Destaque:

| Código | Produto | Custo cadastrado | Preço de venda | Estimativa (mediana de comparável interno) |
|---|---|---|---|---|
| 1016 | Broca AR 04.0mm blister C/10 | R$ 15,73 | R$ 7,50 | R$ 0,97 (3 comparáveis da família "Broca blister") |
| 1458 | Curva ESG 90° curta SN DN 40 Fortlev | R$ 6,10 | R$ 3,65 | R$ 17,63 (3 comparáveis; aqui o comparável sugere o **preço de venda** é que pode estar baixo, não o custo) |
| 1516 | Caixa de luz octogonal 4x4 Fortlev | R$ 14,25 | R$ 4,10 | R$ 1,21 (1 comparável) |
| PRD00016 | Estribo Flexfer 10x16 4,2mm | R$ 60,00 | R$ 1,20 | sem comparável no relatório |
| 20708 | Pó de brita 5m³ | R$ 133,60 | R$ 0,00 | sem comparável, preço de venda também zerado |
| 21603 | Telha cerâmica esmaltada | R$ 8,00 | R$ 1,60 | sem comparável |

**Custo cadastrado zerado (33 itens).** Impede calcular margem real desses SKUs, tratados como margem indefinida nas contas deste diagnóstico (não entraram no cálculo de margem por categoria nem na matriz giro x margem quando cruzados). Exemplos com comparável interno encontrado:

| Código | Produto | Preço de venda | Custo estimado (mediana comparável) |
|---|---|---|---|
| 1021 | Broca AR 06.5mm blister C/10 | R$ 6,15 | R$ 0,97 |
| 1044 | Broca encaixe SDS Plus 10x160mm | R$ 14,20 | R$ 8,25 |
| 1045 | Broca encaixe SDS Plus 10x210mm | R$ 16,10 | R$ 8,25 |
| 1447 | Luva ESG SN DN 50 Fortlev | R$ 2,70 | R$ 3,44 |
| 1332 | Par chip CH PH 4.0x40 BC PH2 Multifix | R$ 0,20 | sem comparável |

Metodologia da estimativa: mediana do custo de produtos com nome-base semelhante no mesmo relatório de estoque, excluindo os próprios outliers da base de comparação. Só apliquei quando havia pelo menos 1 comparável real no relatório. Nos 34 casos sem comparável interno, não pesquisei preço de mercado externo item a item porque o impacto financeiro individual é pequeno (a maioria tem estoque de 1 a 10 unidades); se o cliente quiser a estimativa de mercado desses itens específicos, posso rodar essa pesquisa à parte. Em nenhum dos dois casos o valor estimado substitui o dado cadastrado: é benchmark para o cliente confirmar ou corrigir no ERP, listado por completo na aba "Auditoria outliers cadastro" da planilha.

### Recomendação de ação por quadrante

- **Estrela** (85 SKUs, R$ 2.942,70 em estoque): manter reposição normal, são os produtos que já funcionam bem em giro e margem.
- **Isca** (78 SKUs, R$ 24.446,22 em estoque): manter estoque saudável, é onde está a maior parte do capital parado do grupo cruzado, mas é capital que sustenta o fluxo de caixa e atrai cliente pra loja. Não é candidato a liquidar.
- **Reserva de lucro** (62 SKUs, R$ 1.603,65 em estoque): baixo giro mas margem boa, avaliar se vale destacar em vitrine ou combinar em kit (ver candidatos a kit no `diagnostico-curva-abc.md`) pra aumentar a saída sem mexer em preço.
- **Candidato a liquidar** (70 SKUs, R$ 5.375,16 em estoque): primeiro lugar a investigar pra ação de desova ou promoção, maior retorno de capital liberado por SKU afetado.

Essas recomendações valem para o quadrante como grupo. Para os 37 SKUs específicos com classificação provisória (ver seção acima), a ação certa pode mudar depois que o cliente confirmar o custo, principalmente a Argamassa massa reboco cinza 20kg (código 12010): hoje ela está no grupo "manter reposição normal" (Estrela), mas se o custo de R$ 16,59 for o válido, ela cai para o mesmo grupo do Cimento (Isca, manter estoque saudável sem decisão de preço), o que muda a lógica do kit sugerido no `diagnostico-curva-abc.md`. Não decido preço final de liquidação nem desconto, isso é decisão do `@copywriter`/`@gestor-trafego` junto com o cliente.

### Comparação com o período/snapshot anterior

Primeiro snapshot registrado para este cliente, sem comparação anterior.

### Próximos passos

1. `@gestor-trafego`/`@copywriter` usam a lista de risco de ruptura antes de colocar Telha cerâmica esmaltada, Fita crepe amarela, Argamassa massa reboco ou os dois Ferros de vergalhão em campanha: reforçar compra antes ou reduzir orçamento até repor.
2. Avaliar liquidação dos 70 SKUs do quadrante "candidato a liquidar" (R$ 5.375,16 parados a custo).
3. Corrigir no ERP os 49 itens de cadastro com custo fora do padrão listados na auditoria, começando pelos que também aparecem em risco de ruptura (Telha cerâmica esmaltada).
4. Confirmar com o cliente se aceita o proxy de estoque parado usado aqui (sem venda no acumulado da Curva ABC) ou se vale pedir ao ERP um relatório com data de última venda por SKU pra aplicar a régua padrão de 6 ou mais meses.
5. `@analista-dados` usa estoque parado e valor por quadrante como KPI de dashboard quando o cliente tiver conta de mídia ativa.
6. Confirmar com o cliente os 23 SKUs sem venda no acumulado e com última compra em 22/12/2025 (o lote mais antigo entre os 148 parados), candidatos mais fortes a ação de baixa ou liquidação.
7. Corrigir no ERP o cadastro dos 2 itens que mais distorcem o "top valor em estoque" bruto (22483, bucha plástica c/ anel concreto 8mm, e PRD00016, Estribo Flexfer), ambos com custo maior que o preço de venda.
8. Levar para a reunião com o cliente as duas opções de custo dos 86 SKUs com mais de um fornecedor, já lado a lado nas 4 tabelas afetadas (valor em estoque por produto, estoque por categoria, estoque parado e matriz giro x margem), e decidir junto qual custo vale por SKU ou por regra geral: se o ERP tiver custo médio ponderado ou custo de reposição já calculado, ele é mais confiável do que mínimo, máximo ou compra mais recente, e resolve de vez os até R$ 6.152,98 de diferença no valor total em estoque.
9. Confirmar com o cliente o custo real da Argamassa massa reboco cinza 20kg (código 12010) antes de fechar o kit "cimento + argamassa" com o `@copywriter`: a margem varia de 56,5% a 24,2% dependendo do fornecedor considerado, o que muda o quadrante do item (Estrela ou Isca) e o racional do kit.
10. Revisar com o cliente os outros 36 SKUs com classificação de quadrante provisória (lista completa na aba "Matriz giro x margem" da planilha, coluna "Classificação provisória") antes de qualquer decisão de campanha, vitrine ou liquidação que dependa de qual quadrante eles ocupam.

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
