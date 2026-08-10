# Diagnóstico de Tráfego Pago para Construmais

**Metodologia:** Pilar 2, Domínio Territorial, atividade Anúncios Geolocalizados, Método Viga Mestra
**Como ler este arquivo:** histórico cumulativo, uma rodada por análise, da mais recente (topo) para a mais antiga (final).

---

## Rodada 1, 10/08/2026

**Briefing usado:** CLIENTE.md da Construmais (seção Tracking atualizada nesta mesma data), Histórico do cliente e plano de tráfego anterior (`outputs/9 - Outros/2026-07-plano-trafego-e-copy.md`, v1 de julho/2026)
**Cliente:** Construmais, loja de material de construção, João Pessoa/PB
**Objetivo:** venda, via orçamento gerado por WhatsApp ou formulário
**Budget mensal atual de mídia:** R$ 2.000,00 (pago direto às plataformas pelo cliente, à parte do contrato de R$ 2.200,00/mês com a Pillar)
**Status:** diagnóstico Nível 1 (estrutural) nas duas plataformas, sem dado de campanha real ainda

### Passo 0, verificação de performance anterior

Não existe nenhum RESUMO DE PERFORMANCE do `@analista-dados` salvo em `outputs/` até agora. A Regra 22 (retroalimentação de performance) não se aplica aqui: esta é a primeira leitura desde que Meta e Google Ads entraram formalmente no Tracking do CLIENTE.md. O Histórico do cliente também não registra nenhum ALERTA de métrica de rodada anterior. Este diagnóstico parte do plano de julho/2026 como referência de estrutura pretendida, não de resultado medido.

Uma ressalva importante antes de qualquer recomendação: o formulário de onboarding (21/07/2026) já registrava "já investe em anúncios atualmente: sim" antes do plano de julho existir. Não está confirmado se as campanhas rodando hoje seguem a estrutura proposta em julho (60% Meta, 40% Google) ou se são campanhas anteriores ao contrato com a Pillar. Confirmar isso com o Tony, ou com quem administra a conta no dia a dia, é o primeiro passo antes de qualquer mudança de budget.

**Atualização (10/08/2026):** ressalva resolvida. As campanhas ativas hoje já são geridas pela Pillar, não são remanescentes de antes do contrato. O Alex reativou as campanhas que estavam performando melhor como solução temporária, enquanto o site novo e as novas estratégias (alocação 85% Google / 15% Meta abaixo) ainda estão em configuração.

### Meta Ads

Testei a CLI antes de começar:

```
meta --version
```

Retornou "command not found". A conta já tem Pixel ID (1037733894418340) e Ad Account ID (act_817561456848056) confirmados no Tracking, mas sem a CLI disponível não dá para ler campanha, conjunto ou insight direto da API.

Para um diagnóstico de verdade da Meta, existem 2 caminhos:

```
[1] MODO MANUAL - exportar o CSV do Gerenciador de Anúncios (últimos 30 dias,
    nível de campanha e conjunto) e colar aqui. Eu analiso e devolvo
    recomendação em markdown, você executa os ajustes manualmente.

[2] MODO CLI - setup técnico único (cerca de 1h) que conecta a Ads CLI
    oficial da Meta ao Claude Code. Depois disso eu puxo os dados direto
    da API e ainda posso executar ajustes na conta, sempre com confirmação
    textual sua e tudo nascendo em PAUSED. Passo a passo completo em
    `_squad/01-gestor-trafego/cli-onboarding.md`.
```

Sem CSV nem CLI, o que dá para avaliar hoje é só estrutural.

**Já está pronto:**
- Pixel instalado, ID confirmado
- Ad Account vinculado

**Falta confirmar** (nada disso está documentado em nenhum output ou no CLIENTE.md hoje):
- Se o Pixel está de fato disparando evento de conversão e recebendo dado, não só instalado
- Quais campanhas estão ativas, com que objetivo (Leads, Vendas, Alcance) e budget diário real
- Se a estrutura de julho (Advantage+ Audience 70% mais Retargeting 30%, raio de 15km) foi implementada, ou se a conta roda outra coisa
- CTR de link, CPM, frequência e CPL dos últimos 30 dias
- Se existe audiência de retargeting configurada (visitantes do site mais engajamento Instagram/Facebook)

Com CSV ou CLI liberada, o próximo passo é rodar o funil de `diagnostico-de-conta.md` (impressões, cliques, leads, custo) para achar o gargalo real em vez de estimar.

### Google Ads

Não existe integração automatizada de Google Ads documentada no squad hoje, diferente do Meta, que tem CLI. O diagnóstico aqui fica em Nível 1 (manual), com o que já está confirmado no Tracking.

