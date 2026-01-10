---
title: Une introduction aux Subjects en programmation réactive
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-28T16:15:19.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-subjects-in-reactive-programming-bbdc8fed7b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6gi30QcIoPkwcxpz5d4wkg.png
tags:
- name: JavaScript
  slug: javascript
- name: observables
  slug: observables
- name: Reactive Programming
  slug: reactive-programming
- name: RxJS
  slug: rxjs
- name: 'tech '
  slug: tech
seo_title: Une introduction aux Subjects en programmation réactive
seo_desc: 'By Dler Ari

  A Subject is a “special” type of observable that allows us to broadcast values to
  multiple subscribers. The cool thing about Subjects, is that it provides a real-time
  response.

  For instance, if we have a subject with 10 subscribers, whene...'
---

Par Dler Ari

Un Subject est un type "spécial" d'observable qui nous permet de diffuser des valeurs à plusieurs abonnés. Le côté intéressant des Subjects, c'est qu'ils fournissent une réponse en temps réel.

Par exemple, si nous avons un subject avec 10 abonnés, chaque fois que nous poussons des valeurs vers le subject, nous pouvons voir la valeur capturée par chaque abonné.

Cela introduit quelques défis ; que se passe-t-il si nous poussons certaines valeurs, puis nous abonnons, ou vice-versa ? Le timing joue un rôle important, si nous nous abonnons tard, nous ne pourrons pas accéder aux valeurs, similaire à si quelqu'un rejoint un événement sportif en direct à la télévision 30 minutes plus tard.

Heureusement, nous avons 4 types de Subjects qui nous permettent de "voyager dans le temps" dans lesquels nous pouvons accéder aux valeurs même si nous nous abonnons tard ou non.

#### Sujets que nous allons couvrir :

1. Qu'est-ce qu'un Subject avec un exemple pratique
2. BehaviorSubject : Obtenir le dernier message
3. ReplaySubject : Voyage dans le temps
4. AsyncSubject : Une fois terminé, obtenir le dernier message

### 1. Qu'est-ce qu'un Subject ?

