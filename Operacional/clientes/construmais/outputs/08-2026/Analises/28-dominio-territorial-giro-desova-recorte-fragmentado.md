# Giro de Desova: Bloco "121 a 150 dias" + "Acima de 180 dias" - Construmais

**Cliente:** Construmais (Tony Carvalho Barbosa), João Pessoa/PB
**Nicho:** Loja de material de construção, B2C local + profissional autônomo, ticket médio até R$ 300 (`_squad/_shared/nichos.md`)
**Objetivo desta entrega:** avaliar, com `@gestor-trafego` e `@copywriter`, se o recorte de giro comprometido sinalizado pelo `@inteligencia-dados` (buckets "121 a 150 dias" e "Acima de 180 dias", R$ 99.010,99) justifica campanha ou criativo pago, e decidir o destino de cada parte
**Handoff:** Pilar 1 (Inteligência de Dados) para Pilar 2 (Domínio Territorial, decisão de mídia do `@gestor-trafego`) e Pilar 4 (Vendedor de Elite, checklist de balcão), conforme item 5 dos "Próximos passos" de `outputs/_diagnosticos/inteligencia-dados/diagnostico-giro-estoque.md`
**Fonte dos dados:** `outputs/_diagnosticos/inteligencia-dados/diagnostico-giro-estoque.md`, seção "Período/Snapshot: 03/08/2026", e extração direta de `08-2026/Arquivos/26-inteligencia-dados-giro-estoque-por-bucket_2026-08-03.xlsx` (aba "Ranking por valor de estoque", filtrado pelos 2 buckets)
**Status:** v1, sujeito a refinamento e validação do Tony
**Nível do `@gestor-trafego` nesta entrega:** Nível 1 (padrão). O `CLIENTE.md` ainda não tem Ad Account ID nem Pixel Meta preenchidos, então este plano é para execução manual no Gerenciador de Anúncios, não para rodar via Meta Ads CLI.
**Não é o mesmo recorte de** `outputs/08-2026/Analises/11-combo-de-produtos-estrategia-desova-estoque-parado.md`, que tratou o bucket "Nunca vendeu em 14 meses" (R$ 351.523,17). Aquele documento segue válido e não foi alterado. Aqui o recorte é o giro "só um pouco menos parado" (121 dias ou mais, mas com venda registrada dentro da janela de 14 meses), bem mais fragmentado.

---

## Contexto herdado do Pilar 1 (não reconfirmado aqui)

- Recorte alvo: **R$ 99.010,99 em 1.155 SKUs** (bucket "121 a 150 dias", R$ 45.164,61 em 536 SKUs, mais "Acima de 180 dias", R$ 53.846,38 em 619 SKUs).
- **Ticket médio por SKU é baixo e a distribuição é bem concentrada nos itens pequenos:** média de R$ 85,72, mediana de R$ 42,46. Só 51 dos 1.155 SKUs (4,4%) passam de R$ 300, somando R$ 31.680,20 (32% do valor do recorte). Nenhum item isolado passa de R$ 4.000.
- O "dias sem venda" de cada item é um piso aproximado, não uma contagem exata (metodologia completa na seção "Metodologia da classificação por bucket" de `diagnostico-giro-estoque.md`). Os dois buckets aqui cobrem uma faixa real de 125 a ~459 dias sem venda, dependendo do item.
- **Nenhum item deste recorte tem confirmação qualitativa individual do Tony ainda**, diferente do recorte de `11-combo-de-produtos-estrategia-desova-estoque-parado.md`, que já tinha Cumeeira Zincalum e Vareta Solda confirmadas por ele. Nada abaixo assume confirmação que não existe.
- **Bloco de referência, não é alvo desta ação:** "31 a 60 dias" soma R$ 426.567,77 em 1.888 SKUs, dominado por Material Básico (R$ 203.203,17), que já é o Kit Fundação/Alvenaria de giro validado. Esse bloco vende bem sozinho e não precisa de reforço promocional agora, ele só serve aqui de contraste pra mostrar que o problema do recorte de hoje não é "estoque parado" no sentido amplo, é giro mais lento em itens de baixo valor unitário.
- **Categoria corrompida "MD-MD-MD-MD-MD- MD-MD-MD-MD-MD-" segue afetando parte deste recorte:** R$ 4.276,29 em 75 SKUs (média R$ 57,02/SKU). Mesma pendência de cadastro já registrada em `diagnostico-estoque.md` e no recorte anterior (lá era R$ 102.131,64). Não força identificação por aproximação de nome, fica só sinalizado como pendência de correção de cadastro no ERP.
- 1 SKU (código 12079, Bota PVC PT/AM NR 41, R$ 63,16) veio sem categoria preenchida no export. Entra no total geral, fica fora da tabela por categoria abaixo por falta de dado.

