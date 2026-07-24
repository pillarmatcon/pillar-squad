# Estruturas de Campanha

> Templates prontos para Meta Ads e Google Ads. Adaptar o nome do cliente, orçamento e criativos. A estrutura é o esqueleto, os textos vêm do Agente 02, os criativos do Agente 03.

---

## Meta Ads

### Estrutura 1: Geração de Leads (serviço local)

Ideal para: clínica, estética, barbearia, consultório, escola, escritório de advocacia, imobiliária.

```
CAMPANHA: [CLIENTE] - Leads - [OFERTA] - [MÊS/ANO]
  Objetivo: Leads
  Budget: R$ X/dia (concentrado na campanha, não no conjunto)
  Pixel: SIM - evento Lead configurado na LP

  CONJUNTO 1: Advantage+ Audience
    Segmentação: Advantage+ (deixar o Meta otimizar)
    Localização: raio de Xkm em [cidade] ou cidade específica
    Posicionamentos: Automático (Meta recomenda)
    Orçamento: 70% do budget total

    ANÚNCIO A: [tipo: imagem única - Story + Post] - criativo da oferta principal
    ANÚNCIO B: [tipo: vídeo ou imagem] - depoimento de cliente
    ANÚNCIO C: [tipo: imagem] - hook de dor/problema

  CONJUNTO 2: Retargeting
    Segmentação: visitantes do site últimos 30 dias + engajamento Instagram 60 dias
    Orçamento: 30% do budget total

    ANÚNCIO A: [tipo: imagem] - oferta com urgência
    ANÚNCIO B: [tipo: imagem] - depoimento específico

NOMEAÇÃO DE ANÚNCIO (padrão):
  [CLIENTE]-[OBJETIVO]-[FORMATO]-[HOOK]-[DATA]
  Exemplo: CLINICAVITAL-LEADS-IMAGEM-HOOK-ADIA-2026-05
```

**Quando usar Advantage+ Audience:**
O Meta usa os dados do Pixel para encontrar quem tem mais chance de converter. Para negócios que já têm Pixel com eventos rodando, funciona melhor que segmentação manual. Para contas novas (menos de 50 eventos/semana), combinar com segmentação por interesse como "semente".

---

### Estrutura 2: Advantage+ Shopping (e-commerce)

Ideal para: loja virtual, delivery, produto físico com compra direta.

```
CAMPANHA: [CLIENTE] - Vendas - Advantage+ - [MÊS/ANO]
  Objetivo: Vendas (evento Purchase no Pixel)
  Budget: R$ X/dia
  Catálogo: SIM (necessário ter catálogo de produtos vinculado)

  CONJUNTO 1: Advantage+ Shopping Campaign
    Segmentação: Automática (Advantage+ define tudo)
    Budget: 100% - não segmentar manualmente
    
    ANÚNCIOS: subir de 5 a 15 criativos variados
      - Produto em uso (lifestyle)
      - Produto isolado (fundo branco)
      - Carrossel de produtos
      - Vídeo curto (15-30s) mostrando o produto
      - Depoimento com produto

NOTA: Advantage+ Shopping não permite segmentação manual. O algoritmo escolhe tudo.
Desvantagem: menor controle. Vantagem: geralmente tem ROAS superior em contas maduras.
```

---

### Estrutura 3: Campanha de Branding Local (awareness)

Ideal para: inauguração, lançamento de produto, evento, nova unidade.

```
CAMPANHA: [CLIENTE] - Branding - [EVENTO] - [MÊS/ANO]
  Objetivo: Alcance (Reach) ou Reconhecimento de Marca
  Budget: R$ 20-50/dia, duração de 7-14 dias
  Frequência-alvo: 3-5x por pessoa

  CONJUNTO 1: Localização por raio
    Segmentação: pessoas em raio de 5km do endereço
    Limite de frequência: 2x por dia

    ANÚNCIO A: vídeo 15s com oferta de inauguração
    ANÚNCIO B: imagem com oferta limitada
```

---

## Google Ads

