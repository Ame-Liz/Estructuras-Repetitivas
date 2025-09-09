n = int(input("Ingresa cuantos renglones en la piramide quieres: "))

for i in range(1, n + 1):
    vacio = " " * (n - i)
    sim = "*" * (2 * i - 1)
    print(vacio + sim)
