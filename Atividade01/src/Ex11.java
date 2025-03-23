import java.util.Scanner;

public class Ex11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String usuario, senha;

        System.out.print("Digite o nome de usuário: ");
        usuario = scanner.nextLine();

        System.out.print("Digite a senha: ");
        senha = scanner.nextLine();

        while (usuario.equals(senha)) {
            System.out.println("A senha não pode ser igual ao nome de usuário. Tente novamente.");

            System.out.print("Digite o nome de usuário: ");
            usuario = scanner.nextLine();

            System.out.print("Digite a senha: ");
            senha = scanner.nextLine();
        }

        System.out.println("Cadastro realizado com sucesso!");

        scanner.close();
    }
}