---

## 1. Priorização (decisão do `@gestor-trafego`)

### 1.1 Por que este recorte pede uma régua diferente do anterior

O recorte de `11-combo-de-produtos-estrategia-desova-estoque-parado.md` tinha itens de ticket alto e concentrado: 8 SKUs já respondiam por mais de R$ 190 mil, com um item sozinho (Cumeeira Zincalum) valendo R$ 77.948,00. Isso permitiu montar 2 kits com apelo claro (Cerca e Portão, Cobertura Completa) e justificar criativo pago em cima deles.

Este recorte é o oposto: 1.155 SKUs, nenhum passando de R$ 4.000, a maioria abaixo de R$ 100. Aplicar a mesma régua do documento anterior (valor médio por SKU decide se compensa mídia paga) aqui aponta pra uma conclusão diferente, não porque a régua mudou, mas porque o dado é outro.

### 1.2 Estoque por categoria e decisão de canal

| Categoria | Valor | SKUs | Valor médio/SKU | Decisão |
|---|---|---|---|---|
| Hidráulica | R$ 14.766,96 | 197 | R$ 74,96 | Fora de mídia paga, cauda fragmentada |
| Ferramentas | R$ 14.596,65 | 216 | R$ 67,58 | Fora de mídia paga, cauda fragmentada |
| Ferragem | R$ 14.108,09 | 233 | R$ 60,55 | Fora de mídia paga, cauda fragmentada |
| Pintura | R$ 10.119,01 | 98 | R$ 103,26 | Fora de mídia paga, cauda fragmentada |
| Material Elétrico | R$ 9.892,83 | 137 | R$ 72,21 | Fora de mídia paga, cauda fragmentada |
| Material Básico | R$ 8.303,50 | 16 | R$ 518,97 | 3 itens entram em rotação de creative dentro de campanha já ativa, ver 1.3. Resto no balcão |
| Utilidades e Jardim | R$ 5.457,48 | 66 | R$ 82,69 | Fora de mídia paga, cauda fragmentada |
| Cobertura | R$ 4.976,88 | 8 | R$ 622,11 | 4 itens entram em rotação de creative dentro de campanha já ativa, ver 1.3 |
| Cadastro corrompido "MD-MD-MD..." | R$ 4.276,29 | 75 | R$ 57,02 | Represado até correção de cadastro (mesma pendência do recorte anterior) |
| Metais | R$ 3.922,98 | 41 | R$ 95,68 | Fora de mídia paga, cauda fragmentada |
| Impermeabilizantes | R$ 2.480,40 | 13 | R$ 190,80 | Fora de mídia paga, volume baixo demais pra campanha própria |
| Esquadrias | R$ 1.804,90 | 9 | R$ 200,54 | Fora de mídia paga, volume baixo demais pra campanha própria |
| Iluminação | R$ 1.472,33 | 12 | R$ 122,69 | Fora de mídia paga, volume baixo demais pra campanha própria |
| Cerâmica | R$ 934,63 | 10 | R$ 93,46 | Fora de mídia paga |
| Argamassas e Rejunte | R$ 891,39 | 10 | R$ 89,14 | Fora de mídia paga |
| Material p/ Piscina | R$ 670,27 | 7 | R$ 95,75 | Fora de mídia paga |
| Louças Sanitária | R$ 170,87 | 4 | R$ 42,72 | Fora de mídia paga |
| Armários, Gabinetes | R$ 102,24 | 1 | R$ 102,24 | Fora de mídia paga |
| Refrigeração | R$ 0,11 | 1 | R$ 0,11 | Irrelevante |
| (sem categoria no export) | R$ 63,16 | 1 | R$ 63,16 | Fora de mídia paga |

