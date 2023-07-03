#Programa inicial

#importando modulo_limpar_tela
import modulo_limpar_tela

import Programa_Login.modulo_importacao_Criar_login as modulo_importacao_Criar_login

#Enquanto verdadeiro roda o programa, para só sair quando a opção sair for selecionada
while True:
    
    #Chama função limpar_tela do modulo_limpar_tela
    modulo_limpar_tela.limpar_tela()
    
    #Printa o nome do programa para o usuário
    print('Controle de finanças Pessoais')

    print('Digite um dos números abaixo para validar uma opção')
    opcao = int(input('(1) Entrar \n(2) Cadastrar \n(3)Sair'))

    match opcao:
        case 1:
            print('Entrar login')
        
        case 2:

            Primeira_parte.Criar_login.modulo_criar_senha.criar_senha()

        case 3:
            break

        case _:
            print('Opção inválida, tente novamente')
            #Contador_Tentartivas