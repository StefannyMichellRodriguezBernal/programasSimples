# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
numero = int(input("ingresa un numero de 3 digitos"))
centena = numero/100
decena = (numero%100)/10
unidad = (numero%100)%10
print("%d%d%d"%(unidad, decena, centena))
