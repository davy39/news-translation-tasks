---
title: Qu'est-ce que la métaprogrammation en JavaScript ? En français, s'il vous plaît.
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2020-11-03T17:06:32.000Z'
originalURL: https://freecodecamp.org/news/what-is-metaprogramming-in-javascript-in-english-please
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/cover_freeCodeCamp.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que la métaprogrammation en JavaScript ? En français, s'il vous
  plaît.
seo_desc: 'JavaScript has many useful features that most developers know about. At
  the same time, there are some hidden gems that can solve really challenging problems
  if you''re aware of them.

  Metaprogramming in JavaScript is one such concept that many of us ma...'
---

JavaScript possède de nombreuses fonctionnalités utiles que la plupart des développeurs connaissent. En même temps, il existe quelques pépites cachées qui peuvent résoudre des problèmes vraiment difficiles si vous en êtes conscient.

La métaprogrammation en JavaScript est un concept que beaucoup d'entre nous ne connaissent peut-être pas. Dans cet article, nous allons apprendre ce qu'est la métaprogrammation et comment elle nous est utile.

Avec ES6 (ECMAScript 2015), nous avons le support des objets `Reflect` et `Proxy` qui nous permettent de faire de la métaprogrammation avec facilité. Dans cet article, nous apprendrons comment les utiliser avec des exemples.

# **Qu'est-ce que la métaprogrammation ?**

La `métaprogrammation` n'est rien de moins que de la _magie en programmation_ ! Que diriez-vous d'écrire un programme qui lit, modifie, analyse et même génère un programme ? Cela ne semble-t-il pas magique et puissant ?

![Image](https://lh5.googleusercontent.com/elwIjsjlSeV2c9VBF07ZDHmurJ5_NdeIJ0bDOSNpNai644OhE90gDbGlyOnL4xea5D7S6s9M17V3w4h3zgpr8Q9sn3Ke8BuzPJySs4JI6J0v0jvgX6eSdalnFdULzTWh85IjQMFGjYX-ymmAOA)
_La métaprogrammation est magique_

Wikipedia décrit la métaprogrammation comme suit :

> La `métaprogrammation` est une technique de programmation dans laquelle les programmes informatiques ont la capacité de traiter d'autres programmes comme leurs données. Cela signifie qu'un programme peut être conçu pour lire, générer, analyser ou transformer d'autres programmes, et même se modifier lui-même pendant son exécution.

En termes simples, la métaprogrammation implique l'écriture de code qui peut

* Générer du code
* Manipuler des constructions de langage au moment de l'exécution. Ce phénomène est connu sous le nom de `métaprogrammation réflexive` ou `réflexion`.

## **Qu'est-ce que la réflexion en métaprogrammation ?**

La `réflexion` est une branche de la métaprogrammation. La réflexion a trois sous-branches :

1. **Introspection** : Le code est capable de s'inspecter lui-même. Il est utilisé pour accéder aux propriétés internes de sorte que nous pouvons obtenir des informations de bas niveau sur notre code.
2. **Auto-modification** : Comme le nom l'indique, le code est capable de se modifier lui-même.
3. **Intercession** : Le sens littéral de l'intercession est d'agir au nom de quelqu'un d'autre. En métaprogrammation, l'intercession fait exactement cela en utilisant des concepts comme l'encapsulation, le piégeage, l'interception.

ES6 nous donne l'objet `Reflect` (aka l'API Reflect) pour atteindre l'`introspection`. L'objet `Proxy` de ES6 nous aide avec l'`intercession`. Nous ne parlerons pas trop de l'`auto-modification` car nous voulons nous en éloigner autant que possible.

Attendez une seconde ! Juste pour être clair, la métaprogrammation n'a pas été introduite dans ES6. Elle était plutôt disponible dans le langage depuis sa création. ES6 l'a simplement rendue beaucoup plus facile à utiliser.

## **L'ère pré-ES6 de la métaprogrammation**

Vous vous souvenez de `eval` ? Jetons un coup d'œil à la façon dont il était utilisé :

```js
const blog = {
    name: 'freeCodeCamp'
}
console.log('Avant eval:', blog);

const key = 'author';
const value = 'Tapas';
testEval = () => eval(`blog.${key} = '${value}'`);

// Appeler la fonction
testEval();

console.log('Après la magie eval:', blog);

```

Comme vous pouvez le remarquer, `eval` a aidé à la génération de code supplémentaire. Dans ce cas, l'objet `blog` a été modifié avec une propriété supplémentaire au moment de l'exécution.

```shell
Avant eval: {name: freeCodeCamp}
Après la magie eval: {name: "freeCodeCamp", author: "Tapas"}

```

### **Introspection**

