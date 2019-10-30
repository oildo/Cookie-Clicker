import pygame
from pygame.locals import *
import func
import button
import auto_clicker



# declaration des variables
money = 0
position_cookie = (250,125)
REFRESH_ANIMATION = 1
AUTO_CLICK_TIMER = 2

#initialisation du MultiClicker
multi_clicker = func.MultiClicker(50)

# pre-initialisation du mixer pygame
pygame.mixer.pre_init(30000,-16,2,2048)

# initialisation de pygame
pygame.init()

# creation de la fenetre
fenetre = pygame.display.set_mode((800, 650))
pygame.display.set_caption("cookie clicker")# nom de la fenetre
pygame.display.set_icon(pygame.image.load("icon.png"))

# affichage du fond
fond = pygame.image.load("background_milk.jpg").convert()
fenetre.blit(fond, (0,0))

# affichage du cookie
cookie = pygame.image.load("cookie.png").convert_alpha()
fenetre.blit(cookie, (250, 125))

# initialisation de l'objet d'animation du cookie
animation = func.CookieAnimation(250, 125, 300, 301)

# initialisation de l'image de cookie du score
cookie_score = pygame.image.load("cookie_score.png").convert_alpha()
fenetre.blit(cookie, (0, 0))

# initialisation du son de croc
son_croc = pygame.mixer.Sound("croc.wav")

# initialisation du son de cash
son_cash = pygame.mixer.Sound("cash.wav")

# initialisation d'un timer pour l'animation cookie
pygame.time.set_timer(REFRESH_ANIMATION, 100)

# initialisation d'un timer pour l'auto click
pygame.time.set_timer(AUTO_CLICK_TIMER, 2000)

# initialisation d'une police d'écriture
font=pygame.font.Font(None, 40)

# affichage du score
string_score = str(money)
text_score = font.render(string_score,1,(255,255,255))
fenetre.blit(text_score, (30, 30))

# initialisation d'un texte qui montre le multiplicateur
string_multiplicateur = "x1"
text_multiplicateur = font.render(string_multiplicateur,1,(255,255,255))
fenetre.blit(text_multiplicateur, (30, text_multiplicateur.get_height() + 75))

# affichage dde l'amelioration des clicks
amelioration_cookie = pygame.image.load("amelioration_cookie.png").convert_alpha()
fenetre.blit(amelioration_cookie, (-50, -50))

# affichage du shop de clicks
string_click = str(multi_clicker.get_price())
text_click = font.render(string_click,1,(255,255,255))
pos_click_x =  fenetre.get_width() - text_click.get_width() - amelioration_cookie.get_width() - 30
pos_click_y = 30
position_click = (pos_click_x, pos_click_y)
fenetre.blit(text_score, position_click)
# initialisation d'un bouton pour acheter des multiplicateur de clicks
button_click_x = pos_click_x
button_click_y = pos_click_y
button_click = button.Button(fenetre, button_click_x, button_click_y, text_click.get_width() + amelioration_cookie.get_width(), amelioration_cookie.get_height())#text_click.get_height())

# initialisation de l'objet AutoClicker
auto_click = auto_clicker.AutoClicker(fenetre, 400, 75)

# initialisation d'un texte qui montre les autoclicks
string_auto_click = "+" + str(auto_click.get_add()) + " tt les 2 secs"
text_auto_click = font.render(string_auto_click,1,(255,255,255))
fenetre.blit(text_auto_click, (30, text_auto_click.get_height() + 40))

# rafraichissement de la fenetre
pygame.display.flip()

# message de bienvenue ("bienvenu dans cookie clicker")
pygame.mixer.Sound("msg_bienvenue.wav").play()

#boucle infinie
continuer = True
while continuer:
    for event in pygame.event.get():   # On parcours la liste de tous les événements reçus

        #si on clique sur le cookie
        # cookie.get_rect().collidepoint(event.pos[0], event.pos[1])
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and animation.is_clicked(event.pos[0], event.pos[1]):
            money += multi_clicker.get_multiplicateur()  # on met a jour le score selon le multiplicateur
            string_score = str(money)  # "cookie : " +
            son_croc.play()
        # les facons de quitter le programme
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = False

        if event.type == KEYDOWN and event.key == K_f:
            fenetre_f = pygame.display.set_mode((800, 650))

        if event.type == MOUSEBUTTONDOWN and event.button == 1:

            if button_click.is_clicked(event.pos) and money >= multi_clicker.get_price():
                money = multi_clicker.buy(money)
                string_click = str(multi_clicker.get_price())
                text_click = font.render(string_click,1,(255,255,255))
                string_score = str(money) # met a jour le texte du score
                # mise a jour des coordonnees du texte
                text_click = font.render(string_click,1,(255,255,255))
                pos_click_x =  fenetre.get_width() - text_click.get_width() - amelioration_cookie.get_width() - 30
                pos_click_y = 30
                position_click = (pos_click_x, pos_click_y)
                # mise a jour des coordonees du bouton
                button_click = button.Button(fenetre, pos_click_x, pos_click_y,\
                 text_click.get_width() + amelioration_cookie.get_width(), amelioration_cookie.get_height())
                # mise a jour du texte du multiplicateur
                string_multiplicateur = "x" + str(multi_clicker.get_multiplicateur())
                son_cash.play()

            if auto_click.is_clicked(event.pos) and money >= auto_click.get_price():
                money = auto_click.buy(money)
                string_score = str(money)
                string_auto_click = "+" + str(auto_click.get_add()) + " chaque 2 secs"
                text_auto_click = font.render(string_auto_click,1,(255,255,255))
                son_cash.play()


        # evenement issus de de timers
        if event.type == REFRESH_ANIMATION:
            animation.next_anim(1)  # met a jour lanimation
            position_cookie = (animation.x, animation.y)  # met a jour la position du cookie

        if event.type == AUTO_CLICK_TIMER:
            money += auto_click.get_add()
            string_score = str(money)
            son_croc.play()

    # met a jour les differents textes
    text_score = font.render(string_score,1,(255,255,255))
    text_multiplicateur = font.render(string_multiplicateur,1,(255,255,255))

    # Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(cookie, position_cookie)
    fenetre.blit(text_score, (30, 30))
    fenetre.blit(text_multiplicateur, (30, text_multiplicateur.get_height() + 75))
    fenetre.blit(text_auto_click, (30, text_auto_click.get_height() + 40))
    button_click.draw()
    fenetre.blit(text_click, position_click)
    fenetre.blit(cookie_score, (35 + text_score.get_width(), 27))
    fenetre.blit(amelioration_cookie, (pos_click_x + text_click.get_width() + 5, button_click_y))
    auto_click.draw()



    # rafraichissement de la fenetre
    pygame.display.flip()

#confirmation du bon deroulement du programme
print("\n\n\nle programme s'est terminé normalement")
