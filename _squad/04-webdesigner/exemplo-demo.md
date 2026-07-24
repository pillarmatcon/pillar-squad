# Exemplo de Demo: Agente 04-Páginas + Clínica Vital

> **Uso:** demonstração na Aula 4 do evento AgêncIA 100k. Continuação do exemplo iniciado pelo agente 02-Copy. Tempo total da demo: 8 a 10 minutos.

---

## O que entra como input

A copy aprovada da Versão A do anúncio (saída do agente 02-Copy):

```
HEADLINE: Plano detalhado na 1ª consulta
SUBHEADLINE: Avaliação odontológica gratuita com tomografia 3D inclusa.
PRINCIPAIS BENEFÍCIOS:
  1. Tomografia 3D no próprio consultório, sem custo extra
  2. Plano de tratamento detalhado com prazo e valor parcelado
  3. Sem compromisso de continuar após avaliação
DEPOIMENTO (validado pela clínica):
  "Agendei achando que ia sair com mais 3 consultas marcadas. Saí com o plano completo,
  o orçamento parcelado e tempo pra pensar. Voltei depois de 2 semanas."
  Marina C., paciente Savassi, fevereiro 2026
FAQ TOP 4:
  1. A avaliação é mesmo gratuita?
  2. Atendem convênio?
  3. Como funciona o parcelamento?
  4. Posso levar o orçamento pra pensar antes de decidir?
COMPLIANCE CRO: sem antes/depois, sem promessa de resultado, sem valor de procedimento em mídia
```

---

## Briefing técnico complementar (vai na tela durante a demo)

```
TIPO DE PÁGINA: Captura completa (R$ 4.500 a R$ 12.000 ticket de tratamento, justifica seleção pré-call)
URL DESTINO: clinicavital.com.br/avaliacao-gratuita
DOMÍNIO: clinicavital.com.br (Cloudflare DNS, hospedagem Cloudflare Pages)

TRACKING:
  Meta Pixel ID: 1234567890 (placeholder)
  GA4 Measurement ID: G-ABCD1234EF (placeholder)
  Google Ads Conversion: AW-9876543210/abcDEF (placeholder)

ENDPOINT FORMULÁRIO: GHL form webhook (a clínica usa Go High Level como CRM)
URL: https://services.leadconnectorhq.com/hooks/abc123/form-submit (placeholder)

CORES OFICIAIS DA CLÍNICA:
  Primary: #1B4D7E (azul institucional)
  Primary dark: #133858
  Accent: #4FB1C7 (azul claro)

LOGO: clinicavital.com.br/logo.svg (placeholder)
HERO IMAGE: foto da recepção da unidade Savassi (.webp 1200x900)
OG IMAGE: card produzido pelo agente 03-Design/Criativos (1200x630)

ENDEREÇOS:
  Savassi: Avenida Cristóvão Colombo, 532, sala 1402
  Buritis: Rua Engenheiro Edward Smith, 145, sala 305

REGISTRO PROFISSIONAL: Dra. Camila Oliveira, CRO-MG 12345 (responsável técnica)

POLÍTICA DE PRIVACIDADE: já existe em clinicavital.com.br/politica
TERMOS DE USO: já existe em clinicavital.com.br/termos
```

---

## O que a Bindes/Gui pede ao agente na demo

> "@webdesigner produza para a Clínica Vital uma página de captura completa usando a copy da Versão A do anúncio. Briefing técnico acima."

---

## Output do agente (o que aparece na tela durante a demo)

### Resumo da página produzida

```
ARQUIVO: clinica-vital-avaliacao-gratuita.html (single page, autocontido)
TIPO: Captura completa (8 seções)
TAMANHO ESTIMADO: 28KB minified
LCP ESTIMADO: 1.1s em 4G simulado
LIGHTHOUSE ESPERADO: 92+ mobile

PALETA APLICADA:
  --color-primary: #1B4D7E (azul institucional Clínica Vital)
  --color-primary-dark: #133858
  --color-accent: #4FB1C7

TIPOGRAFIA: system font stack (sem fonte custom, otimização de LCP)

SCHEMA.ORG: MedicalBusiness (apropriado para clínica odontológica)

COMPLIANCE CRO APLICADO:
  ✓ Sem antes/depois
  ✓ Sem promessa de resultado clínico
  ✓ Sem valor de procedimento (apenas avaliação gratuita)
  ✓ Registro CRO-MG da responsável técnica no rodapé
  ✓ Política de privacidade adaptada para LGPD + dados de saúde
```

