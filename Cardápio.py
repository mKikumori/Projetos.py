
#mostrar o cardapio
#escolher uma area do cardapio
#escolhar um prato dentro da area escolhida
#entregar o prato pedido
#finalizar quando estiver satisfeito
#pagar a conta








cardapio = ["Pastas", "Carnes", "Saladas", "Sobremesas", "Bebidas"]
pratos_pastas = ["Prato1", "Prato2", "Prato3", "Prato4"]
pratos_carnes = ["Prato1", "Prato2", "Prato3", "Prato4"]
pratos_saladas = ["Prato1", "Prato2", "Prato3", "Prato4"]
pratos_sobremesas = ["Prato1", "Prato2", "Prato3", "Prato4"]
pratos_bebidas = ["Prato1", "Prato2", "Prato3", "Prato4"]


finalizar_conta = False
satisfeito = False
print(cardapio)

while(not satisfeito and not finalizar_conta):
    pedido = imput("Qual sera seu pedido?")
        if(pedido == "Pastas"):
            print(pratos_pastas)
            prato = imput("Qual sera seu prato?")
        elif(pedido == "Carnes"):
            print(pratos_carnes)
            prato = imput("Qual sera seu prato?")
        elif(pedido == "Saladas")
            print(pratos_saladas)
            prato = imput("Qual sera seu prato?")
        elif(pedido == "Sobremesas")
            print(pratos_sobremesas)
            prato = imput("Qual sera seu prato?")
        elif(pedido == "Sobremesas")
            print(pratos_bebidas)
            prato = imput("Qual sera seu prato?")
        else:
            print("Trarei a conta")
            finalizar_conta = True
            
            
        if(finalizar_conta = True):
            print(conta)
            pagamento = int(imput("Valor entregue para pagar:"))
            if(pagamento < conta):
                print("Seu pagamento nao foi o suficiente")
                continue
            else:
                troco = pagamento - conta
                print(f"Troco de {troco} reais)
                print("Volte sempre")
            
            
