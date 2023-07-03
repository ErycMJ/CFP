#Modulo responsável pela validação de uma senha, para liberar o acesso ao programa

#Importa modulo_criar_senha
import  modulo_criar_senha

#Importa modulo_senha_cadastrada
import modulo_senha_cadastrada

#Criando função senha_valida
def senha_valida():

    #Valida que criar_senha e senha_cadastrada são iguais
    senha_valida = (modulo_criar_senha.criar_senha() == modulo_senha_cadastrada.senha_cadastrada())
    #Retorna usuario_valido para uso ao longo do programa
    return senha_valida
