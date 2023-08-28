from contador import Contador
class Decimal(Contador):
    def __init__(self):
        self.valor = 0
        self.tope = 0
    def avanzar(self, tope):
        self.tope = tope
        for i in range (self.tope):
            self.valor =+ i
            print(self.valor)

    
