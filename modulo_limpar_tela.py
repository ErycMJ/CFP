#Modulo para limpar tela ao longo do programa

#importa bibliotecas para limpar tela e para contagem de tempo
import os, time

#Criando função limpar_tela
def limpar_tela():

    #Tempo de dois segundos
    time.sleep(2)
    #Limpa tela
    os.system('cls')
