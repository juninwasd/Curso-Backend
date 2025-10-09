import requests

def print_resposta(resposta):
    print("Método:", resposta.request.method)
    print("Status Code:", resposta.status_code)
    print("URL:", resposta.url)
    print("-")

def main():
    print("\n=== REQUISIÇAO GET ===")
    params = {"nome": "joao", "curso": "Python"}
    get_resp = requests.get("https://httpbin.org/get", params=params)
    print_resposta(get_resp)

    print("\n=== REQUISIÇAO POST ===")
    post_data = {"nome": "joao", "cidade": "Recife", "idade": 25}
    post_resp = requests.post("https://httpbin.org/post", json=post_data)
    print_resposta(post_resp)
    
    
    print("\n=== REQUISIÇAO PUT ===")
    put_data = {"nome": "joao", "cidade": "Salvador", "idade": 30}
    put_resp = requests.put("https://httpbin.org/put", json=put_data)
    print_resposta(put_resp)
    
    
    print("\n=== REQUISIÇAO DELETE ===")
    delete_data = {"user_id": 123456}
    delete_resp = requests.delete("https://httpbin.org/delete", json=delete_data)
    print_resposta(delete_resp)
    
if __name__ == "__main__":
    main()