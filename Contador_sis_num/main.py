from binario import *
from decimal import *
from hexadecimal import *
from octal import *

opc = input("Seleccione en que sistema quiere contar: \n 1. decimal \n 2. binario \n 3. hexadecimal \n 4. octal")

if opc == "1":
    count = Decimal()
    count.avanzar(10)
elif opc == "2":
    count = Binario()
    count.avanzar(10)
elif opc == "3":
    count = Hexadecimal()
    count.avanzar(10)
else:
    count = Octal()
    count.avanzar(10)