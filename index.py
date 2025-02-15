menu = """

[d] = Despositar 💵⬆️
[s] = Sacar 💵⬇️
[e] = Extrato 💵📊
[q] = Sair 🔚

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("🚫 Falha na operação! Por favor informe um valor válido.")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saques >= LIMITE_SAQUES
        
        if saldo_excedido:
            print("🚫 Falha na operação! Saldo insuficiente!")
        
        elif limite_excedido:
            print("🚫 Falha na operação! Valor de saque excedido!")
        
        elif saque_excedido:
            print("🚫 Falha na operação! Limite de saques diários excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    
    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("🚫Não foram realizadas movimentações na conta." if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo:.2f}")
        print("======================================")
    
    elif opcao == "q":
        break
        
    else:
        print("❌ Operação inválida, por favor selecione novamente a operação desejada.")
        