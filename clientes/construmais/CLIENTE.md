# Cliente: Construmais

## Identidade
- **Agência responsável:** Pillar (ver `_squad/_shared/identidade-agencia.md`)
- **Responsável pela conta (lado Pillar):** Murillo e Alex
- **Contato principal (lado cliente, decisor):** Tony Carvalho Barbosa
- **Nicho:** Loja de material de construção (varejo local, materiais básicos, elétrica, hidráulica e pintura), com atendimento a consumidor final e profissional autônomo (pedreiro, eletricista, encanador, pintor). Perfil catalogado em `_squad/_shared/nichos.md`.
- **Cidade / região:** João Pessoa/PB
- **CNPJ:** 13.796.094/0001-07
- **Endereço:** Rua Elias Cavalcanti de Albuquerque, 750, Cristo Redentor, João Pessoa/PB, CEP 58070-400
- **Telefone fixo:** (83) 3223-1568
- **WhatsApp comercial:** (83) 9 9847-1242
  - Nota: o formulário de onboarding (21/07/2026) trouxe um terceiro número, "55 83 8855-5601". Optou-se por usar os dois números acima porque vieram direto do site oficial já publicado da loja, fonte mais confiável. Se aparecer divergência nova, confirmar direto com o Tony.
- **E-mail comercial:** contato@construmaisjp.com.br
- **Site:** construmaisjp.com.br (site institucional já existe, desenvolvido pela agência "Anova Agência" — simples, sem blog, sem catálogo de produtos, sem SEO. Foi replicado em HTML/CSS como base editável, incluindo logo, fachada, foto do Tony e galeria de fotos da loja. Útil como ponto de partida para o `@webdesigner`, não precisa construir do zero.)
- **Instagram:** @construmaisjpa
- **Facebook:** /construmaisjp
- **Tempo de mercado:** 15 anos (consistente com fundação em 2011 citada no depoimento institucional do site)
- **Total de colaboradores:** 6 (2 vendedores)
- **Cores da marca:** Vermelho principal #EE2526 (dominante, fundo, logo, camisa do mascote) / Amarelo #F4D000 (destaque, preço, CTA, capacete e colete do mascote) / Laranja #F7941D (uso pontual, só nas botas do mascote, ainda aproximado) / Branco (texto principal, contorno do logo) / Preto (sombra, contorno, fundo de vídeo)
  - Fonte: brand kit extraído em 2026-07-23 a partir da análise do perfil, grid de posts e legendas do Instagram @construmaisjpa (não veio do formulário de onboarding). Vermelho e amarelo confirmados em hex exato pelo Tony/agência em 2026-07-23 (#EE2526 e #F4D000). **Substitui** a paleta laranja terracota/amarelo mostarda registrada antes, que era suposição baseada só no nicho, sem dado real de marca.
  - Ajuste em 2026-07-23: a leitura inicial do grid do Instagram supunha o laranja como cor dominante do mascote (capacete e colete). O arquivo real do mascote (`marca/mascote-construmais.png`, registrado na sétima atualização do Histórico) mostra capacete e colete **amarelos**, com o laranja aparecendo só nas botas. Laranja deixa de ser cor de destaque do mascote e passa a detalhe secundário.
  - Pendência remanescente: o laranja (#F7941D) ainda é aproximação visual do grid, não confirmado em hex exato. Vermelho e amarelo já estão travados.
  - **Atenção:** os outputs já entregues em julho de 2026 (`outputs/2026-07-carrossel-oferta.html`, `2026-07-dashboard-metas.html`, `2026-07-landing-page-captura.html`) foram produzidos com a paleta antiga (laranja terracota) e precisam ser regenerados com a paleta real, agora com vermelho e amarelo confirmados.
- **Fonte da marca:** wordmark "construmais" em fonte arredondada bold levemente itálica ("constru" em amarelo, "mais" em branco) / títulos de impacto em fonte condensada geométrica bold (tipo Poppins ExtraBold ou Montserrat Black, a confirmar) / datas comemorativas em script cursiva dourada (tipo Pacifico ou Lobster, a confirmar) / apoio e legenda em sans-serif simples
  - Substitui a suposição anterior de "Inter" (system font stack neutra, sem base real). Fonte exata do wordmark e da condensada ainda não confirmada, listada como pendência no brand kit.

## Contexto Operacional & Mercado (briefing de reunião, 23/07/2026)
Ata completa em `historico/2026-07-23-briefing-reuniao-tony.md`.
- **Gestão interna:** a esposa do Tony atua como gerente da loja.
- **Logística:** retorno do motorista da loja previsto para 06/08/2026, com impacto direto no cronograma de operação/entrega.
- **Posicionamento atual:** a loja vende proporcionalmente mais para fora do seu raio de atuação imediato do que para o próprio bairro. Objetivo central declarado pelo Tony: inverter essa dinâmica e dominar a demanda local antes de expandir.
- **Percepção do cliente sobre a Pillar:** Tony citou explicitamente o dinamismo e a postura executiva/técnica da agência como diferencial frente à "mesmice" de agências tradicionais que já testou antes.
- **Contexto macro de João Pessoa/PB:** mudança de perfil econômico da cidade, historicamente 80/20 dependente de funcionalismo público, dando lugar ao avanço de grandes empresas e forte expansão imobiliária/hoteleira. Abertura do que seria o maior polo turístico do Nordeste (resorts, redes hoteleiras) está impulsionando a construção civil na região — tese de mercado do Tony, não dado oficial verificado pela agência.

## Oferta atual
- **O que está sendo promovido:** Materiais Básicos, Elétrica, Hidráulica e Pintura (linha completa de loja de material de construção)
- **Sistema Tintométrico (linha de acabamento / alto ticket):** sistema de tinta capaz de manipular até 5.000 cores. Objetivo de mídia (Google e Meta Ads) é posicionar a Construmais como referência local em tintas e mistura personalizada dentro do bairro Cristo Redentor e arredores. (Fonte: briefing 23/07/2026)
- **Material básico ensacado (linha de volume / alta margem):** venda de areia, brita e cascalho ensacados em sacos de 20 kg, com sacaria de ráfia personalizada da marca e máquina de costura própria para fechamento profissional. Margem por m³/unidade é bem mais alta que a venda a granel. Entrega de sacos de 20 kg é viável dentro do bairro; fora do bairro ou em maiores volumes fica inviável em pequenos lotes pelo custo de frete, exigindo frete dinâmico ou embutido no preço. Segmentação por bairros combina duas lógicas: áreas carentes de suprimento rápido de material básico e bairros de classe média/alta (público Z4, alto ticket). (Fonte: briefing 23/07/2026)
- **Preço / condição:** Não informado no formulário (sem menção a parcelamento, desconto ou frete grátis como política vigente). Não usar essas condições em copy sem confirmação adicional do cliente.
- **Ticket médio do cliente final:** até R$ 300 (baixo ticket, faixa "Até R$ 300" do formulário de onboarding, 21/07/2026)
- **Meta de conversão:** Venda (via orçamento gerado por WhatsApp/formulário que converte em compra na loja ou entrega)

## Público
- **Perfil:** Não detalhado explicitamente pelo cliente como persona, mas o formulário confirma o padrão B2C local + profissional autônomo já assumido no plano de julho de 2026: morador de João Pessoa fazendo reforma/construção e profissional (pedreiro, eletricista, encanador, pintor) comprando para obra de terceiros.
- **Dor concreta:** Confirmada indiretamente pelas "maiores dificuldades enfrentadas nas vendas" relatadas pelo cliente: frete quando cobrado, desconto e preço são os principais pontos de atrito no fechamento.
- **Frase verbatim do público:** Ainda não coletada. O formulário de onboarding não capturou fala literal de cliente final, só a visão do lojista.

## Tom da marca
- **Voz:** Próxima e informal (usa "a gente" em vez de "nós", tratamento direto ao cliente). Varia em 3 modos conforme o tipo de post: educativo/prestativo com dicas e emojis temáticos (⚠️🔥🔎), acolhedor e mais poético em datas comemorativas (Dia das Mães, Páscoa, Dia do Construtor), confiante e institucional em posts de trajetória/aniversário (reforça os 15 anos de mercado).
- **Personalidade:** Loja de bairro que resolve rápido, atendimento de confiança. Sempre fecha com CTA comercial claro (WhatsApp, endereço físico, "arrasta pro lado", "salva e compartilha").
  - Fonte: brand kit extraído em 2026-07-23 da análise do perfil, grid de posts e legendas do Instagram @construmaisjpa. **Substitui** a suposição anterior ("direta e prática, sem tecnicismo", marcada como não validada), agora com base em conteúdo real publicado pela marca.

## Identidade visual (brand kit @construmaisjpa, 2026-07-23)
- **Logo:** círculo vermelho com casa amarela estilizada e "C" branco no centro (remete a "casa" + inicial da marca). Arquivo real em `clientes/construmais/marca/logo-construmais.png`.
- **Mascote:** operário 3D (capacete amarelo, colete amarelo, camisa vermelha com o logo estampado, calça jeans, botas laranjas, segurando colher de pedreiro), usado em datas comemorativas e promoções para humanizar a marca. Arquivo real em `clientes/construmais/marca/mascote-construmais.png`.
- **Ícones recorrentes:** capacete de segurança, ferramentas, tomadas elétricas, vergalhões
- **Molduras/faixas:** faixas diagonais amarelas sobre vermelho para avisos e comunicados ("Comunicado!", "Aviso importante")
- **Fotografia:** produtos e trabalhadores reais, sempre com tratamento de cor quente (mesma temperatura vermelho-amarela da paleta)
- **Emojis recorrentes na comunicação:** 🏗️🔌📲📍✅ (reforçam o segmento e humanizam a mensagem)
- Fonte: mesmo brand kit do Instagram @construmaisjpa. Nenhum destes elementos vinha do formulário de onboarding original. Pendência: formalizar isso como guideline de marca completo (regras de uso do mascote, hex exatos, arquivo de fonte) se o cliente confirmar que quer consolidar identidade visual própria em vez da paleta neutra usada antes.

## Contrato com a Pillar
- **Início:** 16/07/2026. Contrato de 12 meses, vigência prevista até 16/07/2027.
- **Valor:** R$ 2.200,00/mês, contrato de 12 meses. Distinto do orçamento de mídia (R$ 2.000,00/mês pago direto às plataformas pela Construmais).
- **Escopo contratado (Anexo I):** reduzido de um detalhamento por 5 pilares para 4 itens, por decisão de redução de risco jurídico da Pillar: Curva ABC/giro de estoque (Pilar 1), Google Meu Negócio (Pilar 2), Tráfego Pago (Pilar 2), Treinamento Comercial (Pilar 4).
- **Fora do escopo contratado atualmente:** Pilar 3 (Combo de Produtos) e Pilar 5 (Plano Obra Integral). Tratar qualquer entrega nesses dois pilares como possível upsell futuro a negociar, não como entrega padrão já vendida ao cliente.
- **SLA:** 2 dias úteis para entrega ou alteração de arte/criativo.
- **Rescisão:** carência de 5 dias úteis após notificação por escrito antes de rescisão imediata (cláusula 6.2).

## Diagnóstico Método Viga Mestra (formulário de onboarding, 21/07/2026)

Respostas reais do cliente, organizadas pelos 5 pilares de `_squad/_shared/metodo-viga-mestra.md`. Substitui a nota anterior de "pendente de dado real".

### Pilar 1, Inteligência de Dados
- Sistema de gestão / ERP: Pontual Tecnologia
- Possui CRM: não
- Dados de cliente cadastrados no sistema: nome, celular (WhatsApp), e-mail, endereço, CPF
- **Análise refeita em 2026-07-23 com leitura direta dos 5 arquivos originais** (`Curva ABC parte 1 a 4.pdf`, 168 páginas lidas por completo, e `Estoque ETL.xlsx`, 15.228 linhas), não mais compilação de resumo de conversa. Catálogo ativo: 15.228 SKUs. Período coberto: 14 meses, 01/05/2025 a 30/06/2026, faturamento total confirmado de R$ 3.081.818,22 (média mensal R$ 220.129,87), custo total R$ 1.871.502,08, margem bruta agregada de 39,27%. Curva ABC estável nos 4 períodos: Classe A 56,7 a 60,2%, B 24,7 a 27,1%, C 15,1 a 16,2% do faturamento. Material Básico responde por 42,21% do faturamento, seguido de Hidráulica (10,10%) e Pintura (8,42%).
- **Auditoria de qualidade do dado de estoque (`Estoque ETL.xlsx`), confirmada com leitura direta da planilha:** fornecedor cadastrado como a própria loja (57 itens, exato), quantidade negativa (17 itens, exato, valor financeiro negativo de R$ 139.191,14), preço de venda zerado com estoque ativo (4 itens, exato), custo zerado com venda ativa (1 item, não 2 como se dizia antes), margem acima de 1.000% (27 itens, exato), margem negativa (199 itens, exato), custo final menor que custo inicial (104 itens, antes 103), categoria/grupo corrompido em 34,52% da base (5.257 itens, exato, confirmado como problema real do arquivo fonte, não artefato de leitura), produto com nome duplicado em código diferente (10 grupos, 24 códigos, antes citado como 20 itens). Inconsistência preço x custo/margem (checagem já embutida na própria planilha, tolerância de R$ 2): 147 itens, achado novo.
- **Suspeita de superfaturamento:** não foi possível reproduzir com os arquivos disponíveis a metodologia exata por trás do "18 casos confirmados, R$ 754.497" citado antes (não há campo de "caso confirmado" nos arquivos). O caso do colorante citado antes existe e foi relocalizado (código 11073, Custo Inicial R$ 131,13 x Custo Final R$ 0,16, cerca de 827x de distorção, antes citado como 1.075x, mesma direção do problema, magnitude um pouco diferente por método de cálculo). Rodando peer-comparison próprio (mediana de custo por categoria + unidade), encontrei 1.579 outliers acima de 6x a mediana (não 134), número maior porque o agrupamento por categoria+unidade é mais largo que subcategoria/família de produto; tratar como lista para checagem manual, não como confirmado. Ver lista dos 7 casos mais extremos e ressalvas de falso positivo no diagnóstico completo.
- **Estoque parado calculado pela primeira vez:** 1.682 itens sem nenhuma venda em nenhum dos 4 períodos (14 meses completos) e com saldo em estoque positivo, valendo R$ 320.903,02 a custo (35,6% de todo o custo de estoque atual, que é R$ 900.940,38 no total). Limitação: a planilha não tem campo de "data de última venda", só "data de última compra" (do fornecedor), então o cálculo usa ausência de venda nos 4 relatórios de Curva ABC, não uma data exata de última movimentação.
- **Contradições identificadas entre o diagnóstico anterior (compilado de memória) e a análise direta dos arquivos:** faturamento do recorte de 6 meses citado antes como R$ 732.186,81 não bate com o R$ 1.377.269,74 impresso no rodapé oficial da Parte 1 do relatório; recorte de 2 meses citado como R$ 341.258,40 não bate com R$ 454.844,56 do rodapé da Parte 2; custo total de estoque citado como "~R$ 550 mil" não bate com R$ 900.940,38 direto da planilha; potencial de venda do estoque citado como "mais de R$ 1 milhão" não bate com R$ 1.879.478,79 direto da planilha. Recomendado confirmar com o Tony se a fonte anterior usava outro filtro (categoria ou classe ABC específica) antes de descartar de vez os números antigos.
- Diagnóstico formal completo (Curva ABC, giro, margem por categoria, estoque parado, auditoria de dado, produtos isca, 5 candidatos a kit com efeito de margem calculado) em `clientes/construmais/outputs/2026-07-diagnostico-estoque.md`, produzido pelo `@inteligencia-dados` a partir dos arquivos originais.
- Este pilar já tem base analítica forte, mais forte inclusive que os demais, mas com pendência crítica de correção de dado antes de qualquer decisão de precificação ou kit basear-se nele.

### Pilar 2, Domínio Territorial
- Raio de entrega considerado lucrativo hoje: 5km
- **Raio de campanha de mídia paga (briefing 23/07/2026):** distinto do raio de entrega lucrativo acima. Definido inicialmente em até 10 km da loja, com foco no bairro Cristo Redentor (população estimada de ~40.000 pessoas), priorizando reconhecimento de marca e dominância de demanda local antes de expandir.
- Regiões foco (maior ticket, marcadas pelo cliente): Manaíra, Tambaú, Cabo Branco, Camboinha, Poço, Intermares, João Agripino, Brisamar. Também citadas com volume: Jardim Cidade Universitária, Bancários, Geisel, José Américo, Cidade dos Colibris, Anatólia, Centro, Jaguaribe, Penha, Tambauzinho
- Concorrentes diretos: Macol (mais tempo de loja), Lojão da Econômica (maior poder econômico), Carajás (home center), Araujo Material de Construção (mais tempo de loja, mix diversificado)
- Concorrentes adicionais (fonte distinta, levantamento de 23/07/2026, não veio do formulário de onboarding): **Tupan** (BR-230 km 24, Cristo Redentor — mesmo bairro da Construmais, foco em atacado e construtores, forte em telhas, caixas d'água e cimento, site próprio tupan.ind.br) e **Beira Rio Construção** (bairro Torre — posicionada em acabamento e tradição, showroom para pisos, louças e metais)
- Reviews do Google já existentes e positivos (bom atendimento, preços justos, variedade), mas é um ativo subutilizado hoje, não reforçado no site nem nas redes
- Já investe em anúncios atualmente: sim, Google Ads e Meta Ads (Instagram/Facebook)
- Orçamento mensal atual de marketing: R$ 2.000,00 (confirma o budget do briefing express de julho de 2026)

### Pilar 3, Combo de Produtos
- Ticket médio geral atual: até R$ 300
- Kits por fase de obra: não comercializa hoje, mas tem interesse em estruturar. Oportunidade direta de proposta.
- Cross-sell natural já observado pelo próprio lojista: areia e cimento (oferecer vedalit), joelho e tubo (oferecer cola), cerâmica e argamassa (oferecer rejunte), tinta e rolo de pintura (oferecer lixa)
- **Decisão estratégica confirmada (23/07/2026):** não montar combos/kits de produtos da Construmais incluindo produtos de acabamento, tendo em vista a concorrência de atacadistas e home centers próximos (ver Beira Rio Construção no Pilar 2). Kits devem ficar concentrados em material básico, elétrica, hidráulica e pintura.
- **Estratégia completa de 10 kits por fase de obra (fundação, estrutura, alvenaria, cobertura, impermeabilização, hidráulica esgoto, hidráulica água fria/metais, elétrica, revestimento, pintura, mais 2 kits transversais de fixação e ferramentas de corte) e playbook de execução comercial em `outputs/2026-07-estrategia-kits-e-vendas.md`.** Corrige um erro de domínio técnico do diagnóstico anterior (`outputs/2026-07-diagnostico-estoque.md`): o Kit Alvenaria tinha Tijolo + Argamassa Cola Forte AC-II, mas AC-II é argamassa colante para piso/cerâmica (norma ABNT), não serve para assentar tijolo. Composição corrigida: Tijolo + Areia Fina. A AC-II foi realocada para o Kit Revestimento, onde se aplica de fato.
- **Nota de escopo:** ainda que o Pilar 3 esteja fora do contrato assinado hoje, o Tony e a Pillar tratam os 5 pilares como parte de um método único, então o material de kits acima é produzido como entregável completo, a formalizar como upsell de contrato quando o cliente confirmar.

### Pilar 4, Vendedor de Elite
- Volume diário estimado de orçamentos: até 15/dia
- Taxa de conversão orçamento-venda: não monitorada ("não temos esta métrica")
- Tempo médio de resposta declarado: até 15 minutos
- Roteiro/script de vendas: existe, mas informal (não formalizado)
- Remuneração da equipe: apenas salário fixo, sem comissão
- Follow-up de orçamento não fechado: não é feito hoje
- Maiores dificuldades relatadas na venda: frete quando cobrado, desconto, preço
- Nota: este é o pilar com maior lacuna de processo hoje (sem follow-up, sem métrica de conversão, script informal). Prioridade natural para o playbook de atendimento do `@copywriter`.

### Pilar 5, Plano Obra Integral
- Parcerias ou benefícios para profissionais da construção (pedreiro, encanador etc.): não existe hoje
- Acompanhamento de fase da obra do cliente para ofertar próxima etapa: não é feito
- Mecanismo de fidelização do consumidor final: não existe, mas tem interesse
- **Estratégia B2B e parcerias de campo (briefing 23/07/2026):** a Construmais atende do começo ao fim da obra. Plano de estruturação de programas formais de indicação e fornecimento para: administradoras de condomínios (material básico ensacado para reparos e manutenção predial), indústrias/fábricas/comércios locais (suprimento recorrente via contrato direto), e vendedores/instaladores de piscina de fibra (parceria pela demanda contínua de areia de assentamento/filtro). Já é homologada junto ao Grupo Aena (aeroportos), Sistema Loggi/Grupo MRV e Controll (setor elétrico). Para especificadores (arquitetos, engenheiros, mestres de obra, construtoras), o comportamento observado é que o cliente final B2B/residencial geralmente compra por indicação direta do profissional de campo, não por busca própria.

### Objetivos declarados pelo cliente
- Meta para os próximos 12 meses: dobrar o faturamento
- Expectativa com a assessoria da Pillar: ganhar visibilidade onde ainda não é conhecido, virar opção de compra com aumento de seguidores, e ajudar a atingir a meta de faturamento
- Algo não perguntado que o cliente queira mencionar: não

## Presença Digital & Social Media (briefing 23/07/2026)
- **Dor atual do cliente:** desejo claro de ganhar seguidores qualificados e construir autoridade local.
- **Posicionamento pessoal:** humanizar a comunicação e transformar o Instagram no "rosto do Tony" (autoridade e presença do dono), reforçando o padrão institucional já identificado no brand kit.
- **Alinhamento operacional:** o Tony está cotando uma agência parceira de Social Media para captação presencial de conteúdo na loja (fotos e vídeos), fora do escopo contratado com a Pillar.
- **Ação pendente da Pillar:** solicitar ao Tony o acervo de vídeos e fotos brutas da estrutura física e do estoque da loja, para uso em campanhas de performance/resposta direta enquanto o banco de fotos formal não existe (pendência já registrada nos outputs de Google Meu Negócio e dos criativos de Dia dos Pais).

## Plano de Ação (reunião de briefing, 23/07/2026)
| Ação | Prioridade | Responsável | Prazo |
| :--- | :---: | :---: | :---: |
| Configurar campanhas de tráfego local (Google Perfil / Meta) no raio de 10km (foco: Cristo Redentor) | Alta | Agência Pillar | A definir |
| Estruturar oferta de Tintas / Sistema Tintométrico (até 5 mil cores) | Alta | Agência Pillar | A definir |
| Criar campanha específica de Materiais Ensacados para condomínios e bairros alvo | Média | Agência Pillar | A definir |
| Solicitar acervo de vídeos e fotos da loja ao Tony | Alta | Atendimento | Imediato |
| Alinhar cronograma considerando o retorno do motorista | Média | Operacional | 06/08/2026 |

## Compliance
- **Restrições do nicho:** Nenhuma regulamentação setorial específica (não é saúde, direito ou financeiro). Aplica-se o Código de Defesa do Consumidor padrão: preço exibido em anúncio precisa ser real e vigente, prazo de entrega prometido precisa ser cumprível, garantia mencionada precisa ser a política real da loja.
- **O que não pode ser dito:** Preço ou condição de parcelamento que não seja política real e vigente da loja. Prazo de entrega que a loja não consegue cumprir. Frete grátis, já que o cliente relatou frete cobrado como ponto de atrito, não como cortesia.

## Tracking
- **Pixel Meta ID:** [PREENCHER - não veio no formulário de onboarding]
- **GA4 ID:** [PREENCHER - não veio no formulário de onboarding]
- **Domínio principal:** construmaisjp.com.br
- **Ad Account ID Meta (act_...):** [PREENCHER - opcional, necessário só se for usar Meta Ads CLI Nível 2/3]

## Métricas-alvo
- **CPL meta:** R$ 30-80 (benchmark adaptado de "Reforma/Construção" em `_squad/01-gestor-trafego/benchmarks.md`. O nicho "loja de material de construção" já está catalogado em `_shared/nichos.md`, mas `benchmarks.md` ainda não tem uma linha numérica dedicada, então a aproximação segue valendo até termos entrada própria lá)
- **CPA meta:** R$ 60-150 (estimativa anterior). Agora que o ticket médio real é conhecido (até R$ 300, baixo ticket), este número deve ser recalculado pelo `@gestor-trafego` na próxima rodada. Falta ainda margem de lucro e taxa de fechamento real (o cliente não monitora "a cada 10 orçamentos, quantas vendas"), então o recálculo fica como estimativa até esses dois dados existirem.
- **ROAS meta:** não aplicável neste momento (loja física sem e-commerce declarado). Se o cliente abrir venda online com catálogo, recalcular.

## Histórico
- **2026-07:** Cliente novo. Primeira entrega do squad: plano de tráfego, copy, carrossel, landing page e dashboard de metas.
- **2026-07-23:** Migração de contexto para a pasta do cliente: nicho "loja de material de construção" formalizado em `_shared/nichos.md`, identidade da Pillar registrada em `_shared/identidade-agencia.md`, Método Viga Mestra documentado em `_shared/metodo-viga-mestra.md` e ligado a este cliente. Dashboard de julho atualizado com o nome da agência no rodapé.
- **2026-07-23 (mesma data, atualização):** Formulário de onboarding do cliente (Método Viga Mestra) recebido e processado. CNPJ, endereço, e-mail, site, Instagram, ticket médio e diagnóstico completo dos 5 pilares preenchidos com dado real. Pendências que restam: preço/condição comercial, frase verbatim do público final, Pixel Meta ID, GA4 ID, margem de lucro e taxa de conversão de orçamento.
- **2026-07-23 (mesma data, segunda atualização):** Levantamento de conversas anteriores do projeto no claude.ai trouxe: telefones corrigidos (fixo e WhatsApp do site oficial, substituindo o número único do formulário), termos do contrato Pillar-Construmais (R$ 2.200/mês, escopo real de 4 dos 5 pilares), site institucional existente já replicado como base editável, e a auditoria de estoque com suspeita de superfaturamento de aproximadamente R$ 754 mil. Diagnóstico formal do Pilar 1 criado pelo `@inteligencia-dados` em `outputs/2026-07-diagnostico-estoque.md`.
- **2026-07-23 (mesma data, terceira atualização):** Diagnóstico do Pilar 1 refeito do zero com leitura direta dos 5 arquivos originais (`Curva ABC parte 1 a 4.pdf`, `Estoque ETL.xlsx`), não mais compilação de resumo de conversa. Maior parte dos achados da auditoria de estoque confirmada com exatidão (fornecedor próprio, quantidade negativa, margem >1.000%, margem negativa, categoria corrompida). Estoque parado calculado pela primeira vez (R$ 320.903,02, 1.682 itens). Encontradas contradições relevantes entre o que se dizia antes e o que os arquivos mostram: faturamento dos recortes de 6 e 2 meses, custo total de estoque e potencial de venda do estoque não bateram com os números anteriores (ver diagnóstico completo para o detalhe). O número de R$ 754 mil de superfaturamento em 18 casos não pôde ser reproduzido com os arquivos disponíveis.
- **2026-07-23 (quarta atualização):** Brand kit real extraído da análise do Instagram @construmaisjpa (perfil, grid de posts, legendas): paleta vermelho/amarelo/laranja com mascote de operário, tipografia condensada bold + wordmark arredondado + script dourada, voz próxima e informal variando entre modo educativo, acolhedor (datas comemorativas) e institucional (trajetória/aniversário). Substitui a paleta laranja terracota e a suposição de tom "direto e prático" registradas antes, que eram estimativas sem dado real de marca. Pendências: hex exatos ainda são aproximação visual, fonte exata do wordmark/condensada não confirmada, e os 3 outputs de 2026-07 (carrossel, dashboard, LP) precisam ser regenerados com a paleta real.
- **2026-07-23 (quinta atualização):** Vermelho e amarelo da paleta de marca confirmados em hex exato: `#EE2526` e `#F4D000`. Substitui os intervalos aproximados extraídos do grid do Instagram na atualização anterior. Laranja intermediário (`#F7941D`) segue pendente de confirmação.
- **2026-07-23 (sexta atualização):** Levantamento de mais uma conversa anterior trouxe: origem do site institucional (feito pela Anova Agência, sem blog/catálogo/SEO), Facebook (/construmaisjp), concorrentes adicionais no Pilar 2 (Tupan e Beira Rio Construção, fonte distinta do formulário de onboarding) e reviews do Google positivas mas subutilizadas, e confirmação da decisão estratégica de não incluir produtos de acabamento em kits/combos do Pilar 3 por causa dos atacadistas e home centers próximos.
- **2026-07-23 (sétima atualização):** Logo e mascote reais da Construmais salvos em `marca/logo-construmais.png` e `marca/mascote-construmais.png` (mascote corrigido: capacete e colete amarelos, não laranja como se supunha antes pelo grid do Instagram). Criado `outputs/2026-07-estrategia-kits-e-vendas.md` com estratégia de 10 kits por fase de obra e playbook de execução comercial (Pilar 3 e Pilar 4). Esse arquivo corrige um erro de domínio técnico do diagnóstico anterior (`outputs/2026-07-diagnostico-estoque.md`, kit Alvenaria tinha Argamassa AC-II em vez de Areia Fina) e detalha faturamento por categoria dentro de cada Curva ABC (A, B e C). Pendência: confirmar com o Tony se ele topa formalizar o Pilar 3 no contrato.
- **2026-07-23 (oitava atualização):** Margem combinada exata do Kit Alvenaria recalculada com Areia Fina no lugar da AC-II: 31,38%, contra 33,82% do Tijolo isolado (queda de 2,44 pontos percentuais, não ganho). Achado relevante: ao contrário dos outros 4 kits calculados, o pareamento tecnicamente correto reduz a margem percentual porque a Areia Fina tem margem própria mais baixa que o Tijolo. O argumento comercial desse kit específico passa a ser captura de compra conjunta (cimento, areia e tijolo são comprados juntos na mesma obra), não ganho de margem. Atualizado em `outputs/2026-07-diagnostico-estoque.md` e `outputs/2026-07-estrategia-kits-e-vendas.md`.
- **2026-07-23 (nona atualização):** Vermelho e amarelo da paleta de marca confirmados em hex exato: `#EE2526` e `#F4D000`. Os 3 outputs de julho (`2026-07-carrossel-oferta.html`, `2026-07-dashboard-metas.html`, `2026-07-landing-page-captura.html`) foram regenerados com a paleta correta, substituindo o laranja terracota antigo. Pendência remanescente: laranja intermediário (`#F7941D`) e a fonte exata do wordmark/condensada seguem sem confirmação; considerar também revisão de cor do mascote à luz da correção registrada na sétima atualização (capacete/colete amarelos, não laranja).
- **2026-07-23 (décima atualização):** Ajuste na descrição da paleta: o laranja `#F7941D` deixa de ser tratado como cor do mascote (capacete/colete) e passa a uso pontual (só nas botas), já que o arquivo real do mascote (sétima atualização) mostra capacete e colete amarelos. Amarelo `#F4D000` confirmado como cor do mascote. Sem impacto nos 3 outputs regenerados, que não usam variável de laranja.
- **2026-07-23 (décima primeira atualização):** Criado `outputs/2026-07-otimizacao-google-meu-negocio.md` com otimização completa do perfil Google Meu Negócio (Pilar 2, item contratado): descrição, categorias, lista de produtos por prioridade de faturamento, Q&A, calendário de posts de 30 dias e estratégia de avaliações reais (sem review simulada). Pendências levantadas que ainda faltam confirmar com o Tony: horário de funcionamento, política de frete, prazo de entrega, forma de pagamento e banco de fotos de produto.
- **2026-07-23 (décima segunda atualização):** Criado `outputs/2026-07-23-script-respostas-avaliacoes-google.md` com scripts de resposta a avaliação do Google (5 estrelas, 3-4 estrelas, 1-2 estrelas), complementando a estratégia de captação de review já registrada em `outputs/2026-07-otimizacao-google-meu-negocio.md`. Pendência: respostas que tocam frete/prazo/pagamento/horário só reconhecem o ponto e chamam pro WhatsApp, sem confirmar política real, até o Tony validar.
- **2026-07-23 (décima terceira atualização):** Criado `outputs/2026-07-23-apresentacao-kits-inteligentes.md`, versão client-facing da estratégia de kits (Pilar 3) para o Tony decidir sobre formalizar upsell de contrato. Resume os 3 kits prioritários, roadmap das outras 9 combinações mapeadas e nota de escopo (Pilar 3 fora do Anexo I assinado).
- **2026-07-23 (décima quarta atualização):** Criado `outputs/2026-07-23-script-cliente-oculto-concorrentes.md` com script de cliente oculto (WhatsApp) para os 6 concorrentes diretos, cobrindo preço de Tijolo/Cimento/Areia Fina/Pedra Britada, frete, prazo e forma de pagamento. Execução manual pendente (pessoa do time, número neutro).
- **2026-07-23 (décima quinta atualização):** Criado `outputs/2026-07-23-skus-ferramentas-kit-dia-dos-pais.md`, aprofundamento em SKU da categoria Ferramentas para a campanha de Dia dos Pais. Achado: Carro de Mão 65L Tramontina é o único item de ticket alto com giro/margem comprovados; furadeira e parafusadeira elétricas têm giro próximo de zero, não sustentam kit ancorado nelas.
- **2026-07-23 (décima sexta atualização):** Criado `outputs/2026-07-23-pesquisa-concorrentes-dia-dos-pais.md`. Nenhum dos 6 concorrentes diretos tem campanha de Dia dos Pais confirmada publicamente hoje; mercado nacional do nicho (Leroy Merlin, Telhanorte, C&C) já valida a data. Achado à parte: domínio `tupan.ind.br` registrado como site do concorrente Tupan parece pertencer a outra empresa, pendente de verificação com o Tony.
- **2026-07-23 (décima sétima atualização):** Criado `outputs/2026-07-23-plano-trafego-dia-dos-pais.md`: Meta Ads como plataforma prioritária, Google evergreen mantido, estrutura para Kit Reforma e Kit Ferramenta Manual (sem preço fechado), calendário comprimido para 17 dias (campanha até 09/08/2026). Bloqueios: aval do Tony pro Pilar 3 e preço do kit; pendência de confirmar split de budget Google/Meta.
- **2026-07-23 (décima oitava atualização):** Criado `outputs/2026-07-23-copy-campanha-dia-dos-pais.md` com 6 headlines, 2 anúncios completos, 1 anúncio backup com o mascote, mensagens de WhatsApp pré-preenchidas e reforço do script de resposta ultrarrápida (Pilar 4) para leads de Dia dos Pais. Placeholders de preço seguem pendentes de confirmação do Tony.
- **2026-07-23 (décima nona atualização):** Criados os 3 criativos de Dia dos Pais pelo `@designer-carrossel` (carrossel Kit Reforma, carrossel Kit Ferramenta Manual, imagem backup com mascote real). Produtos em ilustração/ícone por falta de banco de fotos real; preços com placeholder bloqueado até confirmação do Tony.
- **2026-07-23 (vigésima atualização):** Briefing de reunião com o Tony (ata completa em `historico/2026-07-23-briefing-reuniao-tony.md`) trouxe contexto operacional (esposa gerente da loja, retorno do motorista em 06/08/2026, percepção do cliente sobre o diferencial da Pillar), diagnóstico macro de João Pessoa (mudança de perfil econômico, polo turístico), geomarketing do bairro Cristo Redentor (~40.000 hab, raio de campanha de mídia definido em 10km, distinto do raio de entrega lucrativo de 5km já registrado), detalhamento do Sistema Tintométrico (5.000 cores) e da estratégia de Material Básico Ensacado (sacos de 20kg, sacaria própria, lógica de raio de entrega), estratégia B2B (condomínios, indústrias, piscineiros, homologações Aena/Loggi-MRV/Controll, especificadores) e plano de ação com 5 itens. Menção do Tony ao Grupo Elizabeth tratada como comentário pontual, não item de plano (relacionamento encerrado após aquisição estrangeira do grupo). CLIENTE.md atualizado com os dados nas seções correspondentes (Contexto Operacional, Oferta atual, Pilar 2, Pilar 5, Presença Digital, Plano de Ação).
