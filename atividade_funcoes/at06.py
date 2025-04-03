def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = sum(1 for char in texto if char in vogais)
    return contador

# Exemplo de uso
frase = "quero comer"
print(f"Quantidade de vogais: {contar_vogais(frase)}")