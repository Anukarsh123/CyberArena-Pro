import pygame

class Player:

    def __init__(self):

        self.x = 100
        self.y = 250

        self.width = 50
        self.height = 50

        self.speed = 5

        self.max_health = 100
        self.health = 100

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (0,255,255),
            (self.x,self.y,self.width,self.height)
        )
