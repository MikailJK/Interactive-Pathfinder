# node class
import pygame

open_color = (255, 200, 0 )
closed_color = (52, 191, 105)
path_color = (239, 98, 158)
end_color = (230, 57, 70)
start_color = (1, 186, 239)
wall_color = (11, 79, 108)
background_color = (251, 251, 255)
line_color = (11, 79, 108)


class node(object):

    def __init__(self, left, top, size, x, y, win):
        self.left = left
        self.top = top
        self.size = size
        self.rect = pygame.Rect(left, top, size, size)
        self.changed = True
        self.fill_color = background_color
        self.line_width = 1
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = 0
        self.goal = False
        self.win = win
        self.closed = False
        self.wall = False
        self.open = False

    def draw(self):
        pygame.draw.rect(self.win, self.fill_color, self.rect, 0)
        pygame.draw.rect(self.win, line_color, self.rect, self.line_width)


    def clicked(self, win, selector):
        if selector == 0:
            self.fill_color = wall_color
            self.wall = True
        elif selector == 1:
            self.fill_color = start_color
        elif selector == 2:
            self.fill_color = end_color
            self.goal = True
        #self.line_width = 0
        self.draw()
        return self

    def visited(self):
        self.fill_color = open_color
        self.draw()
        pygame.display.update()

    def draw_path(self):
        self.fill_color = path_color
        self.draw()
        pygame.display.update()

    def isOver(self, pos):
        if self.left < pos[0] < self.left + self.size:
            if self.top < pos[1] < self.top + self.size:
                return True

        return False

    def valid(self):
        if self.closed or self.wall:
            return False
        return True

    def close(self):
        self.closed = True
        self.fill_color = closed_color
        self.draw()
        pygame.display.update()

    def reset(self):
        target = False
        self.fill_color = background_color
        self.draw()
        self.goal = False;
        pygame.display.update()


    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

