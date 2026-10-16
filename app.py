from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curiosidades')
def curiosidades():
    return render_template('curiosidades.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    mensagem_sucesso = None
    if request.method == 'POST':
        # Captura os campos mapeados da tabela do banco de dados
        autor = request.form.get('autor')
        email = request.form.get('email')
        categoria = request.form.get('categoria')
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        
        # Exemplo no terminal da simulação da inserção SQL
        print("--- NOVO REGISTRO PARA O BANCO DE DADOS ---")
        print(f"Autor: {autor} | Email: {email}")
        print(f"Categoria: {categoria} | Título: {titulo}")
        print(f"Descrição: {descricao}")
        print("-------------------------------------------")
        
        mensagem_sucesso = f"Sucesso! A curiosidade '{titulo}' foi enviada e está pronta para o Banco de Dados."
        
    return render_template('contato.html', mensagem_sucesso=mensagem_sucesso)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)