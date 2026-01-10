---
title: Développement de jeux Python – Comment créer un jeu de course de tortues avec
  PyCharm
subtitle: ''
author: Programming with Shahan
co_authors: []
series: null
date: '2022-02-01T15:49:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-racing-game-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/python-game.png
tags:
- name: Game Development
  slug: game-development
- name: Python
  slug: python
seo_title: Développement de jeux Python – Comment créer un jeu de course de tortues
  avec PyCharm
seo_desc: "In this article, you'll learn how to build a racing game in Python using\
  \ the Turtle library in just 39 lines of code. \nHere's what we're going to create:\n\
  \nTurtle Racing Game Project Overview\n\U0001F9F5 Prerequisites\nVery basic knowledge\
  \ of Python programming..."
---

Dans cet article, vous apprendrez à créer un jeu de course en Python en utilisant la bibliothèque Turtle en seulement 39 lignes de code. 

Voici ce que nous allons créer :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/turtle-overview.gif)
_Aperçu du projet de jeu de course de tortues_

## 🧠 Prérequis

Une connaissance très basique de la programmation Python sera suffisante pour suivre ce tutoriel. De plus, je suppose que vous ne savez rien de cette bibliothèque [turtle](https://docs.python.org/3/library/turtle.html). Je vais tout vous enseigner à partir de zéro.

## 🛠️ Outils que nous allons utiliser

Tout d'abord, si vous n'avez pas Python installé sur votre machine, allez sur [python.org](https://www.python.org/) pour télécharger la dernière version de Python et installez-la immédiatement. 

Pour écrire le programme, nous utiliserons [PyCharm](https://www.jetbrains.com/pycharm/), qui est l'environnement de développement intégré (IDE) le plus populaire pour Python. Après avoir installé [PyCharm](https://www.jetbrains.com/pycharm/) sur votre machine, vous êtes prêt à construire ce jeu incroyable à partir de zéro. 

## ⛳ Objectifs du projet

Concrètement, nous allons écrire un programme qui déplace un objet tortue horizontalement jusqu'à ce qu'il atteigne notre ligne d'arrivée calculée. Ensuite, nous créerons sept répliques uniques de cet objet tortue en utilisant une boucle `for` avec différentes couleurs et des vitesses de déplacement aléatoires.

Nous ajouterons également une image de fond (routes avec des voies pour que les tortues fassent la course) afin de créer quelque chose qui ressemble à un environnement de course réel. 

Ensuite, nous calculerons différentes valeurs le long de l'axe vertical ou Y pour définir leurs positions de départ. 

Enfin, nous demanderons à l'utilisateur d'entrer son pari (couleur de la tortue) de sorte que si la couleur du pari de l'utilisateur correspond à la couleur de notre tortue gagnante, nous afficherons **Gagnant !** à l'écran. Sinon, nous afficherons **Vous avez perdu !** à l'écran. 

Note : pour les lecteurs d'écran ou toute personne intéressée par l'obtention du code source complet de ce projet, vous pouvez y accéder dans mon [dépôt GitHub ici](https://github.com/codewithshahan/python-racing-game). 

Alors, êtes-vous excité à l'idée de construire ce jeu ? Moi aussi. Commençons !

## 👩‍💻 Comment configurer le projet 

Ouvrez votre IDE PyCharm. Ensuite, cliquez sur Nouveau Projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-25-185042.png)
_création d'un nouveau projet_

 Appelons-le **racing-game** et cliquons sur **créer**.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2-5.png)
_Nom du projet_

Ensuite, ajoutez un nouveau fichier Python appelé `main.py`. 

## 📋 Comment utiliser la bibliothèque Turtle

Maintenant, allons sur la [documentation de turtle-graphics python](https://docs.python.org/3/library/turtle.html). Ici, vous trouverez tous les détails sur cette bibliothèque. 

Faisons défiler vers le bas et allons à la section des méthodes Turtle. Vous verrez différents types de méthodes que nous pouvons utiliser pour de nombreux objectifs différents. Nous en utiliserons quelques-unes dans notre projet actuel. 

Je recommande de lire cette documentation au moins une fois avant de plonger dans le code. Mais ne vous inquiétez pas, je vais la simplifier pour vous pendant que nous écrivons le programme. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/3-5.png)
_docs turtle_

### Importer la bibliothèque

Alors, importons **Turtle** et **Screen** du module turtle. Appelez cet écran dans une nouvelle variable appelée **screen**. Ensuite, appelez la fonction `screen.exitonclick()` pour arrêter le programme lorsque nous cliquons sur l'écran. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/4-3.png)

## 🎨 Comment définir le canevas du jeu

Maintenant, travaillons avec l'objet screen pour définir notre canevas de jeu. Donc, définissons la **largeur** à 800 pixels et la **hauteur** à 600 pixels.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/5-4.png)

 Voici le résultat : 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/6-1.png)

### Comment ajouter des graphiques de fond

Il est temps de charger notre image de fond pour notre canevas. Donc, faisons glisser notre fichier **road.gif** dans notre projet racing-game. [Cliquez sur ce lien pour télécharger les graphiques.](https://drive.google.com/file/d/14n2LlzMELtUazYYdEfusx_uVpyRU_n9t/view?usp=sharing) 

Ajoutons cette image en utilisant **`screen.bgpic`('road.gif'**).

![Image](https://www.freecodecamp.org/news/content/images/2022/01/7-1.png)

 Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/8-1.png)

## 🐢 Comment travailler avec les objets Turtle

Maintenant, créons une instance de tortue en utilisant la méthode `Turtle()` avec la forme appelée **turtle**.

Mais elle semblera vraiment petite. Donc, nous devons définir `shapesize(2)`. 

### Comment positionner les tortues

Maintenant, nous devons changer l'emplacement de notre tortue vers le coin inférieur gauche en utilisant `goto(x=-350, y=-260)`.

Ici, nous définissons `x` pour déplacer la tortue horizontalement et `y` pour verticalement avec les valeurs calculées par rapport à notre canevas. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/9-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/01/10-1.png)

Ici, vous pouvez voir que la tortue s'est déplacée vers l'emplacement souhaité. Donc, nous pouvons prendre la position `y` dans une variable globale et ajouter différents types de valeurs pour positionner nos tortues sur leurs routes respectives.  

### Comment créer les répliques de tortues

Maintenant, nous devons créer sept types différents d'objets tortues. Pour cette raison, nous utiliserons une boucle `for`. 

Donc, `for` index dans `range(0, 7)` et ensuite déplacer notre instance de tortue existante dans cette boucle. Et bien sûr, nous devons changer `y` en notre variable globale de positions `y` et obtenir leurs **indexes** dans l'ordre.  

![Image](https://www.freecodecamp.org/news/content/images/2022/01/11-4.png)

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/12-1.png)

### Comment définir les couleurs des tortues

Comme vous pouvez le voir, nous avons sept instances de tortues créées de manière égale avec différentes positions `y`. Ajoutons quelques couleurs aléatoires en utilisant une variable globale de couleurs comme nous l'avons fait pour les positions `y`. Ensuite, utilisez la méthode `color(colors[index])` avec leurs index. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/13-2.png)

Voici le résultat – magnifique ! 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/14-2.png)

