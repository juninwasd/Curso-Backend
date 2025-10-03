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
                print(f"- {a.nome} (Matrícula: {a.matricula})")
        else:
            print("Nenhum aluno cadastrado.")

    elif opcao == "6":
        if professores:
            print("\n--- Professores Cadastrados ---")
            for p in professores:
                print(f"- {p.nome} (SIAPE: {p.siape})")
        else:
            print("Nenhum professor cadastrado.")

    elif opcao == "7":
        print("Saindo do sistema... Até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")
