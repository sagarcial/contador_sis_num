from contador import Contador
class Hexadecimal(Contador):
    def __init__(self):
        self.valor = 0
        self.tope = 0
    def avanzar_hexadecimal(self, tope):
        for i in range(tope + 1):
            print(hex(i)[2:])

if __name__ == "__main__":
    count = Hexadecimal()
    count.avanzar_hexadecimal(100)