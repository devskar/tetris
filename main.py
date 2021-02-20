import pygame
from game import Tetris
from objects.block import Block

BACKGROUND_COLOR = (179, 179, 255)
FIELD_POSITION = (100, 0)
GAME_HEIGHT = 500
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

    # creating tetris object
    tetris = Tetris()

    tetris.field.draw()

    # showing the 'playground' surface on screen
    screen.blit(tetris.field.surface, FIELD_POSITION)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if tetris.is_running:
                    # movement keys
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        tetris.current_block.move_x(1)

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        tetris.current_block.move_x(-1)

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        tetris.current_block.drop(1)

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        tetris.current_block.rotate()

                if not tetris.is_running:
                    tetris.start()

        if tetris.is_running:

            if tetris.current_block.solid:
                for coord in tetris.current_block.coordinates:
                    tetris.solid_coords[coord[0]][coord[1]] = [1]
                    tetris.create_new_block()

            tetris.field.draw()
            tetris.field.draw_block(tetris.current_block)

            tetris.current_block.drop(1)
            screen.blit(tetris.field.surface, FIELD_POSITION)

        pygame.display.flip()


if __name__ == '__main__':
    main()
