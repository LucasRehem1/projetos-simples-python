"""Elabore um algoritmo que receba do usuário “n” números inteiros (quanto ele quiser). O algoritmo deverá ler os n
números e devolver.
O maior e o menor número. A média dos números. A somatória desses números. A produtória desses números
(o resultado da multiplicação de todos eles). A quantidade de números positivos e a quantidade de números
negativos. A quantidade de números pares e a quantidade de números ímpares."""

# Declaro o valor das variaveis
maior = 0
menor = float(100000)
resultado = 0
positivo = 0
negativo = 0
produtoria = 1
impar = 0
par = 0

# Solitia a quantidade de valores que o usuario quer digitar
n = int(input("Quantos valores você quer digitar? "))

# Loop que começa em 1 e vai até o valor da variavel n+1, o +1 é para chegarmos no valor correto
for i in range(1, n+1):

    # Solicita o valor ao usuário
    v = int(input(f"Digite o {i}º valor: "))

    # Armazena o resultado e o resultado da produtoria
    resultado = resultado + v
    produtoria = produtoria * v

    # Armazena o maior número
    if v > maior:
        maior = v

    # Armazena o menor número
    if v < menor:
        menor = v

    # armazena os positivos e negativos
    if v > 0:
        positivo = positivo + 1
    elif v < 0:
        negativo = negativo + 1

    # Armazena os impares e pares
    if v % 2 == 1:
        impar = impar + 1
    elif v % 2 == 0:
        par = par + 1

# Armazena a média
media = resultado / n

# Mostra na tela os resultados
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Resultado: {resultado}")
print(f"Média: {media:.2f}")
print(f"Produtoria: {produtoria}")
print(f"Números positivos: {positivo}")
print(f"Números negativos: {negativo}")
print(f"Números pares: {par}")
print(f"Números impares: {impar}")
