---
title: Tutoriel PyGame – Comment créer un jeu d'enlèvement d'extraterrestres
subtitle: ''
author: Juan P. Romano
co_authors: []
series: null
date: '2024-01-02T23:55:29.000Z'
originalURL: https://freecodecamp.org/news/pygame-tutorial-alien-abduction-game
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/alien_abduction_game.png
tags:
- name: Game Development
  slug: game-development
- name: pygame
  slug: pygame
- name: Python
  slug: python
seo_title: Tutoriel PyGame – Comment créer un jeu d'enlèvement d'extraterrestres
seo_desc: Ever since I was a kid, I've been hooked on video games. My first experience
  with coding involved kind of a wild project – a Tron races simulator in Quick Basic
  on an ancient IBM computer (I was like 6 years old, so I didn't really understand
  what I ...
---

Depuis que je suis enfant, je suis accro aux jeux vidéo. Ma première expérience avec la programmation impliquait un projet un peu fou – un simulateur de courses Tron en Quick Basic sur un ancien ordinateur IBM (j'avais environ 6 ans, donc je ne comprenais pas vraiment ce que je faisais).

En avançant rapidement à travers les années de programmation, me voici, toujours en train d'écrire des logiciels et de me lancer dans le monde du développement de jeux.

Avec pour objectif de devenir un développeur de jeux indépendant, j'ai décidé d'explorer PyGame, étant donné ma "maîtrise" de Python en l'enseignant et tout.

Après quelques remue-méninges, j'ai abouti à un concept original : un jeu où vous incarnez un extraterrestre se baladant dans un OVNI. Votre mission ? Atteindre un quota spécifique d'enlèvements chaque semaine pour éviter les sanctions de la Fédération Intergalactique.

Je ne vais pas mentir, je me suis fortement inspiré de l'ancien "Luna lander" que j'avais sur le même ancien ordinateur IBM.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-65.png align="left")

*Capture d'écran en noir et blanc de Luna Lander*

### Pourquoi je pense que créer des jeux est plus cool que votre projet de codage moyen

Imaginez que vous êtes en train de coder, et soudain, cela vous frappe – les jeux ! Oui, nous parlons de la matière qui transforme un écran en un univers interactif où vous n'êtes pas juste un codeur – vous êtes un sorcier créant des sorts (ou des lignes de code) qui font bouger, tirer et exploser des choses sans répercussions légales.

Voici pourquoi se lancer dans le développement de jeux, c'est comme trouver le niveau secret du développement logiciel :

1. **C'est du codage avec un but** : Oubliez les programmes ennuyeux – vous créez un univers où les extraterrestres enlèvent des vaches parce que... pourquoi pas ?

2. **Plus de codage en loup solitaire** : Les jeux ont besoin de plus que du code. Ils ont aussi besoin d'histoires, de personnages et de graphismes cool. Soudain, vous n'êtes plus juste un codeur – vous êtes une armée à vous tout seul conquérant le design, le storytelling et peut-être un peu d'ingénierie sonore.

3. **C'est comme des LEGO pour les codeurs** : Vous construisez des trucs, vous les cassez, et puis vous les reconstruisez ! Le développement de jeux, c'est tout sur l'essai et l'erreur, ce qui en fait les LEGO des projets de codage. Qui a dit que le débogage ne pouvait pas être amusant ?

4. **Fête de la créativité** : Vous avez déjà voulu créer un monde où la gravité fonctionne de côté, et où les vaches portent des combinaisons spatiales ? Dans le développement de jeux, votre créativité s'emballe.

5. **Résoudre des mystères, édition codage** : Les jeux viennent avec des énigmes. Pas juste pour les joueurs, mais pour vous, le maître d'œuvre derrière les scènes. Pensez-y comme créer votre propre roman policier de codage où chaque bug est un rebondissement de l'intrigue attendant d'être résolu.

6. **Apprendre en jouant** : Vous vous souvenez de ces manuels scolaires ennuyeux ? Eh bien, oubliez-les. Avec le développement de jeux, vous ne lisez pas – vous jouez.

7. **Montrez vos compétences** : Construire des jeux, ce n'est pas juste pour le fun. C'est pour montrer vos muscles de codeur. Votre jeu est votre trophée, votre badge d'honneur. Imaginez arriver à un entretien d'embauche avec un jeu que vous avez construit. Qui est cool maintenant ?

Alors, pourquoi se contenter de coder quand on peut créer un univers ? Le développement de jeux, c'est là où le codage devient une aventure épique, et vous, mon ami, êtes le héros. **Prêt à passer au niveau supérieur ?**

D'accord, créons ce jeu ensemble, étape par étape, et faisons-en un truc génial ! Vous vous demandez à quoi il ressemblera une fois terminé ? Jetez un œil à cet aperçu élégant :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-66.png align="left")

*Aperçu de ce à quoi le jeu ressemblera, montrant un vaisseau spatial extraterrestre descendant pour ramasser des vaches.*

## Table des matières :

1. [Comment configurer l'environnement](#heading-installation)

2. [Comment concevoir le concept du jeu](#heading-conception-du-concept-du-jeu)

3. [Comment coder le jeu](#heading-comment-coder-le-jeu)

4. [Conclusion](#heading-conclusion)

## Comment configurer l'environnement

### Installer PyGame

Commençons ce voyage en configurant le terrain de jeu. Tout d'abord, vous devrez installer PyGame. Voici un guide simple pour vous aider à démarrer.

### 1. Créer un nouveau répertoire

Ouvrez votre terminal préféré et naviguez jusqu'à l'emplacement où vous souhaitez conserver votre jeu. Créez un nouveau répertoire pour votre projet. Appelons-le "*AlienAbductionGame.*"

```bash
mkdir AlienAbductionGame
```

### 2. Naviguer vers le répertoire du projet

Déplacez-vous dans votre répertoire nouvellement créé.

```bash
cd AlienAbductionGame
```

### 3. Installer PyGame

```bash
pip install pygame
```

Super ! Maintenant, vous êtes équipé de PyGame et prêt à vous lancer dans le codage.

### Qu'est-ce que vous avez besoin d'autre pour commencer ?

Vous avez déjà Python avec PyGame installé sur votre ordinateur. Donc, la dernière chose dont vous avez besoin est votre éditeur de code préféré. J'utiliserai et recommanderai Visual Studio Code, mais vous pouvez utiliser n'importe quel autre éditeur que vous aimez ou avec lequel vous vous sentez à l'aise.

Une fois que vous avez tout installé et que votre éditeur est prêt, commençons par comprendre le concept du jeu et ses mécaniques.

## Comment concevoir le concept du jeu

### Idée de jeu : Aventure d'enlèvement d'extraterrestres

Imaginez ceci : Vous êtes un pilote extraterrestre qui se balade dans le cosmos à bord de votre fidèle OVNI. Malheureusement, vous êtes en retard sur votre quota hebdomadaire d'enlèvements, et la Fédération Intergalactique n'est pas très contente. Pour éviter une pénalité cosmique, vous devez enlever diverses cibles sur Terre.

### Mécaniques

#### Quota d'enlèvements et niveaux :

Au début de chaque niveau, vous recevez un quota spécifique d'enlèvements. Cela représente le nombre de vaches que vous devez enlever pour progresser.

Le jeu se compose de dix niveaux, chacun avec un quota croissant. Compléter un niveau débloque le suivant et réinitialise le compteur de quota.

#### Commandes de l'OVNI :

Utilisez les touches fléchées ou vos commandes préférées pour naviguer l'OVNI à travers l'écran de jeu.

Des mouvements précis sont cruciaux pour des enlèvements réussis. Maîtriser les commandes assure une acquisition efficace des cibles.

#### Cibles – vaches adorables :

Les cibles sont des vaches charmantes et pixelisées se promenant à la surface de la Terre. Vous approcherez une vache, activerez votre faisceau tracteur (barre d'espace), et regarderez la vache disparaître de votre écran.

#### Mécaniques du faisceau tracteur :

Vous appuierez sur la barre d'espace pour activer le faisceau tracteur, qui s'étend de votre OVNI au sol.

Lorsque le faisceau touche une vache, il déclenche le processus d'enlèvement, et la vache disparaît, augmentant votre score et votre quota d'enlèvements.

#### Minuterie et urgence :

Chaque niveau est accompagné d'une minuterie de compte à rebours, ajoutant un sentiment d'urgence à vos enlèvements.

Atteindre avec succès le quota d'enlèvements avant que la minuterie n'atteigne zéro assure la progression au niveau suivant.

### Comment décider des éléments du jeu (vaisseau spatial, cibles, etc.)

En ce qui concerne la sélection des éléments de votre jeu, la simplicité est la clé. Plus c'est simple, mieux c'est. Alors, jetons un coup d'œil à ce dont vous aurez besoin pour faire fonctionner les mécaniques du jeu.

1. **Vaisseau spatial (OVNI) :**

* Au lieu de designs complexes, concentrez-vous sur un sprite d'OVNI distinctif, un mignon

* Donnez la priorité aux mouvements fluides et à la réactivité aux commandes du joueur.

2. **Cibles (vaches) :**

* Optez pour un sprite de vache mignon qui correspond à l'humour du jeu.

* Envisagez de changer la couleur de la vache lorsqu'elle est enlevée – vous coderez une bulle rouge signifiant l'enlèvement.

3. **Arrière-plan et environnement :**

* Maintenez un arrière-plan propre et simple, en ajustant le schéma de couleurs pour correspondre à la progression du jeu.

* Modifiez progressivement la couleur des étoiles à chaque niveau pour signifier l'avancement.

4. **Faisceau tracteur :**

* Assurez-vous que le faisceau tracteur est visuellement distinguable. Vous pouvez expérimenter avec une couleur jaune simple mais efficace.

5. **Indicateurs de niveau :**

* Implémentez un indicateur de niveau simple affichant le niveau actuel. Cela peut être une petite section dans le coin de l'écran.

6. **Écrans de fin de jeu et de victoire :**

* Concevez des écrans simples indiquant le succès ou l'échec. Un simple "Game Over" et "You Win" avec un texte d'accompagnement suffira, comme le suivant

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-64.png align="left")

*Écran de victoire*

## Comment coder le jeu

### Présentation des sections clés du code

Maintenant que vous avez une idée claire et une compréhension de nos mécaniques de jeu et de ses éléments, il est temps de se plonger dans le code. Nous allons parcourir les sections clés du code.

Tout d'abord, commençons par importer les éléments nécessaires pour coder notre jeu :

```python
import pygame
import random
import sys
```

Dans cette section, vous importez trois modules : `pygame`, `random`, et `sys`.

* **pygame** : C'est la bibliothèque principale que vous utilisez pour créer le jeu. Elle fournit des fonctions et des outils pour gérer les graphiques, les entrées utilisateur, et plus encore.

* **random** : vous utiliserez ce module pour générer des nombres aléatoires. Cela s'avère utile lorsque vous voulez que des choses se produisent de manière imprévisible, comme la position initiale des cibles.

* **sys** : Ce module fournit l'accès à certaines variables utilisées ou maintenues par l'interpréteur Python et à des fonctions qui interagissent fortement avec l'interpréteur. Vous l'utiliserez pour gérer les événements système, tels que quitter le jeu lorsque le joueur ferme la fenêtre.

Donc, vous vous équipez essentiellement des outils nécessaires pour rendre le jeu visuellement attrayant, dynamique et réactif aux entrées du joueur.

### Comment coder l'écran de démarrage

```python
def start_screen(screen):
    # Constantes
    WIDTH, HEIGHT = 800, 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FONT_SIZE = 30

    # Police pour afficher le texte
    font = pygame.font.Font(None, FONT_SIZE)

    # Remplir l'écran avec la couleur de fond
    screen.fill(BLACK)

    # Texte d'introduction
    intro_text = [
        "Bienvenue, Enleveur d'Extraterrestres !",
        "Vous êtes en retard sur votre quota hebdomadaire d'enlèvements.",
        "Aidez l'extraterrestre à rattraper son retard en enlevant des cibles sur Terre !",
        "",
        "----------------------------------------------------------------------------------------------",
        "Déplacez l'OVNI avec les FLÈCHES et", 
        "appuyez sur ESPACE pour enlever les vaches avec le faisceau tracteur.",
        "----------------------------------------------------------------------------------------------",
        "",
        "Appuyez sur n'importe quelle touche pour commencer le jeu...",
        "",
    ]

    # Rendre et afficher le texte d'introduction
    y_position = HEIGHT // 4
    for line in intro_text:
        text = font.render(line, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, y_position))
        screen.blit(text, text_rect)
        y_position += FONT_SIZE

    pygame.display.flip()

    # Attendre une pression de touche pour commencer le jeu
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
```

**Explication du code :**

* La fonction `start_screen` prend un paramètre `screen`, qui est la fenêtre Pygame où vous afficherez notre introduction. Elle définit quelques constantes pour les dimensions de l'écran, les couleurs et la taille de la police.

* L'écran est rempli avec un fond noir.

* Un texte d'introduction est défini dans `intro_text`, fournissant un message de bienvenue, des instructions et une invite pour commencer le jeu.

* En utilisant la fonctionnalité de police de Pygame, le texte est rendu et affiché sur l'écran.

* La fonction attend ensuite une pression de touche pour commencer le jeu en appelant la fonction `wait_for_key`.

* La fonction `wait_for_key` boucle jusqu'à ce qu'une touche soit pressée ou que l'utilisateur ferme la fenêtre. Si une touche est pressée, la boucle se termine et l'écran d'introduction disparaît.

À ce stade, vous devriez avoir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-68.png align="left")

*Écran de démarrage*

### Comment construire la fonction de texte à l'écran

Maintenant, examinons le bloc de code suivant :

```python
def show_text_on_screen(screen, text, font_size, y_position):
    font = pygame.font.Font(None, font_size)
    text_render = font.render(text, True, (255, 255, 255))
    text_rect = text_render.get_rect(center=(WIDTH // 2, y_position))
    screen.blit(text_render, text_rect)
```

Ce code définit une fonction `show_text_on_screen` qui affiche un message texte sur la fenêtre Pygame. Décomposons-le :

* La fonction prend quatre paramètres :

1. `screen` : La fenêtre Pygame où le texte sera affiché

2. `text` : Le message ou la chaîne de texte à afficher.

3. `font_size` : La taille de la police pour le texte.

4. `y_position` : La position verticale sur l'écran où le texte sera centré.

* Il crée un objet de police Pygame avec la taille spécifiée.

* En utilisant l'objet de police, il rend le texte avec la couleur blanche (`(255, 255, 255)` représente les valeurs RVB pour le blanc).

* La méthode `get_rect` est utilisée pour obtenir la zone rectangulaire qui englobe le texte rendu. Le centre de ce rectangle est défini pour être au centre horizontal et à la position verticale spécifiée.

* Enfin, le texte rendu est blité (dessiné) sur l'écran à la position spécifiée.

* Cette fonction fournit un moyen pratique d'afficher des messages texte sur l'écran avec une taille de police et une position verticale spécifiées.

### Comment coder l'écran "Game Over"

Maintenant, vous allez coder un écran de fin de jeu, alors continuez et vérifiez le bloc de code suivant :

```python
def game_over_screen(screen):
    screen.fill((0, 0, 0))  # Remplit l'écran de noir
    show_text_on_screen(screen, "Game Over", 50, HEIGHT // 3)
    show_text_on_screen(screen, f"Votre score final : {score}", 30, HEIGHT // 2)
    show_text_on_screen(screen, "Appuyez sur n'importe quelle touche pour quitter...", 20, HEIGHT * 2 // 3)
    pygame.display.flip()
    wait_for_key()
```

Décortiquons l'écran de fin de jeu :

* `screen.fill((0, 0, 0))` : Remplit toute la fenêtre Pygame avec un fond noir.

* `show_text_on_screen(screen, "Game Over", 50, HEIGHT // 3)` : Affiche le texte "Game Over" avec une taille de police de 50, centré verticalement à un tiers de la hauteur de l'écran.

* `show_text_on_screen(screen, f"Votre score final : {score}", 30, HEIGHT // 2)` : Affiche le score final du joueur avec une taille de police de 30, centré verticalement à la moitié de la hauteur de l'écran.

* `show_text_on_screen(screen, "Appuyez sur n'importe quelle touche pour quitter...", 20, HEIGHT * 2 // 3)` : Affiche l'instruction d'appuyer sur n'importe quelle touche pour quitter avec une taille de police de 20, centré verticalement aux deux tiers de la hauteur de l'écran.

* `pygame.display.flip()` : Met à jour l'affichage pour montrer les changements.

* `wait_for_key()` : Attend une pression de touche avant de continuer, faisant effectivement en sorte que l'écran reste jusqu'à ce que le joueur interagisse.

Cette fonction est utilisée pour montrer un écran de fin de jeu avec des informations pertinentes telles que le score final et une instruction de sortie, quelque chose qui à ce stade devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-67.png align="left")

*Écran de fin de jeu*

### Vous avez gagné ! Comment coder l'écran de victoire :)

Et enfin, mais non des moindres, vous avez l'écran de victoire, alors jetons un coup d'œil au code de l'écran :

```python
def victory_screen(screen):
    screen.fill((0, 0, 0))  # Remplit l'écran de noir
    show_text_on_screen(screen, "Félicitations !", 50, HEIGHT // 3)
    show_text_on_screen(screen, f"Vous avez complété tous les niveaux avec un score de {score}", 30, HEIGHT // 2)
    show_text_on_screen(screen, "Appuyez sur n'importe quelle touche pour quitter...", 20, HEIGHT * 2 // 3)
    pygame.display.flip()
    wait_for_key()
```

Explication du code :

* `screen.fill((0, 0, 0))` : Remplit toute la fenêtre Pygame avec un fond noir.

* `show_text_on_screen(screen, "Félicitations !", 50, HEIGHT // 3)` : Affiche le texte "Félicitations !" avec une taille de police de 50, centré verticalement à un tiers de la hauteur de l'écran.

* `show_text_on_screen(screen, f"Vous avez complété tous les niveaux avec un score de {score}", 30, HEIGHT // 2)` : Affiche un message de félicitations avec le score final du joueur et une taille de police de 30, centré verticalement à la moitié de la hauteur de l'écran.

* `show_text_on_screen(screen, "Appuyez sur n'importe quelle touche pour quitter...", 20, HEIGHT * 2 // 3)` : Affiche l'instruction d'appuyer sur n'importe quelle touche pour quitter avec une taille de police de 20, centré verticalement aux deux tiers de la hauteur de l'écran.

* `pygame.display.flip()` : Met à jour l'affichage pour montrer les changements.

* `wait_for_key()` : Attend une pression de touche avant de continuer, faisant effectivement en sorte que l'écran reste jusqu'à ce que le joueur interagisse.

Cette fonction est utilisée pour montrer un écran de victoire avec un message de félicitations et le score final du joueur.

Maintenant, vous avez le début du jeu, les écrans que vous utiliserez pour communiquer avec le joueur.

### Construisons quelques sprites

Ensuite, vous coderez les paramètres de base tels que la taille de la fenêtre, les sprites (l'OVNI et la vache), les couleurs, les étoiles, et ainsi de suite.

Jetez un coup d'œil au bloc de code suivant :

```python
# Charger les images du vaisseau spatial et de la vache
ovni = pygame.image.load("ovni.png")
cow = pygame.image.load("cow.png")

# Redimensionner les images si nécessaire
ovni = pygame.transform.scale(ovni, (50, 50))
cow = pygame.transform.scale(cow, (40, 40))

# Initialiser Pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)  # Couleur bleu clair pour l'indicateur de niveau
SHIP_GREEN = (0, 255, 0)  # Couleur verte pour le vaisseau
GRASS_GREEN = (0, 100, 0)  # Couleur verte plus foncée pour l'herbe
STAR_COUNT = int(WIDTH * HEIGHT * 0.001)
```

Explication du code :

* `ovni = pygame.image.load("ovni.png")` et `cow = pygame.image.load("cow.png")` : Chargent les images du vaisseau spatial (ovni) et de la vache à partir de fichiers.

* `ovni = pygame.transform.scale(ovni, (50, 50))` et `cow = pygame.transform.scale(cow, (40, 40))` : Redimensionnent les images si nécessaire. Dans ce cas, le vaisseau spatial est redimensionné à une largeur et une hauteur de 50 pixels, et la vache est redimensionnée à une largeur et une hauteur de 40 pixels.

* `pygame.init()` : Initialise Pygame.

Constantes :

* `WIDTH, HEIGHT = 800, 600` : Définit la largeur et la hauteur de la fenêtre de jeu.

* `FPS = 60` : Définit les images par seconde pour le jeu.

* Couleurs : `BLACK, WHITE, RED, YELLOW, GRAY, ORANGE` : Définissent des constantes de couleur en utilisant des valeurs RVB. `LIGHT_BLUE, SHIP_GREEN, GRASS_GREEN` : Constantes de couleur supplémentaires pour des éléments spécifiques.

* `STAR_COUNT` : Calcule le nombre d'étoiles en fonction de la taille de la fenêtre.

Cette section gère la configuration des images pour le vaisseau spatial et la vache, en ajustant leurs tailles si nécessaire. Elle établit également des constantes pour divers aspects du jeu.

Les étapes suivantes impliquent la création de la fenêtre de jeu et la mise en place des commandes du joueur, de la détection des collisions et d'autres éléments essentiels du gameplay.

### Comment coder la fenêtre de jeu et configurer les FPS

```python
# Créer la fenêtre de jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu d'enlèvement d'extraterrestres")

# Horloge pour contrôler le taux de rafraîchissement
clock = pygame.time.Clock()

# Joueur (vaisseau spatial extraterrestre)
player_rect = pygame.Rect(WIDTH // 2 - 25, 10, 50, 50)
player_speed = 5

# Liste pour stocker les cibles (animaux)
targets = []

# Définir le score initial
score = 0

# Police pour afficher le score, le niveau et le minuteur
font = pygame.font.Font(None, 36)

# Drapeau pour suivre si la barre d'espace est pressée
space_pressed = False

# Liste pour stocker les étoiles
stars = [{'x': random.randint(0, WIDTH), 'y': random.randint(0, HEIGHT), 'size': random.randint(1, 3),
          'color': LIGHT_BLUE} for _ in range(STAR_COUNT)]

# Zone herbeuse en bas
grass_rect = pygame.Rect(0, HEIGHT - 40, WIDTH, 40)

# Variables de niveau et de compte à rebours
current_level = 1
abduction_target = 10  # Cible initiale
countdown_timer = 60  # Minuteur de compte à rebours initial en secondes
current_score = 0  # Nouveau compteur pour suivre le score du niveau actuel

# Compteur pour contrôler le rythme des apparitions des cibles
target_spawn_counter = 0
TARGET_SPAWN_RATE = max(30, 120 - (current_level * 90))  # Ajuste le rythme en fonction du niveau actuel

# Liste des couleurs pour chaque niveau
level_colors = [
    LIGHT_BLUE,
    ORANGE,
    RED,
    YELLOW,
    GRAY,
    (0, 255, 0),  # Vert
    (255, 0, 255),  # Violet
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (128, 0, 128),  # Indigo
]
```

Explication du code :

**Création de la fenêtre de jeu :**

* `screen = pygame.display.set_mode((WIDTH, HEIGHT))` : Cette ligne crée la fenêtre de jeu avec la largeur et la hauteur spécifiées.

* `pygame.display.set_caption("Jeu d'enlèvement d'extraterrestres")` : Définit le titre ou la légende de la fenêtre de jeu.

**Horloge pour le taux de rafraîchissement :**

* `clock = pygame.time.Clock()` : Initialise un objet horloge pour contrôler le taux de rafraîchissement du jeu.

**Joueur (Vaisseau spatial extraterrestre) :**

* `player_rect = pygame.Rect(WIDTH // 2 - 25, 10, 50, 50)` : Définit une zone rectangulaire pour le joueur (vaisseau spatial extraterrestre) en haut au centre de la fenêtre.

* `player_speed = 5` : Définit la vitesse à laquelle le joueur peut se déplacer.

**Cibles (Animaux) :**

* `targets = []` : Initialise une liste vide pour stocker les cibles (animaux).

**Score :**

* `score = 0` : Initialise le score à zéro.

**Police pour afficher le texte :**

* `font = pygame.font.Font(None, 36)` : Crée un objet de police pour afficher le score, le niveau et le minuteur.

**Drapeau de la barre d'espace pressée :**

* `space_pressed = False` : Initialise un drapeau pour suivre si la barre d'espace est pressée.

**Étoiles :**

* `stars = [...]` : Crée une liste d'étoiles avec des positions, tailles et couleurs aléatoires. Cela est utilisé pour créer un fond étoilé.

**Zone herbeuse en bas :**

* `grass_rect = pygame.Rect(0, HEIGHT - 40, WIDTH, 40)` : Définit une zone rectangulaire en bas pour un fond herbeux.

**Variables de niveau et de compte à rebours :**

* `current_level = 1` : Initialise le jeu au niveau 1.

* `abduction_target = 10` : Définit la cible initiale d'enlèvements.

* `countdown_timer = 60` : Définit le minuteur de compte à rebours initial en secondes.

* `current_score = 0` : Initialise un compteur pour suivre le score du niveau actuel.

**Compteur d'apparition des cibles :**

* `target_spawn_counter = 0` : Initialise un compteur pour contrôler le rythme des apparitions des cibles.

**Taux d'apparition des cibles :**

* `TARGET_SPAWN_RATE = max(30, 120 - (current_level * 90))` : Ajuste le taux d'apparition des cibles en fonction du niveau actuel.

**Couleurs pour chaque niveau :**

* `level_colors = [...]` : Définit une liste de couleurs pour chaque niveau, qui seront utilisées dans le jeu.

Ces variables et paramètres établissent l'état initial du jeu, définissant le joueur, les cibles, le système de score et les éléments visuels. Votre jeu évoluera et répondra aux actions du joueur en fonction de ces conditions initiales.

### Comment coder les mécanismes du jeu

Jetez un coup d'œil à ces fonctions que vous utiliserez pour exécuter le jeu. Essayez de les coder vous-même avant de copier et coller le code. Cela vous aidera à comprendre le processus de réflexion entre les mécaniques et le code réel.

```python
# Fonction pour afficher l'écran de démarrage
start_screen(screen)

# Boucle principale du jeu
running = True
game_started = False  # Drapeau pour suivre si le jeu a commencé

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_started:
                game_started = True  # Définit le drapeau à True pour éviter d'appeler start_screen à plusieurs reprises
                continue  # Saute le reste de la boucle jusqu'à ce que le jeu ait commencé
            elif event.key == pygame.K_SPACE:
                space_pressed = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            space_pressed = False

    keys = pygame.key.get_pressed()

    # Déplacer le joueur
    player_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
    player_rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed

    # Assurer que le joueur reste dans les limites de l'écran
    player_rect.x = max(0, min(player_rect.x, WIDTH - player_rect.width))
    player_rect.y = max(0, min(player_rect.y, HEIGHT - player_rect.height))

    # Faire apparaître une nouvelle cible en fonction du compteur
    target_spawn_counter += 1
    if target_spawn_counter >= TARGET_SPAWN_RATE:
        target_rect = pygame.Rect(random.randint(0, WIDTH - 20), HEIGHT - 50, 50, 50)
        targets.append(target_rect)
        target_spawn_counter = 0

    # Mettre à jour l'animation de lueurs des étoiles et la couleur pour le niveau actuel
    for star in stars:
        star['size'] += 0.05
        if star['size'] > 3:
            star['size'] = 1
        star['color'] = level_colors[current_level - 1]
```

Explication du code :

**Afficher l'écran de démarrage :**

* `start_screen(screen)` : Appelle la fonction `start_screen` pour afficher l'écran de démarrage initial.

**Boucle principale du jeu :**

* `running = True` : Initialise un drapeau pour contrôler la boucle principale du jeu.

* `game_started = False` : Initialise un drapeau pour suivre si le jeu a commencé.

**Gestion des événements :**

* La boucle itère à travers les événements pygame pour vérifier les entrées de l'utilisateur et les événements de la fenêtre.

* `pygame.QUIT` : Si l'utilisateur ferme la fenêtre de jeu, le drapeau `running` est défini sur `False`, quittant le jeu.

* `pygame.KEYDOWN` : Si une touche est pressée :

* Si le jeu a commencé (`game_started` est `True`), la boucle est sautée, empêchant les appels répétés à l'écran de démarrage.

* Si la barre d'espace (`pygame.K_SPACE`) est pressée et que le jeu n'a pas commencé, `space_pressed` est défini sur `True`.

* `pygame.KEYUP` : Si une touche est relâchée :

* Si la touche relâchée est la barre d'espace, `space_pressed` est défini sur `False`.

**Mouvement du joueur :**

* La position du joueur (`player_rect`) est mise à jour en fonction de l'entrée des touches fléchées.

* La coordonnée x du joueur est ajustée par la différence entre les touches fléchées droite et gauche multipliée par la vitesse du joueur.

* La coordonnée y du joueur est ajustée par la différence entre les touches fléchées bas et haut multipliée par la vitesse du joueur.

* La position du joueur est contrainte pour rester dans les limites de l'écran.

**Apparition des cibles :**

* Un compteur (`target_spawn_counter`) est incrémenté à chaque itération.

* Si le compteur dépasse le taux d'apparition des cibles (`TARGET_SPAWN_RATE`), une nouvelle cible est créée à une coordonnée x aléatoire dans la largeur de l'écran et une coordonnée y fixe au-dessus du bord inférieur de l'écran.

* La cible est représentée par un rectangle (`target_rect`) ajouté à la liste `targets`.

* Le compteur est réinitialisé.

**Mise à jour de l'animation des étoiles :**

* L'animation des étoiles est mise à jour en augmentant leur taille. Si la taille dépasse 3, elle est réinitialisée à 1.

* La couleur de chaque étoile est définie en fonction du niveau actuel.

Cette partie du code gère les entrées de l'utilisateur, le mouvement du joueur, l'apparition des cibles et met à jour l'animation des étoiles. C'est un composant crucial de la boucle de jeu, assurant l'interaction du joueur et la progression dans le jeu.

### Comment rendre les éléments du jeu (joueur, actifs, etc.)

La partie suivante du code gère le rendu des éléments du jeu à l'écran, y compris les étoiles, la zone herbeuse, le vaisseau spatial du joueur et les cibles. Il gère également le dessin du faisceau tracteur et les collisions entre le faisceau tracteur et les cibles.

```python
# Effacer l'écran
    screen.fill(BLACK)

    # Dessiner les étoiles avec une couleur basée sur le niveau
    for star in stars:
        pygame.draw.circle(screen, star['color'], (star['x'], star['y']), int(star['size']))

    # Dessiner la zone herbeuse
    pygame.draw.rect(screen, GRASS_GREEN, grass_rect)

    # Dessiner le joueur et les cibles
    screen.blit(ovni, player_rect)
    
    for target in targets:
        screen.blit(cow, target)

    # Dessiner le faisceau tracteur lorsque la barre d'espace est pressée
    if space_pressed:
        tractor_beam_rect = pygame.Rect(player_rect.centerx - 2, player_rect.centery, 4, HEIGHT - player_rect.centery)
        pygame.draw.line(screen, YELLOW, (player_rect.centerx, player_rect.centery),
                         (player_rect.centerx, HEIGHT), 2)

        # Vérifier les collisions avec les cibles
        for target in targets[:]:
            if tractor_beam_rect.colliderect(target):
                # Changer la couleur du faisceau tracteur en jaune
                pygame.draw.line(screen, YELLOW, (player_rect.centerx, player_rect.centery),
                                 (player_rect.centerx, target.bottom), 2)
                # Changer la couleur de la cible en rouge
                pygame.draw.rect(screen, RED, target)
                targets.remove(target)
                current_score += 1
                score += 1
```

Explication du code :

**Effacer l'écran :**

* `screen.fill(BLACK)` : Remplit tout l'écran avec une couleur noire, effaçant effectivement l'image précédente.

**Dessiner les étoiles :**

* Itère à travers la liste des étoiles (`stars`) et dessine chaque étoile comme un cercle sur l'écran.

* La couleur du cercle est déterminée par l'attribut de couleur de l'étoile, et sa position et sa taille sont basées sur les coordonnées x et y de l'étoile et sa taille.

**Dessiner la zone herbeuse :**

* `pygame.draw.rect(screen, GRASS_GREEN, grass_rect)` : Dessine un rectangle représentant la zone herbeuse en bas de l'écran. La couleur est définie sur `GRASS_GREEN`.

**Dessiner le joueur et les cibles :**

* `screen.blit(ovni, player_rect)` : Dessine le vaisseau spatial du joueur (`ovni`) sur l'écran à la position spécifiée par `player_rect`.

* `for target in targets: screen.blit(cow, target)` : Dessine chaque cible (vache) de la liste `targets` sur l'écran à leurs positions respectives.

**Dessiner le faisceau tracteur (lorsque la barre d'espace est pressée) :**

* Vérifie si la barre d'espace est pressée (`space_pressed` est `True`).

* Si vrai, `tractor_beam_rect` : Crée un rectangle représentant le faisceau tracteur basé sur la position du joueur.

* `pygame.draw.line` : Dessine une ligne jaune représentant le faisceau tracteur du centre du joueur au bas de l'écran.

* Vérifie les collisions entre le faisceau tracteur et les cibles.

* Si une collision est détectée, la cible est supprimée, la couleur du faisceau tracteur change en jaune, et la couleur de la cible change en rouge.

* Le score est mis à jour.

### Logique du jeu

Maintenant, vous avez presque terminé – mais d'abord, vous devez ajouter une logique au jeu comme le compte à rebours qui vous donne une minute par niveau. Vous devez également dessiner une barre de navigation, une simple avec quatre éléments contenant le score général, l'indicateur de niveau, le minuteur et les enlèvements.

Voici comment nous allons faire tout cela :

```python
info_line_y = 10  # Ajustez la position verticale si nécessaire
    info_spacing = 75  # Ajustez l'espacement si nécessaire

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

    # Dessiner le minuteur de compte à rebours dans un rectangle rouge en haut à gauche (à côté du niveau)
    timer_text = font.render(f"Temps : {int(countdown_timer)}", True, WHITE)
    timer_rect = timer_text.get_rect(topleft=(level_rect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(screen, RED, timer_rect.inflate(10, 5))
    screen.blit(timer_text, timer_rect)

    # Dessiner les cibles à acquérir pour le niveau actuel dans un rectangle gris en haut à gauche (à côté du minuteur)
    targets_text = font.render(f"Enlèvements : {current_score}/{abduction_target}", True, WHITE)
    targets_rect = targets_text.get_rect(topleft=(timer_rect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(screen, GRAY, targets_rect.inflate(10, 5))
    screen.blit(targets_text, targets_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter le taux de rafraîchissement
    clock.tick(FPS)
```

Explication du code :

**Positionnement de la ligne d'information :**

* `info_line_y = 10` : Spécifie la position verticale pour la ligne d'information en haut de l'écran.

* `info_spacing = 75` : Définit l'espacement entre les différentes informations sur la ligne.

**Dessiner le score :**

* `score_text` : Rend le texte du score en utilisant la police du jeu.

* `score_rect` : Récupère le rectangle qui englobe le texte du score rendu.

* `pygame.draw.rect` : Dessine un rectangle orange autour du texte du score, créant un fond.

* `screen.blit(score_text, score_rect)` : Affiche (rend) le texte du score sur l'écran.

**Dessiner l'indicateur de niveau :**

* `level_text` : Rend le texte de l'indicateur de niveau.

* `level_rect` : Récupère le rectangle pour le texte de l'indicateur de niveau.

* `pygame.draw.rect` : Dessine un rectangle bleu clair autour du texte de l'indicateur de niveau.

* `screen.blit(level_text, level_rect)` : Affiche le texte de l'indicateur de niveau sur l'écran.

**Dessiner le minuteur de compte à rebours :**

* `timer_text` : Rend le texte du minuteur de compte à rebours.

* `timer_rect` : Récupère le rectangle pour le texte du minuteur de compte à rebours.

* `pygame.draw.rect` : Dessine un rectangle rouge autour du texte du minuteur de compte à rebours.

* `screen.blit(timer_text, timer_rect)` : Affiche le texte du minuteur de compte à rebours sur l'écran.

**Dessiner les cibles d'enlèvement :**

* `targets_text` : Rend le texte indiquant le nombre d'enlèvements requis pour le niveau actuel.

* `targets_rect` : Récupère le rectangle pour le texte des cibles d'enlèvement.

* `pygame.draw.rect` : Dessine un rectangle gris autour du texte des cibles d'enlèvement.

* `screen.blit(targets_text, targets_rect)` : Affiche le texte des cibles d'enlèvement sur l'écran.

**Mettre à jour l'affichage :**

* `pygame.display.flip()` : Met à jour l'affichage pour refléter les changements apportés dans cette itération.

**Limite du taux de rafraîchissement :**

* `clock.tick(FPS)` : Limite le taux de rafraîchissement au nombre d'images par seconde spécifié (`FPS`). Cela garantit que le jeu fonctionne à une vitesse constante sur différents systèmes.

Et maintenant, nous sommes prêts pour le dernier bloc de code. Il contient la logique du compte à rebours liée à la logique de progression des niveaux et à la réinitialisation des enlèvements. Cela signifie que vous devez réinitialiser les enlèvements effectués par le joueur à zéro chaque fois que vous passez un niveau, par exemple :

* Niveau 1 : 0/10 enlèvements

* Niveau 2 : 0/20 enlèvements

Et ainsi de suite – le quota maximum d'enlèvements est de 100 enlèvements au niveau 10, en ajoutant 10 enlèvements au quota requis pour chaque niveau.

### Logique du minuteur et fonction de sortie

Vérifiez le dernier bloc de code :

```python
 # Logique du compte à rebours
    countdown_timer -= 1 / FPS  # Diminue le minuteur en fonction du taux de rafraîchissement
    if countdown_timer <= 0:
        # Vérifie si le joueur a atteint l'objectif d'enlèvements pour le niveau actuel
        if current_score < abduction_target:
            # Le joueur n'a pas atteint l'objectif d'enlèvements, termine le jeu
            game_over_screen(screen)
            running = False
        else:
            # Passe au niveau suivant
            current_level += 1
            if current_level <= 10:
                current_score = 0
                abduction_target = 10 * current_level
                countdown_timer = 60  # Réinitialise le minuteur de compte à rebours pour le niveau suivant
                # Réinitialise le texte des cibles pour le niveau suivant
                targets_text = font.render(f"Enlèvements : {current_score}/{abduction_target}", True, WHITE)
                targets_rect = targets_text.get_rect(topleft=(timer_rect.topright[0] + info_spacing, info_line_y))

    # Vérifie si le joueur a atteint l'objectif d'enlèvements pour le niveau actuel
    if current_score >= abduction_target:
        # Passe au niveau suivant
        current_level += 1
        if current_level <= 10:
            current_score = 0
            abduction_target = 10 * current_level
            countdown_timer = 60  # Réinitialise le minuteur de compte à rebours pour le niveau suivant
            # Réinitialise le texte des cibles pour le niveau suivant
            targets_text = font.render(f"Enlèvements : {current_score}/{abduction_target}", True, WHITE)
            targets_rect = targets_text.get_rect(topleft=(timer_rect.topright[0] + info_spacing, info_line_y))
        else:
            victory_screen(screen)
            running = False

# Quitter Pygame
pygame.quit()
```

**Logique du compte à rebours :**

* `countdown_timer -= 1 / FPS` : Diminue le compte à rebours de la fraction `1 / FPS`. Cet ajustement garantit que le minuteur diminue uniformément en fonction du taux de rafraîchissement.

**Vérification de l'expiration du minuteur :**

* `if countdown_timer <= 0:` : Vérifie si le compte à rebours a atteint ou est tombé en dessous de zéro.

**Le joueur n'a pas atteint l'objectif d'enlèvements :**

* `if current_score < abduction_target:` : Vérifie si le score actuel du joueur est inférieur à l'objectif d'enlèvements pour le niveau actuel.

* `game_over_screen(screen)` : Appelle la fonction pour afficher l'écran de fin de jeu.

* `running = False` : Définit le drapeau `running` sur `False`, mettant fin à la boucle de jeu.

**Passer au niveau suivant :**

* `else:` : Exécute lorsque le joueur a atteint l'objectif d'enlèvements pour le niveau actuel.

* `current_level += 1` : Incrémente le niveau actuel.

* `if current_level <= 10:` : Vérifie s'il reste des niveaux à parcourir.

* `current_score = 0` : Réinitialise le score actuel pour le niveau suivant.

* `abduction_target = 10 * current_level` : Définit l'objectif d'enlèvements pour le niveau suivant.

* `countdown_timer = 60` : Réinitialise le compte à rebours pour le niveau suivant.

* Réinitialise le texte des cibles pour le niveau suivant.

* `targets_text = font.render(f"Enlèvements : {current_score}/{abduction_target}", True, WHITE)`

* `targets_rect = targets_text.get_rect(topleft=(timer_rect.topright[0] + info_spacing, info_line_y))`

**Le joueur a atteint l'objectif d'enlèvements pour tous les niveaux :**

* `else:` : Exécute lorsque le joueur a réussi à compléter tous les niveaux (atteint le niveau 10).

* `victory_screen(screen)` : Appelle la fonction pour afficher l'écran de victoire.

* `running = False` : Définit le drapeau `running` sur `False`, mettant fin à la boucle de jeu.

**Quitter Pygame :**

* `pygame.quit()` : Nettoie et quitte Pygame après la fin de la boucle de jeu.

Maintenant, vous avez terminé et vous pouvez exécuter le jeu en tapant ceci dans votre terminal :

```bash
python aliend_aductions_game.py
```

Si tout est correct, vous devriez voir l'écran de démarrage qui vous permettra de jouer après avoir appuyé sur n'importe quelle touche.

## Conclusion

Nous avons couvert beaucoup de choses dans ce tutoriel. Vous avez commencé par configurer l'environnement de développement, installer PyGame et concevoir le concept du jeu avec des mécaniques simples.

Ensuite, vous avez suivi le processus étape par étape de codage du jeu, de l'initialisation de l'environnement à la mise en œuvre des commandes du joueur, des collisions et des éléments dynamiques. Vous avez appris comment intégrer des images pour le vaisseau spatial et les vaches, créant une expérience visuelle engageante.

Le jeu comprend divers niveaux, chacun avec son propre défi et un minuteur de compte à rebours, ajoutant un élément d'urgence. Vous avez mis en place un système de score, une progression de niveau et des graphismes engageants pour améliorer l'expérience du joueur.

### Encouragement pour un apprentissage supplémentaire :

Félicitations pour être arrivé à ce stade ! Le développement de jeux est un chemin d'apprentissage dynamique et gratifiant, et il y a toujours plus à apprendre. Alors que vous continuez, envisagez de vous plonger dans des sujets plus avancés tels que :

1. **Graphismes avancés** : améliorez votre jeu avec des graphismes plus détaillés, des animations et des effets visuels.

2. **Son et musique** : intégrez des effets sonores et de la musique de fond pour élever l'expérience de jeu.

3. **Physique du jeu** : explorez des mouvements et des interactions réalistes dans le monde du jeu.

4. **Fonctionnalité multijoueur** : apprenez à implémenter des fonctionnalités multijoueurs pour une expérience plus interactive.

5. **Techniques d'optimisation** : plongez dans l'optimisation de votre code et de vos graphismes pour de meilleures performances.

Si vous arrivez à ce stade, merci d'avoir lu et j'espère que vous apprécierez cet article autant que j'ai apprécié le faire, vous pouvez également consulter le code original de ce jeu et télécharger les actifs depuis ici :

%[https://github.com/jpromanonet/alien_abduction_game]