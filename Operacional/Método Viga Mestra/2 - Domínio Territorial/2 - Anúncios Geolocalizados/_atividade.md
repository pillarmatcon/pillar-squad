# Atividade: Anúncios Geolocalizados

Estruturar campanha de tráfego pago com raio de entrega definido, pra investir verba só em quem está perto o suficiente pra virar cliente de verdade, não em quem é só curioso ou está longe demais pra comprar material de construção com frete viável.

## Por que importa pra performance

Material de construção tem baixo ticket relativo por item e frete caro proporcionalmente. Anúncio sem raio bem definido paga por clique de gente fora da área de entrega lucrativa, inflando CPL sem gerar venda real. Blindar o raio é a diferença entre CPL "bonito no relatório" e CPL que efetivamente vira orçamento fechado.

## Como executar

1. Definir o raio de entrega lucrativo cruzando custo logístico médio com ticket médio do cliente, não usar raio arbitrário.
2. Montar a segmentação geográfica na plataforma (Meta Ads: raio em km ao redor da loja; Google: raio + extensão de local), seguindo os templates de `Claude/_squad/01-gestor-trafego/estruturas-de-campanha.md`.
3. Criar lista de exclusão geográfica pra não desperdiçar impressão fora do raio.
4. Vincular rastreamento (Pixel, GA4, UTMs) antes de subir qualquer campanha, conforme Passo 6 do workflow do `@gestor-trafego`.
5. Revisar o raio a cada ciclo de relatório, expandindo ou reduzindo conforme o CPL real por distância.

## Cadência recomendada

Estrutura definida na criação da campanha, revisão do raio a cada relatório quinzenal ou mensal do `@analista-dados`.

## Indicadores de sucesso

- CPL e CPA dentro do benchmark do nicho (comparar com `Claude/_squad/01-gestor-trafego/benchmarks.md`)
- % do orçamento gasto dentro do raio de entrega lucrativo
- Taxa de conversão de lead pra orçamento fechado, segmentada por distância até a loja

## Squad responsável

`@gestor-trafego` executa. `@analista-dados` mede o resultado por raio nos relatórios seguintes.

## Operação enxuta

Não expandir o raio pra "pegar mais gente" sem antes checar o CPL por distância no relatório. Raio maior sem dado que sustente é a forma mais comum de estourar orçamento sem aumentar venda.

## Tarefas desta atividade

1. **Definição do raio de entrega lucrativo**: cruzar custo logístico médio com ticket médio, documentar o racional.
2. **Estrutura de campanha Meta Ads com raio blindado**: segmentação geográfica + exclusão fora do raio.
3. **Estrutura de campanha Google Local/Performance Max com raio**: extensão de local + segmentação geográfica.
4. **Revisão periódica do raio**: ajuste conforme CPL real por distância, alimentado pelo relatório do `@analista-dados`.

Nenhuma tarefa tem arquivo `.md` de script pronto ainda. Ao criar um, seguir `Claude/_squad/_shared/template-tarefa.md`.
