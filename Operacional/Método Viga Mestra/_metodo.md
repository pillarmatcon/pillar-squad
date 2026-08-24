# Método Viga Mestra

Metodologia proprietária da Pillar para lojas de material de construção (MatCon), o único nicho que a agência atende. Este arquivo é a biblioteca completa de playbooks: os 5 pilares, cada atividade dentro deles e as tarefas/scripts já documentados, tudo num só lugar.

## Regra: aqui é template, não execução

Todo conteúdo deste arquivo é genérico, com `[placeholders]` no lugar de qualquer dado de cliente (nome da loja, WhatsApp, telefone, nome de vendedor). Isso permite seguir a tarefa, executar, delegar pra um colaborador ou pedir pro squad rodar, pra qualquer cliente MatCon.

A versão real, preenchida com o dado do cliente, fica em `Operacional/clientes/<nome>/outputs/`, nunca aqui.

## Onde está o "porquê" de cada pilar

O racional completo dos 5 pilares (problema que resolve, resultado que busca, qual agente do squad mais aplica) está em `_squad/_shared/metodo-viga-mestra.md` — essa é a fonte da verdade sobre o "porquê". Este arquivo aqui é o "como": o playbook operacional de cada atividade.

## Ferramenta associada (Curva ABC)

O Pilar 1 tem uma ferramenta pronta (script Python, não template) que converte PDF de Curva ABC do sistema Pontual Tecnologia em XLSX padronizado, zero IA na conversão. Fica em `Operacional/Método Viga Mestra/Ferramenta Curva ABC/` (`SKILL.md` + `pillar_padroniza_curva_abc.py`), fora deste arquivo porque é código, não playbook.

## Quando uma atividade não tem nenhuma tarefa/script ainda

Fica dito explicitamente na própria atividade, abaixo. Não existe tarefa "fantasma" só pra preencher espaço. Ao documentar uma tarefa nova com passo a passo pronto, seguir `_squad/_shared/template-tarefa.md`.

## Sumário

1. Inteligência de Dados — Curva ABC do Estoque, Giro de Estoque e Margem, Produtos Isca
2. Domínio Territorial — Google Meu Negócio, Anúncios Geolocalizados, Captura de Buscas em Alta
3. Combo de Produtos — Kits Inteligentes por Fase da Obra, Checklist de Venda Adicional, Precificação Isca
4. Vendedor de Elite — Resposta Ultrarrápida, Playbook de Fechamento de Orçamento, Régua de Follow-up
5. Plano Obra Integral — Jornada do Cliente, Bônus e Cashback de Recompra, Cronograma de Ofertas Preditivas, Parceria com Profissionais

---

# Pilar 1: Inteligência de Dados

Agente que mais aplica: `@inteligencia-dados`.

**Problema que resolve:** dinheiro preso em estoque parado e perda de venda por falta de produto.

**Resultado que busca:** estoque que vira caixa rápido e compra baseada em demanda real.

## Atividade 1.1 — Curva ABC do Estoque

Classificar cada produto pelo peso real que ele tem no negócio (faturamento e margem), a partir das vendas registradas no ERP, e usar essa classificação como lente para ler o estoque. A curva em si é feita com base nas vendas, nunca na quantidade parada em prateleira. É a base de tudo: sem saber o que é A, B ou C, qualquer decisão de compra, exposição ou campanha vira chute.

**Duas coisas diferentes: curva e leitura de estoque**

- A curva ABC usa vendas, não estoque. O critério de corte (A ≈80%, B ≈15%, C ≈5%) é sempre sobre faturamento e margem gerados no período, nunca sobre quantidade em estoque. Um item pode ter estoque baixo e ainda ser A (porque vende muito), ou estoque alto e ser C (porque não vende).
- O estoque é lido depois, à luz da curva, mas em atividade própria (1.2, Giro de Estoque e Margem). Esta atividade entrega o "o que vende e quanto vale"; a leitura de estoque em cima disso é sempre da atividade seguinte.
- O relatório de Curva ABC já traz o "Grupo Z" (ou nomenclatura equivalente do ERP do cliente): os SKUs sem nenhuma venda no período coberto. É matéria-prima pra giro parado e estoque parado, mas essa leitura em si é documentada na atividade 1.2, não aqui. Só cito a origem (relatório, período, Grupo Z) quando a atividade 1.2 usar esse dado.

**Por que importa pra performance**

Loja de material de construção costuma ter centenas de SKUs, mas uma fração pequena deles concentra a maior parte do faturamento. Sem a curva feita, o dono trata os itens A (os que sustentam o caixa) com a mesma atenção dos itens C (os que ocupam prateleira e capital parado). Isso custa duas coisas ao mesmo tempo: falta do produto que mais vende (ruptura de estoque no item A, oportunidade de faturamento perdida) e capital preso em item que quase não gira (item C parado). A curva ABC corrige as duas em um único diagnóstico.

**Como executar**

1. Pedir ao cliente a exportação do relatório de estoque/vendas do ERP (Curva ABC pronta, ou vendas por SKU no período).
2. Se a fonte for PDF do sistema Pontual Tecnologia, rodar antes a ferramenta em `Operacional/Método Viga Mestra/Ferramenta Curva ABC/SKILL.md` (script `pillar_padroniza_curva_abc.py`) pra converter em XLSX padronizado.
3. `@inteligencia-dados` classifica os produtos em A (≈80% do faturamento), B (≈15%) e C (≈5% restante), usando sempre dado de venda, documentando o critério de corte usado.
4. Cruzar a classificação por faturamento com a classificação por margem bruta, pois nem todo item A em faturamento é A em margem.
5. Entregar o diagnóstico com a participação de cada categoria de produto (básico, elétrica, hidráulica, pintura, acabamento, ferramentas) na curva.
6. Passar a classificação (e o Grupo Z, se o relatório trouxer) pra atividade 1.2, que calcula giro, capital parado e risco de ruptura em cima dela.

**Cadência recomendada:** mensal para clientes com movimento intenso; trimestral é o mínimo aceitável para não perder a fotografia do negócio desatualizada. Recalcular sempre que o cliente trouxer um relatório novo, mesmo fora do ciclo.

**Indicadores de sucesso**

- % do faturamento concentrado nos itens A (referência de saúde: 70 a 85%)
- Grupo A, B e C bem definidos e estáveis entre períodos (se o corte muda muito de um período pro outro sem motivo de negócio, vale revisar o critério)

Indicadores de giro, capital parado e risco de ruptura ficam na atividade 1.2, calculados sobre esta classificação.

**Squad responsável:** `@inteligencia-dados` executa. Exige relatório real de ERP anexado, nunca estima número sem fonte.

**Operação enxuta:** uma curva ABC bem feita substitui reunião de "achismo" sobre o que comprar. É a atividade de maior alavancagem do Pilar 1: baixo esforço de execução (um relatório, uma rodada de classificação), alto impacto na decisão de compra e campanha dos meses seguintes.

**Tarefas desta atividade**

1. **Padronização do relatório de origem** (quando PDF Pontual): converter pra XLSX antes de qualquer leitura, script determinístico, zero custo de IA na conversão. Ferramenta pronta em `Operacional/Método Viga Mestra/Ferramenta Curva ABC/`: `SKILL.md` + `pillar_padroniza_curva_abc.py`.
2. **Classificação ABC por faturamento**: ordenar produtos por receita de venda, aplicar corte 80/15/5, documentar o critério.
3. **Classificação ABC por margem**: repetir o corte usando margem bruta em vez de faturamento, e apontar onde as duas classificações divergem.
4. **Leitura de participação por categoria**: consolidar a curva por categoria de produto, não só por SKU individual, pra virar leitura executiva pro dono da loja.

Leitura de giro, capital parado, risco de ruptura e giro parado (a partir desta classificação e do Grupo Z do relatório, se houver) é tarefa da atividade 1.2, não desta atividade.

As tarefas 2 a 4 ainda não têm arquivo `.md` de script pronto. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

## Atividade 1.2 — Giro de Estoque e Margem

Cruzar dois números que sozinhos enganam: giro (quão rápido o produto vende) e margem (quanto sobra em cada venda). Um item pode girar rápido e dar pouco lucro, ou girar devagar e ser essencial pra margem. A leitura só fica útil quando os dois são vistos juntos.

**Por que importa pra performance**

