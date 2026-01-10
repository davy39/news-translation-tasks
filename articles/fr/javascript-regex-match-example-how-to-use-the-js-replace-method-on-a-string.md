---
title: Exemple de correspondance Regex JavaScript – Comment utiliser JS Replace sur
  une chaîne
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2021-01-04T10:21:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-regex-match-example-how-to-use-the-js-replace-method-on-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/6020e04e0a2838549dcc0c26-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Regex
  slug: regex
- name: Regular Expressions
  slug: regular-expressions
seo_title: Exemple de correspondance Regex JavaScript – Comment utiliser JS Replace
  sur une chaîne
seo_desc: 'Regular expressions, abbreviated as regex, or sometimes regexp, are one
  of those concepts that you probably know is really powerful and useful. But they
  can be daunting, especially for beginning programmers.

  It doesn''t have to be this way. JavaScript...'
---

Les expressions régulières, abrégées en regex, ou parfois regexp, sont l'un de ces concepts que vous savez probablement très puissants et utiles. Mais elles peuvent être intimidantes, surtout pour les programmeurs débutants.

Cela n'a pas à être le cas. JavaScript inclut plusieurs méthodes utiles qui rendent l'utilisation des expressions régulières beaucoup plus gérable. Parmi les méthodes incluses, les méthodes `.match()`, `.matchAll()` et `.replace()` sont probablement celles que vous utiliserez le plus souvent.

Dans ce tutoriel, nous allons passer en revue les tenants et aboutissants de ces méthodes, et examiner quelques raisons pour lesquelles vous pourriez les utiliser plutôt que les autres méthodes JS incluses.

## Une brève introduction aux expressions régulières

Selon MDN, les expressions régulières sont des "motifs utilisés pour faire correspondre des combinaisons de caractères dans des chaînes".

Ces motifs peuvent parfois inclure des caractères spéciaux (`*`, `+`), des assertions (`\W`, `^`), des groupes et des plages (`(abc)`, `[123]`), et d'autres choses qui rendent les regex si puissantes mais difficiles à comprendre.

Au cœur, les regex concernent la recherche de motifs dans des chaînes – tout, depuis le test d'une chaîne pour un seul caractère jusqu'à la vérification qu'un numéro de téléphone est valide, peut être fait avec des expressions régulières.

Si vous êtes tout nouveau dans les regex et que vous aimeriez vous entraîner avant de continuer, consultez nos [défis de codage interactifs](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/using-the-test-method).

## Comment utiliser la méthode `.match()`

Donc, si les regex concernent la recherche de motifs dans des chaînes, vous pourriez vous demander ce qui rend la méthode `.match()` si utile ?

Contrairement à la méthode `.test()` qui retourne simplement `true` ou `false`, `.match()` retournera réellement la correspondance contre la chaîne que vous testez. Par exemple :

```js
const csLewisQuote = 'We are what we believe we are.';
const regex1 = /are/;
const regex2 = /eat/;

csLewisQuote.match(regex1); // ["are", index: 3, input: "We are what we believe we are.", groups: undefined]

csLewisQuote.match(regex2); // null

```

Cela peut être vraiment utile pour certains projets, surtout si vous voulez extraire et manipuler les données que vous correspondez sans changer la chaîne originale.

Si tout ce que vous voulez savoir est si un motif de recherche est trouvé ou non, utilisez la méthode `.test()` – elle est beaucoup plus rapide.

Il y a deux valeurs de retour principales que vous pouvez attendre de la méthode `.match()` :

1. S'il y a une correspondance, la méthode `.match()` retournera un tableau avec la correspondance. Nous entrerons dans plus de détails à ce sujet dans un instant.
2. S'il n'y a pas de correspondance, la méthode `.match()` retournera `null`.

Certains d'entre vous ont peut-être déjà remarqué cela, mais si vous regardez l'exemple ci-dessus, `.match()` ne correspond qu'à la première occurrence du mot "are".

Souvent, vous voudrez savoir combien de fois un motif est correspond à la chaîne que vous testez, alors regardons comment faire cela avec `.match()`.

### Différents modes de correspondance

S'il y a une correspondance, le tableau que `.match()` retourne a deux modes différents, pour ne pas dire mieux.

