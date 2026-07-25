# Regras Globais do Squad: Pillar MatCon

> **Aplicação:** o orquestrador e os 6 agentes especialistas deste squad seguem estas regras sem exceção.

---

## Regras de copy (toda saída textual)

1. **Nunca usar travessão.** Proibido em qualquer texto: em-dash (caractere Unicode U+2014) e en-dash (U+2013) são banidos. Use hífen comum (`-`), dois pontos (`:`), vírgula, ponto final ou reescreva a frase. Para ranges numéricos use hífen ou "às" (ex: "R$ 20-40", "14h às 19h"). Para separação explicativa use hífen com espaços (ex: "Plano de tráfego, estrutura Meta Ads...") ou dois pontos. Regra inegociável que vale para: LP, anúncio, email, mensagem, descrição de criativo, README, SKILL.md, comentário em código, qualquer texto que o agente produza.
2. **Sem emoji em landing page e email transacional.** Permitido em copy de anúncio social, criativo (Story/Post) e mensagem de WhatsApp quando faz sentido para o nicho.
3. **Acentuação correta sempre.** Português brasileiro com todas as marcações gráficas. Nunca "nao", "tambem", "atencao".
4. **Sem marketês.** Banidos: "transforme sua vida", "no cenário atual", "virar o jogo", "alavancar", "potencializar", "trazer resultados", "multiplique seus ganhos", "destrave seu potencial".
5. **Sem números fictícios.** Toda métrica citada vem do briefing ou de dado público verificável. "Mais de 10 mil clientes atendidos" só se for verdade comprovada.
6. **Sem promessa de garantia que não existe.** "Resultado em 7 dias", "ROI garantido", "100% de satisfação" só se for política real do cliente.
6b. **Verbo no imperativo sempre na forma de "você", nunca misturado com "tu".** Todo CTA usa a conjugação do imperativo afirmativo de "você" (que pega emprestada do subjuntivo): "mande", "conheça", "chame", "confira", "agende", "ligue", "peça", "venha". Nunca a forma de "tu" ("manda", "conhece", "chama", "confere", "vem"), mesmo que soe mais falada ou espontânea. É um erro fácil de cometer porque na fala coloquial brasileira é comum misturar o pronome "você" com a conjugação de "tu" ("você manda", "você conhece"), mas em peça publicitária escrita isso lê como erro de português, não como tom casual. Antes de fechar qualquer CTA com dois verbos (ex: "Manda mensagem... e conhece as opções"), confere os dois na mesma forma. Se o cliente tiver voz de marca explicitamente "tu" (nicho regional, briefing confirma), documentar a exceção e manter "tu" em 100% dos verbos da peça, nunca misturado com "você".

## Regras de execução

7. **Sem briefing, não executa.** Se o briefing mínimo (versão curta de `_shared/briefing-template.md`) não estiver completo, o agente para e pede o que falta.
8. **Sem nicho mapeado, não executa.** Se o nicho do briefing não estiver na galeria de `_shared/nichos.md` e o agente não conseguir mapear via 5 perguntas-chave, ele para e pergunta.
9. **Não inventa dado do cliente.** Se faltar informação para uma escolha, o agente devolve a pergunta para o usuário ao invés de chutar.
10. **Não inventa case ou prova social.** Cases citados em copy precisam vir do briefing como fato real do cliente.

## Regras de output

11. **Sempre indicar o que é "v1, sujeito a refinamento"** vs "pronto para publicar". O agente sabe a diferença e sinaliza.
12. **Sempre listar próximos passos** ao fim de qualquer entrega (o que falta para usar de verdade, ou o que validar com o cliente).
13. **Sempre referenciar o briefing usado** no início da entrega (qual versão, quem é o cliente, qual objetivo). Isso evita confusão quando você produz para vários clientes.

## Regras anti-IA (para tudo que vai virar arte/design)

14. **Sem fontes arredondadas e infantis** em peças de marca premium ou técnica. Comic Sans, Quicksand etc. estão fora.
15. **Sem stock photo genérico de pessoa de braço cruzado sorrindo.** Se não tem foto real do cliente, o agente sugere alternativa (ilustração, foto de produto, foto de bastidor).
16. **Sem gradient mesh roxo→rosa→azul gratuito.** Cor tem propósito ou não está no design.
17. **Sem cards `rounded-2xl shadow-lg border` idênticos repetidos.** Variar a hierarquia visual.

## Regras de compliance

18. **Compliance MatCon (CDC padrão).** A Pillar atende hoje só loja de material de construção, nicho sem regulamentação publicitária específica além do Código de Defesa do Consumidor: sem propaganda de preço enganosa, sem prometer prazo de entrega ou disponibilidade de estoque que não existe, garantia de produto sempre conforme a política real do cliente (ver perfil completo em `_shared/nichos.md`). Se a Pillar um dia atender um cliente fora do nicho MatCon (saúde, direito, financeiro etc.): os SKILLs de copywriter, webdesigner, designer-criativos e gestor-trafego trazem seções de referência sobre saúde (CFM/CRO) e direito (OAB), mas são ponto de partida, não mapeamento completo. Validar a regulamentação vigente daquele setor antes de publicar qualquer peça.

## Regra final anti-cara-de-IA no texto (Humanizer)

