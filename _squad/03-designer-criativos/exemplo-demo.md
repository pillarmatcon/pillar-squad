# Exemplo de Demo: Agente 03-Design/Criativos + Clínica Vital

> **Uso:** demonstração na Aula 4 do evento AgêncIA 100k. Continuação do exemplo iniciado pelo agente 02-Copy. Tempo total da demo: 4 a 6 minutos.

---

## O que entra como input

A copy aprovada da Versão B do anúncio (saída do agente 02-Copy, 1 composição só, hook + solução + prova + CTA condensados):

```
ESTRUTURA: Criativo de Oferta, 1 peça (Story + Post)
EYEBROW: Pra quem adia
HEADLINE: Adia o dentista? Tem motivo
SUBHEADLINE: A avaliação gratuita resolve os dois motivos: medo do que vai descobrir e medo do valor
SELO DE PROVA: "Saí com o plano completo e tempo pra pensar." Marina C., paciente Savassi
CTA: Agendar avaliação gratuita
SUB DO CTA: Tomografia 3D inclusa

DEPOIMENTO COMPLETO (já validado, usado em peça de prova social separada):
"Agendei achando que ia sair com mais 3 consultas marcadas. Saí com o plano completo,
o orçamento parcelado e tempo pra pensar. Voltei depois de 2 semanas."
Marina C., paciente Savassi, fevereiro 2026

COMPLIANCE CRO: sem antes/depois, sem promessa de resultado, sem valor de procedimento
```

---

## Briefing técnico complementar

```
DESTINO: Anúncio Meta + Stories e feed do Instagram (mesma peça, 2 formatos)
FORMATOS: Story (1080x1920) + Post (1080x1350)

CORES OFICIAIS:
  Primary: #1B4D7E (azul institucional)
  Primary dark: #133858
  Accent: #4FB1C7 (azul claro)

FOTO:
  Status: aguardando foto real da recepção da unidade Savassi (placeholder cinza por enquanto)
  Onde está: clinicavital.com.br/fotos/recepcao-savassi.webp (a ser criada)

LOGO: Clínica Vital (texto, sem ícone gráfico complexo)

TOM VISUAL:
  Profissional, próximo, sem termo técnico
  Tipografia: system font stack (sem fonte custom no v1)
  Sem gradient mesh, sem ícone-emoji
```

---

## O que a Bindes/Gui pede ao agente na demo

> "@designer-criativos produza para a Clínica Vital o criativo de oferta (Story + Post) usando a copy da Versão B. Briefing técnico acima."

---

## Output do agente (o que aparece na tela durante a demo)

### Resumo do criativo produzido

```
ARQUIVO: clinica-vital-oferta.html (single file, Story 1080x1920 + Post 1080x1350)
TIPO: Criativo de Oferta
TEMPLATE-BASE: templates-html/oferta.html

PALETA APLICADA:
  --color-primary: #1B4D7E
  --color-primary-dark: #133858
  --color-accent: #4FB1C7

COMPLIANCE CRO APLICADO:
  ✓ Sem antes/depois
  ✓ Sem promessa de resultado clínico
  ✓ Sem valor de procedimento
  ✓ Tom acolhedor mas firme, sem captação ativa agressiva
```

### Texto exato da peça (igual nos dois formatos)

```
LOGO: Clínica Vital
EYEBROW: Pra quem adia
HEADLINE: Adia o dentista? Tem motivo
SUBHEADLINE: A avaliação gratuita resolve os dois motivos: medo do que vai descobrir e medo do valor
BOTÃO CTA:
  Texto: Agendar avaliação
  Sub: Gratuita, com tomografia 3D
```

No Story, o botão de CTA fica acima da zona de segurança do rodapé (~250px). No Post, fica a 96px da borda inferior. A foto da recepção da unidade Savassi ocupa toda a composição, com um degradê escuro subindo de baixo pra garantir contraste do texto.

---

## Anti-IA checklist rodado antes da entrega

- ✅ Sem fonte arredondada infantil (system font stack profissional)
- ✅ Sem gradient mesh roxo-rosa-azul (paleta sólida da marca)
- ✅ Sem card `rounded-2xl shadow-lg` genérico
- ✅ Sem stock photo genérico (foto real da recepção Savassi a ser inserida)
- ✅ Sem 3 emojis enfileirados (zero emoji)
- ✅ Sem brilho gratuito atrás do texto (degradê é funcional, pra legibilidade)
- ✅ Tipografia tem hierarquia clara (eyebrow / headline / subheadline / botão)
- ✅ Cor tem propósito (azul Clínica Vital no botão de CTA)
- ✅ Foto é real do cliente (aguardando substituir placeholder)
- ✅ Espaço respiratório nos 4 lados (padding 80-96px)
- ✅ 1 ideia central (não enche)
- ✅ CTA claro (botão de cor sólida, texto direto)
- ✅ Identidade do cliente aparece (logo, cor primária, sem ser excessivo)
- ✅ Nada cai nas zonas de segurança do Story (topo/rodapé ~250px)
- ✅ Compliance CRO aplicado item a item

