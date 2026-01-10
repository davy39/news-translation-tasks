---
title: 'Langages de programmation interprétés vs compilés : quelle est la différence
  ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-10T17:10:00.000Z'
originalURL: https://freecodecamp.org/news/compiled-versus-interpreted-languages
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e00740569d1a4ca3acf.jpg
tags:
- name: programming languages
  slug: programming-languages
seo_title: 'Langages de programmation interprétés vs compilés : quelle est la différence
  ?'
seo_desc: "Every program is a set of instructions, whether it’s to add two numbers\
  \ or send a request over the internet. Compilers and interpreters take human-readable\
  \ code and convert it to computer-readable machine code. \nIn a compiled language,\
  \ the target mac..."
---

Chaque programme est un ensemble d'instructions, qu'il s'agisse d'additionner deux nombres ou d'envoyer une requête sur internet. Les compilateurs et les interpréteurs prennent le code lisible par l'homme et le convertissent en code machine lisible par l'ordinateur. 

Dans un langage compilé, la machine cible traduit directement le programme. Dans un langage interprété, le code source n'est pas directement traduit par la machine cible. Au lieu de cela, un programme _différent_, aka l'interpréteur, lit et exécute le code.

### **D'accord... mais que signifie cela _réellement_ ?**

Imaginez que vous avez une recette de houmous que vous voulez préparer, mais qu'elle est écrite en grec ancien. Il existe deux façons pour vous, qui ne parlez pas le grec ancien, de suivre ses instructions.

La première est si quelqu'un avait déjà traduit la recette en anglais pour vous. Vous (et toute autre personne parlant anglais) pourriez lire la version anglaise de la recette et préparer le houmous. Considérez cette recette traduite comme la version _compilée_.

La deuxième façon est si vous avez un ami qui connaît le grec ancien. Lorsque vous êtes prêt à préparer le houmous, votre ami s'assoit à côté de vous et traduit la recette en anglais au fur et à mesure, ligne par ligne. Dans ce cas, votre ami est l'interpréteur pour la version _interprétée_ de la recette.

### **Langages compilés**

Les langages compilés sont convertis directement en code machine que le processeur peut exécuter. Par conséquent, ils tendent à être plus rapides et plus efficaces à exécuter que les langages interprétés. Ils donnent également au développeur plus de contrôle sur les aspects matériels, comme la gestion de la mémoire et l'utilisation du CPU.

Les langages compilés nécessitent une étape de "construction" - ils doivent être compilés manuellement d'abord. Vous devez "reconstruire" le programme chaque fois que vous devez apporter une modification. Dans notre exemple de houmous, l'ensemble de la traduction est écrite avant de vous parvenir. Si l'auteur original décide qu'il veut utiliser un autre type d'huile d'olive, l'ensemble de la recette devrait être traduit à nouveau et renvoyé.

Des exemples de langages purement compilés sont C, C++, Erlang, Haskell, Rust et Go.

### **Langages interprétés**

Les interpréteurs parcourent un programme ligne par ligne et exécutent chaque commande. Ici, si l'auteur décide qu'il veut utiliser un autre type d'huile d'olive, il pourrait barrer l'ancienne et ajouter la nouvelle. Votre ami traducteur pourrait alors vous transmettre ce changement au fur et à mesure.

Les langages interprétés étaient autrefois significativement plus lents que les langages compilés. Mais, avec le développement de la [compilation à la volée](https://guide.freecodecamp.org/computer-science/just-in-time-compilation), cet écart se réduit.

Des exemples de langages interprétés courants sont PHP, Ruby, Python et JavaScript.

### **Un petit bémol**

La plupart des langages de programmation peuvent avoir à la fois des implémentations compilées et interprétées - le langage lui-même n'est pas nécessairement compilé ou interprété. Cependant, pour simplifier, ils sont généralement désignés comme tels.

Python, par exemple, peut être exécuté soit comme un programme compilé, soit comme un langage interprété en mode interactif. D'autre part, la plupart des outils en ligne de commande, des CLIs et des shells peuvent théoriquement être classés comme des langages interprétés.

## Avantages et inconvénients

### Avantages des langages compilés

Les programmes qui sont compilés en code machine natif tendent à être plus rapides que le code interprété. Cela est dû au fait que le processus de traduction du code au moment de l'exécution ajoute une surcharge, ce qui peut rendre le programme globalement plus lent.

### Inconvénients des langages compilés

Les inconvénients les plus notables sont :

* Temps supplémentaire nécessaire pour compléter toute l'étape de compilation avant les tests
* Dépendance à la plateforme du code binaire généré

### Avantages des langages interprétés

Les langages interprétés tendent à être plus flexibles et offrent souvent des fonctionnalités comme le typage dynamique et une taille de programme plus petite. De plus, comme les interpréteurs exécutent eux-mêmes le code source du programme, le code lui-même est indépendant de la plateforme.

### Inconvénients des langages interprétés

L'inconvénient le plus notable est la vitesse d'exécution typique par rapport aux langages compilés.