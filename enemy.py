import pygame
import random

class Enemy:

    def __init__(self):

        self.x = random.randint(700, 950)
        self.y = random.randint(50, 550)

        self.width = 40
        self.height = 40

        self.speed = 3

    def move(self):

        self.x -= self.speed

        if self.x < -50:
            self.x = 1000

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (255,0,0),
            (self.x,self.y,self.width,self.height)
        )
