import random

dicas =["O irmão é diabético", 
        "A mãe estava de jejum de 12 horas para um exame as 6 horas da manhã",
        "Andressa estava de TPM", 
        "O embrulho do chocolate estava no lixo da cozinha na manhã seguinte", 
        "O cholate era ao leite"]
suspeitos = ["Andressa", "Mãe", "Irmão", "Lissa", "Fernanda"]

perguntas = ["Onde você estava de manhã?",
    "Onde você estava de tarde?",
    "Onde você estava de noite?",
    "Quem você acha que é o culpado?",
    "Você gosta de chocolate?"]

respostas = [
    ["Guardei meu chocolate na geladeira e esperei minhas amigas chegarem.",
    "Estava na cozinha a manhã inteira",
    "Na escola até às 16:00",
    "Em casa fazendo um bolo para minhas amigas",
    "Na faculdade, estudando."],

    ["Fazendo almoço com a  fer. Depois eu e  as meninas jogamos jogos de tabuleiro.",
    "Fiquei no meu quarto assistindo dorama.",
    "Cheguei em  casa às 17:00 e fiquei jogando vídeogame até a hora do jantar.",
    "Cheguei na casa da Andressa meio-dia e fiz tarefa da facul enquanto elas faziam o almoço.",
    "Cheguei na casa da Andressa às 11:00 e ajudei com  o almoço."],

    ["Pedi yakissoba no Ifood. Então jantamos às 19:30.",
    "Levei o lixo para fora às 20:00. Então fui dormir.",
    "Jantei o yakissoba que minha irmã pediu e joguei videogame até meia-noite.",
    "Jantei. Tomei meu remédio para dormir e capotei às 21:00.",
    "Fiquei assistindo vídeos no youtube até dormir mais ou menos às 22:30."],

    ["Meu irmão sempre rouba minhas coisas.",
    "A Andressa devora todos os chocolates quando está de TPM.",
    "Ouvi alguém saindo do quarto das meninas durante a noite...",
    "A Fer foi na cozinha sozinha durante a tarde.",
    "A Lissa estava com as mãos sujas de chocolate."],

    ["Amo.", "Gosto muito.", "Não como faz algum tempo", "Até que sim", "Só chocolate amargo"]
]

culpado = "Andressa"
pontos = 6

#interrogação dos suspeitos
def interrogarSuspeito():
    global pontos #tem que ser global para valer para todas as funções

    #se os pontos acabam, puxa o minijogo de matemática
    if pontos <= 0:
        print("=========================================================================================================")
        print()
        print("VOCÊ ESTÁ SEM PONTOS!")
        print()
        minijogo()
        return

    #printa os suspeitos
    print()
    print("=========================================================================================================")
    print()
    print("SUSPEITOS: ")

    for i in range(len(suspeitos)):
        print(f"{i + 1}. {suspeitos[i]}")

    #aqui o jogador escolhe o suspeito
    posicaoSuspeito = int(input(" - Digite o número do suspeito que deseja interrogar: ")) - 1
    if posicaoSuspeito < 0 or posicaoSuspeito >= len(suspeitos):
        print("Suspeito inválido... Tente novamente.")
        return

    #printa as peruntas
    print()
    print("=========================================================================================================")
    print()
    print("PERGUNTAS:")
    for i in range(len(perguntas)):
        print(f"{i + 1}. {perguntas[i]}")

    #aqui o jogador escolhe a pergunta
    posicaoPergunta = int(input(" - Digite o número da pergunta que você deseja fazer: ")) - 1
    if posicaoPergunta < 0 or posicaoPergunta >= len(perguntas):
        print(f"Pergunta inválida... Tente novamente.")
        return

    #transformei em matriz para achar a resposta :p
    resposta = respostas[posicaoPergunta][posicaoSuspeito]
    print()
    print(f"RESPOSTA DE {suspeitos[posicaoSuspeito]}:")
    print(f"  {resposta}")
    pontos -= 1 #toda vez que o jogador faz uma pergunta, ele gasta um ponto
    print()
    print(f"Você está com {pontos} pontos.")
    print()