**Leitura direta:** nenhuma categoria deste recorte tem valor médio por SKU que sustente campanha paga própria. Pra comparar com o que já foi decidido antes: em `11-combo-de-produtos-estrategia-desova-estoque-parado.md`, Ferragem (R$ 81,17/SKU), Ferramentas (R$ 71,68/SKU) e Material Elétrico (R$ 85,68/SKU) já tinham sido classificadas "baixo demais pra campanha paga por SKU, custo de aquisição por clique come a margem". As mesmas 3 categorias aparecem aqui com médias iguais ou menores (Ferragem R$ 60,55, Ferramentas R$ 67,58, Material Elétrico R$ 72,21). Não faz sentido promover agora o que já foi descartado com um valor médio mais alto antes.

Isso vale inclusive pra sugestão inicial de agrupar Hidráulica, Ferramentas e Ferragem numa campanha só por somarem cerca de R$ 43,4 mil juntas: o total agregado não muda a régua, porque a campanha não vende "categoria", vende produto. Um anúncio pra R$ 43,4 mil espalhados em 646 SKUs distintos (média de R$ 67,25 cada) não tem um produto pra colocar na tela, só uma lista de itens sem coerência de oferta entre si.

### 1.3 Os 7 itens que aproveitam campanha já ativa, sem orçamento novo

Dois grupos pequenos deste recorte pertencem à mesma família de produto de kits que já estão rodando desde `11-combo-de-produtos-estrategia-desova-estoque-parado.md`. Não justificam campanha própria, mas também não precisam esperar giro orgânico: entram como sugestão de venda complementar quando o kit já ativo for vendido, sem criativo novo nem budget novo.

| Código | Produto | Categoria | Valor | Bucket | Kit já ativo que complementa |
|---|---|---|---|---|---|
| 13801 | Tela Moeda Ferro 1,90cm | Material Básico | R$ 3.945,41 | Acima de 180 dias | Kit Cerca e Portão (fechamento alternativo à Tela Alambrado) |
| 461 | Linha Mista 3x6 | Cobertura | R$ 2.261,29 | 121 a 150 dias | Kit Cobertura Completa |
| 14790 | Telha PVC Incolor Ondafort | Cobertura | R$ 970,85 | 121 a 150 dias | Kit Cobertura Completa (claraboia/iluminação de telhado) |
| 14583 | Telha Translúcida Leitosa | Cobertura | R$ 764,05 | Acima de 180 dias | Kit Cobertura Completa (claraboia/iluminação de telhado) |
| 14393 | Forro PVC Liso | Cobertura | R$ 670,11 | Acima de 180 dias | Kit Cobertura Completa (acabamento de forro) |
| 7775 | Cantoneira Ferro 3/4 Serralheiro | Material Básico | R$ 295,13 | Acima de 180 dias | Kit Cerca e Portão (reforço de estrutura) |
| 5994 | Tela Galv p/ Viveiro | Material Básico | R$ 280,28 | 121 a 150 dias | Kit Cerca e Portão (fechamento de viveiro/cercamento menor) |
| **Total** | | | **R$ 9.187,12** | | |

**Por que estes e não outros:** o critério não foi "maior valor", foi pertencer com clareza à mesma função de produto de um kit que já existe e já está sendo anunciado. Tela Moeda Ferro, Tela Galv p/ Viveiro e Cantoneira Ferro Serralheiro são material de fechamento e estrutura metálica, mesma função de Metalon e Tela Alambrado do Kit Cerca e Portão. Telha PVC Incolor, Telha Translúcida e Forro PVC estão literalmente cadastrados na categoria "Cobertura" e complementam o par Cumeeira/Telha do Kit Cobertura Completa (claraboia e acabamento de forro, que costumam entrar no mesmo pedido de quem fecha telhado). Linha Mista está na mesma categoria "Cobertura", mas o nome do produto não deixa claro o uso específico (não vou afirmar pra que serve sem confirmação), então entra no grupo pela categoria, sem alegar função exata na copy.

**O que isso muda na prática:** nenhum criativo novo, nenhum conjunto novo, nenhum budget novo. Só o checklist de balcão (seção 4) passa a incluir estes 7 itens como sugestão de venda adicional quando o vendedor fechar o Kit Cerca e Portão ou o Kit Cobertura Completa. Fica registrado que o Kit Cerca e Portão originalmente cita Tela Alambrado como o item de fechamento: a Tela Moeda Ferro entra como alternativa de fechamento, não como substituição, o vendedor oferece a que tiver em estoque ou for mais barata pro cliente.

---

## 2. Estratégia de tráfego pago (Pilar 2)

### RESUMO DA DECISÃO

