# algoritmo para praticar o uso de vetores e matrizes

# Função para armazenar a nota na disciplina
def obter_nota(disciplina):
    notas = []
    try:
        for i in range(1, 3+1):
            nota = float(input(f"Insira a {i}ª nota de {disciplina} "))
            notas.append(nota)
    except ValueError:
        print("Por favor, digite um número válido.")
    return notas

# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas) if notas else 0

# Apresentando o nome da escola (nome ficticio)
print("=== Escola Matrix ===\n")

# Armazenando o nome do aluno
nome = input("Digite seu nome: ")

# Utilizando a função obter_nota para solicitar e armazenar as notas de cada matéria
portugues = obter_nota("portugues")
matematica = obter_nota("matematica")
historia = obter_nota("historia")

# Armazenando a média geral das notas
notas_gerais = portugues + matematica + historia
media_geral = calcular_media(notas_gerais)

# Utilizando a função calcular_media para calcular a média de cada matéria
media_p = calcular_media(portugues)
media_m = calcular_media(matematica)
media_h = calcular_media(historia)

# Mostrando o nome do aluno na tela
print(f"\nAluno: {nome}")

# Mostrando as notas e as médias de cada matéria na tela
print(f"\nSuas notas em português: {portugues}")
print(f"Média em português: {media_p:.1f}\n")

print(f"Suas notas em matemática: {matematica}")
print(f"Média em matemática: {media_m:.1f}\n")

print(f"Suas notas em história: {historia}")
print(f"Média em história: {media_h:.1f}\n")

print(f"Media geral: {media_geral:.1f}")
