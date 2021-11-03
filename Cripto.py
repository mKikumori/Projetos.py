
senha_escolhida = input("Crie sua senha:")

total_de_tentativas = 5
locked = False
acertou = False
errou = 0
palavra_acertada = ["_" for caractere in senha_escolhida]

print(palavra_acertada)

while (not locked and not acertou):

    chute = str(input("Digite uma letra ou numero: "))
    chute = chute.strip().upper()

    if (chute in senha_escolhida):
        sequencia = 0
        for caractere in senha_escolhida:
            if (chute == caractere):
                palavra_acertada[sequencia] = caractere
            sequencia += 1
    else:
        errou -= 1

    locked = errou == total_de_tentativas == 0
    acertou = "_" not in palavra_acertada
    print(palavra_acertada)

if (palavra_acertada == senha_escolhida):
    print(senha_escolhida)