```
Cliente: Construmais
Recorte avaliado: R$ 99.010,99 em 1.155 SKUs (buckets 121-150 e Acima de 180 dias)
Decisão: nenhuma campanha nova, nenhum conjunto novo, nenhum criativo pago novo
Budget: R$ 0 adicional. Os 7 itens da seção 1.3 (R$ 9.187,12) entram só como sugestão de balcão
  atrelada aos kits já ativos (Cerca e Portão, Cobertura Completa)
Resto do recorte (R$ 89.823,87, ~1.148 SKUs): checklist de balcão genérico + post orgânico
```

**Por que não abrir campanha nem criativo pago para nenhuma parte deste recorte:** a régua usada em `11-combo-de-produtos-estrategia-desova-estoque-parado.md` (valor médio por SKU compensa CPC, ou não) já rejeitou categorias com média de R$ 71 a R$ 86 por SKU. Este recorte inteiro tem média de R$ 85,72 e mediana de R$ 42,46, abaixo ou igual ao que já foi descartado. Manter a mesma régua aqui significa não abrir campanha nova nem gastar criativo em nenhuma categoria isolada. Isso não é uma régua mais dura, é a mesma régua aplicada de novo, e o resultado natural quando o dado é mais fragmentado que da última vez.

O único uso de mídia que este recorte sustenta é o que já está descrito na seção 1.3: aproveitar 7 itens que se encaixam em kits já ativos, sem custo incremental nenhum, porque a estrutura de campanha e o público já existem e não precisam de nada novo.

**Quando reconsiderar:** se o Tony confirmar individualmente que algum item deste recorte tem relevância que o valor de estoque sozinho não mostra (por exemplo, um item de reposição frequente por profissional recorrente, mesmo com ticket baixo), essa confirmação pode justificar revisão pontual. Sem isso, o recorte segue como está.

### RASTREAMENTO

```
[ ] Nenhuma UTM nova necessária, não há criativo novo nem conjunto novo
[ ] Ao adicionar os 7 itens da seção 1.3 no checklist de balcão, registrar no PDV a taxa de anexo
    junto com a taxa de anexo já medida do Kit Cerca e Portão e do Kit Cobertura Completa
    (mesma métrica de `24-estrategia-kits-e-vendas.md`, seção 4.4)
```

### QUANDO REVISITAR

```
Próxima rodada de Curva ABC / snapshot de estoque: reclassificar este recorte. Item que continuar
girando abaixo do bucket "31 a 60 dias" segue como está aqui; item que passar pra "Nunca vendeu"
migra pro critério mais severo já usado em `11-combo-de-produtos-estrategia-desova-estoque-parado.md`.
```

---

## 3. Ângulos de copy (decisão do `@copywriter`)

Como nenhum item ou categoria deste recorte entrou em mídia paga (seção 2), não há headline nem anúncio pago pra produzir aqui. O trabalho de copy fica inteiro no ângulo orgânico e no reforço do checklist de balcão, que reaproveita o template já existente `01-dominio-territorial-template-tem-na-construmais.html`, mesma peça usada no recorte anterior. Sem promessa de desconto ou preço não confirmado pelo Tony, sem frete grátis (Compliance do `CLIENTE.md`).

### Post orgânico "Comunicado" (categoria genérica, cauda fragmentada)

Cobre o grosso do recorte (R$ 89.823,87 em cerca de 1.148 SKUs de Hidráulica, Ferramentas, Ferragem, Pintura, Material Elétrico, Utilidades e Jardim, Metais e as categorias menores), sem apontar item específico, já que nenhum item isolado tem apelo suficiente pra virar peça sozinho.

**Legenda do selo (`.badge-inner` do template):**
- L1 (categoria): Comunicado
- L2 (nome): Tem de tudo
- L3 (detalhe): passa e confere

**Texto do post/story:**
Comunicado Construmais: chave de fenda, torneira, disjuntor, lixa, mangueira. A gente tem parafuso, conexão e ferragem parados aqui há um tempo, e o preço tá pronto pra sair rápido. Passa na loja ou chama no WhatsApp pra ver o que tem disponível. 🏗️🔧✅
**CTA:** Chame no WhatsApp

**Sugestão de criativo:** foto real de uma bancada ou prateleira com mix de ferragem/ferramentas (Hidráulica, Ferramentas, Ferragem, Material Elétrico), com faixa amarela diagonal "Comunicado!" seguindo o padrão de avisos da marca. Sem foto própria disponível, usar o mascote no balcão apontando pra prateleira.