**Já está pronto:**
- Customer ID confirmado (891-156-9115)
- Acesso da Pillar via MCC confirmado
- Conversion action "Lead WhatsApp 2" (tipo Contato) configurada, ID 867725854, rótulo `0vYmCIKljLMcEJ7k4Z0D`. Isso já resolve o primeiro item da etapa 1 do checklist de `diagnostico-de-conta.md` para Google: a conta rastreia conversão real de contato, não só clique ou visualização de página.

**Falta** (nenhum dado abaixo existe hoje em output do cliente):
- GA4 ainda não existe. O Tracking confirma que só será criado depois do site novo. Sem GA4, não dá para medir comportamento pós-clique na LP, taxa de conversão do funil completo, nem atribuição fora do evento pontual já configurado
- GTM confirmado como decisão, container ID pendente. Sem GTM implementado, qualquer evento novo de conversão além do que já existe exige alteração direta no código do site
- Relatório de campanhas dos últimos 30 dias: nome, status, tipo (Search, Performance Max ou Display), budget diário, gasto, impressões, cliques, CTR, CPC médio, conversões, custo por conversão
- Relatório de termos de pesquisa, para separar busca real que converte de busca que só consome budget
- Quality Score por palavra-chave
- Parcela de impressões, e se a perda é por budget ou por rank
- Se a extensão de localização está vinculada ao perfil do Google Meu Negócio, que já existe e está em otimização pelo Pilar 2, mas sem confirmação de que a extensão está ativa na conta de anúncios
- Se existe lista de negativas e se está atualizada

**Pedido direto para o cliente, ou para quem administra a conta hoje:** exportar do Google Ads, últimos 30 dias, o relatório de campanhas em CSV e o relatório de termos de pesquisa. Com isso já dá para rodar as etapas 2 e 3 do funil de `diagnostico-de-conta.md` para Search.

### Raio de campanha, ponto de atenção estrutural

O Tracking e o briefing de 23/07 fixam o raio de campanha de mídia paga em até 10km da loja, focado no bairro Cristo Redentor, deliberadamente maior que o raio de entrega lucrativo (5km), porque o objetivo declarado é dominância de marca local antes de expandir. Isso é decisão consciente, não erro. Mas o playbook de Anúncios Geolocalizados (`Operacional/Método Viga Mestra/2 - Domínio Territorial/2 - Anúncios Geolocalizados/_atividade.md`) recomenda revisar o raio a cada relatório, comparando CPL por distância até a loja. Sem dado de campanha, seja Meta ou Google, não dá para saber se os 10km estão gerando desperdício de clique fora da área comercialmente viável. Mais um motivo para priorizar a captura de dado real antes do próximo ciclo.

### Alocação de budget: R$ 2.000/mês entre Meta e Google

A regra de ouro de `_squad/01-gestor-trafego/SKILL.md` é direta: budget pequeno funciona melhor concentrado numa plataforma só. O próprio SKILL usa como exemplo um cliente com R$ 1.500/mês inteiro em Meta contra R$ 750 mais R$ 750 dividido. R$ 2.000/mês da Construmais não é tão pequeno assim: passa dos mínimos de dado das duas plataformas (Meta R$ 900/mês, Google Search R$ 600/mês), soma R$ 1.500 e sobra R$ 500 de folga. Só por esse critério, dividir ainda seria defensável.

Só que o cliente já disse onde quer o foco: Google Ads é 80/20 para ele, não Meta. Isso muda a leitura. O plano de julho propôs 60% Meta e 40% Google (R$ 1.200 e R$ 800), invertendo a prioridade que o Tony pede hoje. Se esse plano foi mesmo implementado, a estrutura atual está desalinhada com a prioridade real do cliente. É outro motivo para confirmar primeiro o que está rodando de fato.

Cruzando os dois critérios, regra de ouro mais prioridade declarada, a alocação mais coerente concentra o budget em Google, não divide meio a meio:

**Opção recomendada, concentração em Google Ads:** R$ 2.000/mês (R$ 66/dia) inteiro em Google Search. Fica acima do mínimo de dado (R$ 600/mês) e perto do mínimo para escalar (R$ 1.800/mês), com folga de R$ 200. Meta Ads pausado como campanha paga por enquanto, mantendo só o Pixel ativo e a presença orgânica no Instagram, que já está em construção pelo Pilar 2 como "rosto do Tony". Reavaliar em 60 dias, quando o Google já tiver dado suficiente para saber se sobra espaço de budget para reabrir o Meta.

**Opção alternativa, se o cliente quiser manter presença paga no Meta:** 85% Google (R$ 1.700/mês, R$ 56/dia) e 15% Meta (R$ 300/mês, R$ 10/dia). Atenção: R$ 300/mês fica abaixo do mínimo de R$ 900/mês que o próprio SKILL considera necessário para gerar dado confiável de Meta. Nesse cenário, o Meta não deve ser tratado como teste de prospecção nova, e sim como manutenção de retargeting leve de quem já visitou o site ou engajou no Instagram, sem expectativa de otimização por falta de volume de evento.

