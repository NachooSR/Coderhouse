'''
A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media. Cada nota tiene un valor porcentual:

La primera nota vale un 15% del total

La segunda nota vale un 35% del total

La tercera nota vale un 50% del total
'''

def calcular_promedio(nota_1: int,nota_2: int ,nota_3: int)-> float:
    
    suma= float(nota_1 * 0.15 + nota_2 * 0.35 + nota_3 *0.5)
    return suma

nota_1= 10
nota_2= 7
nota_3= 4

promedio = calcular_promedio(nota_1, nota_2, nota_3)
print(f"El promedio es:{promedio: .2f} ")

# Ejercicio de listas anidadas
matriz = [
[1, 5, 1],
[2, 1, 2],
[3, 0, 1],
[1, 4, 4] ]

for fila in matriz:
    valor_agregar= sum(fila)
    fila.append(valor_agregar)

for fila in matriz:
    for elemento in fila:
        print(f"{elemento} |",end=" ")
    print("\n")

'''
Consigna Sets

Crear un conjunto en Python que posea los siguientes elementos:

Países: Inglaterra, USA, México.

Posteriormente agrega nuestro set de países, los elementos de: Islandia, Italia, Argentina y Portugal, USA

Elimina a los países: Chile e Italia

Pregunta: ¿Qué pasa si queremos eliminar al país Chile utilizando el método remove?, ¿Qué pasó con el element de USA?

'''

paises = {"Inglaterra", "USA","Mexico"}

paises.update(["Islandia","Italia","Argentina","Portugal","USA"])
paises.remove("Italia")
paises.discard("Chile")

#paises.remove("Chile")

# Si queremos remover "Chile" arroja error porque no existe
# El elemento USA se inserta una sola vez





'''
Consigna Dicts

Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre por pantalla:

Ejemplo del output solicitado:

Juan tiene 25 años, y vive en Carrera 7 - Bogotá
'''

name_user = input("Ingrese nombre: ").strip()
edad_user = int(input("Ingrese edad: "))
direccion = input("Ingrese direccion: ").strip()

persona = {
    "name": name_user,
    "edad": edad_user,
    "direccion_person": direccion
}

print(
    f"{persona['name']} tiene {persona['edad']} anios y vive en {persona['direccion_person']}"
)