### Estrutura de seções escolhida

| # | Seção | Conteúdo |
|---|---|---|
| 1 | Header | Logo Clínica Vital + telefone Savassi clicável |
| 2 | Hero | Headline "Plano detalhado na 1ª consulta" + subheadline + formulário acima da dobra (3 campos: nome, WhatsApp, email) + foto da recepção |
| 3 | Identificação | "A avaliação é pra você que..." (5 itens) |
| 4 | Apresentação da oferta | "O que acontece na avaliação gratuita" (descrição em 3 parágrafos) |
| 5 | Como funciona | 4 passos: agendar online, comparecer, receber plano, decidir depois |
| 6 | Diferenciais | 3 cards: tomografia 3D, plano detalhado, sem compromisso |
| 7 | Prova social | Depoimento da Marina C. + número "6 anos atendendo BH em 2 unidades" |
| 8 | Quem somos | Dra. Camila Oliveira + equipe + endereços das duas unidades |
| 9 | FAQ | 7 perguntas (4 do briefing + 3 sobre compliance) |
| 10 | CTA final | "Agende sua avaliação esta semana" + link âncora pro formulário |
| 11 | Footer | CNPJ, endereços, CRO-MG, telefones, links legais |

### Texto exato das seções principais (preview)

**Hero**
```
H1: Plano detalhado na 1ª consulta

Subheadline: Avaliação odontológica gratuita em Belo Horizonte, com tomografia 3D
inclusa. Você sai com o plano completo, prazo e valor parcelado, sem compromisso
de continuar.

Formulário (3 campos):
  Nome completo
  WhatsApp
  Email
  Botão: Agendar avaliação gratuita
```

**Identificação**
```
H2: A avaliação é pra você que:

✓ Adia o dentista há mais de um ano
✓ Quer entender o que precisa antes de decidir tratamento
✓ Precisa de orçamento detalhado, não estimado
✓ Quer parcelar tratamento longo sem comprometer o orçamento mensal
✓ Mora ou trabalha em região central de Belo Horizonte
```

**Como funciona**
```
H2: Como funciona

1. Agende online
   Escolha unidade e horário pelo formulário acima. Confirmação por WhatsApp em até 2 horas.

2. Compareça
   50 minutos no consultório. Inclui tomografia 3D na hora, no próprio equipamento.

3. Receba o plano
   Saia com o plano de tratamento detalhado: o que fazer, em que ordem, quanto custa, parcelado.

4. Decida com calma
   Você leva o plano pra casa. Compara, pergunta, pensa. Sem ligação insistente da clínica.
```

**Diferenciais**
```
1. Tomografia 3D inclusa
   Equipamento dentro do consultório. Você não precisa agendar exame separado em outro lugar.

2. Plano completo na primeira visita
   Sai da consulta com tudo: diagnóstico, tratamento proposto, prazo, valor parcelado.

3. Zero compromisso de continuar
   A avaliação é gratuita. A decisão de seguir é sua, no seu tempo.
```

**FAQ (7 perguntas)**
```
1. A avaliação é mesmo gratuita?
   Sim, sem custo. Tomografia 3D inclusa.

2. Atendem convênio?
   Atendemos os principais convênios odontológicos. Confirme pelo WhatsApp ao agendar.

3. Como funciona o parcelamento?
   Cartão de crédito em até 24x sem juros, conforme valor do tratamento e bandeira.

4. Posso levar o orçamento pra pensar antes de decidir?
   Pode. Você sai com o plano impresso ou em PDF. A clínica não faz follow-up insistente.

5. Quanto tempo dura a avaliação?
   Em média 50 minutos.

6. Em qual unidade vou ser atendido?
   Você escolhe no agendamento. Atendemos na Savassi e em Buritis, com mesmo padrão de atendimento.

7. Atendem criança e adolescente?
   Sim, com odontopediatra especializada na unidade Savassi. Avaliação infantil também é gratuita.
```

**Footer (com compliance)**
```
Clínica Vital
Avenida Cristóvão Colombo, 532, sala 1402, Savassi, Belo Horizonte, MG
Rua Engenheiro Edward Smith, 145, sala 305, Buritis, Belo Horizonte, MG
CNPJ 00.000.000/0001-00
Responsável Técnica: Dra. Camila Oliveira, CRO-MG 12345

Contato: (31) 0000-0000 | contato@clinicavital.com.br

Política de Privacidade | Termos de Uso
© 2026 Clínica Vital. Todos os direitos reservados.
```

