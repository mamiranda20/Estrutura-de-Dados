def menu():
    print("\n=== 🎵 GERENCIADOR DE MÚSICAS 🎵 ===")
    print("1 - Tocar nova música")
    print("2 - Desfazer última música tocada")
    print("3 - Ver última música tocada")
    print("4 - Mostrar histórico completo")
    print("5 - Encerrar programa")

pilha = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        musica = input("Digite o nome da música que está tocando: ")
        pilha.append(musica)
        print(f"🎧 Tocando agora: {musica}")

    elif opcao == "2":
        if pilha:
            removida = pilha.pop()
            print(f"⏪ Removida do histórico: {removida}")
        else:
            print("O histórico está vazio. Nenhuma música para remover.")

    elif opcao == "3":
        if pilha:
            print(f"🎶 Última música tocada: {pilha[-1]}")
        else:
            print("Nenhuma música foi tocada ainda.")

    elif opcao == "4":
        if pilha:
            print("\n📜 Histórico de músicas (da primeira à última):")
            for i, musica in enumerate(pilha, start=1):
                print(f"{i}. {musica}")
            print(f"\n▶️ Última tocada: {pilha[-1]}")
        else:
            print("O histórico está vazio. Toque uma música para começar!")

    elif opcao == "5":
        print("\n🎧 Programa encerrado. Até a próxima batida! 🎵")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")
