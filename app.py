from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Inicializa o banco se não existir
def init_db():
    if not os.path.exists('agenda.db'):
        conn = sqlite3.connect('agenda.db')
        conn.execute('''
            CREATE TABLE eventos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data TEXT NOT NULL,
                hora TEXT NOT NULL,
                local TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

# Conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('agenda.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página de visualização
@app.route('/')
def index():
    conn = get_db_connection()
    eventos = conn.execute('SELECT * FROM eventos ORDER BY data, hora').fetchall()
    conn.close()
    return render_template('index.html', eventos=eventos)

# Página de edição
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    conn = get_db_connection()
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['data']
        hora = request.form['hora']
        local = request.form['local']
        conn.execute('INSERT INTO eventos (nome, data, hora, local) VALUES (?, ?, ?, ?)',
                     (nome, data, hora, local))
        conn.commit()
        return redirect('/edit')
    eventos = conn.execute('SELECT * FROM eventos ORDER BY data, hora').fetchall()
    conn.close()
    return render_template('edit.html', eventos=eventos)

# Rota para excluir evento
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM eventos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/edit')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
