---
title: Model-View-Controller (MVC) Expliqué à travers la Commande de Boissons au Bar
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-02T14:32:25.000Z'
originalURL: https://freecodecamp.org/news/model-view-controller-mvc-explained-through-ordering-drinks-at-the-bar-efcba6255053
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VRDZ0Xh-gOEJlAm1h7UMOg.jpeg
tags:
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Model-View-Controller (MVC) Expliqué à travers la Commande de Boissons
  au Bar
seo_desc: 'By Kevin Kononenko

  If you have been to a bar, then MVC ain’t that hard.

  Model-view-controller (MVC) frameworks are a crucial part of building modern web
  applications. Walk into a room of web developers, and you will likely be bombarded
  with mentions ...'
---

Par Kevin Kononenko

#### Si vous êtes déjà allé dans un bar, alors MVC n'est pas si difficile.

Les frameworks Model-View-Controller (MVC) sont une partie cruciale de la construction d'applications web modernes. Entrez dans une pièce remplie de développeurs web, et vous serez probablement bombardé de mentions de Ruby on Rails, Angular ou Django.

Plus généralement, la logique MVC peut être utilisée pour décrire presque n'importe quel processus de développement web qui utilise un langage comme PHP, Ruby, Python ou JavaScript.

#### Néanmoins...

De nombreux développeurs web naviguent dans ce monde mystérieux en se frayant un chemin à travers les obstacles avec un sourire sur le visage. Lorsqu'un développeur senior ou un coéquipier doit examiner le code de l'un de ces développeurs, il poussera immédiatement un cri, suivi d'une rapide leçon sur les pratiques de codage courantes.

Ce n'est pas une façon de vivre ! En fait, le modèle MVC dans le développement web moderne peut être facilement expliqué en commandant une boisson à un barman. Et oui, cela signifie que si vous êtes déjà allé dans un bar, alors vous pouvez comprendre le principal modèle structurel partagé par toutes les applications web.

![Image](https://cdn-media-1.freecodecamp.org/images/1*f0mX-pFfwmoQKGdIUQoXEQ.jpeg)

_Braver les obstacles jusqu'à ce que la réalité frappe_

**Qu'est-ce que le modèle MVC ?**

* **Modèle** : Structure vos données sous une forme fiable et les prépare en fonction des instructions du contrôleur
* **Vue** : Affiche les données à l'utilisateur dans un format facile à comprendre, en fonction des actions de l'utilisateur
* **Contrôleur** : Reçoit les commandes de l'utilisateur, envoie des commandes au modèle pour les mises à jour des données, envoie des instructions à la vue pour mettre à jour l'interface.

Ou, sous forme de diagramme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4SxbmCrI5YVp1Uyj1Jstsg.png)
_Crédit Image : Real Python_

C'était ennuyeux. Passons au bar.

#### Un développeur web débutant entre dans un bar...

Vous entrez dans un bar un vendredi soir et vous approchez du barman. Comme le bar est déjà bondé, vous vous frayez un chemin à travers la foule jusqu'à ce que vous attiriez enfin l'attention du barman, et vous lancez, « Un Manhattan, s'il vous plaît ! »

Vous êtes l'**utilisateur**, et votre commande de boisson est la **requête de l'utilisateur**. Pour vous, le Manhattan est simplement votre boisson préférée, et vous savez assez bien que ce sera une boisson sucrée et délicieuse.

Le barman vous fait un rapide signe de tête. Pour le barman, le Manhattan n'est pas une boisson savoureuse, c'est simplement une série d'étapes :

1. Prendre un verre
2. Ajouter du whisky
3. Ajouter du vermouth
4. Ajouter des amers
5. Remuer la boisson
6. Ajouter une cerise
7. Demander la carte de crédit et facturer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AMWKKh4SxqNrcM5dNnSsfQ.jpeg)
_Crédit Image : Wikipedia_

