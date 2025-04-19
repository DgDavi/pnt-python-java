usuarios = []
usuario_logado = None

def cadastrar_usuario():
    nome = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")

    for u in usuarios:
        if u["nome"] == nome:
            print("Esse nome de usuário já existe.")
            return

    novo_usuario = {
        "nome": nome,
        "senha": senha,
        "saldo": 0.0,
        "transacoes": []
    }

    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

def login():
    global usuario_logado
    nome = input("Usuário: ")
    senha = input("Senha: ")

    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            usuario_logado = u
            print(f"Bem-vindo, {nome}!")
            return

    print("Usuário ou senha incorretos.")

def logout():
    global usuario_logado
    usuario_logado = None
    print("Logout realizado com sucesso.")

def depositar():
    valor = float(input("Digite o valor para depósito: "))
    if valor > 0:
        usuario_logado["saldo"] += valor
        usuario_logado["transacoes"].append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido.")

def sacar():
    valor = float(input("Digite o valor para saque: "))
    if 0 < valor <= usuario_logado["saldo"]:
        usuario_logado["saldo"] -= valor
        usuario_logado["transacoes"].append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Saldo insuficiente ou valor inválido.")

def ver_saldo():
    print(f"Saldo atual: R$ {usuario_logado['saldo']:.2f}")

def ver_transacoes():
    print("Histórico de transações:")
    for t in usuario_logado["transacoes"]:
        print("-", t)

def menu_principal():
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Cadastrar Usuário")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            login()
            if usuario_logado:
                menu_usuario()
        elif opcao == "3":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

def menu_usuario():
    while True:
        print("\n--- Menu do Usuário ---")
        print("1. Ver Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Ver Transações")
        print("5. Logout")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ver_saldo()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            ver_transacoes()
        elif opcao == "5":
            logout()
            break
        else:
            print("Opção inválida.")

menu_principal()