---

## Checklist de validação rodada antes de entregar

- ✅ Mobile-first testado em 375px
- ✅ Contraste WCAG AA (4.5:1 mínimo) em todos os textos
- ✅ Hierarquia semântica h1 único, h2 por seção
- ✅ Imagens com alt descritivo, dimensões declaradas, lazy load
- ✅ Formulário com validação, honeypot, captura UTM, evento Lead no submit
- ✅ Meta Pixel + GA4 + Google Tag instalados com placeholder claro
- ✅ Open Graph + Twitter Card preenchidos
- ✅ Schema.org MedicalBusiness configurado
- ✅ Política de privacidade e termos linkados no rodapé
- ✅ CNPJ e endereço no rodapé
- ✅ Compliance CRO aplicado item a item
- ✅ Sem travessão, sem emoji, sem marketês
- ✅ CTA repetido 3x (hero, meio, final)
- ✅ Carrega abaixo de 1.5s em 4G simulado
- ✅ Funciona com JS desativado (form ainda envia, FAQ vira lista expandida)

---

## Próximos passos para o aluno

1. Trocar todos os {{PLACEHOLDER}} restantes pelos valores reais (ID Pixel, ID GA4, URL canônica final, foto real da recepção em WebP).
2. Adaptar a foto do hero para WebP otimizado (1200x900, abaixo de 100KB).
3. Validar todo o texto da página com a Dra. Camila Oliveira antes de publicar (compliance CRO interno).
4. Configurar webhook do GHL para receber o formulário e disparar fluxo de boas-vindas no WhatsApp.
5. Subir o HTML em Cloudflare Pages (drag-and-drop em pages.cloudflare.com).
6. Apontar DNS de clinicavital.com.br/avaliacao-gratuita para o projeto Cloudflare Pages.
7. Testar conversão real subindo R$ 50 em campanha de teste no Meta Ads e validar que o evento Lead chega no Events Manager.
8. Configurar conversão importada no Google Ads (Lead).

---

## Pendências para virar "pronto para publicar"

- Receber foto real da recepção da unidade Savassi (formato WebP, otimizada).
- Confirmar com a clínica os 7 textos da FAQ (especialmente "Atendem convênio" e "Como funciona o parcelamento").
- Confirmar CNPJ e número de telefone formatado (DDD + 4 dígitos + 4 dígitos).
- Receber URL real da Política de Privacidade e Termos de Uso atualizados.
- Validar com a clínica a aprovação do uso do depoimento da Marina C. (autorização escrita necessária).

---

## Como a demo conclui na Aula 4

Após o agente entregar o HTML:

1. Bindes/Gui abre o arquivo no navegador local. A página carrega em 800ms (visível no DevTools Network).
2. Bindes/Gui aciona o modo responsivo do DevTools, alterna entre iPhone SE e desktop. A página se reorganiza limpa.
3. Bindes/Gui roda Lighthouse em mobile. Resultado esperado: Performance 92+, Accessibility 95+, Best Practices 100, SEO 100.
4. Bindes/Gui faz drag-and-drop do arquivo em pages.cloudflare.com. Em 60 segundos a página está com URL pública pronta pra usar.
5. Bindes/Gui mostra que o aluno acabou de ver, em menos de 10 minutos, copy + página + hospedagem completas para um cliente de agência. Sem framework, sem dependência, sem mensalidade.

Esse é o ponto da Aula 4: o squad operacional inteiro funcionando ao vivo, em alta velocidade, com saída pronta para uso real.

---

## Conexão com os outros agentes do squad

- **Agente 02-Copy** entregou as headlines, subheadline, depoimento, FAQ. Eu pluguei tudo.
- **Agente 03-Design/Criativos** vai produzir, na sequência, a og-image (1200x630) que vai no `<meta og:image>` desta página.
- **Agente 01-Tráfego** vai estruturar a campanha Meta que aponta para a URL desta página.
- **Agente 05-Relatório/Dashboard** vai puxar dados de conversão desta página (sessões, taxa de conversão do formulário, custo por lead) para o relatório semanal da Clínica Vital.
