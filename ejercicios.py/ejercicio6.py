numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))   
op = input("Ingresa la operación que deseas realizar (+, -, *, /): ")
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
if op == "+":
    print(f"La suma de {numero1} y {numero2} es {suma}")
elif op == "-":
    print(f"La resta de {numero1} y {numero2} es {resta}")
elif op == "*":
    print(f"La multiplicación de {numero1} y {numero2} es {multiplicacion}")
elif op == "/" and numero2 != 0:
    print(f"La división de {numero1} y {numero2} es {division}")
else:
    print("Operación no válida o división por cero.")
