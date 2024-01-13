# algoritmo para praticar o uso de vetores e matrizes

portugues = []
matematica = []
historia = []

print("=== Escola Matrix ===")

try:

    for i in range(1,3+1):
        nota = float(input(f"Insira a {i}ª nota de Português: "))
        portugues.append(nota)

    for j in range(1,3+1):
        nota = float(input(f"Insira a {j}ª nota de Matemática: "))
        matematica.append(nota)

    for k in range(1,3+1):
        nota = float(input(f"Insira a {k}ª nota de História: "))
        historia.append(nota)

except ValueError:
    print("Por favor, digite um número válido.")

notas_gerais = portugues + matematica + historia
media_geral = sum(notas_gerais) / len(notas_gerais)

media_p = sum(portugues) / len(portugues)
media_m = sum(matematica) / len(matematica)
media_h = sum(historia) / len(historia)

print(f"\nSuas notas em português: {portugues}")
print(f"Média em português: {media_p:.1f}\n")

print(f"Suas notas em matemática: {matematica}")
print(f"Média em matemática: {media_m:.1f}\n")

print(f"Suas notas em história: {historia}")
print(f"Média em história: {media_h:.1f}")

print(f"Media geral: {media_geral:.1f}")
