as_number = int(input("Ingrese el número de AS BGP: "))

# AS privados: 64512 - 65534 (RFC 6996)
if 64512 <= as_number <= 65534:
    print(f"El AS {as_number} es PRIVADO.")
else:
    print(f"El AS {as_number} es PÚBLICO.")
