---
title: Comment écrire des applications robustes à chaque fois, en utilisant « The
  Clean Architecture »
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-04T19:48:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-robust-apps-consistently-with-the-clean-architecture-9bdca93e17b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*biSmg94qPg58-ppug82-Ng.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment écrire des applications robustes à chaque fois, en utilisant «
  The Clean Architecture »
seo_desc: 'By Daniel Oliveira

  As developers, we can’t keep from using external libraries and frameworks in our
  systems. The community’s hands build marvelous tools, and using them is only natural.
  However, everything has a downside.

  Careless teams and individua...'
---

Par Daniel Oliveira

En tant que développeurs, nous ne pouvons pas nous empêcher d'utiliser des bibliothèques et des frameworks externes dans nos systèmes. La communauté construit des outils merveilleux, et les utiliser est tout à fait naturel. Cependant, tout a un inconvénient.

Des équipes et des individus négligents peuvent se retrouver dans une situation dangereuse en structurant leurs systèmes autour des outils qu'ils utilisent. Les règles métiers se mélangent avec les détails d'implémentation. Cela peut entraîner un système fragile, difficile à étendre et à maintenir. Ce qui devrait être un changement rapide dans l'interface utilisateur se transforme en une chasse aux bugs qui dure des heures. **Mais cela ne doit pas être comme ça.**

L'architecture logicielle propose des modèles et des règles pour déterminer les structures (comme les classes, les interfaces et les structs) dans un système et comment elles se rapportent les unes aux autres. Ces règles favorisent la réutilisabilité et la séparation des préoccupations pour ces éléments. Cela facilite le changement des détails d'implémentation tels que le SGBD ou la bibliothèque front-end. Les refactorisations et les corrections de bugs affectent le moins possible de parties du système. Et l'ajout de nouvelles fonctionnalités devient un jeu d'enfant.

