import java.util.Scanner;
public class Ex07 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número ímpar: ");
        int numeroImpar = scanner.nextInt();

        if (numeroImpar % 2 == 0) {
            System.out.println("O número digitado não é ímpar.");
        } else {
            int numeroAnterior = numeroImpar - 2;
            int numeroProximo = numeroImpar + 2;
            int diferenca = (numeroProximo * numeroProximo) - (numeroAnterior * numeroAnterior);
            System.out.println("A diferença entre o quadrado do número anterior e do próximo número ímpar é: " + diferenca);
        }
        scanner.close();
    }
}