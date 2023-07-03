#Modulo responsável pela validação de um usuário, para liberar o acesso ao programa

#Importa modulo_criar_usuario
import modulo_criar_usuario

#Importar modulo_usuario_cadastrado
import modulo_usuario_cadastrado

#Importa modulo_limpar_tela
import modulo_limpar_tela

#Criando função usuario_valido
def usuario_valido():

    #Chama função limpar_tela do modulo_limpar_tela
    modulo_limpar_tela.limpar_tela()

    #Valida que criar_usuario e usuario_cadastrado são iguais
    usuario_valido = ( modulo_criar_usuario.criar_usuario() == modulo_usuario_cadastrado.usuario_cadastrado())
    #Retorna usuario_valido para uso ao longo do programa
    return usuario_valido
