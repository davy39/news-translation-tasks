---
title: Fermetures, Fonctions Currifiées et Abstractions Intéressantes en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-26T14:56:12.000Z'
originalURL: https://freecodecamp.org/news/playing-around-with-closures-currying-and-cool-abstractions
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/curry.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: Web Development
  slug: web-development
seo_title: Fermetures, Fonctions Currifiées et Abstractions Intéressantes en JavaScript
seo_desc: 'By TK

  In this article, we will talk about closures and curried functions and we''ll play
  around with these concepts to build cool abstractions. I want to show the idea behind
  each concept, but also make it very practical with examples and refactored c...'
---

Par TK

Dans cet article, nous allons parler des fermetures et des fonctions currifiées, et nous allons explorer ces concepts pour construire des abstractions intéressantes. Je veux montrer l'idée derrière chaque concept, mais aussi les rendre très pratiques avec des exemples et du code refactorisé pour les rendre plus amusants.

## Fermetures

Les fermetures sont un sujet courant en JavaScript, et c'est celui par lequel nous allons commencer. Selon MDN :

> Une fermeture est la combinaison d'une fonction regroupée (enfermée) avec des références à son état environnant (l'environnement lexical).

En gros, chaque fois qu'une fonction est créée, une fermeture est également créée et elle donne accès à l'état (variables, constantes, fonctions, etc.). L'état environnant est connu sous le nom d'`environnement lexical`.

Montrons un exemple simple :

```javascript
function makeFunction() {
  const name = 'TK';
  function displayName() {
    console.log(name);
  }
  return displayName;
};

```

Que avons-nous ici ?

* Notre fonction principale s'appelle `makeFunction`
* Une constante nommée `name` est assignée avec la chaîne de caractères, `'TK'`
* La définition de la fonction `displayName` (qui se contente de logger la constante `name`)
* Et enfin, `makeFunction` retourne la fonction `displayName`

Ce n'est qu'une définition de fonction. Lorsque nous appelons `makeFunction`, elle créera tout ce qui est à l'intérieur : une constante et une autre fonction, dans ce cas.

Comme nous le savons, lorsque la fonction `displayName` est créée, la fermeture est également créée et elle rend la fonction consciente de son environnement, dans ce cas, la constante `name`. C'est pourquoi nous pouvons `console.log` la constante `name` sans rien casser. La fonction connaît l'environnement lexical.

```javascript
const myFunction = makeFunction();
myFunction(); // TK

```

Super ! Cela fonctionne comme prévu. La valeur de retour de `makeFunction` est une fonction que nous stockons dans la constante `myFunction`. Lorsque nous appelons `myFunction`, elle affiche `TK`.

Nous pouvons également la faire fonctionner comme une fonction fléchée :

```javascript
const makeFunction = () => {
  const name = 'TK';
  return () => console.log(name);
};

```

Mais que se passe-t-il si nous voulons passer le nom et l'afficher ? Simple ! Utilisez un paramètre :

```javascript
const makeFunction = (name = 'TK') => {
  return () => console.log(name);
};

// Ou en une seule ligne
const makeFunction = (name = 'TK') => () => console.log(name);

```

Maintenant, nous pouvons jouer avec le nom :

```javascript
const myFunction = makeFunction();
myFunction(); // TK

const myFunction = makeFunction('Dan');
myFunction(); // Dan

```

`myFunction` est consciente de l'argument qui est passé, qu'il s'agisse d'une valeur par défaut ou dynamique.

La fermeture garantit que la fonction créée est non seulement consciente des constantes/variables, mais aussi des autres fonctions à l'intérieur de la fonction.

Donc, cela fonctionne également :

```javascript
const makeFunction = (name = 'TK') => {
  const display = () => console.log(name);
  return () => display();
};

const myFunction = makeFunction();
myFunction(); // TK

```

La fonction retournée connaît la fonction `display` et est capable de l'appeler.

Une technique puissante consiste à utiliser les fermetures pour créer des fonctions et des variables "privées".

Il y a quelques mois, j'apprenais les structures de données (encore !) et je voulais implémenter chacune d'elles. Mais j'utilisais toujours l'approche orientée objet. En tant qu'enthousiaste de la programmation fonctionnelle, je voulais construire toutes les structures de données en suivant les principes de la FP (fonctions pures, immutabilité, transparence référentielle, etc.).

La première structure de données que j'apprenais était la Pile. Elle est assez simple. L'API principale est :

* `push` : ajouter un élément à la première place de la pile
* `pop` : supprimer le premier élément de la pile
* `peek` : obtenir le premier élément de la pile
* `isEmpty` : vérifier si la pile est vide
* `size` : obtenir le nombre d'éléments que la pile contient

Nous pourrions clairement créer une fonction simple pour chaque "méthode" et lui passer les données de la pile. Elle pourrait alors utiliser/transformer les données et les retourner.

