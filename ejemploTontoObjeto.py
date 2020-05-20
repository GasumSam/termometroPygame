class Objeto():
    __atributoPrivado = None
    atributoPrivado = None
    
    def __init__(self):
        self.__atributoPrivado = 0
        self.atributoPrivado = "me lo ha pedido Jorge"
        
    def getAtributoPrivado(self):
        return self.__atributoPrivado