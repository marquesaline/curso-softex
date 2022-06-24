# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar. 

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 


def calculadora():
    opcao = ""
    while opcao != "0":
        print("Digite uma das opções de operações da calculadora: \n 1: Soma \n 2: Subtração \n 3: Multiplicação \n 4: Divisão \n 0: Sair ")
        opcao = int(input())

        if(opcao == 0):
            break

        elif(opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4):
            print("Digite o 1º valor: ")
            num1 = int(input())
            print("Digite o 2º valor: ")
            num2 = int(input())
            if(opcao == 1):
                resultado = num1 + num2
                print("Resultado = " + str(resultado))
            elif(opcao == 2):
                resultado = num1 - num2
                print("Resultado = " + str(resultado))
            elif(opcao == 3):
                resultado = num1 * num2
                print("Resultado = " + str(resultado))
            elif(opcao == 4):
                resultado = num1 / num2
                print("Resultado = " + str(resultado))
        else: 
            print("Essa opção não existe")
           

calculadora()