# Propostas Comerciais

> Propostas geradas pela Pillar para **prospects** (clientes em potencial), não para clientes já fechados.

Diferença para `Operacional/clientes/`: lá cada pasta é um cliente ativo com `CLIENTE.md` e identidade visual do próprio cliente. Aqui, cada pasta é um prospect e a identidade visual usada é sempre da Pillar (`_squad/_shared/identidade-agencia.md`).

## Estrutura por prospect

```
Comercial/propostas/<nome-prospect>/
├── proposta-<YYYY-MM-DD>.html
└── assets/
    └── logo-pillar.png       ← copiado de _squad/_shared/marca-pillar/logo-pillar.png
```

## Como gerar

Chame `@webdesigner` pedindo uma proposta comercial para o prospect, com: nome, diagnóstico (2 a 3 pontos reais), plano/entregas propostas, investimento e validade da proposta. O agente usa `_squad/04-webdesigner/templates-html/proposta-comercial.html` como base.

Se um prospect virar cliente fechado, a pasta dele passa a viver em `Operacional/clientes/<nome>/` seguindo o `_TEMPLATE` de lá, não aqui.
