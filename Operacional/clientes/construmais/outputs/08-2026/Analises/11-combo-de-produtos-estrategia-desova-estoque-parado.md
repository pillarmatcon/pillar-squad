# Estratégia de Giro de Estoque Parado - Construmais

**Cliente:** Construmais (Tony Carvalho Barbosa), João Pessoa/PB
**Nicho:** Loja de material de construção, B2C local + profissional autônomo, ticket médio até R$ 300 (`_squad/_shared/nichos.md`)
**Objetivo desta entrega:** transformar estoque parado em caixa, com handoff do Pilar 1 (Inteligência de Dados) para o Pilar 3 (Combo de Produtos, decisão do `@copywriter`) e o Pilar 2 (Domínio Territorial, tráfego pago, decisão do `@gestor-trafego`)
**Fonte dos dados:** `outputs/_diagnosticos/inteligencia-dados/diagnostico-estoque.md`, seção "Atualização de Estoque: 03/08/2026", e extração direta de `08-2026/Arquivos/03-inteligencia-dados-estoque-auditado_2026-08-03.xlsx` (aba "Estoque parado (ajustado)")
**Status:** v1, sujeito a refinamento e validação do Tony
**Nível do `@gestor-trafego` nesta entrega:** Nível 1 (padrão). O `CLIENTE.md` ainda não tem Ad Account ID nem Pixel Meta preenchidos, então o plano de mídia abaixo é para execução manual no Gerenciador de Anúncios, não para rodar via Meta Ads CLI.

---

## Contexto herdado do Pilar 1 (não reconfirmado aqui)

- Estoque parado real e atual: **R$ 373.769,46 a custo, em 1.732 SKUs**, sem venda registrada em 14 meses (mai/2025 a jun/2026).
- 3 outliers de cadastro (cabo flex 7153, mangueira 7874, colorante 11073) já saíram desse número, pendentes de confirmação do Tony. Não tratar como estoque real disponível.
- Ticket médio do cliente final é baixo (até R$ 300). Decisão estratégica de 23/07/2026 já fechada: kit não leva produto de acabamento, fica em material básico, elétrica, hidráulica e pintura.
- Kit Fundação e Alvenaria (cimento + areia + pedra britada + tijolo) segue validado como âncora de giro nos 4 períodos de Curva ABC. Ele não entra nesta estratégia como alvo (não é item parado), mas aparece como referência de comparação onde fizer sentido.
- Raio de mídia: até 10km da loja, foco Cristo Redentor. Orçamento de mídia do cliente: R$ 2.000/mês, hoje dividido entre as campanhas de Sistema Tintométrico e Material Básico Ensacado (`CLIENTE.md`, Plano de Ação 23/07/2026). O split exato em R$ entre as duas não está documentado, então a proposta de mídia abaixo evita assumir um número que ninguém confirmou.

---

## 1. Priorização

### 1.1 Regra de corte antes de qualquer campanha

Nem todo item com valor alto em estoque parado é mercadoria pra empurrar pro cliente final. Dois filtros correm antes da lista de prioridade:

1. **É mercadoria de revenda de verdade?** Sacola, embalagem e item de uso interno da própria loja saem da lista de campanha, mesmo tendo valor alto parado. Vira decisão operacional do Tony (descontinuar compra, usar o estoque internamente, ou repor com fornecedor mais barato), não vira anúncio.
2. **O cadastro sustenta uma oferta pública?** Preço ou custo com sinal de erro não pode virar anúncio antes de corrigido. Uma promessa de preço errado na tela é problema de CDC, não só de dado.

### 1.2 Os 8 maiores itens parados, com decisão

