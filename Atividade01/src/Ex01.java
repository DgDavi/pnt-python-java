import java.util.Scanner;

public class Ex01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a primeira nota: ");
        double nota1 = scanner.nextDouble();
        System.out.print("Digite a segunda nota: ");
        double nota2 = scanner.nextDouble();
        System.out.print("Digite a terceira nota: ");
        double nota3 = scanner.nextDouble();

        double mediaAritmetica = (nota1 + nota2 + nota3) / 3;
        double mediaPonderada1 = (nota1 * 2 + nota2 * 2 + nota3 * 3) / 7;
        double mediaPonderada2 = (nota1 * 1 + nota2 * 2 + nota3 * 2) / 5;

        System.out.println("Média Aritmética: " + mediaAritmetica);
        System.out.println("Média Ponderada (pesos 2, 2, 3): " + mediaPonderada1);
        System.out.println("Média Ponderada (pesos 1, 2, 2): " + mediaPonderada2);

        scanner.close();
    }
}
