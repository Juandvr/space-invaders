import pygame
import os

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        image_path = os.path.join('assets', 'images', 'bullet.png')
        self.image = pygame.transform.scale_by(pygame.image.load(image_path).convert_alpha(), 8)
        self.rect = self.image.get_rect()
        self.speed = 7
        self.rect.centerx = x
        self.rect.top = y

    def update(self):
        assert self.rect is not None
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()