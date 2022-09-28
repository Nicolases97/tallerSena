#TALLER 6 PYTHON
print("AUTOR(A): Nicolas Esteban Zapata Fontecha")
#FECHA: 28 - Septiembre - 2022

from datetime import date
hoy = date.today()
print("Hoy es el dia: ", hoy)
print()
print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
num1= int(input("Digite un numero: "))
print("***Ciclo controlado por contador***")
i=1
while i <= num1:
    print(i)
    i+=1
print("Fin del ciclo")

print()
print("***Ciclo controlado por eventos***")
i=1
numero1 = 5
numero2 = int(input("Digite un numero entre 1 a 10: "))
while numero2 != numero1:
    i+=1
    print("*No has acertado al numero")
    numero2 = int(input("Digite un numero entre 1 a 10: "))
print("Acertaste en el intento No.", i)
print("Fin del ciclo")

print()
print("***Ciclo abortado con la sentencia break***")
amistad= input("Digite nombre de una amigo: ")
amistad = amistad.upper()
for character in amistad:
    print(character)
    if character == "A":
        break
print("Fin del ciclo")
print()
print("FIN")
