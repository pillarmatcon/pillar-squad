# Disparo WhatsApp ConstruMais: lotes de 50 no layout Suri

Base: `Relatório de clientes 01/01/2025 a 06/10/2026` (1.363 linhas). Modelo: planilha Suri (`numero*`, `parametro de template 1*`, `nome`).

## Resultado
- 1.184 contatos aptos, em 24 lotes (23 de 50 e 1 de 34), na ordem da base.
- 179 ficaram de fora dos lotes (aba `fora_dos_lotes` em `14-disparo-whatsapp-controle.xlsx`).

## Regras aplicadas
- Número: WhatsApp primeiro, depois Celular, Telefone2 e Home. Origem: 987 WhatsApp, 176 Celular, 21 com o 9 incluído (13 WhatsApp, 8 Home).
- Números de 10 dígitos (DDD + 8 dígitos começando em 6 a 9) receberam o 9 depois do DDD, por decisão do usuário.
- Empresas ficam fora dos lotes, por decisão do usuário.
- Formato: `55` + DDD + 9 dígitos. Só celular válido entra.
- Parâmetro 1 = primeiro nome; `nome` = nome completo. Acentos corrompidos na base foram corrigidos.
- Duplicado de número: fica a primeira ocorrência.

## Fora dos lotes
| Motivo | Qtd |
|---|---|
| Provável empresa (LTDA, engenharia, condomínio etc.) | 88 |
| Sem número | 39 |
| Número inválido ou fixo | 33 |
| Duplicado | 19 |

## Controle
`14-disparo-whatsapp-controle.xlsx`: aba `lotes` (status por lote), `contatos` e `fora_dos_lotes`.
