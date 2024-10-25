class Agencia:
    def __init__(self, user_telefone, user_cnpj, num):
        self.user_telefone = user_telefone
        self.user_cnpj = user_cnpj
        self.num = num
        self.clientes = []
        self.caixa = 0
        self.user_emprestimos = 0
        
        def VerificarCaixa(self):
            if self.caixa < 1000000:
                print('Caixa abaixo do nivel recomendado. Caixa Atual: {}'.format(self.caixa))
            else:
                print('O valor de Caixa está ok. Caixa Atual: {}'.format(self.caixa))

        def Emprestimos(self, valor, user_cpf, juros):
            if self.caixa>valor:
                self.user_emprestimos.append((valor, user_cpf, juros))
                print('Empréstimo efetuado com sucesso!')
            else:
                print('Não foi possível efetuar o empréstimo. Dinheiro não disponível.')
        
        def Add_Cliente(self, user_name, user_cpf, user_patrimonio):
            self.clientes.append((user_name, user_cpf, user_patrimonio))



agencia1 = Agencia(22223333, 20000000, 4568)
agencia1.caixa = 1000000
print(agencia1.__dict__)
# agencia1.verificar_caixa()
agencia1.user_emprestimos(10,11122233344, 0.1)
agencia1.Add_Cliente('Lira', 11122233344, 10000)
print(agencia1.clientes)

class AgenciaVirtual(Agencia):
    def __init__(self, site, user_telefone, user_cnpj):
        self.site = site
        super().__init__(user_telefone, user_cnpj, num)
        self.caixa_paypal = 0

        def DepositarPaypal(self, valor):
            self.caixa -= valor
            self.caixa_paypal += valor

        def SacarPaypal(self)    :
            self.caixa_paypal -= valor
            self.caixa += valor
    pass
class AgenciaComum(Agencia):
    def __init__(self, user_telefone, user_cnpj):
        super().__init__(user_telefone, user_cnpj, randint(1001, 9999))
        self.caixa = 1000000
    pass
class Agenciapremium(Agencia):
    def __init__(self, user_telefone, user_cnpj):
        super().__init__(user_telefone, user_cnpj, randint(1001, 9999))
        self.caixa = 1000000

    def Add_Cliente(self, user_name, user_cpf, user_patrimonio):
        if user_patrimonio>1000000:
            super().adicionar_cliente(user_name, user_cpf, user_patrimonio)
        else:
            print('Cliente não possui o patrimonio minimo necessario.')    
    pass

agencia_virtual= AgenciaVirtual(22224444, 1520000000, 1000)
print(AgenciaVirtual.__dict__)
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 22224444,152000000000)
agencia_virtual.verificar_caixa()
print(agencia_virtual.__dict__)

agencia_comum = AgenciaComum(33334444, 222000000000)
agencia_comum.verficar_caixa()
print(agencia_comum.__dict__)

agencia_premium = Agenciapremium(33333333, 30000000000000)
print('agencia_premium:')
print(agencia_premium,__dict__)

agencia_virtual.depositar_paypal(20000)
print (agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

agencia1.Add_Cliente('Lira', 1111111111, 10000000)
print('clientes agencia 1: ', agencia1.clientes)

agencia_virtual.Add_Cliente('Lira', 1111111111, 10000000)
print('clientes agencia virtual: ', agencia_virtual.clientes)

agencia_comum.Add_Cliente('Lira', 1111111111, 10000000)
print('clientes agencia comum: ', agencia1.clientes)

agencia_premium.Add_Cliente('Lira', 1111111111, 10000000)
print('clientes agencia premium: ', agencia_premium.clientes)
