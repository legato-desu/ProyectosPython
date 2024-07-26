# 15 game

import pygame
from keyboard import is_pressed
"""
Create a window that runs the 15 game
"""

def white_box():
    chart = []
    for i in range(4):
        line = []
        for j in range(4):
            c = i * 4 + j + 1
            if c == 16:
                c = 0
            line.append(c)
        chart.append(line)
    return chart
def find_target(chart:list):
    i = 0
    for line in chart:
        if not 0 in line:
            i+=1
        else:
            j = line.index(0)
            return i,j
def wait(miliseg):
    pygame.time.delay(miliseg)
def write(screen,texto,x,y,color=(250,250,250)):
    font = pygame.font.SysFont("comic sans",32)
    txt = font.render(texto, True, color)
    screen.blit(txt,(x,y))
class Rompe:
    def __init__(self):
        self.chart = white_box()
    def dibujar(self,screen):
        for i in range(4):
            for j in range(4):
                x = 100 * j
                y = 100 * i
                square = self.chart[i][j]
                if (square % 2) == 1:
                    color = (250, 0, 0)
                elif square == 0:
                    color = (0, 0, 0)
                    square = " "
                else:
                    color = (0, 0, 250)
                aux = pygame.rect.Rect(x, y, 100, 100)
                pygame.draw.rect(screen, color, aux)
                pygame.draw.rect(screen, (0, 0, 0), aux, 2)
                write(screen, str(square), x + 40, y + 40)
    def move(self):
        if is_pressed("r"):
            self.chart = white_box()
        i,j = find_target(self.chart)
        a,b = -1,-1
        if is_pressed("down"):
            a= i+1
            b = j
        elif is_pressed("up"):
            a = i-1
            b = j
        elif is_pressed("left"):
            a = i
            b = j-1
        elif is_pressed("right"):
            a = i
            b = j+1
        if not(a>3 or a<0 or b<0 or b>3):
            aux = self.chart[i][j]
            self.chart[i][j] = self.chart[a][b]
            self.chart[a][b] = aux
            wait(50)

pygame.init()
# Set up the drawing window
maxx, maxy = 400,400
size = [maxx,maxy]
screen = pygame.display.set_mode(size)
game = Rompe()
running = True
# Run until the user asks to quit
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if is_pressed("esc") or is_pressed("\n"):
        running = False
    # Fill the background with white
    screen.fill((0, 0, 0))

    #Game
    game.dibujar(screen)
    game.move()
    wait(100)
    #Flip the display
    pygame.display.update()
# Done! Time to quit.
pygame.quit()