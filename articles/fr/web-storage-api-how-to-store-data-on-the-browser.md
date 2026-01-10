---
title: Web Storage API – Comment stocker des données dans le navigateur
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-01-12T17:43:34.000Z'
originalURL: https://freecodecamp.org/news/web-storage-api-how-to-store-data-on-the-browser
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/web-storage-api-feature-image.png
tags:
- name: browser
  slug: browser
- name: data
  slug: data
- name: storage
  slug: storage
- name: Web Development
  slug: web-development
seo_title: Web Storage API – Comment stocker des données dans le navigateur
seo_desc: 'The Web Storage API is a set of APIs exposed by the browser so that you
  can store data in the browser.

  The data stored in the Web Storage use the key/value pair format, and both data
  will be stored as strings.

  There are two types of storage introduce...'
---

L'API Web Storage est un ensemble d'API exposées par le navigateur afin que vous puissiez stocker des données dans le navigateur.

Les données stockées dans le Web Storage utilisent le format paire clé/valeur, et les deux données seront stockées sous forme de chaînes de caractères.

Il existe deux types de stockage introduits dans l'API Web Storage : Local Storage et Session Storage.

Dans cet article, je vais vous montrer comment utiliser l'API Web Storage et pourquoi elle est utile pour les développeurs web.

## Comment fonctionne l'API Web Storage

L'API Web Storage expose un ensemble d'objets et de méthodes que vous pouvez utiliser pour stocker des données dans le navigateur. Les données que vous stockez dans le Web Storage sont privées, ce qui signifie qu'aucun autre site web ne peut y accéder.

Dans Google Chrome, vous pouvez consulter le Web Storage en ouvrant la fenêtre des outils de développement et en allant dans l'onglet Application comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/web-storage-location-1.png)
_Emplacement du stockage web dans Google Chrome_

Dans l'image ci-dessus, vous pouvez voir que le menu Storage contient également d'autres types de stockage comme Indexed DB, Web SQL et les cookies. La norme Web SQL a été abandonnée, et IndexedDB est rarement utilisée car elle est trop complexe. Toute donnée que vous stockez dans IndexedDB pourrait mieux être stockée sur le serveur.

Quant aux cookies, c'est un mécanisme plus traditionnel de stockage de données qui ne vous permet de stocker qu'un maximum de 4 Ko de données. En revanche, la capacité du Local Storage est de 10 Mo et celle du session storage est de 5 Mo.

C'est pourquoi nous allons nous concentrer uniquement sur le Local Storage et le Session Storage dans cet article.

## Local Storage et Session Storage expliqués

Le Local Storage et le Session Storage sont les deux mécanismes standard pris en charge par l'API Web Storage.

Le stockage web est spécifique au domaine, ce qui signifie que les données stockées sous un domaine (netflix.com) ne peuvent pas être accessibles par un autre domaine (www.netflix.com ou members.netflix.com).

Le stockage web est également spécifique au protocole. Cela signifie que les données que vous stockez dans un site `http://` ne seront pas disponibles sous le site `https://`.

La principale différence entre le Local et le Session Storage est que le Local Storage stockera vos données pour toujours. Si vous souhaitez supprimer les données, vous devez utiliser la méthode disponible ou les effacer manuellement depuis l'onglet Applications.

En revanche, les données stockées dans le session storage ne sont disponibles que pendant la session de la page. Lorsque vous fermez le navigateur ou l'onglet, le session storage pour cet onglet spécifique est supprimé.

Le Local et le Session Storage peuvent être accessibles via l'objet `window` sous les variables `localStorage` et `sessionStorage`, respectivement. Voyons maintenant les méthodes et propriétés de ces types de stockage.

### Méthodes et propriétés du Local et Session Storage

Le Local et le Session Storage ont les mêmes méthodes et propriétés. Pour définir une nouvelle paire clé/valeur dans le Local Storage, vous pouvez utiliser la méthode `setItem()` de l'objet `localStorage` :

```js
localStorage.setItem('firstName', 'Nathan');
```

Si vous regardez dans le menu Local Storage du navigateur, vous devriez voir les données ci-dessus enregistrées dans le stockage comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/localstorage-setitem.png)
_Stockage d'une paire clé/valeur dans le Local Storage_

La clé que vous utilisez dans `localStorage` doit être unique. Si vous définissez une autre donnée avec une clé qui existe déjà, alors la méthode `setItem()` remplacera la valeur précédente par la nouvelle.

Pour obtenir la valeur du local storage, vous devez appeler la méthode `getItem()` et passer la clé que vous avez utilisée lors de l'enregistrement des données. Si la clé n'existe pas, alors `getItem()` retournera `null` :

```js
const firstName = localStorage.getItem('firstName');
console.log(firstName); // Nathan

const lastName = localStorage.getItem('lastName');
console.log(lastName); // null
```

Pour supprimer les données que vous avez dans le local storage, appelez la méthode `removeItem()` et passez la clé pointant vers les données que vous souhaitez supprimer :

```js
localStorage.removeItem('firstName');
```

La méthode `removeItem()` retournera toujours `undefined`. Lorsque les données que vous souhaitez supprimer n'existent pas, la méthode ne fait simplement rien.

Si vous souhaitez effacer le stockage, vous pouvez utiliser la méthode `clear()` :

```js
localStorage.clear();
```

