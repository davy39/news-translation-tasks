---
title: Comment formater une date avec JavaScript - Formatage de date en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-05-31T17:48:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-a-date-with-javascript-date-formatting-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/cover-template.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment formater une date avec JavaScript - Formatage de date en JS
seo_desc: 'Dates are a fundamental part of many JavaScript applications, whether it''s
  displaying the current date on a webpage or handling user input for scheduling events.

  But displaying dates in a clear and consistent format is crucial for a positive
  user exp...'
---

Les dates sont une partie fondamentale de nombreuses applications JavaScript, qu'il s'agisse d'afficher la date actuelle sur une page web ou de gérer les entrées utilisateur pour la planification d'événements.

Mais afficher les dates dans un format clair et cohérent est crucial pour une expérience utilisateur positive.

Par le passé, j'ai écrit deux articles sur le formatage des dates. Le premier expliquait uniquement [comment utiliser la méthode `toLocaleDateString()` pour formater les dates](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/), tandis que le second expliquait [le formatage personnalisé des dates avec les méthodes `getFullYear()`, `getMonth()` et `getDate()`](https://www.freecodecamp.org/news/javascript-date-format-how-to-format-a-date-in-js/).

Dans cet article, nous explorerons diverses techniques pour formater les dates en JavaScript, vous permettant de présenter les dates dans le format souhaité pour votre application.

## Comment utiliser l'objet Date de JavaScript

Avant de plonger dans le formatage des dates, familiarisons-nous avec l'objet `Date` de JavaScript. Il fournit des méthodes pour travailler efficacement avec les dates et les heures.

Pour créer une nouvelle instance de date, vous pouvez utiliser le constructeur `new Date()`.

Par exemple :

```js
const currentDate = new Date();
console.log(currentDate); // Wed May 31 2023 08:26:18 GMT+0100 (Heure normale d'Afrique de l'Ouest)
```

Le code ci-dessus affichera la date et l'heure actuelles dans le format par défaut. Cependant, ce format n'est pas adapté à tous les cas d'utilisation.

C'est pourquoi nous devons formater les dates afin de pouvoir extraire ce dont nous avons besoin de cet objet date.

En JavaScript, il n'existe pas de syntaxe directe qui vous fournit le format attendu, car le format de la date varie en fonction de la localisation, des circonstances, etc.

## Méthodes de base de formatage de date en JavaScript

JavaScript fournit quelques méthodes intégrées pour formater les dates de manière pratique. Examinons certaines de ces méthodes :

1. **toDateString()** : Cette méthode convertit la partie date d'un objet `Date` en une chaîne de caractères lisible.

Par exemple :

```js
const date = new Date();
console.log(date.toDateString());
```

Sortie : `Wed May 30 2023`

2. **toISOString()** : Cette méthode convertit un objet `Date` en une représentation de chaîne suivant le format ISO 8601.

Par exemple :

```js
const date = new Date();
console.log(date.toISOString());
```

Sortie : `2023-05-30T00:00:00.000Z`

3. **toLocaleDateString()** : Cette méthode retourne une chaîne représentant la partie date d'un objet `Date` en utilisant les conventions locales du système.

Par exemple :

```js
const date = new Date();
console.log(date.toLocaleDateString());
```

Sortie : `5/30/2023`. Ce format peut varier en fonction des paramètres régionaux du système. Pour plus d'explications sur le fonctionnement de cette méthode, [lisez cet article](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/).

## Formatage personnalisé des dates en JavaScript

Bien que les méthodes de formatage de base puissent être utiles dans certains scénarios, vous aurez souvent besoin de plus de contrôle sur le format de la date.

JavaScript offre plusieurs façons d'atteindre un formatage personnalisé des dates :

1. **Concatenation de chaînes** : Une approche consiste à concaténer manuellement les différents composants d'une date en utilisant la manipulation de chaînes.

Par exemple :

```js
const date = new Date();
const formattedDate = `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`;
console.log(formattedDate);
```

Sortie : `**30-5-2023**`.

