
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Projects {

    public static void antepost(Scanner myObj) {
        boolean choice = true;

        while (choice) {
            try {
                System.out.println("Bem vindo ao calculador em Java de número anterior e sucessor\n");
                System.out.print("Insira Seu Número: ");
                int usernum = myObj.nextInt();

                int post = usernum + 1;
                int ant = usernum - 1;

                System.out.println("\nO número inserido pelo usuário foi: " + usernum);
                System.out.println("O número posterior foi: " + post);
                System.out.println("O número anterior foi: " + ant);

                System.out.print("\nQuer Continuar? (S/N): ");
                String retorno = myObj.next().trim().toLowerCase();
                if (!retorno.equals("s") && !retorno.equals("sim")) {
                    choice = false;
                }
            } catch (Exception e) {
                System.out.println("⚠️ Entrada inválida, tente novamente!");
                myObj.nextLine(); // limpa buffer
            }
        }
    }

    public static void minimsal(Scanner myObj) {
        System.out.println("Bem vindo ao calculador de Salários Mínimos!");
        int umsalmin = 1500;

        System.out.print("Insira seu salário: ");
        float usersal = myObj.nextFloat();

        double quociente = usersal / umsalmin;
        int arredondado = (int) Math.round(quociente);

        System.out.println("Você tem " + arredondado + " salários mínimos no seu salário.");
    }

    public static void ipicalc(Scanner myObj) {
        List<Product> products = new ArrayList<>();
        boolean seguir = true;

        while (seguir) {
            try {
                Product product = new Product();

                System.out.println("\n--- Lista de Produtos Cadastrados ---");
                for (Product p : products) {
                    System.out.println(p.getId() + ": " + p.getName() + " - R$ " + p.getPrice() + " - Unidades: " + p.getQuantity());
                }

                System.out.print("Insira o código da peça: ");
                product.setId(myObj.nextInt());
                myObj.nextLine();

                System.out.print("Insira o Nome da peça: ");
                product.setName(myObj.nextLine());

                System.out.print("Insira o Preço da peça: ");
                product.setPrice(myObj.nextDouble());

                System.out.print("Insira a Quantidade da peça: ");
                product.setQuantity(myObj.nextInt());
                myObj.nextLine();

                products.add(product);
                System.out.println("✅ Produto cadastrado com sucesso: " + product.getId() + " - " + product.getName());

                System.out.print("\nGostaria de cadastrar mais algum produto? (S/N): ");
                String retorno = myObj.nextLine().trim().toLowerCase();
                if (!retorno.equals("s") && !retorno.equals("sim")) {
                    seguir = false;
                }

                // cálculo subtotal
                double subtotal = 0.0;
                System.out.println("\n--- Lista de Produtos (cálculo do IPI) ---");
                for (Product p : products) {
                    double parcial = p.getQuantity() * p.getPrice();
                    subtotal += parcial;
                    System.out.println(p.getId() + ": " + p.getName() + " - R$ " + p.getPrice() + " - Quantidade: " + p.getQuantity() + " → Parcial: " + parcial);
                }

                double IPI = 10.0; // 10%
                double fator = 1 + (IPI / 100.0);
                double total = subtotal * fator;

                System.out.println("Subtotal sem IPI: R$ " + subtotal);
                System.out.println("Total com IPI: R$ " + total);

            } catch (Exception e) {
                System.out.println("⚠️ Entrada inválida, tente novamente!");
                myObj.nextLine(); // limpar buffer
            }
        }
    }

    public static void sal(Scanner myObj) {
        System.out.print("Insira o valor do seu saldo: ");
        double saldo = myObj.nextDouble();

        double reajuste = saldo + saldo * 0.01;
        System.out.println("O Seu Saldo Após O Reajuste É: " + reajuste);
    }

    public static void med(Scanner myObj) {
        boolean choice = true;

        while (choice) {
            System.out.print("Insira o primeiro valor: ");
            int n1 = myObj.nextInt();
            System.out.print("Insira o segundo valor: ");
            int n2 = myObj.nextInt();
            System.out.print("Insira o terceiro valor: ");
            int n3 = myObj.nextInt();

            int primeira_media = (n1 + n2 + n3) / 3;
            System.out.println(">>> O Valor da Primeira Média É: " + primeira_media);

            System.out.print("Insira o quarto valor: ");
            int n4 = myObj.nextInt();
            System.out.print("Insira o quinto valor: ");
            int n5 = myObj.nextInt();
            System.out.print("Insira o sexto valor: ");
            int n6 = myObj.nextInt();

            int segunda_media = (n4 + n5 + n6) / 3;
            System.out.println(">>> O Valor da Segunda Média É: " + segunda_media);

            int soma = primeira_media + segunda_media;
            System.out.println(">>> O Valor da Soma das Médias É: " + soma);

            double media = soma / 2.0;
            System.out.println("A Média da Soma das Médias É: " + media);

            System.out.print("\nQuer continuar? (S/N): ");
            String retorno = myObj.next().trim().toLowerCase();
            if (!retorno.equals("s") && !retorno.equals("sim")) {
                choice = false;
            }
        }
    }

    public static void totdias(Scanner myObj) {
        System.out.print("Quantos Anos Você Tem? ");
        int userAnos = myObj.nextInt();

        System.out.print("Quantos Meses Você Tem? ");
        int userMeses = myObj.nextInt();

        System.out.print("Quantos Dias Você Tem? ");
        int userDia = myObj.nextInt();

        int totaldias = userMeses * 30 + userAnos * 365 + userDia;

        System.out.println("Você tem " + userAnos + " anos, " + userMeses + " meses e " + userDia + " dias");
        System.out.println("O Total De Dias É: " + totaldias);
    }

    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        System.out.print("Qual das atividades você quer ver? (1-6): ");
        int atividade = myObj.nextInt();

        switch (atividade) {
            case 1 -> totdias(myObj);
            case 2 -> med(myObj);
            case 3 -> sal(myObj);
            case 4 -> ipicalc(myObj);
            case 5 -> minimsal(myObj);
            case 6 -> antepost(myObj);
            default -> System.out.println("Opção Inválida");
        }

        myObj.close();
    }

    public static class Product {
        private int id;
        private String name;
        private double price;
        private int quantity;

        public int getId() { return id; }
        public void setId(int id) { this.id = id; }

        public String getName() { return name; }
        public void setName(String name) { this.name = name; }

        public double getPrice() { return price; }
        public void setPrice(double price) { this.price = price; }

        public int getQuantity() { return quantity; }
        public void setQuantity(int quantity) { this.quantity = quantity; }
    }
}
