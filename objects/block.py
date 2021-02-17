import pygame

RECT_SIZE = 20


class Block:
    def __init__(self, form, screen):
        self.screen = screen
        self.color = (255, 255, 255)
        self.form = form
        self.solid = False

        self.speed = 0
        self.x, self.y = 100, 10

    def drop(self):
        self.speed = 20

    def update(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, RECT_SIZE, RECT_SIZE])

    def rotate(self):
        pass

    def push(self):
        pass