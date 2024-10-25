from Banco import ContaCorrente, CartaoCredito

#programa

conta_lira = ContaCorrente("lira","111.222.333.45", "452788","1897")
conta_lira.consultar_saldo()

conta_maeLira = ContaCorrente("Beth", "222.333.444-55", "55555", "656565")
# conta_maeLira.consultar_saldo()

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


#programa
conta_lira = ContaCorrente("lira","111.222.333.45", "1234","34062")
cartao_Lira = CartaoCredito("Lira",conta_lira)
#numero aleatoriio exemplo
cartao_Lira.num=190
#retorna o numero da contas associada ao cartao de lira
print(cartao_Lira.conta_corrente._num_conta)
#retorna a lista de cartoes associados a conta corrente
print(conta_lira._cartoes)
#acessando o primeiro item da lista
print(conta_lira._cartoes[0].num)
print( cartao_Lira.num, 
      cartao_Lira.titular,
      cartao_Lira.validade,
      cartao_Lira.cod_seg,
      cartao_Lira.limite,
      )
print(cartao_Lira.__dict__)