Dinheiro parado em estoque é dinheiro que a loja não tem em caixa. Quando ninguém mede giro por categoria, o padrão de compra vira reposição no automático, comprando de novo o que sempre foi comprado, sem checar se aquele item ainda merece espaço de prateleira e capital de giro. Cruzar com margem evita o erro oposto: cortar um item de giro baixo que na verdade sustenta boa parte do lucro.

**Uso direto em decisão de mídia.** Esta atividade não é só leitura financeira, é insumo direto pro `@gestor-trafego`/`@copywriter` decidirem o que anunciar: (1) **risco de ruptura**, item de giro alto com estoque baixo ou caindo não deve entrar em campanha nova sem reforço de compra confirmado, ou tem o orçamento reduzido até repor, anunciar o que vai faltar queima verba e frustra cliente; (2) **giro parado**, item com estoque alto e saída lenta é candidato a virar foco de campanha ou promoção pra desovar, a mídia empurra o que não sai sozinho. As duas leituras dependem de cruzar venda (Curva ABC) com estoque, por isso um input central desta atividade é o "Grupo Z" que já vem dentro do relatório de Curva ABC (SKUs sem venda no período), complementado por snapshot de estoque separado quando o cliente mandar um.

**Como executar**

1. Calcular giro por SKU/categoria: quantidade vendida no período dividida pelo estoque médio do mesmo período. Cruza a classificação ABC (vinda da atividade 1.1) com o estoque físico de cada produto.
2. Calcular margem bruta (%) e margem bruta absoluta (R$) por SKU/categoria.
3. Montar a matriz giro x margem em 4 quadrantes: alto giro/alta margem (estrela, priorizar), alto giro/baixa margem (produto isca, ver atividade 1.3), baixo giro/alta margem (manter, é reserva de lucro), baixo giro/baixa margem (candidato a liquidar ou descontinuar).
4. Identificar estoque parado: produto sem saída há mais de 6 meses (ou o período que o cliente definir), com valor financeiro parado a custo. Usa o "Grupo Z" do relatório de Curva ABC como base, refinado por snapshot de estoque separado quando existir (quantidade e custo mais atuais).
5. Sinalizar risco de ruptura: item A ou B (da curva) com giro alto e estoque baixo ou em queda, pronto pra virar alerta antes de entrar ou continuar em campanha.
6. Sinalizar giro parado como oportunidade de mídia: item de estoque alto e saída lenta, candidato a campanha/promoção de desova, handoff explícito pro `@copywriter`/`@gestor-trafego`.
7. Recomendar ação por quadrante, sem decidir preço ou promoção sozinho, essa decisão é do `@copywriter`/`@gestor-trafego` ou do cliente.

**Cadência recomendada:** mensal, alinhada com o fechamento do ERP do cliente. Estoque parado pode ser revisado a cada 2 meses, o quadro muda pouco em ciclos mais curtos.

**Indicadores de sucesso**

- R$ parado em estoque de baixo giro (tendência: caindo mês a mês)
- Giro médio dos itens A da curva ABC
- Nº de itens movidos do quadrante "baixo giro/baixa margem" para liquidação ou descontinuação
- Nº de itens A/B sinalizados com risco de ruptura antes de entrar em campanha (referência: zero campanha nova rodando sobre item sem esse checklist)
- Nº de itens de giro parado que viraram campanha/promoção de desova

**Squad responsável:** `@inteligencia-dados` executa e documenta o critério de agrupamento usado. Resultado alimenta `@analista-dados` (KPI de dashboard) e `@copywriter`/`@gestor-trafego` (decisão de que anunciar, risco de ruptura antes de subir campanha e giro parado como foco de promoção).

**Operação enxuta:** não é necessário recalcular giro produto a produto toda semana, isso é ruído. O ganho real vem de rodar a matriz uma vez por mês e agir nos poucos itens que mudaram de quadrante, não em recalcular tudo com frequência desnecessária.

**Tarefas desta atividade**

1. **Cálculo de giro por SKU/categoria**: quantidade vendida ÷ estoque médio no período.
2. **Cruzamento giro x margem (matriz 2x2)**: classificar cada categoria nos 4 quadrantes e documentar a leitura.
3. **Identificação de estoque parado**: produtos sem saída há mais de 6 meses, com valor financeiro parado a custo, usando o Grupo Z da Curva ABC como base.
4. **Sinalização de risco de ruptura**: itens A/B com giro alto e estoque baixo/caindo, handoff pro `@gestor-trafego`/`@copywriter` antes de subir ou manter campanha.
5. **Sinalização de giro parado como oportunidade de mídia**: itens de estoque alto e saída lenta, handoff pro `@copywriter`/`@gestor-trafego` como candidato a campanha de desova.
6. **Recomendação de ação por quadrante**: liquidar, manter, priorizar ou investigar, sem decidir preço final.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

## Atividade 1.3 — Produtos Isca

Identificar os produtos de giro altíssimo e margem baixa que trazem o cliente pra dentro da loja, mesmo sem serem os mais lucrativos por unidade vendida. Cimento, areia e itens básicos costumam entrar nessa categoria em loja de material de construção.

**Por que importa pra performance**

Produto isca não existe pra dar lucro sozinho, existe pra gerar fluxo. O erro comum é tratar item isca como qualquer outro e tentar aumentar margem nele, o que afasta o cliente logo na porta de entrada. O acerto é reconhecer o papel estratégico do item isca e usar o fluxo que ele gera pra empurrar o mix de alta margem (handoff direto pro Pilar 3, Combo de Produtos).

**Como executar**

1. Partir da matriz giro x margem (atividade 1.2) e isolar o quadrante alto giro/baixa margem.
2. Confirmar que o item realmente puxa fluxo de cliente novo pra loja, não é só um item barato sem relevância de venda.
3. Checar se o preço praticado não está abaixo do custo, produto isca com margem negativa é prejuízo disfarçado de estratégia.
4. Cruzar cada produto isca com o produto de margem mais alta da mesma etapa de obra, gerando candidatos a kit.
5. Entregar a lista de produtos isca com o racional de por que cada um foi classificado assim, sem decidir preço ou promoção, isso é do `@copywriter`/`@gestor-trafego`.

**Cadência recomendada:** revisão trimestral, junto com a atualização da curva ABC. Produto isca muda pouco de um mês pro outro, ciclo mais curto não traz ganho.

**Indicadores de sucesso**

- Nº de produtos isca identificados com candidato a kit associado (handoff completo pro Pilar 3)
- Margem mínima garantida no item isca (nunca abaixo do custo)
- Participação do item isca no fluxo de clientes novos, quando o cliente tiver esse dado

**Squad responsável:** `@inteligencia-dados` identifica. `@copywriter` e `@gestor-trafego` decidem o que fazer com a informação (kit, precificação, campanha).

**Operação enxuta:** poucos produtos isca sustentam a maior parte do fluxo. Não é preciso vasculhar o catálogo inteiro, é preciso confirmar os 3 a 5 itens que já são candidatos óbvios pelo giro e formalizar o racional, pra virar direcionamento consistente pro squad inteiro em vez de decisão informal do dono da loja.

**Tarefas desta atividade**

1. **Identificação de produtos âncora**: isolar o quadrante alto giro/baixa margem da matriz da atividade anterior.
2. **Checagem de margem mínima**: garantir que nenhum item isca está sendo vendido abaixo do custo.
3. **Cruzamento com candidato a kit**: parear produto isca com produto de margem complementar da mesma fase de obra (handoff pro Pilar 3).

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

---

# Pilar 2: Domínio Territorial

Agente que mais aplica: `@gestor-trafego`.

**Problema que resolve:** verba de anúncio jogada fora com quem está longe ou é só "curioso".

**Resultado que busca:** ser a primeira opção (top of mind) num raio de entrega lucrativo.

## Atividade 2.1 — Google Meu Negócio

Manter o Perfil da Empresa no Google (Google Meu Negócio) completo, atualizado e respondido, pra ser a opção que aparece primeiro quando alguém no bairro busca "material de construção perto de mim".

**Por que importa pra performance**

O Perfil da Empresa é o ativo de menor custo e maior retorno em domínio territorial: não tem CPC, não compete em leilão, e aparece justamente pra quem já está buscando ativamente. Um perfil incompleto ou sem resposta às avaliações perde posição no mapa pra concorrente que cuida do próprio perfil, mesmo que o produto e o preço sejam iguais.

**Como executar**

