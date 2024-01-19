# Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
import math
n = abs(float(input("ingresar numero: ")))
nDecimal, nEntero = math.modf(n)
print("parte decimal: {: .2f}".format(nDecimal))
