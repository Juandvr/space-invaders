import pygame
import os
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED
from game.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets):
        super().__init__()

        image_path = os.path.join('assets', 'images', 'ship.png')
        self.image = pygame.transform.scale_by(pygame.image.load(image_path).convert_alpha(), 8)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.speed = PLAYER_SPEED
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.cooldown = 200
        self.last_shot_time = 0

    def update(self):
        assert self.rect is not None
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_z]:
            self.shoot()

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def shoot(self):
        assert self.rect is not None
        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot_time >= self.cooldown:
            Bullet(self.rect.centerx, self.rect.top, self.all_sprites, self.bullets)
            self.last_shot_time = current_time