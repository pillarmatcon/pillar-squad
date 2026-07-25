---
name: padroniza-curva-abc
description: >
  Use esta skill sempre que o cliente MatCon enviar um relatório de
  "Curva ABC" em PDF exportado do sistema Pontual Tecnologia (ERP),
  antes de rodar o diagnóstico do Pilar 1 (Inteligência de Dados).
  Trigger para: "curva abc", "relatório de estoque em pdf", "pdf da
  pontual", "exportei do sistema", "planilha de giro de produto",
  ou qualquer PDF anexado que pareça relatório de ERP de loja de
  material de construção. Converte o PDF bruto (que não é lido de
  forma confiável direto pelo modelo, por volume de linhas e
  formatação tabular) em .xlsx padronizado, pronto para o
  `@inteligencia-dados` calcular giro, margem, estoque parado e
  produtos isca. 100% determinístico (regex/posição de coluna +
  pandas), ZERO chamada de IA na conversão em si — o custo de token
  fica restrito a rodar o comando e ler o resumo, não a "ler" o PDF
  inteiro linha por linha.
---

# Padronizador de Curva ABC · Pontual Tecnologia (PDF → XLSX)

Skill de pré-processamento do Pilar 1 (Inteligência de Dados) do Método Viga Mestra. Não faz diagnóstico, não interpreta número, só converte o PDF do ERP num XLSX limpo e padronizado. Quem lê o XLSX e produz o diagnóstico é o `@inteligencia-dados`, seguindo o próprio `SKILL.md` dele.

## Por que existe separada do agente

Ler um PDF de Curva ABC com centenas ou milhares de produtos direto no chat custa muito token e é sujeito a erro de leitura (o modelo pode pular linha, trocar número). Esse script resolve a parte mecânica (extrair texto/posição do PDF, reconhecer os campos, montar a tabela) com regex e biblioteca de PDF, sem IA nenhuma. O agente só entra depois, para interpretar os números já organizados.

## Quando usar

- Cliente ou usuário anexa um PDF cujo título é "Curva ABC" (ou relatório equivalente de giro/estoque) exportado do sistema Pontual Tecnologia.
- Antes de rodar `@inteligencia-dados` com esse tipo de fonte.
- Não usar para relatórios que já vêm em CSV/XLSX do próprio ERP (nesse caso não precisa converter nada, o agente lê direto).

## O script

Arquivo: `pillar_padroniza_curva_abc.py`, nesta mesma pasta.

Detecta sozinho qual dos dois layouts do relatório está recebendo:

- **Formato simples** — 2 linhas por produto, rótulo por extenso.
- **Formato estendido** — inclui colunas de categoria (Grupo, Sub-Grupo, Linha, Família), parseado por posição de coluna.

Tolera um glitch conhecido de extração de PDF (dígito solto que a extração empurra pro meio de um rótulo, ex. "Venda Tota1l"). Se aparecer um layout novo que o script não reconheça, ele não inventa parsing, ele reporta linha de falha.

## Passo a passo (o agente executa via Bash tool, usuário não roda nada)

1. **Confirmar dependências instaladas.** Rodar:
   ```bash
   python -c "import pandas, pdfplumber, openpyxl" 2>&1
   ```
   Se faltar alguma, instalar:
   ```bash
   pip install pandas pdfplumber openpyxl
   ```

2. **Rodar o script apontando pro PDF do cliente e pro destino em `outputs/`:**
   ```bash
   python "Operacional/Método Viga Mestra/1 - Inteligência de Dados/1 - Curva ABC do Estoque/pillar_padroniza_curva_abc.py" "<caminho do PDF recebido>" "Operacional/clientes/<nome-cliente>/outputs/<YYYY-MM>-curva-abc-padronizada.xlsx"
   ```
   Se for prospect (ainda sem `CLIENTE.md`), salvar em `Comercial/propostas/<nome-prospect>/<YYYY-MM>-curva-abc-padronizada.xlsx`.

3. **Ler o resumo impresso no terminal** (produtos padronizados, grupos encontrados, linhas com falha de parsing). Reportar esse resumo ao usuário em 2-3 linhas.

4. **Se "Linhas com falha de parsing" for maior que zero:** mostrar as linhas de falha (o script já imprime até 10) e avisar o usuário que uma pequena fração não foi reconhecida automaticamente, em vez de preencher com valor estimado. Se o padrão da falha for claro (variação do glitch de dígito solto, ou layout novo), pode ajustar o regex/faixas de coluna do script e rodar de novo; não adivinhar valor dentro do XLSX.

5. **Passar a mão para `@inteligencia-dados`**, apontando o XLSX gerado como fonte. Ele segue o próprio workflow a partir daí (giro, margem, estoque parado, produtos isca).

## Regras que seguem valendo

- Sem arquivo de origem real (PDF do cliente), não há o que padronizar. Não gerar XLSX de exemplo nem dado fictício.
- O XLSX gerado é planilha intermediária de trabalho, não é entregável final ao cliente. O entregável é o diagnóstico do `@inteligencia-dados`.
- Se o relatório vier em layout diferente dos dois que o script já reconhece (nova versão do ERP, por exemplo), tratar como falha de parsing total, não tentar forçar um dos dois parsers existentes.

## Custo de token

Rodar este script no ambiente do agente consome token pela chamada de ferramenta em si (não pelo conteúdo do PDF, que o script lê localmente sem IA). Para um PDF pontual isso é desprezível. Para uso recorrente e volumoso, oferecer ao usuário rodar localmente na máquina dele (mesmo comando, fora do Claude Code) como alternativa de custo zero — ver instrução de uso local no topo deste arquivo.
