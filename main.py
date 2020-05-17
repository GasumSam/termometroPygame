import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/termo1.png")

class NumberInput():
    __value = 0
    __strValue = "0"
    __position = [0, 0]
    __size = [0, 0]
    
    def __init__(self, value=0):
        self.__font = pygame.font.SysFont("Arial", 24)
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))  #Creamos un rectángulo como casillero para los datos
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self._position[0]
        rect.top = self.__position[1]
        rect.size = self.__size 
        
        '''
        return {
                "fondo": rect,
                "texto"
            }
        '''
        
        return (rect, textBlock)
        
    #Getter y Setter
        
    def value(self, val=None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val)
                self.__strValue = val
            except:
                pass

    def width(self, val = None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass

    def height(self, val = None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass

    def size(self, val = None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass


    def posX(self, val = None):
        if val == None:
            return self.__position[0]  #Devuelve la coordenada width
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
            
    def posY(self, val = None):
        if val == None:
            return self.__position[1]  #Devuelve la coordenada width
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
            
    def pos(self, val = None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass

class mainApp():   #MainApp refresca la imagen
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))    #Pantalla principal
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244, 236 , 203))
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((106, 58))
        self.entrada.size((133, 28))
                
    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
    #Aquí es donde refresca la imagen
        #Pintamos el termómetro en su posición
            self.__screen.blit(self.termometro.custome, (50, 34))
        #Pintamos el cuadro texto
            text = self.entrada.render()  #Obtenemos rectángulo blanco y foto de texto  lo asignamos a la variable text
            pygame.draw.rect(self._screen, (255, 255, 255), text[0]) #Creamos el rectángulo blanco con sus datos (posición y tamaño) text[0]
            self.__screen.blit(text[1], self.entrada.pos()) #Pintamos la foto del texto (text[1])
            
            pygame.display.flip()
        
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()