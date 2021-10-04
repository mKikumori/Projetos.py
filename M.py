import random

    print("--x-- Test tests --x--")
    

    perguntas = ["pergunta1", "pergunta2", "pergunta3", "pergunta3", "pergunta4", "pergunta5"]

    numero = random.randrange(0, len(perguntas))
    pergunta_secreta = perguntas[numero].upper()
    
    
    respostas = ["Ácido carboxílico", "Cetona", "Aldeido", "Éster", "Éter"]
    
    resposta1 = [perguntas,0] == [respostas,0]
    resposta2 = [perguntas,1] == [respostas,1]
    resposta3 = [perguntas,2] == [respostas,2]
    resposta4 = [perguntas,3] == [respostas,3]
    resposta5 = [perguntas,4] == [respostas,4]
    
    
    
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
        print(f"Alternativas: {respostas}")
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = input("Insira a resposta: ")
        print("Resposta insetida: ")
        
        
        if(chute == resposta1):
            print("Respostas correta")
        elif(chute == resposta2):
            print("Respostas correta")
        elif(chute == resposta3):
            print("Respostas correta")
        elif(chute == resposta4):
            print("Respostas correta")
        elif(chute == resposta5):
            print("Respostas correta")
        else:
            print("Resposta errada")
         
        
