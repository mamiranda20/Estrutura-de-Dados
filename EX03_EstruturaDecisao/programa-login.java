import java.util.*;

public class Main {
    public static void main(String[] args) {
      String codigo;
      System.out.println("Digite o código");
      Scanner scanner = new Scanner(System.in); 
      codigo = scanner.nextLine();
      System.out.println();
      if (codigo.equals ("Admin123")){
        System.out.println("Bem-vindo, Administrador");
      }
      else if (codigo.equals ("User123")){
     System.out.println("Bem-vindo, Usuário!");
      } 
     else{
     System.out.println("Código incorreto");
     }
  }
}