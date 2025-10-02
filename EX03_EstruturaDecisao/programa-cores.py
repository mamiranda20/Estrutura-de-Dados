cor = input("Digite uma cor:\n")

if (cor != "azul" and cor != "vermelho" and cor != "amarelo" ):
    print("Essa cor não faz parte das cores primárias!")
elif (cor == "vermelho"):
    print("VERMELHO: calor, energia, perigo")
    print("AZUL: calma, inteligência, frio")
elif (cor == "verde"):
    print("VERDE: natureza, renovação, esperança ")
elif (cor == "amarelo"):
    print("AMARELO: alegria, riqueza, luz")