# 1 Primer programa

name_user = input("Ingrese nombre: ").strip()
edad_user = int(input("Ingrese edad: "))

print(f"{name_user} tiene {edad_user} años")

# 2 Desafio string

cadena_1 = "versátil"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programación"

print(f"{cadena_2} {cadena_3} {cadena_4} {cadena_1}") 

# 3 Desafio numeros
def promedio_partidos(ganados: int,perdidos: int,empatados: int) -> float :
    return float(((ganados * 3) + (empatados * 1)) / 12)

p_ganados= int(input("Partidos ganados: "))
p_empatados= int(input("Partidos empatados: "))
p_perdidos= int(input("Partidos perdidos: "))

promedio_equipo = promedio_partidos(p_ganados,p_perdidos,p_empatados)

print(f"Promedio: {promedio_equipo:.2f}")

# 4 Desafio slicing

cadena = "acitametaM ,5.8 ,otipeP ordeP"

cadena_voltada= cadena[::-1]
partes= cadena_voltada.split(",")


nombre_alumno= partes[0].strip()
nota= partes[1].strip()
materia= partes[2].strip()

print(f"{nombre_alumno} ha sacado un {nota} en {materia}")