19. **Revisão Humanizer obrigatória nas 3 saídas textuais.** Antes de entregar copy, criativo ou landing page, o agente roda o protocolo completo em `_shared/humanizer.md` (10 padrões: aberturas travadas, tríades artificiais, conectores marcados, ritmo monótono, fechamentos resumidores, adjetivos genéricos sem prova, vocabulário corporativo vazio, "Você sabe que...", "uma forma de" + verbo, pares redundantes). Se algum padrão falhar, reescreve e roda de novo. A entrega final inclui a linha `✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados` no rodapé.

## Regras de execução em conta real do cliente (CLI write: Nível 3)

20. **Comandos write em conta real são opt-in com confirmação textual explícita.** Aplica quando o `@gestor-trafego` opera no Nível 3 (executar plano via Meta Ads CLI) ou em qualquer cenário futuro de integração de execução. Protocolo inviolável:

   - O agente deve **mostrar EXATAMENTE quais comandos vai rodar** (lista completa, com IDs, valores e flags) antes de executar
   - O agente deve **pedir confirmação textual explícita** do tipo "Responda SIM CONFIRMO para prosseguir", não aceitar "ok", "vai", "manda", "pode"
   - Recursos criados nascem em `status=PAUSED`. Nunca em ACTIVE direto
   - Mudança de budget acima de 50% do valor atual exige confirmação dupla (mostra delta + pede SIM CONFIRMO de novo)
   - Deleção é proibida. Sempre arquivar/pausar em vez de deletar
   - Operações restritas à conta declarada no `CLIENTE.md` do cliente em foco. Trabalhar em outra conta exige novo briefing
   - Todo write é logado em `Operacional/clientes/<nome>/historico/<YYYY-MM-DD>-execucao-<agente>.md` com comandos, IDs criados, status final e próximas ações manuais
   - **Token nunca passa pelo chat.** Token mora em env var permanente do sistema: `~/.zshrc` ou `~/.bashrc` no Mac/Linux, variável de ambiente de usuário no Windows (escopo User, via PowerShell). Se você colar token no chat por engano, o agente para, alerta e instrui a revogar antes de continuar (regra herdada de `_skills/meta-ads-cli-setup/SKILL.md`)

## Regras de atualização de histórico do cliente

21. **Toda entrega que use ou gere dado real do cliente propõe uma atualização do Histórico do CLIENTE.md, e pede confirmação antes de gravar.** Ao final de qualquer execução que leia `Operacional/clientes/<nome>/CLIENTE.md` ou produza um output novo em `Operacional/clientes/<nome>/outputs/`, o agente redige a linha candidata, no formato já usado no arquivo:

   - **YYYY-MM-DD:** [resumo em 1-3 frases do que foi feito, arquivo gerado se houver, e pendência que ficou em aberto]

   e pergunta ao usuário algo como "Posso registrar esta linha no Histórico do CLIENTE.md?" Só grava depois de confirmação explícita. Se o usuário não responder ou pedir para seguir sem isso, o agente segue em frente e não trava a entrega por causa disso.

   Regras da atualização, uma vez confirmada:
   - Sempre acrescenta, nunca reescreve ou apaga linha anterior do Histórico
   - Cita o arquivo de output relevante quando existir (ex: `outputs/2026-07-diagnostico-estoque.md`; para `@inteligencia-dados`, que mantém um único diagnóstico cumulativo por cliente, ex: `outputs/1 - Inteligência de Dados/1 - Curva ABC do Estoque/diagnostico-estoque.md`, seção do período recém adicionado)
   - Se a execução revelou contradição com dado anterior do CLIENTE.md (número que não bate, informação desatualizada), registra a contradição na mesma linha, não corrige o dado antigo silenciosamente
   - Não confundir com `Operacional/clientes/<nome>/historico/`, pasta reservada a log de execução em conta real (Regra 20, Nível 3). O Histórico do CLIENTE.md é o resumo narrativo do relacionamento com o cliente, a pasta historico/ é o log técnico de comandos rodados
   - Se o agente rodou em modo consulta pura, sem gerar output nem mudar entendimento do cliente (ex: só respondeu uma pergunta), não propõe linha nenhuma

## Regra de retroalimentação de performance

22. **Antes de propor ajuste de campanha ou copy nova para cliente ativo, leia o resultado anterior.** Aplica ao `@gestor-trafego` (novo plano ou ajuste de budget/estrutura) e ao `@copywriter` (nova variação de anúncio) sempre que o cliente já tiver pelo menos um RESUMO DE PERFORMANCE salvo em `Operacional/clientes/<nome>/outputs/` (gerado pelo `@analista-dados`, `_squad/05-analista-dados/SKILL.md`).

   - Leia o RESUMO DE PERFORMANCE mais recente e o Histórico do `CLIENTE.md` antes de decidir
   - Se houver ALERTA (métrica fora do benchmark), a proposta nova precisa citar explicitamente qual métrica motivou a mudança
   - Se o cliente não tiver relatório anterior (primeira campanha, primeira copy), a regra não se aplica, segue o fluxo normal
   - Não vale para pedido pontual sem intenção de ajuste (ex: "só me dá 3 headlines novas pra testar", sem relação com resultado passado). Nesse caso, mencionar o resumo é bônus, não obrigação

---

## O que acontece quando uma regra é quebrada

O agente para a execução, sinaliza qual regra foi quebrada e devolve para o usuário. Não publica nada. Não esconde o problema.

Exemplo de mensagem quando o briefing pede algo que viola regra:
> "Pediu garantia de 100% de satisfação na headline. Não tenho confirmação no briefing de que isso é política real do cliente. Vou parar aqui. Confirma se a garantia existe e qual o texto exato dela."
