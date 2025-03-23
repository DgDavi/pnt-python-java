import java.util.Scanner;

public class Ex10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número inteiro maior que 1: ");
        int num = scanner.nextInt();

        if (num <= 1) {
            System.out.println("Número inválido! Digite um número maior que 1.");
        } else {
            boolean primo = true;
            for (int i = 2; i <= Math.sqrt(num); i++) {
                if (num % i == 0) {
                    primo = false;
                    break;
                }
            }

            if (primo) {
                System.out.println(num + " é um número primo.");
            } else {
                System.out.println(num + " não é um número primo.");
            }
        }

        scanner.close();
    }
}
