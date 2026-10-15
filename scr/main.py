def main():
    tarefas = []

    while True:
        print("\n===== TASKTRACKER =====")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nCadastro de nova tarefa")

        elif opcao == "2":
            print("\nVisualização de tarefas")

        elif opcao == "3":
            print("\nEncerrando o TaskTracker...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    main()