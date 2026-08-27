# Estratégia de Kits por Fase de Obra e Playbook de Vendas, Construmais

**Cliente:** Construmais (Tony Carvalho Barbosa)
**Fonte dos dados:** os mesmos 4 relatórios de Curva ABC do ERP Pontual Tecnologia usados em `outputs/07-2026/Analises/23-diagnostico-estoque.md` (01/05/2025 a 30/06/2026, 14 meses). Faturamento total, custo, margem agregada e Curva ABC já confirmados naquele diagnóstico, não repetidos aqui em detalhe.
**Metodologia:** Pilar 3 (Combo de Produtos) e Pilar 4 (Vendedor de Elite) do Método Viga Mestra.
**Status:** v1, sujeito a refinamento.

**Nota de escopo contratual:** Pilar 3 (Combo de Produtos) não está detalhado como item formal no Anexo I hoje com a Construmais, conforme `CLIENTE.md`, seção Contrato com a Pillar. Isso é só uma decisão de risco jurídico da Pillar sobre o que fica formalmente descrito e cobrado no contrato, o Método Viga Mestra é único e a parte de kits deste documento é entregue como as demais. O que ainda depende de confirmação do Tony é incluir o Pilar 3 como item explícito e faturável do contrato (upsell contratual), não a execução do trabalho em si. O Pilar 4 (Treinamento Comercial / Vendedor de Elite) já está detalhado no Anexo I, então a seção de playbook de vendas abaixo tem também essa cobertura formal.

---

## 1. Correção de metodologia em relação à versão anterior

Duas correções importantes em cima do que já tinha sido levantado antes:

1. **Giro (quantidade vendida) e margem/faturamento em R$ são coisas diferentes e não devem ser confundidas na escolha de âncora de kit.** Produtos como Areia Fina, Pedra Britada e Pedra Calcária aparecem no topo de margem bruta em R$ por causa do preço unitário alto (venda por m³), mas não têm giro alto em quantidade. Eles servem como produto de margem/complemento no kit, nunca como âncora.

2. **Erro de pareamento técnico no Kit Alvenaria já registrado em `outputs/07-2026/Analises/23-diagnostico-estoque.md`.** Aquele arquivo tem "Tijolo C/8 Furos + Argamassa Cola Forte AC-II 15kg" como composição do Kit Alvenaria. Isso está tecnicamente errado: a classificação AC-I/AC-II/AC-III (norma ABNT NBR 14081) identifica argamassa colante para assentar piso ou cerâmica, não para assentar tijolo. Assentamento de alvenaria usa traço de cimento e areia, não argamassa colante industrializada. A composição correta:
   - **Kit Alvenaria:** Tijolo C/8 Furos + Areia Fina (para o traço de assentamento, junto com o cimento já coberto no Kit Estrutura/Fundação)
   - **Argamassa Cola Forte AC-II** passa para o Kit Revestimento/Acabamento, pareada com piso cerâmico, onde ela realmente se aplica

A tabela "Candidatos a kit" de `outputs/07-2026/Analises/23-diagnostico-estoque.md` deve ser lida com essa correção. A versão completa e corrigida está na seção 3 abaixo.

---

## 2. Faturamento por categoria dentro de cada Curva ABC

Complementa a tabela "Participação por categoria" já existente no diagnóstico de estoque, agora quebrada por Curva.

### Curva A (R$ 1.846.434,98, 59,91% do total)
Material Básico domina com 65,66% da própria Curva A (39,34% do faturamento total da loja). Depois vêm Hidráulica (6,47%), Cobertura (6,14%), Argamassas e Rejunte (5,77%) e Pintura (4,56%). Material Básico é o motor de giro da Curva A.

### Curva B (R$ 772.785,61, 25,08% do total)
Perfil diferente da Curva A: aqui quem lidera é Pintura (16,22% da Curva B) e Hidráulica (13,99%), seguidos de Material Elétrico (12,02%) e só depois Material Básico (11,76%). A Curva B puxa mais para acabamento e instalação do que para material de obra bruta.

### Curva C (R$ 462.597,63, 15,01% do total)
Cauda longa clássica: Ferramentas (19,15% da Curva C), Hidráulica (17,62%), Ferragem (14,52%) e Material Elétrico (13,46%) lideram, com Material Básico caindo para só 1,54% da Curva C. É a faixa mais fragmentada, candidata natural para revisão de mix e desova de estoque parado (ver `outputs/07-2026/Analises/23-diagnostico-estoque.md`, seção Estoque).

---

## 3. Estratégia de 10 kits por fase de obra (corrigida)

