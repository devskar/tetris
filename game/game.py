from handler.form_handler import FormHandler
from objects.block import Block

# game width and high in amount of blocks
GAME_WIDTH, GAME_HEIGHT = 10, 25


class Tetris:
    def __init__(self, screen):

        self.screen = screen

        self.form_handler = FormHandler()

        self.solid_blocks = []
        self.current_block = Block(self.form_handler.get_random_form(), screen)

        self.game_over = False
        self.score = 0

        self.__running = False

    def start(self):
        self.__running = True
        self.current_block.drop()

    def is_running(self):
        return self.__running
