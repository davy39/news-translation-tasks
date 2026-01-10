---
title: 'ES8 : Les nouveautés du langage JavaScript en 2017'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-15T08:54:55.000Z'
originalURL: https://freecodecamp.org/news/es8-the-new-features-of-javascript-7506210a1a22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9yuM4oWXT1Wfo0Cx5jkMwA.png
tags:
- name: es8
  slug: es8
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: 'ES8 : Les nouveautés du langage JavaScript en 2017'
seo_desc: 'By Flavio H. Freitas

  ES8 is live! Released earlier this summer, ES8 (also called ES2017) offers new ways
  of coding with JavaScript. Let''s explore them.

  If you have the latest version of Chrome, open the console and let''s code together.


  How to access...'
---

Par Flavio H. Freitas

ES8 est disponible ! Publié plus tôt cet été, ES8 (également appelé ES2017) offre de nouvelles façons de coder avec JavaScript. Explorons-les.

Si vous avez la dernière version de Chrome, ouvrez la console et codons ensemble.

![Image](https://cdn-media-1.freecodecamp.org/images/IA-BH2UVyy--TrnW3x4zwQuxEMfW47VTVb5F align="left")

*Comment accéder à la console JavaScript dans Chrome : Affichage > Développeur > Console JavaScript*

## Object.values()

Accédez à toutes les valeurs de notre objet sans complication. Voici un exemple :

```javascript
const countries = {
    BR: 'Brazil',
    DE: 'Germany',
    RO: 'Romania',
    US: 'United States of America'
};

Object.values(countries); // ['Brazil', 'Germany', 'Romania', 'United States of America']
```

## Object.entries()

Transformez les attributs de votre **objet** en un **tableau** d'attributs :

```javascript
const countries = {
    BR: 'Brazil',
    DE: 'Germany',
    RO: 'Romania',
    US: 'United States of America'
};

Object.entries(countries); 
// [['BR', 'Brazil'], ['DE', 'Germany'], ['RO', 'Romania'], ['US','United States of America']]
```

## Remplissage de chaînes (padStart et padEnd)

Cela retourne la chaîne passée en ajoutant le remplissage au début ou à la fin. La définition de la fonction est :

```javascript
'string'.padStart(targetLength, padString)
'string'.padEnd(targetLength, padString)
```

Nous pouvons faire :

```javascript
'0.10'.padStart(10); // retourne une chaîne de longueur 10, en ajoutant des espaces vides au début
'hi'.padStart(1);            // 'hi'
'hi'.padStart(5);            // '   hi'
'hi'.padStart(5, 'abcd');    // 'abchi'
'hi'.padStart(10, 'abcd');   // 'abcdabcdhi'
'loading'.padEnd(10, '.');   // 'loading...'

// exemple utile pour faciliter la lecture
'0.10'.padStart(12);         // '       0.10'
'23.10'.padStart(12);        // '      23.10'
'12,330.10'.padStart(12);    // '  12,330.10'
```

## Object.getOwnPropertyDescriptors()

Il retourne tous les descripteurs de propriétés propres (non hérités) d'un objet. Les attributs de l'objet retourné peuvent être : `value`, `writable`, `get`, `set`, `configurable` et `enumerable`.

```javascript
const obj = {
    name: 'Pablo',
    get foo() { return 42; }
};

Object.getOwnPropertyDescriptors(obj);
//
// {
//  "name": {
//     "value": "Pablo",
//     "writable":true,
//     "enumerable":true,
//     "configurable":true
//  },
//  "foo":{
//     "enumerable":true,
//     "configurable":true,
//     "get": function foo()
//     "set": undefined
//  }
// }
```

Un exemple pratique est : JavaScript a une méthode pour copier les propriétés `Object.assign()`. Elle copie la propriété dont la clé est `key`. Comme ceci :

```javascript
const value = source[key]; // get
target[key] = value;       // set
```

Et dans certains cas, cela échoue car il ne copie pas correctement les propriétés avec des attributs non par défaut tels que les getters, setters et les propriétés non modifiables.

Par exemple :

```javascript
const objTarget = {};
const objSource = {
    set greet(name) { console.log('hey, ' + name); }
};

Object.assign(objTarget, objSource);
objTarget.greet = 'love';     // essayer de définir échoue, définit greet = 'love'
```

Solution :

```javascript
const objTarget = {};
const objSource = {
    set greet(name) { console.log('hey, ' + name); }
};

Object.defineProperties(objTarget,          
           Object.getOwnPropertyDescriptors(objSource));

objTarget.greet = 'love'; // affiche 'hey, love'
```

## Virgules finales dans les listes de paramètres et les appels de fonction

Il s'agit d'un changement de syntaxe. Il nous permet d'écrire une déclaration de fonction valide avec une virgule à la fin.

```javascript
getDescription(name, age,) { ... }
```

## Fonctions asynchrones (async et await)

Cela facilite grandement le travail avec les fonctions asynchrones :

```javascript
function loadExternalContent() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('hello');
        }, 3000);
    });
}

async function getContent() {
    const text = await loadExternalContent();
    console.log(text);
}

console.log('it will call function');
getContent();
console.log('it called function');

// il imprime :
'it will call function' // synchrone
'it called function'    // synchrone
'hello'                 // asynchrone (après 3 secondes)
```

## Mémoire partagée et atomiques

Selon la [spécification](https://tc39.github.io/ecmascript_sharedmem/shmem.html) :

> "La mémoire partagée est exposée sous la forme d'un nouveau type SharedArrayBuffer ; Le nouvel objet global Atomics fournit des opérations atomiques sur les emplacements de mémoire partagée, y compris des opérations qui peuvent être utilisées pour créer des primitives de synchronisation bloquantes."

Cela signifie :

Mémoire partagée : nous pouvons permettre à plusieurs threads de lire et d'écrire les mêmes données avec le nouveau constructeur `SharedArrayBuffer`.

Atomics : Nous pouvons utiliser l'objet `Atomics` pour nous assurer que rien de ce qui est écrit ou lu ne sera interrompu au milieu du processus. Ainsi, les opérations sont terminées avant que la suivante ne commence.

Si vous avez aimé cet article, n'oubliez pas de l'aimer et de m'applaudir — cela signifie beaucoup pour l'auteur ? Et [suivez-moi](https://medium.com/@flaviohfreitas) si vous voulez lire plus d'articles sur la Culture, la Technologie et les Startups.

**Flávio H. de Freitas** est un Entrepreneur, Ingénieur, Amoureux de la Technologie, Rêveur et Voyageur. Il a travaillé en tant que **CTO** au **Brésil**, dans la **Silicon Valley et en Europe**.