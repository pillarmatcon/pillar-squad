# Diagnóstico de Giro de Estoque e Margem para Construmais
**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra, atividade "Giro de Estoque e Margem"
**Como ler este arquivo:** histórico cumulativo, uma seção por período/snapshot coberto por relatório de estoque do cliente, do mais recente (topo) para o mais antigo (final), independente da ordem em que os relatórios foram processados.

**Nota de migração (26/08/2026):** este arquivo é novo. Até esta data, Curva ABC e Giro/Estoque do cliente viviam juntos em `diagnostico-estoque.md` (formato antigo, anterior à divisão em dois arquivos do `_squad/06-inteligencia-dados/SKILL.md` atual). Optei por **não migrar agora** o conteúdo histórico inteiro daquele arquivo (as auditorias de cadastro e o detalhamento do snapshot de 03/08/2026, além das 4 seções de período de Curva ABC) para cá: é uma reorganização grande e puramente mecânica, sem gerar leitura nova, e o risco de erro de transcrição num arquivo com centenas de valores financeiros não compensa fazer isso no meio de uma entrega que já tem cálculo novo. `diagnostico-estoque.md` segue sendo a fonte de verdade da auditoria de cadastro de 03/08/2026 (outliers críticos, categoria corrompida, fornecedor duplicado etc.) e dos 4 períodos de Curva ABC até uma migração completa ser feita à parte, que fica proposta como tarefa independente. Este arquivo novo começa direto pela seção mais recente, já no formato de `diagnostico-giro-estoque.md` do SKILL.md atual, e referencia `diagnostico-estoque.md` sempre que usa um número que nasceu lá.

## Visão geral acumulada
*(atualizar este bloco a cada novo período/snapshot processado, não é seção fixa)*

| Período/Snapshot | Estoque com giro comprometido (121+ dias, no mínimo) | Giro predominante (por valor) | Observação |
|---|---|---|---|
| 03/08/2026 (cruzado com os 4 períodos de Curva ABC, mai/2025 a jun/2026) | R$ 450.534,16 em 2.888 SKUs (50,9% do estoque comercial ajustado) | Bucket "31 a 60 dias" concentra 48,2% do valor (R$ 426.567,77 em 1.888 SKUs) | Primeira seção deste arquivo, sem período anterior para comparar |

Uma leitura que já aparece nesta primeira rodada: **metade do valor de estoque a custo da loja (50,9%) está em produtos sem venda confirmada há pelo menos 121 dias**, incluindo os 1.733 SKUs que não venderam nenhuma unidade nos 14 meses inteiros cobertos pelos 4 relatórios de Curva ABC. Isso é maior que o "estoque parado" de R$ 373.769,46 já reportado em `diagnostico-estoque.md` (03/08/2026) porque aquele número olhava só para "nunca vendeu nos 4 períodos"; aqui a leitura inclui também quem vendeu por último há mais de 4 meses, não só quem nunca vendeu.

---

## Período/Snapshot: 03/08/2026, cruzado com os 4 períodos de Curva ABC (01/05/2025 a 30/06/2026)
**Fonte dos dados:** `Produto em 03-08-26.htm` (snapshot de estoque, sistema Pontual Tecnologia) cruzado com `qtd_vendida` dos 4 arquivos de Curva ABC padronizados (mai-out/2025, nov-dez/2025, jan-mar/2026, abr-jun/2026), processado em 08-2026
**Planilha:** `08-2026/Arquivos/26-inteligencia-dados-giro-estoque-por-bucket_2026-08-03.xlsx` (abas: Ranking por valor de estoque, Resumo por bucket, Ativo imobilizado excluído, Outliers críticos excluídos)
**Status:** v1, sujeito a refinamento
**Pedido que originou esta seção:** classificar o estoque por giro em buckets de 30/60/90/120/150/180/acima de 180 dias sem venda, trazendo os principais produtos por valor em estoque com categoria, custo e margem, já considerando os erros de cadastro já identificados.

### Metodologia da classificação por bucket (leia antes de usar os números abaixo)
Nenhum dos relatórios de origem tem campo de "data da última venda" por SKU. O que existe são 4 relatórios de Curva ABC por período fechado, com durações desiguais (6, 2, 3 e 3 meses), cada um dizendo só se o SKU vendeu ou não vendeu naquele período, não em que dia. Para aproximar "dias sem venda" a partir disso, segui este critério, auditável mas explicitamente uma aproximação:

1. Para cada SKU, identifiquei o período mais recente (entre os 4) em que ele teve `qtd_vendida > 0`.
2. Contei os dias entre o **fim** desse período e a data do snapshot de estoque (03/08/2026). Esse número é um **piso**: o SKU pode ter vendido em qualquer dia daquele período, então o valor real de "dias sem venda" pode ser maior, até o tamanho do próprio período.
3. Por isso, cada bucket abaixo tem uma faixa real possível, não um número exato. Uso o piso (mais otimista) para decidir em qual dos 7 buckets pedidos o SKU cai, e mostro a faixa completa ao lado.

| Cohort (último período com venda) | Piso (dias, usado para o bucket) | Teto real possível (dias) | Bucket usado |
|---|---|---|---|
| Vendeu em abr-jun/2026 (mais recente) | 34 | ~125 | 31 a 60 dias |
| Vendeu em jan-mar/2026 (não depois) | 125 | ~214 | 121 a 150 dias |
| Vendeu em nov-dez/2025 (não depois) | 215 | ~275 | Acima de 180 dias |
| Vendeu em mai-out/2025 (não depois) | 276 | ~459 | Acima de 180 dias |
| Nunca vendeu em nenhum dos 4 períodos | ≥ 459 (desde o início da janela observada) | Sem limite conhecido, pode ser mais antigo | Nunca vendeu (14 meses) |
| Não existe em nenhuma Curva ABC (SKU novo) | Não aplicável | Não aplicável | Sem histórico (SKU novo) |

**Consequência direta e importante:** com a granularidade dos relatórios disponíveis hoje (períodos de 2 a 6 meses, não corte mensal), os buckets "até 30 dias", "61 a 90 dias", "91 a 120 dias" e "151 a 180 dias" **não podem ser preenchidos com dado real nenhum**: nenhum piso calculável cai dentro dessas faixas, porque os 4 relatórios não têm um período que termine ali. Mantive as 7 linhas pedidas na tabela abaixo para respeitar o pedido, com essas 4 marcadas como estruturalmente vazias, não como "zero produtos parados" por engano de leitura.

Se o cliente puder exportar Curva ABC mensal (em vez de bimestral/trimestral/semestral) daqui pra frente, os buckets intermediários passam a ser calculáveis de verdade. Registrado como próximo passo.

### Limitações da fonte de dados
1. **Sem data de última venda por SKU**, ver metodologia acima. Todo bucket é uma faixa aproximada, não uma contagem exata de dias.
2. **Erros de cadastro já identificados foram considerados no valor de estoque, não no bucket de giro.** O giro (vendeu ou não vendeu) vem da Curva ABC, que não é afetada pelos outliers de custo/quantidade do snapshot de estoque. Os ajustes abaixo mudam só o valor em R$, não o bucket:
   - **Códigos 7153 (Cabo Flex 2,5mm Azul Cobrecom) e 7874 (Mangueira Corrugada 20mm Krona): excluídos inteiramente do ranking.** Quantidade cadastrada em forte desacordo com os pares da própria linha (79.263,9 PC e 164.736.600 MT, respectivamente), pendente de confirmação do Tony desde 03/08/2026, ver detalhe completo em `diagnostico-estoque.md`, seção "Atualização de Estoque: 03/08/2026".
   - **Código 11073 (Colorante Icores BA Amarelo P0411 0,9L): custo usado ajustado para R$ 0,15/ml** (mediana da linha, erro já confirmado pelo Tony em 23/07/2026, ainda sem correção no ERP em 03/08/2026), no lugar do R$ 158,67/ml cadastrado. Valor em estoque com o custo corrigido: R$ 680,89 (era R$ 720.244,40 ao custo cadastrado).
   - **Código 11022 (Sacolas 30x40 Imp): custo usado ajustado para R$ 0,225/un** (ponto médio da faixa R$ 0,15-0,30 já benchmarcada em `diagnostico-estoque.md` contra o item irmão da mesma família). Valor em estoque com o custo corrigido: R$ 451,13 (era R$ 23.378,30 ao custo cadastrado). **Confirmado pelo Tony em 26/08/2026 que essas sacolas são uso interno da loja (ensacar areia e brita), não mercadoria de revenda**, então giro zero é esperado, não deveria ser lido como estoque parado problemático.
   - **Código 3214 (Tubo PVC Rosca 1 pol Tigre): valor mantido ao custo cadastrado (R$ 8,06/pc, R$ 8.058,63 no total), sem correção.** O benchmark contra os pares da linha não resolve se o problema é o custo, o preço ou a quantidade cadastrada (999,83 PC, muito acima de qualquer par), então não há uma estimativa única confiável para substituir. Tony confirmou em 26/08/2026 que é produto de giro baixo, mas isso não resolve a dúvida de cadastro. Segue pendente de checagem direta.
   - **2 itens de Ativo Imobilizado com estoque positivo (triciclo de entrega, código 14160, R$ 26.000,40; notebook, código 9928, R$ 2.499,00) foram excluídos do ranking comercial**, mesmo critério já usado nos 4 períodos de Curva ABC (que excluem ativo imobilizado da análise comercial). Não são mercadoria de revenda.
   - **As confirmações do Tony de 26/08/2026 sobre Metalon 30x20, Torneira e Tela não foram aplicadas a nenhum código específico nesta rodada.** O contexto que originou esta análise já registrava os 3 como "item novo, ainda sem código/valor cruzado". Tentei cruzar por nome do produto e o resultado confirma por que isso ainda não tinha sido feito: "Metalon 30x20" não bate com nenhum SKU pelo formato de nome usado no cadastro (o produto mais próximo, código 14346, está grafado "METALON GALV 30MM X 20MM"); "Torneira" aparece em 103 SKUs distintos no catálogo (torneira de pia, de jardim, boia, reparo); "Tela" aparece em 32 SKUs de famílias bem diferentes (tela mosqueteiro, tela de galinheiro, fita telada, e até "CERÂMICA ... STELA", que não tem relação nenhuma com o item citado pelo Tony, apanhado só pela substring "tela" dentro do nome da marca). Aplicar a nota a um desses códigos por aproximação de nome seria inventar o cruzamento, não confirmá-lo. Fica como próximo passo perguntar ao Tony o código ou nome exato dos 3 itens antes de cruzar.
