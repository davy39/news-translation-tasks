---
title: Tutoriel PyGame – Comment créer un jeu de balle rebondissante
subtitle: ''
author: Juan P. Romano
co_authors: []
series: null
date: '2024-01-23T22:46:54.000Z'
originalURL: https://freecodecamp.org/news/pygame-tutorial-build-a-bouncing-game
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/bouncing_ball.png
tags:
- name: Game Development
  slug: game-development
- name: pygame
  slug: pygame
- name: Python
  slug: python
seo_title: Tutoriel PyGame – Comment créer un jeu de balle rebondissante
seo_desc: 'In this tutorial, you''ll learn how to create a simple yet funny bouncing
  ball game using the PyGame library.

  Whether you''re a beginner seeking to grasp the fundamentals of game development
  or an enthusiast eager to explore PyGame''s capabilities, this...'
---

Dans ce tutoriel, vous apprendrez à créer un jeu simple mais amusant de balle rebondissante en utilisant la bibliothèque PyGame.

Que vous soyez un débutant cherchant à comprendre les bases du développement de jeux ou un passionné désireux d'explorer les capacités de PyGame, cet article est votre guide pour créer un jeu simple mais captivant.

Vous devez simplement décomposer les étapes, lire le code et profiter du voyage !

À la fin de ce tutoriel, votre jeu devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/bouncing_game.png align="left")

## Table des matières

