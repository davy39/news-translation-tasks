---
title: Comment utiliser PyCharm pour déboguer votre code Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T16:02:46.000Z'
originalURL: https://freecodecamp.org/news/debugging-with-pycharm-be282bcd6172
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gx9zzO6SmaEn8btnqGxhGw.png
tags:
- name: coding
  slug: coding
- name: debugging
  slug: debugging
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment utiliser PyCharm pour déboguer votre code Python
seo_desc: 'By Ori Roza

  Debugging code in any language might be frustrating, but it is especially so in
  Python where we cannot recognize a bug immediately.

  In addition, Python provides us with the PDB library as a tool for debugging, which
  can also be difficult ...'
---

Par Ori Roza

Le débogage de code dans n'importe quel langage peut être frustrant, mais c'est particulièrement vrai en Python où nous ne pouvons pas reconnaître un bug immédiatement.

De plus, Python nous fournit la bibliothèque PDB comme outil de débogage, qui peut également être difficile à manipuler.

Heureusement, nous avons l'IDE PyCharm. Il utilise PyDev et nous offre une nouvelle expérience de débogage !

Dans cet article, je vais passer en revue les principales fonctionnalités de débogage les plus utiles que PyCharm a à offrir et vous apprendre à les utiliser efficacement.

### **Points d'arrêt**

Les points d'arrêt peuvent être inutiles lorsque nous sommes confrontés à un bug qui se produit dans certaines conditions.

De plus, lorsque nous en avons beaucoup, c'est un vrai désordre.

Heureusement, PyCharm nous donne la possibilité de gérer les points d'arrêt de manière efficace :

1. Appuyez sur Ctrl+Shift+F8 (ou Exécuter->Voir les points d'arrêt)
2. Tous les points d'arrêt que nous avons définis dans le projet seront listés comme montré ci-dessous (voir 1)

![Image](https://cdn-media-1.freecodecamp.org/images/IHZir8fKIXc1VaiKH5CGgCkTd5vL-oD0mBhX)

3. Comme nous pouvons le voir, pour chaque point d'arrêt, nous pouvons définir une condition qui déclenchera le point d'arrêt (voir 2)

4. De plus, nous pouvons définir une condition très spéciale qui contrôle si le point d'arrêt sera déclenché lorsqu'une exception se produit (voir 3) dans deux états différents :

a. À la terminaison (après la fin du script)

b. À la levée (avant la fin du script)

![Image](https://cdn-media-1.freecodecamp.org/images/SJGgsckNaq4mVIilo6VIxgdDQqWssYOVUwGa)

### **Attacher à des processus locaux**

Vous êtes-vous déjà demandé s'il était possible de déboguer un processus distant ?

**Oui, vous pouvez !** (et c'est si facile !)

Que vous exécutiez d'autres processus en arrière-plan ou que vous les créiez dans le cadre du flux, PyCharm vous offre un moyen très efficace de déboguer des processus distants :

1. Comme montré ci-dessous, ouvrez Exécuter->Attacher à un processus local

![Image](https://cdn-media-1.freecodecamp.org/images/oI2Ghz8BzkjVL0eVIio1sQ6U0AUVXzQ1Nw-k)

2. Maintenant, choisissez le processus Python que vous souhaitez déboguer :

![Image](https://cdn-media-1.freecodecamp.org/images/jiRdyqnMR6OkAL2eHmmNugs3Q3bxrPHY5ptz)

3. Ensuite, le processus que vous avez choisi sera débogué dans PyCharm :

![Image](https://cdn-media-1.freecodecamp.org/images/lvUB8VZzwEh8qGMO1IaJYJsfxM6vYhU4utBP)

### **Interpréteur Python avec l'environnement chargé**

Effectuer des calculs et manipuler les variables du code actuellement débogué fait gagner du temps et nous permet d'apporter des modifications dans un véritable bac à sable !

PyCharm nous fournit un interpréteur Python avec l'environnement chargé.

1. Dans l'onglet console, appuyez sur le bouton marqué :

![Image](https://cdn-media-1.freecodecamp.org/images/mNjPxZPfvIRxBgiGUy4KJE0DqSiFsP28vkhb)

2. Comme vous pouvez le voir ci-dessous, l'interpréteur reconnaît nos variables !

![Image](https://cdn-media-1.freecodecamp.org/images/gmMkT9W-rclIcNk0gT7zuPJu40ubqLQOkHez)

### **Conclusion**

PyCharm nous offre de nombreux outils fantastiques, et ce débogueur en fait partie.

Le débogage peut parfois être difficile, mais si vous utilisez les bons outils, cela peut être plus facile et même amusant !

J'espère que cet article vous a appris quelque chose de nouveau, et j'attends avec impatience vos retours. S'il vous plaît, dites-moi — était-ce utile pour vous ?