Dans cet article, je vais expliquer un [modèle d'architecture proposé en 2012](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html) par Robert C. Martin, [Uncle Bob](https://twitter.com/unclebobmartin). Il est l'auteur de classiques comme [Clean Code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_1?ie=UTF8&qid=1501969656&sr=8-1&keywords=clean+code) et [The Clean Coder.](https://www.amazon.com/Clean-Coder-Conduct-Professional-Programmers/dp/0137081073/ref=sr_1_2?ie=UTF8&qid=1501969656&sr=8-2&keywords=clean+code) En octobre de cette année, il lancera un autre livre, [Clean Architecture](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164/ref=pd_sim_14_2?_encoding=UTF8&pd_rd_i=0134494164&pd_rd_r=BJG6B8A17K06QHXKKWEJ&pd_rd_w=MqqNH&pd_rd_wg=G8bDT&psc=1&refRID=BJG6B8A17K06QHXKKWEJ).

Le modèle porte le même nom que le livre, et il est construit sur des concepts simples :

![Image](https://cdn-media-1.freecodecamp.org/images/1*biSmg94qPg58-ppug82-Ng.jpeg)

Divisez la composition du système en couches avec des rôles distincts et bien définis. Et restreignez les relations entre les entités dans différentes couches. Il n'y a rien de nouveau à diviser votre application en couches. Mais j'ai choisi cette approche car c'était celle qui était la plus simple à comprendre et à exécuter. Et cela rend les tests des cas d'utilisation extrêmement simples.

Nous devons simplement nous assurer que les **Interactors** fonctionnent correctement, et nous sommes prêts à partir. Ne vous inquiétez pas si le mot « Interactors » vous a semblé étrange, nous allons en apprendre davantage à leur sujet bientôt.

De l'intérieur vers l'extérieur, nous allons explorer chacune des couches un peu plus en détail. Nous utiliserons une application d'exemple qui nous est assez familière : les compteurs. Il ne faut pas de temps pour comprendre, donc nous pouvons nous concentrer sur le sujet de cet article.

Vous pouvez trouver une démonstration de l'application [ici](http://www.dvalbrand.com/counter-clean-architecture/), et les exemples de code seront en TypeScript. Certains des extraits de code ci-dessous utilisent React et Redux. Certaines connaissances sur ces solutions peuvent aider à les comprendre. Pourtant, les concepts de Clean Architecture sont beaucoup plus universels. Vous serez en mesure de les comprendre même sans connaissance préalable des outils mentionnés.

#### Entités

Les entités sont dans le diagramme en tant que Règles Métiers de l'Entreprise. Les entités incluent les règles métiers qui sont universelles à une entreprise. Elles représentent des entités qui sont basiques à son domaine d'opération. Elles sont les composants avec le niveau d'abstraction le plus élevé.

Dans notre exemple de compteurs, il y a une Entité très évidente : le `Counter` lui-même.

#### Cas d'Utilisation

Les Cas d'Utilisation sont indiqués comme Règles Métiers de l'Application. Ils représentent chacun des cas d'utilisation d'une seule application. Chaque élément de cette couche fournit une interface à la couche externe et agit comme un hub qui communique avec d'autres parties du système. Ils sont responsables de l'exécution complète des cas d'utilisation et sont communément appelés Interactors.

Dans notre exemple, nous avons un Cas d'Utilisation pour `incrémenter` ou `décrémenter` notre `counter` :

Notez que la fonction de fabrication pour `ChangeCounterInteractor` reçoit un paramètre de type `CounterGateway`. Nous discuterons de l'existence de ce type plus tard dans l'article. Mais nous pouvons dire que les Gateways sont ce qui se trouve entre les Cas d'Utilisation et la couche suivante.

#### Adaptateurs d'Interface

Cette couche constitue la frontière entre les règles métiers du système et les outils qui lui permettent d'interagir avec le monde extérieur, comme les bases de données et les interfaces graphiques. Les éléments de cette couche agissent comme des médiateurs, recevant des données d'une couche et les transmettant à l'autre, en adaptant les données selon les besoins.

Dans notre exemple, nous avons plusieurs Adaptateurs d'Interface. L'un d'eux est le composant React qui présente le `Counter` et ses contrôles pour `incrémenter` et `décrémenter` :

Notez que le composant n'utilise pas une instance de `Counter` pour présenter sa valeur, mais une instance de `CounterViewData` à la place. Nous avons fait ce changement pour **découpler la logique de présentation des données métiers**. Un exemple de cela est la logique d'affichage du compteur basée sur le mode de vue (chiffres romains ou indo-arabes). Une implémentation de `CounterViewData` suit ci-dessous :

Un autre exemple d'Adaptateur d'Interface serait notre implémentation Redux de l'application. Les modules responsables des requêtes à un serveur et l'utilisation du stockage local vivraient également à l'intérieur de cette couche.

#### Frameworks et Drivers

Les outils que votre système utilise pour communiquer avec le monde extérieur composent la couche la plus externe. Nous n'écrivons généralement pas de code dans cette couche, qui inclut des bibliothèques telles que React/Redux, les API du navigateur, etc.

#### La Règle de Dépendance

Cette division en couches a deux objectifs principaux. L'un d'eux est de clarifier les responsabilités de chaque partie du système. L'autre est de s'assurer que chacune d'elles remplit ses rôles aussi indépendamment que possible les unes des autres. Pour que cela se produise, il y a une règle qui stipule comment les éléments doivent dépendre les uns des autres :

**Un élément ne doit pas dépendre d'un élément appartenant à une couche extérieure à la sienne.**

Par exemple, un élément dans la couche des Cas d'Utilisation ne peut pas avoir de connaissance sur une classe ou un module lié à l'interface graphique ou à la persistance des données. De même, une Entité ne peut pas savoir quels Cas d'Utilisation l'utilisent.

Cette règle a peut-être soulevé des questions dans votre esprit. Prenons un Cas d'Utilisation, par exemple. Il est déclenché à la suite d'une interaction de l'utilisateur avec l'interface utilisateur. Son exécution implique la mise à jour dans un stockage de données persistant tel qu'une base de données. Comment l'Interactor peut-il effectuer les appels pertinents aux routines de mise à jour sans dépendre d'un Adaptateur d'Interface qui est responsable de la persistance des données ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*gPL-gKEX2D406BonMpA_NA.jpeg)

La réponse réside dans un élément que nous avons mentionné précédemment : les **Gateways**. Ils sont responsables de l'établissement de l'interface nécessaire aux Cas d'Utilisation pour accomplir leur travail. Une fois qu'ils ont établi cette interface, c'est aux Adaptateurs d'Interface de remplir leur partie du contrat, comme le montre le diagramme ci-dessus. Nous avons l'interface `CounterGateway` et une implémentation concrète utilisant Redux ci-dessous :

#### Vous n'en avez peut-être pas besoin

Bien sûr, cette application d'exemple était quelque peu trop compliquée pour une application de compteur d'incrémentation/décrémentation. Et je tiens à préciser que vous n'avez pas besoin de tout cela pour un petit projet ou un prototype. Mais croyez-moi, à mesure que votre application grandit, vous voudrez maximiser la réutilisabilité et la maintenabilité. Une bonne architecture logicielle rend les projets résistants au passage du temps.

#### D'accord... Alors quoi ?

Avec cet article, nous avons découvert une approche pour découpler les entités de nos systèmes. Cela les rend plus faciles à maintenir et à étendre. Par exemple, pour construire la même application en utilisant Vue.js, nous n'aurions qu'à réécrire les composants `CounterPage` et `CounterWidget`. Le code source de l'application d'exemple est dans le lien ci-dessous :

[**Valbrand/counter-clean-architecture**](https://github.com/Valbrand/counter-clean-architecture)
[_Contribuez au développement de counter-clean-architecture en créant un compte sur GitHub._github.com](https://github.com/Valbrand/counter-clean-architecture)

Cette histoire a été traduite en portugais par moi ! Elle est disponible [ici](https://medium.com/@Valbrand/voc%C3%AA-n%C3%A3o-%C3%A9-o-seu-framework-d95f81c28ae9).

Quels sont les avantages et les inconvénients que vous voyez dans cette approche ? Avez-vous utilisé quelque chose de similaire en production ? Partagez vos expériences dans les réponses. Si vous aimez l'article, applaudissez-moi !