### Fase 1, Fundação/Concretagem
- Âncora: Cimento Montes Claros CPII F 32 (3.700 sc, margem 14,4%, giro alto e a pior margem do top 15 de giro)
- Complemento: Areia Média (460 m³, margem 46,6%), Pedra Britada 1/19 (291 m³, margem 53,4%), Vergalhão CA-50, Malha Soldada Q-196

### Fase 2, Estrutura de Laje Pré-moldada
- Âncora: Bloco p/Laje 30x07x20 (1.819 un, margem 52,9%, top 15 giro geral)
- Complemento: Treliça Premoldada TG8 (1.170 m, margem 54,3%), Canaleta Premoldada (margem aproximada de 53%)

### Fase 3, Alvenaria (levante de parede), corrigida
- Âncora: Tijolo C/8 Furos 09x19x19 (282.430 un, margem 33,8%, o maior giro de toda a loja)
- Complemento correto: **Areia Fina** (1.343 m³, margem 27,8%, para o traço de assentamento, junto com o cimento já coberto na Fase 1)
- A versão anterior tinha Argamassa AC-II por engano nesse kit. Ela não serve para assentar tijolo, ver seção 1.
- **Margem combinada recalculada:** 31,38% (Tijolo + Areia Fina), contra 33,82% do Tijolo isolado, uma queda de 2,44 pontos percentuais. Diferente dos outros kits deste documento, esse pareamento tecnicamente correto reduz a margem percentual, porque a Areia Fina tem margem própria mais baixa que o Tijolo. O argumento comercial aqui não é ganho de margem, é captura de um par de produtos que a obra já compra junto (cimento e areia, cobertos nas Fases 1 e 3, mais o tijolo).

### Fase 4, Cobertura
- Âncora: Telha Canal Russa 1ª e 2ª (11.089 e 22.085 un, margens de 65% e 52,7%, giro alto e margem alta ao mesmo tempo)
- Opção econômica: Telha Canal Carnaúba 1ª (2.000 un, margem 24,2%)
- Único caso do catálogo em que o próprio produto de giro já vem com margem boa, sem precisar de reforço.

### Fase 5, Impermeabilização (pós-laje, pré-revestimento)
- Âncora (giro dentro da categoria): Tarugo PE 06mm Prorubber (500 un, margem 67,4%, a maior margem percentual desse grupo)
- Complemento: Adesivo Selante PU 40 Gold (445 un, margem 44,4%), Cimento Asfáltico Oxidado Viapol

### Fase 6, Instalações Hidráulicas de Esgoto
- Âncora: Tubo PVC ESG 200mm (Krona/Corplastik)
- Complemento: Joelho 45 PVC ESG 200mm Fortlev (margem 66,2%, a maior margem percentual de todo o catálogo), Luva PVC ESG 200mm

### Fase 7, Instalações Hidráulicas de Água Fria e Metais
- Âncora: Joelho 90 PVC Sold 20mm Krona (989 un, margem 63,3%, giro dentro da categoria)
- Complemento: Luva PVC Sold 20mm Krona (579 un, margem 64,9%), Te PVC Sold 20mm Krona (386 un, margem 59%), Registro Gaveta Metal 1502 Deca (1.381 un, margem 42,5%)

### Fase 8, Instalações Elétricas
- Âncora: Cabo Flex 2,5mm Vermelho/Azul Megatron (958 e 808 un, margem próxima de 40%, giro dentro da categoria)
- Complemento: Caixa Plástica Embutir 4x2 Krona (868 un, margem 46,6%)

### Fase 9, Revestimento/Acabamento (aqui a AC-II entra corretamente)
- Âncora: Piso Cerâmico Riviera 37x59cm (175 un, margem 35,2%, giro dentro da categoria)
- Complemento: **Argamassa Cola Forte AC-II 15kg** (2.099 sc, margem 38,1%, produto correto para assentar o piso), Rejunte Porcelanato/Cerâmica Quartzolit, Nivelador Eco Ved Cortag

### Fase 10, Pintura
- Âncora: Massa PVA Branco Neve 3L (355 un, margem 39,3%, giro dentro da categoria)
- Complemento/upsell: serviço de tintometria (margem de até 99%, é o serviço de tingir a tinta)
- Tinta em pó CH-1 Megao tem giro menor mas ticket mais alto, opção premium a oferecer junto.

### Kits transversais, usados em qualquer fase

