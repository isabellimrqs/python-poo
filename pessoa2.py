class Pessoa2:
    def __init__(self,name: str,idade: int) -> None:
        self.name = name
        self.idade = idade

    def dirigir(self,veiculo: str) -> None:
        print('Dirigindo um(a) {}'.format(veiculo))

    def cantar(self) -> None:
        print('Lalalala')
    
    def apresentar_documento(self) -> int :
        return self.idade
    
pessoa2 = Pessoa2('Isabelli',18)
att = pessoa2.apresentar_documento
print(att)

