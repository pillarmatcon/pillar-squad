# Como Exportar o Criativo (Story + Post) em PNG

> **Para quem é:** você, depois de receber um arquivo HTML do agente 03-Design/Criativos, precisando transformar o Story e o Post em PNG individual para postar no Instagram ou subir como criativo no Meta Ads.

---

## Resposta direta

**Caminho mais simples:** Chrome DevTools → "Capture node screenshot" em `#story` e em `#post`. Sem instalar nada. 30 segundos por criativo.

**Caminho automatizado:** Script Playwright em Node.js. Roda 1 vez, gera os 2 PNGs. Bom pra produção em escala.

Os dois caminhos abaixo. Use o que cabe na sua rotina.

---

## Caminho 1: Chrome DevTools (recomendado)

Funciona em Chrome, Edge e Brave. Não funciona em Safari (DevTools não tem essa função no momento).

### Passo a passo

**1. Abrir o arquivo HTML no navegador**

- Localizar o arquivo `.html` que o agente entregou
- Botão direito → "Abrir com" → escolher Chrome, Edge ou Brave
- A página abre mostrando o Story e o Post, um abaixo do outro

**2. Abrir DevTools**

- Pressionar `F12` (ou Ctrl+Shift+I no Windows / Cmd+Option+I no Mac)
- O painel de DevTools abre na lateral direita ou inferior

**3. Selecionar o Story**

- No DevTools, na aba "Elements", clicar no ícone de seleção (canto superior esquerdo do DevTools, parece uma seta dentro de um quadrado), ou pressionar Ctrl+Shift+C (Cmd+Shift+C no Mac)
- Clicar na peça de formato vertical na página
- O DevTools destaca o `<article id="story">` no painel

**4. Capturar screenshot do Story**

- Com o `<article>` selecionado no DevTools, abrir Command Menu: Ctrl+Shift+P (Cmd+Shift+P no Mac)
- Digitar: `screenshot`
- Aparecem 4 opções. Escolher: **"Capture node screenshot"**
- O navegador baixa automaticamente um arquivo PNG do Story (1080x1920)

**5. Repetir para o Post**

- Voltar à seleção, clicar na peça de formato 4:5 (`#post`)
- Ctrl+Shift+P → "Capture node screenshot"
- O navegador baixa o PNG do Post (1080x1350)

**6. Renomear os arquivos baixados**

- Os arquivos vêm com nome genérico ("article.png", "(1).png" etc.)
- Renomear para: `cliente-data-story.png` e `cliente-data-post.png`
- Exemplo: `clinica-vital-2026-05-01-story.png`, `clinica-vital-2026-05-01-post.png`

### Tempo total

- Story + Post: cerca de 30 segundos

### Vantagens

- Zero instalação
- Funciona em qualquer máquina com Chrome
- Resolução exata (sem perda)
- Aprende em 5 minutos

### Limitações

- Manual (2 capturas, uma por formato)
- Não funciona em Safari (Apple ainda não implementou Capture node screenshot)
- Tela do computador precisa ter resolução suficiente para mostrar a peça sem corte (ideal: monitor Full HD ou maior)

---

## Caminho 2: Script Playwright (automação)

Para quem produz muitos criativos por semana. Investimento inicial de 10 minutos, depois é 1 comando por criativo.

### Pré-requisitos

