import random

C_validos= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

long = int(input("Ingrese la longitud de la contraseña: "))

contra = input("Ingrese la contraseña:")

empty = ""

for i in range (long):
    empty = (str(contra)[-10:]) + random.choice(C_validos)

print("La contraseña generada es: ", empty)