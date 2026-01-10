---
title: Une introduction aux observables en programmation réactive
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-22T16:40:36.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-observables-in-reactive-programming-1cfd3e23bb94
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5FEY_E1x_bCfWpz3RiIFXw.png
tags:
- name: JavaScript
  slug: javascript
- name: Reactive Programming
  slug: reactive-programming
- name: RxJS
  slug: rxjs
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction aux observables en programmation réactive
seo_desc: 'By Dler Ari

  One of the most challenging things for new developers to learn is the observer pattern.
  Understanding how to effectively use it with RxJS to deal with asynchronous data
  such as user events, HTTP requests or any other events that require w...'
---

Par Dler Ari

L'une des choses les plus difficiles pour les nouveaux développeurs à apprendre est le modèle d'observateur. Comprendre comment l'utiliser efficacement avec RxJS pour gérer des données asynchrones telles que les événements utilisateur, les requêtes HTTP ou tout autre événement nécessitant d'attendre que quelque chose se termine est délicat.

Ce avec quoi la plupart des gens ont du mal, c'est la nouvelle approche. Cela nécessite un état d'esprit différent où la visualisation joue un rôle important. Nous considérons les données comme une séquence de valeurs qui se transmettent au fil du temps plutôt que comme une seule valeur récupérée une fois. Cet état d'esprit est connu sous le nom de programmation réactive.

Puisque le modèle d'observateur est un écosystème assez vaste composé de nombreuses parties importantes, j'ai choisi de le réduire en me concentrant uniquement sur les Observables. Je partagerai bientôt d'autres articles couvrant le reste du modèle d'observateur, comme comment gérer RxJS.

#### Sujets que nous allons couvrir :

1. Que signifie vraiment asynchrone ?
2. Quel modèle utiliser (Observer ou Promise)
3. Comment créer un Observable (les exemples de code commencent ici)
4. Comment s'abonner à un Observable
5. Comment se désabonner d'un Observable

### 1. Que signifie vraiment asynchrone ?

L'une des choses avec le web, et la majorité des langages, c'est que lorsque vous demandez des données comme une liste d'utilisateurs depuis le serveur, vous ne pouvez pas garantir que les données seront retournées. Il y a un problème d'incertitude.

L'une des raisons peut être que les données ne sont pas présentes, le serveur peut être en panne, ou l'URL HTTP n'est pas valide parce que quelqu'un a changé la chaîne de requête.

Pour cette raison, entre autres, nous devons traiter ces données de manière asynchrone. Nous demandons la liste des utilisateurs et attendons qu'elle soit récupérée, mais nous n'arrêtons pas toute l'application pour une simple opération.

C'est comme demander à un collègue de résoudre une tâche au lieu d'envoyer toute l'équipe ; ce serait une approche coûteuse et peu judicieuse.

Clarifions une idée fausse : les termes synchrone ou asynchrone n'ont rien à voir avec le multithreading, où les opérations sont exécutées en même temps. Cela signifie simplement que les opérations sont soit **dépendantes** soit **indépendantes** les unes des autres, c'est tout.

Comparons la différence entre synchrone et asynchrone pour mieux comprendre comment ils fonctionnent vraiment.

#### Qu'est-ce que le synchrone ?

Avec les événements synchrones, vous attendez qu'un événement se termine avant de passer à une autre tâche.

