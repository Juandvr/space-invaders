import pygame
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Space Invaders')

    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player(all_sprites, bullets)
    all_sprites.add(player)

    black = (0, 0, 0)
    white = (255, 255, 255)

    clock = pygame.time.Clock()
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            print(event)

        all_sprites.update()

        screen.fill(white)
        all_sprites.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()