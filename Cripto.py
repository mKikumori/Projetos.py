
senha_escolhida = input("Crie sua senha:")

locked = False
time_out = False
acertou = False
palavra_acertada = ["_" for caractere in senha_escolhida]
errou = 0

print("Escolha o nivel de encriptacao")
print("(1) Fácil, (2) Médio, (3) Difícil")
numero_de_tentativas = int(input("Nivel: ")

if(numero_de_tentativas == 1):
    total_de_tentativas = 5
elif(numero_de_tentativas == 2):
    total_de_tentativas = 3
elif(numero_de_tentatuvas == 3):
    total_de_tentativas = 1
                           
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
        errou += 1

    locked = errou == len(senha_escolhida)
    acertou = "_" not in palavra_acertada
    print(palavra_acertada)

                           
    if (locked = True):
        total_de_tentativas -= 1
            if (total_de_tentativas == 0):
                print("Timed-out")
                           
print("Fim")
