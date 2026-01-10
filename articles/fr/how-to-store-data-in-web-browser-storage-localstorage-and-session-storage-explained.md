---
title: Comment stocker des données dans le stockage du navigateur web - localStorage
  et sessionStorage expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-store-data-in-web-browser-storage-localstorage-and-session-storage-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d02740569d1a4ca3567.jpg
tags:
- name: Browsers
  slug: browsers
- name: storage
  slug: storage
- name: toothbrush
  slug: toothbrush
seo_title: Comment stocker des données dans le stockage du navigateur web - localStorage
  et sessionStorage expliqués
seo_desc: In order to manage data handled by your web application, you do not necessarily
  need a database. The respective Browser Storage features are supported by Chrome
  (version 4 and higher), Mozilla Firefox (version 3.5 and higher) and Internet Explorer
  (v...
---

Afin de gérer les données traitées par votre application web, vous n'avez pas nécessairement besoin d'une base de données. Les fonctionnalités de stockage du navigateur respectives sont supportées par Chrome (version 4 et supérieure), Mozilla Firefox (version 3.5 et supérieure) et Internet Explorer (version 8 et supérieure), ainsi qu'une gamme d'autres navigateurs, y compris ceux d'iOS et d'Android.

Il existe deux principales possibilités pour le stockage dans le navigateur : localStorage et sessionStorage.

## **localStorage**

Tout contenu/donnée enregistré dans l'objet `localStorage` sera disponible après le redémarrage du navigateur (fermeture et réouverture). Afin d'**_enregistrer un élément_** dans `localStorage`, vous pouvez utiliser la méthode `setItem()`. Cette méthode doit recevoir une clé et une valeur.

```text
Exemple : localStorage.setItem("mykey","myvalue");
```

Pour **_récupérer l'élément du localStorage_**, la méthode `getItem` doit être utilisée. La méthode `getItem` doit recevoir la clé des données que vous souhaitez récupérer :

```text
  Exemple : localStorage.getItem("mykey");
```

Vous pouvez supprimer un élément de `localStorage` en utilisant la méthode `removeItem()`. Cette méthode doit recevoir la clé de l'élément à supprimer :

```text
  Exemple : localStorage.removeItem("mykey");
```

Pour effacer entièrement le `localStorage`, vous devez utiliser la méthode `clear()` sur l'objet `localStorage` :

```text
  Exemple : localStorage.clear();
```

## **sessionStorage**

Les éléments enregistrés dans l'objet `sessionStorage` resteront jusqu'à ce que le navigateur soit fermé par l'utilisateur. Ensuite, le stockage sera effacé.

Vous pouvez enregistrer un élément dans `sessionStorage`, veuillez utiliser la méthode `setItem()` sur l'objet `sessionStorage` :

```text
Exemple : sessionStorage.setItem("mykey","myvalue");
```

Pour **_récupérer l'élément du sessionStorage_**, la méthode `getItem` doit être utilisée. La méthode `getItem` doit recevoir la clé des données que vous souhaitez récupérer :

```text
  Exemple : sessionStorage.getItem("mykey");
```

Vous pouvez supprimer un élément de `sessionStorage` en utilisant la méthode `removeItem()`. Cette méthode doit recevoir la clé de l'élément à supprimer :

```text
  Exemple : sessionStorage.removeItem("mykey");
```

Pour effacer entièrement le `sessionStorage`, vous devez utiliser la méthode `clear()` sur l'objet `sessionStorage` :

```text
  Exemple : sessionStorage.clear();
```

## **Enregistrer des tableaux dans localStorage et sessionStorage**

Vous ne pouvez pas seulement enregistrer des valeurs uniques dans `localStorage` et `sessionStorage`, mais vous pouvez également enregistrer le contenu d'un tableau.

Dans cet exemple, nous avons un tableau avec des nombres :

```text
var ourArray =[1,2,3,4,5];
```

Nous pouvons maintenant l'enregistrer dans `localStorage` ou `sessionStorage` en utilisant la méthode `setItem()` :

```text
localStorage.setItem("ourarraykey",JSON.stringify(ourArray));
```

ou, pour `sessionStorage` :

```text
sessionStorage.setItem("ourarraykey",JSON.stringify(ourArray));
```

Afin d'être enregistré, le tableau doit d'abord être converti en une chaîne de caractères. Dans l'exemple montré ci-dessus, nous utilisons la méthode `JSON.stringify` pour accomplir cela.

Lors de la récupération de nos données depuis `localStorage` ou `sessionStorage`, convertissez-les à nouveau en un tableau :

```text
var storedArray = localStorage.getItem("ourarraykey");
ourArray = JSON.parse(storedArray);
```

ou, pour `sessionStorage` :

```text
var storedArray = sessionStorage.getItem("ourarraykey");
ourArray = JSON.parse(storedArray);
```