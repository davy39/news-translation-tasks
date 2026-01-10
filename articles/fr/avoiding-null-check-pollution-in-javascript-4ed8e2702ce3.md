---
title: 'Comment éviter la pollution des vérifications de null en JavaScript : utilisez
  les Optionnels'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-08T11:28:38.000Z'
originalURL: https://freecodecamp.org/news/avoiding-null-check-pollution-in-javascript-4ed8e2702ce3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uJIvAC_iHveiJ5BEse6YMA.jpeg
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Comment éviter la pollution des vérifications de null en JavaScript :
  utilisez les Optionnels'
seo_desc: 'By Konstantin Blokhin

  I’ve been using JavaScript for the past few years and have been enjoying it in general.
  But it lacks some cool features from other languages. For instance, there is no
  built-in safe navigation and no means to avoid null checks. ...'
---

Par Konstantin Blokhin

J'utilise JavaScript depuis quelques années et je l'apprécie généralement. Mais il manque certaines fonctionnalités intéressantes présentes dans d'autres langages. Par exemple, il n'y a pas de navigation sécurisée intégrée et aucun moyen d'éviter les vérifications de null. Le code est pollué par des branches conditionnelles boilerplate. C'est sujet aux erreurs et moins lisible.

Qu'est-ce qui ne va pas avec les vérifications de null, pourriez-vous demander ?