### Comment supprimer les lignes disgracieuses

Vous pouvez voir qu'il y a des lignes disgracieuses qui pointent vers le milieu, et la direction du mouvement est très lente. Donc, nous pouvons utiliser les méthodes `speed('fastest')` et `penup()` pour résoudre ces problèmes. Jetez un coup d'œil ! 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/15-2.png)

### Comment faire avancer les tortues

Maintenant, qu'est-ce que nous devons faire d'autre ? Oui, vous l'avez compris ! Nous devons définir une allure aléatoire pour chaque tortue. Mais avant de faire cela, comment pouvons-nous faire avancer une seule tortue ? 

Eh bien, vous pouvez utiliser la méthode `forward()` pour cela. Disons que nous devons faire avancer nos tortues de 30 pixels. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/17.png)

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/18.png)

Mais elles ne se déplacent pas en continu. Que pouvons-nous faire d'autre ici ? Réfléchissez-y et revenez voir mes solutions.

Donc, pour résoudre ce problème, nous prenons une variable appelée **is_on** et la définissons sur `True`. Maintenant, nous allons exécuter notre programme en continu jusqu'à ce que nous le romptions en utilisant une boucle `while`.

Maintenant, nous avons l'opportunité de faire avancer notre tortue en continu de 30 pixels à chaque étape. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/7-2.png)

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/9-2.png)

Elle se déplace comme un avion parce que nous avons défini `forward` à 30.

### Comment faire courir plusieurs tortues en synchronisation 

Maintenant, nous devons cibler tous les objets tortues, pas seulement un seul. Mais comment pouvons-nous faire cela ? Réfléchissez-y et revenez voir ma solution.

Donc, nous pouvons prendre une variable globale appelée **all_turtle** et la définir sur une liste vide. Maintenant, dans la boucle for, après avoir créé sept nouvelles instances de tortues, nous pouvons `append` notre nouvelle tortue à cette liste globale **all_turtle**. De cette façon, nous pouvons y accéder dans d'autres blocs de code.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/19.png)

