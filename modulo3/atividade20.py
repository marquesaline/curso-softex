# Instruções do projeto
# Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter 
# a seguinte estrutura:

# aluno: Nome do aluno;
# nota_1: Primeira nota;
# nota_2: Segunda nota;
# faltas: Número de faltas;

# O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média 
# das duas notas do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

# O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa 
# deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

# Por fim, o programa deverá mostrar na tela:
# - o maior número de faltas;
# - a média geral das notas dos alunos;
# - e a maior média.

# Veja em anexo um exemplo do arquivo “notas_alunos.csv”.


import pandas as panda

df = panda.read_csv("modulo3/notas_alunos.csv")

def alunosSituacao(dataframe):

    media_alunos = (dataframe["nota_1"] + dataframe["nota_2"]) / 2

    dataframe = dataframe.assign(media = media_alunos)

    dataframe['situacao'] = ''

    dataframe.loc[(dataframe["media"] < 7) | (dataframe["faltas"] > 5),  "situacao"] = "Reprovado"
    dataframe.loc[(dataframe["media"] >= 7) & (dataframe["faltas"] < 5),  "situacao"] = "Aprovado"

    print(dataframe)
    maiorFalta = dataframe['faltas'].max()
    mediaNotas = dataframe[['nota_1', 'nota_2']].median()
    maiorMedia =dataframe['media'].max()

    print("Maior quantidade de faltas: " + str(maiorFalta))
    print("Média geral das notas: " + str(mediaNotas))
    print("Maior média: " + str(maiorMedia))
    dataframe.to_csv("modulo3/alunos_situacao.csv")


alunosSituacao(df)