Avant l'inclusion de l'objet `Reflect` dans ES6, nous pouvions toujours faire de l'introspection. Voici un exemple de lecture de la structure du programme :

```js
var users = {
    'Tom': 32,
    'Bill': 50,
    'Sam': 65
};

Object.keys(users).forEach(name => {
    const age = users[name];
    console.log(`User ${name} is ${age} years old!`);
});

```

Ici, nous lisons la structure de l'objet `users` et nous enregistrons la paire clé-valeur dans une phrase.

```shell
User Tom is 32 years old!
User Bill is 50 years old!
User Sam is 65 years old!

```

### **Auto-modification**

Prenons un objet blog qui a une méthode pour se modifier lui-même :

```js
var blog = {
    name: 'freeCodeCamp',
    modifySelf: function(key, value) {blog[key] = value}
}

```

L'objet `blog` peut se modifier lui-même en faisant ceci :

```js
blog.modifySelf('author', 'Tapas');

```

### **Intercession**

L'`intercession` en métaprogrammation signifie agir ou changer les choses au nom de quelqu'un ou de quelque chose d'autre. La méthode pré-ES6 `Object.defineProperty()` peut changer la sémantique d'un objet :

```js
var sun = {};

Object.defineProperty(sun, 'rises', {
    value: true,
    configurable: false,
    writable: false,
    enumerable: false
});

console.log('sun rises', sun.rises);
sun.rises = false;
console.log('sun rises', sun.rises);

```

Sortie :

```shell
sun rises true
sun rises true

```

Comme vous pouvez le voir, l'objet `sun` a été créé comme un objet normal. Ensuite, la sémantique a été modifiée pour qu'il ne soit pas modifiable.

Maintenant, passons à la compréhension des objets `Reflect` et `Proxy` avec leurs utilisations respectives.

# **L'API Reflect**

Dans ES6, Reflect est un nouvel `objet global` (comme Math) qui fournit un certain nombre de fonctions utilitaires. Certaines de ces fonctions peuvent faire exactement la même chose que les méthodes de `Object` ou `Function`.

Toutes ces fonctions sont des fonctions d'introspection où vous pouvez interroger certains détails internes sur le programme au moment de l'exécution.

Voici la liste des méthodes disponibles de l'objet `Reflect`.

```js
// Méthodes de l'objet Reflect

Reflect.apply()
Reflect.construct()
Reflect.get()
Reflect.has()
Reflect.ownKeys()
Reflect.set()
Reflect.setPrototypeOf()
Reflect.defineProperty()
Reflect.deleteProperty()
Reflect.getOwnPropertyDescriptor()
Reflect.getPrototypeOf()
Reflect.isExtensible()

```

Mais attendez, voici une question : Pourquoi avons-nous besoin d'un nouvel objet API alors que celles-ci pourraient déjà exister ou pourraient être ajoutées à `Object` ou `Function` ?

Confus ? Essayons de comprendre cela.

### **Tout dans un seul espace de noms**

JavaScript avait déjà le support de la réflexion d'objet. Mais ces API n'étaient pas organisées sous un seul espace de noms. Depuis ES6, elles sont maintenant sous `Reflect`.

Toutes les méthodes de l'objet Reflect sont statiques par nature. Cela signifie que vous n'avez pas besoin d'instancier l'objet Reflect en utilisant le mot-clé `new`.

### **Simple à utiliser**

Les méthodes d'`introspection` de `Object` lancent une exception lorsqu'elles ne parviennent pas à compléter l'opération. Cela représente une charge supplémentaire pour le consommateur (le programmeur) de gérer cette exception dans le code.

Vous pouvez préférer le gérer comme un `booléen (true | false)` plutôt que d'utiliser la gestion des exceptions. L'objet Reflect vous aide à faire cela.

Voici un exemple avec Object.defineProperty :

```js
 try {
        Object.defineProperty(obj, name, desc);
    } catch (e) {
        // Gérer l'exception
    }
```

Et avec l'API Reflect :

```js
if (Reflect.defineProperty(obj, name, desc)) {
  // succès
} else {
 // échec (et bien mieux)
}

```

### **L'impression de la fonction de première classe**

Nous pouvons trouver l'existence d'une propriété pour un objet comme (prop in obj). Si nous devons l'utiliser plusieurs fois dans notre code, nous devons créer une fonction en enveloppant ce code.

Dans ES6, l'API Reflect résout ce problème en introduisant une fonction de première classe, `Reflect.has(obj, prop)`.

Regardons un autre exemple : Supprimer une propriété d'objet.

```js
const obj = { bar: true, baz: false};

// Nous définissons cette fonction
function deleteProperty(object, key) {
    delete object[key];
}
deleteProperty(obj, 'bar');

```

Avec l'API Reflect :

```js
// Avec l'API Reflect
Reflect.deleteProperty(obj, 'bar');

```

