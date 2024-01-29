class MinhaClasse: 
    estatico = 'Lhama' #Variável de classe

    def __init__(self,estado):
        self.estado = estado

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)
MinhaClasse.estatico = 'Developer'

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
