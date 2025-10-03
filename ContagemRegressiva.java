import java.util.*;

public class ContagemRegressiva {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        // Solicita número ao usuário
        System.out.print("Digite um número inteiro positivo: ");
        int numero = entrada.nextInt();

        // Laço de repetição: enquanto numero >= 0
        while (numero >= 0) {
            System.out.println(numero);
            numero--; // decrementa o valor
        }

        System.out.println("Fim da contagem regressiva!");
        entrada.close();
    }
}
