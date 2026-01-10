---
title: Qu'est-ce que les langages d'assemblage ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-05T00:51:00.000Z'
originalURL: https://freecodecamp.org/news/what-are-assembly-languages
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e31740569d1a4ca3bd0.jpg
tags:
- name: programming languages
  slug: programming-languages
- name: toothbrush
  slug: toothbrush
seo_title: Qu'est-ce que les langages d'assemblage ?
seo_desc: 'Assembly Language is the interface between higher level languages (C++,
  Java, etc) and machine code (binary). For a compiled language, the compiler transforms
  higher level code into assembly language code.

  Every family of CPUs define their own Instru...'
---

Le langage d'assemblage est l'interface entre les langages de haut niveau (C++, Java, etc.) et le code machine (binaire). Pour un langage compilé, le compilateur transforme le code de haut niveau en code en langage d'assemblage.

Chaque famille de CPU définit sa propre Architecture de Jeu d'Instructions (ISA), un ensemble d'instructions de base que le CPU peut exécuter sans nécessiter de traduction ou de transformation supplémentaire. Le compilateur décompose les instructions composites de haut niveau en opérations disponibles dans l'ISA.

Certaines des ISA les plus courantes utilisées aujourd'hui incluent MIPS, ARM, Intel x86, RISC-V.

Les assembleurs décomposent les instructions d'assemblage en leurs représentations binaires respectives et remplacent les adresses génériques du code d'assemblage par des adresses explicites de registres et de mémoire de votre ordinateur.

Le code où le temps d'exécution et le contrôle sont cruciaux peut être écrit directement en assembleur. Cela, cependant, prolonge le temps de développement et rend le développement plus difficile. Il convient également de noter qu'une grande quantité de recherches a été consacrée à l'optimisation des compilateurs pour le code généré automatiquement.

Le langage d'assemblage est principalement utilisé dans les situations suivantes :

* Il est nécessaire d'utiliser des instructions CPU non disponibles dans les langages de haut niveau.
* Il n'existe pas de langage de haut niveau pour programmer certains types de processeurs.
* Implémentation d'un compilateur pour un langage de haut niveau sur une nouvelle ISA.

![Image des niveaux de code](https://raw.githubusercontent.com/colbybanbury/assemblyPicture/master/Screenshot%20from%202017-10-14%2014-03-06.png)

####