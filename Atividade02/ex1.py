import json
from datetime import datetime

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    if not existe_arquivo():
        return []
    arquivo = open(ARQUIVO_TAREFAS, "r")
    conteudo = arquivo.read()
    tarefas = json.loads(conteudo)
    arquivo.close()
    return tarefas

def existe_arquivo():
    import os
    return os.path.exists(ARQUIVO_TAREFAS)

def salvar_tarefas(tarefas):
    arquivo = open(ARQUIVO_TAREFAS, "w")
    conteudo = json.dumps(tarefas, indent=4)
    arquivo.write(conteudo)
    arquivo.close()

def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except:
        return False

def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ")

    while True:
        prazo = input("Prazo (AAAA-MM-DD): ")
        if validar_data(prazo):
            break
        else:
            print("Data inválida. Use o formato AAAA-MM-DD e certifique-se de que a data existe.")

    nova_tarefa = {
        "descricao": descricao,
        "prazo": prazo,
        "concluida": False
    }

    tarefas = carregar_tarefas()
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    tarefas = carregar_tarefas()
    tarefas.sort(key=lambda tarefa: datetime.strptime(tarefa["prazo"], "%Y-%m-%d"))

    for i in range(len(tarefas)):
        tarefa = tarefas[i]
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        prazo_formatado = datetime.strptime(tarefa["prazo"], "%Y-%m-%d").strftime("%d-%m-%Y")
        print(f"{i + 1}. {tarefa['descricao']} - Prazo: {prazo_formatado} - Status: {status}")

def marcar_tarefa_como_concluida():
    listar_tarefas()
    numero = input("Digite o número da tarefa que você concluiu: ")

    if numero.isdigit():
        numero = int(numero)
        tarefas = carregar_tarefas()

        if numero >= 1 and numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    else:
        print("Digite um número válido.")

def menu():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_tarefa_como_concluida()
        elif opcao == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
