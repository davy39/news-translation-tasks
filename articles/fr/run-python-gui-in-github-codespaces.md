---
title: Comment exécuter des applications GUI Python dans GitHub Codespaces avec Xvfb
  et noVNC
subtitle: ''
author: Ayodele Aransiola
co_authors: []
series: null
date: '2025-09-12T22:41:26.158Z'
originalURL: https://freecodecamp.org/news/run-python-gui-in-github-codespaces
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757716674058/86bb9af9-0977-4548-a050-36c3b9ea3e16.png
tags:
- name: Python
  slug: python
- name: codespaces
  slug: codespaces
seo_title: Comment exécuter des applications GUI Python dans GitHub Codespaces avec
  Xvfb et noVNC
seo_desc: 'GitHub Codespaces gives you a full development environment in the cloud,
  directly in your browser. It’s great for writing and running code, but there’s one
  big limitation: it doesn’t support graphical applications out of the box, especially
  for Pytho...'
---

GitHub Codespaces vous offre un environnement de développement complet dans le cloud, directement dans votre navigateur. C’est un excellent outil pour écrire et exécuter du code, mais il présente une limitation majeure : il ne prend pas en charge les applications graphiques nativement, en particulier pour le code Python.

Si vous essayez d'exécuter une bibliothèque GUI Python comme Pygame, Tkinter ou PyQt dans Codespaces, vous obtiendrez une erreur. C’est parce que Codespaces fonctionne dans un environnement « headless » (sans tête). Il n’y a pas d’affichage physique sur lequel votre application peut ouvrir une fenêtre.

Dans cet article, je vais vous montrer comment corriger cela. Vous apprendrez à configurer un bureau virtuel à l'aide de Xvfb et à le diffuser dans votre navigateur via noVNC. À la fin, vous serez en mesure d'exécuter n'importe quelle application GUI Python dans GitHub Codespaces.

## Table des matières

