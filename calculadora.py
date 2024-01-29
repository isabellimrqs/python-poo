class Calculadora:
    def calcular(self,op,n1,n2):
        if op == '+':
            return self.__adicionar(n1,n2)
        elif op == '-':
             return self.__subtrair(n1,n2)
        else: 
            print('Inválido')

    #encapsulamento privado

    def __adicionar(self,n1,n2):
        return n1 + n2
    
    
    def __subtrair(self,n1,n2):
        return n1 - n2
    
conta = Calculadora()
resultado = conta.calcular('-',5,2)
print(resultado)
