# Carta de diagnóstico de presença digital (template oficial)

Carta de 5 páginas para abordar dono de loja de material de construção (MatCon) que ainda não é cliente. Mostra, com dado real do Google e do Instagram da própria loja, o que a Pillar enxergou de fora e termina num convite por WhatsApp. Identidade visual sempre da Pillar (`_squad/_shared/identidade-agencia.md`).

Assinam Murillo e Alex, sócios da Pillar. Telefone, @ e QR code da Pillar já vêm fixos.

## Arquivos desta pasta

| Arquivo | Para quê |
|---|---|
| `carta-diagnostico-matcon.html` | O template. É o único arquivo que se edita. |
| `carta-diagnostico-matcon.pdf` | Como o template aparece sem preenchimento (referência). |
| `gerar-pdf.sh` | Gera o PDF a partir do HTML. |
| `assets/logo-pillar.png`, `assets/qr-whatsapp-pillar.png` | Fixos. O QR abre o WhatsApp da Pillar com a mensagem "Olá! Gostaria de conhecer as ideias da Pillar sobre a minha loja." |
| `assets/fachada.jpg`, `mapa-local-falcon.png`, `print-google.jpg`, `print-instagram.jpg` | Imagens de exemplo com aviso "SUBSTITUIR". Troque por imagens reais, mantendo o nome do arquivo. |

## Passo a passo para uma carta nova

1. **Copie a pasta** para `Comercial/propostas/<nome-do-prospect>/` e renomeie o HTML para `carta-diagnostico-AAAA-MM-DD.html`. Não edite o template original.
2. **Rode o Local Falcon:** busca "materiais de construção perto de mim", grade 5 x 5, raio de 1 km, centrada no endereço da loja. Se usar outra grade ou raio, ajuste os números "25 pontos" e "1 km" no texto.
3. **Junte o material** (ver tabela abaixo).
4. **Preencha os campos** em `[colchetes]` com fundo laranja claro. Ao preencher, apague o `<span class="ph">` ao redor, para o destaque sair. Remova o que não se aplicar.
5. **Troque as 4 imagens** em `assets/`.
6. **Gere o PDF** com `./gerar-pdf.sh carta-diagnostico-AAAA-MM-DD.html`. Sem o script: abra o HTML no Chrome, Ctrl+P, destino "Salvar como PDF", margens "Nenhuma", "Gráficos de plano de fundo" ligado.
7. **Confira o checklist** no fim deste arquivo antes de enviar.

## De onde vem cada campo

| Campo | Fonte |
|---|---|
| Nome da loja, bairro, cidade | Perfil do Google da loja |
| Nome do dono | Perguntar ou achar no Instagram. Se forem dois, use "vocês" e "Nome e Nome" no título |
| Ponto forte 1 e 2 (página 1) | Nota e avaliações no Google, % de pontos no top 3 (SoLV), presença no mapa (campo "Found in") |
| N lojas na mesma busca | Local Falcon, "Total Competitors" |
| Frase de apoio (página 1) | Um fato que sustente a reputação. Ex: "A nota 4,9 mostra que quem compra aí gosta." |
| Frase lida no mapa (página 3) | Mapa de calor: onde a loja fica no topo e onde cai (pontos e posições reais) |
| Ranking top 5 (página 3) | Tabela "Business Results Comparison" do Local Falcon: SoLV = Top 3, ATRP = Pos. média |
| Sinal de espaço (página 4) | Algo verificável: volume de avaliações contra a concorrência, nota, avaliação sem resposta, perfil incompleto |
| Fachada | Foto do Google ou da loja. Recorte em faixa de 170 x 62 mm (proporção 2,7 para 1) |
| Print do Google | Ficha da loja no celular. Corte a barra de status e notificações |
| Print do Instagram | Topo do perfil no celular. Corte a barra de status e o espaço em branco do fim |

## Situações comuns e como escrever

- **Loja é a líder do mapa:** celebrar a liderança nas páginas 1 e 2 e mostrar na página 3 onde a vantagem some. Linha 1 do ranking com a classe `own`.
- **Loja não é a líder:** mostrar a distância para a líder em pontos percentuais e, na tabela, descomentar a linha extra com a posição real da loja e tirar `own` da linha 1.
- **Poucas avaliações:** não use a nota como ponto forte nas páginas 1 e 2 (nota 5,0 com 3 avaliações se contradiz com a página 4). Use a liderança no mapa e deixe o volume de avaliações para a página 4.
- **Nota abaixo de concorrentes:** use o volume como ponto forte (páginas 1 e 2) e a nota como sinal de espaço (página 4).
- **Singular e plural:** escreva "1 avaliação", não "1 avaliações".
- **A frase da página 5** ("Nós enxergamos a vitrine: Instagram, anúncios, Google, avaliações") só vale se vocês olharam mesmo o Instagram e os anúncios. Se não olharam, tire o que faltar.

## Regras de escrita (Regras globais do squad)

- Só dado real. Nunca inventar posição, nota, avaliação ou seguidor (regras 5 e 9).
- Sem travessão em nenhum texto. Português com acentuação correta.
- Imperativo sempre na forma de "você" (regra 6b).
- Revise com `_squad/_shared/humanizer.md` antes de enviar.
- O ranking cita lojas reais da região, com dados públicos do Google. Se a carta de uma loja citar outro prospect da Pillar, decida antes se mantém o nome.

## Checklist antes de enviar

- [ ] Nenhum `[colchete]` ou fundo laranja claro sobrou no PDF.
- [ ] Nota e avaliações conferem com o perfil do Google **no dia do envio**.
- [ ] O centro do mapa do Local Falcon é o endereço da loja.
- [ ] A data da varredura aparece e não está velha demais.
- [ ] QR code testado com a câmera do celular: abre o WhatsApp da Pillar com a mensagem pronta.
- [ ] Prints sem barra de status e sem notificação pessoal.
- [ ] A carta tem 5 páginas, sem texto sobre o rodapé.
- [ ] Definido como a carta chega ao dono (WhatsApp, e-mail ou impressa).

## Histórico

- 2026-10-13: primeiras três cartas (Lojão da Construção, Achei Materiais para Construções, Soberana Materiais de Construção) em `Comercial/propostas/`. Este template consolida o formato final aprovado nelas.
