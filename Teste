import random

print("--x-- Test tests --x--")

perguntas = ["pergunta1", "pergunta2", "pergunta3", "pergunta3", "pergunta4", "pergunta5"]

numero = random.randrange(0, len(perguntas))
pergunta_secreta = perguntas[numero].upper()

respostas = ["Amida", "Cetona", "Amina", "Éster", "Éter"]

resposta1 = "Amida"
resposta2 = "Cetona"
resposta3 = "Amina"
resposta4 = "Éster"
resposta5 = "Éter"
pontos = 100
pontos_perdidos = 20

print("Selecione um nível de dificuldade: ")
print("(1) Fácil, (2) Médio, (3) Difícil")

nivel = int(input("Nível de dificuldade: "))

if (nivel == 1):
    numero_de_tentativas = 5
elif (nivel == 2):
    numero_de_tentativas = 3
elif (nivel == 3):
    numero_de_tentativas = 1

for rodada in range(1, numero_de_tentativas + 1):

    print(pergunta_secreta)
    print(f"Alternativas: {respostas}")
    print(f"Tentativa {rodada} de {numero_de_tentativas}, {pontos} pontos")
    chute = input("Insira a resposta: ")
    print(f"Resposta insetida: {chute}")
    if (chute == resposta1):
        print(f"Respostas correta e você fez {pontos} pontos")
        break
    elif (chute == resposta2):
        print(f"Respostas correta e você fez {pontos} pontos")
        break
    elif (chute == resposta3):
        print(f"Respostas correta e você fez {pontos} pontos")
        break
    elif (chute == resposta4):
        print(f"Respostas correta e você fez {pontos} pontos")
        break
    elif (chute == resposta5):
        print(f"Respostas correta e você fez {pontos} pontos")
        break
    else:
        pontos = abs(pontos - pontos_perdidos)
        print(f"Resposta errada, {pontos} pontos")

print("Fim de jogo")
