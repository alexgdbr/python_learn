class Cliente:

    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def imprime(self):
        print("Cliente:", self._nome,
              "\nEndereço:", self._endereco)

class Conta:

    _quant = 0

    @classmethod
    def adiciona_conta(cls):
        cls._quant += 1

    @classmethod
    def quantidade(cls):
        return cls._quant

    def __init__(self, numero, cliente):
        self.adiciona_conta
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0

    def depositar(self, valor):
        self._saldo += valor

    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False

    def imprime(self):
        print("conta:", str(self._numero), 
              "\nSaldo:", str(self._saldo))
        self._cliente.imprime()


cliente = Cliente("João da Silva", "Rua A, 123")
conta1 = Conta(1111, cliente)
cliente = Cliente("Maria Oliveira", "Rua B, 456")
conta2 = Conta(2222, cliente)
conta1.depositar(1000.00)
conta1.transferir(conta2, 200.00)
conta1.imprime()
print()
conta2.imprime()
# print("Contas criadas:", Conta.quantidade())
# conta1 = Conta(1111)
# print("Contas criadas:", Conta.quantidade())
# conta2 = Conta(2222)
# print("Contas criadas:", Conta.quantidade())


        
# conta1 = Conta(1111)
# conta2 = Conta(2222)
# conta2.depositar(500.0)
# print("Saldo atual:")
# print("Saldo da conta 1:", conta1.saldo())
# print("Saldo da conta 2:", conta2.saldo())
# conta2.transferir(conta1, 200.0)
# print("Saldo da conta 1:", conta1.saldo())
# print("Saldo da conta 2:", conta2.saldo())

# conta2.depositar(500.0)
# conta2.sacar(1000.0)
