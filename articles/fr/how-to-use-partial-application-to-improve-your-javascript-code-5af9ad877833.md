---
title: Comment utiliser l'application partielle pour améliorer votre code JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T15:44:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-partial-application-to-improve-your-javascript-code-5af9ad877833
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wj-ZuazaL-hq_6keyoVbGA.jpeg
tags:
- name: development
  slug: development
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment utiliser l'application partielle pour améliorer votre code JavaScript
seo_desc: 'By Rick Henry

  Making use of this functional technique can make your code more elegant


  Functional programming gives us techniques to solve problems in our code. One of
  these, partial application, is a little tricky to understand but it can allow us
  t...'
---

Par Rick Henry

#### Utiliser cette technique fonctionnelle peut rendre votre code plus élégant

![Image](https://cdn-media-1.freecodecamp.org/images/YlwtX1HWYUmiNRvHck44VFmc7Ho86aQTIG54)

La programmation fonctionnelle nous donne des techniques pour résoudre des problèmes dans notre code. L'une d'entre elles, l'application partielle, est un peu difficile à comprendre, mais elle peut nous permettre d'écrire moins de code (ce qui semble intéressant, n'est-ce pas ?).

#### Qu'est-ce que c'est ?

L'application partielle commence avec une fonction. Nous prenons cette fonction et créons une nouvelle avec un ou plusieurs de ses arguments déjà "définis" ou _partiellement appliqués_. Cela semble étrange, mais cela réduira le nombre de paramètres nécessaires pour nos fonctions.

Donnons un peu de contexte sur le moment où nous pourrions utiliser l'application partielle :

```
const list = (lastJoin, ...items) => {  const commaSeparated = items.slice(0,-1).join(", ");  const lastItem = items.pop();  return `${commaSeparated} ${lastJoin} ${lastItem}`;}
```

Cette petite fonction prend un seul mot, `lastJoin`, et un nombre arbitraire d'`items`. Initialement, `list` déclare une variable `commaSeparated`. Cette variable stocke un tableau joint séparé par des virgules de tous les éléments sauf le dernier. À la ligne suivante, nous stockons le dernier élément dans `items` dans une variable `lastItem`. La fonction retourne ensuite en utilisant un modèle de chaîne.

La fonction retourne ensuite les `items`, sous forme de chaîne, au format de liste. Par exemple :

```
list("and", "red", "green", "blue");     // "red, green and blue"list("with", "red", "green", "blue");    // "red, green with blue"list("or", "red", "green", "blue");      // "red, green or blue"
```

Notre fonction `list` nous permet de créer des listes quand nous le voulons. Chaque type de liste que nous créons, "and", "with", "or" est une spécialisation de la fonction générale `list`. Ne serait-il pas agréable qu'ils puissent être des fonctions à part entière ?!

#### Comment utiliser l'application partielle

C'est là que l'application partielle peut aider. Par exemple, pour créer une fonction `listAnd`, nous "définissons" (ou _appliquons partiellement_) l'argument `lastJoin` pour qu'il soit "and". Le résultat de cette opération signifie que nous pouvons invoquer notre fonction partiellement appliquée comme ceci :

```
listAnd("red", "green", "blue");    // "red, green and blue"
```

Cela ne doit pas s'arrêter là non plus. Nous pouvons créer de nombreuses fonctions spécialisées en _appliquant partiellement_ un argument à notre fonction de liste :

```
listOr("red", "green", "blue");      // "red, green or blue"listWith("red", "green", "blue");    // "red, green with blue"
```

Pour ce faire, nous devons créer une fonction utilitaire `partial` :

```
const partial = (fn, firstArg) => {  return (...lastArgs) => {    return fn(firstArg, ...lastArgs);  }}
```

Cette fonction prend une fonction `fn` comme premier paramètre et `firstArg` comme second. Elle retourne une toute nouvelle fonction avec un paramètre, `lastArgs`. Cela rassemble les arguments passés.

Maintenant, pour créer notre fonction `listAnd`, nous invoquons `partial` en passant notre fonction `list` et notre mot de jointure final :

```
const listAnd = partial(list, "and");
```

Notre fonction `listAnd` ne prend maintenant qu'une liste arbitraire d'éléments. Cette fonction, lorsqu'elle est invoquée, appellera à son tour la fonction `list` passée. Nous pouvons voir qu'elle recevra "and" comme premier argument et les `lastArgs` rassemblés par la suite.

Nous avons maintenant créé une fonction partiellement appliquée. Nous pouvons utiliser cette fonction spécialisée encore et encore dans notre programme :

```
listAnd("red", "green", "blue");    // "red, green and blue"
```

#### **Aller plus loin**

La fonction `partial` que nous avons créée est destinée à illustrer le fonctionnement de l'application partielle. Il existe d'excellentes bibliothèques JavaScript fonctionnelles disponibles qui ont cette utilité intégrée, comme [Ramda JS](https://ramdajs.com/docs/#partial).

Il est intéressant de noter que même si vous êtes nouveau dans le concept d'application partielle, il y a de fortes chances que vous l'ayez déjà utilisée. Si vous avez déjà utilisé la méthode `.bind()` sur une fonction, c'est un exemple d'application partielle. Il est courant de passer `this` à bind pour définir son contexte. Sous le capot, il applique partiellement `this` et retourne une nouvelle fonction.