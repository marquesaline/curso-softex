# Desenvolva um código que simule uma eleição com três candidatos.
# - candidato_X => 889
# - candidato_Y => 847
# - candidato_Z => 515
# - branco => 0

# O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não 
# corresponda a nenhum candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um 
# texto ao invés de número, o código deve retornar uma mensagem para votar novamente.

# Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de 
# votos e, também, a quantidade de votos de cada candidato, os brancos e nulos 

import enum

class Candidatos(enum.Enum):
    candidatoX = 889
    candidatoY = 847
    candidatoZ = 515
    branco = 0

def votacao(): 
    x = 0
    y = 0
    z = 0
    nulo = 0
    while True:
        voto = input("Informe o seu voto: ")
        
        try: 
            votoNum = int(voto)
            if(votoNum == Candidatos.candidatoX.value):
                x = x + 1
            elif(votoNum == Candidatos.candidatoY.value):
                y = y + 1
            elif(votoNum == Candidatos.candidatoZ.value):
                z = z + 1
            else:
                nulo = nulo + 1
        except ValueError:
            print('Erro: Digite um número')
            continue 
        else: 
            finalizar = input("Deseja encerrar a votação: ")

            if(finalizar == "Sim" or finalizar == "sim"):
                break
            else:
                continue


    if(x > y and x > z):
        print("O candidato vencedor foi: CandidatoX")
    elif(y > x and y > z):
        print("O candidato vencedor foi: CandidatoY")
    elif(z > x and z > y):
        print("O candidato vencedor foi: CandidatoZ")

    print("Quantidade de votos de cada candidato e os votos nulos: ")
    print("CandidatoX: " + str(x))
    print("CandidatoY: " + str(y))
    print("CandidatoZ: " + str(z))
    print("Nulos: " + str(nulo))



votacao()