| # | Produto                                    | Valor em estoque                                                                                                                                                                                                                                                                                                                                                              | Categoria                                     | Decisão                        | Por quê                                                                                                    |
| - | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 1 | Cumeeira Zincalum 0,43                     | R$ 77.948,00                                                                                                                                                                                                                                                                                                                                                                  | Material Básico                              | **Promover, mídia paga** | Item real de cobertura, encaixa no Kit Cobertura Completa (item 2 abaixo)                                   |
| 2 | Vareta Solda Oxi 1,59mm Gerdau             | R$ 74.755,80                                                                                                                                                                                                                                                                                                                                                                  | Cadastro corrompido, provável Ferragem/Metal | **Promover, mídia paga** | Insumo de solda, identificável pelo nome mesmo com categoria quebrada no ERP. Entra no Kit Cerca e Portão |
| 3 | Sacolas 30x40 Imp                          | R$ 23.378,30 | Material de Uso e Consumo | **Excluir da campanha** | Embalagem da própria loja, não mercadoria de revenda. Preço cadastrado de R$ 0,20 contra custo de R$ 11,66 é erro de cadastro (markup negativo de quase 100%), reportar ao Tony antes de qualquer decisão sobre o item                                                                            |                                               |                                 |                                                                                                             |
| 4 | Sacola Recicladas VD 60x80                 | R$ 11.672,50                                                                                                                                                                                                                                                                                                                                                                  | Material de Uso e Consumo                     | **Excluir da campanha**   | Mesmo caso do item 3, embalagem interna                                                                     |
| 5 | Tubo PVC Rosca 1 pol Tigre                 | R$ 8.058,63 | Cadastro corrompido, claramente Hidráulica | **Não promover até checar preço** | Preço de R$ 96,00 contra custo de R$ 8,06 é markup de aprox. 1.091%, muito fora do padrão dos outros 7 itens desta tabela (todos entre 52% e 146%). Ou o preço está errado, ou o custo está errado. Não colocar em anúncio antes do Tony confirmar qual dos dois |                                               |                                 |                                                                                                             |
| 6 | Metalon Galv 30x20mm 1,25mm Ch18           | R$ 2.943,39                                                                                                                                                                                                                                                                                                                                                                   | Material Básico                              | **Promover, mídia paga** | Estrutura pra cerca/portão, entra no Kit Cerca e Portão                                                   |
| 7 | Torneira Met Filtro ABS BM 2172 Imperatriz | R$ 2.599,56 | Cadastro corrompido, claramente Metais/Hidráulica | **Promover, mídia paga** | Item de ticket mais alto (R$ 160), bom complemento do Tubo PVC Rosca assim que o preço deste for confirmado                                                                                                                                                                 |                                               |                                 |                                                                                                             |
| 8 | Tela Alambrado Practica Belgo              | R$ 2.130,00                                                                                                                                                                                                                                                                                                                                                                   | Material Básico                              | **Promover, mídia paga** | Fecha o trio com Metalon e Vareta Solda no Kit Cerca e Portão                                              |

**Achado que muda a prioridade:** os itens 2, 6 e 8 (Vareta Solda, Metalon e Tela Alambrado) juntos somam **R$ 79.829,19**, quase o mesmo valor do item 1 sozinho, e formam um kit natural de construção de cerca/portão que nenhum dos três resolveria sozinho como oferta. Ver seção 2.

### 1.3 Estoque parado por categoria, os 8 maiores grupos

| Categoria                         | Valor parado                                                                                                                                                                                                      | Itens | Decisão de canal                                                                                                                                                                                                     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cadastro corrompido "MD-MD-MD..." | R$ 102.131,64                                                                                                                                                                                                     | 371   | Não dá pra campanha de categoria (não sabemos o que é a maior parte). Só os itens já identificados pelo nome entram (Vareta Solda, Tubo PVC Rosca). Resto fica represado até o Tony corrigir o cadastro no ERP |
| Material Básico                  | R$ 83.968,25                                                                                                                                                                                                      | 22    | Campanha paga nos itens de maior valor (Cumeeira, Metalon, Tela), resto via giro orgânico e balcão                                                                                                                  |
| Material de Uso e Consumo         | R$ 54.545,54                                                                                                                                                                                                      | 75    | **Fora da campanha inteira.** Categoria mistura sacola, embalagem, boné, celular, coisas que não são produto de revenda. Decisão operacional do Tony, não de marketing                                     |
| Ferragem                          | R$ 22.891,26 | 282 | Valor médio de R$ 81,17 por item. Baixo demais pra justificar campanha paga por SKU, custo de aquisição por clique come a margem. Fica no balcão (checklist de venda) e giro orgânico |       |                                                                                                                                                                                                                       |
| Pintura                           | R$ 21.101,43                                                                                                                                                                                                      | 107   | Fora do escopo de kit desta rodada por decisão já fechada de não misturar acabamento no combo (23/07/2026). Giro orgânico e balcão                                                                               |
| Ferramentas                       | R$ 18.418,81                                                                                                                                                                                                      | 257   | Mesma lógica de Ferragem, cauda fragmentada, balcão e orgânico                                                                                                                                                     |
| Hidráulica                       | R$ 16.548,25                                                                                                                                                                                                      | 204   | Os 2 itens de maior valor (Tubo PVC Rosca, Torneira) já cobertos na tabela 1.2, resto no balcão                                                                                                                     |
| Material Elétrico                | R$ 11.481,37                                                                                                                                                                                                      | 134   | Cauda fragmentada, balcão e orgânico                                                                                                                                                                                |

