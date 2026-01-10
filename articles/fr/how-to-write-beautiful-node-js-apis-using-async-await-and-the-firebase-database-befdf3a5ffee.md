---
title: Comment écrire de belles API Node.js en utilisant async/await et la base de
  données Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-05T03:29:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-beautiful-node-js-apis-using-async-await-and-the-firebase-database-befdf3a5ffee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6wZYofh0czXf3SO8Ubw2xg.png
tags:
- name: Firebase
  slug: firebase
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment écrire de belles API Node.js en utilisant async/await et la base
  de données Firebase
seo_desc: 'By Paul Breslin

  This tutorial will cover the typical use cases you’ll come across when writing RESTful
  API endpoints to read and write to a Firebase Database instance.

  There will be a focus on beautiful asynchronous code, which makes use of the async...'
---

Par Paul Breslin

Ce tutoriel couvrira les cas d'utilisation typiques que vous rencontrerez lors de l'écriture de points de terminaison d'API RESTful pour lire et écrire dans une instance de base de données Firebase.

Il y aura un accent sur le code asynchrone **beau**, qui utilise la fonctionnalité `async/await` dans Node.js (disponible dans la version 7.6 et supérieure).

(N'hésitez pas à sourire doucement en disant au revoir à l'enfer des callbacks ?)

### Prérequis

Je suppose que vous avez déjà une application Node.js configurée avec le Firebase Admin SDK. Si ce n'est pas le cas, consultez le [guide d'installation officiel](https://firebase.google.com/docs/admin/setup).

### Écrire des données

Commençons par créer un exemple de point de terminaison `POST` qui sauvegardera des mots dans notre instance de base de données Firebase :

Il s'agit d'un point de terminaison très basique qui prend un `userId` et une valeur `word`, puis sauvegarde le mot donné dans une collection `words`. Assez simple.

Mais quelque chose ne va pas. Il nous manque la gestion des erreurs ! Dans l'exemple ci-dessus, nous retournons un code de statut `201` (signifiant que la ressource a été créée), même si le mot n'a pas été correctement sauvegardé dans notre instance de base de données Firebase.

Alors, ajoutons une gestion des erreurs :

Maintenant que le point de terminaison retourne des codes de statut précis, le client peut afficher un message pertinent à l'utilisateur. Par exemple, « Mot sauvegardé avec succès. » Ou « Impossible de sauvegarder le mot, cliquez ici pour réessayer. »

> Note : si certaines syntaxes ES2015+ vous semblent inconnues, consultez le guide Babel [ES2015](https://babeljs.io/learn-es2015/).

### Lire des données

D'accord, maintenant que nous avons écrit des données dans notre base de données Firebase, essayons de les lire.

Tout d'abord, voyons à quoi ressemble un point de terminaison `GET` en utilisant la méthode originale basée sur les promesses :

Encore une fois, assez simple. Maintenant, comparons-le avec une version `async/await` du même code :

Remarquez le mot-clé `async` ajouté avant les paramètres de la fonction `(req, res)` et le mot-clé `await` qui précède maintenant l'instruction `db.ref()`.

La méthode `db.ref()` retourne une promesse, ce qui signifie que nous pouvons utiliser le mot-clé `await` pour « suspendre » l'exécution du script. (Le mot-clé `await` peut être utilisé avec n'importe quelle promesse).

La méthode finale `res.send()` ne s'exécutera **qu'après** que la promesse `db.ref()` soit remplie.

C'est bien et bon, mais la vraie beauté de `async/await` devient apparente lorsque vous devez enchaîner plusieurs requêtes asynchrones.

Supposons que vous deviez exécuter un certain nombre de fonctions asynchrones séquentiellement :

Pas très joli. Cela est également connu sous le nom de « pyramide de la mort » (et nous n'avons même pas encore ajouté de gestionnaires d'erreurs).

Maintenant, regardez le même extrait réécrit pour utiliser `async/await` :

Plus de pyramide de la mort ! De plus, toutes les instructions `await` peuvent être enveloppées dans un seul bloc `try/catch` pour gérer les erreurs :

### Requêtes async/await parallèles

Que faire dans les cas où vous devez récupérer plusieurs enregistrements de votre base de données Firebase en même temps ?

Facile. Utilisez simplement la méthode `Promise.all()` pour exécuter des requêtes de base de données Firebase en parallèle :

### Une dernière chose

Lors de la création d'un point de terminaison pour retourner des données récupérées d'une instance de base de données Firebase, faites attention à ne pas simplement retourner tout `snapshot.val()`. Cela peut causer un problème avec l'analyse JSON côté client.

Par exemple, supposons que votre client a le code suivant :

Le `snapshot.val()` retourné par Firebase peut être soit un objet JSON, soit `null` si aucun enregistrement n'existe. Si `null` est retourné, le `response.json()` dans l'extrait ci-dessus générera une erreur, car il tente d'analyser un type non-objet.

Pour vous protéger contre cela, vous pouvez utiliser `Object.assign()` pour toujours retourner un objet au client :

Merci d'avoir lu !

_Intéressé à voir un projet réel construit sur Firebase et Node.js ? Découvrez [Vocabify](https://vocabifyapp.com), le constructeur de vocabulaire qui vous aide à retenir les mots que vous rencontrez._