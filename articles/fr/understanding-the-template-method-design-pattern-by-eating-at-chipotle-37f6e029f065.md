---
title: Comprendre le patron de conception Template Method en mangeant chez Chipotle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T15:26:43.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-template-method-design-pattern-by-eating-at-chipotle-37f6e029f065
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rQ4O--pESIxq1jr_JcBPqA.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comprendre le patron de conception Template Method en mangeant chez Chipotle
seo_desc: 'By Sihui Huang

  Object-Oriented Design Patterns in Life— gain an intuitive understanding of OO design
  patterns by linking them with real-life examples.


  Template Method is a commonly used design pattern in programming and real life.

  Before we dive int...'
---

Par Sihui Huang

[Patrons de conception orientés objet dans la vie — acquérez une compréhension intuitive des patrons de conception OO en les reliant à des exemples de la vie réelle.](http://www.sihui.io/design-patterns/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*rQ4O--pESIxq1jr_JcBPqA.png)

Template Method est un patron de conception couramment utilisé en programmation et dans la vie réelle.

Avant de plonger dans les détails du patron, apprenons une leçon de vie importante :

### Chipotle 101 : Comment commander chez Chipotle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HgB3orsQPykXtWf7cmI1Xg.png)

Quatre étapes sont impliquées :

1. Choisissez un « contenant » : Burrito vs Bowl vs Tacos vs Salade
2. Ajoutez de la viande : Poulet vs Steak vs Barbacoa vs Carnitas vs Végétarien
3. Ajoutez des garnitures : Tomate vs Maïs vs Piment vert vs Piment rouge
4. Ajoutez des extras et des boissons : Chips vs Guacamole vs Salsa vs Bière vs Soda

Par exemple, ma commande habituelle est Bowl + Steak + (Tomate + Maïs) + Guacamole et celle de mon amie Amber est Burrito + Poulet + (Piment vert + Piment rouge) + (Chips + Soda).

Si nous codons nos commandes habituelles en Ruby, elles ressembleront à ceci :

Lorsque nous commandons, nous mettons tout ce que nous voulons dans le contenant et retournons le contenant rempli.

Malheureusement, Amber et moi avons décidé de suivre un régime pendant un certain temps. Et nous avons décidé que lorsque nous commanderions chez Chipotle, nous ne pourrions prendre que de la tomate comme garniture et aucun extra. Nos choix sont donc limités à :

1. Contenant : Burrito vs Bowl vs Tacos vs Salade
2. Viande : Poulet vs Steak vs Barbacoa vs Carnitas vs Végétarien
3. Garnitures : Tomate
4. Pas d'extras ni de boissons

Pendant le régime, nos commandes habituelles doivent être modifiées en :

* Sihui : Bowl + Steak + Tomate + Pas d'extras ni de boissons
* Amber : Burrito + Poulet + Tomate + Pas d'extras ni de boissons

En écrivant nos commandes en Ruby, nous obtenons ce qui suit :

Puisque nos deux commandes ont exactement les mêmes méthodes _toppings_, _extras_ et _order_, il est logique de les extraire dans une classe parente, _DietOrder_, et de faire en sorte que _DietOrderSihui_ et _DietOrderAmber_ en héritent.

Maintenant, notre ami Ben veut rejoindre notre Club de Régime Chipotle, et il aime les Tacos avec des Carnitas. Sa commande sera donc :

Ta-da, vous venez d'apprendre le patron de conception Template Method ! ? ? ?

Vous ne me croyez pas ?

Jetez un œil à la définition du Template Method :

> Le patron Template Method est un patron de conception comportemental qui

> - définit le squelette du programme d'un algorithme dans une opération,

> - délègue certaines étapes aux sous-classes.

> Il permet de redéfinir certaines étapes d'un algorithme sans modifier la structure de l'algorithme.

Cela ne ressemble-t-il pas exactement à ce que nous venons de faire avec notre _DietOrder_ et _SihuiDietOrder/AmberDietOrder/BenDietOrder_ ?

_DietOrder_ définit le squelette de la commande : on ne peut prendre que de la tomate comme garniture et pas d'extras ni de boissons, et on commande en choisissant un contenant et en mettant tout à l'intérieur du contenant choisi.

_SihuiDietOrder/AmberDietOrder/BenDietOrder_ redéfinissent le contenant et la viande en fonction de nos préférences personnelles.

Disons qu'un mois s'est écoulé, et qu'Amber et moi avons suivi notre régime strictement. Nous avons décidé de nous récompenser avec des jours de triche (cheat days) !

Lors d'un jour de triche, nous prenons du soda comme boisson. ??? Et chacun d'entre nous peut décider quel jour du mois sera son jour de triche.

Comme Ben est nouveau dans le club, il décide de s'en tenir au régime strictement un peu plus longtemps.

Voyons à quoi cela ressemble en Ruby :

Dans _DietOrder_, nous demandons si aujourd'hui est un jour de triche. Si c'est le cas, nous pouvons avoir un Soda en extra. Sinon, il n'y a pas d'extras. Et par défaut, aujourd'hui n'est pas un jour de triche.

Amber et moi définissons nos propres jours de triche :

Comme Ben suit le régime strictement, il n'a pas de jour de triche.

Sa classe n'a pas besoin de changer.

La méthode _is_cheat_day?_ est un hook (crochet).

Un hook fournit un moyen pour une sous-classe d'implémenter une partie optionnelle d'un algorithme.

Si la sous-classe ne se soucie pas de cette partie, elle peut l'ignorer et utiliser l'implémentation par défaut de la classe parente.

Dans notre cas, _is_cheat_day?_ est optionnel. SihuiDietOrder et AmberDietOrder l'implémentent parce que nous voulons avoir un jour de triche chaque mois. Mais Ben ne veut pas de jour de triche. Donc BenDietOrder ignore l'implémentation de _is_cheat_day?_ et utilise celle par défaut de DietOrder, qui retourne toujours false.

Deux principes importants de conception orientée objet sont utilisés dans le Template Method :

1. Encapsuler ce qui varie.

Dans notre cas, les parties qui varient sont _vessel_, _meat_ et _is_cheat_day?_. Nous les encapsulons dans des sous-classes. Pour les parties qui ne varient pas, _toppings_ et _extras_, nous les laissons dans la classe parente.

2. Le principe d'Hollywood : Ne nous appelez pas, nous vous appellerons.

Oui, le principe d'Hollywood est [une chose réelle](http://wiki.c2.com/?HollywoodPrinciple).

À Hollywood, les producteurs de films disent aux acteurs : « Ne nous appelez pas, nous vous appellerons si nous trouvons un rôle qui vous convient. »

En programmation, les composants de bas niveau peuvent participer au calcul, comme _AmberDietOrder_ définissant son propre _is_cheat_day?_, mais les composants de haut niveau contrôlent quand et comment, comme _DietOrder_ appelant _is_cheat_day?_ à l'intérieur d'_extras_.

### Points à retenir :

**Une définition =&**gt;

> Le patron Template Method est un patron de conception comportemental qui

> - définit le squelette du programme d'un algorithme dans une opération,

> - délègue certaines étapes aux sous-classes.

> Il permet de redéfinir certaines étapes d'un algorithme sans modifier la structure de l'algorithme.

**Deux principes de conception =&**gt;

> 1. Encapsuler ce qui varie.

> 2. Le principe d'Hollywood : Ne nous appelez pas, nous vous appellerons.

Ou…

vous pouvez simplement repartir avec une commande Chipotle ? ? ?

La prochaine fois, nous emmènerons notre aventure de conception et de nourriture chez ???

![Image](https://cdn-media-1.freecodecamp.org/images/1*WpzelusOe2vXZa9tXugL9Q.png)