deposito = 15
total_guardado = 0

for semana in range(1, 7):
    print(f"Semana {semana}: R$ {deposito:.2f}")
    total_guardado += deposito
    deposito += 5
print(f"Total guardado após as 6 semanas: R$ {total_guardado:.2f}")