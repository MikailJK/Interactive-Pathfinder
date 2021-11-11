import pygame

fill_color = (50, 50, 50)


class button(object):

    def __init__(self, left, top, height, width, image,  win, func):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.func = func
        self.rect = pygame.Rect(left, top, width, height)
        image = pygame.transform.scale(image, (width, height))
        win.blit(image, self.rect)


    def isOver(self, pos):
        if self.left < pos[0] < self.left + self.width:
            if self.top < pos[1] < self.top + self.height:
                return True

        return False

    def clicked(self, win):
        self.func(win)
