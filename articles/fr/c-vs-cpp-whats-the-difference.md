---
title: C vs C++ – Quelles sont les différences ?
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-04T20:16:23.000Z'
originalURL: https://freecodecamp.org/news/c-vs-cpp-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/vanesa-giaconi-n1nwTr_-lH4-unsplash.jpg
tags:
- name: C++
  slug: c-2
- name: c programming
  slug: c-programming
seo_title: C vs C++ – Quelles sont les différences ?
seo_desc: 'The C and C++ programming languages power a large part of the world''s
  products, applications, and websites.

  Each helped lay the foundation for the creation of many popular programming languages,
  such as Java. They also support many languages that you...'
---

Les langages de programmation C et C++ alimentent une grande partie des produits, applications et sites web du monde.

Chacun a aidé à poser les bases de la création de nombreux langages de programmation populaires, comme Java. Ils supportent également de nombreux langages que vous pourriez utiliser régulièrement pour vos projets de programmation, comme Python.

Dans cet article, vous trouverez un aperçu général et adapté aux débutants des deux langages, ainsi que leurs principales similitudes et différences.

## Les origines de C et C++

### Une histoire du langage de programmation C

Ken Thompson et Dennis Ritchie avaient travaillé pendant plusieurs années sur le projet MULTICS (Multiplexed Information and Computing Service) aux laboratoires AT&T Bell.

Après l'arrêt du projet, en 1969, Ken Thompson a commencé à travailler sur son jeu *Space Travel* sur une machine PDP-7 peu utilisée.

En faisant cela, il a fini par écrire un système d'exploitation presque complet, Unix, à partir de zéro en langage d'assemblage.

Tout en travaillant sur MULTICS, Thompson et Ritchie avaient écrit des logiciels système et des utilitaires de programmation en utilisant des langages de haut niveau. Et ils avaient vu à quel point le processus était plus facile, comparé au langage d'assemblage cryptique et difficile à déchiffrer.

Ritchie a rejoint Thompson pour aider à porter Unix sur une nouvelle machine – le PDP-11.

Pendant cette période, ils ont expérimenté divers langages de haut niveau qui pourraient aider à accomplir la tâche.

Ils ont utilisé BCPL (Basic Combined Programming Language), qui était largement utilisé pendant l'ère MULTICS. Après l'avoir essayé, Thompson a fini par écrire un nouveau langage – le langage de programmation B.

Le langage B était similaire à BCPL mais était une version plus simple et épurée.

Mais B n'était pas assez puissant et ne tirait pas pleinement parti des nouvelles fonctionnalités et de la puissance du PDP-11.


