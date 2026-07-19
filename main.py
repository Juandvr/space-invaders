import pygame
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    pygame.init()

    gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Space Invaders')

    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            print(event)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()