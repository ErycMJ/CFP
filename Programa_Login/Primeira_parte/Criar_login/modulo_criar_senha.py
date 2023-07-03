#Modulo para criar senha

#Importa modulo_limpa_tela
import modulo_limpar_tela

#Criando função criar_senha
def criar_senha():

    #Chama função limpar_tela do modulo_limpar_tela
    modulo_limpar_tela.limpar_tela()

    #Criando senha
    senha = input('Crie uma senha para entrar no programa: ')
    #Retorna senha para uso ao longo do programa
    return senha
