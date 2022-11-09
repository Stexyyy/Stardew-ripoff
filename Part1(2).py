import pygame #provides functions to help you with mulitmedia
import sys#lets you mess with python runtime environment and variables/functions that interact with the interpreter!
from settings import *
from level import Level

#----- Class Game ---------------------
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        
    def run(self):
        while True: #GAME LOOP!!!!------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #releases memory stuff pygame was holding onto lol
                    sys.exit() #actually exits python interpreter
                dt = self.clock.tick()/1000 #handles FPS
                self.level.run(dt)
                pygame.display.update() #update is like flip, but we can update *portions* of the screen if we want!

#END OF THE GAME LOOP!!!!--------------------------------------------

#MAIN (starting point of program) --------------------------------------
if __name__=='__main__':
    game = Game() #creates game object from class Game
    game.run() #(insert corny joke about forest running) (LMAO)