1. Checar se o perfil está com categoria principal e categorias secundárias corretas, horário de funcionamento real, endereço e telefone conferidos.
2. Completar atributos do perfil (aceita cartão, tem estacionamento, faz entrega) e subir fotos reais da loja e da equipe, não banco de imagem.
3. Publicar posts semanais no perfil (novidade de estoque, promoção pontual, obra de cliente com autorização), o Google prioriza perfil ativo.
4. Responder toda avaliação nova em até poucos dias, usando o script de variações (tarefa 2.1.1 abaixo).
5. Monitorar a seção de Perguntas e Respostas do perfil, responder perguntas de clientes em potencial antes que um concorrente responda por eles.

**Cadência recomendada:** checklist de otimização: revisão mensal. Postagem: semanal. Resposta a avaliação: em até 2-3 dias corridos após ela aparecer.

**Indicadores de sucesso**

- Nota média do perfil e volume de avaliações respondidas (meta: 100% respondidas)
- Nº de posts publicados no mês (meta: ao menos 4)
- Posição do perfil no pacote local (Google Maps) pras buscas mais relevantes do nicho

**Squad responsável:** `@gestor-trafego` executa e mantém o checklist.

**Operação enxuta:** isso não exige ferramenta paga nem agência dedicada full time: 15 a 20 minutos por semana bem usados (1 post + resposta de avaliação pendente) já sustentam o perfil ativo. O erro mais comum não é falta de tempo, é abandonar o perfil depois do cadastro inicial.

**Tarefas desta atividade**

1. Respostas a avaliações do Google — script com variações por faixa de nota, ver 2.1.1 abaixo.
2. Checklist de otimização de perfil — ver 2.1.2 abaixo.
3. Rotina de postagem semanal e priorização de fotos — ver 2.1.3 abaixo.
4. **Monitoramento de Perguntas e Respostas**: checagem periódica pra responder antes do concorrente ou de um usuário qualquer (coberto dentro do checklist de otimização de perfil, item 5 de 2.1.2).

### 2.1.1 — Script de respostas a avaliações do Google

Alterne entre as variações pra não repetir sempre o mesmo texto. Troque `[nome]` pelo nome que aparece na avaliação, `[nome da loja]`, `[whatsapp]` e `[telefone]` pelos dados reais do cliente.

**Resposta a avaliação 5 estrelas**

Variação A, agradecimento direto:
> Fico feliz que deu tudo certo, [nome]! O time da [nome da loja] agradece o comentário. Sempre que precisar de mais alguma coisa pra obra, a gente tá aqui. 🙏

Variação B, reforça o jeito de atender:
> Valeu demais pela avaliação, [nome]. A gente trabalha pra ser aquela loja de bairro que resolve rápido, e ver isso reconhecido vale muito. Volta sempre que precisar.

Variação C, com espaço pra reforço de categoria (só se o cliente já citou o que comprou):
> Muito obrigado pelo carinho, [nome]! Fico contente que [o que o cliente citou] chegou como você esperava. Qualquer coisa pra próxima etapa da obra, é só chamar a gente.

Quando usar a Variação C: só entra menção de produto se o cliente já citou o que comprou na própria avaliação. Nunca inventar o que ele levou. Exemplos de encaixe, puxando sempre a palavra que o cliente usou:
- Cliente escreveu "comprei o tijolo lá, foi rápido" → preencher com "a entrega do tijolo"
- Cliente escreveu "fiz a reforma toda com vocês" → preencher com "o material pra reforma"
- Cliente escreveu "cimento sempre com estoque, nunca falta" → preencher com "o cimento"
- Cliente escreveu "atendimento bom, telha de qualidade" → preencher com "a telha"

Se a avaliação for só "Excelente!" ou 5 estrelas sem nenhum contexto, usa a Variação A ou B. Forçar menção de produto numa avaliação sem contexto é o tipo de resposta genérica que este bloco quer evitar.

**Resposta a avaliação 3-4 estrelas (mista ou neutra)**

Reconhece o ponto levantado sem se justificar demais e sem soar na defensiva. Se houver reclamação específica, convida pro WhatsApp, sem confirmar nem negar política que a loja ainda não fechou.

Variação A, ponto vago (ex: "bom, mas podia ser melhor"):
> Oi, [nome], obrigado por avaliar a gente. Anotado o seu comentário, vamos usar pra melhorar. Se tiver algo específico que não ficou bom, chama no WhatsApp [whatsapp] que a gente escuta com calma.

Variação B, reclamação sobre atendimento ou tempo de espera:
> Oi, [nome], obrigado pelo retorno. Sentimos que essa experiência não ficou como devia nesse ponto. Pode me chamar no WhatsApp [whatsapp] pra eu entender melhor o que aconteceu? Assim a gente consegue resolver direito.

Variação C, reclamação sobre frete, prazo, preço ou forma de pagamento:
> Oi, [nome], obrigado por avaliar. Entendo o que você colocou sobre [frete/prazo/pagamento], e prefiro tratar isso direto com você pra dar uma resposta certa. Chama no WhatsApp [whatsapp] que a gente confirma sua situação com calma.

Por que a Variação C não detalha a política: confirme antes com o cliente se a loja já fechou horário de funcionamento, frete, prazo e forma de pagamento. Confirmar qualquer um desses publicamente pode contradizer a política real quando ela for definida, e vira problema de Código de Defesa do Consumidor se o texto publicado não bater com o que a loja pratica de fato.

**Resposta a avaliação 1-2 estrelas (negativa)**

Nunca contesta publicamente, mesmo quando a avaliação parecer injusta. Reconhece o desconforto do cliente sem admitir culpa que não foi confirmada, e sempre puxa a conversa pro privado.

Variação A, reclamação genérica, sem detalhe do que houve:
> Oi, [nome]. Lamento que a experiência não tenha sido boa. Queria entender melhor o que aconteceu pra resolver. Pode me chamar no WhatsApp [whatsapp] ou ligar [telefone]? Prefiro tratar com você diretamente.

Variação B, reclamação específica (produto, atendimento, entrega):
> Oi, [nome]. Sinto muito que não tenha sido essa a experiência que você esperava com a gente, não é isso que a [nome da loja] busca no dia a dia. Me chama no WhatsApp [whatsapp] com os detalhes do que houve, pra eu olhar o seu caso com atenção e resolver.

Variação C, avaliação parece injusta ou traz um relato que a loja não reconhece:
> Oi, [nome]. Vejo que sua experiência não foi boa, e isso preocupa a gente. Pra entender direito o que aconteceu (esse relato não bate com o que temos registrado aqui), pode me chamar no WhatsApp [whatsapp]? Assim dá pra conversar com calma e ver o que de fato houve.

Por que a Variação C não nega nem confirma: mesmo quando a reclamação parece estranha ou sem fundamento, a resposta pública não entra em debate. Contestar em público vira briga de comentário e afasta quem estiver lendo o perfil depois. A apuração do que aconteceu fica pro privado.

Se a reclamação for sobre frete, prazo, pagamento ou horário: segue a mesma lógica da Variação C do bloco de 3-4 estrelas. Reconhece, não confirma nem nega valor ou prazo, chama pro WhatsApp.

**Boas práticas gerais (valem pros 3 blocos)**

- Responder em poucos dias ajuda a mostrar que alguém acompanha o perfil de verdade.
- Nunca copiar a mesma resposta pra avaliações seguidas. Mesmo com o texto base parecido, troca ao menos uma frase.
- Nunca oferecer desconto, brinde ou reembolso na resposta pública, isso se resolve no privado, depois de entender o caso.

### 2.1.2 — Checklist de otimização de perfil

**1. Dados-base do perfil (revisão mensal)**

Confere se o que está publicado no perfil ainda bate com a realidade da loja. Divergência aqui é o motivo mais comum de perfil perder posição no pacote local, mesmo com nota alta.

Passo a passo:
1. Nome da empresa: igual ao nome real da loja, sem inserir palavra-chave extra (ex: "[nome da loja] Material de Construção Barato" é prática que o Google pune, remove ou suspende o perfil).
2. Endereço e telefone: confere contra o site oficial e o WhatsApp comercial vigente. Se houver mais de uma fonte de telefone (ex: fixo e celular/WhatsApp), decidir com o cliente qual é o principal e qual entra como "telefone adicional".
3. Horário de funcionamento: confere contra o horário real de abertura/fechamento, incluindo sábado e feriado. Horário errado gera avaliação negativa por "loja fechada quando o Google disse aberta".
4. Categoria principal e secundárias: reconfirma se ainda são as mais específicas disponíveis, sem forçar categoria que a loja não atende de verdade (ver seção 2).
5. Link do site: sempre o domínio oficial, nunca link de rede social como site principal.

