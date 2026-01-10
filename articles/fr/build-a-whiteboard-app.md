---
title: Comment créer une application de tableau blanc avec Python et Tkinter
subtitle: ''
author: Juan P. Romano
co_authors: []
series: null
date: '2023-11-07T22:23:59.000Z'
originalURL: https://freecodecamp.org/news/build-a-whiteboard-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/whiteboard_tkinter_python_banner_pic.png
tags:
- name: Python
  slug: python
- name: tkinter
  slug: tkinter
seo_title: Comment créer une application de tableau blanc avec Python et Tkinter
seo_desc: 'In this tutorial, you will learn how to build a simple whiteboard app using
  Python and Tkinter.

  Some months ago, I was teaching a Python course. I was struggling to convey certain
  concepts because it was an online course, and I couldn''t use a whitebo...'
---

Dans ce tutoriel, vous apprendrez à créer une application de tableau blanc simple en utilisant Python et Tkinter.

Il y a quelques mois, j'enseignais un cours de Python. J'avais du mal à transmettre certains concepts car c'était un cours en ligne, et je ne pouvais pas utiliser un tableau blanc ou même un tableau traditionnel. La fonctionnalité de tableau blanc intégrée dans Google Meet était également assez complexe à utiliser et à partager.

Alors, j'ai décidé de chercher sur Google pour voir s'il y avait des dépôts GitHub avec des applications de tableau blanc.

J'en ai trouvé beaucoup. Mais après en avoir essayé beaucoup, j'ai constaté que les applications étaient souvent trop compliquées pour mes besoins. Je voulais quelque chose de plus simple, où je pourrais choisir des couleurs et des tailles de ligne, et puis je pourrais dessiner moi-même.

Alors, qu'ai-je fait ? J'ai décidé de coder ma propre application. Et pour ce processus, j'ai choisi d'utiliser Python et Tkinter, la boîte à outils GUI (Interface Graphique Utilisateur) par défaut qui vient avec Python.

Le résultat final ?

