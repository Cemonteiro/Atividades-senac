#orientação objeto
import os
os.system('cls')
class Ave:
    def __init__(self,nome):
        self.possui_penas = True
        self.possui_bico = True
        self.possui_asas = True
        self.nome = nome 
        
    def voa (self):
        if self.possui_asas:
            print(f"Sou um {self.nome} e estou voando :)")
class Passeriformes(Ave):
    pass

class galliformes(Ave):
    def voa(self):
        print (f"Sou uma {self.nome} e eu não consigo voar :(")

pardal = Passeriformes('pardal')
bem_te_vi = Passeriformes('Bem-te-vi')
galinha = galliformes('galinha')
calopsita = Passeriformes('calopsita')

calopsita.voa()
galinha.voa()


# class Monitor:
#     def __init__(self,modelo):
#         self.possui_polegadas = True
#         self.possui_espessura = True
#         self.possui_imagem = True
#         self.modelo = modelo
#     def mostrar_modelo (self):
#         if self.possui_imagem:
#             print (f"modelo do monitor {self.modelo}")    
# Monitor_sansumg = Monitor ('sansumg') 
# Monitor_AOC = Monitor ('AOC')
# Monitor_dell = Monitor ('dell')
# Monitor_sansumg.mostrar_modelo()
# Monitor_AOC.mostrar_modelo()
# Monitor_dell.mostrar_modelo()
