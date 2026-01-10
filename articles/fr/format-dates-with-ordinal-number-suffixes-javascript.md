---
title: Comment formater les dates avec des suffixes de nombres ordinaux (-st, -nd,
  -rd, -th) en JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-01-03T21:57:47.000Z'
originalURL: https://freecodecamp.org/news/format-dates-with-ordinal-number-suffixes-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-template--4-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment formater les dates avec des suffixes de nombres ordinaux (-st,
  -nd, -rd, -th) en JavaScript
seo_desc: 'Many online resources teach you how to format dates. But it''s hard to
  find any that explain how to format dates with an ordinal number suffix (like 1st)
  in JavaScript – without using a library.

  In this short article, you will learn how to format date...'
---

De nombreuses ressources en ligne vous apprennent à formater des dates. Mais il est difficile d'en trouver qui expliquent comment formater des dates avec un suffixe de nombre ordinal (comme 1**er**) en JavaScript – sans utiliser de bibliothèque.

Dans cet article court, vous apprendrez à formater des dates en JavaScript avec des nombres ordinaux. Les nombres ordinaux utilisent tous un suffixe. Les suffixes sont « -er » (comme pour 1er), « -nd » (comme pour 2nd), « -rd » (comme pour 3rd), ou « -th » (comme pour 4th). Ils sont utilisés pour les dates et lorsque vous devez ordonner quelque chose. Au lieu de 15, vous auriez 15th, par exemple.

Pour les dates, c'est aussi une manière conviviale de représenter une date sur une page web, et il peut vous être demandé de formater votre date avec des nombres ordinaux, comme le 15 mai 2022, au lieu de 15 mai 2022.

## Comment formater les dates en JavaScript

Il existe de nombreuses façons de formater vos dates en JavaScript. Mais pour cela, vous avez besoin du jour, du mois et de l'année assignés à différentes variables afin de pouvoir les rassembler dans l'ordre souhaité :

```js
const dateObj = new Date();
const day = dateObj.getDate();
const month = dateObj.toLocaleString("default", { month: "long" });
const year = dateObj.getFullYear();

const date = `${month} ${day}, ${year}`;
console.log(date); // "décembre 23, 2022"
```

**Note :** Vous pouvez en apprendre davantage sur la façon de formater les dates dans [cet article](https://www.freecodecamp.org/news/javascript-date-format-how-to-format-a-date-in-js/) et cette [méthode en une ligne](https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/).

## Comment formater les dates avec des suffixes de nombres ordinaux (-st, -nd, -rd, et -th) en JavaScript

Maintenant que vous avez votre date, mais vous voulez que le jour soit formaté comme un nombre ordinal – ce qui signifie que 23 devrait être 23rd, par exemple.

Vous pouvez créer une fonction qui vérifie chaque nombre et retourne le suffixe approprié.

```js
const nthNumber = (number) => {
  if (number > 3 && number < 21) return "th";
  switch (number % 10) {
    case 1:
      return "st";
    case 2:
      return "nd";
    case 3:
      return "rd";
    default:
      return "th";
  }
};
```

Cette méthode vérifie chaque groupe de nombres et retourne le suffixe approprié. Par exemple, de 4 à 20, il aura le suffixe de nombre ordinal « th ». Ensuite, les instructions de cas de commutation vérifient correctement d'autres groupes de nombres et retournent le suffixe de nombre ordinal approprié.

Vous pouvez maintenant mettre à jour votre arrangement de date pour ajouter la fonction `nthNumber()` et passer le numéro du jour :

```js
const date = `${month} ${day}${nthNumber(day)}, ${year}`;
console.log(date); // "décembre 23rd, 2022"
```

Voici à quoi ressemble l'ensemble du code :

```js
const dateObj = new Date();
const day = dateObj.getDate();
const month = dateObj.toLocaleString("default", { month: "long" });
const year = dateObj.getFullYear();

const nthNumber = (number) => {
  if (number > 3 && number < 21) return "th";
  switch (number % 10) {
    case 1:
      return "st";
    case 2:
      return "nd";
    case 3:
      return "rd";
    default:
      return "th";
  }
};

const date = `${month} ${day}${nthNumber(day)}, ${year}`;
console.log(date); // "décembre 23rd, 2022"
```

## Conclusion

Vous pouvez écrire la fonction de nombreuses manières, mais tout ce que vous faites, c'est vérifier le nombre pour attacher le suffixe de nombre ordinal approprié. Voici une autre façon d'écrire la méthode :

```js
const nthNumber = (number) => {
  return number > 0
    ? ["th", "st", "nd", "rd"][
        (number > 3 && number < 21) || number % 10 > 3 ? 0 : number % 10
      ]
    : "";
};
```

N'hésitez pas à ajuster la fonction pour produire le résultat souhaité, et amusez-vous à coder !