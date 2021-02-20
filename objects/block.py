import random

colors = [(250, 176, 0), (241, 79, 28), (107, 126, 247), (150, 46, 19), (0, 163, 232), (124, 180, 0)]


class Block:
    def __init__(self, form):

        self.color = self.__get_random_color()
        self.form = form

        # calculates start position on the field
        self.start_pos = int(5 - len(self.form[0]) / 2)

        self.coordinates = self.calculate_start_coords()

        self.speed = 0

    def drop(self):
        self.speed = 20

    def update(self):
        pass

    def rotate(self):
        pass

    def push(self):
        pass

    # adds x and y amount to all coordinates
    def change_coords(self, x_amount, y_amount):
        for coord in self.coordinates:
            coord[0] += x_amount
            coord[1] += y_amount

    # returns the start position of the block on the field
    def calculate_start_coords(self):
        coords = []

        # loops through the form of the block and adds all coordinates
        for y, row in enumerate(self.form):
            for x, column in enumerate(self.form[y]):
                # checks if a square belongs to the position
                if column != '0':
                    coords.append((self.start_pos + x, y))
        return coords

    # returns a random color
    def __get_random_color(self):
        return colors[random.randint(0, len(colors) - 1)]
