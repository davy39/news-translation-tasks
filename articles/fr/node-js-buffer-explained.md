---
title: Node.js Buffer Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-17T00:35:00.000Z'
originalURL: https://freecodecamp.org/news/node-js-buffer-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c8d740569d1a4ca32d7.jpg
tags:
- name: Node.js
  slug: nodejs
- name: toothbrush
  slug: toothbrush
seo_title: Node.js Buffer Expliqué
seo_desc: 'What are Buffers?

  Binary is simply a set or a collection of 1 and 0. Each number in a binary, each
  1 and 0 in a set are called a bit. Computer converts the data to this binary format
  to store and perform operations. For example, the following are fiv...'
---

## **Qu'est-ce que les Buffers ?**

Le binaire est simplement un ensemble ou une collection de `1` et de `0`. Chaque nombre dans un binaire, chaque 1 et 0 dans un ensemble sont appelés un _bit_. L'ordinateur convertit les données dans ce format binaire pour les stocker et effectuer des opérations. Par exemple, voici cinq binaires différents :

`10, 01, 001, 1110, 00101011`

JavaScript ne possède pas de type de données octet dans son API principale. Pour gérer les données binaires, Node.js inclut une implémentation de buffer binaire avec un module global appelé `Buffer`.

### **Créer un Buffer**

Il existe différentes façons de créer un buffer dans Node.js. Vous pouvez créer un buffer vide avec une taille de 10 octets.

```javascript
const buf1 = Buffer.alloc(10);
```

À partir de chaînes encodées en UTF-8, la création se fait comme ceci :

```javascript
const buf2 = Buffer.from('Bonjour le monde !');
```

Il existe différents encodages acceptés lors de la création d'un Buffer :

* ascii
* utf-8
* base64
* latin1
* binaire
* hex

Il existe trois fonctions distinctes allouées dans l'API Buffer pour utiliser et créer de nouveaux buffers. Dans les exemples ci-dessus, nous avons vu `alloc()` et `from()`. La troisième est `allocUnsafe()`.

```javascript
const buf3 = Buffer.allocUnsafe(10);
```

Lorsqu'il est retourné, cette fonction peut contenir d'anciennes données qui doivent être écrasées.

### **Interactions avec Buffer**

Il existe différentes interactions qui peuvent être faites avec l'API Buffer. Nous allons en couvrir la plupart ici. Commençons par convertir un buffer en JSON.

```javascript
let bufferOne = Buffer.from('Ceci est un exemple de buffer.');
console.log(bufferOne);

// Sortie : <Buffer 43 65 63 69 20 65 73 74 20 75 6e 20 65 78 65 6d 70 6c 65 20 64 65 20 62 75 66 66 65 72 2e>

let json = JSON.stringify(bufferOne);
console.log(json);

// Sortie : {"type": "Buffer", "data": [67,101,99,105,32,101,115,116,32,117,110,32,101,120,101,109,112,108,101,32,100,101,32,98,117,102,102,101,114,46]}
```

Le JSON précise que le type d'objet transformé est un Buffer, ainsi que ses données. La conversion d'un buffer vide en JSON nous montre qu'il ne contient que des zéros.

```javascript
const emptyBuf = Buffer.alloc(10);

emptyBuf.toJSON();

// Sortie : { "type": "Buffer", "data": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] }
```

Notez que l'API Buffer fournit également une fonction directe `toJSON()` pour convertir un buffer en un objet JSON. Pour examiner la taille d'un buffer, nous pouvons utiliser la méthode `length`.

```javascript
emptyBuf.length;
// Sortie : 10
```

Maintenant, convertissons le buffer en une chaîne lisible, dans notre cas, encodée en utf-8.

```javascript
console.log(bufferOne.toString('utf8'));

// Sortie : Ceci est un exemple de buffer.
```

`.toString()` convertit par défaut un buffer en une chaîne au format utf-8. C'est ainsi que vous décodez un buffer. Si vous spécifiez un encodage, vous pouvez convertir le buffer dans un autre encodage.

```javascript
console.log(bufferOne.toString('base64'));
```

## Plus d'informations sur les Buffers :

* [Besoin d'une meilleure compréhension des buffers dans Node.js ? Consultez ceci.](https://www.freecodecamp.org/news/do-you-want-a-better-understanding-of-buffer-in-node-js-check-this-out-2e29de2968e8/)