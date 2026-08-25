# Detalhe de SKU, categoria Ferramentas (e complemento Ferragem), para Kit Dia dos Pais

**Fonte dos dados:** os mesmos 5 arquivos originais do diagnóstico de estoque de 2026-07-23, localizados em `Diagnóstico Tony - Construmais/Arquivos/` fora da pasta do workspace: `Curva ABC parte 1.pdf` (01/05/2025 a 31/10/2025), `Curva ABC parte 2.pdf` (01/11/2025 a 31/12/2025), `Curva ABC parte 3.pdf` (01/01/2026 a 31/03/2026), `Curva ABC parte 4.pdf` (01/04/2026 a 30/06/2026) e `Estoque ETL.xlsx` (aba "Estoque", 15.228 linhas).

**Metodologia:** Pilar 1, Inteligência de Dados, Método Viga Mestra. Este arquivo é um recorte de aprofundamento do `outputs/07-2026/23-diagnostico-estoque.md` (que já traz giro/margem agregados de Ferramentas: 5,17% do faturamento, margem bruta média 46,20%), agora aberto em nível de SKU individual para dar suporte à campanha de Dia dos Pais com kits com ferramentas.

**Status:** v1, sujeito a refinamento.

## Nota de metodologia (leia antes de usar os números)

O diagnóstico original foi produzido com um script de extração próprio. Nesta sessão, sem acesso a esse script, refiz a extração com outra ferramenta (`pdftotext -table`, do pacote poppler/xpdf, que já entrega as colunas do relatório de Curva ABC alinhadas por posição, mais robusto que o modo `-layout` usado antes) e um parser próprio em Perl para reconstruir cada linha de produto (código, produto, unidade, quantidade vendida, custo total, venda total, margem) nas 4 partes da Curva ABC, cruzado por código com a coluna "Grupo" da planilha `Estoque ETL.xlsx` para isolar os produtos de Ferramentas (2.227 códigos cadastrados) e Ferragem (1.753 códigos cadastrados).

**Checagem de consistência com o diagnóstico anterior (validação cruzada, não coincidência):**
- Faturamento agregado de Ferramentas nesta extração: R$ 157.585,70, margem bruta 46,22%. Valor do diagnóstico original: R$ 157.405,62, margem 46,20%. Diferença de R$ 180,08 (0,11% do total), dentro da margem de cobertura já documentada no diagnóstico original (96,5% a 98,8% de cobertura linha a linha por período).
- Faturamento agregado de Ferragem nesta extração: R$ 151.093,13, margem bruta 49,27%, batendo exatamente com o valor do diagnóstico original.
- Os 2 produtos de Ferramentas já citados no ranking geral do diagnóstico original batem com exatidão nesta extração: Lixa Massa G120 A257 Norton (918 un, margem 66,79%) e Disco de Corte 4.1/2X3/64X7/8 Starrett (601 un, margem 61,20%).
- Os 3 primeiros produtos de Ferragem do ranking geral também batem com exatidão: Parafuso Auto Broc Zinc 12x1 Jomarca (13.027 un, R$ 6.016,20, margem 52,02%) e Bucha Nylon 08 Fixaforte (4.133 un, R$ 1.036,61, margem 67,00%).

Essa checagem cruzada dá confiança de que o método de extração está correto e comparável ao diagnóstico original, mesmo usando ferramenta diferente.

**Limitações específicas desta extração:**
1. Cobertura de linhas: dos 15.228 códigos por período, o parser reconstrói com sucesso a linha completa (produto + números) para aproximadamente 2.100 a 2.550 códigos por período de 2 a 3 meses (Partes 2 a 4) e aproximadamente 15.154 de 15.156 candidatos na Parte 1 (5 meses, formato de relatório mais simples). A maior parte dos códigos "perdidos" nas Partes 2 a 4 são itens sem nenhuma venda no período (campos em branco no relatório), o que não afeta os rankings de giro e margem deste arquivo, já que um item sem venda não entraria no ranking de qualquer forma.
2. Diferente do diagnóstico original, não fiz aqui uma auditoria específica de produtos de Ferramentas cadastrados em mais de um código (o problema documentado antes foi em dois tipos de cimento, categoria Material Básico). Não posso descartar que algum SKU de Ferramentas tenha o mesmo problema (por exemplo, o mesmo modelo de disco de corte comprado de lotes diferentes), o que faria o giro real de um produto específico ficar subestimado no ranking abaixo. Sinalizo isso como possível refinamento futuro, não verifiquei código a código.
3. Todos os valores abaixo somam os 14 meses completos (4 períodos), exatamente como no diagnóstico original.

## Participação de Ferramentas no total (contexto, do diagnóstico original)

Ferramentas responde por R$ 157.405,62 (5,17% do faturamento total da loja em 14 meses), margem bruta média de 46,20%, a segunda maior margem percentual entre todas as categorias da loja (atrás só de Ferragem, 49,27%). De 2.227 SKUs cadastrados em Ferramentas, 1.008 (45,3%) tiveram pelo menos uma venda nos 14 meses. Os demais 1.219 SKUs (54,7%) não venderam nada no período, consistente com o achado geral de estoque parado do diagnóstico original.

## Top 15 produtos de Ferramentas por giro (quantidade vendida, 14 meses)

| # | Produto | Unidade | Qtde. vendida | Faturamento | Margem % |
|---|---|---|---|---|---|
| 1 | Lixa Massa G120 A257 Norton | UN | 918 | R$ 1.371,40 | 66,79% |
| 2 | Disco Corte 4.1/2X3/64X7/8 Starrett | UN | 601 | R$ 2.400,66 | 61,20% |
| 3 | Disco Corte 7X1/16X7/8 Starrett | UN | 319 | R$ 2.549,86 | 46,12% |
| 4 | Lixa Massa G080 A257 Norton | UN | 290 | R$ 578,97 | 65,19% |
| 5 | Lixa Massa G180 A257 Norton | UN | 272 | R$ 407,92 | 66,47% |
| 6 | Luva Malha PT 4 Fios Pigmentada PT Imbat | UN | 254 | R$ 1.266,94 | 56,49% |
| 7 | Rebite Alum 5.0X14MM Waves Plus | UN | 245 | R$ 73,56 | 56,70% |
| 8 | Lixa Massa G100 A257 Norton | UN | 229 | R$ 342,87 | 61,26% |
| 9 | Lâmina Serra 300MM 12 Bimetal BS1218 18D Starrett | UN | 222 | R$ 3.109,50 | 47,83% |
| 10 | Lixa Massa G150 A257 Norton | UN | 209 | R$ 313,92 | 65,03% |
| 11 | Corda Ecológica Seda 8MM VD Pratk | MT | 206 | R$ 412,00 | 59,00% |
| 12 | Lápis Mad Carpinteiro 18CM Irwin | UN | 172 | R$ 515,38 | 54,75% |
| 13 | Máscara Desc S/Válvula P2 PFF2 Plastcor | UN | 156 | R$ 623,88 | 78,20% |
| 14 | Lixa Massa G120 230U 3M | UN | 151 | R$ 227,88 | 65,54% |
| 15 | Máscara Desc C/Válvula P1 Plastcor | UN | 151 | R$ 755,00 | 73,33% |

Leitura: os itens de maior giro dentro de Ferramentas são, em sua maioria, consumíveis de baixo ticket unitário (lixa, disco de corte, EPI descartável). Isso confirma o padrão já visto na categoria Ferragem no diagnóstico original (giro alto puxado por itens de reposição de obra, não por ferramenta em si), e reforça por que este recorte específico de SKU era necessário: o giro por si só não aponta produto com apelo de presente.

## Top 8 produtos de Ferramentas por margem bruta absoluta (R$, 14 meses)

| # | Produto | Unidade | Qtde. vendida | Faturamento | Margem R$ | Margem % |
|---|---|---|---|---|---|---|
| 1 | Carro de Mão 65L Extra Forte Tramontina | UN | 21 | R$ 9.230,00 | R$ 3.607,27 | 39,08% |
| 2 | Disco Diamant Turbo Porc 110MM 60863 Cortag | UN | 110 | R$ 4.645,55 | R$ 2.306,12 | 49,64% |
| 3 | Lâmina Serra 300MM 12 Bimetal BS1218 18D Starrett | UN | 222 | R$ 3.109,50 | R$ 1.487,16 | 47,83% |
| 4 | Disco Corte 4.1/2X3/64X7/8 Starrett | UN | 601 | R$ 2.400,66 | R$ 1.469,11 | 61,20% |
| 5 | Eletrodo 3.25MM KG E6013 Gerdau | KG | 120,55 | R$ 3.629,00 | R$ 1.328,24 | 36,60% |
| 6 | Disco Corte 7X1/16X7/8 Starrett | UN | 319 | R$ 2.549,86 | R$ 1.176,12 | 46,12% |
| 7 | Lixa Massa G120 A257 Norton | UN | 918 | R$ 1.371,40 | R$ 915,90 | 66,79% |
| 8 | Bota Couro P/Const Bico PVC 39 Vulcaflex | UN | 21 | R$ 1.905,38 | R$ 792,90 | 41,61% |

