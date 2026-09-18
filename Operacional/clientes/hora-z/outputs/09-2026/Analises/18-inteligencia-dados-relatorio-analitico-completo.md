![Pillar](../../../../../../_squad/_shared/marca-pillar/logo-pillar.png)

# Relatório Analítico Completo — Diagnóstico Pilar 1, Hora Z
**Marketing com Resultado Concreto**
Pillar · Método Viga Mestra, Pilar 1 (Inteligência de Dados)

---

> Versão expandida do relatório de 18/09/2026: em vez de só exemplos, traz a lista completa de produtos de cada classificação (quais são os 85 SKUs Estrela, os 78 Isca, os 173 da Curva ABC classe A, os 148 parados, os 49 com outlier de cadastro, os 86 com mais de um fornecedor), extraída direto das planilhas de apoio, sem curadoria manual. Fonte: `outputs/_diagnosticos/inteligencia-dados/diagnostico-curva-abc.md` e `diagnostico-giro-estoque.md`, e as planilhas `15-inteligencia-dados-curva-abc-padronizada_acumulado-ate-2026-09-15.xlsx` e `15-inteligencia-dados-estoque-giro-margem_snapshot-2026-09-15.xlsx`, ambas em `outputs/09-2026/Arquivos/`.
>
> **Nota sobre o total de estoque:** o valor total em estoque a custo deste diagnóstico é R$ 40.661,03 (443 SKUs únicos, uma linha por produto). Se você somar custo × estoque direto no relatório bruto do cliente ("Produtos por Fornecedor", 544 linhas), sem remover as 101 linhas duplicadas de produtos comprados de mais de um fornecedor, chega em R$ 62.301,85 — um valor inflado, porque o mesmo estoque físico é contado mais de uma vez (a mesma quantidade em unidades se repete em cada linha de fornecedor do mesmo produto). R$ 40.661,03 é o número correto, uma linha por produto.

## Sumário

