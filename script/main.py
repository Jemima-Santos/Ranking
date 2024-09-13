import os
''''
Autor: Jemima Santos da Silva
Componente Curricular: Algoritmos I
Concluído em: 14/09/2024
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''

#imprimindo cabeçalho
print("==============================================================")
print("               MARATONA DE PROGRAMAÇÃO - UEFS                 ")
print("==============================================================")
print("\n                Bem-vindo à competição!")
print("==============================================================")
print("\n")
print("\n")
print("\n")

# Limpa o terminal para iniciar a exibição do menu
os.system('cls')         

# Inicializar a variável menu
menu = 0  

# Loop do menu principal até que o usuário escolha a opção de sair e exibição do menu
while menu != 6:
    os.system('cls')  
    print("--------------------------------------------------------------")
    print("                           MENU                              ")
    print("--------------------------------------------------------------")
    print("1 - Inserir o peso das questões")
    print("2 - Inserir o nome das equipes")
    print("3 - Inserir a resposta das equipes")
    print("4 - Ver ranking geral")
    print("5 - Ver pontuação de cada equipe")
    print("6 - Sair")
    print("--------------------------------------------------------------")

# Solicita ao usuário uma opção do menu
    menu = int(input("Escolha uma opção: "))
    os.system('cls') 

# Se o menu for 1, o usuário irá inserir os pesos das questões
    if menu == 1:
    # input dos pesos com validação para ser maior que 0

        os.system('cls') 
        pesoFaceis = int(input("Digite o peso das questões fáceis: ")) 
        if (pesoFaceis <= 0):
            while pesoFaceis <= 0:
                print("\nValor invalido! \nDigite novamente!\n")
                pesoFaceis = int(input("Digite o peso das questões fáceis: "))
                print("\n")

        pesoMedias = int(input("Digite o peso das questões médias: ")) 
        if (pesoMedias <= 0):
            while pesoMedias <= 0:
                print("\nValor invalido! \nDigite novamente!\n")
                pesoMedias = int(input("Digite o peso das questões médias: "))
                print("\n")

        pesoDificeis = int(input("Digite o peso das questões difíceis: ")) 
        if (pesoDificeis <= 0):
            while pesoDificeis <= 0:
                print("\nValor invalido! \nDigite novamente!\n")
                pesoDificeis = int(input("Digite o peso das questões difíceis: "))
                print("\n")

        print("\nPesos inseridos com sucesso!\n")
        # Pausa para o usuário ler a mensagem
        input("Pressione Enter para voltar ao menu...")  
        os.system('cls')

# Se o menu for 2, o usuário irá inserir o nome das equipes
    elif menu == 2:
        os.system('cls')
    # Se o nome da equipe for vazio, atribui um nome padrão
        grupo1 = input("Digite o nome da equipe 1: ")
        if grupo1 == "":  
            grupo1 = "A"

        grupo2 = input("Digite o nome da equipe 2: ")
        if grupo2 == "":
            grupo2 = "B"

        grupo3 = input("Digite o nome da equipe 3: ")
        if grupo3 == "":
            grupo3 = "C"

        grupo4 = input("Digite o nome da equipe 4: ")
        if grupo4 == "":
            grupo4 = "D"

        grupo5 = input("Digite o nome da equipe 5: ")
        if grupo5 == "":
            grupo5 = "E"

        #Exibindo o nome das equipes
        os.system('cls')  
        print(f"O nome da equipe 1 ficou como: {grupo1}")
        print(f"O nome da equipe 2 ficou como: {grupo2}")
        print(f"O nome da equipe 3 ficou como: {grupo3}")
        print(f"O nome da equipe 4 ficou como: {grupo4}")
        print(f"O nome da equipe 5 ficou como: {grupo5}")
        print("\n")

        #Voltando ao menu
        print("\nNome das equipes inseridas com sucesso!\n")
        input("Pressione Enter para voltar ao menu...")
        os.system('cls')

# Se o menu for 3, o usuário irá inserir as respostas das equipes
    elif menu == 3:
        os.system('cls')
        # Recebe os valores de acertos e tempo das equipes 

        #Equipe 1
        faceis1 = int(input("Digite quantas questões fáceis o grupo 1 acertou: "))
        medias1 = int(input("Digite quantas questões médias o grupo 1 acertou: "))
        dificeis1 = int(input("Digite quantas questões difíceis o grupo 1 acertou: "))
        tempo1 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
        # Calcula a pontuação total da equipe 1
        totalPontos1 = faceis1 * pesoFaceis + medias1 * pesoMedias + dificeis1 * pesoDificeis
        os.system('cls')

        #Equipe 2
        faceis2 = int(input("Digite quantas questões fáceis o grupo 2 acertou: "))
        medias2 = int(input("Digite quantas questões médias o grupo 2 acertou: "))
        dificeis2 = int(input("Digite quantas questões difíceis o grupo 2 acertou: "))
        tempo2 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
        totalPontos2 = faceis2 * pesoFaceis + medias2 * pesoMedias + dificeis2 * pesoDificeis
        os.system('cls')

        #Equipe 3
        faceis3 = int(input("Digite quantas questões fáceis o grupo 3 acertou: "))
        medias3 = int(input("Digite quantas questões médias o grupo 3 acertou: "))
        dificeis3 = int(input("Digite quantas questões difíceis o grupo 3 acertou: "))
        tempo3 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
        totalPontos3 = faceis3 * pesoFaceis + medias3 * pesoMedias + dificeis3 * pesoDificeis
        os.system('cls')

        #Equipe 4
        faceis4 = int(input("Digite quantas questões fáceis o grupo 4 acertou: "))
        medias4 = int(input("Digite quantas questões médias o grupo 4 acertou: "))
        dificeis4 = int(input("Digite quantas questões difíceis o grupo 4 acertou: "))
        tempo4 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
        totalPontos4 = faceis4 * pesoFaceis + medias4 * pesoMedias + dificeis4 * pesoDificeis
        os.system('cls')

        #Equipe 5
        faceis5 = int(input("Digite quantas questões fáceis o grupo 5 acertou: "))
        medias5 = int(input("Digite quantas questões médias o grupo 5 acertou: "))
        dificeis5 = int(input("Digite quantas questões difíceis o grupo 5 acertou: "))
        tempo5 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
        totalPontos5 = faceis5 * pesoFaceis + medias5 * pesoMedias + dificeis5 * pesoDificeis
        os.system('cls') 

        print("\nRespostas das equipes inseridas com sucesso!\n")
        # Pausa para o usuário ler a mensagem
        input("Pressione Enter para voltar ao menu...")
        os.system('cls') 

# Verificando empate e criando o ranking
# Comparando e ordenando os grupos com base nos critérios especificados
if menu == 4:
    # Primeiro, compara o grupo 1 com o grupo 2
    if totalPontos1 < totalPontos2 or (totalPontos1 == totalPontos2 and dificeis1 < dificeis2) or (totalPontos1 == totalPontos2 and dificeis1 == dificeis2 and tempo1 > tempo2):
        # Se o grupo 1 tem menos pontos que o grupo 2, ou
        # Se ambos os grupos têm o mesmo número de pontos, mas o grupo 1 tem menos questões difíceis resolvidas, ou
        # Se ambos os grupos têm o mesmo número de pontos e questões difíceis, mas o grupo 1 gastou mais tempo, então
        # Troca os valores entre grupo 1 e grupo 2 para manter a ordem correta.
        totalPontos1, totalPontos2 = totalPontos2, totalPontos1
        grupo1, grupo2 = grupo2, grupo1
        tempo1, tempo2 = tempo2, tempo1
        faceis1, faceis2 = faceis2, faceis1
        medias1, medias2 = medias2, medias1
        dificeis1, dificeis2 = dificeis2, dificeis1

    # Em seguida, compara o grupo 2 com o grupo 3
    if totalPontos2 < totalPontos3 or (totalPontos2 == totalPontos3 and dificeis2 < dificeis3) or (totalPontos2 == totalPontos3 and dificeis2 == dificeis3 and tempo2 > tempo3):
        # Se o grupo 2 tem menos pontos que o grupo 3, ou
        # Se ambos os grupos têm o mesmo número de pontos, mas o grupo 2 tem menos questões difíceis resolvidas, ou
        # Se ambos os grupos têm o mesmo número de pontos e questões difíceis, mas o grupo 2 gastou mais tempo, então
        # Troca os valores entre grupo 2 e grupo 3 para manter a ordem correta.
        totalPontos2, totalPontos3 = totalPontos3, totalPontos2
        grupo2, grupo3 = grupo3, grupo2
        tempo2, tempo3 = tempo3, tempo2
        faceis2, faceis3 = faceis3, faceis2
        medias2, medias3 = medias3, medias2
        dificeis2, dificeis3 = dificeis3, dificeis2

    # Agora, compara o grupo 3 com o grupo 4
    if totalPontos3 < totalPontos4 or (totalPontos3 == totalPontos4 and dificeis3 < dificeis4) or (totalPontos3 == totalPontos4 and dificeis3 == dificeis4 and tempo3 > tempo4):
        # Se o grupo 3 tem menos pontos que o grupo 4, ou
        # Se ambos os grupos têm o mesmo número de pontos, mas o grupo 3 tem menos questões difíceis resolvidas, ou
        # Se ambos os grupos têm o mesmo número de pontos e questões difíceis, mas o grupo 3 gastou mais tempo, então
        # Troca os valores entre grupo 3 e grupo 4 para manter a ordem correta.
        totalPontos3, totalPontos4 = totalPontos4, totalPontos3
        grupo3, grupo4 = grupo4, grupo3
        tempo3, tempo4 = tempo4, tempo3
        faceis3, faceis4 = faceis4, faceis3
        medias3, medias4 = medias4, medias3
        dificeis3, dificeis4 = dificeis4, dificeis3

    # Finalmente, compara o grupo 4 com o grupo 5
    if totalPontos4 < totalPontos5 or (totalPontos4 == totalPontos5 and dificeis4 < dificeis5) or (totalPontos4 == totalPontos5 and dificeis4 == dificeis5 and tempo4 > tempo5):
        # Se o grupo 4 tem menos pontos que o grupo 5, ou
        # Se ambos os grupos têm o mesmo número de pontos, mas o grupo 4 tem menos questões difíceis resolvidas, ou
        # Se ambos os grupos têm o mesmo número de pontos e questões difíceis, mas o grupo 4 gastou mais tempo, então
        # Troca os valores entre grupo 4 e grupo 5 para manter a ordem correta.
        totalPontos4, totalPontos5 = totalPontos5, totalPontos4
        grupo4, grupo5 = grupo5, grupo4
        tempo4, tempo5 = tempo5, tempo4
        faceis4, faceis5 = faceis5, faceis4
        medias4, medias5 = medias5, medias4
        dificeis4, dificeis5 = dificeis5, dificeis4

        # Associando os grupos ordenados ao ranking final
        
        # Após ordenar os grupos com base nos critérios especificados,
        # este bloco de código é responsável por associar os grupos
        # classificados às suas respectivas posições no ranking final.

        # Atribuindo os grupos classificados às suas posições no ranking.
        primeiro = grupo1
        segundo = grupo2
        terceiro = grupo3
        quarto = grupo4
        quinto = grupo5

        # Atribuindo os pontos totais correspondentes aos grupos
        # classificados às suas posições no ranking.
        totalPontosPrimeiro = totalPontos1
        totalPontosSegundo = totalPontos2
        totalPontosTerceiro = totalPontos3
        totalPontosQuarto = totalPontos4
        totalPontosQuinto = totalPontos5

        tempoPrimeiro = tempo1
        tempoSegundo = tempo2
        tempoTerceiro = tempo3
        tempoQuarto= tempo4
        tempoQuinto = tempo5

        # Calculando a média total de acertos
        mediaTotal = (totalPontos1 + totalPontos2 + totalPontos3 + totalPontos4 + totalPontos5) / 5

        # Exibindo o ranking final com tabulação, total de pontos e média de acertos
        print("--------------------------------------------------------------")
        print("                     RANKING GERAL                           ")
        print("--------------------------------------------------------------")
        # Exibindo o ranking com formatação e média total
        print(f"1º - {primeiro:<12} | Pontos: {totalPontosPrimeiro:<4} | Tempo: {tempoPrimeiro:<4}")
        print(f"2º - {segundo:<12} | Pontos: {totalPontosSegundo:<4} | Tempo: {tempoSegundo:<4}")
        print(f"3º - {terceiro:<12} | Pontos: {totalPontosTerceiro:<4} | Tempo: {tempoTerceiro:<4}")
        print(f"4º - {quarto:<12} | Pontos: {totalPontosQuarto:<4} | Tempo: {tempoQuarto:<4}")
        print(f"5º - {quinto:<12} | Pontos: {totalPontosQuinto:<4} | Tempo: {tempoQuinto:<4}")
        print("-" * 40)
        print(f"Média Total de Pontos: {mediaTotal:.2f}")
        print("-" * 40)
        print(f"A equipe que que resolveu o maior número de problemas difíceis foi: {mediaTotal:.2f}")
        print("="*40)
        input("Pressione Enter para voltar ao menu...")

#Exibindo as informações de cada equipe 
elif menu == 5:
        # Exibindo o detalhamento de cada equipe   
        print("--------------------------------------------------------------")
        print("              DETALHAMENTO DE PONTUAÇÃO DAS EQUIPES         ")
        print("--------------------------------------------------------------")
        print(f"| {'Equipe':<12} | {'Total de Pontos':<15} | {'Questões Fáceis':<15} | {'Questões Médias':<15} | {'Questões Difíceis':<20} | {'Tempo de Prova (minutos)':<25} |")
        print("--------------------------------------------------------------")

        # Detalhes da Equipe 1
        print(f"| {grupo1:<12} | {totalPontos1:<15} | {faceis1:<15} | {medias1:<15} | {dificeis1:<20} | {tempo1:<25.2f} |")

        # Detalhes da Equipe 2
        print(f"| {grupo2:<12} | {totalPontos2:<15} | {faceis2:<15} | {medias2:<15} | {dificeis2:<20} | {tempo2:<25.2f} |")

        # Detalhes da Equipe 3
        print(f"| {grupo3:<12} | {totalPontos3:<15} | {faceis3:<15} | {medias3:<15} | {dificeis3:<20} | {tempo3:<25.2f} |")

        # Detalhes da Equipe 4
        print(f"| {grupo4:<12} | {totalPontos4:<15} | {faceis4:<15} | {medias4:<15} | {dificeis4:<20} | {tempo4:<25.2f} |")

        # Detalhes da Equipe 5
        print(f"| {grupo5:<12} | {totalPontos5:<15} | {faceis5:<15} | {medias5:<15} | {dificeis5:<20} | {tempo5:<25.2f} |")

        print("--------------------------------------------------------------")
        input("Pressione Enter para voltar ao menu...")   

#Encerrando o código
elif menu == 6:
        print("Competição encerrada!")