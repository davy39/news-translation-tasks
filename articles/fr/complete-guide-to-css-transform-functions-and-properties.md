---
title: Guide complet des fonctions et propriétés de transformation CSS
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2023-06-19T21:13:33.000Z'
originalURL: https://freecodecamp.org/news/complete-guide-to-css-transform-functions-and-properties
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738338625918/27521e84-35de-4453-a153-1d419e1d0e2b.png
tags:
- name: code
  slug: code
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Guide complet des fonctions et propriétés de transformation CSS
seo_desc: 'CSS transform allows you to translate, rotate, skew, scale, or add perspective
  effects to HTML elements.

  This tutorial discusses everything you need to know to transform HTML elements like
  a pro.

  Table of Contents


  What is the CSS transform Property?...'
---

**La transformation CSS** permet de translater, faire pivoter, incliner, redimensionner ou ajouter des effets de perspective aux éléments HTML.

Ce tutoriel aborde tout ce que vous devez savoir pour transformer des éléments HTML comme un professionnel.

## Table des matières

1. [Qu'est-ce que la propriété CSS `transform` ?](#heading-quest-ce-que-la-propriete-css-transform)
    
2. [Qu'est-ce que la fonction CSS `rotate()` ?](#heading-quest-ce-que-la-fonction-css-rotate)
    
3. [Qu'est-ce que la fonction CSS `rotateX()` ?](#heading-quest-ce-que-la-fonction-css-rotatex)
    
4. [Qu'est-ce que la fonction CSS `rotateY()` ?](#heading-quest-ce-que-la-fonction-css-rotatey)
    
5. [Qu'est-ce que la fonction CSS `rotateZ()` ?](#heading-quest-ce-que-la-fonction-css-rotatez)
    
6. [Qu'est-ce que la fonction CSS `rotate3d()` ?](#heading-quest-ce-que-la-fonction-css-rotate3d)
    
7. [Fonctions de rotation CSS vs. propriété `rotate` : Quelle est la différence ?](#heading-fonctions-de-rotation-css-vs-propriete-rotate-quelle-est-la-difference)
    
8. [Qu'est-ce que la fonction CSS `scale()` ?](#heading-quest-ce-que-la-fonction-css-scale)
    
9. [Fonction CSS `scale()` vs. propriété `scale` : Quelle est la différence ?](#heading-fonction-css-scale-vs-propriete-scale-quelle-est-la-difference)
    
10. [Qu'est-ce que la fonction CSS `scaleZ()` ?](#heading-quest-ce-que-la-fonction-css-scalez)
    
11. [Qu'est-ce que la fonction CSS `scale3d()` ?](#heading-quest-ce-que-la-fonction-css-scale3d)
    
12. [Qu'est-ce que la fonction CSS `skew()` ?](#heading-quest-ce-que-la-fonction-css-skew)
    
13. [Qu'est-ce que la fonction CSS `translate()` ?](#heading-quest-ce-que-la-fonction-css-translate)
    
14. [Qu'est-ce que la fonction CSS `translateZ()` ?](#heading-quest-ce-que-la-fonction-css-translatez)
    
15. [Qu'est-ce que la fonction CSS `translate3d()` ?](#heading-quest-ce-que-la-fonction-css-translate3d)
    
16. [Fonctions de translation CSS vs. propriété `translate` : Quelle est la différence ?](#heading-fonctions-de-translation-css-vs-propriete-translate-quelle-est-la-difference)
    
17. [Qu'est-ce que la fonction CSS `perspective()` ?](#heading-quest-ce-que-la-fonction-css-perspective)
    
18. [Fonction CSS `perspective()` vs. propriété `perspective` : Quelle est la différence ?](#heading-fonction-css-perspective-vs-propriete-perspective-quelle-est-la-difference)
    
19. [Qu'est-ce que la fonction CSS `matrix()` ?](#heading-quest-ce-que-la-fonction-css-matrix)
    
20. [Pourquoi l'ordre des fonctions de transformation CSS est-il important ?](#heading-pourquoi-lordre-des-fonctions-de-transformation-css-est-il-important)
    
21. [Outils pour convertir les fonctions de transformation en `matrix()`](#heading-outils-pour-convertir-les-fonctions-de-transformation-en-matrix)
    
22. [Choses importantes à savoir sur la transformation des éléments en CSS](#heading-choses-importantes-a-savoir-sur-la-transformation-des-elements-en-css)
    
23. [Conclusion](#heading-conclusion)
    

Alors, sans plus attendre, discutons de la propriété CSS `transform`.

## Qu'est-ce que la propriété CSS `transform` ?

La propriété CSS `transform` spécifie l'effet de transformation que vous souhaitez appliquer à un élément HTML.

**Voici la syntaxe :**

```css
html-element {
  transform: valeur;
}
```

La propriété CSS `transform` accepte les valeurs suivantes :

* `inherit` : Transforme l'élément avec la valeur `transform` de son élément parent.
    
* `initial` : Transforme l'élément HTML avec sa valeur `transform` par défaut.
    
* `matrix()` : Transforme l'élément en deux dimensions avec une matrice de six valeurs.
    
* `matrix3d()` : Transforme l'élément HTML en trois dimensions avec une matrice 4x4 de seize valeurs.
    
* `none` : N'applique *aucune* transformation à l'élément HTML.
    
* `perspective()` : Transforme un élément 3D transformé avec une vue en perspective.
    
* `rotate()` : Transforme l'élément en le faisant pivoter en deux dimensions.
    
* `rotate3d()` : Transforme l'élément en le faisant pivoter en trois dimensions.
    
* `rotateX()` : Transforme l'élément en le faisant pivoter en trois dimensions le long de l'axe X.
    
* `rotateY()` : Transforme l'élément en le faisant pivoter en trois dimensions le long de l'axe Y.
    
* `rotateZ()` : Transforme l'élément HTML en le faisant pivoter en trois dimensions le long de l'axe Z.
    
* `scale()` : Transforme l'élément en le redimensionnant en deux dimensions.
    
* `scale3d()` : Transforme l'élément en le redimensionnant en trois dimensions.
    
* `scaleX()` : Transforme l'élément en le redimensionnant le long de l'axe X.
    
* `scaleY()` : Transforme l'élément en le redimensionnant le long de l'axe Y.
    
* `scaleZ()` : Transforme l'élément HTML en le redimensionnant en trois dimensions le long de l'axe Z.
    
* `skew()` : Transforme l'élément en l'inclinant en deux dimensions le long des axes X et Y.
    
* `skewX()` : Transforme l'élément en l'inclinant en deux dimensions le long de l'axe X.
    
* `skewY()` : Transforme l'élément en l'inclinant en deux dimensions le long de l'axe Y.
    
* `translate()` : Transforme l'élément HTML en le déplaçant (translatant) en deux dimensions.
    
* `translate3d()` : Transforme l'élément en le déplaçant en trois dimensions.
    
* `translateX()` : Transforme l'élément en le déplaçant le long de l'axe X.
    
* `translateY()` : Transforme l'élément en le déplaçant le long de l'axe Y.
    
* `translateZ()` : Transforme l'élément en le déplaçant en trois dimensions le long de l'axe Z.
    

**Note :** La propriété `transform` accepte une ou plusieurs [fonctions de transformation CSS](https://codesweetly.com/web-tech-terms-c#css-transform-functions). Par exemple, voici une déclaration `transform` valide :

```css
div {
  transform: perspective(370px) scaleZ(5) rotate(17deg);
}
```

Dans l'extrait ci-dessus, nous avons assigné trois fonctions de transformation à la propriété `transform`. Parlons davantage de certaines des valeurs de `transform`.

## Qu'est-ce que la fonction CSS `rotate()` ?

`rotate()` transforme un élément en le faisant pivoter en deux dimensions autour d'un point fixe.

**Note :**

* "Origine de la transformation" est le point fixe autour duquel un élément pivote.
    
* Vous pouvez définir le point fixe de votre élément en utilisant la propriété CSS [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin). Mais la valeur par défaut est `center`.
    

### Syntaxe de la fonction CSS `rotate()`

`rotate()` accepte un seul [argument](https://codesweetly.com/javascript-arguments-vs-parameters). Voici la syntaxe :

```css
element {
  transform: rotate(angle);
}
```

**Notez ce qui suit :**

* La fonction `rotate(angle)` est équivalente à `rotate3d(0, 0, 1, angle)` ou `rotateZ(angle)`.
    
* L'argument `angle` spécifie l'angle de rotation de l'élément.
    
* `angle` peut être en [degrés](https://en.wikipedia.org/wiki/Degree_%28angle%29), [gradians](https://en.wikipedia.org/wiki/Gradian), [radians](https://en.wikipedia.org/wiki/Radian), ou [tours](https://en.wikipedia.org/wiki/Turn_%28angle%29).
    
* Un argument `angle` se compose d'un nombre suivi de l'unité que vous souhaitez utiliser, par exemple, `45deg`.
    
* La direction d'écriture de votre navigateur détermine la direction de rotation de l'élément.
    
* Un angle positif fera pivoter l'élément dans le sens des aiguilles d'une montre dans une direction d'écriture de gauche à droite. Mais un angle négatif effectuera une rotation dans le sens inverse des aiguilles d'une montre.
    
* Un angle positif fera pivoter l'élément dans le sens inverse des aiguilles d'une montre dans un contexte d'écriture de droite à gauche. Mais un angle négatif effectuera une rotation dans le sens des aiguilles d'une montre.
    

### Exemples de la fonction CSS `rotate()`

Voici quelques exemples de fonctionnement de la fonction CSS `rotate()`.

#### Comment effectuer une rotation de zéro degré en CSS :

```css
img {
  transform: rotate(0deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-zcgvaa?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotate()` pour spécifier une rotation de zéro degré (0°) pour l'élément image.

#### Comment effectuer une rotation de 45 degrés en CSS :

```css
img {
  transform: rotate(45deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-86xhmx?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotate()` pour spécifier une rotation de quarante-cinq degrés (45°) pour l'élément image.

#### Comment effectuer une rotation de moins soixante-dix degrés en CSS :

```css
img {
  transform: rotate(-70deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-3gb1my?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotate()` pour spécifier une rotation de moins soixante-dix degrés (70°) pour l'élément image.

## Qu'est-ce que la fonction CSS `rotateX()` ?

`rotateX()` transforme un élément en le faisant pivoter en trois dimensions autour de l'axe X.

![Illustration du système de coordonnées cartésiennes 3D](https://www.freecodecamp.org/news/content/images/2023/06/cartesian-coordinate-system-three-dimensional-diagram-codesweetly.png align="left")

*Un système de coordonnées cartésiennes tridimensionnel montrant les axes X, Y et Z*

### Syntaxe de la fonction CSS `rotateX()`

`rotateX()` accepte un seul argument. Voici la syntaxe :

```css
element {
  transform: rotateX(angle);
}
```

**Notez ce qui suit :**

* La fonction `rotateX(angle)` est équivalente à `rotate3d(1, 0, 0, angle)`.
    
* L'argument `angle` spécifie l'angle de rotation de l'élément.
    
* `angle` peut être en degré, gradian, radian ou tour.
    
* Un argument `angle` se compose d'un nombre suivi de l'unité que vous souhaitez utiliser, par exemple, `45deg`.
    

### Exemples de la fonction CSS `rotateX()`

Voici quelques exemples de fonctionnement de la fonction CSS `rotateX()`.

#### Comment effectuer une rotation de zéro degré autour de l'axe X :

```css
img {
  transform: rotateX(0deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ej9ent?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotateX()` pour spécifier une rotation de zéro degré (0°) pour l'image autour de l'axe X.

#### Comment effectuer une rotation de 70 degrés autour de l'axe X :

```css
img {
  transform: rotateX(70deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-fvhyjx?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotateX()` pour spécifier une rotation de soixante-dix degrés (70°) pour l'image autour de l'axe X.

## Qu'est-ce que la fonction CSS `rotateY()` ?

`rotateY()` transforme un élément en le faisant pivoter en trois dimensions autour de l'axe Y.

### Syntaxe de la fonction CSS `rotateY()`

`rotateY()` accepte un seul argument. Voici la syntaxe :

```css
element {
  transform: rotateY(angle);
}
```

**Notez ce qui suit :**

* La fonction `rotateY(angle)` est équivalente à `rotate3d(0, 1, 0, angle)`.
    
* L'argument `angle` spécifie l'angle de rotation de l'élément.
    
* `angle` peut être en degrés, gradians, radians ou tours.
    
* Un argument `angle` se compose d'un nombre suivi de l'unité que vous souhaitez utiliser, par exemple, `45deg`.
    

### Exemples de la fonction CSS `rotateY()`

Voici quelques exemples de fonctionnement de la fonction CSS `rotateY()`.

#### Comment effectuer une rotation de zéro degré autour de l'axe Y :

```css
img {
  transform: rotateY(0deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-frg3ks?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotateY()` pour spécifier une rotation de zéro degré (0°) pour l'image autour de l'axe Y.

#### Comment effectuer une rotation de 70 degrés autour de l'axe Y :

```css
img {
  transform: rotateY(70deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-yvydga?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotateY()` pour spécifier une rotation de soixante-dix degrés (70°) pour l'image autour de l'axe Y.

## Qu'est-ce que la fonction CSS `rotateZ()` ?

`rotateZ()` transforme un élément en le faisant pivoter en trois dimensions autour de l'axe Z.

### Syntaxe de la fonction CSS `rotateZ()`

`rotateZ()` accepte un seul argument. Voici la syntaxe :

```css
element {
  transform: rotateZ(angle);
}
```

**Notez ce qui suit :**

* La fonction `rotateZ(angle)` est équivalente à `rotate3d(0, 0, 1, angle)` ou `rotate(angle)`.
    
* L'argument `angle` spécifie l'angle de rotation de l'élément.
    
* `angle` peut être en degrés, gradians, radians ou tours.
    
* Un argument `angle` se compose d'un nombre suivi de l'unité que vous souhaitez utiliser, par exemple, `45deg`.
    

### Exemples de la fonction CSS `rotateZ()`

Voici quelques exemples de fonctionnement de la fonction CSS `rotateZ()`.

#### Comment effectuer une rotation de zéro degré autour de l'axe Z :

```css
img {
  transform: rotateZ(0deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ozqupq?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotateZ()` pour spécifier une rotation de zéro degré (0°) pour l'image autour de l'axe Z.

#### Comment effectuer une rotation de 70 degrés autour de l'axe Z :

```css
img {
  transform: rotateZ(70deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-g6qrwc?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotateZ()` pour spécifier une rotation de soixante-dix degrés (70°) pour l'image autour de l'axe Z.

## Qu'est-ce que la fonction CSS `rotate3d()` ?

`rotate3d()` transforme un élément en le faisant pivoter en trois dimensions autour des axes x, y et z.

### Syntaxe de la fonction CSS `rotate3d()`

`rotate3d()` accepte quatre arguments. Voici la syntaxe :

```css
element {
  transform: rotate3d(x, y, z, angle);
}
```

**Notez ce qui suit :**

* Les arguments `x`, `y` et `z` sont des nombres spécifiant les coordonnées x, y et z.
    
* Les coordonnées sont l'axe autour duquel l'élément va pivoter.
    
* L'argument `angle` spécifie l'angle de rotation de l'élément.
    
* `angle` peut être en degrés, gradians, radians ou tours.
    
* Un argument `angle` se compose d'un nombre suivi de l'unité que vous souhaitez utiliser, par exemple, `45deg`.
    

### Exemples de la fonction CSS `rotate3d()`

Voici quelques exemples de fonctionnement de la fonction CSS `rotate3d()`.

#### Comment effectuer une rotation de 70 degrés autour de l'axe Z :

```css
img {
  transform: rotate3d(0, 0, 1, 70deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-i6f9pr?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotate3d()` pour spécifier une rotation de soixante-dix degrés (70°) pour l'image autour de l'axe Z.

#### Comment effectuer une rotation de 70 degrés autour des axes X, Y et Z :

```css
img {
  transform: rotate3d(1, 1, 1, 70deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ctws81?file=style.css)

L'extrait ci-dessus a utilisé la fonction `rotate3d()` pour spécifier une rotation de soixante-dix degrés (70°) pour l'image autour des axes x, y et z.

## Fonctions de rotation CSS vs. propriété `rotate` : Quelle est la différence ?

Les fonctions de rotation CSS et la propriété CSS `rotate` offrent deux moyens similaires de spécifier des transformations de rotation.

Les principales différences entre les deux techniques de rotation sont les suivantes :

* La propriété CSS `rotate` permet de faire pivoter un élément sans utiliser la propriété CSS `transform`.
    
* La syntaxe de la propriété CSS `rotate` est plus courte que celle de son alternative fonctionnelle.
    
* La propriété CSS `rotate` vous évite de devoir mémoriser l'ordre spécifique pour positionner les [fonctions de transformation](https://codesweetly.com/web-tech-terms-c#css-transform-functions).
    
* Les navigateurs calculent la matrice des fonctions de transformation dans l'ordre où vous les avez assignées à la propriété CSS `transform`, de gauche à droite.
    
* Les navigateurs calculent la matrice des propriétés de transformation dans l'ordre suivant :
    
    1. `translate`
        
    2. `rotate`
        
    3. `scale`
        

Voici quelques exemples.

### Comment utiliser la propriété CSS `rotate` vs. la fonction pour effectuer une rotation de 45 degrés

```css
img {
  rotate: 45deg; /* Équivalent à une propriété transform: rotate(45deg) */
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-rdw9a5?file=style.css)

L'extrait ci-dessus a utilisé la propriété `rotate` pour spécifier une rotation de quarante-cinq degrés (45°) pour l'élément image.

### Comment utiliser la propriété CSS `rotate` vs. la fonction pour effectuer une rotation de 70 degrés autour de l'axe X

```css
img {
  rotate: x 70deg; /* Équivalent à une propriété transform: rotateX(70deg) */
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-pal1am?file=style.css)

L'extrait ci-dessus a utilisé la propriété `rotate` pour spécifier une rotation de soixante-dix degrés (70°) pour l'image autour de l'axe X.

### Comment utiliser la propriété CSS `rotate` vs. la fonction pour effectuer une rotation de 70 degrés autour de l'axe Y

```css
img {
  rotate: y 70deg; /* Équivalent à une propriété transform: rotateY(70deg) */
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ldnmfd?file=style.css)

L'extrait ci-dessus a utilisé la propriété `rotate` pour spécifier une rotation de soixante-dix degrés (70°) pour l'image autour de l'axe Y.

### Comment utiliser la propriété CSS `rotate` vs. la fonction pour effectuer une rotation de 70 degrés autour de l'axe Z

```css
img {
  rotate: z 70deg; /* Équivalent à une propriété transform: rotateZ(70deg) */
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-stf9ty?file=style.css)

L'extrait ci-dessus a utilisé la propriété `rotate` pour spécifier une rotation de soixante-dix degrés (70°) pour l'image autour de l'axe Z.

### Comment utiliser la propriété CSS `rotate` vs. la fonction pour effectuer une rotation de 70 degrés autour des axes X, Y et Z

```css
img {
  rotate: 1 1 1 70deg; /* Équivalent à une propriété transform: rotate3d(1, 1, 1, 70deg) */
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-qfflxq?file=style.css)

L'extrait ci-dessus a utilisé la propriété `rotate` pour spécifier une rotation de soixante-dix degrés (70°) pour l'image autour des axes x, y et z.

**Note :** Une valeur `none` indique aux navigateurs de *ne pas* faire pivoter l'élément sélectionné.

## Qu'est-ce que la fonction CSS `scale()` ?

`scale()` transforme un élément en le redimensionnant (en le mettant à l'échelle) en deux dimensions à partir d'un point fixe.

**Note :**

* "Origine de la transformation" est le point fixe à partir duquel l'ordinateur met à l'échelle un élément.
    
* Vous pouvez définir le point fixe de votre élément en utilisant la propriété CSS `transform-origin`. Mais la valeur par défaut est `center`.
    

### Syntaxe de la fonction CSS `scale()`

`scale()` accepte deux arguments. Voici la syntaxe :

```css
element {
  transform: scale(x, y);
}
```

**Notez ce qui suit :**

* L'argument `x` peut être un nombre ou un pourcentage. Il spécifie le facteur de mise à l'échelle de l'élément le long de l'axe x.
    
* L'argument `y` peut également être un nombre ou un pourcentage. Il définit le facteur de mise à l'échelle de l'élément le long de l'axe y.
    
* La valeur par défaut de l'axe Y est `x`. Par conséquent, si vous ne fournissez pas d'argument `y`, le navigateur utilise automatiquement la valeur de `x`.
    
* Supposons que `x` et `y` soient égaux. Dans ce cas, les navigateurs mettront à l'échelle votre élément uniformément et conserveront son rapport d'aspect.
    

![Illustration du système de coordonnées cartésiennes 2D](https://www.freecodecamp.org/news/content/images/2023/06/cartesian-coordinate-system-two-dimensional-diagram-codesweetly.png align="left")

*Un système de coordonnées cartésiennes bidimensionnel montrant les axes X et Y*

### Exemples de la fonction CSS `scale()`

Voici quelques exemples de fonctionnement de la fonction CSS `scale()`.

#### Comment mettre à l'échelle un élément uniformément le long des axes X et Y en CSS :

```css
img {
  transform: scale(0.3);
  transform-origin: left;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-k3d6nm?file=style.css)

L'extrait ci-dessus a utilisé la fonction `scale()` pour spécifier un facteur de mise à l'échelle de `0.3` pour l'élément image le long des axes X et Y.

**Note :**

* `scale(0.3)` est équivalent à `scale(0.3, 0.3)`.
    
* L'équivalence en pourcentage de `scale(0.3)` est `scale(30%)`.
    

#### Comment mettre à l'échelle un élément de manière non uniforme le long des axes X et Y en CSS :

```css
img {
  transform: scale(0.3, 65%);
  transform-origin: top left;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-fxjhwb?file=style.css)

L'extrait ci-dessus a utilisé la fonction `scale()` pour spécifier un facteur de mise à l'échelle de `0.3` pour l'image le long de l'axe X et `65%` le long de l'axe Y.

#### Comment mettre à l'échelle un élément uniquement le long de l'axe X :

```css
img {
  transform: scale(0.3, 1);
  transform-origin: top left;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-7mwvto?file=style.css)

L'extrait ci-dessus a utilisé la fonction `scale()` pour spécifier un facteur de mise à l'échelle de `0.3` pour l'image uniquement le long de l'axe X.

**Note :**

* Un facteur de mise à l'échelle de `1` ou `100%` indique aux navigateurs de *ne pas* appliquer d'effet de mise à l'échelle sur l'élément sélectionné.
    
* `scale(0.3, 1)` est équivalent à `scaleX(0.3)`.
    

#### Comment mettre à l'échelle un élément uniquement le long de l'axe Y :

```css
img {
  transform: scale(100%, 0.2);
  transform-origin: top left;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-i5yrt4?file=style.css)

L'extrait ci-dessus a utilisé la fonction `scale()` pour spécifier un facteur de mise à l'échelle de `0.2` pour l'image uniquement le long de l'axe Y.

**Note :**

* Un facteur de mise à l'échelle de `100%` ou `1` indique aux navigateurs de *ne pas* appliquer d'effet de mise à l'échelle sur l'élément sélectionné.
    
* `scale(100%, 0.2)` est équivalent à `scaleY(0.2)`.
    

## Fonction CSS `scale()` vs. propriété `scale` : Quelle est la différence ?

La fonction CSS `scale()` et la propriété CSS `scale` offrent deux moyens similaires de spécifier une transformation d'échelle.

Les principales différences entre les deux techniques de mise à l'échelle sont les suivantes :

* La propriété CSS `scale` permet de mettre à l'échelle un élément sans utiliser la propriété CSS `transform`.
    
* La syntaxe de la propriété CSS `scale` est plus courte que celle de son alternative fonctionnelle.
    
* La propriété CSS `scale` vous évite de devoir mémoriser l'ordre spécifique pour positionner les fonctions de transformation.
    
* Les navigateurs calculent la matrice des fonctions de transformation dans l'ordre où vous les avez assignées à la propriété CSS `transform`, de gauche à droite.
    
* Les navigateurs calculent la matrice des propriétés de transformation dans l'ordre suivant :
    
    1. `translate`
        
    2. `rotate`
        
    3. `scale`
        

**Voici un exemple :**

Utilisez la propriété CSS `scale` pour mettre à l'échelle un élément de manière non uniforme le long des axes X et Y.

```css
img {
  scale: 0.3 65%; /* Équivalent à une propriété transform: scale(0.3, 65%) */
  transform-origin: top left;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-exkib5?file=style.css)

L'extrait ci-dessus a utilisé la propriété `scale` pour spécifier un facteur de mise à l'échelle de `0.3` pour l'image le long de l'axe X et `65%` le long de l'axe Y.

**Note :** Une valeur `none` indique aux navigateurs de *ne pas* mettre à l'échelle l'élément sélectionné.

## Qu'est-ce que la fonction CSS `scaleZ()` ?

`scaleZ()` transforme un élément en le redimensionnant (en le mettant à l'échelle) en trois dimensions à partir d'un point fixe le long de l'axe z.

**Note :**

* "Origine de la transformation" est le point fixe à partir duquel l'ordinateur met à l'échelle un élément.
    
* Vous pouvez définir le point fixe de votre élément en utilisant la propriété CSS `transform-origin`. Mais la valeur par défaut est `center`.
    

### Syntaxe de la fonction CSS `scaleZ()`

`scaleZ()` accepte un seul argument. Voici la syntaxe :

```css
element {
  transform: scaleZ(nombre);
}
```

**Note :**

* La fonction `scaleZ(nombre)` est équivalente à `scale3d(1, 1, nombre)`.
    
* L'argument `nombre` spécifie le facteur de mise à l'échelle de l'élément le long de l'axe z.
    

### Exemples de la fonction CSS `scaleZ()`

Nous utilisons souvent `scaleZ()` avec d'autres fonctions CSS telles que `perspective()`, `translateZ()` et `rotateX()`. Voici quelques exemples.

#### Comment utiliser `scaleZ()` avec les fonctions CSS `perspective()` et `rotateX()` :

```css
img {
  transform: perspective(370px) scaleZ(5) rotateX(17deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-kqmccz?file=style.css)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons utilisé la fonction `perspective()` pour définir une distance de `370px` entre l'utilisateur et le [plan z=0](https://codesweetly.com/css-perspective-function#what-is-the-z0-plane).
    
2. La fonction `scaleZ()` spécifie un facteur de mise à l'échelle de `5` pour l'image le long de l'axe z.
    
3. Nous avons utilisé la fonction `rotateX()` pour faire pivoter l'image de dix-sept degrés (17°) autour de l'axe x.
    

**Note :**

* Listez `perspective()` en premier chaque fois que vous l'enchaînez avec d'autres [fonctions de transformation CSS](https://codesweetly.com/web-tech-terms-c#css-transform-functions). Sinon, les navigateurs pourraient transformer incorrectement l'élément sélectionné.
    
* Listez la fonction `scaleZ()` avant `rotateX()`. Sinon, le navigateur ne mettra *pas* à l'échelle l'élément.
    

#### Comment utiliser `scaleZ()` avec les fonctions CSS `perspective()` et `translateZ()` :

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(370px) scaleZ(5) translateZ(30px);
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-uyw767?file=style.css)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons utilisé la fonction `perspective()` pour définir une distance de `370px` entre l'utilisateur et le plan z=0.
    
2. La fonction `scaleZ()` spécifie un facteur de mise à l'échelle de `5` pour l'image le long de l'axe z.
    
3. Nous avons utilisé la fonction `translateZ()` pour repositionner la `second-image` à trente pixels (`30px`) de sa position d'origine le long de l'axe z.
    

## Qu'est-ce que la fonction CSS `scale3d()` ?

`scale3d()` transforme un élément en le redimensionnant (en le mettant à l'échelle) en trois dimensions à partir d'un point fixe le long des axes x, y et z.

**Note :**

* "Origine de la transformation" est le point fixe à partir duquel l'ordinateur met à l'échelle un élément.
    
* Vous pouvez définir le point fixe de votre élément en utilisant la propriété CSS `transform-origin`. Mais la valeur par défaut est `center`.
    

### Syntaxe de la fonction CSS `scale3d()`

`scale3d()` accepte trois arguments. Voici la syntaxe :

```css
element {
  transform: scale3d(x, y, z);
}
```

Les arguments `x`, `y` et `z` sont des nombres spécifiant les coordonnées x, y et z. Les coordonnées sont l'axe le long duquel les navigateurs mettront à l'échelle l'élément.

### Exemples de la fonction CSS `scale3d()`

Voici quelques exemples de fonctionnement de la fonction CSS `scale3d()`.

#### Comment utiliser `scale3d()` avec les fonctions CSS `perspective()` et `rotateX()` :

```css
img {
  transform: perspective(370px) scale3d(1, 1, 5) rotateX(17deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-inndft?file=style.css)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons utilisé la fonction `perspective()` pour définir une distance de `370px` entre l'utilisateur et le plan z=0.
    
2. La fonction `scale3d()` spécifie un facteur de mise à l'échelle de `1`, `1` et `5` pour l'image le long des axes x, y et z.
    
3. Nous avons utilisé la fonction `rotateX()` pour faire pivoter l'image de dix-sept degrés (17°) autour de l'axe x.
    

**Note :**

* Un facteur de mise à l'échelle de `1` n'appliquera *aucun* effet de mise à l'échelle sur l'élément.
    
* Listez `perspective()` en premier chaque fois que vous l'enchaînez avec d'autres fonctions de transformation CSS. Sinon, les navigateurs pourraient transformer incorrectement l'élément sélectionné.
    
* Listez la fonction `scale3d()` avant `rotateX()`. Sinon, le navigateur ne mettra *pas* à l'échelle l'élément.
    

#### Comment mettre à l'échelle des éléments en trois dimensions :

```css
img {
  width: 40%;
}

.second-image {
  transform: scale3d(5, 3, 0.05);
  transform-origin: top left;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-hq8kbr?file=style.css)

Nous avons utilisé la fonction `scale3d()` pour spécifier un facteur de mise à l'échelle de `5`, `3` et `0.05` pour l'image le long des axes x, y et z.

## Qu'est-ce que la fonction CSS `skew()` ?

`skew()` transforme un élément en l'inclinant (en le déformant) en deux dimensions autour d'un point fixe.

**Note :**

* "Origine de la transformation" est le point fixe à partir duquel l'ordinateur incline un élément.
    
* Vous pouvez définir le point fixe de votre élément en utilisant la propriété CSS `transform-origin`. Mais la valeur par défaut est `center`.
    

### Syntaxe de la fonction CSS `skew()`

`skew()` accepte deux arguments. Voici la syntaxe :

```css
element {
  transform: skew(aX, aY);
}
```

**Notez ce qui suit :**

* L'argument `aX` spécifie l'angle d'inclinaison de l'élément le long de l'axe x.
    
* L'argument `aY` spécifie l'angle d'inclinaison de l'élément le long de l'axe y.
    
* `aX` et `aY` peuvent être en degrés, gradians, radians ou tours.
    
* Un argument `angle` se compose d'un nombre suivi de l'unité que vous souhaitez utiliser, par exemple, `45deg`.
    
* `aY` est un argument facultatif.
    

### Exemples de la fonction CSS `skew()`

Voici quelques exemples de fonctionnement de la fonction CSS `skew()`.

#### Comment incliner un élément uniquement le long de l'axe X :

```css
img {
  transform: skew(30deg);
  transform-origin: top;
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-gx5dy4?file=style.css)

L'extrait ci-dessus a utilisé la fonction `skew()` pour appliquer une inclinaison de trente degrés (30°) sur l'image uniquement le long de l'axe x.

**Note :** `skew(30deg)` est équivalent à `skewX(30deg)`.

#### Comment incliner un élément uniquement le long de l'axe Y :

```css
img {
  transform: skew(0, 40deg);
  transform-origin: top left;
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-nbkjfj?file=style.css)

L'extrait ci-dessus a utilisé la fonction `skew()` pour appliquer une inclinaison de quarante degrés (40°) sur l'image uniquement le long de l'axe y.

**Note :**

* Un degré d'inclinaison zéro (`0`) indique aux navigateurs de *ne pas* appliquer d'effet d'inclinaison sur l'élément sélectionné.
    
* `skew(0, 40deg)` est équivalent à `skewY(40deg)`.
    

#### Comment incliner un élément le long des axes X et Y :

```css
img {
  transform: skew(30deg, 40deg);
  transform-origin: top left;
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ofrk9v?file=style.css)

L'extrait ci-dessus a utilisé la fonction `skew()` pour appliquer une inclinaison de trente degrés (30°) sur l'image le long de l'axe x. Et quarante degrés (40°) le long de l'axe y.

## Qu'est-ce que la fonction CSS `translate()` ?

`translate()` transforme un élément en le repositionnant (en le translatant) en deux dimensions.

### Syntaxe de la fonction CSS `translate()`

`translate()` accepte deux arguments. Voici la syntaxe :

```css
element {
  transform: translate(x, y);
}
```

**Notez ce qui suit :**

* L'argument `x` peut être une valeur de longueur ou de pourcentage. Il spécifie la distance à laquelle vous souhaitez déplacer l'élément de sa position d'origine sur l'axe x.
    
* L'argument `y` peut être une valeur de longueur ou de pourcentage. Il définit la distance à laquelle vous souhaitez déplacer l'élément de sa position d'origine sur l'axe y.
    
* `y` est un argument facultatif.
    

### Exemples de la fonction CSS `translate()`

Voici quelques exemples de fonctionnement de la fonction CSS `translate()`.

#### Comment translater un élément uniquement le long de l'axe X :

```css
img {
  transform: translate(150px);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-kuaqzz?file=style.css)

L'extrait ci-dessus a utilisé la fonction `translate()` pour repositionner l'image à `150px` de sa position d'origine le long de l'axe x.

Vous pouvez également l'écrire comme ceci, en spécifiant le `X` :

```css
img {
  transform: translateX(150px);
  width: 80%
```

**Note :** `translate(150px)` est équivalent à `translateX(150px)`.

#### Comment translater un élément uniquement le long de l'axe Y :

```css
img {
  transform: translate(0, 55%);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-2bchbd?file=style.css)

L'extrait ci-dessus a utilisé la fonction `translate()` pour repositionner l'image à `55%` de sa position d'origine le long de l'axe y.

**Note :**

* Une distance de translation zéro (`0`) indique aux navigateurs de *ne pas* appliquer d'effet de translation sur l'élément sélectionné.
    
* `translate(0, 55%)` est équivalent à `translateY(55%)`.
    

#### Comment translater un élément le long des axes X et Y :

```css
img {
  transform: translate(60%, 300px);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-uwpvu4?file=style.css)

L'extrait ci-dessus a utilisé la fonction `translate()` pour repositionner l'image à `60%` de sa position d'origine le long de l'axe x et à `300px` de son axe y.

## Qu'est-ce que la fonction CSS `translateZ()` ?

`translateZ()` transforme un élément en le repositionnant (en le translatant) en trois dimensions le long de l'axe z.

![Illustration du système de coordonnées cartésiennes 3D](https://www.freecodecamp.org/news/content/images/2023/06/cartesian-coordinate-system-three-dimensional-diagram-codesweetly-1.png align="left")

*Un système de coordonnées cartésiennes tridimensionnel montrant les axes X, Y et Z*

### Syntaxe de la fonction CSS `translateZ()`

`translateZ()` accepte un seul argument. Voici la syntaxe :

```css
element {
  transform: translateZ(longueur);
}
```

L'argument `longueur` spécifie la distance à laquelle vous souhaitez déplacer l'élément de sa position d'origine sur l'axe z.

![Illustration de l'argument de longueur de translateZ en CSS](https://www.freecodecamp.org/news/content/images/2023/06/cartesian-coordinate-system-three-dimensional-length-diagram-codesweetly.png align="left")

*Un système de coordonnées cartésiennes tridimensionnel avec une flèche rouge définissant la longueur de translation du plan vert*

### Exemples de la fonction CSS `translateZ()`

Nous utilisons souvent `translateZ()` avec la fonction `perspective()`. Voici quelques exemples.

#### Comment utiliser `translateZ()` avec la fonction CSS `perspective()` :

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(33px) translateZ(10px);
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-hvf8bb?file=style.css)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons utilisé la fonction `perspective()` pour définir une distance de `33px` entre l'utilisateur et le [plan z=0](https://codesweetly.com/css-perspective-function#what-is-the-z0-plane).
    
2. Nous avons utilisé la fonction `translateZ()` pour repositionner la `second-image` à dix pixels (`10px`) de sa position d'origine le long de l'axe z.
    

**Note :**

* Supposons que la position de l'axe z de la `second-image` soit supérieure ou égale à l'[argument](https://codesweetly.com/javascript-arguments-vs-parameters) de la fonction `perspective()`. Dans ce cas, l'image disparaîtra comme si elle était derrière l'utilisateur. En d'autres termes, l'élément sélectionné disparaît lorsque l'utilisateur est dans la même position que l'élément (ou lorsque l'élément est derrière l'utilisateur).
    
* Plus la distance de l'utilisateur à la position de l'axe z de l'élément est grande, moins l'effet de perspective sera intense, et vice-versa.
    

#### Comment utiliser `translateZ()` avec une perspective de `70px` :

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(70px) translateZ(10px);
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-vqd7mm?file=style.css)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons utilisé la fonction `perspective()` pour définir une distance de `70px` entre l'utilisateur et le plan z=0.
    
2. Nous avons utilisé la fonction `translateZ()` pour repositionner la `second-image` à dix pixels (`10px`) de sa position d'origine le long de l'axe z.
    

## Qu'est-ce que la fonction CSS `translate3d()` ?

`translate3d()` transforme un élément en le repositionnant (en le translatant) en trois dimensions le long des axes x, y et z.

### Syntaxe de la fonction CSS `translate3d()`

`translate3d()` accepte trois arguments. Voici la syntaxe :

```css
element {
  transform: translate3d(x, y, z);
}
```

**Notez ce qui suit :**

* L'argument `x` peut être une valeur de longueur ou de pourcentage. Il spécifie la distance à laquelle vous souhaitez déplacer l'élément de sa position d'origine sur l'axe x.
    
* L'argument `y` peut être une valeur de longueur ou de pourcentage. Il définit la distance à laquelle vous souhaitez déplacer l'élément de sa position d'origine sur l'axe y.
    
* `z` ne peut être qu'une longueur, et non un pourcentage. Il définit la distance à laquelle vous souhaitez déplacer l'élément de sa position d'origine sur l'axe z.
    

### Exemples de la fonction CSS `translate3d()`

Voici quelques exemples de fonctionnement de la fonction CSS `translate3d()`.

#### Comment translater un élément uniquement le long de l'axe X

```css
img {
  transform: translate3d(150px, 0, 0);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-qrxxmx?file=style.css)

L'extrait ci-dessus a utilisé la fonction `translate3d()` pour repositionner l'image à `150px` de sa position d'origine le long de l'axe x.

**Note :** `translate3d(150px, 0, 0)` est équivalent à `translateX(150px)`.

#### Comment translater des éléments en trois dimensions :

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(300px) translate3d(15%, 45%, 200px);
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-rksery?file=style.css)

L'extrait ci-dessus a utilisé la fonction `translate3d()` pour repositionner l'image à `15%` de sa position d'origine le long de l'axe x, à `45%` de son axe y et à `200px` de son axe z.

## Fonctions de translation CSS vs. propriété `translate` : Quelle est la différence ?

Les fonctions de translation CSS et la propriété CSS `translate` offrent deux moyens similaires de spécifier une transformation de translation.

Les principales différences entre les deux techniques de translation sont les suivantes :

* La propriété CSS `translate` permet de translater un élément sans utiliser la propriété CSS `transform`.
    
* La syntaxe de la propriété CSS `translate` est plus courte que celle de son alternative fonctionnelle.
    
* La propriété CSS `translate` vous évite de devoir mémoriser l'ordre spécifique pour positionner les fonctions de transformation.
    
* Les navigateurs calculent la matrice des fonctions de transformation dans l'ordre où vous les avez assignées à la propriété CSS `transform`, de gauche à droite.
    
* Les navigateurs calculent la matrice des propriétés de transformation dans l'ordre suivant :
    
    1. `translate`
        
    2. `rotate`
        
    3. `scale`
        

Voici quelques exemples.

### Comment utiliser la propriété CSS `translate` vs. la fonction pour translater un élément le long des axes X et Y

```css
img {
  translate: 60% 300px; /* Équivalent à une propriété transform: translate(60%, 300px) */
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-mhrmbj?file=style.css)

L'extrait ci-dessus a utilisé la propriété `translate` pour repositionner l'image à `60%` de sa position d'origine le long de l'axe x. Et à `300px` de son axe y.

**Note :** Supposons que vous souhaitiez translater un élément le long de l'axe z. Dans ce cas, définissez une propriété `perspective` sur l'"élément parent" de l'élément que vous souhaitez translater. Sinon, l'élément ne se déplacera pas le long de son axe z.

### Comment utiliser la propriété CSS `translate` vs. la fonction pour translater un élément le long de l'axe Z

```css
img {
  width: 40%;
}

div {
  perspective: 35px;
}

.second-image {
  translate: 0px 0px 17px; /* Équivalent à une propriété transform: translateZ(17px) */
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-gjr5sl?file=style.css)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons utilisé la propriété `perspective` pour définir une distance de `35px` entre l'utilisateur et le plan z=0.
    
2. Nous avons utilisé la propriété `translate` pour repositionner la `second-image` à dix-sept pixels (`17px`) de sa position d'origine le long de l'axe z.
    

### Comment utiliser la propriété CSS `translate` vs. la fonction pour translater un élément en trois dimensions

```css
img {
  width: 40%;
}

div {
  perspective: 300px;
}

.second-image {
  translate: 50% 25% 200px; /* Équivalent à une propriété transform: translate3d(50%, 25%, 200px) */
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-pgqrgc?file=style.css)

L'extrait ci-dessus a utilisé la propriété `translate` pour repositionner l'image à `50%` de sa position d'origine le long de l'axe x, à `25%` de son axe y et à `200px` de son axe z.

**Note :** Une valeur `none` indique aux navigateurs de *ne pas* translater l'élément sélectionné.

## Qu'est-ce que la fonction CSS `perspective()` ?

`perspective()` transforme un élément en ajoutant des effets de perspective.

### Syntaxe de la fonction CSS `perspective()`

`perspective()` n'accepte qu'un seul argument. Voici la syntaxe :

```css
element {
  transform: perspective(longueur);
}
```

L'argument `longueur` spécifie la distance de l'utilisateur au [plan z=0](https://codesweetly.com/css-perspective-function#what-is-the-z0-plane).

![Illustration de la méthode perspective() en CSS](https://www.freecodecamp.org/news/content/images/2023/06/cartesian-coordinate-system-perspective-method-illustration-codesweetly.png align="left")

*Un système de coordonnées cartésiennes tridimensionnel avec une flèche rouge définissant la distance entre l'utilisateur et le plan z=0*

### Exemples de la fonction CSS `perspective()`

Nous utilisons souvent `perspective()` avec d'autres fonctions CSS telles que `translateZ()`, `rotateX()` et `rotateY()`. Voici quelques exemples.

#### Comment utiliser `perspective()` avec la fonction CSS `translateZ()` :

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(33px) translateZ(10px);
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-hvf8bb?file=style.css)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons utilisé la fonction `perspective()` pour définir une distance de `33px` entre l'utilisateur et le plan z=0.
    
2. Nous avons utilisé la fonction `translateZ()` pour repositionner la `second-image` à dix pixels (`10px`) de sa position d'origine le long de l'axe z.
    

**Notez ce qui suit :**

* Supposons que la position de l'axe z de la `second-image` soit supérieure ou égale à l'argument de la fonction `perspective()`. Dans ce cas, l'image disparaîtra comme si elle était derrière l'utilisateur. En d'autres termes, l'élément sélectionné disparaît lorsque l'utilisateur est dans la même position que l'élément (ou lorsque l'élément est derrière l'utilisateur).
    
* Plus la distance de l'utilisateur à la position de l'axe z de l'élément est grande, moins l'effet de perspective sera intense, et vice-versa.
    

#### Comment utiliser `perspective()` avec la fonction CSS `rotateY()` :

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(33px) rotateY(-10deg);
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-tptutx?file=style.css)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons utilisé la fonction `perspective()` pour définir une distance de `33px` entre l'utilisateur et le plan z=0.
    
2. Nous avons utilisé la fonction `rotateY()` pour faire pivoter la `second-image` de moins dix degrés (-10°) autour de l'axe y.
    

#### Comment utiliser `perspective()` avec la fonction CSS `rotateX()` :

```css
img {
  width: 40%;
}

.second-image {
  transform: perspective(33px) rotateX(17deg);
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-8ddydv?file=style.css)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons utilisé la fonction `perspective()` pour définir une distance de `33px` entre l'utilisateur et le plan z=0.
    
2. Nous avons utilisé la fonction `rotateX()` pour faire pivoter la `second-image` de dix-sept degrés (17°) autour de l'axe x.
    

## Fonction CSS `perspective()` vs. propriété `perspective` : Quelle est la différence ?

La fonction CSS `perspective()` et la propriété `perspective` offrent deux moyens similaires d'ajouter des effets de perspective aux éléments HTML.

Les principales différences entre les deux techniques de perspective sont les suivantes :

* Nous appliquons la fonction `perspective()` "directement sur l'élément" auquel nous voulons ajouter des effets de perspective.
    
* Nous appliquons la propriété `perspective` "sur l'élément parent" de l'élément auquel nous voulons ajouter des effets de perspective.
    
* La fonction `perspective()` fonctionne comme une valeur de la propriété `transform`.
    
* La propriété CSS `perspective` vous permet de créer des effets de perspective sans utiliser la propriété CSS `transform`.
    

**Voici un exemple :**

Utilisez la propriété CSS `perspective` pour ajouter un effet de perspective à un élément enfant :

```css
img {
  width: 40%;
}

div {
  perspective: 33px;
}

.second-image {
  rotate: x 17deg;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-psssbh?file=style.css)

Voici ce que nous avons fait dans l'extrait ci-dessus :

1. Nous avons utilisé la propriété `perspective` pour définir une distance de `33px` entre l'utilisateur et le plan z=0.
    
2. Nous avons utilisé la propriété `rotate` pour faire pivoter la `second-image` de dix-sept degrés (17°) autour de l'axe x.
    

**Note :**

* La propriété CSS `perspective` vous évite de devoir mémoriser l'ordre spécifique pour positionner les fonctions de transformation.
    
* Une valeur `none` indique aux navigateurs de *ne pas* ajouter d'effet de perspective aux enfants de l'élément sélectionné.
    

## Qu'est-ce que la fonction CSS `matrix()` ?

La fonction CSS `matrix()` est une abréviation pour les fonctions de transformation 2D suivantes :

* `scaleX()`
    
* `skewY()`
    
* `skewX()`
    
* `scaleY()`
    
* `translateX()`
    
* `translateY()`
    

En d'autres termes, au lieu d'écrire :

```css
img {
  transform-origin: 0 0;
  transform: translateX(100px) translateY(250px) scaleX(2) scaleY(0.9)
    skewX(10deg) skewY(35deg);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-jquhyy?file=style.css)

Vous pouvez alternativement utiliser la fonction `matrix()` pour raccourcir votre code comme suit :

```css
img {
  transform-origin: 0 0;
  transform: matrix(2.24693, 0.630187, 0.352654, 0.9, 100, 250);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-zzlwhn?file=style.css)

### Syntaxe de la fonction CSS `matrix()`

La fonction `matrix()` accepte six valeurs. Voici la syntaxe :

```css
matrix(scaleX(), skewY(), skewX(), scaleY(), translateX(), translateY())
```

Vous pouvez représenter les valeurs de la matrice CSS sous forme de [coordonnées homogènes](https://en.wikipedia.org/wiki/Homogeneous_coordinates) sur [ℝℙ<sup>2</sup>](https://en.wikipedia.org/wiki/Real_projective_space) comme suit :

```txt
| scX skX tX | ← x-axis
| skY scY tY | ← y-axis
|  0   0   1 | ← constantes
```

**Notez ce qui suit :**

* `scX` et `skX` sont des nombres décrivant la transformation linéaire de mise à l'échelle et d'inclinaison d'un élément sur l'axe x.
    
* `tX` est un nombre représentant la translation d'un élément sur l'axe x.
    
* `skY` et `scY` sont des nombres décrivant la transformation linéaire d'inclinaison et de mise à l'échelle d'un élément sur l'axe y.
    
* `tY` est un nombre représentant la translation d'un élément sur l'axe y.
    
* `0`, `0`, `1` sont des constantes.
    
* Nous ne passons pas les constantes en tant qu'[arguments](https://codesweetly.com/javascript-arguments-vs-parameters) à la fonction `matrix()` car l'ordinateur les implique automatiquement.
    

### Exemples de la fonction CSS `matrix()`

Voici quelques exemples de la fonction CSS `matrix()`.

#### Comment convertir `scaleX()` en fonction `matrix()` :

Considérez la propriété `transform` suivante :

```css
img {
  transform-origin: 0 0;
  transform: scaleX(2);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-9r2euo?file=style.css)

Voici l'équivalent `matrix()` de la fonction `scaleX()` ci-dessus :

```css
img {
  transform-origin: 0 0;
  transform: matrix(2, 0, 0, 1, 0, 0); /* scX, skY, skX, scY, tX, tY */
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-bypfbf?file=style.css)

Représentons également les valeurs de la matrice sous forme de coordonnées homogènes sur ℝℙ<sup>2</sup> :

```txt
| 2 0 0 | ← x-axis
| 0 1 0 | ← y-axis
| 0 0 1 | ← constantes
```

Voici un autre exemple.

#### Comment convertir `translateY()` en fonction `matrix()` :

```css
img {
  transform-origin: 0 0;
  transform: translateY(250px);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-w25f3w?file=style.css)

Voici l'équivalent `matrix()` de la fonction `translateY()` ci-dessus :

```css
img {
  transform-origin: 0 0;
  transform: matrix(1, 0, 0, 1, 0, 250); /* scX, skY, skX, scY, tX, tY */
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-1coxrt?file=style.css)

Représentons également les valeurs de la matrice sous forme de coordonnées homogènes sur ℝℙ<sup>2</sup> :

```txt
| 1 0 0   | ← x-axis
| 0 1 250 | ← y-axis
| 0 0 1   | ← constantes
```

Voici un troisième exemple.

#### Comment convertir `translateX()` et `scale()` en fonction `matrix()` :

```css
img {
  transform-origin: 0 0;
  transform: translateX(100px) scale(2);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-wje2fa?file=style.css)

Voici la syntaxe pour convertir la valeur de la propriété `transform` ci-dessus en `matrix()` :

```txt
matrix = (coordonnées homogènes de translateX) x (coordonnées homogènes de scale)
```

Commençons la conversion en définissant les coordonnées homogènes de `translateX(100px)` :

```txt
| 1 0 100 | ← x-axis
| 0 1 0   | ← y-axis
| 0 0 1   | ← constantes
```

Définissons également les coordonnées homogènes de `scale(2)` :

```txt
| 2 0 0 | ← x-axis
| 0 2 0 | ← y-axis
| 0 0 1 | ← constantes
```

Il est maintenant temps de multiplier les deux coordonnées homogènes en utilisant la syntaxe suivante :

```txt
| a d g |   | j m p |   | aj + dk + gl   am + dn + go   ap +dq  + gr |
| b e h | x | k n q | = | bj + ek + hl   bm + en + ho   bp + eq + hr |
| c f i |   | l o r |   | cj + fk + il   cm + fn + io   cp + fq + ir |
```

Mettons en œuvre la syntaxe ci-dessus comme suit :

```txt
| 1 0 100 |   | 2 0 0 |   | 2 + 0 + 0   0 + 0 + 0   0 + 0 + 100 |
| 0 1  0  | x | 0 2 0 | = | 0 + 0 + 0   0 + 2 + 0   0 + 0 +  0  |
| 0 0  1  |   | 0 0 1 |   | 0 + 0 + 0   0 + 0 + 0   0 + 0 +  1  |
```

L'étape suivante consiste à résoudre l'addition. Faisons cela maintenant.

```txt
| 1 0 100 |   | 2 0 0 |   | 2 0 100 |
| 0 1  0  | x | 0 2 0 | = | 0 2  0  |
| 0 0  1  |   | 0 0 1 |   | 0 0  1  |
```

Le résultat de l'addition ci-dessus nous donne les coordonnées homogènes de la propriété `transform: translateX(100px) scale(2)`.

En d'autres termes, le produit de `(coordonnées homogènes de translateX)` et `(coordonnées homogènes de scale)` est égal à :

```txt
| 2 0 100 | ← x-axis
| 0 2  0  | ← y-axis
| 0 0  1  | ← constantes
```

Par conséquent, l'équivalence matricielle de `transform: translateX(100px) scale(2)` est `transform: matrix(2, 0, 0, 2, 100, 0)`.

```css
img {
  transform-origin: 0 0;
  transform: matrix(2, 0, 0, 2, 100, 0);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-njrg4k?file=style.css)

Veuillez noter que `transform: translateX(100px) scale(2)` et `transform: scale(2) translateX(100px)` retournent des matrices différentes. Voici un exemple de la deuxième disposition ci-dessous.

#### Comment convertir `scale()` et `translateX()` en fonction `matrix()` :

Considérez la propriété `transform` suivante :

```css
img {
  transform-origin: 0 0;
  transform: scale(2) translateX(100px);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-39trog?file=style.css)

Voici la syntaxe pour convertir la valeur de la propriété `transform` ci-dessus en `matrix()` :

```txt
matrix = (coordonnées homogènes de scale) x (coordonnées homogènes de translateX)
```

Commençons la conversion en définissant les coordonnées homogènes de `scale(2)` :

```txt
| 2 0 0 | ← x-axis
| 0 2 0 | ← y-axis
| 0 0 1 | ← constantes
```

Définissons également les coordonnées homogènes de `translateX(100px)` :

```txt
| 1 0 100 | ← x-axis
| 0 1  0  | ← y-axis
| 0 0  1  | ← constantes
```

Il est maintenant temps de multiplier les deux coordonnées homogènes en utilisant la syntaxe suivante :

```txt
| a d g |   | j m p |   | aj + dk + gl   am + dn + go   ap +dq  + gr |
| b e h | x | k n q | = | bj + ek + hl   bm + en + ho   bp + eq + hr |
| c f i |   | l o r |   | cj + fk + il   cm + fn + io   cp + fq + ir |
```

Mettons en œuvre la syntaxe ci-dessus comme suit :

```txt
| 2 0 0 |   | 1 0 100 |   | 2 + 0 + 0   0 + 0 + 0   200 + 0 + 0 |
| 0 2 0 | x | 0 1  0  | = | 0 + 0 + 0   0 + 2 + 0    0 + 0 + 0  |
| 0 0 1 |   | 0 0  1  |   | 0 + 0 + 0   0 + 0 + 0    0 + 0 + 1  |
```

L'étape suivante consiste à résoudre l'addition. Faisons cela maintenant.

```txt
| 2 0 0 |   | 1 0 100 |   | 2 0 200 |
| 0 2 0 | x | 0 1  0  | = | 0 2  0  |
| 0 0 1 |   | 0 0  1  |   | 0 0  1  |
```

Le résultat de l'addition ci-dessus nous donne les coordonnées homogènes de la propriété `transform: scale(2) translateX(100px)`.

En d'autres termes, le produit de `(coordonnées homogènes de scale)` et `(coordonnées homogènes de translateX)` est égal à :

```txt
| 2 0 200 | ← x-axis
| 0 2  0  | ← y-axis
| 0 0  1  | ← constantes
```

Par conséquent, l'équivalence matricielle de `transform: scale(2) translateX(100px)` est `transform: matrix(2, 0, 0, 2, 200, 0)`.

```css
img {
  transform-origin: 0 0;
  transform: matrix(2, 0, 0, 2, 200, 0);
  width: 80%;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-3m4vgk?file=style.css)

Remarquez que `transform: scale(2) translateX(100px)` est égal à `transform: matrix(2, 0, 0, 2, 200, 0)`. Et `transform: translateX(100px) scale(2)` est équivalent à `transform: matrix(2, 0, 0, 2, 100, 0)`.

En d'autres termes, l'ordre dans lequel vous écrivez les fonctions de transformation est important. Discutons-en davantage ci-dessous.

## Pourquoi l'ordre des fonctions de transformation CSS est-il important ?

L'ordre dans lequel vous écrivez les [fonctions de transformation CSS](https://codesweetly.com/web-tech-terms-c#css-transform-functions) est important en raison de la manière dont les navigateurs calculent les valeurs de la matrice.

Par exemple, considérons l'extrait suivant :

```css
div {
  position: absolute;
  width: 100px;
  height: 100px;
  transform-origin: 0 0;
}

.red {
  border: 3px solid red;
  background-color: rgba(255, 0, 0, 0.5);
}

.green {
  border: 3px solid green;
  background-color: rgba(0, 128, 0, 0.5);
  transform: translateX(100px) scale(2);
}

.blue {
  border: 3px solid blue;
  background-color: rgba(0, 0, 255, 0.5);
  transform: scale(2) translateX(100px);
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-rvkagy?file=style.css)

La seule différence entre les divs vert et bleu est l'ordre dans lequel nous avons écrit leurs fonctions de transformation.

Cependant, l'ordinateur a translaté les deux conteneurs en utilisant des valeurs différentes (`100px` pour le div vert et `200px` pour le bleu).

Alors, pourquoi l'ordre des fonctions de transformation a-t-il affecté les valeurs de translation des divs ? Voici la raison :

* Les navigateurs multiplient les coordonnées homogènes de chaque fonction de transformation dans l'ordre, de gauche à droite.
    

En d'autres termes, l'ordinateur a utilisé la syntaxe suivante pour calculer la matrice du div vert :

* [Matrice du div vert](#comment-convertir-translatex-et-scale-en-fonction-matrix) = (coordonnées homogènes de translateX) x (coordonnées homogènes de scale)
    

Et il a utilisé la syntaxe suivante pour calculer la matrice du div bleu :

* [Matrice du div bleu](#comment-convertir-scale-et-translatex-en-fonction-matrix) = (coordonnées homogènes de scale) x (coordonnées homogènes de translateX)
    

Par conséquent, la position des fonctions de transformation a déterminé les [arguments](https://codesweetly.com/javascript-arguments-vs-parameters) de la matrice car les navigateurs ont commencé le calcul dans l'ordre, de la fonction la plus à gauche à la plus à droite.

Savoir comment convertir les fonctions de transformation en `matrix()` est bénéfique. Et avoir quelques outils de conversion peut être utile. Discutons donc de quelques outils utiles que vous pouvez utiliser.

## Outils pour convertir les fonctions de transformation en `matrix()`

Les deux outils que vous pouvez utiliser pour effectuer une conversion rapide des fonctions de transformation en `matrix()` sont :

* La méthode JavaScript `window.getComputedStyle()`
    
* L'outil de résolution de matrice d'Eric Meyer et Aaron Gustafson
    

### Comment utiliser `window.getComputedStyle()` pour convertir les fonctions de transformation en `matrix()`

Supposons que vous souhaitiez convertir les fonctions de transformation suivantes en matrice :

```css
img {
  transform-origin: 0 0;
  transform: scale(2) translateX(100px);
  width: 80%;
}
```

Vous ajouterez un attribut `id` à l'élément image :

```html
<img
  src="https://cdn.pixabay.com/photo/2022/09/26/23/26/african-american-7481724_960_720.jpg"
  alt=""
  id="image"
/>
```

Ensuite, en JavaScript, vous :

1. Utiliserez l'attribut `id` pour obtenir l'élément image.
    
2. Utiliserez la méthode [`window.getComputedStyle()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle) pour obtenir la valeur de la propriété `transform` de l'image.
    

**Voici le code :**

```js
// Obtenez l'élément image par son nom d'id :
const image = document.getElementById("image");

// Obtenez la valeur de la propriété transform de l'élément image :
const matrix = window.getComputedStyle(image).getPropertyValue("transform");

// Journalisez la valeur de la variable matrix dans la console :
console.log(matrix);
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-39trog?devToolsHeight=33&file=index.js)

Les navigateurs, par défaut, convertissent la valeur d'une propriété CSS `transform` en son équivalent matriciel. Ainsi, l'extrait ci-dessus a retourné la valeur calculée de l'image.

Discutons maintenant du deuxième outil de conversion.

### Comment utiliser l'outil de résolution de matrice pour convertir les fonctions de transformation en `matrix()`

Supposons que vous souhaitiez convertir les fonctions de transformation suivantes en une `matrix()` :

```css
img {
  transform-origin: 0 0;
  transform: scale(2) translateX(100px);
  width: 80%;
}
```

Vous ferez ce qui suit :

1. Allez sur le site Web The Matrix Resolutions : [https://meyerweb.com/eric/tools/matrix/](https://meyerweb.com/eric/tools/matrix/).
    
2. Collez vos fonctions de transformation (`scale(2) translateX(100px)`) dans le premier champ de texte.
    
3. Cliquez sur le bouton "The Red Pill" pour générer l'équivalence matricielle des fonctions de transformation.
    

![Capture d'écran de l'outil de résolution de matrice](https://www.freecodecamp.org/news/content/images/2023/06/how-to-use-the-matrix-resolutions-tool-codesweetly.jpg align="left")

*Cliquez sur le bouton de la pilule rouge pour convertir les fonctions de transformation CSS en une fonction matrix()*

**Astuce :** Utilisez [matrix3d()](https://codesweetly.com/css-matrix3d-function) pour créer une matrice de transformation 3D.

## Choses importantes à savoir sur la transformation des éléments en CSS

Voici trois faits essentiels à retenir lorsque vous transformez des éléments en CSS.

### 1. La transformation crée un contexte de superposition

Supposons que vous définissiez la propriété `transform` sur une valeur autre que `none`. Dans ce cas, le navigateur créera un [contexte de superposition](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context). Et l'élément transformé servira de [bloc conteneur](https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block) pour tout élément positionné de manière [absolue](https://codesweetly.com/css-position-property#what-is-position-absolute-in-css) ou [fixe](https://codesweetly.com/css-position-property#what-is-position-fixed-in-css) qu'il contient.

### 2. Les animations de mise à l'échelle et de zoom causent des problèmes d'accessibilité

Chaque fois que vous incluez des animations de mise à l'échelle ou de zoom dans votre application, offrez aux utilisateurs une option pour désactiver les animations. Cette option est nécessaire car les animations de mise à l'échelle et de zoom causent des [problèmes d'accessibilité](https://developer.mozilla.org/en-US/docs/Web/CSS/transform#accessibility_concerns).

### 3. Tous les éléments ne sont pas transformables

Vous ne pouvez pas transformer les [modèles de boîte](https://codesweetly.com/css-box-model) suivants :

* [Éléments en ligne non remplacés](https://codesweetly.com/css-transform-property#non-replaced-vs-replaced-elements-whats-the-difference)
    
* [Boîtes de colonne de tableau](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)
    
* [Groupes de colonnes de tableau](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
    

## Conclusion

Dans cet article, nous avons discuté de tous les outils de transformation CSS dont vous avez besoin pour translater, faire pivoter, incliner, mettre à l'échelle ou ajouter des effets de perspective aux éléments HTML.

J'espère que vous avez trouvé cet article utile.

### Merci d'avoir lu !

Si vous aimez ce tutoriel, vous apprécierez mon [livre sur CSS Flexbox](https://amzn.to/3N3XUws). C'est un guide de référence rapide pratique qui utilise des images et des exemples en direct pour expliquer Flexbox.

[![Obtenez le livre CSS Flexbox de CodeSweetly sur Amazon](https://www.freecodecamp.org/news/content/images/2023/06/css-flexbox-book-get-banner-codesweetly.png align="left")](https://amzn.to/3N3XUws)