3. **Categoria corrompida no cadastro do cliente ("MD-MD-MD-...") segue afetando 2 dos 20 maiores itens desta lista** (Vareta Solda Oxi e Tubo PVC Rosca, ambos na tabela abaixo) **e outros itens mais abaixo no ranking completo da planilha** (ex: a Torneira código 8953, fora do top 20), mesma pendência já registrada em `diagnostico-estoque.md`, sem correção nova nesta rodada.
4. **Margem mostrada é markup sobre custo cadastrado no ERP** ((Preço − Custo Final) / Custo Final × 100), o mesmo campo "% Margem" do snapshot de estoque. Não é o mesmo cálculo de margem bruta % sobre venda usado nos períodos de Curva ABC (que é sobre faturamento real). Os dois não são comparáveis diretamente, mesma ressalva já registrada em `diagnostico-estoque.md`.
5. **68 SKUs novos** (criados depois de jun/2026, sem nenhuma Curva ABC que os cubra) entram como "sem histórico", não como "parado": não dá para saber se giram ou não ainda.

### Classificação de giro por bucket (dias sem venda, aproximado)
| Bucket solicitado | Faixa real possível (dias) | SKUs | Valor em estoque (ajustado) | % do total |
|---|---|---|---|---|
| Até 30 dias | Não populável com a granularidade atual (ver metodologia) | 0 | R$ 0,00 | 0,0% |
| 31 a 60 dias | 34 a ~125 dias | 1.888 | R$ 426.567,77 | 48,2% |
| 61 a 90 dias | Não populável com a granularidade atual (ver metodologia) | 0 | R$ 0,00 | 0,0% |
| 91 a 120 dias | Não populável com a granularidade atual (ver metodologia) | 0 | R$ 0,00 | 0,0% |
| 121 a 150 dias | 125 a ~214 dias | 536 | R$ 45.164,61 | 5,1% |
| 151 a 180 dias | Não populável com a granularidade atual (ver metodologia) | 0 | R$ 0,00 | 0,0% |
| Acima de 180 dias | 215 a ~459 dias (mistura dos 2 períodos mais antigos) | 619 | R$ 53.846,38 | 6,1% |
| Nunca vendeu (14 meses completos) | ≥ 459 dias dentro da janela observada, pode ser mais antigo | 1.733 | R$ 351.523,17 | 39,7% |
| Sem histórico (SKU novo, pós jun/2026) | Não aplicável | 68 | R$ 7.254,58 | 0,8% |
| **Total (mercadoria comercial, exclui outliers críticos e ativo imobilizado)** | | **4.844** | **R$ 884.356,51** | **100,0%** |

