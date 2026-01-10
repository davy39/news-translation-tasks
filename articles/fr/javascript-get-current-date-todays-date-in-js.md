---
title: JavaScript Obtenir la Date Actuelle – La Date d'Aujourd'hui en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-17T15:45:01.000Z'
originalURL: https://freecodecamp.org/news/javascript-get-current-date-todays-date-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template--2-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Obtenir la Date Actuelle – La Date d'Aujourd'hui en JS
seo_desc: 'When you''re developing web applications, you might need to include the
  current date on which a particular operation is performed.

  For example, when submitting data via a form, you may want to include the date that
  data was created or when the form wa...'
---

Lorsque vous développez des applications web, vous pourriez avoir besoin d'inclure la date actuelle à laquelle une opération particulière est effectuée.

Par exemple, lors de la soumission de données via un formulaire, vous pourriez vouloir inclure la date à laquelle les données ont été créées ou lorsque le formulaire a été soumis.

Dans cet article, nous allons apprendre comment obtenir facilement la date actuelle (la date d'aujourd'hui) avec JavaScript à partir de zéro. Nous apprendrons également comment faire cela avec une bibliothèque externe comme Moment.js, une bibliothèque de dates JavaScript populaire.

Juste une note – en général, il n'est pas recommandé d'utiliser une bibliothèque externe pour une opération comme celle-ci. Mais si vous avez déjà une bibliothèque installée sur votre projet ou si vous l'utilisez pour d'autres opérations dans votre application, vous pouvez l'utiliser.

### Voici un Scrim Interactif sur Comment Obtenir la Date Actuelle en JavaScript

<iframe src="https://scrimba.com/scrim/coc634945941f26de68c42292?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## Comment Obtenir la Date Actuelle en JavaScript

En JavaScript, nous pouvons facilement obtenir la date ou l'heure actuelle en utilisant l'objet `new Date()`. Par défaut, il utilise le fuseau horaire de notre navigateur et affiche la date sous forme de chaîne de texte complète, telle que "Fri Jun 17 2022 10:54:59 GMT+0100 (British Summer Time)" qui contient la date actuelle, l'heure et le fuseau horaire.

```js
const date = new Date();
console.log(date); // Fri Jun 17 2022 11:27:28 GMT+0100 (British Summer Time)
```

Voyons comment nous pouvons extraire uniquement la date de cette longue chaîne. Nous allons la rendre plus lisible et compréhensible pour les utilisateurs en utilisant certaines méthodes JavaScript qui opèrent sur un objet de date.

### Comment Utiliser les Méthodes de Date JavaScript

L'objet date prend en charge de nombreuses méthodes de date, mais pour cet article, nous n'avons besoin que de la date actuelle et n'utiliserons que trois méthodes :

* `getFullYear()` – nous utiliserons cette méthode pour obtenir l'année sous forme de nombre à quatre chiffres (yyyy), par exemple 2022.
  
* `getMonth()` – Cela obtient le mois sous forme de nombre (0-11), par exemple 2 pour mars puisque c'est un index basé sur zéro (ce qui signifie qu'il commence à 0).
  
* `getDate()` – obtient le jour sous forme de nombre (1-31).
  

Mettons maintenant tout cela ensemble en fonction du format dans lequel nous voulons que notre date apparaisse :

```js
const date = new Date();

let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();

// Cet arrangement peut être modifié en fonction de la manière dont nous voulons que le format de la date apparaisse.
let currentDate = `${day}-${month}-${year}`;
console.log(currentDate); // "17-6-2022"
```

**Note :** Nous avons ajouté un à la valeur de `date.getMonth()` puisque c'est un index basé sur `0`. Supposons que nous ne voulons pas utiliser de tiret(-) entre nos valeurs de date, tout ce que nous avons à faire est de remplacer le tiret par ce que nous préférons.

### Comment Utiliser la Méthode toJSON()

Nous venons de voir comment obtenir la date actuelle en utilisant les méthodes de date. Voyons maintenant comment utiliser la méthode `toJSON()`, qui retourne notre date au format `yyyy-mm-dd` en plus du format de l'heure, `hh:mm:ss.ms`.

```js
let date = new Date().toJSON();
console.log(date); // 2022-06-17T11:06:50.369Z
```

Puisque nous voulons uniquement la date actuelle, nous pouvons utiliser la méthode `slice()` de cette manière pour obtenir les 10 premiers caractères :

```js
let currentDate = new Date().toJSON().slice(0, 10);
console.log(currentDate); // "2022-06-17"
```

### Comment Utiliser toLocaleDateString()

Il s'agit d'une autre méthode simple qui retourne l'objet date sous forme de chaîne en utilisant les conventions locales. Par exemple, le format de la date diffère entre les langues, et cette méthode accepte un argument pour corriger cela.

Commençons par passer un argument :

```js
let date = new Date().toLocaleDateString();
console.log(date); // 6/17/2022
```

Supposons que nous voulons l'heure en Allemagne :

```js
let date = new Date().toLocaleDateString("de-DE");
console.log(date); // 17.6.2022
```

Note : Nous pouvons obtenir une liste de tous les codes de locale [ici](https://saimana.com/list-of-country-locale-code/).

### Comment Utiliser Moment.js

Moment.js est l'un des packages de dates les plus populaires disponibles pour tous, et nous pouvons l'utiliser pour obtenir la date actuelle également.

 Tant que vous avez Moment.js installé dans votre projet, tout ce que vous avez à faire est d'obtenir la date actuelle comme suit :

```js
var date = moment();

var currentDate = date.format('D/MM/YYYY');
console.log(currentDate); // "17/06/2022"
```

Nous pouvons également le manipuler en fonction de la manière dont nous voulons que le format de la date apparaisse.

## Conclusion

Dans cet article, nous avons appris diverses approches pour obtenir la date actuelle en utilisant JavaScript seul ou avec une bibliothèque JavaScript externe.

Vous pouvez lire plus sur la manière dont vous pouvez facilement formater les dates [ici](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/).

Embarquez pour un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.