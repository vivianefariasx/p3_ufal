class Carro:
    def __init__(self, eficiencia,gasolina): 
        self.eficiencia = eficiencia              #eficiencia e valor inicial de gasolina 
        self.gasolina = gasolina

    def dirigir(self, quilometros):
            self.dirigir = quilometros     #quantos km serão dirigidos 

    def abastecer(self, litros):
         self.abastecer = litros    #Abastecer o carro

    def atualizacao (self):
         ga = self.gasolina + self.abastecer   #Atualizar a gasolina 
         return ga 

    def potencia (self):
         g = self.dirigir / self.eficiencia   #Calculo de litros por quilometros 
         return g 

    def nivel_de_gasolina(self):
        x = self.atualizacao() - self.potencia() # Calculo do valor gasto em litros do valor disponivel no tanque 
        return x
    
        
carro1 = Carro (12,0)
carro1.abastecer(60)
carro1.dirigir(96)
carro1.atualizacao()
carro1.potencia()
carro1.nivel_de_gasolina()


print("A eficiencia do motor é de",carro1.eficiencia, "km por litro")
print("A quantidade de gasolina no tanque é", carro1.gasolina, "litros")
print("O carro foi abastecido com", carro1.abastecer, "litros de gasolina")
print("O nivel de gasolina é de:", carro1.atualizacao(), "listros no tanque")
print("Dirigir", carro1.dirigir, "km" )
print("O nivel de gasolina é de:", carro1.nivel_de_gasolina(),"litros no tanque")