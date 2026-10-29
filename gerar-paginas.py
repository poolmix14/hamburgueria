# Gera as páginas p/<num>/index.html (uma por pedido) a partir da lista ITENS do index.html.
# Essas páginas existem só para o WhatsApp mostrar a miniatura da foto ao lado do link.
# Rode de novo sempre que adicionar/alterar um lanche:   python gerar-paginas.py
import re, os, html, shutil

SITE = "https://poolmix14.github.io/hamburgueria/"   # endereço do site no GitHub Pages

base = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(base, "index.html"), encoding="utf-8").read()
itens = re.findall(r'num:"([^"]+)".*?nome:"([^"]+)",\s*preco:([\d.]+),\s*img:"([^"]+)"', src, re.S)

pasta = os.path.join(base, "p")
shutil.rmtree(pasta, ignore_errors=True)

for num, nome, preco, img in itens:
    preco_br = "R$ " + f"{float(preco):.2f}".replace(".", ",")
    titulo = html.escape(f"Pedido nº {num} - {nome}")
    desc = html.escape(f"{preco_br} · Nossa Hamburgueria Artesanal")
    foto = SITE + "img/" + img
    destino = f"../../#pedido-{num}"
    d = os.path.join(pasta, num.lower())
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(f"""<!doctype html>
<html lang="pt-BR"><head>
<meta charset="utf-8">
<title>{titulo}</title>
<meta property="og:type" content="website">
<meta property="og:site_name" content="Nossa Hamburgueria">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{foto}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:url" content="{SITE}p/{num.lower()}/">
<meta http-equiv="refresh" content="0; url={destino}">
</head><body style="background:#0f0d0b;color:#f3ebdd;font-family:sans-serif">
<a href="{destino}" style="color:#f6c766">Ver no cardápio</a>
</body></html>
""")
print(len(itens), "páginas geradas em", pasta)
