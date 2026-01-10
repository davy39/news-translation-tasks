---
title: Orthogonalité en génie logiciel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-18T01:18:00.000Z'
originalURL: https://freecodecamp.org/news/orthogonality-in-software-engineering
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dca740569d1a4ca39a9.jpg
tags:
- name: Software Engineering
  slug: software-engineering
- name: toothbrush
  slug: toothbrush
seo_title: Orthogonalité en génie logiciel
seo_desc: "Orthogonality\nIn software engineering, a system is considered orthogonal\
  \ if changing one of its components changes the state of that component only. \n\
  For instance, consider a program with three variables: a, b, and c. Changing the\
  \ value of a should n..."
---

## **Orthogonalité**

En génie logiciel, un système est considéré comme orthogonal si la modification de l'un de ses composants ne modifie que l'état de ce composant.

Par exemple, considérons un programme avec trois variables : a, b et c. Changer la valeur de a ne devrait pas changer la valeur de b ou c, à condition qu'elles soient indépendantes.

Cette propriété est particulièrement cruciale lors du débogage d'un programme, car on s'appuie sur la réduction du nombre de parties mobiles d'un programme pour identifier la cause racine du problème.

Voir la citation suivante d'Eric S. Raymond dans "L'Art de la programmation UNIX" :

> L'orthogonalité est l'une des propriétés les plus importantes qui peuvent aider à rendre même les conceptions complexes compactes. Dans une conception purement orthogonale, les opérations n'ont pas d'effets secondaires ; chaque action (qu'il s'agisse d'un appel d'API, d'une invocation de macro ou d'une opération de langage) ne change qu'une seule chose sans affecter les autres. Il n'y a qu'une seule façon de changer chaque propriété du système que vous contrôlez.

L'orthogonalité est un principe de conception logicielle pour écrire des composants de manière à ce que la modification d'un composant n'affecte pas les autres composants. C'est la combinaison de deux autres principes, à savoir la forte cohésion et le faible couplage.

C'est en fait un terme emprunté aux mathématiques. Par exemple, deux lignes sont orthogonales si elles sont perpendiculaires. En conception logicielle, deux composants sont orthogonaux si une modification de l'un n'affecte pas l'autre.

L'application de ce concept aux classes ou à d'autres sections de code entraîne un couplage réduit. Pour être orthogonales, deux classes ne doivent pas dépendre de l'implémentation de l'autre. Elles ne doivent pas non plus partager de données globales. La modification des détails internes d'une classe n'affecte pas l'autre classe. Les composants doivent être indépendants et n'avoir qu'une seule responsabilité.

Considérons une méthode qui lit une liste de nombres à partir d'un fichier et les retourne dans l'ordre trié. Maintenant, les exigences changent et les nombres sont dans une base de données. Modifier cette méthode pour accéder à la base de données obligerait le code client à changer. Si cela était deux méthodes différentes, alors une nouvelle source n'affecterait pas la méthode de tri. Seul le code client devrait connaître la source des nombres.

## Forte Cohésion

À l'intérieur d'un composant logiciel, le code doit être fortement connecté. Cela indique que le code est correctement divisé.

Si un composant avait deux parties ou plus relativement déconnectées, cela pourrait indiquer que ces parties devraient être dans un composant différent, ou dans leur propre composant.

## Faible Couplage

Entre les composants logiciels, il devrait y avoir peu de connexions. Si deux composants sont fortement couplés, cela pourrait indiquer qu'ils doivent être un seul composant, ou qu'ils doivent être divisés différemment en plus de composants.