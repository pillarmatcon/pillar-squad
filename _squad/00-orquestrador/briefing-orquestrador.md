# Briefing para o Orquestrador

> Preencha e cole direto no chat depois de `@orquestrador`. O orquestrador lê cada campo e sabe exatamente o que passar para cada agente do squad.

---

## Versão completa (3 minutos de preenchimento)

```
@orquestrador

## CLIENTE
Nome:
Segmento:
Cidade / Região:
Instagram:
Site (se tiver):

## OFERTA
O que está sendo promovido:
Condição / preço:
Como funciona (em 1 frase):

## PÚBLICO
Quem é o cliente ideal (idade, perfil, situação):
Principal dor ou problema que a oferta resolve:
Principal objeção que ele tem antes de aceitar:

## OBJETIVO DA CAMPANHA
O que conta como resultado: [ ] Lead  [ ] Agendamento  [ ] Venda  [ ] Visita
Meta numérica: ___ por mês
Destino do lead: [ ] WhatsApp  [ ] Formulário  [ ] Ligação  [ ] Checkout direto

## BUDGET
Investimento mensal em anúncios: R$
Plataforma preferida (se tiver): [ ] Meta Ads  [ ] Google  [ ] Ambas  [ ] Sem preferência

## IDENTIDADE VISUAL
Cor primária (HEX ou descreva):
Cor secundária (HEX ou descreva):
Tom visual: [ ] Profissional/sério  [ ] Próximo/acolhedor  [ ] Moderno/jovem  [ ] Outro:

## TRACKING (preencher se já tiver)
Meta Pixel ID:
GA4 Measurement ID:
Google Ads Conversion ID:

## RESTRIÇÕES E COMPLIANCE
Tem restrição do segmento? (ex: CFM para saúde, OAB para direito):
Algo que NÃO pode aparecer na comunicação:
Tem depoimento de cliente disponível? [ ] Sim - com autorização escrita  [ ] Não
```

---

## Versão express (1 minuto: para demo ou cliente novo)

Quando você não tem todos os dados ainda. O orquestrador preenche as lacunas com as melhores práticas do nicho.

```
@orquestrador

CLIENTE: [nome do negócio]
NICHO: [segmento] - [cidade]
OFERTA: [o que é] + [condição - ex: gratuito, R$ X, 1ª consulta grátis]
OBJETIVO: [lead / agendamento / venda]
BUDGET: R$ [X]/mês
COR PRIMÁRIA: [HEX ou "não sei" - o orquestrador escolhe]
INSTAGRAM: [@handle ou "não tem"]
```

---

## O que cada campo alimenta

| Campo | Vai para |
|---|---|
| Nome, segmento, cidade | Todos os agentes, contexto base |
| Oferta + condição | Agente 02 (copy), Agente 03 (criativo), Agente 04 (LP) |
| Público + dor + objeção | Agente 02 (copy, define o ângulo e o framework) |
| Objetivo + meta numérica | Agente 01 (tráfego, define estrutura de campanha) + Agente 05 (dashboard, define as metas) |
| Destino do lead | Agente 01 (configuração da campanha) + Agente 04 (formulário da LP) |
| Budget + plataforma | Agente 01 (estrutura de campanha + distribuição de budget) |
| Cores + tom visual | Agente 03 (CSS do criativo) + Agente 04 (CSS da LP) |
| Pixel ID + GA4 | Agente 04 (instala o tracking na LP automaticamente) |
| Compliance | Agente 02 (copy) + Agente 03 (criativo), checklist antes da entrega |
| Depoimento disponível | Agente 03 (decide se usa template prova ou oferta) |

---

## Exemplo preenchido: Clínica Vital

```
@orquestrador

## CLIENTE
Nome: Clínica Vital
Segmento: Odontologia
Cidade / Região: Belo Horizonte - Savassi e Lourdes
Instagram: @clinicavital
Site: clinicavital.com.br

## OFERTA
O que está sendo promovido: Avaliação odontológica gratuita
Condição / preço: Gratuita, com tomografia 3D inclusa
Como funciona: Paciente agenda, passa na consulta, recebe o plano de tratamento completo com orçamento parcelado - sem compromisso de continuar

## PÚBLICO
Quem é o cliente ideal: Adultos 28-55 anos, BH, que adiam o dentista por medo ou por não saber o valor
Principal dor: Medo de descobrir um problema caro, medo da dor, vergonha de ter adiado tanto
Principal objeção: "Vou marcar e vão me enrolar para fechar um pacote caro"

## OBJETIVO DA CAMPANHA
O que conta como resultado: [x] Agendamento
Meta numérica: 40 agendamentos por mês por unidade (80 no total)
Destino do lead: [x] Formulário

## BUDGET
Investimento mensal em anúncios: R$ 6.000 (R$ 3.000 por unidade)
Plataforma preferida: [x] Meta Ads (Google Ads a partir do mês 2)

## IDENTIDADE VISUAL
Cor primária: #1B4D7E (azul institucional)
Cor secundária: #4FB1C7 (azul claro)
Tom visual: [x] Profissional/sério + Próximo/acolhedor

## TRACKING
Meta Pixel ID: (a criar - Agente 04 instala o código, cliente cria o pixel no BM)
GA4 Measurement ID: (a criar)
Google Ads Conversion ID: (não tem ainda)

## RESTRIÇÕES E COMPLIANCE
Restrição: CFM/CRO - sem antes/depois, sem promessa de resultado clínico, sem valor de procedimento
Não pode aparecer: comparativo de preço com concorrentes, imagens de procedimentos invasivos
Depoimento disponível: [x] Sim - Marina C., autorização escrita assinada em 28/02/2026
```

---

## Dicas de preenchimento

**Cor primária:** se o cliente não souber o HEX, peça a logo em PNG e diga "a cor principal da sua logo". Se não tiver logo, descreva: "azul escuro", "verde natureza", "laranja vibrante", o orquestrador escolhe o HEX mais adequado para o nicho.

**Pixel e GA4:** se o cliente ainda não tem, deixe em branco. O Agente 04 entrega a LP com os campos de tracking prontos e instrui o cliente a inserir o código depois. Não trava a entrega.

**Objeção principal:** esse campo muda completamente o ângulo da copy. Vale 1 minuto de pesquisa, pergunte ao cliente: "qual é a principal dúvida que o seu cliente tem antes de fechar com você?"

**Meta numérica:** se o cliente não sabe, use o benchmark do nicho como referência (Agente 01 tem os valores). Exemplo para odontologia: 30-50 leads/mês com R$ 3.000 de budget.

**Compliance:** se não souber as restrições do segmento, deixe em branco. O orquestrador aplica automaticamente as restrições padrão do nicho identificado no campo Segmento.
