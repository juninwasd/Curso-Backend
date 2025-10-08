import requests

resposta = requests.get("https://www.google.com")

print("Status Code:", resposta.status_code)
print("\nCabeçalhos:", resposta.headers)
print("\nCorpo:", resposta.text)