**Exemple :** Vous êtes dans une file d'attente pour obtenir un billet de cinéma. Vous ne pouvez pas en obtenir un tant que tout le monde devant vous n'en a pas obtenu un, et il en va de même pour les personnes derrière vous dans la file. Répondu par [themightysapien](https://stackoverflow.com/users/1428344/themightysapien).

#### Qu'est-ce que l'asynchrone ?

Avec les événements asynchrones, vous n'attendez pas, vous pouvez passer à la tâche suivante jusqu'à ce que les données soient disponibles.

**Exemple :** Vous êtes dans un restaurant avec beaucoup d'autres personnes. Vous commandez votre nourriture. D'autres personnes peuvent aussi commander leur nourriture, elles n'ont pas à attendre que votre nourriture soit cuisinée et servie avant de pouvoir commander. Dans la cuisine, les employés du restaurant cuisinent, servent et prennent des commandes en continu. Les gens recevront leur nourriture dès qu'elle sera cuisinée. Répondu par [themightysapien](https://stackoverflow.com/users/1428344/themightysapien).

D'accord, donc en résumé, cela nous permet soit d'attendre que les opérations se produisent avant de pouvoir continuer, soit de ne pas attendre jusqu'à ce que les données soient prêtes.

### 2. Quel modèle utiliser (Observer ou Promise)

Tout d'abord, le modèle d'observateur et le modèle de promesse traitent tous deux des opérations asynchrones. Des opérations telles que les événements utilisateur ou les requêtes HTTP, ou tout autre événement qui s'exécute indépendamment.

La majorité des opérations aujourd'hui nécessitent un certain type de gestion asynchrone/synchrone, et comprendre comment cela fonctionne joue un rôle important lors de la construction d'applications robustes.

Ce n'est pas censé rendre votre vie plus difficile, mais plus facile. Cependant, cela nécessite une courbe d'apprentissage qui peut être une approche douloureuse, mais la récompense à la fin en vaut la peine.

#### Restez avec un seul modèle

La différence réside dans la complexité de l'application. Si vous traitez une petite application où la tâche consiste simplement à obtenir une liste d'utilisateurs depuis le serveur, ou à afficher les membres actifs, alors les promesses avec l'`Fetch API` ([lire plus](https://medium.freecodecamp.org/a-practical-es6-guide-on-how-to-perform-http-requests-using-the-fetch-api-594c3d91a547)) fonctionnent bien.

Mais si vous traitez une grande application avec de nombreuses opérations asynchrones qui nécessitent de modifier les données, d'effectuer plusieurs opérations sur un flux de données, ou de les réutiliser à plusieurs endroits, alors le modèle d'observateur fonctionne très bien.

#### Puis-je utiliser les deux modèles dans un seul projet ?

Oui, mais il n'est pas recommandé de mélanger deux architectures qui font essentiellement la même chose (gérer des événements asynchrones). Au lieu de cela, restez avec un seul modèle et apprenez-en davantage à ce sujet.

#### Améliorez vos compétences avec RxJS

Avec RxJS, vous avez accès à 189 opérateurs avec documentation + [d'autres grandes ressources](https://reactive.how/). Et chacun de ces opérateurs sont simplement des rappels qui font quelque chose sur le flux de données.

Si vous êtes familier avec les prototypes fonctionnels de JavaScript (méthodes) tels que `map()`, `filter()`, et `reduce()`, vous les trouverez dans RxJS. Notez que le concept est le même mais le code écrit ne l'est pas.

Alors, quelle est la différence entre ces deux modèles ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*EAzaxT7ejRGLcvL4pgVqPA.png)
_Observable vs Promise_

Voici une comparaison rapide entre le modèle d'observateur et le modèle de promesse. Les points clés sont qu'une promesse émet une seule valeur une fois que le rappel `.then()` est utilisé, tandis qu'un Observable émet plusieurs valeurs sous forme de séquence de données qui se transmettent au fil du temps. Un autre point important est qu'un Observable peut être annulé ou réessayé tandis qu'une promesse ne le peut pas. Cependant, il existe des packages externes qui permettent d'annuler une promesse.

### 3. Comment créer un Observable ?

Voici quelques façons de créer un Observable :

* créer un Observable à partir de zéro
* transformer une promesse en Observable
* ou utiliser un framework qui le fait pour vous en arrière-plan, comme Angular.

> Saviez-vous qu'Angular utilise extensivement le modèle d'observateur ? Toutes les opérations asynchrones telles que HTTP GET ou l'écoute d'événements ou de changements de valeur suivent le modèle d'observateur.

Si vous souhaitez jamais imiter (tester) un scénario du monde réel, pour ainsi dire passer des valeurs au fil du temps, je vous recommande vivement d'utiliser la fonction interval. Cela passe des valeurs après x temps en millisecondes. Donc si vous avez un intervalle où x est 2000ms — il passe chaque valeur (incréments) après 2 secondes.

### 4. Comment s'abonner à un Observable ?

Un Observable est simplement une collection de données qui attend d'être invoquée (abonnée) avant de pouvoir émettre des données. Si vous avez travaillé avec des promesses, alors la façon d'accéder aux données est de les enchaîner avec l'opérateur `then()` ou d'utiliser l'`async/await` ES6.

Donc, en suivant l'exemple précédent, comment accède-t-on aux données ?

Comme montré ci-dessus, lorsque nous nous abonnons, nous disons à l'Observable de nous passer ce qu'il contient. Cela peut être un tableau, une collection d'événements, ou une séquence d'objets, etc.

Une erreur courante de débutant que j'ai vue parmi les développeurs est qu'ils effectuent de nombreuses opérations sur l'Observable mais s'énervent parce qu'ils ne voient aucun résultat. Vous n'êtes pas seul ! J'ai fait cette erreur plusieurs fois et en règle générale — n'oubliez jamais de vous abonner.

### 5. Comment se désabonner d'un Observable ?

Il est important de se désabonner, sinon nous finissons avec une fuite de mémoire qui ralentit le navigateur. Si vous avez travaillé avec Angular, il y a un pipe nommé `asyncPipe` qui s'abonne et se désabonne automatiquement pour vous.

La façon dont nous nous désabonnons est que nous créons une référence à chaque Observable qui est abonné en créant une variable pour préserver son état actuel. Ensuite, pour chaque variable, nous l'enchaînons avec la méthode `unsubscribe()`. N'oubliez pas que vous ne pouvez vous désabonner qu'après vous être abonné. C'est assez simple mais souvent oublié.

Remarquez, si vous vous désabonnez ici, `Observable_1` et `Observable_2` vont sortir les données avant qu'ils ne soient désabonnés parce que ce sont des Observables froids (non dépendants du temps), tandis que `Observable_3` et `Observable_4` ne vont rien sortir parce que ce sont des Observables chauds (dépendants du temps).

### Résumé

Comme mentionné ci-dessus, la partie la plus difficile de l'apprentissage du modèle d'observateur est l'état d'esprit. Un état d'esprit où nous regardons les valeurs différemment, comme une séquence de données qui émet au fil du temps. Dans cet article, nous avons couvert les types de façons dont nous pouvons créer un Observable, ainsi que comment s'abonner et se désabonner.

Je recommande d'utiliser le modèle d'observateur car il offre tout ce que le modèle de promesse offre, et bien plus. Il offre également quelques grands opérateurs pour empêcher les utilisateurs d'envoyer des milliers de requêtes inutiles au backend.

L'un d'eux est `debounceTime` qui donne à l'utilisateur assez de temps pour écrire un mot complet, puis envoie une requête au lieu d'une requête pour chaque caractère. Vous pouvez, bien sûr, atteindre cela avec une simple promesse, mais cela nécessite quelques lignes de code.

Je couvrirai davantage la programmation réactive dans un proche avenir, restez à l'écoute !

Si vous êtes intéressé à en apprendre davantage sur l'écosystème web, voici quelques articles que j'ai écrits pour améliorer vos compétences web, profitez-en :)

* [Améliorez vos compétences avec ces méthodes JavaScript](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f)
* [Une comparaison entre Angular et React](https://medium.freecodecamp.org/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76)
* [Un guide pratique des modules ES6](https://medium.freecodecamp.org/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773)
* [Comment effectuer des requêtes HTTP en utilisant l'API Fetch](http://A practical ES6 guide on how to perform HTTP requests using the Fetch API)
* [Concepts web importants à apprendre](https://medium.freecodecamp.org/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0?gi=6274e9c4d599)

> _Si vous voulez devenir un meilleur développeur web, démarrer votre propre entreprise, enseigner aux autres ou améliorer vos compétences en développement, vous pouvez me trouver sur Medium où je publie sur une base hebdomadaire. Ou vous pouvez me suivre sur [Twitter](http://twitter.com/dleroari), où je poste des conseils et astuces pertinents en développement web._

> _P.S. Si vous avez aimé cet article et en voulez plus comme celui-ci, veuillez applaudir ❤ et partager avec des amis qui pourraient en avoir besoin, c'est du bon karma._