- Node.js 18+ instalado ([nodejs.org](https://nodejs.org))
- Terminal aberto (Cmd na pasta do projeto Mac, PowerShell no Windows)

### Setup (1 vez)

**1. Criar pasta para o script**

```bash
mkdir export-criativo
cd export-criativo
npm init -y
npm install playwright
npx playwright install chromium
```

**2. Criar arquivo `export.js`**

```javascript
// export.js
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function exportCreative(htmlPath, outputDir) {
  const absoluteHtmlPath = path.resolve(htmlPath);
  const fileUrl = 'file://' + absoluteHtmlPath;

  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1200, height: 2000 },
    deviceScaleFactor: 2
  });
  const page = await context.newPage();

  await page.goto(fileUrl, { waitUntil: 'networkidle' });

  const formatos = [
    { selector: '#story', filename: 'story.png' },
    { selector: '#post', filename: 'post.png' }
  ];

  for (const { selector, filename } of formatos) {
    const el = await page.$(selector);
    if (!el) {
      console.error(`  ✗ Não encontrei ${selector}`);
      continue;
    }
    const outputPath = path.join(outputDir, filename);
    await el.screenshot({ path: outputPath, omitBackground: false });
    console.log(`  ✓ ${filename}`);
  }

  await browser.close();
  console.log(`\nConcluído. PNGs em ${outputDir}/`);
}

const [, htmlPath, outputDir] = process.argv;

if (!htmlPath || !outputDir) {
  console.error('Uso: node export.js <caminho.html> <pasta-saida>');
  console.error('Exemplo: node export.js criativo-clinica-vital.html ./output');
  process.exit(1);
}

exportCreative(htmlPath, outputDir);
```

**3. Rodar para o seu criativo**

```bash
node export.js ../caminho/para/criativo-clinica-vital.html ./output
```

Saída esperada:
```
  ✓ story.png
  ✓ post.png

Concluído. PNGs em ./output/
```

Os 2 PNGs aparecem na pasta `output/`, prontos para subir.

### Tempo total

- Setup inicial: 10 minutos (1 vez só, fica configurado)
- Por criativo exportado depois: 5 a 10 segundos

### Vantagens

- Automação total
- Roda no headless, sem abrir janela
- Resolução 2x (deviceScaleFactor 2), ótimo pra zoom no Instagram
- Pode rodar em CI/CD se a agência crescer

### Limitações

- Precisa Node.js instalado
- Curva de aprendizado pra quem nunca usou terminal

---

## Caminho 3: Print de tela manual (fallback)

Se nem Chrome DevTools nem Playwright funcionarem, é possível tirar print de cada peça "no olho":

### macOS

- Abrir HTML no navegador
- Cmd+Shift+5 → Captura de área
- Marcar exatamente a área da peça (1080x1920 ou 1080x1350)
- Salvar PNG

### Windows

- Abrir HTML no navegador
- Ferramenta de Captura (Snipping Tool) ou Win+Shift+S
- Marcar exatamente a área da peça
- Salvar PNG

### Limitação

- Difícil garantir as dimensões exatas (vai sair próximo, mas não exato)
- Posicionamento de zoom do navegador interfere no resultado
- **Não recomendo este caminho** a não ser como último recurso. Caminho 1 (DevTools) é tão fácil quanto e gera dimensão correta.

---

## Caminho 4: Site online de captura (alternativa)

Para quem não consegue usar Chrome DevTools nem Playwright e precisa de alternativa rápida online:

- [GoFullPage](https://gofullpage.com) (extensão Chrome): captura página inteira ou área selecionada, exporta PNG
- [Awesome Screenshot](https://www.awesomescreenshot.com) (extensão): mesmo princípio
- [Web Capture](https://web-capture.net) (web): cola URL e baixa PNG

**Limitação:** essas ferramentas geralmente capturam a página inteira (não a peça individual). Servem para validação visual rápida, não para entrega final em dimensão exata.

---

## Validação dos PNGs antes de subir

Depois de exportar, antes de mandar pro cliente ou subir no Meta Ads:

1. ✅ Story tem dimensão 1080x1920 e Post tem 1080x1350 (verificar nas propriedades do arquivo)
2. ✅ Nenhuma peça está cortada, com texto saindo da margem
3. ✅ Tipografia está legível em escala mobile (abrir o PNG em tela 100% e ver se o texto secundário ainda lê)
4. ✅ Cores batem com o briefing (sem alteração inesperada por CSS)
5. ✅ Logo do cliente está visível nas duas peças
6. ✅ Foto carregou corretamente (não tem placeholder cinza)
7. ✅ CTA está claro e legível (quando aplicável)
8. ✅ No Story, nada de headline/CTA cai nas zonas de segurança (topo/rodapé ~250px)

Se algum item falha, voltar ao HTML, ajustar e exportar de novo.

---

## Onde subir os PNGs depois

### Instagram (Stories e feed)

- Story: Instagram → câmera de Stories → selecionar da galeria → publicar
- Post: Novo post → selecionar o PNG do feed → publicar

### Anúncio Meta Ads

- Gerenciador de Anúncios → Criar anúncio
- Tipo de criativo: Imagem única
- Usar o PNG do Post para posicionamentos de feed e o do Story para posicionamentos de Stories/Reels (o Meta pede 1 arquivo por posicionamento quando a proporção muda)
- Configurar título e descrição do anúncio (a copy do agente 02-Copy serve aqui)

### Google Drive ou Notion (backup)

- Criar pasta `criativos/cliente/data/`
- Subir os PNGs para arquivar
- Útil para repetir versões depois ou prestar conta ao cliente

---

## FAQ

**O DevTools captura mais do que a peça. Como evitar?**

Garantir que está selecionando o `<article id="story">` ou `<article id="post">` exato (não o `<body>` nem um `<div>` pai). Use Ctrl+Shift+C (Cmd+Shift+C) para entrar em modo de seleção visual e clique exatamente na peça.

**O PNG está em baixa resolução. Como aumentar?**

No Chrome DevTools: clique no menu de 3 pontos → "Run command" → digite "device pixel ratio" → mude para 2. Isso gera PNG em 2x. Útil pra anúncio que vai aparecer em tela grande.

No Playwright: já está configurado com `deviceScaleFactor: 2`. Se quiser 3x, mudar para 3.

**Tem como exportar em JPEG em vez de PNG?**

Sim. No Playwright, mudar a extensão do arquivo de `.png` para `.jpg` e adicionar `quality: 90` no `screenshot({})`. JPEG é menor (mais leve no upload) mas perde qualidade visível em fundos sólidos. PNG é o padrão recomendado para Instagram.

**Preciso pedir o criativo em carrossel pra um cliente específico, dá pra exportar do mesmo jeito?**

Dá. Se o agente 03 produziu um carrossel sob pedido explícito (exceção, não o padrão da Pillar), o HTML vem com vários `<article class="card">` em sequência em vez de `#story`/`#post`. O mesmo Caminho 1 e Caminho 2 funcionam, só repetindo a captura card a card.

---

## Resumo executivo

| Caminho | Ideal para | Setup | Tempo por criativo |
|---|---|---|---|
| Chrome DevTools | Uso comum, vários criativos/semana | Zero | 30 segundos |
| Playwright | Volume alto, 10+/semana ou com equipe | 10 min (1 vez) | 5-10 segundos |
| Print de tela | Último recurso quando nada funciona | Zero | 2 minutos (e dimensão imprecisa) |
| Extensão online | Alternativa quando não tem Chrome | 30 segundos | 1-2 minutos (página toda, não a peça) |

**Padrão recomendado pelo squad:** Chrome DevTools. Funciona sem nenhum setup adicional na maioria dos casos.
