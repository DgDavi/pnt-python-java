def criar_mapa_assentos(filas, colunas):
    return [['O' for _ in range(colunas)] for _ in range(filas)]

def exibir_mapa(mapa_assentos):
    print("Mapa de Assentos (O = Disponível, X = Reservado):")
    for i, fila in enumerate(mapa_assentos):
        print(f"Fila {i + 1}: {' '.join(fila)}")
    print()

def reservar_assento(mapa_assentos, fila, coluna):
    if mapa_assentos[fila][coluna] == 'O':
        mapa_assentos[fila][coluna] = 'X'
        print(f"Assento na fila {fila + 1}, coluna {coluna + 1} reservado com sucesso!")
    else:
        print(f"Assento na fila {fila + 1}, coluna {coluna + 1} já está reservado.")
    print()

def cancelar_reserva(mapa_assentos, fila, coluna):
    if mapa_assentos[fila][coluna] == 'X':
        mapa_assentos[fila][coluna] = 'O'
        print(f"Reserva do assento na fila {fila + 1}, coluna {coluna + 1} cancelada com sucesso!")
    else:
        print(f"Assento na fila {fila + 1}, coluna {coluna + 1} não está reservado.")
    print()


filas, colunas = 5, 5
mapa_assentos = criar_mapa_assentos(filas, colunas)

while True:
    print("1. Visualizar mapa de assentos")
    print("2. Reservar um assento")
    print("3. Cancelar uma reserva")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        exibir_mapa(mapa_assentos)
    elif opcao == '2':
        try:
            fila = int(input("Informe o número da fila: ")) - 1
            coluna = int(input("Informe o número da coluna: ")) - 1
            reservar_assento(mapa_assentos, fila, coluna)
        except (ValueError, IndexError):
            print("Entrada inválida. Tente novamente.\n")
    elif opcao == '3':
        try:
            fila = int(input("Informe o número da fila: ")) - 1
            coluna = int(input("Informe o número da coluna: ")) - 1
            cancelar_reserva(mapa_assentos, fila, coluna)
        except (ValueError, IndexError):
            print("Entrada inválida. Tente novamente.\n")
    elif opcao == '4':
        print("Encerrando o sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
