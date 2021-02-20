class Block:
    def __init__(self, form, tetris):

        self.tetris = tetris
        self.color = tetris.get_random_color
        self.form = form
        self.solid = False
        # calculates start x value on the field
        self.start_pos = int(5 - len(self.form[0]) / 2)

        self.coordinates = self.calculate_start_coords()

    # rotates the block
    def rotate(self):

        new_form = []

        for i in range(len(self.form[0])):
            row = ''
            for old_row in reversed(self.form):
                row += old_row[i]
            new_form.append(row)

        self.form = new_form


    def drop(self, amount):

        for coord in self.coordinates:
            poss_y = coord[1] + amount

            # checks if the block would hit the bottom or top
            if not 0 <= poss_y < self.tetris.get_game_height:
                self.solid = True
                return

            # checks if the block would hit a solid square
            if self.tetris.solid_coords[poss_y][coord[0]] == 1:
                self.solid = True
                return

        for coord in self.coordinates:
            # adds amount to all y coordinates
            coord[1] += amount

    def move_x(self, amount):

        for coord in self.coordinates:
            poss_x = coord[0] + amount

            # checks if the block would hit an edge
            if not 0 <= poss_x < self.tetris.get_game_width:
                return

            # checks if the block would hit a solid square
            if self.tetris.solid_coords[coord[1]][poss_x] == 1:
                return

        for coord in self.coordinates:
            # adds amount to all x coordinates
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
