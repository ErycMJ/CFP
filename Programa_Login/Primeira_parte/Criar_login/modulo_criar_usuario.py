#Modulo para criar usuario

#Importa modulo_limpa_tela
import modulo_limpar_tela

#Criando função criar_usuario
def criar_usuario():

    #Chama função limpar_tela do modulo_limpar_tela
    modulo_limpar_tela.limpar_tela()

    #Criando usuário
    usuario = input('Crie um usuário para entrar no programa: ')
    #Retorna usuario para uso ao longo do programa
    return usuario
