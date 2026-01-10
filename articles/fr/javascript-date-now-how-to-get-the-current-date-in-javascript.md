---
title: JavaScript Date Now – Comment obtenir la date actuelle en JavaScript
date: '2020-06-15T05:35:17.000Z'
author: freeCodeCamp
authorURL: https://www.freecodecamp.org/news/author/vijit/
originalURL: https://freecodecamp.org/news/javascript-date-now-how-to-get-the-current-date-in-javascript
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a4b740569d1a4ca24bd.jpg
tags:
- name: JavaScript
  slug: javascript
seo_desc: "By Vijit Ail\nMany applications you build will have some sort of a date\
  \ component, whether it's the creation date of a resource, or the timestamp of an\
  \ activity. \nDealing with date and timestamp formatting can be exhausting. In this\
  \ guide, you will le..."
---


De nombreuses applications que vous développez comporteront un composant de date, qu'il s'agisse de la date de création d'une ressource ou de l'horodatage (*timestamp*) d'une activité.

<!-- more -->

Gérer le formatage des dates et des horodatages peut être épuisant. Dans ce guide, vous apprendrez comment obtenir la date actuelle sous différents formats en JavaScript.

## L'objet Date de JavaScript

JavaScript possède un objet `Date` intégré qui stocke la date et l'heure et fournit des méthodes pour les manipuler.

Pour créer une nouvelle instance de l'objet `Date`, utilisez le mot-clé `new` :

```js
const date = new Date();
```

L'objet `Date` contient un `Number` qui représente les millisecondes écoulées depuis l'Époque (*Epoch*), c'est-à-dire le 1er janvier 1970.

Vous pouvez passer une chaîne de caractères de date au constructeur `Date` pour créer un objet pour la date spécifiée :

```js
const date = new Date('Jul 12 2011');
```

Pour obtenir l'année en cours, utilisez la méthode d'instance `getFullYear()` de l'objet `Date`. La méthode `getFullYear()` renvoie l'année de la date spécifiée dans le constructeur `Date` :

```js
const currentYear = date.getFullYear();
console.log(currentYear); //2020
```

De même, il existe des méthodes pour obtenir le jour actuel du mois et le mois en cours :

```js
const today = date.getDate();
const currentMonth = date.getMonth() + 1; 
```

La méthode `getDate()` renvoie le jour actuel du mois (1-31).

La méthode `getMonth()` renvoie le mois de la date spécifiée. Un point à noter concernant la méthode `getMonth()` est qu'elle renvoie des valeurs indexées à partir de 0 (0-11) où 0 correspond à janvier et 11 à décembre. D'où l'ajout de 1 pour normaliser la valeur du mois.

## Date now

`now()` est une méthode statique de l'objet `Date`. Elle renvoie la valeur en millisecondes représentant le temps écoulé depuis l'Époque. Vous pouvez passer les millisecondes renvoyées par la méthode `now()` dans le constructeur `Date` pour instancier un nouvel objet `Date` :

```js
const timeElapsed = Date.now();
const today = new Date(timeElapsed);
```

## Formater la date

Vous pouvez formater la date dans plusieurs formats (GMT, ISO, etc.) en utilisant les méthodes de l'objet `Date`.

La méthode `toDateString()` renvoie la date dans un format lisible par l'homme :

```js
today.toDateString(); // "Sun Jun 14 2020"
```

La méthode `toISOString()` renvoie la date suivant le format étendu ISO 8601 :

```js
today.toISOString(); // "2020-06-13T18:30:00.000Z"
```

La méthode `toUTCString()` renvoie la date au format du fuseau horaire UTC :

```js
today.toUTCString(); // "Sat, 13 Jun 2020 18:30:00 GMT"
```

La méthode `toLocaleDateString()` renvoie la date dans un format sensible à la localisation :

```js
today.toLocaleDateString(); // "6/14/2020"
```

Vous trouverez la référence complète des méthodes `Date` dans la [documentation MDN][1].

## Fonction de formatage de date personnalisée

En dehors des formats mentionnés dans la section précédente, votre application peut nécessiter un format de données différent. Il pourrait s'agir du format `yy/dd/mm` ou `yyyy-dd-mm`, ou quelque chose de similaire.

Pour résoudre ce problème, il est préférable de créer une fonction réutilisable afin qu'elle puisse être utilisée dans plusieurs projets.

Dans cette section, créons donc une fonction utilitaire qui renverra la date dans le format spécifié dans l'argument de la fonction :

```js
const today = new Date();

function formatDate(date, format) {
	//
}

formatDate(today, 'mm/dd/yy');
```

Vous devez remplacer les chaînes "mm", "dd", "yy" par les valeurs respectives du mois, du jour et de l'année provenant de la chaîne de format passée en argument.

Pour ce faire, vous pouvez utiliser la méthode `replace()` comme illustré ci-dessous :

```js
format.replace('mm', date.getMonth() + 1);
```

Mais cela entraînera un chaînage de méthodes important et rendra la maintenance difficile à mesure que vous essaierez de rendre la fonction plus flexible :

```js
format.replace('mm', date.getMonth() + 1)
    .replace('yy', date.getFullYear())
	.replace('dd', date.getDate());
```

Au lieu de chaîner les méthodes, vous pouvez utiliser une expression régulière avec la méthode `replace()`.

Créez d'abord un objet qui représentera une paire clé-valeur de la sous-chaîne et de sa valeur respective :

```js
const formatMap = {
	mm: date.getMonth() + 1,
    dd: date.getDate(),
    yy: date.getFullYear().toString().slice(-2),
    yyyy: date.getFullYear()
};
```

Ensuite, utilisez une expression régulière pour faire correspondre et remplacer les chaînes :

```js
formattedDate = format.replace(/mm|dd|yy|yyy/gi, matched => map[matched]);
```

La fonction complète ressemble à ceci :

```js
function formatDate(date, format) {
    const map = {
        mm: date.getMonth() + 1,
        dd: date.getDate(),
        yy: date.getFullYear().toString().slice(-2),
        yyyy: date.getFullYear()
    }

    return format.replace(/mm|dd|yy|yyy/gi, matched => map[matched])
}
```

Vous pouvez également ajouter la possibilité de formater des horodatages dans la fonction.

## Conclusion

J'espère que vous avez maintenant une meilleure compréhension de l'objet `Date` en JavaScript. Vous pouvez également utiliser d'autres bibliothèques tierces comme `datesj` et `moment` pour gérer les dates dans votre application.

D'ici la prochaine fois, restez prudents et continuez à coder avec passion.

[1]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date