![Image](https://www.freecodecamp.org/news/content/images/2023/11/image-10.png align="left")

*Les fenêtres de l'application de tableau blanc avec une toile blanche pour commencer à dessiner et à écrire et le sélecteur de couleur RVB.*

Alors dans ce tutoriel, je vais vous guider à travers le processus afin que vous puissiez le construire vous-même. Cela vous aidera à perfectionner vos compétences en Python et à en apprendre davantage sur Tkinter, aussi.

## Comment construire la fonctionnalité de l'application

### Configurer votre environnement de développement

La construction de cette application est assez simple. Vous aurez besoin de la dernière version de Python installée, que vous pouvez télécharger et installer depuis ici :

%[https://www.python.org/] 

Si vous êtes un utilisateur Linux, vous n'aurez pas besoin de l'installer car il est fourni avec votre distribution. De plus, vous devez avoir une compréhension de base de Python et savoir comment créer des fonctions.

Après avoir vérifié que vous avez déjà Python installé sur votre ordinateur, ouvrez Visual Studio Code ou votre éditeur de code préféré pour commencer à écrire du code.

### Comment construire la fonctionnalité de dessin

Créez un fichier Python et commencez par importer les modules Tkinter et color chooser, comme ceci :

```python
import tkinter as tk
from tkinter.colorchooser import askcolor
```

Après avoir importé Tkinter et le module colorchooser, qui ouvrira une modale pour sélectionner nos combinaisons de couleurs RVB, vous pouvez commencer à écrire les fonctions pour faire fonctionner ce tableau blanc.

Tout d'abord, créez une fonction pour commencer à dessiner, comme ceci :

```python
def start_drawing(event):
    global is_drawing, prev_x, prev_y
    is_drawing = True
    prev_x, prev_y = event.x, event.y
```

Ce code définit une fonction nommée `start_drawing` qui est destinée à gérer le début d'une action de dessin dans une application d'interface graphique (GUI).

Décomposons ce que fait cette fonction :

1. `def start_drawing(event):`: Cette ligne définit une fonction nommée `start_drawing` qui prend un `event` comme paramètre. En programmation GUI, les événements sont des actions ou des occurrences (comme des clics de souris, des pressions de touches, etc.) qui déclenchent des fonctions spécifiques lorsqu'elles se produisent.
    
2. `global is_drawing, prev_x, prev_y`: Cette ligne déclare que les variables `is_drawing`, `prev_x` et `prev_y` sont des variables globales. En Python, les variables globales sont accessibles de n'importe où dans le code et peuvent être modifiées dans les fonctions. Cette ligne garantit que ces variables sont accessibles dans la fonction.
    
3. `is_drawing = True`: Cette ligne définit la variable `is_drawing` à `True`. Cette variable est généralement utilisée pour indiquer si une action de dessin est en cours. En la définissant à `True`, la fonction signale qu'une action de dessin a commencé.
    
4. `prev_x, prev_y = event.x, event.y`: Cette ligne capture les coordonnées actuelles du curseur de la souris lorsque la fonction `start_drawing` est appelée. Elle attribue les coordonnées `x` et `y` du curseur de la souris à ce moment-là aux variables `prev_x` et `prev_y`. Ces variables sont utilisées pour suivre le point de départ de l'action de dessin.
    

Ainsi, lorsque cette fonction est appelée (généralement en réponse à un événement de clic de souris), elle définit le drapeau `is_drawing` à `True` pour indiquer qu'une action de dessin est en cours et enregistre la position initiale du curseur de la souris en utilisant les variables `prev_x` et `prev_y`. Ces variables sont ensuite utilisées dans les actions de dessin suivantes pour connecter le point de départ avec la position actuelle du curseur afin de créer un dessin sur le canevas.

Maintenant, continuons à coder. Ensuite, nous devons écrire une fonction pour dessiner sur le tableau blanc, comme ceci :

```python
def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)
        prev_x, prev_y = current_x, current_y
```

Un dessin est essentiellement une combinaison de points remplis de couleurs, fonctionnant comme un vecteur. Pour fonctionner comme un vecteur, il doit avoir un point de départ et un point de fin. Donc, après avoir créé une fonction pour commencer à dessiner, vous aurez besoin d'une fonction pour arrêter de dessiner, comme ceci :

```python
def stop_drawing(event):
    global is_drawing
    is_drawing = False
```

### Comment construire la fonctionnalité de changement de couleur

Maintenant que vous avez la fonctionnalité de dessin principale, l'étape suivante consiste à implémenter la fonction de changement de couleur. Il s'agit d'une fonction simple qui appelle le module `askcolor`, qui fait déjà partie de Tkinter, comme ceci :

```python
def change_pen_color():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color
```

Pour la dernière fonctionnalité, vous créerez une fonction pour ajuster la largeur de la ligne, vous permettant de choisir l'épaisseur de vos lignes. Voici comment l'implémenter :

```python
def change_line_width(value):
    global line_width
    line_width = int(value)
```

Maintenant, vous avez terminé les fonctions. Ensuite, vous utiliserez Tkinter pour créer la fenêtre de votre application et des boutons pour choisir les couleurs, effacer le tableau blanc et sélectionner la largeur de votre ligne.

## Comment construire l'interface graphique

GUI signifie Interface Graphique Utilisateur, représentant les fenêtres avec lesquelles vous interagissez sur votre ordinateur, smartphone, tablette, etc.

Lors de la programmation d'une application de bureau utilisant Python et Tkinter, vous définissez la taille, la position, les boutons et tout autre élément que vous souhaitez pour votre programme. Dans ce cas, vous devez créer les éléments suivants :

* Un titre pour votre application.
    
* Une toile blanche vierge pour dessiner.
    
* Un cadre pour contenir les contrôles de votre application sur la même ligne.
    
* Un bouton de couleur.
    
* Un bouton pour effacer la toile afin d'effacer tout votre travail et de recommencer à dessiner.
    
* Un curseur pour sélectionner la largeur de votre ligne.
    

### Comment créer votre fenêtre

Commencez par créer une fenêtre avec un titre et une toile blanche :

```python
root = tk.Tk()
root.title("Application de Tableau Blanc")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

is_drawing = False
drawing_color = "black"
line_width = 2

root.geometry("800x600")
```

Décomposons ce que fait chaque partie :

1. `root = tk.Tk()`: Cette ligne crée la fenêtre principale de l'application. Elle initialise une application Tkinter et l'assigne à la variable `root`. Cette fenêtre sert de conteneur pour tous les éléments graphiques de l'application de tableau blanc.
    
2. `root.title("Application de Tableau Blanc")`: Cela définit le titre de la fenêtre de l'application à "Application de Tableau Blanc". Le titre apparaît dans la barre de titre de la fenêtre et fournit un nom pour l'application.
    
3. `canvas = tk.Canvas(root, bg="white")`: Cette ligne crée une toile de dessin dans la fenêtre principale de l'application. La toile est une zone rectangulaire blanche où les utilisateurs peuvent dessiner. Elle est initialisée avec une couleur de fond blanche. La toile est assignée à la variable `canvas`.
    
4. `canvas.pack(fill="both", expand=True)`: Cela configure la toile pour remplir à la fois l'espace horizontal et vertical de la fenêtre de l'application. Cela permet à la toile de s'étendre et d'occuper toute la fenêtre.
    
5. `is_drawing = False`: Cela initialise une variable `is_drawing` à `False`. Elle est généralement utilisée pour suivre si l'utilisateur est en train de dessiner ou non. Lorsque l'utilisateur commence à dessiner, cette variable est définie à `True` pour indiquer une action de dessin en cours.
    
6. `drawing_color = "black"`: Cela initialise une variable `drawing_color` à "black". Elle spécifie la couleur qui sera utilisée pour dessiner sur la toile. Vous pouvez changer cette couleur selon vos besoins pour dessiner avec différentes couleurs avec les fonctions que vous ajouterez plus tard dans ce tutoriel.
    
7. `line_width = 2`: Cela initialise une variable `line_width` à 2. Elle spécifie la largeur des lignes ou des traits utilisés pour dessiner. Vous pouvez ajuster cette valeur pour changer l'épaisseur des lignes.
    
8. `root.geometry("800x600")`: Cela définit la taille initiale de la fenêtre de l'application à 800 pixels de largeur et 600 pixels de hauteur. Cela définit les dimensions de la fenêtre lorsqu'elle est affichée pour la première fois, mais vous pouvez redimensionner votre fenêtre et avec elle, votre espace de toile.
    

### Comment construire votre barre de navigation et vos contrôles

La prochaine chose que vous devez faire est de créer un cadre pour contenir les boutons ou les contrôles sur la même ligne. C'est la manière la plus confortable d'avoir des boutons, et c'est une sorte de barre de navigation.

```python
controls_frame = tk.Frame(root)
controls_frame.pack(side="top", fill="x")
```

Ensuite, créez deux boutons et donnez-leur des positions fixes par défaut sur votre écran, comme ceci :

```python
color_button = tk.Button(controls_frame, text="Changer la Couleur", command=change_pen_color)
clear_button = tk.Button(controls_frame, text="Effacer la Toile", command=lambda: canvas.delete("all"))

color_button.pack(side="left", padx=5, pady=5)
clear_button.pack(side="left", padx=5, pady=5)
```

Donc, si vous exécutez votre application maintenant, vous verrez quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/image-14.png align="left")

*La fenêtre de l'application avec la toile vierge et deux boutons, l'un pour changer les couleurs et l'autre pour effacer la toile.*

Vous avez déjà les deux boutons principaux pour votre application, l'un pour changer les couleurs et l'autre pour effacer la toile. Le dernier contrôle que vous devez créer est un curseur pour la fonction de largeur de ligne. Pour cela, vous écrirez le code suivant :

```python
line_width_label = tk.Label(controls_frame, text="Largeur de Ligne :")
line_width_label.pack(side="left", padx=5, pady=5)

line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val))
line_width_slider.set(line_width)
line_width_slider.pack(side="left", padx=5, pady=5)
```

Et encore, faisons un récapitulatif de ce qui se passe ici :

1. `line_width_label = tk.Label(controls_frame, text="Largeur de Ligne :")`: Cette ligne crée un widget d'étiquette avec le texte "Largeur de Ligne :". L'étiquette est destinée à afficher du texte pour décrire le but du curseur suivant (qui contrôle la largeur de la ligne). Elle est placée dans le widget `controls_frame`.
    
2. `line_width_label.pack(side="left", padx=5, pady=5)`: Cette ligne configure le placement de l'étiquette dans le `controls_frame`.
    
3. `side="left"`: Cela définit l'étiquette pour qu'elle soit placée sur le côté gauche du `controls_frame`. Cela garantit que l'étiquette est alignée à gauche.
    
4. `padx=5`: Cela ajoute un remplissage horizontal de 5 pixels autour de l'étiquette, créant un certain espacement.
    
5. `pady=5`: Cela ajoute un remplissage vertical de 5 pixels autour de l'étiquette, créant un espacement.
    
6. `line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val))`: Cette ligne crée un widget curseur horizontal (Scale widget) qui permet à l'utilisateur de sélectionner une largeur de ligne. Le curseur varie d'une valeur minimale de 1 (`from_=1`) à une valeur maximale de 10 (`to=10`). L'option `command` est définie pour appeler la fonction `change_line_width` avec la valeur sélectionnée chaque fois que la position du curseur change.
    
7. `line_width_slider.set(line_width)`: Cela définit la position initiale du curseur à la valeur stockée dans la variable `line_width`, qui est initialisée plus tôt dans le code. Cela garantit que le curseur commence à la largeur de ligne par défaut.
    
8. `line_width_slider.pack(side="left", padx=5, pady=5)`: Cette ligne configure le placement du curseur dans le `controls_frame`. Il est placé sur le côté gauche, et un remplissage est ajouté pour créer un espacement autour du curseur.
    

Donc, si vous atteignez ce point, votre application devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/image-15.png align="left")

