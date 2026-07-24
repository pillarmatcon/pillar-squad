# Exemplo de Demo: Agente 05-Relatório/Dashboard + Clínica Vital

> **Uso:** demonstração na Aula 4 do evento AgêncIA 100k. Fecha o ciclo da demo, o Agente 01 planejou, os Agentes 02/03/04 executaram, o Agente 05 mede. Tempo total da demo: 4 a 6 minutos.

---

## O que entra como input

O dono da agência traz os dados da semana 1 da campanha da Clínica Vital. Formato: tabela digitada no chat (Tier 1, manual).

```
DADOS DA SEMANA 1 - META ADS - CLÍNICA VITAL
Período: 05/05/2026 a 11/05/2026
Investimento: R$ 1.400

Campanha Savassi:
  Impressões: 48.200
  Cliques: 712
  Leads (formulário): 31
  Agendamentos confirmados: 19

Campanha Lourdes:
  Impressões: 44.600
  Cliques: 698
  Leads (formulário): 28
  Agendamentos confirmados: 17

Dados da landing page (GA4):
  Visitantes únicos: 1.380
  Conversões (formulário enviado): 59
  Tempo médio na página: 1m 42s

Criativos ativos:
  Criativo de oferta (Story + Post): 520 cliques, 38 leads, CPL R$ 36,84
  Imagem estática (equipe/consultório): 890 cliques, 21 leads, CPL R$ 66,67

Semana anterior (histórico):
  Não há - primeira semana de campanha.
```

---

## O que a Bindes/Gui pede ao agente na demo

> "@analista-dados gere o relatório da semana 1 da Clínica Vital com os dados acima. Meta do Agente 01: CPL R$ 30-50, CPA R$ 60-100, 40 agendamentos/semana por unidade."

---

## Output do agente (o que aparece na tela durante a demo)

---

### Arquivo gerado

```
ARQUIVO: clinica-vital-dashboard-semana1.html
Abrir no Chrome → Ctrl+P → Salvar como PDF (A4 Paisagem) para enviar ao cliente
```

---

### Dados preenchidos no dashboard

```
NOME_CLIENTE: Clínica Vital
PERIODO: 05/05 a 11/05/2026
TIPO_CAMPANHA: Meta Ads - Geração de Agendamentos
NOME_AGENCIA: [Nome da Agência do Aluno]
STATUS_GERAL: normal
TEXTO_STATUS_GERAL: Dentro do esperado

KPI DESTAQUE:
  LABEL: Agendamentos na semana
  VALOR: 36
  META: 80/mês (20/semana por unidade)

INVESTIMENTO: 1.400
PLATAFORMA: Meta Ads (Savassi + Lourdes)

CPL: 23,73  (1.400 ÷ 59 leads)
META_CPL: 30-50
STATUS_CPL: otimo  ← CPL abaixo da meta (ótimo)

LABEL_CPA: Custo por agendamento
CPA: 38,89  (1.400 ÷ 36 agendamentos)
META_CPA: 60-100
STATUS_CPA: otimo

CTR: 1,45%  ((712+698) ÷ (48200+44600) × 100)
STATUS_CTR: normal

TAXA_LP: 4,28%  (59 ÷ 1380 × 100)
STATUS_TAXA_LP: atencao  ← abaixo de 10%, merece atenção

LEADS: 59
META_LEADS: 80-120/mês (20-30/semana)
STATUS_LEADS: normal

IMPRESSOES: 92.800
```

---

### Tabela de criativos

```
Criativo de oferta (Story + Post):
  Impressões: ~55.000 (estimado pela proporção de cliques)
  CTR: 0,95%
  Leads: 38
  CPL: R$ 36,84
  Status: normal

Imagem estática:
  Impressões: ~37.800
  CTR: 2,35%
  Leads: 21
  CPL: R$ 66,67
  Status: atencao  ← CTR alto mas CPL acima da meta
```

---

### Análise gerada pelo agente

**O que funcionou:**
- CPL de R$ 23,73 está abaixo do benchmark de R$ 30-50, campanha bem configurada desde o início
- CPA de R$ 38,89 por agendamento é excelente para odontologia (meta era R$ 60-100)
- Criativo de oferta (Story + Post) gerou mais leads (38 vs 21) com CPL menor, criativo alinhado com a oferta

