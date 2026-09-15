# Diagnóstico de Giro de Estoque e Margem para Hora Z
**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra, atividade "Giro de Estoque e Margem"
**Como ler este arquivo:** histórico cumulativo, uma seção por período/snapshot coberto por relatório de estoque do cliente, do mais recente (topo) para o mais antigo (final), independente da ordem em que os relatórios foram processados.

## Visão geral acumulada

| Período/snapshot | Estoque parado corrigido | Giro médio (mediana) | Quadrante predominante |
|---|---|---|---|
| Snapshot 15/09/2026 | R$ 6.293,29 (148 SKUs, proxy por ausência de venda) | 4 unidades (mediana, 295 SKUs cruzados) | Estrela (85 de 295 SKUs cruzados) |

Primeira rodada, sem snapshot anterior para comparar evolução de estoque parado ou mudança de quadrante.

---

## Período/Snapshot: 15/09/2026 (snapshot único de estoque)
**Fonte dos dados:** `Estoque.xlsx`, aba "Produtos por Fornecedor", recebido do cliente em 15/09/2026, processado em 09-2026. Cruzado com `Curva_Abc.xlsx` (mesma data de recebimento) para leitura de giro.
**Planilha(s):** `09-2026/Arquivos/15-inteligencia-dados-estoque-giro-margem_snapshot-2026-09-15.xlsx`
**Status:** v1, sujeito a refinamento

### Resumo executivo

- Valor total em estoque a custo: R$ 40.661,03, em 443 SKUs únicos.
- O relatório de estoque não declara data de corte explícita. Usei a data de hoje (15/09/2026) como data do snapshot, conforme instrução do cliente.
- **Limitação principal desta rodada: não há data de última venda por SKU em nenhum dos dois relatórios recebidos**, só data de última compra (quando fornecedor comprou o produto, não quando o cliente final comprou). Isso impede aplicar a definição padrão de estoque parado ("sem saída há 6 ou mais meses"). Na falta dela, usei um proxy: SKU que está no snapshot de estoque e não aparece em nenhuma linha da Curva ABC recebida (que cobre um acumulado, período não declarado, ver `diagnostico-curva-abc.md`). Isso aproxima "sem venda no período coberto", não "sem venda há X meses". Recomendo pedir ao ERP um relatório com data de última venda por SKU pra refinar isso na próxima rodada.
- O relatório de estoque original ("Produtos por Fornecedor") lista 543 linhas para 443 SKUs únicos: 100 produtos aparecem em mais de uma linha porque o mesmo código já foi comprado de mais de um fornecedor ao longo do tempo. Estoque disponível e preço de venda são idênticos entre as linhas duplicadas do mesmo código (só custo, fornecedor e data de compra variam), então deduplicei mantendo a linha com a compra mais recente, que é o custo mais atual disponível.
- 148 dos 443 SKUs do estoque atual (33%) não têm nenhuma venda registrada na Curva ABC recebida, valor financeiro parado a custo de R$ 6.293,29 (15,5% do valor total em estoque).
- Auditoria de cadastro encontrou 49 SKUs com valor de custo fora do padrão: 33 com custo zerado e 16 com custo cadastrado acima do próprio preço de venda (prejuízo no cadastro, não necessariamente prejuízo real na venda). Detalhe na seção própria abaixo.

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

### Matriz giro x margem (4 quadrantes)

Cálculo restrito aos 295 SKUs presentes nos dois relatórios (giro vem da Curva ABC, margem vem do Estoque). Limiar de corte: mediana do próprio grupo cruzado, giro igual ou acima de 4 unidades vendidas no acumulado é "alto giro", margem igual ou acima de 44,3% é "alta margem".

| Quadrante | SKUs | Valor em estoque a custo |
|---|---|---|
| Estrela (alto giro, alta margem) | 85 | R$ 2.942,70 |
| Isca (alto giro, baixa margem) | 78 | R$ 24.446,22 |
| Reserva de lucro (baixo giro, alta margem) | 62 | R$ 1.603,65 |
| Candidato a liquidar (baixo giro, baixa margem) | 70 | R$ 5.375,16 |

O quadrante isca concentra quase 60% do valor em estoque a custo entre os SKUs cruzados, coerente com o achado do `diagnostico-curva-abc.md`: cimento, tijolo e argamassas de giro alto exigem capital parado em volume mesmo com margem percentual apertada. O quadrante candidato a liquidar (R$ 5.375,16) é o primeiro lugar a olhar pra liberar caixa sem mexer em item que ainda gira bem.

