---
title: Qu'est-ce qu'une factorielle ? Comment calculer les factorielles avec des exemples
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-08-03T16:32:53.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-factorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/antoine-dautry-_zsL306fDck-unsplash.jpg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: Qu'est-ce qu'une factorielle ? Comment calculer les factorielles avec des
  exemples
seo_desc: 'A factorial is a mathematical operation that you write like this: n!. It
  represents the multiplication of all numbers between 1 and n.

  So if you were to have 3!, for example, you''d compute 3 x 2 x 1 (which = 6). Let''s
  see how it works with some more ...'
---

Une factorielle est une opération mathématique que vous écrivez comme ceci : `n!`. Elle représente la multiplication de tous les nombres entre 1 et n.

Ainsi, si vous aviez `3!`, par exemple, vous calculeriez 3 x 2 x 1 (ce qui = 6). Voyons comment cela fonctionne avec quelques exemples supplémentaires.

## Définition d'une factorielle

La factorielle d'un nombre est la multiplication de tous les nombres entre 1 et le nombre lui-même. Elle s'écrit comme ceci : `n!`. Ainsi, la factorielle de 2 est `2!` (= 1 × 2).

Pour calculer une factorielle, vous devez savoir deux choses :

1. `0! = 1`
2. `n! = (n - 1)! × n`

La factorielle de 0 a une valeur de 1, et la factorielle d'un nombre `n` est égale à la multiplication entre le nombre `n` et la factorielle de `n-1`.

Par exemple, `5!` est égal à `4! × 5`.

Voici les premières valeurs de factorielle pour vous donner une idée de comment cela fonctionne :

| Factorielle | Multiplication | Résultat |
| -- | -- | -- |
| 0! | 1 | 1 |
| 1! | 1 | 1 |
| 2! | 1 × 2 | 2 |
| 3! | 1 × 2 × 3 | 6 |
| 4! | 1 × 2 × 3 × 4 | 24 |
| 5! | 1 × 2 × 3 × 4 × 5 | 120 |
| 6! | 1 × 2 × 3 × 4 × 5 × 6 | 720 |
| 7! | 1 × 2 × 3 × 4 × 5 × 6 × 7 | 5040 |
| 8! | 1 × 2 × 3 × 4 × 5 × 6 × 7 × 8 | 40,320 |
| 9! | 1 × 2 × 3 × 4 × 5 × 6 × 7 × 8 × 9 | 362,880 |

## À quoi sert une factorielle ?

En termes pratiques, une factorielle est le nombre de permutations différentes que vous pouvez avoir avec `n` éléments : 3 éléments peuvent être arrangés en exactement 6 façons différentes (exprimé comme `3!`).

Par exemple, voyons tous les arrangements que vous pouvez avoir avec les trois éléments, A, B et C :

```text
ABC
ACB
BAC
BCA
CAB
CBA
```

Et en effet, `3! = 6`.

### Comment calculer la factorielle de 0

En regardant la factorielle de ce point de vue, quelle est la factorielle de 0 ?

Eh bien, combien de façons différentes pouvez-vous arranger 0 éléments ?

Il y a exactement 1 façon d'arranger zéro éléments. Et c'est en faisant une séquence de zéro éléments.

### Cas d'utilisation des factorielles

Vous utilisez typiquement une factorielle lorsque vous avez un problème lié au nombre d'arrangements possibles. Regardons quelques exemples de problèmes.

#### Exemple de problème de factorielle 1 : les lettres du mot "camper"

_Combien de façons différentes pouvez-vous arranger les lettres du mot `camper` ?_

Le mot `camper` a 6 lettres, donc le nombre d'arrangements possibles est donné par la factorielle de 6 : `6! = 6 × 5 × 4 × 3 × 2 × 1 = 720`. Cela aurait été un nombre assez grand d'arrangements à trouver à la main, n'est-ce pas ?

#### Exemple de problème de factorielle 2 : tirer des boules colorées d'un sac

Disons qu'il y a trois boules dans un sac – une verte, une bleue et une jaune.

Si vous tirez les trois boules en séquence, quelle est la chance que vous obteniez la jaune en premier, la verte en second et la bleue en dernier ?

Peut-être vous demandez-vous maintenant ce que les chances ont à voir avec les factorielles – eh bien, dans un instant vous verrez.

Il y a 6 séquences possibles dans lesquelles les boules peuvent être tirées : 3! = 6.

Il y a une chance de 1 sur le nombre total de possibilités d'obtenir la séquence jaune-vert-bleu, donc c'est `1/(3!)` ou `1/6` ou `16,7 %` de chance d'obtenir le résultat souhaité.

## Comment calculer une factorielle de manière programmatique avec JavaScript

Il y a deux façons de calculer les factorielles de manière programmatique en JavaScript :

### Comment calculer une factorielle en JS avec la récursivité

Revenons aux deux choses à savoir lors du calcul d'une factorielle – c'est-à-dire `0! = 1` et `n! = (n - 1)! × n`. Nous pouvons utiliser la première pour créer le cas de base de la fonction récursive, car dans ce cas, nous connaissons déjà le résultat.

```js
function factorial(n) {
  if (n === 0) {
      return 1;
  }
}
```

La deuxième chose à savoir sur la façon de calculer une factorielle, `n! = (n - 1)! × n`, peut être le cas récursif.

```javascript
function factorial(n) {
    if (n === 0) {
        return 1;
    } else {
        return factorial(n-1) * n;
    }
}
    
```

### Comment calculer une factorielle avec une boucle `while` en JavaScript

Nous avons dit précédemment que `0! = 1`. Ainsi, pour calculer la factorielle d'un nombre avec une boucle, nous pouvons initialiser une variable à `1`, et multiplier les nombres de `n` à `1` par la variable à l'intérieur de la boucle.

De cette manière, si l'entrée est supérieure à 1, la sortie sera facilement 1.

```javascript
function factorial(n) {
    let result = 1;
    while (n > 1) {
        result *= n;
        n--;
    }
    return result;
}
```

## Conclusion

La factorielle est un opérateur assez important à connaître si vous vous intéressez aux statistiques et aux probabilités.

Dans cet article, vous avez appris comment calculer une factorielle, une application simple, et vous avez vu comment la calculer en utilisant JavaScript.

Amusez-vous bien avec cela !