Comme mentionné, un Subject n'est rien de plus qu'un observable avec quelques caractéristiques supplémentaires. Un observable est par définition une [collection invocable](https://rxjs.dev/guide/overview) qui émet des données une fois abonné. Pendant ce temps, un Subject est là où nous contrôlons l'état du "quand émettre des données" à plusieurs abonnés.

Un Subject nous permet d'invoquer des méthodes comme `.next()`, `.complete()` et `.error()` à l'extérieur, tandis que dans un observable, nous invoquons ces méthodes en tant que callbacks.

```js
// Création d'un Observable
const observable = new Observable((observer) => {
    observer.next(10);
    observer.next(5);
    observer.complete();
});

// Création d'un Subject
const subject = new Subject();
subject.next(10);
subject.next(5);
subject.complete();
```

#### Exemple pratique : Construisons un simple groupe de chat en utilisant un Subject

Imaginons que nous construisons une simple application de chat où les gens peuvent poster des messages dans le groupe de chat. La première étape est de créer une instance du Subject, puis de l'assigner à un `chatGroup`.

```js
// Créer un subject "Observable"
const chatGroup = new Subject();
```

Maintenant que notre groupe de chat (Subject) est créé, la prochaine chose à faire est d'ajouter des messages. Créons une conversation typique entre deux amis.

```js
// Pousser des valeurs vers le flux
chatGroup.next('David - Salut, quelle série à la mode recommandes-tu ?');
chatGroup.next('Peter - Game of Thrones, Bodyguard ou Narcos sont quelques-unes des bonnes');
chatGroup.next('David - Intéressant, laquelle est la plus à la mode ?');
chatGroup.next('Peter - Game of Thrones !');
```

Jusqu'à présent, tout va bien — nous avons 4 messages postés dans notre groupe de chat, alors que se passe-t-il si nous nous abonnons ? Ou disons qu'un nouvel ami nommé John veut rejoindre la conversation. Peut-il voir les anciens messages ?

```js
// Afficher les messages
chatGroup.subscribe((messages) => {
    console.log(messages)
})
```

Malheureusement non, John rate la conversation parce qu'il s'abonne tard. C'est un exemple parfait de la façon dont la programmation réactive fonctionne — l'idée de valeurs passant au fil du temps, et ainsi, nous devons nous abonner au bon moment pour accéder aux valeurs.

Pour élargir l'exemple précédent, que se passe-t-il si John entre au milieu de la conversation ?

```js
// Pousser des valeurs vers le flux
chatGroup.next('David - Salut, quelle série à la mode recommandes-tu ?');
chatGroup.next('Peter - Game of Thrones, Bodyguard ou Narcos sont quelques-unes des bonnes');

// John entre dans la conversation
chatGroup.subscribe((messages) => {
    console.log(messages)
});

chatGroup.next('David - Intéressant, laquelle est la plus à la mode ?');
chatGroup.next('Peter - Game of Thrones !');

// SORTIE
// David - Intéressant, laquelle est la plus à la mode ?
// Peter - Game of Thrones !
```

Une fois que John s'abonne, il voit les deux derniers messages. Le Subject fait ce pour quoi il est prévu. Mais que faire si nous voulons que John voie tous les messages, ou seulement le dernier, ou soit notifié lorsqu'un nouveau message est posté ?

En général, ces Subjects sont principalement similaires, mais chacun offre une fonctionnalité supplémentaire, décrivons-les un par un.

### 2. BehaviorSubject : Obtenir le dernier message

Le BehaviorSubject est similaire à un Subject sauf qu'il nécessite une valeur initiale en tant qu'argument pour marquer le point de départ du flux de données. La raison est que lorsque nous nous abonnons, il retourne le dernier message. C'est un concept similaire lorsque nous traitons avec des tableaux ; où nous faisons `array.length-1` pour obtenir la dernière valeur.

```js
import {BehaviorSubject } from "rxjs";

// Créer un Subject
const chatGroup = new BehaviorSubject('Point de départ');

// Pousser des valeurs vers le flux de données
chatGroup.next('David - Salut, quelle série à la mode recommandes-tu ?');
chatGroup.next('Peter - Game of Thrones, Bodyguard ou Narcos sont quelques-unes des bonnes');
chatGroup.next('David - Intéressant, laquelle est la plus à la mode ?');
chatGroup.next('Peter - Game of Thrones !');

// John entre dans la conversation
chatGroup.subscribe((messages) => {
    console.log(messages)
})

// SORTIE
// Peter - Game of Thrones !
```

### 3. ReplaySubject : Voyage dans le temps

Le ReplaySubject, comme son nom l'indique, une fois abonné, il diffuse tous les messages, peu importe si nous nous sommes abonnés tard ou non. C'est comme un voyage dans le temps, où nous pouvons accéder à toutes les valeurs qui ont été diffusées.

```js

import { ReplaySubject } from "rxjs";

// Créer un Subject
const chatGroup = new ReplaySubject();

// Pousser des valeurs vers le flux de données
chatGroup.next('David - Salut, quelle série à la mode recommandes-tu ?');
chatGroup.next('Peter - Game of Thrones, Bodyguard ou Narcos sont quelques-unes des bonnes');
chatGroup.next('David - Intéressant, laquelle est la plus à la mode ?');
chatGroup.next('Peter - Game of Thrones !');

// John entre dans la conversation
chatGroup.subscribe((messages) => {
    console.log(messages)
})

// SORTIE
// David - Salut, quelle série à la mode recommandes-tu ?'
// Peter - Game of Thrones, Bodyguard ou Narcos sont quelques-unes des bonnes'
// David - Intéressant, laquelle est la plus à la mode ?'
// Peter - Game of Thrones !'
```

### 4. AsyncSubject : Une fois terminé, obtenir le dernier message

L'AsyncSubject est similaire au BehaviorSubject en termes d'émission de la dernière valeur une fois abonné. La seule différence est qu'il nécessite une méthode `complete()` pour marquer le flux comme terminé. Une fois cela fait, la dernière valeur est émise.

```js
import { AsyncSubject } from "rxjs";

// Créer un Subject
const chatGroup = new AsyncSubject();

// Pousser des valeurs vers le flux de données
chatGroup.next('David - Salut, quelle série à la mode recommandes-tu ?');
chatGroup.next('Peter - Game of Thrones, Bodyguard ou Narcos sont quelques-unes des bonnes');
chatGroup.next('David - Intéressant, laquelle est la plus à la mode ?');
chatGroup.next('Peter - Game of Thrones !');

chatGroup.complete(); // <-- Marquer le flux comme terminé

// John entre dans la conversation
chatGroup.subscribe((messages) => {
    console.log(messages)
})

// SORTIE
// Peter - Game of Thrones !'
```

### Résumé

Revenons à notre exemple précédent avec John, nous pouvons maintenant décider si nous voulons que John accède à toute la conversation (ReplaySubject), au dernier message (BehaviorSubject), ou au dernier message une fois la conversation terminée (AsyncSubject).

Si vous avez du mal à identifier si un Subject est la bonne solution, l'article « [To Use a Subject or Not to Use a Subject](http://davesexton.com/blog/post/To-Use-Subject-Or-Not-To-Use-Subject.aspx) » de Dave Sixton décrit quand utiliser les Subjects selon deux critères :

1. Uniquement lorsque l'on veut **convertir** un Observable froid en un observable chaud.
2. **Générer** un observable chaud qui passe des données en continu.

En bref, seule la créativité limite le potentiel d'utilisation de la programmation réactive. Il y aura certains scénarios où les Observables feront la majeure partie du travail, mais comprendre ce que sont les Subjects et quels types de Subjects existent, améliorera définitivement vos compétences en programmation réactive.

Si vous êtes intéressé à en apprendre davantage sur l'écosystème web, voici quelques articles que j'ai écrits, profitez-en.

* [Une comparaison entre Angular et React](https://medium.freecodecamp.org/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76)
* [Un guide pratique des modules ES6](https://medium.freecodecamp.org/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773)
* [Comment effectuer des requêtes HTTP en utilisant l'API Fetch](http://A practical ES6 guide on how to perform HTTP requests using the Fetch API)
* [Concepts web importants à apprendre](https://medium.freecodecamp.org/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0?gi=6274e9c4d599)
* [Améliorez vos compétences avec ces méthodes JavaScript](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f)
* [Créer des commandes bash personnalisées](https://codeburst.io/learn-how-to-create-custom-bash-commands-in-less-than-4-minutes-6d4ceadd9590)

Vous pouvez me trouver sur Medium où je publie sur une base hebdomadaire. Ou vous pouvez me suivre sur [Twitter](http://twitter.com/dleroari), où je poste des conseils et astuces pertinents sur le développement web.