---
title: Format de Date en JavaScript – Comment Formater une Date en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-08-24T15:25:15.000Z'
originalURL: https://freecodecamp.org/news/javascript-date-format-how-to-format-a-date-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-template--2-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Format de Date en JavaScript – Comment Formater une Date en JS
seo_desc: 'JavaScript is one of the three fundamental web technologies you''ll use
  when developing websites or web applications.

  When creating these web pages, you will, at some point, likely need to use dates
  for some reason – such as displaying when something ...'
---

JavaScript est l'une des trois technologies web fondamentales que vous utiliserez lors du développement de sites web ou d'applications web.

Lors de la création de ces pages web, vous aurez probablement besoin d'utiliser des dates à un moment donné – par exemple pour afficher quand quelque chose a été téléchargé, stocké, etc.

Dans cet article, vous apprendrez comment formater des dates en JavaScript et verrez comment vous pouvez le faire avec une bibliothèque JavaScript populaire connue sous le nom de [moment.js](https://momentjs.com/).

## Comment Obtenir des Dates en JavaScript

En JavaScript, vous utilisez soit le constructeur `new Date()` ou `Date()` pour obtenir vos dates (soit la date actuelle ou une date spécifique).

Le constructeur `new Date()` retourne un nouvel objet `Date`, tandis que le constructeur `Date()` retourne une représentation sous forme de chaîne de la date et de l'heure actuelles.

```js
let stringDate = Date();
console.log(stringDate); // "Tue Aug 23 2022 14:47:12 GMT-0700 (Pacific Daylight Time)"

let objectDate = new Date();
console.log(objectDate); // Tue Aug 23 2022 14:47:12 GMT-0700 (Pacific Daylight Time)
```

Ces dates au format complet comprennent le jour, le mois, l'année, les minutes, l'heure et d'autres informations dont vous n'avez pas toujours besoin.

Votre principale préoccupation est de voir comment vous pouvez formater ces valeurs de date pour retourner des dates dans des formats lisibles, que vous pouvez intégrer sur votre page web pour que tout le monde comprenne.

## Comment Formater des Dates en JavaScript

Le formatage des dates dépend de vous et de vos besoins. Dans certains pays, le mois vient avant le jour, puis l'année (06/22/2022). Dans d'autres, le jour vient avant le mois, puis l'année (22/06/2022), et bien plus encore.

Quelle que soit la forme, vous voulez décomposer la valeur de l'objet date et obtenir les informations nécessaires que vous souhaitez pour votre page web.

Cela est possible avec les méthodes de date JavaScript. Il existe de nombreuses méthodes, mais puisque vous ne vous intéressez qu'aux dates dans cet article, vous n'aurez besoin que de trois d'entre elles :

* `getFullYear()` – Vous utiliserez cette méthode pour obtenir l'année sous forme de nombre à quatre chiffres (yyyy). Par exemple, 2022.

* `getMonth()` – Vous utiliserez cette méthode pour obtenir le mois sous forme de nombre entre 0-11, chaque nombre représentant les mois de janvier à décembre. Par exemple, `2` sera l'index pour mars puisque c'est un indexage basé sur zéro (ce qui signifie qu'il commence à partir de `0`).

* `getDate()` – Vous utiliserez cette méthode pour obtenir le jour sous forme de nombre entre 1-31 (ceci n'est pas un index, mais la valeur exacte du jour, donc il commence à partir de 1 et non de 0).

**Note :** Ces méthodes ne peuvent être appliquées ou ne fonctionneront qu'avec le constructeur `new Date()`, qui retourne un objet date.

```js
let objectDate = new Date();


let day = objectDate.getDate();
console.log(day); // 23

let month = objectDate.getMonth();
console.log(month + 1); // 8

let year = objectDate.getFullYear();
console.log(year); // 2022
```

Vous remarquerez que `1` est ajouté à la valeur `month` ci-dessus. Cela est dû au fait que le mois est indexé à `0`. La valeur commence à partir de `0`. Cela signifie que `7` signifiera août au lieu de `8`.

À ce stade, vous avez pu extraire toutes les valeurs de date de l'objet date. Vous pouvez maintenant les organiser dans le format que vous souhaitez :

```js
let format1 = month + "/" + day + "/" + year;
console.log(format1); // 7/23/2022

let format2 = day + "/" + month + "/" + year;
console.log(format2); // 23/7/2022

let format3 = month + "-" + day + "-" + year;
console.log(format3); // 7-23-2022

let format4 = day + "-" + month + "-" + year;
console.log(format4); // 23-7-2022
```

Dans l'exemple ci-dessus, vous avez concaténé les valeurs en utilisant l'opérateur plus. Vous pouvez également utiliser des littéraux de gabarit pour concaténer :

```js
let format1 = `${month}/${day}/${year}`;
console.log(format1); // 7/23/2022

let format2 = `${day}/${month}/${year}`;
console.log(format2); // 23/7/2022

let format3 = `${month}-${day}-${year}`;
console.log(format3); // 7-23-2022

let format4 = `${day}-${month}-${year}`;
console.log(format4); // 23-7-2022
```

Maintenant, vous avez vu les différentes façons dont vous pourriez vouloir formater votre date.

Un autre scénario peut être si vous voulez que la valeur du mois et du jour soit précédée par 0 si c'est une valeur numérique unique (de 1-9). Pour ce faire, vous devrez ajouter une condition pour gérer cela avant de formater vos dates :

```js
if (day < 10) {
    day = '0' + day;
}

if (month < 10) {
    month = `0${month}`;
}

let format1 = `${month}/${day}/${year}`;
console.log(format1); // 07/23/2022
```

Intéressé par d'autres façons de formater des dates en JavaScript ? Consultez mon article sur "[**Comment Formater des Dates en JavaScript avec une Ligne de Code**](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/)".

## Comment Formater des Dates en JavaScript avec Moment.js

[Moment.js](https://momentjs.com/) est une bibliothèque JavaScript de date et d'heure que vous pouvez utiliser pour formater rapidement vos dates sans gérer la logique avec autant de lignes de code.

Pour utiliser cette bibliothèque, vous devez installer le package dans votre projet en utilisant l'une de vos [options préférées dans la documentation](https://momentjs.com/).

Pour ce guide, vous ne vous intéressez qu'à la façon dont vous pouvez formater des dates avec Moment.js :

```js
let date = moment().format();

console.log(date); // 2022-08-23T16:50:22-07:00
```

Pour formater cette valeur de date/heure, tout ce que vous avez à faire est d'entrer votre format préféré, et il retournera la date formatée comme vu ci-dessous :

```js
let dateFormat1 = moment().format('D-MM-YYYY');
console.log(dateFormat1); // 23-08-2022

let dateFormat2 = moment().format('D/MM/YYYY');
console.log(dateFormat2); // 23/08/2022

let dateFormat3 = moment().format('MM-D-YYYY');
console.log(dateFormat3); // 08-23-2022

let dateFormat4 = moment().format('MM/D/YYYY');
console.log(dateFormat4); // 08/23/2022
```

## Conclusion

Cet article vous a appris comment formater des dates en JavaScript, soit à partir de zéro soit avec la bibliothèque moment.js.

Soyez prudent lorsque vous utilisez une bibliothèque pour de petits projets, car les bibliothèques augmentent la taille de votre projet. Cela est dû au fait que ces bibliothèques sont conçues pour gérer beaucoup plus d'opérations. Mais pour utiliser une opération minimale, vous devez toujours installer la bibliothèque entière.

Il est toujours recommandé d'effectuer des opérations simples comme celle-ci à partir de zéro. C'est-à-dire, sauf si vous êtes obligé d'utiliser la bibliothèque, ou si la bibliothèque a déjà été installée, ou si vous travaillez sur un projet à grande échelle qui nécessite un certain formatage complexe.

Amusez-vous bien en codant !

Embarquez dans un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.