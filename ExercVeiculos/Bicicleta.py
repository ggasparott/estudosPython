from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, marchas):
        super().__init__(marca, modelo)
        self.marchas = marchas
    
    def mover(self):
        print("A bicicleta ta se movendo")
