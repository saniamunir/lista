# coding: utf-8
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:",["Alberto","Benito","Carmen"])
