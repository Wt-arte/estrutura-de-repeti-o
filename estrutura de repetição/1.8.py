a = 0
b = 0
for i in range(1, 6):
    idade = int(input(f"Digite a idade do {i}º estudante: "))
    while idade < 0:
        print("Idade inválida! Digite novamente.")
        idade = int(input(f"Digite a idade do {i}º estudante: "))

    if idade == 16:
        a += 1
        print(f"O estudante {i} tem 16 anos.")
    elif idade > 16:
        b += 1
        print(f"O estudante {i} tem mais de 16 anos.")
print(f"Quantidade de estudantes com 16 anos: {a}")
print(f"Quantidade de estudantes com mais de 16 anos: {b}")