from flask import Flask
import os


app = Flask(__name__)
@app.route("/")

def calcular_imc (peso, altura):
 
 imc = peso / (altura ** 2)
 return imc

def classificar_IMC(imc):
  if imc <= 18.5:
    return "Abaixo do peso"
  elif imc <= 25:
    return "peso normal"
  elif imc <= 30:
    return "sobrepeso"
  elif imc <= 40:
    return "obesidade"
  else:
    return "obesidade grave"
  
def main():
  peso = 60
  altura = 1.70

  imc = classificar_IMC(peso, altura)
  classificação = classificar_IMC(imc)

    
  resposta = f"""
    <h1>Operador IMC</h1>
    <ul>
        <li>Seu IMC é{imc}</li>

        <li>Classificação: {classificação}</li>
    </ul>
    """
  return resposta

if __name__ == "__main__":
    app.run(debug=True)

main()