* [Pourquoi Codespaces nécessite une configuration supplémentaire pour les GUI](#pourquoi-codespaces-nécessite-une-configuration-supplémentaire-pour-les-gui)
    
* [Étape 1 : Créer le dépôt et ouvrir le Codespace](#étape-1-créer-le-dépôt-et-ouvrir-le-codespace)
    
* [Étape 2 : Ajouter le script de configuration](#étape-2-ajouter-le-script-de-configuration)
    
* [Étape 3 : Démarrer l'environnement GUI](#étape-3-démarrer-l-environnement-gui)
    
* [Étape 4 : Ouvrir le bureau noVNC](#étape-4-ouvrir-le-bureau-novnc)
    
* [Étape 5 : Exécuter votre application GUI Python](#étape-5-exécuter-votre-application-gui-python)
    
* [Astuces](#astuces)
    
* [Conclusion](#conclusion)
    

## Prérequis

Avant de commencer, vous devriez avoir :

* Un compte GitHub et l'accès à GitHub Codespaces.
    
* Une connaissance de base de Python.
    
* Une application GUI Python à tester (nous utiliserons un petit exemple Pygame).
    

## Pourquoi Codespaces nécessite une configuration supplémentaire pour les GUI

Lorsque vous exécutez un code GUI tel que :

```python
import pygame
pygame.display.set_mode((800, 600))
```

Sur votre machine locale, Python demande à votre système d'exploitation de créer une fenêtre. Mais Codespaces s'exécute sur un serveur sans moniteur attaché. Sans affichage, votre application GUI ne peut pas effectuer de rendu.

C'est là qu'intervient [**Xvfb**](https://www.x.org/archive/X11R7.7/doc/man/man1/Xvfb.1.xhtml) (X virtual framebuffer). Il simule un affichage en mémoire, de sorte que les programmes GUI pensent s'exécuter sur un véritable écran. Pour rendre cet écran visible dans le navigateur, vous pouvez utiliser [**noVNC**](https://novnc.com/info.html), qui diffuse l'affichage virtuel via un client web.

Ensemble, Xvfb et noVNC transforment Codespaces en un bureau basé sur le cloud pour les applications GUI.

## Étape 1 : Créer le dépôt et ouvrir le Codespace

Tout d'abord, créez un dépôt GitHub pour votre projet (ou un dépôt de démonstration) et ouvrez-le dans Codespaces :

![Capture d'écran d'un nouveau dépôt](https://cdn.hashnode.com/res/hashnode/image/upload/v1757336978616/4a41c394-0d85-48de-b7d6-14a0a3dae56d.jpeg align="center")

## Étape 2 : Ajouter le script de configuration

Créez un fichier nommé `start-gui.sh` à la racine de votre projet.

![une capture d'écran de GitHub Codespace avec un fichier bash créé](https://cdn.hashnode.com/res/hashnode/image/upload/v1757337705472/b1b75b17-57b9-437c-a79e-18f6b1f55cae.png align="center")

Collez le code suivant dans le fichier `start-gui.sh` :

```bash
#!/usr/bin/env bash
set -e

echo "Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y xvfb x11vnc fluxbox websockify novnc

echo "Starting virtual display..."
Xvfb :1 -screen 0 1024x768x24 &
export DISPLAY=:1
fluxbox &

echo "Starting VNC server..."
x11vnc -display :1 -nopw -forever -shared -rfbport 5900 &

echo "Starting noVNC on port 6080..."
websockify --web=/usr/share/novnc 6080 localhost:5900 &

echo ""
echo "GUI environment is ready!"
echo "Go to the Ports tab, set port 6080 to Public, and open the link."
```

Expliquons ce script pour que vous puissiez comprendre ce qu'il fait :

### `set -e`

* Cela indique au shell de s'arrêter immédiatement si une commande échoue.
    
* Sans cela, le script continuerait de s'exécuter même si quelque chose ne va pas (comme un échec d'installation).
    

### Installation des dépendances

`sudo apt-get update -y` : met à jour votre liste de paquets.

`sudo apt-get install -y` ⁣installe les paquets listés (xvfb, x11vnc, fluxbox, websockify et novnc)

* **xvfb** : crée un affichage « factice » (écran virtuel en mémoire).
        
* **x11vnc** : partage cet affichage factice via le protocole VNC.
        
* **Fluxbox** : un gestionnaire de fenêtres léger, pour que le bureau dispose d'un environnement GUI.
        
* **websockify** : convertit le trafic VNC en WebSockets pour qu'il puisse s'exécuter dans un navigateur.
        
* **novnc** : fournit un client de navigation pour se connecter au bureau.
        

### Affichage virtuel

* `Xvfb :1 -screen 0 1024x768x24 &` : démarre le framebuffer virtuel sur l'affichage `:1` avec une résolution de `1024x768` et des couleurs 24 bits.
    
* `export DISPLAY=:1` : indique aux applications (comme les GUI Python) de dessiner sur cet écran virtuel au lieu de chercher une unité d'affichage réelle.
    
* `fluxbox &` : lance le gestionnaire de fenêtres pour que les applications GUI aient un bureau où s'afficher.
    

### Serveur VNC

* `x11vnc -display :1` : vous connecte à l'affichage factice (`:1`).
    
* `-nopw` : garantit qu'aucun mot de passe n'est requis.
    
* `-forever` : maintient le VNC en cours d'exécution même si les clients se déconnectent.
    
* `-shared` : autorise plusieurs clients.
    
* `-rfbport 5900` : expose le serveur interne sur le port standard de VNC.
    

### Serveur noVNC

* `websockify` agit comme un pont qui convertit le trafic WebSocket vers le protocole VNC (sur le port 5900).
    
* `--web=/usr/share/novnc` : sert les fichiers du client web noVNC.
    
* `6080` : le port sur lequel vous vous connecterez dans votre navigateur (celui-ci est accessible publiquement).
    
* [`localhost:5900`](http://localhost:5900) : redirige le trafic vers le serveur VNC démarré précédemment.
    

Vous ne devriez exposer que le **port 6080** (noVNC) en tant que **Public** et garder le **5900** (VNC brut) privé car :

* Le **Port 5900 (VNC)** utilise le protocole VNC brut, qui n'est **pas chiffré** et ne nécessite pas de mot de passe dans cette configuration. S'il est exposé, n'importe qui pourrait se connecter directement et contrôler votre bureau Codespace.
    
* Le **Port 6080 (noVNC)** fonctionne via **WebSockets + HTTPS**, donc le trafic est chiffré et sécurisé via la connexion de GitHub Codespaces. De plus, il ne sert que le client web noVNC, pas le protocole VNC brut.
    

> **5900 = dangereux à exposer**, **6080 = moyen sécurisé par navigateur pour visualiser la GUI**.

L'étape suivante consiste à rendre le fichier bash exécutable en exécutant le code ci-dessous dans le terminal :

```bash
chmod +x start-gui.sh
```

## Étape 3 : Démarrer l'environnement GUI

Exécutez le script :

```bash
./start-gui.sh
```

![le terminal pendant l'exécution du script bash](https://cdn.hashnode.com/res/hashnode/image/upload/v1757339165120/f99b3381-d038-4eb6-944d-3fabad058c95.png align="center")

Ceci va :

1. Installer toutes les dépendances (Xvfb, fluxbox, x11vnc, novnc).
    
2. Démarrer un affichage virtuel (`DISPLAY=:1`).
    
3. Lancer un gestionnaire de fenêtres léger (fluxbox).
    
4. Diffuser le bureau vers votre navigateur via noVNC sur le port `6080`.
    

## Étape 4 : Ouvrir le bureau noVNC

1. Dans Codespaces, ouvrez l'onglet Ports.
    
2. Trouvez le port 6080 et changez sa visibilité en public (clic droit sur le mot « private »).
    
3. Ouvrez l'URL dans un nouvel onglet du navigateur.
    
4. Cliquez sur `vnc.html` ou `vnc_auto.html` si vous y êtes invité.
    
    ![capture d'écran de l'onglet port sur Codespace](https://cdn.hashnode.com/res/hashnode/image/upload/v1757339315843/e3fcfd7b-d946-4c46-b4a9-09b905574a80.png align="center")
    

![ouvrez l'adresse redirigée du port 6080 dans un nouvel onglet, et vous obtiendrez cet écran](https://cdn.hashnode.com/res/hashnode/image/upload/v1757339400603/d8e0e412-7669-4c41-b1e4-5f13d8125de1.png align="center")

Vous devriez maintenant voir un bureau Linux léger s'exécuter dans votre navigateur.

![un bureau linux léger s'exécutant sur votre navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1757339486345/f5831d0e-d66e-4549-902a-13e3c8bd8bf0.png align="center")

## Étape 5 : Exécuter votre application GUI Python

Dans un nouveau terminal Codespaces, exécutez :

```javascript
export DISPLAY=:1
python3 your_script.py
```

Votre application GUI Python devrait apparaître dans le bureau noVNC 🎉.

Par exemple, voici un script Pygame simple `test.py` :

```python
import pygame
from pygame import display, font, event
from pygame.locals import *

# Setup display
pygame.init()
screen = display.set_mode()
display.set_caption("Capstone 2")
myFont = font.SysFont('arial', 12)  # Choose a font to use in game

# Directions displayed throughout game
directions = "Please press the 'Y' key for yes and the 'N' key for no."

# Counts how many questions have been asked
currentQuestion = 0


# Determines which question to ask
def story(answer, count):
    screen.fill("white")
    if count == 0:
        question1(answer)
    elif count == 1:
        question2(answer)
    elif count == 2:
        question3(answer)
    elif count == 3:
        end(answer)


# Displays the first part of the story
def intro():
    # Break up the string into multiple variables because there isn't text wrapping in Pygame
    intro1 = "Once upon a time lived a brave hero named Anya."
    intro2 = "She lived a simple life in a small village, making biscuits for the village people."
    intro3 = "One day, late at night, she hears a loud noise outside the village."
    q1 = "Should she go outside to investigate? Yes or no?"

    screen.fill("white")
    textSurface = myFont.render(intro1, True, "black")
    screen.blit(textSurface, (10, 10))
    textSurface = myFont.render(intro2, True, "black")
    screen.blit(textSurface, (10, 24))
    textSurface = myFont.render(intro3, True, "black")
    screen.blit(textSurface, (10, 38))
    textSurface = myFont.render(q1, True, "black")
    screen.blit(textSurface, (10, 52))
    textSurface = myFont.render(directions, True, "black")
    screen.blit(textSurface, (10, 66))


# First question
def question1(answer):
    if answer == K_y:
        yes1 = "She ventures into the dark, prepared for danger."
        yes2 = "Eventually, she sees an army of ogres coming toward her village!"
        q2 = "Should she fight the ogres? Yes or no?"

        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(yes2, True, "black")
        screen.blit(textSurface, (10, 24))
        textSurface = myFont.render(q2, True, "black")
        screen.blit(textSurface, (10, 38))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 52))

    elif answer == K_n:
        no1 = "She chooses the safety of her home and stays inside."
        no2 = "However, the sounds do not go away."
        no3 = "She can tell something is very wrong..."
        no4 = "Eventually, she sees an army of ogres coming toward her village!"
        q2 = "Should she fight the ogres? Yes or no?"

        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(no2, True, "black")
        screen.blit(textSurface, (10, 24))
        textSurface = myFont.render(no3, True, "black")
        screen.blit(textSurface, (10, 38))
        textSurface = myFont.render(no4, True, "black")
        screen.blit(textSurface, (10, 52))
        textSurface = myFont.render(q2, True, "black")
        screen.blit(textSurface, (10, 66))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 80))


# Second question
def question2(answer):
    if answer == K_y:
        yes1 = "She bravely confronts the ogres, hoping to protect her village from harm."
        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))

    elif answer == K_n:
        no1 = "The ogres raid the village but Anya manages to escape with her life."
        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))

    story2 = "The ogres decide to leave but she knows they will be back."
    story3 = "Anya decides to talk with a village elder about what she should do."
    story4 = "The elder says there is a powerful sword hidden in the Ancient Forest."
    q3 = "Should Anya risk her life to retrieve it? Yes or no?"

    textSurface = myFont.render(story2, True, "black")
    screen.blit(textSurface, (10, 24))
    textSurface = myFont.render(story3, True, "black")
    screen.blit(textSurface, (10, 38))
    textSurface = myFont.render(story4, True, "black")
    screen.blit(textSurface, (10, 52))
    textSurface = myFont.render(q3, True, "black")
    screen.blit(textSurface, (10, 66))
    textSurface = myFont.render(directions, True, "black")
    screen.blit(textSurface, (10, 80))


# Third question
def question3(answer):
    if answer == K_y:
        yes1 = "Although Anya almost died in the Ancient Forest,"
        yes2 = "she returns with the Sword of Legends!"
        yes3 = "In the dead of winter, the ogres come back."
        yes4 = "This time they are being led by their evil king."
        q4 = "Should Anya fight the ogre king now that she has the Sword of Legends?"

        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(yes2, True, "black")
        screen.blit(textSurface, (10, 24))
        textSurface = myFont.render(yes3, True, "black")
        screen.blit(textSurface, (10, 38))
        textSurface = myFont.render(yes4, True, "black")
        screen.blit(textSurface, (10, 52))
        textSurface = myFont.render(q4, True, "black")
        screen.blit(textSurface, (10, 66))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 80))

    elif answer == K_n:
        no1 = "Anya decides it's too risky to go into the forest alone."
        no2 = "She hopes for the best with the weapons she has."
        no3 = "In the dead of winter, the ogres come back."
        no4 = "This time they are being led by their evil king."
        q4 = "Should Anya fight the king even though she doesn't have the Sword of Legends?"

        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(no2, True, "black")
        screen.blit(textSurface, (10, 24))
        textSurface = myFont.render(no3, True, "black")
        screen.blit(textSurface, (10, 38))
        textSurface = myFont.render(no4, True, "black")
        screen.blit(textSurface, (10, 52))
        textSurface = myFont.render(q4, True, "black")
        screen.blit(textSurface, (10, 66))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 80))


# Ending
def end(answer):
    if answer == K_y:
        yes1 = "Tension fills the air as she prepares to fight the king. The duel commences..."
        end1 = "After an intense battle, Anya strikes the final blow!"
        end2 = "The king surrenders and pleads for mercy."
        end3 = "Anya is a true hero, who shows mercy to the king."
        end4 = "This act of kindness warms the evil king's heart,"
        end5 = "who promises to leave the village alone for eternity."
        end6 = "The end!"

        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(end1, True, "black")
        screen.blit(textSurface, (10, 24))
        textSurface = myFont.render(end2, True, "black")
        screen.blit(textSurface, (10, 38))
        textSurface = myFont.render(end3, True, "black")
        screen.blit(textSurface, (10, 52))
        textSurface = myFont.render(end4, True, "black")
        screen.blit(textSurface, (10, 66))
        textSurface = myFont.render(end5, True, "black")
        screen.blit(textSurface, (10, 80))
        textSurface = myFont.render(end6, True, "black")
        screen.blit(textSurface, (10, 94))

    elif answer == K_n:
        no1 = "Anya refuses to duel the king, who laughs at her cowardice."
        end1 = "This buys some time for the villagers to escape."
        end2 = "Sadly, the ogre king takes over Anya's village."
        end3 = "She is just thankful that the villagers were able to get to safety."
        end4 = "The end!"

        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(end1, True, "black")
        screen.blit(textSurface, (10, 24))
        textSurface = myFont.render(end2, True, "black")
        screen.blit(textSurface, (10, 38))
        textSurface = myFont.render(end3, True, "black")
        screen.blit(textSurface, (10, 52))
        textSurface = myFont.render(end4, True, "black")
        screen.blit(textSurface, (10, 66))


# Game loop
while True:
    # Checks to see if at beginning of game
    if currentQuestion == 0:
        intro()

    # Get the most recent event
    currentEvent = event.poll()

    # Displays the correct question based on event that occurs
    if currentEvent.type == KEYDOWN:
        story(currentEvent.key, currentQuestion)
        currentQuestion = currentQuestion + 1

    # add text to screen
    display.update()
```

> source du code : codecombat (développement de jeu Python)

Le code ci-dessus est un jeu d'histoire interactif simple écrit avec Pygame. Dans les premières lignes, vous importez **Pygame** ainsi que ses modules display, font et event.

`pygame.locals` apporte des constantes comme `K_y` (touche Y), `K_n` (touche N) et `KEYDOWN`.

La ligne suivante initialise Pygame et crée une fenêtre (`screen`). Elle définit également le titre de la fenêtre puis charge une police pour le rendu du texte.

Ensuite, vous avez la section des fonctions qui gèrent l'histoire (`intro`, `question1`, `question2`, `question3` et les conditions basées sur la réponse du joueur).

En résumé, le code est un jeu textuel dont vous êtes le héros avec un seul personnage, Anya. Les choix du joueur déterminent quel texte est affiché.

Pour exécuter ce script, installez `pygame`.

```bash
sudo apt-get update
sudo apt-get install -y python3-pygame
pip install pygame
```

Le code ci-dessus installera `pygame` dans votre environnement, après quoi vous pourrez exécuter le script.

```bash
python3 test.py
```

Lorsque vous exécutez cela dans Codespaces, la fenêtre apparaîtra dans l'onglet noVNC. Si elle ne s'ouvre pas automatiquement, cliquez sur `connect`.

![capture d'écran de la sortie de l'application gui python](https://cdn.hashnode.com/res/hashnode/image/upload/v1757340287440/77bafc3f-f3eb-402a-8ce1-9cfe6a739b3c.png align="center")

## Astuces

![Erreur ALSA dans codespaces](https://cdn.hashnode.com/res/hashnode/image/upload/v1757340460701/c3c8376a-4b6f-4a05-8ed3-83c036476150.png align="center")

* **Ignorez les erreurs ALSA** : Codespaces n'a pas de sortie sonore, les avertissements audio sont donc normaux.
    
* **Ajustez la résolution** : Modifiez `1024x768x24` dans le script si vous voulez un écran plus grand (ou plus petit).
    
* **Utilisation avec d'autres bibliothèques** : Tkinter, PyQt et les graphiques interactifs Matplotlib fonctionneront tous avec cette configuration.
    
* **Automatisez l'export DISPLAY** : Ajoutez `export DISPLAY=:1` dans votre fichier bash si vous ne voulez pas le taper à chaque fois.
    

## Conclusion

Vous venez de transformer GitHub Codespaces en un environnement GUI Python. En utilisant Xvfb et noVNC, vous pouvez exécuter des applications qui nécessitent normalement un environnement de bureau directement dans votre navigateur.

Que vous construisiez des jeux, testiez des interfaces ou enseigniez les graphismes Python, vous pouvez désormais tout faire dans Codespaces sans quitter le cloud.

> Vous voulez essayer vous-même ? Clonez ce [dépôt](https://github.com/CodeLeom/Python-codespaces), exécutez `./start-gui.sh`, et lancez votre première application GUI dans Codespaces dès aujourd'hui.