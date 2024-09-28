#Extensão para escolher aleatoriamente uma jogada
import random
#Onde o usuário irá inserir sua modalidade
modalidade = int(input("Escolha a modalidade que deseja jogar 1- humano x humano; 2- humano x computador; 3- computador x computador: "))
#Placar dos jogadores
contadorUm = 0
contadorDois = 0
#Váriavel para o computador escolher aleatoriamente
lista = ["pedra", "papel", "tesoura"]
#Váriavel para a condição while continuar caso o usuário escolha continuar
continua = "não"
#Condição para caso o usuário insira uma modalidade inválida
while modalidade != 1 and modalidade != 2 and modalidade != 3:
    print("Modalidade inválida, digite novamente!")
    modalidade = int(input("Escolha a modalidade que deseja jogar 1- humano x humano; 2- humano x computador; 3- computador x computador:"))

#Condições para quando for escolhido as jogadas dos jogadores
while continua == "não":
    if modalidade == 1:
        jogadorUm = int(input("Jogador 1 digite sua jogada, escolha entre 1-pedra, 2-papel e 3-tesoura: "))
        jogadorDois = int(input("Jogador 2 digite sua jogada, escolha entre 1-pedra, 2- papel e 3-tesoura: "))
    elif modalidade == 2:
        jogadorUm = int(input("Jogador 1 digite sua jogada, escolha entre 1-pedra 2-papel e 3-tesoura: "))
        jogadorDois = random.choice(lista)
        print(jogadorDois)
    else:
        jogadorUm = random.choice(lista)
        print(jogadorUm)
        jogadorDois = random.choice(lista)
        print(jogadorDois)
    if jogadorUm == jogadorDois:
        print("Empate!")
    elif jogadorUm == 1 and jogadorDois == 2:
        print("Jogador 2 venceu!")
        contadorDois += 1
    elif jogadorUm == 1 and jogadorDois == 3:
        print("Jogador 1 venceu!")
        contadorUm += 1
    elif jogadorUm == 2 and jogadorDois == 3:
        print("Jogador 2 venceu!")
        contadorDois += 1
    elif jogadorUm == 2 and jogadorDois == 1:
        print("Jogador 1 venceu!")
        contadorUm += 1
    elif jogadorUm == 3 and jogadorDois == 1:
        print("Jogador 2 venceu!")
        contadorDois += 1
    elif jogadorUm == 3 and jogadorDois == 2:
        print("Jogador 1 venceu!")
        contadorUm += 1
    continua = input("Deseja sair, digite sim ou não: ")
#Placar final caso o usuário queria finalizar o jogo
print(f"Jogador 1: {contadorUm} Jogador 2: {contadorDois}  ")
print("Obrigada por jogar, att. Andressa")