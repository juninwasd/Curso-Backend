import requests

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "CursoBackendPython/1.0 (Aluno Marcelo; +https://meuportfolio.dev)"
}

resposta = requests.get(url, headers=headers)

print("Status Code:", resposta.status_code)
print("\nCabeçalhos recebidos pelo servidor: ")
print(resposta.json()["headers"])