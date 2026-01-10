---
title: Comment utiliser WeakMap et WeakSet en JavaScript
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-06-07T16:57:53.000Z'
originalURL: https://freecodecamp.org/news/weakmap-and-weakset-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser WeakMap et WeakSet en JavaScript
seo_desc: "JavaScript offers a number of tools for organizing and managing data. And\
  \ while developers often use widely recognized tools like Maps and Sets, they may\
  \ often overlook certain other valuable resources. \nFor example, are you familiar\
  \ with WeakMap and..."
---

JavaScript offre un certain nombre d'outils pour organiser et gérer les données. Et bien que les développeurs utilisent souvent des outils largement reconnus comme Maps et Sets, ils peuvent souvent négliger certaines autres ressources précieuses.

Par exemple, connaissez-vous WeakMap et WeakSet ? Ce sont des outils spéciaux en JavaScript qui aident à stocker et gérer les données de manière unique.

Cet article explore WeakMap et WeakSet de manière claire et complète. Nous commencerons par comprendre le concept de références faibles et comment elles diffèrent des structures de données traditionnelles. Ensuite, nous approfondirons chaque concept, en expliquant ce qu'ils sont, comment les créer et les méthodes qu'ils offrent.

En cours de route, nous verrons des exemples pratiques de la manière dont WeakMap et WeakSet peuvent rationaliser votre code et débloquer de nouvelles possibilités.

Que vous soyez un pro de JavaScript ou que vous débutiez, comprendre WeakMap et WeakSet vous permet d'écrire un code plus propre et plus efficace.

## Table des matières

