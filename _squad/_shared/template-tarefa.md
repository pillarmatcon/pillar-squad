# Template de Tarefa (Método Viga Mestra)

> **Quando usar:** toda vez que uma nova tarefa for adicionada dentro de uma atividade em `Operacional/Método Viga Mestra/`. Modelo extraído de `Operacional/Método Viga Mestra/2 - Domínio Territorial/1 - Google Meu Negócio/script-respostas-avaliacoes-google.md`, a primeira tarefa documentada nesse formato.
> **Regra:** tarefa dentro de `Operacional/Método Viga Mestra/` é sempre genérica, com `[placeholders]` no lugar de qualquer dado de cliente (nome da loja, WhatsApp, telefone, nome de vendedor). A versão real e preenchida para um cliente específico vai em `Operacional/clientes/<nome>/outputs/`, nunca aqui.

---

## Estrutura sugerida

```markdown
## 1. [Nome do cenário ou passo 1]

[Contexto de quando esse cenário se aplica]

**Variação A, [critério que diferencia essa variação]**
> [Texto ou instrução, com [placeholders] no lugar de dado real]

**Variação B, [critério]**
> [Texto]

**Quando usar cada variação:** [regra de decisão, incluindo casos em que NÃO usar]

---

## 2. [Próximo cenário ou passo]

[...]

---

## Boas práticas gerais (valem pra todos os blocos)

- [Regra prática 1]
- [Regra prática 2]
- [O que nunca fazer]
```

## Princípios ao escrever uma tarefa

1. **Passo a passo executável.** Quem ler (usuário, colaborador ou agente) precisa conseguir seguir sem perguntar nada a mais.
2. **Variações, não uma resposta única.** Evita robotização e cobre os cenários reais que a tarefa encontra.
3. **Explicar o "quando usar" de cada variação**, não só listar. É o que faz a tarefa ser seguida certo em vez de aplicada por acaso.
4. **Justificar a decisão não óbvia.** Se uma variação evita dizer algo (ex: não confirmar política que a loja não fechou), explicar o motivo, não só a instrução.
5. **Placeholders sempre entre colchetes** (`[nome]`, `[whatsapp]`, `[nome da loja]`), nunca dado real de cliente.
6. **Fechar com boas práticas gerais**, se houver regras que valem pra tarefa inteira e não só pra um cenário.

## Nomeação do arquivo

`nome-descritivo-da-tarefa.md`, minúsculo, com hífen, sem prefixo de data (data é só para outputs reais em `Operacional/clientes/<nome>/outputs/`).
