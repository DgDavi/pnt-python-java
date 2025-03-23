import java.util.Scanner;

public class Ex02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um valor em segundos: ");
        int totalSegundos = scanner.nextInt();

        int dias = totalSegundos / 86400;
        int horas = (totalSegundos % 86400) / 3600;
        int minutos = (totalSegundos % 3600) / 60;
        int segundos = totalSegundos % 60;

        System.out.println("Dias: " + dias);
        System.out.println("Horas: " + horas);
        System.out.println("Minutos: " + minutos);
        System.out.println("Segundos: " + segundos);

        scanner.close();
    }
}
