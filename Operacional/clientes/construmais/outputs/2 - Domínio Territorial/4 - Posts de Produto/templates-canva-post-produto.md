# Templates Canva — Post de Produto (Construmais)

Arquivo único do Canva com 10 templates de post de produto, um por página, seguindo a identidade visual da Construmais (vermelho `#EE2526`, amarelo `#F4D000`, laranja pontual `#F7941D`, tipografia condensada bold, tom próximo e comercial).

**Link do arquivo (10 páginas):** https://www.canva.com/d/sC8vEcjUnzKDmnZ

## Páginas

1. **Produto em Destaque** — selo circular com categoria/nome/medida, mesmo espírito do [template-tem-na-construmais.html](template-tem-na-construmais.html)
2. **Promoção / Preço** — bloco "de/por" com preço em destaque
3. **Novidade / Chegou** — anúncio de produto novo no mix
4. **Comunicado / Aviso Importante** — faixas diagonais amarelas, estilo sinalização de obra, para avisos (reposição de estoque, mudança de horário etc.)
5. **Kit / Combo de Produtos** — 2–3 produtos lado a lado com preço do kit (Pilar 3)
6. **Dica Educativa** — "Você sabia?" vinculado ao uso do produto
7. **Últimas Unidades / Estoque Limitado** — urgência de loja física
8. **Linha Completa de Categoria** — mosaico de produtos da mesma categoria (elétrica, hidráulica, pintura etc.)
9. **Prova Social** — depoimento real de cliente vinculado a um produto
10. **Sazonal / Data Comemorativa** — moldura temática genérica para datas (Dia dos Pais, Dia do Construtor etc.)

## Pendências e ressalvas

- **Sem Brand Kit do Canva:** a conta Canva conectada não tem um Brand Kit cadastrado para a Construmais (nem para a Pillar). As cores e o tom foram aplicados manualmente em cada geração, a partir do brand kit documentado no `CLIENTE.md`, não vinculados a um Brand Kit formal do Canva.
- **Sem logo/mascote reais:** os arquivos `marca/logo-construmais.png` e `marca/mascote-construmais.png` são locais e a ferramenta de upload do Canva só aceita URLs já públicas. Todas as 10 páginas usam um retângulo pontilhado com o texto `[LOGO CONSTRUMAIS]` no lugar do logo real. Antes de usar os templates em produção, alguém precisa inserir o logo real manualmente no Canva (upload direto na interface) e, se for repetir em todas as páginas, considerar transformar o arquivo em Brand Template do Canva.
- **Textos são placeholders**, seguindo o mesmo padrão do template HTML (`[NOME DO PRODUTO]`, `[CATEGORIA]`, `[PREÇO]`, `[WHATSAPP]`, `[ENDEREÇO]` etc.) — precisam ser substituídos por dado real de cada post antes de publicar.
- Cada página foi escolhida como a 1ª opção entre 4 candidatos gerados pela IA do Canva por template. Se alguma página não agradar visualmente, é possível gerar novas opções e trocar só aquela página no arquivo (via `merge-designs`, sem precisar refazer as outras 9).
