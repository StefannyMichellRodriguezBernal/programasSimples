import math 
TemperaturaInicial = float(input("temperatura inicial del huevo: "))
TemperaturaEbu = 100
M = 47
P = 1.038
C = 3.7
K = 0.0054

dividiendo = math.pow(M, (2/3)) * (C * (math.pow(P, (1/3))))
divisor = (K * math.pow(math.pi,2)) * math.pow((4*math.pi) /3, (2/3))
resultado = dividiendo/divisor 
resultado2 = math.log(0.76 * ((TemperaturaInicial - TemperaturaEbu) / (70 - TemperaturaEbu)))
segundos = resultado * resultado2
minutos = round(segundos/60)

print(f"el tiempo maximo para prepararlo a la copa {round(segundos)} segundos")
print(f"el tiempo maximo para prepararlo a la copa {minutos} minutos")
