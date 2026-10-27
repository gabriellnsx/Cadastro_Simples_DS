#Variaveis para cadastro
nome = ""
idade = ""
usuario = ""
senha = ""

#Variaveis para login
login_usuario = ""
login_senha = ""

#Apenas a tela de visualização
while True:
    print("==================")
    print("Sistema de Cadastro")
    print("==================")

    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = input ("Escolha uma opção: ")
    #Funcionalidades
    #Se o usuario digitar o valor 1, vai ser exebido
    # a ação abaixo:
    if (opcao == "1"):
        print("==========================")
        print("=====Tela de Cadastro=====")
        print("==========================")
        nome = input("Digite o seu nome: ")
        idade = input("Digite a sua idade: ")
        usuario = input("Digite seu Usuário: ")
        senha = input("Digite sua senha: ")
        print("\n Cadastro realizado!\n")
        #se digitar 2, abre a tela de login
    elif (opcao == "2"):
            print("===================")
            print("===Tela de Login===")
            print("===================")
            login_usuario = input("Digite o usuário: ")
            login_senha = input("Digite a senha: ")

            #Processamento de usuario e senha
            if login_usuario == usuario  and login_senha == senha:
                while True:
                    print("\nLogin realizado com sucesso!\n")
                    print("Bem vindo,", nome)
                    print("\n=====área do Usuario=====\n")
                    print("1 - Ver os dados cadastrados")
                    print("2 - Voltar para o menu anterior")

                    usuario_opcao = input("Escolha uma das opções do menu acima: ")

                    if (usuario_opcao == "1"):
                        print("\n=====================")
                        print("===Dados Cadastrados===")
                        print("=====================\n")
                        #Mostrar dados do usuário:
                        print("Nome do usuário: ", nome)
                    elif(usuario_opcao == "2"):
                        print("\n Voce está voltando para o menu anterior")
                        break
                    else:
                        print("\nOpção digitada inválida, use os números do Menu!")
                #Se não estiver correto entra no caso abaixo
                else:
                    print("\nUsuário ou senha incorretos\n")

            #se digitar 3, sai da execução
            elif(opcao == "3"):
                print("\nVoce está saindo do cadastro, até mais!\n")
                break
            #Se não for nem 1,2 ou 3, mostrar erro e repetir o código
            else:
                print("Valor digitado, inválido, use apenas números inteiro do menu")