Mais nous pouvons également créer une pile avec des données privées et n'exposer que les méthodes de l'API. Faisons cela !

```javascript
const buildStack = () => {
  let items = [];

  const push = (item) => items = [item, ...items];
  const pop = () => items = items.slice(1);
  const peek = () => items[0];
  const isEmpty = () => !items.length;
  const size = () => items.length;

  return {
    push,
    pop,
    peek,
    isEmpty,
    size,
  };
};

```

Parce que nous avons créé la pile `items` à l'intérieur de notre fonction `buildStack`, elle est "privée". Elle ne peut être accessible qu'à l'intérieur de la fonction. Dans ce cas, seules `push`, `pop`, etc. pourraient toucher les données. C'est exactement ce que nous recherchons.

Et comment l'utilisons-nous ? Comme ceci :

```javascript
const stack = buildStack();

stack.isEmpty(); // true

stack.push(1); // [1]
stack.push(2); // [2, 1]
stack.push(3); // [3, 2, 1]
stack.push(4); // [4, 3, 2, 1]
stack.push(5); // [5, 4, 3, 2, 1]

stack.peek(); // 5
stack.size(); // 5
stack.isEmpty(); // false

stack.pop(); // [4, 3, 2, 1]
stack.pop(); // [3, 2, 1]
stack.pop(); // [2, 1]
stack.pop(); // [1]

stack.isEmpty(); // false
stack.peek(); // 1
stack.pop(); // []
stack.isEmpty(); // true
stack.size(); // 0

```

Ainsi, lorsque la pile est créée, toutes les fonctions sont conscientes des données `items`. Mais à l'extérieur de la fonction, nous ne pouvons pas accéder à ces données. Elles sont privées. Nous modifions simplement les données en utilisant l'API intégrée de la pile.

## **Curry**

> "La currification est le processus de prise d'une fonction avec plusieurs arguments et de la transformer en une séquence de fonctions chacune avec un seul argument."
> - [Frontend Interview](https://frontendinterview.co/question/what-is-currying-function?tech=javascript)

Imaginez donc que vous avez une fonction avec plusieurs arguments : `f(a, b, c)`. En utilisant la currification, nous obtenons une fonction `f(a)` qui retourne une fonction `g(b)` qui retourne une fonction `h(c)`.

En gros : `f(a, b, c)` > `f(a) => g(b) => h(c)`

Construisons un exemple simple qui additionne deux nombres. Mais d'abord, sans currification :

```javascript
const add = (x, y) => x + y;
add(1, 2); // 3

```

Super ! Très simple ! Ici, nous avons une fonction avec deux arguments. Pour la transformer en une fonction currifiée, nous avons besoin d'une fonction qui reçoit `x` et retourne une fonction qui reçoit `y` et retourne la somme des deux valeurs.

```javascript
const add = (x) => {
  function addY(y) {
    return x + y;
  }

  return addY;
};

```

Nous pouvons refactoriser `addY` en une fonction fléchée anonyme :

```javascript
const add = (x) => {
  return (y) => {
    return x + y;
  }
};

```

Ou la simplifier en construisant des fonctions fléchées en une ligne :

```javascript
const add = (x) => (y) => x + y;

```

Ces trois différentes fonctions currifiées ont le même comportement : construire une séquence de fonctions avec un seul argument.

Comment pouvons-nous l'utiliser ?

```javascript
add(10)(20); // 30

```

Au premier abord, cela peut sembler un peu étrange, mais il y a une logique derrière cela. `add(10)` retourne une fonction. Et nous appelons cette fonction avec la valeur `20`.

Cela revient au même que :

```javascript
const addTen = add(10);
addTen(20); // 30

```

Et c'est intéressant. Nous pouvons générer des fonctions spécialisées en appelant la première fonction. Imaginez que nous voulons une fonction `increment`. Nous pouvons la générer à partir de notre fonction `add` en passant `1` comme valeur.

```javascript
const increment = add(1);
increment(9); // 10

```

Lorsque j'implémentais [Lazy Cypress](https://github.com/leandrotk/lazy-cypress), une bibliothèque npm pour enregistrer le comportement de l'utilisateur sur une page de formulaire et générer du code de test Cypress, je voulais construire une fonction pour générer cette chaîne `input[data-testid="123"]`. J'avais donc l'élément (`input`), l'attribut (`data-testid`), et la valeur (`123`). L'interpolation de cette chaîne en JavaScript ressemblerait à ceci : `${element}[${attribute}="${value}"]`.

Ma première implémentation consistait à recevoir ces trois valeurs comme paramètres et à retourner la chaîne interpolée ci-dessus :

```javascript
const buildSelector = (element, attribute, value) =>
  `${element}[${attribute}="${value}"]`;

buildSelector('input', 'data-testid', 123); // input[data-testid="123"]

```

Et c'était super. J'ai obtenu ce que je cherchais.

Mais en même temps, je voulais construire une fonction plus idiomatique. Quelque chose où je pourrais écrire "P_rendre l'élément X avec l'attribut Y et la valeur Z_ ". Donc si nous décomposons cette phrase en trois étapes :

* "_prendre un élément X_" : `get(x)`
* "_avec l'attribut Y_" : `withAttribute(y)`
* "_et la valeur Z_" : `andValue(z)`

Nous pouvons transformer `buildSelector(x, y, z)` en `get(x)` > `withAttribute(y)` > `andValue(z)` en utilisant le concept de currification.

```javascript
const get = (element) => {
  return {
    withAttribute: (attribute) => {
      return {
        andValue: (value) => `${element}[${attribute}="${value}"]`,
      }
    }
  };
};

```

Ici, nous utilisons une idée différente : retourner un objet avec une fonction comme clé-valeur. Ensuite, nous pouvons obtenir cette syntaxe : `get(x).withAttribute(y).andValue(z)`.

Et pour chaque objet retourné, nous avons la fonction suivante et l'argument.

Temps de refactorisation ! Supprimons les instructions `return` :

```javascript
const get = (element) => ({
  withAttribute: (attribute) => ({
    andValue: (value) => `${element}[${attribute}="${value}"]`,
  }),
});

```

Je pense que cela a l'air plus joli. Et voici comment nous l'utilisons :

```javascript
const selector = get('input')
  .withAttribute('data-testid')
  .andValue(123);

selector; // input[data-testid="123"]

```

La fonction `andValue` connaît les valeurs `element` et `attribute` car elle est consciente de l'environnement lexical comme avec les fermetures dont nous avons parlé auparavant.

Nous pouvons également implémenter des fonctions en utilisant la "currification partielle" en séparant le premier argument du reste, par exemple.

Après avoir fait du développement web pendant longtemps, je suis très familier avec l'[API Web des écouteurs d'événements](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener). Voici comment l'utiliser :