Quando essa checagem pega algo desatualizado: corrigir direto no painel do Google Business Profile, sem esperar o ciclo mensal seguinte, e registrar a mudança na ficha do cliente.

**2. Categorias (revisão mensal, junto com a seção 1)**

Categoria principal: a que descreve o negócio como um todo, ex: "Loja de materiais de construção". Só existe uma.

Categorias secundárias: usar o diagnóstico de estoque/Curva ABC pra ordenar por peso de faturamento, entrando primeiro a categoria que mais fatura. Limite prático: cadastrar as secundárias que realmente têm produto e giro relevante, não todas as disponíveis na lista do Google.

Por que não forçar categoria de nicho isolado: categoria certa demais (ex: uma subcategoria que representa menos de 2% do faturamento) dilui a relevância de busca da categoria principal em vez de somar. Cadastrar categoria só porque existe é o erro mais comum aqui.

**3. Atributos do perfil (revisão mensal)**

Marcar todos que forem verdade hoje, sem exceção: aceita cartão, tem estacionamento, faz entrega, retirada na loja, acessibilidade (entrada pra cadeira de rodas), Wi-Fi, etc. O Google usa atributo marcado como filtro de busca ("material de construção com entrega perto de mim"), perfil sem atributo marcado simplesmente não aparece nesses filtros mesmo que a loja atenda.

Cuidado: nunca marcar atributo que a loja não sustenta de verdade (ex: "aceita cartão" se só aceita em valor mínimo, ou "estacionamento" se só tem 1 vaga informal). Atributo incorreto vira motivo de avaliação negativa.

**4. Fotos e banco de imagem (revisão mensal, execução contínua)**

1. Fachada: pelo menos 1 foto atual e nítida, é a primeira impressão de quem busca no mapa.
2. Interior/prateleiras: mostra organização e variedade real do estoque.
3. Equipe: humaniza o perfil, especialmente se o dono/gerente aparece (reforça confiança em loja de bairro).
4. Produtos: ver rotina de postagem semanal (2.1.3) pra cadência e critério de prioridade.

Nunca usar: foto de banco de imagem ou material de fabricante genérico no lugar de foto real da loja. O Google prioriza perfil com conteúdo próprio, e cliente percebe foto genérica como sinal de perfil abandonado.

**5. Perguntas e Respostas, Q&A (checagem periódica)**

O Q&A é aberto: qualquer pessoa pergunta e qualquer pessoa responde, inclusive sem ser o dono. Checar a cada revisão mensal (ou sempre que notificado) se apareceu pergunta nova sem resposta oficial, e responder antes que um terceiro responda errado.

Perguntas recorrentes que valem popular preventivamente: forma de pagamento, se atende profissional autônomo (pedreiro, eletricista etc.), raio/política de entrega, como pedir orçamento. Nunca confirmar publicamente política de frete, prazo ou pagamento sem o cliente ter validado que é a regra real e vigente da loja.

**Boas práticas gerais (valem pro checklist inteiro)**

- Cada item corrigido no painel do Google leva de minutos a 1 dia pra refletir na busca pública, não é instantâneo.
- Nunca preencher campo com dado supondo ("provavelmente é isso"). Se o dado não está confirmado, marcar como pendência e perguntar ao cliente, nunca inventar.
- Revisão mensal cobre o perfil inteiro; revisão semanal (ver 2.1.3) cobre só post novo e avaliação pendente. As duas cadências são complementares, não substituem uma à outra.

### 2.1.3 — Rotina de postagem semanal e priorização de fotos

**1. Cadência de postagem**

1 post nativo por semana no perfil (Novidade ou Produto), alternando produto de giro alto com dica prática de obra. O Google prioriza perfil ativo no algoritmo de busca local, perfil parado perde posição mesmo com nota alta.

Tipos de post disponíveis no Google Business Profile:
- **Novidade:** informativo, sem data de validade, uso mais livre.
- **Produto:** ficha de produto com nome, foto, preço opcional, descrição curta. É o tipo que mais aproveita o banco de fotos priorizado na seção 3.
- **Oferta:** exige data de início/fim e condição real e vigente. Só usar se a promoção for política confirmada da loja, nunca com preço ou prazo supostos.
- **Evento:** data específica (ex: aniversário da loja, feira, mutirão).

**2. Repositório de fotos e agendamento manual (operação enxuta)**

Situação real hoje: o Google Business Profile não tem um recurso nativo de "agendar post pra data futura" no fluxo padrão de conta gratuita. Toda publicação de post/foto é imediata no momento em que alguém do time sobe o conteúdo. Por isso, "publicar 8 fotos ao longo de 8 semanas" na prática vira uma fila manual com lembrete, não uma automação de fato, a menos que se pague uma ferramenta terceira (ver seção 4).

Como organizar a fila, dado um repositório de N fotos:
1. Cada foto do repositório recebe um número de ordem de publicação, definido pela priorização da seção 3 (nunca pela ordem em que a foto chegou na pasta).
2. Uma planilha ou lista de controle registra: nº da semana, nome do arquivo, produto/tema, status (pendente / publicada), data de publicação.
3. Toda semana (mesma rotina que já cobre resposta de avaliação), o responsável pega a próxima foto pendente da fila, sobe como post de Produto ou Novidade, marca como publicada.
4. Quando o repositório de N fotos acaba, reponhe com fotos novas seguindo o mesmo critério de prioridade, não deixa a fila zerar sem próximo lote definido.

Por que não construir automação via API agora: o Google restringe o acesso de escrita da Business Profile API (posts, fotos) a parceiros aprovados via processo de solicitação, não é self-service. Pra uma agência do porte da Pillar, atendendo o volume de clientes de hoje, o custo de aprovação, manutenção e risco de a API mudar não se paga frente a uma tarefa de poucos minutos por semana. Reavaliar isso só se o número de clientes que exigem essa rotina crescer o suficiente pra justificar o investimento.

**3. Priorização de fotos e produtos (ligação com Curva ABC)**

Ordem de prioridade pra decidir qual foto/produto entra na fila antes do outro, do mais forte pro mais fraco:

1. Produto que o cliente pediu explicitamente pra divulgar mais (ex: uma linha de alto ticket que o dono quer posicionar, tipo um sistema de mistura de tinta personalizada). Entra na fila mesmo que o giro ainda não seja alto, porque é decisão comercial do cliente, não só dado de estoque. Alternar com os itens abaixo, não ocupar todas as semanas só com esse produto.
2. Produtos Classe A da Curva ABC (maior faturamento), especialmente os de maior giro dentro da Classe A. São o que mais sustenta a loja e o que mais gente já procura por nome.
3. Produtos de maior margem dentro das classes A/B, quando não coincidirem com os do item 2. Puxa produto rentável pra visibilidade, não só volume.
4. Produtos "isca" identificados no diagnóstico de estoque (Pilar 1, atividade 1.3). Item de giro alto e ticket baixo que atrai fluxo de gente pra loja, mesmo sem ser o de maior margem.
5. Institucional/reforço de marca (fachada, equipe, tempo de mercado, bastidor da loja), pra intercalar entre os posts de produto e não deixar o perfil parecer catálogo puro.

Fonte do dado: diagnóstico de estoque e Curva ABC do cliente (`outputs/_diagnosticos/inteligencia-dados/diagnostico-curva-abc.md` e `diagnostico-giro-estoque.md`, ou equivalente). Nunca estimar giro, faturamento ou margem de cabeça, sempre puxar do diagnóstico real mais recente daquele cliente.

Regra de mistura: numa fila de 8 fotos, por exemplo, uma distribuição saudável é algo como 2 produtos pedidos pelo cliente, 3 Classe A/giro alto, 1 de margem, 1 isca, 1 institucional. Ajustar a proporção conforme o que o diagnóstico de estoque daquele cliente específico mostrar como prioridade real.

**4. Se o cliente ou a agência quiser automação de verdade (upsell futuro, não operação padrão)**

Existem ferramentas terceiras de agendamento de redes sociais que já têm parceria aprovada com o Google e permitem programar post/foto do Business Profile com data futura pelo próprio painel delas (categoria de produto: social media schedulers com suporte a Google Business Profile). Antes de recomendar uma ferramenta específica a um cliente, confirmar preço, limites de conta e recursos atuais direto no site do fornecedor, porque essas ferramentas mudam plano e funcionalidade com frequência e não há dado confiável fixo pra citar aqui. Tratar como upsell de operação a ser avaliado caso a caso, não como parte do serviço padrão da Pillar hoje.

