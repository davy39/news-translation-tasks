---
title: 'Apprenez les bases de la programmation : les principales différences entre
  les ensembles et les tableaux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-09T20:58:34.000Z'
originalURL: https://freecodecamp.org/news/learn-your-coding-fundamentals-the-main-differences-between-sets-and-arrays-4a9ed29bfb2f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Anf4qCqSznUgoHTw7O6c2w.jpeg
tags:
- name: learning
  slug: learning
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Apprenez les bases de la programmation : les principales différences entre
  les ensembles et les tableaux'
seo_desc: 'By Anthony Sistilli

  A question I get a lot from my CS students at The Forge is why I often use sets
  instead of plain old arrays in interview problems.

  To answer that question, we have to understand the fundamental differences between
  a set and an arr...'
---

Par Anthony Sistilli

Une question que mes étudiants en informatique à [The Forge](https://theforge.ca/) me posent souvent est pourquoi j'utilise souvent des ensembles au lieu de simples tableaux dans les problèmes d'entretien.

Pour répondre à cette question, nous devons comprendre les différences fondamentales entre un ensemble et un tableau.

**Si vous êtes un apprenant visuel et préférez une explication vidéo, [voici une vidéo de 3 minutes](https://www.youtube.com/watch?v=2eeH-Outrz8&t=38s) qui explique la réponse (bien que moins en profondeur).**

Les tableaux étaient l'une des premières structures de données que j'ai apprises à utiliser.

Non seulement ils sont une structure de données fondamentale utilisée dans presque toutes les applications de codage, mais ils sont également assez faciles à comprendre.

Ce n'est que beaucoup plus tard dans ma carrière de développeur que j'ai été introduit à l'étrange, mais magique, cousin du tableau :

**L'ensemble.**

Les ensembles sont comme des tableaux... sauf qu'ils ne le sont pas.

#### Rappelons-nous rapidement comment fonctionne un tableau

Les tableaux :

* Sont ordonnés
* Ont des indices commençant à 0
* Peuvent contenir des éléments dupliqués
* Ont un temps de recherche O(n) lorsque vous recherchez un élément

#### Cependant, les ensembles se comportent un peu différemment

Les ensembles :

* Sont **non ordonnés** (dans presque tous les langages)
* Ont des **indices hachés**
* **NE peuvent PAS** contenir d'éléments dupliqués
* Ont un **temps de recherche O(1)** lorsque vous recherchez un élément

Examinons cela plus en détail.

### 1. Les ensembles insèrent par hachage

Les éléments dans un ensemble sont stockés de manière assez différente de ceux d'un tableau.

La manière dont un ensemble stocke ses éléments est par **hachage.**

#### Supposons que vous souhaitez stocker le caractère "A" dans un ensemble et un tableau.

Le tableau trouverait simplement le **prochain index disponible**, sauf indication contraire, et placerait l'élément à cet index.

![Image](https://cdn-media-1.freecodecamp.org/images/FwFrdUKwMFGwt5B01MWujBfopRwiSCap8Wcn)
_Notre "A" obtient un index de 0 puisqu'il s'agit du premier élément._

Avec le hachage, cependant, les choses semblent un peu différentes.

#### Comment fonctionne le hachage

**Le hachage** est l'acte de prendre une entrée (x), de la déformer avec une fonction de hachage spécifique (h), et d'obtenir une sortie finale (y).

En gros h(x) = (y)

Cela semble un peu confus, n'est-ce pas ?

Ne vous inquiétez pas ! Cela devrait éclaircir les choses.

Un exemple simple de fonction de hachage (h) pourrait être d'ajouter "asdf" à la fin de votre entrée (x).

Si (x) est "A" et ajouter "asdf" est (h), la sortie (y) serait simplement comme suit :

"A" + "asdf" → "Aasdf"

Donc "Aasdf" serait notre (y).

#### Donc, comment un ensemble utilise-t-il le hachage ?

Un ensemble utilise le hachage pour décider où stocker votre entrée (x).

En résumé, un ensemble prend votre entrée, la hache et la stocke à l'index qui correspond à l'entrée hachée, alias la sortie (y).

![Image](https://cdn-media-1.freecodecamp.org/images/mX-gjXZ-UBKN-KrZtS-D5TrPeWs6RMJpUzk-)
_Aasdf est l'index de notre élément "A"._

C'est la raison pour laquelle les ensembles sont non ordonnés dans la plupart des langages.

L'indexation des tableaux est facile, de 0 à n, donc vous pouvez facilement vous souvenir de ce qui vient ensuite.

Mais avec les fonctions de hachage complexes que la plupart des compilateurs utilisent, l'ordre dans lequel les éléments ont été insérés ne peut pas être retrouvé à moins de garder un mécanisme d'indexation secondaire.

### 2. Les ensembles ne peuvent pas contenir de doublons

C'est exact !

Un ensemble **ne peut contenir que des éléments uniques.**

Contrairement à ce que cela peut sembler, cela peut en réalité être extrêmement utile dans de nombreuses situations, y compris dans les [questions d'entretien de Google](https://medium.freecodecamp.org/solving-a-google-interview-question-python-2-code-included-eddefcaeffb2).

Pourquoi fait-il cela, me demanderez-vous ?

Eh bien, à cause du hachage !

Puisque ma fonction de hachage (h) restera cohérente pendant l'exécution de mon programme, entrer la même entrée (x) donnera toujours la même sortie (y).

Cela signifie que si j'essayais d'insérer un second "A", ma fonction de hachage produirait la même adresse que le premier "A", et **elle le remplacerait simplement !**

![Image](https://cdn-media-1.freecodecamp.org/images/IyMXWH3PLwT0wcCwoRflRpnwCgIVLQSFIQnS)

Avec un tableau, il ajouterait simplement le second "A" au prochain index disponible.

### 3. Les ensembles ont un temps de recherche O(1)

Supposons que vous avez un tableau de _n_ éléments, où _n_ est un grand nombre, et que vous souhaitez voir si "A" existe dans ce tableau.

Eh bien, dans le pire des cas, "A" n'existe pas.

Et pour le découvrir, vous devriez parcourir tous les _n_ éléments !

![Image](https://cdn-media-1.freecodecamp.org/images/KwkpUKEYPgs4TdrbGRCgfqdSayyFRCJ33eWC)
_TABLEAU. DE. FORTUNE !_

**Cela donne à un tableau une complexité temporelle de O(n) lorsqu'il s'agit de rechercher un élément.**

#### Nous pouvons économiser beaucoup de temps avec un ensemble

Si nous voulions trouver si un élément existe ou non dans notre ensemble, tout ce que nous avons à faire est de hacher cet élément et de vérifier l'index !

Rappelez-vous : L'index où un élément est stocké est lié à l'élément lui-même.

Par conséquent, si nous voulions voir si "A" existe dans notre ensemble, nous devrions simplement le hacher (+ "asdf") et vérifier cet index !

Puisque ce processus prendra toujours un nombre constant d'opérations, peu importe la taille de l'ensemble, il a une complexité temporelle constante.

**Cela signifie qu'un ensemble a une complexité temporelle de O(1) lorsqu'il s'agit de rechercher un élément... Ce qui est une énorme amélioration !**

### Pouvez-vous penser à des situations où cela est utile ?

Si vous ne pouvez pas, consultez cette [question d'entretien de Google](https://medium.freecodecamp.org/solving-a-google-interview-question-python-2-code-included-eddefcaeffb2) où un ensemble fait toute la différence !

Merci d'avoir lu !

.a

**P.S — Pour plus de tutoriels sur les structures de données et les algorithmes, et pour la préparation aux entretiens, consultez [www.TheForge.ca!](http://www.TheForge.ca!)**

**Nous aidons les étudiants et les nouveaux diplômés à décrocher leur emploi de rêve en logiciel !**