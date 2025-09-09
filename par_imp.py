n = int(input("¿Cuántos números par e impar deseas contar?: "))

par = 0
imp = 0

for i in range(1, n + 1):
    par += i * 2

for i in range(1, n + 1):
    imp += (2 * i) - 1

print("La suma de los primeros", n, "números pares es:", par)
print("La suma de los primeros", n, "números impares es:", imp)
