import java.util.Scanner;

public class Ex13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o salário inicial: ");
        double salarioInicial = scanner.nextDouble();

        System.out.print("Digite o aumento percentual inicial (em %): ");
        double aumentoPercentual = scanner.nextDouble();

        System.out.print("Digite o número de anos: ");
        int anos = scanner.nextInt();

        double salarioAtual = salarioInicial;
        for (int i = 1; i <= anos; i++) {
            salarioAtual += salarioAtual * (aumentoPercentual / 100);
            aumentoPercentual *= 2;  // O aumento percentual dobra a cada ano
        }

        System.out.printf("Salário após %d anos: %.2f\n", anos, salarioAtual);

        scanner.close();
    }
}