**Leitura direta:** dá pra endereçar cerca de R$ 90.500,00 do estoque parado (Kit Cerca e Portão + Kit Cobertura, sem contar o Kit Hidráulica que ainda depende da checagem de preço) com só 2 a 3 campanhas de combo bem definidas. O resto, cerca de R$ 245 mil espalhados em milhares de SKUs de baixo valor individual, não compensa mídia paga item a item. Esse volume se resolve com checklist de balcão e giro orgânico (seção 5), não com anúncio.

---

## 2. Estratégia de combo/oferta (Pilar 3)

Kits pensados pra parear item parado com produto que já sai da prateleira, sempre dentro de material básico, elétrica, hidráulica e pintura, sem entrar em acabamento (decisão de 23/07/2026 mantida).

### Kit Cerca e Portão

**Composição:** Metalon Galv 30x20mm (estrutura) + Tela Alambrado Practica Belgo (fechamento) + Vareta Solda Oxi 1,59mm Gerdau (montagem)

Os três já saem juntos na prática: quem constrói cerca ou portão precisa da estrutura de metalon, da tela pra fechar e da solda pra unir o metalon. É o único combo desta lista formado inteiramente por itens parados, o que significa que ele resolve três problemas de estoque com uma única oferta.

**Público:** profissional de serralheria (que compra pra revenda de serviço) e morador/proprietário fazendo cerca, muro ou portão de terreno, sítio ou quintal.

**Referência de markup cadastrado** (preço menos custo, dividido pelo custo, mesmo cálculo usado no diagnóstico de estoque, não é margem sobre venda real): Metalon 52,4%, Tela Alambrado 87,8%, Vareta Solda 145,1%. Os três têm folga de markup acima da média do catálogo, o que dá espaço real pra um desconto de combo sem sacrificar o resultado.

**Sugestão de precificação:** kit com preço 5% a 8% abaixo da soma dos 3 itens separados. **Não confirmado com o Tony ainda**, então nenhuma peça de anúncio abaixo cita um percentual fechado até essa validação.

### Kit Cobertura Completa

**Composição:** Cumeeira Zincalum 0,43 (parado) + Telha Canal Russa (giro alto, âncora já validada na Fase 4 da estratégia de kits por fase de obra, `outputs/07-2026/Analises/24-estrategia-kits-e-vendas.md`)

Quem compra telha de cobertura via de regra também precisa da cumeeira pra fechar o cume do telhado. Amarrar a cumeeira parada ao produto que já vende bem é a versão mais direta de "empurrar o que não sai sozinho junto com o que já sai".

**Público:** quem está fechando ou trocando telhado, morador em obra de cobertura ou reforma, e o pedreiro/empreiteiro que executa esse serviço.

**Sugestão de precificação:** manter o preço da telha (produto que já gira bem, não precisa de desconto pra vender) e aplicar o desconto só na cumeeira quando comprada junto, faixa sugerida de 10% a 15% sobre a cumeeira isolada (ela é o item parado, tem mais folga pra ceder preço). **Pendente de validação do Tony.**

### Kit Hidráulica Reforço (condicional)

**Composição:** Tubo PVC Rosca 1 pol Tigre + Torneira Met Filtro ABS Imperatriz

Combo natural de reforma de banheiro, área externa ou substituição de torneira com troca de trecho de cano. **Este kit fica pausado até o Tony confirmar o preço real do Tubo PVC Rosca** (ver seção 1.2, item 5). Assim que o preço for corrigido no ERP, o kit está pronto pra entrar em campanha com a mesma lógica dos outros dois.

### Como o combo aparece no ponto de venda

Segue o mesmo modelo já validado em `outputs/07-2026/Analises/24-estrategia-kits-e-vendas.md` (seção 4, Playbook de execução comercial):

- **Balcão:** quando o vendedor bate Metalon, Tela Alambrado ou Cumeeira no PDV, o sistema (ou uma folha impressa no caixa) sugere o complemento antes de fechar a venda.
- **Orçamento de obra/cerca:** o kit já entra montado na proposta, não como sugestão depois de fechado.
- **Nome do kit no caixa e na campanha:** "Kit Cerca e Portão" e "Kit Cobertura Completa", nunca tratado como dois produtos soltos.

---

