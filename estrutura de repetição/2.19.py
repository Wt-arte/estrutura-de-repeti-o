menos_12 = 0
entre_12_59 = 0
maior_60 = 0
for i in range(1, 8):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    while idade < 0:
        print("Idade inválida! Digite novamente.")
        idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    if idade < 12:
        menos_12 += 1
    elif idade <= 59:
        entre_12_59 += 1
    else:
        maior_60 += 1
print(f"Quantidade de pessoas com menos de 12 anos: {menos_12}")
print(f"Quantidade de pessoas entre 12 e 59 anos: {entre_12_59}")
print(f"Quantidade de pessoas com 60 anos ou mais: {maior_60}")
