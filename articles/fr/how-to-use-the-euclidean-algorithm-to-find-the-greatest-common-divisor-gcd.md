---
title: Comment utiliser l'algorithme d'Euclide pour trouver le Plus Grand Commun Diviseur
  (PGCD)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T22:39:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-euclidean-algorithm-to-find-the-greatest-common-divisor-gcd
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e4c740569d1a4ca3c63.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: Comment utiliser l'algorithme d'Euclide pour trouver le Plus Grand Commun
  Diviseur (PGCD)
seo_desc: 'For this topic you must know about the Greatest Common Divisor (GCD) and
  the MOD operation first.

  Greatest Common Divisor (GCD)

  The GCD of two or more integers is the largest integer that divides each of the
  integers such that their remainder is zero...'
---

Pour ce sujet, vous devez d'abord connaître le Plus Grand Commun Diviseur (PGCD) et l'opération MOD.

### Plus Grand Commun Diviseur (PGCD)

Le PGCD de deux ou plusieurs entiers est le plus grand entier qui divise chacun des entiers de telle sorte que leur reste soit zéro.

Voici un exemple :

PGCD de 20, 30 = 10 (10 est le plus grand nombre qui divise 20 et 30 avec un reste de 0)
PGCD de 42, 120, 285 = 3 (3 est le plus grand nombre qui divise 42, 120 et 285 avec un reste de 0)

### Opération « mod »

L'opération mod vous donne le reste lorsque deux entiers positifs sont divisés. Nous l'écrivons comme suit :
`A mod B = R`

Cela signifie que diviser A par B vous donne le reste R. Cela est différent de votre opération de division qui vous donne le quotient.

Voici un exemple :

7 mod 2 = 1 _(Diviser 7 par 2 donne un reste de 1)_
42 mod 7 = 0 _(Diviser 42 par 7 donne un reste de 0)_

Si vous comprenez les deux concepts ci-dessus, vous comprendrez facilement l'algorithme d'Euclide.

## Algorithme d'Euclide pour le Plus Grand Commun Diviseur (PGCD)

L'algorithme d'Euclide trouve le PGCD de 2 nombres.

Vous comprendrez mieux cet algorithme en le voyant en action. Supposons que vous souhaitiez calculer le PGCD de 1220 et 516, appliquons l'algorithme d'Euclide.

Pseudo-code de l'algorithme :

Étape 1 : **Soit `a, b` les deux nombres**
Étape 2 : **`a mod b = R`**
Étape 3 : **Soit `a = b` et `b = R`**
Étape 4 : **Répéter les étapes 2 et 3 jusqu'à ce que `a mod b` soit supérieur à 0**
Étape 5 : **PGCD = b**
Étape 6 : Fin

Voici le code Javascript pour effectuer le PGCD :

```javascript
function gcd(a, b) {
  var R;
  while ((a % b) > 0)  {
    R = a % b;
    a = b;
    b = R;
  }
  return b;
}
```

Voici le code Javascript pour effectuer le PGCD en utilisant la récursivité :

```javascript
function gcd(a, b) {
  if (b == 0)
    return a;
  else
    return gcd(b, (a % b));
}
```

Vous pouvez également utiliser l'algorithme d'Euclide pour trouver le PGCD de plus de deux nombres. Puisque le PGCD est associatif, l'opération suivante est valide : `PGCD(a,b,c) == PGCD(PGCD(a,b), c)`

Calculez le PGCD des deux premiers nombres, puis trouvez le PGCD du résultat et du nombre suivant. Exemple : `PGCD(203,91,77) == PGCD(PGCD(203,91),77) == PGCD(7, 77) == 7`

Vous pouvez trouver le PGCD de `n` nombres de la même manière.