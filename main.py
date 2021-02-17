import pygame
from game.game import Tetris

BACKGROUND_COLOR = (179, 179, 255)
GAME_HEIGHT = 600
GAME_WIDTH = 400
FPS = 10


def main():
    # initializing the pygame module
    pygame.init()

    # general information
    pygame.display.set_caption('Tetris')

    # creating screen
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()

    running = True
    clock = pygame.time.Clock()

    tetris = Tetris(screen)

    tetris.current_block.draw()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not tetris.is_running():
                if event.type == pygame.KEYDOWN:
                    tetris.start()

        if tetris.is_running():
            screen.fill(BACKGROUND_COLOR)
            tetris.current_block.draw()
            tetris.current_block.update()

        pygame.display.flip()


if __name__ == '__main__':
    main()
