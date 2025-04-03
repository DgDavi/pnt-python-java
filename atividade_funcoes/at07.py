import random

def rolar_dado():
    return random.randint(1, 6)

# Exemplo de uso
resultado = rolar_dado()
print(f"O número sorteado foi: {resultado}")