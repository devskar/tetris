class Block:
    def __init__(self, form, tetris):

        self.tetris = tetris
        self.color = tetris.get_random_color
        self.form = form
        self.solid = False
        # calculates start x value on the field
        self.start_pos = int(5 - len(self.form[0]) / 2)

        self.direction = 0

        self.y, self.x = 0, self.start_pos
        self.square_coords = self.calculate_square_coords(self.form)

    # rotates the block
    def rotate(self):

        new_form = []

        for i in range(len(self.form[0])):
            row = ''
            for old_row in reversed(self.form):
                row += old_row[i]
            new_form.append(row)

        for coord in self.calculate_square_coords(new_form):
            if self.tetris.solid_coords[coord[1]][coord[0]] == 1:
                return

        self.form = new_form
        self.update_square_coords()

    def drop(self, amount=1):

        for coord in self.square_coords:
            poss_y = coord[1] + amount

            # checks if the block would hit the bottom or top
            if not 0 <= poss_y < self.tetris.get_game_height:
                self.solid = True
                return

            # checks if the block would hit a solid square
            if self.tetris.solid_coords[poss_y][coord[0]] == 1:
                self.solid = True
                return

        self.y += amount
        self.update_square_coords()

    def move_x(self, amount):

        for coord in self.square_coords:
            poss_x = coord[0] + amount

            # checks if the block would hit an edge
            if not 0 <= poss_x < self.tetris.get_game_width:
                return

            # checks if the block would hit a solid square
            if self.tetris.solid_coords[coord[1]][poss_x] == 1:
                return

        # adds amount to all x coordinates
        self.x += amount
        self.update_square_coords()

    def update_square_coords(self):
        self.square_coords = self.calculate_square_coords(self.form)

    def calculate_square_coords(self, form):

        coords = []

        for y, row in enumerate(form):
            for x, column in enumerate(row):
                if column == '1':
                    coords.append([self.x + x, self.y + y])
        return coords
