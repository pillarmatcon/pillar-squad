# Base de conhecimento do assistente virtual (Suri) da Construmais: README de entrega

**Pedido:** criar vários arquivos `.txt` para alimentar a base de conhecimento do assistente virtual configurado na Suri, a partir do que já está anotado sobre a Construmais (05/11/2026).
**Pasta dos arquivos:** `outputs/11-2026/Arquivos/05-base-conhecimento-suri/`
**Status:** v1, pendente de validação do Tony nos pontos listados abaixo.

## Arquivos para subir na Suri (11 arquivos `.txt`)

| # | Arquivo | O que cobre |
|---|---|---|
| 01 | `01-sobre-a-construmais.txt` | Quem é a loja, o que vende, diferenciais, reputação, redes |
| 02 | `02-contatos-endereco-e-horario.txt` | Endereço, horário, telefones, canais, acessibilidade, fora do horário |
| 03 | `03-departamentos-e-produtos.txt` | Departamentos e itens que mais saem (sem preço e sem garantia de estoque) |
| 04 | `04-tintas-e-sistema-tintometrico.txt` | Tintométrico (até 5.000 cores), como pedir uma cor, limites do assistente |
| 05 | `05-areia-brita-e-cascalho-ensacados.txt` | Ensacados de 20 kg, para quem serve, perguntas de qualificação |
| 06 | `06-o-que-costuma-ir-junto-por-fase-da-obra.txt` | Complementos por fase de obra e lembretes de balcão (sem desconto de kit) |
| 07 | `07-como-pedir-orcamento.txt` | Fluxo de orçamento, dados a coletar, o que o assistente não faz |
| 08 | `08-entrega-frete-e-pagamento.txt` | O que está confirmado, o que não está, respostas-padrão |
| 09 | `09-profissionais-e-empresas.txt` | Profissionais, especificadores, empresas, condomínios, piscineiros |
| 10 | `10-perguntas-frequentes.txt` | 27 perguntas e respostas prontas |
| 11 | `11-tom-de-voz-e-regras-do-assistente.txt` | Tom, limites, quando passar para humano, reclamações |

Este README não deve ser enviado para a Suri (tem conteúdo interno da agência).

## De onde veio cada informação

- Dados da loja, contatos, horário, atributos do Google: `CLIENTE.md` e `_diagnosticos/dominio-territorial/diagnostico-perfil-google-meu-negocio.md`.
- Tintométrico, ensacados, B2B e homologações: ata `historico/2026-07-23-briefing-reuniao-tony.md`.
- Produtos e departamentos: copy das páginas de departamento (`08-2026/Analises/07-copy-paginas-departamentos-construmais.md`, baseada em Curva ABC e estoque) e estratégia de kits (`07-2026/Analises/24-estrategia-kits-e-vendas.md`).
- Tom de voz e cautelas de compliance: `CLIENTE.md` (Tom da marca e Compliance) e script de respostas a avaliações do Google.

## O que ficou de fora de propósito (conteúdo interno, não é para o cliente final)

Faturamento, custos, margens, Curva ABC, estoque parado, achados de qualidade de dado do ERP, suspeita de superfaturamento, valor do contrato com a Pillar, orçamento de mídia, estratégia contra concorrentes (Macol, Lojão da Econômica, Carajás, Araujo, Tupan, Beira Rio), hipóteses do programa de parceria com profissionais (percentuais de benefício, níveis, tabela), desconto de 3% a 5% sugerido para kits, assuntos pessoais do Tony e da equipe, o episódio do Grupo Elizabeth, e a logística do retorno do motorista. Nenhum nome de cliente das avaliações foi usado.

## Pendências para o Tony antes de colocar o assistente no ar

Enquanto estas respostas não existirem, o assistente está instruído a não afirmar nada sobre elas e a passar para um vendedor.

1. **Frete:** regra ou valor de cobrança, e se existe alguma condição de frete grátis (hoje o assistente nunca anuncia).
2. **Prazo de entrega** realista e cumprível.
3. **Formas de pagamento:** cartão, Pix, boleto, parcelamento e desconto à vista. Uma avaliação de 2018 no Google cita "parcelamento", mas isso nunca foi confirmado como política vigente.
4. **Área de entrega:** só temos "raio de 5 km considerado lucrativo". A resposta de Q&A do Google (`24-dominio-territorial-otimizacao-google-meu-negocio.md`) cita Manaíra, Tambaú, Cabo Branco e outros bairros dentro desse raio, o que parece incompatível em distância a partir do Cristo Redentor. Por isso a base não lista bairros atendidos. Vale pedir ao Tony uma lista real.
5. **Troca, devolução e garantia:** regras e prazos.
6. **Nota fiscal e outras perguntas de balcão** que o assistente receberá (nota fiscal com CNPJ, boleto para empresa etc.).
7. **Feriados:** se a loja abre.
8. **Citar nomes das homologações** (Grupo Aena, Sistema Loggi / Grupo MRV, Controll) para clientes: confirmar com o Tony se pode. Ficou no arquivo 09; se não puder, trocar por "fornecedora homologada em grandes empresas".
9. **Número do assistente e transbordo:** hoje o WhatsApp secundário (83) 9 9847-1242 está em teste com agente de IA e o principal (API oficial) é (83) 9 8855-5601. Definir em qual número o assistente vai rodar e como o transbordo para o vendedor funciona na Suri. A base cita os dois números como canais da loja e não diz qual é qual para o assistente.
10. **Texto do template do disparo de WhatsApp** (24 lotes de 14/10/2026): a base orienta o assistente a tratar respostas como contato normal, mas ajustar quando tivermos o texto enviado.
11. **Nome comercial "telha canal tipo russa":** é o nome do cadastro do ERP, ainda a confirmar com o Tony.
12. **Limites da Suri:** não confirmei tamanho máximo por arquivo nem formatos aceitos. Se a plataforma limitar, os arquivos 03 e 10 são os maiores e podem ser divididos.
13. **Lista de produtos:** reflete os itens de maior saída do trimestre abr-jun/2026 e dos kits. Se o Tony quiser, dá para ampliar com mais categorias a partir do ERP.

## Próximos passos

1. Tony responde as pendências 1, 2, 3, 5 e 7 (as que mais aparecem em conversa). Eu atualizo os arquivos 02, 08 e 10 com as respostas reais.
2. Subir os 11 arquivos na Suri e testar com perguntas reais (preço, frete, tinta, ensacado, reclamação).
3. Revisar o que o assistente passou para humano na primeira semana e incluir as perguntas novas no arquivo 10.
