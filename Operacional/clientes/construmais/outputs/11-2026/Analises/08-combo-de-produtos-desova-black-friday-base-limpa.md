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
- **Colorantes Icores (R$ 5.224 em 9 itens):** insumo do sistema tintométrico, estoque em ml a centavos. Não é produto de prateleira.

## Pool real para a Black Friday

| Bloco | Valor a custo | SKUs |
|---|---|---|
| "Nunca vendeu em 14 meses" no total (planilha) | R$ 351.523 | 1.724 |
| Menos itens acima (cumeeira, vareta, tubo, sacola 30x40, colorante 11073, uso e consumo, outros colorantes) | - R$ 198.286 | - |
| "Nunca vendeu" limpo | ~R$ 153.200 | ~1.639 |
| "121 a 150 dias" + "Acima de 180 dias" (sem uso e consumo, Tela Moeda e Forro PVC) | ~R$ 94.400 | ~1.152 |
| **Pool real** | **~R$ 247.600** | **2.791** |

O pool a preço de tabela vale cerca de R$ 473 mil, ou seja, a margem cadastrada permite desconto real.

## Concentração: o pool é uma cauda longa

| Faixa | Valor a custo |
|---|---|
| 20 maiores SKUs | R$ 28.393 (11,5%) |
| 50 maiores | R$ 46.606 (18,8%) |
| 100 maiores | R$ 67.836 (27,4%) |
| 200 maiores | R$ 98.262 (39,7%) |

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
| Cobertura | R$ 8.791 | 24 | R$ 14.649 |
| Esquadrias | R$ 9.087 | 32 | R$ 15.306 |

## Candidatos mais fortes para destaque (a validar com o Tony)

Itens de ticket mais alto, com preço de tabela acima de R$ 100, que justificam um anúncio ou um destaque individual. Os 416 SKUs com preço de tabela de R$ 100 ou mais somam R$ 96.589 a custo, 39% do pool.

| Código | Produto | Qtde | Custo un. | Preço | Valor a custo |
|---|---|---|---|---|---|
| 14346 | Metalon Galv 30x20 Ch18 | 47 | R$ 62,36 | R$ 95 | R$ 2.943 |
| 8953 | Torneira Met Filtro Imperatriz | 27 | R$ 96,28 | R$ 160 | R$ 2.600 |
| 461 | Linha Mista 3x6 | 67,5 | R$ 33,50 | R$ 52 | R$ 2.261 |
| 15511 | Madeirite Plastificado 18mm | 10 | R$ 222 | R$ 340 | R$ 2.220 |
| 16124 | Tela Alambrado Prática | 50 | R$ 42,60 | R$ 80 | R$ 2.130 |
| 2540 | Rebocal Multiuso Mibra 20kg | 71 | R$ 24,60 | R$ 40 | R$ 1.747 |
| 15525 | Bacia p/ Caixa Acoplada Deca | 3 | R$ 527,27 | R$ 770 | R$ 1.582 |
| 10442 | Porcelanato Bali Polido 61x61 | 30 | R$ 48,84 | R$ 70 | R$ 1.469 |
| 11611 | Kit Aço Cacau 40 Cozimax | 4 | R$ 342,51 | R$ 400 | R$ 1.370 |

Já aparecem pares de kit possíveis (sem Cumeeira e sem Vareta): Metalon + Tela Alambrado, Bacia + Caixa Acoplada Deca, Telhas PVC/translúcida + Linha Mista (Tela Moeda Ferro e Forro PVC saíram, ver acima).

Atenção ao Metalon: o diagnóstico de estoque registra o Metalon 30x20 com estoque zerado (furo de estoque). Conferir saldo físico antes de anunciar.

## Pendências antes de virar plano

1. Tony valida item a item os 50 a 100 maiores do pool (encomenda, erro de cadastro, desova real). O Bloco 2 do cruzamento de setembro já pedia isso.
2. Corrigir a Vareta no ERP e registrar a correção em `diagnostico-estoque.md`, `diagnostico-giro-estoque.md` e na planilha (hoje dizem "slow-mover genuíno").
3. Corrigir o cadastro do Tubo PVC Rosca e da categoria "MD-MD-MD...".
4. Nova exportação de estoque e Curva ABC do Pontual para atualizar o snapshot de agosto antes da campanha.
5. Definir com o Tony: desconto máximo, orçamento extra de mídia para novembro, datas da campanha.

---

Sem Humanizer final: rascunho de análise de dados, ainda sem copy.
