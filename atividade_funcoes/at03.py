def contar_caracteres_sem_espacos(frase):
    return len(frase.replace(" ", ""))

# Exemplo de uso
frase = "quero comer"
print(f"Número de caracteres: {contar_caracteres_sem_espacos(frase)}")