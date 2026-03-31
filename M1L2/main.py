import random

C_validos= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

long = int(input("Ingrese la longitud de la contraseña: "))

empty = ""

for i in range (long):
    empty = empty + random.choice(C_validos)

print("La contraseña generada es: ", empty)