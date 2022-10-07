import pygame #provides functions to help you with mulitmedia
import sys #lets you mess with python runtime environment and variables/functions that interact with the interpreter!
#from settings import * #lets you access config/settings properties from all python modules

#----- Class Game ---------------------
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        self.clock = pygame.time.Clock()
        
    def run(self):
        while True: #GAME LOOP!!!!------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #releases memory stuff pygame was holding onto lol
                    sys.exit() #actually exits python interpreter
                    
                dt = self.clock.tick()/1000 #handles FPS
                pygame.display.update() #update is like flip, but we can update *portions* of the screen if we want!

#END OF THE GAME LOOP!!!!--------------------------------------------

#MAIN (starting point of program) --------------------------------------
if __name__=='__main__':
    game = Game() #creates game object from class Game
    game.run() #(insert corny joke about forest running) (LMAO)

