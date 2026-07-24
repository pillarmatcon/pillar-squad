# Exemplo de Demo: Agente 01-Tráfego + Clínica Vital

> **Uso:** demonstração na Aula 4 do evento AgêncIA 100k. Primeiro agente do squad a ser usado, define a estratégia que os outros agentes vão executar. Tempo total da demo: 5 a 7 minutos.

---

## O que entra como input

O dono da agência (aluno) traz o briefing do cliente:

```
CLIENTE: Clínica Vital
NICHO: Odontologia - 2 unidades em BH (Savassi e Lourdes)
OFERTA: Avaliação gratuita com tomografia 3D inclusa (sem compromisso de continuar)
OBJETIVO: Gerar agendamentos de avaliação - meta: 40 agendamentos/mês por unidade
BUDGET MENSAL: R$ 6.000 (R$ 3.000 por unidade)
GEOLOCALIZAÇÃO: raio de 5km em cada unidade (Savassi e Lourdes, BH/MG)
TICKET MÉDIO: R$ 1.800 por tratamento fechado
PRESENÇA ATUAL: Instagram ativo (@clinicavital), sem Meta Ads rodando, sem Pixel instalado
```

---

## O que a Bindes/Gui pede ao agente na demo

> "@gestor-trafego monte o plano de tráfego para a Clínica Vital. Briefing acima. Queremos gerar 80 agendamentos/mês no total (40 por unidade)."

---

## Output do agente (o que aparece na tela durante a demo)

---

### Resumo executivo do plano

```
CLIENTE: Clínica Vital
OBJETIVO: 80 agendamentos/mês (40 por unidade - Savassi e Lourdes)
BUDGET: R$ 6.000/mês (R$ 200/dia)
PLATAFORMA PRINCIPAL: Meta Ads
PLATAFORMA SECUNDÁRIA: Google Search (a partir do mês 2)
META DE CPL: R$ 30-50 por lead
META DE CPA (agendamento): R$ 60-100 por agendamento confirmado
PIXEL: instalar antes de subir qualquer anúncio
```

---

### Estrutura de campanha: Meta Ads (mês 1)

```
CAMPANHA 1: CLINICAVITAL-META-LEADS-AVALGRATIS-SAVASSI-052026
  Objetivo: Leads
  Budget: R$ 100/dia
  Evento de conversão: Lead (formulário de agendamento)
  URL de destino: LP de agendamento da unidade Savassi (Agente 04 produz)

  CONJUNTO 1: Advantage+ Audience - SAVASSI (70% do budget = R$ 70/dia)
    Segmentação: Advantage+ com sinal de localização
    Sinal de localização: pessoas em raio de 5km do Savassi, BH
    Posicionamentos: Automático
    Orçamento: R$ 70/dia

    ANÚNCIO A: [IMAGEM ÚNICA - STORY/POST] clinica-vital-story.png + clinica-vital-post.png
      Copy de anúncio: "Adia o dentista? Tem motivo. A avaliação gratuita resolve."
      CTA: Saiba Mais → LP de agendamento Savassi
      
    ANÚNCIO B: [IMAGEM ESTÁTICA] foto do consultório ou equipe
      Copy: "Avaliação gratuita com tomografia 3D. Sem compromisso de continuar."
      CTA: Agendar Agora
      
    ANÚNCIO C: [VÍDEO 15-30s] depoimento da Marina C. ou tour do consultório
      Hook: "Vim cheio de medo. Saí com um plano. Sem pressão."

  CONJUNTO 2: Retargeting Savassi (30% = R$ 30/dia)
    Segmentação: visitantes da LP + engajamento Instagram 60 dias
    Orçamento: R$ 30/dia (ativar após 7 dias da campanha principal)

    ANÚNCIO A: [IMAGEM] oferta com urgência
      Copy: "Você visitou a Clínica Vital. Ainda dá tempo de agendar esta semana."

CAMPANHA 2: CLINICAVITAL-META-LEADS-AVALGRATIS-LOURDES-052026
  [estrutura idêntica à campanha 1, com localização Lourdes]
  Budget: R$ 100/dia
```

---

### Estrutura de campanha: Google Search (mês 2)

