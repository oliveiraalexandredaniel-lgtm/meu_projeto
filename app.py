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
        # Captura os dados enviados pelo formulário
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')
        
        # Mensagem de confirmação que será exibida na tela
        mensagem_sucesso = f"Obrigado, {nome}! Sua mensagem foi enviada com sucesso."
        
    return render_template('contato.html', mensagem_sucesso=mensagem_sucesso)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)