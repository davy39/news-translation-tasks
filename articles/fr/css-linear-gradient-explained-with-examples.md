---
title: CSS Linear Gradient Expliqué avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/css-linear-gradient-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cfc740569d1a4ca3543.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: toothbrush
  slug: toothbrush
seo_title: CSS Linear Gradient Expliqué avec des Exemples
seo_desc: 'In a linear gradient, the colors flow in a single direction, for example
  from left to right, top to bottom, or any angle you choose.


  A linear gradient with two color stops

  Syntax

  To create a linear gradient you must define at least two color stops. ...'
---

Dans un dégradé linéaire, les couleurs s'écoulent dans une seule direction, par exemple de gauche à droite, de haut en bas, ou selon n'importe quel angle que vous choisissez.

![Un dégradé avec deux arrêts de couleur](https://cdn.discordapp.com/attachments/261391445074771978/371707961422118912/image.png)
_Un dégradé linéaire avec deux arrêts de couleur_

## Syntaxe

Pour créer un dégradé linéaire, vous devez définir au moins deux arrêts de couleur. Ce sont les couleurs parmi lesquelles les transitions sont créées. Il est déclaré sur les propriétés **background** ou **background-image**.

```text
background: linear-gradient(direction, couleur-arrêt1, couleur-arrêt2, ...);
```

Si aucune direction n'est spécifiée, la transition par défaut est de haut en bas.

## Exemples

### De haut en bas :

```text
background: linear-gradient(red, yellow);
```

![De haut en bas](https://cdn.discordapp.com/attachments/261391445074771978/371702268803809301/image.png)

**De gauche à droite :**

Pour le faire de gauche à droite, vous ajoutez un paramètre supplémentaire au début de la fonction `linear-gradient()` commençant par le mot **to** qui indique la direction :

```text
background: linear-gradient(to right, red, yellow);
```

![De gauche à droite](https://cdn.discordapp.com/attachments/261391445074771978/371702990161051648/image.png)

**Dég**radés diagonaux** :

Vous pouvez également faire une transition de dégradé en diagonale en spécifiant les positions de départ horizontales et verticales, par exemple, en haut à gauche ou en bas à droite.

Voici un exemple pour un dégradé commençant en haut à gauche :

```text
background: linear-gradient(to bottom right, red, yellow);
```

![En haut à gauche](https://cdn.discordapp.com/attachments/261391445074771978/371705382105776128/image.png)

### **Utilisation d'angles pour spécifier la direction du dégradé**

Vous pouvez également utiliser des angles pour être plus précis dans la spécification de la direction du dégradé :

```text
background: linear-gradient(angle, couleur-arrêt1, couleur-arrêt2);
```

L'angle est spécifié comme un angle entre une ligne horizontale et la ligne de dégradé.

```text
background: linear-gradient(90deg, red, yellow);
```

![90 degrés](https://cdn.discordapp.com/attachments/261391445074771978/371710718698848256/image.png)

### **Utilisation de plus de deux couleurs**

Vous n'êtes pas limité à seulement deux couleurs – vous pouvez utiliser autant de couleurs séparées par des virgules que vous le souhaitez.

```text
background: linear-gradient(red, yellow, green);
```

![Un dégradé avec 3 arrêts de couleur](https://cdn.discordapp.com/attachments/261391445074771978/371706534591201281/image.png)

Vous pouvez également utiliser d'autres syntaxes de couleur comme RGB ou des codes hexadécimaux pour spécifier les couleurs.

### **Arrêts de couleur nets**

Vous pouvez non seulement utiliser des dégradés pour des transitions avec des couleurs qui s'estompent, mais aussi pour changer d'une couleur unie à une autre couleur unie instantanément :

```text
background: linear-gradient(to right, red 15%, yellow 15%);
```

![Arrêts de couleur nets](https://cdn.discordapp.com/attachments/261391445074771978/371716730046775318/image.png)

## Plus d'informations :

* [The CSS Handbook: a handy guide to CSS for developers](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/)