```
CAMPANHA: CLINICAVITAL-GOOGLE-SEARCH-ODONTO-BH-062026
  Tipo: Rede de Pesquisa
  Objetivo: Leads (ligação ou formulário)
  Budget: R$ 60/dia
  Localização: Belo Horizonte - bairros Savassi, Lourdes, Funcionários, Belvedere, Anchieta

  GRUPO 1: Alta intenção - dentista BH
    Palavras-chave:
      "dentista savassi bh"
      "dentista lourdes bh"
      "clínica odontológica belo horizonte"
      +dentista +avaliação +gratuita +bh
      
    Negativas:
      -concurso -faculdade -escola -curso -emprego -grátis -gratuito

    ANÚNCIO RSA 1:
      Título 1: Dentista no Savassi | Avaliação Gratuita
      Título 2: Clínica Vital BH | Tomografia 3D Inclusa
      Título 3: Agende em 30 Segundos | Sem Compromisso
      Descrição 1: Avaliação completa com tomografia 3D sem custo. Plano de tratamento detalhado e você decide se continua.
      Descrição 2: Atendimento no Savassi e Lourdes. Mais de 500 pacientes atendidos. Confira os depoimentos.

  GRUPO 2: Procedimento específico
    Palavras-chave:
      "implante dental bh"
      "aparelho invisível belo horizonte"
      "clareamento dental savassi"
      +tratamento +dentário +bh +preço

    ANÚNCIO RSA 2:
      Título 1: Implante Dental | Avalie Grátis em BH
      Título 2: Clínica Vital | Savassi e Lourdes
      Título 3: Orçamento no Mesmo Dia
      Descrição 1: Avaliação gratuita com tomografia 3D. Saiba exatamente o que você precisa e quanto vai custar.

  EXTENSÕES:
    Sitelinks: Sobre a Clínica | Como Funciona | Depoimentos | Localização
    Chamada: (31) XXXX-XXXX
    Local: extensão de localização do Google Ads com endereço comercial
    Destaque: "Tomografia 3D Inclusa" | "Sem Compromisso" | "Atendimento Rápido"
```

---

### Criativos necessários (para o Agente 03)

```
LANÇAMENTO (semana 1):
  1. Criativo de oferta - Story (1080x1920) + Post (1080x1350)
     → já pronto: clinica-vital-oferta.html (Agente 03 já entregou)
  2. OG Image da LP (1200x630)
     → briefing: para o <meta og:image> da landing page (Agente 04 solicitou)

TESTE (semana 3):
  3. Criativo alternativo - hook diferente: "Tem medo do dentista?"
     → mesmo template de oferta, troca headline e subheadline
  4. Criativo de prova social - foto da Marina C. com citação, Story + Post
```

---

### Rastreamento

```
ANTES DE SUBIR QUALQUER ANÚNCIO:

Meta Pixel:
  ID do Pixel: a criar no Gerenciador de Negócios da Clínica Vital
  Instalar em: LP de agendamento Savassi + LP de agendamento Lourdes + obrigado.html
  Eventos obrigatórios:
    PageView → automático ao instalar o pixel
    Lead → disparar no obrigado.html após agendamento confirmado

GA4:
  Measurement ID: a criar no Google Analytics
  Instalar em: mesmas páginas
  Evento: generate_lead (ao submeter formulário)

Google Tag (se ativar Google Ads no mês 2):
  Conversion ID: a criar no Google Ads
  Evento: Lead (mesma página de obrigado)

UTMs para Meta Ads:
  Criativo de oferta Savassi:
  ?utm_source=meta&utm_medium=cpc&utm_campaign=CLINICAVITAL-LEADS-SAVASSI-052026&utm_content=story-post

  (Repetir padrão para Lourdes trocando -SAVASSI- por -LOURDES-)
```

---

### Benchmarks para este cliente

```
REFERÊNCIA (nicho odontologia, Meta Ads, BH):

CPL esperado: R$ 30-50 por lead gerado
CPA esperado (agendamento confirmado): R$ 60-100
  [assumindo taxa de agendamento de 60-70% dos leads - odonto tem alta intenção]

COM BUDGET DE R$ 200/DIA (R$ 6.000/MÊS):
  Leads esperados: 120-200/mês
  Agendamentos esperados: 72-140/mês
  Meta de 80 agendamentos: viável no cenário conservador

CPL máximo que a Clínica Vital pode pagar sem prejuízo:
  Ticket médio: R$ 1.800
  Taxa de fechamento estimada: 30% dos agendamentos viram tratamento
  Margem: ~50%
  
  CPL máximo = 1.800 × 0,30 × 0,50 = R$ 270
  
  Ou seja: mesmo pagando R$ 270/lead, o negócio ainda é lucrativo.
  Com CPL de R$ 30-50, a margem de segurança é enorme.
```

