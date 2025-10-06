from aluno import Aluno
from professor import Professor
from curso import Curso

cursos = set()
alunos = set()
Professores = set()



while True:
    opcao = input("Escolha uma Opção: ")

    if opcao == "1":
        nome_curso = input("Nome do cursos: ")
        curso = Curso(nome_curso)
        cursos.add(curso)
        print(f"Curso {nome_curso} cadastro com sucesso!")
        
    elif opcao == "2":
        nome_aluno = input("Nome do aluno: ")
        aluno = Aluno(nome_aluno)
        alunos.add(aluno)
        print(f"Aluno '{nome_aluno}' cadastro com sucesso!")

    elif opcao == "3":
        nome_professor = input("Nome do professor: ")
        professor = Professor(nome_professor)
        Professores.add(professor)
        print(f"Professor '{nome_professor}' cadastro com sucesso!")

    elif opcao == "4":
        if cursos:
            print("\n--- Cursos Cadastrados ---")
            for c in cursos:
                print(f"- {c.nome}")
        else:
            print("Nenhum curso cadastrado.")

    elif opcao == "5":
        if alunos:
            print("\n--- Alunos Cadastrados ---")
            for a in alunos:
                print(f"- {a.nome} ")
        else:
            print("Nenhum aluno cadastrado.")

    elif opcao == "6":
        if Professores:
            print("\n--- Professores Cadastrados ---")
            for p in Professores:
                print(f"- {p.nomes}")
        else:
            print("Nenhum professor cadastrado.")

    elif opcao == "7":
        print("Saindo do sistema... Até mais!")


    else:
        print("Opção inválida! Tente novamente.")
    