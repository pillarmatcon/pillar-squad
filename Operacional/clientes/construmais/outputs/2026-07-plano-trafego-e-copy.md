# Construmais - Plano de Tráfego e Copy

**Briefing usado:** versão express (Cliente, Nicho, Oferta, Objetivo, Budget), fornecida em 2026-07-22
**Cliente:** Construmais
**Nicho:** Material de Construção (varejo local, materiais básicos, elétrica, hidráulica e pintura), João Pessoa/PB
**Objetivo:** Venda (via orçamento que converte em compra na loja ou entrega)
**Budget:** R$ 2.000/mês
**Status geral:** v1, sujeito a refinamento e validação do cliente

**Nota de mapeamento de nicho:** "Material de construção" não está na galeria de `_shared/nichos.md`. Perfil mapeado pelo framework de 6 dimensões:
- Tipo de oferta: produto físico (varejo), com componente de atendimento a profissional autônomo
- Modelo comercial: B2C local, com cauda B2B pequena (pedreiro, eletricista, encanador, pintor comprando para obra de terceiros)
- Ticket: baixo a médio por compra avulsa, podendo subir bastante em reforma completa (dado real não informado pelo cliente)
- Jornada: mistura de compra impulsiva (peça avulsa urgente, ex: registro furou) e compra planejada (reforma, construção)
- Recompra: esporádica para morador comum, frequente para profissional autônomo
- Compliance: nenhuma regulamentação setorial específica, aplica-se Código de Defesa do Consumidor padrão

---

## ETAPA 1: PLANO DE TRÁFEGO (Agente 01, Gestor de Tráfego)

### RESUMO DO PLANO

```
Cliente: Construmais
Objetivo: Venda (orçamento gerado por WhatsApp/formulário, convertido em compra na loja ou entrega)
Budget: R$ 2.000/mês (aprox. R$ 66/dia)
Plataforma principal: Meta Ads (60% do budget) + Google Search (40% do budget)
Meta de resultado: 25 a 65 orçamentos/mês (a variação depende do CPL real observado nas primeiras semanas)
```

Com R$ 2.000/mês o budget fica acima do mínimo de dados de Meta Ads (R$ 900/mês) e de Google Search (R$ 600/mês), então dá para rodar as duas plataformas ao mesmo tempo sem diluir demais. Abaixo de R$ 1.500/mês a recomendação seria concentrar tudo em uma única plataforma, mas aqui o valor comporta as duas com volume suficiente para gerar dado em 2 a 3 semanas.

A divisão fica 60% Meta (R$ 1.200/mês, R$ 40/dia) e 40% Google Search (R$ 800/mês, R$ 26/dia). Meta puxa mais peso porque o gatilho de reforma costuma ser visual (antes de decidir trocar o piso ou pintar a fachada, a pessoa se inspira vendo material) e porque o Advantage+ aprende rápido com o volume de eventos que R$ 40/dia sustenta. Google Search entra para capturar quem já está buscando ativamente ("loja de material de construção João Pessoa", "loja de tinta perto de mim"), que é intenção de compra madura e custa menos por resultado quando bem segmentado.

### ESTRUTURA DE CAMPANHA

#### Meta Ads: Geração de Orçamento (adaptação da Estrutura 1 de `estruturas-de-campanha.md`)

```
CAMPANHA: CONSTRUMAIS-META-LEADS-ORCAMENTO-072026
  Objetivo: Cadastro (evento Lead via formulário na landing page)
  Budget: R$ 40/dia
  Pixel: Meta Pixel instalado na LP, evento Lead disparado na confirmação

  CONJUNTO 1: Advantage+ Audience
    Segmentação: Advantage+ (algoritmo otimiza)
    Localização: João Pessoa e raio de 15km (cobre Cabedelo, Bayeux, Santa Rita)
    Posicionamentos: automático
    Orçamento: 70% do budget da campanha (R$ 28/dia)

    ANÚNCIO A: carrossel de oferta (5 cards, estrutura PAS) com a linha completa Básicos/Elétrica/Hidráulica/Pintura
    ANÚNCIO B: imagem única com hook de dor (obra parada por falta de material)
    ANÚNCIO C: imagem única com hook de identificação (profissional autônomo que revende ou compra para o cliente dele)

  CONJUNTO 2: Retargeting
    Segmentação: visitantes da LP nos últimos 30 dias + engajamento no Instagram/Facebook nos últimos 60 dias
    Orçamento: 30% do budget da campanha (R$ 12/dia)

    ANÚNCIO A: imagem com CTA direto ("Finalize seu orçamento")
    ANÚNCIO B: imagem reforçando o diferencial de ter as 4 categorias na mesma loja

NOMEAÇÃO DE ANÚNCIO:
  CONSTRUMAIS-LEADS-CARROSSEL-HOOK-OBRAPARADA-0726
  CONSTRUMAIS-LEADS-IMAGEM-HOOK-PROFISSIONAL-0726
```

