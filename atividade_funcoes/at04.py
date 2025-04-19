def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    
    if media >= 7:
        status = 'Aprovado'
    else:
        status = 'Reprovado'

    return media, status


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media, status = calcular_media(nota1, nota2, nota3)
print(f"Média: {media:.2f}")
print(f"Status: {status}")
