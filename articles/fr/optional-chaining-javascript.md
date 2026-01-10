---
title: Chaînage optionnel en JavaScript – Expliqué avec des exemples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-13T21:54:21.000Z'
originalURL: https://freecodecamp.org/news/optional-chaining-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-7-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Chaînage optionnel en JavaScript – Expliqué avec des exemples
seo_desc: 'JavaScript development often involves navigating through nested objects,
  which can be cumbersome and error-prone, especially when dealing with null or undefined
  values. Enter optional chaining—a game-changer in modern JavaScript syntax.

  In this artic...'
---

Le développement JavaScript implique souvent de naviguer à travers des objets imbriqués, ce qui peut être fastidieux et sujet aux erreurs, surtout lorsqu'on traite des valeurs `null` ou `undefined`. Voici le chaînage optionnel—une révolution dans la syntaxe moderne de JavaScript.

Dans cet article, nous explorerons le chaînage optionnel à travers des exemples pratiques, démontrant comment il simplifie le code et rend le développement plus efficace.

Vous pouvez obtenir tout le code source depuis [ici](https://github.com/dotslashbit/fcc-article-resources/blob/main/js-optional-chaining/index.js).

## Table des matières

* [Qu'est-ce que le chaînage optionnel](#heading-quest-ce-que-le-chainage-optionnel) ?
* [Comment accéder aux propriétés imbriquées](#heading-comment-acceder-aux-proprietes-imbriquees)
* [Comment appeler des méthodes imbriquées](#heading-comment-appeler-des-methodes-imbriquees)
* [Accès dynamique aux propriétés](#heading-acces-dynamique-aux-proprietes)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que le chaînage optionnel (`?.`) ?

Le chaînage optionnel, introduit dans ECMAScript 2020, est une fonctionnalité qui simplifie le processus d'accès aux propriétés et méthodes des objets ou tableaux imbriqués lorsque les propriétés intermédiaires peuvent être `null` ou `undefined`.

L'opérateur de chaînage optionnel (`?.`) permet d'accéder aux propriétés ou méthodes sans avoir besoin de vérifications explicites pour `null` ou `undefined`. Si une propriété intermédiaire dans la chaîne est `null` ou `undefined`, l'expression est court-circuitée, et le résultat est défini sur `undefined`.

En programmation, le "court-circuit" fait référence au comportement où l'évaluation d'une expression s'arrête dès qu'une valeur `null` ou `undefined` est rencontrée le long de la chaîne de propriétés ou de méthodes accédées. Au lieu de continuer à évaluer l'expression, le résultat est immédiatement défini sur `undefined`, et tout accès ultérieur à une propriété ou une méthode est ignoré.

Maintenant, plongeons dans des exemples pratiques pour voir comment le chaînage optionnel fonctionne dans des scénarios réels.

## Comment accéder aux propriétés imbriquées

Dans cet exemple, nous avons un objet JavaScript représentant un utilisateur avec des informations d'adresse imbriquées.

```javascript
const user = {
  name: "John",
  address: {
    city: "New York",
    zipcode: "10001"
  }
};

```

### Approche traditionnelle

La manière traditionnelle d'accéder à la propriété `city` dans l'adresse de l'utilisateur implique plusieurs vérifications pour s'assurer que les propriétés existent et ne sont pas `null` ou `undefined`.

```javascript
let city;
if (user && user.address && user.address.city) {
  city = user.address.city;
} else {
  city = "Inconnu";
}

console.log("Approche traditionnelle :", city); // Sortie : New York


```

Ce code vérifie si l'objet utilisateur existe, s'il a une propriété `address`, et si la propriété `address` a une propriété `city`. Si l'une de ces conditions échoue, la variable `city` est définie sur "Inconnu".

### Approche avec chaînage optionnel

Avec le chaînage optionnel, l'accès à la propriété `city` imbriquée devient beaucoup plus simple :

```javascript
const city = user?.address?.city || "Inconnu";

console.log("Approche avec chaînage optionnel :", city); // Sortie : New York

```

L'opérateur `?.` est utilisé pour accéder à la propriété `city` de l'adresse de l'utilisateur. Si une propriété intermédiaire (`user` ou `address`) est `null` ou `undefined`, l'expression est court-circuitée, et le résultat est immédiatement défini sur "Inconnu".

## Comment appeler des méthodes imbriquées

Dans cet exemple, nous avons un objet utilisateur avec une méthode `getAddress()` qui retourne l'adresse de l'utilisateur.

```javascript
const user = {
  name: "Alice",
  getAddress() {
    return {
      city: "San Francisco",
      zipcode: "94105"
    };
  }
};

```

### Approche traditionnelle

La manière traditionnelle d'appeler la méthode `getAddress()` et d'accéder à la propriété `city` implique des vérifications supplémentaires pour s'assurer que la méthode existe et retourne une valeur non nulle.

```javascript
let city;
if (user && user.getAddress) {
  const address = user.getAddress();
  if (address) {
    city = address.city;
  }
}

console.log("Approche traditionnelle :", city); // Sortie : San Francisco

```

Ce code vérifie d'abord si l'objet utilisateur existe et s'il a une méthode `getAddress`. Ensuite, il appelle la méthode et vérifie si l'objet `address` retourné existe avant d'accéder à sa propriété `city`.

### Approche avec chaînage optionnel

Avec le chaînage optionnel, l'appel de la méthode imbriquée et l'accès à la propriété `city` peuvent être faits de manière plus concise :

```javascript
const city = user?.getAddress?.().city || "Inconnu";

console.log("Approche avec chaînage optionnel :", city); // Sortie : San Francisco

```

Ici, l'opérateur de chaînage optionnel est utilisé pour appeler la méthode `getAddress()` et accéder à sa propriété `city`. Si la méthode `getAddress` ou une propriété intermédiaire dans la chaîne est `null` ou `undefined`, l'expression est court-circuitée, et le résultat est immédiatement défini sur "Inconnu".

## Accès dynamique aux propriétés

Dans cet exemple, nous avons un tableau d'utilisateurs, où chaque utilisateur peut ou non avoir un profil.

```javascript
const users = [
  { id: 1, profile: { name: "Alice" } },
  { id: 2 },
  { id: 3, profile: { name: "Bob" } }
];

```

### Approche traditionnelle

La manière traditionnelle d'accéder dynamiquement au nom du profil implique plusieurs vérifications pour chaque objet utilisateur dans le tableau.

```javascript
const names = users.map(user => {
  if (user && user.profile && user.profile.name) {
    return user.profile.name;
  } else {
    return "Inconnu";
  }
});

console.log("Approche traditionnelle :", names); // Sortie : ["Alice", "Inconnu", "Bob"]

```

Ce code utilise `map()` pour itérer sur chaque objet utilisateur dans le tableau et vérifie s'il a un profil avec une propriété `name`. Si la propriété `name` existe, elle est retournée — sinon, "Inconnu" est retourné.

### Approche avec chaînage optionnel

Avec le chaînage optionnel, l'accès dynamique aux propriétés devient plus simple :

```javascript
const names = users.map(user => user?.profile?.name || "Inconnu");

console.log("Approche avec chaînage optionnel :", names); // Sortie : ["Alice", "Inconnu", "Bob"]

```

Ici, l'opérateur de chaînage optionnel est utilisé pour accéder à la propriété `name` du profil de chaque utilisateur. Si une propriété intermédiaire dans la chaîne est `null` ou `undefined`, l'expression est court-circuitée, et "Inconnu" est retourné comme valeur par défaut.

## Conclusion

En appliquant le chaînage optionnel, vous pouvez simplifier votre code et le rendre plus lisible et maintenable.

Alors que JavaScript continue d'évoluer, des fonctionnalités comme le chaînage optionnel jouent un rôle crucial dans l'amélioration de la productivité des développeurs et de la qualité du code.