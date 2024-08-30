import random 

caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890:;<=>?@#$%&'()*+,-./"
contraseña = " "

longitud = int(input("Ingrese la longitud de la contraseña a generar: "))

for _ in range(longitud):
    contraseña += random.choice(caracteres)

print ("Su contraseña es: " + contraseña)