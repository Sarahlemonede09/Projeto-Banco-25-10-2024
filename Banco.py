from datetime import datetime
import pytz

class ContaCorrente():
    """
    Objetivo da aula é criar uma conta corrente para gerenciar as contas 
    dos clientes.

    Atributos:

    noma(str) - nome cliente
    cpf(str) - cpf cliente
    _agencia(str) - _agencia cliente
    _num_conta(str) - numero da conta do cliente
    saldo: saldo disponivel da conta
    _limite: _limite disponivel que o cliente tem
    transações: histórico da movimentação das transações
    do cliente.
    """
    #  FUNÇÕES
    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y  %H: %M:%S')
    
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

    def consultar_saldo(self):
        print('Seu _saldo atual é de R${:,.2f}'.format(self._saldo))
        pass

    def _limite_conta(self):
        self._limite = -1000
        return self._limite   

    def despositar_dinheiro(self,valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente.data_hora()))
        pass

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self,valor):
        if self._saldo -valor < self._limite_conta():
            print('Você não tem _saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((valor, self._saldo, ContaCorrente.data_hora()))
            pass
    def consultar_historico_transacoes(self):
        print ("Histórico de transações: ")
        for transacao in self._transacoes:
            print(transacao)
    
    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente.data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente.data_hora()))
    
    #Conta do responsável

    def __int__(self, nome, cpf, _agencia, _num_conta):
        self.nome = nome
        self._cpf = cpf
        self._saldo = 0
        # self.__limite = None
        self._agencia = _agencia
        self._num_conta = _num_conta
        
#programa

conta_lira = ContaCorrente("lira","111.222.333.45", "452788","1897")
conta_lira.consultar_saldo()

conta_maeLira = ContaCorrente("Beth", "222.333.444-55", "55555", "656565")
conta_maeLira.consultar_saldo()

#Depositando dinheiro na conta:
conta_lira.despositar_dinheiro(1500)
conta_lira.consultar_saldo()

#transferencia de dinheiro
conta_lira.transferir(1000, conta_maeLira)


#Sacando dinheiro da conta
conta_lira.sacar_dinheiro(1000)
conta_lira.consultar_saldo()
conta_lira.consultar_historico_transacoes()

print('Saldo da conta é de = ', conta_lira._saldo)
print("|-----------------------------------------|")
print("Cpf: ", conta_lira._cpf)
print("Agência: ", conta_lira._agencia)
print("Número da Conta: ", conta_lira._num_conta)
print("|-----------------------------------------|")
print(conta_lira._transacoes)
print("|-----------------------------------------|")

# #saldo via metodos
# print (conta_lira.__saldo)
# #tentando mudar o valor do saldo "por fora " do programa
# conta_lira.__saldo = 8000
# #novo valor atribuido apos tentativa de burlar o sistema
# print(conta_lira.__saldo)

# from datetime import datetime
# import pytz
# from random import randint
# class CartaoCredito:

#     @staticmethod
#     def data_hora():
#         fuso_BR = pytz.timezone('Brazil/East')
#         horario_BR = datetime.now(fuso_BR)
#         return horario_BR
    
#     def __int__(self, titular, conta_corrente):
#         self.num = randint(10000000000000000000, 99999999999999999999)
#         self.titular = titular
#         self.validade = '{}/{}', format(CartaoCredito.data_hora().month, CartaoCredito.data_hora().year + 4)
#         self.cod_seg = '{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
#         self._limite = None
#         self.conta_corrente = conta_corrente
#         conta_corrente._cartoes.append(self)




# #programa
# conta_lira = ContaCorrente("lira","111.222.333.45", "1234","34062")
# cartao_Lira = CartaoCredito("Lira",conta_lira)
# #numero aleatoriio exemplo
# cartao_Lira.num=190
# #retorna o numero da contas associada ao cartao de lira
# print(cartao_Lira.conta_corrente._num_conta)
# #retorna a lista de cartoes associados a conta corrente
# print(conta_lira._cartoes)
# #acessando o primeiro item da lista
# print(conta_lira._cartoes[0].num)
# print( cartao_Lira.num, 
#       cartao_Lira.titular,
#       cartao_Lira.validade,
#       cartao_Lira.cod_seg,
#       cartao_Lira.limite,
#       )
# print(cartao_Lira.__dict__)