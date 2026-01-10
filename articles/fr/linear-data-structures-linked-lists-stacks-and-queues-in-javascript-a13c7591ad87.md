---
title: 'Structures de données linéaires : listes chaînées, piles et files d''attente
  en JS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T14:09:52.000Z'
originalURL: https://freecodecamp.org/news/linear-data-structures-linked-lists-stacks-and-queues-in-javascript-a13c7591ad87
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AlfSJzw3bKoEHHaO9oiMqQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'Structures de données linéaires : listes chaînées, piles et files d''attente
  en JS'
seo_desc: 'By Yung L. Leung

  Building from Simple Algorithms & Data Structures in JS, here we’ll look at data
  structures beyond arrays and key-value objects, beyond “labelled & deposit” boxes.
  Like a road along a path, linked lists, stacks & queues are direct wa...'
---

Par Yung L. Leung

En partant de [Simple Algorithms & Data Structures in JS](https://medium.freecodecamp.org/a-step-towards-computing-as-a-science-algorithms-data-structures-4c0e2d6ae79a?source=friends_link&sk=1291dffce9f32b30f36339d59a66e12c), nous allons examiner des structures de données au-delà des tableaux et des objets clé-valeur, au-delà des boîtes "étiquetées et déposées". Comme une route le long d'un chemin, les **listes chaînées**, les **piles** et les **files d'attente** sont des moyens directs de passer d'une unité de données à la suivante.

### Listes chaînées

Une **liste chaînée** est comme un ensemble de boîtes enchaînées ensemble et stockées dans une pièce sombre. Pour accéder à une boîte, il faut commencer à une extrémité (tête ou queue) et suivre les liens, d'une boîte à la suivante. En arrivant à une boîte, vous êtes dirigé vers la direction de la boîte suivante. **Il n'y a pas d'index** pour servir de guide pour sauter à une boîte quelconque.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kaShgNb9EtR7ps6odxP3QA.png)
_[source](https://www.blackline.com/blog/rpa/blockchain-finance-6-things/" rel="noopener" target="_blank" title=")_

Vous pouvez facilement **unshift** ou **push** des "boîtes" à la tête ou à la queue de la liste chaînée. Vous pouvez également facilement **shift** ou **pop** des "boîtes" de la tête ou de la queue. La tête ou la queue sont facilement accessibles. Mais, pour **insérer** ou **supprimer** des "boîtes" le long du corps de cette liste chaînée, pour **définir** des éléments dans une "boîte" qui est au-delà de la tête ou de la queue, est plus difficile. Cela nécessite de commencer à la tête (ou à la queue) et de passer d'une "boîte" actuelle à la suivante, avant de pouvoir **obtenir** votre "boîte" souhaitée.

Une **liste simplement chaînée** est une liste chaînée à sens unique. Cela signifie que vous ne pouvez vous déplacer que vers l'avant, de la tête à la queue. La complexité pour **unshift** et **shift** est constante (**O(1)**). Cela est dû au fait que l'ajout d'une "boîte" ou sa suppression du début nécessite uniquement l'accès à la tête de la liste. La complexité pour **push** une "boîte" à la fin est également **O(1)** pour une raison similaire, la queue est immédiatement accessible.

Mais, pour **pop** la queue, il faut réassigner une nouvelle queue, qui n'est accessible qu'en se déplaçant vers l'avant à partir de la tête, d'où une complexité linéaire (**O(n)**). Un nombre **n** de "boîtes" nécessite **n** étapes (opérations) pour atteindre l'avant-dernière "boîte" et la réassigner comme nouvelle queue. De même, pour **insérer/supprimer** une "boîte", ou pour **obtenir/définir** des éléments dans une "boîte" le long du corps d'une liste, il faut parcourir à partir de la tête, et donc leurs complexités sont en général **O(n)**.

Une **liste doublement chaînée** est une liste chaînée à double sens. Cela signifie que vous pouvez vous déplacer vers l'avant à partir de la tête ou de la queue. Un avantage est que la tête et la queue sont facilement accessibles pour ajouter des "boîtes" ou en supprimer. La complexité pour **unshift**, **shift**, **push** ou **pop** est **O(1)**. La nouvelle queue requise pour supprimer une queue est accessible à partir de la queue actuelle.

Un autre avantage de pouvoir voyager à partir de deux points de départ différents (tête ou queue) est que pour **insérer/supprimer** une "boîte" ou pour **obtenir/définir** des "éléments" dans une "boîte" le long du corps d'une liste prend la moitié du temps d'une liste simplement chaînée. C'est-à-dire que leurs complexités sont **la moitié de O(n)**. Si la "boîte" ou l'"élément" est situé dans la deuxième moitié de la liste, le voyage à partir de la queue ne nécessitera pas de parcourir la première moitié de la liste. L'inverse est également vrai. Bien qu'un **O(1/2 n)** tende à être simplifié en **O(n)**.

### Piles

Une **pile** est un tas d'éléments soigneusement empilés les uns sur les autres. Un nouvel élément peut être **poussé** sur le dessus de la pile, un à la fois, construisant la hauteur de la pile. Inversement, chaque élément peut être **retiré**, un à la fois, du sommet de la pile. Le dernier élément entré est toujours le premier élément sorti (**LIFO**).

![Image](https://cdn-media-1.freecodecamp.org/images/1*H0FjbIyvwvDMrw0OCqyCwQ.jpeg)
_Annie Spratt de [UnSplash](https://unsplash.com/photos/thI_CZAB0MY" rel="noopener" target="_blank" title=")_

Puisqu'une pile fonctionne selon un processus LIFO, la complexité pour **pousser** un élément au sommet de la pile ou pour le **retirer** est une constante de **O(1)**. Le sommet de la pile est facilement accessible.

### Files d'attente

Une **file d'attente** est une ligne d'éléments, soigneusement disposés les uns à côté des autres. Un nouvel élément peut être **enfilé** à la fin de la ligne, un à la fois, allongant la ligne. Inversement, chaque élément peut être **défiler** du début de la ligne, un à la fois. Le premier élément entré est toujours le premier élément sorti (**FIFO**).

![Image](https://cdn-media-1.freecodecamp.org/images/1*hRd8rEZW87TbU1_uc6xCQw.jpeg)
_[source](http://www.communityvoiceks.com/news/wichita_news/sedgwick-county-treasurer-launches-new-virtual-waiting-line-process/article_e1fce0c2-f05f-11e5-979b-93e21092f3d5.html" rel="noopener" target="_blank" title=")_

Puisque le début et la fin de la ligne sont facilement accessibles, les opérations **enqueue** et **dequeue** d'une file d'attente ont une complexité de **O(1)**.

Merci d'avoir lu !

### Référence :

[https://www.udemy.com/js-algorithms-and-data-structures-masterclass/](https://www.udemy.com/js-algorithms-and-data-structures-masterclass/)