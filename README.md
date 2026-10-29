# Nossa Hamburgueria — Cardápio online

Site de uma página só (index.html + pasta img). Cada lanche tem um número (o mesmo nome da foto em `img/`).
Ao tocar em **Pedir nº X**, o WhatsApp (21) 96605-0013 abre com a primeira mensagem já escrita:

```
*PEDIDO Nº 4 — COMBO CASAL NOSSO SMASH BACON*
R$ 68,90

Olá, Nossa Hamburgueria! Quero fazer esse pedido

https://poolmix14.github.io/hamburgueria/p/4/
```

## Publicar no GitHub Pages
1. Crie um repositório (ex.: `nossa-hamburgueria`) e envie o conteúdo desta pasta (`index.html` e `img/`).
2. No repositório: **Settings → Pages → Source: Deploy from a branch → main / (root)** → Save.
3. Em 1–2 minutos o site fica em `https://SEU-USUARIO.github.io/nossa-hamburgueria/`.

## Editar o cardápio
Tudo fica no começo do `<script>` do `index.html`:
- `WHATSAPP` — número que recebe os pedidos.
- `ABRE` / `FECHA` — horário (mostra "Aberto agora" / "Fechado").
- `ITENS` — cada lanche: `num`, `cat`, `nome`, `preco`, `img`, `desc` e `tag` (opcional: "Lançamento", "Novidade"...).
  Para um lanche novo: coloque a foto em `img/` e adicione uma linha em `ITENS`.

Link direto para um item: `.../#pedido-4`

## Miniatura da foto no WhatsApp
A pasta `p/` tem uma página por pedido (ex.: `p/7/`). O link dela vai no fim da mensagem e faz o
WhatsApp mostrar a foto do lanche ao lado do card. Depois de adicionar ou mudar um lanche em `ITENS`,
rode `python gerar-paginas.py` e suba a pasta `p/` de novo.