Le premier mode est lorsque le drapeau global (`g`) n'est pas utilisé, comme dans l'exemple ci-dessus :

```js
const csLewisQuote = 'We are what we believe we are.';
const regex = /are/;

csLewisQuote.match(regex); // ["are", index: 3, input: "We are what we believe we are.", groups: undefined]

```

Dans ce cas, nous `.match()` un tableau avec la première correspondance ainsi que l'index de la correspondance dans la chaîne originale, la chaîne originale elle-même, et tous les groupes de correspondance qui ont été utilisés.

Mais disons que vous voulez voir combien de fois le mot "are" apparaît dans une chaîne. Pour cela, ajoutez simplement le drapeau de recherche global à votre expression régulière :

```js
const csLewisQuote = 'We are what we believe we are.';
const regex = /are/g;

csLewisQuote.match(regex); // ["are", "are"]

```

Vous n'obtiendrez pas les autres informations incluses avec le mode non global, mais vous obtiendrez un tableau avec toutes les correspondances dans la chaîne que vous testez.

### Sensibilité à la casse

Une chose importante à retenir est que les regex sont sensibles à la casse. Par exemple, disons que vous voulez voir combien de fois le mot "we" apparaît dans votre chaîne :

```js
const csLewisQuote = 'We are what we believe we are.';
const regex = /we/g;

csLewisQuote.match(regex); // ["we", "we"]

```

Dans ce cas, vous correspondez à un "w" minuscule suivi d'un "e" minuscule, ce qui n'apparaît que deux fois.

Si vous voulez toutes les instances du mot "we" qu'il soit en majuscule ou en minuscule, vous avez quelques options.

Tout d'abord, vous pourriez utiliser la méthode `.toLowercase()` sur la chaîne avant de la tester avec la méthode `.match()` :

```js
const csLewisQuote = 'We are what we believe we are.'.toLowerCase();
const regex = /we/g;

csLewisQuote.match(regex); // ["we", "we", "we"]

```

Ou si vous voulez préserver la casse originale, vous pourriez ajouter le drapeau de recherche insensible à la casse (`i`) à votre expression régulière :

```js
const csLewisQuote = 'We are what we believe we are.';
const regex = /we/gi;

csLewisQuote.match(regex); // ["We", "we", "we"]

```

## La nouvelle méthode `.matchAll()`

Maintenant que vous savez tout sur la méthode `.match()`, il vaut la peine de noter que la méthode `.matchAll()` a été récemment introduite.

Contrairement à la méthode `.match()` qui retourne un tableau ou `null`, `.matchAll()` nécessite le drapeau de recherche global (`g`), et retourne soit un itérateur soit un tableau vide :

```js
const csLewisQuote = 'We are what we believe we are.';
const regex1 = /we/gi;
const regex2 = /eat/gi;

[...csLewisQuote.matchAll(regex1)]; 
// [
//   ["We", index: 0, input: "We are what we believe we are.", groups: undefined],
//   ["we", index: 12, input: "We are what we believe we are.", groups: undefined]
//   ["we", index: 23, input: "We are what we believe we are.", groups: undefined]
// ]

[...csLewisQuote.matchAll(regex2)]; // []

```

Bien que cela semble être juste une méthode `.match()` plus compliquée, le principal avantage que `.matchAll()` offre est qu'elle fonctionne mieux avec les groupes de capture.

Voici un exemple simple :

```js
const csLewisRepeat = "We We are are";
const repeatRegex = /(\w+)\s\1/g;

csLewisRepeat.match(repeatRegex); // ["We We", "are are"]

```

```js
const csLewisRepeat = "We We are are";
const repeatRegex = /(\w+)\s\1/g;

[...repeatStr.matchAll(repeatRegex)];

// [
//   ["We We", "We", index: 0, input: "We We are are", groups: undefined],
//   ["are are", "are", index: 6, input: "We We are are", groups: undefined],
// ]

```

Bien que cela ne fasse qu'effleurer la surface, gardez à l'esprit qu'il est probablement préférable d'utiliser `.matchAll()` si vous utilisez le drapeau `g` et que vous voulez toutes les informations supplémentaires que `.match()` fournit pour une seule correspondance (index, la chaîne originale, et ainsi de suite).

