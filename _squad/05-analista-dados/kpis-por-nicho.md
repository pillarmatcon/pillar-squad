# KPIs por Tipo de Negócio

> Quais métricas acompanhar, com qual frequência e o que significa cada número, por tipo de negócio. Usar em conjunto com os benchmarks do Agente 01.
>
> **Nota MatCon:** a Pillar atende loja de material de construção, modelo mais próximo de varejo físico com cauda B2B (profissional recorrente) do que de serviço com agendamento. A seção "E-commerce e varejo online" abaixo é o ponto de partida principal, adaptando "pedido" para "venda de balcão/orçamento fechado" conforme o caso. As seções de outros tipos de negócio foram removidas para manter o arquivo focado; se a Pillar atender um cliente fora do nicho MatCon, adicionar de volta a seção equivalente aqui.

---

## Como usar este arquivo

Cada tipo de negócio tem um conjunto de KPIs primários (os que determinam se a campanha está funcionando) e secundários (os que ajudam a entender o porquê). No relatório para o cliente, focar nos primários. Os secundários ficam na análise interna do gestor.

---

## E-commerce e varejo online

**Exemplos:** loja virtual, delivery, marmita fit, artesanato, roupas, acessórios.

**O cliente quer saber:** quanto vendeu e quanto lucrou com o tráfego.

### KPIs primários

| KPI | Fórmula | Meta típica | Pergunta que responde |
|---|---|---|---|
| ROAS | Receita atribuída ÷ Investimento | Acima de 3x (varia por margem) | "Estou tendo retorno?" |
| Pedidos/semana | Total de pedidos gerados via tráfego | Depende do negócio | "A campanha está gerando compras?" |
| Ticket médio | Receita total ÷ pedidos | Comparar com histórico | "Mudou o perfil de quem compra?" |
| Custo por pedido (CPA) | Investimento ÷ pedidos | Ver benchmarks por ticket | "Quanto pago por cada venda?" |

### KPIs secundários

| KPI | O que indica |
|---|---|
| Taxa de conversão da loja | Visitantes que compram, abaixo de 1% é problema |
| Valor médio por sessão | Receita ÷ sessões únicas |
| Taxa de abandono de carrinho | Se o checkout está com problema |
| Retorno de clientes | % de pedidos de clientes que já compraram |

### ROAS de breakeven por margem

| Margem bruta | ROAS mínimo para não perder dinheiro |
|---|---|
| 20% | 5,0x |
| 30% | 3,3x |
| 40% | 2,5x |
| 50% | 2,0x |
| 60% | 1,7x |

---

## KPIs universais (todo tipo de negócio)

Independente do nicho, estes indicadores sempre entram no relatório:

| KPI | O que mede | Verde | Amarelo | Vermelho |
|---|---|---|---|---|
| CTR de link | Eficácia do criativo em gerar clique | Acima de 1,5% | 0,8-1,5% | Abaixo de 0,8% |
| Taxa de conversão LP | Eficácia da landing page | Acima de 15% (lead grátis) | 8-15% | Abaixo de 8% |
| Frequência do anúncio | Fadiga do criativo | 1,5-3x | 3-5x | Acima de 5x |
| CPM | Custo de alcance | R$ 15-35 | R$ 35-70 | Acima de R$ 70 |

---

## Formato de tabela de KPIs para o dashboard

Usar este modelo para preencher o `template-dashboard.html`:

```
PERÍODO: [data início] a [data fim]
PLATAFORMA: Meta Ads / Google Ads / ambas

KPI               | RESULTADO  | META      | STATUS
------------------|------------|-----------|--------
Investimento      | R$ X.XXX   | R$ X.XXX  | -
Impressões        | XX.XXX     | -         | -
Cliques           | X.XXX      | -         | -
CTR               | X,X%       | >1,5%     | 🟢/🟡/🔴
Leads             | XXX        | XXX       | 🟢/🟡/🔴
CPL               | R$ XX      | R$ XX     | 🟢/🟡/🔴
Agendamentos      | XX         | XX        | 🟢/🟡/🔴
CPA               | R$ XX      | R$ XX     | 🟢/🟡/🔴
Taxa LP           | XX%        | >15%      | 🟢/🟡/🔴
ROAS              | X,Xx       | >Xx       | 🟢/🟡/🔴 (se aplicável)
```
