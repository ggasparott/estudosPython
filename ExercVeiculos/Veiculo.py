from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
    
    def exibir_detalhes(self):
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")

    @abstractmethod
    def mover(self):
        pass