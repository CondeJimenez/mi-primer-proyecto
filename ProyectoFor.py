# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.

num = int(input("Ingrese un numero: "))
if num < 1:
    print("Imposible, escribe un numero mayor a 0")
else:
    for i in range(num):
        print(i)