import pygame

class Renderer:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 36)