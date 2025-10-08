import requests


#----------------------------------------------------

url4 = ("https://httpbin.org/get")

dados4 = {"Nome": "Junio", "Curso": "Desenvolvedor Backend"}

resultado2 = requests.get(url4, json=dados4)

print("\nmétodo:\n", resultado2.request.method)
print("\nCódigo de status:\n", resultado2.status_code)
print("\nCorpo da resposta:\n", resultado2.json())
print("\nUrl:\n", url4)

#----------------------------------------------------

url3 = "https://httpbin.org/post"
dados3 = {"usuario": "Junio", "Cidade": "Mogi_guacu", "Idade": "16"}

resultado = requests.post(url3, json=dados3)

print("\nmétodo:\n", resultado.request.method)
print("\nCódigo de status:\n", resultado.status_code)
print("\nCorpo da resposta:\n", resultado.json())
print("\nUrl:\n", url3)

#----------------------------------------------------

url2 = "https://httpbin.org/put"

dados2 =  { 
    "id": 1,
    "Cidade": "Mogi_Guacu",
    "Idade": "16",
}

resultado = requests.put(url2, json=dados2)

print("\nmethod:\n", resultado.request.method)
print("\nStatus Code:\n", resultado.status_code)
print("\nCorpo da resposta:\n", resultado.json())
print("\nUrl:\n", url2)

#----------------------------------------------------

url1 = "https://httpbin.org/delete"

dados1 =  { 
    "User_id": 1
}
resposta = requests.delete(url1, json=dados1)

print("\nMetodo:\n", resposta.request.method)
print("\nStatus Code:\n", resposta.status_code)
print("\nCorpo da resposta:\n", resposta.text)
print("\nUrl:\n", url1)
