1. [Comment installer l'environnement de développement](#heading-installation)

2. [Définir le concept du jeu](#heading-definir-le-concept-du-jeu)

3. [Initialisation de l'application](#heading-initialisation-de-lapplication)

4. [Comment créer une instance PyGame](#heading-comment-creer-une-instance-pygame)

5. [Comment créer les écrans du jeu](#heading-comment-creer-les-ecrans-du-jeu)

6. [Boucle principale du jeu](#heading-boucle-principale-du-jeu)

7. [Conclusion](#heading-conclusion)

## Comment installer l'environnement de développement

### Outils et logiciels

Avant de vous lancer dans l'aventure du codage, parlons des outils qui alimenteront votre créativité.

#### Python

Vous utiliserez Python, un langage de programmation polyvalent et adapté aux débutants. Sa syntaxe claire et son vaste support de bibliothèques en font un excellent choix pour le développement de jeux.

Si vous n'avez pas Python installé, rendez-vous sur [python.org](https://www.python.org/) pour télécharger et installer la dernière version.

#### PyGame

Votre arme secrète pour ce projet. PyGame, un ensemble de modules Python, simplifie le développement de jeux en gérant des éléments multimédias comme les images et les sons. C'est le moteur qui alimentera votre jeu.

Pour installer PyGame, vous pouvez utiliser la commande suivante dans votre terminal ou invite de commandes :

```bash
pip install pygame
```

#### Éditeur de texte

Que ce soit VSCode, PyCharm ou Thonny, ces environnements offrent des fonctionnalités comme la coloration syntaxique et des outils de débogage. Choisissez celui avec lequel vous êtes le plus à l'aise, et préparons-nous à écrire du code !

J'utiliserai VSCode, mais n'hésitez pas à utiliser celui que vous préférez. Si vous vous sentez aventureux, vous pouvez essayer Thonny !

Maintenant que vous êtes armé des bons outils, plongeons dans le code et donnons vie à votre jeu.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/screenshot-1.png align="left")

*Ceci est Thonny*

## Définir le concept du jeu

### Concept et mécaniques du jeu

Décomposons les concepts et mécaniques de base que vous allez implémenter.

**Contrôle de la plateforme :**

* Objectif : Utiliser les touches fléchées pour déplacer la plateforme vers la gauche ou la droite.

* Implémentation : Votre plateforme se déplace horizontalement en fonction des entrées clavier.

* Limites : Assurez-vous que la plateforme reste dans les limites de l'écran.

**Dynamique de la balle rebondissante :**

* Objectif : Guider la balle rebondissante à travers l'écran.

* Implémentation : La balle se déplace indépendamment, rebondissant sur les murs et la plateforme.

* Interaction : Marquez des points chaque fois que la balle rebondit avec succès sur la plateforme.

**Système de score :**

* Objectif : Accumuler des points en fonction des rebonds réussis.

* Implémentation : Votre codage détermine le système de score.

* Défi : Optimisez le mécanisme de score pour des scores plus élevés.

**Progression des niveaux :**

* Objectif : Avancer à travers les niveaux à mesure que votre score atteint des paliers.

* Implémentation : À chaque 10 points, vous passez à un nouveau niveau.

* Défi : Attendez-vous à une difficulté et une complexité accrues à chaque niveau.

**Couleur dynamique de la plateforme :**

* Objectif : La couleur de la plateforme change à chaque niveau, ajoutant une dynamique visuelle.

* Implémentation : Les couleurs sont générées aléatoirement lors de l'atteinte d'un nouveau niveau.

* Touche esthétique : Ajoute de la variété et de l'excitation à l'expérience de jeu.

**Vies et fin de jeu :**

* Objectif : Évitez de laisser la balle tomber hors de l'écran pour conserver vos vies.

* Implémentation : Les vies diminuent avec les rebonds manqués. La fin de jeu survient lorsque les vies sont épuisées (vous n'avez que 3 vies).

* Redémarrage : Après la fin de jeu, redémarrez avec trois vies et un score frais.

## Comment coder le jeu

### Initialisation de l'application

Dans cette section, vous définirez des constantes telles que les dimensions de l'écran, les propriétés de la balle et de la plateforme, et les couleurs.

Vous initialiserez également PyGame, configurerez l'écran d'affichage et créerez un objet horloge pour contrôler le taux de rafraîchissement.

Ensuite, vous initialiserez les variables pour le jeu, y compris la position de la balle, la vitesse, la position de la plateforme, la vitesse, le score, les vies et le niveau actuel.

Voici le code pour faire tout cela :

```python
import pygame
import sys
import random

# Constantes
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 10
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)  # Couleur bleu clair pour l'indicateur de niveau
```

Décomposons le code étape par étape :

**Importation des bibliothèques :**

* `import pygame` : Importe la bibliothèque Pygame, utilisée pour développer des jeux en Python.

* `import sys` : Importe le module sys, fournissant l'accès à certaines variables utilisées ou maintenues par l'interpréteur et à des fonctions qui interagissent avec l'interpréteur.

**Constantes :**

* `WIDTH, HEIGHT = 800, 600` : Définit les dimensions de la fenêtre de jeu.

* `BALL_RADIUS = 20` : Spécifie le rayon de la balle rebondissante.

* `PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 10` : Définit les dimensions de la plateforme.

* `FPS = 60` : Définit les images par seconde, contrôlant la vitesse du jeu.

* Diverses constantes de couleur comme `BLACK`, `WHITE`, `RED`, `YELLOW`, `ORANGE` et `LIGHT_BLUE` représentent les valeurs RVB des couleurs utilisées dans le jeu.

## Comment créer une instance PyGame

Maintenant, vous allez créer la fenêtre PyGame et définir quelques variables globales que vous utiliserez pour chaque niveau du jeu :

```python
# Initialiser Pygame
pygame.init()

# Créer l'écran
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")
font = pygame.font.Font(None, 36)

# Horloge pour contrôler le taux de rafraîchissement
clock = pygame.time.Clock()

# Initialiser les variables pour le jeu
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]  # Vitesse de départ plus rapide
platform_pos = [WIDTH // 2 - PLATFORM_WIDTH // 2, HEIGHT - PLATFORM_HEIGHT - 10]
platform_speed = 10
score = 0
lives = 3
current_level = 1
platform_color = ORANGE  # Initialiser la couleur de la plateforme
```

**Initialisation de Pygame :**

* `pygame.init()` : Initialise la bibliothèque Pygame.

**Créer la fenêtre de jeu :**

* `screen = pygame.display.set_mode((WIDTH, HEIGHT))` : Crée la fenêtre de jeu avec les dimensions spécifiées.

* `pygame.display.set_caption("Bouncing Ball Game")` : Définit le titre de la fenêtre de jeu.

* `font = pygame.font.Font(None, 36)` : Initialise un objet de police pour le rendu du texte.

**Horloge pour le contrôle du taux de rafraîchissement :**

* `clock = pygame.time.Clock()` : Crée un objet horloge pour contrôler le taux de rafraîchissement.

**Initialisation des variables de jeu :**

* `ball_pos = [WIDTH // 2, HEIGHT // 2]` : Initialise la position de départ de la balle au centre de l'écran.

* `ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]` : Initialise la vitesse de départ de la balle avec des valeurs aléatoires.

* `platform_pos = [WIDTH // 2 - PLATFORM_WIDTH // 2, HEIGHT - PLATFORM_HEIGHT - 10]` : Initialise la position de départ de la plateforme.

* `platform_speed = 10` : Définit la vitesse à laquelle la plateforme se déplace.

* `score = 0` : Initialise le score du joueur.

* `lives = 3` : Initialise le nombre de vies du joueur.

* `current_level = 1` : Initialise le niveau actuel du jeu.

* `platform_color = ORANGE` : Initialise la couleur de la plateforme.

## Comment créer les écrans du jeu

Vous allez créer au moins trois écrans, un pour démarrer le jeu, un pour gagner le jeu et un pour perdre le jeu. Vous pouvez utiliser le code suivant pour faire tout cela :

```python
# Fonctions pour les écrans
def start_screen():
    screen.fill(BLACK)
    show_text_on_screen("Bouncing Ball Game", 50, HEIGHT // 4)
    show_text_on_screen("Appuyez sur n'importe quelle touche pour commencer...", 30, HEIGHT // 3)
    show_text_on_screen("Déplacez la plateforme avec les touches fléchées...", 30, HEIGHT // 2)
    pygame.display.flip()
    wait_for_key()

def game_over_screen():
    screen.fill(BLACK)
    show_text_on_screen("Game Over", 50, HEIGHT // 3)
    show_text_on_screen(f"Votre score final : {score}", 30, HEIGHT // 2)
    show_text_on_screen("Appuyez sur n'importe quelle touche pour redémarrer...", 20, HEIGHT * 2 // 3)
    pygame.display.flip()
    wait_for_key()

def victory_screen():
    screen.fill(BLACK)
    show_text_on_screen("Félicitations !", 50, HEIGHT // 3)
    show_text_on_screen(f"Vous avez gagné avec un score de {score}", 30, HEIGHT // 2)
    show_text_on_screen("Appuyez sur n'importe quelle touche pour quitter...", 20, HEIGHT * 2 // 3)
    pygame.display.flip()
    wait_for_key()

def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def show_text_on_screen(text, font_size, y_position):
    font = pygame.font.Font(None, font_size)
    text_render = font.render(text, True, WHITE)
    text_rect = text_render.get_rect(center=(WIDTH // 2, y_position))
    screen.blit(text_render, text_rect)

def change_platform_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
```

Passons en revue les fonctions :

Fonction `start_screen()` :

* Efface l'écran avec un fond noir en utilisant `screen.fill(BLACK)`.

* Affiche le titre du jeu et les instructions en utilisant `show_text_on_screen`.

* Met à jour l'affichage pour rendre les changements visibles avec `pygame.display.flip()`.

* Appelle `wait_for_key()` pour attendre une pression de touche avant de continuer.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-105.png align="left")

Fonction `game_over_screen()` :

* Efface l'écran avec un fond noir.

* Affiche le message de fin de jeu, le score final et les instructions pour redémarrer.

* Met à jour l'affichage.

* Appelle `wait_for_key()` pour attendre une pression de touche.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-106.png align="left")

Fonction `victory_screen()` :

* Efface l'écran avec un fond noir.

* Affiche un message de félicitations, le score final et les instructions pour quitter.

* Met à jour l'affichage.

* Appelle `wait_for_key()` pour attendre une pression de touche.

Fonction `wait_for_key()` :

* Attend soit un événement de sortie (fermeture de la fenêtre de jeu), soit un événement de pression de touche.

* Si l'événement est une sortie, elle quitte le jeu en utilisant `pygame.quit()` et `sys.exit()`.

* Si l'événement est une pression de touche, elle sort de la boucle d'attente.

Fonction `show_text_on_screen(text, font_size, y_position)` :

* Affiche du texte sur l'écran avec la taille de police et la position Y spécifiées.

* Utilise la classe `pygame.font.Font` pour créer un objet de police.

* Affiche le texte sur une surface avec la couleur spécifiée (blanc dans ce cas).

* Positionne le texte au centre de l'écran à la position Y spécifiée.

* Dessine le texte sur l'écran de jeu.

Fonction `change_platform_color()` :

* Retourne une couleur RVB aléatoire pour changer la couleur de la plateforme.

Ces fonctions gèrent différents aspects des écrans de jeu, des interactions utilisateur et de l'affichage du texte. Elles contribuent à la structure globale et à l'expérience utilisateur du jeu.

## Boucle principale du jeu

Et maintenant, vous allez coder la boucle principale du jeu avec ses mécaniques appliquées. Examinons d'abord le code, puis l'explication.

Il s'agit du plus long bloc de code de ce tutoriel, alors soyez patient – cela en vaut la peine.

```python
# Boucle principale du jeu
start_screen()
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()

    # Déplacer la plateforme
    platform_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * platform_speed
    platform_pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * platform_speed

    # Assurer que la plateforme reste dans les limites de l'écran
    platform_pos[0] = max(0, min(platform_pos[0], WIDTH - PLATFORM_WIDTH))
    platform_pos[1] = max(0, min(platform_pos[1], HEIGHT - PLATFORM_HEIGHT))

    # Déplacer la balle
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Rebondir sur les murs
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH:
        ball_speed[0] = -ball_speed[0]

    if ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]

    # Vérifier si la balle touche la plateforme
    if (
        platform_pos[0] <= ball_pos[0] <= platform_pos[0] + PLATFORM_WIDTH
        and platform_pos[1] <= ball_pos[1] <= platform_pos[1] + PLATFORM_HEIGHT
    ):
        ball_speed[1] = -ball_speed[1]
        score += 1

    # Vérifier si le joueur passe au niveau suivant
    if score >= current_level * 10:
        current_level += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]  # Vitesse aléatoire de la balle
        platform_color = change_platform_color()

    # Vérifier si la balle tombe hors de l'écran
    if ball_pos[1] >= HEIGHT:
        # Diminuer les vies
        lives -= 1
        if lives == 0:
            game_over_screen()
            start_screen()  # Redémarrer le jeu après la fin de partie
            score = 0
            lives = 3
            current_level = 1
        else:
            # Réinitialiser la position de la balle
            ball_pos = [WIDTH // 2, HEIGHT // 2]
            # Vitesse aléatoire de la balle
            ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]

    # Effacer l'écran
    screen.fill(BLACK)

    # Dessiner la balle
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    # Dessiner la plateforme
    pygame.draw.rect(screen, platform_color, (int(platform_pos[0]), int(platform_pos[1]), PLATFORM_WIDTH, PLATFORM_HEIGHT))

    # Afficher les informations
    info_line_y = 10  # Ajuster la position verticale si nécessaire
    info_spacing = 75  # Ajuster l'espacement si nécessaire

    # Dessiner le score dans un rectangle orange en haut à gauche
    score_text = font.render(f"Score : {score}", True, WHITE)
    score_rect = score_text.get_rect(topleft=(10, info_line_y))
    pygame.draw.rect(screen, ORANGE, score_rect.inflate(10, 5))
    screen.blit(score_text, score_rect)

    # Dessiner l'indicateur de niveau dans un rectangle bleu clair en haut à gauche (à côté du score)
    level_text = font.render(f"Niveau : {current_level}", True, WHITE)
    level_rect = level_text.get_rect(topleft=(score_rect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(screen, LIGHT_BLUE, level_rect.inflate(10, 5))
    screen.blit(level_text, level_rect)

    # Dessiner les vies dans un rectangle rouge en haut à gauche (à côté du niveau)
    lives_text = font.render(f"Vies : {lives}", True, WHITE)
    lives_rect = lives_text.get_rect(topleft=(level_rect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(screen, RED, lives_rect.inflate(10, 5))
    screen.blit(lives_text, lives_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Contrôler le taux de rafraîchissement
    clock.tick(FPS)

# Quitter Pygame
pygame.quit()
```

D'accord, c'était beaucoup – mais voici ce que nous avons fait dans le code ci-dessus :

**Initialisation et écran de démarrage :**

* Appelle `start_screen()` pour afficher l'écran initial avec les instructions.

* Définit `game_running` sur `True` pour initier la boucle principale du jeu.

**Boucle principale du jeu :**

* Continue jusqu'à ce que `game_running` devienne `False` (par exemple, lorsque l'utilisateur ferme la fenêtre de jeu).

**Gestion des événements :**

* Vérifie les événements en utilisant `pygame.event.get()`.

* Si un événement de sortie (fermeture de la fenêtre de jeu) est détecté, définit `game_running` sur `False` pour quitter la boucle.

**Mouvement de la plateforme :**

* Lit l'état des touches fléchées en utilisant `pygame.key.get_pressed()`.

* Ajuste la position de la plateforme en fonction des entrées des touches fléchées.

* Assure que la plateforme reste dans les limites de l'écran.

**Mouvement et rebond de la balle :**

* Met à jour la position de la balle en fonction de sa vitesse.

* Implémente le rebond sur les murs en inversant la vitesse lorsque les bords de l'écran sont atteints.

**Détection des collisions :**

* Vérifie si la balle touche la plateforme en comparant les positions.

* Si une collision se produit, la vitesse verticale de la balle est inversée et le joueur marque un point.

**Progression des niveaux :**

* Vérifie si le joueur a marqué suffisamment de points pour passer au niveau suivant.

* Si c'est le cas, incrémente le niveau, réinitialise la position de la balle, randomise sa vitesse et change la couleur de la plateforme.

**Vérification de la fin de jeu :**

* Surveille si la balle tombe hors de l'écran.

* Diminue le nombre de vies si la balle est en dessous de l'écran.

* Si les vies sont épuisées, affiche l'écran de fin de jeu, redémarre le jeu et réinitialise le score, les vies et le niveau.

**Rendu de l'écran :**

* Efface l'écran avec un fond noir.

* Dessine la balle et la plateforme sur l'écran.

* Affiche les informations de score, de niveau et de vies dans des rectangles avec des couleurs spécifiques.

**Mise à jour de l'affichage et contrôle du taux de rafraîchissement :**

* Met à jour l'affichage pour montrer les changements.

* Contrôle le taux de rafraîchissement avec `clock.tick(FPS)`.

**Terminaison du jeu :**

* Quitte PyGame et termine le programme lorsque la boucle principale est quittée.

Cette structure assure un gameplay continu, la gestion des entrées utilisateur, la mise à jour de l'état du jeu et fournit un retour visuel au joueur.

## Conclusion

Dans ce tutoriel, vous avez navigué à travers les intrications de plusieurs fonctions clés qui forment l'épine dorsale de votre jeu de balle rebondissante.

Récapitulons leurs rôles :

La fonction `start_screen()` efface l'écran avec un fond noir, affiche le titre du jeu et les instructions, met à jour l'affichage pour la visibilité et attend une pression de touche en utilisant `wait_for_key()`.

La fonction `game_over_screen()` efface l'écran avec un fond noir, affiche le message de fin de jeu, le score final et les instructions de redémarrage, met à jour l'affichage et attend une pression de touche avec `wait_for_key()`.

La fonction `victory_screen()` efface l'écran avec un fond noir, affiche un message de félicitations, le score final et les instructions de sortie, met à jour l'affichage et attend une pression de touche avec `wait_for_key()`.

La fonction `wait_for_key()` attend soit un événement de sortie (fermeture de la fenêtre de jeu), soit un événement de pression de touche. Elle quitte le jeu en cas de sortie et sort de la boucle d'attente si une touche est pressée.

La fonction `show_text_on_screen(text, font_size, y_position)` affiche du texte sur l'écran avec les attributs spécifiés, utilise la classe `pygame.font.Font` pour créer un objet de police et positionne et dessine le texte au centre de l'écran.

Et la fonction `change_platform_color()` retourne une couleur RVB aléatoire pour changer la couleur de la plateforme.

En suivant ces fonctions, vous avez plongé dans la boucle principale du jeu, le cœur de notre jeu. Elle orchestrer les mécaniques du jeu, y compris la gestion des événements, le mouvement de la plateforme et de la balle, la détection des collisions, la progression des niveaux et la terminaison du jeu.

Vous avez vu comment cette boucle assure un gameplay continu, des interactions utilisateur réactives et des visuels dynamiques.

Maintenant que vous êtes équipé de la compréhension de ces fonctions et de la boucle principale, vous avez les connaissances pour expérimenter, ajuster et développer votre jeu. Vous vous sentez prêt à vous lancer dans votre voyage de développement de jeux, à explorer de nouvelles fonctionnalités et à créer des expériences de jeu uniques. Bon codage !

Si vous souhaitez télécharger le code ou jouer au jeu, vous pouvez le trouver ici :

%[https://github.com/jpromanonet/bouncing_ball_game]