**Nota sobre categoria especial:** material de construção não entra em categoria de anúncio especial do Meta (diferente de saúde, crédito, emprego, política ou habitação). Segmentação por interesse, comportamento e localização pode ser feita normalmente.

#### Google Search: Capturar demanda existente (adaptação da Estrutura 4)

```
CAMPANHA: CONSTRUMAIS-GOOGLE-SEARCH-MATERIALCONSTRUCAO-072026
  Tipo: Rede de Pesquisa
  Objetivo: Cadastro (formulário de orçamento) ou ligação
  Budget: R$ 26/dia
  Segmentação geográfica: João Pessoa/PB e raio de atuação da loja

  GRUPO DE ANÚNCIOS 1: Loja geral (alta intenção)
    Palavras-chave:
      "loja de material de construção João Pessoa" (frase)
      [material de construção João Pessoa] (exata)
      +loja +material +construção +perto
      "loja de material de construção perto de mim"

    Negativas obrigatórias:
      -grátis -gratuito -concurso -emprego -vaga -curso -faculdade -salário -aprendizagem

    ANÚNCIOS (mínimo 3 variações RSA):
      Título 1: Material de Construção em João Pessoa
      Título 2: Construmais | Básico, Elétrica, Hidráulica e Pintura
      Título 3: Peça seu Orçamento em Minutos
      Descrição 1: Tudo para sua obra em um só lugar. Material básico, elétrica, hidráulica e pintura. Peça o orçamento agora.
      Descrição 2: Loja em João Pessoa. Atendimento para morador e para profissional da obra. Fale com a gente pelo WhatsApp.

  GRUPO DE ANÚNCIOS 2: Categoria específica (elétrica, hidráulica, pintura)
    Palavras-chave:
      "material elétrico João Pessoa"
      "material hidráulico João Pessoa"
      "loja de tinta João Pessoa"
      +fio +tomada +disjuntor +João+Pessoa
      +cano +registro +conexão +João+Pessoa

    ANÚNCIOS: foco na categoria específica buscada + CTA de orçamento

  EXTENSÕES OBRIGATÓRIAS:
    - Sitelinks: Categorias (Elétrica, Hidráulica, Pintura, Básicos), Localização, WhatsApp
    - Chamada: telefone da loja
    - Local: endereço da loja (extensão de localização do Google Ads, requer Google Meu Negócio ativo)
    - Frase de destaque: "Orçamento sem compromisso", "4 categorias em uma loja só"
```

### SEGMENTAÇÃO

**Meta Ads:**
- Advantage+ Audience como estrutura principal, o Meta aprende com o Pixel
- Semente inicial de interesse (para contas novas, até acumular 50 eventos/semana): reforma residencial, construção civil, decoração de interiores, "faça você mesmo", ferramentas
- Retargeting obrigatório desde o lançamento: visitantes da LP + engajamento Instagram/Facebook

**Google Search:**
- Palavras-chave de correspondência de frase e exata para controlar custo, ampla modificada só no grupo de categoria específica
- Lista de negativas aplicada em nível de campanha
- Extensão de localização vinculada ao Google Meu Negócio (pendência: cliente precisa ter perfil do Google Meu Negócio ativo e verificado, se ainda não tiver)

**Retargeting (ambas as plataformas):**
- Lista de visitantes do site/LP dos últimos 30 dias
- Lista de engajamento em Instagram/Facebook dos últimos 60 dias

### CRIATIVOS NECESSÁRIOS