Achado principal desta tabela: **Carro de Mão 65L Extra Forte Tramontina é o único item de Ferramentas com ticket unitário alto (R$ 439,52 em média) que também é o maior gerador de margem absoluta da categoria inteira**, à frente até de itens de giro muito mais alto. É o produto mais próximo de um "candidato natural" a âncora de kit de ticket elevado dentro de Ferramentas.

## Produtos de ticket mais alto (não consumível): o que existe e o que não vende

O pedido era verificar se existe, dentro de Ferramentas, algum item de ticket mais alto com apelo de presente (furadeira, parafusadeira, kit manual, trena, nível, martelo etc.), separado do consumível de obra. A resposta é mista, e é importante ser direto sobre isso:

### O que tem venda real e ticket relevante

| Grupo de produto | SKUs cadastrados | SKUs com venda em 14 meses | Total vendido | Faturamento | Margem bruta |
|---|---|---|---|---|---|
| Carro de Mão (carrinho de obra) | 22 | 8 | 43 un | R$ 12.633,62 | 39,71% |
| Trena | 31 | 13 | 148 un | R$ 3.894,56 | 46,36% |
| Alicate | 45 | 12 | 69 un | R$ 2.986,71 | 46,00% |
| Marreta | 16 | 8 | 29 un | R$ 1.851,38 | 45,81% |
| Furadeira (elétrica) | 12 | 6 | 9 un | R$ 1.905,03 | 38,90% |
| Enxada | 16 | 6 | 48 un | R$ 2.081,95 | 43,44% |
| Martelo | 42 | 15 | 48 un | R$ 1.688,22 | 44,37% |
| Nível (bolha) | 30 | 5 | 30 un | R$ 1.152,08 | 46,40% |

Nota: "Carro de Mão" acima inclui 5 modelos completos vendidos (65L Tramontina, 45L Maestro, 60L Thor, 45L chapa 26 e 45L chapa 22) mais alguns itens de reposição (eixo, aro, pneu avulso), que não têm apelo de presente e devem ficar de fora de qualquer composição de kit.

### O que existe no catálogo mas praticamente não vende

Parafusadeira e Esmerilhadeira, os dois tipos de ferramenta elétrica de maior ticket potencial no catálogo (preço de tabela entre R$ 250 e R$ 700), **têm zero unidades vendidas em 14 meses completos**, em todos os SKUs cadastrados (4 modelos de parafusadeira, 6 modelos de esmerilhadeira/lixadeira elétrica). Furadeira elétrica vende, mas em volume muito baixo: 9 unidades no total, espalhadas em 6 modelos diferentes (1 a 2 unidades por modelo), o que não sustenta esses modelos como âncora de giro comprovado, só como produto de catálogo com movimento esporádico.

Isso significa: **não há, hoje, uma ferramenta elétrica de ticket alto com giro comprovado o suficiente para ancorar um kit com segurança de dado**. O candidato de ticket alto com giro real é o Carro de Mão, e o candidato de ticket médio com giro mais distribuído é o conjunto de ferramentas manuais (trena, alicate, martelo, nível, marreta, enxada).

## Complemento em Ferragem (top 10 por giro, para referência de kit)

Os itens abaixo já apareciam de forma agregada no diagnóstico original; aqui estão isolados para referência de composição de kit, todos confirmados batendo com exatidão contra o diagnóstico original.

| # | Produto | Qtde. vendida | Faturamento | Margem % |
|---|---|---|---|---|
| 1 | Parafuso Auto Broc Zinc 12x1 Jomarca | 13.027 un | R$ 6.016,20 | 52,02% |
| 2 | Bucha Nylon 08 Fixaforte | 4.133 un | R$ 1.036,61 | 67,00% |
| 3 | Bucha Nylon 06 Fixaforte | 2.217 un | R$ 333,00 | 60,05% |
| 4 | Bucha Nylon 10 Fixaforte | 1.945 un | R$ 972,99 | 62,02% |
| 5 | Arruela Lisa Zinc 3/16 Jomarca | 1.779 un | R$ 282,59 | 65,47% |
| 6 | Parafuso PH CB Chata BC 4.0x20 Jomarca | 1.638 un | R$ 246,91 | 75,25% |
| 7 | Parafuso PH CB Chata BC 4.0x40 Jomarca | 1.553 un | R$ 310,79 | 63,41% |
| 8 | Bucha Nylon 08 C/Anel Fixaforte | 1.522 un | R$ 610,86 | 65,12% |
| 9 | Arruela Lisa Zinc 1/4 Enerlux | 1.319 un | R$ 396,86 | 56,79% |
| 10 | Porca SX Zinc UNC 1/4 Jomarca | 1.310 un | R$ 264,29 | 55,39% |

