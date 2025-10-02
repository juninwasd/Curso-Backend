from feiralivre_class import Feira

fruta_0 = Feira("Abacate")
fruta_1 = Feira("Abacaxi")
fruta_2 = Feira("Açaí")
fruta_3 = Feira("Acerola")
fruta_4 = Feira("Ameixa")
fruta_5 = Feira("Amora")
fruta_6 = Feira("Banana")
fruta_7 = Feira("Caju")
fruta_8 = Feira("Carambola")
fruta_9 = Feira("Cereja")
fruta_10 = Feira("Coco")
fruta_11 = Feira("Figo")
fruta_12 = Feira("Framboesa")
fruta_13 = Feira("Goiaba")
fruta_14 = Feira("Jabuticaba")
fruta_15 = Feira("Jaca")
fruta_16 = Feira("Kiwi")
fruta_17 = Feira("Laranja")
fruta_18 = Feira("Limão")
fruta_19 = Feira("Maçã")
fruta_20 = Feira("Mamão")
fruta_21 = Feira("Manga")
fruta_22 = Feira("Maracujá")
fruta_23 = Feira("Melancia")
fruta_24 = Feira("Morango")

print("Bem-vindo à Feira do Seu JoÂo "
    '''
    ''')
print("Gostaria de comprar algumas frutas? Estamos com ofertas incriveis do mês de outubro!!!"
    '''
    ''')

cliente = input("Gostaria que digitasse seu nome aqui: para colocar no comprovante "
    '''
    ''')
print("Aqui está algumas frutas do nosso catálogo"
'''
[0]Abacate  
[1]Abacaxi     
[2]Açaí        
[3]Acerola     
[4]Ameixa
[5]Amora
[6]Banana
[7]Caju
[8]Carambola
[9]Cereja
[10]Coco
[11]Figo
[12]Framboesa
[13]Goiaba
[14]Jabuticaba
[15]Jaca
[16]Kiwi
[17]Laranja
[18]Limão
[19]Maçã
[20]Mamão
[21]Manga
[22]Maracujá
[23]Melancia
[24]Morango

''')

selecao = int(input("Selecione o número da Fruta desejado(a): "))
lista_compras = (fruta_0,fruta_1,fruta_2,fruta_3,fruta_4,fruta_5,fruta_6,fruta_7,fruta_8,fruta_9,fruta_10,fruta_11,
                 fruta_12,fruta_13,fruta_14,fruta_15,fruta_16,fruta_17,fruta_18,fruta_19,fruta_20,fruta_21,fruta_22,
                 fruta_23,fruta_24)
opcao_selecionada = int(selecao)
for opcao in lista_compras:
        if opcao_selecionada >= 24:
            print("Essa opção não está incluída em nossa Mercadoria")
            break
        if opcao_selecionada == selecao :
            print(f"{cliente} seu(a) Produto:  {lista_compras[opcao_selecionada].fruta} está marcado.")
            print(f"volte sempre {cliente}")
            break
            