## Comment utiliser la méthode `.replace()`

Maintenant que vous savez comment faire correspondre des motifs dans des chaînes, vous voudrez probablement faire quelque chose d'utile avec ces correspondances.

L'une des choses les plus courantes que vous ferez une fois que vous aurez trouvé un motif correspondant est de remplacer ce motif par autre chose. Par exemple, vous pourriez vouloir remplacer "paid" dans "paidCodeCamp" par "free". Les regex seraient un bon moyen de faire cela.

Puisque `.match()` et `.matchAll()` retournent des informations sur l'index pour chaque motif correspondant, selon la façon dont vous l'utilisez, vous pourriez utiliser cela pour faire une manipulation de chaîne sophistiquée. Mais il y a une manière plus facile – en utilisant la méthode `.replace()`.

Avec `.replace()`, tout ce que vous avez à faire est de lui passer une chaîne ou une expression régulière que vous voulez faire correspondre comme premier argument, et une chaîne pour remplacer ce motif correspondant comme deuxième argument :

```js
const campString = 'paidCodeCamp';
const fCCString1 = campString.replace('paid', 'free');
const fCCString2 = campString.replace(/paid/, 'free');

console.log(campString); // "paidCodeCamp"
console.log(fCCString1); // "freeCodeCamp"
console.log(fCCString2); // "freeCodeCamp"

```

Le meilleur aspect est que `.replace()` retourne une nouvelle chaîne, et l'original reste le même.

Similaire à la méthode `.match()`, `.replace()` ne remplacera que le premier motif correspondant qu'il trouve à moins que vous n'utilisiez regex avec le drapeau `g` :

```js
const campString = 'paidCodeCamp is awesome. You should check out paidCodeCamp.';
const fCCString1 = campString.replace('paid', 'free');
const fCCString2 = campString.replace(/paid/g, 'free');

console.log(fCCString1); // "freeCodeCamp is awesome. You should check out paidCodeCamp."
console.log(fCCString2); // "freeCodeCamp is awesome. You should check out freeCodeCamp."

```

Et similaire à avant, que vous passiez une chaîne ou une expression régulière comme premier argument, il est important de se rappeler que le motif de correspondance est sensible à la casse :

```js
const campString = 'PaidCodeCamp is awesome. You should check out PaidCodeCamp.';
const fCCString1 = campString.replace('Paid', 'free');
const fCCString2 = campString.replace(/paid/gi, 'free');

console.log(fCCString1); // "freeCodeCamp is awesome. You should check out PaidCodeCamp."
console.log(fCCString2); // "freeCodeCamp is awesome. You should check out freeCodeCamp."

```

## Comment utiliser la méthode `.replaceAll()`

Tout comme `.match()` a une méthode plus récente `.matchAll()`, `.replace()` a une méthode plus récente `.replaceAll()`.

La seule réelle différence entre `.replace()` et `.replaceAll()` est que vous devez utiliser le drapeau de recherche global si vous utilisez une expression régulière avec `.replaceAll()` :

```js
const campString = 'paidCodeCamp is awesome. You should check out paidCodeCamp.';
const fCCString1 = campString.replaceAll('paid', 'free');
const fCCString2 = campString.replaceAll(/paid/g, 'free');

console.log(fCCString1); // "freeCodeCamp is awesome. You should check out freeCodeCamp."
console.log(fCCString2); // "freeCodeCamp is awesome. You should check out freeCodeCamp."

```

Le vrai avantage avec `.replaceAll()` est qu'il est un peu plus lisible, et remplace tous les motifs correspondants lorsque vous lui passez une chaîne comme premier argument.

C'est tout ! Maintenant vous connaissez les bases de la correspondance et du remplacement de parties de chaînes avec regex et quelques méthodes JS intégrées. Ce sont des exemples assez simples, mais j'espère qu'ils ont tout de même montré à quel point même un peu de regex peut être puissant.

Cela a-t-il été utile ? Comment utilisez-vous les méthodes `.match()`, `.matchAll()`, `.replace()`, et `.replaceAll()` ? Faites-le moi savoir sur [Twitter](https://twitter.com/kriskoishigawa).