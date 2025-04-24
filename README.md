# 📅 Agenda Flask

Uma agenda web simples feita com **Flask + SQLite** com duas páginas:
- 👀 Visualização pública dos eventos (`/`)
- 🛠 Edição da agenda (`/edit`) com opção de adicionar e remover

## ✨ Tecnologias
- Python
- Flask
- SQLite
- HTML/CSS
- Render (Deploy)

---

## 🚀 Como rodar localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode o projeto:
```bash
python app.py
```

Acesse em [http://localhost:5000](http://localhost:5000)

---

## ☁️ Deploy no Render

1. Crie um repositório no GitHub e suba os arquivos.
2. Vá para [Render](https://render.com), crie uma conta.
3. Crie um novo Web Service:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Environment:** Python
4. Pronto! O Render cuidará do deploy e manterá seu app online.

---

## 📂 Estrutura
```
agenda/
├── app.py
├── agenda.db         # Criado automaticamente
├── templates/
│   ├── index.html
│   └── edit.html
├── static/
│   └── style.css     # (opcional para estilização)
├── requirements.txt
└── README.md
```

---

Feito por Ricardo Costa DJ 🎧
