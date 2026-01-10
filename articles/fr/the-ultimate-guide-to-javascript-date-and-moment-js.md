---
title: Le guide ultime sur les dates en JavaScript et Moment.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-02T18:01:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-javascript-date-and-moment-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ee7740569d1a4ca3fce.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Le guide ultime sur les dates en JavaScript et Moment.js
seo_desc: 'Welcome to our ultimate guide on the JavaScript Date object and Moment.js.
  This tutorial will teach you everything you need to know about working with dates
  and times in your projects.

  How to Create a Date Object

  Get the current date and time

  const n...'
---

Bienvenue dans notre guide ultime sur l'objet `Date` de JavaScript et Moment.js. Ce tutoriel vous apprendra tout ce que vous devez savoir sur la manipulation des dates et des heures dans vos projets.

## Comment créer un objet `Date`

### Obtenir la date et l'heure actuelles

```js
const now = new Date();

// Mon Aug 10 2019 12:58:21 GMT-0400 (Eastern Daylight Time)
```

### Obtenir une date et une heure avec des valeurs individuelles

```js
const specifiedDate = new Date(2019, 4, 29, 15, 0, 0, 0);

// Wed May 29 2019 15:00:00 GMT-0400 (Eastern Daylight Time)
```

La syntaxe est `Date(année, mois, jour, heure, minute, seconde, milliseconde)`. 

Notez que les mois sont indexés à partir de zéro, commençant par janvier à 0 et se terminant par décembre à 11.

### Obtenir une date et une heure à partir d'un timestamp

```js
const unixEpoch = new Date(0);
```

Cela représente le temps du jeudi 1er janvier 1970 (UTC), ou l'heure de l'époque Unix. L'époque Unix est importante car c'est ce que JavaScript, Python, PHP et d'autres langages et systèmes utilisent en interne pour calculer l'heure actuelle.

`new Date(ms)` retourne la date de l'époque plus le nombre de millisecondes que vous passez. Dans une journée, il y a 86 400 000 millisecondes, donc :

```js
const dayAfterEpoch = new Date(86400000);
```

retournera vendredi 2 janvier 1970 (UTC).

### Obtenir une date et une heure à partir d'une chaîne de caractères

```js
const stringDate = new Date('May 29, 2019 15:00:00');

// Wed May 29 2019 15:00:00 GMT-0400 (Eastern Daylight Time)
```

Obtenir la date de cette manière est très flexible. Tous les exemples ci-dessous retournent des objets `Date` valides :

```js
new Date('2019-06') // 1er juin 2019 00:00:00
new Date('2019-06-16') // 16 juin 2019
new Date('2019') // 1er janvier 2019 00:00:00
new Date('JUNE 16, 2019')
new Date('6/23/2019')
```

Vous pouvez également utiliser la méthode `Date.parse()` pour retourner le nombre de millisecondes depuis l'époque (1er janvier 1970) :

```js
Date.parse('1970-01-02') // 86400000
Date.parse('6/16/2019') // 1560610800000
```

### Définir un fuseau horaire

Lors du passage d'une chaîne de date sans définir de fuseau horaire, JavaScript suppose que la date/heure est en UTC avant de la convertir dans le fuseau horaire de votre navigateur :

```js
const exactBirthdate = new Date('6/13/2018 06:27:00');

console.log(exactBirthdate) // Wed Jun 13 2018 06:27:00 GMT+0900 (Korean Standard Time)
```

Cela peut entraîner des erreurs où la date retournée est décalée de plusieurs heures. Pour éviter cela, passez un fuseau horaire avec la chaîne :

```js
const exactBirthdate = new Date('6/13/2018 06:27:00 GMT-1000');

console.log(exactBirthdate) // Thu Jun 14 2018 01:27:00 GMT+0900 (Korean Standard Time)

/*
Ces formats fonctionnent également :

new Date('6/13/2018 06:27:00 GMT-10:00');
new Date('6/13/2018 06:27:00 -1000');
new Date('6/13/2018 06:27:00 -10:00');
*/
```

Vous pouvez également passer certains codes de fuseau horaire, mais pas tous :

```js
const exactBirthdate = new Date('6/13/2018 06:27:00 PDT');

console.log(exactBirthdate) // Thu Jun 14 2018 01:27:00 GMT+0900 (Korean Standard Time)
```

## Méthodes de l'objet `Date`

Souvent, vous n'aurez pas besoin de la date entière, mais seulement d'une partie comme le jour, la semaine ou le mois. Heureusement, il existe un certain nombre de méthodes pour faire exactement cela :

```js
const birthday = new Date('6/13/2018 06:27:39');

birthday.getMonth() // 5 (0 est janvier)
birthday.getDate() // 13
birthday.getDay() // 3 (0 est dimanche)
birthday.getFullYear() // 2018
birthday.getTime() // 1528838859000 (millisecondes depuis l'époque Unix)
birthday.getHours() // 6
birthday.getMinutes() // 27
birthday.getSeconds() // 39
birthday.getTimezoneOffset() // -540 (décalage horaire en minutes basé sur l'emplacement de votre navigateur)
```

