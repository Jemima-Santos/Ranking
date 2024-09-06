import os

print("Maratona de Programação UEFS")

#Inputs do peso pelo usuário
pesoFaceis = int(input("Digite o peso das questões fáceis: "))
pesoMedias = int(input("Digite o peso das questões médias: "))
pesoDificeis = int(input("Digite o peso das questões difíceis: "))
print("--------------------------------------------------------------")
print("\n")

#Definindo o nome das equipes
grupo1 = input("Digite o nome da equipe 1: ")
grupo2 = input("Digite o nome da equipe 2: ")
grupo3 = input("Digite o nome da equipe 3: ")
grupo4 = input("Digite o nome da equipe 4: ")
grupo5 = input("Digite o nome da equipe 5: ")
print("--------------------------------------------------------------")
print("\n")

#Equipe 1
faceis1 = int(input("Digite quantas questões fáceis o grupo 1 acertou: "))
medias1 = int(input("Digite quantas questões médias o grupo 1 acertou: "))
dificeis1 = int(input("Digite quantas questões difíceis o grupo 1 acertou: "))
tempo1 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
totalPontos1 = faceis1 * pesoFaceis + medias1 * pesoMedias + dificeis1 * pesoDificeis
print("--------------------------------------------------------------")
print("\n")

#Equipe 2
faceis2 = int(input("Digite quantas questões fáceis o grupo 2 acertou: "))
medias2 = int(input("Digite quantas questões médias o grupo 2 acertou: "))
dificeis2 = int(input("Digite quantas questões difíceis o grupo 2 acertou: "))
tempo2 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
totalPontos2 = faceis2 * pesoFaceis + medias2 * pesoMedias + dificeis2 * pesoDificeis
print("--------------------------------------------------------------")
print("\n")

#Equipe 3
faceis3 = int(input("Digite quantas questões fáceis o grupo 3 acertou: "))
medias3 = int(input("Digite quantas questões médias o grupo 3 acertou: "))
dificeis3 = int(input("Digite quantas questões difíceis o grupo 3 acertou: "))
tempo3 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
totalPontos3 = faceis3 * pesoFaceis + medias3 * pesoMedias + dificeis3 * pesoDificeis
print("--------------------------------------------------------------")
print("\n")


#Equipe 4
faceis4 = int(input("Digite quantas questões fáceis o grupo 4 acertou: "))
medias4 = int(input("Digite quantas questões médias o grupo 4 acertou: "))
dificeis4 = int(input("Digite quantas questões difíceis o grupo 4 acertou: "))
tempo4 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
totalPontos4 = faceis4 * pesoFaceis + medias4 * pesoMedias + dificeis4 * pesoDificeis
print("--------------------------------------------------------------")
print("\n")


#Equipe 5
faceis5 = int(input("Digite quantas questões fáceis o grupo 5 acertou: "))
medias5 = int(input("Digite quantas questões médias o grupo 5 acertou: "))
dificeis5 = int(input("Digite quantas questões difíceis o grupo 5 acertou: "))
tempo5 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
totalPontos5 = faceis5 * pesoFaceis + medias5 * pesoMedias + dificeis5 * pesoDificeis
print("--------------------------------------------------------------")
print("\n")

# Inicializando variáveis de ranking
primeiro = grupo1
segundo = grupo2
terceiro = grupo3
quarto = grupo4
quinto = grupo5
pontosPrimeiro = totalPontos1
pontosSegundo = totalPontos2
pontosTerceiro = totalPontos3
pontosQuarto = totalPontos4
pontosQuinto = totalPontos5

# Comparando e organizando os rankings
if totalPontos2 > pontosPrimeiro:
    quinto = quarto
    quarto = terceiro
    terceiro = segundo
    segundo = primeiro
    primeiro = grupo2
    pontosPrimeiro = totalPontos2
elif totalPontos2 > pontosSegundo:
    quinto = quarto
    quarto = terceiro
    terceiro = segundo
    segundo = grupo2
    pontosSegundo = totalPontos2
elif totalPontos2 > pontosTerceiro:
    quinto = quarto
    quarto = terceiro
    terceiro = grupo2
    pontosTerceiro = totalPontos2
elif totalPontos2 > pontosQuarto:
    quinto = quarto
    quarto = grupo2
    pontosQuarto = totalPontos2
elif totalPontos2 > pontosQuinto:
    quinto = grupo2
    pontosQuinto = totalPontos2

# Repete o mesmo processo para os outros grupos
if totalPontos3 > pontosPrimeiro:
    quinto = quarto
    quarto = terceiro
    terceiro = segundo
    segundo = primeiro
    primeiro = grupo3
    pontosPrimeiro = totalPontos3
elif totalPontos3 > pontosSegundo:
    quinto = quarto
    quarto = terceiro
    terceiro = segundo
    segundo = grupo3
    pontosSegundo = totalPontos3