La méthode `clear()` supprime toutes les paires clé/valeur de l'objet de stockage auquel vous accédez.

### Propriétés du Local et Session Storage

Les deux types de stockage n'ont qu'une seule propriété, qui est la propriété `length` qui montre la quantité de données stockées dans ceux-ci.

```js
sessionStorage.setItem('firstName', 'Nathan');
sessionStorage.setItem('lastName', 'Sebhastian');

console.log(sessionStorage.length); // 2

sessionStorage.clear();
console.log(sessionStorage.length); // 0
```

Et ce sont toutes les méthodes et propriétés auxquelles vous pouvez accéder dans `localStorage` et `sessionStorage`.

## Comment stocker des chaînes JSON dans le stockage Web Storage

Puisque le Web Storage stocke toujours les données sous forme de chaînes, vous pouvez stocker des données complexes sous forme de chaîne JSON, puis convertir cette chaîne en objet lorsque vous y accédez.

Par exemple, supposons que je souhaite stocker les informations suivantes sur un utilisateur :

```js
const user = {
  firstName: 'Nathan',
  lastName: 'Sebhastian',
  url: 'https://codewithnathan.com',
};
```

Au début, je pourrais stocker les données sous forme de série de paires clé/valeur comme ceci :

```js
localStorage.setItem('firstName', user.firstName);
localStorage.setItem('lastName', user.lastName);
localStorage.setItem('url', user.url);
```

Mais une meilleure façon est de convertir l'objet JavaScript en une chaîne JSON, puis de stocker les données sous une seule clé comme suit :

```js
const user = {
  firstName: 'Nathan',
  lastName: 'Sebhastian',
  url: 'https://codewithnathan.com',
};

const userData = JSON.stringify(user);

localStorage.setItem('user', userData);
```

Maintenant, le local storage n'aura qu'une seule paire clé/valeur avec la chaîne JSON comme valeur. Vous pouvez ouvrir l'onglet Applications pour voir cela :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/store-as-json.png)
_Stockage d'une chaîne JSON dans le Local Storage_

Lorsque vous avez besoin des données, appelez les méthodes `getItem()` et `JSON.parse()` comme suit :

```js
const getUser = JSON.parse(localStorage.getItem('user'));

console.log(getUser);
// {firstName: 'Nathan', lastName: 'Sebhastian', url: 'https://codewithnathan.com'}
```

Ici, vous pouvez voir que les données sont retournées sous forme d'objet JavaScript régulier.

## Local Storage vs Session Storage – Lequel utiliser ?

D'après mon expérience, `localStorage` est le mécanisme de stockage Web préféré car les données persisteront aussi longtemps que vous en aurez besoin. Lorsque vous n'avez plus besoin des données, vous pouvez les supprimer en utilisant la méthode `removeItem()`.

`sessionStorage` n'est utilisé que lorsque vous devez stocker des données temporaires, comme le suivi de l'affichage d'une boîte de dialogue à l'utilisateur ou non.

Mais cela est également ouvert à la discussion car vous ne souhaitez peut-être pas afficher une boîte de dialogue à chaque fois que l'utilisateur se connecte à votre application web, mais seulement une fois. Dans ce cas, vous devriez utiliser `localStorage` à la place.

Ma règle générale est d'utiliser `localStorage` en premier, et `sessionStorage` lorsque la situation l'exige.

## Avantages de l'utilisation de l'API Web Storage

Maintenant que vous savez comment fonctionne l'API Web Storage, vous pouvez voir qu'il y a certains avantages à l'utiliser :

1. Stocker des données dans le navigateur réduit le besoin de faire une requête serveur pour une information. Cela peut améliorer les performances de vos applications web.
2. Le format simple de paire clé/valeur vous permet de stocker les préférences de l'utilisateur et les paramètres locaux qui doivent persister entre les sessions.
3. L'API Web Storage est simple à utiliser, fournissant seulement quelques méthodes et une propriété. Il est simple de définir et de récupérer des données en utilisant JavaScript.
4. Elle a un support hors ligne. En stockant les données nécessaires localement, le Web Storage permet à votre application web de fonctionner hors ligne.
5. Le Web Storage est également une API standardisée, ce qui signifie que le code que vous écrivez fonctionnera dans de nombreux navigateurs différents.

Mais bien sûr, toutes les données ne doivent pas être stockées dans l'API Web Storage. Vous avez toujours besoin d'une base de données serveur pour conserver les enregistrements importants pour votre application.

## Conclusion

Le Web Storage est une API utile qui vous permet de stocker et de récupérer rapidement des données depuis le navigateur. En utilisant le Web Storage, vous pouvez stocker les préférences de l'utilisateur lors de l'accès à votre application.

`localStorage` vous permet de stocker des données pour toujours jusqu'à ce qu'elles soient supprimées manuellement, tandis que `sessionStorage` persistera tant que le navigateur ou l'onglet est ouvert.

Certains avantages de l'utilisation de l'API Web Storage incluent la réduction des requêtes serveur, le support hors ligne et une API simple qui est facile à utiliser. Elle est également standardisée, donc elle fonctionnera sur différents navigateurs.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://codewithnathan.com/beginning-modern-javascript).

[![](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://codewithnathan.com/beginning-modern-javascript)

Le livre est conçu pour être facile pour les débutants et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif qui vous aidera à comprendre comment utiliser JavaScript pour créer une application web dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À plus tard !