## Facilitez le travail avec les dates grâce à Moment.js

Obtenir des dates et des heures correctes n'est pas une mince affaire. Chaque pays semble avoir une manière différente de formater les dates, et tenir compte des différents fuseaux horaires et de l'heure d'été prend, eh bien, beaucoup de temps. C'est là que Moment.js brille - il facilite l'analyse, le formatage et l'affichage des dates.

Pour commencer à utiliser Moment.js, installez-le via un gestionnaire de paquets comme `npm`, ou ajoutez-le à votre site via un CDN. Consultez la [documentation de Moment.js](https://momentjs.com/docs/) pour plus de détails.

### Obtenir la date et l'heure actuelles avec Moment.js

```js
const now = moment();
```

Cela retourne un objet avec la date et l'heure basées sur l'emplacement de votre navigateur, ainsi que d'autres informations de localisation. C'est similaire à `new Date()` natif de JavaScript.

### Obtenir une date et une heure à partir d'un timestamp avec Moment.js

Similaire à `new Date(ms)`, vous pouvez passer le nombre de millisecondes depuis l'époque à `moment()` :

```js
const dayAfterEpoch = moment(86400000);
```

Si vous souhaitez obtenir une date en utilisant un timestamp Unix en secondes, vous pouvez utiliser la méthode `unix()` :

```js
const dayAfterEpoch = moment.unix(86400);
```

### Obtenir une date et une heure à partir d'une chaîne avec Moment.js

Analyser une date à partir d'une chaîne avec Moment.js est facile, et la bibliothèque accepte les chaînes au format ISO 8601 ou RFC 2822 Date Time, ainsi que toute chaîne acceptée par l'objet `Date` de JavaScript.

Les chaînes ISO 8601 sont recommandées car il s'agit d'un format largement accepté. Voici quelques exemples :

```js
moment('2019-04-21');
moment('2019-04-21T05:30');
moment('2019-04-21 05:30');

moment('20190421');
moment('20190421T0530');
```

### Définir un fuseau horaire avec Moment.js

Jusqu'à présent, nous avons utilisé Moment.js en mode _local_, ce qui signifie que toute entrée est supposée être une date ou une heure locale. Cela est similaire au fonctionnement de l'objet `Date` natif de JavaScript :

```js
const exactBirthMoment = moment('2018-06-13 06:27:00');

console.log(exactBirthMoment) // Wed Jun 13 2018 06:27:00 GMT+0900 (Korean Standard Time)
```

Cependant, pour définir un fuseau horaire, vous devez d'abord obtenir l'objet Moment en mode _UTC_ :

```js
const exactBirthMoment = moment.utc('2018-06-13 06:27:00');

console.log(exactBirthMoment) // Wed Jun 13 2018 15:27:00 GMT+0900 (Korean Standard Time)
```

Ensuite, vous pouvez ajuster la différence de fuseaux horaires avec la méthode `utcOffset()` :

```js
const exactBirthMoment = moment.utc('2018-06-13 06:27:00').utcOffset('+10:00');

console.log(exactBirthMoment) // Wed Jun 13 2018 06:27:00 GMT+0900 (Korean Standard Time)
```

Vous pouvez également définir le décalage UTC sous forme de nombre ou de chaîne :

```js
moment.utc().utcOffset(10) // Nombre d'heures de décalage
moment.utc().utcOffset(600) // Nombre de minutes de décalage
moment.utc().utcOffset('+10:00') // Nombre d'heures de décalage sous forme de chaîne
```

Pour utiliser des fuseaux horaires nommés (`America/Los_Angeles`) ou des codes de fuseau horaire (`PDT`) avec des objets Moment, consultez la bibliothèque [Moment Timezone](https://momentjs.com/timezone/).

### Formater la date et l'heure avec Moment.js

L'un des principaux atouts de Moment.js par rapport aux objets `Date` natifs de JavaScript est la facilité avec laquelle vous pouvez formater la date et l'heure de sortie. Il suffit d'enchaîner la méthode `format()` à un objet de date Moment et de lui passer une chaîne de format en tant que paramètre :

```js
moment().format('MM-DD-YY'); // "08-13-19"
moment().format('MM-DD-YYYY'); // "08-13-2019"
moment().format('MM/DD/YYYY'); // "08/13/2019"
moment().format('MMM Do, YYYY') // "Aug 13th, 2019"
moment().format('ddd MMMM Do, YYYY HH:mm:ss') // "Tues August 13th, 2019 19:29:20"
moment().format('dddd, MMMM Do, YYYY -- hh:mm:ss A') // "Tuesday, August 13th, 2019 -- 07:31:02 PM"
```

Voici un tableau avec quelques jetons de formatage courants :

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Lato, sans-serif;font-size:2.2rem;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Lato, sans-serif;font-size:2.2rem;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-v1p6{font-size:2.2rem;font-family:Lato !important;;text-align:right;vertical-align:top}
.tg .tg-nh17{font-size:2.2rem;font-family:Lato !important;;text-align:left;vertical-align:top}
.tg .tg-htb4{font-weight:bold;font-size:2.2rem;font-family:Lato !important;;background-color:#efefef;text-align:center;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-htb4">Entrée</th>
    <th class="tg-htb4">Sortie</th>
    <th class="tg-htb4">Description</th>
  </tr>
  <tr>
    <td class="tg-v1p6">YYYY</td>
    <td class="tg-nh17">2019</td>
    <td class="tg-nh17">Année sur 4 chiffres</td>
  </tr>
  <tr>
    <td class="tg-v1p6">YY</td>
    <td class="tg-nh17">19</td>
    <td class="tg-nh17">Année sur 2 chiffres</td>
  </tr>
  <tr>
    <td class="tg-v1p6">MMMM</td>
    <td class="tg-nh17">August</td>
    <td class="tg-nh17">Nom complet du mois</td>
  </tr>
  <tr>
    <td class="tg-v1p6">MMM</td>
    <td class="tg-nh17">Aug</td>
    <td class="tg-nh17">Nom abrégé du mois</td>
  </tr>
  <tr>
    <td class="tg-v1p6">MM</td>
    <td class="tg-nh17">08</td>
    <td class="tg-nh17">Mois sur 2 chiffres</td>
  </tr>
  <tr>
    <td class="tg-v1p6">M</td>
    <td class="tg-nh17">8</td>
    <td class="tg-nh17">Mois sur 1 chiffre</td>
  </tr>
  <tr>
    <td class="tg-v1p6">DDD</td>
    <td class="tg-nh17">225</td>
    <td class="tg-nh17">Jour de l'année</td>
  </tr>
  <tr>
    <td class="tg-v1p6">DD</td>
    <td class="tg-nh17">13</td>
    <td class="tg-nh17">Jour du mois</td>
  </tr>
  <tr>
    <td class="tg-v1p6">Do</td>
    <td class="tg-nh17">13th</td>
    <td class="tg-nh17">Jour du mois avec ordinal</td>
  </tr>
  <tr>
    <td class="tg-v1p6">dddd</td>
    <td class="tg-nh17">Wednesday</td>
    <td class="tg-nh17">Nom complet du jour</td>
  </tr>
  <tr>
    <td class="tg-v1p6">ddd</td>
    <td class="tg-nh17">Wed</td>
    <td class="tg-nh17">Nom abrégé du jour</td>
  </tr>
  <tr>
    <td class="tg-v1p6">HH</td>
    <td class="tg-nh17">17</td>
    <td class="tg-nh17">Heures en format 24 heures</td>
  </tr>
  <tr>
    <td class="tg-v1p6">hh</td>
    <td class="tg-nh17">05</td>
    <td class="tg-nh17">Heures en format 12 heures</td>
  </tr>
  <tr>
    <td class="tg-v1p6">mm</td>
    <td class="tg-nh17">32</td>
    <td class="tg-nh17">Minutes</td>
  </tr>
  <tr>
    <td class="tg-v1p6">ss</td>
    <td class="tg-nh17">19</td>
    <td class="tg-nh17">Secondes</td>
  </tr>
  <tr>
    <td class="tg-v1p6">a</td>
    <td class="tg-nh17">am / pm</td>
    <td class="tg-nh17">Ante ou post meridiem</td>
  </tr>
  <tr>
    <td class="tg-v1p6">A</td>
    <td class="tg-nh17">AM / PM</td>
    <td class="tg-nh17">Ante ou post meridiem en majuscules</td>
  </tr>
  <tr>
    <td class="tg-v1p6">ZZ</td>
    <td class="tg-nh17">+0900</td>
    <td class="tg-nh17">Décalage horaire par rapport à l'UTC</td>
  </tr>
  <tr>
    <td class="tg-v1p6">X</td>
    <td class="tg-nh17">1410715640.579</td>
    <td class="tg-nh17">Timestamp Unix en secondes</td>
  </tr>
  <tr>
    <td class="tg-v1p6">XX</td>
    <td class="tg-nh17">1410715640579</td>
    <td class="tg-nh17">Timestamp Unix en millisecondes</td>
  </tr>
</table>

Consultez la [documentation de Moment.js](https://momentjs.com/docs/) pour plus de jetons de formatage.

Travailler avec les objets `Date` de JavaScript et Moment.js n'a pas à être chronophage. Maintenant, vous devriez en savoir assez pour commencer avec les deux.