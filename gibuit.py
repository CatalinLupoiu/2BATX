#!/usr/bin/env python
# -*- coding: utf-8 -*-


numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 0:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print "Dígame la palabra", (i+1)
        palabra = raw_input()
	lista += [palabra]
    print"La lista creada es:",lista
inversa3=[]
for i in lista :
	inversa3 = [i]+inversa3
print"La lista inversa es:", inversa3
