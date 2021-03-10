from pathlib import Path
import random

PATH = FILE_PATH = f'{Path(__file__).parents[1]}\\resources\\forms.txt'


class FormHandler:

    def __init__(self):
        self.forms = []
        self.load_forms()

    # taking the forms from forms.txt
    def load_forms(self):

        # opening and reading the txt file
        with open(FILE_PATH, 'r') as file:
            content = file.read()

        temp_array = content.split('\n')

        temp_form = []

        # putting all forms in the forms array together
        for part in temp_array:
            if part == '':
                self.forms.append(temp_form[:])
                temp_form.clear()
            else:
                temp_form.append(part)

    def get_random_form(self):
        return self.forms[random.randint(0, len(self.forms) - 1)]

