---
title: Comment créer un jeu de Visual Novel en 10 minutes - Tutoriel Python Ren'Py
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-06-22T16:18:29.000Z'
originalURL: https://freecodecamp.org/news/use-python-to-create-a-visual-novel
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-21-at-14.23.10-1.png
tags:
- name: Game Development
  slug: game-development
- name: Python
  slug: python
seo_title: Comment créer un jeu de Visual Novel en 10 minutes - Tutoriel Python Ren'Py
seo_desc: 'Do you have a story idea that you''d like to turn into a novel? How about
  adding visual appeal and interactivity to that novel?

  A Visual Novel might be the game genre you are looking for. And this tutorial is
  here to help set you up in 10 minutes, wit...'
---

Avez-vous une idée d'histoire que vous aimeriez transformer en roman ? Et si vous ajoutiez un attrait visuel et de l'interactivité à ce roman ?

Un [Visual Novel](https://en.wikipedia.org/wiki/Visual_novel) pourrait être le genre de jeu que vous recherchez. Et ce tutoriel est là pour vous aider à vous lancer en 10 minutes, avec une expérience de codage minimale requise. Commençons !

## Introduction et installation de l'outil

Nous allons utiliser [le moteur Ren'Py Visual Novel](https://www.renpy.org/), qui est construit sur Python 2.7. Comme Python lui-même est un langage de script, vous pourrez "scénariser" votre projet de visual novel dans Ren'Py.

> Depuis l'arrivée de Python 3, Python 2.7 a été abandonné et n'est plus activement maintenu. Soyez rassuré - Python 2.7 possède toutes les fonctionnalités dont nous avons besoin pour créer un visual novel génial. De plus, la dernière version de Ren'Py, [Ren'Py SDK 7.4](https://www.renpy.org/release/7.4.0), offre un mode de compatibilité pour Python 3. Les développeurs expriment également l'espoir de s'intégrer pleinement avec Python 3 dans la prochaine version, Ren'Py 8.0.

### Comment télécharger et installer Ren'Py

Vous pouvez télécharger la dernière version de Ren'Py pour votre système d'exploitation (Windows, Mac, Linux) sur [son site officiel](https://www.renpy.org/).

Une fois que vous avez téléchargé et installé Ren'Py, vous pouvez ouvrir le lanceur Ren'Py, sélectionner l'un des projets de démarrage (Tutorial, The Question) à gauche, et cliquer sur **Lancer le projet**.

Consultez le **Tutoriel** pour avoir un aperçu de toute la puissance de ce moteur, ou **The Question** pour voir un visual novel très basique que vous pouvez créer en 10 minutes.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-21-at-10.51.50.png align="left")

*Le lanceur Ren'Py*

## Comment créer un nouveau projet dans Ren'Py

Créons un nouveau projet. J'ai appelé le mien **Randonnée en forêt🌲**, mettant en scène une scène simple où deux enfants explorent un sentier forestier.

Faites attention à la résolution que vous choisissez : Par défaut, elle est de 1280 x 720. Lorsque nous ajoutons des images, nos images de fond doivent également respecter ces dimensions.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/foresthike.gif align="left")

### Comment exécuter le projet de base

Lancez le projet de base. Appuyez sur **Démarrer** depuis le menu principal. Après deux brèves lignes de dialogue, le script se termine et nous sommes ramenés au menu principal.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/launch.gif align="left")

*Exécution du projet de base*

## Comment scénariser notre projet

Commençons à scénariser notre jeu basé sur le modèle.