```javascript
const log = () => console.log('clicked');
button.addEventListener('click', log);

```

Je voulais créer une abstraction pour construire des écouteurs d'événements spécialisés et les utiliser en passant l'élément et un gestionnaire de rappel.

```javascript
const buildEventListener = (event) => (element, handler) => element.addEventListener(event, handler);

```

De cette façon, je peux créer différents écouteurs d'événements spécialisés et les utiliser comme des fonctions.

```javascript
const onClick = buildEventListener('click');
onClick(button, log);

const onHover = buildEventListener('hover');
onHover(link, log);

```

Avec tous ces concepts, j'ai pu créer une requête SQL en utilisant la syntaxe JavaScript. Je voulais interroger des données JSON comme ceci :

```javascript
const json = {
  "users": [
    {
      "id": 1,
      "name": "TK",
      "age": 25,
      "email": "tk@mail.com"
    },
    {
      "id": 2,
      "name": "Kaio",
      "age": 11,
      "email": "kaio@mail.com"
    },
    {
      "id": 3,
      "name": "Daniel",
      "age": 28,
      "email": "dani@mail.com"
    }
  ]
}

```

J'ai donc construit un moteur simple pour gérer cette implémentation :

```javascript
const startEngine = (json) => (attributes) => ({ from: from(json, attributes) });

const buildAttributes = (node) => (acc, attribute) => ({ ...acc, [attribute]: node[attribute] });

const executeQuery = (attributes, attribute, value) => (resultList, node) =>
  node[attribute] === value
    ? [...resultList, attributes.reduce(buildAttributes(node), {})]
    : resultList;

const where = (json, attributes) => (attribute, value) =>
  json
    .reduce(executeQuery(attributes, attribute, value), []);

const from = (json, attributes) => (node) => ({ where: where(json[node], attributes) });

```

Avec cette implémentation, nous pouvons démarrer le moteur avec les données JSON :

```javascript
const select = startEngine(json);

```

Et l'utiliser comme une requête SQL :

```javascript
select(['id', 'name'])
  .from('users')
  .where('id', 1);

result; // [{ id: 1, name: 'TK' }]

```

C'est tout pour aujourd'hui. Je pourrais continuer à vous montrer de nombreux exemples différents d'abstractions, mais je vais vous laisser jouer avec ces concepts.

Vous pouvez trouver d'autres articles comme celui-ci [sur mon blog](https://leandrotk.github.io/tk/2020/03/closure-currying-and-cool-abstractions/index.html).

Mon [Twitter](https://twitter.com/leandrotk_) et [Github](https://github.com/leandrotk).

## Ressources

* [Code source de l'article de blog](https://github.com/tk-notes/blog/tree/master/closures-currying-and-cool-abstractions)
* [Fermetures | MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
* [Currying | Fun Fun Function](https://www.youtube.com/watch?v=iZLP4qOwY8I)
* [Apprendre React en construisant une application](https://alterclass.io/?ref=5ec57f513c1321001703dcd2)