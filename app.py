from flask import Flask, render_template, request, redirect, url_for, session
import random
import math
import os
import inimigos

app = Flask(__name__)
app.secret_key = os.urandom(24)

limitesPorNivel = {1: 5, 2: 8, 3: 10, 4: 14, 5: 16, 6: 18}
multiplicadoresVida = {1: 1, 2: 1.2, 3: 1.3, 4: 1.4, 5: 1.5, 6: 1.7}

def sorteadorTipoInimigo():
    return random.choice(inimigos.inimigos)

def gerarInimigosLogica(nivel):
    nome, vidaMax, esquivaMax, elemento, rank, danoTexto = sorteadorTipoInimigo()
    vidaMax = math.ceil(vidaMax * multiplicadoresVida.get(nivel, 1))
    quantidadeMax = limitesPorNivel.get(nivel, 5)
    quantidade = random.randint(1, quantidadeMax)

    listaInimigos = []
    for i in range(quantidade):
        vida = random.randint(1, vidaMax)
        esquiva = random.randint(1, esquivaMax)
        listaInimigos.append({
            "nome": nome,
            "vida": vida,
            "esquiva": esquiva,
            "elemento": elemento,
            "rank": rank,
            "dano": danoTexto,
            "numero": i + 1
        })
    return listaInimigos

@app.route('/')
def index():
    if 'nivelGlobal' not in session:
        session['nivelGlobal'] = 6
    if 'listaInimigos' not in session:
        session['listaInimigos'] = gerarInimigosLogica(session['nivelGlobal'])
        
    return render_template('index.html', 
                           inimigos=session['listaInimigos'], 
                           nivelGlobal=session['nivelGlobal'],
                           limitesPorNivel=limitesPorNivel)

@app.route('/gerar', methods=['POST'])
def gerar():
    nivel = int(request.form.get('nivel', 6))
    session['nivelGlobal'] = nivel

    session['listaInimigos'] = gerarInimigosLogica(nivel)
    return redirect(url_for('index'))

@app.route('/dano/<int:inimigoIdx>', methods=['POST'])
def aplicarDano(inimigoIdx):
    try:
        dano = int(request.form.get('dano', 0))
    except ValueError:
        dano = 0

    lista = session.get('listaInimigos', [])

    if 0 <= inimigoIdx < len(lista):
        if lista[inimigoIdx]["vida"] > 0:
            lista[inimigoIdx]["vida"] -= dano
            if lista[inimigoIdx]["vida"] < 0:
                lista[inimigoIdx]["vida"] = 0

        session['listaInimigos'] = lista

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)