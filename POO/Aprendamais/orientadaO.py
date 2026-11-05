class Funcionario:
  def __init__(self, nome, salario, cargo):
    self.nome = nome
    self.salario = salario
    self.cargo = cargo

  def calcular_bonus(self):
    return self.salario * 0.10

  def exibir_dados(self):
    print(f"Nome: {self.nome}")
    print(f"Cargo: {self.cargo}")
    print(f"Salário: R$ {self.salario}")

# Uso
func1 = Funcionario("Maria Silva", 5000, "Desenvolvedora")
func2 = Funcionario("João Santos", 4500, "Analista")

bonus1 = func1.calcular_bonus()
func1.exibir_dados()