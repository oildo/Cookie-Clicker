import pygame

class AutoClicker(object):
    """docstring for AutoClicker."""

    def __init__(self, fenetre, x, y):
        self.fenetre = fenetre
        self.x = x
        self.y = y
        self. height = 50
        self.width = 50
        self.marge = 8
        self.marge_d = int(self.marge*2)  # marge [D]oubléen
        self.marge_q = int(self.marge*4)  # marge [Q]uadruplée
        self.color_rect = (113, 186, 241)
        self.color_fond = (86, 155, 207)
        self.rect = (0, 0, 0, 0)
        self.rect_fond = (0, 0, 0, 0)
        self.price = 15
        self.string_text = str(self.price)


        self.font=pygame.font.Font(None, 40)
        self.text = self.font.render(self.string_text,1,(255,255,255))

        self.image =  pygame.image.load("mouse_click.png").convert_alpha()
        self.previous_add = 1  # pour calculer le prochain "add"
        self.add = 1  # les cookies en plus données

    def is_clicked(self, point):
        if self.x - self.marge_d <= point[0] <= self.x + self.width + self.marge_d and \
         self.y - self.marge_d <= point[1] <= self.y + self.height + self.marge_d:
            return True
        else:
            return False

    def buy(self, money):
        temporary_add = self.add
        self.add += self.previous_add
        self.previous_add = temporary_add
        money -= self.price
        self.price *=2
        return int(money)

    def get_price(self):
        return self.price

    def get_add(self):
        return self.add

    def draw(self):
        self.string_text = str(self.price)
        self.text = self.font.render(self.string_text,1,(255,255,255))

        self.width = self.text.get_width() + self.image.get_width() + 5
        self.height = self.image.get_height()
        self.x = self.fenetre.get_width() - self.width - 30
        self.y = 100

        self.rect = (self.x - self.marge, self.y - self.marge, self.width + self.marge_d, self.height + self.marge_d)
        self.rect_fond = (self.x - self.marge_d, self.y - self.marge_d, self.width + self.marge_q, self.height + self.marge_q)

        pygame.draw.rect(self.fenetre, self.color_fond, self.rect_fond)
        pygame.draw.rect(self.fenetre, self.color_rect, self.rect)

        self.fenetre.blit(self.text, (self.x, self.y))
        self.fenetre.blit(self.image, (self.x + self.text.get_width(), self.y))




















# oh yeah
