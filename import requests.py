import requests
import json
from flask import Flask
import os



'''
url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "CursoBackendPython/1.0 (Aluno Marcelo; +https://meuportfolio.dev)"
}

resposta = requests.get(url, headers=headers)

print("Status Code:", resposta.status_code)
print("\nCabeçalhos recebidos pelo servidor: ")
print(resposta.json()["headers"])


texto = '{"curso": "Backend", "modulo": "HTTP"}'
dados = json.loads(texto)
print(dados["curso"])

novo_json = json.dumps(dados, indent=2)
print (novo_json)


url = "https://httpbin.org/bearer"

token = "cba321zyx789"

headers = {
    "Authorization": f"Bearer {token}"
}
resposta = requests.get(url, headers=headers)
print("Status Code:", resposta.status_code)
print("Resposta do servidor:")
print(resposta.json())
'''

app = Flask(__name__)
@app.route("/")
def home():
    
    soma = 30 + 57
    multiplicacao = 15 * 7
    divisao =  25 / 4
    resto = 37 % 5
    potencia = 6 ** 4
    resposta = f"""
    <h1>Operadores Aritmétrica</h1>
    <ul>
        <li>1. Calcule a Soma de 30 + 57: = {soma}</li>
        
        <li>2. Multiplique 15 por 7 = {multiplicacao}</li>
        
        <li>3. Divida 25 por 4 e veja o resultado = {divisao}</li>
        
        <li>4. Descubra o resto da divisão de 37 por 5 = {resto}</li>
        
        <li>5. Eleve 6 à potência de 4= {potencia}</li>
        
    </ul>
    """
    return resposta

if __name__ == "__main__":
    app.run(debug=True)