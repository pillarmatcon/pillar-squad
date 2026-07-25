# Diagnóstico de Conta de Tráfego

> Checklist sequencial para diagnosticar uma conta de Meta Ads ou Google Ads que já está rodando. Seguir a ordem, cada etapa depende da anterior.

---

## Quando usar este diagnóstico

- Cliente chegou com campanha rodando e quer melhorar os resultados
- Conta "travou", parou de escalar ou CPL subiu muito
- Cliente quer saber por que não está tendo retorno
- Antes de propor qualquer mudança estrutural, diagnosticar primeiro, mudar depois

**Regra de ouro:** Nunca propor mudança sem antes entender o que está causando o problema. Mudar tudo ao mesmo tempo é a pior estratégia, não dá para saber o que funcionou.

---

## Funil de diagnóstico Meta Ads

Seguir sempre nesta ordem. O problema está no primeiro ponto que está fora do benchmark.

```
IMPRESSÕES → CLIQUES → LEADS/CONVERSÕES → CUSTO

Se as impressões são baixas → problema de alcance (budget, bid, rejeição do anúncio)
Se as impressões são altas mas os cliques são baixos → problema no criativo
Se os cliques são bons mas os leads são baixos → problema na landing page
Se os leads são bons mas o CPA é alto → problema de qualidade do lead / funil de venda
```

---

## Meta Ads: Diagnóstico passo a passo

### Etapa 1: Verificar saúde da conta

| Item | O que verificar | Como verificar |
|---|---|---|
| Status da conta | Ativa, restrita ou desabilitada | Gerenciador de Negócios → Qualidade da Conta |
| Pixel ativo | Evento de conversão recebendo dados | Events Manager → verificar se Pixel está "Ativo" |
| Método de pagamento | Fatura em dia, sem bloqueio | Configurações de Faturamento |
| Política de anúncios | Anúncios rejeitados | Central de Anúncios → filtrar por "Rejeitado" |

**Se a conta estiver restrita:** Não tente consertar campanhas antes de resolver a restrição. Recurso no Facebook Business Support é o único caminho.

---

### Etapa 2: Analisar métricas de topo (alcance e impressões)

**Período de análise:** últimos 30 dias. Nunca analisar menos de 7 dias, muito volátil.

| Métrica | Saudável | Atenção | Problema |
|---|---|---|---|
| CPM (custo por mil impressões) | R$ 15-40 | R$ 40-80 | Acima de R$ 80 |
| Frequência | 1,5-3x | 3-5x | Acima de 5x |
| Alcance | Crescendo | Estável | Caindo semana a semana |

**CPM alto:** audiência muito pequena ou muito concorrida. Soluções: ampliar localização, usar Advantage+ Audience, testar novo público.

**Frequência alta (acima de 5x):** criativo em fadiga. Solução: lançar novos criativos imediatamente, expandir audiência.

---

### Etapa 3: Hook Rate (métrica mais importante para criativos)

**Hook Rate = (ThruPlays de 3 segundos / Impressões) × 100**

No Gerenciador de Anúncios, adicionar a coluna "Reproduções de Vídeo em 3 Segundos".

| Hook Rate | Diagnóstico | Ação |
|---|---|---|
| Acima de 30% | Excelente, o hook está prendendo | Escalar o criativo |
| 20-30% | Bom, testar variações do hook | Manter + testar |
| 10-20% | Fraco, o hook não está funcionando | Criar novos hooks |
| Abaixo de 10% | Crítico, o criativo não está parando o scroll | Pausar e refazer |

**Nota:** Hook Rate só se aplica a vídeos. Para imagens, a métrica equivalente é CTR (cliques no link / impressões).

---

### Etapa 4: Body Rate (engajamento com o conteúdo)

**Body Rate = (Reproduções de 25% do vídeo / Reproduções de 3 segundos) × 100**

Mede quantas pessoas que passaram pelo hook continuam assistindo.

| Body Rate | Diagnóstico | Ação |
|---|---|---|
| Acima de 50% | Excelente, conteúdo engajando | Escalar |
| 30-50% | Bom | Manter |
| Abaixo de 30% | O hook prendeu mas o body perdeu | Melhorar primeiros 10 segundos após o hook |

---

### Etapa 5: CTR (cliques no link)

**CTR de link = Cliques no link / Impressões × 100**

| CTR | Diagnóstico | Ação |
|---|---|---|
| Acima de 2% | Excelente | Escalar |
| 1-2% | Bom | Manter + testar variações |
| 0,5-1% | Fraco, CTA não está funcionando | Melhorar CTA no criativo e copy |
| Abaixo de 0,5% | Crítico | Pausar, refazer criativo |

**Atenção:** Não confundir CTR de link com CTR total (que inclui cliques no perfil, no "ver mais", etc.). Usar sempre CTR de link.

---

### Etapa 6: Taxa de conversão da landing page

**Taxa de conversão = Leads / Visitantes únicos da LP × 100**

Para medir: comparar cliques no link (Meta) com Leads recebidos (LP ou CRM).

