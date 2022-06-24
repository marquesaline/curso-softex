#  Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 
# e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, 
# ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o 
# erro e continuará perguntando até que um valor correto seja preenchido.



def idade(nome, anoNasc):
    while anoNasc < 1922 or anoNasc > 2021:
        print("Ano de nascimento não esperado. Digite um ano válido: ")
        anoNasc = int(input())
    
    idade = 2022 - anoNasc
    print("Nome completo: " + nome)
    print("Idade: " + str(idade))

print("Digite seu nome completo: ")
nomeCompleto = input()
print("Digite o ano do seu nascimento: ")
anoNasc = int(input())

idade(nomeCompleto, anoNasc)