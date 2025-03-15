import java.util.Scanner;

public class ex02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite os segundos: ");
        int segundos = scanner.nextInt();

        int dias = segundos / 86400;
        int resto = segundos % 86400;
        int horas = resto / 3600;
        resto = resto % 3600;
        int minutos = resto / 60;
        int segundosRestantes = resto % 60;

        System.out.printf("%d dias, %d horas, %d minutos e %d segundos%n", dias, horas, minutos, segundosRestantes);
        scanner.close();
    }
}
