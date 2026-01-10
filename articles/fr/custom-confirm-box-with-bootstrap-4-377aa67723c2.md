---
title: Comment créer une boîte de confirmation personnalisée avec Bootstrap4 et ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-23T15:55:43.000Z'
originalURL: https://freecodecamp.org/news/custom-confirm-box-with-bootstrap-4-377aa67723c2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8tI8tEqNrAaaNkDAbXEQsw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer une boîte de confirmation personnalisée avec Bootstrap4 et
  ES6
seo_desc: 'By Prashant Yadav

  We put lots of sweat into achieving a good design, but imagine a scenario where
  we have to use something which is styled default to browsers. It ruins our hard
  work as it changes browser to browser.

  Same happened with me: I had put ...'
---

Par Prashant Yadav

Nous mettons beaucoup de travail pour obtenir un bon design, mais imaginez un scénario où nous devons utiliser quelque chose qui est stylisé par défaut dans les navigateurs. Cela ruine notre travail acharné car cela change d'un navigateur à l'autre.

La même chose m'est arrivée : j'avais mis beaucoup d'efforts pour créer une SPA, mais le client voulait une boîte de confirmation avec une logique métier. Malheureusement, l'utilisation de la boîte de confirmation intégrée était le seul facteur étrange dans le design. J'ai donc créé une boîte de confirmation personnalisée.

Voyons comment vous pouvez créer votre propre boîte de confirmation personnalisée avec Bootstrap4 et [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/).

Un **modal** est une boîte de dialogue popup disponible avec Bootstrap. Nous pouvons utiliser sa fonctionnalité pour gérer la popup et la concevoir selon nos besoins. Il dispose de différentes méthodes que nous pouvons utiliser pour atteindre notre objectif.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jrEUFkPpPS4MUkcTpS9Chw.png)
_Boîte de confirmation personnalisée_

Consultez la démonstration en direct [ici](https://learnersbucket.com/examples/bootstrap4/custom-confirm-box-with-bootstrap/).

* Nous allons utiliser le modal Bootstrap4 pour créer la boîte de dialogue popup.
* Nous utiliserons la fonction de rappel (_callback_) JavaScript pour gérer la réponse.
* Comme Bootstrap dépend de JQuery, nous l'utiliserons pour les événements.

### #Méthodes du modal Bootstrap

.modal(options): Active le contenu en tant que modal avec les options ci-dessous.

.modal("toggle"): Affiche ou masque le modal en fonction de son état actuel.

.modal("show"): Ouvre le modal.

.modal("hide"): Masque le modal.

### #Options du modal Bootstrap

{backdrop: true ou false, default: true}: Le modal doit-il se masquer lorsqu'on clique à l'extérieur du modal.

{ keyboard: true ou false, default: true}: Le modal doit-il se masquer lorsqu'une touche du clavier est pressée.

{ show: true ou false, default: true}: Pour afficher le modal lors de l'initialisation.

### #Événements du modal Bootstrap

.on('show.bs.modal'): Lorsque le modal est sur le point d'être affiché mais ne l'est pas encore.

.on('shown.bs.modal'): Lorsque le modal est affiché.

.on('hide.bs.modal'): Lorsque le modal est sur le point d'être masqué mais ne l'est pas encore.

.on('hidden.bs.modal'): Lorsque le modal est masqué.

#### Dépendances

Importez toutes les dépendances en utilisant le CDN.

Nous allons maintenant créer une fonction qui générera notre boîte de confirmation avec notre message personnalisé et retournera la sortie sélectionnée par l'utilisateur.

Nous n'avons pas besoin de l'en-tête et du pied de page du modal. Nous utiliserons simplement le corps du modal et afficherons notre message dans une balise <h4>. Ensuite, nous créerons deux boutons en dessous avec différentes classes `btn-yes` et `btn-no` qui seront utilisés pour gérer la réponse.

#### Explication

* Nous avons créé une `fonction` qui accepte un `message` et un rappel `handler`.
* Dans celle-ci, nous ajoutons le modal à la fin de la balise `body` avec la méthode `appendTo` de JQuery.
* Après avoir ajouté le modal, nous déclenchons ou affichons le modal avec la méthode `modal` de Bootstrap. Nous passons également deux paramètres `{backdrop: 'static', keyboard:false}` qui empêchent le modal de se masquer avec les événements du clavier, comme appuyer sur la touche **ÉCHAP** ou cliquer dans la zone de l'arrière-plan.
* Nous vérifions si le modal est masqué avec `hidden.bs.modal` de Bootstrap, puis nous supprimons le modal avec la méthode `remove` de JQuery. Cela empêchera d'ajouter un modal à chaque fois.

Nous avons créé une fonction qui rendra et ouvrira notre boîte de confirmation personnalisée, nous devons donc maintenant gérer la réponse fournie par l'utilisateur.

Nous utiliserons une fonction de rappel pour gérer la réponse. En JavaScript, nous pouvons passer la fonction en tant qu'argument à une autre fonction et l'appeler. Les fonctions passées en tant qu'arguments sont appelées fonctions de rappel.

### Gestion de la réponse

#### Explication

Si le bouton **oui** ou **non** est pressé, nous passons `true` ou `false` à la fonction de rappel et l'appelons. Après cela, nous masquons le modal.

Nous pouvons appeler notre boîte de confirmation comme ceci où nous le souhaitons.

Consultez la démonstration en direct [ici](https://learnersbucket.com/examples/bootstrap4/custom-confirm-box-with-bootstrap/).

Avec une boîte de confirmation personnalisée, nous avons un contrôle total sur le design et un certain contrôle sur la fonctionnalité.

Si vous avez aimé cet article, donnez-lui quelques ? et partagez-le ! Si vous avez des questions à ce sujet, n'hésitez pas à me les poser.

_Pour plus de contenu comme celui-ci et des solutions algorithmiques en Javascript, suivez-moi sur_ [**Twitter**](https://twitter.com/LearnersBucket)_._ J'écris sur [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/), React, Nodejs, [Structures de données](https://learnersbucket.com/tutorials/topics/data-structures/), et [Algorithmes](https://learnersbucket.com/examples/topics/algorithms/) sur [_learnersbucket.com_](https://learnersbucket.com/)_._