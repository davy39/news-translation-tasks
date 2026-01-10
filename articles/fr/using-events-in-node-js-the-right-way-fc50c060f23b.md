---
title: Comment utiliser les événements dans Node.js de la bonne manière
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-03T17:01:06.000Z'
originalURL: https://freecodecamp.org/news/using-events-in-node-js-the-right-way-fc50c060f23b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_B5O6c-2DYQWOp0HV4hm7Q.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment utiliser les événements dans Node.js de la bonne manière
seo_desc: 'By Usama Ashraf

  Before event-driven programming became popular, the standard way to communicate
  between different parts of an application was pretty straightforward: a component
  that wanted to send out a message to another one explicitly invoked a me...'
---

Par Usama Ashraf

Avant que la programmation pilotée par événements ne devienne populaire, la manière standard de communiquer entre différentes parties d'une application était assez simple : un composant qui voulait envoyer un message à un autre invoquait explicitement une méthode sur ce composant. Mais le code piloté par événements est écrit pour _réagir_ plutôt que pour être _appelé_.

#### Les avantages de l'événementiel

Cette approche rend nos composants beaucoup **plus découplés**. Alors que nous continuons à écrire une application, nous identifions des événements en cours de route. Nous les déclenchons au bon moment et attachons un ou plusieurs _écouteurs d'événements_ à chacun d'eux. **L'extension des fonctionnalités devient beaucoup plus facile.** Nous pouvons ajouter plus d'écouteurs à un événement particulier. Nous ne modifions pas les écouteurs existants ni la partie de l'application où l'événement a été déclenché. Ce dont nous parlons est le modèle Observer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jAzlEy_JIYvhYRrrD-DcqA.jpeg)
_[https://www.dofactory.com/javascript/observer-design-pattern](https://www.dofactory.com/javascript/observer-design-pattern" rel="noopener" target="_blank" title=")_

#### Concevoir une architecture pilotée par événements

L'identification des événements est très importante. Nous ne voulons pas finir par devoir supprimer/remplacer des événements existants du système. Cela pourrait nous obliger à supprimer/modifier un nombre quelconque d'écouteurs qui étaient attachés à l'événement. Le principe général que j'utilise est de _considérer le déclenchement d'un événement uniquement lorsqu'une unité de logique métier termine son exécution._

Donc, disons que vous voulez envoyer une série de différents emails après l'inscription d'un utilisateur. Maintenant, le processus d'inscription lui-même peut impliquer de nombreuses étapes compliquées et des requêtes. Mais d'un point de vue métier, c'est _une seule étape_. Et chacun des emails à envoyer sont des étapes individuelles également. Il serait donc logique de déclencher un événement dès que l'inscription est terminée. Nous avons plusieurs écouteurs attachés à celui-ci, chacun responsable de l'envoi d'un type d'email.

L'architecture asynchrone et pilotée par événements de Node possède certains types d'objets appelés « émetteurs ». Ils émettent des événements nommés qui provoquent l'invocation de fonctions appelées « écouteurs ». Tous les objets qui émettent des événements sont des instances de la classe [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter). En l'utilisant, nous pouvons créer nos propres événements :

#### Un exemple

Utilisons le module intégré [events](https://nodejs.org/api/events.html) (que je vous encourage à consulter en détail) pour accéder à `EventEmitter`.

Voici la partie de l'application où notre serveur reçoit une requête HTTP, enregistre un nouvel utilisateur et émet un événement :

Et un module séparé où nous attachons un écouteur :

Il est bon de _séparer la politique de l'implémentation_. Dans ce cas, la politique signifie quels écouteurs sont abonnés à quels événements. L'implémentation signifie les écouteurs eux-mêmes.

Cette séparation permet également à l'écouteur de devenir réutilisable. Il peut être attaché à d'autres événements qui envoient le même message (un objet utilisateur). Il est également important de mentionner que _lorsque plusieurs écouteurs sont attachés à un seul événement, ils seront exécutés de manière synchrone et dans l'ordre où ils ont été attachés_. Ainsi, `someOtherListener` s'exécutera après que `sendEmailOnRegistration` ait terminé son exécution.

Cependant, si vous souhaitez que vos écouteurs s'exécutent de manière asynchrone, vous pouvez simplement envelopper leurs implémentations avec `setImmediate` comme ceci :

#### Gardez vos écouteurs propres

Respectez le principe de responsabilité unique lors de l'écriture des écouteurs. Un écouteur doit faire une seule chose et bien la faire. Évitez, par exemple, d'écrire trop de conditionnelles dans un écouteur qui décident quoi faire en fonction des données (message) transmises par l'événement. Il serait beaucoup plus approprié d'utiliser différents événements dans ce cas :

#### Détacher explicitement les écouteurs lorsque nécessaire

Dans l'exemple précédent, nos écouteurs étaient des fonctions totalement indépendantes. Mais dans les cas où un écouteur est associé à un objet (c'est une méthode), il doit être détaché manuellement des événements auxquels il s'était abonné. Sinon, l'objet ne sera jamais collecté par le garbage collector puisque une partie de l'objet (l'écouteur) continuera à être référencée par un objet externe (l'émetteur). Ainsi, la possibilité d'une fuite de mémoire.

Par exemple, si nous construisons une application de chat et que nous voulons que la responsabilité d'afficher une notification lorsqu'un nouveau message arrive dans un salon de discussion auquel un utilisateur s'est connecté incombe à cet objet utilisateur lui-même, nous pourrions faire ceci :

Lorsque l'utilisateur ferme son onglet ou perd sa connexion Internet pendant un certain temps, naturellement, nous pourrions vouloir déclencher un rappel côté serveur qui notifie les autres utilisateurs que l'un d'eux vient de se déconnecter. À ce stade, bien sûr, il n'a plus aucun sens que `displayNewMessageNotification` soit invoqué pour l'utilisateur hors ligne. Il continuera à être appelé pour les nouveaux messages à moins que nous ne le supprimions explicitement. Si nous ne le faisons pas, en plus de l'appel inutile, l'objet utilisateur restera également en mémoire indéfiniment. Assurez-vous donc d'appeler `disconnectFromChatroom` dans votre rappel côté serveur qui s'exécute chaque fois qu'un utilisateur se déconnecte.

#### Attention

Le couplage lâche dans les architectures pilotées par événements peut également entraîner une complexité accrue si nous ne sommes pas prudents. Il peut être difficile de suivre les dépendances dans notre système. Notre application deviendra particulièrement sujette à ce problème si nous commençons à émettre des événements à partir des écouteurs. Cela pourrait éventuellement déclencher des chaînes d'événements inattendus.