**Fixação/Ferragem (balcão rápido)**
- Âncora: Parafuso Auto Broc Zinc 12x1 Jomarca (13.027 un) e Bucha Nylon 06/08/10 Fixaforte (2.217 / 4.133 / 1.945 un), todos no top 15 geral de giro, margens de 52% a 67%
- Não precisa de complemento externo, os próprios itens de giro já têm margem alta. Ideal para checklist fixo de caixa.

**Ferramentas de Corte/Abrasivos**
- Âncora: Lixa Massa G120 Norton (918 un, margem 66,8%)
- Complemento: Disco de Corte 4.1/2 Starrett (601 un, margem 61,2%)

**Prioridade de lançamento sugerida:** Fases 1 a 4 têm âncoras de giro comprovadas contra o catálogo inteiro, junto com o kit transversal de Fixação, lançar primeiro. As demais fases usam líder de giro dentro da própria categoria (volume alto para aquele nicho, não para a loja toda), lançar numa segunda etapa.

---

## 4. Playbook de execução comercial (Pilar 4, dentro do escopo contratado)

### 4.1 Onde o kit precisa aparecer (3 pontos de contato)
- **Balcão de atendimento, o mais importante:** não pode depender da memória do vendedor. Precisa virar checklist obrigatório: quando o vendedor bate Tijolo, Cimento ou Tubo PVC 200mm no PDV, o sistema (ou uma folha impressa no caixa, se o Pontual não permitir regra automática) sugere o complemento antes de fechar.
- **Orçamento de obra:** quando o cliente pede orçamento de material para laje, parede, cobertura etc., o kit já vem montado na proposta como composição padrão, não como sugestão posterior.
- **Entrega/retirada:** se o cliente já comprou o item âncora e não levou o complemento, é o momento de reforçar (por exemplo: "já separou a areia para esse tijolo?").

### 4.2 Como apresentar
- Dar nome ao kit ("Kit Alvenaria", "Kit Cobertura Completa") em vez de tratar como produto mais produto solto.
- Preço do kit levemente abaixo da soma individual, um desconto de 3% a 5% já costuma bastar. O complemento tem margem alta o suficiente para absorver o desconto sem sacrificar o resultado.
- Tabela de referência fixa no caixa e no orçamento, com a proporção de complemento por unidade de âncora baseada na proporção real de venda dos dados, tirando a decisão da mão do vendedor.

### 4.3 Prioridade de treinamento
Não lançar os 10 de uma vez. Começar pelos 3 com dado mais forte:
1. **Kit Alvenaria** (tijolo + areia fina): os dois maiores giros da loja, venda praticamente automática.
2. **Kit Fixação** (parafuso + bucha): ticket baixo, decisão rápida, ótimo para treinar o vendedor a nunca fechar venda sem perguntar.
3. **Kit Hidráulica PVC 200mm** (tubo + joelho/luva): maior margem percentual do catálogo, mas depende mais do vendedor lembrar, é venda de projeto, não balcão corrido.

Depois de 30 dias rodando, expandir para os outros 7 kits.

### 4.4 Como medir se está funcionando
Pedir ao Tony, daqui a 60 a 90 dias, para tirar do Pontual a mesma Curva ABC e comparar a taxa de anexo: das vendas do produto âncora, quantas vieram acompanhadas do complemento no mesmo cupom. Se esse número subir, o kit está funcionando. Se não subir, o problema é execução no balcão, não o kit em si.

---

## 5. Gancho estratégico para a conversa Viga Mestra / Pillar

Os kits mostram o "o quê" (dado concreto, líder de giro por categoria, oportunidade de margem clara), mas a execução, checklist no PDV, treinamento, medição de taxa de anexo, é o "como". Esse acompanhamento contínuo é o tipo de trabalho que a metodologia Viga Mestra da Pillar oferece de forma recorrente, e é ponte natural entre este diagnóstico e uma eventual expansão de escopo com o Tony para incluir o Pilar 3 formalmente no contrato.

---

## Próximos passos

1. Corrigir a composição do Kit Alvenaria em qualquer material já produzido ou em produção que tenha usado a versão antiga (Tijolo + Argamassa AC-II).
2. Confirmar com o Tony se ele topa expandir o contrato para incluir o Pilar 3 (Combo de Produtos) formalmente, já que o playbook de vendas (Pilar 4) já está no escopo e os dois pilares se complementam na prática.
3. `@copywriter` pode usar os 10 kits e o playbook de vendas para roteiro de atendimento e follow-up de orçamento (Pilar 4, já contratado).
4. Antes de lançar qualquer kit em campanha paga, confirmar com o Tony se ele já quer formalizar o Pilar 3 como item explícito do contrato (upsell contratual), o trabalho de kit em si já é entregue como parte do método único.
