# Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
c1 = int(input("ingrese la primera nota del certamen"))
c2 = int(input("ingrese la segunda nota del certamen"))
nl = int(input("ingre una nota de laboratorio"))

nc = (59.5 - 0.3 * nl)/0.7
c3 = 3 * nc - (c1 + c2) + 1

print("necesita nota", int(round(c3)), "en el certamen 3")