## 3. Estratégia de tráfego pago (Pilar 2)

### RESUMO DO PLANO

```
Cliente: Construmais
Objetivo: Girar estoque parado (Cumeeira, Metalon, Tela Alambrado, Vareta Solda), via orçamento no WhatsApp
Budget: sem linha nova dedicada nesta fase. Entra como rotação de criativo dentro da campanha de Material Básico Ensacado já ativa
Plataforma: Meta Ads (Facebook + Instagram)
Meta de resultado: orçamentos citando "Kit Cerca" ou "Kit Cobertura" pelo WhatsApp, acompanhado no PDV pela taxa de anexo (mesma métrica já usada nos outros kits)
```

**Por que não abrir campanha nova agora:** com R$ 2.000/mês já divididos entre Tintométrico e Material Básico Ensacado, e sem o split exato documentado, uma terceira linha nova ficaria abaixo do mínimo de R$ 30/dia (R$ 900/mês) que o próprio benchmark da Pillar recomenda pra gerar dado confiável (`_squad/01-gestor-trafego/SKILL.md`, "Decisão de budget mínimo por plataforma"). Dividir um budget já apertado em mais uma frente reduz o volume de evento em todas, contra a regra de ouro do próprio agente: concentrar budget pequeno em vez de fatiar.

**O que fazer em vez disso:** o público do Kit Cerca e Portão e do Kit Cobertura Completa é o mesmo raio geográfico e, em boa parte, o mesmo perfil de quem já é alvo da campanha de Material Básico Ensacado (bairros com demanda de reforma, dentro dos 10km, foco Cristo Redentor). Os novos criativos entram como variação dentro dessa campanha existente, testando ao lado dos criativos atuais, sem abrir orçamento novo. Isso evita canibalizar o Tintométrico (que é público e objetivo diferente, tinta/acabamento) e não compete por budget com a campanha vigente.

**Quando abrir campanha dedicada:** se os criativos de desova tiverem CTR ou custo por resultado melhor que os criativos atuais de Material Básico Ensacado depois de 3 a 4 semanas rodando juntos, aí faz sentido pedir ao Tony um incremento de budget (ex: mais R$ 300 a R$ 500/mês) pra isolar a campanha de desova e medir separado.

### ESTRUTURA DE CAMPANHA

```
CAMPANHA EXISTENTE: Material Básico Ensacado (nome real da campanha a confirmar no Gerenciador)
  Ação: adicionar 1 conjunto de anúncios novo, ou 2 a 3 anúncios novos dentro do conjunto atual

  CONJUNTO NOVO: Liquida Estoque - Cerca e Cobertura
    Segmentação: Advantage+ com semente de interesse (cerca, portão, serralheria, cobertura residencial, reforma de telhado, construção civil)
    Localização: raio de 10km da loja, foco Cristo Redentor (mesma geo já usada nas campanhas ativas)
    Orçamento: fatia do orçamento já alocado à campanha de Material Básico Ensacado, não é budget incremental nesta fase

    ANÚNCIO A: Kit Cerca e Portão (imagem única, Story + Post)
    ANÚNCIO B: Kit Cobertura Completa (imagem única, Story + Post)
```

Formato padrão da Pillar: imagem única em Story e Post. Sem carrossel nesta fase (carrossel só entra se o Tony pedir explicitamente).

### SEGMENTAÇÃO

- **Meta Ads:** Advantage+ com semente de interesse dividida por criativo. Kit Cerca e Portão mira serralheria, cerca residencial, "faça você mesmo" e construção civil. Kit Cobertura mira reforma de telhado e construção civil.
- **Geografia:** raio de 10km da loja, com prioridade de exibição pro bairro Cristo Redentor, mesma configuração já usada nas campanhas correntes.
- **Retargeting:** reaproveitar a lista de engajamento Instagram/Facebook e visitantes de site já existente, se houver, sem criar lista nova só pra este teste.

### CRIATIVOS NECESSÁRIOS

| # | Formato                     | Peça                  | Produto em foco                         | Onde entra                                                    |
| - | --------------------------- | ---------------------- | --------------------------------------- | ------------------------------------------------------------- |
| 1 | Imagem única, Story + Post | Kit Cerca e Portão    | Metalon + Tela Alambrado + Vareta Solda | Conjunto novo dentro da campanha de Material Básico Ensacado |
| 2 | Imagem única, Story + Post | Kit Cobertura Completa | Cumeeira + Telha                        | Conjunto novo dentro da campanha de Material Básico Ensacado |

