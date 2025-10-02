from viagem_class import Viagem_class

viagem_0 = Viagem_class("Havaí")
viagem_1 = Viagem_class("Dubai")
viagem_2 = Viagem_class("Chique chique📌📍")
viagem_3 = Viagem_class("americanas")
viagem_4 = Viagem_class("França")

print("#############################################################################"
    '''
    ''')

print("Bem-Vindos! Japa Viagens tem algumas ofertas para você"
    '''
    ''')
viajante = print("Digite seu nome aqui:  ")

print (f"{viajante} temos 5 destinos que combina com você: "
'''
[0]Havaí
[1]Dubai
[2]chique chique
[3]americanas
[4]França

''')

selecao = int(input("Selecione o número da viagem desejada: "))
lista_viagem = (viagem_0,viagem_1,viagem_2,viagem_3,viagem_4)
opcao_selecionada = int(selecao)
for opcao in lista_viagem:
    if opcao_selecionada >= 5:
        print("Essa opção não está incluída em nosso destino")
        break
    if opcao_selecionada <= 4:
        print(f"{viajante} sua viagem para {lista_viagem[opcao_selecionada].destino}está marcado.")
        print("Volte sempre!")
        break
    
