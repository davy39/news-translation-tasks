---
title: Comment implémenter le Théorème des Restes Chinois en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T22:06:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-the-chinese-remainder-theorem-in-java-db88a3f1ffe0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*wyjesOXusRqfQ_BG
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: cybersecurity
  slug: cybersecurity
- name: Java
  slug: java
- name: General Programming
  slug: programming
seo_title: Comment implémenter le Théorème des Restes Chinois en Java
seo_desc: 'By Anuj Pahade

  This post assumes that you know what Chinese Remainder Theorem (CRT) is and focuses
  on its implementation in Java. If you don’t, I’d recommend you read about it here.

  You can find the link to the complete code at the end of this post. ...'
---

Par Anuj Pahade

Cet article suppose que vous savez ce qu'est le Théorème des Restes Chinois (CRT) et se concentre sur son implémentation en Java. Si ce n'est pas le cas, je vous recommande de le lire [ici](https://en.wikipedia.org/wiki/Chinese_remainder_theorem).

Vous pouvez trouver le lien vers le code complet à la fin de cet article. Alors, commençons.

#### Que devons-nous trouver ?

Nous devons trouver X. ?

L'énoncé est le suivant :

Il existe un _nombre positif minimum_ X tel que :

```
X % number[0]    =  remainder[0], X % number[1]    =  remainder[1], ...............X % number[k-1]  =  remainder[k-1]
```

Ainsi, nous avons deux tableaux.

1. **Le tableau de nombres :** Tous les nombres de ce tableau sont premiers entre eux deux à deux. Cela signifie que, si vous choisissez deux nombres quelconques dans le tableau, vous constaterez que leur plus grand commun diviseur est 1.
2. **Le tableau de restes :** Comme vous pouvez le voir dans les expressions ci-dessus, lorsque X est divisé par un nombre _n_ du tableau _number_, il laisse un reste respectif du tableau _remainder_.

### Étapes pour implémenter le CRT

Voici les étapes, ou comme nous, ingénieurs, disons, l'« algorithme », pour implémenter le CRT.

#### Étape 1 : Trouver le produit de tous les nombres dans le premier tableau.

```
for(int i=0; i<number.length; i++ ){   product *= number[i];}
```

#### Étape 2 : Trouver le produit partiel de chaque nombre.

Produit partiel de _n_ = produit/_n_

```
for(int i=0; i<num.length; i++){   partialProduct[i] = product/number[i];}
```

#### 3. Trouver l'inverse multiplicatif modulaire de number[i] modulo partialProduct[i].

Ici, nous trouvons l'inverse en utilisant l'[algorithme d'Euclide étendu](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/). Ainsi, nous appelons _computeInverse(partialProduct[i],num[i])_

```
public static int computeInverse(int a, int b){         int m = b, t, q;         int x = 0, y = 1;               if (b == 1)             return 0;               // Appliquer l'algorithme d'Euclide étendu         while (a > 1)         {             // q est le quotient             q = a / b;             t = b;                   // procéder maintenant comme l'algorithme d'Euclide             b = a % b;a = t;             t = x;             x = y - q * x;             y = t;         }               // Rendre x1 positif         if (y < 0)          y += m;               return y;     }
```

#### Étape 4 : Somme finale

```
sum += partialProduct[i] * inverse[i] * rem[i];
```

#### Étape 5 : Retourner le plus petit X

Pour trouver le plus petit de toutes les solutions, nous divisons la somme de l'étape 4 par le produit de l'étape 2.

```
return sum % product;
```

Ainsi, nous avons trouvé notre X. Je vous recommande d'essayer d'implémenter le code par vous-même avant de regarder le code dans le lien ci-dessous.

Merci d'avoir lu l'article. J'espère qu'il vous a aidé. Laissez des suggestions dans les commentaires ci-dessous ou contactez-moi avec une meilleure version de [ce code](https://github.com/anujpahade/CRT) ou des questions sur anujp5678[at]gmail[dot]com ou connectez-vous avec [moi sur LinkedIn](https://www.linkedin.com/in/anuj-pahade/).

N'oubliez pas d'applaudir. ? Les applaudissements motivent.

Amusez-vous bien et bon codage ! :)