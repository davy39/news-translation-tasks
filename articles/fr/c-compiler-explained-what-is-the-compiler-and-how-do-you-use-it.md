---
title: 'Compilateur C++ expliqué : qu''est-ce qu''un compilateur et comment l''utiliser
  ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-10T23:40:00.000Z'
originalURL: https://freecodecamp.org/news/c-compiler-explained-what-is-the-compiler-and-how-do-you-use-it
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ca5740569d1a4ca3364.jpg
tags:
- name: C++
  slug: c-2
- name: compilers
  slug: compilers
- name: toothbrush
  slug: toothbrush
seo_title: 'Compilateur C++ expliqué : qu''est-ce qu''un compilateur et comment l''utiliser
  ?'
seo_desc: 'Intro to C++ Compilers

  In order to get started with C++, you will need to learn a little about compilers
  and how C++ runs on your computer.

  When all is said and done, computers only understand one language, machine language.
  Machine language is entir...'
---

## Introduction aux compilateurs C++

Pour commencer avec C++, vous devrez apprendre un peu sur les compilateurs et comment C++ s'exécute sur votre ordinateur.

En fin de compte, les ordinateurs ne comprennent qu'une seule langue, le langage machine. Le langage machine est entièrement composé de bits binaires, ou de 0 et de 1.

Bien qu'il soit possible de programmer en binaire, ce serait incroyablement fastidieux et chronophage. Nous, les humains, avons donc développé des langages de programmation pour faciliter le développement de logiciels.

Le langage d'assemblage est une correspondance directe 1 à 1 avec le langage machine. Des langages comme C, C++ et COBOL sont un peu plus élevés et doivent être compilés. Cela va encore plus haut. Des langages comme JavaScript et Python ont des composants qui sont traduits en C++ ou d'autres langages de bas niveau avant d'être compilés, ce qui les rend effectivement des langages "plus élevés" que C ou C++.

Parce que l'architecture des ordinateurs est composée de commutateurs électroniques et de câbles qui ne peuvent fonctionner qu'avec des 1 et des 0 binaires, vous avez besoin d'un compilateur pour traduire votre code du C++ de haut niveau en langage machine que le CPU peut comprendre.

## Comment fonctionnent les compilateurs

Les compilateurs sont des programmes utilitaires qui prennent votre code et le transforment en fichiers exécutables de code machine.

Lorsque vous exécutez un compilateur sur votre code, tout d'abord, le préprocesseur lit le code source (le fichier C++ que vous venez d'écrire). Le préprocesseur recherche des directives de préprocesseur (lignes de code commençant par un #). Les directives de préprocesseur amènent le préprocesseur à modifier votre code d'une certaine manière (en ajoutant généralement une bibliothèque ou un autre fichier C++).

Ensuite, le compilateur traite le code pré-traité ligne par ligne, traduisant chaque ligne en l'instruction de langage machine appropriée. Cela révèlera également toute erreur de syntaxe présente dans votre code source et générera une erreur sur la ligne de commande.

Enfin, si aucune erreur n'est présente, le compilateur crée un fichier objet avec le binaire de langage machine nécessaire pour s'exécuter sur votre machine. Bien que le fichier objet que le compilateur vient de créer soit probablement suffisant pour faire quelque chose sur votre ordinateur, ce n'est toujours pas un exécutable fonctionnel de votre programme C++. Il reste une étape importante pour obtenir un programme exécutable.

C++ contient une vaste bibliothèque pour aider à effectuer des tâches difficiles comme les E/S et la manipulation du matériel. Vous pouvez inclure ces bibliothèques avec des directives de préprocesseur, mais le préprocesseur ne les ajoute pas automatiquement à votre code.

Pour que vous ayez un programme exécutable final, un autre utilitaire appelé l'éditeur de liens doit combiner vos fichiers objets avec les fonctions de bibliothèque nécessaires pour exécuter le code.

Pensez à cela comme ayant tous les blocs nécessaires pour construire une maison. Le compilateur a fabriqué tous les blocs, mais l'éditeur de liens est celui qui les assemble tous pour enfin créer une maison. Une fois cela fait, vous avez maintenant un fichier exécutable fonctionnel !

## **Comment compiler un fichier**

Supposons que vous avez un fichier C++ appelé `helloWorld.cpp`...

### **Si vous êtes sur Windows**

#### **Utilisation d'un IDE comme CodeBlocks**

C'est aussi simple que de cliquer sur les boutons de construction et d'exécution, ils créeront un fichier dans le dossier du projet.

![img](https://i.imgur.com/FwZuFGy.png)

#### **Utilisation de l'invite de commande**

1. Ouvrez une invite de commande de développeur - Pour cette étape, vous devrez avoir Microsoft Visual Studio ou un autre IDE qui vous permet de compiler votre programme à partir de la ligne de commande. Vous pouvez également rechercher des compilateurs C++ en ligne.
2. Accédez directement au code source
3. Exécutez le compilateur sur votre code source (en supposant que vous utilisez le compilateur Microsoft Visual Studio) `cl /EHsc helloWorld.cpp`

Cela créera maintenant un fichier objet et le liera automatiquement pour vous. Si vous regardez dans ce même dossier, vous verrez un fichier exécutable hellWorld.exe (notez l'extension exe) est maintenant présent.

1. Tapez `helloWorld` dans l'invite pour exécuter l'exécutable

Alternativement, de nombreux IDE permettent une construction et une visualisation rapides de votre programme. Cela peut être plus facile puisque votre version de Windows peut ne pas être pré-emballée avec un utilitaire de compilateur.

### **Si vous êtes sur Linux ou OSX**

1. Ouvrez une fenêtre de terminal et accédez au répertoire du code source
2. Exécutez le compilateur sur votre code source `g++ helloWorld.cpp -o helloWorld`

Cela créera un fichier objet et le liera automatiquement pour vous. Regardez dans le dossier et vous verrez un fichier exécutable helloWorld.exe (notez l'extension exe).

1. Tapez `./helloWorld` dans la fenêtre de terminal pour exécuter le fichier exécutable

g++ est le compilateur standard Linux et est un excellent utilitaire. Il est fourni avec le système d'exploitation.

NOTE : pour compiler et exécuter votre code directement, exécutez `g++ -o helloWorld helloWorld.cpp; ./helloWorld` afin que lorsque vous devez compiler et exécuter votre code plusieurs fois, flèche vers le haut-entrée.

Il existe plusieurs types de compilateurs différents. Les deux listés sont ceux qui sont généralement fournis avec Windows ou Linux/OSX.

## Plus d'informations sur C++

* [Introduction à la programmation C++](https://www.freecodecamp.org/news/the-c-plus-plus-programming-language/)
* [Programmation orientée objet en C++](https://www.freecodecamp.org/news/object-oriented-programming-in-c/)
* [Algorithmes de graphes et structures de données expliqués en C++ et Java](https://www.freecodecamp.org/news/graph-algorithms-and-data-structures-explained-with-java-and-c-examples/)
* [Comment compiler votre code C++ dans VS Code](https://www.freecodecamp.org/news/how-to-compile-your-c-code-in-visual-studio-code/)