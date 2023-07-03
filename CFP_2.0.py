#importa bibliotecas para limpar tela e para contagem de tempo
import os, time

#Comando para limpar tela
os.system('cls')

#Como na primeira vez em que o programa é rodado ainda não temos ninguém cadastrado, 
#As variaveis 'usuario_cadastrado' e 'senha_cadastrada' iniciam vazias
usuario_cadastrado = ''
senha_cadastrada = ''

#Para que não tenha o problema de adivinhação de senha, será iniciado um contador para limitar as tentativas
tentativas = 0

#Para iniciar o programa em loop
i = 0
#valor iniciodo é 0
ganhos = 0
perdas = 0
valor_total = 0
metaMes = 0
metaAno = 0
resultadoMes = 0
resultadoAno = 0
#O programa é iniciado dentro de uma estrutura de repetição, 

#Vai validar a opção do usuário
def receber_numero():
    while True:
        entrada = input("Digite um número: ")
        if entrada.isdigit():
            numero = int(entrada)
            return numero
        else:
            print("\033[0;49;91mEntrada inválida. Digite apenas números.\033[m")

while i == 0:


    #Começo
    print('\033[0;49;36m----Controle de Finanças Pessoais / C.F.P.----\033[m')

    #Opções do usuário
    print('Digite: \n(1) Para Entrar \n(2) Para Cadastrar Usuário \n(3) \033[0;49;91mSair\033[m\n ')


    # Exemplo de uso
    opcao = receber_numero()

    #Utilizando match para executar uma ação de acordo com a escolha do usuário
    match opcao:

        #Se escolha for 1. Entrar 
        case 1:
            #Informar usuário que ele está fazendo um login
            print('Digite usuário e senha para ter acesso as suas informações')

            #Inputação dos dados
            usuario = input('Usuário: ')
            senha = input('Senha: ')
            #Validação de Usuário e Senha

            #Se o usúario inputado pelo usuário bater com um usuário já cadastrado, o usuário entra para usuario_valido
            usuario_valido = (usuario_cadastrado == usuario)
            #Se a senha inputada pelo usuário bater com a senha já cadastrada, vinculada com o usuário, a senha entra para senha_valida
            senha_valida = (senha_cadastrada == senha)

            #Para senha usuario não valido OU senha não valida, o programa volta para opções do usuário 
            if  (not usuario_valido) or (not senha_valida):

                #Pausa de 2 segundos
                time.sleep(1)
                #Limpa a tela
                os.system('cls')

                #Volta pro match case
                print('\033[0;49;91mUsuário ou senha invalidos, tente novamente!\033[m')

                #Soma 1 a tentativas
                tentativas += 1

                #Quando tentativas chega a 3 o programa finaliza 
                if tentativas == 3:
                    #Encerra programa por excesso de tentativas
                    print('Limite de tentativas excedido! Encerrando o programa...')
                    #Pausa de 2 segundos
                    time.sleep(1)
                    #Limpa a tela
                    os.system('cls')
                    #Sai do script
                    break

                #Pausa de 2 segundos
                time.sleep(1)
                #Limpa a tela
                os.system('cls')

            #Para senha usuario valido E senha valida, o programa 'Controle de Finanças Pessoais', ou 'C.F.P.' é iniciado
            elif  usuario_valido and senha_valida:
                #Pausa de 2 segundos
                time.sleep(1)
                #Limpa a tela
                os.system('cls')


                def extrato():
                    print('\033[0;49;36m---------------------Inicio do Programa--------------------------\033[m')
                    # Valor inicial da conta
                     #Deixar global para quando sair do while ficar salvo
                    
                    
                    while True:
                        # Começo
                        print('\033[0;49;36mControle de Finanças Pessoais / C.F.P.\033[m')

                        # Opções do usuário
                        print('Digite: \n(1) Ver Extrato \n(2) Adicionar ganhos e perdas \n(3) Metas do usuario \n(4) Para Tela Inicial\n')

                        # Valida a opção do usuário
                        def receber_numero():
                            while True:
                                entrada = input("Digite um número: ")
                                if entrada.isdigit():
                                    numero = int(entrada)
                                    return numero
                                else:
                                    print("\033[0;49;91mEntrada inválida. Digite apenas números.\033[m")
                       
                        def extrato_numero():
                            global perdas
                            global ganhos
                            global valor_total

                            while True:
                                ganho = input("Digite o valor dos ganhos do mês: ").replace(',', '.')
                                perda = input("Digite o valor das perdas do mês: ").replace(',', '.')
                                if ganho and perda:
                                    ganhos = float(ganho)
                                    perdas = float(perda)
                                    valor_total += ganhos - perdas
                                    return ganhos,perdas,valor_total
                                else:
                                    print("\033[0;49;91mEntrada inválida. Digite apenas números.\033[m")

                        def meta_numero():
                            global metaAno
                            global metaMes
                            global resultadoMes
                            global resultadoAno

                            while True:
                                Mes = input("Digite a meta do mês: ").replace(',', '.')
                                Ano = input("Digite a meta do ano: ").replace(',', '.')

                                if Mes.isdigit() and Ano.isdigit():
                                    metaMes = int(Mes)
                                    metaAno = int(Ano)

                                    resultadoMes = metaMes - valor_total
                                    resultadoAno = metaAno - valor_total
    
                                    return metaAno , metaMes
                                else:
                                    print("\033[0;49;91mEntrada inválida. Digite apenas números.\033[m")

                        # Exemplo de uso
                        number = receber_numero()


                        if number == 1:
                            print(f"Ganhos: R$ {ganhos}")
                            print(f"Perdas: R$ {perdas}\n")
                            print(f"\nMetas: Mês: R$ {metaMes},\nAno: R$ {metaAno}\n")
                            print(f"Valor total na conta: R$ {valor_total}\n")

                        elif number == 2:
                            print("\nDigites os valores\n")
                            
                            extrato_numero()
                            # Calcula o extrato
                            print("Extrato do mês:")
                            print(f"Ganhos: R$ {ganhos}")
                            print(f"Perdas: R$ {perdas}")
                            print(f"Valor total na conta: R$ {valor_total}")
                        
                        elif number == 3:
                            def meta():
                                #Deixar global para quando sair do while ficar salvo
                                global metaAno
                                global metaMes

                                while True:
                                    print('\nDigite: \n(1) Ver Meta \n(2) Adicionar Meta\n(3) \033[0;49;91mVoltar\033[m ')
                                    def receber_numero():
                                        while True:
                                            entrada = input("Digite um número: ")
                                            if entrada.isdigit():
                                                numero = float(entrada)
                                                return numero
                                            else:
                                                print("\033[0;49;91mEntrada inválida. Digite apenas números.\033[m")

                                    # Exemplo de uso
                                    number = receber_numero()


                                    if number == 1:
                                        print(f"Meta para a conta:\nMês: R$ {metaMes},\nAno: R$ {metaAno}")
                                        print(f"Valor na conta: R$ {valor_total}\n")
                                        
                                        print(f"Diferença do valor para a meta:\nMês: R$ {resultadoMes},\nAno: R$ {resultadoAno}")
                                        
                                    elif number == 2:
                                        print("\nDigite os valores\n")
                                        
                                        meta_numero()

                                        print("---- Metas ----")
                                        print(f"Meta para a conta:\nMês: R$ {metaMes},\nAno: R$ {metaAno}\n")

                                    elif number == 3:
                                        break

                            meta()
                        elif number == 4:
                            time.sleep(1)
                            # Limpa a tela
                            os.system('cls')
                            break

                        # Opções do usuário
                        print('\nDigite: (0) Para Voltar\n')
                        voltar = input('Opção: ')

                        if voltar == 0:
                            time.sleep(1)
                            # Limpa a tela
                            os.system('cls')
                        else:
                            #Alerta o usuário de que escolheu uma opção inexistente 
                            print('\033[0;49;91mOpção inválida!\033[m')
                            #Pausa de 2 segundos
                            time.sleep(1)
                            #Limpa a tela
                            os.system('cls')

                extrato()

         #Se escolha for 2. Cadastrar Usuário 
        case 2:
            #Informar usuário que ele está fazendo um cadastro de usuário
            print('Faça o cadastro para ter acesso ao programa!')

            # Captura os valores de nome de usuário e senha dos inputs do usuário
            usuario = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")

            #Salvar os dados cadastrados em variaveis, para validar a opção 1. Entrar
            usuario_cadastrado = usuario
            senha_cadastrada = senha

            print("\033[0;49;92mOs dados foram salvos com sucesso.\033[m")

            #Pausa de 2 segundos
            time.sleep(1)
            #Limpa a tela
            os.system('cls')

        #Se escolha for 3. Sair 
        case 3:
            #Pausa de 2 segundos
            time.sleep(1)
            #Limpa a tela
            os.system('cls')
            #Sai do script
            break

        #Um case que abrange caracteres quaisquer, diferentes dos três especificados
        case _:
            #Alerta o usuário de que escolheu uma opção inexistente 
            print('\033[0;49;91mOpção inválida!\033[m')
            #Pausa de 2 segundos
            time.sleep(1)
            #Limpa a tela
            os.system('cls')
            