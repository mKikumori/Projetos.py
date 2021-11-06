
#mostrar o cardapio
#escolher uma area do cardapio
#escolhar um prato dentro da area escolhida
#entregar o prato pedido
#finalizar quando estiver satisfeito
#pagar a conta








cardapio = ["Pastas(1), Carnes(2), Saladas(3), Sobremesas(4), Bebidas(5)"]
pratos_pastas = ["Prato1", "Prato2", "Prato3", "Prato4"]
pratos_carnes = ["Prato1", "Prato2", "Prato3", "Prato4"]
pratos_saladas = ["Prato1", "Prato2", "Prato3", "Prato4"]
pratos_sobremesas = ["Prato1", "Prato2", "Prato3", "Prato4"]
pratos_bebidas = ["Prato1", "Prato2", "Prato3", "Prato4"]

pratos_pastas[0] = 23.99
pratos_pastas[1] = 32.99
pratos_pastas[2] = 32.00
pratos_pastas[3] = 21.99
pratos_carnes[0] = 52.00
pratos_carnes[1] = 37.00
pratos_carnes[2] = 61.99
pratos_carnes[3] = 34.99
pratos_saladas[0] = 12.99
pratos_saladas[1] = 20.99
pratos_saladas[2] = 14.99
pratos_saladas[3] = 23.00
pratos_sobremesas[0] = 32.99
pratos_sobremesas[1] = 21.99
pratos_sobremesas[2] = 33.00
pratos_sobremesas[3] = 31.99
pratos_bebidas[0] = 9.99
pratos_bebidas[1] = 13.99
pratos_bebidas[2] = 27.00
pratos_bebidas[3] = 39.99

satisfeito = False

while (not satisfeito):
    print(cardapio)
    pedido = int(input("Se deseja pedir algo mais digite o numero do seu pedido:"))
    conta = []
    if (pedido == 1):
        print(pratos_pastas)
        prato = int(input("Qual sera seu prato?"))
        conta.append(prato)
    elif (pedido == 2):
        print(pratos_carnes)
        prato = int(input("Qual sera seu prato?"))
        conta.append(prato)
    elif (pedido == 3):
        print(pratos_saladas)
        prato = int(input("Qual sera seu prato?"))
        conta.append(prato)
    elif (pedido == 4):
        print(pratos_sobremesas)
        prato = int(input("Qual sera seu prato?"))
        conta.append(prato)
    elif (pedido == 5):
        print(pratos_bebidas)
        prato = int(input("Qual sera seu prato?"))
        conta.append(prato)
    else:
        print("Trarei a conta")
        satisfeito = True



    if (satisfeito == True):
        conta_final = sum([conta])
        print(conta)
        pagamento = int(input("Valor entregue para pagar:"))
        if (pagamento < conta_final):
            print("Seu pagamento nao foi o suficiente")
            continue
        else:
            troco = pagamento - conta_final
            print(f"Troco de {troco} reais")
            print("Volte sempre")