| # | Formato | Copy usada | Hook | Conjunto |
|---|---|---|---|---|
| 1 | Carrossel (5 cards, PAS) | Ver Etapa 2 e Etapa 3 | Obra parada por falta de material | Advantage+ (principal) |
| 2 | Imagem única | Ver Etapa 2, versão dor/agitação | "Você já foi em 3 lojas atrás da mesma peça?" | Advantage+ (teste A/B) |
| 3 | Imagem única | Ver Etapa 2, versão identificação profissional | Foco no profissional autônomo | Advantage+ (teste A/B) |
| 4 | Imagem única | CTA direto de retomada | "Finalize seu orçamento" | Retargeting |

Lançamento com 2 criativos no conjunto principal (carrossel + imagem de dor) e 1 no retargeting. O terceiro criativo (identificação profissional) entra na segunda semana como teste A/B, conforme calendário de voo.

### RASTREAMENTO

```
[ ] Meta Pixel instalado na LP (Agente 04 já entrega com placeholder de ID)
[ ] Evento Lead configurado para disparar no envio do formulário de orçamento
[ ] GA4 + Google Tag instalados na LP
[ ] Evento de conversão do Google Ads configurado na página de obrigado
[ ] UTMs em todos os links de anúncio:
    Meta: ?utm_source=meta&utm_medium=cpc&utm_campaign=CONSTRUMAIS-LEADS-ORCAMENTO-072026&utm_content={{ad.name}}
    Google: autotagging ativado na conta (Google insere os parâmetros automaticamente)
[ ] Google Meu Negócio ativo e verificado (necessário para extensão de local)
```

### CALENDÁRIO DE VOO (primeiros 60 dias)

```
SEMANA 1-2: LANÇAMENTO
  - Subir Meta com 2 criativos (carrossel + imagem de dor) e Google Search com os 2 grupos de anúncio
  - Budget conservador, sem mexer em nada, deixar o algoritmo aprender
  - Meta: coletar os primeiros 30 a 50 eventos de conversão em cada plataforma

SEMANA 3-4: PRIMEIRA OTIMIZAÇÃO
  - Comparar CPL real com o benchmark (R$ 30-80)
  - Pausar o criativo com pior CTR
  - Subir o terceiro criativo (identificação profissional) como teste A/B
  - Revisar palavras-chave do Google Search: pausar as que geraram clique sem conversão em volume relevante

SEMANA 5-8: ESCALA
  - Se o CPL estiver dentro do benchmark, aumentar budget em 20-30% a cada 5-7 dias
  - Ativar campanha de retargeting se ainda não tiver dado suficiente
  - Renovar o criativo de melhor desempenho com uma variação de hook

A PARTIR DO MÊS 3: MANUTENÇÃO
  - Renovar criativos a cada 30-45 dias
  - Relatório quinzenal com o Agente 05 (dashboard)
  - Atenção à sazonalidade: aumento de busca por material de pintura e reforma costuma subir antes de datas como Dia das Mães e fim de ano
```

### BENCHMARKS ESPERADOS

| Métrica | Referência usada | Ótimo | Normal | Atenção |
|---|---|---|---|---|
| CPL (orçamento) | Adaptado de "Reforma/Construção" em `benchmarks.md` (categoria mais próxima disponível) | R$ 30-80 | R$ 80-150 | Acima de R$ 150 |
| CTR de link | Padrão Meta Ads | Acima de 1,5% | 0,8-1,5% | Abaixo de 0,8% |
| Taxa de conversão da LP | Padrão lead gratuito | Acima de 20% | 10-20% | Abaixo de 10% |
| CTR Google Search | Padrão de busca | Acima de 7% | 3-7% | Abaixo de 3% |

**Importante:** como "material de construção" não tem benchmark próprio catalogado, o CPL meta acima é uma estimativa adaptada. Depois do primeiro ciclo de 30 dias, recalibrar com o dado real do cliente em vez do benchmark genérico.

**Fórmula de CPL máximo (pendente do ticket médio real):**
```
CPL máximo = Ticket médio × Taxa de fechamento × Margem bruta
```
Assim que o cliente informar ticket médio, taxa de fechamento (orçamento que vira venda) e margem, recalcular o CPL máximo real e ajustar a meta acima.

---

## ETAPA 2: COPY DOS ANÚNCIOS (Agente 02, Copywriter)

**Framework escolhido:** PAS (Problema, Agitação, Solução) para o anúncio principal, por ser o framework recomendado para geração de lead/agendamento em serviço local. Adaptado aqui para "geração de orçamento" em vez de "agendamento".

