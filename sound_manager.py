import pygame

class SoundManager:

    def __init__(self):

        pygame.mixer.init()

    def play_music(self, path):

        pygame.mixer.music.load(path)

        pygame.mixer.music.play(-1)

    def play_sound(self, sound):

        effect = pygame.mixer.Sound(sound)

        effect.play()
