from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Configurações do Banco de Dados MySQL na EC2 DB
DB_HOST = '172.31.17.240'  # IP Privado da instância do Banco
DB_USER = 'daniel'
DB_PASSWORD = 'fatecfatec'
DB_NAME = 'banco_dan'

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curiosidades')
def curiosidades():
    # Procura todos os registos da tabela mensagens_contato
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM mensagens_contato ORDER BY id DESC")
            lista_curiosidades = cursor.fetchall()
        conn.close()
    except Exception as e:
        lista_curiosidades = []
        print(f"Erro ao procurar registos: {e}")
        
    return render_template('curiosidades.html', curiosidades=lista_curiosidades)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        # Captura os dados enviados pelo formulário da web
        autor = request.form.get('autor') or request.form.get('nome')
        email = request.form.get('email')
        categoria = request.form.get('categoria')
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao') or request.form.get('mensagem')

        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                # Grava diretamente na tabela mensagens_contato existente
                sql = """
                    INSERT INTO mensagens_contato (nome, email, categoria, titulo, mensagem)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (autor, email, categoria, titulo, descricao))
            conn.close()
            print("Registo guardado com sucesso no MySQL!")
            return redirect(url_for('curiosidades'))
        except Exception as e:
            print(f"Erro ao guardar no banco de dados: {e}")
            return f"Erro ao guardar no banco de dados: {e}", 500

    return render_template('contato.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