### Estrutura 4: Campanha Search (capturar demanda existente)

Ideal para: qualquer negócio com busca ativa no Google (dentista, advogado, hotel, dedetizador, mecânica, eletricista).

```
CAMPANHA: [CLIENTE] - Search - [SERVIÇO] - [CIDADE]
  Tipo: Rede de Pesquisa
  Objetivo: Leads (ligações ou formulário)
  Budget: R$ X/dia
  Segmentação geográfica: cidade(s) específica(s)

  GRUPO DE ANÚNCIOS 1: Busca pelo serviço (alta intenção)
    Palavras-chave:
      +dentista +[cidade] (correspondência ampla modificada)
      "dentista em [cidade]" (frase)
      [dentista [cidade]] (exata)
      +clínica +odontológica +[bairro]
    
    Negativas obrigatórias:
      -grátis -gratuito -concurso -escola -faculdade -curso -emprego -salário

    ANÚNCIOS (mínimo 3 variações RSA):
      Título 1: Dentista em [Cidade] | Avaliação Gratuita
      Título 2: Clínica [Nome] | Tomografia 3D Inclusa
      Título 3: Agende Hoje | Atendimento Rápido
      Descrição 1: Avaliação gratuita com tomografia 3D. Plano de tratamento sem compromisso. Ligue agora.
      Descrição 2: Clínica no [Bairro]. Mais de X pacientes atendidos. Agende pelo WhatsApp em 30 segundos.

  GRUPO DE ANÚNCIOS 2: Busca por dor/problema (média intenção)
    Palavras-chave:
      +dor +dente +o+que+fazer
      +implante +dental +[cidade]
      +aparelho +invisível +[cidade]
    
    ANÚNCIOS: foco em solução + CTA de agendamento

  EXTENSÕES OBRIGATÓRIAS:
    - Sitelinks: Sobre Nós, Localização, WhatsApp, Instagram
    - Chamada: número de telefone clicável
    - Local: endereço comercial da unidade (extensão de localização do Google Ads)
    - Frase de destaque: "Avaliação Gratuita", "Tomografia 3D Inclusa"
```

---

### Estrutura 5: Performance Max (capturar demanda em múltiplos canais)

Ideal para: e-commerce com catálogo, negócio que quer estar em Search + YouTube + Display + Maps ao mesmo tempo.

```
CAMPANHA: [CLIENTE] - PMax - [PRODUTO/SERVIÇO] - [MÊS/ANO]
  Tipo: Performance Max
  Objetivo: Conversões (Lead ou Purchase)
  Budget: R$ X/dia (mínimo R$ 50/dia para ter dados suficientes)

  GRUPO DE RECURSOS 1: Principal
    Imagens: 5-20 (variadas: produto, lifestyle, logotipo)
    Vídeos: 1-5 (horizontal, vertical e quadrado)
    Títulos: 5 (máximo 30 caracteres cada)
    Títulos longos: 5 (máximo 90 caracteres)
    Descrições: 5 (máximo 90 caracteres)
    CTA: Agendar, Comprar Agora, Saiba Mais (escolher o mais relevante)
    URL final: LP com rastreamento de conversão

  SINAIS DE AUDIÊNCIA (não é segmentação - é direcionamento inicial):
    - Lista de clientes existentes (e-mail ou telefone)
    - Visitantes do site (Pixel instalado)
    - Interesses relacionados ao produto

NOTA: PMax tem baixo controle granular. O Google decide onde mostrar. 
Não recomendado para contas novas sem histórico de conversão.
```

---

### Estrutura 6: Campanha de Retargeting no Google Display

Ideal para: reativar visitantes do site que não converteram.

```
CAMPANHA: [CLIENTE] - Display - Retargeting - [MÊS/ANO]
  Tipo: Rede de Display
  Objetivo: Conversões
  Budget: R$ 15-30/dia

  GRUPO DE ANÚNCIOS 1: Visitantes do site (últimos 30 dias)
    Audiência: remarketing tag / GA4 integrado
    
    ANÚNCIOS:
      - Banner 300x250 com oferta
      - Banner 728x90 (leaderboard)
      - Banner 160x600 (arranha-céu)
      - Anúncio responsivo de display (mais fácil: sobe imagens e texto, Google monta)

NOTA: Requer Google Tag instalado no site para criar lista de remarketing.
```

