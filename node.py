# node class
import pygame


class node(object):

    def __init__(self, left, top, width, height, index):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(left, top, width, height)
        self.changed = True
        self.color = (0, 0, 0)
        self.line_width = 1
        self.index = index

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect, self.line_width)

    def clicked(self, win):
        self.color = (0, 255, 0)
        self.line_width = 0
        self.draw(win)

    def isOver(self, pos):
        if self.left < pos[0] < self.left + self.width:
            if self.top < pos[1] < self.top + self.height:
                return True

        return False