---

### Calendário de voo (primeiros 60 dias)

```
SEMANA 1 (instalação):
  [ ] Criar Pixel Meta + instalar na LP (Agente 04 configura)
  [ ] Criar GA4 + instalar na LP
  [ ] Subir campanha Savassi e Lourdes no Meta Ads
  [ ] Budget: 70% do planejado (R$ 140/dia) - fase de aprendizado
  [ ] NÃO MEXER em nada por 7 dias mínimo

SEMANA 2 (primeiros dados):
  [ ] Verificar: Pixel está recebendo eventos? (Events Manager)
  [ ] Verificar: CPL está dentro do benchmark? (R$ 30-50)
  [ ] Verificar: algum anúncio rejeitado? (revisar copy para compliance CRO)
  [ ] Se CPL acima de R$ 70: aplicar diagnóstico (diagnostico-de-conta.md)
  [ ] Lançar retargeting (conjunto 2)

SEMANA 3 (primeiro teste A/B):
  [ ] Pausar anúncio com pior CTR
  [ ] Lançar variação com hook diferente (Agente 03 produz)
  [ ] Aumentar budget para 100% (R$ 200/dia)

SEMANA 4 (primeira revisão):
  [ ] Relatório de resultados semana 1-4 (Agente 05)
  [ ] Comparar CPL real vs benchmark
  [ ] Decisão: escalar, otimizar ou reformular

MÊS 2 (expansão):
  [ ] Lançar Google Search se CPL Meta estiver abaixo de R$ 60
  [ ] Budget Google: R$ 60/dia (nova verba ou remanejamento)
  [ ] Configurar extensão de localização do Google Ads com endereço das 2 unidades
  [ ] Criar campanha de retargeting no Google Display
```

---

## Como a demo conclui na Aula 4

Após o agente entregar o plano:

1. **Bindes/Gui mostra o plano completo:** campanha, segmentação, criativos, UTMs, benchmarks.
2. **Bindes/Gui comenta:** "Repara que o agente calculou o CPL máximo que a clínica pode pagar. R$ 270 por lead ainda dá lucro. Estamos mirando R$ 30-50. A margem de segurança é 5x."
3. **Bindes/Gui mostra a conexão:** "Esse plano pede 2 criativos. O Agente 03 já entregou o de oferta, Story e Post. Agora peço a OG Image."
4. **Bindes/Gui comenta:** "Repara que o agente já escreveu as UTMs. Quando o Agente 05 fizer o dashboard, vai usar exatamente essas UTMs para medir."
5. **Bindes/Gui faz o pitch:** "Em 6 minutos saímos de um briefing para um plano de tráfego com estrutura, budget, benchmarks e calendário. Sem contratar gestor de tráfego, sem esperar uma semana por um planejamento. O cliente recebe isso hoje."

---

## Conexão com os outros agentes do squad

- **Agente 02-Copy** vai escrever a copy dos anúncios indicados aqui (criativo de oferta, copy de anúncio Meta)
- **Agente 03-Design/Criativos** vai produzir os 2 criativos indicados (oferta em Story + Post já pronto, OG Image pendente)
- **Agente 04-Páginas** vai construir a LP com o Pixel e os eventos de conversão que este agente especificou
- **Agente 05-Dashboard** vai usar as UTMs, as metas de CPL/CPA e os benchmarks definidos aqui para montar o relatório de performance

---

## Variações que o aluno pode pedir depois

1. **Versão com budget reduzido (R$ 2.000/mês):** concentrar em uma unidade, sem Google no início
2. **Versão com budget ampliado (R$ 15.000/mês):** escalar Meta + Google + TikTok
3. **Diagnóstico de conta existente:** trazer dados da conta atual e receber análise com recomendações
4. **Plano para outro nicho:** mesmo formato, adaptado para restaurante, escola, e-commerce, etc.
