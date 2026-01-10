---
title: Notation Big O expliquée avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/big-o-notation-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cf0740569d1a4ca3502.jpg
tags:
- name: algorithms
  slug: algorithms
- name: '#big o notation'
  slug: big-o-notation
- name: data structures
  slug: data-structures
- name: toothbrush
  slug: toothbrush
seo_title: Notation Big O expliquée avec des exemples
seo_desc: 'Big O notation is a way to describe the speed or complexity of a given
  algorithm. If your current project demands a predefined algorithm, it''s important
  to understand how fast or slow it is compared to other options.

  What is Big O notation and how do...'
---

La notation Big O est une manière de décrire la vitesse ou la complexité d'un algorithme donné. Si votre projet actuel nécessite un algorithme prédéfini, il est important de comprendre à quelle vitesse ou lenteur il est comparé à d'autres options.

## Qu'est-ce que la notation Big O et comment fonctionne-t-elle ?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31781171-74c6b48a-b500-11e7-9626-f715b37b10f0.png)

Simplement dit, la notation Big O vous indique le nombre d'opérations qu'un algorithme effectuera. Elle tire son nom du "Big O" littéral devant le nombre estimé d'opérations.

Ce que la notation Big O ne vous indique pas, c'est la vitesse de l'algorithme en secondes. Il y a bien trop de facteurs qui influencent le temps qu'un algorithme prend pour s'exécuter. Au lieu de cela, vous utiliserez la notation Big O pour comparer différents algorithmes en fonction du nombre d'opérations qu'ils effectuent.

### Big O établit un temps d'exécution dans le pire des cas

Imaginez que vous êtes un enseignant avec une élève nommée Jane. Vous souhaitez trouver ses dossiers, alors vous utilisez un algorithme de recherche simple pour parcourir la base de données de votre district scolaire.

Vous savez que la recherche simple prend O(n) fois pour s'exécuter. Cela signifie que, dans le pire des cas, vous devrez rechercher chaque dossier (représenté par n) pour trouver celui de Jane.

Mais lorsque vous exécutez la recherche simple, vous trouvez que les dossiers de Jane sont la toute première entrée dans la base de données. Vous n'avez pas à regarder chaque entrée – vous l'avez trouvé du premier coup.

_Cet algorithme a-t-il pris O(n) temps ? Ou a-t-il pris O(1) temps parce que vous avez trouvé les dossiers de Jane du premier coup ?_

Dans ce cas, O(1) est le meilleur scénario – vous avez eu de la chance que les dossiers de Jane soient en haut. Mais la notation Big O se concentre sur le pire scénario, qui est O(n) pour la recherche simple. C'est une assurance que la recherche simple ne sera jamais plus lente que O(n) temps.

### Les temps d'exécution des algorithmes croissent à des rythmes différents

Supposons qu'il faille 1 milliseconde pour vérifier chaque élément dans la base de données du district scolaire.

Avec la recherche simple, si vous devez vérifier 10 entrées, cela prendra 10 ms pour s'exécuter. Mais avec l'_algorithme de recherche binaire_, vous n'avez besoin de vérifier que 3 éléments, ce qui prend 3 ms pour s'exécuter.

Dans la plupart des cas, la liste ou la base de données que vous devez rechercher comportera des centaines ou des milliers d'éléments.

S'il y a 1 milliard d'éléments, l'utilisation de la recherche simple prendra jusqu'à 1 milliard de ms, soit 11 jours. En revanche, l'utilisation de la recherche binaire ne prendra que 32 ms dans le pire des cas :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31781165-723a053c-b500-11e7-937c-7b33db281efe.png)

Clairement, les temps d'exécution pour la recherche simple et la recherche binaire ne croissent pas presque au même rythme. À mesure que la liste des entrées s'agrandit, la recherche binaire ne prend qu'un peu plus de temps pour s'exécuter. Le temps d'exécution de la recherche simple croît exponentiellement à mesure que la liste des entrées augmente.

C'est pourquoi il est si important de savoir comment le temps d'exécution augmente en relation avec la taille d'une liste. Et c'est exactement là où la notation Big O est si utile.

### La notation Big O montre le nombre d'opérations

Comme mentionné ci-dessus, la notation Big O ne montre pas le _temps_ qu'un algorithme prendra pour s'exécuter. Au lieu de cela, elle montre le nombre d'opérations qu'il effectuera. Elle vous indique à quelle vitesse un algorithme croît et vous permet de le comparer avec d'autres.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/31781175-768c208e-b500-11e7-9718-e632d1391e2d.png)

Voici quelques algorithmes courants et leurs temps d'exécution en notation Big O :

| Notation Big O | Exemple d'algorithme |
| :---: | :---: |
| O(log n) | Recherche binaire |
| O(n) | Recherche simple |
| O(n * log n)  | Quicksort |
| O(n2) | Tri par sélection |
| O(n!) | Problème du voyageur de commerce |

Maintenant, vous en savez assez pour être dangereux avec la notation Big O. Allez-y et commencez à comparer des algorithmes.