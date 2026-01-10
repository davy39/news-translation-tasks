---
title: Web Storage Expliqué – Comment utiliser localStorage et sessionStorage dans
  les projets JavaScript
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2023-10-09T16:45:31.000Z'
originalURL: https://freecodecamp.org/news/web-storage-localstorage-vs-sessionstorage-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/web-storage-explained-local-and-session-storage-objects-in-javascript-codesweetly.jpg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: storage
  slug: storage
- name: Web Development
  slug: web-development
seo_title: Web Storage Expliqué – Comment utiliser localStorage et sessionStorage
  dans les projets JavaScript
seo_desc: 'Web Storage is what the JavaScript API browsers provide for storing data
  locally and securely within a user’s browser.

  Session and local storage are the two main types of web storage. They are similar
  to regular properties objects, but they persist (...'
---

**Web Storage** est ce que les navigateurs fournissent via l'API JavaScript pour stocker des données localement et en toute sécurité dans le navigateur d'un utilisateur.

Session et local storage sont les deux principaux types de stockage web. Ils sont similaires aux objets propriétés réguliers, mais ils persistent (ne disparaissent pas) lorsque la page web se recharge.

Cet article vise à vous montrer exactement comment les deux objets de stockage fonctionnent en JavaScript. Nous utiliserons également un exercice de liste de tâches pour pratiquer l'utilisation du stockage web dans un projet d'application web.

## Table des matières

1. [Qu'est-ce que l'objet Session Storage ?](#heading-questce-que-lobjet-session-storage)
2. [Qu'est-ce que l'objet Local Storage ?](#heading-questce-que-lobjet-local-storage)
3. [Comment accéder aux objets Session et Local Storage](#heading-comment-acceder-aux-objets-session-et-local-storage)
4. [Quelles sont les interfaces intégrées du Web Storage ?](#heading-quelles-sont-les-interfaces-integrees-du-web-storage)
   - [Qu'est-ce que la méthode `setItem()` du web storage ?](#heading-questce-que-la-methode-setitem-du-web-storage)
   - [Qu'est-ce que la méthode `key()` du web storage ?](#heading-questce-que-la-methode-key-du-web-storage)
   - [Qu'est-ce que la méthode `getItem()` du web storage ?](#heading-questce-que-la-methode-getitem-du-web-storage)
   - [Qu'est-ce que la propriété `length` du web storage ?](#heading-questce-que-la-propriete-length-du-web-storage)
   - [Qu'est-ce que la méthode `removeItem()` du web storage ?](#heading-questce-que-la-methode-removeitem-du-web-storage)
   - [Qu'est-ce que la méthode `clear()` du web storage ?](#heading-questce-que-la-methode-clear-du-web-storage)
5. [Il est temps de pratiquer avec le Web Storage 🏃‍♂️🏀‍♀️](#heading-il-est-temps-de-pratiquer-avec-le-web-storage)
   - [Le Problème](#heading-le-probleme)
   - [Votre Exercice](#heading-votre-exercice)
   - [Exercice Bonus](#heading-exercice-bonus)
6. [Comment avez-vous abordé la résolution de l'exercice sur le Web Storage ?](#heading-comment-avez-vous-aborde-la-resolution-de-lexercice-sur-le-web-storage)
   - [Comment empêcher les éléments To-Do du panneau Session Storage de disparaître lors du rechargement de la page](#heading-comment-empecher-les-elements-to-do-du-panneau-session-storage-de-disparaitre-lors-du-rechargement-de-la-page)
   - [Comment empêcher les éléments To-Do du panneau Local Storage de disparaître lors du rechargement ou de la réouverture de la page](#heading-comment-empecher-les-elements-to-do-du-panneau-local-storage-de-disparaitre-lors-du-rechargement-ou-de-la-reouverture-de-la-page)
   - [Comment afficher automatiquement les tâches précédemment ajoutées de la section Session lors du rechargement de la page](#heading-comment-afficher-automatiquement-les-taches-precedemment-ajoutees-de-la-section-session-lors-du-rechargement-de-la-page)
   - [Comment afficher automatiquement les tâches précédemment ajoutées de la section Local lors du rechargement ou de la réouverture de la page](#heading-comment-afficher-automatiquement-les-taches-precedemment-ajoutees-de-la-section-local-lors-du-rechargement-ou-de-la-reouverture-de-la-page)
   - [Comment vérifier le nombre total d'éléments dans le session storage du navigateur](#heading-comment-verifier-le-nombre-total-delements-dans-le-session-storage-du-navigateur)
   - [Comment afficher le nom de l'élément d'index zéro du local storage](#heading-comment-afficher-le-nom-de-lelement-dindex-zero-du-local-storage)
   - [Comment vider le session storage du navigateur](#heading-comment-vider-le-session-storage-du-navigateur)
7. [Comment continuer à pratiquer avec le Web Storage 🧑‍💻🚀](#heading-comment-continuer-a-pratiquer-avec-le-web-storage)
8. [Web Storage vs. Cookies : Quelle est la différence ?](#heading-web-storage-vs-cookies-quelle-est-la-difference)
9. [Conclusion](#heading-conclusion)

Sans plus attendre, discutons du session storage.

## Qu'est-ce que l'objet Session Storage ?

L'objet session storage (`window.sessionStorage`) stocke des données qui persistent uniquement pour une session d'un onglet ouvert.

En d'autres termes, tout ce qui est stocké dans l'objet `window.sessionStorage` ne disparaîtra pas lors du rechargement de la page web. Au lieu de cela, l'ordinateur supprimera les données stockées uniquement lorsque les utilisateurs fermeront l'onglet ou la fenêtre du navigateur.

**Notez ce qui suit :**

* Les données stockées dans le session storage sont par [origine](https://developer.mozilla.org/en-US/docs/Glossary/Origin) et par instance. En d'autres termes, l'objet `sessionStorage` de `http://freecodecamp.com` est différent de l'objet `sessionStorage` de `https://freecodecamp.com` parce que les deux origines utilisent des [schémas](https://codesweetly.com/web-address-url#scheme) différents (`http` et `https`).
* Par instance signifie par fenêtre ou par onglet. En d'autres termes, la durée de vie de l'objet `sessionStorage` expire une fois que les utilisateurs ferment l'instance (fenêtre ou onglet).
* Les navigateurs créent une session de page unique pour chaque nouvel onglet ou fenêtre. Par conséquent, les utilisateurs peuvent exécuter plusieurs instances d'une application sans interférer avec le session storage de chaque instance. (Note : Les cookies ne prennent pas bien en charge l'exécution de plusieurs instances de la même application. Une telle tentative peut provoquer des erreurs telles que [double entrée de réservations](https://html.spec.whatwg.org/multipage/webstorage.html#introduction-15).)
* Le session storage est une propriété de l'objet global `Window`. Donc `sessionStorage.setItem()` est équivalent à `window.sessionStorage.setItem()`.

## Qu'est-ce que l'objet Local Storage ?

L'objet local storage (`window.localStorage`) stocke des données qui persistent même lorsque les utilisateurs ferment leur onglet de navigateur (ou fenêtre).

En d'autres termes, tout ce qui est stocké dans l'objet `window.localStorage` ne disparaîtra pas lors d'un rechargement ou d'une réouverture de la page web ou lorsque les utilisateurs ferment leurs navigateurs. Ces données n'ont pas de date d'expiration. Les navigateurs ne les effacent jamais automatiquement.

L'ordinateur supprimera le contenu de l'objet `window.localStorage` uniquement dans les cas suivants :

1. Lorsque le contenu est effacé via JavaScript
2. Lorsque le cache du navigateur est effacé

**Notez ce qui suit :**

* La limite de stockage de l'objet `window.localStorage` est plus grande que celle du `window.sessionStorage`.
* Les données stockées dans le local storage sont par [origine](https://developer.mozilla.org/en-US/docs/Glossary/Origin). En d'autres termes, l'objet `localStorage` de `http://freecodecamp.com` est différent de l'objet `localStorage` de `https://freecodecamp.com` parce que les deux origines utilisent des [schémas](https://codesweetly.com/web-address-url#scheme) différents (`http` et `https`).
* Il existe des incohérences dans la manière dont les navigateurs gèrent le stockage local des documents non servis à partir d'un serveur web (par exemple, les pages avec un schéma d'URL `file:`). Par conséquent, l'objet `localStorage` peut se comporter différemment selon les navigateurs lorsqu'il est utilisé avec des URL non-HTTP, telles que `file:///document/on/users/local/system.html`.
* Le local storage est une propriété de l'objet global `Window`. Par conséquent, `localStorage.setItem()` est équivalent à `window.localStorage.setItem()`.

## Comment accéder aux objets Session et Local Storage

Vous pouvez accéder aux deux stockages web en :

1. Utilisant la même technique que celle utilisée pour [accéder aux objets JavaScript réguliers](https://codesweetly.com/javascript-properties-object#how-to-access-an-objects-value)
2. Utilisant les interfaces intégrées du web storage

Par exemple, considérons l'extrait suivant :

```js
sessionStorage.bestColor = "Green";
sessionStorage["bestColor"] = "Green";
sessionStorage.setItem("bestColor", "Green");
```

Les trois instructions ci-dessus font la même chose—elles définissent la valeur de `bestColor`. Mais la troisième ligne est recommandée car elle utilise la méthode `setItem()` du web storage.

**Astuce :** vous devriez préférer utiliser les interfaces intégrées du web storage pour éviter [les pièges de l'utilisation d'objets comme magasins clé/valeur](https://2ality.com/2012/01/objects-as-maps.html).

Discutons davantage des interfaces intégrées du web storage ci-dessous.

## Quelles sont les interfaces intégrées du Web Storage ?

Les interfaces intégrées du web storage sont les outils recommandés pour lire et manipuler les objets `sessionStorage` et `localStorage` d'un navigateur.

Les six (6) interfaces intégrées sont :

* `setItem()`
* `key()`
* `getItem()`
* `length`
* `removeItem()`
* `clear()`

Discutons de chacune maintenant.

### Qu'est-ce que la méthode `setItem()` du web storage ?

La méthode `setItem()` stocke ses arguments `key` et `value` à l'intérieur de l'objet de stockage web spécifié.

#### Syntaxe de la méthode `setItem()`

`setItem()` accepte deux arguments requis. Voici la syntaxe :

```js
webStorageObject.setItem(key, value);
```

* `webStorageObject` représente l'objet de stockage (`localStorage` ou `sessionStorage`) que vous souhaitez manipuler.
* `key` est le premier argument accepté par `setItem()`. Il s'agit d'un argument de chaîne requis représentant le nom de la propriété de stockage web que vous souhaitez créer ou mettre à jour.
* `value` est le deuxième argument accepté par `setItem()`. Il s'agit d'un argument de chaîne requis spécifiant la valeur de la `key` que vous créez ou mettez à jour.

**Note :**

* Les arguments `key` et `value` sont toujours des chaînes.
* Supposons que vous fournissiez un entier comme `key` ou `value`. Dans ce cas, les navigateurs les convertiront en chaînes automatiquement.
* `setItem()` peut afficher un message d'erreur si l'objet de stockage est plein.

#### Exemple 1 : Comment stocker des données dans l'objet session storage

1. Invoquez la méthode `setItem()` de `sessionStorage`.
2. Fournissez le nom et la valeur des données que vous souhaitez stocker.

```js
// Stocker la couleur : "Pink" à l'intérieur de l'objet session storage du navigateur :
sessionStorage.setItem("color", "Pink");

// Journaliser l'objet session storage dans la console :
console.log(sessionStorage);

// L'invocation ci-dessus retournera :
{color: "Pink"}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/setitem/js-25hgkp)

**Note :** Votre session storage du navigateur peut contenir des données supplémentaires s'il utilise déjà l'objet de stockage pour stocker des informations.

#### Exemple 2 : Comment stocker des données dans l'objet local storage

1. Invoquez la méthode `setItem()` de `localStorage`.
2. Fournissez le nom et la valeur des données que vous souhaitez stocker.

```js
// Stocker la couleur : "Pink" à l'intérieur de l'objet local storage du navigateur :
localStorage.setItem("color", "Pink");

// Journaliser l'objet local storage dans la console :
console.log(localStorage);

// L'invocation ci-dessus retournera :
{color: "Pink"}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/setitem/js-2hluvw)

**Note :**

* Votre local storage du navigateur peut contenir des données supplémentaires s'il utilise déjà l'objet de stockage pour stocker des informations.
* Il est préférable de sérialiser les objets avant de les stocker dans le local ou session storage. Sinon, l'ordinateur stockera l'objet sous la forme `"[object Object]"`.

#### Exemple 3 : Les navigateurs utilisent `"[object Object]"` pour les objets non sérialisés dans le web storage

```js
// Stocker l'objet myBio à l'intérieur de l'objet session storage du navigateur :
sessionStorage.setItem("myBio", { name: "Oluwatobi" });

// Journaliser l'objet session storage dans la console :
console.log(sessionStorage);

// L'invocation ci-dessus retournera :
{myBio: "[object Object]", length: 1}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/setitem/js-n8m7hc)

Vous pouvez voir que l'ordinateur a stocké l'objet sous la forme `"[object Object]"` parce que nous ne l'avons pas sérialisé.

#### Exemple 4 : Comment stocker des objets sérialisés dans le web storage

```js
// Stocker l'objet myBio à l'intérieur de l'objet session storage du navigateur :
sessionStorage.setItem("myBio", JSON.stringify({ name: "Oluwatobi" }));

// Journaliser l'objet session storage dans la console :
console.log(sessionStorage);

// L'invocation ci-dessus retournera :
{myBio: '{"name":"Oluwatobi"}', length: 1}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/setitem/js-edfh43)

Nous avons utilisé `JSON.stringify()` pour convertir l'objet en JSON avant de le stocker dans le web storage.

**Astuce :** Apprenez [comment convertir JSON en objets JavaScript](https://codesweetly.com/json-explained#how-to-convert-a-json-text-to-a-javascript-object).

### Qu'est-ce que la méthode `key()` du web storage ?

La méthode `key()` récupère le nom (clé) d'un élément de stockage web spécifié.

#### Syntaxe de la méthode `key()`

`key()` accepte un argument requis. Voici la syntaxe :

```js
webStorageObject.key(index);
```

* `webStorageObject` représente l'objet de stockage (`localStorage` ou `sessionStorage`) dont vous souhaitez obtenir la clé.
* `index` est un argument requis. Il s'agit d'un [entier](https://codesweetly.com/web-tech-terms-i#integer) spécifiant l'[index](https://codesweetly.com/web-tech-terms-i#index) de l'élément dont vous souhaitez obtenir la clé.

#### Exemple 1 : Comment obtenir le nom d'un élément dans l'objet session storage

1. Invoquez la méthode `key()` de `sessionStorage`.
2. Fournissez l'index de l'élément dont vous souhaitez obtenir le nom.

```js
// Stocker carColor : "Pink" à l'intérieur de l'objet session storage du navigateur :
sessionStorage.setItem("carColor", "Pink");

// Stocker pcColor : "Yellow" à l'intérieur de l'objet session storage :
sessionStorage.setItem("pcColor", "Yellow");

// Stocker laptopColor : "White" à l'intérieur de l'objet session storage :
sessionStorage.setItem("laptopColor", "White");

// Obtenir le nom de l'élément à l'index 1 :
sessionStorage.key(1);
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/key/js-tptqtg)

**Important :** L'[agent utilisateur](https://en.wikipedia.org/wiki/User_agent) définit l'ordre des éléments dans le session storage. En d'autres termes, la sortie de `key()` peut varier en fonction de la manière dont l'agent utilisateur ordonne les éléments du web storage. Vous ne devriez donc pas vous fier à `key()` pour retourner une valeur constante.

#### Exemple 2 : Comment obtenir le nom d'un élément dans l'objet local storage

1. Invoquez la méthode `key()` de `localStorage`.
2. Fournissez l'index de l'élément dont vous souhaitez obtenir le nom.

```js
// Stocker carColor : "Pink" à l'intérieur de l'objet local storage du navigateur :
localStorage.setItem("carColor", "Pink");

// Stocker pcColor : "Yellow" à l'intérieur de l'objet local storage :
localStorage.setItem("pcColor", "Yellow");

// Stocker laptopColor : "White" à l'intérieur de l'objet local storage :
localStorage.setItem("laptopColor", "White");

// Obtenir le nom de l'élément à l'index 1 :
localStorage.key(1);
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/key/js-tclrbd)

**Important :** L'agent utilisateur définit l'ordre des éléments dans le local storage. En d'autres termes, la sortie de `key()` peut varier en fonction de la manière dont l'agent utilisateur ordonne les éléments du web storage. Vous ne devriez donc pas vous fier à `key()` pour retourner une valeur constante.

### Qu'est-ce que la méthode `getItem()` du web storage ?

La méthode `getItem()` récupère la valeur d'un élément de stockage web spécifié.

#### Syntaxe de la méthode `getItem()`

`getItem()` accepte un argument requis. Voici la syntaxe :

```js
webStorageObject.getItem(key);
```

* `webStorageObject` représente l'objet de stockage (`localStorage` ou `sessionStorage`) dont vous souhaitez obtenir l'élément.
* `key` est un argument requis. Il s'agit d'une [chaîne](https://codesweetly.com/javascript-primitive-data-type#string-primitive-data-type) spécifiant le nom de la [propriété](https://codesweetly.com/javascript-properties-object#syntax-of-a-javascript-object) de stockage web dont vous souhaitez obtenir la valeur.

#### Exemple 1 : Comment obtenir des données de l'objet session storage

1. Invoquez la méthode `getItem()` de `sessionStorage`.
2. Fournissez le nom des données que vous souhaitez obtenir.

```js
// Stocker la couleur : "Pink" à l'intérieur de l'objet session storage du navigateur :
sessionStorage.setItem("color", "Pink");

// Obtenir la valeur de la couleur à partir du session storage :
sessionStorage.getItem("color");

// L'invocation ci-dessus retournera :
"Pink"
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/getitem/js-xk9auv)

#### Exemple 2 : Comment obtenir des données de l'objet local storage

1. Invoquez la méthode `getItem()` de `localStorage`.
2. Fournissez le nom des données que vous souhaitez obtenir.

```js
// Stocker la couleur : "Pink" à l'intérieur de l'objet local storage du navigateur :
localStorage.setItem("color", "Pink");

// Obtenir la valeur de la couleur à partir du local storage :
localStorage.getItem("color");

// L'invocation ci-dessus retournera :
"Pink"
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/getitem/js-terw5e)

**Note :** La méthode `getItem()` retournera `null` si son argument n'existe pas dans le web storage spécifié.

### Qu'est-ce que la propriété `length` du web storage ?

La propriété `length` retourne le nombre de [propriétés](https://codesweetly.com/javascript-properties-object#syntax-of-a-javascript-object) dans le web storage spécifié.

#### Syntaxe de la propriété `length`

Voici la syntaxe de `length` :

```js
webStorageObject.length;
```

`webStorageObject` représente l'objet de stockage (`localStorage` ou `sessionStorage`) dont vous souhaitez vérifier la longueur.

#### Exemple 1 : Comment vérifier le nombre d'éléments dans l'objet session storage

Invoquez la propriété `length` de `sessionStorage`.

```js
// Stocker carColor : "Pink" à l'intérieur de l'objet session storage du navigateur :
sessionStorage.setItem("carColor", "Pink");

// Stocker pcColor : "Yellow" à l'intérieur de l'objet session storage :
sessionStorage.setItem("pcColor", "Yellow");

// Stocker laptopColor : "White" à l'intérieur de l'objet session storage :
sessionStorage.setItem("laptopColor", "White");

// Vérifier le nombre d'éléments dans le session storage :
sessionStorage.length;

// L'invocation ci-dessus peut retourner :
3
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/length/js-zasgst)

**Note :** Votre invocation `sessionStorage.length` peut retourner une valeur supérieure à `3` si votre session storage du navigateur contient déjà des informations stockées.

#### Exemple 2 : Comment vérifier le nombre d'éléments dans l'objet local storage

Invoquez la propriété `length` de `localStorage`.

```js
// Stocker carColor : "Pink" à l'intérieur de l'objet local storage du navigateur :
localStorage.setItem("carColor", "Pink");

// Stocker pcColor : "Yellow" à l'intérieur de l'objet local storage :
localStorage.setItem("pcColor", "Yellow");

// Stocker laptopColor : "White" à l'intérieur de l'objet local storage :
localStorage.setItem("laptopColor", "White");

// Vérifier le nombre d'éléments dans le local storage :
localStorage.length;

// L'invocation ci-dessus peut retourner :
3
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/length/js-3f6lac)

**Note :** Votre invocation `localStorage.length` peut retourner une valeur supérieure à `3` si votre local storage du navigateur contient déjà des informations stockées.

### Qu'est-ce que la méthode `removeItem()` du web storage ?

La méthode `removeItem()` supprime une propriété du web storage spécifié.

#### Syntaxe de la méthode `removeItem()`

`removeItem()` accepte un argument requis. Voici la syntaxe :

```js
webStorageObject.removeItem(key);
```

* `webStorageObject` représente l'objet de stockage (`localStorage` ou `sessionStorage`) dont vous souhaitez supprimer l'élément.
* `key` est un argument requis. Il s'agit d'une chaîne spécifiant le nom de la propriété de stockage web que vous souhaitez supprimer.

#### Exemple 1 : Comment supprimer des données de l'objet session storage

1. Invoquez la méthode `removeItem()` de `sessionStorage`.
2. Fournissez le nom des données que vous souhaitez supprimer.

```js
// Stocker carColor : "Pink" à l'intérieur de l'objet session storage du navigateur :
sessionStorage.setItem("carColor", "Pink");

// Stocker pcColor : "Yellow" à l'intérieur de l'objet session storage :
sessionStorage.setItem("pcColor", "Yellow");

// Stocker laptopColor : "White" à l'intérieur de l'objet session storage :
sessionStorage.setItem("laptopColor", "White");

// Supprimer l'élément pcColor du session storage :
sessionStorage.removeItem("pcColor");

// Confirmer si l'élément pcColor existe toujours dans le session storage :
sessionStorage.getItem("pcColor");

// L'invocation ci-dessus retournera :
null
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/removeitem/js-1mywnh)

**Note :** La méthode `removeItem()` ne fera rien si son argument n'existe pas dans le session storage.

#### Exemple 2 : Comment supprimer des données de l'objet local storage

1. Invoquez la méthode `removeItem()` de `localStorage`.
2. Fournissez le nom des données que vous souhaitez supprimer.

```js
// Stocker carColor : "Pink" à l'intérieur de l'objet local storage du navigateur :
localStorage.setItem("carColor", "Pink");

// Stocker pcColor : "Yellow" à l'intérieur de l'objet local storage :
localStorage.setItem("pcColor", "Yellow");

// Stocker laptopColor : "White" à l'intérieur de l'objet local storage :
localStorage.setItem("laptopColor", "White");

// Supprimer l'élément pcColor du local storage :
localStorage.removeItem("pcColor");

// Confirmer si l'élément pcColor existe toujours dans le local storage :
localStorage.getItem("pcColor");

// L'invocation ci-dessus retournera :
null
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/removeitem/js-8doou3)

**Note :** La méthode `removeItem()` ne fera rien si son argument n'existe pas dans le local storage.

### Qu'est-ce que la méthode `clear()` du web storage ?

La méthode `clear()` efface (supprime) tous les éléments du web storage spécifié.

#### Syntaxe de la méthode `clear()`

`clear()` n'accepte aucun argument. Voici la syntaxe :

```js
webStorageObject.clear();
```

`webStorageObject` représente l'objet de stockage (`localStorage` ou `sessionStorage`) dont vous souhaitez effacer les éléments.

#### Exemple 1 : Comment effacer tous les éléments de l'objet session storage

Invoquez la méthode `clear()` de `sessionStorage`.

```js
// Stocker carColor : "Pink" à l'intérieur de l'objet session storage du navigateur :
sessionStorage.setItem("carColor", "Pink");

// Stocker pcColor : "Yellow" à l'intérieur de l'objet session storage :
sessionStorage.setItem("pcColor", "Yellow");

// Stocker laptopColor : "White" à l'intérieur de l'objet session storage :
sessionStorage.setItem("laptopColor", "White");

// Effacer tous les éléments du session storage :
sessionStorage.clear();

// Confirmer si le session storage contient encore des éléments :
console.log(sessionStorage);

// L'invocation ci-dessus retournera :
{length: 0}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/clear/js-an86yu)

#### Exemple 2 : Comment effacer tous les éléments de l'objet local storage

Invoquez la méthode `clear()` de `localStorage`.

```js
// Stocker carColor : "Pink" à l'intérieur de l'objet local storage du navigateur :
localStorage.setItem("carColor", "Pink");

// Stocker pcColor : "Yellow" à l'intérieur de l'objet local storage :
localStorage.setItem("pcColor", "Yellow");

// Stocker laptopColor : "White" à l'intérieur de l'objet local storage :
localStorage.setItem("laptopColor", "White");

// Effacer tous les éléments du local storage :
localStorage.clear();

// Confirmer si le local storage contient encore des éléments :
console.log(localStorage);

// L'invocation ci-dessus retournera :
{length: 0}
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/clear/js-w5vyem)

Maintenant que nous savons ce qu'est le web storage et comment y accéder, nous pouvons pratiquer son utilisation dans un projet JavaScript.

## Il est temps de pratiquer avec le Web Storage 🏃‍♂️🏀‍♀️

Considérez l'application de liste de tâches suivante :

%[https://www.youtube.com/watch?v=78MRup0PN7c]

### Le Problème

Le problème avec l'[application de liste de tâches](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-mgl6ie) est le suivant :

* Les tâches disparaissent chaque fois que les utilisateurs actualisent la page web.

### Votre Exercice

Utilisez les API de Web Storage appropriées pour accomplir les tâches suivantes :

1. Empêcher les éléments To-Do du panneau Session de disparaître chaque fois que les utilisateurs rechargent le navigateur.
2. Empêcher les éléments To-Do de la section Local de disparaître chaque fois que les utilisateurs rechargent ou ferment leur onglet de navigateur (ou fenêtre).
3. Afficher automatiquement les tâches précédemment ajoutées de la section Session lors du rechargement de la page.
4. Afficher automatiquement les tâches précédemment ajoutées de la section Local lors du rechargement de la page (ou de la réouverture du navigateur).

### Exercice Bonus

Utilisez la console de votre navigateur pour :

1. Vérifier le nombre d'éléments dans l'objet session storage de votre navigateur.
2. Afficher le nom de l'élément d'index zéro de votre local storage.
3. Supprimer tous les éléments du session storage de votre navigateur.

[**Essayez l'exercice sur le Web Storage**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-mgl6ie)

**Note :** Vous bénéficierez beaucoup plus de ce tutoriel si vous essayez l'exercice vous-même.

Si vous êtes bloqué, ne vous découragez pas. Au lieu de cela, révisez la leçon et essayez à nouveau.

Une fois que vous avez donné le meilleur de vous-même (vous ne vous trompez que vous-même si vous ne le faites pas !), nous pouvons discuter de la manière dont j'ai abordé l'exercice ci-dessous.

## Comment avez-vous abordé la résolution de l'exercice sur le Web Storage ?

Voici des moyens réalisables de réaliser l'exercice.

### Comment empêcher les éléments To-Do du panneau Session Storage de disparaître lors du rechargement de la page

Chaque fois que les utilisateurs cliquent sur le bouton "Ajouter une tâche",

1. Obtenez le contenu existant du session storage, le cas échéant. Sinon, retournez un tableau vide.
2. Fusionnez les éléments de la liste de tâches existants avec la nouvelle entrée de l'utilisateur.
3. Ajoutez la nouvelle liste de tâches à l'objet session storage du navigateur.

**Voici le code :**

```js
sessionAddTaskBtn.addEventListener('click', () => {
  // Obtenez le contenu existant du session storage, le cas échéant. Sinon, retournez un tableau vide :
  const currentTodoArray =
    JSON.parse(sessionStorage.getItem('codesweetlyStore')) || [];

  // Fusionnez currentTodoArray avec la nouvelle entrée de l'utilisateur :
  const newTodoArray = [
    ...currentTodoArray,
    { checked: false, text: sessionInputEle.value },
  ];

  // Ajoutez newTodoArray à l'objet session storage :
  sessionStorage.setItem('codesweetlyStore', JSON.stringify(newTodoArray));

  const todoLiElements = createTodoLiElements(newTodoArray);
  sessionTodosContainer.replaceChildren(...todoLiElements);
  sessionInputEle.value = '';
});
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-txyt66)

**Note :** Les trois points (`...`) précédant la variable `currentTodoArray` représentent l'[opérateur de décomposition](https://codesweetly.com/spread-operator). Nous l'avons utilisé dans l'objet `newTodoArray` pour copier les éléments de `currentTodoArray` dans `newTodoArray`.

### Comment empêcher les éléments To-Do du panneau Local Storage de disparaître lors du rechargement ou de la réouverture de la page

1. Obtenez le contenu existant du local storage, le cas échéant. Sinon, retournez un tableau vide.
2. Fusionnez les éléments de la liste de tâches existants avec la nouvelle entrée de l'utilisateur.
3. Ajoutez la nouvelle liste de tâches à l'objet local storage du navigateur.

**Voici le code :**

```js
localAddTaskBtn.addEventListener('click', () => {
  // Obtenez le contenu existant du local storage, le cas échéant. Sinon, retournez un tableau vide :
  const currentTodoArray =
    JSON.parse(localStorage.getItem('codesweetlyStore')) || [];

  // Fusionnez currentTodoArray avec la nouvelle entrée de l'utilisateur :
  const newTodoArray = [
    ...currentTodoArray,
    { checked: false, text: localInputEle.value },
  ];

  // Ajoutez newTodoArray à l'objet local storage :
  sessionStorage.setItem('codesweetlyStore', JSON.stringify(newTodoArray));

  const todoLiElements = createTodoLiElements(newTodoArray);
  localTodosContainer.replaceChildren(...todoLiElements);
  localInputEle.value = '';
});
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-dpuffp)

**Note :** L'instruction `localTodosContainer.replaceChildren(...todoLiElements)` indique au navigateur de remplacer les éléments enfants actuels de `localTodosContainer` par la liste des `<li>` dans le tableau `todoLiElements`.

### Comment afficher automatiquement les tâches précédemment ajoutées de la section Session lors du rechargement de la page

Chaque fois que les utilisateurs rechargent la page,

1. Obtenez le contenu existant du session storage, le cas échéant. Sinon, retournez un tableau vide.
2. Utilisez le contenu récupéré pour créer des éléments `<li>`.
3. Remplissez l'espace d'affichage des tâches avec les éléments `<li>`.

**Voici le code :**

```js
window.addEventListener('load', () => {
  // Obtenez le contenu existant du session storage, le cas échéant. Sinon, retournez un tableau vide :
  const sessionTodoArray =
    JSON.parse(sessionStorage.getItem('codesweetlyStore')) || [];

  // Utilisez le sessionTodoArray récupéré pour créer des éléments <li> :
  const todoLiElements = createTodoLiElements(sessionTodoArray);

  // Remplissez l'espace d'affichage des tâches avec les todoLiElements :
  sessionTodosContainer.replaceChildren(...todoLiElements);
});
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-zga551)

### Comment afficher automatiquement les tâches précédemment ajoutées de la section Local lors du rechargement ou de la réouverture de la page

Chaque fois que les utilisateurs rechargent ou rouvrent la page,

1. Obtenez le contenu existant du local storage, le cas échéant. Sinon, retournez un tableau vide.
2. Utilisez le contenu récupéré pour créer des éléments `<li>`.
3. Remplissez l'espace d'affichage des tâches avec les éléments `<li>`.

**Voici le code :**

```js
window.addEventListener('load', () => {
  // Obtenez le contenu existant du local storage, le cas échéant. Sinon, retournez un tableau vide :
  const localTodoArray =
    JSON.parse(localStorage.getItem('codesweetlyStore')) || [];

  // Utilisez le localTodoArray récupéré pour créer des éléments <li> :
  const todoLiElements = createTodoLiElements(localTodoArray);

  // Remplissez l'espace d'affichage des tâches avec les todoLiElements :
  localTodosContainer.replaceChildren(...todoLiElements);
});
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-srmnst)

### Comment vérifier le nombre total d'éléments dans le session storage du navigateur

Utilisez la propriété `length` du session storage comme suit :

```js
console.log(sessionStorage.length);
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-m4pmhf)

### Comment afficher le nom de l'élément d'index zéro du local storage

Utilisez la méthode `key()` du local storage comme suit :

```js
console.log(localStorage.key(0));
```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-th8xr7)

### Comment vider le session storage du navigateur

Utilisez la méthode `clear()` du session storage comme suit :

```js
sessionStorage.clear();
```

## Comment continuer à pratiquer avec le Web Storage 🧑‍💻🚀

L'application de liste de tâches a encore beaucoup de potentiel. Par exemple, vous pouvez :

* La convertir en une application React TypeScript.
* La rendre accessible au clavier.
* Permettre aux utilisateurs de supprimer ou de modifier des tâches individuelles.
* Permettre aux utilisateurs de marquer des tâches spécifiques comme importantes.
* Laisser les utilisateurs spécifier des dates d'échéance.

Alors, n'hésitez pas à continuer à développer ce que nous avons construit dans ce tutoriel afin de mieux comprendre les objets de stockage web.

Par exemple, voici ma tentative de [rendre les deux panneaux fonctionnels](https://codesweetly.com/try-it-sdk/javascript/web-storage-apis/to-do-app/js-ax8tvk) :

%[https://youtu.be/gDiU-ubWPD4]

Avant de conclure notre discussion, vous devriez connaître certaines différences entre le web storage et les cookies. Alors, parlons-en ci-dessous.

## Web Storage vs. Cookies : Quelle est la différence ?

Le web storage et les cookies sont deux principales façons de stocker des données localement dans le navigateur d'un utilisateur. Mais ils fonctionnent différemment. Voici les principales distinctions entre eux.

### Limite de stockage

**Cookies :** Ont une limite de stockage maximale de 4 kilooctets.

**Web storage :** Peut stocker beaucoup plus que 4 kilooctets de données. Par exemple, Safari 8 peut stocker jusqu'à 5 Mo, tandis que Firefox 34 permet 10 Mo.

### Transfert de données vers le serveur

**Cookies :** Transfèrent les données vers le serveur chaque fois que les navigateurs envoient des requêtes HTTP au serveur web.

**Web storage :** Ne transfèrent jamais les données vers le serveur.

**Note :** C'est une perte de bande passante des utilisateurs d'envoyer des données au serveur si ces informations sont nécessaires uniquement par le client (navigateur), et non par le serveur.

### Faible intégrité et confidentialité

**Cookies :** Souffrent de problèmes de [faible intégrité](https://datatracker.ietf.org/doc/html/rfc6265#section-8.6) et de [faible confidentialité](https://datatracker.ietf.org/doc/html/rfc6265#section-8.5).

**Web storage :** Ne souffrent pas de problèmes de faible intégrité et de confidentialité car ils stockent les données par [origine](https://developer.mozilla.org/en-US/docs/Glossary/Origin).

### Propriété

**Cookies :** Les cookies sont une propriété de l'objet [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document).

**Web storage :** Le web storage est une propriété de l'objet [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window).

### Expiration

**Cookie :** Vous pouvez spécifier une date d'expiration pour un cookie.

**Web storage :** Les navigateurs déterminent la date d'expiration du web storage.

### Récupération de données individuelles

**Cookies :** Il n'y a aucun moyen de récupérer des données individuelles. Vous devez toujours rappeler toutes les données pour lire une seule.

**Web storage :** Vous pouvez choisir les données spécifiques que vous souhaitez récupérer.

### La syntaxe pour stocker des données

**Cookies :**

```js
document.cookie = "key=value";
```

**Web storage :**

```js
webStorageObject.setItem(key, value);
```

### La syntaxe pour lire des données

**Cookies :**

```js
document.cookie;
```

**Web storage :**

```js
webStorageObject.getItem(key);
```

### La syntaxe pour supprimer des données

**Cookies :**

```js
document.cookie = "key=; expires=Thu, 01 May 1930 00:00:00 UTC";
```

L'extrait ci-dessus supprime le cookie en attribuant une valeur vide à la propriété `key` et en définissant une date d'expiration passée.

**Web storage :**

```js
webStorageObject.removeItem(key);
```

## Conclusion

Dans cet article, nous avons discuté de la manière d'utiliser le web storage et ses interfaces intégrées. Nous avons également utilisé un projet de liste de tâches pour pratiquer l'utilisation des objets local et session storage afin de stocker des données localement et en toute sécurité dans les navigateurs des utilisateurs.

Merci d'avoir lu !

### Et voici une ressource utile sur React TypeScript :

J'ai écrit un livre sur la [Création de paquets NPM](https://amzn.to/3Pa4bI4) !

C'est un livre adapté aux débutants qui vous guide de zéro à la création, au test et à la publication de paquets NPM comme un pro.

[![Livre sur la création de paquets NPM maintenant disponible sur Amazon](https://www.freecodecamp.org/news/content/images/2023/09/creating-npm-package-banner-codesweetly.png)](https://amzn.to/3Pa4bI4)