**Boas práticas gerais (valem pra rotina inteira)**

- Nunca subir foto de banco de imagem no lugar de foto real do produto/loja, isso já é regra do checklist de otimização (2.1.2).
- Post de Oferta exige condição real e vigente, nunca preço ou prazo suposto.
- Se a fila de fotos ficar sem próximo item definido, isso é sinal de alerta pra pedir mais fotos ao cliente antes que a rotina semanal quebre por falta de material.

## Atividade 2.2 — Anúncios Geolocalizados

Estruturar campanha de tráfego pago com raio de entrega definido, pra investir verba só em quem está perto o suficiente pra virar cliente de verdade, não em quem é só curioso ou está longe demais pra comprar material de construção com frete viável.

**Por que importa pra performance**

Material de construção tem baixo ticket relativo por item e frete caro proporcionalmente. Anúncio sem raio bem definido paga por clique de gente fora da área de entrega lucrativa, inflando CPL sem gerar venda real. Blindar o raio é a diferença entre CPL "bonito no relatório" e CPL que efetivamente vira orçamento fechado.

**Como executar**

1. Definir o raio de entrega lucrativo cruzando custo logístico médio com ticket médio do cliente, não usar raio arbitrário.
2. Montar a segmentação geográfica na plataforma (Meta Ads: raio em km ao redor da loja; Google: raio + extensão de local), seguindo os templates de `_squad/01-gestor-trafego/estruturas-de-campanha.md`.
3. Criar lista de exclusão geográfica pra não desperdiçar impressão fora do raio.
4. Vincular rastreamento (Pixel, GA4, UTMs) antes de subir qualquer campanha, conforme o workflow do `@gestor-trafego`.
5. Revisar o raio a cada ciclo de relatório, expandindo ou reduzindo conforme o CPL real por distância.

**Cadência recomendada:** estrutura definida na criação da campanha, revisão do raio a cada relatório quinzenal ou mensal do `@analista-dados`.

**Indicadores de sucesso**

- CPL e CPA dentro do benchmark do nicho (comparar com `_squad/01-gestor-trafego/benchmarks.md`)
- % do orçamento gasto dentro do raio de entrega lucrativo
- Taxa de conversão de lead pra orçamento fechado, segmentada por distância até a loja

**Squad responsável:** `@gestor-trafego` executa. `@analista-dados` mede o resultado por raio nos relatórios seguintes.

**Operação enxuta:** não expandir o raio pra "pegar mais gente" sem antes checar o CPL por distância no relatório. Raio maior sem dado que sustente é a forma mais comum de estourar orçamento sem aumentar venda.

**Tarefas desta atividade**

1. **Definição do raio de entrega lucrativo**: cruzar custo logístico médio com ticket médio, documentar o racional.
2. **Estrutura de campanha Meta Ads com raio blindado**: segmentação geográfica + exclusão fora do raio.
3. **Estrutura de campanha Google Local/Performance Max com raio**: extensão de local + segmentação geográfica.
4. **Revisão periódica do raio**: ajuste conforme CPL real por distância, alimentado pelo relatório do `@analista-dados`.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

## Atividade 2.3 — Captura de Buscas em Alta

Identificar picos de busca por produtos específicos (sazonais, ligados a clima ou calendário de obra da região) e capturar essa demanda no Google Search antes de o concorrente aparecer primeiro.

**Por que importa pra performance**

Diferente do anúncio de topo de funil, aqui a pessoa já está buscando o produto ativamente, a intenção de compra é alta. Não capturar essa busca é entregar de graça pro concorrente um cliente que já decidiu comprar, só falta decidir onde. Reagir rápido a um pico de busca custa menos e converte mais que competir o ano inteiro pelas mesmas palavras-chave de sempre.

**Como executar**

1. Monitorar tendência de busca (Google Trends, Planejador de Palavras-chave do Google Ads) pra termos relevantes do catálogo do cliente.
2. Cruzar pico de busca com calendário local (época de chuva, período de reforma pós-feriado, sazonalidade regional que o cliente confirmar), sem presumir sazonalidade que o cliente não validou.
3. Montar campanha de Google Search focada na palavra-chave em alta, com lista de negativas pra não gastar com busca fora de intenção de compra.
4. Vincular a LP ou página de categoria certa pro produto em alta, não a home genérica da loja.
5. Acompanhar o desempenho nos primeiros dias, esse tipo de campanha tem janela curta de relevância.

**Cadência recomendada:** monitoramento contínuo (leve, poucos minutos por semana), ativação de campanha pontual assim que um pico relevante for identificado e confirmado com o cliente.

**Indicadores de sucesso**

- CTR e taxa de conversão da campanha de busca em alta comparados à campanha padrão do mesmo cliente
- Velocidade entre identificar o pico e a campanha estar no ar
- CPA da campanha de captura de busca comparado ao benchmark do nicho

**Squad responsável:** `@gestor-trafego` executa, com apoio de `@copywriter` pra headline focada na palavra de busca.

**Operação enxuta:** essa atividade não precisa de monitoramento diário nem ferramenta paga de tendência. Uma checagem semanal de 10 minutos no Google Trends já é suficiente pra pegar a maioria dos picos relevantes com antecedência útil.

**Tarefas desta atividade**

1. **Monitoramento de termos em alta**: checagem periódica de tendência de busca pro catálogo do cliente.
2. **Validação de sazonalidade com o cliente**: nunca presumir calendário sazonal sem confirmação, cada região tem padrão próprio.
3. **Estrutura de campanha de captura**: Google Search focado na palavra em alta, com página de destino certa e lista de negativas.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

---

# Pilar 3: Combo de Produtos

Agentes que mais aplicam: `@copywriter` + `@gestor-trafego`. Candidatos a kit vêm do diagnóstico do `@inteligencia-dados`.

**Problema que resolve:** vender só o "grosso" (com margem baixa) e perder o acessório pro vizinho.

**Resultado que busca:** aumento do ticket médio transformando produtos em soluções completas.

## Atividade 3.1 — Kits Inteligentes por Fase da Obra

Montar kits de produtos organizados pela etapa real da obra (fundação, alvenaria, instalações, acabamento), vendendo solução completa em vez de item avulso.

**Por que importa pra performance**

Quem compra cimento pra fundação também vai precisar de vergalhão, brita e areia na mesma fase. Vender só o item que o cliente pediu, sem oferecer o kit da etapa, é deixar o resto da compra pro concorrente da esquina. Kit bem montado aumenta ticket médio sem precisar de desconto agressivo, porque resolve a dor real (não esquecer nada da etapa) em vez de só empilhar produto.

**Como executar**

1. Partir dos candidatos a kit levantados pelo `@inteligencia-dados` (produto-âncora de giro cruzado com produto de margem complementar da mesma fase de obra).
2. Mapear as fases de obra do nicho MatCon e os produtos típicos de cada uma (fundação, alvenaria, cobertura, instalações, acabamento).
3. `@copywriter` escreve a descrição de oferta do kit: o que é, pra quem, o que entrega, quanto custa, como contratar.
4. `@gestor-trafego` decide se o kit vira campanha própria ou é oferta dentro de uma campanha maior.
5. Testar o kit em escala pequena antes de escalar o investimento, confirmando se o ticket médio realmente sobe.

**Cadência recomendada:** revisão trimestral do catálogo de kits, alinhada com a atualização da curva ABC (Pilar 1). Kit sazonal (ex: campanha de reforma pós-feriado) pode ter ciclo mais curto, conforme calendário comercial.

**Indicadores de sucesso**

- Ticket médio de venda com kit vs venda de item avulso
- Nº de kits ativos com pelo menos 1 campanha ou destaque de ponto de venda rodando
- Taxa de conversão do kit em campanha comparada ao produto vendido isolado

**Squad responsável:** `@inteligencia-dados` (candidatos) → `@copywriter` (oferta) → `@gestor-trafego` (campanha, se aplicável).

**Operação enxuta:** não é preciso lançar dezenas de kits de uma vez. 2 a 3 kits bem montados, testados e comprovados valem mais que um catálogo inteiro de combinações genéricas que ninguém testou. Escalar o que já validou ticket médio maior antes de criar kit novo.

**Tarefas desta atividade**