**O que precisa de atenção:**
- Taxa de conversão da LP está em 4,28%, abaixo dos 10% esperados para oferta gratuita. De 1.380 visitantes, apenas 59 preencheram. Cada 1% de melhoria na LP = +14 leads sem aumentar o investimento
- Imagem estática tem CTR alto (2,35%) mas converte menos em lead, a página de destino pode não estar alinhada com o criativo
- Semana 1 ainda está em fase de aprendizado do algoritmo (menos de 50 eventos por conjunto), não mudar nada ainda

**Próximas ações:**

1. **Otimizar a landing page:** taxa de 4,28% indica gargalo. Testar: reduzir campos do formulário de 5 para 3 (nome, telefone, unidade), mover o botão de agendamento para cima do scroll, adicionar o depoimento da Marina C. acima do formulário.
   Prazo: esta semana. Impacto esperado: +5-8 leads/semana sem custo adicional.

2. **Manter a campanha sem alterar:** fase de aprendizado do Meta Ads. O algoritmo precisa de 50 eventos de conversão por conjunto para sair do aprendizado. Aguardar semana 2 antes de qualquer mudança de segmentação ou criativo.
   Prazo: próxima semana.

3. **Preparar variação do criativo de oferta:** está performando bem. Na semana 3, testar novo hook na headline: "Tem medo do dentista?" (Agente 03 produz, mesmo formato Story + Post). Manter o original ativo para comparativo.
   Prazo: semana 3.

---

### Cálculo de ROI mostrado na demo

```
CÁLCULO DE ROI - SEMANA 1

Investimento: R$ 1.400
Agendamentos gerados: 36
Taxa de comparecimento estimada: 65% → 23 comparecimentos
Taxa de fechamento estimada: 35% → 8 tratamentos fechados
Ticket médio: R$ 1.800

Receita atribuída: 8 × R$ 1.800 = R$ 14.400
ROI = (14.400 - 1.400) ÷ 1.400 × 100 = 928%

Para cada R$ 1 investido em anúncio, R$ 10,28 de receita gerada.

NOTA: Estes são valores estimados com base em benchmarks do nicho. 
A Clínica Vital precisa registrar os comparecimentos e fechamentos 
reais para termos o ROI exato. Pedimos que registrem a origem 
"Meta Ads" no sistema no momento do agendamento.
```

---

## Como a demo conclui na Aula 4

Após o agente entregar o dashboard e o relatório:

1. **Bindes/Gui abre o HTML no Chrome.** O dashboard aparece com os KPIs coloridos (verde para CPL e CPA ótimos, laranja para taxa de LP).
2. **Bindes/Gui destaca o CPL:** "Olha o CPL: R$ 23,73. A meta era R$ 50. Estamos 53% abaixo do benchmark. Primeira semana."
3. **Bindes/Gui destaca o problema:** "Taxa de LP em 4%. Isso aqui é onde está o dinheiro perdido. Se a taxa fosse 10%, teríamos 138 leads no lugar de 59, com o mesmo orçamento."
4. **Bindes/Gui mostra o PDF:** Ctrl+P → Salvar como PDF. "Isso aqui você manda pro cliente toda semana. Profissional, visual, com o logo dele. Em 2 minutos."
5. **Bindes/Gui fecha o ciclo:** "Em uma semana: o Agente 01 planejou a campanha, o Agente 02 escreveu os anúncios, o Agente 03 fez o criativo, o Agente 04 construiu a LP, e o Agente 05 gerou o relatório. Isso aqui é o trabalho de uma semana inteira de uma equipe. Você fez em uma tarde."

---

## Conexão com os outros agentes após o relatório

O dashboard identifica 3 gargalos e já sabe qual agente chama:

| Problema identificado | Agente responsável |
|---|---|
| Taxa de LP baixa (4,28%) | Agente 04, Páginas otimiza o formulário e o CTA |
| Criativo com CTR alto mas CPL alto (imagem estática) | Agente 02, Copy revisa a copy do anúncio para alinhar com a LP |
| Preparar variação de criativo para semana 3 | Agente 03, Design/Criativos produz novo hook |
| Semana 2 sem alteração (fase de aprendizado) | Agente 01, Tráfego confirma: não mexer até 50 eventos por conjunto |