| Taxa de conversão LP | Diagnóstico por tipo de oferta |
|---|---|
| Acima de 20% | Excelente (qualquer tipo de oferta) |
| 10-20% | Bom para lead gratuito (consulta, avaliação, orçamento) |
| 5-10% | Aceitável para lead gratuito; fraco para produto pago |
| Abaixo de 5% | Problema na LP, não está convencendo |

**Se a taxa de conversão da LP é baixa mas o CTR é bom:**
- A LP não está alinhada com a promessa do anúncio (desconexão criativo/LP)
- Formulário com muitos campos
- LP lenta (acima de 3s para carregar)
- Copy da LP não resolve a objeção principal
- CTA não está visível no mobile

---

### Etapa 7: CPL (custo por lead)

**CPL = Investimento / Leads gerados**

Comparar com o benchmark do nicho (arquivo `benchmarks.md`).

| CPL vs benchmark | Diagnóstico | Prioridade de ação |
|---|---|---|
| Abaixo de 80% do benchmark | Excelente, escalar com cuidado | Aumentar budget 20% |
| 80-120% do benchmark | Normal | Manter e otimizar gradual |
| 120-200% do benchmark | Caro, investigar gargalo | Aplicar funil de diagnóstico |
| Acima de 200% do benchmark | Crítico, parar e reformular | Auditoria completa |

---

### Etapa 8: Qualidade do lead (pós-conversão)

Mesmo com CPL bom, o lead pode ser lixo. Verificar com o cliente:

- **Taxa de atendimento:** quantos leads atendem o telefone / respondem o WhatsApp?
  - Abaixo de 30%: segmentação errada ou formulário coletando dados genéricos
  - Acima de 60%: saudável

- **Taxa de comparecimento:** para clientes que dependem de agendamento presencial
  - Abaixo de 40%: lead de baixa intenção; mudar oferta ou segmentação
  - Acima de 70%: saudável

- **Taxa de fechamento:** quantos leads viram clientes?
  - Depende do nicho, comparar com histórico do cliente (antes das campanhas)

---

## Google Ads: Diagnóstico passo a passo

### Etapa 1: Verificar estrutura e configurações

| Item | O que verificar |
|---|---|
| Rotação de anúncios | Deve ser "Otimizar: preferir os anúncios com melhor desempenho" |
| Correspondência de palavras-chave | Não usar só ampla sem negativas |
| Lista de negativas | Existe e está atualizada? |
| Extensões | Sitelinks, chamada e local estão ativos? |
| Conversões | Está rastreando conversão real (não só "visualização de página")? |

---

### Etapa 2: Métricas de Search

| Métrica | Referência | Diagnóstico se abaixo |
|---|---|---|
| Parcela de impressões | Acima de 50% | Budget baixo ou Quality Score ruim |
| CTR Search | Acima de 5% | Anúncio não relevante, título fraco |
| Quality Score | Acima de 7 | LP não alinhada com a keyword, copy fraca |
| CPC médio | Ver benchmark por nicho | Palavras muito concorridas, baixar lance |

**Parcela de impressões perdida:**
- Perdida por budget: aumentar budget
- Perdida por rank: melhorar Quality Score (LP + copy de anúncio)

---

### Etapa 3: Análise de palavras-chave

Verificar no relatório de termos de pesquisa:

1. **Quais termos estão gerando conversão?** Transformar em palavras-chave exatas.
2. **Quais termos estão gastando budget sem converter?** Adicionar como negativas.
3. **Termos irrelevantes entrando?** Melhorar lista de negativas.

Regra: revisar o relatório de termos de pesquisa toda semana nas primeiras 4 semanas.

---

## Diagnóstico rápido (versão express para demo)

Se o cliente trouxer uma conta para diagnosticar em 10 minutos, fazer estas 5 perguntas:

```
1. "Qual é o CPL atual?" → compara com benchmark do nicho
2. "Qual o CTR dos anúncios?" → abaixo de 1% = problema no criativo
3. "Qual a frequência dos anúncios?" → acima de 5x = fadiga
4. "Tem pixel/tag de conversão instalado?" → sem pixel = voando no escuro
5. "Qual a taxa de conversão da LP?" → abaixo de 10% = gargalo na página
```

Com essas 5 respostas, já dá para identificar onde está o maior gargalo e propor a ação de maior impacto.

---

## Registro de diagnóstico (template para enviar ao cliente)

```
DIAGNÓSTICO DE CONTA - [CLIENTE] - [DATA]

CONTA: [Meta Ads / Google Ads]
PERÍODO ANALISADO: [data início] a [data fim]
INVESTIMENTO NO PERÍODO: R$ X

RESULTADO ATUAL:
  CPL atual: R$ X
  CPL benchmark do nicho: R$ X
  Variação: +X% ou -X% vs benchmark

PRINCIPAIS ACHADOS:
  [1] [métrica] está [valor] - [diagnóstico em 1 frase]
  [2] ...
  [3] ...

GARGALO PRINCIPAL: [onde está o maior problema]

AÇÕES RECOMENDADAS (ordem de prioridade):
  [1] [ação] - impacto esperado: [X]
  [2] ...
  [3] ...

PRÓXIMA REVISÃO: [data - geralmente 7-14 dias depois]
```
