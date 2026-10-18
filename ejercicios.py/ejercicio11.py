temperatura = int(input("ingrese la temperatura: "))
if temperatura < 10:
    print("fio")
elif temperatura >=10 and temperatura < 25:
    print("templado")
elif temperatura >= 25 and temperatura < 35:
    print("caluroso")
else:
    print("muy caluroso")
