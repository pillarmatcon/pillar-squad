# Desova Black Friday: base de estoque limpa - Construmais

**Cliente:** Construmais (Tony Carvalho Barbosa), João Pessoa/PB
**Objetivo:** definir o pool real de estoque para acelerar na Black Friday, descontando o que já foi confirmado como não problemático
**Fonte:** `08-2026/Arquivos/26-inteligencia-dados-giro-estoque-por-bucket_2026-08-03.xlsx` (snapshot de 03/08/2026), `_diagnosticos/inteligencia-dados/diagnostico-giro-estoque.md`, `09-2026/Analises/15-inteligencia-dados-cruzamento-margem-meta-viabiliza.md`
**Status:** v1, sujeito a validação do Tony. O snapshot tem 3 meses, o estoque atual pode ter mudado.

## Correções que invalidam o documento de agosto

`08-2026/Analises/11-combo-de-produtos-estrategia-desova-estoque-parado.md` está desatualizado nestes pontos:

- **Cumeeira Zincalum (R$ 77.948,00):** vendida por encomenda (Tony, 26/08/2026). Não é estoque parado. Fora da desova, e o Kit Cobertura Completa perde a âncora.
- **Vareta Solda Oxi (R$ 74.755,80):** erro de cadastro. O item deveria estar cadastrado em kg e foi cadastrado em unidade, então a quantidade (7.329) e o valor são irreais, o item vale centavos. Fora da desova e fora de qualquer cálculo de estoque. O Kit Cerca e Portão perde a Vareta. Correção informada pelo usuário em 08/11/2026, **o diagnóstico e a planilha ainda dizem "slow-mover genuíno" e precisam ser corrigidos.**
- **Sacolas 30x40:** uso interno da loja, não é revenda (o doc antigo citava R$ 23.378,30, a planilha auditada traz R$ 451,12).
- **Tubo PVC Rosca 1 pol (R$ 8.058,63):** giro baixo confirmado, mas com dúvida de cadastro (preço R$ 96 contra custo R$ 8,06). Fora até o cadastro ser checado.
- **Material de Uso e Consumo (R$ 31.167 sem as sacolas 30x40):** sacola, bobina, boné, celular, gôndola. Não é mercadoria de revenda, é decisão operacional do Tony.
- **Tela Moeda Ferro 1,90cm (R$ 3.945,41):** o Tony deixou o estoque em consignação na loja de um amigo (informado em 08/11/2026). Não está disponível na Construmais, então sai da desova e da lista de destaques.
- **Forro PVC Liso (R$ 670,11):** vendeu tudo (informado em 08/11/2026). Sai da desova.
- **Linha Mista 3x6 (código 461, R$ 2.261,29):** o Tony informou que a Construmais não vende mais esse item (08/11/2026). Fica fora do pool até esclarecer se o saldo físico existe e se ele topa queimar (ver tabela de conferência).
- **Colorantes Icores (R$ 5.224 em 9 itens):** insumo do sistema tintométrico, estoque em ml a centavos. Não é produto de prateleira.

## Pool real para a Black Friday

| Bloco | Valor a custo | SKUs |
|---|---|---|
| "Nunca vendeu em 14 meses" no total (planilha) | R$ 351.523 | 1.724 |
| Menos itens acima (cumeeira, vareta, tubo, sacola 30x40, colorante 11073, uso e consumo, outros colorantes) | - R$ 198.286 | - |
| "Nunca vendeu" limpo | ~R$ 153.200 | ~1.639 |
| "121 a 150 dias" + "Acima de 180 dias" (limpo, sem Tela Moeda, Forro PVC e Linha Mista) | ~R$ 92.100 | ~1.151 |
| **Pool real** | **~R$ 245.400** | **2.790** |

O pool a preço de tabela vale cerca de R$ 470 mil, ou seja, a margem cadastrada permite desconto real.

## Concentração: o pool é uma cauda longa

| Faixa | Valor a custo |
|---|---|
| 20 maiores SKUs | R$ 26.905 (11,0%) |
| 50 maiores | R$ 44.837 (18,3%) |
| 100 maiores | R$ 65.945 (26,9%) |
| 200 maiores | R$ 96.261 (39,2%) |

Os 20 maiores itens são pequenos: nenhum passa de R$ 4 mil. Isso muda a lógica de mídia: a Black Friday não se resolve com 1 ou 2 kits âncora, precisa de oferta ampla (vitrine de ofertas, balcão, WhatsApp) mais destaque pago em poucos itens.

## Categorias do pool

| Categoria | Valor a custo | SKUs | Valor a preço de tabela |
|---|---|---|---|
| Ferragem | R$ 36.999 | 515 | R$ 73.810 |
| Ferramentas | R$ 33.015 | 473 | R$ 60.776 |
| Hidráulica | R$ 31.315 | 401 | R$ 58.835 |
| Pintura | R$ 25.997 | 196 | R$ 42.496 |
| Cadastro corrompido "MD-MD-MD..." | R$ 23.683 | 439 | R$ 45.426 |
| Material Elétrico | R$ 21.374 | 271 | R$ 64.315 |
| Utilidades e Jardim | R$ 16.385 | 171 | R$ 28.880 |
| Material Básico | R$ 10.378 | 36 | R$ 17.817 |
| Cobertura | R$ 6.530 | 23 | R$ 11.139 |
| Esquadrias | R$ 9.087 | 32 | R$ 15.306 |

## Itens aprovados pelo Tony para promoção

Em 09/11/2026 o Tony respondeu à lista de candidatos de destaque: **só estes três podem entrar** na promoção.

| Código | Produto | Qtde | Custo un. | Preço | Valor a custo | A preço de tabela | Markup cadastrado |
|---|---|---|---|---|---|---|---|
| 15525 | Bacia p/ Caixa Acoplada Izy Conforto Deca | 3 | R$ 527,27 | R$ 770 | R$ 1.582 | R$ 2.310 | 46% |
| 10442 | Porcelanato Bali Polido 61x61 (cx 1,88 m²) | 30,1 cx | R$ 48,84 | R$ 70 | R$ 1.469 | R$ 2.107 | 43% |
| 11611 | Kit Aço Cacau 40 Cozimax | 4 | R$ 342,51 | R$ 400 | R$ 1.370 | R$ 1.600 | 17% |
| | **Total** | | | | **R$ 4.421** | **R$ 6.017** | |

**Leitura:**
- O destaque aprovado é pequeno: R$ 4.421 a custo, cerca de 1,8% do pool de ~R$ 245 mil. A Black Friday não se sustenta nesses três itens, o grosso continua sendo oferta ampla (balcão, WhatsApp, vitrine) sobre o restante do pool, que ainda não passou pela validação do Tony.
- O Kit Aço Cacau tem markup de só 17%, pouco espaço para desconto. Qualquer desconto precisa ser calculado antes de ir para a peça.
- A Bacia Deca pede a Caixa Acoplada (código 15526, R$ 843,24 a custo, 3 un, preço R$ 430). Ela não estava na lista enviada ao Tony, então não sei se também está apta. Perguntar antes de montar o par.
- Os outros candidatos da lista (Metalon, Torneira Imperatriz, Madeirite, Tela Alambrado e Rebocal) ficam como **não aptos a promoção** por decisão do Tony. Não sei o motivo de cada um e não vou presumir. Com isso, caem também os pares de kit Metalon + Tela Alambrado e Telhas PVC + Linha Mista.
- O alerta de estoque zerado do Metalon deixa de importar para a campanha.

## Tabela de conferência com o Tony

Atualizada à medida que o Tony responde.

| Código | Produto | Valor a custo | Situação | Data | Observação |
|---|---|---|---|---|---|
| 1986 | Cumeeira Zincalum 0,43 | R$ 77.948,00 | Fora: encomenda | 26/08/2026 | Confirmado pelo Tony |
| 3746 | Vareta Solda Oxi | R$ 74.755,80 | Fora: erro de cadastro (kg lançado em un) | 08/11/2026 | Informado pelo usuário |
| 13801 | Tela Moeda Ferro 1,90cm | R$ 3.945,41 | Fora: consignação em loja de amigo | 08/11/2026 | Tony |
| 14393 | Forro PVC Liso | R$ 670,11 | Fora: vendeu tudo | 08/11/2026 | Tony |
| 461 | Linha Mista 3x6 | R$ 2.261,29 | Fora do pool: não vende mais | 08/11/2026 | Pendente: ainda tem saldo físico? Topa queimar? |
| 14346 | Metalon Galv 30x20 Ch18 | R$ 2.943,39 | Fora da promoção: não apto | 09/11/2026 | Tony, sem motivo informado |
| 8953 | Torneira Met Filtro Imperatriz | R$ 2.599,56 | Fora da promoção: não apto | 09/11/2026 | Tony, sem motivo informado |
| 15511 | Madeirite Plastificado 18mm | R$ 2.220,00 | Fora da promoção: não apto | 09/11/2026 | Tony, sem motivo informado |
| 16124 | Tela Alambrado Prática | R$ 2.130,00 | Fora da promoção: não apto | 09/11/2026 | Tony, sem motivo informado |
| 2540 | Rebocal Multiuso Mibra 20kg | R$ 1.746,60 | Fora da promoção: não apto | 09/11/2026 | Tony, sem motivo informado |
| 15525 | Bacia p/ Caixa Acoplada Deca | R$ 1.581,81 | **Apto a promoção** | 09/11/2026 | Tony |
| 10442 | Porcelanato Bali Polido 61x61 | R$ 1.469,11 | **Apto a promoção** | 09/11/2026 | Tony |
| 11611 | Kit Aço Cacau 40 Cozimax | R$ 1.370,04 | **Apto a promoção** | 09/11/2026 | Tony |
| 15526 | Caixa Acoplada Duo Izy Deca | R$ 843,24 | Pendente | - | Par da Bacia, não estava na lista |
| 5634 | Linha Massaranduba 3x6 | R$ 691,20 | Pendente | - | Mesma família da Linha Mista, perguntar se também saiu de linha |

## Pendências antes de virar plano

1. Tony valida item a item os 50 a 100 maiores do pool (encomenda, erro de cadastro, desova real). O Bloco 2 do cruzamento de setembro já pedia isso.
2. Corrigir a Vareta no ERP e registrar a correção em `diagnostico-estoque.md`, `diagnostico-giro-estoque.md` e na planilha (hoje dizem "slow-mover genuíno").
3. Corrigir o cadastro do Tubo PVC Rosca e da categoria "MD-MD-MD...".
4. Nova exportação de estoque e Curva ABC do Pontual para atualizar o snapshot de agosto antes da campanha.
5. Definir com o Tony: desconto máximo, orçamento extra de mídia para novembro, datas da campanha.

---

Sem Humanizer final: rascunho de análise de dados, ainda sem copy.
