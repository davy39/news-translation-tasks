---
title: Un pas vers l'informatique en tant que science
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T21:02:36.000Z'
originalURL: https://freecodecamp.org/news/a-step-towards-computing-as-a-science-algorithms-data-structures-4c0e2d6ae79a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*494Zt3R4wuX6jGEE93bGyg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Un pas vers l'informatique en tant que science
seo_desc: 'By Yung L. Leung

  Simple Algorithms & Data Structures in JS


  _Photo by J. Craig on [Un-splash](https://unsplash.com/photos/HH4WBGNyltc" rel="noopener"
  target="blank" title=")

  An algorithm is the steps taken to solve a problem. A data structure is data...'
---

Par Yung L. Leung

#### Algorithmes simples et structures de données en JS

![Image](https://cdn-media-1.freecodecamp.org/images/SzQAdm6hPSs6JDis5HmlTUsfRMeAn3gR3Q6z)
_Photo par J. Craig sur [Un-splash](https://unsplash.com/photos/HH4WBGNyltc" rel="noopener" target="_blank" title=")_

Un **algorithme** est l'ensemble des étapes nécessaires pour résoudre un problème. Une **structure de données** est une organisation de données permettant un accès efficace. Vous pouvez utiliser un algorithme pour résoudre toutes sortes de problèmes (par exemple, rechercher une donnée ou trier une collection de données) pour une structure de données donnée.

Ainsi, en ce qui concerne les ordinateurs, un **algorithme** est la méthode utilisée pour effectuer une tâche (par exemple, recherche linéaire, recherche binaire, tri à bulles, tri par sélection, tri par insertion, etc.), tandis qu'une **structure de données** est l'objet sur lequel vous appliquez cette méthode (par exemple, tableau, objets à paires clé-valeur, etc.). Vous pouvez donc rechercher, trier ou créer méthodiquement un ensemble de données organisé.

### Une structure de données simple

#### Tableau

Un **tableau** est comme une série de boîtes numérotées (**index**) allant du plus bas (0) au plus haut (2). Chaque boîte est fixe et reste ordonnée selon son étiquette.

![Image](https://cdn-media-1.freecodecamp.org/images/1b9YMqQJlydsZT6RkSa6w0EhBWycwnEwBvxe)

Vous pouvez sauter à n'importe quelle boîte étiquetée pour voir son contenu (nomTableau[2]), ajouter du contenu ou remplacer son contenu (nomTableau[2] = "Sherlock Holmes"). Vous pouvez **ajouter** une nouvelle boîte de contenu à la fin de votre collection (nomTableau.push("Les Mémoires de Sherlock Holmes")).

![Image](https://cdn-media-1.freecodecamp.org/images/GBmaTMT21U4XkgINEpi6zbABzdSTUL3HOgQP)

Cela donne à la nouvelle boîte l'étiquette suivante dans la séquence (3). Pour revenir à votre collection de boîtes d'origine, vous pouvez **retirer** la dernière boîte (nomTableau.pop()).

Vous pouvez également **retirer** la première boîte (nomTableau.shift()), mais cela nécessitera de réétiqueter toutes les autres boîtes.

![Image](https://cdn-media-1.freecodecamp.org/images/SaNd1RwP9IGtFhZ8JlUXmUoYgSZbTSw2-ApI)

Votre collection Sherlock Holmes est maintenant dans la boîte étiquetée 1. Si vous **insérez** une nouvelle boîte de contenu au début de votre collection, vous pouvez ajouter une nouvelle boîte de contenu (nomTableau.unshift("Dr. Strange")).

![Image](https://cdn-media-1.freecodecamp.org/images/MNkPBN3GvJN-TxmukjSFaN7s6iDVRJwC0o0j)

Cela nous donne notre collection Dr. Strange & Sherlock Holmes dans les boîtes étiquetées 0 & 2.

### Recherche dans une structure de données

#### Recherche linéaire

Une **recherche linéaire** est comme marcher le long d'un tableau de boîtes (par exemple, 0 — 16) et ouvrir chaque couverture pour voir si son contenu est ce que vous cherchez (par exemple, 37).

![Image](https://cdn-media-1.freecodecamp.org/images/pxaLBaOpULERV7f1iJJeRG14Rm5ROMx62Sq5)
_[source](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif" rel="noopener" target="_blank" title=")_

Ainsi, pour un index allant du début d'une collection (disons 0) à sa fin (sa longueur moins un), nous pouvons rechercher notre contenu souhaité dans une boîte et passer à la suivante. Nous pouvons incrémenter d'une boîte à la suivante jusqu'à trouver une correspondance.

#### Recherche binaire

Une **recherche binaire** est comme rechercher dans un tableau de boîtes, dont le contenu est ordonné (par exemple, numérique ou alphabétique), en sautant à mi-chemin vers une boîte centrale et en vérifiant son contenu pour l'élément souhaité. Si vous avez dépassé, vous **sautez en arrière**, à mi-chemin entre votre position actuelle et le point de départ. Sinon, vous **sautez en avant**, à mi-chemin entre votre position actuelle et le point final.

![Image](https://cdn-media-1.freecodecamp.org/images/NnKWfGNACsLaYbS0WvBCI4Ipx0k7Ojmoa4DP)
_[source](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif" rel="noopener" target="_blank" title=")_

Ainsi, ce que vous pouvez faire est de garder une trace de votre index bas (initialement **0**), milieu (**8**) et haut (initialement **16**). La position du milieu est toujours la moitié de la somme des index bas et haut. Vous vérifiez la boîte du milieu pour une correspondance (par exemple, **37**). Si c'est moins que ce que vous attendiez (< 37), alors vous sautez en avant. Vous réinitialisez votre index bas pour qu'il dépasse votre position actuelle du milieu de un (8 + 1 = 9). Ensuite, vous recalculez une nouvelle position du milieu ((9 + 16) / 2 **≈** 12).

**En d'autres termes, vous pouvez sauter en avant dans votre recherche en réinitialisant votre index bas et en recalculant un nouvel index du milieu. Inversement, si vous avez dépassé, vous pouvez sauter en arrière en réinitialisant votre index haut et en recalculant un nouvel index du milieu.**

Contrairement à la recherche linéaire, ce type est binaire. Vous devinez toujours si votre élément est situé dans la première ou la deuxième moitié de votre collection de boîtes.

### Tri d'une structure de données

#### Tri à bulles

Un **tri à bulles** est le tri d'une collection en échangeant continuellement une valeur plus élevée avec une valeur adjacente plus faible, ce qui a pour effet de faire remonter la valeur la plus élevée à la surface.

![Image](https://cdn-media-1.freecodecamp.org/images/HawSOQIini2SfP9RayRvllpjAXrMxQMJi3yV)
_[source](https://upload.wikimedia.org/wikipedia/commons/5/54/Sorting_bubblesort_anim.gif" rel="noopener" target="_blank" title=")_

Ainsi, pour la longueur de votre collection, en commençant à l'index 0, vous échangez le contenu d'un index actuel (i) avec le contenu d'un index ultérieur (i + 1), si le premier est plus grand en valeur. Ensuite, vous passez à l'ensemble suivant d'index (i + 1 vs. i + 2), et ainsi de suite.

À un moment donné, vous arriverez à une boîte contenant la valeur la plus élevée de votre collection. Et ainsi, ce sera le contenu qui continuera à être échangé vers l'avant. D'où l'effet de bulle vers le haut. Vous répétez ce processus jusqu'à ce que votre collection soit triée, de la plus faible à la plus élevée en valeur.

Puisque la dernière boîte de chaque itération se terminera par la valeur la plus élevée, vous répétez le processus en excluant les dernières boîtes.

#### Tri par sélection

Un **tri par sélection** est le tri d'une collection en **sélectionnant** continuellement la valeur la plus faible et en l'échangeant à une extrémité.

![Image](https://cdn-media-1.freecodecamp.org/images/bbeO5vQWD0Q6Dl6tRXVsHMoXjwtFF109Z99H)
_[source](https://codepumpkin.com/selection-sort-algorithms/" rel="noopener" target="_blank" title=")_

Ainsi, ici, vous parcourez toute votre collection pour trouver la valeur la plus faible. Une fois trouvée, vous échangez son contenu avec la boîte étiquetée avec l'index le plus bas (initialement index 0). Vous répétez ce processus en commençant par l'index suivant le plus bas (index 1) puisque votre valeur la plus faible est dans sa position correcte. À chaque itération, la plage de longueur pour votre scan diminue de 1, jusqu'à ce que toute votre collection soit triée de la plus faible à la plus élevée en valeur.

#### Tri par insertion

Un **tri par insertion** est le tri d'une collection en **insérant** chaque valeur rencontrée dans sa position correcte.

![Image](https://cdn-media-1.freecodecamp.org/images/q27NtXV17832eN--MmZuUaCUiY4r1QExDI-R)
_[source](https://gfycat.com/densebaggyibis" rel="noopener" target="_blank" title=")_

Ainsi, plutôt que de parcourir toute une collection par itération (par exemple, tri à bulles et tri par sélection), vous commencez aux index 0 et 1 pour comparer leurs valeurs. Si la valeur ultérieure est plus faible, si le contenu de l'index 1 est inférieur en valeur à celui de l'index 0, vous échangez leurs contenus. Vous passez à la boîte suivante à l'index 2 et comparez avec vos boîtes précédemment triées (index 1, puis index 0).

Chaque fois que vous rencontrez une valeur plus élevée, vous échangez son contenu vers la droite. Lorsque vous avez trouvé la position correcte, vous insérez le contenu (précédemment à l'index 2) dans la boîte correcte. Ainsi, c'est comme si vous "retiriez" le contenu d'une boîte ultérieure et que vous alliez vers une boîte antérieure.

Si la boîte antérieure a une valeur plus élevée que ce que vous tenez, vous déplacez son contenu vers la boîte ultérieure. Vous continuez à faire cela jusqu'à ce que vous trouviez l'endroit correct pour insérer ce que vous tenez.

### Une autre structure de données simple

#### Objets à paires clé-valeur

Un **objet à paires clé-valeur** est comme un ensemble de boîtes de dépôt non étiquetées. Chaque clé unique ouvre une pièce spécifique de données. Contrairement à un tableau, il s'agit de données non ordonnées accessibles par des clés uniques.

![Image](https://cdn-media-1.freecodecamp.org/images/exHs5jS2Faf9ymhaXL2954GoGeaPAFp78oP2)
_[source](https://cdn.shopify.com/s/files/1/1147/6518/products/safeandvaultstore-sdbx9-safe-deposit-boxes_large.jpg?v=1495593363" rel="noopener" target="_blank" title=")_

Ainsi, vous accédez à une boîte de dépôt en utilisant sa clé (nomObjet['s']), changez son contenu ou créez une clé qui ouvre un contenu spécifié (nomObjet['s'] = "Sherlock Holmes"). Vous pouvez accéder à toutes les clés créées ou à tout le contenu stocké dans toutes vos boîtes de dépôt (Object.keys(nomObjet) ou Object.values(nomObjet)).

### Conclusion

Les **algorithmes** de base (recherches linéaire et binaire ; tris à bulles, par sélection et par insertion) et les **structures de données** (tableaux et objets clé-valeur) soulèvent des questions de temps et d'espace concernant la gestion des données. Les considérations du **temps** nécessaire pour rechercher, trier ou accéder aux données et de l'espace **mémoire** requis pour ces processus peuvent élever un développeur logiciel de la programmation informatique à la science informatique. Cela vous fait passer de la pensée de la programmation pour l'efficacité à la programmation pour l'efficience.