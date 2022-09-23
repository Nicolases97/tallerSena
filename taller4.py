#TALLER 4 PYTHON
#AUTOR(A): Nicolas Esteban Zapata Fontecha
#FECHA: 21-Septiembre-2022

from datetime import date
hoy = date.today()
print("Hoy es el dia: ", hoy)
print()
print("EJERCICIO DE LAS CLASES DE TRIANGULOS")
a= int(input("Digite el valor de A: "))
b= int(input("Digite el valor de B: "))
c= int(input("Digite el valor de C: "))

if a==b and a==c and b==c:
    print("EL TRIANGULO ES EQUILATERO")
else:
    if a==b or b==c or a==c:
        print("EL TRIANGULO ES ISOCELES")
    else:
        print("EL TRIANGULO ES ESCALENO")
print()
animal = input("Digite un animal: ")
animal = animal.upper()
if animal == "PERRO":
    print("El", animal, "es el mejor amigo del hombre")
elif animal == "GATO":
    print("El", animal,"persigue a los ratones")
elif animal == "OSO":
    print("Al", animal, "le gusta la miel")
else:
    print("El animal no es perro, gato u oso, el animal es: ", animal)
print()
print("FIN")
