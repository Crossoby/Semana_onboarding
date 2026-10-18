numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))
suma = numero1 + numero2
resta = numero1 - numero2
if suma > 10:
    print(f"La suma de {numero1} y {numero2} es {suma}, que es mayor que 10")
elif suma == 10:
    print(f"La suma de {numero1} y {numero2} es {suma}, que es igual a 10")
else:
    print(f"La suma de {numero1} y {numero2} es {suma}, que es menor que 10")       
if resta < 10:
    print(f"La resta de {numero1} y {numero2} es {resta}, que es menor que 10")
elif resta == 10:
    print(f"La resta de {numero1} y {numero2} es {resta}, que es igual a 10")
else:
    print(f"La resta de {numero1} y {numero2} es {resta}, que es mayor que 10") 
