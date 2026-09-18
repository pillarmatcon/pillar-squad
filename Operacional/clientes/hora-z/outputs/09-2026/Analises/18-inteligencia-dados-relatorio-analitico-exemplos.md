![Pillar](../../../../../../_squad/_shared/marca-pillar/logo-pillar.png)

# Relatório Analítico — Diagnóstico Pilar 1, Hora Z
**Marketing com Resultado Concreto**
Pillar · Método Viga Mestra, Pilar 1 (Inteligência de Dados)

---

> Este relatório traz os principais produtos usados como exemplo em cada seção da apresentação do diagnóstico (não a lista completa de SKUs, só os itens mais representativos), e uma seção dedicada aos outliers que foram deixados de fora de cada cálculo, com o motivo de cada exclusão. Fonte de todos os números: `diagnostico-curva-abc.md` e `diagnostico-giro-estoque.md`, em `outputs/_diagnosticos/inteligencia-dados/`, atualizados em 18/09/2026. Relatórios de origem: `Curva_Abc.xlsx` e `Estoque.xlsx`, recebidos do cliente em 15/09/2026.

## 1. Indicador de giro (quantidade) x Curva ABC (faturamento)

A classificação que vem pronta do ERP do cliente é por quantidade vendida, não é Curva ABC. Os exemplos abaixo mostram por que as duas leituras divergem:

| Produto | Classe por quantidade | Classe por faturamento | Leitura |
|---|---|---|---|
| Cimento Supremo 50kg | B | **A** | Ticket alto, não volume, é o que fatura (704 un., R$ 27.868,00) |
| Tijolo 6 furos 09x14x24 (22114) | A | A | Único caso em que as duas leituras coincidem |
| Vermelho segurança epóxi piso Farben (21070) | C | **A** | Só 16 unidades vendidas, mas 2º maior faturamento da loja (R$ 8.638,46) |
| Bucha plástica tijolo oco 06mm (1589) | B | C | 460 unidades vendidas, mas valor unitário baixo demais para pesar no faturamento (R$ 46,00) |

## 2. Curva ABC oficial, por faturamento

Base: R$ 291.831,91, 1.185 SKUs (sem os 2 lançamentos "Plataforma", ver seção de outliers). Classe A = 173 SKUs (79,9% do faturamento), B = 369 SKUs (15,0%), C = 643 SKUs (5,0%).

| # | Produto | Categoria | Faturamento | Margem |
|---|---|---|---|---|
| 1 | Cimento Supremo 50kg | Básico | R$ 27.868,00 | 16,8% |
| 2 | Vermelho segurança epóxi piso Farben | Acabamento | R$ 8.638,46 | 0,3% (custo R$ 261,69 x preço R$ 262,41, confirmar cadastro) |
| 4 | Argamassa Superkola 3Mais 20kg | Básico | R$ 7.166,12 | 37,9% |
| 6 | Tijolo 6 furos 09x14x24 | Básico | R$ 6.452,00 | 36,8% |

## 3. Categorias por faturamento e margem

| Categoria | Faturamento | % do total | Margem ponderada | Cobertura |
|---|---|---|---|---|
| Básico | R$ 145.326,68 | 49,8% | 29,9% | 46,1% do faturamento da categoria |
| Acabamento | R$ 35.804,53 | 12,3% | 6,8%* | 30,3% do faturamento da categoria |

*Puxada quase só pelo item Vermelho segurança epóxi piso Farben (margem 0,3%, R$ 8.638 de faturamento), não representa o departamento inteiro.

Top produtos usados como exemplo de cada categoria: **Básico** — Cimento Supremo 50kg, Argamassa Superkola 3Mais, Tijolo 6 furos 09x14x24. **Acabamento** — Vermelho segurança epóxi piso Farben, Epóxi piso branco Farben.

## 4. Estoque por categoria

| Categoria | Valor bruto | Valor sem outliers de cadastro |
|---|---|---|
| Básico | R$ 20.890,00 | R$ 10.934,68 |
| **Total (443 SKUs)** | **R$ 40.661,03** | **R$ 28.474,77** |

Básico perde quase metade do valor bruto só por causa de 4 itens com custo mal cadastrado (ver outliers abaixo).

## 5. Top produtos em estoque (valor e quantidade)

| Produto | Categoria | Valor em estoque |
|---|---|---|
| Cimento Supremo 50kg | Básico | R$ 3.135,00 a R$ 3.505,50 (2 fornecedores cadastrados, faixa sem escolha única) |
| Tijolo 6 furos 09x14x24 | Básico | R$ 1.508,40 a R$ 2.436,07 (4 fornecedores, maior variação da lista) |
| Tijolo 6 furos 09x14x29 | Básico | 2.598 unidades, maior quantidade física do estoque |

## 6. Estoque parado, por tempo

Lote mais antigo: 22/12/2025 (23 SKUs sem venda desde então, candidatos mais fortes a estoque parado de verdade). Exemplos: Piscina Fast Set 2.300L (R$ 241,33), Jogo brocas/talhadeira SDS Plus 13 peças (R$ 155,00).

**Achado de cadastro dentro deste grupo:** a Válvula click 1.1/4" (código 20357) está contando R$ 0,00 no total de estoque parado porque a compra mais recente cadastrada tem custo zerado por erro; pelo outro fornecedor, o valor real seria R$ 53,72.

## 7. Matriz giro x margem e risco de ruptura

