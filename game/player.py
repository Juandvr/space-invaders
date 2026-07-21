import pygame
import os
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_path = os.path.join('assets', 'images', 'ship.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))