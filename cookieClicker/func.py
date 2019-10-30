class CookieAnimation:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.anim_bas = True

    def next_anim(self, vitesse):
        # met a jour les coordonnees de l'objet

        #decide si il faut monter ou descendre
        if self.y >= 145:
            self.anim_bas = False
        elif self.y <= 105:
            self.anim_bas = True

        #change les coordonees de y
        if self.anim_bas:
            self.y += vitesse
        else:
            self.y -= vitesse

    def is_clicked(self,mouse_x, mouse_y):
        # renvoie True si la souris est sur le cookie
        if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
            return True
        else:
            return False


class MultiClicker:
    def __init__(self, price_init):
        self.multiplicateur = 1
        self.multiplicateur_price = 1
        self.price_init = price_init

    def buy(self, money):
        money -= self.multiplicateur_price * self.price_init
        self.multiplicateur_price *= 3
        self.multiplicateur *= 2
        return money

    def get_price(self):
        return int(self.multiplicateur_price * self.price_init)

    def get_multiplicateur(self):
        return self.multiplicateur