Tout d'abord, l'inventeur de la référence null, [Tony Hoare](http://en.wikipedia.org/wiki/Tony_Hoare), l'a qualifiée de **erreur à un milliard de dollars** :

> Mais je n'ai pas pu résister à la tentation d'inclure une référence null, simplement parce que c'était si facile à implémenter. Cela a conduit à d'innombrables erreurs, vulnérabilités et plantages système, qui ont probablement causé un milliard de dollars de douleur et de dommages au cours des quarante dernières années.

JavaScript ne fait pas exception. Combien de fois avez-vous rencontré l'erreur `TypeError: Cannot read property 'bar' of null` ? Pour éviter cela, les développeurs doivent toujours **garder à l'esprit cette possibilité de null**. Et ils préféreraient se concentrer sur la vraie chose, comme la logique spécifique à l'application.

Ensuite, vous devez effectivement introduire de nouvelles branches conditionnelles dans votre code. Et généralement, vous ne voulez pas en avoir beaucoup, car les instructions `**if**` **tendent à diminuer la lisibilité globale du code**. Prenez l'[anti-pattern de la flèche](http://wiki.c2.com/?ArrowAntiPattern) comme exemple extrême. De plus, ces instructions sont presque sans signification en termes de votre domaine ou de votre logique métier.

J'aime l'une des façons de résoudre ce problème, expliquée [ici](http://michaelfeathers.silvrback.com/converting-queries-to-commands) par Michael Feathers — l'approche des "commandes au lieu des requêtes". Et il développe également cette idée et [parle](https://www.youtube.com/watch?v=AnZ0uTOerUI) des avantages du code inconditionnel en général.

En gros, au lieu d'interroger une donnée et de vérifier si elle est présente pour un traitement ultérieur, nous exprimons simplement notre intention et laissons les internes du module décider si l'action doit être entreprise ou non.

Disons que nous voulons récupérer un utilisateur et les livres préférés de ses amis pour une recommandation. Le code pourrait être comme suit :

Donc, je préférerais avoir un module pour encapsuler la logique de vérification. Par conséquent, nous lui disons simplement quoi faire avec un utilisateur actif :

Le code est maintenant plus axé sur la logique métier. Et nous pouvons le réutiliser pour effectuer d'autres actions avec un utilisateur actif sans le fardeau des vérifications de null.

Mais la solution donnée est un peu trop spécifique. De plus, nous avons toujours une vérification de null dans notre contrôleur ou un autre endroit où nous utilisons la fonction.

Une approche plus générale est nécessaire. Ce dont nous avons besoin, c'est d'un type de données spécial, un conteneur pour les valeurs nulles — comme la classe [Optional](https://docs.oracle.com/javase/9/docs/api/java/util/Optional.html) en Java, par exemple. Le point est que toute action donnée au conteneur ne sera exécutée que sur une valeur contenue non vide.

Il existe certaines bibliothèques JS (comme [Optional.js](https://github.com/JasonStorey/Optional.js)), implémentant presque la même interface que Java Optional. Mais elles ne tiennent pas compte de la nature asynchrone de JS et ne fonctionnent pas avec les Promesses.

Et la plupart du temps, lorsque l'absence d'une valeur est possible, nous devons en réalité traiter avec des promesses et des fonctions asynchrones. Par exemple, prenons les requêtes de ressources externes comme les requêtes de base de données et les appels d'API.

C'est là que [AsyncOptional](https://github.com/treble-snake/async-optional) vient à la rescousse. Donc, **c'est un conteneur pour une valeur optionnelle de nature asynchrone**. *Optional* signifie que la valeur peut être présente ou absente. À la fois `null` et `undefined` sont considérés comme absents.

Dès que nous voulons dire au programme quoi faire avec une valeur non vide, la méthode de fabrication est appelée "with" :

```
const withUser = AsyncOptional.with(user);
```

Ensuite, nous pourrions faire un certain traitement, comme il est montré dans l'exemple ci-dessous. Une fois que nous avons terminé et que nous voulons fixer le résultat quelque part, l'une des méthodes terminales doit être utilisée.

Par exemple, lorsque nous n'avons pas besoin de réagir à une valeur vide :

Nous pouvons également spécifier quoi faire en cas d'absence de la valeur de cette manière naturelle :

Entre les appels de méthode de fabrication et terminale, il peut y avoir n'importe quelle logique de traitement, décrite dans le [readme](https://github.com/treble-snake/async-optional#transform-it). Il est garanti qu'aucune action ne sera entreprise sur une valeur vide.

Certaines des actions que vous pouvez utiliser pour traiter la valeur :

Alors, jetons un dernier coup d'œil à notre exemple :

Donc, en quoi est-ce mieux par rapport à l'original ?

Je crois que la réponse est — c'est bien **plus propre et lisible**, et la lisibilité est l'essence d'un bon code.

Tout d'abord, nous nous sommes débarrassés des branches conditionnelles de vérification de null, donc nous pouvons nous concentrer sur l'important — qui est la logique métier du système.

Ensuite, nous avons éliminé la possibilité d'avoir des exceptions de pointeur null ici. Cela signifie que nous n'avons pas à garder à l'esprit la nullabilité de la valeur, ce qui est une façon de moins d'introduire des bugs.

Un autre cas où la bibliothèque peut être utile est dans une situation de "valeur par défaut". Disons que nous avons une sorte de formulaire pour que l'utilisateur remplisse, et parmi les autres champs, il y a une sélection de fruits. L'utilisateur peut choisir une orange, une pomme ou rien.

Donc, la sortie est :

```
conditionalChooseFruit('Joe');// => Vous n'avez rien choisi, Joe.
```

```
conditionalChooseFruit('Joe', {notFruit: 'x'});// => Vous n'avez rien choisi, Joe.
```

```
conditionalChooseFruit('Joe', {fruit: 1});// => Vous avez choisi une pomme, Joe.
```

```
conditionalChooseFruit('Joe', {fruit: 11});// => Vous avez choisi un mauvais jardinier avec qui vous embrouiller, Joe.
```

Pour moi, cette méthode semble un peu désordonnée même avec l'aide de async/await et des conditions inversées. La logique métier est brouillée par les branches conditionnelles.

Et avec AsyncOptional, cela peut être réécrit de manière plus directe :

N'est-ce pas plus lisible ?

Donc, la bibliothèque [AsyncOptional](https://github.com/treble-snake/async-optional) pourrait vous aider à :

* écrire du code que vous pourriez trouver plus lisible, maintenable, propre et agréable ;
* éviter les `TypeErrors` liés à null, augmentant ainsi la stabilité de votre système ;
* travailler avec les Promesses et les fonctions asynchrones de la même manière propre (et cela fonctionne également avec les fonctions synchrones).

*Si vous avez aimé les exemples, n'hésitez pas à explorer le fichier [Readme](https://github.com/treble-snake/async-optional#about) dans le dépôt [GitHub](https://github.com/treble-snake/async-optional) ou même à consulter la documentation complète de l'[API](https://github.com/treble-snake/async-optional/blob/master/docs/APIDOC.md). Je me permets même de vous suggérer d'installer le [package via npm](https://www.npmjs.com/package/async-optional). :) J'apprécierais également tout retour.*

[**async-optional**](https://www.npmjs.com/package/async-optional)
[_Implémentation d'Optional avec support async_www.npmjs.com](https://www.npmjs.com/package/async-optional)