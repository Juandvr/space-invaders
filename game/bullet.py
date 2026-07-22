import pygame
import os
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPEED

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_path = os.path.join('assets', 'images', 'bullet.png')
        self.image = pygame.transform.scale_by(pygame.image.load(image_path).convert_alpha(), 8)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.speed = BULLET_SPEED