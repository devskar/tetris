import pygame
from game import Tetris

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

                if event.key == pygame.K_r:
                    running = False
                    main()

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

            # checks if the current block became solid
            if tetris.current_block.solid:

                tetris.round += 1

                # adding coordinates from the current block to solid squares
                for coord in tetris.current_block.coordinates:
                    tetris.solid_coords[coord[1]][coord[0]] = 1

                    # creating a new block
                    tetris.create_new_block()

            for row in tetris.solid_coords:
                if row.count(1) == len(row):
                    tetris.solid_coords.remove([1] * 10)
                    tetris.solid_coords.append([0] * 10)

            # re-drawing the field
            tetris.field.draw()

            for y, row in enumerate(tetris.solid_coords):
                for x, column in enumerate(tetris.solid_coords[y]):
                    # checks if a square belongs to the position
                    if column == 1:
                        tetris.field.draw_rectangle((255, 255, 204), x, y)

            # drawing the block on the field
            tetris.field.draw_block(tetris.current_block)

            # dropping the block one square down
            tetris.current_block.drop(1)

            # updating the field on the main surface
            screen.blit(tetris.field.surface, FIELD_POSITION)

        pygame.display.flip()


if __name__ == '__main__':
    main()
