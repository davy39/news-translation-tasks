---
title: Un guide rapide mais complet sur IndexedDB et le stockage de données dans les
  navigateurs
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2019-06-01T11:07:00.000Z'
originalURL: https://freecodecamp.org/news/a-quick-but-complete-guide-to-indexeddb-25f030425501
coverImage: https://cdn-media-1.freecodecamp.org/images/1*p6r6gML9zfQ0MlNx7IWx_A.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Un guide rapide mais complet sur IndexedDB et le stockage de données dans
  les navigateurs
seo_desc: 'Interested in learning JavaScript? Get my JavaScript ebook at jshandbook.com


  Introduction to IndexedDB

  IndexedDB is one of the storage capabilities introduced into browsers over the years.

  It''s a key/value store (a noSQL database) considered to be t...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook JavaScript sur [jshandbook.com](https://jshandbook.com/)


## Introduction à IndexedDB

IndexedDB est l'une des capacités de stockage introduites dans les navigateurs au fil des ans.
C'est un magasin clé/valeur (une base de données noSQL) considérée comme **la solution définitive pour stocker des données dans les navigateurs**.

Il s'agit d'une API asynchrone, ce qui signifie que l'exécution d'opérations coûteuses ne bloquera pas le thread de l'interface utilisateur, offrant ainsi une expérience fluide aux utilisateurs. Elle peut stocker une quantité indéfinie de données, bien que, une fois un certain seuil dépassé, l'utilisateur soit invité à accorder au site des limites plus élevées.

Elle est [prise en charge par tous les navigateurs modernes](http://caniuse.com/#feat=indexeddb).

Elle prend en charge les transactions, la gestion des versions et offre de bonnes performances.

Dans le navigateur, nous pouvons également utiliser :

- [**Cookies**](https://flaviocopes.com/cookies/) : peuvent héberger une très petite quantité de chaînes
- [**Web Storage**](https://flaviocopes.com/web-storage-api/) (ou DOM Storage), un terme qui identifie communément localStorage et sessionStorage, deux magasins clé/valeur. sessionStorage ne conserve pas les données, qui sont effacées lorsque la session se termine, tandis que localStorage conserve les données entre les sessions.

Local/session storage ont l'inconvénient d'être limités à une taille petite (et inconsistante), avec les implémentations des navigateurs offrant de 2 Mo à 10 Mo d'espace par site.

Dans le passé, nous avions également **Web SQL**, un wrapper autour de SQLite, mais maintenant cela est **obsolète** et non pris en charge sur certains navigateurs modernes. Ce n'a jamais été une norme reconnue et ne devrait donc pas être utilisé, bien que 83 % des utilisateurs aient cette technologie sur leurs appareils [selon Can I Use](http://caniuse.com/#feat=sql-storage).

Bien que vous puissiez techniquement créer plusieurs bases de données par site, vous créez généralement **une seule base de données**, et à l'intérieur de cette base de données, vous pouvez créer **plusieurs magasins d'objets**.

Une base de données est **privée à un domaine**, donc aucun autre site ne peut accéder aux magasins IndexedDB d'un autre site.

Chaque magasin contient généralement un ensemble de _choses_, qui peuvent être :

- chaînes de caractères
- nombres
- objets
- tableaux
- dates

> Par exemple, vous pouvez avoir un magasin qui contient des publications, un autre qui contient des commentaires.

Un magasin contient un certain nombre d'éléments qui ont une clé unique, qui représente la manière dont un objet peut être identifié.

Vous pouvez modifier ces magasins en utilisant des transactions, en effectuant des opérations d'ajout, de modification et de suppression, et en itérant sur les éléments qu'ils contiennent.

Depuis l'avènement des [Promesses](https://flaviocopes.com/javascript-promises) dans ES6, et le passage ultérieur des API à l'utilisation des promesses, l'API IndexedDB semble un peu _old school_.

Bien qu'il n'y ait rien de mal à cela, dans tous les exemples que je vais expliquer, j'utiliserai la [IndexedDB Promised Library](https://github.com/jakearchibald/idb) de Jake Archibald, qui est une petite couche au-dessus de l'API IndexedDB pour la rendre plus facile à utiliser.

> Cette bibliothèque est également utilisée dans tous les exemples sur le site des développeurs Google concernant IndexedDB.

## Créer une base de données IndexedDB

La manière la plus simple est d'utiliser *unpkg*, en ajoutant ceci à l'en-tête de la page :

```html
<script type="module">
import { openDB, deleteDB } from 'https://unpkg.com/idb?module'
</script>
```

Avant d'utiliser l'API IndexedDB, assurez-vous toujours de vérifier la prise en charge dans le navigateur, même si elle est largement disponible, on ne sait jamais quel navigateur l'utilisateur utilise :

```js
(() => {
  'use strict'

  if (!('indexedDB' in window)) {
    console.warn('IndexedDB non supporté')
    return
  }

  //...Code IndexedDB
})()
```

### Comment **créer une base de données**

En utilisant `openDB()` :

```js
(async () => {
  //...

  const dbName = 'mydbname'
  const storeName = 'store1'
  const version = 1 // les versions commencent à 1

  const db = await openDB(dbName, version, {
    upgrade(db, oldVersion, newVersion, transaction) {
      const store = db.createObjectStore(storeName)
    }
  })
})()
```

Les deux premiers paramètres sont le nom de la base de données et la version. Le troisième paramètre, qui est optionnel, est un objet qui contient une fonction **appelée uniquement si le numéro de version est supérieur à la version actuellement installée de la base de données**. Dans le corps de la fonction, vous pouvez mettre à niveau la structure (magasins et index) de la base de données.

## Ajouter des données dans un magasin

### Ajouter des données lors de la création du magasin, l'initialiser

Vous utilisez la méthode `put` du magasin d'objets, mais vous avez d'abord besoin d'une référence à celui-ci, que vous pouvez obtenir à partir de `db.createObjectStore()` lorsque vous le créez.

Lorsque vous utilisez `put`, la valeur est le premier argument, la clé est le second. Cela est dû au fait que si vous spécifiez `keyPath` lors de la création du magasin d'objets, vous n'avez pas besoin d'entrer le nom de la clé à chaque demande de put(), vous pouvez simplement écrire la valeur.

Cela remplit `store0` dès que nous le créons :

```js
(async () => {
  //...
  const dbName = 'mydbname'
  const storeName = 'store0'
  const version = 1

  const db = await openDB(dbName, version,{
    upgrade(db, oldVersion, newVersion, transaction) {
      const store = db.createObjectStore(storeName)
      store.put('Hello world!', 'Hello')
    }
  })
})()
```

### Ajouter des données lorsque le magasin est déjà créé, en utilisant des transactions

Pour ajouter des éléments plus tard, vous devez créer une transaction de lecture/écriture, qui garantit l'intégrité de la base de données (si une opération échoue, toutes les opérations de la transaction sont annulées et l'état revient à un état connu).

Pour cela, utilisez une référence à l'objet `dbPromise` que nous avons obtenu lors de l'appel à `openDB`, et exécutez :

```js
(async () => {
  //...
  const dbName = 'mydbname'
  const storeName = 'store0'
  const version = 1

  const db = await openDB(/* ... */)

  const tx = db.transaction(storeName, 'readwrite')
  const store = await tx.objectStore(storeName)

  const val = 'hey!'
  const key = 'Hello again'
  const value = await store.put(val, key)
  await tx.done
})()
```


## Obtenir des données à partir d'un magasin

### Obtenir un élément d'un magasin : `get()`

```js
const key = 'Hello again'
const item = await db.transaction(storeName).objectStore(storeName).get(key)
```

### Obtenir tous les éléments d'un magasin : `getAll()`

Obtenir toutes les clés stockées

```js
const items = await db.transaction(storeName).objectStore(storeName).getAllKeys()
```

Obtenir toutes les valeurs stockées

```js
const items = await db.transaction(storeName).objectStore(storeName).getAll()
```

## Supprimer des données de IndexedDB

Supprimer la base de données, un magasin d'objets et des données

### Supprimer une base de données IndexedDB entière

```js
const dbName = 'mydbname'
await deleteDB(dbName)
```

### Pour supprimer des données dans un magasin d'objets

Nous utilisons une transaction :

```js
(async () => {
  //...

  const dbName = 'mydbname'
  const storeName = 'store1'
  const version = 1

  const db = await openDB(dbName, version, {
    upgrade(db, oldVersion, newVersion, transaction) {
      const store = db.createObjectStore(storeName)
    }
  })

  const tx = await db.transaction(storeName, 'readwrite')
  const store = await tx.objectStore(storeName)

  const key = 'Hello again'
  await store.delete(key)
  await tx.done
})()
```


## Migrer depuis une version précédente d'une base de données

Le troisième paramètre (optionnel) de la fonction `openDB()` est un objet qui peut contenir une fonction `upgrade` **appelée uniquement si le numéro de version est supérieur à la version actuellement installée de la base de données**. Dans le corps de cette fonction, vous pouvez mettre à niveau la structure (magasins et index) de la base de données :

```js
const name = 'mydbname'
const version = 1
openDB(name, version, {
  upgrade(db, oldVersion, newVersion, transaction) {
    console.log(oldVersion)
  }
})
```

Dans ce callback, vous pouvez vérifier depuis quelle version l'utilisateur met à jour, et effectuer certaines opérations en conséquence.

Vous pouvez effectuer une migration depuis une version précédente de la base de données en utilisant cette syntaxe

```js
(async () => {
  //...
  const dbName = 'mydbname'
  const storeName = 'store0'
  const version = 1

  const db = await openDB(dbName, version, {
    upgrade(db, oldVersion, newVersion, transaction) {
      switch (oldVersion) {
        case 0: // aucune base de données créée auparavant
          // un magasin introduit dans la version 1
          db.createObjectStore('store1')
        case 1:
          // un nouveau magasin dans la version 2
          db.createObjectStore('store2', { keyPath: 'name' })
      }
      db.createObjectStore(storeName)
    }
  })
})()
```


## Clés uniques

`createObjectStore()` comme vous pouvez le voir dans `case 1` accepte un deuxième paramètre qui indique la clé d'index de la base de données. Cela est très utile lorsque vous stockez des objets : les appels `put()` n'ont pas besoin d'un deuxième paramètre, mais peuvent simplement prendre la valeur (un objet) et la clé sera mappée à la propriété de l'objet qui a ce nom.

L'index vous donne un moyen de récupérer une valeur plus tard par cette clé spécifique, et il doit être unique (chaque élément doit avoir une clé différente).

Une clé peut être définie pour s'auto-incrémenter, donc vous n'avez pas besoin de la suivre dans le code client :

```js
db.createObjectStore('notes', { autoIncrement: true })
```

Utilisez l'auto-incrémentation si vos valeurs ne contiennent pas déjà une clé unique (par exemple, si vous collectez des adresses e-mail sans un nom associé).

### Vérifier si un magasin existe

Vous pouvez vérifier si un magasin d'objets existe déjà en appelant la méthode `objectStoreNames()` :

```js
const storeName = 'store1'

if (!db.objectStoreNames.contains(storeName)) {
  db.createObjectStore(storeName)
}
```

## Supprimer de IndexedDB

Supprimer la base de données, un magasin d'objets et des données

### Supprimer une base de données

```js
await deleteDB('mydb')
```

### Supprimer un magasin d'objets

Un magasin d'objets ne peut être supprimé que dans le callback lors de l'ouverture d'une base de données, et ce callback n'est appelé que si vous spécifiez une version supérieure à celle actuellement installée :

```js
const db = await openDB('dogsdb', 2, {
  upgrade(db, oldVersion, newVersion, transaction) {
    switch (oldVersion) {
      case 0: // aucune base de données créée auparavant
        // un magasin introduit dans la version 1
        db.createObjectStore('store1')
      case 1:
        // supprimer l'ancien magasin dans la version 2, en créer un nouveau
        db.deleteObjectStore('store1')
        db.createObjectStore('store2')
    }
  }
})
```

### Pour supprimer des données dans un magasin d'objets, utilisez une transaction

```js
const key = 232 // une clé aléatoire

const db = await openDB(/*...*/)
const tx = await db.transaction('store', 'readwrite')
const store = await tx.objectStore('store')
await store.delete(key)
await tx.complete
```

## Il y a plus !

Ce ne sont que les bases. Je n'ai pas parlé des curseurs et d'autres choses plus avancées. Il y a plus à savoir sur IndexedDB, mais j'espère que cela vous donne un bon départ.

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon livre JavaScript sur [jshandbook.com](https://jshandbook.com/)