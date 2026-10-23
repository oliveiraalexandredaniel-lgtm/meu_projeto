from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curiosidades')
def curiosidades():
    return render_template('curiosidades.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    mensagem_sucesso = None
    if request.method == 'POST':
        # Captura os dados enviados pelo formulário HTML
        autor = request.form.get('autor')
        email = request.form.get('email')
        categoria = request.form.get('categoria')
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        
        # Define a mensagem de confirmação para o template
        mensagem_sucesso = f"Curiosidade '{titulo}' cadastrada com sucesso!"
        
    return render_template('contato.html', mensagem_sucesso=mensagem_sucesso)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
