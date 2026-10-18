numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero1 == numero2:
    print(f"{numero1} es igual a {numero2}")
else:
    print(f"{numero1} es menor que {numero2}")