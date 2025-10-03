#include <stdio.h>
#include <string.h>

int main() {
    char palavra[100];   // espaço para armazenar a palavra
    int i, totalVogais = 0;

    // Pede a palavra ao usuário
    printf("Digite uma palavra: ");
    scanf("%s", palavra);

    // Percorre cada letra da palavra
    for (i = 0; i < strlen(palavra); i++) {
        char letra = palavra[i];

        // Verifica se é vogal (maiúscula ou minúscula)
        if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u' ||
            letra == 'A' || letra == 'E' || letra == 'I' || letra == 'O' || letra == 'U') {
            totalVogais++;
        }
    }

    // Mostra resultado
    printf("A palavra '%s' possui %d vogais.\n", palavra, totalVogais);

    return 0;
}
