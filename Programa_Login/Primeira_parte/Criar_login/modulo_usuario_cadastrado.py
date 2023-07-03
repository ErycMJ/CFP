#Modulo para salvar variavel criar_usuario na variavel usuario_cadastrado

#Importa modulo_criar_usuario
import  modulo_criar_usuario

#Importa modulo_limpar_tela
import modulo_limpar_tela

#Criando função usuario_cadastrado
def usuario_cadastrado():

    #Chama função limpar_tela do modulo_limpar_tela
    modulo_limpar_tela.limpar_tela()
    
    #A variavel usuario_cadastrado recebe criar_usuario
    usuario_cadastrado = modulo_criar_usuario.criar_usuario()
    #Retorna usuario_valido para uso ao longo do programa
    return usuario_cadastrado