1. [Qu'est-ce qu'une WeakMap ?](#heading-quest-ce-quune-weakmap)
 [Caractéristiques clés de WeakMap](#heading-caracteristiques-cles-de-weakmap)
2. [Comment créer une WeakMap en utilisant le constructeur `new WeakMap()`](#heading-comment-creer-une-weakmap-en-utilisant-le-constructeur-new-weakmap)
3. [Cas d'utilisation courants pour WeakMap](#heading-cas-dutilisation-courants-pour-weakmap)
4. [Méthodes de WeakMap](#heading-methodes-de-weakmap)
5. [Qu'est-ce qu'un WeakSet ?](#heading-quest-ce-quun-weakset)
 [Caractéristiques clés de WeakSet](#heading-caracteristiques-cles-de-weakset)
6. [Comment créer un WeakSet en utilisant le constructeur `new WeakSet()`](#heading-comment-creer-un-weakset-en-utilisant-le-constructeur-new-weakset)
7. [Cas d'utilisation courants pour WeakSet](#heading-cas-dutilisation-courants-pour-weakset)
8. [Méthodes de WeakSet](#heading-methodes-de-weakset)
9. [WeakSet vs. WeakMap](#heading-weakset-vs-weakmap)
10. [Conclusion](#heading-conclusion)

## Qu'est-ce qu'une WeakMap ?

WeakMap est une structure de données intégrée en JavaScript introduite dans ECMAScript 6 (ES6). Elle est conçue pour stocker des paires clé-valeur où les clés doivent être des objets et les valeurs peuvent être arbitraires.

Elle diffère d'une Map régulière en ce sens qu'elle permet des références faibles à ses clés. Cela signifie que si un objet est utilisé comme clé et qu'il n'y a pas d'autres références à celui-ci, il peut être collecté par le garbage collector.

### Caractéristiques clés de WeakMap

#### Clés uniquement objets :

WeakMap n'accepte que les objets comme clés. Si vous tentez d'utiliser une clé non-objet, comme une chaîne ou un nombre, cela entraînera une erreur TypeError.

```javascript
const weakMap = new WeakMap();
const key = {}; // Clé valide, car c'est un objet
const invalidKey = 'string'; // Clé invalide, car ce n'est pas un objet
weakMap.set(key, 'value'); // Cela fonctionnera
weakMap.set(invalidKey, 'value'); // TypeError: Invalid value used as weak map key

```

#### Collecte des clés par le garbage collector :

WeakMap permet aux clés d'être collectées par le garbage collector lorsqu'il n'y a plus d'autres références à celles-ci. Cela signifie que si un objet utilisé comme clé dans une WeakMap n'est plus référencé ailleurs dans le programme, il peut être automatiquement supprimé de la WeakMap.

```javascript
let key = {name: 'John'};
const weakMap = new WeakMap();
weakMap.set(key, 'value');
key = null; // Suppression de la référence à la clé
// À ce stade, puisque il n'y a plus d'autres références à l'objet clé,
// il peut être collecté par le garbage collector, et la paire clé-valeur dans la WeakMap sera automatiquement supprimée

```

#### Pas d'énumération des clés :

Contrairement aux objets Map réguliers, WeakMap n'expose pas de méthodes pour énumérer ses clés, telles que `keys()`, `values()`, ou `entries()`. Cela est dû au fait que les clés peuvent être soumises à la collecte des déchets, et les exposer empêcherait leur collecte.

```javascript
const weakMap = new WeakMap();
const key = {};
weakMap.set(key, 'value');
console.log(weakMap.keys()); // TypeError: weakMap.keys is not a function

```

#### Pas de propriété Size :

WeakMap n'a pas de propriété `size` comme les objets Map réguliers. Encore une fois, cela est dû au fait que la taille de la WeakMap pourrait changer à mesure que les clés sont collectées par le garbage collector.

```javascript
const weakMap = new WeakMap();
console.log(weakMap.size); // undefined

```

#### Gestion de la mémoire :

WeakMap est particulièrement utile dans les scénarios où vous devez associer des données supplémentaires à des objets mais ne souhaitez pas empêcher ces objets d'être collectés par le garbage collector lorsqu'ils ne sont plus nécessaires. Cela le rend utile pour le cache, le stockage de données privées et d'autres opérations sensibles à la mémoire.

## Comment créer une WeakMap en utilisant le constructeur `new WeakMap()`

Créer une WeakMap en utilisant le constructeur `new WeakMap()` est simple. Voici comment vous pouvez le faire :

Tout d'abord, décomposons la syntaxe de création d'une WeakMap en utilisant le constructeur `new WeakMap()` :

```javascript
const weakMap = new WeakMap();

```

* `new WeakMap()` : C'est l'appel du constructeur qui crée une nouvelle instance de WeakMap.
* `const weakMap` : Cela déclare une variable nommée `weakMap` pour contenir la référence à la nouvelle instance de WeakMap créée.
* `=` : C'est l'opérateur d'assignation, qui assigne la nouvelle instance de WeakMap créée à la variable `weakMap`.

Maintenant, créons un exemple de WeakMap :

```javascript
// Création d'une nouvelle WeakMap
const weakMap = new WeakMap();

// Création d'objets à utiliser comme clés
const user1 = { id: 1 };
const user2 = { id: 2 };

// Définition de paires clé-valeur dans la WeakMap
weakMap.set(user1, 'John');
weakMap.set(user2, 'Alice');

// Récupération des valeurs de la WeakMap
console.log(weakMap.get(user1)); // Sortie : John
console.log(weakMap.get(user2)); // Sortie : Alice

// Suppression d'une paire clé-valeur de la WeakMap
weakMap.delete(user1);

// Tentative de récupération de la valeur après suppression
console.log(weakMap.get(user1)); // Sortie : undefined

```

Dans cet exemple :

* Nous créons une nouvelle instance de WeakMap en utilisant le constructeur `new WeakMap()`.
* Deux objets `user1` et `user2` sont créés pour servir de clés dans la WeakMap.
* Des paires clé-valeur sont définies dans la WeakMap en utilisant la méthode `set()`, associant chaque objet utilisateur à un nom correspondant.
* Nous récupérons les valeurs associées à `user1` et `user2` en utilisant la méthode `get()`.
* Ensuite, nous supprimons la paire clé-valeur associée à `user1` en utilisant la méthode `delete()`.
* Enfin, nous tentons de récupérer la valeur associée à `user1` à nouveau, ce qui retourne `undefined` puisque la paire clé-valeur a été supprimée.

N'oubliez pas que WeakMap n'accepte que les objets comme clés. Si vous essayez d'utiliser une clé non-objet, cela entraînera une erreur TypeError.

De plus, WeakMap ne supporte pas les méthodes comme `keys()`, `values()`, ou `entries()`, ni n'a de propriétés comme `size`. Cela est dû au fait que les clés de WeakMap peuvent être soumises à la collecte des déchets, et les exposer interférerait avec ce processus.

## Cas d'utilisation courants pour WeakMap

WeakMap est une structure de données spécialisée en JavaScript conçue pour des cas d'utilisation spécifiques où vous devez associer des données supplémentaires à des objets sans empêcher ces objets d'être collectés par le garbage collector.

Voici quelques scénarios courants où WeakMap est particulièrement utile :

### Stockage de données privées :

WeakMap peut être utilisé pour stocker des données privées associées à des objets. Cela est souvent utilisé dans les bibliothèques ou frameworks pour attacher des données privées à des objets sans les exposer au monde extérieur.

Puisque les clés de WeakMap sont faiblement maintenues, les données privées seront automatiquement supprimées lorsque l'objet sera collecté par le garbage collector.

```javascript
const privateData = new WeakMap();

class MyClass {
    constructor() {
        privateData.set(this, { secret: 'my secret data' });
    }

    getSecretData() {
        return privateData.get(this).secret;
    }
}

const obj = new MyClass();
console.log(obj.getSecretData()); // Sortie : my secret data

```

### Mécanisme de cache :

WeakMap peut être utilisé pour mettre en cache des données où les valeurs mises en cache peuvent être collectées par le garbage collector si elles ne sont plus nécessaires.

Cela peut être particulièrement utile dans les scénarios où vous souhaitez mettre en cache des données associées à des objets ou des calculs spécifiques, mais souhaitez vous assurer que le cache n'empêche pas ces objets d'être collectés par le garbage collector lorsqu'ils ne sont plus nécessaires.

```javascript
const cache = new WeakMap();

function expensiveCalculation(obj) {
    if (!cache.has(obj)) {
        const result = // perform expensive calculation
        cache.set(obj, result);
    }
    return cache.get(obj);
}

const data = { /* some data */ };
console.log(expensiveCalculation(data)); // Effectue un calcul coûteux
console.log(expensiveCalculation(data)); // Retourne le résultat mis en cache

```

### Gestion des éléments DOM :

WeakMap peut être utilisé pour garder une trace des éléments DOM sans empêcher leur collecte par le garbage collector lorsqu'ils sont supprimés du DOM.

Cela est particulièrement utile dans les scénarios où vous souhaitez associer des données ou des comportements supplémentaires aux éléments DOM, mais souhaitez vous assurer que ces associations n'empêchent pas les éléments d'être correctement nettoyés lorsqu'ils ne sont plus nécessaires.

```javascript
const elementData = new WeakMap();

function attachEventListener(element, callback) {
    element.addEventListener('click', callback);
    elementData.set(element, { callback });
}

function detachEventListener(element) {
    const data = elementData.get(element);
    if (data) {
        element.removeEventListener('click', data.callback);
        elementData.delete(element);
    }
}

const button = document.getElementById('myButton');
attachEventListener(button, () => {
    console.log('Button clicked');
});

```

### Mémoïsation :

WeakMap peut être utilisé pour la mémoïsation dans les fonctions où les valeurs mises en cache peuvent être automatiquement effacées si elles ne sont plus nécessaires.

Cela est utile dans les scénarios où vous souhaitez mettre en cache les résultats d'appels de fonctions coûteux, mais souhaitez vous assurer que le cache ne croît pas indéfiniment et ne consomme pas une mémoire excessive.

```javascript
const memoizationCache = new WeakMap();

function memoizedFunction(obj) {
    if (!memoizationCache.has(obj)) {
        const result = // perform expensive computation
        memoizationCache.set(obj, result);
    }
    return memoizationCache.get(obj);
}

const data = { /* some data */ };
console.log(memoizedFunction(data)); // Effectue un calcul coûteux
console.log(memoizedFunction(data)); // Retourne le résultat mis en cache

```

## Méthodes de WeakMap

WeakMap en JavaScript a un ensemble limité de méthodes par rapport à d'autres structures de données comme Map.

Voici les méthodes disponibles pour WeakMap :

### `set(key, value)` :

Cette méthode définit une nouvelle paire clé-valeur dans la WeakMap. La clé doit être un objet, et la valeur peut être de n'importe quel type de données.

```javascript
const weakMap = new WeakMap();
const key = {};
weakMap.set(key, 'value');

```

### `get(key)` :

Cette méthode récupère la valeur associée à la clé spécifiée dans la WeakMap. Si la clé n'est pas trouvée, elle retourne undefined.

```javascript
const weakMap = new WeakMap();
const key = {};
weakMap.set(key, 'value');
console.log(weakMap.get(key)); // Sortie : value

```

### `has(key)` :

Cette méthode vérifie si la clé spécifiée existe dans la WeakMap. Elle retourne true si la clé existe et false sinon.

```javascript
const weakMap = new WeakMap();
const key = {};
weakMap.set(key, 'value');
console.log(weakMap.has(key)); // Sortie : true

```

### `delete(key)` :

Cette méthode supprime la clé spécifiée et sa valeur associée de la WeakMap. Elle retourne true si la clé existait et a été supprimée avec succès, et false sinon.

```javascript
const weakMap = new WeakMap();
const key = {};
weakMap.set(key, 'value');
console.log(weakMap.delete(key)); // Sortie : true

```

N'oubliez pas que WeakMap n'a pas de méthodes comme `keys()`, `values()`, `entries()`, ou de propriétés comme `size`. Cela est dû au fait que les clés de WeakMap peuvent être soumises à la collecte des déchets, et les exposer interférerait avec ce processus.
De plus, WeakMap ne permet pas l'itération sur ses clés ou valeurs pour la même raison.

## Qu'est-ce qu'un WeakSet ?

WeakSet est une autre structure de données spécialisée introduite dans ECMAScript 6 (ES6) aux côtés de WeakMap. Elle est conçue pour fonctionner avec des collections d'objets.

Contrairement à Set, WeakSet n'autorise que les objets à être stockés, et comme WeakMap, elle détient des références faibles à ces objets. Cela signifie que si un objet stocké dans un WeakSet n'a pas d'autres références ailleurs dans le programme, il peut être automatiquement collecté par le garbage collector. Cela rend WeakSet particulièrement utile dans les scénarios où vous devez maintenir une collection d'objets sans empêcher leur nettoyage lorsqu'ils ne sont plus nécessaires.

### Caractéristiques clés de WeakSet

#### Valeurs uniquement objets :

WeakSet n'autorise que les objets à être stockés comme valeurs. Si vous tentez d'ajouter une valeur non-objet, comme un type primitif ou un autre type de données, cela entraînera une erreur TypeError.

#### Références faibles :

Similaire à WeakMap, WeakSet détient des références faibles à ses éléments. Cela signifie que si un objet stocké dans un WeakSet n'a pas d'autres références ailleurs dans le programme, il peut être automatiquement collecté par le garbage collector.

#### Pas d'énumération :

WeakSet ne fournit pas de méthodes comme `keys()`, `values()`, ou `entries()`, ni ne supporte l'itération avec `forEach()`. Cela est dû au fait que le contenu d'un WeakSet peut changer à mesure que les objets sont collectés par le garbage collector, et les exposer interférerait avec ce processus.

#### Pas de propriété Size :

WeakSet n'a pas de propriété `size` comme les objets Set. Cela est dû au fait que la taille d'un WeakSet pourrait changer à mesure que les objets sont collectés par le garbage collector, et exposer la propriété size ne fournirait pas d'informations précises.

#### Gestion de la mémoire :

WeakSet est utile pour les scénarios où vous devez maintenir une collection d'objets mais ne souhaitez pas empêcher ces objets d'être collectés par le garbage collector lorsqu'ils ne sont plus nécessaires.
Cela peut être particulièrement utile dans les scénarios tels que la gestion des événements, où les objets peuvent être ajoutés à l'ensemble temporairement puis supprimés plus tard.

## Comment créer un WeakSet en utilisant le constructeur `new WeakSet()`

Tout d'abord, décomposons la syntaxe :

```javascript
const weakSet = new WeakSet();

```

* `new WeakSet()` : C'est l'appel du constructeur qui crée une nouvelle instance de WeakSet.
* `const weakSet` : Cela déclare une variable nommée `weakSet` pour contenir la référence à la nouvelle instance de WeakSet créée.
* `=` : C'est l'opérateur d'assignation, qui assigne la nouvelle instance de WeakSet créée à la variable `weakSet`.

Maintenant, créons un exemple de WeakMap :

```javascript
// Création d'un nouveau WeakSet
const weakSet = new WeakSet();

// Création de quelques objets à ajouter au WeakSet
const obj1 = { id: 1 };
const obj2 = { id: 2 };
const obj3 = { id: 3 };

// Ajout d'objets au WeakSet
weakSet.add(obj1);
weakSet.add(obj2);
weakSet.add(obj3);

// Vérification si un objet existe dans le WeakSet
console.log(weakSet.has(obj1)); // Sortie : true
console.log(weakSet.has(obj2)); // Sortie : true
console.log(weakSet.has(obj3)); // Sortie : true

// Suppression d'un objet du WeakSet
weakSet.delete(obj2);

// Vérification si l'objet supprimé existe toujours
console.log(weakSet.has(obj2)); // Sortie : false

```

Dans cet exemple :

* Nous créons d'abord une nouvelle instance de WeakSet en utilisant le constructeur `new WeakSet()`.
* Ensuite, nous créons trois objets différents `obj1`, `obj2`, et `obj3` que nous voulons ajouter au WeakSet.
* Nous ajoutons ces objets au WeakSet en utilisant la méthode `add()`.
* Nous vérifions si chaque objet existe dans le WeakSet en utilisant la méthode `has()`.
* Ensuite, nous supprimons `obj2` du WeakSet en utilisant la méthode `delete()`.
* Enfin, nous vérifions si `obj2` existe toujours dans le WeakSet, ce qui retourne `false` puisque il a été supprimé.

## Cas d'utilisation courants pour WeakSet

WeakSet en JavaScript sert des objectifs spécifiques grâce à sa capacité à détenir des références faibles aux objets.

Voici quelques cas d'utilisation courants où WeakSet peut être particulièrement utile :

### Vérification de l'appartenance d'objets :

WeakSet est utile pour suivre l'appartenance d'objets dans une collection sans empêcher leur collecte par le garbage collector lorsqu'ils ne sont plus nécessaires.

Cela peut être utile dans les scénarios où vous devez garder une trace d'un ensemble dynamique d'objets, comme la gestion des gestionnaires d'événements ou le suivi des associations de données temporaires.

```javascript
const eventHandlers = new WeakSet();

function addEventHandler(element, handler) {
    eventHandlers.add(handler);
    element.addEventListener('click', handler);
}

function removeEventHandler(element, handler) {
    eventHandlers.delete(handler);
    element.removeEventListener('click', handler);
}

```

### Prévention de la duplication d'objets :

WeakSet peut être utilisé pour s'assurer que les objets ne sont pas dupliqués dans une collection. Puisque WeakSet ne peut contenir que des objets uniques, tenter d'ajouter le même objet plusieurs fois n'aura aucun effet.

```javascript
const uniqueObjects = new WeakSet();

function addObject(obj) {
    if (!uniqueObjects.has(obj)) {
        uniqueObjects.add(obj);
        console.log('Object added:', obj);
    } else {
        console.log('Object already exists:', obj);
    }
}

const obj1 = { id: 1 };
const obj2 = { id: 2 };
addObject(obj1); // Sortie : Object added: { id: 1 }
addObject(obj1); // Sortie : Object already exists: { id: 1 }
addObject(obj2); // Sortie : Object added: { id: 2 }

```

### Gestion des références faibles dans les caches :

WeakSet peut être utilisé pour détenir des références faibles aux objets stockés dans un cache. Cela permet aux objets mis en cache d'être collectés par le garbage collector lorsqu'ils ne sont plus nécessaires, empêchant ainsi les fuites de mémoire.

```javascript
const cache = new WeakSet();

function addToCache(obj) {
    cache.add(obj);
}

function isCached(obj) {
    return cache.has(obj);
}

const cachedObj = { data: 'cached data' };
addToCache(cachedObj);
console.log(isCached(cachedObj)); // Sortie : true

// Après avoir supprimé toutes les références à cachedObj
cachedObj = null;
console.log(isCached(cachedObj)); // Sortie : false (cachedObj est collecté par le garbage collector)

```

### Gestion des références d'objets dans les structures de données :

WeakSet peut être utilisé pour gérer les références d'objets dans diverses structures de données, telles que les graphes ou les structures arborescentes, où les objets peuvent être ajoutés et supprimés dynamiquement.

```javascript
const references = new WeakSet();

function addReference(obj) {
    references.add(obj);
}

function removeReference(obj) {
    references.delete(obj);
}

const obj1 = { id: 1 };
const obj2 = { id: 2 };
addReference(obj1);
addReference(obj2);
removeReference(obj1);

```

## Méthodes de WeakSet

WeakSet en JavaScript a un ensemble limité de méthodes par rapport à d'autres structures de données comme Set. Voici les méthodes disponibles pour WeakSet :

### `add(value)` :

Cette méthode ajoute la valeur spécifiée (qui doit être un objet) au WeakSet. Si la valeur est déjà présente dans le WeakSet, la méthode n'a aucun effet.

```javascript
const weakSet = new WeakSet();
const obj = { id: 1 };
weakSet.add(obj);

```

### `delete(value)` :

Cette méthode supprime la valeur spécifiée du WeakSet, si elle existe. Elle retourne `true` si la valeur a été supprimée avec succès, et `false` sinon.

```javascript
const weakSet = new WeakSet();
const obj = { id: 1 };
weakSet.add(obj);
console.log(weakSet.delete(obj)); // Sortie : true

```

### `has(value)` :

Cette méthode vérifie si la valeur spécifiée existe dans le WeakSet. Elle retourne `true` si la valeur est présente, et `false` sinon.

```javascript
const weakSet = new WeakSet();
const obj = { id: 1 };
weakSet.add(obj);
console.log(weakSet.has(obj)); // Sortie : true

```

WeakSet n'a pas de méthodes comme `values()` ou `forEach()` pour l'itération, ni de propriétés comme `size`. Cela est dû au fait que WeakSet est conçu pour détenir des références faibles aux objets, et exposer son contenu interférerait avec ce processus. De plus, WeakSet ne permet pas l'itération sur ses valeurs pour des raisons similaires.

## WeakSet vs. WeakMap

WeakSet et WeakMap sont tous deux des structures de données spécialisées en JavaScript qui détiennent des références faibles aux objets, mais ils servent des objectifs légèrement différents.

Voici une comparaison entre les deux :

### 1. Objectif :

**WeakSet :** Conçu pour stocker une collection d'objets où chaque objet ne peut apparaître qu'une seule fois dans l'ensemble. WeakSet est utile lorsque vous devez suivre l'existence d'objets sans stocker de données supplémentaires associées à ceux-ci.

**WeakMap :** Conçu pour stocker des paires clé-valeur où les clés doivent être des objets et les valeurs peuvent être arbitraires. WeakMap est utile lorsque vous devez associer des données supplémentaires à des objets mais souhaitez permettre à ces objets d'être collectés par le garbage collector lorsqu'ils ne sont plus nécessaires.

### 2. Contenu :

**WeakSet :** Contient uniquement des objets comme valeurs. Les valeurs dans un WeakSet peuvent être vérifiées pour leur existence, mais il n'y a pas de données associées.

**WeakMap :** Contient des paires clé-valeur, où les clés doivent être des objets et les valeurs peuvent être de n'importe quel type de données. Chaque paire clé-valeur représente une association entre un objet et certaines données.

### 3. Itération :

**WeakSet :** Ne supporte pas les méthodes comme `keys()`, `values()`, ou `forEach()`. WeakSet ne permet pas l'itération directe sur ses valeurs, car exposer les valeurs interférerait avec le mécanisme de référence faible.

**WeakMap :** Ne supporte pas non plus les méthodes comme `keys()`, `values()`, ou `forEach()` pour des raisons similaires. WeakMap ne permet pas l'itération directe sur ses clés ou valeurs pour éviter les interférences avec le mécanisme de référence faible.

### 4. Utilisation :

**WeakSet :** Communément utilisé pour gérer des collections d'objets, comme le suivi des gestionnaires d'événements, la gestion des références d'objets uniques, ou la prévention de la duplication d'objets dans une collection.

**WeakMap :** Communément utilisé pour associer des données supplémentaires à des objets, comme la mise en cache de données liées à des objets spécifiques, le stockage de données privées associées à des objets, ou la gestion des références d'objets dans des structures de données comme les graphes ou les arbres.

## Conclusion

Bien que les structures de données familières comme Map et Set excellent en JavaScript, WeakMap et WeakSet offrent une approche unique. Ces structures utilisent des références faibles pour gérer automatiquement la mémoire associée aux objets.

Cela peut être particulièrement bénéfique pour les objets de courte durée ou ceux impliqués dans des références circulaires.

Dans cet article, nous avons exploré comment créer et utiliser WeakMap et WeakSet, ainsi que leurs cas d'utilisation courants, vous permettant d'écrire un code JavaScript plus propre et plus efficace en mémoire.

Connectez-vous avec moi sur [LinkedIn](https://ng.linkedin.com/in/joan-ayebola).