| Quadrante | SKUs | Valor em estoque |
|---|---|---|
| Estrela | 85 | R$ 2.942,70 |
| Isca | 78 | R$ 24.446,22 |
| Reserva de lucro | 62 | R$ 1.603,65 |
| Candidato a liquidar | 70 | R$ 5.375,16 |

**Caso de exemplo mais relevante:** Argamassa Massa Reboco 20kg (código 12010) está classificada como Estrela (margem 56,5%), mas tem um segundo fornecedor cadastrado com custo mais alto, que derrubaria a margem para 24,2%, mudando o quadrante para Isca. Como esse item é ingrediente de um kit sugerido (seção 8), a classificação é tratada como provisória até o cliente confirmar o custo.

**Risco de ruptura:** Telha cerâmica esmaltada (estoque zerado, vendeu 150 unidades), Ferro 3/8 e Ferro 5/16 (9 e 10 unidades em estoque, giro alto).

## 8. Kits de produto propostos (Pilar 3)

- **Kit 1:** Cimento Supremo 50kg (isca, margem 16,8%) + Argamassa Massa Reboco 20kg (margem provisória, 56,5% a 24,2%) ou Argamassa Extrakolla 2 (alternativa estável, margem 42,2%, fornecedor único).
- **Kit 2:** Tijolo 6 furos / Bloco de concreto (isca, giro altíssimo) + Argamassa Superkola 3Mais 20kg (margem 37,9%).

---

## Outliers excluídos, explicitamente, e o porquê

Nenhum destes itens foi apagado do relatório de origem, só tratado fora do cálculo principal quando distorceria a leitura. Cada um está documentado nos diagnósticos-fonte, com a planilha e a aba onde pode ser conferido linha a linha.

### 1. Dois lançamentos "Plataforma" — excluídos do faturamento "sem outliers"

| Item | Faturamento | Motivo da exclusão |
|---|---|---|
| Plataforma -Z-45/25J RT | R$ 133.748,71 | Código fora do padrão do catálogo, aparece uma única vez, sem como confirmar pela planilha se é venda de equipamento, aluguel registrado como venda ou erro de lançamento |
| 114887 - Plataforma - Z-3422 DC | R$ 95.674,30 | Mesmo motivo |

Juntos somam R$ 229.423,01, quase 44% do faturamento bruto total (R$ 521.254,92). Toda a Curva ABC, a participação por categoria e a margem por categoria deste relatório usam a base sem esses dois lançamentos (R$ 291.831,91). **Pendente de confirmação do cliente antes de qualquer decisão de mídia por categoria.**

### 2. SKUs com custo cadastrado acima do preço de venda — excluídos do "top valor em estoque sem outliers" e tratados com margem não confiável

| Código | Produto | Custo cadastrado | Preço de venda | Motivo |
|---|---|---|---|---|
| 22483 | Bucha plástica c/ anel concreto 8mm | R$ 11,25 | R$ 0,05 | Custo 225x maior que o preço, erro claro de cadastro. Sozinho inflava o topo do ranking bruto de valor em estoque em R$ 5.377,50 |
| PRD00016 | Estribo Flexfer 10x16 4,2mm | R$ 60,00 | R$ 1,20 | Mesmo padrão, inflava o ranking em R$ 2.520,00 |
| 16420 | Corante base d'água 50ml xadrez preto | R$ 50,02 | R$ 7,50 | Mesmo padrão |
| 21603 | Telha cerâmica esmaltada | R$ 8,00 | R$ 1,60 | Este item também está em risco de ruptura (estoque zerado); o cadastro deve ser corrigido antes de repor, para não comprar de novo com margem errada |

16 itens no total têm esse padrão. Motivo geral: indica erro de cadastro (unidade de compra diferente da unidade de venda, custo de lote lançado como custo unitário, ou preço de venda desatualizado), não necessariamente prejuízo real na venda.

### 3. 33 SKUs com custo cadastrado zerado — excluídos do cálculo de margem por categoria e da matriz giro x margem

Custo zero impede calcular margem real. Esses itens foram tratados como "margem indefinida", nunca como 0% nem como 100%, e não entraram nas médias ponderadas por categoria nem na classificação de quadrante da matriz giro x margem quando cruzados com a Curva ABC. Exemplos: Broca AR 06.5mm blister C/10 (código 1021, preço R$ 6,15), Broca encaixe SDS Plus 10x160mm (código 1044, preço R$ 14,20).

### Nota à parte: 86 SKUs com mais de um fornecedor não são outliers, são ambiguidade legítima

Diferente dos itens acima, os 86 SKUs comprados de mais de um fornecedor (ex: Cimento Supremo 50kg, com custo de R$ 33,00 ou R$ 36,90 dependendo do fornecedor) não foram excluídos de nada. Cada custo cadastrado é real, só existe mais de um. Por isso não entram nesta lista de outliers, aparecem com a faixa mínimo-máximo lado a lado nas quatro tabelas em que a margem influencia a leitura, para decisão em reunião com o cliente, e não como erro de cadastro.

---

**Arquivos de referência completos:**
- `outputs/_diagnosticos/inteligencia-dados/diagnostico-curva-abc.md`
- `outputs/_diagnosticos/inteligencia-dados/diagnostico-giro-estoque.md`
- `outputs/09-2026/Arquivos/15-inteligencia-dados-curva-abc-padronizada_acumulado-ate-2026-09-15.xlsx`
- `outputs/09-2026/Arquivos/15-inteligencia-dados-estoque-giro-margem_snapshot-2026-09-15.xlsx`

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados

*Pillar · Marketing com Resultado Concreto*