Le cerveau du barman est le **contrôleur**. Dès que vous prononcez le mot « Manhattan » dans une langue qu'il comprend, le travail commence. Ce travail est similaire dans la nature à la préparation d'une margarita ou d'un daiquiri à la fraise, mais utilise des ingrédients distincts qui ne seront jamais confondus. Le barman ne peut utiliser que les outils et les ressources qui se trouvent derrière le bar. Cet ensemble d'outils limité est le **modèle**, et comprend les éléments suivants :

* Les mains du barman
* Shakers/équipement de mélange
* Alcools
* Mélanges
* Verres
* Garnitures

Peut-être que dans un bar plus chic, ils pourraient avoir un assistant robot ! Ou un mélangeur de boissons automatique. Cela n'a pas d'importance pour votre barman particulier, qui ne peut utiliser que les ressources disponibles.

Enfin, la boisson finie que vous pouvez voir et consommer est la **vue**. La vue est construite à partir des options limitées du modèle, et arrangée et transmise via le contrôleur (c'est-à-dire le cerveau du barman).

### **Leçons Apprises**

* Vous voulez une autre boisson ? Crier sur votre verre vide, la vue, ne vous sera d'aucune utilité. Vous devez parler au barman.
* Le temps passé entre le moment où le barman entend la demande et commence à créer la boisson doit être absolument minimal. Cela est parfois connu sous le nom de « contrôleur maigre » - en d'autres termes, le contrôleur doit contenir une quantité minimale de logique, et déléguer autant que possible au modèle. Un excellent barman aura non seulement mémorisé les recettes, mais préparera également les ingrédients et les outils de manière fiable chaque soir afin qu'un minimum de recherche et d'arrangement soit nécessaire une fois que les clients commencent à commander.
* Le barman pourrait-il verser tous les ingrédients directement dans la bouche du client et s'attendre à ce que le client les fasse tourner et mélange la boisson ? Oui, peut-être, je suppose. Vous voulez garder autant de votre logique que possible dans le modèle plutôt que dans la vue. En d'autres termes, préparer la boisson derrière le bar est préférable à la mélanger dans la bouche du client.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fpP-3F2rQUApiAx5Hm3H7w.png)
_Crédit Image : Xperience_

* Si vous commandez une bière, le barman n'aura presque rien à faire. Peut-être qu'il enlèvera simplement le bouchon et vous tendra la boisson. Cela dit, vous devez toujours demander au barman. La bière n'apparaîtra pas magiquement devant vous.

### Relier cela au Développement Web

Voici comment le même processus se déroule dans une application web moderne :

* L'utilisateur fait une **requête** le long d'une route, disons /home.
* Le **contrôleur** reçoit cette requête et donne un ensemble spécifique d'ordres qui sont liés à cette route. Ces instructions pourraient être soit pour la **vue** de mettre à jour ou de servir une certaine page, soit pour le **modèle** d'effectuer une logique spécifique. Supposons que cette requête ait une certaine logique associée.
* Le modèle exécute la logique, extrait d'une base de données et envoie une réponse cohérente basée sur les instructions du contrôleur.
* Le contrôleur transmet ensuite ces données à la vue pour mettre à jour l'interface utilisateur.

Chaque fois qu'une requête arrive, elle doit d'abord passer par le contrôleur avant de pouvoir être convertie en instructions pour la vue ou le modèle. L'article [Ruby on Rails sur Wikipedia](https://en.wikipedia.org/wiki/Ruby_on_Rails#Technical_overview) contient un aperçu supplémentaire si vous cherchez plus d'informations.

Chaque fois que vous devez apprendre un nouveau framework de développement web, vous rencontrerez ce modèle MVC cohérent. Et si un framework particulier diffère de celui-ci, vous pouvez être sûr que les auteurs expliqueront leur nouveau modèle avec des références à MVC.

Cela devrait rendre l'apprentissage beaucoup plus facile - une fois que vous développez avec MVC une fois, chaque nouveau framework peut s'intégrer dans votre zone de confort.

**Avez-vous apprécié ce guide ? Faites-le moi savoir dans les commentaires !**