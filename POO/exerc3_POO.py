class Veiculo:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa
        # SInicializando o combustivel em 100 e a quilometragem em 0
        self.combustivel = 100
        self.quilometragem = 0

    def viajar(self, distancia):
        # 1. Aumente a quilometragem do veículo com base na distância
        self.quilometragem += distancia

        # 2. Diminua o combustível (1% por km)
        self.combustivel -= distancia

        # 3. Dê um print avisando que o veículo viajou X km
        print(f"O {self.modelo} (Placa: {self.placa}) viajou {distancia} km.")

        pass

    def abastecer(self):
        # 1. Altere o combustível de volta para 100
        self.combustivel = 100

        # 2. Dê um print avisando que o tanque está cheio
        print(f"O tanque do {self.modelo} foi reabastecido e está em 100%!")
        pass


# --- ÁREA DE TESTES (Não mexa aqui, use para testar seu código) ---
# carro = Veiculo("Fiorino", "XYZ-9876")
# carro.viajar(30)
# print(f"Combustível atual: {carro.combustivel}%")
# print(f"KM atual: {carro.quilometragem} km")
# carro.abastecer()


# --- ÁREA DE TESTES (Não mexa aqui, use para testar seu código) ---
carro = Veiculo("Fiorino", "XYZ-9876")
carro.viajar(30)
print(f"Combustível atual: {carro.combustivel}%")
print(f"KM atual: {carro.quilometragem} km")
carro.abastecer()