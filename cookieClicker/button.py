import pygame

class Button(object):
    """docstring for Button."""

    def __init__(self, fenetre, x, y, width, height):
        self.fenetre = fenetre
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.marge = 8
        self.marge_d = int(self.marge *2) # marge [D]oublée
        self.marge_q = int(self.marge *4) # marge [Q]uadruplée
        self.color = (113, 186, 241)
        self.color_fond = (86, 155, 207)
        self.rect = (x - self.marge, y - self.marge, width + self.marge_d, height + self.marge_d)
        self.rect_fond = (x - self.marge_d, y - self.marge_d, width + self.marge_q, height + self.marge_q)

    def draw(self):
        pygame.draw.rect(self.fenetre, self.color_fond, self.rect_fond)
        pygame.draw.rect(self.fenetre, self.color, self.rect)

    def is_clicked(self, position):  # position[0] = x, position[1] = y
        # retourne True si le point indiqué par "position" est dans le boutton
        if self.x - self.marge_d <=position[0] <= self.x +self.width + self.marge_d and\
         self.y - self.marge_d <=position[1] <= self.y + self.height + self.marge_d :
            return True
        else:
            return False
