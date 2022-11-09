import pygame
from settings import *

class Player(pygame.sprite.Sprite): #this is a child class of pygame's sprite class
    def __init__(self, pos, group):
        super().__init__(group) #this gives this class access to the functions inside the group class
        
        #general setup
        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos) #set the position to be the center of the rect
        
        #movement attributes
        self.direction - pygame.mathVector2() 
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print("up")
        #obviously more directions will be put here
    
    def update(self,dt):
        self.input()
