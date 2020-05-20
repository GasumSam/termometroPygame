import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/termo1.png")

    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        return "{:10.2f}".format(resultado) 

class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad = "C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))

        self.__tipoUnidad = unidad
        
    def custome(self):
        if self.__tipoUnidad == 'F':
            return self.__customes[0]
        else:
            return self.__customes[1]
        
    def change(self):
        if self.__tipoUnidad == 'F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
            
    def unidad(self):
        return self.__tipoUnidad     #Return responde
            

class NumberInput():
    #Esto pertenece a toda la clase, a todos las las funciones, no necesita un self
    __value = 0  #Valor del cuadrito en numérico
    __strValue = "0"   #Valor cadena | #Esta clase, al estar fuera del constructor no podrá alterarse, el constructor lee de aquí
    __position = [0, 0]  #Atributo posición esquina
    __size = [0, 0] #Atributo tamaño
    __pointsCount = 0
    
    
    def __init__(self, value=0):  #Constructor  | Si no tiene parámetros coge los que aparezcan por defecto para el objeto NumberInput
        self.__font = pygame.font.SysFont("Arial", 24)
        self.value(value)  #Si ya lo tengo hecho, me llamo a mi mismo
        
        '''
        try:
            self.__strValue = int(value)  #Aparece un self como atributo del objeto, se invoca a toda la clase
            self.__strValue = str(value)
        except:
            pass

        ''' 
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointsCount == 0):  #Limitamos a 10 caracteres 
                self.__strValue += event.unicode
                self.value(self.__strValue)
                if event.unicode == '.':
                    self.__pointsCount += 1
            elif event.key == K_BACKSPACE:
                if self.__strValue[-1] == '.':
                    self.__pointsCount -= 1
                self.__strValue = self._strValue[:-1]
                self.value(self.__strValue)
  
             
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))  #Creamos un rectángulo como casillero para los datos
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
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
       # print(val)  #Para saber qué está entrando
        if val == None:
            return self.__value
        else:
            val = str(val)
            print(val, "cadena")
            try:
                self.__value = float(val)  #Al meter una cadena con decimales en un int PETA
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
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
       # self.__screen.fill((244, 236 , 203))  A la línea 182
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((106, 58))
        self.entrada.size((133, 28))
        
        self.selector = Selector()
                
    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    #Control de eventos
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)
                    
        #Pintamos el fondo de pantalla
                self.__screen.fill((144, 236, 203))
                    
    #Aquí es donde refresca la imagen
        #Pintamos el termómetro en su posición
            self.__screen.blit(self.termometro.custome, (50, 34))
        #Pintamos el cuadro texto
            text = self.entrada.render()  #Obtenemos rectángulo blanco y foto de texto  lo asignamos a la variable text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) #Creamos el rectángulo blanco con sus datos (posición y tamaño) text[0]
            self.__screen.blit(text[1], self.entrada.pos()) #Pintamos la foto del texto (text[1])
            
            #Pintamos el selector  |  SE HA CAMBIADO SELECTOR POR __SCREEN, DABA FALLO
            self.__screen.blit(self.selector.custome(), (112, 153))  # Creo Custome en la línea 18
            
            pygame.display.flip()
        
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()