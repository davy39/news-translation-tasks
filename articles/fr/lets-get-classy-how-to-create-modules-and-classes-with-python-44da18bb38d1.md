---
title: 'Soyons élégants : comment créer des modules et des classes avec Python'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T20:47:24.000Z'
originalURL: https://freecodecamp.org/news/lets-get-classy-how-to-create-modules-and-classes-with-python-44da18bb38d1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0PG2toS66TDJQQ7AtHGJ-Q.png
tags:
- name: class
  slug: class
- name: coding
  slug: coding
- name: modules
  slug: modules
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: 'Soyons élégants : comment créer des modules et des classes avec Python'
seo_desc: 'By Hari Santanam

  In object-oriented computer languages such as Python, classes are basically a template
  to create your own objects. Objects are an encapsulation of variables and functions
  into a single entity. Objects get their variables and function...'
---

Par Hari Santanam

Dans les langages de programmation orientés objet comme Python, les classes sont essentiellement un modèle pour créer vos propres objets. Les objets sont une encapsulation de variables et de fonctions en une seule entité. Les objets obtiennent leurs variables et fonctions à partir des classes.

Que dites-vous ?

Voici quelques exemples qui vous aideront à comprendre — lisez la suite. Il y a aussi une console de code interactive, il suffit de presser le bouton « Exécuter » en haut de la fenêtre spécifique.

La manière la plus simple de décrire les classes et comment les utiliser est la suivante :

Imaginez que vous avez de grands pouvoirs. Vous créez une espèce (« classe »).

Ensuite, vous créez des attributs pour cette espèce (« propriétés ») — taille, poids, membres, couleur, pouvoirs, et ainsi de suite.

Ensuite, vous créez une instance de cette espèce — Fido le chien, Drogon de Game of Thrones, et ainsi de suite. Ensuite, vous travaillez avec ces instances :

* Dans un jeu, par exemple, ils s'engageraient dans une action, interagiraient, en utilisant leurs attributs.
* Dans une application bancaire, ils seraient les différentes transactions.
* Dans une application d'achat/vente/échange/location de véhicules, la classe véhicule pourrait alors engendrer des sous-classes telles que les voitures. Chacune aurait des attributs tels que le kilométrage, les options, les caractéristiques, la couleur et la finition.

Vous pouvez déjà voir pourquoi cela est utile. Vous créez, réutilisez, adaptez et améliorez des éléments de manière très efficace, logique et utile.

À ce stade, vous avez probablement réalisé que c'est une façon de classer et de regrouper, similaire à la manière dont les humains apprennent :

* Les animaux sont des êtres vivants qui ne sont ni humains ni arbres, dans un sens basique
* puis vous passez à différents types d'animaux — les chiens, les chats sont probablement les premiers animaux que la plupart d'entre nous avons appris à connaître
* puis vous passez à différents attributs des animaux — formes, tailles, sons, appendices et ainsi de suite.

Par exemple, lorsque vous étiez enfant, votre première compréhension d'un chien était probablement quelque chose avec quatre pattes qui aboyait. Ensuite, vous avez appris à distinguer que certains étaient de vrais chiens, d'autres étaient des jouets. Que ce concept de « chien » contenait de nombreux types.

Créer et utiliser des classes, c'est essentiellement :

* construire un modèle pour mettre des « choses » dedans — une classification
* qui peut ensuite être exploitée. Par exemple, récupérer toutes les personnes avec des chiens que vous pourriez demander de lier à un blog sur les animaux de compagnie, ou tous les clients de la banque qui pourraient être de bons prospects pour une nouvelle carte de crédit.

Le point principal ici est que les **classes** sont des objets qui peuvent produire des instances de ces modèles, sur lesquelles des opérations et des méthodes peuvent être appliquées. C'est une excellente façon de conceptualiser, organiser et construire une hiérarchie pour toute organisation ou processus.

Alors que notre monde devient plus complexe, c'est une façon de mimiquer cette complexité d'un point de vue hiérarchique. Cela construit également une compréhension plus profonde des processus et des interactions pour les contextes commerciaux, techniques et sociaux d'un point de vue technologique de l'information virtuelle.

