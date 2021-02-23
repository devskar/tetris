from handler.form_handler import FormHandler
from objects.block import Block
import pygame, random

# game width and high in amount of blocks
GAME_WIDTH, GAME_HEIGHT = 10, 20
RECT_SIZE = 25
COLORS = [(250, 176, 0), (241, 79, 28), (107, 126, 247), (150, 46, 19), (0, 163, 232), (124, 180, 0)]


class Tetris:

    def __init__(self):

        self.field = Field()

        self.form_handler = FormHandler()

        self.solid_coords = [[0] * GAME_WIDTH for _ in range(GAME_HEIGHT)]

        self.current_block = None

        self.game_over = False
        self.score = 0
        self.round = 1

        self.__running = False

    def start(self):
        self.create_new_block()
        self.__running = True

        # dropping the block every x milliseconds
        pygame.time.set_timer(self.get_block_down_event, self.get_speed)

    def create_new_block(self):
        del self.current_block
        self.current_block = Block(self.form_handler.get_random_form(), self)

    @property
    def get_speed(self):
        return round(1/self.round * 200) + 50

    @property
    def is_running(self):
        return self.__running

    @property
    def get_rect_size(self):
        return RECT_SIZE

    @property
    def get_game_height(self):
        return GAME_HEIGHT

    @property
    def get_game_width(self):
        return GAME_WIDTH

    @property
    def get_colors(self):
        return COLORS

    @property
    def get_random_color(self):
        return COLORS[random.randint(0, len(COLORS) - 1)]

    @property
    def get_block_down_event(self):
        return pygame.USEREVENT + 1


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

        for y2, row in enumerate(block.form):
            for x2, column in enumerate(row):
                if column == '1':
                    self.draw_rectangle(block.color, block.x+x2, block.y+y2)

    def draw_rectangle(self, color, x, y):
        pygame.draw.rect(self.surface, color, self.__tulip_outer(x, y))

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
