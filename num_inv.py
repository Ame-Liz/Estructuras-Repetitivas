n = int(input("Ingresa un número entero: "))

signo = -1 if n < 0 else 1
n = abs(n)

inv = 0
while n > 0:
    digito = n % 10
    inv = inv * 10 + digito
    n //= 10

inv *= signo

print("Número invertido:", inv)