2 criativos no lançamento é suficiente pra um teste dentro de campanha já ativa. O Kit Hidráulica Reforço só vira criativo depois de resolvido o preço do Tubo PVC Rosca.

### RASTREAMENTO

```
[ ] Confirmar nome/ID exato da campanha de Material Básico Ensacado no Gerenciador antes de criar o conjunto novo
[ ] UTM nos dois criativos novos: utm_source=meta&utm_medium=cpc&utm_campaign=MATERIALBASICOENSACADO&utm_content=KITCERCAPORTAO (e KITCOBERTURA)
[ ] Meta Pixel e evento de conversão já configurados na campanha existente, reaproveitar, não recriar
[ ] Registrar no CLIENTE.md o Ad Account ID e Pixel ID reais assim que o Tony ou a equipe interna tiver acesso, hoje aparecem como [PREENCHER]
```

### CALENDÁRIO DE VOO

```
SEMANA 1: subir os 2 criativos novos dentro do conjunto/campanha existente, sem mexer no budget total
SEMANA 2-3: comparar CTR e custo por resultado dos criativos novos contra os criativos atuais da campanha
SEMANA 4: decisão, se performance for igual ou melhor, propor ao Tony orçamento dedicado pra escalar; se for pior, pausar e ajustar criativo antes de tentar de novo
```

### BENCHMARKS ESPERADOS

O CPL de referência de R$ 30-80 do `CLIENTE.md` foi calibrado pra geração de orçamento geral da loja, não pra um SKU específico de ticket mais baixo (Cumeeira R$ 41, Metalon R$ 95, Tela R$ 80/un). Pra este teste, a métrica mais honesta não é CPL isolado, é a **taxa de anexo no PDV** (das vendas do item âncora, quantas saíram com o complemento), a mesma métrica já usada nos outros kits (`outputs/07-2026/Analises/24-estrategia-kits-e-vendas.md`, seção 4.4). Comparar CPL dos criativos novos contra os atuais da campanha serve como sinal de custo, mas a decisão de continuar ou não depende do PDV, não só do Gerenciador de Anúncios.

---

## 4. Ângulos de copy e criativo

**Framework:** identificação + benefício direto, adaptado ao tom próximo e informal da Construmais (`CLIENTE.md`, Tom da marca). Sem promessa de desconto fechado até o Tony validar o percentual (seção 2). Sem frete grátis, sem parcelamento que não seja política real da loja (Compliance do `CLIENTE.md`).

### Kit Cerca e Portão

**Headline 1 (identificação, serralheiro):** Vai levantar cerca ou portão?
**Subheadline:** Metalon, tela de alambrado e vareta de solda numa loja só, em João Pessoa.

**Headline 2 (dor):** Terreno sem cerca ainda?
**Subheadline:** Resolve estrutura, fechamento e solda no mesmo pedido na Construmais.

**Texto do anúncio (Story + Post):**
Cerca, muro ou portão pede três coisas ao mesmo tempo: metalon pra estrutura, tela pra fechar e solda pra unir tudo. A Construmais tem os três prontos pra pegar, no bairro Cristo Redentor. Chame no WhatsApp e peça o valor do Kit Cerca e Portão.
**CTA:** Peça seu orçamento

**Sugestão de criativo:** foto real do metalon e da tela de alambrado empilhados na loja, com faixa amarela diagonal "Comunicado!" reforçando a novidade do kit, seguindo o padrão visual já usado em avisos da marca. Se não houver foto própria disponível, usar o mascote segurando a colher de pedreiro ao lado do produto.

### Kit Cobertura Completa

**Headline 1 (dor funcional):** Telhado fechado, mas sem cumeeira?
**Subheadline:** Cumeeira Zincalum e telha no mesmo pedido, na Construmais.

**Headline 2 (benefício direto):** Cobertura completa numa loja só
**Subheadline:** Telha e cumeeira sem precisar rodar atrás de fornecedor diferente pra cada peça.

**Texto do anúncio (Story + Post):**
Quem está fechando telhado sabe que falta a cumeeira pra dar acabamento no cume. Na Construmais, telha e cumeeira saem do mesmo pedido, no bairro Cristo Redentor e arredores. Chame no WhatsApp e feche o Kit Cobertura Completa.
**CTA:** Falar com a Construmais

**Sugestão de criativo:** foto de telhado com cumeeira aplicada (se o Tony tiver registro de obra atendida, com autorização) ou foto de produto na loja com faixa "Oferta relâmpago" se o desconto for aprovado a tempo do lançamento.

