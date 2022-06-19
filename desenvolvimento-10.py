# Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
# O método deve:

# - calcular três números complexos;
# - realizar todas as operações básicas;
# - e imprimir as propriedades real e img do números. 



class complexos:

    def __init__(self, n1, n2, n3, n4, n5, n6):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5 
        self.n6 = n6  

        complexo1 = complex(self.n1,self.n2)
        complexo2 = complex(self.n3,self.n4)
        complexo3 = complex(self.n5,self.n6)

        self.complexo1 = complexo1
        self.complexo2 = complexo2
        self.complexo3 = complexo3
        
    def numerosComplexos(self):

        print(self.complexo1, self.complexo2, self.complexo3)
        print(self.complexo1.real, self.complexo1.imag, self.complexo2.real, self.complexo2.imag, self.complexo3.real, self.complexo3.imag)

    
    def soma(self):

        complexoNovo = self.complexo1.real + self.complexo2.real + self.complexo3.real, self.complexo1.imag + self.complexo2.imag + self.complexo3.imag
        print("Resultado da soma = ", complexoNovo)
        

    def subtracao(self):

        complexoNovo = self.complexo1.real - self.complexo2.real - self.complexo3.real, self.complexo1.imag - self.complexo2.imag - self.complexo3.imag
        print("Resultado da subtração = ", complexoNovo)
        

    def multiplicacao(self):
        
        complexoNovo = self.complexo1.real * self.complexo2.real * self.complexo3.real, self.complexo1.imag * self.complexo2.imag * self.complexo3.imag
        print("Resultado da multiplicacão = ", complexoNovo)
        

    def divisao(self):

        complexoNovo = self.complexo1.real / self.complexo2.real / self.complexo3.real, self.complexo1.imag / self.complexo2.imag / self.complexo3.imag
        print("Resultado da divisão = ", complexoNovo)



valores = complexos(1,2,3,4,5,6)
valores.numerosComplexos()
valores.soma()
valores.subtracao()
valores.multiplicacao()
valores.divisao()
