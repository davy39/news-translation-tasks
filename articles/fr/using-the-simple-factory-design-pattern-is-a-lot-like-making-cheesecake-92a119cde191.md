---
title: Utiliser le modèle de conception Simple Factory, c'est comme faire un cheesecake
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-26T12:47:05.000Z'
originalURL: https://freecodecamp.org/news/using-the-simple-factory-design-pattern-is-a-lot-like-making-cheesecake-92a119cde191
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JtDoAdFERT4heuYF6gGpyg.png
tags:
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: software design patterns
  slug: software-design-patterns
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Utiliser le modèle de conception Simple Factory, c'est comme faire un cheesecake
seo_desc: 'By Sihui Huang

  Factory Patterns are about encapsulating object creation.

  But before diving into details of the patterns, let’s talk about cheesecake. Because
  cheesecake is about … happiness! ???


  Let’s focus our gaze on six of my personal favorites: ...'
---

Par Sihui Huang

Les modèles de Factory concernent l'encapsulation de la création d'objets.

Mais avant de plonger dans les détails des modèles, parlons de cheesecake. Parce que le cheesecake, c'est du bonheur ! 😊🍰

![Image](https://cdn-media-1.freecodecamp.org/images/1*DX0_N89jW5HSmgl5FEuLPQ.png)

Concentrons-nous sur six de mes préférés : Cheesecake Original, Cheesecake Oreo, Cheesecake Café, Cheesecake Tiramisu, Cheesecake S'mores et Cheesecake Noisette.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GB-APPbSeUEBzrrmtsc09w.png)

Et voici comment nous faisons un cheesecake :

Créer une instance de cheesecake en fonction du type sélectionné -> Faire la croûte -> Ajouter des couches sur la croûte -> Cuire -> Réfrigérer -> Ajouter des garnitures au gâteau -> Retourner le gâteau ! 🍰

Attendez... ce cheesecake à la lime et à la mangue a l'air très tentant 😋.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oxZrWU870mXJeFCF4RqPBw.png)

Laissez-moi l'ajouter à ma liste :

Une seconde...

J'ai consommé trop de caféine ces derniers temps. Je ne veux plus que le cheesecake au café soit sur ma liste. Laissez-moi mettre à jour la méthode _make_cheesecake_ à nouveau.

Oooh... ils ont une version low carb de cheesecake. C'est toujours bien d'avoir une option low carb. Il faut qu'il soit sur ma liste !

Donc, depuis la première fois où nous avons défini `make_cheesecake`, nous l'avons mise à jour trois fois. Chaque fois, le changement était pour la même raison exacte — mettre à jour ma liste de cheesecakes. Et tout le reste, `make_crust`_,_ `add_layers`_,_ `bake`_,_ `refrigerate`_,_ et `add_toppings`, est resté le même.

Désolé de changer d'avis toutes les trois secondes. Mais comme on dit : **le changement est la seule constante dans la vie (et le développement logiciel).**

Pour être honnête, nous devrons changer la liste au moins une fois de plus : le cheesecake à la citrouille sera disponible à partir de septembre. Il est MONDIALEMENT CÉLÈBRE ! Sans aucun doute, nous devons l'ajouter à la liste une fois septembre arrivé. Oups, cela signifie que nous devons le retirer de la liste lorsque la saison des fêtes sera passée.

Il est évident que ma liste de cheesecakes change souvent.

Il existe un principe de conception : **encapsuler ce qui varie**.

Nous devrions l'essayer.

### Il est temps pour une Cheesecake Factory !

La `CheesecakeFactory` est une classe simple. Tout ce qu'elle fait, c'est créer et retourner le cheesecake correct en fonction d'un type donné.

Avec l'aide de `CheesecakeFactory`, la méthode `make_cheesecake` devient beaucoup plus simple.

La méthode `make_cheesecake` peut maintenant se concentrer sur les étapes réelles de la fabrication d'un cheesecake sans avoir à se soucier des différents types de cheesecakes.

Notre `CheesecakeFactory` est un exemple d'utilisation de la Simple Factory. **Simple Factory est utilisée pour encapsuler la création d'objets.**

### La famille des modèles de Factory

Outre la Simple Factory, il y a deux autres membres de la famille des modèles de Factory : **Factory Method** et **Abstract Factory.** Nous n'entrerons pas dans les détails de ces deux modèles.

En résumé, Factory Method et Abstract Factory utilisent l'héritage. Factory Method concerne la création d'un type d'objet, et Abstract Factory concerne la création d'une famille de différents types d'objets. Tous les trois concernent l'encapsulation de la création d'objets en utilisant le principe de conception : encapsuler ce qui varie.

### Avantages de l'utilisation de Simple Factory

Extraire la logique de création du cheesecake correct en fonction d'un type donné est un petit changement qui nous apporte de nombreux avantages. Le plus grand avantage est que nous pouvons modifier la liste de cheesecakes sans toucher à la méthode `make_cheesecake` et à son test. Tout ce que nous avons à faire est de mettre à jour la classe `CheesecakeFactory` et de laisser `make_cheesecake` et son test tranquilles.

Nous voulons séparer les parties qui varient souvent des parties stables. Parce que chaque fois que nous modifions une partie de notre code, nous pouvons introduire des bugs. Les parties qui varient sont les parties fragiles de notre système. Nous voulons garder les parties stables à l'écart des parties fragiles. Ainsi, si nous introduisions des bugs lors de la mise à jour d'une partie du système, il serait plus facile pour nous de localiser le bug.

### Points à retenir :

1. **Les modèles de Factory sont utilisés pour encapsuler la création d'objets.**
2. **Principe de conception : encapsuler ce qui varie.**

Je dois courir pour aller chercher un cheesecake maintenant.

N'oubliez pas de vous abonner pour ne pas manquer le prochain article !

La prochaine fois, nous jetterons un coup d'œil à quelques waaaaaaaaffles !

![Image](https://cdn-media-1.freecodecamp.org/images/1*LvuKW5NzZsznwP-Y3TfInA.png)