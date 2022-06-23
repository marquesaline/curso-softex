# Faça uma função calculadora de dois números com três parâmetros: 
# os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a 
# operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num1, num2, operacao):
    if(operacao == 1):
        soma = num1 + num2
        return "Soma = " + str(soma)
    elif(operacao == 2):
        subtracao = num1 - num2
        return "Subtração = " + str(subtracao)
    elif(operacao == 3):
        multiplicacao = num1 * num2
        return "Multiplicação = " + str(multiplicacao)
    elif(operacao == 4):
        divisao = num1 / num2
        return "Divisão = " + str(divisao)
    else:
        return "Resultado = 0 " 