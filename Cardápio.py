
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


pratos_pastas[0] = 23.99
pratos_pastas[1] = 45.99
pratos_pastas[2] = 32.00
pratos_pastas[3] = 21.99
pratos_carnes[0] =



satisfeito = False
print(cardapio)

while(not satisfeito):
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
            satisfeito = True
            
            
        if(satisfeito = True):
            print(conta)
            pagamento = int(imput("Valor entregue para pagar:"))
            if(pagamento < conta):
                print("Seu pagamento nao foi o suficiente")
                continue
            else:
                troco = pagamento - conta
                print(f"Troco de {troco} reais)
                print("Volte sempre")
            
            