1. **Mapeamento de fases da obra e produtos típicos**: base pra qualquer kit, feito uma vez e revisado só quando o catálogo do cliente mudar.
2. **Montagem de kit a partir dos candidatos do diagnóstico de estoque**: usar o handoff do Pilar 1, não criar combinação sem base em giro/margem real.
3. **Copy de oferta do kit**: descrição, preço, CTA, seguindo a estrutura "Descrição de oferta" do `@copywriter`.
4. **Teste piloto antes de escalar**: validar ticket médio em pequena escala antes de investir em campanha maior.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

## Atividade 3.2 — Checklist de Venda Adicional

Checklist simples pra o vendedor de balcão ou WhatsApp lembrar de oferecer o acessório ou item complementar toda vez que fecha a venda principal, sem depender da memória ou da vontade do vendedor no dia.

**Por que importa pra performance**

O vendedor sem checklist vende só o que o cliente pediu. Quem comprou tinta esquece do rolo, quem comprou torneira esquece do sifão. Cada um desses itens esquecidos é venda perdida pro vizinho, porque o cliente vai comprar em outro lugar mesmo, só que não na loja que já tinha ele no balcão. O checklist existe pra transformar essa venda esquecida em rotina.

**Como executar**

1. Levantar, por categoria de produto principal, quais itens complementares fazem sentido oferecer junto (ex: quem leva tinta, oferecer rolo, pincel e fita crepe).
2. Montar o checklist em formato curto, o vendedor precisa conseguir usar em segundos, não uma lista longa que ninguém lê no balcão.
3. Treinar o time de venda com o roteiro de abordagem, oferecendo o complemento sem parecer forçado ou insistente.
4. Revisar o checklist com o dono da loja periodicamente, categoria nova ou sazonalidade muda o que faz sentido oferecer.

**Cadência recomendada:** montagem inicial única por categoria principal, revisão a cada 2-3 meses ou quando o mix de produtos mudar.

**Indicadores de sucesso**

- Ticket médio da venda com item adicional vs venda sem oferta
- % de vendas principais em que o vendedor registrou ter oferecido o complemento (se o cliente tiver como medir isso)

**Squad responsável:** `@copywriter` monta o checklist e o roteiro de abordagem.

**Operação enxuta:** o ganho vem de um checklist curto e realmente usado, não de um documento extenso e ignorado. Melhor ter 5 categorias com checklist ativo no balcão do que 20 categorias documentadas e esquecidas na gaveta.

**Tarefas desta atividade**

1. **Checklist de produto complementar por categoria principal**: lista curta e prática pro balcão.
2. **Roteiro de abordagem do vendedor**: como oferecer o complemento sem soar forçado.
3. **Revisão periódica com o dono da loja**: ajuste conforme mudança de mix ou sazonalidade.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

## Atividade 3.3 — Precificação Isca

Definir a estratégia de preço agressivo no produto isca (identificado no Pilar 1) de forma que ele continue puxando cliente pra loja sem virar prejuízo, e que esse fluxo seja usado de propósito pra empurrar o mix de alta margem.

**Por que importa pra performance**

Precificação isca malfeita tem dois riscos opostos: preço tão baixo que vira prejuízo disfarçado de estratégia, ou preço tão "seguro" que perde a força de atrair cliente. O objetivo aqui não é o menor preço possível, é o preço que sustenta a função de isca (trazer gente pra loja) sem comprometer a saúde financeira do item.

**Como executar**

1. Partir da lista de produtos isca identificados pelo `@inteligencia-dados`, com a margem mínima aceitável já calculada.
2. Definir o preço de gancho do item isca, nunca abaixo do custo, mesmo que o concorrente pratique isso.
3. Vincular a comunicação do preço isca (anúncio, vitrine, perfil do Google) à oferta do kit ou do mix de alta margem correspondente, pra capturar o cliente que veio atrás do preço baixo.
4. Acompanhar se a entrada de cliente pelo item isca está de fato convertendo em venda de mix complementar.

**Cadência recomendada:** revisão trimestral, junto com a atualização da curva ABC e da matriz giro x margem (Pilar 1). Revisar antes se o custo do fornecedor mudar de forma relevante.

**Indicadores de sucesso**

- Margem do item isca sempre acima do custo (nunca negativa)
- Ticket médio de quem entra pelo item isca vs quem entra por outro caminho
- Taxa de conversão do item isca em venda de kit ou mix complementar

**Squad responsável:** `@copywriter` e `@gestor-trafego` decidem a comunicação do preço. `@inteligencia-dados` fornece a margem mínima aceitável, não decide preço final sozinho.

**Operação enxuta:** não é necessário reprecificar o catálogo inteiro. O trabalho se concentra nos poucos itens isca já identificados no Pilar 1, revisados com a frequência que o custo do fornecedor exigir, e não mais que isso.

**Tarefas desta atividade**

1. **Definição de margem mínima aceitável**: nunca vender item isca abaixo do custo, mesmo sob pressão de preço do concorrente.
2. **Estratégia de preço de gancho vinculado ao mix**: comunicação do preço isca sempre junto da oferta de kit ou complemento.
3. **Monitoramento de impacto no ticket médio**: confirmar se o fluxo gerado pelo item isca está convertendo em venda de margem maior.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

---

# Pilar 4: Vendedor de Elite

Agente que mais aplica: `@copywriter` (ver "Playbook de vendedor" em `_squad/02-copywriter/SKILL.md`).

**Problema que resolve:** atendimento lento, orçamentos "frios" e falta de acompanhamento (follow-up).

**Resultado que busca:** padronizar o atendimento, acelerar o tempo de resposta e aumentar a taxa de conversão.

## Atividade 4.1 — Resposta Ultrarrápida

Garantir que todo contato de orçamento (WhatsApp, Instagram, formulário, ligação) seja respondido em até 15 minutos, o padrão do Pilar 4.

**Por que importa pra performance**

Quem pede orçamento de material de construção costuma pedir em mais de um lugar ao mesmo tempo. Quem responde primeiro larga na frente, muitas vezes fecha a venda antes do concorrente nem ter respondido. Velocidade de resposta não é gentileza, é vantagem competitiva direta: cada minuto de atraso é uma janela a mais pra outro concorrente fechar o cliente primeiro.

**Como executar**

1. Definir a meta de tempo de resposta (padrão do Pilar 4: até 15 minutos) e deixar claro pra toda a equipe de vendas.
2. Montar o script de resposta ultrarrápida (saudação, confirmação de recebimento, pergunta de qualificação, promessa de prazo de retorno com valor).
3. Organizar rotina de plantão ou revezamento pra garantir cobertura em horário comercial, inclusive fora do horário de pico.
4. Medir o tempo real de resposta (mesmo que manualmente, com registro simples de horário do pedido e horário da resposta).

**Cadência recomendada:** o script é fixo até ser revisado. A medição de tempo de resposta deve ser semanal no início da implementação, depois mensal quando a rotina já estiver consolidada.

**Indicadores de sucesso**

- % de contatos respondidos em até 15 minutos
- Tempo médio de resposta no mês
- Taxa de conversão de orçamento respondido rápido vs respondido tarde (quando o cliente tiver esse dado)

**Squad responsável:** `@copywriter` monta o script (ver "Playbook de vendedor" em `_squad/02-copywriter/SKILL.md`).

**Operação enxuta:** não exige ferramenta cara de CRM pra começar. Um combinado simples de plantão entre os vendedores, com o script pronto, já resolve a maior parte do problema. Ferramenta de automação de resposta só faz sentido depois que o volume de contato justificar o investimento.

**Tarefas desta atividade**

1. **Script de resposta ultrarrápida**: texto pronto pro vendedor usar assim que o orçamento chega, com meta de tempo declarada.
2. **Rotina de plantão/revezamento**: garantir que sempre exista alguém responsável por responder dentro da meta, mesmo em pico de movimento.
3. **Medição de tempo de resposta**: registro simples pra saber se a meta de 15 minutos está sendo cumprida de fato.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

## Atividade 4.2 — Playbook de Fechamento de Orçamento

Roteiro de perguntas de qualificação e respostas prontas pra objeção, pra o vendedor conduzir o orçamento até o fechamento em vez de só informar preço e esperar o cliente decidir sozinho.

**Por que importa pra performance**

Vendedor sem playbook responde preço na lata, sem entender o que o cliente realmente precisa, e perde a chance de mostrar valor antes do número. Isso deixa a decisão do cliente inteiramente baseada em preço, terreno onde a loja quase sempre perde pra quem baixa mais. Qualificar antes de responder e ter resposta pronta pra objeção muda essa dinâmica.

**Como executar**

