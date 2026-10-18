compra = float(input("Ingrese el valor de su compra: "))
if compra >= 200000: 
    print(f"su compra se le hizo un descuento del 20% quedando un total de {compra -(compra * 0.20)}")
elif compra >= 100000: 
    print(f"su compra tiene un descuento del 10% quedando un total de {compra -(compra * 0.10)}")
else:
    print(f"el valor total de su compra es {compra}")