for i in range(1, 7):
    numero = int(input(f"Digite o {i}º número inteiro: "))    
    if i == 1:
        soma = numero
    else:
        soma += numero
print(f"A soma dos números digitados é: {soma}")