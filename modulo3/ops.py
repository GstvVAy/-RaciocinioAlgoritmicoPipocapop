class ops:
    def __init__(self, id_produto=str, quantidade_produto=int, Matriz_produto=dict, temp=int ):
        self.idp = id_produto 
        self.quant = quantidade_produto
        self.matriz= Matriz_produto
        self.temp = temp
        
    
    def demanda(self):
        return self.quant/self.temp
    
    def reserva(self):
        return int((self.demanda()*0.2))
    
    def material(self):
        for x in self.matriz:
            self.matriz[x]*=self.quant
        return self.matriz

    
