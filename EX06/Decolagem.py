from collections import deque

def menu():
    print("\n=== CONTROLE DE DECOLAGEM ===")
    print("1 - Adicionar avião à fila de decolagem")
    print("2 - Autorizar decolagem do próximo avião")
    print("3 - Mostrar fila de decolagem")
    print("4 - Sair")

fila = deque()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        aviao = input("Digite o nome ou código do avião: ")
        fila.append(aviao)
        print(f"Avião {aviao} adicionado à fila de decolagem. 🛫")

    elif opcao == "2":
        if fila:
            decolando = fila.popleft()
            print(f"✈️  Avião {decolando} autorizado para decolar!")
        else:
            print("Nenhum avião na fila para decolagem.")

    elif opcao == "3":
        if fila:
            print("\n🧾 Fila atual de decolagem:")
            for i, aviao in enumerate(fila, start=1):
                print(f"{i}. {aviao}")
        else:
            print("A fila de decolagem está vazia no momento.")

    elif opcao == "4":
        print("Encerrando o sistema de controle de decolagem. 🌤️")
        break

    else:
        print("Opção inválida! Tente novamente.")
