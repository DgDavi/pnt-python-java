import java.util.Scanner;

public class Ex04 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número de dias que o carro foi alugado: ");
        int dias = scanner.nextInt();
        System.out.print("Digite o número de quilômetros percorridos: ");
        double quilometros = scanner.nextDouble();

        double custoTotal = dias * 90.0;
        if (quilometros > 100) {
            double kmExtra = quilometros - 100;
            custoTotal += kmExtra * 12.0;
        }

        System.out.printf("O custo total é: R$%.2f%n", custoTotal);

        scanner.close();
    }
}