1. Levantar de 3 a 5 perguntas de qualificação que o vendedor faz antes de fechar o preço (o que precisa, pra quando, quanto já sabe do que quer).
2. Mapear as 2 a 3 objeções mais comuns do nicho (preço, prazo de entrega, comparação com concorrente), sempre confirmadas com o cliente, nunca inventadas.
3. Escrever a resposta pronta pra cada objeção, sem gatilho de urgência falso (nunca "última unidade" ou "preço só até hoje" se não for verdade).
4. Treinar o time de vendas com o roteiro, garantindo que fica natural, não decorado palavra por palavra.

**Cadência recomendada:** montagem inicial única, revisão a cada 2-3 meses ou quando surgir objeção nova recorrente que o playbook ainda não cobre.

**Indicadores de sucesso**

- Taxa de conversão de orçamento em venda fechada
- Nº de objeções cobertas pelo playbook vs objeções novas que aparecem sem resposta pronta

**Squad responsável:** `@copywriter` monta o playbook completo (ver "Playbook de vendedor" em `_squad/02-copywriter/SKILL.md`).

**Operação enxuta:** playbook eficaz cobre as poucas objeções que realmente aparecem no dia a dia da loja, não um catálogo genérico de objeções de manual de vendas. Perguntar ao dono da loja quais objeções ele mais ouve é mais rápido e mais preciso que tentar prever tudo.

**Tarefas desta atividade**

1. **Perguntas de qualificação**: 3 a 5 perguntas antes de informar preço, pra entender a real necessidade do cliente.
2. **Quebra de objeção**: resposta pronta pras objeções mais comuns confirmadas pelo cliente (nunca inventadas).
3. **Gatilho de fechamento sem mentira**: reforço de valor real, nunca urgência ou escassez falsa.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

## Atividade 4.3 — Régua de Follow-up

Sequência sistematizada de contato (D0, D1, D3, D7, D15) pra não deixar o orçamento esfriar sem acompanhamento, com critério claro de quando parar de insistir.

**Por que importa pra performance**

A maior parte do orçamento perdido não é perdida na primeira conversa, é perdida no silêncio depois dela. Cliente que não responde de imediato não significa cliente que não vai comprar, significa cliente que precisa de mais um toque, no momento certo, com o argumento certo. Sem régua, esse follow-up depende da memória do vendedor e quase nunca acontece de forma consistente.

**Como executar**

1. Definir a sequência de dias (padrão sugerido: D0 confirmação, D1 se não respondeu, D3 se ainda não respondeu, D7 reforço de valor, D15 última tentativa antes de arquivar).
2. Escrever 1 mensagem por etapa, cada uma com objetivo único (reaquecer, agregar informação nova, criar urgência real ou encerrar educadamente).
3. Definir com clareza o critério de parar: D15 sem resposta significa arquivar, não continuar follow-up infinito que incomoda o cliente.
4. Acompanhar a taxa de resposta por etapa da régua, pra saber em qual ponto o cliente mais volta a responder.

**Cadência recomendada:** a régua roda por orçamento individual (D0 a D15 de cada lead). A revisão do desempenho da régua como um todo é mensal.

**Indicadores de sucesso**

- Taxa de resposta por etapa da régua (D1, D3, D7, D15)
- % de orçamentos recuperados via follow-up que sem ele teriam sido perdidos
- Tempo médio entre o primeiro contato e o fechamento, quando o follow-up foi decisivo

**Squad responsável:** `@copywriter` monta a régua completa (ver "Playbook de vendedor" em `_squad/02-copywriter/SKILL.md`).

**Operação enxuta:** 5 mensagens bem escritas, reutilizáveis pra qualquer orçamento parado, resolvem isso sem precisar de ferramenta de automação cara. O ganho está em usar a régua de verdade, todo orçamento, sem pular etapa, mais do que na sofisticação da ferramenta.

**Tarefas desta atividade**

1. **Sequência de mensagens D0 a D15**: uma mensagem por etapa, objetivo único cada.
2. **Critério de quando arquivar**: D15 sem resposta encerra o follow-up, sem insistência infinita.
3. **Revisão da taxa de resposta por etapa**: identificar em qual dia o cliente mais volta a responder, pra calibrar a régua.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

---

# Pilar 5: Plano Obra Integral

Agentes que mais aplicam: `@analista-dados` + `@copywriter`.

**Problema que resolve:** o cliente compra o cimento, mas faz o acabamento em outra loja.

**Resultado que busca:** fidelizar o cliente em todas as etapas da obra (LTV máximo).

## Atividade 5.1 — Jornada do Cliente

Rastrear em que fase da obra cada cliente está (fundação, alvenaria, instalações, acabamento), pra saber o que faz sentido oferecer em cada momento em vez de tratar todo cliente com a mesma oferta genérica.

**Por que importa pra performance**

Obra tem sequência previsível. Quem comprou cimento agora vai precisar de fiação elétrica daqui a algumas semanas e de revestimento meses depois. Loja que não registra isso perde o timing certo de oferta e deixa o cliente decidir sozinho onde comprar cada etapa seguinte, quase sempre porque a loja nunca mais apareceu depois da primeira venda. Rastrear a jornada é o que sustenta o Pilar 5 inteiro: sem saber a fase, não tem como prever a próxima oferta.

**Como executar**

1. Registrar a fase de obra declarada ou inferida por cada cliente, em CRM simples ou planilha, o formato importa menos que o hábito de registrar.
2. Mapear o funil de fases típico do nicho MatCon (fundação, alvenaria, cobertura, instalações, acabamento) como referência de sequência.
3. Atualizar o status do cliente sempre que houver contato novo (compra, orçamento, atendimento), não deixar o registro parado no primeiro cadastro.
4. Usar esse registro como insumo pro cronograma de ofertas preditivas (atividade 5.3) e pro dashboard de LTV do `@analista-dados`.

**Cadência recomendada:** atualização contínua, a cada interação com o cliente. Revisão do funil como um todo (quantos clientes em cada fase) mensal.

**Indicadores de sucesso**

- % de clientes com fase de obra registrada e atualizada
- Nº de clientes que avançaram de fase e receberam oferta correspondente
- LTV médio do cliente que teve jornada acompanhada vs cliente sem acompanhamento (quando o dado existir)

**Squad responsável:** `@analista-dados` estrutura o KPI de retenção. `@copywriter` usa a fase pra calibrar a oferta.

**Operação enxuta:** não precisa de CRM sofisticado pra começar. Uma planilha com nome, contato, última compra e fase estimada já é suficiente pra sustentar as ofertas preditivas da próxima atividade. Ferramenta mais robusta só se justifica quando o volume de clientes tornar a planilha difícil de manter.

**Tarefas desta atividade**

1. **Registro de fase da obra por cliente**: CRM ou planilha simples, atualizado a cada interação.
2. **Mapeamento do funil de fases**: fundação, alvenaria, cobertura, instalações, acabamento, como referência pra prever a próxima necessidade.
3. **Atualização periódica do status**: garantir que o registro não fica parado no primeiro cadastro.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

## Atividade 5.2 — Bônus e Cashback de Recompra

Mecanismo simples de bônus ou cashback pra dar ao cliente um motivo concreto de voltar na mesma loja quando chegar a hora de comprar o material fino (acabamento), em vez de fechar em outro lugar só por não ter sido lembrado.

**Por que importa pra performance**

O material fino tem margem melhor que o material bruto da fundação, mas é justamente nessa etapa que o cliente mais migra pra outra loja, seja por acreditar que "loja de material bruto não tem acabamento bom", seja por simplesmente não ter sido chamado de volta. Um mecanismo de recompra dá ao cliente um motivo tangível (não só relacionamento) pra fechar o ciclo inteiro da obra na mesma loja.

**Como executar**

1. Desenhar a regra do bônus ou cashback de forma simples, sem letra miúda que o cliente não entenda de cara (ex: "a cada R$ X em material bruto, R$ Y de crédito pra usar no acabamento").
2. Confirmar com o cliente (dono da loja) se a regra é financeiramente sustentável antes de comunicar publicamente, nunca prometer benefício que a loja não confirmou como real.
3. Comunicar o benefício no ponto de venda e na mensagem de acompanhamento (handoff com o Pilar 4, régua de follow-up).
4. Medir a taxa de recompra de quem usou o benefício vs quem não usou.

**Cadência recomendada:** definição da regra uma vez, com revisão trimestral ou sempre que a margem do material fino mudar.

**Indicadores de sucesso**

