media = 0
maior = []
for i in range(1, 6):
    nota = int(input(f"Digite a {i}ª nota do aluno de 0 a 10: "))
    while nota < 0 or nota > 10:
        print("Nota inválida! Digite novamente.")
        nota = int(input(f"Digite a {i}ª nota do aluno de 0 a 10: "))
    media += nota
    if nota >= 6:
        maior.append(nota)
media = media / 5
print(f"A media do aluno é: {media}")
if maior:
    print(f"As notas maiores que 6 são: {maior}")
