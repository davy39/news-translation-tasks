---
title: JavaScript Timestamp – Comment utiliser getTime() pour générer des timestamps
  en JS
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-19T17:58:01.000Z'
originalURL: https://freecodecamp.org/news/javascript-timestamp-how-to-use-gettime-to-generate-timestamps-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/aron-visuals-BXOXnQ26B7o-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Timestamp – Comment utiliser getTime() pour générer des timestamps
  en JS
seo_desc: 'In JavaScript, timestamps are usually associated with Unix time. And there
  are different methods for generating such timestamps.

  When we make use of the different JavaScript methods for generating timestamps,
  they return the number of milliseconds th...'
---

En JavaScript, les timestamps sont généralement associés à l'[Unix time](https://en.wikipedia.org/wiki/Unix_time). Et il existe différentes méthodes pour générer de tels timestamps.

Lorsque nous utilisons les différentes méthodes JavaScript pour générer des timestamps, elles retournent le nombre de millisecondes écoulées depuis le 1er janvier 1970 UTC (l'Unix time).

Dans cet article, vous apprendrez à utiliser les méthodes suivantes pour générer des timestamps Unix en JavaScript :

* La méthode `getTime()`.
* La méthode `Date.now()`.
* La méthode `valueOf()`.

## Comment utiliser `getTime()` pour générer des timestamps en JS

```javascript
var timestamp = new Date().getTime();

console.log(timestamp)
// 1660926192826
```

Dans l'exemple ci-dessus, nous avons créé un objet `new Date()` et l'avons stocké dans une variable `timestamp`.

Nous avons également attaché la méthode `getTime()` à l'objet `new Date()` en utilisant la notation par point : `new Date().getTime()`. Cela a retourné l'Unix time à ce moment-là en millisecondes : 1660926192826.

Pour obtenir le timestamp en secondes, vous divisez le timestamp actuel par 1000. C'est-à-dire :

```javascript
var timestamp = new Date().getTime();

console.log(Math.floor(timestamp / 1000))

```

## Comment utiliser `Date.now()` pour générer des timestamps en JS

```javascript
var timestamp = Date.now();

console.log(timestamp)
// 1660926758875
```

Dans l'exemple ci-dessus, nous avons obtenu le timestamp Unix à ce moment précis en utilisant la méthode `Date.now()`.

Les timestamps que vous voyez dans ces exemples seront différents des vôtres. Cela est dû au fait que vous obtiendrez le timestamp du temps écoulé depuis le 1er janvier 1970 UTC jusqu'à votre heure actuelle.

## Comment utiliser `valueOf()` pour générer des timestamps en JS

```javascript
var timestamp = new Date().valueOf();

console.log(timestamp)
// 1660928777955
```

Tout comme la méthode `getTime()`, nous devons attacher la méthode `valueOf()` à un objet `new Date()` afin de générer un timestamp Unix.

L'objet `new Date()`, sans `getTime()` ou `valueOf()`, retourne les informations sur votre heure actuelle.

## Résumé

Dans cet article, nous avons parlé des timestamps en JavaScript. Ils sont généralement associés à l'Unix time.

Nous avons vu trois méthodes différentes qui peuvent être utilisées pour générer des timestamps en JavaScript avec des exemples de code.

Bon codage !