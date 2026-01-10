---
title: Comment formater un nombre en devise en JavaScript
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-11-03T15:29:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-number-as-currency-in-javascript-one-line-of-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover-template--2-.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment formater un nombre en devise en JavaScript
seo_desc: 'When you''re working with data from an API or an external resource, you''ll
  get these data in some general format. For example, if you are building a store,
  you might have data like price.

  This price data might be in the form of a general number such a...'
---

Lorsque vous travaillez avec des données provenant d'une API ou d'une ressource externe, vous obtiendrez ces données dans un format général. Par exemple, si vous construisez un magasin, vous pourriez avoir des données comme le prix.

Ces données de prix pourraient être sous la forme d'un nombre général tel que 14340 ou tout autre nombre comme vu dans le tableau ci-dessous :

```js
const books = [
    {
        "id": 001,
        "name": "Clean Code",
        "price": 10.99,
    },
    {
        "id": 002,
        "name": "Introduction to Algorithms",
        "price": 1199,
    },
    {
        "id": 003,
        "name": "Programming Pearls",
        "price": 1.05,
    },
    {
        "id": 004,
        "name": "Program or Be Programmed",
        "price": 14340,
    }
]
```

Vous ne voulez pas passer directement des nombres dans votre application ou votre page web car ils seraient difficiles à comprendre pour les lecteurs et les utilisateurs.

Même si vous ajoutez un symbole de devise, cela ne résout pas le problème car vous voudriez ajouter des virgules et des décimales aux positions correctes. Vous voudriez également que chaque prix soit affiché en fonction de la devise avec un formatage approprié.

Par exemple, 14340 serait $14,340.00 (dollars américains) ou ₹14,340.00 (roupies) ou €14.340,00 (euros) et ainsi de suite, selon la devise, la locale et le style définis. Et vous pouvez convertir ces nombres en devises en utilisant la méthode `Intl.NumberFormat()` en JavaScript.

Au cas où vous seriez pressé, voici un exemple de base de ce à quoi ressemblera le code :

```js
const price = 14340;

// Formater le prix ci-dessus en USD en utilisant la locale, le style et la devise.
let USDollar = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});

console.log(`La version formatée de ${price} est ${USDollar.format(price)}`);
// La version formatée de 14340 est $14,340.00
```

Dans cet article, je vais vous aider à comprendre chacune des options ci-dessus, ce qu'elles font et comment utiliser correctement cette méthode pour formater un nombre en devise.

## Comment utiliser le constructeur `Intl.NumberFormat()` pour formater des nombres en devise

Vous pouvez utiliser le constructeur `Intl.NumberFormat()` pour créer des objets `Intl.NumberFormat` qui permettent un formatage de nombres sensible à la langue, tel que le formatage de devise.

Ce constructeur prend deux paramètres principaux, `locales` et `options`. Ils sont tous deux optionnels.

```js
new Intl.NumberFormat(locales, options)

// Ou

Intl.NumberFormat(locales, options)
```

**Notez** que `Intl.NumberFormat()` peut être appelé avec ou sans `new`. Les deux créeront une nouvelle instance `Intl.NumberFormat`.

Lorsque vous utilisez le constructeur `Intl.NumberFormat()` sans passer de locale ou d'option, il ne formatera le nombre qu'en ajoutant des virgules.

```js
const price = 14340;
console.log(new Intl.NumberFormat().format(price)); // 14,340
```

Vous ne voulez pas un formatage de nombre régulier, comme vu ci-dessus. Vous voulez formater ces nombres en devise afin qu'il retourne le symbole de devise avec un formatage approprié sans avoir à concaténer manuellement.

Explorons maintenant les deux paramètres.

### Le premier argument : Locales

La locale est un paramètre optionnel qui peut être passé sous forme de chaîne. Elle représente une région géographique, politique ou culturelle spécifique. Elle formate simplement le nombre en fonction de la locale et n'est pas le formatage de devise.

