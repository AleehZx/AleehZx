python
from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        texto = request.form['texto']
        opcao = request.form['opcao']
        # Aqui você pode adicionar a lógica para a consulta
        resultado = f'Você digitou: {texto} e escolheu: {opcao}'

    html = '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meu Site</title>
    </head>
    <body>
        <h1>Consulta</h1>
        <form method="POST">
            <label for="texto">Digite algo:</label>
            <input type="text" id="texto" name="texto" required>
            <br>
            <label for="opcao">Escolha uma opção:</label>
            <select id="opcao" name="opcao">
                <option value="opcao1">Opção 1</option>
                <option value="opcao2">Opção 2</option>
                <option value="opcao3">Opção 3</option>
            </select>
            <br>
            <button type="submit">Consultar</button>
        </form>
        {% if resultado %}
            <h2>{{ resultado }}</h2>
        {% endif %}
    </body>
    </html>
    '''

    return render_template_string(html, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