---

## Como a demo conclui na Aula 4

Após o agente entregar o HTML:

1. **Bindes/Gui abre o arquivo no navegador.** O Story (1080x1920) e o Post (1080x1350) aparecem um abaixo do outro, mesma foto e copy, composições diferentes.
2. **Bindes/Gui demonstra a exportação PNG (Chrome DevTools):**
   - F12 abre DevTools
   - Ctrl+Shift+C entra em modo de seleção
   - Clica no Story (`<article id="story">`)
   - Ctrl+Shift+P → "Capture node screenshot"
   - PNG do Story baixado
3. **Bindes/Gui repete pro Post.** Em 30 segundos, 2 PNGs prontos.
4. **Bindes/Gui mostra os 2 PNGs renomeados:** `clinica-vital-story.png`, `clinica-vital-post.png`.
5. **Bindes/Gui mostra que esses PNGs sobem direto:**
   - No Instagram da Clínica Vital (Stories e feed)
   - No Meta Ads como criativo da campanha de oferta
6. **Bindes/Gui comenta:** "Em 6 minutos saímos da copy aprovada para 2 PNGs prontos pra subir, um pra cada formato que a Pillar realmente usa. Sem Photoshop, sem Figma, sem designer terceirizado, sem Canva. O custo dessa entrega é zero. Multiplique por 20 clientes da agência por mês."

---

## Próximos passos para o aluno

1. Substituir o placeholder cinza pela foto real da recepção da unidade Savassi (formato WebP, otimizada).
2. Validar com a Dra. Camila Oliveira (responsável técnica) os textos antes de publicar (compliance CRO interno).
3. Renomear os PNGs com convenção: `cliente-data-formato.png` (ex: `clinicavital-2026-05-04-story.png`, `clinicavital-2026-05-04-post.png`).
4. Subir no Instagram da Clínica Vital (recomendado: terça ou quinta entre 18h e 20h, melhor horário para o público de BH).
5. Configurar como criativo de imagem única no Meta Ads, dentro da campanha de avaliação gratuita (a ser estruturada pelo agente 01-Tráfego), usando o Post para feed e o Story para posicionamentos de Stories/Reels.
6. Acompanhar performance (CTR, CPM por formato) via dashboard do agente 05.
7. Após 7 dias, decidir se renova o criativo ou mantém. Se renovar, voltar ao agente 03 com aprendizado coletado.

---

## Pendências para virar "pronto para publicar"

- Foto real da recepção da unidade Savassi, otimizada em WebP.
- Validação interna CRO com a Dra. Camila Oliveira.
- Confirmação do handle exato do Instagram (`@clinicavital` é confirmado?).
- Review final dos 2 PNGs em mobile (abrir cada PNG em celular, ver se a tipografia ainda lê e se nada caiu na zona de segurança do Story).

---

## Conexão com os outros agentes do squad

- **Agente 02-Copy** entregou o texto da peça. Eu pluguei.
- **Agente 04-Páginas** vai usar uma variação simplificada deste design para gerar a og-image (1200x630) que vai no `<meta og:image>` da LP da Clínica Vital.
- **Agente 01-Tráfego** vai usar os 2 PNGs (Story + Post) como criativo no Meta Ads, dentro da estrutura de campanha que vai ser produzida.
- **Agente 05-Relatório/Dashboard** vai puxar performance dos criativos por formato (Story vs. Post), pra reportar qual funciona melhor pro cliente.

---

## Variações que o aluno pode pedir depois

1. **Criativo de prova social:** depoimento completo da Marina C. em peça própria (Story + Post), usando `templates-html/prova.html`.
2. **Criativo educativo:** insight avulso sobre saúde bucal, publicado em posts separados ao longo da semana, usando `templates-html/educativo.html`.
3. **Versão quadrada (1080x1080):** pontual, pra LinkedIn ou perfil que peça esse formato.
4. **Versão pacote (A/B):** mesma estrutura com hooks diferentes na headline, pra testar qual converte mais.
5. **Carrossel, só se pedido explicitamente:** exceção ao padrão da Pillar. Se o aluno pedir, confirmo estrutura e quantidade de cards antes de desenhar (ver seção "Exceção: carrossel" do SKILL.md).

Qualquer dessas o agente 03 produz adaptando os templates-base.
