import pygame
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.player import Player
from game.enemy import Alien

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Space Invaders')

    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    player = Player(all_sprites, bullets)
    alien = Alien()
    aliens.add(alien)
    all_sprites.add(player, aliens)

    black = (0, 0, 0)
    white = (255, 255, 255)

    clock = pygame.time.Clock()
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        for bullet in bullets:
            for alien in aliens:
                if bullet.rect.colliderect(alien.rect):
                    alien.hit(bullet.damage)
                    bullet.kill()
                    break

        screen.fill(white)
        all_sprites.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()