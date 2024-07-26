import pygame
from keyboard import is_pressed
def cuadro_blanco():
    cuadro = []
    for i in range(4):
        linea = []
        for j in range(4):
            c = i * 4 + j + 1
            if c == 16:
                c = 0
            linea.append(c)
        cuadro.append(linea)
    return cuadro
def encuentra_blanco(cuadro:list):
    i = 0
    for linea in cuadro:
        if not 0 in linea:
            i+=1
        else:
            j = linea.index(0)
            return i,j
def wait(miliseg):
    pygame.time.delay(miliseg)
def escribir(screen,texto,x,y,color=(250,250,250)):
    font = pygame.font.SysFont("comic sans",32)
    txt = font.render(texto, True, color)
    screen.blit(txt,(x,y))
class Rompe:
    def __init__(self):
        self.cuadro = cuadro_blanco()
    def dibujar(self,screen):
        for i in range(4):
            for j in range(4):
                x = 100 * j
                y = 100 * i
                cuadrito = self.cuadro[i][j]
                if (cuadrito % 2) == 1:
                    color = (250, 0, 0)
                elif cuadrito == 0:
                    color = (0, 0, 0)
                    cuadrito = ' '
                else:
                    color = (0, 0, 250)
                aux = pygame.rect.Rect(x, y, 100, 100)
                pygame.draw.rect(screen, color, aux)
                pygame.draw.rect(screen, (0, 0, 0), aux, 2)
                escribir(screen, str(cuadrito), x + 40, y + 40)
    def mover(self):
        if is_pressed('r'):
            self.cuadro = cuadro_blanco()
        i,j = encuentra_blanco(self.cuadro)
        a,b = -1,-1
        if is_pressed('down'):
            a= i+1
            b = j
        elif is_pressed('up'):
            a = i-1
            b = j
        elif is_pressed('left'):
            a = i
            b = j-1
        elif is_pressed('right'):
            a = i
            b = j+1
        if not(a>3 or a<0 or b<0 or b>3):
            aux = self.cuadro[i][j]
            self.cuadro[i][j] = self.cuadro[a][b]
            self.cuadro[a][b] = aux
            wait(50)

pygame.init()
# Set up the drawing window
maxx, maxy = 400,400
size = [maxx,maxy]
screen = pygame.display.set_mode(size)
juego = Rompe()
running = True
# Run until the user asks to quit
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if is_pressed('esc') or is_pressed('\n'):
        running = False
    # Fill the background with white
    screen.fill((0, 0, 0))

    #Game
    juego.dibujar(screen)
    juego.mover()
    wait(100)
    #Flip the display
    pygame.display.update()
# Done! Time to quit.
pygame.quit()