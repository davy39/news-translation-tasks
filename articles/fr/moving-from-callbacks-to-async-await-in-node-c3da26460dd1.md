---
title: Comment passer des Callbacks à Async Await dans Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T18:03:44.000Z'
originalURL: https://freecodecamp.org/news/moving-from-callbacks-to-async-await-in-node-c3da26460dd1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ImJyPIRNLiLXjGSfJQl_dA.png
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
seo_title: Comment passer des Callbacks à Async Await dans Node
seo_desc: 'By Nitish Phanse

  I recently got a chance to work with Node again. Being a huge fan of promises, I
  never tried async await. Why? Because promises worked fine for me, that’s why.

  Sure thing promises work fine for simple controllers. Couple database que...'
---

Par Nitish Phanse

J'ai récemment eu l'occasion de travailler à nouveau avec Node. Étant un grand fan des promesses, je n'ai jamais essayé async await. Pourquoi ? Parce que les promesses fonctionnaient bien pour moi, c'est pourquoi.

Bien sûr, les promesses fonctionnent bien pour des contrôleurs simples. Couplez des requêtes de base de données et la gestion des erreurs, et les promesses peuvent devenir désagréables. Oui, même si vous les enchaînez. Et si une valeur résolue dans votre deuxième chaîne de promesses était nécessaire dans votre quatrième promesse ? Mais encore une fois, je contournais généralement le problème (_définir une variable let en haut de la portée de la fonction et la réassigner puis l'utiliser plus loin_).

### Définition du cas d'utilisation

Je crée une simple spécification d'API, où la route est `**POST /users**`. Le corps de la poste contient certains détails de l'utilisateur. Si l'utilisateur existe dans la base de données, ses valeurs sont mises à jour, sinon une nouvelle entrée est créée dans la base de données.

Pour simplifier, je n'utilise aucun ORM / base de données. Je crée un modèle d'utilisateur factice et utilise `setTimeout` pour simuler des appels d'API et des requêtes de base de données. J'utilise également `Math.random()` pour décider s'il faut lancer une erreur pour le cas de la gestion des erreurs.

> Je vais faire ces appels d'abord via des callbacks, puis des promesses, et enfin en utilisant async/await.

Ok, c'est l'heure de faire un peu de code maintenant.

#### **Serveur express simple**

#### **Modèle d'utilisateur**

Ce code de modèle d'utilisateur est un objet utilisateur factice qui effectuera des appels d'API simulés. Il y a deux types d'appels effectués : l'un avec des callbacks et l'autre avec des promesses. Les deux font effectivement la même chose. Encore une fois, j'ai codé en dur beaucoup de choses ici pour simplifier.

### Callbacks

La manière traditionnelle de faire toute sorte d'I/O non bloquant était avec un callback où tout appel d'I/O était de la forme

```
someAsyncOperation(dataObject, function(error, success) {
```

```
  if (error) {    // gérer l'erreur  } else {    // faire quelque chose avec succès  }})
```

Cela fonctionne bien si vous effectuez une opération asynchrone. Si vous finissez par faire plusieurs opérations asynchrone avec des callbacks, vous finirez par ce qu'on appelle la _pyramide de l'enfer des callbacks_.

#### **_Avantages :_**

1. Pratique pour les opérations asynchrone uniques. Permet un contrôle facile des données et des erreurs.
2. Devrait fonctionner sur chaque version de node et presque tous les packages de node. Comme les callbacks sont des fonctions, elles n'ont pas besoin de transpilers.

#### **_Inconvénients :_**

1. Pour plusieurs opérations asynchrone imbriquées, cela crée un enfer de callbacks
2. La gestion des erreurs doit être faite pour chaque opération (pas de gestionnaire d'exceptions global)

### Promesses

Les promesses sont des objets qui ont 3 états principaux — en attente, résolue et rejetée. Selon la réponse d'une action asynchrone, une promesse est soit résolue soit rejetée. Plusieurs promesses peuvent être enchaînées les unes sous les autres. Un seul gestionnaire catch en bas est suffisant pour une erreur dans n'importe quelle promesse.

#### **_Avantages :_**

1. Permet un enchaînement facile des opérations asynchrone. Ce qui est retourné dans la fonction `.then` peut être enchaîné dans la fonction `.then` suivante.
2. Un gestionnaire catch en bas attrapera une erreur si l'une des promesses enchaînées lance une exception.

#### **_Inconvénients :_**

1. La plupart des bibliothèques peuvent nécessiter un wrapper promisify autour comme bluebird, sauf si elles supportent les promesses dès le départ.
2. La portée d'une fonction enchaînée est isolée à cette fonction elle-même. Donc certaines données résolues dans la deuxième chaîne ne peuvent pas être utilisées dans la quatrième chaîne sauf si une variable let globale est déclarée.

### Async / Await

Async / await, à la fin de la journée, est toujours une promesse. C'est juste une manière d'écrire du code asynchrone de manière synchrone.

Chaque fonction asynchrone doit être préfixée avec `async`. Chaque action asynchrone doit être préfixée avec le mot `await`. De plus, chaque fonction asynchrone retourne une promesse qui peut être résolue plus loin.

#### **_Avantages :_**

1. CODE PROPRE. Je ne peux pas insister assez sur ce point. Toutes les parties résolues peuvent être accessibles dans le bloc try.
2. L'ensemble du bloc peut être traité comme un morceau de code synchrone. (Bien qu'il soit asynchrone par nature).
3. Ajout de try, catch au code asynchrone.
4. Un gestionnaire d'erreurs unifié dans le bloc catch.

#### **_Inconvénients :_**

1. Node 8+ est livré avec async await intégré. Pour les versions plus anciennes, un transpiler babel est nécessaire pour le code côté serveur.
2. L'ajout du mot-clé async n'est pas très intuitif.
3. L'utilisation de async/await à l'intérieur d'un constructeur de promesse est un anti-pattern.

4. Encore une fois, pour certaines bibliothèques ne supportant que les callbacks, une bibliothèque promisify globale peut être nécessaire pour supporter async / await

### **Conclusion**

En conclusion, je dirais que nous avons converti un cas d'utilisation particulier d'une forme de callbacks à des promesses pour enfin utiliser async await.

Dans l'ensemble, mon avis sur cela est que j'ai trouvé le code async await vraiment propre et facile à comprendre. Comme les gens veulent apprendre Node, ils trouvent la partie asynchrone une tâche intimidante. De plus, les personnes venant d'un background Java, PHP ou même Python peuvent facilement commencer à créer des applications dans node sans se soucier des callbacks / promesses.

J'espère que cet article a été utile. Au cas où il y aurait des erreurs, faites-le moi savoir. Je serais heureux de les corriger.