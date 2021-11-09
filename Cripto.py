
senha_escolhida = input("Crie sua senha:")

locked = False
acertou = False
palavra_acertada = ["_" for caractere in senha_escolhida]

print("Escolha o nivel de encriptacao")
print("(1) Fácil, (2) Médio, (3) Difícil")
numero_de_tentativas = int(input("Nivel: ")

if(nivel == 1):
    total_de_tentativas = 15
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5

                           
print(palavra_acertada)

while (not locked and not acertou):

    chute = str(input("Digite uma letra ou numero: "))
    chute = chute.upper()

    if (chute in senha_escolhida):
        sequencia = 0
        for caractere in senha_escolhida:
            if (chute == caractere):
                palavra_acertada[sequencia] = caractere
            sequencia += 1
    else:
        total_de_tentativas -= 1

    locked = total_de_tentativas == 0
    acertou = "_" not in palavra_acertada
    print(palavra_acertada)

if (palavra_acertada == senha_escolhida):
    print(senha_escolhida)
