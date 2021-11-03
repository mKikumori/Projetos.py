import random


arquivo = open("senhas.txt", "r")
senhas = []

    for linha in arquio:
        senhas.append(linha.strip())
      
    arquivo.close
    
    numero = random.randrange(0, len(senhas))
    palavra_secreta = senhas[numero].upper()
    
    
    total_de_tentativas = False
    acertou = False
    errou = 0
    palavra_acertada = ["_" for letra in palavra_secreta]
    
    print(palavra_acertada)
    
    while(not total_de_tentativas and not acertou):
      
        print(palavra_acertada)
        chute = input("Digite uma letra:")
        chute = chute.strip().upper()

            if(chute in palavra_secreta):
                sequencia = 0
                for letra in palavra_secreta:
                    if(chute == letra):
                        palavra_acertada[sequencia] = letra
                    sequencia += 1
            else:
                errou += 1

        
            total_de_tentativas = errou == len(palavra_secreta)
            acertou = "_" not in palavra acertada
        
            if(palavra_acertada == palavra_secreta)
                print(palavra_secreta)