---

## Nomeação padronizada de campanhas

Usar sempre o mesmo padrão para todos os clientes. Facilita relatório e diagnóstico.

```
CAMPANHA:
[CLIENTE]-[PLATAFORMA]-[OBJETIVO]-[OFERTA]-[MMAAAA]

Exemplos:
CLINICAVITAL-META-LEADS-AVALGRATIS-052026
CLINICAVITAL-GOOGLE-SEARCH-IMPLANTE-052026
PADARIADAMAR-META-VENDAS-MARMITA-052026

CONJUNTO DE ANÚNCIOS:
[SEGMENTAÇÃO]-[BUDGET%]

Exemplos:
ADVANTAGE-PLUS-70pct
RETARGETING-30pct
BUSCA-ALTA-INTENCAO

ANÚNCIO:
[FORMATO]-[HOOK]-[DATA]

Exemplos:
IMAGEM-ADIA-DENTISTA-0526
VIDEO-DEPOIMENTO-MARINA-0526
IMAGEM-DOR-MEDO-0526
```

---

## Calendário de voo padrão (primeiros 60 dias)

```
SEMANA 1-2: LANÇAMENTO
  - Subir campanha com 2-3 criativos
  - Budget conservador (70% do budget planejado)
  - Não mexer em nada - deixar o algoritmo aprender
  - Meta: coletar primeiros 50 eventos de conversão

SEMANA 3-4: PRIMEIRA OTIMIZAÇÃO
  - Analisar CPL/CPA real vs benchmark
  - Pausar criativo com pior desempenho
  - Lançar 1 criativo novo (A/B test)
  - Ajustar segmentação se CPL estiver muito alto
  - Meta: reduzir CPL em 20%

SEMANA 5-8: ESCALA
  - Aumentar budget em +20-30% a cada 5-7 dias (não dobrar de uma vez)
  - Criar campanha de retargeting se ainda não tiver
  - Testar novo hook no criativo (Agente 03)
  - Meta: escalar volume mantendo CPL dentro do benchmark

A PARTIR DO MÊS 3: MANUTENÇÃO
  - Renovar criativos a cada 30-45 dias (fadiga de anúncio)
  - Relatório semanal via Agente 05
  - Ajuste de budget conforme sazonalidade do nicho
```

---

## Configuração de pixel e rastreamento

### Meta Pixel

```html
<!-- Colar no <head> de todas as páginas -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'SEU_PIXEL_ID');
fbq('track', 'PageView');
</script>

<!-- Na página de agradecimento / após conversão: -->
<script>fbq('track', 'Lead');</script>
<!-- OU para venda: -->
<script>fbq('track', 'Purchase', {value: 0.00, currency: 'BRL'});</script>
```

### GA4 + Google Tag

```html
<!-- Google Tag (colar no <head>) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
  // Se tiver Google Ads também:
  gtag('config', 'AW-XXXXXXXXXX');
</script>

<!-- Evento de conversão no Google Ads (página de obrigado) -->
<script>
  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXXX/XXXXXXXX',
    'value': 1.0,
    'currency': 'BRL'
  });
</script>
```

### UTM padrão para todos os links de anúncio

```
Meta Ads:
?utm_source=meta&utm_medium=cpc&utm_campaign={{campaign.name}}&utm_content={{ad.name}}

Google Ads (usar parâmetros automáticos):
Marcar "Autotagging" nas configurações da conta - o Google insere os parâmetros automaticamente

Manual (quando não tiver autotagging):
?utm_source=google&utm_medium=cpc&utm_campaign=NOME_CAMPANHA&utm_term=KEYWORD

WhatsApp:
?utm_source=whatsapp&utm_medium=referral&utm_campaign=NOME_CAMPANHA
```
