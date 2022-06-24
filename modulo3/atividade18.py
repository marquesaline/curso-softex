#  Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 
# e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, 
# ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o 
# erro e continuará perguntando até que um valor correto seja preenchido.

nomeCompleto = input("Digite seu nome completo: ")
while True:
    anoNasc = input("Digite o ano do nascimento: ")
    try:
        ano = int(anoNasc)
        if(ano):
            while(ano < 1922 or ano > 2021):
                anoNasc = input("Digite um ano válido: ")
                ano = int(anoNasc)
    except ValueError:
        print('Error: Digite um número')
        continue
    else:
        idade = 2022 - ano
        print("Nome completo: " + nomeCompleto)
        print("Idade: " + str(idade))
        break
    
   
   

    
    