### **Une manière plus fiable d'utiliser la méthode apply()**

La méthode `apply()` dans ES5 aide à appeler une fonction avec le contexte d'une valeur `this`. Nous pouvons également passer les arguments sous forme de tableau.

```js
Function.prototype.apply.call(func, obj, arr);
// ou
func.apply(obj, arr);

```

Cela est moins fiable car `func` pourrait être un objet qui aurait défini sa propre méthode `apply`.

Dans ES6, nous avons une manière plus fiable et élégante de résoudre cela :

```js
Reflect.apply(func, obj, arr);

```

Dans ce cas, nous obtiendrons une [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError) si `func` n'est pas appelable.

### **Aider d'autres types de réflexion**

Nous verrons ce que cela signifie un peu plus tard lorsque nous apprendrons l'objet `Proxy`. Les méthodes de l'API Reflect peuvent être utilisées avec Proxy dans de nombreux cas d'utilisation.

# **L'objet Proxy**

L'objet `Proxy` de ES6 aide à l'`intercession`.

Comme le nom l'indique, un objet `proxy` aide à agir au nom de quelque chose. Il le fait en virtualisant un autre objet. La virtualisation d'objet fournit des comportements personnalisés à cet objet.

Par exemple, en utilisant l'objet proxy, nous pouvons virtualiser la recherche de propriétés d'objet, l'invocation de fonction, et ainsi de suite. Nous verrons certains de ces détails plus en détail ci-dessous.

Voici quelques termes utiles que vous devez retenir et utiliser :

* La `cible` : Un objet auquel le proxy fournit des comportements personnalisés.
* Le `gestionnaire` : Il s'agit d'un objet qui contient des pièges.
* Le `piège` : Un piège est une méthode qui fournit l'accès aux propriétés de l'objet cible. Cela est réalisé en utilisant les méthodes de l'API Reflect. Chacune des méthodes de piège est mappée avec les méthodes de l'API Reflect.

Vous pouvez l'imaginer comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/flow-1.png)

Un gestionnaire avec une fonction `piège` doit être défini. Ensuite, nous devons créer un objet Proxy en utilisant le gestionnaire et l'objet cible. L'objet Proxy aura toutes les modifications avec les comportements personnalisés appliqués.

C'est parfaitement normal si vous ne comprenez pas encore tout à fait à partir de la description ci-dessus. Nous allons en saisir le sens à travers du code et des exemples dans un instant.

La syntaxe pour créer un objet Proxy est la suivante :

```js
let proxy = new Proxy(target, handler);

```

Il existe de nombreux pièges proxy (fonctions de gestionnaire) disponibles pour accéder et personnaliser un objet cible. Voici la liste de ceux-ci.

```js
handler.apply()
handler.construct()
handler.get()
handler.has()
handler.ownKeys()
handler.set()
handler.setPrototypeOf()
handler.getPrototypeOf()
handler.defineProperty()
handler.deleteProperty()
handler.getOwnPropertyDescriptor()
handler.preventExtensions()
handler.isExtensible()

```

Notez que chacun des pièges a un mappage avec les méthodes de l'objet `Reflect`. Cela signifie que vous pouvez utiliser `Reflect` et `Proxy` ensemble dans de nombreux cas d'utilisation.

## **Comment obtenir des valeurs de propriétés d'objet indisponibles**

Regardons un exemple d'objet `employee` et essayons d'imprimer certaines de ses propriétés :

```js
const employee = {
    firstName: 'Tapas',
    lastName: 'Adhikary'
};

console.log(employee.firstName);
console.log(employee.lastName);
console.log(employee.org);
console.log(employee.fullName);

```

La sortie attendue est la suivante :

```shell
Tapas
Adhikary
undefined
undefined

```

Maintenant, utilisons l'objet Proxy pour ajouter un comportement personnalisé à l'objet `employee`.

### **Étape 1 : Créer un gestionnaire qui utilise un piège get**

Nous utiliserons un piège appelé `get` qui nous permet d'obtenir une valeur de propriété. Voici notre gestionnaire :

```js
let handler = {
    get: function(target, fieldName) {

        if(fieldName === 'fullName' ) {
            return `${target.firstName} ${target.lastName}`;
        }

        return fieldName in target ?
            target[fieldName] :
                `No such property as, '${fieldName}'!`

    }
};

```

Le gestionnaire ci-dessus aide à créer la valeur pour la propriété `fullName`. Il ajoute également un message d'erreur plus clair lorsqu'une propriété d'objet est manquante.

### **Étape 2 : Créer un objet Proxy**

Comme nous avons l'objet cible `employee` et le gestionnaire, nous pourrons créer un objet Proxy comme ceci :