![Image](https://www.freecodecamp.org/news/content/images/2021/11/Ken_Thompson_-sitting-_and_Dennis_Ritchie_at_PDP-11_-2876612463-.jpg)
_Thompson (assis) et Ritchie travaillant ensemble sur un PDP-11. [Crédit image et texte de Wikipedia](https://en.wikipedia.org/wiki/Ken_Thompson#/media/File:Ken_Thompson_(sitting)_and_Dennis_Ritchie_at_PDP-11_(2876612463).jpg)_

Dennis Ritchie a commencé à améliorer le langage B et a fini par créer le langage de programmation C.

C est un langage portable, ce qui signifie que les programmes écrits dans ce langage peuvent être transférés et utilisés sur une variété d'architectures de machines. Il est très rapide et facile à compiler et a une correspondance directe avec le code machine, donnant au programmeur l'accès à des fonctionnalités de bas niveau.

Ils ont fini par réécrire le système d'exploitation Unix en C en 1972.

Puisque C était portable et était le langage dans lequel Unix était implémenté, les développeurs ont commencé à l'adopter et à l'utiliser largement. Cela a conduit au succès du système d'exploitation Unix, et en retour, le langage C est devenu populaire.

Dennis Ritchie et Brian Kernighan ont co-écrit le livre 'Le langage de programmation C' en 1977, qui a créé une norme pour la manière dont le langage devait être utilisé. Ce livre a encore popularisé le langage.

C est extrêmement significatif dans l'histoire de l'informatique et sa création a conduit à la création de nombreux autres langages de programmation. Pour cette raison, il est souvent appelé la '*mère*' de tous les langages de programmation.

### Histoire de C++

En 1979, le chercheur Bjarne Stroustrup a été embauché aux laboratoires AT&T Bell.

Dans les années 1970, la complexité et la puissance de calcul des ordinateurs ont augmenté et les limitations du langage de programmation C ont commencé à apparaître.

Au début des années 1980, Bjarne Stroustrup a créé un nouveau langage qui a été influencé par deux choses :

 - Les capacités de programmation orientée objet d'un autre langage, Simula, qui offrait une approche différente de la programmation par rapport à C. Le code pouvait être abstrait et mieux organisé et tout pouvait être représenté en utilisant des classes.
 - Le langage de programmation système, C, qui offrait la capacité de se rapprocher du matériel de la machine et d'effectuer des tâches de calcul de bas niveau exigeantes.

Ces deux idées combinées ont permis une abstraction de plus haut niveau sans perdre l'efficacité de bas niveau de C. Ainsi, le langage '*C avec classes*' a été créé.

En 1984, 'C avec classes' a été renommé en C++.

Ainsi, C++ est un sur-ensemble de C, ce qui signifie qu'il s'agissait d'une *extension* de C et qu'il est basé sur celui-ci. C++ offre simplement des capacités supplémentaires au langage C.

## Similitudes entre C et C++

Voici quelques-unes des similitudes entre C et C++.

### Syntaxe et structure du code

La syntaxe globale des deux langages est très similaire. Les opérateurs et les mots-clés utilisés en C sont également utilisés en C++ pour réaliser les mêmes choses. Mais C++ a plus de mots-clés que C, et il a une grammaire étendue.

Les commentaires en ligne, `//`, et les commentaires en bloc, `*/ */`, ont la même apparence.

De plus, chaque instruction se termine par un point-virgule, `;`.

Les conditionnelles, les boucles, l'initialisation et la déclaration de variables – tout cela a une apparence similaire entre les deux langages.

C et C++ ont tous deux une méthode `main()`, qui lance chaque programme, et tous deux incluent des fichiers d'en-tête en haut des fichiers respectifs, avec `#include`.

### Langages de programmation compilés

C et C++ sont tous deux des langages de programmation compilés.

Un compilateur est un programme logiciel informatique.

Il prend le code source qu'un programmeur a écrit dans un langage de programmation de haut niveau et le *traduit* dans un autre langage que l'ordinateur peut comprendre.

Cette forme est d'abord du code assembleur qui est à nouveau traduit en code machine – le langage natif de tous les ordinateurs.

Le langage machine est un ensemble d'instructions qui sont comprises directement par le CPU (Unité Centrale de Traitement) d'un ordinateur.

Une fois que le code source a été traduit en code machine, un fichier exécutable binaire, `a.out`, est créé.

## Différences entre C et C++

Examinons maintenant quelques-unes des différences entre les deux langages.

### Méthodes d'entrée et de sortie

C et C++ utilisent des méthodes différentes pour afficher des informations sur la console et recevoir des informations de l'utilisateur.

En C, `scanf()` est utilisé pour l'entrée utilisateur, tandis que `printf()` est utilisé pour la sortie de données.

En C++, `std::cin >>` est utilisé pour obtenir l'entrée utilisateur et `std::cout <<` est utilisé pour la sortie de données.

### Le paradigme de programmation

La différence la plus importante entre les deux langages est l'approche différente de la programmation que chacun utilise.

C est un **langage orienté procédural** et son accent est mis sur les fonctions.

Les programmes sont divisés en un ensemble de fonctions et ils consistent en des instructions étape par étape, ou commandes, à exécuter dans un ordre séquentiel.

Ce style de programmation spécifie *comment* faire quelque chose, en donnant des étapes structurées pour la manière dont les tâches de calcul seront effectuées, suivant une approche de haut en bas.

Ce style de programmation peut devenir assez désordonné et sujet aux erreurs lorsque les programmes grandissent en taille. Cela conduit à beaucoup de copier-coller dans le fichier et à la mise à jour de nombreuses fonctions lorsqu'il y a un changement.

En plus d'être un langage procédural, C++ est également un **langage de programmation orienté objet**, qui est basé sur le concept de diviser un programme en objets.

Tout est organisé et divisé en plus petits groupes de parties liées ou *objets*, qui sont une instance d'une *classe*, suivant une approche de bas en haut.

La programmation orientée objet est basée sur quatre principes : *encapsulation, abstraction, héritage et polymorphisme*.

Ce style de programmation crée un code plus lisible et utilisable qui est plus facile à maintenir, tout en offrant une meilleure sécurité des données.

### La STL

C++ offre la STL – Standard Template Library – et C ne l'offre pas.

Elle fournit des classes de modèles pour les structures de données couramment utilisées et des composants pour implémenter des fonctionnalités intégrées supplémentaires.

Un tel composant est les conteneurs tels que les [Vecteurs](https://www.freecodecamp.org/news/c-vector-std-pattern-vector-in-cpp-with-example-code/), qui stockent des collections d'objets.

### Espaces de noms

Les espaces de noms sont une fonctionnalité disponible en C++ et non en C.

Ils sont des conteneurs utilisés pour organiser le code en groupes logiques d'identifiants et d'objets similaires sous un nom, dans une portée.

Ils empêchent les collisions de noms lorsque plusieurs bibliothèques sont présentes, et empêchent les conflits avec les noms d'autres espaces de noms dans un programme.

Un exemple d'espace de noms est `std::`.

Une façon d'utiliser un espace de noms et de l'introduire dans une portée est d'utiliser le mot-clé `using`, par exemple `using namespace std;`.

### Gestion des exceptions

C n'offre pas de moyen de gérer les exceptions dans les programmes qui aident à prévenir les erreurs.

C++, en revanche, supporte la gestion des exceptions en introduisant des blocs `try` et `catch`.

### Extension de fichier

L'extension de fichier pour un fichier contenant du code C est `.c`, tandis que l'extension de fichier pour les fichiers C++ est `.cpp`.

## Où sont utilisés C et C++ ?

C est couramment utilisé pour des tâches de calcul de bas niveau très exigeantes où la vitesse, l'efficacité et un accès proche à la machine sont indispensables.

C suppose que les programmeurs savent ce qu'ils font et leur donne de la liberté.

C'est donc le langage de choix pour les systèmes d'exploitation, les dispositifs embarqués, la programmation système, les noyaux et les pilotes, le développement de compilateurs, et l'industrie croissante des applications IoT (Internet des Objets).

C++ permet à nouveau au programmeur un accès proche et une manipulation de la machine, tout en offrant une efficacité et des performances élevées pour les systèmes à grande échelle. En même temps, il est de plus haut niveau avec suffisamment d'abstraction par rapport à la machine.

C++ est un langage de choix populaire pour la création de moteurs de jeu et de graphismes informatiques et d'applications, d'applications VR, de navigateurs web tels que Google Chrome, Mozilla Firefox et Safari, et d'extensions de navigateur web. Le moteur de recherche Google est également construit en C++.

## Comment apprendre C et C++

Voici une liste de quelques ressources pour vous aider à commencer votre apprentissage de C et C++.

Pour apprendre C :
- [Le guide du débutant en C : Apprenez les bases du langage de programmation C en quelques heures](https://www.freecodecamp.org/news/the-c-beginners-handbook/)
- [Qu'est-ce que le langage de programmation C ? Un tutoriel pour débutants](https://www.freecodecamp.org/news/what-is-the-c-programming-language-beginner-tutorial/)
- [Tutoriel de programmation C pour débutants](https://www.youtube.com/watch?v=KJgsSFOSQv0)

Pour apprendre C++ :

- [Le langage de programmation C++](https://www.freecodecamp.org/news/the-c-plus-plus-programming-language/)
- [Tutoriel C++ pour débutants](https://www.youtube.com/watch?v=vLnPwxZdW4Y)
- [Apprenez la programmation orientée objet (OOP) en C++](https://www.freecodecamp.org/news/learn-object-oriented-programming-oop-in-c-full-video-course/)
- [Apprenez le C++ moderne en construisant un plugin audio](https://www.freecodecamp.org/news/learn-modern-cpp-by-building-an-audio-plugin/)

## Conclusion

Merci d'avoir lu jusqu'à la fin, et j'espère que vous avez trouvé cet article utile.

Vous avez appris les origines de C et C++ et leur contexte historique. Vous avez ensuite vu quelques-unes de leurs similitudes et différences, comment chaque langage est utilisé, et quelques ressources pour commencer à apprendre ces langages.

Bon codage !