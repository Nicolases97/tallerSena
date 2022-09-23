#TALLER 3 PYTHON
#AUTOR(A): Nicolas Esteban Zapata Fontecha
#FECHA: 21-Septiembre-2022

from datetime import date
hoy = date.today()
print("Hoy es el dia",hoy)

a= int (input("Digite el valor de A: "))
b= int (input("Digite el valor de B: "))
if a>=b:
    print("A es mayor o igual a B")
else:
    print("A es menor que B")
print()
curso1= "Requerimientos"
curso2= "Algoritmos"
print("El curso1 es: ", curso1)
print("El curso2 es: ", curso2)
if curso1 == "Requerimientos" and curso2== "Algoritmos":
    print("Usted estudia Programación de Software")
else:
    print("Usted estudia otro programa diferente a Programación de Software")
print()
print("*** Final del analisis del Programa de Formación ***")
print()
frase =input("Digite una frase: ")
print("La frase en Mayuscula es: ", frase.upper())
longitud = len(frase)
print("La longitud de la frase es: ", longitud, "caracteres")
if longitud > 10:
    print("La frase contiene mas de 10 caracteres")
else:
    print("La frase contiene menos de 10 caracteres")
print()
print("FIN")