```js
let proxy = new Proxy(employee, handler);

```

### **Étape 3 : Accéder aux propriétés sur l'objet Proxy**

Maintenant, nous pouvons accéder aux propriétés de l'objet employee en utilisant l'objet proxy, comme ceci :

```js
console.log(proxy.firstName);
console.log(proxy.lastName);
console.log(proxy.org);
console.log(proxy.fullName);

```

La sortie sera :

```shell
Tapas
Adhikary
No such property as, 'org'!
Tapas Adhikary

```

Remarquez comment nous avons magiquement changé les choses pour l'objet `employee` !

## **Proxy pour la validation des valeurs**

Créons un objet proxy pour valider une valeur entière.

### **Étape 1 : Créer un gestionnaire qui utilise un piège set**

Le gestionnaire ressemble à ceci :

```js
const validator = {
    set: function(obj, prop, value) {
        if (prop === 'age') {
            if(!Number.isInteger(value)) {
                throw new TypeError('Age is always an Integer, Please Correct it!');
            }
            if(value < 0) {
                throw new TypeError('This is insane, a negative age?');
            }
        }
    }
};

```

### **Étape 2 : Créer un objet Proxy**

Créez un objet proxy comme ceci :

```js
let proxy = new Proxy(employee, validator);

```

### **Étape 3 : Assigner une valeur non entière à une propriété, par exemple, age**

Essayez de faire ceci :

```js
proxy.age = 'I am testing a blunder'; // valeur de chaîne

```

La sortie sera comme ceci :

```shell
TypeError: Age is always an Integer, Please Correct it!
    at Object.set (E:\Projects\KOSS\metaprogramming\js-mtprog\proxy\userSetProxy.js:28:23)
    at Object.<anonymous> (E:\Projects\KOSS\metaprogramming\js-mtprog\proxy\userSetProxy.js:40:7)
    at Module._compile (module.js:652:30)
    at Object.Module._extensions..js (module.js:663:10)
    at Module.load (module.js:565:32)
    at tryModuleLoad (module.js:505:12)
    at Function.Module._load (module.js:497:3)
    at Function.Module.runMain (module.js:693:10)
    at startup (bootstrap_node.js:188:16)
    at bootstrap_node.js:609:3

```

De même, essayez de faire ceci :

```js
p.age = -1; // entraînera une erreur

```

## **Comment utiliser Proxy et Reflect ensemble**

Voici un exemple de gestionnaire où nous utilisons des méthodes de l'API Reflect :

```js
const employee = {
    firstName: 'Tapas',
    lastName: 'Adhikary'
};

let logHandler = {
    get: function(target, fieldName) {
        console.log("Log: ", target[fieldName]);
        
        // Utiliser la méthode get de l'objet Reflect
        return Reflect.get(target, fieldName);
    }
};

let func = () => {
    let p = new Proxy(employee, logHandler);
    p.firstName;
    p.lastName;
};

func();
```

## **Quelques autres cas d'utilisation de Proxy**

Il existe plusieurs autres cas d'utilisation où ce concept peut être utilisé.

* Pour protéger le champ _ID_ d'un objet contre la suppression (piège : deleteProperty)
* Pour tracer les accès aux propriétés (piège : get, set)
* Pour la liaison de données (piège : set)
* Avec des références révocables
* Pour manipuler le comportement de l'opérateur `in`

... et bien d'autres.

# **Pièges de la métaprogrammation**

Bien que le concept de `métaprogrammation` nous donne beaucoup de pouvoir, la magie peut parfois mal tourner.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/black_magic.gif)
_Faites attention à l'autre côté de la magie_

Faites attention à :

* Trop de `magie` ! Assurez-vous de la comprendre avant de l'appliquer.
* Possibles impacts sur les performances lorsque vous rendez l'impossible possible
* Peut être vu comme du contre-débogage.

# **En résumé**

Pour résumer,

* `Reflect` et `Proxy` sont de grandes inclusions dans JavaScript pour aider à la métaprogrammation.
* De nombreuses situations complexes peuvent être gérées avec leur aide.
* Soyez conscient des inconvénients également.
* Les [Symboles ES6](https://blog.greenroots.info/explain-me-like-i-am-five-what-are-es6-symbols-ckeuz5sb8001qafs14of305dw) peuvent également être utilisés avec vos classes et objets existants pour changer leur comportement.

J'espère que vous avez trouvé cet article instructif. Tout le code source utilisé dans cet article peut être trouvé dans mon [dépôt GitHub](https://github.com/atapas/js-mtprog).

Veuillez partager l'article afin que d'autres puissent le lire également. Vous pouvez me mentionner sur Twitter ([@tapasadhikary](https://twitter.com/tapasadhikary)) avec des commentaires, ou n'hésitez pas à me suivre.