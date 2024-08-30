import os

print("Maratona de Programação UEFS")

pesoFaceis = int(input("Digite o peso das questões fáceis: "))
pesoMedias = int(input("Digite o peso das questões médias: "))
pesoDificeis = int(input("Digite o peso das questões difíceis: "))

grupoA = input("Digite o nome da equipe 1: ")
#grupoB = input("Digite o nome da equipe 2: ")
#grupoC = input("Digite o nome da equipe 3: ")
#grupoD = input("Digite o nome da equipe 4: ")
#grupoE = input("Digite o nome da equipe 5: ")


faceis = int(input("Digite quantas questões fáceis o grupo 1 acertou: "))
medias = int(input("Digite quantas questões médias o grupo 1 acertou: "))
dificeis = int(input("Digite quantas questões difíceis o grupo 1 acertou: "))
totalPontos1 = faceis * pesoFaceis + medias * pesoMedias + dificeis * pesoDificeis
print("--------------------------------------------------------------")
print(" ")

faceis = int(input("Digite quantas questões fáceis o grupo 2 acertou: "))
medias = int(input("Digite quantas questões médias o grupo 2 acertou: "))
dificeis = int(input("Digite quantas questões difíceis o grupo 2 acertou: "))
totalPontos2 = faceis * pesoFaceis + medias * pesoMedias + dificeis * pesoDificeis
print("--------------------------------------------------------------")
print(" ")

faceis = int(input("Digite quantas questões fáceis o grupo 3 acertou: "))
medias = int(input("Digite quantas questões médias o grupo 3 acertou: "))
dificeis = int(input("Digite quantas questões difíceis o grupo 3 acertou: "))
totalPontos3 = faceis * pesoFaceis + medias * pesoMedias + dificeis * pesoDificeis
print("--------------------------------------------------------------")
print(" ")

faceis = int(input("Digite quantas questões fáceis o grupo 4 acertou: "))
medias = int(input("Digite quantas questões médias o grupo 4 acertou: "))
dificeis = int(input("Digite quantas questões difíceis o grupo 4 acertou: "))
totalPontos4 = faceis * pesoFaceis + medias * pesoMedias + dificeis * pesoDificeis
print("--------------------------------------------------------------")
print(" ")

faceis = int(input("Digite quantas questões fáceis o grupo 5 acertou: "))
medias = int(input("Digite quantas questões médias o grupo 5 acertou: "))
dificeis = int(input("Digite quantas questões difíceis o grupo 5 acertou: "))
totalPontos5 = faceis * pesoFaceis + medias * pesoMedias + dificeis * pesoDificeis



print (f"A equipe 1 ficou com {totalPontos1} pontos!")
print (f"A equipe 2 ficou com {totalPontos2} pontos!")
print (f"A equipe 3 ficou com {totalPontos3} pontos!")
print (f"A equipe 4 ficou com {totalPontos4} pontos!")
print (f"A equipe 5 ficou com {totalPontos5} pontos!")