1. [Curva ABC oficial por faturamento — Classe A completa (173 SKUs)](#1-curva-abc-oficial-por-faturamento)
2. [Categorias por faturamento — top 15 por categoria](#2-categorias-por-faturamento)
3. [Matriz Giro x Margem — os 295 SKUs completos, por quadrante](#3-matriz-giro-x-margem-completa)
4. [Estoque parado — os 148 SKUs completos](#4-estoque-parado-completo)
5. [Top produtos em estoque por valor — top 20 bruto e top 15 sem outliers](#5-top-produtos-em-estoque-por-valor)
6. [Maiores quantidades em estoque — top 20](#6-maiores-quantidades-em-estoque)
7. [Auditoria de cadastro — os 49 SKUs com custo fora do padrão](#7-auditoria-de-cadastro-completa)
8. [Sensibilidade de custo por múltiplos fornecedores — os 86 SKUs](#8-sensibilidade-de-custo-por-fornecedor)
9. [Outliers excluídos, explicitamente, e o porquê](#9-outliers-excluídos)

---
## 1. Curva ABC oficial por faturamento

Classe A completa: **173 SKUs**, responsáveis por 79,9% do faturamento sem outliers (R$ 291.831,91). Classe B (369 SKUs, 15,0% do faturamento) e Classe C (643 SKUs, 5,0%) não estão listadas produto a produto aqui pelo volume (mais de 1.000 SKUs de cauda longa somados); lista completa das três classes na aba "Curva ABC por faturamento" da planilha.

| # | Código | Produto | Categoria | Faturamento | Qtd. vendida | Classe (qtd.) | Margem |
|---|---|---|---|---|---|---|---|
| 1 | PRD00045 | Cimento Supremo 50Kg | Básico | R$ 27.868,00 | 704 | B | 16,8% |
| 2 | 21070 | Vermelho Seguranca 5Ra/14 Epoxi Piso  2.88L Farben | Acabamento | R$ 8.638,46 | 16 | C | 0,3% |
| 3 | 21445 | Epoxi Piso Branco Farben 2,8L | Acabamento | R$ 7.873,06 | 24 | C | sem dado |
| 4 | 22446 | Argamassa Superkola 3Mais Cinza 20Kg | Básico | R$ 7.166,12 | 290 | B | 37,9% |
| 5 | PRD00040 | Ar Condicionado 9.000 Btu Inverter Frio - Tcl | Não classificado | R$ 6.600,00 | 3 | C | sem dado |
| 6 | 22114 | Tijolo 6 Furos 09 X 14 X 24 Cer. Lorenzetti | Básico | R$ 6.452,00 | 6.860 | A | 36,8% |
| 7 | 21437 | Catalisador Epoxi P/Piso  0.72L Farben | Acabamento | R$ 5.495,40 | 51 | C | sem dado |
| 8 | 20861 | Areia Fina Cinza 1 M³ | Básico | R$ 5.440,07 | 25,5 | C | sem dado |
| 9 | 21356 | Bloco Concreto Normal  14 X 19 X 39 | Básico | R$ 5.248,80 | 1.470 | B | sem dado |
| 10 | 20492 | Fundo Preparador Parede 18L Alessi | Pintura | R$ 4.312,00 | 16 | C | sem dado |
| 11 | 20250 | Tijolo 6 Furos 09 X 14 X 29 Cer. Lorenzetti | Básico | R$ 4.229,00 | 4.170 | B | 34,1% |
| 12 | PRD00079 | Areia Com Brita 00 - 1M³ | Básico | R$ 3.914,77 | 20 | C | sem dado |
| 13 | 20252 | Refletor Slim Led 200 120 6500K Autovolt - Aluminio Unico | Elétrica | R$ 3.747,00 | 30 | C | sem dado |
| 14 | 101010 | Ferro 3/8 (12 Metros) 10Mm | Básico | R$ 3.449,59 | 61 | B | 28,5% |
| 15 | 20912 | Ferro 5/16 (12 Metros) 8Mm | Básico | R$ 3.205,40 | 86 | B | 27,0% |
| 16 | 20957 | Po De Pedra Ou Brita 1M³ | Básico | R$ 3.121,24 | 10,5 | C | sem dado |
| 17 | 110203 | Perfume Boticário | Bazar/diversos | R$ 3.075,42 | 1 | C | sem dado |
| 18 | 12010 | Argamassa Massa Reboco Cinza 20Kg | Básico | R$ 3.061,60 | 138 | B | 56,5% |
| 19 | 22445 | Argamassa Extrakolla 2 Cinza 20Kg | Básico | R$ 3.034,50 | 143 | B | 42,2% |
| 20 | 20756 | Laje Isopor | Básico | R$ 2.944,73 | 48,7 | C | sem dado |
| 21 | PRD00129 | Areia Com Brita 01 1M³ | Básico | R$ 2.676,85 | 15 | C | sem dado |
| 22 | 20758 | Cimento Supremo Cpiv | Básico | R$ 2.345,30 | 60 | B | sem dado |
| 23 | 20714 | Bica Corrida 1M³ | Básico | R$ 2.310,13 | 15,5 | C | sem dado |
| 24 | 22837 | Porta Interna Lisa | Acabamento | R$ 2.308,60 | 7 | C | sem dado |
| 25 | 21452 | Tubo Esgoto 100Mm - 6M | Hidráulica | R$ 2.260,40 | 26 | C | 33,5% |
| 26 | PRD00137 | Cabo De Aco 6,35Mm 1/4 | Básico | R$ 2.190,00 | 200 | B | sem dado |
| 27 | 21383 | Tabua Caixaria 25Cm X 2,5Cm X  3,00 M | Básico | R$ 2.115,00 | 66 | B | sem dado |
| 28 | 20944 | Taxa De Entrega Itoupava Central Bongo | Serviço (entrega) | R$ 2.083,00 | 107 | B | sem dado |
| 29 | 20639 | Telha Eternit 2,44 X 0,50 X 4Mm | Básico | R$ 2.070,02 | 94 | B | sem dado |
| 30 | 009273 | Pf Sext 1/2X5 | Básico | R$ 1.971,00 | 300 | B | sem dado |
| 31 | 20796 | Areia Media 1M³ | Básico | R$ 1.925,12 | 10 | C | sem dado |
| 32 | 22758 | Tinta Acril. Fosco Economico 15Lt Eucatrex | Pintura | R$ 1.800,00 | 20 | C | sem dado |
| 33 | 21072 | Diluente Epoxi 8500 5L Farben | Não classificado | R$ 1.766,00 | 4 | C | sem dado |
| 34 | 20556 | Brita 01 1M³ | Básico | R$ 1.748,34 | 10 | C | sem dado |
| 35 | 21384 | Bloco Estrutural 14 X 19 X 39 | Básico | R$ 1.737,00 | 415 | B | sem dado |
| 36 | 21698 | Tinta Amarelo Seguranca Piso | Pintura | R$ 1.614,00 | 6 | C | sem dado |
| 37 | 21627 | Amarelo Seguranca 5Ra/14 Epoxi Piso  2.88L Farben | Acabamento | R$ 1.587,34 | 4 | C | sem dado |
| 38 | 20612 | Tela Leve 2X3 Bitola 20X20 Malha Pop | Básico | R$ 1.494,27 | 33 | C | sem dado |
| 39 | 21603 | Telha Cerâmica Esmaltada | Acabamento | R$ 1.425,00 | 150 | B | sem dado |
| 40 | 21435 | Fita Crepe Amarela 18X40 Automotiva | Pintura | R$ 1.292,50 | 167 | B | 38,7% |
| 41 | 22686 | Carrinho De Carga 45 L Minasul | Ferramentas | R$ 1.205,06 | 7 | C | 38,1% |
| 42 | 20701 | Tinta Acril. Preto Semi Brilho | Pintura | R$ 1.178,90 | 4 | C | sem dado |
| 43 | 21596 | Lixadeira De Parede 220V Vonder | Ferramentas | R$ 1.153,12 | 1 | C | sem dado |
| 44 | 20856 | Brita 00 1M³ | Básico | R$ 1.126,99 | 7,5 | C | sem dado |
| 45 | PRD00135 | Lukspiso Cinza Chumbo 3,6L | Pintura | R$ 1.111,48 | 7 | C | sem dado |
| 46 | PRD00122 | Balcao De Cozinha Com Três Portas Mdf | Bazar/diversos | R$ 1.100,00 | 1 | C | sem dado |
| 47 | 4436 | Cabo De Aco Plastificado 3/32" 2,40Mm | Básico | R$ 1.040,00 | 400 | B | sem dado |
| 48 | 21350 | Aco Ca 50 3/8" 10Mm(7,40Kg) 12M | Básico | R$ 1.038,00 | 20 | C | sem dado |
| 49 | 109461 | Tabua Caixaria 30Cm X 2,5Cm X 3M | Básico | R$ 1.025,64 | 17 | C | sem dado |
| 50 | 21266 | Bloco Concreto Fechamento 14X19X39 | Básico | R$ 1.018,50 | 210 | B | sem dado |
| 51 | 123 | Celular Marca Poco | Bazar/diversos | R$ 1.000,00 | 1 | C | sem dado |
| 52 | 20984 | Refletor Tr Led 200 - 16000 Lúmens - Autovolt 6500K Luz Fria Taschibra | Elétrica | R$ 984,00 | 6 | C | sem dado |
| 53 | 22023 | Torneira Prima Eletronica 5500W 220V Black Zagonel | Hidráulica | R$ 983,50 | 4 | C | sem dado |
| 54 | 003127 | Tubo Concreto 30X100 | Hidráulica | R$ 980,00 | 10 | C | sem dado |
| 55 | 20875 | Brita N1 | Básico | R$ 978,00 | 3 | C | sem dado |
| 56 | 22027 | Piso Dacar Amarelo Demarcacao 18 Lts | Acabamento | R$ 960,00 | 2 | C | sem dado |
| 57 | 22148 | Piso Dacar Vermelho Demarcacao 18 Lts | Acabamento | R$ 960,00 | 2 | C | sem dado |
| 58 | PRD00017 | Estribo De Aco 07 X 14Cm | Básico | R$ 945,10 | 804 | B | 61,7% |
| 59 | 21374 | Areiao Sem Pedra 1M³ | Básico | R$ 932,10 | 4,5 | C | sem dado |
| 60 | PRD00119 | Tabua Caixaria 15Cm X 2,5Cm X 3,00Mt | Básico | R$ 921,93 | 26 | C | sem dado |
| 61 | PRD00082 | Contaminado 5M³ | Não classificado | R$ 910,00 | 1 | C | sem dado |
| 62 | PRD00117 | Trelica Leve 5,3X3,2X3,2Mm 6 M | Básico | R$ 881,58 | 22 | C | sem dado |
| 63 | 20978 | Caibro Cambara 5 X10 X 3 Metros | Básico | R$ 881,40 | 11 | C | sem dado |
| 64 | 009272 | Pf C/Porca Sext 1/2X2.1/2 | Básico | R$ 870,00 | 300 | B | sem dado |
| 65 | 1606 | Cortador Piso Master 115Cm Cortag 61600 - 61600 | Acabamento | R$ 870,00 | 1 | C | sem dado |
| 66 | 21100 | Forro / Teto | Não classificado | R$ 868,00 | 1 | C | sem dado |
| 67 | 20708 | Po De Brita 5M³ | Básico | R$ 845,00 | 1 | C | sem dado |
| 68 | 21344 | Coluna Armada 8Mm 7X14X6M | Básico | R$ 841,80 | 6 | C | sem dado |
| 69 | 22757 | Areia Media Ensacada - Balde | Básico | R$ 823,00 | 57 | C | 52,8% |
| 70 | 22269 | Tanquinho Mueler | Não classificado | R$ 787,00 | 1 | C | sem dado |
| 71 | 1996 | Areia Suja Rio 1M³ | Básico | R$ 760,00 | 1 | C | sem dado |
| 72 | 22501 | Tijolo De Vedacao 6 Furos - 09X14X24 | Básico | R$ 754,20 | 838 | B | sem dado |
| 73 | 20336 | Concreto Pronto 20Kg | Básico | R$ 744,88 | 31 | C | 42,6% |
| 74 | 20757 | Aco Ca 50 5/16" 8Mm(4,74Kg) 12M | Básico | R$ 743,00 | 21 | C | sem dado |
| 75 | 1212 | Prego Polido 17X27 1Kg Com Cabeca | Básico | R$ 708,90 | 36 | C | 42,0% |
| 76 | 12345 | Pu 40 Cinza 380G Orbi Quimica | Não classificado | R$ 700,00 | 35 | C | 58,2% |
| 77 | PRD00123 | Ventilador De Parede 60Cm Ventisol | Elétrica | R$ 699,00 | 2 | C | sem dado |
| 78 | 22236 | Roçadeira Palisad | Ferramentas | R$ 692,30 | 1 | C | sem dado |
| 79 | 21358 | Lona Preta 4X100  (50Micras) | Não classificado | R$ 673,30 | 137 | B | sem dado |
| 80 | 21966 | Hardtop Xp Amarelo Segurança Mun Jotun | Não classificado | R$ 660,00 | 2 | C | sem dado |
| 81 | 20857 | Brita 02 1M³ | Básico | R$ 643,06 | 4 | C | sem dado |
| 82 | 20913 | Ferro 5,0Mm (12 Metros) 1,848Kg T-Diversos Bruto | Básico | R$ 633,68 | 32 | C | 34,2% |
| 83 | 20718 | Espuma Expansiva 500Ml 320G Tekbond | Acabamento | R$ 631,80 | 24 | C | 32,4% |
| 84 | 22161 | Air Fryer Tamanho Medio Mecanica Black+Decker Afm4 220V | Bazar/diversos | R$ 605,00 | 1 | C | sem dado |
| 85 | 22257 | Estribo De Aco 07 X 20Cm | Básico | R$ 602,50 | 450 | B | 63,2% |
| 86 | 21563 | Seixo Amarelo N° 02 1M² | Básico | R$ 600,00 | 3 | C | sem dado |
| 87 | 21423 | Desempenadeira Aco Inox 60Cm Galo | Ferramentas | R$ 599,98 | 2 | C | sem dado |
| 88 | 22617 | Caibro Pinus Tratado 5X10X3,5M | Básico | R$ 599,92 | 8 | C | sem dado |
| 89 | 20276 | Tijolo Refratario Liso | Básico | R$ 599,00 | 100 | B | sem dado |
| 90 | 22468 | Lona Preta 4X100 75 Micros | Não classificado | R$ 595,90 | 101 | B | 45,7% |
| 91 | 21450 | Tubo Esgoto 50Mm - 6M | Hidráulica | R$ 585,92 | 9 | C | 30,7% |
| 92 | 20280 | Porta Angelim Completa | Acabamento | R$ 580,00 | 1 | C | sem dado |
| 93 | 1943 | Concreto Contrapiso | Básico | R$ 574,86 | 25 | C | sem dado |
| 94 | 20745 | Areia Fina Amarela 1M³ | Básico | R$ 549,82 | 1 | C | sem dado |
| 95 | PRD00121 | Armário De Cozinha Branco Mdf | Bazar/diversos | R$ 540,00 | 1 | C | sem dado |
| 96 | 21227 | Bloco Concreto 19X19X40 | Básico | R$ 532,00 | 140 | B | sem dado |
| 97 | 20593 | Ducha Nd Eletronica 7700W 220V Branco Zagonel | Hidráulica | R$ 523,60 | 4 | C | sem dado |
| 98 | 21454 | Tubo Soldavel 25Mm - 6M | Hidráulica | R$ 514,28 | 18 | C | 43,9% |
| 99 | 22646 | Tubo Esgoto 150Mm - 6M | Hidráulica | R$ 510,20 | 2 | C | 38,3% |
| 100 | 2014 | Plaqueta Refrataria 10 Furos - 22,9 X 11,4 X 3,2 Cm | Básico | R$ 510,00 | 60 | B | sem dado |
| 101 | 21306 | Sarrafo Pinus Caixaria 2,5 X 5Cm X 3M | Básico | R$ 509,30 | 51 | C | sem dado |
| 102 | 21460 | Tubo Esgoto 100Mm - 3M | Hidráulica | R$ 507,00 | 19 | C | sem dado |
| 103 | PRD00110 | Caixa De Agua 1000Lt Sultanque | Hidráulica | R$ 500,69 | 1 | C | sem dado |
| 104 | 22365 | Ducha Ducali Eletronica Black 7500W 220V Ddcel75220Bl03 | Hidráulica | R$ 500,25 | 1 | C | sem dado |
| 105 | 1940 | Cimento Nacional 50 Kg | Básico | R$ 475,40 | 13 | C | sem dado |
| 106 | 20703 | Luminaria De Emergencia / Bloco Autonomo 2 Farol 1200 Lumens 110V - 220V Blumenau | Elétrica | R$ 472,50 | 3 | C | sem dado |
| 107 | 21586 | Tinta Super Cobertura Semibrilho 18L Branco 1231 Resicolor - 1231 - Onu 1263 Classe Iii | Pintura | R$ 468,00 | 1 | C | sem dado |
| 108 | 22138 | Verniz Maritimo 3,6L Alessi | Pintura | R$ 466,00 | 3 | C | 42,0% |
| 109 | 1299 | Furadeira 3/8 Imp Gsb 450Re 450W Bosch | Ferramentas | R$ 462,00 | 1 | C | sem dado |
| 110 | 21436 | Thinner 5000/6000 18L Farben | Pintura | R$ 461,50 | 2 | C | sem dado |
| 111 | 22273 | Cabo Pp 3X2,50Mm 100Mt Corfio Preto 500V | Elétrica | R$ 460,60 | 47 | C | sem dado |
| 112 | 1295 | Caixa Pe Fortlev 1.000 L | Hidráulica | R$ 452,00 | 1 | C | sem dado |
| 113 | 20849 | Cabo Flexivel 2,5Mm 100Mt Azul | Elétrica | R$ 451,90 | 35 | C | sem dado |
| 114 | 21399 | Mecanismo P/ Caixa Acoplada Entrada + Saida + Botao- Roco | Hidráulica | R$ 449,70 | 3 | C | sem dado |
| 115 | 22906 | Massa Pronta Reparatec - Impermeavel | Pintura | R$ 449,10 | 9 | C | sem dado |
| 116 | 1211 | Prego Polido 17X27 1Kg Cabeca Dupla Gerdau - 117000253 | Básico | R$ 447,80 | 18 | C | 52,9% |
| 117 | 21702 | Pe Direito 8X8 3M Pinus Tratado | Básico | R$ 443,96 | 4 | C | sem dado |
| 118 | 22618 | Pinus Tratado Sarrafo 2,5 Cm X 5 Cm X 3M | Básico | R$ 431,76 | 24 | C | sem dado |
| 119 | PRD00011 | Esmerilhadeira 4.1/2" Dwe750-B2 220V De | Ferramentas | R$ 431,50 | 1 | C | sem dado |
| 120 | 21938 | Bermuda Brim Cinza Elastico Tam G | EPI/segurança | R$ 431,40 | 6 | C | sem dado |
| 121 | 20509 | Fita Crepe  Profissional Azul 48Mmx50M Larga Atlas | Pintura | R$ 430,00 | 20 | C | 62,0% |
| 122 | 22391 | Calçado Botina Taa Nobuck Marrom C.A 40.362 Bellga N 39 | EPI/segurança | R$ 426,00 | 2 | C | sem dado |
| 123 | 20793 | Argamassa Graute Cinza Certa Kg | Básico | R$ 423,30 | 17 | C | sem dado |
| 124 | 22454 | Rejunte Acrilico Bicomponente Platina 1Kg Pote | Acabamento | R$ 420,72 | 19 | C | 23,5% |
| 125 | 21167 | Madeira Pinus 6X12 - 3M | Básico | R$ 410,00 | 2 | C | sem dado |
| 126 | 1832 | Serra Marmore 125Mm 1400 W 220V Dewalt | Ferramentas | R$ 410,00 | 1 | C | sem dado |
| 127 | PRD00070 | Moerão Concreto Reto 2M | Básico | R$ 405,00 | 9 | C | sem dado |
| 128 | 20472 | Po De Brita | Básico | R$ 400,00 | 2 | C | sem dado |
| 129 | 1904 | Caixa Gordura 42L C/Cesto Limpeza | Hidráulica | R$ 398,90 | 3 | C | 71,1% |
| 130 | 1732 | Ducha Eletronica Advanced 7500W 220V | Hidráulica | R$ 397,80 | 2 | C | sem dado |
| 131 | 22458 | Rejunte Acrilico Bicomponente Branco 1Kg Pote | Acabamento | R$ 392,22 | 18 | C | 23,5% |
| 132 | 22150 | Areia Fina Cinza Ensacada - Balde | Básico | R$ 390,00 | 26 | C | sem dado |
| 133 | 22127 | Carro Mao 065L Extraforte Cinza 77714235 | Ferramentas | R$ 390,00 | 1 | C | sem dado |
| 134 | 21346 | Pedrisco Com Pó 1M³ | Básico | R$ 379,00 | 2 | C | sem dado |
| 135 | 21326 | Ac3 Porcelanato Cinza 20Kg Arga Certa Argamassa | Acabamento | R$ 377,00 | 13 | C | sem dado |
| 136 | 20990 | Arame Recozido N 18 | Básico | R$ 376,25 | 21 | C | 50,6% |
| 137 | 21571 | Colete Refletivo "Xg" Amarelo 10.01.2.3 | EPI/segurança | R$ 376,00 | 11 | C | sem dado |
| 138 | 20924 | Cumeeira Normal 15 5Mm | Básico | R$ 375,00 | 6 | C | sem dado |
| 139 | 22649 | Bloco Calha 20Cm | Básico | R$ 374,94 | 59 | B | sem dado |
| 140 | 21841 | Telha Eternit  2,44 X 1,10 X 6Mm | Básico | R$ 371,50 | 5 | C | sem dado |
| 141 | 20640 | Cal Hidratada | Básico | R$ 368,00 | 19 | C | 42,9% |
| 142 | 1201 | Manta Termica Simples 1 Face 1,20M - Metro | Básico | R$ 360,75 | 71 | B | 27,7% |
| 143 | 21809 | Estribo De Aço 20 X 9 | Básico | R$ 360,00 | 300 | B | sem dado |
| 144 | 20908 | Estribo 15X20X5Mm | Básico | R$ 358,00 | 200 | B | sem dado |
| 145 | 1897 | Cabo Flexivel 2,5Mm 100 M Verde | Elétrica | R$ 349,90 | 1 | C | sem dado |
| 146 | 1595 | Cabo Flexivel 2,5Mm 100Mt Preto | Elétrica | R$ 349,50 | 1 | C | sem dado |
| 147 | 22050 | Thinner 900Ml Qualyvinil | Pintura | R$ 348,20 | 13 | C | sem dado |
| 148 | 20971 | Telha Eternit 1,83 X 1,10 X 5Mm | Básico | R$ 345,10 | 7 | C | sem dado |
| 149 | 22237 | Roçadeira Agv 1000, 1.000 W, 220 V~, Vonder | Ferramentas | R$ 345,00 | 1 | C | sem dado |
| 150 | 22133 | Impermeabilizante Asfaltico Neutrol 03,6L 121826 | Pintura | R$ 339,80 | 2 | C | sem dado |
| 151 | 21681 | Picareta Alviao C/Cabo Minasul | Ferramentas | R$ 336,90 | 3 | C | 43,1% |
| 152 | 20487 | Torneira Eletrica Luna Parede 220V 5500W Branca Zagonel | Hidráulica | R$ 328,50 | 2 | C | sem dado |
| 153 | 1634 | Lona Plastica Preta 4X100M 30Kg Lonax | Básico | R$ 324,70 | 56 | C | sem dado |
| 154 | 22130 | Escada Exten. 07X02 Deg. Madeira Eucalipto F.S 2,07 A 3,44Mt | Ferramentas | R$ 322,50 | 1 | C | sem dado |
| 155 | 20974 | Cumeeira Universal 6Mm | Básico | R$ 321,60 | 6 | C | 25,4% |
| 156 | 22824 | Taxa De Entrega Itoupava Central | Serviço (entrega) | R$ 320,00 | 11 | C | sem dado |
| 157 | 1197 | Eletroduto Flexivel Corrugada 25Mm 3/4 50M Krona | Elétrica | R$ 317,50 | 116 | B | sem dado |
| 158 | 20504 | Aco Ca 60 3/16" 4,2Mm (1,308Kg) 12M | Básico | R$ 314,50 | 24 | C | sem dado |
| 159 | 22234 | Jogo Chave Fenda/Philips 6Pc Tramontina (1/4X3-3/16X3-1/8X3) 41110/506 - 41110/506 | Ferramentas | R$ 313,50 | 5 | C | sem dado |
| 160 | 21434 | Tubo Concreto 100X20X4Cm | Hidráulica | R$ 311,20 | 8 | C | sem dado |
| 161 | PRD00064 | Pu 40 Preto 380G Orbi Quimica | Não classificado | R$ 310,00 | 15 | C | 62,8% |
| 162 | 22254 | Taxa De Entrega Vila Itoupava Bongo | Serviço (entrega) | R$ 310,00 | 7 | C | sem dado |
| 163 | 22441 | Tinta Acrilica Pratika Fosco Branco 3,6L | Pintura | R$ 303,60 | 6 | C | sem dado |
| 164 | 22582 | Kit Acessorios Banheiro Basico 5Pç Cromado Bella Arte | Acabamento | R$ 302,90 | 3 | C | 35,8% |
| 165 | 1597 | Cabo Pp 2X2,50Mm 100Mt Corfio Preto 500V | Elétrica | R$ 302,10 | 30 | C | sem dado |
| 166 | 21124 | Tabua Caixaria 10Cm X 2,5Cm X 3,00Mt | Básico | R$ 301,68 | 23 | C | sem dado |
| 167 | 22217 | Luminaria Deluxe By Avant | Elétrica | R$ 300,00 | 1 | C | sem dado |
| 168 | 21585 | Base Acrilico Classica Toque Fosco Premium Suvinil A 3,2 Lts. A162 Ouro Branco | Não classificado | R$ 300,00 | 1 | C | sem dado |
| 169 | 21939 | Bermuda Brim Cinza Elastico Tam Gg | EPI/segurança | R$ 299,60 | 4 | C | sem dado |
| 170 | 20634 | Tijolo 6 Furos 09 X 14 X 29 (6F) Demarchi | Básico | R$ 297,00 | 180 | B | sem dado |
| 171 | 22645 | Sarrafo Pinus Bruto 3M | Básico | R$ 290,88 | 32 | C | sem dado |
| 172 | 22448 | Fundo Preparador Parede Incolor 18L | Pintura | R$ 290,00 | 1 | C | sem dado |
| 173 | PRD00068 | Argamassa Porcelanato Piso Sobre Piso 20Kg | Acabamento | R$ 288,00 | 12 | C | sem dado |

---
## 2. Categorias por faturamento

Top 15 produtos por faturamento dentro de cada categoria (lista completa de cada categoria na aba "Curva ABC por faturamento" da planilha, filtrando pela coluna Categoria).

### Acabamento (60 SKUs no total, top 15 abaixo)

| # | Código | Produto | Faturamento | Qtd. | Margem |
|---|---|---|---|---|---|
| 1 | 21070 | Vermelho Seguranca 5Ra/14 Epoxi Piso  2.88L Farben | R$ 8.638,46 | 16 | 0,3% |
| 2 | 21445 | Epoxi Piso Branco Farben 2,8L | R$ 7.873,06 | 24 | sem dado |
| 3 | 21437 | Catalisador Epoxi P/Piso  0.72L Farben | R$ 5.495,40 | 51 | sem dado |
| 4 | 22837 | Porta Interna Lisa | R$ 2.308,60 | 7 | sem dado |
| 5 | 21627 | Amarelo Seguranca 5Ra/14 Epoxi Piso  2.88L Farben | R$ 1.587,34 | 4 | sem dado |
| 6 | 21603 | Telha Cerâmica Esmaltada | R$ 1.425,00 | 150 | sem dado |
| 7 | 22027 | Piso Dacar Amarelo Demarcacao 18 Lts | R$ 960,00 | 2 | sem dado |
| 8 | 22148 | Piso Dacar Vermelho Demarcacao 18 Lts | R$ 960,00 | 2 | sem dado |
| 9 | 1606 | Cortador Piso Master 115Cm Cortag 61600 - 61600 | R$ 870,00 | 1 | sem dado |
| 10 | 20718 | Espuma Expansiva 500Ml 320G Tekbond | R$ 631,80 | 24 | 32,4% |
| 11 | 20280 | Porta Angelim Completa | R$ 580,00 | 1 | sem dado |
| 12 | 22454 | Rejunte Acrilico Bicomponente Platina 1Kg Pote | R$ 420,72 | 19 | 23,5% |
| 13 | 22458 | Rejunte Acrilico Bicomponente Branco 1Kg Pote | R$ 392,22 | 18 | 23,5% |
| 14 | 21326 | Ac3 Porcelanato Cinza 20Kg Arga Certa Argamassa | R$ 377,00 | 13 | sem dado |
| 15 | 22582 | Kit Acessorios Banheiro Basico 5Pç Cromado Bella Arte | R$ 302,90 | 3 | 35,8% |

### Básico (238 SKUs no total, top 15 abaixo)

| # | Código | Produto | Faturamento | Qtd. | Margem |
|---|---|---|---|---|---|
| 1 | PRD00045 | Cimento Supremo 50Kg | R$ 27.868,00 | 704 | 16,8% |
| 2 | 22446 | Argamassa Superkola 3Mais Cinza 20Kg | R$ 7.166,12 | 290 | 37,9% |
| 3 | 22114 | Tijolo 6 Furos 09 X 14 X 24 Cer. Lorenzetti | R$ 6.452,00 | 6.860 | 36,8% |
| 4 | 20861 | Areia Fina Cinza 1 M³ | R$ 5.440,07 | 25,5 | sem dado |
| 5 | 21356 | Bloco Concreto Normal  14 X 19 X 39 | R$ 5.248,80 | 1.470 | sem dado |
| 6 | 20250 | Tijolo 6 Furos 09 X 14 X 29 Cer. Lorenzetti | R$ 4.229,00 | 4.170 | 34,1% |
| 7 | PRD00079 | Areia Com Brita 00 - 1M³ | R$ 3.914,77 | 20 | sem dado |
| 8 | 101010 | Ferro 3/8 (12 Metros) 10Mm | R$ 3.449,59 | 61 | 28,5% |
| 9 | 20912 | Ferro 5/16 (12 Metros) 8Mm | R$ 3.205,40 | 86 | 27,0% |
| 10 | 20957 | Po De Pedra Ou Brita 1M³ | R$ 3.121,24 | 10,5 | sem dado |
| 11 | 12010 | Argamassa Massa Reboco Cinza 20Kg | R$ 3.061,60 | 138 | 56,5% |
| 12 | 22445 | Argamassa Extrakolla 2 Cinza 20Kg | R$ 3.034,50 | 143 | 42,2% |
| 13 | 20756 | Laje Isopor | R$ 2.944,73 | 48,7 | sem dado |
| 14 | PRD00129 | Areia Com Brita 01 1M³ | R$ 2.676,85 | 15 | sem dado |
| 15 | 20758 | Cimento Supremo Cpiv | R$ 2.345,30 | 60 | sem dado |

### Bazar/diversos (12 SKUs no total, top 15 abaixo)

| # | Código | Produto | Faturamento | Qtd. | Margem |
|---|---|---|---|---|---|
| 1 | 110203 | Perfume Boticário | R$ 3.075,42 | 1 | sem dado |
| 2 | PRD00122 | Balcao De Cozinha Com Três Portas Mdf | R$ 1.100,00 | 1 | sem dado |
| 3 | 123 | Celular Marca Poco | R$ 1.000,00 | 1 | sem dado |
| 4 | 22161 | Air Fryer Tamanho Medio Mecanica Black+Decker Afm4 220V | R$ 605,00 | 1 | sem dado |
| 5 | PRD00121 | Armário De Cozinha Branco Mdf | R$ 540,00 | 1 | sem dado |
| 6 | 22184 | Jogo De Faca Tramontina | R$ 140,00 | 2 | sem dado |
| 7 | 22167 | Fuy171 Chaleira De Vidro Com Capacidade De 2L | R$ 113,90 | 1 | sem dado |
| 8 | 22219 | Garrafa Termica Soprano 1L | R$ 32,00 | 1 | sem dado |
| 9 | 21876 | Guarda Chuva Sombrinha Preta Mor | R$ 25,50 | 1 | 38,6% |
| 10 | 21210 | Kit Reparo P/Bicicleta 7 Peças | R$ 15,00 | 1 | sem dado |
| 11 | 21773 | Conveniência Drops Halls Morango - 28Gr | R$ 3,00 | 1 | sem dado |
| 12 | 22838 | Cha Ice Tea Limao Zero C/ Gás - 290Ml | R$ 2,35 | 1 | sem dado |

### Elétrica (109 SKUs no total, top 15 abaixo)

| # | Código | Produto | Faturamento | Qtd. | Margem |
|---|---|---|---|---|---|
| 1 | 20252 | Refletor Slim Led 200 120 6500K Autovolt - Aluminio Unico | R$ 3.747,00 | 30 | sem dado |
| 2 | 20984 | Refletor Tr Led 200 - 16000 Lúmens - Autovolt 6500K Luz Fria Taschibra | R$ 984,00 | 6 | sem dado |
| 3 | PRD00123 | Ventilador De Parede 60Cm Ventisol | R$ 699,00 | 2 | sem dado |
| 4 | 20703 | Luminaria De Emergencia / Bloco Autonomo 2 Farol 1200 Lumens 110V - 220V Blumenau | R$ 472,50 | 3 | sem dado |
| 5 | 22273 | Cabo Pp 3X2,50Mm 100Mt Corfio Preto 500V | R$ 460,60 | 47 | sem dado |
| 6 | 20849 | Cabo Flexivel 2,5Mm 100Mt Azul | R$ 451,90 | 35 | sem dado |
| 7 | 1897 | Cabo Flexivel 2,5Mm 100 M Verde | R$ 349,90 | 1 | sem dado |
| 8 | 1595 | Cabo Flexivel 2,5Mm 100Mt Preto | R$ 349,50 | 1 | sem dado |
| 9 | 1197 | Eletroduto Flexivel Corrugada 25Mm 3/4 50M Krona | R$ 317,50 | 116 | sem dado |
| 10 | 1597 | Cabo Pp 2X2,50Mm 100Mt Corfio Preto 500V | R$ 302,10 | 30 | sem dado |
| 11 | 22217 | Luminaria Deluxe By Avant | R$ 300,00 | 1 | sem dado |
| 12 | 20361 | Cabo Cci 2 Vias | R$ 258,00 | 20 | 43,1% |
| 13 | 1071 | Cabo Flexivel Corfio1,5Mm 100Mt Azul | R$ 255,80 | 2 | sem dado |
| 14 | 20847 | Cabo Flexivel Corfio1,5Mm 1Mt Verde | R$ 252,00 | 126 | sem dado |
| 15 | 1160 | Cabo Flexivel Corfio2,5Mm 100Mt Vermelho* | R$ 222,74 | 8 | sem dado |

### EPI/segurança (28 SKUs no total, top 15 abaixo)

| # | Código | Produto | Faturamento | Qtd. | Margem |
|---|---|---|---|---|---|
| 1 | 21938 | Bermuda Brim Cinza Elastico Tam G | R$ 431,40 | 6 | sem dado |
| 2 | 22391 | Calçado Botina Taa Nobuck Marrom C.A 40.362 Bellga N 39 | R$ 426,00 | 2 | sem dado |
| 3 | 21571 | Colete Refletivo "Xg" Amarelo 10.01.2.3 | R$ 376,00 | 11 | sem dado |
| 4 | 21939 | Bermuda Brim Cinza Elastico Tam Gg | R$ 299,60 | 4 | sem dado |
| 5 | 22090 | Calçado Botina Tp092C Sem Bico 3 Gomos N43 Bidensidade Ca.41335 Nobuck Cafe Com Cadarco Cartom - 3961 | R$ 259,90 | 2 | sem dado |
| 6 | 20801 | Calçado Botina Taa Nobuck Marrom C.A 40.362 Bellga N 44 | R$ 213,00 | 1 | sem dado |
| 7 | 22393 | Calçado Botina Taa Nobuck Marrom C.A 40.362 Bellga N 41 | R$ 213,00 | 1 | sem dado |
| 8 | 22394 | Calçado Botina Taa Nobuck Marrom C.A 40.362 Bellga N 42 | R$ 213,00 | 1 | sem dado |
| 9 | 22395 | Calçado Botina Taa Nobuck Marrom C.A 40.362 Bellga N 43 | R$ 213,00 | 1 | sem dado |
| 10 | 22398 | Calçado Botina Taa Nobuck Preta C.A 40.362 Bellga N 40 | R$ 213,00 | 1 | sem dado |
| 11 | 22386 | Botina Taa Nobuck Castor C.A 40.362 Bellga N 40 | R$ 213,00 | 1 | sem dado |
| 12 | 1712 | Calçado Botina Taa Nobuck Castor C.A 40.362 Bellga N 38 | R$ 191,00 | 1 | sem dado |
| 13 | 21411 | Calçado Botina Monod.Pu C/Elast. 39 | R$ 162,60 | 2 | sem dado |
| 14 | 21415 | Calçado Botina Monod.Pu C/Elast. 44 | R$ 162,60 | 2 | sem dado |
| 15 | 22089 | Botina Tp092C Sem Bico 3 Gomos N42 Bidensidade Ca.41335 Nobuck Cafe Com Cadarco Cartom - 3960 | R$ 149,90 | 1 | sem dado |

### Ferramentas (169 SKUs no total, top 15 abaixo)

| # | Código | Produto | Faturamento | Qtd. | Margem |
|---|---|---|---|---|---|
| 1 | 22686 | Carrinho De Carga 45 L Minasul | R$ 1.205,06 | 7 | 38,1% |
| 2 | 21596 | Lixadeira De Parede 220V Vonder | R$ 1.153,12 | 1 | sem dado |
| 3 | 22236 | Roçadeira Palisad | R$ 692,30 | 1 | sem dado |
| 4 | 21423 | Desempenadeira Aco Inox 60Cm Galo | R$ 599,98 | 2 | sem dado |
| 5 | 1299 | Furadeira 3/8 Imp Gsb 450Re 450W Bosch | R$ 462,00 | 1 | sem dado |
| 6 | PRD00011 | Esmerilhadeira 4.1/2" Dwe750-B2 220V De | R$ 431,50 | 1 | sem dado |
| 7 | 1832 | Serra Marmore 125Mm 1400 W 220V Dewalt | R$ 410,00 | 1 | sem dado |
| 8 | 22127 | Carro Mao 065L Extraforte Cinza 77714235 | R$ 390,00 | 1 | sem dado |
| 9 | 22237 | Roçadeira Agv 1000, 1.000 W, 220 V~, Vonder | R$ 345,00 | 1 | sem dado |
| 10 | 21681 | Picareta Alviao C/Cabo Minasul | R$ 336,90 | 3 | 43,1% |
| 11 | 22130 | Escada Exten. 07X02 Deg. Madeira Eucalipto F.S 2,07 A 3,44Mt | R$ 322,50 | 1 | sem dado |
| 12 | 22234 | Jogo Chave Fenda/Philips 6Pc Tramontina (1/4X3-3/16X3-1/8X3) 41110/506 - 41110/506 | R$ 313,50 | 5 | sem dado |
| 13 | 1307 | Disco Corte 4.5" 1.0Mm Xt10 Extended 206162 Rhodius | R$ 262,80 | 12 | sem dado |
| 14 | 1184 | Escada Aluminio 5D Maestro 44X106X159Cm 120Kg | R$ 249,90 | 1 | sem dado |
| 15 | 20475 | Enxada Olho Oval 19Cm Com Cabo Eucalipto Pandolfo (Montada) | R$ 209,60 | 4 | 46,3% |

### Hidráulica (342 SKUs no total, top 15 abaixo)

| # | Código | Produto | Faturamento | Qtd. | Margem |
|---|---|---|---|---|---|
| 1 | 21452 | Tubo Esgoto 100Mm - 6M | R$ 2.260,40 | 26 | 33,5% |
| 2 | 22023 | Torneira Prima Eletronica 5500W 220V Black Zagonel | R$ 983,50 | 4 | sem dado |
| 3 | 003127 | Tubo Concreto 30X100 | R$ 980,00 | 10 | sem dado |
| 4 | 21450 | Tubo Esgoto 50Mm - 6M | R$ 585,92 | 9 | 30,7% |
| 5 | 20593 | Ducha Nd Eletronica 7700W 220V Branco Zagonel | R$ 523,60 | 4 | sem dado |
| 6 | 21454 | Tubo Soldavel 25Mm - 6M | R$ 514,28 | 18 | 43,9% |
| 7 | 22646 | Tubo Esgoto 150Mm - 6M | R$ 510,20 | 2 | 38,3% |
| 8 | 21460 | Tubo Esgoto 100Mm - 3M | R$ 507,00 | 19 | sem dado |
| 9 | PRD00110 | Caixa De Agua 1000Lt Sultanque | R$ 500,69 | 1 | sem dado |
| 10 | 22365 | Ducha Ducali Eletronica Black 7500W 220V Ddcel75220Bl03 | R$ 500,25 | 1 | sem dado |
| 11 | 1295 | Caixa Pe Fortlev 1.000 L | R$ 452,00 | 1 | sem dado |
| 12 | 21399 | Mecanismo P/ Caixa Acoplada Entrada + Saida + Botao- Roco | R$ 449,70 | 3 | sem dado |
| 13 | 1904 | Caixa Gordura 42L C/Cesto Limpeza | R$ 398,90 | 3 | 71,1% |
| 14 | 1732 | Ducha Eletronica Advanced 7500W 220V | R$ 397,80 | 2 | sem dado |
| 15 | 20487 | Torneira Eletrica Luna Parede 220V 5500W Branca Zagonel | R$ 328,50 | 2 | sem dado |

### Não classificado (93 SKUs no total, top 15 abaixo)

| # | Código | Produto | Faturamento | Qtd. | Margem |
|---|---|---|---|---|---|
| 1 | PRD00040 | Ar Condicionado 9.000 Btu Inverter Frio - Tcl | R$ 6.600,00 | 3 | sem dado |
| 2 | 21072 | Diluente Epoxi 8500 5L Farben | R$ 1.766,00 | 4 | sem dado |
| 3 | PRD00082 | Contaminado 5M³ | R$ 910,00 | 1 | sem dado |
| 4 | 21100 | Forro / Teto | R$ 868,00 | 1 | sem dado |
| 5 | 22269 | Tanquinho Mueler | R$ 787,00 | 1 | sem dado |
| 6 | 12345 | Pu 40 Cinza 380G Orbi Quimica | R$ 700,00 | 35 | 58,2% |
| 7 | 21358 | Lona Preta 4X100  (50Micras) | R$ 673,30 | 137 | sem dado |
| 8 | 21966 | Hardtop Xp Amarelo Segurança Mun Jotun | R$ 660,00 | 2 | sem dado |
| 9 | 22468 | Lona Preta 4X100 75 Micros | R$ 595,90 | 101 | 45,7% |
| 10 | PRD00064 | Pu 40 Preto 380G Orbi Quimica | R$ 310,00 | 15 | 62,8% |
| 11 | 21585 | Base Acrilico Classica Toque Fosco Premium Suvinil A 3,2 Lts. A162 Ouro Branco | R$ 300,00 | 1 | sem dado |
| 12 | PRD00065 | Pu 40 Branco 380G | R$ 260,00 | 13 | 53,9% |
| 13 | 21574 | Borracha Liquida Spray Branca 400Ml 240G Chemicolor | R$ 220,50 | 7 | 35,0% |
| 14 | 23453 | Sapato Monodensidade S/Bico N°43 | R$ 218,05 | 4 | sem dado |
| 15 | 22947 | Adesivo Instantaneo Ultrarrapido 100G | R$ 196,00 | 7 | 41,1% |

### Pintura (122 SKUs no total, top 15 abaixo)

| # | Código | Produto | Faturamento | Qtd. | Margem |
|---|---|---|---|---|---|
| 1 | 20492 | Fundo Preparador Parede 18L Alessi | R$ 4.312,00 | 16 | sem dado |
| 2 | 22758 | Tinta Acril. Fosco Economico 15Lt Eucatrex | R$ 1.800,00 | 20 | sem dado |
| 3 | 21698 | Tinta Amarelo Seguranca Piso | R$ 1.614,00 | 6 | sem dado |
| 4 | 21435 | Fita Crepe Amarela 18X40 Automotiva | R$ 1.292,50 | 167 | 38,7% |
| 5 | 20701 | Tinta Acril. Preto Semi Brilho | R$ 1.178,90 | 4 | sem dado |
| 6 | PRD00135 | Lukspiso Cinza Chumbo 3,6L | R$ 1.111,48 | 7 | sem dado |
| 7 | 21586 | Tinta Super Cobertura Semibrilho 18L Branco 1231 Resicolor - 1231 - Onu 1263 Classe Iii | R$ 468,00 | 1 | sem dado |
| 8 | 22138 | Verniz Maritimo 3,6L Alessi | R$ 466,00 | 3 | 42,0% |
| 9 | 21436 | Thinner 5000/6000 18L Farben | R$ 461,50 | 2 | sem dado |
| 10 | 22906 | Massa Pronta Reparatec - Impermeavel | R$ 449,10 | 9 | sem dado |
| 11 | 20509 | Fita Crepe  Profissional Azul 48Mmx50M Larga Atlas | R$ 430,00 | 20 | 62,0% |
| 12 | 22050 | Thinner 900Ml Qualyvinil | R$ 348,20 | 13 | sem dado |
| 13 | 22133 | Impermeabilizante Asfaltico Neutrol 03,6L 121826 | R$ 339,80 | 2 | sem dado |
| 14 | 22441 | Tinta Acrilica Pratika Fosco Branco 3,6L | R$ 303,60 | 6 | sem dado |
| 15 | 22448 | Fundo Preparador Parede Incolor 18L | R$ 290,00 | 1 | sem dado |

### Serviço (entrega) (12 SKUs no total, top 15 abaixo)

| # | Código | Produto | Faturamento | Qtd. | Margem |
|---|---|---|---|---|---|
| 1 | 20944 | Taxa De Entrega Itoupava Central Bongo | R$ 2.083,00 | 107 | sem dado |
| 2 | 22824 | Taxa De Entrega Itoupava Central | R$ 320,00 | 11 | sem dado |
| 3 | 22254 | Taxa De Entrega Vila Itoupava Bongo | R$ 310,00 | 7 | sem dado |
| 4 | 22209 | Taxa De Entrega Vila Itoupava Caminhao | R$ 220,00 | 3 | sem dado |
| 5 | 21252 | Taxa De Entrega Itoupava Central Caminhao | R$ 213,66 | 7 | sem dado |
| 6 | 20952 | Taxa Maquina Sipag | R$ 201,66 | 4 | sem dado |
| 7 | 20968 | Taxa De Entrega Itoupavazinha Caminhao | R$ 190,90 | 4 | sem dado |
| 8 | 20945 | Taxa De Entrega Itoupavazinha Bongo | R$ 180,00 | 9 | sem dado |
| 9 | 21251 | Taxa De Entrega Itoupava Norte Caminhao | R$ 150,00 | 3 | sem dado |
| 10 | 22208 | Taxa De Entrega Itoupava Norte Bongo | R$ 80,00 | 2 | sem dado |
| 11 | 22207 | Taxa De Entrega Agua Verde Bongo | R$ 80,00 | 1 | sem dado |
| 12 | 20953 | Taxa De Entrega Salto Norte Bongo | R$ 50,00 | 1 | sem dado |

---
## 3. Matriz Giro x Margem completa

Os 295 SKUs presentes nos dois relatórios (Curva ABC x Estoque), um por quadrante, ordenados por valor em estoque a custo (custo da compra mais recente; SKUs com mais de um fornecedor marcados como provisórios, ver seção 8 para a faixa completa de custo).

### Estrela (alto giro, alta margem) — 85 SKUs, R$ 2.942,70 em estoque

| # | Código | Produto | Categoria | Giro (qtd.) | Margem | Estoque | Valor em estoque | Obs. |
|---|---|---|---|---|---|---|---|---|
| 1 | 22468 | Lona Preta 4X100 75 Micros | Não classificado | 101 | 45,7% | 99 | R$ 317,30 |  |
| 2 | 22461 | Canaleta Adesiva Com Divisoria 20X10X2000Mm Branca | Acabamento | 11 | 55,6% | 54 | R$ 237,38 |  |
| 3 | PRD00065 | Pu 40 Branco 380G | Não classificado | 13 | 53,9% | 19 | R$ 175,07 |  |
| 4 | 20475 | Enxada Olho Oval 19Cm Com Cabo Eucalipto Pandolfo (Montada) | Ferramentas | 4 | 46,3% | 3 | R$ 96,42 |  |
| 5 | 20334 | Eletroduto Corrug 25Mm - 1M | Elétrica | 30 | 50,4% | 70 | R$ 86,77 |  |
| 6 | 12010 | Argamassa Massa Reboco Cinza 20Kg | Básico | 138 | 56,5% | 9 | R$ 85,70 | ⚠ provisório |
| 7 | 21583 | Curva Tipu U Inca Abraçadeira Tubo 100Mm | Hidráulica | 10 | 66,4% | 40 | R$ 79,24 |  |
| 8 | 22717 | Espelho 4X2 Cego On | Elétrica | 5 | 56,2% | 24 | R$ 73,52 |  |
| 9 | 38089 | Fita Veda Rosca 18Mmx50M Fortlev | Hidráulica | 10 | 46,9% | 9 | R$ 71,64 |  |
| 10 | 20990 | Arame Recozido N 18 | Básico | 21 | 50,6% | 9 | R$ 71,10 | ⚠ provisório |
| 11 | 12345 | Pu 40 Cinza 380G Orbi Quimica | Não classificado | 35 | 58,2% | 8 | R$ 66,83 |  |
| 12 | 22482 | Estribo De Aco 07 X 17Cm | Básico | 50 | 66,3% | 150 | R$ 58,19 |  |
| 13 | 22944 | Lapis Carpinteiro Amarelo | Ferramentas | 27 | 44,8% | 42 | R$ 57,96 |  |
| 14 | 21229 | Parafuso Telheiro P Fixar 5/16X110 | Básico | 81 | 57,1% | 130 | R$ 55,77 |  |
| 15 | 1569 | Joelho 90 Sold Bch Latao 20X1/2 Fortlev | Hidráulica | 7 | 58,3% | 15 | R$ 55,65 |  |
| 16 | 22072 | Cola Adesivo Pvc 165G Mundial | Hidráulica | 5 | 50,8% | 6 | R$ 54,62 |  |
| 17 | 21685 | Reducao Excentrica Esgoto 100X050Mm | Hidráulica | 5 | 49,6% | 12 | R$ 53,83 |  |
| 18 | 20282 | Gesso Juntalider 1Kg | Básico | 4 | 59,4% | 17 | R$ 51,81 |  |
| 19 | 1485 | Joelho 45 Soldavel 25Mm Fortlev | Hidráulica | 9 | 56,9% | 38 | R$ 49,18 |  |
| 20 | 20374 | Parafuso Chip 5,0X40 Amarelo | Básico | 14 | 61,4% | 486 | R$ 46,85 |  |
| 21 | PRD00017 | Estribo De Aco 07 X 14Cm | Básico | 804 | 61,7% | 119 | R$ 41,04 | ⚠ provisório |
| 22 | 1472 | Adaptador Sold Curto 32X1 Fortlev | Hidráulica | 6 | 55,3% | 28 | R$ 40,68 |  |
| 23 | 20473 | Abracadeira Tipo U B 3/4 25Mm Inca Zincada Inca | Básico | 18 | 65,0% | 128 | R$ 40,33 |  |
| 24 | 1211 | Prego Polido 17X27 1Kg Cabeca Dupla Gerdau - 117000253 | Básico | 18 | 52,9% | 3 | R$ 36,57 |  |
| 25 | 1431 | Te Esg Sn Dn 40 Fortlev | Hidráulica | 17 | 60,5% | 18 | R$ 35,48 |  |
| 26 | 22313 | Luva Esgoto 100Mm | Hidráulica | 12 | 51,3% | 9 | R$ 34,62 |  |
| 27 | 22101 | Parafuso Ponta Broca 12 - 5,5Mmx1 Sext (Chave 5/16) C/Arruela Auto Brocante Vila - | Ferramentas | 31 | 73,4% | 257 | R$ 34,12 |  |
| 28 | 20687 | Lixa Massa/ Acabamento Grão A100 | Pintura | 18 | 51,3% | 69 | R$ 33,60 |  |
| 29 | 1401 | Joelho 90 Soldavel 25Mm Fortlev | Hidráulica | 25 | 59,1% | 72 | R$ 32,37 |  |
| 30 | 20688 | Lixa Massa/ Madeira Grão 220 | Pintura | 12 | 69,6% | 61 | R$ 29,71 |  |
| 31 | 20452 | Rolo La S/Respingo S/Cabo 23Cm Roma | Pintura | 9 | 52,1% | 4 | R$ 29,68 |  |
| 32 | 22748 | Parafuso Chip 4,5X45 Amarelo | Básico | 200 | 52,0% | 300 | R$ 28,78 |  |
| 33 | 22757 | Areia Media Ensacada - Balde | Básico | 57 | 52,8% | 4 | R$ 28,32 |  |
| 34 | 20352 | Calkor 1L  (Cal Liquido) | Básico | 13 | 51,1% | 5 | R$ 28,10 | ⚠ provisório |
| 35 | 1008 | Balde Plastico 12 Lt Preto | Não classificado | 5 | 45,7% | 3 | R$ 27,51 |  |
| 36 | 22692 | Fita Asfaltica 20Cmx10Mt | Básico | 4 | 58,3% | 1 | R$ 27,31 |  |
| 37 | 22555 | Lixa Massa Tatu Grao 120 | Pintura | 35 | 66,0% | 53 | R$ 27,06 |  |
| 38 | 14283 | Abracadeira Tipo U 3/4 Branca Click | Básico | 58 | 50,9% | 50 | R$ 27,00 |  |
| 39 | 1677 | Torneira Jardim Preto | Hidráulica | 12 | 60,6% | 11 | R$ 25,57 |  |
| 40 | 1163 | Caixa Luz 4X2 Amarela | Elétrica | 77 | 59,7% | 20 | R$ 24,20 |  |
| 41 | 20509 | Fita Crepe  Profissional Azul 48Mmx50M Larga Atlas | Pintura | 20 | 62,0% | 2 | R$ 23,91 |  |
| 42 | 1110 | Rolo La S/ Respingo 09Cm Com Cabo Roma | Pintura | 6 | 44,4% | 5 | R$ 23,36 | ⚠ provisório |
| 43 | 22257 | Estribo De Aco 07 X 20Cm | Básico | 450 | 63,2% | 50 | R$ 23,01 |  |
| 44 | 22018 | Mao Francesa 19 X 12 Cm Branco | Não classificado | 4 | 48,6% | 8 | R$ 22,60 |  |
| 45 | PRD00064 | Pu 40 Preto 380G Orbi Quimica | Não classificado | 15 | 62,8% | 3 | R$ 22,34 |  |
| 46 | 1706 | Luva Pigmentada Branca Fertak | Hidráulica | 6 | 50,4% | 10 | R$ 22,33 |  |
| 47 | 20842 | Gancho Com Bucha 06 Sao Raphael | Básico | 36 | 46,9% | 100 | R$ 21,24 |  |
| 48 | 21501 | Joelho 90 Esgoto 40Mm Fortlev | Hidráulica | 12 | 58,2% | 26 | R$ 20,63 |  |
| 49 | 1861 | Lixa Massa/Madeira  Grão P180 | Pintura | 10 | 73,2% | 42 | R$ 19,67 |  |
| 50 | 21135 | Adesivo Instantaneo 20G Unipega | Não classificado | 4 | 60,1% | 5 | R$ 18,94 |  |
| 51 | 38087 | Fita Veda Rosca 18Mmx10M Qualiflon | Hidráulica | 28 | 58,5% | 18 | R$ 18,68 | ⚠ provisório |
| 52 | 22571 | Parafuso Chip 5,0X80 Amarelo | Básico | 4 | 52,5% | 96 | R$ 18,24 |  |
| 53 | 20596 | Haste P/Chuveiro Branca 1/2" 30Cm Herc | Hidráulica | 4 | 53,0% | 3 | R$ 16,76 |  |
| 54 | 21427 | Parafuso Chip 5,0X60 Amarelo | Básico | 76 | 48,0% | 121 | R$ 15,72 |  |
| 55 | 1502 | Luva Soldavel 25Mm Fortlev | Hidráulica | 48 | 57,8% | 29 | R$ 15,29 |  |
| 56 | 1182 | Disco Serra/Madeira Circular Videa 7. 1/4 24D X 185Mm | Ferramentas | 5 | 50,3% | 1 | R$ 14,91 | ⚠ provisório |
| 57 | 1611 | Desempenadeira Plastica Estriada 14X27 Gerplast | Ferramentas | 4 | 54,1% | 3 | R$ 13,77 | ⚠ provisório |
| 58 | 1632 | Linha Pedreiro 100M 0.80Mm Laranja Vila | Ferramentas | 8 | 63,9% | 2 | R$ 13,00 |  |
| 59 | 22294 | Bucha 06 | Básico | 90 | 85,8% | 910 | R$ 12,93 |  |
| 60 | 22750 | Cadeado 25 Mm - Encartelado | Básico | 4 | 48,0% | 1 | R$ 11,95 |  |
| 61 | 21484 | Fita Isolante Preta 18Mmx10M Manplex | Elétrica | 27 | 57,3% | 5 | R$ 11,75 |  |
| 62 | 21470 | Tinta Spray 400Ml Preto Brilhante Mundial | Pintura | 5 | 51,2% | 1 | R$ 11,71 |  |
| 63 | 21589 | Canaleta Adesiva S/Div. 020X010X2000Mm Branca | Acabamento | 4 | 46,9% | 2 | R$ 10,52 |  |
| 64 | 20665 | Fita Dupla Face 12Mm X 2M Vila | Não classificado | 8 | 56,4% | 3 | R$ 10,33 |  |
| 65 | 21199 | Tubo Extensivo Branco 1,50Cm | Hidráulica | 4 | 44,8% | 1 | R$ 8,55 |  |
| 66 | 1325 | Eletrodo 2,50Mm Heavy Duty | Ferramentas | 30 | 58,5% | 19 | R$ 7,88 |  |
| 67 | 22154 | Prego Aco Com Cabeca 10X10 C/100 Pc Tx | Básico | 5 | 57,8% | 3 | R$ 7,47 |  |
| 68 | 31329 | Bloco Espuma Multiuso Amarelo | Não classificado | 7 | 74,1% | 3 | R$ 6,99 |  |
| 69 | 2487 | Desempenadeira Pvc Estriada 14X27 Roma | Hidráulica | 5 | 60,1% | 1 | R$ 5,59 |  |
| 70 | 21462 | Trena 3Mx16Mm Vila | Ferramentas | 4 | 59,4% | 1 | R$ 5,28 |  |
| 71 | 1014 | Broca Ar 03.0Mm Blister | Ferramentas | 6 | 61,2% | 3 | R$ 2,91 |  |
| 72 | 30839 | Gesso Secagem Rapida 1,0Kg | Básico | 5 | 68,7% | 1 | R$ 2,79 |  |
| 73 | 20998 | Fita Isolante Preta 18Mmx05M Manplex | Elétrica | 11 | 66,9% | 2 | R$ 2,58 |  |
| 74 | 21600 | Parafuso Chip 5,0X70 Amarelo | Básico | 94 | 55,7% | 14 | R$ 2,17 |  |
| 75 | 1332 | Par Chip Ch Ph 4.0X40 Bc Ph2 Multifix | Básico | 94 | 100,0% | 168 | R$ 0,00 |  |
| 76 | 1909 | Fita Asfaltica 20Cm - Venda Por Metro | Básico | 21 | 100,0% | 10 | R$ 0,00 |  |
| 77 | 1143 | Abracadeira Rsf-M C 1/2X5/8 C/100 13X16Mm 9Mm Inca | Básico | 24 | 100,0% | 35 | R$ 0,00 |  |
| 78 | 1997 | Escora De Eucalipto | Básico | 9 | 100,0% | 3 | R$ 0,00 |  |
| 79 | 21476 | Espatula Rejunte Colorida Borracha | Pintura | 11 | 100,0% | 9 | R$ 0,00 |  |
| 80 | 21571 | Colete Refletivo "Xg" Amarelo 10.01.2.3 | EPI/segurança | 11 | 100,0% | 4 | R$ 0,00 | ⚠ provisório |
| 81 | 949 | Fita Crepe Uso Geral Bege Euro 18Mm X 50M | Pintura | 19 | 100,0% | 3 | R$ 0,00 | ⚠ provisório |
| 82 | 22580 | Valvula Lavatorio S/Lad S/Unho 7/8" Plastico | Hidráulica | 5 | 100,0% | 2 | R$ 0,00 |  |
| 83 | 1068 | Broxa Atlas 15X6Cm Media 800/1 - 800/1 | Pintura | 5 | 100,0% | 3 | R$ 0,00 |  |
| 84 | 1447 | Luva Esg Sn Dn 50 Fortlev | Hidráulica | 7 | 100,0% | 15 | R$ 0,00 |  |
| 85 | 22862 | Disco Corte Diamantado Segmentado 110Mm Fertak | Ferramentas | 4 | 100,0% | 8 | R$ 0,00 |  |

### Isca (alto giro, baixa margem) — 78 SKUs, R$ 24.446,22 em estoque

| # | Código | Produto | Categoria | Giro (qtd.) | Margem | Estoque | Valor em estoque | Obs. |
|---|---|---|---|---|---|---|---|---|
| 1 | 22483 | Bucha Plastica C/ Anel Concreto 8Mm | Básico | 22 | -224,0% | 478 | R$ 5.377,50 |  |
| 2 | PRD00045 | Cimento Supremo 50Kg | Básico | 704 | 16,8% | 95 | R$ 3.135,00 |  |
| 3 | PRD00016 | Estribo Flexfer 10X16 4,2Mm | Básico | 180 | -49,0% | 42 | R$ 2.520,00 |  |
| 4 | 20250 | Tijolo 6 Furos 09 X 14 X 29 Cer. Lorenzetti | Básico | 4.170 | 34,1% | 2.598 | R$ 1.883,03 |  |
| 5 | 22114 | Tijolo 6 Furos 09 X 14 X 24 Cer. Lorenzetti | Básico | 6.860 | 36,8% | 2.514 | R$ 1.508,40 |  |
| 6 | 16420 | Corante Base Dagua 50Ml Xadrez Preto | Pintura | 25 | -5,7% | 24 | R$ 1.200,48 |  |
| 7 | 1592 | Bucha Plastica Tijolo Oco 10Mm (500) Branca Ufu Usaf | Básico | 216 | -77,4% | 1.414 | R$ 752,45 |  |
| 8 | 21452 | Tubo Esgoto 100Mm - 6M | Hidráulica | 26 | 33,5% | 12 | R$ 709,43 |  |
| 9 | 1581 | Serra Arco 12.24 Flexivel Starrett | Ferramentas | 4 | -5,5% | 6 | R$ 554,34 |  |
| 10 | 22445 | Argamassa Extrakolla 2 Cinza 20Kg | Básico | 143 | 42,2% | 39 | R$ 507,00 |  |
| 11 | 22446 | Argamassa Superkola 3Mais Cinza 20Kg | Básico | 290 | 37,9% | 24 | R$ 415,68 |  |
| 12 | 101010 | Ferro 3/8 (12 Metros) 10Mm | Básico | 61 | 28,5% | 9 | R$ 386,10 |  |
| 13 | 20912 | Ferro 5/16 (12 Metros) 8Mm | Básico | 86 | 27,0% | 10 | R$ 298,00 |  |
| 14 | 21450 | Tubo Esgoto 50Mm - 6M | Hidráulica | 9 | 30,7% | 7 | R$ 291,00 |  |
| 15 | 21344 | Coluna Armada 8Mm 7X14X6M | Básico | 6 | -7,2% | 2 | R$ 279,80 |  |
| 16 | 22686 | Carrinho De Carga 45 L Minasul | Ferramentas | 7 | 38,1% | 3 | R$ 278,58 | ⚠ provisório |
| 17 | 21070 | Vermelho Seguranca 5Ra/14 Epoxi Piso  2.88L Farben | Acabamento | 16 | 0,3% | 1 | R$ 261,69 |  |
| 18 | 4436 | Cabo De Aco Plastificado 3/32" 2,40Mm | Básico | 400 | -24,0% | 100 | R$ 247,93 | ⚠ provisório |
| 19 | 20974 | Cumeeira Universal 6Mm | Básico | 6 | 25,4% | 6 | R$ 239,94 |  |
| 20 | 20734 | Torneira Jardim Megajato 1/2" Amarela  - Metro | Hidráulica | 7 | 43,2% | 93 | R$ 190,27 | ⚠ provisório |
| 21 | 20530 | Massa Polimérica 5Kg | Pintura | 13 | 25,7% | 12 | R$ 187,20 |  |
| 22 | 21557 | Ferro 4,2Mm (12 Metros) | Básico | 17 | 23,2% | 19 | R$ 182,40 |  |
| 23 | 1016 | Broca Ar 04.0Mm Blister C/10 Din 338 Vila - | Ferramentas | 13 | -109,7% | 11 | R$ 172,97 |  |
| 24 | 20718 | Espuma Expansiva 500Ml 320G Tekbond | Acabamento | 24 | 32,4% | 10 | R$ 135,21 |  |
| 25 | 21809 | Estribo De Aço 20 X 9 | Básico | 300 | -26,2% | 80 | R$ 131,20 |  |
| 26 | 22458 | Rejunte Acrilico Bicomponente Branco 1Kg Pote | Acabamento | 18 | 23,5% | 6 | R$ 130,74 |  |
| 27 | 1457 | Curva Esg 90° Curta  Sn Dn 50 Fortlev | Hidráulica | 5 | 35,6% | 20 | R$ 128,84 |  |
| 28 | 20913 | Ferro 5,0Mm (12 Metros) 1,848Kg T-Diversos Bruto | Básico | 32 | 34,2% | 10 | R$ 124,90 |  |
| 29 | 22905 | Veda Reboco 1L | Pintura | 12 | 34,0% | 10 | R$ 120,74 |  |
| 30 | 22454 | Rejunte Acrilico Bicomponente Platina 1Kg Pote | Acabamento | 19 | 23,5% | 5 | R$ 108,95 |  |
| 31 | 20336 | Concreto Pronto 20Kg | Básico | 31 | 42,6% | 9 | R$ 107,91 |  |
| 32 | 1212 | Prego Polido 17X27 1Kg Com Cabeca | Básico | 36 | 42,0% | 10 | R$ 104,40 | ⚠ provisório |
| 33 | 22456 | Rejunte Juntakor Cinza 1Kg | Acabamento | 23 | 37,7% | 29 | R$ 86,71 |  |
| 34 | 20361 | Cabo Cci 2 Vias | Elétrica | 20 | 43,1% | 180 | R$ 81,93 |  |
| 35 | 21453 | Tubo Soldavel 20Mm - 6M | Hidráulica | 10 | 27,3% | 6 | R$ 78,05 |  |
| 36 | 21454 | Tubo Soldavel 25Mm - 6M | Hidráulica | 18 | 43,9% | 5 | R$ 77,14 | ⚠ provisório |
| 37 | 22146 | Trincha Branca "396" 3.0"  396/7 | Pintura | 7 | 36,9% | 6 | R$ 73,86 | ⚠ provisório |
| 38 | 22455 | Rejunte Juntakor Branco 1Kg | Acabamento | 7 | 37,7% | 24 | R$ 71,76 |  |
| 39 | 1417 | Curva Esg Longa 100Mm | Hidráulica | 4 | 29,5% | 4 | R$ 70,52 |  |
| 40 | 21989 | Oculos Boxer Verde Vonder | EPI/segurança | 5 | 41,6% | 12 | R$ 70,10 | ⚠ provisório |
| 41 | 1503 | Luva Soldavel 20Mm Fortlev | Hidráulica | 25 | 18,0% | 159 | R$ 65,19 |  |
| 42 | 1201 | Manta Termica Simples 1 Face 1,20M - Metro | Básico | 71 | 27,7% | 20 | R$ 65,04 |  |
| 43 | 22956 | Lixa Ferro Gr80 225X275 | Pintura | 16 | 40,4% | 29 | R$ 60,49 | ⚠ provisório |
| 44 | 1112 | Rolo La Anti Respingo 5Cm Atlas | Pintura | 7 | 40,3% | 10 | R$ 59,10 |  |
| 45 | 22457 | Rejunte Juntakor Cinza Claro 1Kg | Acabamento | 15 | 37,7% | 19 | R$ 56,81 |  |
| 46 | 22947 | Adesivo Instantaneo Ultrarrapido 100G | Não classificado | 7 | 41,1% | 3 | R$ 49,44 |  |
| 47 | 1891 | Caixa Medidor Provisoria Preta | Hidráulica | 4 | 38,8% | 1 | R$ 48,93 | ⚠ provisório |
| 48 | 643882 | Lixa Massa Madeira Gr80 225X275 | Pintura | 9 | 41,7% | 66 | R$ 48,13 | ⚠ provisório |
| 49 | 21616 | Lixa Ferro Gr120 225X275 | Pintura | 7 | 39,9% | 25 | R$ 48,11 |  |
| 50 | 21574 | Borracha Liquida Spray Branca 400Ml 240G Chemicolor | Não classificado | 7 | 35,0% | 2 | R$ 44,84 |  |
| 51 | 1446 | Luva Esg Sn Dn 75 Fortlev | Hidráulica | 5 | 37,5% | 13 | R$ 44,66 | ⚠ provisório |
| 52 | 898 | Prego Aco Temperado Com Cabeca 17 X 27 | Básico | 4 | 35,5% | 3 | R$ 40,80 |  |
| 53 | 20640 | Cal Hidratada | Básico | 19 | 42,9% | 3 | R$ 37,50 |  |
| 54 | 1422 | Joelho 90 Esg 75 | Hidráulica | 13 | 34,5% | 8 | R$ 36,69 |  |
| 55 | 21435 | Fita Crepe Amarela 18X40 Automotiva | Pintura | 167 | 38,7% | 7 | R$ 36,47 | ⚠ provisório |
| 56 | 21221 | Rolo Espuma Poliester Cinza C/Cabo 09Cm Atlas | Pintura | 9 | 43,5% | 8 | R$ 33,92 |  |
| 57 | 2804 | Plug Pino Macho 2P+T 20A/250V 39186 Mec-Tronic | Hidráulica | 5 | 42,2% | 7 | R$ 32,17 |  |
| 58 | 23452 | Sapato Monodensidade S/Bico Cano Baixo N°42 | Hidráulica | 5 | 40,1% | 1 | R$ 31,44 |  |
| 59 | 449 | Parafuso Ros Sob Sext 1/4 X 60Mm | Básico | 18 | 32,7% | 82 | R$ 30,34 |  |
| 60 | 22687 | Abracadeira Borboleta 16Mm Metalmatrix | Básico | 4 | 39,7% | 10 | R$ 29,56 |  |
| 61 | 21541 | Lixa Massa Folha Gr150 225X275 Vila | Pintura | 5 | 43,4% | 45 | R$ 25,49 |  |
| 62 | 22144 | Trincha Branca "396" 1.1/2"  396/4 | Pintura | 13 | 37,3% | 5 | R$ 24,75 | ⚠ provisório |
| 63 | 22861 | Disco Corte Inox 4.1/2" - 115X1,0X22,2 Heavy Duty | Ferramentas | 79 | 36,2% | 24 | R$ 24,50 |  |
| 64 | 451 | Parafuso Ros Sob Sext 1/4 X 70Mm | Básico | 41 | 35,0% | 59 | R$ 23,01 |  |
| 65 | 22477 | Broca Videa 06,0Mm | Ferramentas | 6 | 35,6% | 5 | R$ 21,90 |  |
| 66 | 1932 | Painel Led Quadrado Sobrepor Pc 18W 6500K Bivolt | Elétrica | 6 | 43,5% | 1 | R$ 20,28 |  |
| 67 | 2915 | Plug Femea 2P+T 20A/250V 39175 Mec-Tronic | Hidráulica | 8 | 42,3% | 5 | R$ 18,04 |  |
| 68 | 22274 | Fita Veda Rosca 18X10 Qualiflon | Hidráulica | 6 | 35,8% | 14 | R$ 17,08 |  |
| 69 | 876 | Pu 40 Branco 80G Unipega | Não classificado | 4 | 43,4% | 3 | R$ 16,80 |  |
| 70 | 815 | Plug Pino Macho 2P+T 10A/250V | Hidráulica | 15 | 41,1% | 3 | R$ 15,89 | ⚠ provisório |
| 71 | 1481 | Joelho 90 Soldavel 20Mm Fortlev | Hidráulica | 14 | 43,3% | 35 | R$ 12,91 |  |
| 72 | 20962 | Protetor Auditivo/Auricular C/ Cordao | EPI/segurança | 4 | 38,0% | 4 | R$ 11,16 | ⚠ provisório |
| 73 | 20506 | Arame Recozido N 14 | Básico | 4 | 43,4% | 1 | R$ 10,64 |  |
| 74 | 1179 | Disco Diamantado Turbo 20 X 110Mm | Ferramentas | 4 | 42,0% | 1 | R$ 7,25 |  |
| 75 | 21665 | Joelho Esgoto 90.X100Mm 0619 | Hidráulica | 21 | 35,7% | 1 | R$ 5,79 | ⚠ provisório |
| 76 | 991 | Pu 40 Preto 80G Unipega | Não classificado | 6 | 43,4% | 1 | R$ 5,60 |  |
| 77 | PRD00023 | Fita Isolante Anti Chama 19Mmx20M. | Elétrica | 9 | 39,1% | 1 | R$ 3,35 |  |
| 78 | 21603 | Telha Cerâmica Esmaltada | Acabamento | 150 | -4,0% | 0 | R$ 0,00 |  |

### Reserva de lucro (baixo giro, alta margem) — 62 SKUs, R$ 1.603,65 em estoque

| # | Código | Produto | Categoria | Giro (qtd.) | Margem | Estoque | Valor em estoque | Obs. |
|---|---|---|---|---|---|---|---|---|
| 1 | 20516 | Silicone 400G Base Dagua Unipega (Selante Acrilico Branco) - Aes0511.0049 | Acabamento | 3 | 57,2% | 21 | R$ 193,04 |  |
| 2 | 1631 | Linha Pedreiro 100M 0.80Mm Branca Vila | Ferramentas | 1 | 62,4% | 19 | R$ 128,42 |  |
| 3 | 22553 | Parafuso Chipboard Ch Ph 4,0 X 50Mm | Básico | 1 | 49,4% | 1.504 | R$ 114,24 |  |
| 4 | 20356 | Mao Francesa 38.5 X 23.5 Cm Branco | Não classificado | 3 | 44,6% | 12 | R$ 93,00 |  |
| 5 | 1507 | Luva De Correr Soldavel 25Mm | Hidráulica | 3 | 55,3% | 14 | R$ 74,45 |  |
| 6 | 20819 | Disco Diamantado Segmentado 20 X 110Mm Fertak | Ferramentas | 2 | 60,6% | 9 | R$ 67,05 |  |
| 7 | 21096 | Compound Adesivo 1Kg Otto | Não classificado | 1 | 47,2% | 1 | R$ 63,31 |  |
| 8 | 21582 | Abracadeira Nylon Preta 4,8 X 370 - 100Pçs Vila | Básico | 2 | 45,0% | 4 | R$ 53,91 |  |
| 9 | 20766 | Curva Soldavel 90° 25Mm Fortlev | Hidráulica | 3 | 57,0% | 22 | R$ 52,03 |  |
| 10 | 21440 | Te Esg 100Mm | Hidráulica | 2 | 46,6% | 4 | R$ 44,64 |  |
| 11 | 20975 | Prego Polido 19X36 1Kg Com Cabeca Gerdau | Básico | 1 | 45,0% | 4 | R$ 42,92 |  |
| 12 | 20355 | Mao Francesa 29 X 16.5 Cm Branco | Não classificado | 2 | 47,8% | 10 | R$ 39,12 |  |
| 13 | 20246 | Plug Te 3 Saidas 10A 2P+T Perlex | Hidráulica | 2 | 55,9% | 6 | R$ 38,34 |  |
| 14 | 1490 | Curva Soldavel 90° 32Mm Fortlev | Hidráulica | 2 | 54,8% | 7 | R$ 37,32 | ⚠ provisório |
| 15 | 1042 | Broca Encaixe Sds Plus8X160Mm Blister Vila - | Ferramentas | 2 | 48,5% | 5 | R$ 35,81 |  |
| 16 | 22125 | Silicone Incolor Mundial 260G | Não classificado | 2 | 44,8% | 3 | R$ 32,94 |  |
| 17 | 1456 | Joelho 45 Esg Sn Dn 40 Fortlev | Hidráulica | 1 | 60,6% | 23 | R$ 29,48 |  |
| 18 | 11650 | Conjunto Mangueira Jardim Trancada 15M (Fama) | Hidráulica | 1 | 51,1% | 1 | R$ 29,31 |  |
| 19 | 20724 | Broca Aco Rapido P/ Metal 8,0Mm | Ferramentas | 1 | 58,2% | 9 | R$ 28,22 |  |
| 20 | 1904 | Caixa Gordura 42L C/Cesto Limpeza | Hidráulica | 3 | 71,1% | 1 | R$ 27,50 |  |
| 21 | 22924 | Parafuso Ponta Broca 12 - 5,5Mm X 1/2 Sext (Chave 5/16) C/ Arruela Vila | Ferramentas | 1 | 50,8% | 100 | R$ 24,62 | ⚠ provisório |
| 22 | 21486 | Mangueira Entrada Maquina 1,20M | Hidráulica | 3 | 51,1% | 2 | R$ 21,53 | ⚠ provisório |
| 23 | 21982 | Gas De Macarico / Fogareiro 400Ml Unipega | Ferramentas | 2 | 54,4% | 2 | R$ 18,16 |  |
| 24 | 20300 | Disjuntor Monopolar Shb 20A - Soprano | Elétrica | 2 | 59,6% | 3 | R$ 16,38 |  |
| 25 | 22561 | Sifao Tubo Extensivo Branco 1,50Cm Plasbohn | Hidráulica | 3 | 61,5% | 2 | R$ 16,18 |  |
| 26 | 20508 | Disco Serra/Madeira Circular 20.0 X 110 X 24D Fertak | Ferramentas | 1 | 55,4% | 2 | R$ 15,98 |  |
| 27 | 1599 | Caixa Para Massa 20L Preta Gerplast | Não classificado | 1 | 53,1% | 2 | R$ 15,94 |  |
| 28 | 22043 | Pilha Alcalina Aa C/02 Und Eletronic | Elétrica | 1 | 54,3% | 5 | R$ 15,76 | ⚠ provisório |
| 29 | 1073 | Capa Chuva Descartavel Transparente Riplas | EPI/segurança | 2 | 45,5% | 5 | R$ 14,18 |  |
| 30 | 22556 | Cadeado 30 Mm - Encartelado | Básico | 3 | 46,3% | 1 | R$ 13,90 |  |
| 31 | 21503 | Valvula Pia Inox 3.1/2 C/Pino Tampa Inos Padova | Hidráulica | 3 | 58,9% | 2 | R$ 12,32 | ⚠ provisório |
| 32 | 20777 | Valvula Lavatorio S/Lad S/Unho 7/8 '' Cromada Astra | Hidráulica | 1 | 44,5% | 1 | R$ 11,98 |  |
| 33 | 1036 | Broca Videa P/ Concreto 8,0Mm | Ferramentas | 2 | 50,8% | 4 | R$ 11,80 |  |
| 34 | 20458 | Verniz Incolor Maritimo 225Ml Qualyvinil | Pintura | 3 | 45,4% | 1 | R$ 11,20 |  |
| 35 | 20349 | Disco Serra/Madeira Circular Videa 4.3/8 110X20X12D Blister Vila | Ferramentas | 1 | 57,0% | 2 | R$ 11,09 |  |
| 36 | 1847 | Trena Emborrachada 05M X 19Mm Vila | Ferramentas | 1 | 56,5% | 1 | R$ 11,09 |  |
| 37 | 1679 | Trena Emborrachada 5M X 24Mm Fertak | Ferramentas | 2 | 49,8% | 1 | R$ 9,99 |  |
| 38 | 21500 | Conjunto Esguicho / Adaptador E Engate Rapido 1/2" Palisad | Hidráulica | 1 | 60,2% | 1 | R$ 9,75 |  |
| 39 | 20601 | Plug Macho 2P 10A 250V Branco | Hidráulica | 2 | 61,8% | 3 | R$ 9,74 |  |
| 40 | 22312 | Joelho Esgoto 45.X100Mm 0614 | Hidráulica | 3 | 45,4% | 2 | R$ 9,72 |  |
| 41 | 20451 | Prolongador P/Torneira 1/2 Curta 38Mm Zamak Garden | Hidráulica | 2 | 59,5% | 2 | R$ 9,72 |  |
| 42 | 1610 | Desempenadeira Pvc C/Espuma 17X30 Roma | Hidráulica | 2 | 60,5% | 1 | R$ 9,43 |  |
| 43 | 21419 | Epoxi Hobby 16Gr Durepoxi | Não classificado | 3 | 62,6% | 1 | R$ 8,98 |  |
| 44 | 13890 | Esguicho Pistola 7 Funcoes 1/2" 651618 | Hidráulica | 1 | 60,1% | 1 | R$ 7,99 |  |
| 45 | 1851 | Sifao Tubo Extensivel Branco 72Cm Plasbohn | Hidráulica | 3 | 50,4% | 2 | R$ 7,94 |  |
| 46 | 21309 | Chave Philips 3/16X4 Fertak | Ferramentas | 2 | 60,0% | 2 | R$ 7,60 |  |
| 47 | 1548 | Registro Esf Sold Uniao 25Mm | Hidráulica | 1 | 83,9% | 2 | R$ 7,04 |  |
| 48 | 1109 | Rolo La S/ Respingo 05Cm Com Cabo - Roma | Pintura | 2 | 44,9% | 2 | R$ 6,50 |  |
| 49 | 21667 | Jogo Chave Allen Hexagonal 8 Pçs Fertak | Ferramentas | 1 | 57,8% | 1 | R$ 6,29 |  |
| 50 | 20299 | Disjuntor Monopolar Shb 10A - Soprano | Elétrica | 2 | 59,6% | 1 | R$ 5,46 |  |
| 51 | 15885 | Engate Rapido C/ Stop 1/2 (Bestfer) | Hidráulica | 3 | 72,4% | 2 | R$ 4,96 |  |
| 52 | 1619 | Espatula 08Cm Cabo Plastico | Pintura | 1 | 54,4% | 1 | R$ 4,79 |  |
| 53 | 21588 | Fita Dupla Face 12Mmx2Mt | Não classificado | 2 | 56,5% | 1 | R$ 3,70 | ⚠ provisório |
| 54 | 21940 | Cruzeta / Espacador 2,00Mm C/100 | Básico | 1 | 61,3% | 2 | R$ 3,48 |  |
| 55 | 22060 | Cruzeta / Espacador 3,00Mm C/100 | Básico | 1 | 62,2% | 2 | R$ 3,40 |  |
| 56 | 1142 | Abracadeira Rsf-M C 1/2X3/4 C/100 13X19Mm 9Mm Inca | Básico | 3 | 100,0% | 71 | R$ 0,00 |  |
| 57 | 1044 | Broca Encaixe Sds Plus 10X160Mm Blister Vila - | Ferramentas | 1 | 100,0% | 3 | R$ 0,00 |  |
| 58 | 20803 | Convertedor Ferrugem Tf7 100Ml | Não classificado | 2 | 100,0% | 2 | R$ 0,00 | ⚠ provisório |
| 59 | 1574 | Luva Sold Bch Latao 25X3/4 Fortlev | Hidráulica | 1 | 100,0% | 16 | R$ 0,00 |  |
| 60 | 1021 | Broca Ar 06.5Mm Blister C/10 Din 338 Vila - | Ferramentas | 1 | 100,0% | 8 | R$ 0,00 |  |
| 61 | 1579 | Aplicador De Silicone E Pu Profissional 9" Fertak | Ferramentas | 1 | 100,0% | 2 | R$ 0,00 | ⚠ provisório |
| 62 | 22111 | Mangueira Saida Maquina Lavar | Hidráulica | 1 | 100,0% | 3 | R$ 0,00 |  |

### Candidato a liquidar (baixo giro, baixa margem) — 70 SKUs, R$ 5.375,16 em estoque

| # | Código | Produto | Categoria | Giro (qtd.) | Margem | Estoque | Valor em estoque | Obs. |
|---|---|---|---|---|---|---|---|---|
| 1 | 20708 | Po De Brita 5M³ | Básico | 1 |  | 4 | R$ 534,40 |  |
| 2 | 21449 | Tubo Esgoto 40Mm - 6M | Hidráulica | 2 | 41,6% | 13 | R$ 325,63 |  |
| 3 | 21451 | Tubo Esgoto 75Mm - 6M | Hidráulica | 1 | 26,1% | 5 | R$ 317,87 |  |
| 4 | 22646 | Tubo Esgoto 150Mm - 6M | Hidráulica | 2 | 38,3% | 2 | R$ 308,67 |  |
| 5 | 22138 | Verniz Maritimo 3,6L Alessi | Pintura | 3 | 42,0% | 2 | R$ 173,97 |  |
| 6 | 22940 | Regua Pedreiro 2M Pratica | Ferramentas | 1 | 39,5% | 4 | R$ 148,76 |  |
| 7 | 1516 | Caixa De Luz Octogonal 4X4 Fortlev | Elétrica | 2 | -2,5% | 10 | R$ 142,50 |  |
| 8 | 1466 | Adaptador Sold Cx Dagua 50X1.1/2 Fortlev | Hidráulica | 3 | 34,7% | 10 | R$ 137,22 |  |
| 9 | 20681 | Mistura De Areia Fina Com Brita 00 1M³ | Básico | 1 | 31,5% | 1 | R$ 123,41 |  |
| 10 | 21681 | Picareta Alviao C/Cabo Minasul | Ferramentas | 3 | 43,1% | 2 | R$ 119,52 |  |
| 11 | 1468 | Adaptador Sold Cx Dagua 25X3/4 | Hidráulica | 3 | 40,4% | 23 | R$ 116,52 |  |
| 12 | PRD00071 | Ferro 1/4 (12 Metros) 2,94 Kg 6,35Mm | Básico | 1 | 28,6% | 6 | R$ 107,94 |  |
| 13 | 20659 | Corante Base Dagua 50Ml Xadrez Vermelho | Pintura | 3 | -1,9% | 5 | R$ 107,50 |  |
| 14 | 1039 | Broca Encaixe Sds Plus7X160Mm Blister Vila - | Ferramentas | 2 | 32,8% | 13 | R$ 107,09 |  |
| 15 | 22442 | Tinta Acrilica Fosco Branco 18L Isabela | Pintura | 1 | 34,1% | 1 | R$ 105,52 |  |
| 16 | 1625 | Fita Isolante Autofusao 19Mmx10M Foxlux | Elétrica | 2 | 29,1% | 5 | R$ 102,75 |  |
| 17 | 21666 | Jogo Chave Combinada C/12 Pcs 06 A 32Mm Vila | Ferramentas | 2 | 37,6% | 1 | R$ 99,73 |  |
| 18 | 20608 | Rebolo Desbaste Diamantado 4.1/2 115Mm M14 Turbo Vila | Ferramentas | 2 | 36,3% | 3 | R$ 97,44 |  |
| 19 | 20457 | Tomada Sobrepor Externo 1 Tomada 10A Branco Margirius | Elétrica | 3 | 35,8% | 8 | R$ 95,04 |  |
| 20 | 23451 | Sapato Monodensidade S/Bico Cano Baixo N°41 | Hidráulica | 1 | 40,1% | 3 | R$ 94,32 |  |
| 21 | 23450 | Sapato Monodensidade S/Bico Cano Baixo N°40 | Hidráulica | 1 | 40,1% | 3 | R$ 94,32 |  |
| 22 | 20590 | Ducha Eletronica Ballerina 3 Temp. 5350W 220V Zagonei | Hidráulica | 1 | 42,8% | 2 | R$ 87,00 |  |
| 23 | 22583 | Torneira De Boia P/Cx Dagua Alta Vazao 1/2 E 3/4" Cipla | Hidráulica | 2 | 43,3% | 2 | R$ 85,02 | ⚠ provisório |
| 24 | 20776 | Curva Esg 90° Curta Dn 100 | Hidráulica | 3 | 10,4% | 4 | R$ 81,20 |  |
| 25 | 21694 | Tomada Sobrepor Externo 2 Tomada 10A Branco Margirius | Elétrica | 1 | 36,0% | 5 | R$ 76,75 |  |
| 26 | 21990 | Oculos Boxer Ambar Vonder | EPI/segurança | 3 | 41,6% | 13 | R$ 75,94 |  |
| 27 | 20570 | Resistencia Ducha Moment Zagonel | Hidráulica | 2 | 36,8% | 3 | R$ 75,71 |  |
| 28 | 23454 | Sapato Monodensidade S/Bico N°39 | Não classificado | 1 | 38,6% | 2 | R$ 71,14 |  |
| 29 | 1043 | Broca Encaixe Sds Plus8X210Mm Blister Vila - | Ferramentas | 2 | 32,9% | 7 | R$ 70,25 |  |
| 30 | 5943 | Tanque Plastico Branco 26L C/ Valvula Fiberblu | Hidráulica | 1 | 35,0% | 1 | R$ 61,71 | ⚠ provisório |
| 31 | 1428 | Reducao Excentr Esg Sn 75X50 Fortlev | Hidráulica | 2 | 27,4% | 14 | R$ 61,01 |  |
| 32 | 21488 | Manta Liquida Laje Top Galao 4Kg Dryko | Básico | 2 | 37,8% | 1 | R$ 60,95 |  |
| 33 | 1624 | Fita Isolante Autofusao 05M X 19Mm Preta Foxlux | Elétrica | 3 | 34,4% | 5 | R$ 58,70 | ⚠ provisório |
| 34 | 1658 | Oculos Boxer Incolor Vonder | EPI/segurança | 2 | 41,6% | 9 | R$ 52,58 |  |
| 35 | 17401 | Caixa P/Hidrometro Padrao Samae Blumenau/Brusque 9806 | Hidráulica | 1 | 44,1% | 1 | R$ 50,27 |  |
| 36 | 22544 | Valvula Click Lavatorio 7/8 Corpo Abs Tampa C/ Acabamento Inox Padova | Hidráulica | 1 | 37,1% | 3 | R$ 50,01 |  |
| 37 | 1661 | Pa Ajuntar Quadrada Com Cabo Y Vila (Montada) | Não classificado | 2 | 40,2% | 2 | R$ 49,62 |  |
| 38 | 22801 | Esmalte Agua Multiplas Superficies Luckscolor Branco 0,9L | Não classificado | 1 | 35,3% | 1 | R$ 48,55 |  |
| 39 | 20404 | Assento Sanitario Universal Branco Herc - Tampa Envolvente | Hidráulica | 1 | 36,3% | 2 | R$ 47,74 |  |
| 40 | 21704 | Bucha Red Roscavel 3/4X1/2 Fortlev | Hidráulica | 1 | 34,8% | 49 | R$ 47,58 |  |
| 41 | 20286 | Desempenadeira Aco Dentada 48 X 12Cm Dente 10 X 10Mm Dimaestro | Ferramentas | 2 | 40,9% | 2 | R$ 47,30 |  |
| 42 | 22557 | Cadeado 35 Mm - Encartelado | Básico | 1 | 40,2% | 3 | R$ 44,85 |  |
| 43 | 20616 | Chave Grifo 18 Vila | Ferramentas | 1 | 35,9% | 1 | R$ 44,80 |  |
| 44 | 1169 | Gancho Com Bucha 10 | Básico | 2 | 42,2% | 100 | R$ 39,90 |  |
| 45 | 20511 | Fita Crepe Uso Geral 48Mmx50M Atlas | Pintura | 2 | 36,9% | 4 | R$ 39,12 |  |
| 46 | 20870 | Registro Maquina De Lavar Maruja Branco Viqua | Hidráulica | 1 | 38,7% | 3 | R$ 34,95 |  |
| 47 | 22931 | Disco Flap Curvo G40 115X22,2Mm Metal | Não classificado | 2 | 39,3% | 8 | R$ 33,04 |  |
| 48 | 21395 | Engate Flexivel Inox 60Cm 1/2" Fertak | Hidráulica | 1 | 42,4% | 2 | R$ 29,96 |  |
| 49 | 377 | Cadeado 20 Mm - Encartelado | Básico | 1 | 41,1% | 3 | R$ 29,85 |  |
| 50 | 22925 | Disco Flap Curv G120 115X22,2Mm Metal | Não classificado | 3 | 39,3% | 7 | R$ 29,75 |  |
| 51 | 1527 | Cap Esg Sn Dn 40 Fortlev | Hidráulica | 3 | 37,7% | 16 | R$ 28,91 |  |
| 52 | 1983 | Durepoxi 50G | Não classificado | 2 | 40,6% | 5 | R$ 28,20 |  |
| 53 | 875 | Pu 40 Cinza 80G Unipega | Não classificado | 1 | 43,4% | 5 | R$ 28,00 |  |
| 54 | 22108 | Chave Grifo 12 Vila - | Ferramentas | 1 | 43,6% | 1 | R$ 24,52 |  |
| 55 | 21163 | Massa Corrida Pva 900Ml Qualyvinil | Pintura | 1 | 40,3% | 2 | R$ 21,50 |  |
| 56 | 22582 | Kit Acessorios Banheiro Basico 5Pç Cromado Bella Arte | Acabamento | 3 | 35,8% | 1 | R$ 19,24 |  |
| 57 | 1210 | Prego Aco Com Cabeca 16X24 | Básico | 3 | 42,2% | 2 | R$ 19,07 |  |
| 58 | 1458 | Curva Esg 90° Curta  Sn Dn 40 Fortlev | Hidráulica | 2 | -67,0% | 3 | R$ 18,30 |  |
| 59 | 20731 | Trena Emborrachada 05M X 19Mm Thompson | Ferramentas | 2 | 39,7% | 2 | R$ 17,48 |  |
| 60 | 1609 | Desempenadeira C/Eva Grande 17X30Cm Roma | Ferramentas | 2 | 38,4% | 1 | R$ 16,95 |  |
| 61 | 21876 | Guarda Chuva Sombrinha Preta Mor | Bazar/diversos | 1 | 38,6% | 1 | R$ 15,66 |  |
| 62 | 22957 | Facao 20 Cabo Pvc 50Cm Fertak | Hidráulica | 1 | 42,8% | 1 | R$ 15,44 |  |
| 63 | 1603 | Colher Pedreiro 08 Redonda | Ferramentas | 3 | 38,2% | 2 | R$ 15,15 |  |
| 64 | 21211 | Limpa Obra 1,0L | Não classificado | 2 | 42,2% | 1 | R$ 12,71 |  |
| 65 | 22953 | Desempenadeira Denta Cb Plastico 25,5X12Cm Cabo Plastico | Ferramentas | 2 | 43,2% | 1 | R$ 11,88 |  |
| 66 | 21480 | Plugue Femea 2P 10A 250V Branco | Elétrica | 2 | 43,1% | 4 | R$ 11,36 |  |
| 67 | 2004 | Nivelador Piso Fit 2Mm Branco Moldimplas | Acabamento | 1 | 38,4% | 1 | R$ 7,95 |  |
| 68 | 20395 | Nivelador Piso Fit 3Mm Vermelho Moldimplas | Acabamento | 1 | 38,4% | 1 | R$ 7,95 |  |
| 69 | 20804 | Adaptador Soldavel P/Cx Dagua  32Mmx1" - Flange | Hidráulica | 2 | 41,8% | 1 | R$ 5,77 |  |
| 70 | 20814 | Disco Debaste 4. 1/2 115X6, 4X22, 2 Vila | Ferramentas | 1 | 42,0% | 1 | R$ 3,77 |  |

---
## 4. Estoque parado completo

Os 148 SKUs sem nenhuma venda registrada na Curva ABC recebida, valor parado total R$ 6.293,29. Ordenado por antiguidade da última compra (mais antigo primeiro), não por valor; itens sem data preenchida ficam ao final.

| # | Código | Produto | Categoria | Últ. compra | Estoque | Valor parado | Faixa (+1 fornec.) |
|---|---|---|---|---|---|---|---|
| 1 | 22930 | Desempenadeira Plast Dent 12X26 Monoblo | Ferramentas | 22/12/2025 | 1 | R$ 10,99 |  |
| 2 | 22950 | Jogo Brocas Chatas 7 Pcs 1/4-1" | Não classificado | 22/12/2025 | 1 | R$ 31,43 |  |
| 3 | 22917 | Pulverizador Plast Costal Manual 20L. | Não classificado | 22/12/2025 | 1 | R$ 141,47 |  |
| 4 | 22933 | Jogo Broca Bits 110Pcs | Ferramentas | 22/12/2025 | 1 | R$ 155,00 |  |
| 5 | 22920 | Disco Diamantado Porc Cer 110X20Mm | Ferramentas | 22/12/2025 | 1 | R$ 13,91 |  |
| 6 | 22934 | Serrote Prof Poda Cb Plast 350Mm | Ferramentas | 22/12/2025 | 1 | R$ 32,39 |  |
| 7 | 22949 | Jogo Serras Copo Bimetal 7 Pcs | Não classificado | 22/12/2025 | 1 | R$ 93,71 |  |
| 8 | 22935 | Jogo Brocas/Talhadei Sds Plus 13 Pecas | Não classificado | 22/12/2025 | 1 | R$ 157,16 |  |
| 9 | 22937 | Lixador Manual P/ Meia Lixa | Pintura | 22/12/2025 | 1 | R$ 19,95 |  |
| 10 | 22948 | Piscina Fast Set 1000L | Não classificado | 22/12/2025 | 1 | R$ 157,18 |  |
| 11 | 22938 | Lixa Massa Madeira Gr60 225X275 | Pintura | 22/12/2025 | 25 | R$ 11,25 |  |
| 12 | 22941 | Mascara Desc Valv P2 Po/Fumos 126 | EPI/segurança | 22/12/2025 | 1 | R$ 1,43 |  |
| 13 | 22942 | Jogo Brocas 16 Pecas | Não classificado | 22/12/2025 | 1 | R$ 62,02 |  |
| 14 | 22921 | Disco Diamantado Turbo 125X22,2Mm | Ferramentas | 22/12/2025 | 1 | R$ 17,41 |  |
| 15 | 22929 | Jogo Brocas Combinada 9 Pecas | Não classificado | 22/12/2025 | 1 | R$ 19,89 |  |
| 16 | 22928 | Arco Serra Regulavel 12" Reforcado. | Ferramentas | 22/12/2025 | 1 | R$ 33,79 |  |
| 17 | 22923 | Tesoura Aviacao 10" Esquerda | Não classificado | 22/12/2025 | 3 | R$ 73,80 |  |
| 18 | 365726 | Disco Diamantado Turbo 110X20Mm | Ferramentas | 22/12/2025 | 1 | R$ 12,88 |  |
| 19 | 22927 | Disco Diamantado Segmentado 230X25,4 | Ferramentas | 22/12/2025 | 1 | R$ 53,50 |  |
| 20 | 22960 | Jogo Broca Tipo Sds Plus 4Pcs | Ferramentas | 22/12/2025 | 1 | R$ 26,82 |  |
| 21 | 22958 | Fita Zebrada Am/Pr Adesiva 48Mmx30M | Não classificado | 22/12/2025 | 1 | R$ 12,55 |  |
| 22 | 22955 | Piscina Fast Set 2,300L | Não classificado | 22/12/2025 | 1 | R$ 241,33 |  |
| 23 | 22926 | Protetor Auditivo Tipo Concha Wk60Plus. | EPI/segurança | 22/12/2025 | 1 | R$ 27,37 |  |
| 24 | 22943 | Cilindro Gas Mapp Pro 400Gr | Não classificado | 29/01/2026 | 2 | R$ 37,42 | R$ 37,42 a R$ 86,42 |
| 25 | 22829 | Junção 100 X 150 | Não classificado | 29/01/2026 | 3 | R$ 39,77 |  |
| 26 | 506709 | Ventilador Parede Vop Premium 60Cm Preto Bivolt | Elétrica | 13/03/2026 | 2 | R$ 399,96 |  |
| 27 | 25739 | Adesivo Estrutural Tecbond Mf 01,0Kg | Não classificado | 13/03/2026 | 1 | R$ 39,97 |  |
| 28 | 382 | Cadeado 50 Mm - Encartelado | Básico | 25/03/2026 | 2 | R$ 61,20 |  |
| 29 | 383 | Cadeado 30 Mm Haste  Longa - Encartelado | Básico | 25/03/2026 | 2 | R$ 37,80 |  |
| 30 | 384 | Cadeado 35 Mm Haste  Longa - Encartelado | Básico | 25/03/2026 | 2 | R$ 39,00 |  |
| 31 | 22558 | Cadeado 40 Mm - Encartelado | Básico | 25/03/2026 | 2 | R$ 39,60 |  |
| 32 | 21638 | Cacamba Pintura 10L Gerplast | Não classificado | 31/03/2026 | 2 | R$ 15,44 |  |
| 33 | 10100 | Torneira Esfera Jardim Zamac P Cadeado Flux | Hidráulica | 02/04/2026 | 3 | R$ 85,50 |  |
| 34 | 2000 | Nivelador Piso Fit 1Mm Verde Moldimplas | Acabamento | 15/04/2026 | 2 | R$ 15,90 |  |
| 35 | 1659 | Oculos Handex Alfa Cinza | EPI/segurança | 15/04/2026 | 9 | R$ 36,81 |  |
| 36 | PRD00044 | Ferro 1/2 (12 Metros) 12,5Mm | Básico | 23/04/2026 | 1 | R$ 63,90 |  |
| 37 | 1604 | Colher Pedreiro 10 Redonda | Ferramentas | 24/04/2026 | 3 | R$ 27,48 |  |
| 38 | 20950 | Caixa De Correio Uniforme | Não classificado | 24/04/2026 | 2 | R$ 39,18 |  |
| 39 | 20514 | Resistencia 3 Temp Tipo Lorenzetti 220V 5500W Ultra | Não classificado | 24/04/2026 | 1 | R$ 18,52 |  |
| 40 | 21073 | Manta Bidim (M) | Não classificado | 05/05/2026 | 8 | R$ 55,60 |  |
| 41 | 22932 | Fita Dupla Face 25Mmx2M Externo | Não classificado | 12/05/2026 | 4 | R$ 14,80 | R$ 14,80 a R$ 29,20 |
| 42 | 20719 | Interruptor Sobrepor Simples 6A 250V Retangular | Elétrica | 12/05/2026 | 5 | R$ 20,95 |  |
| 43 | 21421 | Resistencia Aquecedor Versatil 3T 220V 6400W Pratimix | Não classificado | 14/05/2026 | 1 | R$ 16,39 |  |
| 44 | 21369 | Resistencia Ballerina/Coroninha 3S 220V 5400W Pratimix | Não classificado | 03/06/2026 | 3 | R$ 38,19 |  |
| 45 | 20480 | Parafuso Drywall Forro 4,2 X 13Mm | Básico | 03/06/2026 | 500 | R$ 19,49 |  |
| 46 | 22371 | Chave Boca / Fixa 12X13Mm Aco Carbono | Ferramentas | 12/06/2026 | 2 | R$ 9,76 |  |
| 47 | 20824 | Prolongador P/Torneira Curto 1/2 Longa 30Mm Zamak Garden | Hidráulica | 12/06/2026 | 2 | R$ 8,24 |  |
| 48 | 21428 | Aditivo Impermeabilizante 3,6L Vedacit | Pintura | 12/06/2026 | 1 | R$ 39,68 |  |
| 49 | 22014 | Bota Pvc N.42 C./Medio C/Forro Innpro | Hidráulica | 18/06/2026 | 1 | R$ 33,68 |  |
| 50 | 1416 | Cap Esg Sn Dn 100 Fortlev | Hidráulica | 22/06/2026 | 10 | R$ 48,17 |  |
| 51 | 21581 | Registro Esfera Sold 32Mm Fortlev | Hidráulica | 22/06/2026 | 9 | R$ 101,75 |  |
| 52 | 22056 | Cap Roscavel Branco 1/2 Cipla | Hidráulica | 26/06/2026 | 3 | R$ 3,45 |  |
| 53 | 20302 | Disjuntor Monopolar Shb 32A - Soprano | Elétrica | 26/06/2026 | 3 | R$ 16,38 |  |
| 54 | 21833 | Cap Roscavel Branco 3/4 Cipla | Hidráulica | 26/06/2026 | 3 | R$ 4,08 |  |
| 55 | 21818 | Bucha Gesso Drywall 06/30Mm N1 Broca 10 | Ferramentas | 26/06/2026 | 100 | R$ 12,52 |  |
| 56 | 1660 | Pa Ajuntar Bico N4 C/ Cabo 1,20 Vila | Não classificado | 26/06/2026 | 1 | R$ 33,11 |  |
| 57 | 22844 | Disjuntor Monopolar Shb 16A - Soprano | Elétrica | 26/06/2026 | 3 | R$ 16,38 |  |
| 58 | 20702 | Cabo Flexivel Corfio 4,0Mm 750V Preto | Elétrica | 26/06/2026 | 100 | R$ 348,96 |  |
| 59 | 20301 | Disjuntor Monopolar Shb 25A- Soprano | Elétrica | 26/06/2026 | 3 | R$ 16,38 |  |
| 60 | 20810 | Botina Tp092 Com Bico N42 Bidensidade Nobuck Cafe Com Cadarco Cartom - | EPI/segurança | 26/06/2026 | 1 | R$ 69,98 |  |
| 61 | 20679 | Painel Led 24W Quadrado Sobrepor 6500K Bivolt Rajix | Elétrica | 02/07/2026 | 2 | R$ 51,05 |  |
| 62 | 22159 | Refletor Led 30W Bivolt 6500K Preto Rajix | Elétrica | 02/07/2026 | 2 | R$ 28,15 |  |
| 63 | 22472 | Lampada Geladeira/ Micro 15W X 220V Brasfort | Elétrica | 03/07/2026 | 2 | R$ 7,18 |  |
| 64 | 20895 | Parafuso Chip 4,5X40 Amarelo | Básico | 03/07/2026 | 500 | R$ 37,98 |  |
| 65 | 1243 | Silicone Acetico Incolor 50G Bisnaga | Não classificado | 03/07/2026 | 2 | R$ 9,29 |  |
| 66 | 20257 | Massa Epoxi 50 Gr Tekbond | Não classificado | 03/07/2026 | 3 | R$ 12,20 |  |
| 67 | 20943 | Chave Teste 3 X 140Mm - 100V A 250V Fertak | Ferramentas | 03/07/2026 | 12 | R$ 23,99 |  |
| 68 | 1646 | Cabo Marreta Momfort | Ferramentas | 10/07/2026 | 1 | R$ 5,96 |  |
| 69 | 20381 | Parafuso Ponta Broca 12 - 5,5Mm X 2 Sext (Chave 5/16) C/ Arruela Vila | Ferramentas | 10/07/2026 | 100 | R$ 21,39 |  |
| 70 | 21902 | Sobrepor Simples Interruptor C/ Placa Ilumi | Elétrica | 10/07/2026 | 5 | R$ 21,90 |  |
| 71 | 20591 | Ducha Lorenzetti Comfort 220V 7500W | Hidráulica | 13/07/2026 | 2 | R$ 182,16 |  |
| 72 | 22348 | Chave Combinada 12Mm | Ferramentas | 27/07/2026 | 1 | R$ 0,00 |  |
| 73 | 22351 | Chave Combinada 14Mm | Ferramentas | 27/07/2026 | 1 | R$ 0,00 |  |
| 74 | 1444 | Luva De Correr Esgoto Dn 40 Krona | Hidráulica | 27/07/2026 | 10 | R$ 0,00 |  |
| 75 | 20773 | Chave Combinada 13Mm | Ferramentas | 27/07/2026 | 1 | R$ 0,00 |  |
| 76 | 22354 | Chave Combinada 15Mm | Ferramentas | 27/07/2026 | 1 | R$ 0,00 |  |
| 77 | 1821 | Martelo Cabo Fibra 29Mm Fertak | Ferramentas | 29/07/2026 | 1 | R$ 28,27 |  |
| 78 | 1896 | Mangueira Nivel Cristal 5/16X1,3Mm - Metro | Hidráulica | 29/07/2026 | 100 | R$ 137,40 |  |
| 79 | 22308 | Extensao Connect 3 Tom. 2P+T 10M Fiolux | Não classificado | 29/07/2026 | 1 | R$ 47,94 |  |
| 80 | 22310 | Ferro Solda 40W 220V Brasfort | Básico | 29/07/2026 | 1 | R$ 23,53 |  |
| 81 | 926 | Lona Polietileno Laranja 2X2M | Não classificado | 29/07/2026 | 1 | R$ 10,97 |  |
| 82 | 929 | Lona Polietileno Laranja 4X3M Nove54 | Não classificado | 29/07/2026 | 1 | R$ 32,90 |  |
| 83 | 22016 | Capa Chuva Motoqueiro Pvc Tornado | EPI/segurança | 29/07/2026 | 1 | R$ 41,00 |  |
| 84 | 21992 | Oculos Fume Deltaplus | EPI/segurança | 29/07/2026 | 5 | R$ 15,76 |  |
| 85 | 20866 | Filtro De Linha 2T+3T Espacadas 2P+T 10A 1M Fiolux | Não classificado | 29/07/2026 | 1 | R$ 24,19 |  |
| 86 | 22876 | Cola Plastica 400G Anjo Classe | Não classificado | 29/07/2026 | 1 | R$ 14,23 |  |
| 87 | 21991 | Oculos Amarelo Deltaplus | EPI/segurança | 29/07/2026 | 5 | R$ 15,76 |  |
| 88 | 20663 | Fechadura  Pali Cromada Interna Soprano | Acabamento | 05/08/2026 | 2 | R$ 83,97 |  |
| 89 | 20662 | Fechadura  Pali Cromada Externa Soprano | Acabamento | 05/08/2026 | 2 | R$ 115,82 |  |
| 90 | 22068 | Cruzeta / Espacador 5,00Mm C/100 | Básico | 05/08/2026 | 3 | R$ 5,22 | R$ 5,22 a R$ 5,28 |
| 91 | 22250 | Cruzeta / Espacador 4,00Mm C/100 | Básico | 05/08/2026 | 2 | R$ 3,48 |  |
| 92 | 1578 | Ancinho Metal 12 Dentes Com Cabo De Madeira 1,20M Max | Básico | 11/08/2026 | 1 | R$ 11,84 |  |
| 93 | 24621 | Soquete C/Rabicho Preto 43.01T Foxlux - 43.01T | Elétrica | 24/08/2026 | 6 | R$ 8,94 |  |
| 94 | 22044 | Borracha Liquida Spray Preta 400Ml 240G Chemicolor | Não classificado | 24/08/2026 | 2 | R$ 43,92 |  |
| 95 | 20996 | Facao 16 Cabo Pvc 40Cm Fertak | Hidráulica | 24/08/2026 | 1 | R$ 14,30 |  |
| 96 | 1628 | Jogo Chave Torx T9 A T40 8 Pçs Blister Vila | Ferramentas | 24/08/2026 | 2 | R$ 36,63 |  |
| 97 | 1715 | Botina Sem Bico Monodensidade Cano Medio N. 43 | EPI/segurança | 24/08/2026 | 1 | R$ 28,03 |  |
| 98 | 21553 | Jogo Chave Torx T10 A T40 7 Pçs Blister Vila | Ferramentas | 24/08/2026 | 2 | R$ 29,31 |  |
| 99 | 21241 | Lixa Ferro Gr100 225X275 | Pintura | 24/08/2026 | 25 | R$ 48,11 |  |
| 100 | 21540 | Lixa Ferro Gr180 225X275 | Pintura | 24/08/2026 | 25 | R$ 48,11 |  |
| 101 | 20674 | Sapato Monodensidade S/Bico Cano Baixo N°43 | Hidráulica | 24/08/2026 | 2 | R$ 62,88 | R$ 62,88 a R$ 62,88 |
| 102 | 22401 | Botina Sem Bico Monodensidade Cano Medio N. 40 | EPI/segurança | 24/08/2026 | 1 | R$ 28,03 |  |
| 103 | 20247 | Verniz Maritimo 0,9L Alessi | Pintura | 24/08/2026 | 2 | R$ 54,25 |  |
| 104 | 20335 | Espude Pvc Branca Fortlev | Hidráulica | 24/08/2026 | 3 | R$ 7,83 |  |
| 105 | 21141 | Mangueira Incolor/Cristal Nivel Silicone 5/16X1,30Mm 10M Unifortte | Hidráulica | 27/08/2026 | 2 | R$ 0,00 |  |
| 106 | 21152 | Trena Emborrachada 10M X 25Mm Thompson | Ferramentas | 27/08/2026 | 2 | R$ 41,54 | R$ 0,00 a R$ 41,54 |
| 107 | 22922 | Desempenadeira Lisa Cb Plastico 12X25,5Cm | Ferramentas | 27/08/2026 | 2 | R$ 34,84 | R$ 26,42 a R$ 34,84 |
| 108 | 22102 | Parafuso P/ Vaso Bognar Latonado B-10 80Mm | Básico | 27/08/2026 | 2 | R$ 7,25 |  |
| 109 | 22682 | Registro De Esfera Maquina De Lavar 1/2"X3/4" Fertak | Hidráulica | 27/08/2026 | 4 | R$ 43,32 | R$ 43,32 a R$ 57,65 |
| 110 | 22045 | Haste Adaptadora P/ Mandril Com Encaixe Sds Plus Cortag | Hidráulica | 27/08/2026 | 2 | R$ 16,75 |  |
| 111 | 1010020 | Becker Prego 16X24 1Kg | Básico | 01/09/2026 | 2 | R$ 24,98 |  |
| 112 | 22402 | Calçado Botina Nobunk N. 40 Cafe | EPI/segurança | 01/09/2026 | 1 | R$ 91,26 |  |
| 113 | 20653 | Fita Crepe Azul Pintura Imob. 24Mmx50M | Pintura | 01/09/2026 | 4 | R$ 57,60 |  |
| 114 | 22399 | Calçado Botina Nobunk N. 38 Cafe | EPI/segurança | 01/09/2026 | 1 | R$ 91,26 |  |
| 115 | 22396 | Calçado Botina Nobunk N. 44 Cafe | EPI/segurança | 01/09/2026 | 1 | R$ 91,26 |  |
| 116 | 21145 | Pilha Alcalina Aaa C/02 Und Eletronic | Elétrica | 01/09/2026 | 7 | R$ 17,60 | R$ 17,60 a R$ 32,90 |
| 117 | 1018 | Broca Ar 05.0Mm Blister | Ferramentas | 01/09/2026 | 3 | R$ 5,21 |  |
| 118 | 21014 | Fita Crepe Azul Pintura Imob. 18Mmx50M Adere | Pintura | 01/09/2026 | 2 | R$ 20,02 |  |
| 119 | 1012 | Broca Ar 02.0Mm Blister | Ferramentas | 01/09/2026 | 3 | R$ 2,59 |  |
| 120 | 1966 | Vassoura Nylon Plastica C/ Cabo Angular | Não classificado | 08/09/2026 | 1 | R$ 14,50 |  |
| 121 | 1608 | Desempenadeira Plastica C/ Borracha 17X30 Vila | Ferramentas | 08/09/2026 | 2 | R$ 27,06 |  |
| 122 | 20357 | Valvula Click 1.1/4" Corpo Plastico Tampa Inox | Hidráulica | 08/09/2026 | 3 | R$ 0,00 | R$ 0,00 a R$ 53,72 |
| 123 | 20684 | Caixa Descarga Branca Alumasa | Não classificado | 08/09/2026 | 2 | R$ 60,30 |  |
| 124 | 20692 | Registro Pressao (Chuveiro) Base 3/4 Docol | Hidráulica | 08/09/2026 | 2 | R$ 67,70 |  |
| 125 | 20775 | Acabamento Para Registro Abs Branco 1/2-3/4-1 Deca E Decol Blukit | Hidráulica | 08/09/2026 | 2 | R$ 34,70 |  |
| 126 | 20813 | Desempenadeira Plastica C/ Borracha 14X27 Vila | Ferramentas | 08/09/2026 | 2 | R$ 22,04 |  |
| 127 | 20885 | Registro Gaveta Docol 3/4 | Hidráulica | 08/09/2026 | 2 | R$ 67,70 |  |
| 128 | 21844 | Vassoura Nylon Plastica C/ Cabo Novica | Não classificado | 08/09/2026 | 2 | R$ 20,22 |  |
| 129 | 1041 | Broca Encaixe Sds Plus8X110Mm Blister Vila - | Ferramentas | 08/09/2026 | 11 | R$ 90,95 |  |
| 130 | 20474 | Assento Sanitario Almofadado Branco Herc | Hidráulica | 08/09/2026 | 2 | R$ 77,80 |  |
| 131 | 1040 | Broca Encaixe Sds Plus7X210Mm Blister Vila - | Ferramentas | 09/09/2026 | 15 | R$ 130,50 |  |
| 132 | 1038 | Broca Encaixe Sds Plus7X110Mm Blister Vila - | Ferramentas | 09/09/2026 | 15 | R$ 109,68 |  |
| 133 | 22215 | Kit Acessorios Banheiro 5Pç Cromado Bella Arte | Acabamento | 11/09/2026 | 1 | R$ 24,47 |  |
| 134 | 22087 | Abracadeira Borboleta 27Mm Metalmatrix | Básico | 11/09/2026 | 10 | R$ 29,56 |  |
| 135 | 22083 | Kit Acessorios Banheiro Basico 5Pç Branco Bella Arte | Acabamento | 11/09/2026 | 1 | R$ 18,27 |  |
| 136 | 22760 | Convertedor Ferrugem Tf7 200Ml | Não classificado | 11/09/2026 | 2 | R$ 18,42 |  |
| 137 | 21552 | Desengraxante 500 Ml Multiuso Spray - H7 Tf7 | Básico | 11/09/2026 | 2 | R$ 112,04 |  |
| 138 | 21292 | Kit Acessorios Banheiro Basico 5Pç Preto Bella Arte | Acabamento | 11/09/2026 | 1 | R$ 18,27 |  |
| 139 | 20685 | Desempenadeira Plastica Estriada 17X30 Gerplast | Ferramentas | 11/09/2026 | 3 | R$ 17,40 |  |
| 140 | 1856 | Estilete 9Mm Hobby Plastico Vila | Ferramentas | 11/09/2026 | 30 | R$ 29,75 |  |
| 141 | 1045 | Broca Encaixe Sds Plus 10X210Mm Blister Vila - | Ferramentas | sem data | 3 | R$ 0,00 |  |
| 142 | 1136 | Tinta Spray Chemicolor Uso Geral 400Ml Verde Escuro - 680087 | Pintura | sem data | 5 | R$ 0,00 |  |
| 143 | 1546 | Elemento Filtrante 9.3/4 Fortlev | Não classificado | sem data | 4 | R$ 0,00 |  |
| 144 | 1575 | Te Sold Bch Latao 20X1/2 Fortlev | Não classificado | sem data | 17 | R$ 0,00 |  |
| 145 | 1577 | Te Sold Bch Latao 25X3/4 Fortlev | Não classificado | sem data | 12 | R$ 0,00 |  |
| 146 | 20397 | Caixaria Mista Pinus | Não classificado | sem data | 2 | R$ 0,00 |  |
| 147 | 21988 | Alic P/Aneis Jg C/4Pc 7"  Vonder | Ferramentas | sem data | 1 | R$ 0,00 |  |
| 148 | 22202 | Pulverizador   750Ml Pu750 Vonder | Não classificado | sem data | 3 | R$ 0,00 |  |

---
## 5. Top produtos em estoque por valor

**Top 20, bruto** (inclui os itens com outlier de cadastro, sinalizados):

| # | Código | Produto | Categoria | Valor em estoque | Outlier cadastro? | Faixa (+1 fornec.) |
|---|---|---|---|---|---|---|
| 1 | 22483 | Bucha Plastica C/ Anel Concreto 8Mm | Básico | R$ 5.377,50 | SIM |  |
| 2 | PRD00045 | Cimento Supremo 50Kg | Básico | R$ 3.135,00 | não | R$ 3.135,00 a R$ 3.505,50 |
| 3 | PRD00016 | Estribo Flexfer 10X16 4,2Mm | Básico | R$ 2.520,00 | SIM |  |
| 4 | 20250 | Tijolo 6 Furos 09 X 14 X 29 Cer. Lorenzetti | Básico | R$ 1.883,03 | não | R$ 1.883,03 a R$ 2.779,86 |
| 5 | 22114 | Tijolo 6 Furos 09 X 14 X 24 Cer. Lorenzetti | Básico | R$ 1.508,40 | não | R$ 1.508,40 a R$ 2.436,07 |
| 6 | 16420 | Corante Base Dagua 50Ml Xadrez Preto | Pintura | R$ 1.200,48 | SIM |  |
| 7 | 1592 | Bucha Plastica Tijolo Oco 10Mm (500) Branca Ufu Usaf | Básico | R$ 752,45 | SIM |  |
| 8 | 21452 | Tubo Esgoto 100Mm - 6M | Hidráulica | R$ 709,43 | não | R$ 707,02 a R$ 719,90 |
| 9 | 1581 | Serra Arco 12.24 Flexivel Starrett | Ferramentas | R$ 554,34 | SIM |  |
| 10 | 20708 | Po De Brita 5M³ | Básico | R$ 534,40 | SIM |  |
| 11 | 22445 | Argamassa Extrakolla 2 Cinza 20Kg | Básico | R$ 507,00 | não |  |
| 12 | 22446 | Argamassa Superkola 3Mais Cinza 20Kg | Básico | R$ 415,68 | não |  |
| 13 | 506709 | Ventilador Parede Vop Premium 60Cm Preto Bivolt | Elétrica | R$ 399,96 | não |  |
| 14 | 101010 | Ferro 3/8 (12 Metros) 10Mm | Básico | R$ 386,10 | não |  |
| 15 | 20702 | Cabo Flexivel Corfio 4,0Mm 750V Preto | Elétrica | R$ 348,96 | não |  |
| 16 | 21449 | Tubo Esgoto 40Mm - 6M | Hidráulica | R$ 325,63 | não |  |
| 17 | 21451 | Tubo Esgoto 75Mm - 6M | Hidráulica | R$ 317,87 | não |  |
| 18 | 22468 | Lona Preta 4X100 75 Micros | Não classificado | R$ 317,30 | não |  |
| 19 | 22646 | Tubo Esgoto 150Mm - 6M | Hidráulica | R$ 308,67 | não |  |
| 20 | 20912 | Ferro 5/16 (12 Metros) 8Mm | Básico | R$ 298,00 | não | R$ 298,00 a R$ 339,50 |

**Top 15, sem outliers de cadastro** (base recomendada para decisão):

| # | Código | Produto | Categoria | Valor em estoque | Faixa (+1 fornec.) |
|---|---|---|---|---|---|
| 1 | PRD00045 | Cimento Supremo 50Kg | Básico | R$ 3.135,00 | R$ 3.135,00 a R$ 3.505,50 |
| 2 | 20250 | Tijolo 6 Furos 09 X 14 X 29 Cer. Lorenzetti | Básico | R$ 1.883,03 | R$ 1.883,03 a R$ 2.779,86 |
| 3 | 22114 | Tijolo 6 Furos 09 X 14 X 24 Cer. Lorenzetti | Básico | R$ 1.508,40 | R$ 1.508,40 a R$ 2.436,07 |
| 4 | 21452 | Tubo Esgoto 100Mm - 6M | Hidráulica | R$ 709,43 | R$ 707,02 a R$ 719,90 |
| 5 | 22445 | Argamassa Extrakolla 2 Cinza 20Kg | Básico | R$ 507,00 |  |
| 6 | 22446 | Argamassa Superkola 3Mais Cinza 20Kg | Básico | R$ 415,68 |  |
| 7 | 506709 | Ventilador Parede Vop Premium 60Cm Preto Bivolt | Elétrica | R$ 399,96 |  |
| 8 | 101010 | Ferro 3/8 (12 Metros) 10Mm | Básico | R$ 386,10 |  |
| 9 | 20702 | Cabo Flexivel Corfio 4,0Mm 750V Preto | Elétrica | R$ 348,96 |  |
| 10 | 21449 | Tubo Esgoto 40Mm - 6M | Hidráulica | R$ 325,63 |  |
| 11 | 21451 | Tubo Esgoto 75Mm - 6M | Hidráulica | R$ 317,87 |  |
| 12 | 22468 | Lona Preta 4X100 75 Micros | Não classificado | R$ 317,30 |  |
| 13 | 22646 | Tubo Esgoto 150Mm - 6M | Hidráulica | R$ 308,67 |  |
| 14 | 20912 | Ferro 5/16 (12 Metros) 8Mm | Básico | R$ 298,00 | R$ 298,00 a R$ 339,50 |
| 15 | 21450 | Tubo Esgoto 50Mm - 6M | Hidráulica | R$ 291,00 |  |

---
## 6. Maiores quantidades em estoque

Top 20 produtos por unidades físicas em estoque, independente do valor.

| # | Código | Produto | Categoria | Estoque (un.) | Valor em estoque |
|---|---|---|---|---|---|
| 1 | 20250 | Tijolo 6 Furos 09 X 14 X 29 Cer. Lorenzetti | Básico | 2.598 | R$ 1.883,03 |
| 2 | 22114 | Tijolo 6 Furos 09 X 14 X 24 Cer. Lorenzetti | Básico | 2.514 | R$ 1.508,40 |
| 3 | 22553 | Parafuso Chipboard Ch Ph 4,0 X 50Mm | Básico | 1.504 | R$ 114,24 |
| 4 | 1592 | Bucha Plastica Tijolo Oco 10Mm (500) Branca Ufu Usaf | Básico | 1.414 | R$ 752,45 |
| 5 | 22294 | Bucha 06 | Básico | 910 | R$ 12,93 |
| 6 | 20480 | Parafuso Drywall Forro 4,2 X 13Mm | Básico | 500 | R$ 19,49 |
| 7 | 20895 | Parafuso Chip 4,5X40 Amarelo | Básico | 500 | R$ 37,98 |
| 8 | 20374 | Parafuso Chip 5,0X40 Amarelo | Básico | 486 | R$ 46,85 |
| 9 | 22483 | Bucha Plastica C/ Anel Concreto 8Mm | Básico | 478 | R$ 5.377,50 |
| 10 | 22748 | Parafuso Chip 4,5X45 Amarelo | Básico | 300 | R$ 28,78 |
| 11 | 22101 | Parafuso Ponta Broca 12 - 5,5Mmx1 Sext (Chave 5/16) C/Arruela Auto Brocante Vila - | Ferramentas | 257 | R$ 34,12 |
| 12 | 20361 | Cabo Cci 2 Vias | Elétrica | 180 | R$ 81,93 |
| 13 | 1332 | Par Chip Ch Ph 4.0X40 Bc Ph2 Multifix | Básico | 168 | R$ 0,00 |
| 14 | 1503 | Luva Soldavel 20Mm Fortlev | Hidráulica | 159 | R$ 65,19 |
| 15 | 22482 | Estribo De Aco 07 X 17Cm | Básico | 150 | R$ 58,19 |
| 16 | 21229 | Parafuso Telheiro P Fixar 5/16X110 | Básico | 130 | R$ 55,77 |
| 17 | 20473 | Abracadeira Tipo U B 3/4 25Mm Inca Zincada Inca | Básico | 128 | R$ 40,33 |
| 18 | 21427 | Parafuso Chip 5,0X60 Amarelo | Básico | 121 | R$ 15,72 |
| 19 | PRD00017 | Estribo De Aco 07 X 14Cm | Básico | 119 | R$ 41,04 |
| 20 | 21818 | Bucha Gesso Drywall 06/30Mm N1 Broca 10 | Ferramentas | 100 | R$ 12,52 |

---
## 7. Auditoria de cadastro completa

Os 49 SKUs com custo cadastrado fora do padrão (16 com custo acima do preço de venda, 33 com custo zerado). Custo estimado é benchmark por mediana de comparável interno, nunca substitui o dado real.

| Código | Produto | Tipo de outlier | Custo cadastrado | Preço venda | Estoque | Custo estimado (comparável) |
|---|---|---|---|---|---|---|
| 20708 | Po De Brita 5M³ | Custo > preço | R$ 133,60 | R$ 0,00 | 4 | sem comparável |
| 1016 | Broca Ar 04.0Mm Blister C/10 Din 338 Vila - | Custo > preço | R$ 15,72 | R$ 7,50 | 11 | R$ 0,97 |
| 1592 | Bucha Plastica Tijolo Oco 10Mm (500) Branca Ufu Usaf | Custo > preço | R$ 0,53 | R$ 0,30 | 1.414 | sem comparável |
| 22483 | Bucha Plastica C/ Anel Concreto 8Mm | Custo > preço | R$ 11,25 | R$ 0,05 | 478 | sem comparável |
| 4436 | Cabo De Aco Plastificado 3/32" 2,40Mm | Custo > preço | R$ 2,48 | R$ 2,00 | 100 | sem comparável |
| 1516 | Caixa De Luz Octogonal 4X4 Fortlev | Custo > preço | R$ 14,25 | R$ 4,10 | 10 | R$ 1,21 |
| 21344 | Coluna Armada 8Mm 7X14X6M | Custo > preço | R$ 139,90 | R$ 130,50 | 2 | sem comparável |
| 16420 | Corante Base Dagua 50Ml Xadrez Preto | Custo > preço | R$ 50,02 | R$ 7,50 | 24 | sem comparável |
| 20659 | Corante Base Dagua 50Ml Xadrez Vermelho | Custo > preço | R$ 21,50 | R$ 7,50 | 5 | sem comparável |
| 1458 | Curva Esg 90° Curta  Sn Dn 40 Fortlev | Custo > preço | R$ 6,10 | R$ 3,65 | 3 | R$ 17,63 |
| 22922 | Desempenadeira Lisa Cb Plastico 12X25,5Cm | Custo > preço | R$ 17,42 | R$ 16,50 | 2 | sem comparável |
| 21552 | Desengraxante 500 Ml Multiuso Spray - H7 Tf7 | Custo > preço | R$ 56,02 | R$ 43,80 | 2 | sem comparável |
| 21809 | Estribo De Aço 20 X 9 | Custo > preço | R$ 1,64 | R$ 1,30 | 80 | sem comparável |
| PRD00016 | Estribo Flexfer 10X16 4,2Mm | Custo > preço | R$ 60,00 | R$ 1,20 | 42 | sem comparável |
| 1581 | Serra Arco 12.24 Flexivel Starrett | Custo > preço | R$ 92,39 | R$ 14,25 | 6 | sem comparável |
| 21603 | Telha Cerâmica Esmaltada | Custo > preço | R$ 8,00 | R$ 1,60 | 0 | sem comparável |
| 1142 | Abracadeira Rsf-M C 1/2X3/4 C/100 13X19Mm 9Mm Inca | Custo zerado | R$ 0,00 | R$ 1,85 | 71 | sem comparável |
| 1143 | Abracadeira Rsf-M C 1/2X5/8 C/100 13X16Mm 9Mm Inca | Custo zerado | R$ 0,00 | R$ 1,85 | 35 | sem comparável |
| 21988 | Alic P/Aneis Jg C/4Pc 7"  Vonder | Custo zerado | R$ 0,00 | R$ 194,00 | 1 | sem comparável |
| 1579 | Aplicador De Silicone E Pu Profissional 9" Fertak | Custo zerado | R$ 0,00 | R$ 25,00 | 2 | sem comparável |
| 1021 | Broca Ar 06.5Mm Blister C/10 Din 338 Vila - | Custo zerado | R$ 0,00 | R$ 6,15 | 8 | R$ 0,97 |
| 1044 | Broca Encaixe Sds Plus 10X160Mm Blister Vila - | Custo zerado | R$ 0,00 | R$ 14,20 | 3 | R$ 8,25 |
| 1045 | Broca Encaixe Sds Plus 10X210Mm Blister Vila - | Custo zerado | R$ 0,00 | R$ 16,10 | 3 | R$ 8,25 |
| 1068 | Broxa Atlas 15X6Cm Media 800/1 - 800/1 | Custo zerado | R$ 0,00 | R$ 11,31 | 3 | sem comparável |
| 20397 | Caixaria Mista Pinus | Custo zerado | R$ 0,00 | R$ 21,90 | 2 | sem comparável |
| 22348 | Chave Combinada 12Mm | Custo zerado | R$ 0,00 | R$ 8,90 | 1 | sem comparável |
| 22351 | Chave Combinada 14Mm | Custo zerado | R$ 0,00 | R$ 10,25 | 1 | sem comparável |
| 20773 | Chave Combinada 13Mm | Custo zerado | R$ 0,00 | R$ 9,50 | 1 | sem comparável |
| 22354 | Chave Combinada 15Mm | Custo zerado | R$ 0,00 | R$ 12,00 | 1 | sem comparável |
| 21571 | Colete Refletivo "Xg" Amarelo 10.01.2.3 | Custo zerado | R$ 0,00 | R$ 29,00 | 4 | sem comparável |
| 20803 | Convertedor Ferrugem Tf7 100Ml | Custo zerado | R$ 0,00 | R$ 9,50 | 2 | R$ 9,21 |
| 22862 | Disco Corte Diamantado Segmentado 110Mm Fertak | Custo zerado | R$ 0,00 | R$ 14,00 | 8 | R$ 1,02 |
| 1546 | Elemento Filtrante 9.3/4 Fortlev | Custo zerado | R$ 0,00 | R$ 41,25 | 4 | sem comparável |
| 1997 | Escora De Eucalipto | Custo zerado | R$ 0,00 | R$ 22,00 | 3 | sem comparável |
| 21476 | Espatula Rejunte Colorida Borracha | Custo zerado | R$ 0,00 | R$ 2,50 | 9 | sem comparável |
| 1909 | Fita Asfaltica 20Cm - Venda Por Metro | Custo zerado | R$ 0,00 | R$ 6,50 | 10 | R$ 27,31 |
| 949 | Fita Crepe Uso Geral Bege Euro 18Mm X 50M | Custo zerado | R$ 0,00 | R$ 5,50 | 3 | R$ 10,01 |
| 1444 | Luva De Correr Esgoto Dn 40 Krona | Custo zerado | R$ 0,00 | R$ 13,90 | 10 | R$ 5,32 |
| 1447 | Luva Esg Sn Dn 50 Fortlev | Custo zerado | R$ 0,00 | R$ 2,70 | 15 | R$ 3,44 |
| 1574 | Luva Sold Bch Latao 25X3/4 Fortlev | Custo zerado | R$ 0,00 | R$ 4,95 | 16 | sem comparável |
| 21141 | Mangueira Incolor/Cristal Nivel Silicone 5/16X1,30Mm 10M Unifortte | Custo zerado | R$ 0,00 | R$ 24,90 | 2 | sem comparável |
| 22111 | Mangueira Saida Maquina Lavar | Custo zerado | R$ 0,00 | R$ 12,00 | 3 | sem comparável |
| 1332 | Par Chip Ch Ph 4.0X40 Bc Ph2 Multifix | Custo zerado | R$ 0,00 | R$ 0,20 | 168 | sem comparável |
| 22202 | Pulverizador   750Ml Pu750 Vonder | Custo zerado | R$ 0,00 | R$ 16,90 | 3 | sem comparável |
| 1575 | Te Sold Bch Latao 20X1/2 Fortlev | Custo zerado | R$ 0,00 | R$ 6,40 | 17 | sem comparável |
| 1577 | Te Sold Bch Latao 25X3/4 Fortlev | Custo zerado | R$ 0,00 | R$ 8,40 | 12 | sem comparável |
| 1136 | Tinta Spray Chemicolor Uso Geral 400Ml Verde Escuro - 680087 | Custo zerado | R$ 0,00 | R$ 21,90 | 5 | R$ 11,71 |
| 20357 | Valvula Click 1.1/4" Corpo Plastico Tampa Inox | Custo zerado | R$ 0,00 | R$ 25,90 | 3 | R$ 16,67 |
| 22580 | Valvula Lavatorio S/Lad S/Unho 7/8" Plastico | Custo zerado | R$ 0,00 | R$ 10,00 | 2 | R$ 11,98 |

---
## 8. Sensibilidade de custo por fornecedor

Os 86 SKUs comprados de mais de um fornecedor a custos diferentes, ordenados pela maior diferença de valor em estoque entre o custo usado (compra mais recente) e o custo máximo já pago. Diferença agregada: R$ 4.964,48.

| Código | Produto | Fornecedores | Estoque | Valor (custo usado) | Valor (custo máx.) | Diferença |
|---|---|---|---|---|---|---|
| 22924 | Parafuso Ponta Broca 12 - 5,5Mm X 1/2 Sext (Chave 5/16) C/ Arruela Vila | 2 | 100 | R$ 24,62 | R$ 1.360,00 | R$ 1.335,38 |
| 22114 | Tijolo 6 Furos 09 X 14 X 24 Cer. Lorenzetti | 4 | 2.514 | R$ 1.508,40 | R$ 2.436,07 | R$ 927,67 |
| 20250 | Tijolo 6 Furos 09 X 14 X 29 Cer. Lorenzetti | 2 | 2.598 | R$ 1.883,03 | R$ 2.779,86 | R$ 896,83 |
| 4436 | Cabo De Aco Plastificado 3/32" 2,40Mm | 3 | 100 | R$ 247,93 | R$ 700,00 | R$ 452,07 |
| PRD00045 | Cimento Supremo 50Kg | 2 | 95 | R$ 3.135,00 | R$ 3.505,50 | R$ 370,50 |
| 21571 | Colete Refletivo "Xg" Amarelo 10.01.2.3 | 2 | 4 | R$ 0,00 | R$ 78,49 | R$ 78,49 |
| PRD00017 | Estribo De Aco 07 X 14Cm | 2 | 119 | R$ 41,04 | R$ 113,94 | R$ 72,91 |
| 20530 | Massa Polimérica 5Kg | 2 | 12 | R$ 187,20 | R$ 258,00 | R$ 70,80 |
| 12010 | Argamassa Massa Reboco Cinza 20Kg | 2 | 9 | R$ 85,70 | R$ 149,31 | R$ 63,61 |
| 20357 | Valvula Click 1.1/4" Corpo Plastico Tampa Inox | 2 | 3 | R$ 0,00 | R$ 53,72 | R$ 53,72 |
| 22582 | Kit Acessorios Banheiro Basico 5Pç Cromado Bella Arte | 2 | 1 | R$ 19,24 | R$ 69,99 | R$ 50,75 |
| 22943 | Cilindro Gas Mapp Pro 400Gr | 2 | 2 | R$ 37,42 | R$ 86,42 | R$ 49,00 |
| 1579 | Aplicador De Silicone E Pu Profissional 9" Fertak | 2 | 2 | R$ 0,00 | R$ 48,66 | R$ 48,66 |
| 20336 | Concreto Pronto 20Kg | 2 | 9 | R$ 107,91 | R$ 155,61 | R$ 47,70 |
| 20912 | Ferro 5/16 (12 Metros) 8Mm | 2 | 10 | R$ 298,00 | R$ 339,50 | R$ 41,50 |
| 1997 | Escora De Eucalipto | 2 | 3 | R$ 0,00 | R$ 36,00 | R$ 36,00 |
| 20608 | Rebolo Desbaste Diamantado 4.1/2 115Mm M14 Turbo Vila | 2 | 3 | R$ 97,44 | R$ 131,52 | R$ 34,08 |
| 21588 | Fita Dupla Face 12Mmx2Mt | 2 | 1 | R$ 3,70 | R$ 32,80 | R$ 29,10 |
| 1490 | Curva Soldavel 90° 32Mm Fortlev | 2 | 7 | R$ 37,32 | R$ 62,79 | R$ 25,47 |
| 1904 | Caixa Gordura 42L C/Cesto Limpeza | 2 | 1 | R$ 27,50 | R$ 51,90 | R$ 24,40 |
| 22957 | Facao 20 Cabo Pvc 50Cm Fertak | 2 | 1 | R$ 15,44 | R$ 34,21 | R$ 18,77 |
| 38087 | Fita Veda Rosca 18Mmx10M Qualiflon | 2 | 18 | R$ 18,68 | R$ 36,72 | R$ 18,04 |
| 21503 | Valvula Pia Inox 3.1/2 C/Pino Tampa Inos Padova | 2 | 2 | R$ 12,32 | R$ 28,90 | R$ 16,58 |
| 21486 | Mangueira Entrada Maquina 1,20M | 2 | 2 | R$ 21,53 | R$ 37,82 | R$ 16,29 |
| 21145 | Pilha Alcalina Aaa C/02 Und Eletronic | 2 | 7 | R$ 17,60 | R$ 32,90 | R$ 15,30 |
| 22932 | Fita Dupla Face 25Mmx2M Externo | 2 | 4 | R$ 14,80 | R$ 29,20 | R$ 14,40 |
| 22682 | Registro De Esfera Maquina De Lavar 1/2"X3/4" Fertak | 2 | 4 | R$ 43,32 | R$ 57,65 | R$ 14,33 |
| 23451 | Sapato Monodensidade S/Bico Cano Baixo N°41 | 3 | 3 | R$ 94,32 | R$ 106,71 | R$ 12,39 |
| 23450 | Sapato Monodensidade S/Bico Cano Baixo N°40 | 3 | 3 | R$ 94,32 | R$ 106,71 | R$ 12,39 |
| 20803 | Convertedor Ferrugem Tf7 100Ml | 2 | 2 | R$ 0,00 | R$ 11,69 | R$ 11,69 |
| 949 | Fita Crepe Uso Geral Bege Euro 18Mm X 50M | 2 | 3 | R$ 0,00 | R$ 11,10 | R$ 11,10 |
| 21452 | Tubo Esgoto 100Mm - 6M | 3 | 12 | R$ 709,43 | R$ 719,90 | R$ 10,48 |
| 20352 | Calkor 1L  (Cal Liquido) | 2 | 5 | R$ 28,10 | R$ 38,35 | R$ 10,25 |
| 22580 | Valvula Lavatorio S/Lad S/Unho 7/8" Plastico | 2 | 2 | R$ 0,00 | R$ 9,94 | R$ 9,94 |
| 20718 | Espuma Expansiva 500Ml 320G Tekbond | 2 | 10 | R$ 135,21 | R$ 144,90 | R$ 9,69 |
| 20990 | Arame Recozido N 18 | 2 | 9 | R$ 71,10 | R$ 80,75 | R$ 9,65 |
| 1611 | Desempenadeira Plastica Estriada 14X27 Gerplast | 2 | 3 | R$ 13,77 | R$ 21,75 | R$ 7,98 |
| 22043 | Pilha Alcalina Aa C/02 Und Eletronic | 2 | 5 | R$ 15,76 | R$ 23,50 | R$ 7,74 |
| 21454 | Tubo Soldavel 25Mm - 6M | 5 | 5 | R$ 77,14 | R$ 82,52 | R$ 5,38 |
| 23452 | Sapato Monodensidade S/Bico Cano Baixo N°42 | 3 | 1 | R$ 31,44 | R$ 35,57 | R$ 4,13 |
| 21501 | Joelho 90 Esgoto 40Mm Fortlev | 2 | 26 | R$ 20,63 | R$ 23,92 | R$ 3,29 |
| 1110 | Rolo La S/ Respingo 09Cm Com Cabo Roma | 3 | 5 | R$ 23,36 | R$ 26,25 | R$ 2,89 |
| 1182 | Disco Serra/Madeira Circular Videa 7. 1/4 24D X 185Mm | 2 | 1 | R$ 14,91 | R$ 17,68 | R$ 2,76 |
| 22687 | Abracadeira Borboleta 16Mm Metalmatrix | 2 | 10 | R$ 29,56 | R$ 32,10 | R$ 2,54 |
| 21453 | Tubo Soldavel 20Mm - 6M | 2 | 6 | R$ 78,05 | R$ 80,31 | R$ 2,26 |
| 22953 | Desempenadeira Denta Cb Plastico 25,5X12Cm Cabo Plastico | 2 | 1 | R$ 11,88 | R$ 13,21 | R$ 1,34 |
| 1983 | Durepoxi 50G | 2 | 5 | R$ 28,20 | R$ 29,28 | R$ 1,08 |
| 14283 | Abracadeira Tipo U 3/4 Branca Click | 2 | 50 | R$ 27,00 | R$ 27,90 | R$ 0,90 |
| 1603 | Colher Pedreiro 08 Redonda | 2 | 2 | R$ 15,15 | R$ 15,98 | R$ 0,83 |
| 20665 | Fita Dupla Face 12Mm X 2M Vila | 2 | 3 | R$ 10,33 | R$ 11,10 | R$ 0,77 |
| 1851 | Sifao Tubo Extensivel Branco 72Cm Plasbohn | 2 | 2 | R$ 7,94 | R$ 8,38 | R$ 0,44 |
| 22060 | Cruzeta / Espacador 3,00Mm C/100 | 2 | 2 | R$ 3,40 | R$ 3,52 | R$ 0,12 |
| 22068 | Cruzeta / Espacador 5,00Mm C/100 | 2 | 3 | R$ 5,22 | R$ 5,28 | R$ 0,06 |
| 21940 | Cruzeta / Espacador 2,00Mm C/100 | 2 | 2 | R$ 3,48 | R$ 3,52 | R$ 0,04 |
| 1677 | Torneira Jardim Preto | 2 | 11 | R$ 25,58 | R$ 25,58 | R$ 0,00 |
| 1624 | Fita Isolante Autofusao 05M X 19Mm Preta Foxlux | 2 | 5 | R$ 58,70 | R$ 58,70 | R$ 0,00 |
| 1891 | Caixa Medidor Provisoria Preta | 3 | 1 | R$ 48,93 | R$ 48,93 | R$ 0,00 |
| 1446 | Luva Esg Sn Dn 75 Fortlev | 2 | 13 | R$ 44,66 | R$ 44,66 | R$ 0,00 |
| 12345 | Pu 40 Cinza 380G Orbi Quimica | 2 | 8 | R$ 66,83 | R$ 66,83 | R$ 0,00 |
| 1468 | Adaptador Sold Cx Dagua 25X3/4 | 2 | 23 | R$ 116,52 | R$ 116,52 | R$ 0,00 |
| 1211 | Prego Polido 17X27 1Kg Cabeca Dupla Gerdau - 117000253 | 2 | 3 | R$ 36,57 | R$ 36,57 | R$ 0,00 |
| 1212 | Prego Polido 17X27 1Kg Com Cabeca | 3 | 10 | R$ 104,40 | R$ 104,40 | R$ 0,00 |
| 1201 | Manta Termica Simples 1 Face 1,20M - Metro | 2 | 20 | R$ 65,04 | R$ 65,04 | R$ 0,00 |
| 20452 | Rolo La S/Respingo S/Cabo 23Cm Roma | 2 | 4 | R$ 29,68 | R$ 29,68 | R$ 0,00 |
| 20596 | Haste P/Chuveiro Branca 1/2" 30Cm Herc | 2 | 3 | R$ 16,76 | R$ 16,76 | R$ 0,00 |
| 21435 | Fita Crepe Amarela 18X40 Automotiva | 3 | 7 | R$ 36,47 | R$ 36,47 | R$ 0,00 |
| 21152 | Trena Emborrachada 10M X 25Mm Thompson | 2 | 2 | R$ 41,54 | R$ 41,54 | R$ 0,00 |
| 20674 | Sapato Monodensidade S/Bico Cano Baixo N°43 | 2 | 2 | R$ 62,88 | R$ 62,88 | R$ 0,00 |
| 20734 | Torneira Jardim Megajato 1/2" Amarela  - Metro | 2 | 93 | R$ 190,27 | R$ 190,27 | R$ 0,00 |
| 20962 | Protetor Auditivo/Auricular C/ Cordao | 2 | 4 | R$ 11,16 | R$ 11,16 | R$ 0,00 |
| 21989 | Oculos Boxer Verde Vonder | 2 | 12 | R$ 70,10 | R$ 70,10 | R$ 0,00 |
| 21665 | Joelho Esgoto 90.X100Mm 0619 | 2 | 1 | R$ 5,79 | R$ 5,79 | R$ 0,00 |
| 21582 | Abracadeira Nylon Preta 4,8 X 370 - 100Pçs Vila | 2 | 4 | R$ 53,91 | R$ 53,91 | R$ 0,00 |
| 22922 | Desempenadeira Lisa Cb Plastico 12X25,5Cm | 2 | 2 | R$ 34,84 | R$ 34,84 | R$ 0,00 |
| 22146 | Trincha Branca "396" 3.0"  396/7 | 2 | 6 | R$ 73,86 | R$ 73,86 | R$ 0,00 |
| 22144 | Trincha Branca "396" 1.1/2"  396/4 | 2 | 5 | R$ 24,75 | R$ 24,75 | R$ 0,00 |
| 22461 | Canaleta Adesiva Com Divisoria 20X10X2000Mm Branca | 2 | 54 | R$ 237,38 | R$ 237,38 | R$ 0,00 |
| 22583 | Torneira De Boia P/Cx Dagua Alta Vazao 1/2 E 3/4" Cipla | 2 | 2 | R$ 85,02 | R$ 85,02 | R$ 0,00 |
| 22686 | Carrinho De Carga 45 L Minasul | 2 | 3 | R$ 278,58 | R$ 278,58 | R$ 0,00 |
| 31329 | Bloco Espuma Multiuso Amarelo | 2 | 3 | R$ 6,99 | R$ 6,99 | R$ 0,00 |
| 22956 | Lixa Ferro Gr80 225X275 | 2 | 29 | R$ 60,49 | R$ 60,49 | R$ 0,00 |
| 23454 | Sapato Monodensidade S/Bico N°39 | 2 | 2 | R$ 71,14 | R$ 71,14 | R$ 0,00 |
| 815 | Plug Pino Macho 2P+T 10A/250V | 2 | 3 | R$ 15,89 | R$ 15,89 | R$ 0,00 |
| 643882 | Lixa Massa Madeira Gr80 225X275 | 2 | 66 | R$ 48,13 | R$ 48,13 | R$ 0,00 |
| 5943 | Tanque Plastico Branco 26L C/ Valvula Fiberblu | 2 | 1 | R$ 61,71 | R$ 61,71 | R$ 0,00 |
| PRD00065 | Pu 40 Branco 380G | 2 | 19 | R$ 175,07 | R$ 175,07 | R$ 0,00 |
---

## 9. Outliers excluídos

Nenhum destes itens foi apagado do relatório de origem, só tratado fora do cálculo principal quando distorceria a leitura. A lista completa dos 49 SKUs de cadastro está na seção 7 acima; aqui o destaque é o porquê de cada tipo de exclusão.

### 9.1 Dois lançamentos "Plataforma" — excluídos do faturamento "sem outliers"

| Item | Faturamento | Motivo da exclusão |
|---|---|---|
| Plataforma -Z-45/25J RT | R$ 133.748,71 | Código fora do padrão do catálogo, aparece uma única vez, sem como confirmar pela planilha se é venda de equipamento, aluguel registrado como venda ou erro de lançamento |
| 114887 - Plataforma - Z-3422 DC | R$ 95.674,30 | Mesmo motivo |

Juntos somam R$ 229.423,01, quase 44% do faturamento bruto total (R$ 521.254,92). Toda a Curva ABC, a participação por categoria e a margem por categoria deste relatório usam a base sem esses dois lançamentos (R$ 291.831,91). **Pendente de confirmação do cliente antes de qualquer decisão de mídia por categoria.**

### 9.2 16 SKUs com custo cadastrado acima do preço de venda — excluídos do "top valor em estoque sem outliers" e tratados com margem não confiável

Lista completa na seção 7 (tipo "Custo > preço"). Motivo geral: indica erro de cadastro (unidade de compra diferente da unidade de venda, custo de lote lançado como custo unitário, ou preço de venda desatualizado), não necessariamente prejuízo real na venda. Os 3 que mais distorciam rankings antes da correção: Bucha plástica c/ anel concreto 8mm (código 22483, inflava o top valor em estoque em R$ 5.377,50), Estribo Flexfer (PRD00016, R$ 2.520,00) e Corante base d'água (16420, R$ 1.200,48).

### 9.3 33 SKUs com custo cadastrado zerado — excluídos do cálculo de margem por categoria e da matriz giro x margem

Lista completa na seção 7 (tipo "Custo zerado"). Custo zero impede calcular margem real. Esses itens foram tratados como "margem indefinida", nunca como 0% nem como 100%, e não entraram nas médias ponderadas por categoria nem na classificação de quadrante da matriz giro x margem quando cruzados com a Curva ABC.

### Nota à parte: 86 SKUs com mais de um fornecedor não são outliers, são ambiguidade legítima

Diferente dos itens acima, os 86 SKUs comprados de mais de um fornecedor (lista completa na seção 8) não foram excluídos de nada. Cada custo cadastrado é real, só existe mais de um. Por isso não entram nesta lista de outliers: aparecem com a faixa mínimo-máximo lado a lado nas tabelas em que a margem influencia a leitura, para decisão em reunião com o cliente, e não como erro de cadastro.

### Nota sobre o total de estoque (dúvida do cliente, 18/09/2026)

R$ 40.661,03 é o valor total em estoque a custo, agrupando por produto (443 SKUs únicos). Somar custo × estoque direto nas 543 linhas válidas do relatório bruto "Produtos por Fornecedor" (sem remover as 101 linhas duplicadas dos 86 SKUs multi-fornecedor) resulta em R$ 62.301,85, um valor inflado em R$ 21.640,82: a mesma quantidade física em estoque é contada mais de uma vez para cada produto com mais de uma linha de fornecedor, porque a coluna "Estoque Disponível" repete o total atual em cada linha, não divide por fornecedor. R$ 40.661,03 é o número correto.

---

**Arquivos de referência completos:**
- `outputs/_diagnosticos/inteligencia-dados/diagnostico-curva-abc.md`
- `outputs/_diagnosticos/inteligencia-dados/diagnostico-giro-estoque.md`
- `outputs/09-2026/Arquivos/15-inteligencia-dados-curva-abc-padronizada_acumulado-ate-2026-09-15.xlsx`
- `outputs/09-2026/Arquivos/15-inteligencia-dados-estoque-giro-margem_snapshot-2026-09-15.xlsx`

---

✓ Humanizer aplicado · 10 padrões anti-cara-de-IA verificados

*Pillar · Marketing com Resultado Concreto*
