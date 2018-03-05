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

sust = input("palabra a cambiar: ")
sust1=input("palabra nueva: ")

count.lista.count(sust)

for i in range(count):

 num=lista.index(sust)
 lista[num]=sust1
 print lista

