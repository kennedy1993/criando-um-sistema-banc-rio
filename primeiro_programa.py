class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} efetuado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} efetuado com sucesso.")
        elif valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")


# Exemplo de uso da classe ContaBancaria
conta = ContaBancaria(1000)  # Criando uma conta com saldo inicial de R$1000

conta.deposito(500)  # Fazendo um depósito de R$500
conta.verificar_saldo()  # Verificando o saldo

conta.saque(200)  # Fazendo um saque de R$200
conta.verificar_saldo()  # Verificando o saldo novamente

conta.saque(2000)  # Tentando sacar um valor maior que o saldo disponível
