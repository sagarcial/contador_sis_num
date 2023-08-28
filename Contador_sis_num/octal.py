from contador import Contador
class Octal(Contador):
    def __init__(self):
        self.valor = 0
        self.tope = 0
    def avanzar_octal(self, tope):
        for i in range(tope + 1):
            print(oct(i)[2:])


if __name__ == "__main__":
    count = Octal()
    count.avanzar_octal(10)

