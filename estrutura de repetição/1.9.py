soma = 0
for i in range(1, 5):
    nota = int(input(f"Digite a {i}ª nota do aluno de 0 a 10: "))
    soma += nota
media = soma / 4
print(f"A media do aluno é: {media}")