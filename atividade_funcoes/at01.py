def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."


print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação desejada: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == "1":
    print("Resultado:", soma(num1, num2))
elif operacao == "2":
    print("Resultado:", subtracao(num1, num2))
elif operacao == "3":
    print("Resultado:", multiplicacao(num1, num2))
elif operacao == "4":
    print("Resultado:", divisao(num1, num2))
else:
    print("Operação inválida.")

