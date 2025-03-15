import java.util.Scanner;

public class ex01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite 3 notas: ");
        double nota1 = scanner.nextDouble();
        double nota2 = scanner.nextDouble();
        double nota3 = scanner.nextDouble();
        double media = (nota1 + nota2 + nota3) / 3;
        double mediaPonderada = (nota1 * 2 + nota2 * 2 + nota3 * 3) / 7;
        double mediaPonderada2 = (nota1 * 1 + nota2 * 2 + nota3 * 2) / 5;

        System.out.printf("Média aritimética: %.2f%n",  media);
        System.out.printf("Média ponderada (2, 2, 3): %.2f%n",  mediaPonderada);
        System.out.printf("Média ponderada (1, 2, 2): %.2f%n", mediaPonderada2);

        scanner.close();
    }
}