### Estoque parado (proxy: sem venda no período coberto pela Curva ABC)

- Valor financeiro parado a custo: R$ 6.293,29, em 148 SKUs.
- Maior concentração em valor: Elétrica (ventilador de parede, cabo flexível), seguida por Ferramentas e Hidráulica.

| Código | Produto | Categoria | Estoque disponível | Valor parado a custo |
|---|---|---|---|---|
| 506709 | Ventilador parede VOP Premium 60cm preto bivolt | Elétrica | 2 | R$ 399,96 |
| 20702 | Cabo flexível Corfio 4,0mm 750V preto | Elétrica | 100 | R$ 348,96 |
| 22955 | Piscina Fast Set 2.300L | Não classificado | 1 | R$ 241,33 |
| 20591 | Ducha Lorenzetti Comfort 220V 7500W | Hidráulica | 2 | R$ 182,16 |
| 22948 | Piscina Fast Set 1000L | Não classificado | 1 | R$ 157,18 |
| 22935 | Jogo brocas/talhadeira SDS Plus 13 peças | Não classificado | 1 | R$ 157,16 |
| 22933 | Jogo broca bits 110 peças | Ferramentas | 1 | R$ 155,00 |

Lista completa das 148 linhas na aba "Estoque parado" da planilha. Repito a limitação: isso é "sem venda no acumulado coberto pela Curva ABC", não "sem venda há 6 ou mais meses". Um item pode não estar aqui parado há muito tempo, só não ter vendido no recorte deste relatório específico. Cliente confirma se o proxy é aceitável ou se vale pedir relatório de última venda por SKU.

### Risco de ruptura

SKU de classe A ou B (top vendas por quantidade na Curva ABC) com estoque atual de 10 unidades ou menos:

| Código | Produto | Categoria | Classe | Giro (qtd. faturada) | Estoque disponível |
|---|---|---|---|---|---|
| 21603 | Telha cerâmica esmaltada | Acabamento | B | 150 | 0 |
| 21435 | Fita crepe amarela 18x40 automotiva | Pintura | B | 167 | 7 |
| 12010 | Argamassa massa reboco cinza 20kg | Básico | B | 138 | 9 |
| 101010 | Ferro 3/8 (12 metros) 10mm | Básico | B | 61 | 9 |
| 20912 | Ferro 5/16 (12 metros) 8mm | Básico | B | 86 | 10 |

A Telha cerâmica esmaltada já está com estoque zerado e teve 150 unidades vendidas no acumulado (classe B), ruptura em curso, não é mais risco futuro. Este item também aparece na auditoria de outliers abaixo (custo cadastrado acima do preço de venda), então antes de repor vale corrigir o cadastro de custo pra não comprar de novo com margem errada no sistema.

Critério provisório: sem o período real da Curva ABC declarado, não dá pra calcular dias de cobertura de estoque (giro diário x estoque atual), só o corte simples "estoque baixo + já vendeu bastante". Refinar quando o cliente confirmar o período.

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

Não decido preço final de liquidação nem desconto, isso é decisão do `@copywriter`/`@gestor-trafego` junto com o cliente.

### Comparação com o período/snapshot anterior

Primeiro snapshot registrado para este cliente, sem comparação anterior.

### Próximos passos

1. `@gestor-trafego`/`@copywriter` usam a lista de risco de ruptura antes de colocar Telha cerâmica esmaltada, Fita crepe amarela, Argamassa massa reboco ou os dois Ferros de vergalhão em campanha: reforçar compra antes ou reduzir orçamento até repor.
2. Avaliar liquidação dos 70 SKUs do quadrante "candidato a liquidar" (R$ 5.375,16 parados a custo).
3. Corrigir no ERP os 49 itens de cadastro com custo fora do padrão listados na auditoria, começando pelos que também aparecem em risco de ruptura (Telha cerâmica esmaltada).
4. Confirmar com o cliente se aceita o proxy de estoque parado usado aqui (sem venda no acumulado da Curva ABC) ou se vale pedir ao ERP um relatório com data de última venda por SKU pra aplicar a régua padrão de 6 ou mais meses.
5. `@analista-dados` usa estoque parado e valor por quadrante como KPI de dashboard quando o cliente tiver conta de mídia ativa.

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
