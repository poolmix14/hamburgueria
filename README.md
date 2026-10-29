# Nossa Hamburgueria — Cardápio online

Site de uma página só (index.html + pasta img). Cada lanche tem um número (o mesmo nome da foto em `img/`).
Ao tocar em **Pedir nº X**, o WhatsApp (21) 96605-0013 abre com a primeira mensagem já escrita:

```
*PEDIDO Nº 4 — COMBO CASAL NOSSO SMASH BACON*
R$ 68,90

Olá, Nossa Hamburgueria! Quero fazer esse pedido 🍔

Foto: https://SEU-USUARIO.github.io/nossa-hamburgueria/img/4.jpg
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