### Comment connecter vos fonctionnalités avec votre interface graphique

Mais si vous appuyez sur les boutons ou déplacez le curseur pour la largeur de la ligne, cela ne fonctionnera pas car vous devez encore lier ou "connecter" les fonctions que vous avez codées au début de ce tutoriel avec les boutons et les contrôles que vous avez créés.

Pour cela, vous allez écrire ce code :

```python
canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

root.mainloop()
```

Donc, un dernier récapitulatif pour comprendre la fin de votre code :

* `canvas.bind("<Button-1>", start_drawing)`: Lorsque le bouton gauche de la souris est cliqué sur la toile, cela déclenche la fonction `start_drawing`.
    
* `canvas.bind("<B1-Motion>", draw)`: Pendant que le bouton gauche de la souris est maintenu enfoncé et que la souris est déplacée sur la toile, cela déclenche la fonction `draw`.
    
* `canvas.bind("<ButtonRelease-1>", stop_drawing)`: Lorsque le bouton gauche de la souris est relâché (événement de relâchement du bouton), cela déclenche la fonction `stop_drawing`.
    
* Et enfin, `root.mainloop()` démarre la boucle principale de l'application, lui permettant de répondre aux interactions et aux événements de l'utilisateur.
    

## Conclusion

J'espère que vous avez apprécié la lecture de ce tutoriel autant que j'ai apprécié l'écrire, et que le tableau blanc vous aide dans ce que vous devez faire.

Si vous souhaitez télécharger l'application, vous pouvez la consulter ici :

%[https://github.com/jpromanonet/white_board_py] 

Jusqu'à la prochaine fois ! Bon codage et continuez à coder pour créer un portfolio cool =D