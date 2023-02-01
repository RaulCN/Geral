import random
import time 

print("Flascard Constituição Brasileira de 88 ")
print("--")
time.sleep(2)
print("Vamos testar nossos conhecimentos sobre a constituicão de 88?  ")
print("--")
time.sleep(7)
print("Responda mentalmente as  perguntas abaixo, aperte enter para ver a resposta, se souber aperte 1, senão souber aperte 0, ao final poderemos treinar somente com as erradas")
print("--")
time.sleep(9)
print("Preparados? ")
time.sleep(1)
print( "Comecemos em 1")
time.sleep(1)
print( "2...")
time.sleep(1)
print( "3...")
time.sleep(1)
print("--")

print( "Responda!")
print("************************")
time.sleep(5)

def mostrar_carta(carta):
    print(carta[0])
    input("Aperte Enter para ver a resposta...")
    print("--")
    print(carta[1])

flashcard = [
["Qual é a idade mínima para ser presidente?", "35 anos"],
["Qual é o número de Estados do Brasil?", "26 e 1 DF"],
["Quantos membros tem o STF?", "11 membros"],
["Quantos artigos tem a CF 1988?", "137 artigos"],
["Qual é a finalidade da CF?", "Ordenar a sociedade"],
["Qual idade mínima para  ser deputado federal?", "25 anos"],
["O que é o TSE?", "Tribunal Superior Eleitoral"],
["Qual é o prazo para uma emenda à CF?", "2 turnos, 3 anos"],
["Quantos votos são necessários para mudar a CF?", "3/5 dos votos"],
["O que é a EC nº 41/03?", "Fim do mandato dos governadores"],
["Quantos votos são necessários para aprovar uma PEC na Câmara dos Deputados?", "3/5 dos votos"],
["Quantos votos são necessários para aprovar uma PEC no Senado Federal?", "3/5 dos votos"],
["Quantos artigos tem o Código Penal Brasileiro?", "308 artigos"],
["Qual é o nome do Código de Processo Penal?", "Código de Processo Penal"],
["Quantos membros tem a Corte Interamericana de Direitos Humanos?", "7 membros"],
["Quantos membros tem a Corte Internacional de Justiça?", "15 membros"],
["Quantos artigos tem a Convenção Americana sobre Direitos Humanos?", "69 artigos"],
["Quantos membros tem a Comissão Interamericana de Direitos Humanos?", "7 membros"],
["Qual é o nome do tratado que regulamenta a Convenção Americana sobre Direitos Humanos?", "Protocolo de San Salvador"],
["Quantos artigos tem o Pacto Internacional dos Direitos Civis e Políticos?", "76 artigos"],
]
perguntas_erradas = []

while flashcard:
    random.shuffle(flashcard)
    total_cartas = len(flashcard)
    cartas_acertadas = 0

    for carta in flashcard:
        mostrar_carta(carta)
        feedback = input("Digite 1 se você acertou ou 0 se você errou: ")
        if feedback == "1":
            cartas_acertadas += 1
        else:
            perguntas_erradas.append(carta)

    porcentagem_acerto = (cartas_acertadas / total_cartas) * 100
    print("Você acertou {} de {} cartas, {:.2f}% de acerto".format(cartas_acertadas, total_cartas, porcentagem_acerto))

    if perguntas_erradas:
        jogar_novamente = input("Deseja jogar novamente apenas com as perguntas erradas? (s/n) ")
    else:
        jogar_novamente = input("Não há mais perguntas para jogar. Deseja jogar com todas as perguntas novamente? (s/n) ")
    if jogar_novamente != "s":
        flashcard = []
        break


    flashcard = perguntas_erradas
    perguntas_erradas = []
    jogar_novamente = input("Deseja jogar novamente apenas com as perguntas erradas? (s/n) ")
    if jogar_novamente != "s":
        flashcard = []
        break
# melhorias
# adcionar comentarios no jogo 
# Explixar as refras do jogo no começo do app
"""Arrumar repetiçao >>> jogar_novamente = input("Deseja jogar novamente apenas com as perguntas erradas? (s/n) ")"""