Des éditeurs de texte comme [Sublime Text](https://www.sublimetext.com/) et [Atom](https://atom.io/) ont tous deux une coloration syntaxique pour les scripts Ren'Py se terminant par `.rpy`. Consultez [ce package Sublime Text](https://packagecontrol.io/packages/Renpy%20Language) et [ce package Atom](https://atom.io/packages/language-renpy).

Les deux lignes de dialogue que nous avons vues se trouvent dans `script.rpy`. Ouvrez ce fichier et son contenu devrait ressembler à ce qui suit. Tout comme en Python, les lignes qui commencent par `#` sont des commentaires et ne seront pas évaluées comme faisant partie du script Ren'Py. Les commentaires et le code ci-dessous sont assez explicites.

```pgsql
# Déclarer les personnages utilisés par ce jeu
define e = Character("Eileen")


# Le jeu commence ici
label start:

    # Afficher un fond
    scene bg room

    # Cela montre un sprite de personnage
    show eileen happy

    # Ces lignes affichent des dialogues.
    e "Vous avez créé un nouveau jeu Ren'Py."
    e "Une fois que vous ajoutez une histoire, des images et de la musique, vous pouvez le publier dans le monde !"

    # Cela termine le jeu.
    return
```

Le `label` est utilisé pour le contrôle de flux, que nous aborderons dans la section suivante.

L'instruction `return` sur la dernière ligne est ce qui nous a ramenés au menu principal.

### Comment déclarer des personnages et ajouter des dialogues

Remplaçons la déclaration de personnage et les dialogues de base par ceux de notre histoire. Voici comment se déroule mon histoire :

```pgsql
define laura = Character('Laura')
define tom = Character('Tom')

label start:

    laura "Attends-moi, Tom !"
    laura "Tom !"
    laura "J'ai dit attends-moi !"
    laura "...Tom ?"
    tom "Bouh !"
    laura "Aïe... pas encore."
    tom "As-tu peur ?"
    laura "Pas du tout."
    laura "Partir comme ça est dangereux, tu sais."
    laura "Nous sommes dans la forêt. Nous pourrions nous perdre."
    tom "D'accord, d'accord, maman. Je ne le referai plus."

    return
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/story.gif align="left")

### Comment ajouter des images et des transitions

Si vous n'êtes pas artiste vous-même, vous pouvez envisager de chercher des ressources dans le domaine créatif commun. [itch.io](https://itch.io/), un marché pour les jeux indépendants, est un excellent endroit pour chercher des ressources.

J'ai trouvé [cet ensemble de sprites de personnages](https://fuelli.itch.io/free-to-use-character-sprites) pour mon projet. Pour les images de fond, j'ai simplement appliqué des filtres artistiques à des images créatives communes, donnant aux images de la vie réelle une esthétique aquarelle agréable.

J'ai mis toutes mes images dans `game/images`. Notez qu'il est acceptable d'utiliser des espaces dans les noms de fichiers d'images.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-21-at-13.23.45.png align="left")

*Une manière conventionnelle d'organiser les ressources d'images*

Ensuite, nous ajoutons à `script.rpy` ces images ainsi que quelques transitions. Ren'Py applique des transitions lorsqu'il voit des mots-clés comme `with` et `at`. Vous pouvez en lire plus sur les transitions dans [la documentation ATL (Animation and Transition Language) de Ren'Py](https://www.renpy.org/doc/html/atl.html).

```pgsql
label start:
    scene bg forest day with fade
    show laura angry
    laura "Attends-moi, Tom !"
    laura "Tom !"
    laura "J'ai dit attends-moi !"
    laura "...Tom ?"
    hide laura
    scene bg forest day with vpunch
    show tom happy at right with moveinbottom
    tom "Bouh !"
    show laura angry at left with moveinleft
    laura "Aïe... pas encore."
    tom "As-tu peur ?"
    laura "Pas du tout."
    show laura sad
    laura "Partir comme ça est dangereux, tu sais."
    laura "Nous sommes dans la forêt. Nous pourrions nous perdre."
    tom "D'accord, d'accord, maman. Je ne le referai plus."

    return
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/images.gif align="left")

Avec l'ajout de visuels, notre histoire prend forme agréablement.

### Comment ajouter des choix

Un jeu avec différentes branches et fins double le plaisir. Ajouter un menu de choix à un script Ren'Py est simple :

```pgsql
menu:
    "Quel chemin devons-nous prendre ?"

    "Gauche" :
        tom "Explorons le sentier de gauche !"
    "Droite" :
        tom "La droite est toujours la bonne direction !"
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/choice.gif align="left")

### Comment utiliser les variables Python et le contrôle de flux

Nous pouvons définir des variables Python dans un script Ren'Py et modifier le flux de notre histoire en fonction de leurs valeurs. Les instructions Python commencent par un `$` ou un bloc `python:` indenté.

Ajout de variables à notre menu de choix précédent :

```pgsql
menu:
    "Quel chemin devons-nous prendre ?"

    "Gauche" :
        tom "Explorons le sentier de gauche !"
        $ is_lost = True
    "Droite" :
        tom "La droite est toujours la bonne direction !"
        $ is_lost = False
