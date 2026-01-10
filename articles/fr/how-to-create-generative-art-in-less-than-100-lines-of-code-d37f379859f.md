---
title: Comment créer de l'art génératif en moins de 100 lignes de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T23:35:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-generative-art-in-less-than-100-lines-of-code-d37f379859f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zMSR6lwGpWySHyxC5kagFA.jpeg
tags:
- name: creativity
  slug: creativity
- name: generative art
  slug: generative-art
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment créer de l'art génératif en moins de 100 lignes de code
seo_desc: 'By Eric Davidson

  Generative art, like any programming topic, can be intimidating if you’ve never
  tried it before. I’ve always been interested in it because I love finding new ways
  that programming can be utilized creatively. Furthermore, I think anyo...'
---

Par Eric Davidson

L'art génératif, comme tout sujet de programmation, peut être intimidant si vous ne l'avez jamais essayé auparavant. J'ai toujours été intéressé par ce domaine car j'adore trouver de nouvelles façons d'utiliser la programmation de manière créative. De plus, je pense que tout le monde peut apprécier le concept d'œuvres d'art qui se créent littéralement elles-mêmes.

![Image](https://cdn-media-1.freecodecamp.org/images/X9dFKTJ0n2XhG9TULvKBtJgApZeErkD6vRDQ)
_Marquée pour réutilisation depuis Pexels_

### Qu'est-ce que l'art génératif ?

L'art génératif est le résultat d'un système qui prend ses propres décisions concernant l'œuvre, plutôt qu'un humain. Le système pourrait être aussi simple qu'un seul programme Python, tant qu'il a des **règles** et un aspect d'**aléatoire**.

Avec la programmation, il est assez simple de créer des règles et des contraintes. Ce sont là des instructions conditionnelles. Cela dit, trouver des moyens de rendre ces règles intéressantes peut être délicat.

![Image](https://cdn-media-1.freecodecamp.org/images/wbde3i5uGTH1rRXb7AAHGUgsp1mgr4jN90JH)
_Le Jeu de la Vie de Conway (Marqué pour réutilisation)_

Le [Jeu de la Vie](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) est un ensemble célèbre de quatre règles simples qui déterminent la "naissance" et la "mort" de chaque cellule dans le système. Chacune des règles joue un rôle dans l'avancement du système à travers chaque génération. Bien que les règles soient simples et faciles à comprendre, des motifs complexes commencent rapidement à émerger et forment finalement des résultats fascinants.

Les règles peuvent être responsables de la création de la fondation de quelque chose d'intéressant, mais même quelque chose d'aussi excitant que le Jeu de la Vie de Conway est prévisible. Puisque les quatre règles sont les facteurs déterminants pour chaque génération, la façon de produire des résultats imprévisibles est d'introduire une randomisation à l'état initial des cellules. Commencer avec une matrice aléatoire rendra chaque exécution unique sans avoir besoin de changer les règles.

Les meilleurs exemples d'art génératif sont ceux qui trouvent une combinaison de prévisibilité et d'aléatoire afin de créer quelque chose d'intéressant qui est également statistiquement **irréproductible**.

### **Pourquoi devriez-vous essayer ?**

Tous les projets secondaires ne se valent pas, et l'art génératif peut ne pas être quelque chose auquel vous êtes enclin à consacrer du temps. Si vous décidez de travailler sur un projet cependant, vous pouvez vous attendre à ces avantages :

* **Expérience** — L'art génératif est une autre opportunité d'affiner certaines compétences nouvelles et anciennes. Il peut servir de passerelle pour pratiquer des concepts comme les algorithmes, les structures de données, et même de nouveaux langages.
* **Résultats Tangibles** — Dans le monde de la programmation, nous voyons rarement quelque chose de physique résultant de nos efforts, ou du moins je ne le vois pas. Actuellement, j'ai quelques posters dans mon salon affichant des impressions de mon art génératif et j'adore que la programmation soit responsable de cela.
* **Projets Attrayants** — Nous avons tous eu l'expérience d'expliquer un projet personnel à quelqu'un, peut-être même lors d'un entretien, sans moyen facile de transmettre l'effort et les résultats du projet. L'art génératif parle de lui-même, et la plupart des gens seront impressionnés par vos créations, même s'ils ne peuvent pas comprendre pleinement les méthodes.

### Par où devriez-vous commencer ?

Se lancer dans l'art génératif est le même processus que pour tout projet, l'étape la plus cruciale est de trouver une idée ou d'en construire une. Une fois que vous avez un objectif en tête, vous pouvez commencer à travailler sur la technologie nécessaire pour l'atteindre.

La plupart de mes projets d'art génératif ont été réalisés en Python. C'est un langage assez facile à prendre en main et il dispose de certains packages incroyables pour aider à la manipulation d'images, comme [Pillow](https://pillow.readthedocs.io/en/5.3.x/).

Heureusement pour vous, il n'est pas nécessaire de chercher très loin pour un point de départ, car j'ai fourni un peu de code ci-dessous pour que vous puissiez jouer avec.

### Générateur de Sprites

Ce projet a commencé lorsque j'ai vu un post montrant un générateur de sprites écrit en JavaScript. Le programme créait des sprites d'art pixelisé de 5x5 avec quelques options de couleurs aléatoires et son résultat ressemblait à des space invaders multicolores.

Je savais que je voulais pratiquer la manipulation d'images en Python, alors j'ai pensé que je pourrais simplement essayer de recréer ce concept par moi-même. De plus, je pensais que je pourrais l'étendre puisque le projet original était si limité en taille des sprites. Je voulais pouvoir spécifier non seulement la taille, mais aussi le nombre de sprites et même la taille de l'image.

Voici un aperçu de deux sorties différentes de la solution que j'ai obtenue :

![Image](https://cdn-media-1.freecodecamp.org/images/4d1yWSxXbv5c8LrTNUaJceViqS7DRXV0wYVS)
_7x7–30–1900_

![Image](https://cdn-media-1.freecodecamp.org/images/UV5HgITUXjpy535zkeoCKPRDs-kn6A6-kGgJ)
_43x43–6–1900_

Ces deux images ne se ressemblent pas du tout, mais elles sont toutes deux les résultats du même système. Sans compter que, en raison de la complexité de l'image et de l'**aléatoire** de la génération des sprites, il y a une probabilité extrêmement élevée que même avec les mêmes arguments, ces images seront à jamais uniques. J'adore ça.

### L'environnement

Si vous voulez commencer à jouer avec le générateur de sprites, il y a un peu de travail de fondation à faire d'abord.

La configuration d'un environnement approprié avec Python peut être délicate. Si vous n'avez pas travaillé avec Python auparavant, vous devrez probablement [télécharger Python 2.7.10](https://www.python.org/downloads/). J'ai initialement eu des problèmes pour configurer l'environnement, donc si vous commencez à rencontrer des problèmes, vous pouvez faire ce que j'ai fait et vous pencher sur les [environnements virtuels](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/). Enfin, assurez-vous d'avoir installé [Pillow](https://pillow.readthedocs.io/en/5.3.x/installation.html) également.

Une fois que vous avez configuré l'environnement, vous pouvez copier mon code dans un fichier avec l'extension .py et l'exécuter avec la commande suivante :

```
python spritething.py [DIMENSIONS_SPRITE] [NOMBRE] [TAILLE_IMAGE]
```

Par exemple, la commande pour créer la première matrice de sprites ci-dessus serait :

```
python spritething.py 7 30 1900
```

### Le code

```
import PIL, random, sysfrom PIL import Image, ImageDraw
```

```
origDimension = 1500
```

```
r = lambda: random.randint(50,215)rc = lambda: (r(), r(), r())
```

```
listSym = []
```

```
def create_square(border, draw, randColor, element, size):  if (element == int(size/2)):    draw.rectangle(border, randColor)  elif (len(listSym) == element+1):    draw.rectangle(border,listSym.pop())  else:    listSym.append(randColor)    draw.rectangle(border, randColor)
```

```
def create_invader(border, draw, size):  x0, y0, x1, y1 = border  squareSize = (x1-x0)/size  randColors = [rc(), rc(), rc(), (0,0,0), (0,0,0), (0,0,0)]  i = 1
```

```
  for y in range(0, size):    i *= -1    element = 0    for x in range(0, size):      topLeftX = x*squareSize + x0      topLeftY = y*squareSize + y0      botRightX = topLeftX + squareSize      botRightY = topLeftY + squareSize
```

```
      create_square((topLeftX, topLeftY, botRightX, botRightY), draw, random.choice(randColors), element, size)      if (element == int(size/2) or element == 0):        i *= -1;      element += i
```

```
def main(size, invaders, imgSize):  origDimension = imgSize  origImage = Image.new('RGB', (origDimension, origDimension))  draw = ImageDraw.Draw(origImage)
```

```
  invaderSize = origDimension/invaders  padding = invaderSize/size
```

```
  for x in range(0, invaders):    for y in range(0, invaders):      topLeftX = x*invaderSize + padding/2      topLeftY = y*invaderSize + padding/2      botRightX = topLeftX + invaderSize - padding      botRightY = topLeftY + invaderSize - padding
```

```
      create_invader((topLeftX, topLeftY, botRightX, botRightY), draw, size)
```

```
  origImage.save("Examples/Example-"+str(size)+"x"+str(size)+"-"+str(invaders)+"-"+str(imgSize)+".jpg")
```

```
if __name__ == "__main__":  main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
```

Cette solution est loin d'être parfaite, mais elle montre que la création d'art génératif ne nécessite pas une tonne de code. Je vais essayer de mon mieux d'expliquer les pièces clés.

La fonction **main** commence par créer l'image initiale et déterminer la taille des sprites. Les deux boucles _for_ sont responsables de la définition d'une bordure pour chaque sprite, divisant essentiellement les dimensions de l'image par le nombre de sprites demandés. Ces valeurs sont utilisées pour déterminer les coordonnées de chacun.

Ignorons le padding et regardons l'image ci-dessous. Imaginez que chacun des quatre carrés représente un sprite avec une taille de 1. La bordure qui est passée à la fonction suivante fait référence aux coordonnées en haut à gauche et en bas à droite. Donc le tuple pour le sprite en haut à gauche serait (0,0,1,1) tandis que le tuple pour le sprite en haut à droite serait (1,0,2,1). Ceux-ci seront utilisés comme les dimensions et les coordonnées de base pour les carrés de chaque sprite.

![Image](https://cdn-media-1.freecodecamp.org/images/dAjC0XQBCbDd1q4TiXlQjd1VZzQhlabZZW6d)
_Exemple de détermination des bordures des sprites_

La fonction **create_invader** détermine la bordure pour chaque carré dans le sprite. Le même processus pour déterminer la bordure est appliqué ici et représenté ci-dessous, sauf qu'au lieu de l'image complète, nous utilisons une bordure prédéterminée pour travailler à l'intérieur. Ces coordonnées finales pour chaque carré seront utilisées dans la fonction suivante pour dessiner réellement le sprite.

![Image](https://cdn-media-1.freecodecamp.org/images/Q2qtvddE3B8kRqrl1ZokRJJ5s8jj8JYDgCg-)
_Exemple de décomposition d'un sprite 3x3_

Pour déterminer la couleur, un simple tableau de trois tuples RGB aléatoires et trois noirs sont utilisés pour simuler une chance de 50% d'être dessinés. Les fonctions lambda près du haut du code sont responsables de la génération des valeurs RGB.

Le vrai truc de cette fonction est de créer de la symétrie. Chaque carré est associé à une valeur d'élément. Dans l'image ci-dessous, vous pouvez voir les valeurs d'élément s'incrémenter jusqu'à atteindre le centre, puis se décrémenter. Les carrés avec des valeurs d'élément correspondantes sont dessinés avec la même couleur.

![Image](https://cdn-media-1.freecodecamp.org/images/FUyF8VhfcaOyLkqTGViXlORkoUQ9K5ILkrjJ)
_Valeurs d'élément et couleurs symétriques pour une ligne dans un sprite 7x7_

Alors que **create_square** reçoit ses paramètres de **create_invader**, il utilise une file d'attente et les valeurs d'élément précédentes pour assurer la symétrie. La première occurrence des valeurs a leurs couleurs poussées dans la file d'attente et les carrés miroir retirent les couleurs.

![Image](https://cdn-media-1.freecodecamp.org/images/79LIdlwEDW-fxT37Ef1iE5p9cdyGxTZ8gXnq)
_Le processus complet de génération_

Je réalise à quel point il est difficile de lire et de comprendre la solution de quelqu'un d'autre pour un problème, et la rudesse du code ne facilite certainement pas sa complexité, mais j'espère que vous avez une assez bonne idée de son fonctionnement. En fin de compte, ce serait incroyable si vous pouviez abandonner mon code et trouver une solution entièrement différente.

### Conclusion

L'art génératif prend du temps à être pleinement apprécié, mais cela en vaut la peine. J'adore pouvoir combiner la programmation avec un visuel plus traditionnel, et j'ai définitivement appris beaucoup dans chacun de mes projets.

Dans l'ensemble, il peut y avoir des projets plus utiles à poursuivre et l'art génératif peut ne pas être quelque chose dont vous avez besoin de l'expérience, mais c'est très amusant et vous ne savez jamais comment cela pourrait vous distinguer de la foule.

Merci d'avoir lu !