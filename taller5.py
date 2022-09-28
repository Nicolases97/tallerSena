#TALLER 5 PYTHON
print("AUTOR(A): Nicolas Esteban Zapata Fontecha")
#FECHA: 28 - Septiembre - 2022

from datetime import date
hoy = date.today()
print("Hoy es el dia: ", hoy)
print()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()
num1= int(input("Digite el primer numero: "))
num2= int(input("Digite el segundo numero: "))
print("Ciclo para el primer numero")
for i in range(num1):
    print(i)
print("Fin del ciclo")

print()
print("Ciclo desde el primer numero hasta el segundo numero")
for i in range(num1,num2):
    print(i)
print("Fin del ciclo")

print()
print("Ciclo desde el primer numero hasta el segundo numero con incrementos de 2")
for i in range(num1,num2,2):
    print(i)
print("Fin del ciclo")

print()
empresa= input("Digite nombre de una empresa: ")
empresa = empresa.lower()
for character in empresa:
    print(character)
print("Fin del ciclo")

print()
print("FIN")