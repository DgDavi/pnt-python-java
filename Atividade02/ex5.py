import json

ARQUIVO_CONTATOS = "contatos.json"

def carregar_contatos():
    try:
        with open(ARQUIVO_CONTATOS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, "w") as arquivo:
        json.dump(contatos, arquivo, indent=4)

def adicionar_contato(nome, telefone, email):
    contatos = carregar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)
    print("Contato adicionado com sucesso!")

def buscar_contato(nome):
    contatos = carregar_contatos()
    resultados = [contato for contato in contatos if nome.lower() in contato["nome"].lower()]
    if resultados:
        print("Contatos encontrados:")
        for contato in resultados:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    else:
        print("Nenhum contato encontrado.")


while True:
    print("\nGerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Buscar Contato")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        adicionar_contato(nome, telefone, email)
    elif opcao == "2":
        nome = input("Digite o nome para buscar: ")
        buscar_contato(nome)
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

