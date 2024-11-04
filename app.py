from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar a consulta
@app.route('/consultar', methods=['POST'])
def consultar():
    tipo_consulta = request.form['tipo_consulta']
    valor_consulta = request.form['valor_consulta']
    apitoken = 'Porra'  # Substitua isso pelo seu token de API

    # Montar a URL da API
    url = f"https://pnsapis.online/api/busca/{tipo_consulta}?query={valor_consulta}&apitoken={apitoken}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status 4xx ou 5xx
        resultado = response.json()  # Obtém a resposta em formato JSON
    except requests.exceptions.RequestException as e:
        resultado = {"error": str(e)}
    
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
