import os


#imprimindo cabeçalho
print("==============================================================")
print("               MARATONA DE PROGRAMAÇÃO - UEFS                 ")
print("==============================================================")
print("\n                Bem-vindo à competição!")
print("==============================================================")
print("\n")
print("\n")
print("\n")
os.system('cls')        


# Inicializar a variável menu
menu = 0
while menu != 6:
#Exibição do menu
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
    menu = int(input("Escolha uma opção: "))
    os.system('cls')  

    if menu == 1:
#Inputs do peso pelo usuário
        os.system('cls')        
        pesoFaceis = int(input("Digite o peso das questões fáceis: "))
        pesoMedias = int(input("Digite o peso das questões médias: "))
        pesoDificeis = int(input("Digite o peso das questões difíceis: "))
        print("\nPesos inseridos com sucesso!\n")
        input("Pressione Enter para voltar ao menu...")
        os.system('cls')  

#Definindo o nome das equipes
    elif menu == 2:
        os.system('cls')  
        grupo1 = input("Digite o nome da equipe 1: ")
        grupo2 = input("Digite o nome da equipe 2: ")
        grupo3 = input("Digite o nome da equipe 3: ")
        grupo4 = input("Digite o nome da equipe 4: ")
        grupo5 = input("Digite o nome da equipe 5: ")
        print("\nNome das equipes inseridas com sucesso!\n")
        input("Pressione Enter para voltar ao menu...")
        os.system('cls')  

    elif menu == 3:
        #Equipe 1
        os.system('cls')    
        faceis1 = int(input("Digite quantas questões fáceis o grupo 1 acertou: "))
        medias1 = int(input("Digite quantas questões médias o grupo 1 acertou: "))
        dificeis1 = int(input("Digite quantas questões difíceis o grupo 1 acertou: "))
        tempo1 = int(input("Digite em minutos quanto tempo a equipe demorou para terminar: "))
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
        input("Pressione Enter para voltar ao menu...")
        os.system('cls')  
    
    elif menu == 4:
        os.system('cls')
        # Verificando empates no primeiro lugar
        if totalPontos1 == totalPontos2 == totalPontos3 == totalPontos4 == totalPontos5:
            if tempo1 < tempo2 and tempo1 < tempo3 and tempo1 < tempo4 and tempo1 < tempo5:
                primeiro = grupo1
            elif tempo2 < tempo1 and tempo2 < tempo3 and tempo2 < tempo4 and tempo2 < tempo5:
                primeiro = grupo2
            elif tempo3 < tempo1 and tempo3 < tempo2 and tempo3 < tempo4 and tempo3 < tempo5:
                primeiro = grupo3
            elif tempo4 < tempo1 and tempo4 < tempo2 and tempo4 < tempo3 and tempo4 < tempo5:
                primeiro = grupo4
            else:
                primeiro = grupo5
        elif totalPontos1 == totalPontos2:
            if tempo1 < tempo2:
                primeiro = grupo1
            elif tempo2 < tempo1:
                primeiro = grupo2
            else:
                if dificeis1 < dificeis2:
                    primeiro = grupo1
                elif dificeis2 < dificeis1:
                    primeiro = grupo2
                else:
                    primeiro = grupo1  # ou grupo2, se preferir
        
        elif totalPontos1 == totalPontos3:
            if tempo1 < tempo3:
                primeiro = grupo1
            elif tempo3 < tempo1:
                primeiro = grupo3
            else:
                if dificeis1 < dificeis3:
                    primeiro = grupo1
                elif dificeis3 < dificeis1:
                    primeiro = grupo3
                else:
                    primeiro = grupo1  # ou grupo3, se preferir
        
        elif totalPontos2 == totalPontos3:
            if tempo2 < tempo3:
                primeiro = grupo2
            elif tempo3 < tempo2:
                primeiro = grupo3
            else:
                if dificeis2 < dificeis3:
                    primeiro = grupo2
                elif dificeis3 < dificeis2:
                    primeiro = grupo3
                else:
                    primeiro = grupo2  # ou grupo3, se preferir
        
        elif totalPontos1 == totalPontos4:
            if tempo1 < tempo4:
                primeiro = grupo1
            elif tempo4 < tempo1:
                primeiro = grupo4
            else:
                if dificeis1 < dificeis4:
                    primeiro = grupo1
                elif dificeis4 < dificeis1:
                    primeiro = grupo4
                else:
                    primeiro = grupo1  # ou grupo4, se preferir

        elif totalPontos2 == totalPontos4:
            if tempo2 < tempo4:
                primeiro = grupo2
            elif tempo4 < tempo2:
                primeiro = grupo4
            else:
                if dificeis2 < dificeis4:
                    primeiro = grupo2
                elif dificeis4 < dificeis2:
                    primeiro = grupo4
                else:
                    primeiro = grupo2  # ou grupo4, se preferir
        
        elif totalPontos3 == totalPontos4:
            if tempo3 < tempo4:
                primeiro = grupo3
            elif tempo4 < tempo3:
                primeiro = grupo4
            else:
                if dificeis3 < dificeis4:
                    primeiro = grupo3
                elif dificeis4 < dificeis3:
                    primeiro = grupo4
                else:
                    primeiro = grupo3  # ou grupo4, se preferir

        # Determinando o segundo lugar após desempate do primeiro
        if primeiro == grupo1:
            # Considerar os restantes
            if totalPontos2 > totalPontos3 and totalPontos2 > totalPontos4 and totalPontos2 > totalPontos5:
                segundo = grupo2
            elif totalPontos3 > totalPontos2 and totalPontos3 > totalPontos4 and totalPontos3 > totalPontos5:
                segundo = grupo3
            elif totalPontos4 > totalPontos2 and totalPontos4 > totalPontos3 and totalPontos4 > totalPontos5:
                segundo = grupo4
            else:
                segundo = grupo5
            
            # Verificando empates no segundo lugar
            if totalPontos2 == totalPontos3:
                if tempo2 < tempo3:
                    segundo = grupo2
                elif tempo3 < tempo2:
                    segundo = grupo3
                else:
                    if dificeis2 < dificeis3:
                        segundo = grupo2
                    elif dificeis3 < dificeis2:
                        segundo = grupo3
                    else:
                        segundo = grupo2  # ou grupo3, se preferir
            
            elif totalPontos2 == totalPontos4:
                if tempo2 < tempo4:
                    segundo = grupo2
                elif tempo4 < tempo2:
                    segundo = grupo4
                else:
                    if dificeis2 < dificeis4:
                        segundo = grupo2
                    elif dificeis4 < dificeis2:
                        segundo = grupo4
                    else:
                        segundo = grupo2  # ou grupo4, se preferir

            elif totalPontos3 == totalPontos4:
                if tempo3 < tempo4:
                    segundo = grupo3
                elif tempo4 < tempo3:
                    segundo = grupo4
                else:
                    if dificeis3 < dificeis4:
                        segundo = grupo3
                    elif dificeis4 < dificeis3:
                        segundo = grupo4
                    else:
                        segundo = grupo3  # ou grupo4, se preferir

        elif primeiro == grupo2:
            # Considerar os restantes
            if totalPontos1 > totalPontos3 and totalPontos1 > totalPontos4 and totalPontos1 > totalPontos5:
                segundo = grupo1
            elif totalPontos3 > totalPontos1 and totalPontos3 > totalPontos4 and totalPontos3 > totalPontos5:
                segundo = grupo3
            elif totalPontos4 > totalPontos1 and totalPontos4 > totalPontos3 and totalPontos4 > totalPontos5:
                segundo = grupo4
            else:
                segundo = grupo5
            
            # Verificando empates no segundo lugar
            if totalPontos1 == totalPontos3:
                if tempo1 < tempo3:
                    segundo = grupo1
                elif tempo3 < tempo1:
                    segundo = grupo3
                else:
                    if dificeis1 < dificeis3:
                        segundo = grupo1
                    elif dificeis3 < dificeis1:
                        segundo = grupo3
                    else:
                        segundo = grupo1  # ou grupo3, se preferir
            
            elif totalPontos1 == totalPontos4:
                if tempo1 < tempo4:
                    segundo = grupo1
                elif tempo4 < tempo1:
                    segundo = grupo4
                else:
                    if dificeis1 < dificeis4:
                        segundo = grupo1
                    elif dificeis4 < dificeis1:
                        segundo = grupo4
                    else:
                        segundo = grupo1  # ou grupo4, se preferir
            
            elif totalPontos3 == totalPontos4:
                if tempo3 < tempo4:
                    segundo = grupo3
                elif tempo4 < tempo3:
                    segundo = grupo4
                else:
                    if dificeis3 < dificeis4:
                        segundo = grupo3
                    elif dificeis4 < dificeis3:
                        segundo = grupo4
                    else:
                        segundo = grupo3  # ou grupo4, se preferir

        elif primeiro == grupo3:
            # Considerar os restantes
            if totalPontos1 > totalPontos2 and totalPontos1 > totalPontos4 and totalPontos1 > totalPontos5:
                segundo = grupo1
            elif totalPontos2 > totalPontos1 and totalPontos2 > totalPontos4 and totalPontos2 > totalPontos5:
                segundo = grupo2
            elif totalPontos4 > totalPontos1 and totalPontos4 > totalPontos2 and totalPontos4 > totalPontos5:
                segundo = grupo4
            else:
                segundo = grupo5
            
            # Verificando empates no segundo lugar
            if totalPontos1 == totalPontos2:
                if tempo1 < tempo2:
                    segundo = grupo1
                elif tempo2 < tempo1:
                    segundo = grupo2
                else:
                    if dificeis1 < dificeis2:
                        segundo = grupo1
                    elif dificeis2 < dificeis1:
                        segundo = grupo2
                    else:
                        segundo = grupo1  # ou grupo2, se preferir
            
            elif totalPontos1 == totalPontos4:
                if tempo1 < tempo4:
                    segundo = grupo1
                elif tempo4 < tempo1:
                    segundo = grupo4
                else:
                    if dificeis1 < dificeis4:
                        segundo = grupo1
                    elif dificeis4 < dificeis1:
                        segundo = grupo4
                    else:
                        segundo = grupo1  # ou grupo4, se preferir
            
            elif totalPontos2 == totalPontos4:
                if tempo2 < tempo4:
                    segundo = grupo2
                elif tempo4 < tempo2:
                    segundo = grupo4
                else:
                    if dificeis2 < dificeis4:
                        segundo = grupo2
                    elif dificeis4 < dificeis2:
                        segundo = grupo4
                    else:
                        segundo = grupo2  # ou grupo4, se preferir

        elif primeiro == grupo4:
            # Considerar os restantes
            if totalPontos1 > totalPontos2 and totalPontos1 > totalPontos3 and totalPontos1 > totalPontos5:
                segundo = grupo1
            elif totalPontos2 > totalPontos1 and totalPontos2 > totalPontos3 and totalPontos2 > totalPontos5:
                segundo = grupo2
            elif totalPontos3 > totalPontos1 and totalPontos3 > totalPontos2 and totalPontos3 > totalPontos5:
                segundo = grupo3
            else:
                segundo = grupo5
            
            # Verificando empates no segundo lugar
            if totalPontos1 == totalPontos2:
                if tempo1 < tempo2:
                    segundo = grupo1
                elif tempo2 < tempo1:
                    segundo = grupo2
                else:
                    if dificeis1 < dificeis2:
                        segundo = grupo1
                    elif dificeis2 < dificeis1:
                        segundo = grupo2
                    else:
                        segundo = grupo1  # ou grupo2, se preferir
            
            elif totalPontos1 == totalPontos3:
                if tempo1 < tempo3:
                    segundo = grupo1
                elif tempo3 < tempo1:
                    segundo = grupo3
                else:
                    if dificeis1 < dificeis3:
                        segundo = grupo1
                    elif dificeis3 < dificeis1:
                        segundo = grupo3
                    else:
                        segundo = grupo1  # ou grupo3, se preferir
            
            elif totalPontos2 == totalPontos3:
                if tempo2 < tempo3:
                    segundo = grupo2
                elif tempo3 < tempo2:
                    segundo = grupo3
                else:
                    if dificeis2 < dificeis3:
                        segundo = grupo2
                    elif dificeis3 < dificeis2:
                        segundo = grupo3
                    else:
                        segundo = grupo2  # ou grupo3, se preferir

        # Determinando o terceiro lugar após desempate do primeiro e segundo
        if primeiro == grupo1 and segundo == grupo2:
            if totalPontos3 > totalPontos4 and totalPontos3 > totalPontos5:
                terceiro = grupo3
            elif totalPontos4 > totalPontos3 and totalPontos4 > totalPontos5:
                terceiro = grupo4
            else:
                terceiro = grupo5
            
            # Verificando empates no terceiro lugar
            if totalPontos3 == totalPontos4:
                if tempo3 < tempo4:
                    terceiro = grupo3
                elif tempo4 < tempo3:
                    terceiro = grupo4
                else:
                    if dificeis3 < dificeis4:
                        terceiro = grupo3
                    elif dificeis4 < dificeis3:
                        terceiro = grupo4
                    else:
                        terceiro = grupo3  # ou grupo4, se preferir
            
            elif totalPontos3 == totalPontos5:
                if tempo3 < tempo5:
                    terceiro = grupo3
                elif tempo5 < tempo3:
                    terceiro = grupo5
                else:
                    if dificeis3 < dificeis5:
                        terceiro = grupo3
                    elif dificeis5 < dificeis3:
                        terceiro = grupo5
                    else:
                        terceiro = grupo3  # ou grupo5, se preferir
            
            elif totalPontos4 == totalPontos5:
                if tempo4 < tempo5:
                    terceiro = grupo4
                elif tempo5 < tempo4:
                    terceiro = grupo5
                else:
                    if dificeis4 < dificeis5:
                        terceiro = grupo4
                    elif dificeis5 < dificeis4:
                        terceiro = grupo5
                    else:
                        terceiro = grupo4  # ou grupo5, se preferir

        elif primeiro == grupo1 and segundo == grupo3:
            if totalPontos2 > totalPontos4 and totalPontos2 > totalPontos5:
                terceiro = grupo2
            elif totalPontos4 > totalPontos2 and totalPontos4 > totalPontos5:
                terceiro = grupo4
            else:
                terceiro = grupo5
            
            # Verificando empates no terceiro lugar
            if totalPontos2 == totalPontos4:
                if tempo2 < tempo4:
                    terceiro = grupo2
                elif tempo4 < tempo2:
                    terceiro = grupo4
                else:
                    if dificeis2 < dificeis4:
                        terceiro = grupo2
                    elif dificeis4 < dificeis2:
                        terceiro = grupo4
                    else:
                        terceiro = grupo2  # ou grupo4, se preferir
            
            elif totalPontos2 == totalPontos5:
                if tempo2 < tempo5:
                    terceiro = grupo2
                elif tempo5 < tempo2:
                    terceiro = grupo5
                else:
                    if dificeis2 < dificeis5:
                        terceiro = grupo2
                    elif dificeis5 < dificeis2:
                        terceiro = grupo5
                    else:
                        terceiro = grupo2  # ou grupo5, se preferir
            
            elif totalPontos4 == totalPontos5:
                if tempo4 < tempo5:
                    terceiro = grupo4
                elif tempo5 < tempo4:
                    terceiro = grupo5
                else:
                    if dificeis4 < dificeis5:
                        terceiro = grupo4
                    elif dificeis5 < dificeis4:
                        terceiro = grupo5
                    else:
                        terceiro = grupo4  # ou grupo5, se preferir

        elif primeiro == grupo1 and segundo == grupo4:
            if totalPontos2 > totalPontos3 and totalPontos2 > totalPontos5:
                terceiro = grupo2
            elif totalPontos3 > totalPontos2 and totalPontos3 > totalPontos5:
                terceiro = grupo3
            else:
                terceiro = grupo5
            
            # Verificando empates no terceiro lugar
            if totalPontos2 == totalPontos3:
                if tempo2 < tempo3:
                    terceiro = grupo2
                elif tempo3 < tempo2:
                    terceiro = grupo3
                else:
                    if dificeis2 < dificeis3:
                        terceiro = grupo2
                    elif dificeis3 < dificeis2:
                        terceiro = grupo3
                    else:
                        terceiro = grupo2  # ou grupo3, se preferir
            
            elif totalPontos2 == totalPontos5:
                if tempo2 < tempo5:
                    terceiro = grupo2
                elif tempo5 < tempo2:
                    terceiro = grupo5
                else:
                    if dificeis2 < dificeis5:
                        terceiro = grupo2
                    elif dificeis5 < dificeis2:
                        terceiro = grupo5
                    else:
                        terceiro = grupo2  # ou grupo5, se preferir
            
            elif totalPontos3 == totalPontos5:
                if tempo3 < tempo5:
                    terceiro = grupo3
                elif tempo5 < tempo3:
                    terceiro = grupo5
                else:
                    if dificeis3 < dificeis5:
                        terceiro = grupo3
                    elif dificeis5 < dificeis3:
                        terceiro = grupo5
                    else:
                        terceiro = grupo3  # ou grupo5, se preferir

        elif primeiro == grupo2 and segundo == grupo3:
            if totalPontos1 > totalPontos4 and totalPontos1 > totalPontos5:
                terceiro = grupo1
            elif totalPontos4 > totalPontos1 and totalPontos4 > totalPontos5:
                terceiro = grupo4
            else:
                terceiro = grupo5
            
            # Verificando empates no terceiro lugar
            if totalPontos1 == totalPontos4:
                if tempo1 < tempo4:
                    terceiro = grupo1
                elif tempo4 < tempo1:
                    terceiro = grupo4
                else:
                    if dificeis1 < dificeis4:
                        terceiro = grupo1
                    elif dificeis4 < dificeis1:
                        terceiro = grupo4
                    else:
                        terceiro = grupo1  # ou grupo4, se preferir
            
            elif totalPontos1 == totalPontos5:
                if tempo1 < tempo5:
                    terceiro = grupo1
                elif tempo5 < tempo1:
                    terceiro = grupo5
                else:
                    if dificeis1 < dificeis5:
                        terceiro = grupo1
                    elif dificeis5 < dificeis1:
                        terceiro = grupo5
                    else:
                        terceiro = grupo1  # ou grupo5, se preferir
            
            elif totalPontos4 == totalPontos5:
                if tempo4 < tempo5:
                    terceiro = grupo4
                elif tempo5 < tempo4:
                    terceiro = grupo5
                else:
                    if dificeis4 < dificeis5:
                        terceiro = grupo4
                    elif dificeis5 < dificeis4:
                        terceiro = grupo5
                    else:
                        terceiro = grupo4  # ou grupo5, se preferir

        elif primeiro == grupo2 and segundo == grupo4:
            if totalPontos1 > totalPontos3 and totalPontos1 > totalPontos5:
                terceiro = grupo1
            elif totalPontos3 > totalPontos1 and totalPontos3 > totalPontos5:
                terceiro = grupo3
            else:
                terceiro = grupo5
            
            # Verificando empates no terceiro lugar
            if totalPontos1 == totalPontos3:
                if tempo1 < tempo3:
                    terceiro = grupo1
                elif tempo3 < tempo1:
                    terceiro = grupo3
                else:
                    if dificeis1 < dificeis3:
                        terceiro = grupo1
                    elif dificeis3 < dificeis1:
                        terceiro = grupo3
                    else:
                        terceiro = grupo1  # ou grupo3, se preferir
            
            elif totalPontos1 == totalPontos5:
                if tempo1 < tempo5:
                    terceiro = grupo1
                elif tempo5 < tempo1:
                    terceiro = grupo5
                else:
                    if dificeis1 < dificeis5:
                        terceiro = grupo1
                    elif dificeis5 < dificeis1:
                        terceiro = grupo5
                    else:
                        terceiro = grupo1  # ou grupo5, se preferir
            
            elif totalPontos3 == totalPontos5:
                if tempo3 < tempo5:
                    terceiro = grupo3
                elif tempo5 < tempo3:
                    terceiro = grupo5
                else:
                    if dificeis3 < dificeis5:
                        terceiro = grupo3
                    elif dificeis5 < dificeis3:
                        terceiro = grupo5
                    else:
                        terceiro = grupo3  # ou grupo5, se preferir

        elif primeiro == grupo3 and segundo == grupo4:
            if totalPontos1 > totalPontos2 and totalPontos1 > totalPontos5:
                terceiro = grupo1
            elif totalPontos2 > totalPontos1 and totalPontos2 > totalPontos5:
                terceiro = grupo2
            else:
                terceiro = grupo5
            
            # Verificando empates no terceiro lugar
            if totalPontos1 == totalPontos2:
                if tempo1 < tempo2:
                    terceiro = grupo1
                elif tempo2 < tempo1:
                    terceiro = grupo2
                else:
                    if dificeis1 < dificeis2:
                        terceiro = grupo1
                    elif dificeis2 < dificeis1:
                        terceiro = grupo2
                    else:
                        terceiro = grupo1  # ou grupo2, se preferir
            
            elif totalPontos1 == totalPontos5:
                if tempo1 < tempo5:
                    terceiro = grupo1
                elif tempo5 < tempo1:
                    terceiro = grupo5
                else:
                    if dificeis1 < dificeis5:
                        terceiro = grupo1
                    elif dificeis5 < dificeis1:
                        terceiro = grupo5
                    else:
                        terceiro = grupo1  # ou grupo5, se preferir
            
            elif totalPontos2 == totalPontos5:
                if tempo2 < tempo5:
                    terceiro = grupo2
                elif tempo5 < tempo2:
                    terceiro = grupo5
                else:
                    if dificeis2 < dificeis5:
                        terceiro = grupo2
                    elif dificeis5 < dificeis2:
                        terceiro = grupo5
                    else:
                        terceiro = grupo2  # ou grupo5, se preferir

        elif primeiro == grupo4 and segundo == grupo5:
            if totalPontos1 > totalPontos2 and totalPontos1 > totalPontos3:
                terceiro = grupo1
            elif totalPontos2 > totalPontos1 and totalPontos2 > totalPontos3:
                terceiro = grupo2
            else:
                terceiro = grupo3
            
            # Verificando empates no terceiro lugar
            if totalPontos1 == totalPontos2:
                if tempo1 < tempo2:
                    terceiro = grupo1
                elif tempo2 < tempo1:
                    terceiro = grupo2
                else:
                    if dificeis1 < dificeis2:
                        terceiro = grupo1
                    elif dificeis2 < dificeis1:
                        terceiro = grupo2
                    else:
                        terceiro = grupo1  # ou grupo2, se preferir
            
            elif totalPontos1 == totalPontos3:
                if tempo1 < tempo3:
                    terceiro = grupo1
                elif tempo3 < tempo1:
                    terceiro = grupo3
                else:
                    if dificeis1 < dificeis3:
                        terceiro = grupo1
                    elif dificeis3 < dificeis1:
                        terceiro = grupo3
                    else:
                        terceiro = grupo1  # ou grupo3, se preferir
            
            elif totalPontos2 == totalPontos3:
                if tempo2 < tempo3:
                    terceiro = grupo2
                elif tempo3 < tempo2:
                    terceiro = grupo3
                else:
                    if dificeis2 < dificeis3:
                        terceiro = grupo2
                    elif dificeis3 < dificeis2:
                        terceiro = grupo3
                    else:
                        terceiro = grupo2  # ou grupo3, se preferir

            # Determinando o primeiro lugar
        if totalPontos1 >= totalPontos2 and totalPontos1 >= totalPontos3 and totalPontos1 >= totalPontos4 and totalPontos1 >= totalPontos5:
            primeiro = grupo1
            totalPontosPrimeiro = totalPontos1
            tempoPrimeiro = tempo1
            dificiesPrimeiro = dificeis1
            totalPontos2, totalPontos3, totalPontos4, totalPontos5 = totalPontos2, totalPontos3, totalPontos4, totalPontos5
        elif totalPontos2 >= totalPontos1 and totalPontos2 >= totalPontos3 and totalPontos2 >= totalPontos4 and totalPontos2 >= totalPontos5:
            primeiro = grupo2
            totalPontosPrimeiro = totalPontos2
            tempoPrimeiro = tempo2
            dificiesPrimeiro = dificeis2
            totalPontos1, totalPontos3, totalPontos4, totalPontos5 = totalPontos1, totalPontos3, totalPontos4, totalPontos5
        elif totalPontos3 >= totalPontos1 and totalPontos3 >= totalPontos2 and totalPontos3 >= totalPontos4 and totalPontos3 >= totalPontos5:
            primeiro = grupo3
            totalPontosPrimeiro = totalPontos3
            tempoPrimeiro = tempo3
            dificiesPrimeiro = dificeis3
            totalPontos1, totalPontos2, totalPontos4, totalPontos5 = totalPontos1, totalPontos2, totalPontos4, totalPontos5
        elif totalPontos4 >= totalPontos1 and totalPontos4 >= totalPontos2 and totalPontos4 >= totalPontos3 and totalPontos4 >= totalPontos5:
            primeiro = grupo4
            totalPontosPrimeiro = totalPontos4
            tempoPrimeiro = tempo4
            dificiesPrimeiro = dificeis4
            totalPontos1, totalPontos2, totalPontos3, totalPontos5 = totalPontos1, totalPontos2, totalPontos3, totalPontos5
        else:
            primeiro = grupo5
            totalPontosPrimeiro = totalPontos5
            tempoPrimeiro = tempo5
            dificiesPrimeiro = dificeis5
            totalPontos1, totalPontos2, totalPontos3, totalPontos4 = totalPontos1, totalPontos2, totalPontos3, totalPontos4

        # Determinando o segundo lugar
        if totalPontos1 >= totalPontos2 and totalPontos1 >= totalPontos3 and totalPontos1 >= totalPontos4:
            segundo = grupo1
            totalPontosSegundo = totalPontos1
            tempoSegundo = tempo1
            dificiesSegundo = dificeis1
        elif totalPontos2 >= totalPontos1 and totalPontos2 >= totalPontos3 and totalPontos2 >= totalPontos4:
            segundo = grupo2
            totalPontosSegundo = totalPontos2
            tempoSegundo = tempo2
            dificiesSegundo = dificeis2
        elif totalPontos3 >= totalPontos1 and totalPontos3 >= totalPontos2 and totalPontos3 >= totalPontos4:
            segundo = grupo3
            totalPontosSegundo = totalPontos3
            tempoSegundo = tempo3
            dificiesSegundo = dificeis3
        else:
            segundo = grupo4
            totalPontosSegundo = totalPontos4
            tempoSegundo = tempo4
            dificiesSegundo = dificeis4

        # Determinando o terceiro lugar
        if totalPontos1 >= totalPontos2 and totalPontos1 >= totalPontos3:
            terceiro = grupo1
            totalPontosTerceiro = totalPontos1
            tempoTerceiro = tempo1
            dificiesTerceiro = dificeis1
        elif totalPontos2 >= totalPontos1 and totalPontos2 >= totalPontos3:
            terceiro = grupo2
            totalPontosTerceiro = totalPontos2
            tempoTerceiro = tempo2
            dificiesTerceiro = dificeis2
        else:
            terceiro = grupo3
            totalPontosTerceiro = totalPontos3
            tempoTerceiro = tempo3
            dificiesTerceiro = dificeis3

        # Determinando o quarto lugar
        if totalPontos1 >= totalPontos2 and totalPontos1 >= totalPontos3 and totalPontos1 >= totalPontos4:
            quarto = grupo1
            totalPontosQuarto = totalPontos1
            tempoQuarto = tempo1
            dificiesQuarto = dificeis1
        elif totalPontos2 >= totalPontos1 and totalPontos2 >= totalPontos3 and totalPontos2 >= totalPontos4:
            quarto = grupo2
            totalPontosQuarto = totalPontos2
            tempoQuarto = tempo2
            dificiesQuarto = dificeis2
        elif totalPontos3 >= totalPontos1 and totalPontos3 >= totalPontos2 and totalPontos3 >= totalPontos4:
            quarto = grupo3
            totalPontosQuarto = totalPontos3
            tempoQuarto = tempo3
            dificiesQuarto = dificeis3
        else:
            quarto = grupo4
            totalPontosQuarto = totalPontos4
            tempoQuarto = tempo4
            dificiesQuarto = dificeis4

        # Determinando o quinto lugar
        if totalPontos1 >= totalPontos2 and totalPontos1 >= totalPontos3 and totalPontos1 >= totalPontos4 and totalPontos1 >= totalPontos5:
            quinto = grupo1
            totalPontosQuinto = totalPontos1
            tempoQuinto = tempo1
            dificiesQuinto = dificeis1
        elif totalPontos2 >= totalPontos1 and totalPontos2 >= totalPontos3 and totalPontos2 >= totalPontos4 and totalPontos2 >= totalPontos5:
            quinto = grupo2
            totalPontosQuinto = totalPontos2
            tempoQuinto = tempo2
            dificiesQuinto = dificeis2
        elif totalPontos3 >= totalPontos1 and totalPontos3 >= totalPontos2 and totalPontos3 >= totalPontos4 and totalPontos3 >= totalPontos5:
            quinto = grupo3
            totalPontosQuinto = totalPontos3
            tempoQuinto = tempo3
            dificiesQuinto = dificeis3
        elif totalPontos4 >= totalPontos1 and totalPontos4 >= totalPontos2 and totalPontos4 >= totalPontos3 and totalPontos4 >= totalPontos5:
            quinto = grupo4
            totalPontosQuinto = totalPontos4
            tempoQuinto = tempo4
            dificiesQuinto = dificeis4
        else:
            quinto = grupo5
            totalPontosQuinto = totalPontos5
            tempoQuinto = tempo5
            dificiesQuinto = dificeis5
        os.system('cls')    
        # Calculando a média total de acertos
        mediaTotal = (totalPontos1 + totalPontos2 + totalPontos3 + totalPontos4 + totalPontos5) / 5

        # Exibindo o ranking final com tabulação, total de pontos e média de acertos
        print("--------------------------------------------------------------")
        print("                     RANKING GERAL                           ")
        print("--------------------------------------------------------------")
        # Exibindo o ranking com formatação e média total
        print(f"1º - {primeiro:<12} | Pontos: {totalPontosPrimeiro:<4}")
        print(f"2º - {segundo:<12} | Pontos: {totalPontosSegundo:<4}")
        print(f"3º - {terceiro:<12} | Pontos: {totalPontosTerceiro:<4}")
        print(f"4º - {quarto:<12} | Pontos: {totalPontosQuarto:<4}")
        print(f"5º - {quinto:<12} | Pontos: {totalPontosQuinto:<4}")
        print("-" * 40)
        print(f"Média Total de Pontos: {mediaTotal:.2f}")
        print("="*40)


    elif menu == 5:
        # Exibindo o detalhamento de cada equipe
        os.system('cls')    
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


    elif menu == 6:
        print("Acabou caralho!")
