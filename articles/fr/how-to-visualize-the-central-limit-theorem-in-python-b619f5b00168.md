---
title: Comment visualiser le Théorème Central Limite en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-12T17:58:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-visualize-the-central-limit-theorem-in-python-b619f5b00168
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0qzlGif4QwGXcRI2jcJHag.gif
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: statistics
  slug: statistics
seo_title: Comment visualiser le Théorème Central Limite en Python
seo_desc: 'By Rohan Joseph

  The Central Limit Theorem states that the sampling distribution of the sample means
  approaches a normal distribution as the sample size gets larger.


  The sample means will converge to a normal distribution regardless of the shape
  of t...'
---

Par Rohan Joseph

Le Théorème Central Limite stipule que la distribution d'échantillonnage des moyennes d'échantillon approche une distribution normale à mesure que la taille de l'échantillon augmente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0qzlGif4QwGXcRI2jcJHag.gif)

Les moyennes des échantillons convergeront vers une distribution normale, quelle que soit la forme de la population. C'est-à-dire que la population peut être positivement ou négativement asymétrique, normale ou non normale.

Le Théorème Central Limite est étroitement lié à la Loi des Grands Nombres, qui stipule que :

> **_à mesure qu'une taille d'échantillon augmente, la moyenne de l'échantillon se rapproche de la moyenne de la population._**

Alors, comment ces deux concepts sont-ils liés ?

Le TCL stipule que — à mesure que la taille de l'échantillon tend vers l'infini, la forme de la distribution ressemble à une courbe en cloche (distribution normale). Le centre de cette distribution des moyennes d'échantillon devient très proche de la moyenne de la population — ce qui est essentiellement la loi des grands nombres.

Illustrons cela en Python avec le classique lancer de dé. Avant de simuler, calculons la valeur attendue d'un lancer de dé.

> _Une valeur attendue est la moyenne des résultats d'une expérience après un grand nombre d'essais._

Voici la formule générale pour calculer une valeur attendue d'une expérience (qui a 6 résultats et 6 probabilités associées).

![Image](https://cdn-media-1.freecodecamp.org/images/1*MrP5yPSiW6frajEopSzKmw.png)

Alors, calculons maintenant la valeur attendue d'un lancer de dé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7BVJPDbH1kwZoBu-QsEjCg.png)

Même s'il est impossible d'obtenir un 3,5 en un seul lancer de dé, avec une augmentation du nombre de lancers de dé, la moyenne des lancers de dé serait proche de 3,5.

1. Pour visualiser cela en Python, importez d'abord les bibliothèques nécessaires : numpy, matplotlib, et [wand](http://docs.wand-py.org/en/0.4.1/guide/install.html). Assurez-vous d'installer [ImageMagick](https://www.imagemagick.org/script/install-source.php) pour sauvegarder les graphiques sous forme de gif.

2. Maintenant, créez 1000 simulations de 10 lancers de dé, et dans chaque simulation, trouvez la moyenne du résultat du dé.

Voici à quoi ressembleraient les 10 premières valeurs attendues du lancer de dé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vGwpzGW6RbPb4-h3smMdMg.png)

3. Écrivez une fonction pour tracer un histogramme des valeurs générées ci-dessus. De plus, en utilisant la fonction d'animation, nous pouvons visualiser comment l'histogramme ressemble lentement à une distribution normale.

**Sortie :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*RRyWvTmmtKN-SE0jReGgLw.gif)

4. Vous pouvez sauvegarder l'animation sous forme de gif en utilisant le morceau de code suivant.

De cette expérience, nous pouvons observer :

1. Avec un nombre plus petit d'échantillons, l'histogramme est dispersé partout et n'a pas de motif défini.
2. Cependant, en augmentant la taille de l'échantillon, la distribution d'échantillonnage commence à ressembler à une distribution normale. C'est le **Théorème Central Limite.**
3. De plus, avec une augmentation de la taille de l'échantillon, la fréquence pour "moyenne du lancer de dé = 3,5" est la plus élevée — ce qui est la valeur attendue d'un lancer de dé. Cela démontre la **Loi des Grands Nombres.**

Alors, comment le Théorème Central Limite est-il utilisé ?

> _Il nous permet de tester l'hypothèse de savoir si notre échantillon représente une population distincte de la population connue. Nous pouvons prendre une moyenne d'un échantillon et la comparer avec la distribution d'échantillonnage pour estimer la probabilité que l'échantillon provienne de la population connue._

Connectez-vous sur [LinkedIn](https://www.linkedin.com/feed/) et consultez GitHub (ci-dessous) pour le notebook complet.

[**rohanjoseph93/Central-Limit-Theorem**](https://github.com/rohanjoseph93/Central-Limit-Theorem/blob/master/Central%20Limit%20Theorem.ipynb)  
[_Visualisez le TCL en Python. Contribuez au développement de rohanjoseph93/Central-Limit-Theorem en créant un compte sur
…_github.com](https://github.com/rohanjoseph93/Central-Limit-Theorem/blob/master/Central%20Limit%20Theorem.ipynb)