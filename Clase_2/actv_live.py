# Crea dos listas lista_1 y lista_2, con cualquier elemento que quieras.
# Realiza los siguientes puntos usando las funciones integradas ya vistas y el método slice [ : ] 
# Imprime la lista correspondiente luego de cada punto.

lista_1= ["Boca Juniors","River Plate"]
lista_2= ["Lunes","Martes","Miercoles"]

# Añade a la lista_1 el 456789 y luego el "Hola Mundo"
lista_1.append(456789)
lista_1.append("Hola Mundo")

print(lista_1)

# Luego añade a la lista_2 el "Hola y adiós", y luego el 5555
lista_2.append("Hola y adios")
lista_2.append(5555)

print(lista_2)

# Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento [:]
lista_3= lista_1[:-1]
print(lista_3)

# Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento [:]
lista_4= lista_2[1:-1]

print(lista_4)

# Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3
lista_5= lista_4 + lista_3

print(lista_5)


# Actividad: Desafío de Tuplas
# Consigna:
# A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:
# Copia esta tupla para iniciar el ejercicio

tupla= (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

print("\nTupla: ",tupla)
listita= sorted(tupla)
print("\nOrdenada: ",listita)


#El último ítem de tupla
print("\nUltimo de tupla: ",tupla[-1])

#El número de ítems de tupla
print("\nLa tupla tiene: ",len(tupla)," elementos")

#La posición donde se encuentra el ítem 87 de tupla
posicion= tupla.index(87)
print(f"\n87 se encuentra en la posicion {posicion+1}")

#Una lista con los últimos tres ítems de tupla
lista_ultimos= tupla[-3:]
print(lista_ultimos)

#Un ítem que haya en la posición 8 de tupla
print(tupla[7])

#El número de veces que el ítem 7 aparece en tupla
cantidad = tupla.count(7)
print("\nEl 7 aparece: ",cantidad, " veces")