#para o jogador adivinhar o culpado
def adivinharCulpado():

    #printa os suspeitos possíveis
    print()
    print("=========================================================================================================")
    print()
    print(f"QUEM É O CULPADO?")
    for i in range(len(suspeitos)):
        print(f"{i + 1}. {suspeitos[i]}")

    #input da escolha do culpado
    posicaoSuspeito = int(input(" - Digite o número do culpado: ")) - 1
    if posicaoSuspeito < 0 or posicaoSuspeito >= len(suspeitos):
        print("Suspeito inválido... Tente novamente.")
        return

    #se o jogador acerta
    if suspeitos[posicaoSuspeito] == culpado:
        print()
        print("=========================================================================================================")
        print()
        print(f"PARABÉNS, VOCÊ ACERTOU!.")

    #se o jogador erra
    else:
        print()
        print("=========================================================================================================")
        print()
        print(f"ERROU!")
        print()
        print(f"Mas você teve sorte, e Andressa adimitiu ter comido o chocolate.")

    #independente se vc acertar ou não, vai explicar o que aconteceu :p
    #eu queria colocar a hhistória inteira, mas achei que ia ser demaiis.
    print()
    print(f"    Andressa era a culpada. Comeu o chocolate porque estava na semana de TPM.")
    print(f"    Enquanto todos dormiam, Andressa foi até a geladeira e comeu seu chocolate.")
    print(f"    A mãe estava de jejum para seu exame de sangue na manhã seguinte.")
    print(f"    O irmão não comeu o chocolate devido sua diabetes.")
    print(f"    Lissa nunca foi à cozinha sozinha. Apenas estava suja de chocolate, pois havia feito um bolo.")
    print(f"    A Fernanda não gosta de chocolate ao leite. ")

#minijogo
def minijogo():
    global pontos
    print()
    print("=========================================================================================================")
    print()
    print(f"\nMINIJOGO!\nGanhe 3 pontos ao acertar!")

    #randomiza os numeros e o sinal
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    sinal = random.choice(["+", "x"]) #só de + e x, pq eu não sabia direito como fazer o primeiro número ser sempre maior que o segundo.

    #soma
    if sinal == "+":
        respostaCerta = n1 + n2
        print(f"{n1} + {n2} = ?")
    #mult
    elif sinal == "x":
        respostaCerta = n1 * n2
        print(f"{n1} x {n2} = ?")
    resposta = int(input(" - Digite a resposta da conta: "))

    #se o jogador acertar
    if resposta == respostaCerta:
        resultado = "ACERTOU"
        pontos += 3
    #e se ele errar
    else:
        resultado = "ERROU"
    print(f"\n{resultado}!")
    print(f"VOCÊ ESTÁ COM {pontos} PONTOS!")

def dica():
    global pontos
    print() 
    print("DICA:")
    print()
    dica = input("Você deseja uma dica e perder ponto (s/n)?")

    if dica == "s":
        pontos -= 1
        print("=========================================================================================================")
        print()
        dicaAleatoria = random.choice(dicas)
        print(f"DICA:{dicaAleatoria} ")
        dicas.remove(dicaAleatoria)
        print()
        print(f"Agora você tem {pontos} pontos.")

    else: 
        print()
        print("=========================================================================================================")
        print()
        print("Ok, vamos continuar!")

#jogo
def main():
    while True:



        #puxa a função da iinterrogação dos suspeitos
        interrogarSuspeito()

        print()
        print("=========================================================================================================")

        #dar dicas
        if len(dicas) > 0:
            dica()

        #tentar acertar o culpado ou nao
        print()
        continuar = input("DESEJA TENTAR ACERTAR O CULPADO? (s/n) ")
        if continuar.lower() == "s":
            #puxa a função de adivinhar o culpado
            adivinharCulpado()
            break

    print("OBRIGADA POR JOGAR! :)")

#início do jogo
print()
print(f"BEM VINDO AO JOGO DE DETETIVE:\nASSALTO À GELADEIRA!!")
print()
print(F"01.02.2024")
print(f"Andressa tinha acabado de voltar do mercado de manhã.")
print(f"Guardou as compras, inclusive seu chocolate, dentro da geladeira.")
print(f"Estava esperando para comer no dia seguinte.")
print(f"Ela estava animada para passar uma tarde em casa com suas amigas, e depois fazer uma noite do pijama.")
print()
print(f"No dia seguinte...")
print()
print(f"02.02.2024")
print(f"Andressa acordou cedo e queria comer seu chocolate.")
print(f"Abriu a geladeira, mas seu chocolate não e stava mais lá.")
print()
print("=========================================================================================================")
print()
print(f"Por causa desse crime, chamaram o detetive de crimes extremamente sério.")
nome = str(input(f" - Digite seu nome: "))
print()
print(f"DESCUBRA O CULPADO, DETETIVE {nome}!")
print()

#roda o jogo
main()