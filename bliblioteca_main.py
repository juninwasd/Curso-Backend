from biblioteca import Biblioteca

Livro_0 = Biblioteca("As crônicas de Narnia ")
Livro_1 = Biblioteca("Harry potter e a pedra filosofal")
Livro_2 = Biblioteca("Harry potter e a câmera secreta")
Livro_3 = Biblioteca("Meridiano de sangue")
Livro_4 = Biblioteca("Dom quixote")
Livro_5 = Biblioteca("Diario de banana")
Livro_6 = Biblioteca("Turma da mônica")
Livro_7 = Biblioteca("Turma do cebolinha")
Livro_8 = Biblioteca("quem mexeu no meu queijo")
Livro_9 = Biblioteca("mexi no queijo de alguem")

print("Bem-vindo a Bliblioteca Virtual"
    '''
    ''')
print("Gostaria de alugar algum livro? Estamos com ofertas incriveis do mês de outubro!!!"
    '''
    ''')

leitor = input("Gostaria que digitasse seu nome aqui:  "
    '''
    ''')
print("Aqui está algumas recomendaçôes"
'''

[0] = ("As crônicas de Narnia ")
[1] = ("Harry potter e a pedra filosofal")
[2] = ("Harry potter e a câmera secreta")
[3] = ("Meridiano de sangue")
[4] = ("Dom quixote")
[5] = ("Diario de banana")
[6] = ("Turma da mônica")
[7] = ("Turma do cebolinha")
[8] = ("quem mexeu no meu queijo")
[9] = ("mexi no queijo de alguem")
''')

selecao = int(input("Selecione o número do livro desejado(a): "))
lista_livros = (Livro_0,Livro_1,Livro_2,Livro_3,Livro_4,Livro_5,Livro_6,Livro_7,Livro_8,Livro_9)
opcao_selecionada = int(selecao)
for opcao in lista_livros:
    if opcao_selecionada >= 5:
        print("Essa opção não está incluída em nossa Biblioteca")
        break
    if opcao_selecionada <= 4:
        print(f"{leitor} seu(a) livro:  {lista_livros[opcao_selecionada].Livro} está marcado.")
        print("Volte sempre!")
        break