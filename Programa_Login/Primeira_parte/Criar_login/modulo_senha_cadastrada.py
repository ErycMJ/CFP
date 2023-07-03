#Modulo para salvar variavel criar_senha na variavel senha_cadastrada

#Importa modulo_criar_senha
import modulo_criar_senha

#Importa modulo_limpar_tela
import modulo_limpar_tela

#Definindo função prar salvar dados
def senha_cadastrada():

    #Chama função limpar_tela do modulo_limpar_tela
    modulo_limpar_tela.limpar_tela()

    #A variavel senha_cadastrada recebe criar_senha
    senha_cadastrada = modulo_criar_senha()
    #Retorna usuario_cadastrado e senha_cadastrada
    return senha_cadastrada
