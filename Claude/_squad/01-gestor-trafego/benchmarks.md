# Benchmarks de Tráfego por Nicho

> Referências para CPL, CPA, ROAS e CTR por tipo de negócio e tipo de oferta. Usar para avaliar se uma conta está performando bem, mal ou dentro do esperado. Todos os valores em R$ e baseados em campanhas no Brasil (2025-2026).
>
> **Nota MatCon:** a Pillar atende loja de material de construção. Não existe uma linha de benchmark de mercado específica para esse nicho, então as tabelas abaixo foram mantidas por proximidade (Imóveis e Construção para reforma/orçamento, E-commerce e Varejo para o lado de venda de produto, Serviços B2B para o relacionamento com profissional recorrente). Trate como ponto de partida e recalibre com o histórico real de campanha do cliente assim que houver dado suficiente (`Operacional/clientes/<nome>/outputs/`).

---

## Como usar este arquivo

1. Identificar o nicho e tipo de oferta do cliente
2. Comparar o resultado atual com o benchmark
3. Se estiver acima do benchmark de "Atenção", aplicar diagnóstico (`diagnostico-de-conta.md`)
4. Se estiver abaixo do benchmark de "Ótimo", escalar o budget com cuidado

**Importante:** Benchmarks são médias. Um resultado fora do benchmark pode ser porque a conta está mal otimizada OU porque o nicho local específico tem CPL diferente. Sempre calibrar com o histórico do próprio cliente.

---

## Benchmarks por nicho: Meta Ads

### Imóveis e Construção

| Tipo | CPL Ótimo | CPL Normal | Taxa de visita ao imóvel |
|---|---|---|---|
| Lançamento residencial | R$ 50-120 | R$ 120-300 | 15-30% |
| Imóvel usado (compra) | R$ 40-100 | R$ 100-250 | 20-40% |
| Aluguel | R$ 20-60 | R$ 60-150 | 30-60% |
| Terreno / loteamento | R$ 60-150 | R$ 150-400 | 10-25% |
| Empreendimento comercial | R$ 80-200 | R$ 200-500 | 10-20% |
| Reforma / construção | R$ 30-80 | R$ 80-200 | 20-40% |

**Atenção Meta Ads:** Imóveis são categoria especial. Sem segmentação por CEP pequeno. Usar cidade ou raio amplo.

---

### Serviços para Empresas (B2B)

| Serviço | CPL Ótimo | CPL Normal |
|---|---|---|
| Contabilidade | R$ 40-100 | R$ 100-250 |
| TI / software / automação | R$ 60-150 | R$ 150-400 |
| Marketing digital (agência) | R$ 50-120 | R$ 120-300 |
| RH / recrutamento | R$ 40-100 | R$ 100-250 |
| Segurança patrimonial | R$ 30-80 | R$ 80-200 |
| Limpeza corporativa | R$ 20-60 | R$ 60-150 |
| Fornecedor / atacado | R$ 25-70 | R$ 70-180 |

**B2B:** Ticket alto justifica CPL mais caro. Um lead de R$ 200 que fecha contrato de R$ 5.000/mês é excelente.

---

### E-commerce e Varejo

| Ticket médio | ROAS Ótimo | ROAS Normal | ROAS Crítico |
|---|---|---|---|
| Abaixo de R$ 80 | Acima de 8x | 4x-8x | Abaixo de 4x |
| R$ 80-200 | Acima de 6x | 3x-6x | Abaixo de 3x |
| R$ 200-500 | Acima de 5x | 2,5x-5x | Abaixo de 2,5x |
| Acima de R$ 500 | Acima de 4x | 2x-4x | Abaixo de 2x |

**Como calcular ROAS mínimo para breakeven:**
```
ROAS mínimo = 1 / margem bruta do produto
Exemplo: produto com 40% de margem → ROAS mínimo = 1 / 0,4 = 2,5x
Abaixo de 2,5x o cliente está perdendo dinheiro com tráfego.
```

---

## Benchmarks de métricas intermediárias (Meta Ads)

| Métrica | Bom | Mediano | Ruim |
|---|---|---|---|
| CPM (R$) | 15-35 | 35-70 | Acima de 70 |
| CTR de link (%) | Acima de 1,5% | 0,8-1,5% | Abaixo de 0,8% |
| Hook Rate vídeo (%) | Acima de 30% | 15-30% | Abaixo de 15% |
| Frequência | 1,5-3x | 3-5x | Acima de 5x |
| Taxa de conversão LP, lead gratuito | Acima de 20% | 10-20% | Abaixo de 10% |
| Taxa de conversão LP, produto pago | Acima de 5% | 2-5% | Abaixo de 2% |

---

## Benchmarks Google Ads: Search

| Métrica | Bom | Mediano | Ruim |
|---|---|---|---|
| CTR Search (%) | Acima de 7% | 3-7% | Abaixo de 3% |
| Quality Score | 7-10 | 5-6 | Abaixo de 5 |
| Taxa de conversão Search | Acima de 10% | 5-10% | Abaixo de 5% |
| Parcela de impressões | Acima de 60% | 30-60% | Abaixo de 30% |

---

## Fórmulas rápidas

### CPL máximo que o cliente pode pagar (para não ter prejuízo)
```
CPL máximo = Ticket médio × Taxa de fechamento × Margem bruta
Exemplo:
  Ticket = R$ 2.000
  Taxa de fechamento = 20% (1 em cada 5 leads fecha)
  Margem = 50%
  CPL máximo = 2.000 × 0,20 × 0,50 = R$ 200
  Ou seja: pagar até R$ 200 por lead ainda é lucrativo.
```

### ROAS mínimo para breakeven
```
ROAS mínimo = 1 / margem bruta
Exemplo: 35% de margem → ROAS mínimo = 2,86x
Qualquer coisa abaixo de 2,86x = o tráfego está destruindo margem.
```

### ROI do tráfego
```
ROI = (Receita gerada pelo tráfego - Investimento em tráfego) / Investimento × 100
Exemplo:
  Investimento: R$ 3.000
  Receita atribuída: R$ 12.000
  ROI = (12.000 - 3.000) / 3.000 × 100 = 300%
```

---

## Fatores que afetam os benchmarks

| Fator | Como afeta |
|---|---|
| Sazonalidade | Janeiro (frio para serviços), dezembro (quente para e-commerce) |
| Competição local | Cidades grandes têm CPM 20-50% mais alto que interior |
| Qualidade do criativo | Criativo fraco pode dobrar o CPL |
| Alinhamento anúncio/LP | Desconexão aumenta CPL em 30-80% |
| Maturidade da conta | Pixel com histórico converte 20-40% mais barato |
| Qualidade da oferta | Oferta fraca: nenhuma otimização salva |
| Velocidade da LP | LP que abre em +3s perde 40% das conversões |
