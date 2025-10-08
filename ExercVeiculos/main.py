from Veiculo import Veiculo
from Carro import Carro
from Bicicleta import Bicicleta

if __name__ == "__main__":
    print("Iniciando testes")
    try:
        veiculo_generico = Veiculo("Marca generico", "Modelo Generico")
    except TypeError as e:
        print(f"Sucesso! O erro aconteceu {e}")

    print("Criando Arquivos testes")

    meu_carro = Carro("Toyota", "Corolla", 4)
    minha_bike = Bicicleta("Caloi", "10", 18)

    meu_carro.exibir_detalhes()
    minha_bike.exibir_detalhes()

    veiculos = [meu_carro, minha_bike]

    for veiculo in veiculos:
        veiculo.mover()