**Vocabulário usado:** "orçamento", "pedido", "obra", "reforma", cliente final e profissional autônomo tratados como "cliente da loja". Evitado "lead" no texto voltado ao dono da loja.

**Pendência de compliance:** nenhuma promessa de prazo de entrega ou preço específico foi incluída, porque o cliente não informou política real de prazo, frete ou parcelamento. Qualquer condição comercial (frete grátis, desconto, parcelamento) só entra na copy depois de confirmada com o cliente.

### Headlines (8 variações)

| # | Ângulo | Headline | Subheadline | Onde testar |
|---|---|---|---|---|
| 1 | Dor | Obra parada esperando material? | Material básico, elétrica, hidráulica e pintura em um só lugar em João Pessoa. | Anúncio Meta, hero da LP |
| 2 | Benefício direto | Tudo para sua reforma em uma única loja | Sem rodar em 3 lugares diferentes atrás de peça. Peça o orçamento agora. | Anúncio Meta |
| 3 | Identificação (profissional) | Pedreiro, eletricista ou encanador em João Pessoa? | Compre o material da obra com orçamento rápido e sem enrolação. | Anúncio Meta, Google Search |
| 4 | Identificação (morador) | Vai reformar a casa em João Pessoa? | Do material básico à tinta da parede, a Construmais resolve. | Anúncio Meta |
| 5 | Contraste | Uma loja só, quatro categorias resolvidas | Básicos, elétrica, hidráulica e pintura sem precisar sair de onde está. | LP, carrossel |
| 6 | Pergunta | Já foi em três lojas atrás da mesma peça? | Na Construmais o cliente resolve tudo de uma vez. | Anúncio Meta |
| 7 | Urgência funcional | Peça furou e a obra não pode esperar? | Fale agora com a Construmais e receba seu orçamento. | Anúncio Meta, WhatsApp |
| 8 | Oferta de conveniência | Orçamento em minutos, sem sair de casa | Preencha o formulário e a Construmais retorna com os valores. | Hero da LP |

### Anúncio Meta Ads completo (3 variações)

#### Versão 1: Direta (foco no benefício imediato)

**Headline principal:** Tudo para sua obra em uma loja só
**Headline secundária:** Básico, elétrica, hidráulica e pintura
**Texto principal:**
Sua obra ou reforma em João Pessoa pode precisar de material básico, fio, cano e tinta ao mesmo tempo. Na Construmais isso resolve em uma visita só, sem precisar rodar a cidade atrás de peça avulsa. Preencha o formulário e receba seu orçamento.
**Descrição:** Loja em João Pessoa. Atendimento para morador e para profissional da obra.
**CTA:** Receber orçamento
**Sugestão de criativo:** carrossel de 5 cards mostrando as 4 categorias e fechando com o CTA. Formato indicado porque permite mostrar a variedade sem depender de uma foto só.

#### Versão 2: Dor/agitação

**Headline principal:** Obra parada custa mais do que parece
**Headline secundária:** Cada dia sem material é um dia de atraso
**Texto principal:**
Falta uma peça e a obra trava. O pedreiro fica parado, o prazo estica, e o transtorno cai em cima de quem contratou o serviço. A Construmais reúne material básico, elétrica, hidráulica e pintura no mesmo lugar, para o cliente não precisar sair correndo atrás de fornecedor diferente para cada etapa da obra.
**Descrição:** Peça o orçamento e resolva antes que a obra pare de novo.
**CTA:** Peça seu orçamento
**Sugestão de criativo:** imagem única com hook de texto grande ("Obra parada custa mais do que parece"), fundo com foto de material de construção real da loja se disponível, ou paleta sólida com tipografia se não houver foto.

#### Versão 3: Diferencial concreto (em vez de "prova social", porque o briefing não trouxe depoimento real nem case verificável)

**Headline principal:** Quatro categorias, um único pedido
**Headline secundária:** Básico, elétrica, hidráulica e pintura sem trocar de fornecedor
**Texto principal:**
Trocar de fornecedor a cada etapa da obra custa tempo. Na Construmais, o material básico, a parte elétrica, a hidráulica e a tinta saem do mesmo pedido, com um único orçamento e um único contato. Menos ligação, menos deslocamento, menos gente diferente para acompanhar.
**Descrição:** Fale com a Construmais e organize a obra em um pedido só.
**CTA:** Falar com a Construmais
**Sugestão de criativo:** imagem única simples, com foco tipográfico no diferencial das 4 categorias.