### Top 20 produtos por valor em estoque (ajustado)
Ordenado por valor de estoque a custo, já com os ajustes de cadastro da seção de limitações acima. Lista completa dos 4.844 SKUs na planilha (aba "Ranking por valor de estoque").

| Código | Produto | Categoria | Qtde. | Valor em estoque | Margem (markup s/ custo) | Bucket de giro |
|---|---|---|---|---|---|---|
| 1986 | Cumeeira Zincalum 0,43 | Material Básico | 2.998,00 un | R$ 77.948,00 | 57,69% | Nunca vendeu¹ |
| 51 | Areia Fina | Material Básico | 1.099,27 mt | R$ 77.861,16 | 83,53% | 31-60 dias |
| 3746 | Vareta Solda Oxi 1,59mm Gerdau | (categoria corrompida) | 7.329,00 un | R$ 74.755,80 | 145,10% | Nunca vendeu² |
| 1322 | Areia Média | Material Básico | 668,53 mt | R$ 47.351,67 | 83,53% | 31-60 dias |
| 92 | Pedra Britada 1 (19) | Material Básico | 190,96 mt | R$ 19.096,22 | 120,00% | 31-60 dias |
| 11024 | Sacola Recicladas VD 60x80 | Material de Uso e Consumo | 1.015,00 kg | R$ 11.672,50 | 73,91% | Nunca vendeu |
| 98 | Pedra Britada 0 (Cascalhinho) | Material Básico | 105,16 mt | R$ 11.216,89 | 125,00% | 31-60 dias |
| 3214 | Tubo PVC Rosca 1 pol Tigre | (categoria corrompida) | 999,83 pc | R$ 8.058,63 | 1.091,07%³ | Nunca vendeu³ |
| 7972 | Cimento Poty CPII Z 32 50kg | Material Básico | 174,00 sc | R$ 6.650,28 | 33,44% | 31-60 dias |
| 2791 | Treliça Premoldada TG8 SL 6/3 x 4/4.2mm | Material Básico | 595,30 mt | R$ 6.548,30 | 100,00% | 31-60 dias |
| 11225 | Saco de Areia Impresso 40x60 | Material de Uso e Consumo | 8.138,00 un | R$ 5.533,84 | 196,30% | 31-60 dias |
| 1344 | Telha Canal Tipo Russa 2ª | Cobertura | 5.585,10 un | R$ 5.194,14 | 50,54% | 31-60 dias |
| 87 | Pedra Calcária | Material Básico | 73,17 mt | R$ 4.878,58 | 275,00% | 31-60 dias |
| 15847 | Sacos Ráfia de PP 50x63 Lam Construmais | Utilidades e Jardim | 5.334,00 un | R$ 4.747,26 | 124,72% | 31-60 dias |
| 167 | Telha Canal Tipo Russa 1ª | Cobertura | 4.324,00 un | R$ 4.151,04 | 45,83% | 31-60 dias |
| 13801 | Tela Moeda Ferro 1,90cm | Material Básico | 89,00 mt | R$ 3.945,41 | 71,45% | Acima de 180 dias |
| 147 | Coluna Ferro 5/16 8,00mm 07x17 | Material Básico | 297,50 mt | R$ 3.671,15 | 78,35% | 31-60 dias |
| 11693 | Abraçadeira Nylon BR 140x3,50 Foxlux | Ferragem | 59.400,02 un | R$ 3.564,00 | 150,00% | 31-60 dias |
| 148 | Coluna Ferro 3/8 10,00mm 07x17 | Material Básico | 211,00 mt | R$ 3.542,69 | 78,73% | 31-60 dias |
| 15800 | Cerâmica 46x46 Br.Neve Ext 2,79m² Stela | Cerâmica | 225,99 m² | R$ 3.527,70 | 110,77% | 31-60 dias |

¹ Cumeeira Zincalum: vendida por encomenda, confirmado pelo Tony em 26/08/2026. Giro zero é o esperado para esse item, não deve ser lido como estoque parado problemático.
² Vareta: confirmado pelo Tony em 26/08/2026 como slow-mover genuíno (item de baixo giro real, não erro de leitura).
³ Tubo PVC Rosca: markup de 1.091% é implausível frente aos pares da mesma linha (66% a 102%), mas a causa (custo, preço ou quantidade cadastrada) segue não resolvida, ver limitação 2 acima. Tony confirmou em 26/08/2026 que é item de giro baixo, sem resolver a dúvida de cadastro.

