from aluno import Aluno
from professor import Professor
from curso import Curso

cursos = set()
alunos = set()
Professores = set()

while True:
    print("\n=== PRINCIPAL ===")
    print("1 - Cadastrar Curso")
    print("2 - Cadastrar aluno")
    print("3 - Cadastrar professor")
    print("4 - listar Cursos")
    print("5 - Listar Alunos")
    print("6 - Listar professores")
    print("7 - Sair")

    opcao = input("Escolha uma Opção: ")

    if opcao == 1:
        nome_curso = input("Nome do cursos: ")
        curso = Curso(nome_curso)
        cursos.add(curso)
        print(f"Curso '{nome_curso}' cadastro com sucesso!")

    elif opcao == 2:
        nome_aluno = input("Nome do aluno: ")
        curso = Curso(nome)