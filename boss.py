import pygame

class Boss:

    def __init__(self):

        self.x = 800
        self.y = 200

        self.width = 120
        self.height = 120

        self.health = 500
        self.max_health = 500

        self.speed = 2

    def move(self):

        self.y += self.speed

        if self.y <= 50 or self.y >= 450:
            self.speed *= -1

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (255,0,255),
            (self.x,self.y,self.width,self.height)
        )
