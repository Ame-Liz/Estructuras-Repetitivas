n= int (input("Ingresa cuantos numeros pares quieres contar "))
suma =0

for i in range(2,n+1,2):
    suma = suma + i

print (" La suma de ", n, "numeros pares es: ",suma)
