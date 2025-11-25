def calcular_promedio(nota_1,nota_2,nota_3):
    return nota_1 * 0.2 + nota_2 * 0.3 + nota_3 * 0.5


nota_1= float(input("Ingrese 1er nota: "))
nota_2= float(input("Ingrese 2da nota: "))
nota_3= float(input("Ingrese 3er nota: "))


promedio= calcular_promedio(nota_1,nota_2,nota_3)

print(f"El promedio final es {promedio:.2f}")

