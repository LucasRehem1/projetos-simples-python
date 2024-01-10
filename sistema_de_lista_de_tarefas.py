# sistema de lista de tarefas

# Lista para armazenar as tarefas
lista_tarefas = []

# Loop para perguntar qual opção você quer executar
while True:
    print("=== Lista de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Sair do programa")

    # Estrutura try para colocar uma messagem de erro e evitar que o programa quebre
    try:
        # Variavel que armazena o valor da opção para que possa ser executada
        opcao = int(input("Escolha uma opção: "))

        # Condicional para adicionar uma tarefa na lista
        if opcao == 1:
            adicionar_tarefa = input("Qual tarefa você quer adicionar a sua lista de tarefas?\n")
            lista_tarefas.append(adicionar_tarefa)

        # Codicional para mostrar o conteudo da lista
        elif opcao == 2:
            print(lista_tarefas)

        # Condicional para remover uma tarefa da lista de tarefas
        elif opcao == 3:
            lista_tarefas.remove(input(f"Qual tarefa você quer remover da lista de tarefas?"))

        # Condicional para parar (Break) o programa
        elif opcao == 4:
            print("Saindo do programa...")
            break
        # Se nenhuma condição for atendida mostrar na tela:
        else:
            print("Opção inválida!")

    # Quando for inserido um dado que não seja do tipo da variavel (no caso tipo int) mostrar mensagem de erro
    except ValueError:
        print("Por favor, insira um número inteiro.")