Nota: o código 13801 ("Tela Moeda Ferro") é um dos 32 SKUs com "tela" no nome do catálogo. A confirmação do Tony sobre "Tela" em 26/08/2026 não foi aplicada a ele nem a nenhum outro código específico, ver limitação 2 acima. As 3 cerâmicas da marca "Stela" no topo desta lista (linha acima e as duas seguintes na planilha completa) não têm relação com essa confirmação, apesar do nome da marca conter a substring "tela".

### Recomendação de ação por bucket
Recomendação por faixa de giro, sem decidir preço final nem promoção (isso é decisão do `@copywriter`/`@gestor-trafego`/cliente):
- **31 a 60 dias (48,2% do valor, R$ 426.567,77):** giro mais recente do grupo, mas o piso de 34 dias pode mascarar item que na verdade só vendeu uma vez lá no início do trimestre (teto real de ~125 dias). Não tratar como "estoque saudável" sem checar caso a caso os itens de maior valor desta faixa.
- **121 a 150 dias (5,1%, R$ 45.164,61) e Acima de 180 dias (6,1%, R$ 53.846,38):** candidatos a ação de desova ou campanha de giro, junto com `@gestor-trafego`, antes de virar estoque parado de fato.
- **Nunca vendeu em 14 meses (39,7%, R$ 351.523,17):** maior bloco de risco. Descontando os 4 itens já confirmados por código específico com o Tony como "não deveria mesmo girar ou já é perda conhecida" (Cumeeira Zincalum R$ 77.948,00, Vareta Solda Oxi R$ 74.755,80, Sacolas 30x40 R$ 451,13 já corrigido, Tubo PVC Rosca R$ 8.058,63, somando R$ 161.213,56, 45,9% deste bloco), ainda sobra R$ 190.309,61 (54,1%) sem explicação qualitativa cruzada por código, candidato a checagem item a item com o Tony ou a entrar em campanha de liquidação. As confirmações sobre Metalon 30x20, Torneira e Tela existem, mas não puderam ser somadas aqui por falta de cruzamento confiável com um código (ver limitação 2 acima).
- **Sem histórico (0,8%, R$ 7.254,58):** SKUs novos, sem ação de giro ainda, só observação daqui pra frente.

### Comparação com o período/snapshot anterior
Primeira seção deste arquivo, sem comparação anterior própria. Para contexto, `diagnostico-estoque.md` já registrava R$ 373.769,46 de estoque parado (1.732 SKUs) para o mesmo snapshot de 03/08/2026, usando o critério mais estrito de "nunca vendeu nos 4 períodos". A diferença para o R$ 351.523,17 aqui (1.733 SKUs) vem da correção adicional de custo do item Sacolas 30x40 (não aplicada naquela rodada), não de uma mudança de critério.

### Próximos passos
1. Pedir ao Tony o código ou nome exato de produto para Metalon 30x20, Torneira e Tela (confirmações de 26/08/2026 que não puderam ser cruzadas por código, ver limitação 2), e confirmar com ele os demais itens do bloco "nunca vendeu" que ainda não têm nota qualitativa registrada, priorizando por valor em estoque na planilha.
2. Resolver a dúvida de cadastro do Tubo PVC Rosca 1 pol (código 3214): qual campo está errado, custo, preço ou quantidade.
3. Cobrar de novo a correção do colorante (código 11073) e dos 2 outliers críticos (7153, 7874) no ERP, pendências já registradas em `diagnostico-estoque.md`.
4. Se possível, pedir ao Tony exportação de Curva ABC em corte mensal daqui pra frente: resolve a lacuna dos buckets 30/90/120/180 que hoje não podem ser calculados com a periodização atual.
5. `@gestor-trafego`/`@copywriter` podem usar o bloco "121 a 150 dias" e "Acima de 180 dias" (R$ 99.010,99 somados) como lista de candidatos a campanha de giro/desova, e o bloco "31 a 60 dias" como referência do que não precisa de reforço promocional agora.
6. Avaliar com o usuário se vale migrar formalmente o conteúdo histórico de `diagnostico-estoque.md` para a estrutura dividida (`diagnostico-curva-abc.md` + o restante deste arquivo), como tarefa separada.

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
