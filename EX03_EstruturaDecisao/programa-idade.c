#include <stdio.h>
int main()
{
    int idade;
    printf("Digite a idade:");
    scanf("%d", &idade);
    printf("idade: %d", idade);
    
    if (idade < 18) {
      printf("Você é menor de idade");
    } 
    else {
      printf("Você é maior de idade");
    }
}