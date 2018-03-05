# coding: utf-8
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra:")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:",["Carmen","Alberto","Benito","Carmen"])

num1= raw_input("Dígame la palabra a buscar:")
count=lista.count (num1)
if count == 0:
 print ("La palabra", num1," no aparece en la lista")
elif count == 1:
 print ("la palabra", num1, " aparece en la lista")
else:
 print ("la palabra no aparece en la lista")
