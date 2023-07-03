#Modulo para guardar usuario_cadastrado e senha_cadastrado em um dicionário

#Importa modulo_limpar_tela
import modulo_limpar_tela

#Importa modulo_usuario_cadastrado
import modulo_usuario_cadastrado

#Importa modulo_senha_cadastrada
import modulo_senha_cadastrada

#Criar função dicionario_login
def dicionario_login():

    #Chama função limpar_tela do modulo_limpar_tela
    modulo_limpar_tela.limpar_tela()

    #Criando dicionário login
    login = {}
    #Dicionário login armazena senha com usuario
    login[modulo_usuario_cadastrado.usuario_cadastrado()] = modulo_senha_cadastrada.senha_cadastrada()
