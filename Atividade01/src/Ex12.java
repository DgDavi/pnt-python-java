import java.util.Scanner;

public class Ex12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe a quantidade de turmas: ");
        int quantidadeTurmas = scanner.nextInt();

        int totalAlunos = 0;
        for (int i = 1; i <= quantidadeTurmas; i++) {
            System.out.print("Informe a quantidade de alunos na turma " + i + ": ");
            int alunosTurma = scanner.nextInt();
            if (alunosTurma > 40) {
                System.out.println("A turma " + i + " tem mais de 40 alunos.");
            }
            totalAlunos += alunosTurma;
        }

        double mediaAlunosPorTurma = (double) totalAlunos / quantidadeTurmas;
        System.out.println("A média de alunos por turma é: " + mediaAlunosPorTurma);

        scanner.close();
    }
}