---
title: 'Une introduction aux algorithmes de tri avancés : merge, quick et radix sort
  en JS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-19T15:45:45.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-advanced-sorting-algorithms-merge-quick-radix-sort-in-javascript-b65842194597
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BtcGRVPLOjnY5zFrhGX4TQ.gif
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: 'Une introduction aux algorithmes de tri avancés : merge, quick et radix
  sort en JS'
seo_desc: 'By Yung L. Leung

  In my previous article, “The Complexity of Simple Algorithms & Data Structures in
  JavaScript,” we discussed simple sorting algorithms (bubble, selection & insertion
  sorts). Here, I go through merge, quick & radix sort, each of which ...'
---

Par Yung L. Leung

Dans mon article précédent, « [The Complexity of Simple Algorithms & Data Structures in JavaScript](https://medium.freecodecamp.org/the-complexity-of-simple-algorithms-and-data-structures-in-javascript-11e25b29de1e?source=friends_link&sk=994bc3da2b4cc5b78da06cf161dad6a7) », nous avons discuté des algorithmes de tri simples (bubble, selection & insertion sorts). Ici, je passe en revue les algorithmes **merge**, **quick** et **radix sort**, chacun d'entre eux présentant une amélioration significative de la **complexité temporelle moyenne**, inférieure à **O(n²)**.

Examinons chacun d'entre eux plus en détail.

### Merge

Un **merge sort** sépare une liste en ses éléments individuels. Il les trie ensuite lors de leur fusion dans une liste ordonnée croissante.

![Image](https://cdn-media-1.freecodecamp.org/images/l8DC03SRDhOSepFxlfGQLZdNFstJiRVv4ro-)
_[source](https://codepumpkin.com/wp-content/uploads/2017/10/MergeSort_Avg_case.gif" rel="noopener" target="_blank" title=")_

En pratique, cela signifie découper continuellement un tableau en tableaux d'un seul élément, avant de pousser chaque élément dans un tableau plus grand (le plus petit en premier). Chaque étape de poussage d'éléments de 2 tableaux plus petits dans 1 tableau plus grand implique de déterminer quel élément de quel tableau a la valeur la plus petite.

La complexité du merge sort est **O((n log n) + 1)**. Rappelez-vous que la notation Big O ([Complexité des algorithmes et structures de données simples en JS](https://medium.freecodecamp.org/the-complexity-of-simple-algorithms-and-data-structures-in-javascript-11e25b29de1e?source=friends_link&sk=994bc3da2b4cc5b78da06cf161dad6a7)) est un compte du **nombre d'opérations (O)** par rapport au **nombre d'éléments (n)**. Ainsi, une liste de 4 éléments nécessite 3 divisions. **Notez** que la liste est déjà ordonnée pour la simplicité de l'exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/4NvlwpDKTdqjvzsLjPGXppr5d1wkuV-DpI5n)
_Division d'une liste de 4 éléments._

La fusion des 4 tableaux nécessite 6 comparaisons.

![Image](https://cdn-media-1.freecodecamp.org/images/-3m3gNldPcs19pC42uSrtnZn6CPZiqSrXnre)
_Une fois divisée, lors de la fusion, les 4 éléments nécessitent un total de 6 comparaisons._

Ainsi, le calcul mathématique est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/30Xikd3S8hvaeN5QCQ7FUebqfRHtXNdfMlOS)
_9 opérations (**3 divisions & 6 comparaisons**) sont nécessaires pour effectuer un merge sort sur un tableau de 4 éléments_

Pour simplifier, la complexité du merge sort est **O(n log n)**. Le **+1** est insignifiant par rapport à la valeur de **n log n** et la base 2 du logarithme est supposée.

### Quick

Un **quick sort** sélectionne une valeur (à l'index 0), échange toutes les valeurs inférieures plus près de celle-ci, puis effectue un échange final pour placer la valeur sélectionnée devant les valeurs inférieures (un index quelque part après 0). De cette manière, toutes les valeurs derrière la **valeur pivot** sont des valeurs inférieures. Toutes les valeurs devant celle-ci sont des valeurs supérieures. Ainsi, lors du pivotement, la **valeur sélectionnée (pivot)** est placée dans sa position correcte. Le processus se répète jusqu'à ce que toutes les valeurs soient « pivotées » à leurs positions correctes.

![Image](https://cdn-media-1.freecodecamp.org/images/kjyINxAg57U9i3L3LR82l3a78eczlbmTWxeJ)
_[source](https://thumbs.gfycat.com/RectangularHarmlessGalapagosmockingbird-size_restricted.gif" rel="noopener" target="_blank" title=")_

Similaire en pratique au **merge sort**, le **quick sort** nécessite de diviser une liste en listes plus petites. Plutôt que de trier lors de la fusion, un pivot est sélectionné pour ordonner la liste de sorte que les valeurs inférieures soient à sa gauche et les valeurs supérieures à sa droite. Par conséquent, il n'est pas surprenant que, comme le **merge sort**, le **quick sort** ait également une complexité de **O(n log n)**.

Ainsi, pour un tableau de 4 éléments, un pivot est sélectionné et sa position correcte est trouvée (par exemple, 2 à l'index 0 appartient à l'index 1). Lors de cette découverte, 3 comparaisons sont faites avec la valeur pivot (2) par rapport aux éléments restants (4, 1 & 3).

![Image](https://cdn-media-1.freecodecamp.org/images/SzBMbtjRvg4D4mob41oxqTAfY533YVJmTC8q)
_Quick Sort du tableau [2, 4, 1, 3]_

Le tableau partiellement trié (1, 2, 4, 3) est ensuite décomposé pour trouver les positions pivot des valeurs **1** et **4 (par comparaison à la valeur 3)**, avant de découvrir la dernière position pivot (valeur **3**). Cela représente 4 comparaisons et la découverte de 4 positions pivot ou :

![Image](https://cdn-media-1.freecodecamp.org/images/44KtTSDkRKtWfoJxjCkRO-cQZ6AqZ9-5Fyb8)
_O(n log n)_

### Radix

Un **radix sort** ordonne continuellement une liste de nombres par leur chiffre en base dix.

![Image](https://cdn-media-1.freecodecamp.org/images/Yol000Gd9BoRp6zYTLOlLaBwogDcQEUQ3DQ9)
_Chiffres de 0 à 9_

Dans ce cas, les nombres (101, 54, 305, 6, 81) sont d'abord ordonnés par leur chiffre des unités, puis par leur chiffre des dizaines et enfin par leur chiffre des centaines. En pratique, cela signifie créer des compartiments (chiffres de 0 à 9) pour stocker les nombres avec des chiffres communs (par exemple, 10**1** et 8**1** partagent un chiffre commun à la place des unités). Ensuite, combiner tous les nombres dans leur ordre de compartiment (en commençant par la place des unités : 10**1**, 8**1**, 5**4**, 30**5**, **6**), avant de répéter le processus avec les chiffres des dizaines. Cela continue jusqu'à ce que les chiffres les plus élevés soient atteints (par exemple, **1**01 et **3**05 ont des chiffres des centaines).

En général, la complexité du **radix sort** est **O(kn)**.

* **n** est le nombre d'éléments
* **k** est le nombre moyen de chiffres par élément

La quantité de nombres à trier (**n**) est le nombre de fois où il est nécessaire de faire des dépôts dans ces compartiments de chiffres. Ainsi, la liste **101, 54, 305, 6, 81** nécessite au moins 5 dépôts. Plus les chiffres (**k**) de la collection de nombres sont élevés, plus il est nécessaire de répéter le processus de tri des unités, dizaines, centaines, milliers, etc. Ainsi, la liste **101, 54, 305, 6, 81** nécessite 5 dépôts pour les **unités**, **dizaines** et **centaines**. Cela représente un total de **3 x 5 = 15** dépôts.

### Conclusion

Apprendre des algorithmes avancés ne diminue pas l'importance des plus basiques. C'est à travers l'étude des algorithmes de base que vous apprenez ce que signifie rechercher ou trier, simplement. Et à partir de cette étude, vous pouvez commencer à comprendre les problèmes qui accompagnent ces algorithmes de base.

Rien n'est créé dans le vide. Tout commence avec une idée. Où cela mène ensuite est limité par l'esprit humain et ce que nous pouvons faire avec le monde physique qui nous entoure. C'est « toujours le premier jour », si vous choisissez d'élargir vos horizons.

### **Référence :**

[https://www.udemy.com/js-algorithms-and-data-structures-masterclass/](https://www.udemy.com/js-algorithms-and-data-structures-masterclass/)