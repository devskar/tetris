from handler.form_handler import FormHandler
from objects.block import Block
import pygame

# game width and high in amount of blocks
GAME_WIDTH, GAME_HEIGHT = 10, 20
RECT_SIZE = 25


class Tetris:

    def __init__(self):

        self.field = Field()

        self.form_handler = FormHandler()

        self.solid_squares = []
        self.current_block = None

        self.game_over = False
        self.score = 0
        self.round = 0

        self.__running = False

    def start(self):
        self.__running = True
        self.current_block = Block(self.form_handler.get_random_form())
        # self.current_block.drop()
        self.field.draw_block(self.current_block)

    def is_running(self):
        return self.__running

    @staticmethod
    def get_rect_size():
        return RECT_SIZE


class Field:

    def __init__(self):
        self.surface = pygame.Surface((GAME_WIDTH * RECT_SIZE, GAME_HEIGHT * RECT_SIZE))
        self.squares = [[0] * GAME_WIDTH] * GAME_HEIGHT

    def draw(self):
        for y in range(len(self.squares)):
            for x in range(len(self.squares[y])):
                # draw outer square
                pygame.draw.rect(self.surface, (64, 64, 64), self.__tulip_outer(x, y))
                # draw inner square
                pygame.draw.rect(self.surface, (0, 0, 0), self.__tulip_inner(x, y))

    # draws the block at the top of the field
    def draw_block(self, block: Block):

        for coord in block.coordinates:
            pygame.draw.rect(self.surface, block.color, self.__tulip_outer(coord[0], coord[1]))

        # # loops through the form of the block and draws all the squares
        # for y, row in enumerate(block.form):
        #     for x, column in enumerate(block.form[y]):
        #         # checks if a square belongs to the position
        #         if column != '0':
        #             pygame.draw.rect(self.surface, block.color, self.__tulip_outer(start_pos + x, y))
        #             # self.draw_outer_square(start_pos + x, y, block.color)
        #             # self.draw_inner_square(start_pos + x, y, (0, 0, 0))

    def draw_outer_square(self, x, y, color):
        pygame.draw.rect(self.surface, color, self.__tulip_outer(x, y))

    def draw_inner_square(self, x, y, color):
        pygame.draw.rect(self.surface, color, self.__tulip_inner(x, y))

    # returns the tulip needed to create the outer square
    @staticmethod
    def __tulip_outer(x, y):
        return x * RECT_SIZE, y * RECT_SIZE, RECT_SIZE, RECT_SIZE

    # returns the tulip needed to create the inner square
    @staticmethod
    def __tulip_inner(x, y):
        return x * RECT_SIZE + 2, y * RECT_SIZE + 2, RECT_SIZE - 4, RECT_SIZE - 4
