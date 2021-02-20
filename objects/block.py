import random
from game import *

colors = [(250, 176, 0), (241, 79, 28), (107, 126, 247), (150, 46, 19), (0, 163, 232), (124, 180, 0)]


class Block:
    def __init__(self, form, tetris):

        self.tetris = tetris
        self.color = get_random_color()
        self.form = form

        # calculates start x value on the field
        self.start_pos = int(5 - len(self.form[0]) / 2)

        self.coordinates = self.calculate_start_coords()

        self.speed = 0

    def update(self):
        pass

    def rotate(self):
        pass

    # adds y value to all coordinates of block and checks if it hits edges
    def drop(self, amount):
        for coord in self.coordinates:
            if not 0 <= (coord[1] + amount) < self.tetris.get_game_height:


                return

        for coord in self.coordinates:
            coord[1] += amount

    # adds x value to all coordinates of block and checks if it hits edges
    def move_x(self, amount):
        for coord in self.coordinates:
            if not 0 <= (coord[0] + amount) < self.tetris.get_game_width:
                return

        for coord in self.coordinates:
            coord[0] += amount

    # returns the start position of the block on the field
    def calculate_start_coords(self):
        coords = []

        # loops through the form of the block and adds all coordinates
        for y, row in enumerate(self.form):
            for x, column in enumerate(self.form[y]):
                # checks if a square belongs to the position
                if column != '0':
                    coords.append([self.start_pos + x, y])
        return coords


# returns a random color
def get_random_color():
    return colors[random.randint(0, len(colors) - 1)]