### Ângulo de liquidação geral (cauda longa, uso orgânico, não paga)

Pra a cauda de Ferragem, Ferramentas, Material Elétrico e Hidráulica que não justifica mídia paga por SKU (seção 1.3), o ângulo é comunicado de loja, não anúncio pago:

**Texto sugerido pro post/story orgânico:**
Comunicado Construmais: chegou parafuso, bucha, disco de corte e mais um monte de item parado no estoque com preço pra sair rápido. Passa na loja ou chama no WhatsApp pra saber o que tem disponível.

Usar o template já existente "Tem na Construmais" (`outputs/08-2026/Arquivos/01-dominio-territorial-template-tem-na-construmais.html`), que já segue a identidade visual da marca.

---

## 5. Ações complementares fora de mídia paga

1. **Checklist de balcão para a cauda longa.** Ferragem, Ferramentas e Material Elétrico têm valor médio por item baixo demais pra campanha paga (R$ 81,17 no caso de Ferragem), mas o vendedor pode empurrar isso no PDV com um checklist simples, seguindo o mesmo modelo do Playbook de Vendas já existente (`outputs/07-2026/Analises/24-estrategia-kits-e-vendas.md`, seção 4).
2. **Posts orgânicos usando o template "Tem na Construmais"** pra dar visibilidade aos itens parados de menor ticket, sem custo de mídia.
3. **Correção de cadastro antes de qualquer coisa em 3 frentes:** o preço do Tubo PVC Rosca (item com markup fora do padrão), a categoria corrompida "MD-MD-MD..." que esconde R$ 102 mil de estoque parado sem identificação, e o preço das Sacolas 30x40 (venda abaixo do custo). Nenhuma dessas três correções depende de campanha, dependem do Tony mexer no Pontual Tecnologia.
4. **Decisão operacional sobre Material de Uso e Consumo** (R$ 54.545,54 parados em sacola, embalagem e itens de uso interno da loja): não é pauta de marketing, é decisão do Tony sobre repor menos, usar o estoque internamente ou negociar devolução com fornecedor.

---

## Sinalização: pronto vs v1

- **Pronto pra usar como estava:** priorização da seção 1 (números direto da planilha auditada), estrutura da campanha na seção 3 (não depende de aprovação de preço).
- **v1, precisa de validação do Tony antes de publicar:** percentual de desconto dos 2 kits (seção 2), preço do Tubo PVC Rosca antes de qualquer peça do Kit Hidráulica Reforço, nome exato da campanha de Material Básico Ensacado no Gerenciador antes de criar o conjunto novo.

## Pendências para virar "pronto para publicar"

1. Tony confirma o percentual de desconto do Kit Cerca e Portão e do Kit Cobertura Completa (sugestões na seção 2, nenhuma delas está na copy final ainda).
2. Tony ou a equipe Pillar confirma no Pontual Tecnologia se o preço do Tubo PVC Rosca (R$ 96,00) ou o custo (R$ 8,06) está errado, antes de montar o Kit Hidráulica Reforço.
3. Confirmar no Gerenciador de Anúncios o nome/ID real da campanha de Material Básico Ensacado, pra saber onde entrar com o conjunto novo.
4. Produzir os 2 criativos (foto real de produto na loja, ou mascote como alternativa) para Kit Cerca e Portão e Kit Cobertura Completa.
5. Confirmar com o Tony se a categoria corrompida "MD-MD-MD..." já tem previsão de correção no ERP, isso libera R$ 102 mil de estoque parado pra reclassificação e eventual campanha futura.

## Próximos passos

1. Levar a priorização (seção 1) e os 2 combos prontos (seção 2) pro Tony validar percentual de desconto.
2. `@webdesigner` ou a equipe interna produz os 2 criativos assim que o Tony aprovar o ângulo.
3. Subir os 2 anúncios como conjunto novo dentro da campanha de Material Básico Ensacado (seção 3), sem abrir orçamento novo nesta fase.
4. Rodar 3 a 4 semanas e comparar CTR/custo por resultado com os criativos atuais antes de pedir orçamento incremental ao Tony.
5. `@analista-dados` inclui a taxa de anexo do Kit Cerca e Portão e do Kit Cobertura Completa no próximo dashboard, mesma métrica já usada nos outros 10 kits por fase de obra.
6. Cobrar do Tony as 3 correções de cadastro listadas na seção 5, item 3, antes da próxima rodada de Curva ABC.

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
