lado1 = int(input("Ingrese el lado 1 del triangulo: "))
lado2 = int(input("Ingrese el lado 2 del triangulo: "))
lado3 = int(input("Ingrese el ultimo lado: "))
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    if lado1 == lado2 == lado3:
        print("equilatero")
    elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado2 :
        print("isosceles")
    elif lado1 != lado2 != lado3:
        print("Escaleno")
else:
    print("ingrese triangulo valido")