Ferragem tem margem bruta ainda mais alta que Ferramentas (49,27% agregada) e um giro muito maior nos itens de fixação, mas ticket unitário baixíssimo (parafuso e bucha são vendidos por unidade ou pacote pequeno). Faz sentido como "brinde de baixo custo dentro do kit" (parafuso/bucha não é presente, mas reforça a percepção de kit completo), não como âncora.

## Leitura para composição de kit Dia dos Pais (racional, não decisão de preço)

Com os dados acima, duas composições fazem sentido pela mesma lógica já usada nos outros 10 kits do arquivo de estratégia (âncora com dado real + complemento que fecha a experiência), mas aqui adaptada para o ângulo de presente, não de obra:

1. **Kit Reforma (ticket mais alto):** Carro de Mão 65L Extra Forte Tramontina como âncora, é o único item de Ferramentas que combina ticket relevante (R$ 439,52 médio) com margem absoluta comprovada (R$ 3.607,27 em 14 meses, a maior da categoria) e giro real, ainda que baixo (21 unidades, mas concentrado num único modelo, sinal de preferência de mercado já validada). Complementar com um item de proteção de giro alto e margem alta da própria Ferramentas, como a Luva Malha PT 4 Fios Pigmentada Imbat (254 un vendidas, margem 56,49%), formando o par funcional "quem carrega material de carro de mão usa luva". Isso segue a mesma lógica de "âncora de ticket/margem mais complemento de giro" já usada no Kit Cobertura e no Kit Impermeabilização do arquivo de estratégia.

2. **Kit Ferramenta Manual (ticket de entrada, apelo de presente clássico):** como não existe uma única ferramenta manual com giro dominante dentro da categoria (ao contrário do Tijolo ou do Cimento no restante do catálogo), a composição aqui precisa reunir 2 a 3 itens complementares que juntos formam a imagem de "kit de ferramentas do pai": Trena (item de maior giro agregado do grupo, 148 un, margem 46,36%) mais Martelo ou Alicate (ambos com giro distribuído em vários modelos e margem semelhante, ao redor de 44% a 46%). Nenhum dos três tem giro que sustente sozinho um kit, mas juntos cobrem o consumível de obra de cada categoria e dão volume de opção de composição ao vendedor montar o kit conforme o que tiver em estoque no momento (útil, já que a maior parte dos SKUs individuais de trena/martelo/alicate vende só 1 a 5 unidades por modelo ao longo de 14 meses).

Fica de fora, por falta de dado que sustente, qualquer composição ancorada em furadeira, parafusadeira ou esmerilhadeira: são os itens de ticket mais alto do catálogo de Ferramentas, mas com giro perto de zero, e um kit apoiado neles corre risco de ficar parado se a demanda não mudar. Se a Pillar ou o Tony quiserem seguir com esse ângulo mesmo assim (furadeira tem apelo de presente forte, é o clássico "presente de Dia dos Pais"), a decisão precisa ser tratada como aposta comercial deliberada, não como algo respaldado por giro histórico, e o preço/margem final de qualquer composição continua sendo decisão do `@copywriter`, do `@gestor-trafego` ou do próprio cliente, não deste diagnóstico.

## Próximos passos

1. `@copywriter` pode usar as duas composições acima (Kit Reforma e Kit Ferramenta Manual) como ponto de partida para copy de oferta de Dia dos Pais, decidindo preço, desconto e nome final do kit.
2. Se a Pillar decidir seguir com o ângulo de furadeira/parafusadeira mesmo com giro baixo, recomendo tratar como teste controlado (poucas unidades, sem grande investimento de mídia), já que não há histórico de venda que sustente a demanda.
3. Confirmar com o Tony se algum modelo de ferramenta manual (trena, martelo, alicate) tem código duplicado por lote de compra, como aconteceu com o cimento no diagnóstico original. Não verifiquei isso especificamente para Ferramentas nesta rodada.
4. Este arquivo não altera nenhum número do diagnóstico original (`outputs/07-2026/23-diagnostico-estoque.md`) nem do `CLIENTE.md`, é um aprofundamento pontual da categoria Ferramentas para viabilizar o pedido de campanha.
