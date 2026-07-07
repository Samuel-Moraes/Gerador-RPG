import tkinter as tk
import random
import math

# Nome | Vida Maxima | Esquiva Maxima | Elemento | Rank
inimigos = [
    ["Desertor", 6, 6, "Terra", 1],
    ["Esqueleto", 6, 6, "Terra", 1],
    ["Moglin", 12, 8, "Terra", 1],
    ["Alma Penada", 12, 8, "Terra", 1],
    ["Slime", 18, 10, "Terra", 1],
    ["Pampka", 20, 12, "Terra", 1],
]

nivelGlobal = 6

limites_por_nivel = {1: 5, 2: 8, 3: 10, 4: 14, 5: 16, 6: 20}
multiplicadores_vida = {1: 1, 2: 1.2, 3: 1.3, 4: 1.4, 5: 1.5, 6: 1.7}

def sorteadorTipoInimigo():
    return random.choice(inimigos)

nome, vida_max, esquiva_max, elemento, rank = sorteadorTipoInimigo()
vida_max = math.ceil(vida_max * multiplicadores_vida.get(nivelGlobal, 1))
quantidade_max = limites_por_nivel.get(nivelGlobal, 5)
quantidade = random.randint(1, quantidade_max)

lista_inimigos = []
for i in range(quantidade):
    vida = random.randint(1, vida_max)
    esquiva = random.randint(1, esquiva_max)
    lista_inimigos.append({
        "nome": nome,
        "vida": vida,
        "esquiva": esquiva,
        "elemento": elemento,
        "rank": rank,
        "numero": i+1  # adiciona número do inimigo
    })

root = tk.Tk()
root.title("Sistema de Inimigos")
root.configure(bg="#1e1e1e")

labels = []
entries = []

def aplicar_dano(inimigo_id):
    try:
        dano = int(entries[inimigo_id].get())
    except ValueError:
        dano = 0
    if lista_inimigos[inimigo_id]["vida"] > 0:
        lista_inimigos[inimigo_id]["vida"] -= dano
        if lista_inimigos[inimigo_id]["vida"] < 0:
            lista_inimigos[inimigo_id]["vida"] = 0

        cor_texto = "#ff0000" if lista_inimigos[inimigo_id]["vida"] == 0 else "#00ff00"

        labels[inimigo_id].config(
            text=f"--------------------\n"
                 f"- {lista_inimigos[inimigo_id]['nome']} {lista_inimigos[inimigo_id]['numero']}\n"
                 f"--------------------\n"
                 f"- Vida: {lista_inimigos[inimigo_id]['vida']}\n"
                 f"- Esquiva: {lista_inimigos[inimigo_id]['esquiva']}\n"
                 f"--------------------\n"
                 f"- Elemento: {lista_inimigos[inimigo_id]['elemento']}\n"
                 f"- Rank: {lista_inimigos[inimigo_id]['rank']}\n"
                 f"--------------------",
            fg=cor_texto
        )
        entries[inimigo_id].delete(0, tk.END)

# Cria os inimigos em grade (5 por coluna)
for idx, inimigo in enumerate(lista_inimigos):
    frame = tk.Frame(root, bg="#1e1e1e", bd=2)
    col = idx // 5
    row = idx % 5
    frame.grid(row=row, column=col, padx=10, pady=5)

    label = tk.Label(
        frame,
        text=f"--------------------\n"
             f"- {inimigo['nome']} - {inimigo['numero']}\n"
             f"--------------------\n"
             f"- Vida: {inimigo['vida']}\n"
             f"- Esquiva: {inimigo['esquiva']}\n"
             f"--------------------\n"
             f"- Elemento: {inimigo['elemento']}\n"
             f"- Rank: {inimigo['rank']}\n"
             f"--------------------",
        fg="#00ff00",
        bg="#1e1e1e",
        font=("Consolas", 10),
        justify="left"
    )
    label.pack(side="top")
    labels.append(label)

    entry = tk.Entry(frame, width=5, font=("Consolas", 10))
    entry.pack(side="left", padx=5)
    entries.append(entry)

    btn = tk.Button(frame, text="Causar Dano", command=lambda i=idx: aplicar_dano(i))
    btn.pack(side="left", padx=5)

root.mainloop()
