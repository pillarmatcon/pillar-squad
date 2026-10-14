# Disparo WhatsApp ConstruMais: lotes de 50 no layout Suri

Base: `Relatório de clientes 01/01/2025 a 06/10/2026` (1.363 linhas). Modelo: planilha Suri (`numero*`, `parametro de template 1*`, `nome`).

## Resultado
- 1.166 contatos aptos, em 24 lotes (23 de 50 e 1 de 16), na ordem da base.
- 197 ficaram de fora dos lotes (aba `fora_dos_lotes` em `14-disparo-whatsapp-controle.xlsx`).

## Regras aplicadas
- Número: WhatsApp primeiro, depois Celular, Telefone2 e Home. Origem: 988 WhatsApp, 178 Celular.
- Formato: `55` + DDD + 9 dígitos. Só celular válido entra.
- Parâmetro 1 = primeiro nome; `nome` = nome completo. Acentos corrompidos na base foram corrigidos.
- Duplicado de número: fica a primeira ocorrência.

## Fora dos lotes
| Motivo | Qtd |
|---|---|
| Provável empresa (LTDA, engenharia, condomínio etc.) | 73 |
| Sem número | 39 |
| Número de 10 dígitos, provavelmente sem o 9 | 36 |
| Número inválido ou fixo | 33 |
| Duplicado | 16 |

## Controle
`14-disparo-whatsapp-controle.xlsx`: aba `lotes` (status por lote), `contatos` e `fora_dos_lotes`.
