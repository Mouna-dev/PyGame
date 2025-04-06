import pygame
import time
import random

pygame.init()

blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)


largeur = 600
hauteur = 400


taille_bloc = 10


vitesse = 15


ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake Game")


clock = pygame.time.Clock()


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def ton_score(score):
    value = score_font.render(f"Score: {score}", True, bleu)
    ecran.blit(value, [0, 0])


def snake(taille_bloc, liste_snake):
    for bloc in liste_snake:
        pygame.draw.rect(ecran, noir, [bloc[0], bloc[1], taille_bloc, taille_bloc])


def message(msg, color):
    msg_surface = font_style.render(msg, True, color)
    ecran.blit(msg_surface, [largeur / 6, hauteur / 3])

def jeu():
    game_over = False
    game_close = False

    x1 = largeur / 2
    y1 = hauteur / 2

    x1_changement = 0
    y1_changement = 0

    liste_snake = []
    longueur_snake = 1

    pomme_x = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
    pomme_y = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0

    while not game_over:

        while game_close:
            ecran.fill(blanc)
            message("Game Over! Appuyez sur C pour rejouer ou Q pour quitter", rouge)
            ton_score(longueur_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jeu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_changement = -taille_bloc
                    y1_changement = 0
                elif event.key == pygame.K_RIGHT:
                    x1_changement = taille_bloc
                    y1_changement = 0
                elif event.key == pygame.K_UP:
                    y1_changement = -taille_bloc
                    x1_changement = 0
                elif event.key == pygame.K_DOWN:
                    y1_changement = taille_bloc
                    x1_changement = 0

        if x1 >= largeur or x1 < 0 or y1 >= hauteur or y1 < 0:
            game_close = True

        x1 += x1_changement
        y1 += y1_changement
        ecran.fill(blanc)

        pygame.draw.rect(ecran, vert, [pomme_x, pomme_y, taille_bloc, taille_bloc])

        tete = [x1, y1]
        liste_snake.append(tete)
        if len(liste_snake) > longueur_snake:
            del liste_snake[0]

        for bloc in liste_snake[:-1]:
            if bloc == tete:
                game_close = True

        snake(taille_bloc, liste_snake)
        ton_score(longueur_snake - 1)

        pygame.display.update()

        if x1 == pomme_x and y1 == pomme_y:
            pomme_x = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
            pomme_y = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0
            longueur_snake += 1

        clock.tick(vitesse)

    pygame.quit()
    quit()

jeu()