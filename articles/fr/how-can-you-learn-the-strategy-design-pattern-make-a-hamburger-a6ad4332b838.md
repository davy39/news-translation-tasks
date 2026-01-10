---
title: Comment apprendre le patron de conception Stratégie ? Fabriquez un hamburger
  !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-26T20:28:49.000Z'
originalURL: https://freecodecamp.org/news/how-can-you-learn-the-strategy-design-pattern-make-a-hamburger-a6ad4332b838
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oIC7jzfYZde2T_Oo6DpI2Q.png
tags:
- name: Design
  slug: design
- name: 'food '
  slug: food
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
seo_title: Comment apprendre le patron de conception Stratégie ? Fabriquez un hamburger
  !
seo_desc: 'By Sihui Huang

  Do you know how to order a burger?

  If so, I have good news for you. Then you know how to use one of the most commonly
  used design patterns, strategy pattern!

  “How so?” you might ask. Well, let’s take a look at the features of strategy ...'
---

Par Sihui Huang

Savez-vous comment commander un burger ?

Si oui, j'ai une bonne nouvelle pour vous. Alors vous savez comment utiliser l'un des patrons de conception les plus couramment utilisés, le [patron stratégie](https://en.wikipedia.org/wiki/Strategy_pattern) !

« Comment cela ? » pourriez-vous demander. Eh bien, examinons les caractéristiques du patron stratégie.

* Il définit une famille d'algorithmes.
* Il encapsule chaque algorithme.
* Il rend les algorithmes interchangeables au sein de cette famille.

Le patron stratégie permet à l'algorithme de varier indépendamment des clients qui l'utilisent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UQuo_svmmX9OKxW3teI12g.png)
_Vous sentez-vous aussi confus que ce gars ?_

En quoi cela a-t-il un rapport avec les burgers ?

Réfléchissons aux burgers pendant un instant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uiU-4XXn3GoQFEGYgRFcEw.png)

Il existe de nombreuses variétés de burgers : burger végétarien, cheeseburger, burger au poulet grillé, et double cheeseburger, pour n'en nommer que quelques-uns. Tous partagent le même format : le pain supérieur + la galette + le pain inférieur.

C'est la galette qui rend chaque burger différent. Un cheeseburger a du fromage et une galette de bœuf au milieu, tandis qu'un burger au poulet grillé a une galette de blanc de poulet grillé.

Récapitulons la définition du patron stratégie en termes de burgers. Quelle est la famille d'algorithmes en termes de burgers ? C'est la famille des différentes galettes :

* galette pour un burger au poulet = [blanc de poulet grillé]
* galette pour un cheeseburger = [fromage + galette de bœuf]
* galette pour un double cheeseburger = [fromage + galette de bœuf + fromage + galette de bœuf]

Elles sont encapsulées et interchangeables les unes avec les autres. Remplacez la galette de burger au poulet par la galette de cheeseburger, et vous obtenez un cheeseburger.

> La stratégie permet à l'algorithme de varier indépendamment des clients qui l'utilisent.

Vous pouvez commander n'importe quel burger que vous aimez. Mais pour un chef, faire un burger suit la même procédure générale : préparer le pain, cuire la galette, puis mettre la galette entre les pains supérieur et inférieur.

Un burger est un exemple concret de l'utilisation du patron stratégie.

Examinons le code.

Il y a trois participants dans le patron stratégie.

**Stratégie** déclare une interface commune à tous les algorithmes pris en charge. Le contexte utilise cette interface pour appeler l'algorithme défini par une stratégie concrète.

**Stratégie concrète** implémente l'algorithme en utilisant l'interface StrategyInterface.

**Contexte** est configuré avec un objet ConcreteStrategy ; maintient une référence à un objet stratégie ; peut définir une interface qui permet à la stratégie d'accéder à ses données.

GrilledChickenStuffing et BeefPattyStuffing sont nos stratégies concrètes. Chacune définit comment sa garniture doit être cuite. La classe `Burger` est notre contexte. Elle est configurée avec une stratégie concrète et utilise la stratégie concrète plus tard lorsqu'un burger doit être cuit.

Dans notre exemple de burger, nous n'avons pas de classe spécifique qui déclare quelle interface les stratégies concrètes doivent implémenter. C'est parce que nous n'en avons pas besoin, grâce au typage canard de Ruby. Si cela marche comme un canard et parle comme un canard, c'est un canard. Si cela peut être cuit comme une galette de burger, c'est une galette de burger.

La stratégie déclare l'interface qu'une stratégie concrète doit implémenter et que le contexte peut utiliser. Comme vous pouvez le voir dans le code ci-dessus, GrilledChickenStuffing et BeefPattyStuffing implémentent tous deux la méthode cook, et c'est la méthode que l'utilisateur d'une stratégie concrète, alias le contexte, attend qu'une stratégie concrète fournisse.

#### **L'idée clé du patron stratégie**

La clé du patron stratégie est de séparer les algorithmes variables dans un objet distinct. Ces objets deviennent une famille d'algorithmes parmi lesquels le contexte peut choisir. Chacun de ces objets, alias les stratégies, fait le même travail et prend en charge la même interface.

Dans notre exemple de burger, nous avons différentes stratégies de galettes pour un burger. Et chacune des stratégies concrètes de galettes de burger prend en charge la même interface en implémentant la méthode cook.

Tout est une question de composition. L'utilisateur a une stratégie et délègue. L'utilisateur de la stratégie délègue le travail. Dans notre exemple, un burger a une galette, et il délègue le travail de cuisson.

#### **Avantages du patron stratégie**

* Il permet une meilleure séparation des préoccupations en séparant un ensemble de stratégies d'une classe et soulage la classe `Burger` de toute responsabilité pour notre connaissance de la garniture.
* Il facilite le changement de stratégie à l'exécution car le patron est basé sur la composition et la délégation, plutôt que sur l'héritage.

#### **Points à surveiller lors de l'utilisation du patron stratégie**

* Le passage de données entre le contexte et la stratégie. Si l'implémentation d'une stratégie concrète nécessite des données du contexte, vous pouvez soit passer les données en tant que paramètres à une stratégie concrète, soit passer le contexte lui-même dans une stratégie concrète. Cela permet à la stratégie concrète d'avoir accès aux données via le contexte. Quelle que soit la méthode que vous choisissez, surveillez l'enchevêtrement du contexte et de la stratégie concrète.
* Vérifiez bien si vous avez réellement besoin du patron stratégie, de la [méthode de modèle](https://en.wikipedia.org/wiki/Template_method_pattern), ou du [patron décorateur](https://en.wikipedia.org/wiki/Decorator_pattern).

#### **Principes de conception utilisés dans le patron stratégie**

* Encapsuler ce qui varie
* Privilégier la composition à l'héritage
* Programmer vers des interfaces, pas vers des implémentations

Maintenant, vous avez appris le patron stratégie.

Voici une question importante : quelle est votre stratégie de burger préférée ? :)

Je publie sur [sihui.io](http://www.sihui.io/) chaque semaine.

Abonnez-vous pour ne pas manquer le prochain article de la série.

La prochaine fois, nous examinerons la méthode de modèle et...

![Image](https://cdn-media-1.freecodecamp.org/images/1*VboteHPFWOiIWe9ujGeiBA.png)