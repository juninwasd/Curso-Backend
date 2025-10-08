import requests
'''
resposta = requests.get("https://jsonplaceholder.typicode.com/users/3")

print("\nStatus Code:", resposta.status_code)
print("\nEmpresa:", resposta.headers["Content-Type"])

variavel = resposta.json()
print(variavel)

variavel2 = variavel
print (variavel2 ["company"]["name"])

url = "https://httpbin.org/post"
dados = {"usuario": "Junio", "curso": "Back-end Python"}

resultado = requests.post(url, json=dados)

print("\nmétodo:\n", resultado.request.method)
print("\nCódigo de status:\n", resultado.status_code)
print("\nCorpo da resposta:\n", resultado.json())


url = "https://jsonplaceholder.typicode.com/posts"

novo_post={
    "title": "Mwu primeiro post via Python",
    "body": "Estou aprendendo sobre HTTP!",
    "userId": 1
}

resposta = requests.post(url, json=novo_post)

print("Status Code:", resposta.status_code)
print("Corpo da resposta:", resposta.json())


url = "https://httpbin.org/post"

novo_post={
    "Nome": "Junio moreira de brito",
    "Cidade": "Mogi Guacu",
    "Curso": "Desenvolvedor Back-End",
    "userId": 1
}

reposta = requests.post(url, json=novo_post)

print("\nmethod:\n", reposta.request.method)
print("\nStatus Code:\n", reposta.status_code)
print("\nCorpo da resposta:\n", reposta.json())
print("\nurl:\n", url)

url = "https://jsonplaceholder.typicode.com/posts/1"

dados_atualizados = {
    "id": 1,
    "title": "Titulo atualizado",
    "body": "Conteudo substituido com sucesso!",
    "userId": 1
}

resposta = requests.put(url, json=dados_atualizados)

print("\nStatus Code:\n", resposta.status_code)
print("\nCorpo da resposta:\n", resposta.json())




url = "https://httpbin.org/put"

dados =  { 
    "id": 1,
    "Nome": "Junio Moreira de brito",
    "Curso": "Desenvolvedor Back-End",
}

resultado = requests.put(url, json=dados)

print("\nmethod:\n", resultado.request.method)
print("\nStatus Code:\n", resultado.status_code)
print("\nCorpo da resposta:\n", resultado.json())

url = "https://httpbin.org/delete"


resposta = requests.delete(url)

print("\nMetodo:\n", resposta.request.method)
print("\nStatus Code:\n", resposta.status_code)
print("\nCorpo da resposta:\n", resposta.text)



url = "https://httpbin.org/patch"

dados_atualizados = {
    "Curso": "Backend Avancado"
}

resposta = requests.patch(url, json=dados_atualizados)

print("\nStatus Code:\n", resposta.status_code)
print("\nCorpo da resposta:\n", resposta.json())
'''

url = "https://httpbin.org/get"

resposta = requests.options(url)

print("\nStatus Code:\n", resposta.status_code)
print("\nMetodos permitidos:\n", resposta.headers.get("Allow"))
print("\nTodos os headers:\n", resposta.headers)

