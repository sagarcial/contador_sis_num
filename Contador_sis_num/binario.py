from contador import Contador

class Binario(Contador):
    def __init__(self):
        self.valor = 0
        self.tope = 0

    def avanzar_binario(self, tope):
        for i in range(tope + 1):
            print(bin(i)[2:])


if __name__ == "__main__":
    count = Binario()
    count.avanzar_binario(10)