- Taxa de recompra de material fino por cliente que já comprou material bruto
- % de clientes que resgatam o bônus/cashback oferecido
- Ticket médio de acabamento entre quem usou o benefício vs quem não usou

**Squad responsável:** `@copywriter` escreve a comunicação do benefício. A regra financeira precisa de confirmação do dono da loja antes de qualquer divulgação.

**Operação enxuta:** um mecanismo simples e sempre cumprido gera mais confiança e recompra do que uma promoção elaborada que o cliente não entende ou desconfia. Começar com uma regra única e fácil de explicar em uma frase, só sofisticar depois que a base estiver validada.

**Tarefas desta atividade**

1. **Desenho do mecanismo de bônus/cashback**: regra simples, validada com o dono da loja antes de qualquer comunicação.
2. **Comunicação do benefício**: mensagem no ponto de venda e no acompanhamento de pós-venda.
3. **Medição de taxa de recompra**: comparar quem usou o benefício com quem não usou.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

## Atividade 5.3 — Cronograma de Ofertas Preditivas

Disparar a oferta certa no momento em que o cliente provavelmente vai precisar dela, antecipando a próxima etapa da obra em vez de esperar ele voltar sozinho.

**Por que importa pra performance**

A obra segue uma sequência previsível de necessidade. Se a loja sabe que um cliente comprou material de fundação há um tempo compatível com o avanço médio de uma obra, ela pode ser a primeira a oferecer o que vem depois, antes do cliente nem começar a procurar em outro lugar. Isso transforma o Pilar 5 de "esperar o cliente lembrar da loja" pra "a loja lembrar o cliente na hora certa".

**Como executar**

1. Partir do registro de jornada do cliente (atividade 5.1) pra saber a fase declarada ou inferida de cada um.
2. Montar um calendário de ofertas por fase esperada da obra, calibrado pelo tempo médio entre etapas que o cliente (dono da loja) confirmar como realista pra região dele.
3. Definir o gatilho de disparo: tempo desde a última compra combinado com a fase declarada, não só uma data fixa genérica.
4. `@copywriter` escreve a mensagem da oferta preditiva, reaproveitando a régua de follow-up do Pilar 4 quando fizer sentido.
5. Acompanhar a taxa de conversão de quem recebeu a oferta preditiva no momento certo vs fora do timing.

**Cadência recomendada:** definição do calendário uma vez, disparo automático ou manual conforme o gatilho de cada cliente. Revisão do calendário a cada 2-3 meses, o tempo médio entre etapas pode variar por região e época do ano.

**Indicadores de sucesso**

- Taxa de conversão da oferta preditiva enviada no timing certo
- Nº de clientes que compraram a etapa seguinte na mesma loja após receber a oferta
- Tempo médio real entre etapas da obra, calibrado com o histórico dos próprios clientes ao longo do tempo

**Squad responsável:** `@analista-dados` acompanha a jornada como KPI. `@copywriter` escreve a sequência de e-mail/WhatsApp da oferta preditiva.

**Operação enxuta:** o calendário não precisa prever tudo com precisão cirúrgica. Acertar a janela aproximada (não o dia exato) já é suficiente pra sair na frente do cliente que ainda nem começou a procurar. Refinar o timing com o tempo, conforme mais dados reais de clientes forem se acumulando.

**Tarefas desta atividade**

1. **Calendário de ofertas por fase esperada da obra**: sequência baseada no tempo médio confirmado com o cliente, não presumido.
2. **Gatilho de disparo**: combinação de tempo desde a última compra com fase declarada.
3. **Acompanhamento de taxa de conversão da oferta preditiva**: medir se o timing está funcionando e recalibrar.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.

## Atividade 5.4 — Parceria com Profissionais

Estruturar uma relação formal com os profissionais de campo (pedreiro, mestre de obra, eletricista, encanador, pintor) e com especificadores (arquiteto, engenheiro, construtora) que compram ou indicam compra pra loja, hoje tratados como cliente avulso mesmo sendo quem mais decide onde a obra do cliente final vai comprar.

**Por que importa pra performance**

Numa loja de MatCon, boa parte do cliente final B2B/residencial não escolhe a loja sozinho, ele compra onde o profissional que está tocando a obra manda comprar. Sem um programa formal, cada profissional decide por conta própria se volta e se indica, e a loja não tem nenhum jeito de reconhecer ou reforçar esse comportamento. Isso é diferente do resto do Pilar 5 (jornada, cashback, ofertas preditivas), que olha pro cliente final: aqui o alvo é o canal de indicação em si.

**Benchmark de mercado (referência, não regra fixa):** grandes players do varejo de MatCon rodam programas nesse formato para profissionais, como o "Com Você"/Clube PRO da Leroy Merlin, o "Juntos Somos +", o Clube Profissional da Maiolini e o Clube do Profissional da Rede Clube da Casa. O padrão comum entre eles: cadastro simples por categoria de ofício, ganho em duas frentes (compra própria + indicação de cliente final), resgate em desconto ou vale-compra, e reconhecimento (capacitação, prioridade de atendimento) além do preço. Nenhum desses programas precisa ser copiado igual, a lógica é o que serve de referência pra uma loja pequena sem CRM.

**Como executar**

1. Segmentar por ofício, não tratar "profissional" como público único: pedreiro/mestre de obra, eletricista, encanador, pintor e especificador têm frequência de compra e categoria de produto relevante diferentes (ver Curva ABC do `@inteligencia-dados` pra saber qual categoria pesa mais pra cada ofício).
2. Desenhar a régua de benefício por segmento (desconto por recompra na categoria do ofício, benefício por indicação de cliente final convertida, prioridade de atendimento/separação de pedido). Nunca comunicar percentual ou condição antes do dono da loja confirmar como política real e sustentável pra margem.
3. Definir um cadastro mínimo (nome, contato, categoria de ofício, histórico de compra/indicação) em planilha simples, sem exigir CRM novo. Cruzar primeiro quem já é comprador recorrente no ERP antes de recrutar do zero.
4. Rodar um piloto com a base já existente (profissionais que já compram na loja) antes de qualquer divulgação paga ou ampla.
5. Divulgar depois do piloto validado: balcão físico, redes sociais/Google Perfil da Empresa, WhatsApp direto pra quem já foi identificado como profissional recorrente.
6. Medir cadastro, recompra, ticket médio do profissional cadastrado vs. geral e indicação convertida.

**Cadência recomendada:** desenho da régua de benefício uma vez, com revisão sempre que a margem por categoria mudar. Cadastro contínuo a cada novo profissional identificado. Revisão do programa como um todo mensal, junto com a revisão de funil da Jornada do Cliente (atividade 5.1).

**Indicadores de sucesso**

- Nº de profissionais cadastrados, por categoria de ofício
- Taxa de recompra do profissional cadastrado vs. não cadastrado
- Ticket médio do profissional cadastrado vs. ticket médio geral da loja
- Nº de indicações rastreadas e taxa de conversão dessas indicações
- Receita atribuída ao canal profissional/indicação como fração do faturamento mensal

**Squad responsável:** `@inteligencia-dados` cruza comprador recorrente por categoria no ERP pra apoiar a segmentação inicial. `@copywriter` escreve o script de abordagem no balcão (handoff com o Pilar 4) e a comunicação do benefício. `@analista-dados` acompanha cadastro, recompra e indicação como KPI. A regra de desconto/benefício sempre precisa de confirmação do dono da loja antes de qualquer comunicação, nunca é decisão do squad sozinho.

**Operação enxuta:** não precisa de cartão físico, aplicativo ou CRM sofisticado pra começar. Uma planilha de cadastro (mesmo formato da Jornada do Cliente) e uma régua de benefício simples, fácil de explicar em uma frase, já sustentam o piloto. Ferramenta mais robusta só se justifica quando o volume de profissionais cadastrados tornar a planilha difícil de manter.

**Tarefas desta atividade**

1. **Segmentação de profissionais por ofício**: mapear categoria de ofício e categoria de produto relevante de cada segmento.
2. **Desenho da régua de benefício por segmento**: desconto por recompra, benefício por indicação, prioridade de atendimento, sempre validado com o dono da loja antes de comunicar.
3. **Cadastro simples em planilha**: nome, contato, ofício, histórico de compra/indicação.
4. **Piloto com base existente**: recrutar primeiro quem já compra na loja, antes de divulgação ampla.
5. **Medição de cadastro, recompra e indicação**: acompanhar os indicadores de sucesso acima.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `_squad/_shared/template-tarefa.md`.