elif totalPontos3 > pontosTerceiro:
    quinto = quarto
    quarto = terceiro
    terceiro = grupo3
    pontosTerceiro = totalPontos3
elif totalPontos3 > pontosQuarto:
    quinto = quarto
    quarto = grupo3
    pontosQuarto = totalPontos3
elif totalPontos3 > pontosQuinto:
    quinto = grupo3
    pontosQuinto = totalPontos3

# Mesma coisa para grupo 4
if totalPontos4 > pontosPrimeiro:
    quinto = quarto
    quarto = terceiro
    terceiro = segundo
    segundo = primeiro
    primeiro = grupo4
    pontosPrimeiro = totalPontos4
elif totalPontos4 > pontosSegundo:
    quinto = quarto
    quarto = terceiro
    terceiro = segundo
    segundo = grupo4
    pontosSegundo = totalPontos4
elif totalPontos4 > pontosTerceiro:
    quinto = quarto
    quarto = terceiro
    terceiro = grupo4
    pontosTerceiro = totalPontos4
elif totalPontos4 > pontosQuarto:
    quinto = quarto
    quarto = grupo4
    pontosQuarto = totalPontos4
elif totalPontos4 > pontosQuinto:
    quinto = grupo4
    pontosQuinto = totalPontos4

# Mesma coisa para grupo 5
if totalPontos5 > pontosPrimeiro:
    quinto = quarto
    quarto = terceiro
    terceiro = segundo
    segundo = primeiro
    primeiro = grupo5
    pontosPrimeiro = totalPontos5
elif totalPontos5 > pontosSegundo:
    quinto = quarto
    quarto = terceiro
    terceiro = segundo
    segundo = grupo5
    pontosSegundo = totalPontos5
elif totalPontos5 > pontosTerceiro:
    quinto = quarto
    quarto = terceiro
    terceiro = grupo5
    pontosTerceiro = totalPontos5
elif totalPontos5 > pontosQuarto:
    quinto = quarto
    quarto = grupo5
    pontosQuarto = totalPontos5
elif totalPontos5 > pontosQuinto:
    quinto = grupo5
    pontosQuinto = totalPontos5

# Exibindo o ranking final com tabulação, total de pontos e média de acertos
print("\n" + "="*40)
print("               Ranking Final")
print("="*40)

# Calculando a média total de acertos
mediaTotal = (totalPontos1 + totalPontos2 + totalPontos3 + totalPontos4 + totalPontos5) / 5

# Exibindo o ranking com formatação e média total
print(f"1º - {primeiro:<12} | Pontos: {pontosPrimeiro:<4}")
print(f"2º - {segundo:<12} | Pontos: {pontosSegundo:<4}")
print(f"3º - {terceiro:<12} | Pontos: {pontosTerceiro:<4}")
print(f"4º - {quarto:<12} | Pontos: {pontosQuarto:<4}")
print(f"5º - {quinto:<12} | Pontos: {pontosQuinto:<4}")
print("-" * 40)
print(f"Média Total de Pontos: {mediaTotal:.2f}")
print("="*40)
















'''
#comparando o grupo 2 com o grupo 1:
if(totalPontos2 > totalPontos1):
    primeiro = grupo2
    segundo = grupo1
elif(totalPontos2 == totalPontos1):
    if(totaldificeis2>totaldificeis1):
            primeiro = grupo2
            segundo = grupo1
    elif(totaldificeis2==totaldificeis1):
        if(tempo2<tempo1):
            primeiro = grupo2
            segundo = grupo1
        elif(tempo2 == tempo1):
            if(totalQuestoes2 > totalQuestoes1):
                primeiro = grupo2
                segundo = grupo1
        else:
            primeiro = grupo1
            segundo = grupo2
    else:
        primeiro = grupo1
        segundo = grupo2
else:
    primeiro = grupo1
    segundo = grupo2


#comparando o grupo 3 com o grupo 1 e 2
if(totalPontos3 > totalPontos2 and totalPontos3 > totalPontos1):
        terceiro = segundo
        segundo = primeiro
        primeiro = grupo3
elif(totalPontos3 == totalPontos2):
    if(totaldificeis3>totaldificeis2):
        terceiro = segundo
        segundo = primeiro
        primeiro = grupo3
    elif(totaldificeis3==totaldificeis2):
        if(tempo3<tempo2):
            terceiro = segundo
            segundo = primeiro
            primeiro = grupo3
        elif(tempo3 == tempo2):
            if(totalQuestoes3 > totalQuestoes2):
                terceiro = segundo
                segundo = primeiro
                primeiro = grupo3
        else:
            terceiro = segundo
            segundo = primeiro
            primeiro = grupo3
    else:
        terceiro = segundo
        segundo = primeiro
        primeiro = grupo3
else:
        terceiro = segundo
        segundo = primeiro
        primeiro = grupo3
'''