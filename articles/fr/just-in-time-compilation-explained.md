---
title: La compilation Just-in-Time expliquée
date: '2020-02-01T00:00:00.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/just-in-time-compilation-explained
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d05740569d1a4ca357b.jpg
tags:
- name: compilers
  slug: compilers
- name: Computer Science
  slug: computer-science
- name: toothbrush
  slug: toothbrush
seo_desc: 'Just-in-time compilation is a method for improving the performance of interpreted
  programs. During execution the program may be compiled into native code to improve
  its performance. It is also known as dynamic compilation.

  Dynamic compilation has som...'
---


La compilation Just-in-Time (JIT) est une méthode permettant d'améliorer les performances des programmes interprétés. Pendant l'exécution, le programme peut être compilé en code natif pour améliorer ses performances. Elle est également connue sous le nom de compilation dynamique.

<!-- more -->

La compilation dynamique présente certains avantages par rapport à la compilation statique. Lors de l'exécution d'applications Java ou C#, l'environnement d'exécution (runtime) peut profiler l'application pendant qu'elle tourne. Cela permet de générer un code plus optimisé. Si le comportement de l'application change en cours d'exécution, l'environnement d'exécution peut recompiler le code.

Certains des inconvénients incluent des délais de démarrage et la surcharge (overhead) liée à la compilation pendant l'exécution. Pour limiter cette surcharge, de nombreux compilateurs JIT ne compilent que les chemins de code qui sont fréquemment utilisés.

## Présentation générale

Traditionnellement, il existe deux méthodes pour convertir le code source dans un format utilisable sur une plateforme. La compilation statique convertit le code dans un langage spécifique à une plateforme. Un interpréteur exécute directement le code source.

La compilation JIT tente de tirer parti des avantages des deux approches. Pendant que le programme interprété s'exécute, le compilateur JIT détermine le code le plus fréquemment utilisé et le compile en code machine. Selon le compilateur, cela peut se faire au niveau d'une méthode ou d'une section de code plus restreinte.

La compilation dynamique a été décrite pour la première fois dans un article de J. McCarthy sur LISP en 1960.

La compilation Just-In-Time, JIT, ou traduction dynamique, est une compilation effectuée pendant l'exécution d'un programme. C'est-à-dire au moment du run time, par opposition à une compilation préalable à l'exécution. Ce qui se produit est la traduction en code machine. Les avantages d'un JIT résident dans le fait que, puisque la compilation a lieu au moment de l'exécution, un compilateur JIT a accès aux informations dynamiques du runtime, ce qui lui permet de réaliser de meilleures optimisations (comme l'inlining de fonctions).

Ce qu'il est important de comprendre à propos de la compilation JIT, c'est qu'elle va compiler le bytecode en instructions de code machine de la machine hôte. Cela signifie que le code machine résultant est optimisé pour l'architecture CPU de la machine sur laquelle il s'exécute.

Voici quelques exemples de compilateurs JIT : la JVM (Java Virtual Machine) pour Java et le CLR (Common Language Runtime) pour C#.

## Historique

Au début, un compilateur était chargé de transformer un langage de haut niveau (défini comme un niveau supérieur à l'assembleur) en code objet (instructions machine), qui était ensuite lié (par un linker) pour former un exécutable.

À un certain stade de l'évolution des langages, les compilateurs compilaient un langage de haut niveau en pseudo-code, qui était ensuite interprété (par un interpréteur) pour exécuter votre programme. Cela a éliminé le code objet et les exécutables, et a permis à ces langages d'être portables sur plusieurs systèmes d'exploitation et plateformes matérielles. Pascal (qui compilait en P-Code) fut l'un des premiers ; Java et C# sont des exemples plus récents. Finalement, le terme P-Code a été remplacé par bytecode, car la plupart des pseudo-opérations font un octet de long.

Un compilateur Just-In-Time (JIT) est une fonctionnalité de l'interpréteur runtime qui, au lieu d'interpréter le bytecode à chaque fois qu'une méthode est invoquée, va compiler le bytecode en instructions de code machine de la machine hôte, puis invoquer ce code objet à la place. Idéalement, l'efficacité de l'exécution du code objet compensera l'inefficacité de la recompilation du programme à chaque exécution.

### Scénario typique

Le code source est entièrement converti en code machine.

### Scénario JIT

Le code source sera converti en une structure de type langage assembleur [par exemple, l'IL (Intermediate Language) pour C#, le ByteCode pour Java].

Le code intermédiaire n'est converti en langage machine que lorsque l'application en a besoin, c'est-à-dire que seuls les codes requis sont convertis en code machine.

## Comparaison JIT vs non-JIT

Avec le JIT, tout le code n'est pas converti en code machine immédiatement. Une partie nécessaire du code est d'abord convertie en code machine, puis si une méthode ou une fonctionnalité appelée n'est pas encore en code machine, elle sera alors transformée, ce qui réduit la charge sur le CPU. Comme le code machine est généré au moment de l'exécution, le compilateur JIT produira un code machine optimisé pour l'architecture CPU de la machine hôte.

Voici quelques exemples de JIT :

-   Java : JVM (Java Virtual Machine)
-   C# : CLR (Common Language Runtime)
-   Android : DVM (Dalvik Virtual Machine) ou ART (Android RunTime) dans les versions plus récentes

La Java Virtual Machine (JVM) exécute le bytecode et maintient un compteur du nombre de fois qu'une fonction est exécutée. Si ce compteur dépasse une limite prédéfinie, le JIT compile le code en langage machine qui peut être directement exécuté par le processeur (contrairement au cas normal où `javac` compile le code en bytecode, puis `java`, l'interpréteur, interprète ce bytecode ligne par ligne pour le convertir en code machine et l'exécuter).

De plus, la prochaine fois que cette fonction est sollicitée, le même code compilé est exécuté à nouveau, contrairement à l'interprétation normale où le code est réinterprété ligne par ligne. Cela rend l'exécution plus rapide.