```js
const price = 143450;

console.log(new Intl.NumberFormat('en-US').format(price)); // 143,450
console.log(new Intl.NumberFormat('en-IN').format(price)); // 1,43,450
console.log(new Intl.NumberFormat('en-DE').format(price)); // 143.450
```

Vous remarquerez que les nombres ou les prix sont maintenant formatés localement en fonction de la locale. Explorons maintenant le paramètre options pour personnaliser les nombres en tant que devise.

### Le deuxième argument : Options (Style, Devise, …)

C'est le paramètre principal et vous pouvez l'utiliser pour appliquer plus de formatage comme celui de la devise. Il s'agit d'un objet JavaScript qui contient d'autres paramètres comme :

* `style` : Vous utilisez cela pour spécifier le type de formatage que vous souhaitez. Cela prend des valeurs comme decimals, currency et units. Pour cet article, vous utiliserez **currency** car c'est le style dans lequel vous souhaitez formater le nombre.
    
* `currency` : Une autre option est currency. Vous pouvez utiliser cette option pour spécifier la devise que vous souhaitez formater, telle que `'USD'`, `'CAD'`, `'GBP'`, `'INR'` et bien d'autres. Cela aidera également à fournir le symbole à la position appropriée en fonction de la locale.
    

```js
// formater le nombre en dollar américain
let USDollar = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});

// formater le nombre en livres sterling
let pounds = Intl.NumberFormat('en-GB', {
    style: 'currency',
    currency: 'GBP',
});

// formater le nombre en roupie indienne
let rupee = new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
});

// formater le nombre en euro
let euro = Intl.NumberFormat('en-DE', {
    style: 'currency',
    currency: 'EUR',
});

console.log('Dollars: ' + USDollar.format(price));
// Dollars: $143,450.00

console.log(`Pounds: ${pounds.format(price)}`);
// Pounds: £143,450.00

console.log('Rupees: ' + rupee.format(price));
// Rupees: ₹1,43,450.00

console.log(`Euro: ${euro.format(price)}`);
// Euro: €143,450.00
```

Il existe d'autres options que vous n'utiliserez probablement jamais ou ne changerez pas, comme `useGrouping`, qui est utilisé pour regrouper le nombre en utilisant des virgules (ou des points, pour certaines locales). Il s'agit d'un champ booléen - par défaut, il est défini sur `true`. C'est pourquoi votre sortie a eu une virgule ou un point dans cet article (comme $143,450.00).

Lorsque vous définissez sa valeur sur `false`, vous remarquerez qu'il n'y a plus de regroupement :

```js
let euro = Intl.NumberFormat('en-DE', {
    style: 'currency',
    currency: 'EUR',
    useGrouping: false,
});

console.log(`Euro: ${euro.format(price)}`);
// Euro: €143450.00
```

Une autre option est `maximumSignificantDigits`. Vous pouvez l'utiliser pour arrondir votre variable de prix en fonction du nombre de chiffres significatifs que vous avez définis. Par exemple, lorsque vous définissez la valeur sur `3`, `143,450.00` deviendra `143,000`.

```js
let pounds = Intl.NumberFormat('en-GB', {
    style: 'currency',
    currency: 'GBP',
    maximumSignificantDigits: 3,
});

console.log(`Pounds: ${pounds.format(price)}`);
// Pounds: £143,000
```

## Voilà ! 🚀

J'espère que cet article a valu votre temps. Vous savez maintenant comment formater un nombre en devise avec JavaScript sans dépendre d'une bibliothèque externe.

Lorsque vous travaillez avec des bibliothèques comme React, Vue et autres, vous pouvez en faire une fonction utilitaire, l'importer dans l'un de vos composants et l'utiliser au lieu d'installer une bibliothèque entière (sauf si vous avez besoin de plus de fonctionnalités).

Amusez-vous bien à coder !