import java.util.Scanner;

public class Ex03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o valor total das mercadorias compradas: R$ ");
        double valorTotal = scanner.nextDouble();

        if (valorTotal <= 500) {
            System.out.println("Não há imposto sobre o valor total.");
        } else {
            double valorImposto = (valorTotal - 500) * 0.50;
            System.out.println("O valor do imposto é: R$ " + valorImposto);
        }

        scanner.close();
    }
}