n = int(input("Ingresa un número entero: "))

n1 = str(abs(n))
contador = 0

for _ in n1:
    contador += 1

print("El número tiene", contador, "dígitos.")
