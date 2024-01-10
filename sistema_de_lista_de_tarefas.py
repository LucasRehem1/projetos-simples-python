# sistema de lista de tarefas

# Lista para armazenar as tarefas
lista_tarefas = []
lista_tarefas_concluida = []

# Loop para perguntar qual opção você quer executar
while True:
    print("=== Lista de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Remover uma tarefa")
    print("4 - Marcar tarefa como concluída")
    print("5 - Visualizar tarefas concluídas")
    print("6 - Sair do programa\n")

    # Estrutura try para colocar uma mensagem de erro e evitar que o programa quebre
    try:
        # Variavel que armazena o valor da opção para que possa ser executada
        opcao = int(input("Escolha uma opção: "))

        # Condicional para adicionar uma tarefa na lista
        if opcao == 1:
            adicionar_tarefa = input("Qual tarefa você quer adicionar a sua lista de tarefas?\n")
            lista_tarefas.append(adicionar_tarefa)

        # Codicional para mostrar o conteudo da lista
        elif opcao == 2:
            print("TAREFAS PENDENTES: ")
            print(lista_tarefas)

        # Condicional para remover uma tarefa da lista_tarefas e coloca-la na lista_tarefas_concluidas
        elif opcao == 3:
            # Variavel para armazenar temporariamente o indice
            remover_tarefa = input("Qual tarefa você quer remover da lista? ")
            # verificação se existe dentro da lista de tarefas para ser removido
            if remover_tarefa in lista_tarefas:
                lista_tarefas.remove(remover_tarefa)
                print(f'A tarefa "{remover_tarefa}" foi removida')
            # Se não estiver na lista, apresentar mensagem:
            else:
                print("Essa tarefa não está na lista.")

        # Condicional para remover uma tarefa da lista_tarefas e adicionar na lista_tarefas_concluida
        elif opcao == 4:
            concluir_tarefa = (input("Qual tarefa você quer marcar como concluída?"))
            if concluir_tarefa in lista_tarefas:
                lista_tarefas.remove(concluir_tarefa)
                lista_tarefas_concluida.append(concluir_tarefa)
            else:
                print("Essa tarefa não está na lista.")

        # Condicional para mostrar lista_tarefas_concluidas
        elif opcao == 5:
            print("TAREFAS CONCLUÍDAS:")
            print(lista_tarefas_concluida)

        # Condicional para parar (Break) o programa
        elif opcao == 6:
            print("Saindo do programa...")
            break

        # Se nenhuma condição for atendida mostrar na tela:
        else:
            print("Opção inválida!")

    # Quando for inserido um dado que não seja do tipo int mostrar mensagem de erro
    except ValueError:
        print("Por favor, insira um número inteiro.")