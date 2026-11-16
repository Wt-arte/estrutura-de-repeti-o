valido = []
for i in range(1, 10):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    if numero % 3 == 0 and numero % 5 == 0:
        valido.append(numero)
    else:
        invalido = 0
print(f"Os números digitados que são múltiplos de 3 e 5 são: {valido}")
print(f"A somas dos números digitados que são múltiplos de 3 e 5 é: {sum(valido)}")