Maintenant, nous avons toutes nos tortues. Donc, tant que notre variable `is_on` est vraie, nous pouvons dire `all_turtle.forward(10)`. De plus, ici, nous devons utiliser une boucle for à nouveau pour obtenir chaque tortue de cette variable globale **all_turtle** et ensuite les déplacer `forward` de 10 pixels. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/20-1.png)

Voyons le résultat jusqu'à présent :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/21.png)

### Comment définir une vitesse de déplacement aléatoire

Donc, nous avons résolu notre problème de déplacement des tortues. Mais elles courent indéfiniment – il n'y a pas de point final. De plus, toutes les tortues se déplacent à la même vitesse. Réfléchissez à ce problème et essayez de le résoudre par vous-même. 

Donc, prenons une nouvelle variable **random_pace** et définissons-la sur `random.randint(0, 7)`. Elle retournera une valeur entre zéro et sept de manière aléatoire. Vous devez importer random en haut. Enfin, passez cette variable **random_pace** à la méthode `forward()` comme `forward(random_pace)`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/22.png)

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/23.png)

## 🏁 Comment définir la ligne d'arrivée

Maintenant, nous devons définir notre ligne d'arrivée sur ce canevas. Pour résoudre ce problème, nous vérifions `si` `turtle.xcor()` > 330, définissons **is_on** = `False`, sinon nous devons continuer à exécuter notre programme. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/24.png)

## 🧑‍💻 Comment demander à l'utilisateur d'entrer son pari

Nous avons terminé avec l'interface utilisateur. Maintenant, nous devons définir une logique pour permettre à l'utilisateur d'entrer son pari et comparer son pari avec notre résultat programmé. 

Pour permettre à l'utilisateur d'entrer son pari, nous pouvons écrire `screen.textinput` avec un espace réservé **'Entrez votre pari'**. Nous allons également **`demander`** à l'utilisateur **"quelle couleur de tortue"** et le stocker dans une variable globale **user_bet**. 

Ensuite, nous prenons une variable **winner**. Nous vérifions si `winner == user_bet` qui proviendra de la couleur d'entrée de l'utilisateur. Nous imprimons **Vous avez gagné**, sinon, **Vous avez perdu** avec la couleur de la tortue gagnante. C'est pourquoi nous devons utiliser une f-string pour passer la variable dans la méthode print.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/25.png)

## 🎉 Comment afficher les résultats à l'écran

Maintenant, je veux que vous affichiez ce texte d'impression sur le canevas avec leur couleur de tortue réactive après avoir touché la ligne d'arrivée. Comment pouvez-vous implémenter cela ? Vous verrez ma solution ensuite.

Donc, ici en haut. Nous prenons deux variables globales **`ALIGN = "right"`** et **`FONT = ("Courier", 28, "bold")`**. Nous allons écrire pour aligner le texte à droite, et aussi rendre la famille de polices courier et la taille de police 28, en gras. 

Maintenant, nous les utiliserons lorsque nous voulons montrer à l'utilisateur les résultats de la course. Donc, lorsque la couleur de la tortue gagnante est égale à la couleur user_bet, nous devons montrer le texte sur le canevas au lieu de l'imprimer dans le terminal. 

Pour ce faire, nous écrivons `turtle.write()` et collons l'instruction print avec font=**FONT** et align=**ALIGN**. Sinon, nous devons montrer le texte "Vous avez perdu" avec les mêmes variables **FONT** et **ALIGN**. Voyez, c'est l'avantage d'utiliser des variables globales.  

![Image](https://www.freecodecamp.org/news/content/images/2022/01/26.png)

Enfin, exécutons ce code une dernière fois. Disons que la tortue rouge sera la gagnante. Mais, comme vous pouvez le voir ci-dessous – Oups, la tortue jaune est la gagnante. Donc, vous pouvez voir la police jaune en gras affichée à côté de cette tortue. C'est pourquoi nous avons utilisé align = "right" et défini la couleur de la tortue en utilisant la méthode `turtle.pencolor()`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/turtle-overview.gif)
_Projet de jeu de course de tortues_

Et voilà - nous avons construit notre jeu de course de tortues. Si vous voulez regarder ce tutoriel sous forme de vidéo, voici un tutoriel vidéo complet pour vous :

## 📹 Tutoriel vidéo complet

%[https://youtu.be/_XmPt7iZtho]

## 👋 Conclusion

Donc, nous sommes à la fin de ce projet de jeu de course. Si vous avez aimé cet article, n'hésitez pas à vous abonner à ma [Chaîne YouTube](https://www.youtube.com/c/programmingwithshahan) ou à m'envoyer un [tweet](https://www.twitter.com/codewithshahan). 

Bon codage !