Vous pouvez manipuler cela comme vous le souhaitez et trouver des moyens plus créatifs de représenter les dates. Vous pouvez lire cet article pour comprendre le formatage personnalisé des dates en détail et [cet article](https://www.freecodecamp.org/news/javascript-date-format-how-to-format-a-date-in-js/) sur [comment formater les dates avec des suffixes de nombres ordinaux (-st, -nd, -rd, -th) en JavaScript](https://www.freecodecamp.org/news/format-dates-with-ordinal-number-suffixes-javascript/).

2. **Intl.DateTimeFormat** : L'objet `Intl` de JavaScript offre des capacités de formatage puissantes grâce à l'objet `DateTimeFormat`. Il fournit un support de localisation et diverses options pour formater les dates et les heures.

Voici un exemple :

```js
const date = new Date();
const formatter = new Intl.DateTimeFormat('en-US', { dateStyle: 'short' });
const formattedDate = formatter.format(date);
console.log(formattedDate);
```

Sortie : `5/30/23`

En utilisant `Intl.DateTimeFormat`, vous pouvez spécifier la locale souhaitée et diverses options pour formater les dates précisément comme nécessaire. Il existe plus d'options que vous pouvez utiliser dans la [documentation officielle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat).

## Comment gérer les fuseaux horaires lors de la manipulation des dates

Lors de la manipulation des dates, il est essentiel de prendre en compte les fuseaux horaires, surtout lorsque l'on traite avec des applications mondiales ou des informations sensibles au temps.

JavaScript fournit des méthodes pour gérer efficacement les fuseaux horaires :

1. **Décalage de fuseau horaire** : La méthode `getTimezoneOffset()` de l'objet `Date` retourne la différence en minutes entre le fuseau horaire local et UTC. Vous pouvez utiliser ce décalage pour ajuster les dates pour des fuseaux horaires spécifiques.

2. **Affichage des fuseaux horaires** : Pour afficher les informations de fuseau horaire avec la date, vous pouvez utiliser la méthode `toLocaleString()` avec les options appropriées.

Par exemple :

```js
const date = new Date();
const formattedDate = date.toLocaleString('en-US', { timeZoneName: 'short' });
console.log(formattedDate);
```

Sortie : `5/30/2023, 12:00:00 AM PDT`.

## Modèles courants de formatage de date

Certains modèles de formatage de date sont couramment utilisés. Voici quelques exemples :

1. **Format de date spécifique** : Pour afficher une date dans un format spécifique, tel que `JJ/MM/AAAA`, vous pouvez utiliser `Intl.DateTimeFormat` avec les options appropriées.

Par exemple :

```js
const date = new Date();
const formatter = new Intl.DateTimeFormat('en-US', { day: '2-digit', month: '2-digit', year: 'numeric' });
const formattedDate = formatter.format(date);
console.log(formattedDate);
```

Sortie : `30/05/2023`.

2. **Format de l'heure** : Pour formater la partie heure d'une date, vous pouvez utiliser les options `hour`, `minute` et `second`.

Par exemple :

```js
const date = new Date();
const formatter = new Intl.DateTimeFormat('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
const formattedTime = formatter.format(date);
console.log(formattedTime);
```

Sortie : `12:00:00 AM`

## Comment gérer les entrées de date

En plus de formater les dates pour l'affichage, il est essentiel de gérer efficacement les entrées utilisateur pour les dates. Voici quelques considérations :

1. **Analyse des entrées utilisateur** : Utilisez la méthode `Date.parse()` ou des bibliothèques externes comme Moment.js ou Luxon pour analyser les dates fournies par l'utilisateur en objets `Date` valides.

2. **Validation des entrées utilisateur** : Mettez en place des mécanismes de validation pour vous assurer que l'entrée de l'utilisateur respecte le format de date attendu. Les expressions régulières ou les bibliothèques externes peuvent aider à cela.

## Conclusion

Le formatage des dates en JavaScript est une compétence essentielle lors de la création d'applications web. En utilisant les méthodes de formatage de date intégrées, les techniques de formatage personnalisé et les bibliothèques externes, vous pouvez vous assurer que les dates sont présentées clairement et avec précision.

Expérimentez avec différentes approches et restez attentif aux fuseaux horaires pour une expérience utilisateur fluide avec le formatage des dates en JavaScript.

Pour approfondir vos connaissances sur le formatage des dates, consultez ces ressources :

* [Format de date JavaScript - Comment formater une date en JS](https://www.freecodecamp.org/news/javascript-date-format-how-to-format-a-date-in-js/)

* [Comment formater les dates en JavaScript avec une ligne de code](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/)

* [Comment formater les dates avec des suffixes de nombres ordinaux (-st, -nd, -rd, -th) en JavaScript](https://www.freecodecamp.org/news/format-dates-with-ordinal-number-suffixes-javascript/)

Embarquez pour un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.