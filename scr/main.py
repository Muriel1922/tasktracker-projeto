
def cadastrar_tarefa(tarefas):
    print("\n===== CADASTRAR TAREFA =====")
    print("Digite 0 no título para cancelar.")

    while True:
        titulo = input("Título: ").strip()

        if titulo == "0":
            print("Cadastro cancelado.")
            return

        if titulo:
            break

        print("Erro: o título não pode ficar vazio!")

    descricao = input("Descrição: ").strip()

    while True:
        prioridade = input(
            "Prioridade (Alta/Média/Baixa): "
        ).strip().lower()

        if prioridade in ("alta", "média", "media", "baixa"):
            if prioridade == "media":
                prioridade = "média"
            prioridade = prioridade.capitalize()
            break

        print("Erro: escolha Alta, Média ou Baixa!")

    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    print("\n===== TAREFAS CADASTRADAS =====")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\n--- Tarefa {numero} ---")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def main():
    tarefas = []

    while True:
        print("\n===== TASKTRACKER =====")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)

        elif opcao == "2":
            visualizar_tarefas(tarefas)

        elif opcao == "3":
            print("\nEncerrando o TaskTracker...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
