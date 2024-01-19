# Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.
import math

catetoA = int(input("ingresa el primer cateto"))
catetoB = int(input("ingresa el segundo cateto"))

sumaCatetos = catetoA + catetoB 
hipotenusa = math.sqrt(catetoA**2+catetoB**2)

print("la hipotenusa es: %f" % (hipotenusa))

