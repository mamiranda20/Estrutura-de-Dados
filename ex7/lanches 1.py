def menu():
    print("\n=== MONTAGEM DO SEU SANDUÍCHE ===")
    print("1 - Adicionar ingrediente")
    print("2 - Remover ingrediente (do topo)")
    print("3 - Ver último ingrediente adicionado")
    print("4 - Mostrar sanduíche completo")
    print("5 - Finalizar pedido")

pilha = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ingrediente = input("Digite o nome do ingrediente: ")
        pilha.append(ingrediente)
        print(f"🥪 {ingrediente} adicionado ao sanduíche.")

    elif opcao == "2":
        if pilha:
            removido = pilha.pop()
            print(f"❌ {removido} foi removido do topo do sanduíche.")
        else:
            print("O sanduíche está vazio! Nenhum ingrediente para remover.")

    elif opcao == "3":
        if pilha:
            print(f"👀 O último ingrediente adicionado foi: {pilha[-1]}")
        else:
            print("O sanduíche ainda não tem ingredientes.")

    elif opcao == "4":
        if pilha:
            print("\n🍔 Seu sanduíche está assim (de baixo para cima):")
            for i, ingrediente in enumerate(pilha, start=1):
                print(f"{i}. {ingrediente}")
            print("🧀 Topo do sanduíche acima!")
        else:
            print("Seu sanduíche está vazio. Adicione ingredientes para começar!")

    elif opcao == "5":
        print("\n🥙 Pedido finalizado! Bom apetite!")
        break

    else:
        print("Opção inválida! Tente novamente.")