**Nota:** quando o cliente puder fornecer um depoimento real (com autorização) ou um número verificável (anos de operação, quantidade de obras atendidas), substituir a Versão 3 por uma versão de prova social de verdade. Isso é mais forte do que o diferencial genérico acima.

### Copy para o carrossel (5 cards, estrutura PAS)

Usada na Etapa 3 (HTML do carrossel).

1. **Hook (Problema):** "Obra parada esperando material?"
2. **Agitação:** "Cada peça que falta é um dia a mais de atraso, e o cliente da obra sente isso no bolso e na paciência."
3. **Solução:** "A Construmais resolve básico, elétrica, hidráulica e pintura em uma loja só, em João Pessoa."
4. **Diferencial concreto (substitui prova social não verificada):** "Um pedido, quatro categorias resolvidas. Menos fornecedor para acompanhar, menos tempo perdido."
5. **CTA:** "Peça seu orçamento agora e resolva o que falta na obra."

### Copy para a landing page

Usada na Etapa 4.

- **Headline do hero:** "Tudo para sua obra em uma loja só em João Pessoa"
- **Subheadline do hero:** "Material básico, elétrica, hidráulica e pintura. Preencha o formulário e receba seu orçamento."
- **Título do formulário:** "Peça seu orçamento"
- **Texto do botão:** "Receber orçamento"
- **Benefício 1 (título):** "Quatro categorias em um pedido só"
  **Benefício 1 (texto):** "Básico, elétrica, hidráulica e pintura sem precisar rodar a cidade atrás de fornecedor diferente para cada etapa da obra."
- **Benefício 2 (título):** "Atendimento para quem mora e para quem trabalha na obra"
  **Benefício 2 (texto):** "Seja para a reforma da própria casa ou para o material que o profissional autônomo compra na obra do cliente dele."
- **Benefício 3 (título):** "Orçamento sem compromisso"
  **Benefício 3 (texto):** "Preenche o formulário, a Construmais retorna com os valores e o cliente decide com calma."
- **FAQ 1:** "A Construmais atende fora de João Pessoa?" - "[PREENCHER: confirmar com o cliente o raio real de atendimento e se há entrega para Cabedelo, Bayeux e Santa Rita.]"
- **FAQ 2:** "Preciso ir até a loja para receber o orçamento?" - "Não. Preencha o formulário com o que precisa e a Construmais retorna pelo contato informado."
- **FAQ 3:** "A Construmais atende profissional autônomo (pedreiro, eletricista, encanador, pintor)?" - "Sim. O atendimento cobre tanto quem está reformando a própria casa quanto o profissional que compra material para a obra do cliente dele."
- **FAQ 4:** "Como funciona a entrega?" - "[PREENCHER: confirmar com o cliente se há entrega, prazo médio e taxa, para não prometer condição que a loja não pratica.]"
- **CTA final (título):** "Sua obra não precisa esperar"
- **CTA final (subtítulo):** "Peça o orçamento agora e resolva o que falta em um pedido só."

---

## Pendências para virar "pronto para publicar"

1. Confirmar com o cliente: Instagram (handle real), site ou domínio, endereço completo, CNPJ, telefone de contato.
2. Confirmar ticket médio, taxa de fechamento de orçamento e margem bruta, para recalcular o CPL máximo real (fórmula na seção de benchmarks acima).
3. Confirmar política real de entrega (se existe, prazo e taxa) antes de publicar a FAQ da LP.
4. Confirmar se há Google Meu Negócio ativo (necessário para extensão de localização no Google Ads).
5. Validar headlines e anúncios com o cliente antes de subir, principalmente o ângulo de "identificação profissional" (confirmar se a loja realmente atende esse público em volume relevante).
6. Assim que houver depoimento real de cliente (com autorização) ou número verificável de tempo de operação, substituir o card de "diferencial concreto" por prova social de verdade no anúncio e no carrossel.
7. Criar conta de Pixel Meta e GA4 caso ainda não existam, e trocar os placeholders nos arquivos HTML pelos IDs reais.

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
