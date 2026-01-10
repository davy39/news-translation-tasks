---
title: Comment générer des nombres entiers aléatoires dans une plage en utilisant
  JavaScript Math.floor - Résolu
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2019-11-28T18:02:00.000Z'
originalURL: https://freecodecamp.org/news/generate-random-whole-numbers-within-a-range-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ef9740569d1a4ca4026.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
seo_title: Comment générer des nombres entiers aléatoires dans une plage en utilisant
  JavaScript Math.floor - Résolu
seo_desc: "Quick Solution\nfunction randomRange(myMin, myMax) {\n  return Math.floor(Math.random()\
  \ * (myMax - myMin + 1) + myMin);\n}\n\nCode Explanation\n\nMath.random() generates\
  \ our random number between 0 and ≈ 0.9.\nBefore multiplying it, it resolves the\
  \ part betw..."
---

## Solution rapide

```javascript
function randomRange(myMin, myMax) {
  return Math.floor(Math.random() * (myMax - myMin + 1) + myMin);
}

```

## Explication du code

* `Math.random()` génère notre nombre aléatoire entre 0 et ≈ 0.9.
* Avant de le multiplier, il résout la partie entre parenthèses `(myMax - myMin + 1)` grâce à l'opérateur de regroupement `(   )`.
* Le résultat de cette multiplication est suivi de l'ajout de `myMin` puis "arrondi" à l'entier le plus grand inférieur ou égal à celui-ci (ex: 9.9 donnerait 9)

Si les valeurs étaient `myMin = 1, myMax = 10`, un résultat pourrait être le suivant :

1. `Math.random() = 0.8244326990411024`
2. `(myMax - myMin + 1) = 10 - 1 + 1 -> 10`
3. `a * b =  8.244326990411024`
4. `c + myMin = 9.244326990411024`
5. `Math.floor(9.244326990411024) = 9`

`randomRange` doit utiliser à la fois `myMax` et `myMin`, et retourner un nombre aléatoire dans votre plage.

Vous ne pouvez pas passer le test si vous réutilisez simplement la fonction `ourRandomRange` dans votre formule `randomRange`. Vous devez écrire votre propre formule qui utilise les variables `myMax` et `myMin`. Cela fera le même travail qu'en utilisant `ourRandomRange`, mais garantit que vous avez compris les principes des fonctions `Math.floor()` et `Math.random()`.