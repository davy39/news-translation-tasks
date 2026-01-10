---
title: Comment valider les URL en JavaScript
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2022-11-22T04:12:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-urls-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/jase-bloor-oCZHIa1D4EU-unsplash--1-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
- name: Regex
  slug: regex
- name: url
  slug: url
seo_title: Comment valider les URL en JavaScript
seo_desc: 'A Uniform Resource Locator (URL) is what leads you to a page or file on
  the internet. URLs serve as the addresses of things on the internet.

  All valid URLs follow certain patterns. So if you know those patterns, you can determine
  whether a URL is val...'
---

Un localisateur de ressource uniforme (URL) est ce qui vous mène à une page ou un fichier sur Internet. Les URL servent d'adresses pour les choses sur Internet.

Toutes les URL valides suivent certains motifs. Ainsi, si vous connaissez ces motifs, vous pouvez déterminer si une URL est valide ou non dans votre programme et donner un retour, lancer une erreur, et ainsi de suite.

Dans ce tutoriel, vous apprendrez trois méthodes pour vérifier si une chaîne de caractères en JavaScript est une URL valide :

* [Comment utiliser le constructeur `URL` pour valider les URL](#heading-comment-utiliser-le-constructeur-url-pour-valider-les-url)

* [Comment utiliser les packages npm pour valider les URL](#heading-comment-utiliser-les-packages-npm-pour-valider-les-url)

* [Comment utiliser les expressions régulières pour valider les URL](#heading-comment-utiliser-les-expressions-regulieres-pour-valider-les-url)

## Comment utiliser le constructeur `URL` pour valider les URL

Lorsque vous passez une chaîne de caractères au constructeur `URL`, il retourne un nouvel objet `URL` si la chaîne est une URL valide. Sinon, il retourne une erreur :

```javascript
const fccUrl = new URL("https://www.freecodecamp.org/");
console.log(fccUrl);
```

Voici ce que vous obtenez lorsque vous affichez `fccUrl` dans la console :

![Un objet URL en JavaScript](https://www.freecodecamp.org/news/content/images/2022/11/validURL.PNG align="left")

*Un* objet `URL` en JavaScript

Cet objet signifie que la chaîne que vous avez passée au constructeur `URL` était une URL valide.

Voyons maintenant ce que vous obtenez lorsque vous passez une chaîne d'URL invalide :

```javascript
const fccUrl = new URL('freecodecamp');
console.log(fccUrl);
```

La chaîne `'freecodecamp'` n'est pas une URL valide. Ainsi, vous obtenez l'erreur `TypeError` suivante :

![Une erreur TypeError après avoir passé une URL invalide au constructeur URL](https://www.freecodecamp.org/news/content/images/2022/11/invalidURL.PNG align="left")

*URL invalide*

Pour résumer :

1. Lorsque vous passez une chaîne d'URL valide au constructeur `URL`, il retourne un nouvel objet `URL`.

2. Lorsque vous passez une chaîne d'URL invalide au constructeur `URL`, il retourne une erreur `TypeError`.

Avec cette connaissance, vous pouvez créer une fonction personnalisée pour vérifier la validité d'une chaîne d'URL donnée.

### Comment créer une fonction de validation d'URL avec le constructeur `URL`

En utilisant le constructeur `URL` et une instruction `try...catch`, vous pouvez créer une fonction personnalisée `isValidUrl` :

```javascript
function isValidUrl(string) {
  try {
    new URL(string);
    return true;
  } catch (err) {
    return false;
  }
}
```

La fonction `isValidUrl` retourne `true` lorsque la chaîne que vous passez en argument est une URL valide. Sinon, elle retourne `false` :

```javascript
console.log(isValidUrl('https://www.freecodecamp.org/')); // true
console.log(isValidUrl('mailto://mail@freecodecamp.org')); // true
console.log(isValidUrl('freecodecamp')); // false
```

### Comment valider uniquement les URL HTTP avec le constructeur `URL`

Parfois, vous pouvez vouloir vérifier si la chaîne est une URL HTTP valide, et rejeter d'autres URL valides comme `'mailto://mail@freecodecamp.org'`.

Si vous regardez de près l'objet `URL`, l'une de ses propriétés est `protocol` :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/protocol.png align="left")

*L'*objet `URL` a une propriété protocol.

Dans l'exemple ci-dessus, la valeur de la propriété protocol est `'https:'`.

Pour vérifier si une chaîne est une URL HTTP valide, vous pouvez utiliser la propriété protocol de l'objet URL :

```javascript
function isValidHttpUrl(string) {
  try {
    const newUrl = new URL(string);
    return newUrl.protocol === 'http:' || newUrl.protocol === 'https:';
  } catch (err) {
    return false;
  }
}

console.log(isValidHttpUrl('https://www.freecodecamp.org/')); // true
console.log(isValidHttpUrl('mailto://mail@freecodecamp.org')); // false
console.log(isValidHttpUrl('freecodecamp')); // false
```

La différence ici est que vous ne retournez pas `true` après la création du nouvel objet `URL`. Au lieu de cela, vous vérifiez si la propriété `protocol` a une valeur égale à `'http:'` ou `'https:'` et vous retournez `true` si c'est le cas et `false` sinon.

## Comment utiliser les packages npm pour valider les URL

Il existe deux packages NPM que vous pouvez utiliser : `is-url` et `is-url-http`.

Ces packages sont le moyen le plus simple de vérifier si une chaîne est une URL valide. Tout ce que vous avez à faire est de passer une chaîne en tant que paramètre, et ils retourneront `true` ou `false`.

Voyons comment fonctionnent ces deux packages.

### Comment valider les URL avec le package `is-url`

Vous pouvez utiliser le package `is-url` pour vérifier si une chaîne est une URL valide. Ce package ne vérifie pas le protocole de l'URL qui lui est passée.

Pour utiliser `is-url`, installez-le d'abord en utilisant la commande suivante :

```javascript
npm install is-url
```

Ensuite, importez-le et passez votre chaîne d'URL en tant qu'argument :

```javascript
import isUrl from 'is-url';

const firstCheck = isUrl('https://www.freecodecamp.org/');
const secondCheck = isUrl('mailto://mail@freecodecamp.org');
const thirdCheck = isUrl('freeCodeCamp');

console.log(firstCheck); // true
console.log(secondCheck); // true
console.log(thirdCheck); // false
```

Le package `is-url` retourne `true` pour les chaînes qui ont des formats d'URL valides et `false` pour les chaînes qui ont des formats d'URL invalides.

Dans l'exemple, `firstCheck` (avec le protocole `https:`) et `secondCheck` (avec le protocole `mailto:`) retournent tous deux `true`.

### Comment valider les URL HTTP avec le package `is-http-url`

Vous pouvez utiliser le package `is-url-http` pour vérifier si une chaîne est une URL HTTP valide.

Installez le package avec la commande suivante :

```javascript
npm install is-url-http
```

Ensuite, importez-le et passez la chaîne d'URL comme suit :

```javascript
import isUrlHttp from 'is-url-http';

const firstCheck = isUrlHttp('https://www.freecodecamp.org/');
const secondCheck = isUrlHttp('mailto://freecodecamp@mail.org');
const thirdCheck = isUrlHttp('freeCodeCamp');

console.log(firstCheck); // true
console.log(secondCheck); // false
console.log(thirdCheck); // false
```

Dans cet exemple, seul `firstCheck` retourne `true`. Le package `is-url-http` ne vérifie pas seulement que la chaîne est une URL valide, il vérifie également si c'est une URL HTTP valide. C'est pourquoi il retourne `false` pour `secondCheck`, qui n'est pas une URL HTTP valide.

## Comment utiliser les expressions régulières pour valider les URL

Vous pouvez également utiliser des expressions régulières, ou regex, pour vérifier si une chaîne est une URL valide ou non.

Toutes les URL valides suivent un motif particulier. Elles ont trois parties principales, qui sont :

* Protocole

* Nom de domaine (ou adresse IP)

* Port et chemin

Parfois, une chaîne de requête ou un localisateur de fragment suit le chemin.

Vous pouvez en apprendre davantage sur les motifs des URL à partir de cet [article freeCodeCamp sur la structure des URL](https://www.freecodecamp.org/news/what-happens-when-you-hit-url-in-your-browser/).

Connaissant le motif des URL, vous pouvez utiliser des expressions régulières pour vérifier l'existence de tels motifs dans une chaîne. Si les motifs existent, alors la chaîne passe le test regex. Sinon, elle échoue.

De plus, en utilisant des expressions régulières, vous pouvez vérifier toutes les URL valides, ou seulement vérifier les URL HTTP valides.

### Comment valider les URL avec les expressions régulières

```javascript
function isValidUrl(str) {
  const pattern = new RegExp(
    '^([a-zA-Z]+:\\/\\/)?' + // protocole
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // nom de domaine
      '((\\d{1,3}\\.){3}\\d{1,3}))' + // OU adresse IP (v4)
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port et chemin
      '(\\?[;&a-z\\d%_.~+=-]*)?' + // chaîne de requête
      '(\\#[-a-z\\d_]*)?$', // localisateur de fragment
    'i'
  );
  return pattern.test(str);
}

console.log(isValidUrl('https://www.freecodecamp.org/')); // true
console.log(isValidUrl('mailto://freecodecamp.org')); // true
console.log(isValidUrl('freeCodeCamp')); // false
```

L'expression régulière dans la fonction `isValidUrl` ci-dessus vérifie si une chaîne est une URL valide. La vérification du protocole `^([a-zA-Z]+:\\/\\/)?` n'est pas limitée à `https:`.

C'est pourquoi le deuxième exemple avec le protocole `mailto:` retourne `true`.

### Comment valider les URL HTTP avec les expressions régulières

Pour utiliser les expressions régulières afin de vérifier si une chaîne est une URL HTTP valide, vous devez modifier la vérification du protocole.

Au lieu de `^([a-zA-Z]+:\\/\\/)?`, vous devez utiliser `'^(https?:\\/\\/)?'` :

```javascript
function isValidHttpUrl(str) {
  const pattern = new RegExp(
    '^(https?:\\/\\/)?' + // protocole
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // nom de domaine
      '((\\d{1,3}\\.){3}\\d{1,3}))' + // OU adresse ip (v4)
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port et chemin
      '(\\?[;&a-z\\d%_.~+=-]*)?' + // chaîne de requête
      '(\\#[-a-z\\d_]*)?$', // localisateur de fragment
    'i'
  );
  return pattern.test(str);
}

console.log(isValidHttpUrl('https://www.freecodecamp.org/')); // true
console.log(isValidHttpUrl('mailto://freecodecamp.org')); // false
console.log(isValidHttpUrl('freeCodeCamp')); // false
```

Maintenant, seul le premier exemple qui a un protocole `https:` valide retourne `true`. Notez que les chaînes d'URL avec `http:` fonctionnent également.

## Conclusion

Dans cet article, vous avez appris comment vérifier la validité des URL en JavaScript. Vous connaissez maintenant les trois méthodes suivantes pour le faire.

* Comment utiliser le constructeur `URL` pour valider les URL

* Comment utiliser les packages npm pour valider les URL (`is-url` et `is-http-url`)

* Comment utiliser les expressions régulières pour valider les URL

C'est à vous de choisir la méthode avec laquelle vous êtes à l'aise pour travailler.

Merci d'avoir lu. Et bon codage !