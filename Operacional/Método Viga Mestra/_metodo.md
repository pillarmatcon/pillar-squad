# Método Viga Mestra

Biblioteca de playbooks genéricos da metodologia própria da Pillar, organizada em três níveis:

```
Pilar > Atividade > Tarefa
```

- **Pilar**: um dos 5 pilares do método (pasta numerada, ex: `2 - Domínio Territorial`). Descrito em `_pilar.md` dentro da pasta.
- **Atividade**: uma frente de execução dentro do pilar (pasta numerada dentro do pilar, ex: `1 - Google Meu Negócio`). Descrita em `_atividade.md` dentro da pasta.
- **Tarefa**: um arquivo `.md` dentro da atividade, com o passo a passo executável (ex: `script-respostas-avaliacoes-google.md`). Formato definido em `Claude/_squad/_shared/template-tarefa.md`.

## Regra: aqui é template, não execução

Todo conteúdo dentro de `Operacional/Método Viga Mestra/` é genérico, com `[placeholders]` no lugar de qualquer dado de cliente. Isso permite seguir a tarefa, executar, delegar pra um colaborador ou pedir pro squad rodar, pra qualquer cliente MatCon.

A versão real, preenchida com o dado do cliente (nome da loja, WhatsApp, telefone, etc), fica em `Operacional/clientes/<nome>/outputs/`, nunca aqui.

## Onde está o "porquê" de cada pilar

O racional completo dos 5 pilares (problema que resolve, resultado que busca, qual agente do squad mais aplica) está em `Claude/_squad/_shared/metodo-viga-mestra.md`. Os `_pilar.md` desta pasta são um resumo local, pra bater o olho sem sair da pasta; a fonte da verdade continua sendo `Claude/_squad/_shared/metodo-viga-mestra.md`.

## Os 5 pilares

1. [Inteligência de Dados](1%20-%20Intelig%C3%AAncia%20de%20Dados/_pilar.md)
2. [Domínio Territorial](2%20-%20Dom%C3%ADnio%20Territorial/_pilar.md)
3. [Combo de Produtos](3%20-%20Combo%20de%20Produtos/_pilar.md)
4. [Vendedor de Elite](4%20-%20Vendedor%20de%20Elite/_pilar.md)
5. [Plano Obra Integral](5%20-%20Plano%20Obra%20Integral/_pilar.md)

## Quando uma atividade não tem nenhuma tarefa ainda

O `_atividade.md` diz isso explicitamente. Não existe tarefa "fantasma" ali só pra preencher espaço. Adicione a tarefa quando o processo for realmente definido, seguindo `Claude/_squad/_shared/template-tarefa.md`.
