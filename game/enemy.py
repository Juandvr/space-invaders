import pygame
import os
from game.settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_path = os.path.join('assets', 'images', 'alien.png')
        self.og_image = pygame.transform.scale_by(pygame.image.load(image_path).convert_alpha(), 8) 
        self.image = self.og_image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, 50))
        self.hp = 3
        self.speed = 5
        self.hit_image = self.image.copy()
        self.hit_image.fill((255, 255, 255, 0), special_flags=pygame.BLEND_RGB_ADD)
        self.hit_timer = 0
        self.hit_cooldown = 80

    def hit(self, damage):
        if self.image == self.og_image:
            self.hp -= damage
            self.hit_timer = pygame.time.get_ticks()

        if self.hp <= 0:
            self.kill()

    def update(self):
        assert self.rect is not None
        self.rect.x += self.speed

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed *= -1
            self.rect.y += 20
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.center = (50, 50)

        if self.hit_timer > 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.hit_timer < self.hit_cooldown:
                self.image = self.hit_image
            else:
                self.image = self.og_image