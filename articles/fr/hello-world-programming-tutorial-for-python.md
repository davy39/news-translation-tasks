---
title: Tutoriel de programmation Hello World pour Python
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-09-16T15:33:08.000Z'
originalURL: https://freecodecamp.org/news/hello-world-programming-tutorial-for-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Article-Image-Hello-World.png
tags:
- name: beginner
  slug: beginner
- name: beginners guide
  slug: beginners-guide
- name: coding
  slug: coding
- name: Python
  slug: python
seo_title: Tutoriel de programmation Hello World pour Python
seo_desc: "\U0001F539 Hello, World!\nHi! if you are reading this article, then you\
  \ are probably starting to dive into the amazing world of programming and computer\
  \ science. That's great. \nIn this article, you will learn:\n\nHow to write your\
  \ first \"Hello, World!\" program ..."
---

## 💡 Bonjour, le monde !

Salut ! Si vous lisez cet article, alors vous commencez probablement à plonger dans le monde passionnant de la programmation et de l'informatique. C'est génial. 

Dans cet article, vous apprendrez :

* Comment écrire votre premier programme `"Bonjour, le monde !"` en Python.
* Comment enregistrer votre code dans un fichier Python.
* Comment exécuter votre code.

Écrire ce programme lorsque vous commencez à apprendre à coder est une tradition dans la communauté des développeurs. 

Profitez de ce moment car il fera définitivement partie de vos souvenirs dans les mois et les années à venir lorsque vous vous souviendrez de vos premiers pas. 

Commençons.

## 💡 "Bonjour, le monde !" dans le shell Python 

### Étape 1 : Démarrer IDLE

Au cours de cet article, nous travaillerons avec [IDLE](https://docs.python.org/3/library/idle.html) (Python's Integrated Development and Learning Environment), qui est automatiquement installé lorsque vous installez Python. C'est là que vous écrirez et exécuterez votre code Python. 

La première chose que vous devez faire est d'ouvrir IDLE. Vous verrez immédiatement l'écran montré ci-dessous. 

Cela s'appelle le shell Python (interpréteur interactif). C'est une fenêtre interactive où vous pouvez entrer des lignes ou des blocs de code et les exécuter immédiatement pour voir leur effet et leur sortie. 

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-92.png)

**💡 Astuce :** Par défaut, vous verrez une taille de police plus petite. Vous pouvez la personnaliser dans "Options > Configure IDLE".

### Étape 2 : Afficher le message

Vous devez indiquer au programme que vous souhaitez afficher un message spécifique en écrivant la ligne de code appropriée. 

En Python, nous utilisons `print()` pour cela :

* D'abord, nous écrivons `print`.
* Ensuite, entre parenthèses, nous écrivons le message ou la valeur que nous voulons afficher.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-182.png)

**💡 Astuce :** Le message `"Bonjour, le monde !"` est entouré de guillemets doubles car il est représenté comme une `chaîne de caractères`, un type de données utilisé pour représenter des séquences de caractères dans votre code (par exemple, du texte). 

### Étape 3 : Voir la sortie

Vous verrez la sortie suivante si vous écrivez cette ligne de code dans le shell Python et appuyez sur entrée :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-89.png)

**💡 Astuce :** Vous remarquerez que la couleur du message à l'intérieur de `print()` passe au vert lorsque vous ajoutez le dernier guillemet. 

Cela se produit parce que IDLE attribue différentes couleurs aux différents types d'éléments que vous pouvez écrire dans votre code (remarquez que `print` est affiché en violet). Cela s'appelle "la coloration syntaxique".

Super ! Vous venez d'écrire votre premier programme `"Bonjour, le monde !"` en Python. 

Si vous souhaitez l'enregistrer afin de l'exécuter plus tard (ou simplement pour le garder comme un bon souvenir de votre premier programme Python !), vous devrez créer un fichier Python, alors voyons comment vous pouvez faire cela. 

## 💡 "Bonjour, le monde !" dans un fichier Python

### Étape 1 : Créer un fichier

Pour créer un fichier Python dans IDLE, vous devez :

* Ouvrir le shell Python.
* Cliquer sur `Fichier` dans la barre d'outils.
* Cliquer sur `Nouveau fichier`.

**💡 Astuces :** Vous pouvez également utiliser le raccourci clavier `Ctrl + N`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-188.png)

Après avoir cliqué sur `Nouveau fichier`, vous verrez immédiatement un nouveau fichier où vous pouvez écrire votre code :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-190.png)
_Nouveau fichier affiché_

### Étape 2 : Écrire le code

Dans le nouveau fichier, écrivez cette ligne de code pour afficher `"Bonjour, le monde !"` :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-191.png)

**💡 Astuce :** La ligne verticale noire épaisse montre où se trouve actuellement le curseur. 

### Étape 3 : Enregistrer le fichier

Enregistrez le nouveau fichier en cliquant sur **Fichier > Enregistrer** ou en utilisant le raccourci clavier `Ctrl + S`. Vous devrez écrire un nom pour votre fichier et choisir où vous souhaitez l'enregistrer. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-192.png)

Après avoir enregistré le fichier, vous verrez quelque chose de très similaire à ceci dans le dossier que vous avez sélectionné :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-195.png)

**💡 Astuces :** Par défaut, les numéros de ligne ne seront pas affichés dans le fichier. Si vous souhaitez les afficher (comme dans les images ci-dessus), allez dans Options > Configure IDLE > Général > Cochez la case "Afficher les numéros de ligne dans les nouvelles fenêtres".

### Étape 4 : Exécuter le programme

Maintenant, vous pouvez exécuter votre fichier en cliquant sur **Exécuter > Exécuter le module** :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-93.png)

Une nouvelle fenêtre s'ouvrira et vous devriez voir la sortie de votre programme en bleu :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-97.png)

Maintenant, votre programme est en sécurité dans un fichier Python et vous pouvez l'exécuter chaque fois que vous en avez besoin.

**Excellent travail !** 

## 💡 Personnalisez votre programme

Vous pouvez personnaliser votre programme pour le rendre unique. Vous devez simplement modifier le fichier Python et changer la chaîne de caractères. 

Par exemple, vous pouvez ajouter votre nom après `Bonjour, le monde !` :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-99.png)

Si vous exécutez le fichier, vous verrez la chaîne de caractères affichée dans le shell Python :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-96.png)

## 💡 Premier programme Python terminé

Excellent travail. Vous venez d'écrire votre premier programme Python. 

La programmation et l'informatique seront clés pour l'avenir de l'humanité. En apprenant à coder, vous pouvez façonner cet avenir. 

Vous créerez des produits et des plateformes incroyables, et vous nous aiderez à faire un pas de plus vers un monde où la technologie fera partie de chaque aspect de notre vie quotidienne.

Pour en savoir plus sur les utilisations de la programmation avec Python, vous pourriez aimer lire mon article "[À quoi sert Python ? 10+ utilisations de codage pour le langage de programmation Python](https://www.freecodecamp.org/news/what-is-python-used-for-10-coding-uses-for-the-python-programming-language/)" 

**J'espère vraiment que vous avez aimé mon article** et que vous l'avez trouvé utile. Suivez-moi sur Twitter [@EstefaniaCassN](https://twitter.com/EstefaniaCassN) et [découvrez mes cours en ligne.](https://www.udemy.com/user/estefania-cn/) ⭐️