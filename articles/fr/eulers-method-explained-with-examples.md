---
title: La méthode d'Euler expliquée avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T18:49:00.000Z'
originalURL: https://freecodecamp.org/news/eulers-method-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d81740569d1a4ca3821.jpg
tags:
- name: Math
  slug: math
- name: toothbrush
  slug: toothbrush
seo_title: La méthode d'Euler expliquée avec des exemples
seo_desc: 'What is Euler’s Method?

  The Euler’s method is a first-order numerical procedure for solving ordinary differential
  equations (ODE) with a given initial value.

  The General Initial Value Problem


  Methodology

  Euler’s method uses the simple formula,


  to c...'
---

# **Qu'est-ce que la méthode d'Euler ?**

La méthode d'Euler est une procédure numérique de premier ordre pour résoudre les équations différentielles ordinaires (EDO) avec une valeur initiale donnée.

## **Le problème général de la valeur initiale**

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn006.png)

## **Méthodologie**

La méthode d'Euler utilise la formule simple,

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn3.png)

pour construire la tangente au point `x` et obtenir la valeur de `y(x+h)`, dont la pente est,

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn008.png)

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/Euler.png)

Dans la méthode d'Euler, vous pouvez approximer la courbe de la solution par la tangente dans chaque intervalle (c'est-à-dire par une séquence de courts segments de ligne), à des étapes de `h`.

_En général_, si vous utilisez une petite taille de pas, la précision de l'approximation augmente.

## **Formule générale**

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn7.png)

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn_new_2.png)

## **Valeur fonctionnelle à un point quelconque `b`, donnée par `y(b)`**

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn6.png)

où,

* **n** = nombre d'étapes
* **h** = largeur de l'intervalle (taille de chaque étape)

### **Pseudocode**

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn_new_1.png)

## **Exemple**

Trouver `y(1)`, donné

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/eqn007.png)

En résolvant analytiquement, la solution est _**y = e<sup>x</sup>**_ et `y(1)`= `2.71828`. (Note : Cette solution analytique est juste pour comparer la précision.)

En utilisant la méthode d'Euler, en considérant `h` = `0.2`, `0.1`, `0.01`, vous pouvez voir les résultats dans le diagramme ci-dessous.

![Image](https://raw.githubusercontent.com/pranabendra/articles/master/Euler-method/images/comparison.png)

Quand `h` = `0.2`, `y(1)` = `2.48832` (erreur = 8.46 %)

Quand `h` = `0.1`, `y(1)` = `2.59374` (erreur = 4.58 %)

Quand `h` = `0.01`, `y(1)` = `2.70481` (erreur = 0.50 %)

Vous pouvez remarquer comment la précision s'améliore lorsque les pas sont petits.