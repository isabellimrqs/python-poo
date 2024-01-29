class ControleRemoto:

    def __init__(self,televisao,comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal avancado')

    def voltar_canal(self):
        print('Voltou o canal')

    def escolher_canal(self,canal):
        print('alterado para o canal: {}'.format(canal))

controle_sala = ControleRemoto('samsung','sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

controle_quarto = ControleRemoto('LG', 'quarto da isabelli')
print(controle_quarto.comodo)
