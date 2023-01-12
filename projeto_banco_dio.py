menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 1 
LIMITE_SAQUES = 3
numero_depositos = 0
extrato_depositos = {}
extrato_saques = {}

while True:
	
	opcao = input(menu)
	
	if opcao == "d": 
		print("Depósito\n")
		print("Qual valor deseja depositar?")
		
		valor_deposito = float(input())

		if valor_deposito < 0:
			print("Deposite um valor positivo!")
		else:
			saldo = saldo + valor_deposito
			extrato_depositos[str(numero_depositos)] = valor_deposito
			numero_depositos += 1
	
	elif opcao == "s": 
		print("Saque")
		print("Qual valor deseja sacar?")

		valor_saque = float(input())

		if valor_saque <= 500 and numero_saques <= LIMITE_SAQUES and valor_saque <= saldo: #Pode sacar
			saldo = saldo - valor_saque
			extrato_saques[str(numero_saques)] = valor_saque
			numero_saques += 1
		elif valor_saque < 0: #Não pode sacar, valor negativo
			print("Saque um valor positivo!")
		elif numero_saques > LIMITE_SAQUES: #Limite de saques atingido
			print("Limite diário de saques atingido!")
		elif valor_saque >= saldo and valor_saque <= 500: #Saldo insuficiente
			print("Saldo insuficiente!")
		else:
			print("Seu valor limite de saque é R$ 500!")

	elif opcao == "e":
		print("Extrato")
		print(f"\nSeu saldo é R$ {saldo:.2f}")
        
		print("\nDepósitos:")
		for ler_depositos in range(0,numero_depositos):
			print(f"R$ {extrato_depositos[str(ler_depositos)]:.2f}")

		print("\nSaques")
		for ler_saques in range(1,numero_saques):
			print(f"R$ {extrato_saques[str(ler_saques)]:.2f}")

	
	elif opcao == "q":
		break

	else:
		print("Operação inválida, por favor selecione novamente a operação desejada")