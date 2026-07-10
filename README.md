# ⚔️ Sistema de Gerenciamento de Inimigos (RPG)

Este é um sistema web responsivo desenvolvido em **Python** utilizando o micro-framework **Flask**. O objetivo do projeto é servir como uma ferramenta de suporte para mestres de RPG de Mesa, permitindo a geração randômica de grupos de inimigos com base em um Nível Global, além de fornecer um painel dinâmico para rastrear atributos vitais e aplicar dano em tempo real.

O visual da aplicação adota uma estética retrô estilo *Terminal Hacker / Sci-Fi RPG*, utilizando fontes monoespaçadas, cores contrastantes (verde neon para estados ativos e vermelho para estados derrotados) e um layout totalmente centralizado e responsivo.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.x & Flask (gerenciamento de rotas, estado de sessão e lógica de dados).
* **Frontend:** HTML5 (estruturação semântica) & CSS3 (layout via Grid e Flexbox com animações).
* **Módulos Nativos:** `random` (sorteios), `math` (arredondamentos) e `os` (criptografia de sessão).

---

## 📁 Estrutura de Pastas do Projeto

Para que o Flask localize corretamente as páginas e as folhas de estilo, o projeto deve seguir rigorosamente a estrutura abaixo:

```text
meu_projeto/
│
├── app.py               # Arquivo principal do servidor Flask
├── inimigos.py          # Módulo contendo a base de dados dos monstros
├── static/
│   └── style.css        # Folha de estilo CSS (Visual do Terminal)
└── templates/
    └── index.html       # Estrutura de interface HTML da aplicação