Não recomendo manter a divisão 60/40 do plano de julho, nem qualquer divisão próxima de meio a meio: ela não segue a regra de ouro (nenhuma das duas plataformas fica com folga real para escalar) nem a prioridade de 80/20 que o cliente definiu para o Google.

### Recálculo de benchmarks: CPL e CPA

O Tracking do CLIENTE.md já sinalizava que o CPA meta (R$ 60-150) era estimativa provisória, esperando ticket médio real e taxa de fechamento para recalcular. O ticket médio real já existe: até R$ 300, baixo ticket, confirmado no formulário de onboarding. A margem bruta agregada também existe: 39,27%, dado real do Pilar 1 (`diagnostico-estoque.md`). O que ainda falta é a taxa de fechamento, quantos orçamentos viram venda, que o Pilar 4 registra hoje como métrica não monitorada.

Com o que já existe, dá para travar o teto rígido de CPA: o ponto em que o cliente empata a conta numa venda única, sem contar recompra.

```
CPA máximo (breakeven, venda única) = Ticket médio × Margem bruta
CPA máximo = R$ 300 × 0,3927 = R$ 117,81
```

Essa conta já muda algo relevante: o CPA meta anterior tinha o teto (R$ 150) acima do breakeven real (R$ 117,81). Uma venda adquirida a R$ 150 de CPA dá prejuízo na venda única, não lucro. Recomendo mirar abaixo do teto, não nele, porque R$ 117,81 é o ponto de equilíbrio exato, sem sobra para frete, comissão futura ou imprevisto. Uma faixa de CPA meta entre R$ 70 e R$ 110 deixa espaço de lucro real sobre o investimento em mídia.

Para o CPL falta a taxa de fechamento para fechar um número único, mas dá para montar uma faixa por cenário, usando o CPA máximo acima:

```
CPL máximo = CPA máximo × Taxa de fechamento
```

| Taxa de fechamento (orçamento vira venda) | CPL máximo |
|---|---|
| 15% | R$ 17,67 |
| 20% | R$ 23,56 |
| 25% | R$ 29,45 |
| 30% | R$ 35,34 |
| 40% | R$ 47,12 |

O CPL meta atual (R$ 30-80) só se sustenta se a taxa de fechamento estiver acima de 25%. Sem esse dado, o topo da faixa (R$ 80) é otimista demais para o ticket real do negócio. Recomendo revisar a faixa de CPL meta para R$ 18 a R$ 35 até o cliente confirmar a taxa de fechamento real, e só então travar um número único.

Duas ressalvas importantes:

1. Esse teto é de venda única. Parte da base da Construmais é profissional autônomo que compra de forma recorrente (o Pilar 4 registra até 15 orçamentos por dia, sem taxa de conversão nem recorrência medidas). Se um cliente comprar da loja mais de uma vez ao ano, o CPA sustentável real é maior que R$ 117,81, porque o retorno não vem de uma venda só. Isso só entra na conta quando o Pilar 4 tiver dado de recorrência.
2. O ticket de R$ 300 é do consumidor final. Ofertas de ticket mais alto que a Construmais quer priorizar em mídia, como o Sistema Tintométrico, teriam teto de CPA e CPL próprios, mais altos, se e quando virarem campanha segmentada à parte com objetivo e ticket declarados.

### Ações recomendadas, em ordem de prioridade

1. Confirmar com o Tony, ou com quem administra a conta hoje, se as campanhas Meta e Google que estão rodando seguem a estrutura do plano de julho ou são anteriores ao contrato com a Pillar.
2. Pedir a exportação do relatório de campanhas (30 dias) e de termos de pesquisa do Google Ads, ou habilitar a Meta Ads CLI, para sair do diagnóstico estrutural e entrar no diagnóstico de resultado real.
3. Decidir com o cliente entre a opção recomendada (100% Google) e a alternativa (85/15), e ajustar o budget nas duas plataformas conforme a decisão.
4. Revisar a faixa de CPL e CPA meta no CLIENTE.md conforme o recálculo acima.
5. Levar ao Pilar 4 a pendência de medir taxa de fechamento, orçamento para venda. Ela trava o cálculo exato de CPL e CPA enquanto não existir.
6. Confirmar se a extensão de localização do Google Ads está de fato vinculada ao Google Meu Negócio.
7. Confirmar se o Pixel Meta está disparando evento de conversão de verdade, não só instalado na página.

### Compliance

Nicho MatCon, sem regulamentação publicitária específica além do Código de Defesa do Consumidor. Nada neste diagnóstico envolve preço, prazo de entrega ou condição comercial anunciada, então não há item de compliance a verificar nesta rodada.

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados
