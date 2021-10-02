import random

    print("--x-- Test tests --x--")
    
    arquivo = open("respostas.txt", "r")
    respostas = []
    
    for linha in arquivo:
        respostas.append(linha.strip())
        
    arquivo.close
    
    numero = random.randrange(0, len(respostas))
    palavra_secreta = respostas[numero].upper()
   

    arquivo2 = open("perguntas.txt", "r")
    perguntas = []

    for linha in arquivo2:
        perguntas.append(linha.strip())

    arquivo2.close

    numero2 = random.randrange(0, len(perguntas))
    pergunta_secreta = perguntas[numero2].upper()



    print(["_" for letra in palavra_secreta])
    
    
    print("Selecione um nível de dificuldade: ")
    print("(1) Fácil, (2) Médio, (3) Difícil")
    
    nivel = int(input("Nível de dificuldade: "))
    
    if(nivel == 1):
        numero_de_tentativas = 5
    elif(nivel == 2):
        numero_de_tentativas = 3
    elif(nivel == 3):
        numero_de_tentativas = 1
    
    for rodada in range(1, total_de_tentativas + 1):

        print(pergunta_secreta)
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Insira a resposta: "))
        print("Resposta insetida: ")
        
        acertou = chute == palavra_secreta
        errou = chute !== palavra_secreta
        
        if(acertou):
            print("Respostas correta")
        if(errou):
            print("Resposta errada")
         
        