### Reforço de balcão para os 7 itens da seção 1.3 (não é post novo, é script de venda)

Texto de apoio pro vendedor oferecer o complemento no fechamento do Kit Cerca e Portão ou do Kit Cobertura Completa, sem virar peça de anúncio:

**No fechamento do Kit Cerca e Portão:** "Além do metalon, da tela e da solda, a gente também tem tela moeda de ferro se preferir outro tipo de fechamento, e cantoneira pra reforçar a estrutura. Quer que eu inclua no orçamento?"

**No fechamento do Kit Cobertura Completa:** "Fechando telhado, a gente também tem telha translúcida pra quem quer clarabóia, e forro de PVC pra acabamento por dentro. Já incluo no seu orçamento?"

### Nota sobre a categoria corrompida

Os R$ 4.276,29 em 75 SKUs sob "MD-MD-MD-MD-MD- MD-MD-MD-MD-MD-" ficam fora de qualquer peça de copy até o Tony corrigir o cadastro no ERP. Mesma decisão já tomada no recorte anterior, sem forçar identificação por aproximação de nome.

---

## 4. Ações complementares fora de mídia paga

1. **Checklist de balcão para a cauda fragmentada.** Hidráulica, Ferramentas, Ferragem, Pintura, Material Elétrico e as categorias menores (R$ 89.823,87 no total) têm valor médio por item baixo demais pra qualquer ação além do PDV. Segue o mesmo modelo do Playbook de Vendas já existente (`outputs/07-2026/Analises/24-estrategia-kits-e-vendas.md`, seção 4).
2. **Sugestão de venda complementar atrelada aos kits já ativos.** Os 7 itens da seção 1.3 (R$ 9.187,12) entram no script de fechamento do Kit Cerca e Portão e do Kit Cobertura Completa, sem virar campanha nem criativo novo.
3. **Post orgânico "Comunicado"** usando o template "Tem na Construmais" pra dar visibilidade geral à cauda fragmentada, sem custo de mídia.
4. **Correção de cadastro:** a categoria corrompida "MD-MD-MD..." segue pendente de correção no Pontual Tecnologia, mesma pendência já cobrada no recorte anterior e em `diagnostico-estoque.md`. Enquanto não for corrigida, R$ 4.276,29 deste recorte ficam represados sem ação de venda dirigida.

---

## Sinalização: pronto vs v1

- **Pronto pra usar como estava:** priorização da seção 1 (números direto da planilha), decisão de não abrir campanha nova (seção 2), script de balcão da seção 3.
- **v1, precisa de validação do Tony antes de publicar:** confirmação de que Tela Moeda Ferro é de fato alternativa viável de fechamento ao lado da Tela Alambrado (nenhuma confirmação qualitativa foi coletada neste recorte), e conferência de que Telha Translúcida/Telha PVC Incolor combinam de fato com o padrão de telha do Kit Cobertura Completa.

## Pendências para virar "pronto para publicar"

1. Tony confirma se Tela Moeda Ferro, Cantoneira Ferro Serralheiro e Tela Galv p/ Viveiro fazem sentido como alternativa/complemento de venda no Kit Cerca e Portão.
2. Tony confirma se Telha PVC Incolor, Telha Translúcida e Forro PVC combinam com o padrão de telha do Kit Cobertura Completa (claraboia e acabamento).
3. Confirmar com o Tony se a categoria corrompida "MD-MD-MD..." já tem previsão de correção no ERP, libera R$ 4.276,29 deste recorte pra reclassificação.
4. Produzir a foto real de bancada/prateleira mista pro post orgânico "Comunicado" (seção 3), ou usar o mascote como alternativa.

## Próximos passos

1. Passar o script de balcão da seção 3 pro vendedor usar no fechamento dos 2 kits já ativos, sem esperar aprovação de mais nada.
2. Publicar o post orgânico "Comunicado" assim que a foto estiver pronta.
3. `@analista-dados` inclui a taxa de anexo dos 7 itens da seção 1.3 no mesmo acompanhamento já feito pro Kit Cerca e Portão e pro Kit Cobertura Completa.
4. Cobrar do Tony a correção de cadastro da categoria "MD-MD-MD..." antes da próxima rodada de Curva ABC.
5. Na próxima atualização de `diagnostico-giro-estoque.md`, reavaliar se algum item deste recorte migrou de bucket (pra "31 a 60 dias", sinal de giro melhorando, ou pra "Nunca vendeu", sinal de piora).

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
