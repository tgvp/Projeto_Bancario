# Projeto Bancário

class ContaBancaria:
    
    # padrão de cores para print de mensagens
    _azul = '\033[94m'
    _vermelho = '\033[91m'
    _branco = '\033[97m'
    _verde = '\033[92m'
    
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.extrato = []
        self._limite_saque = 3
        
    def depositar(self, valor):
        self.saldo += valor
        # print com valor em _azul
        self.extrato.append(f'Depósito: R$ {self._azul}{valor:.2f}{self._branco}')
        print(f'\n\t> {self._azul}Depósito efetuado com sucesso!{self._branco}')
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f'Saque: R$ {self._vermelho}{valor:.2f}{self._branco}')
            print("\n\t> Retire seu dinheiro ...")
            self._limite_saque -= 1
        else:
            print(f'\t> {self._vermelho}Saldo insuficiente!{self._branco}') 
            
    def get_extrato(self):
        return self.extrato
    
    def get_saldo(self):
        if self.saldo:
            print(f'\n\t> Saldo: {self._verde}R$ {self.saldo:.2f}{self._branco}')
        else:
            print(f'\n\t> Saldo: {self._vermelho}R$ {self.saldo:.2f}{self._branco}')
    
    @property
    def possui_movimentacoes(self):
        return True if self.extrato else False
    
    @property
    def possui_limite_diario(self):
        return True if self._limite_saque else False
    
    def display_menu(self):
        return """
    Sistema Bancário

        [d] - Depositar
        [s] - Sacar
        [e] - Extrato

        [q] - Sair

    Opção: """


def main():
    
    conta = ContaBancaria()
    
    while True:
        opcao = input(conta.display_menu()).lower()
        try:
            match opcao:
                
                # Depósito
                case 'd':
                    
                    valor = float(input('\t> Valor do depósito: '))
                    
                    if valor > 0:
                        conta.depositar(valor)
                    else:
                        print('\n\t> Valor inválido! Informe um valor maior que R$ 0.00')
                
                # Saque
                case 's':
                    
                    if conta.possui_limite_diario:
                        
                        valor = float(input('\t> Valor do saque: '))
                        
                        if 0 < valor <= 500:
                            conta.sacar(valor)
                            conta.get_saldo()
                            print(f'\n\t> Saques restantes: {conta._limite_saque}')
                        
                        elif valor > 500:
                            print('\n\t> Limite de saque por operação: R$ 500,00\n\t- Informe um valor menor!')
                        
                        else:
                            print('\n\t> Valor inválido! Informe para saque acima de R$ 0.00')
                        
                    else:
                        print('\n\t> Limite diário de saques atingido!\n\t- Para aumentá-lo, entre em contato com o banco.')
                
                # Extrato
                case 'e':
                    
                    if conta.possui_movimentacoes:
                        print('\n\t> Extrato:', *conta.extrato, sep='\n\t\t- ')
                    else:
                        print('\n\t> Sem movimentações!')
                    
                    conta.get_saldo()
                
                # Sair
                case 'q':
                    print('\n\t> Saindo...')
                    break
                
                case _:
                    print('\n\t> Opção inválida! Tente novamente.')
        
        except Exception as e:
            print(f'\n\t> Valor inválido!\n\t{e}')
        
        
    
if __name__ == '__main__':
    main()