Un exemple pourrait être un jeu vidéo que vous créez. Chaque personnage pourrait être une « classe », avec ses propres attributs, qui interagit avec des instances d'autres classes. Le roi George de la classe « Roi » pourrait interagir avec le bouffon de la cour Funnyman de la classe « Clown », et ainsi de suite. Un Roi pourrait avoir une classe de « serviteur » royal, et une classe de « serviteur » aurait toujours une classe de « Roi », par exemple.

Voici ce que nous allons faire :

* créer une classe et l'utiliser
* créer un module et déplacer la création et l'initialisation de la classe vers le module
* appeler le module dans un nouveau programme pour utiliser la classe

Le code est disponible sur GitHub [ici](https://github.com/HariSan1/class-module).

```
#TSB - Créer une classe en Python - positions de fusée (x,y) et graphique
```

```
#certains éléments et commentaires en gras pour attirer l'attention sur le processusimport matplotlib.pyplot as plt
```

```
class Rocket():  def __init__(self, x=0, y=0):    #chaque fusée a une position (x,y) ; l'utilisateur ou la fonction appelante a le choix    #de passer les valeurs x et y, ou par défaut elles sont définies à 0    self.x = x    self.y = y      def move_up(self):    self.y += 1      def move_down(self):    self.y -= 1      def move_right(self):    self.x += 1      def move_left(self):    self.x -= 1
```

```
#Créer une série de fusées - positions x,y, je l'appelle rocketrockets=[]rockets.append(Rocket())rockets.append(Rocket(0,2))rockets.append(Rocket(1,4))rockets.append(Rocket(2,6))rockets.append(Rocket(3,7))rockets.append(Rocket(5,9))rockets.append(Rocket(8, 15))  #Montrer sur un graphique où se trouve chaque fusée
```

```
for index, rocket in enumerate(rockets):  #position originale des fusées  print("La fusée %d est à (%d, %d)." % (index, rocket.x, rocket.y))  plt.plot(rocket.x, rocket.y, 'ro', linewidth=2, linestyle='dashed', markersize=12)  #déplacer la 'fusée' d'une unité vers le haut  rocket.move_up()  print("La nouvelle position de la fusée %d est à (%d, %d)." % (index, rocket.x, rocket.y))  #tracer la nouvelle position  plt.plot(rocket.x, rocket.y, 'bo', linewidth=2, linestyle='dashed', markersize=12)  #déplacer la fusée vers la gauche, puis tracer la nouvelle position  rocket.move_left()  plt.plot(rocket.x, rocket.y, 'yo', linewidth=2, linestyle='dashed', markersize=12)
```

```
#montrer la légende du graphique pour faire correspondre les couleurs avec la positionplt.gca().legend(('position originale','^ - Déplacé vers le haut', '< - Déplacé vers la gauche'))plt.show()#plt.legend(loc='upper left')
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*HVwrF6BepYaTcRAltJaPDQ.jpeg)
_Sortie du code ci-dessus, utilisant la classe Python_

Maintenant, créons un module et déplaçons une partie du code ci-dessus vers le module. Chaque fois que nous devons créer cet ensemble simple de coordonnées x,y dans un programme, nous pouvons utiliser le module pour le faire.

### Qu'est-ce qu'un module et pourquoi en avons-nous besoin ?

Un module est un fichier contenant des définitions et des instructions Python. Un module est du code Python qui peut être appelé à partir d'autres programmes pour des tâches couramment utilisées, sans avoir à les taper dans chaque programme qui les utilise.

Par exemple, lorsque vous appelez « matplotlib.plot », vous appelez un module de package. Si vous n'aviez pas ce module, vous devriez définir la fonctionnalité de traçage dans **chaque** programme qui utilise un graphique de traçage.

D'après la [documentation](https://docs.python.org/2/tutorial/modules.html) de Python :

> Si vous quittez l'interpréteur Python et que vous y entrez à nouveau, les définitions que vous avez faites (fonctions et variables) sont perdues. Par conséquent, si vous voulez écrire un programme un peu plus long, il est préférable d'utiliser un éditeur de texte pour préparer l'entrée pour l'interpréteur et de l'exécuter avec ce fichier comme entrée. Cela est connu comme la création d'un script. À mesure que votre programme devient plus long, vous pouvez vouloir le diviser en plusieurs fichiers pour une maintenance plus facile. Vous pouvez également vouloir utiliser une fonction pratique que vous avez écrite dans plusieurs programmes sans copier sa définition dans chaque programme.

> Pour supporter cela, Python a un moyen de mettre des définitions dans un fichier et de les utiliser dans un script ou dans une instance interactive de l'interpréteur. Un tel fichier est appelé un module ; les définitions d'un module peuvent être importées dans d'autres modules ou dans le module principal (la collection de variables auxquelles vous avez accès dans un script exécuté au niveau supérieur et en mode calculatrice).

Voici notre module simple. Il prend la création de la classe et les fonctions pour déplacer une instance de cette classe du programme ci-dessus et les place dans sa propre classe. Nous allons ensuite utiliser cela dans un nouveau programme simplement en appelant et en référençant ce module :

Remarquez ce que nous avons fait ci-dessus :

* créé et initialisé la classe
* créé une fonction pour déplacer une instance de la classe dans les quatre directions principales (haut, bas, droite, gauche) et les incréments — en tant que paramètres, ou arguments de la fonction
* créé une autre fonction pour calculer la distance entre deux instances de la classe, en utilisant la formule de distance graphique

Voici comment nous allons utiliser le nouveau module pour réécrire le même programme que dans la première partie. Remarquez dans la section d'importation au début, nous importons maintenant le module `simple_module1` que nous venons de créer :

Voici la sortie du code utilisant notre module. Notez qu'ils sont les mêmes, à l'exception du titre du graphique et de la forme des marqueurs de position, que j'ai changés à des fins de comparaison.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M5O4PXU-UqHuXe62qSPezg.jpeg)
_Sortie du code de création et d'appel de notre propre module !_

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Ihrh85VkkfYuZhiH_4oAg.png)
_Comparaison du fichier original-gauche(créer une classe, l'utiliser) et la même fonctionnalité utilisant un module, droite_

![Image](https://cdn-media-1.freecodecamp.org/images/1*QnBS_HmigffIj6PBz2DvUQ.jpeg)
_Comparaison de la sortie. Du côté droit, j'ai changé la forme du marqueur pour la distinction, mais les positions sont inchangées._

C'est génial, pourriez-vous dire — quelles sont quelques autres utilisations pour cela ? Un exemple classique est un compte bancaire. Une classe client pourrait contenir le nom et les détails de contact et — plus important encore — la classe compte aurait des éléments de dépôt et de retrait.

Cela est grossièrement simplifié mais, à des fins d'illustration, c'est utile. C'est tout — créer un modèle, puis définir des instances de ce modèle avec des détails (propriétés), et ajouter de la valeur en ajoutant, soustrayant, modifiant, déplaçant et utilisant ces instances pour vos objectifs de programme.

Vous vous demandez toujours à propos des classes ? D'accord, soyons « élégants » — voici une autre illustration simple. Nous appellerons cette classe « Personne ». Elle n'a que deux propriétés — nom et âge. Nous ajouterons ensuite une instance de celle-ci avec le nom et l'âge d'une personne, et l'imprimerons. Selon quel est votre objectif, vous pouvez imaginer tous les autres détails que vous pourriez ajouter — par exemple, état matrimonial et préférences de localisation pour une application de réseautage social, expérience de travail en années et spécialisation industrielle pour une application liée à la carrière. Pressez le petit triangle ci-dessous pour voir comment cela fonctionne.

Donc, vous l'avez. Vous pouvez créer de nombreuses classes différentes, avec des classes parentes, des sous-classes et ainsi de suite. Merci d'avoir lu — veuillez applaudir si vous avez aimé. Voici quelques autres références si vous souhaitez en apprendre plus :

* [Documentation Python — Classes](https://docs.python.org/3/tutorial/classes.html)
* [Python Orienté Objet — Tutorials Point](https://www.tutorialspoint.com/python/python_classes_objects.htm)
* [Classes et Objets — learnpython.org](https://www.learnpython.org/en/Classes_and_Objects)