numero = 0
for i in range(1, 7):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    par = numero % 2 == 0
    if par:
        print(f"O {i}º número digitado é par")
    else:
        print(f"O {i}º número digitado é impar")