scene bg forest noon with Dissolve(3.0)
scene bg forest dusk with Dissolve(3.0)
show laura sad at left with moveinleft
laura "Il se fait tard. Es-tu sûr que nous ne sommes pas perdus ?"
if is_lost:
    show tom sad at right with moveinleft
    tom "J'espère que non, mais j'ai un mauvais pressentiment."
else:
    show tom happy at right with moveinleft
    tom "Nous allons bien. Regarde ! Il y a la fin du sentier."
    tom "Je suis le meilleur éclaireur des environs."
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/ezgif.com-gif-maker-2-.gif align="left")

Voir la fin de cet article pour mes ressources artisanales pour travailler avec Python dans Ren'Py.

### Comment jouer de la musique

Selon [la documentation audio de Ren'Py](https://www.renpy.org/doc/html/audio.html), jouer de la musique et des effets sonores est aussi simple que ce qui suit :

```pgsql
play music "mozart.ogg"
play sound "woof.mp3"
```

### Comment sauvegarder et charger le jeu

Ren'Py a fait tout le travail difficile pour nous et dispose d'un système de sauvegarde et de chargement intégré.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/save.gif align="left")

*Sauvegarder le jeu*

![Image](https://www.freecodecamp.org/news/content/images/2021/06/load.gif align="left")

*Charger le jeu*

### Autres personnalisations que vous pouvez faire

Actuellement, dans notre dialogue, toute la ligne de texte est affichée en une fois, au lieu de caractère par caractère. Nous pouvons changer la variable `preference.text_cps` (CPS signifie caractères par seconde) dans `options.rpy` comme ceci.

```pgsql
default preferences.text_cps = 20
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/cps.gif align="left")

*Définir un CPS personnalisé affiche le texte caractère par caractère à un rythme donné*

Il y a encore plus que nous pouvons personnaliser dans `gui.rpy` (GUI signifie Interface Graphique Utilisateur, qui inclut la boîte de texte et les éléments de menu de choix que nous avons vus) ou `screens.rpy`.

## Que peut faire d'autre Ren'Py ?

Les capacités de Ren'Py vont bien au-delà de l'affichage de texte et d'images. Je pourrais aller jusqu'à dire que Ren'Py est aussi capable et polyvalent que Python lui-même.

Avec le module [Pygame](https://www.pygame.org/news), il est possible de créer des mini-jeux complexes dans Ren'Py. J'ai moi-même créé et ouvert plusieurs mini-jeux, dont un moteur d'échecs qui s'intègre avec l'IA d'échecs Stockfish ainsi qu'un moteur de jeu de rythme qui génère automatiquement la carte de rythme pour tout fichier musical.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/promotion.gif align="left")

*Ma démonstration de jeu d'échecs*

![Image](https://www.freecodecamp.org/news/content/images/2021/06/demo-4.gif align="left")

*Ma démonstration de jeu de rythme*

%[https://r3dhummingbird.itch.io/renpy-chess-game]

%[https://r3dhummingbird.itch.io/renpy-rhythm-game]

## Ressources

Ce tutoriel devrait vous aider à commencer avec Ren'Py. Il est toujours utile de se référer à [la documentation officielle](https://www.renpy.org/doc/html/) lorsque vous apprenez les fonctionnalités plus avancées pour ajouter du dynamisme à votre projet.

J'ai également créé du matériel de cours pour vous aider à vous rafraîchir sur les fondamentaux de Python et leurs capacités dans les scripts Ren'Py.

%[https://github.com/RuolinZheng08/python-for-renpy-dev]

%[https://www.udemy.com/course/python-basics-for-renpy-developers/?referralCode=774C55606994052EBFCB]

Consultez ma vidéo d'introduction au cours sur YouTube :

%[https://www.youtube.com/watch?v=pQcb_pfIbI0]

Merci d'avoir lu et amusez-vous à raconter votre histoire !