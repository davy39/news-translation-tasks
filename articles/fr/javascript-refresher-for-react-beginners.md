---
title: Rafraîchissement JavaScript pour les débutants en React – Concepts clés de
  JS à connaître
subtitle: ''
author: Niladri S. Jyoti
co_authors: []
series: null
date: '2024-10-08T15:17:20.457Z'
originalURL: https://freecodecamp.org/news/javascript-refresher-for-react-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727978962525/ee0aad46-7497-4c91-9354-dd8b0f9b4ea6.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: Frontend Development
  slug: frontend-development
- name: Beginner Developers
  slug: beginners
- name: Learning Journey
  slug: learning-journey
seo_title: Rafraîchissement JavaScript pour les débutants en React – Concepts clés
  de JS à connaître
seo_desc: 'The Back Story

  A few years ago, I was introduced to React and immediately fell in love with its
  component-based, state-driven approach to building web applications.

  But as I delved deeper into its ecosystem, I encountered not just React, but a range
  ...'
---

## L'histoire derrière

Il y a quelques années, j'ai été introduit à React et j'ai immédiatement adoré son approche basée sur les composants et pilotée par l'état pour construire des applications web.

Mais alors que je plongeais plus profondément dans son écosystème, j'ai rencontré non seulement React, mais aussi une gamme de bibliothèques de support comme Material UI, React Router, Reactstrap, Redux, et plus encore. Bien que passionnant, ces nouveaux concepts et bibliothèques pouvaient aussi sembler écrasants.

J'ai rapidement réalisé que la maîtrise de React nécessite une solide compréhension de JavaScript moderne, en particulier des fonctionnalités ES6+. Cette réalisation m'a encouragé à revisiter certains sujets fondamentaux de JavaScript, ce qui m'a aidé à devenir plus à l'aise avec React et à écrire un code plus propre et plus efficace.

Dans ce guide, je vais partager mes notes comme référence concise et pratique. Ces concepts clés de JavaScript vous donneront une base solide avant de plonger profondément dans React. Que vous soyez débutant ou que vous revisitiez le langage, ce guide devrait vous donner un coup de pouce alors que vous abordez l'écosystème React.

## Retour au travail

Puisque React est basé sur JavaScript, il est essentiel d'avoir une bonne maîtrise du langage avant de commencer à apprendre React.

Je recommande une ressource complète comme [The Modern JavaScript Tutorial](https://javascript.info/) pour une révision approfondie. Mais si vous vous sentez confiant concernant la plupart de JavaScript et que vous avez juste besoin d'une remise à niveau, voici ma liste recommandée de sujets cruciaux :

1. [Modèles littéraux](#heading-1-modèles-littéraux)

2. [Fonctions fléchées](#heading-2-fonctions-fléchées)

3. [Paramètres par défaut (ou valeurs)](#heading-3-paramètres-par-défaut-ou-valeurs)

4. [Destructuration des objets et des tableaux](#heading-4-destructuration-des-objets-et-des-tableaux)

5. [Opérateurs Rest et Spread](#heading-5-opérateurs-rest-et-spread)

6. [Méthodes Map, Filter et Reduce](#heading-6-méthodes-map-filter-et-reduce)

7. [Problèmes de mutabilité avec des méthodes comme Array Sort](#heading-7-problèmes-de-mutabilité-avec-des-méthodes-comme-array-sort)

8. [Opérateur ternaire](#heading-8-opérateur-ternaire)

9. [Court-circuit et opérateurs logiques](#heading-9-court-circuit-et-opérateurs-logiques)

10. [Chaînage optionnel](#heading-10-chaînage-optionnel)

11. [JS asynchrone (Callbacks, Promesses, Async/Await)](#heading-11-js-asynchrone-callbacks-promesses-asyncawait)

12. [Fermetures](#heading-12-fermetures)

13. [Modules (import/export)](#heading-13-modules-importexport)

14. [Gestion des événements et propagation](#heading-14-gestion-des-événements-et-propagation)

15. [Classes et prototypes](#heading-15-classes-et-prototypes)

## 1. Modèles littéraux

Les modèles littéraux simplifient l'interpolation de chaînes et la mise en forme de texte multiline. En utilisant des backticks (`` `___` ``), vous pouvez intégrer des expressions dans des chaînes avec `${}`. Cela facilite la concaténation de variables et d'expressions avec du texte, éliminant le besoin de concaténation de chaînes fastidieuse.

```javascript
let numEggs = 4;

console.log(`Au petit-déjeuner, je mange ${numEggs} œufs.`);
// Sortie : Au petit-déjeuner, je mange 4 œufs.

console.log(`Aujourd'hui, j'ai mangé seulement la moitié, j'ai mangé juste ${numEggs/2} œufs.`);
// Sortie : Aujourd'hui, j'ai mangé seulement la moitié, j'ai mangé juste 2 œufs.
```

De plus, les modèles littéraux supportent les chaînes multiline (sans avoir besoin du caractère de nouvelle ligne, c'est-à-dire `\n`, et vous pouvez aussi ajouter des espaces). Cela permet aux développeurs de créer un code plus lisible et organisé.

```javascript
console.log(`Aujourd'hui, j'ai eu :
- Petit-déjeuner
- Déjeuner
- Dîner`);
/* Sortie (affiche maintenant le texte multiline comme montré ci-dessous) :
Aujourd'hui, j'ai eu :
- Petit-déjeuner
- Déjeuner
- Dîner
*/
```

Avec leur flexibilité et leur clarté, les modèles littéraux sont devenus une méthode préférée pour gérer les chaînes et le contenu dynamique en JavaScript moderne.

## 2. Fonctions fléchées

Les fonctions fléchées fournissent une syntaxe plus concise pour écrire des fonctions et lient automatiquement `this` au contexte dans lequel elles sont déclarées. Elles sont un pilier du développement React, car elles simplifient les gestionnaires d'événements, les méthodes de cycle de vie et d'autres logiques fonctionnelles. Explorons différentes variations des fonctions fléchées.

**Fonction fléchée avec un seul argument :** Lorsque une fonction fléchée a un seul argument, vous pouvez omettre les parenthèses. Voici un exemple :

```javascript
const greet = name => `Bonjour, ${name}!`;
console.log(greet('John')); // Bonjour, John!
```

**Fonction fléchée sans arguments :** Si il n'y a pas d'arguments, vous devez toujours utiliser des parenthèses.

```javascript
const sayHello = () => 'Bonjour, le monde!';
console.log(sayHello()); // Bonjour, le monde!
```

**Fonction fléchée avec plusieurs arguments :** Pour plusieurs arguments, les parenthèses sont obligatoires.

```javascript
const add = (a, b) => a + b;
console.log(add(2, 3)); // 5
```

**Corps de fonction sur une seule ligne (Retour implicite) :** Lorsque le corps de la fonction est une seule expression, vous pouvez omettre le mot-clé `return` et les accolades. Cela est connu comme un retour implicite.

```javascript
const multiply = (x, y) => x * y;
console.log(multiply(4, 5)); // 20
```

**Corps de fonction sur plusieurs lignes :** Pour une logique plus complexe ou plusieurs instructions, vous avez besoin d'accolades, et un `return` explicite est requis si la fonction retourne une valeur.

```javascript
const getFullName = (firstName, lastName) => {
  const fullName = `${firstName} ${lastName}`;
  return fullName;
};
console.log(getFullName('John', 'Doe')); // John Doe
```

**Retourner un objet :** Pour retourner un objet directement, enveloppez l'objet dans des parenthèses pour éviter la confusion avec le corps de la fonction.

```javascript
const createUser = (name, age) => ({ name, age });
console.log(createUser('Alice', 30)); // { name: 'Alice', age: 30 }
```

**Fonctions fléchées dans les rappels :** Les fonctions fléchées sont souvent utilisées comme rappels pour les méthodes de tableau comme `map`, `filter`, et `reduce`.

```javascript
const numbers = [1, 2, 3, 4];
const squares = numbers.map(num => num * num);
console.log(squares); // [1, 4, 9, 16]
```

Pour en savoir plus sur la façon dont les fonctions fléchées se comparent à d'autres façons de définir des fonctions, vous pouvez lire ce blog sur [les façons d'écrire des fonctions JS](https://medium.com/stackademic/3-common-ways-of-writing-functions-1fc62f478fe3).

## 3. Paramètres par défaut (ou valeurs)

Les paramètres par défaut permettent aux fonctions d'avoir des valeurs prédéfinies si aucun argument n'est passé, ou lorsqu'un argument est `undefined`. Cette fonctionnalité est utile lors de l'écriture de composants flexibles dans React, où vous ne passez pas toujours chaque prop ou argument.

```javascript
function greet(name = 'Inconnu') {
  console.log(`Bonjour, ${name}!`);
}
greet(); // Bonjour, Inconnu!
greet('Alice'); // Bonjour, Alice!
```

Il est pertinent de mentionner ici qu'il existe une autre approche couramment utilisée en JavaScript, qui consiste à utiliser des opérateurs logiques comme `||` pour définir une valeur par défaut lorsque la valeur donnée est falsy (c'est-à-dire, des valeurs comme `0`, `null`, `undefined`, `false`, ou `""`).

```javascript
function greet(name) {
  const finalName = name || 'Inconnu';
  console.log(`Bonjour, ${finalName}!`);
}

greet(); // Bonjour, Inconnu!
greet(''); // Bonjour, Inconnu!
greet('John'); // Bonjour, John!
```

Le processus ci-dessus utilise un concept appelé court-circuit des opérateurs logiques, qui est discuté dans la section 9 ci-dessous.

## 4. Destructuration des objets et des tableaux

La destructuration permet d'extraire des valeurs des tableaux et des propriétés des objets dans des variables. Cette syntaxe concise rend votre code plus propre et plus lisible.

Pour extraire des valeurs spécifiques d'un tableau ou d'un objet, utilisez la destructuration en enfermant les variables souhaitées dans des accolades pour les objets ou des crochets pour les tableaux.

```javascript
// Exemple de destructuration de tableau
const [first, second] = [10, 20];
console.log(first); // 10
```

```javascript
// Exemple de destructuration d'objet
const user = { name: 'Alice', age: 25 };
const { name, age } = user;
console.log(name); // Alice
```

La destructuration est couramment utilisée dans React pour gérer les props et l'état. Pour voir des cas d'utilisation plus spécifiques de la destructuration avec des exemples de code, lisez ce [guide rapide sur la destructuration](https://medium.com/@codenil/destructuring-a-quick-reference-a7b2fa09c88a).

## 5. Opérateurs Rest et Spread

Les opérateurs Rest et Spread sont incroyablement polyvalents et largement utilisés en JavaScript. Les deux sont représentés par trois points (`...`), mais leurs significations diffèrent selon le contexte dans lequel ils sont utilisés.

### Opérateur Spread : Développe les éléments d'un tableau ou d'un objet.

L'opérateur Spread est principalement utilisé pour déballer les tableaux ou les objets en éléments individuels. Cela est particulièrement utile pour créer des copies superficielles ou fusionner des tableaux (et des objets) sans muter l'original.

```javascript
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];
console.log(arr2); // [1, 2, 3, 4, 5]

/* arr2 est créé en développant les éléments de arr1
 et en ajoutant des valeurs supplémentaires */
```

L'opérateur Spread peut également être utilisé pour copier des objets ou combiner des objets :

```javascript
const obj1 = { name: 'Alice', age: 25 };
const obj2 = { ...obj1, job: 'Ingénieur' };
console.log(obj2); // { name: 'Alice', age: 25, job: 'Ingénieur' }

/* obj2 est créé en développant les propriétés de obj1
 et en ajoutant une nouvelle propriété */
```

C'est un modèle courant lors de la mise à jour de l'état dans les applications React.

### Opérateur Rest : Collecte plusieurs éléments dans un tableau.

L'opérateur Rest fait l'inverse : il collecte plusieurs arguments ou éléments dans un seul tableau. Il est particulièrement utile lorsque vous travaillez avec des fonctions variadiques (fonctions qui acceptent un nombre variable d'arguments).

```javascript
function sum(...args) {
  return args.reduce((total, num) => total + num, 0);
}
console.log(sum(1, 2, 3)); // 6
```

Dans cet exemple, `...args` rassemble tous les arguments passés à la fonction dans un tableau. Cela permet à la fonction de gérer dynamiquement n'importe quel nombre d'arguments.

Vous pouvez également utiliser l'opérateur Rest pour collecter les propriétés restantes d'un objet ou les éléments d'un tableau :

```javascript
const [first, ...rest] = [10, 20, 30, 40];
console.log(first); // 10
console.log(rest);  // [20, 30, 40]
```

Cette technique est particulièrement utile dans React lorsque vous travaillez avec des props, où vous pourriez vouloir extraire des propriétés spécifiques et passer le reste aux composants enfants.

## 6. Méthodes Map, Filter et Reduce

Les méthodes `map()`, `filter()`, et `reduce()` sont incroyablement puissantes pour la manipulation de tableaux en JavaScript, et elles jouent un rôle crucial dans React pour des tâches comme le rendu de listes, le filtrage de données et la synthèse d'informations.

* **Map** : Transforme les éléments d'un tableau

* **Filter** : Crée un nouveau tableau avec les éléments qui passent une condition

* **Reduce** : Accumule les valeurs en un seul résultat

### 1. Méthode Map

La méthode `map()` crée un nouveau tableau en transformant chaque élément du tableau original selon la fonction fournie. Cette méthode est essentielle dans React pour le rendu dynamique de listes de composants à partir de tableaux de données.

```javascript
// Exemple (Utilisation de base) :
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(num => num * 2);
console.log(doubled); // [2, 4, 6, 8]
```

Dans React, `map()` est couramment utilisé pour rendre des listes de composants. Voici comment vous pourriez l'utiliser dans un composant React :

```javascript
// Exemple (Rendu d'une liste dans React) :
const users = [
  { id: 1, name: 'Alice' },
  { id: 2, name: 'Bob' },
  { id: 3, name: 'Charlie' }
];

function UserList() {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

/* Notez que chaque élément <li> dans la liste a une prop 'key' unique.
Cela est requis par React lors du rendu de listes comme celle-ci */
```

### 2. Méthode Filter

La méthode `filter()` crée un nouveau tableau avec tous les éléments qui passent la condition spécifiée dans la fonction de rappel. Elle est fréquemment utilisée dans React lorsque vous souhaitez afficher uniquement certains éléments en fonction de l'entrée de l'utilisateur ou d'une condition spécifique.

```javascript
// Exemple (Utilisation de base) :
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // [2, 4]
```

Pour un cas d'utilisation, imaginez que vous avez une liste où certaines tâches sont terminées tandis que d'autres ne le sont pas. Vous pouvez donc utiliser `filter()` pour afficher (rendre) uniquement les tâches qui ne sont pas encore terminées.

```javascript
// Exemple (Filtrage de données dans React) :
const todos = [
  { id: 1, task: 'Apprendre JavaScript', completed: true },
  { id: 2, task: 'Apprendre React', completed: false },
  { id: 3, task: 'Construire un projet', completed: false }
];

function TodoList() {
  const incompleteTodos = todos.filter(todo => !todo.completed);
  return (
    <ul>
      {incompleteTodos.map(todo => (
        <li key={todo.id}>{todo.task}</li>
      ))}
    </ul>
  );
}
```

### 3. Méthode Reduce

La méthode `reduce()` exécute une fonction de réduction sur chaque élément du tableau, résultant en une seule valeur de sortie. Elle est utilisée lorsque vous devez accumuler des données, comme la somme de valeurs ou la combinaison d'objets.

```javascript
// Exemple (Utilisation de base) :
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((total, num) => total + num, 0);
console.log(sum); // 10
```

Vous pourriez utiliser `reduce()` dans React pour calculer un résumé de certaines données, comme le prix total des articles dans un panier d'achat, en considérant le prix individuel des articles et leurs quantités :

```javascript
// Exemple (Utilisation de reduce() dans React) :
const cart = [
  { id: 1, name: 'Pomme', price: 1.5, quantity: 3 },
  { id: 2, name: 'Banane', price: 1, quantity: 2 },
  { id: 3, name: 'Orange', price: 2, quantity: 1 }
];

function CartSummary() {
  const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  return (
    <div>
      <h3>Total : ${total}</h3>
    </div>
  );
}
```

Ces méthodes de tableau sont inestimables dans React pour manipuler et afficher des données dynamiquement. Elles permettent une logique propre, lisible et déclarative au sein de vos composants.

Vous pouvez également combiner ces méthodes pour créer des transformations de données puissantes. Par exemple, vous pouvez filtrer un tableau puis mapper les résultats : `filter()` est utilisé pour extraire uniquement les utilisateurs adultes, et `map()` est ensuite utilisé pour créer une liste de leurs noms.

```javascript
// Exemple : utilisation combinée des méthodes filter et map
const users = [
  { id: 1, name: 'Alice', age: 25 },
  { id: 2, name: 'Bob', age: 17 },
  { id: 3, name: 'Charlie', age: 30 }
];

const adultNames = users
  .filter(user => user.age >= 18)
  .map(user => user.name);
console.log(adultNames); // ['Alice', 'Charlie']
```

Les méthodes `map()` et `filter()` sont plus faciles à comprendre car elles suivent une relation simple "un-à-un" ou "un-à-zéro-ou-plus" : `map()` transforme chaque élément en un nouveau, tandis que `filter()` inclut ou exclut des éléments en fonction d'une condition, retournant un tableau de structure similaire.

En revanche, `reduce()` est plus complexe, car il accumule des valeurs en un seul résultat plutôt que de maintenir une relation un-à-un. Il nécessite de gérer à la fois la valeur actuelle et un accumulateur, ce qui le rend conceptuellement différent et plus difficile à interpréter que `map()` ou `filter()`.

La valeur initiale optionnelle dans `reduce()` ajoute à la complexité, car elle définit le point de départ pour l'accumulation. Sans elle, le premier élément du tableau est utilisé comme accumulateur, ce qui peut causer des résultats inattendus avec des tableaux vides ou des données non numériques. Pour obtenir des résultats cohérents pour votre utilisation de la méthode `reduce()`, vous pouvez lire sur [l'importance d'une valeur initiale](https://medium.com/@codenil/the-importance-of-initial-value-in-array-reduce-method-86284878d1e4).

## 7. Problèmes de mutabilité avec des méthodes comme Array Sort

La méthode `Array.sort()` trie les éléments d'un tableau en place, ce qui signifie qu'elle **mute** le tableau original. Par exemple :

```javascript
const numbers = [4, 2, 3, 1];
numbers.sort();
console.log(numbers); // [1, 2, 3, 4]
```

Bien que cela fonctionne en JavaScript pur, c'est problématique dans React, où **l'immuabilité** est cruciale pour gérer correctement l'état.

React détecte les changements d'état en comparant les états précédents et nouveaux et déclenche des re-rendus basés sur ces changements. Mais lorsqu'un tableau est muté en place (comme avec `sort()`), React peut ne pas reconnaître le changement, entraînant des mises à jour de l'interface utilisateur obsolètes ou un comportement imprévisible.

Pour éviter cela, il est préférable de créer une copie en utilisant l'opérateur de propagation (`...`) ou `slice()` avant de trier, garantissant que l'état original reste inchangé :

```javascript
const numbers = [4, 2, 3, 1];
const sortedNumbers = [...numbers].sort();
console.log(sortedNumbers); // [1, 2, 3, 4]
```

Des méthodes comme `map()`, `filter()`, `reduce()`, ou la copie de tableaux/objets avant de les modifier sont essentielles pour préserver l'immuabilité et assurer une gestion d'état fiable dans React.

## 8. Opérateur ternaire

L'opérateur ternaire est un raccourci pour les instructions conditionnelles. Il a la syntaxe `condition ? expressionSiVrai : expressionSiFaux`. Si la condition est évaluée à vrai, il exécute `expressionSiVrai`. Si elle est fausse, il exécute `expressionSiFaux`.

```javascript
let isUserRegistered = true;
let message = isUserRegistered ? 'Veuillez vous connecter' : 'Veuillez vous inscrire';
console.log(message);
// Sortie : Veuillez vous connecter
```

Dans React, c'est un remplacement efficace pour les instructions if-else dans certains scénarios, comme le [rendu conditionnel](https://blog.stackademic.com/conditional-rendering-in-react-four-different-approaches-f25faddf0161), qui délivre des éléments et des composants basés sur certaines conditions ou valeurs des données d'état ou de props.

## 9. Court-circuit et opérateurs logiques

Les opérateurs logiques comme `&&` (ET) et `||` (OU) peuvent être utilisés pour créer une logique conditionnelle propre et concise en JavaScript. Dans React, ces opérateurs déterminent souvent si un composant ou un élément JSX doit être rendu.

### 1. ET logique (`&&`)

L'opérateur `&&` évalue d'abord l'expression du côté gauche. Si elle est `true`, l'expression du côté droit est évaluée et retournée. Si le côté gauche est `false`, l'expression entière est court-circuitée, ce qui signifie que l'expression du côté droit est ignorée.

```javascript
let isLoggedIn = true;
console.log(isLoggedIn && 'Bienvenue à nouveau !'); // Bienvenue à nouveau !
```

Ce comportement est souvent utilisé dans React pour le rendu conditionnel, comme ceci :

```javascript
function UserGreeting({ isLoggedIn }) {
  return (
    <div>
      {isLoggedIn && <p>Bienvenue à nouveau !</p>}
    </div>
  );
}
```

C'est un modèle courant dans React pour rendre l'interface utilisateur en fonction de certaines conditions sans avoir besoin d'une instruction `if` explicite.

### 2. OU logique (`||`)

L'opérateur `||` fonctionne de manière opposée. Il évalue d'abord l'expression du côté gauche, et si elle est `true` (ou toute valeur truthy), il retourne cette valeur. Si l'expression du côté gauche est `false` (ou toute valeur falsy), il évalue et retourne l'expression du côté droit.

```javascript
let username = '';
console.log(username || 'Invité'); // Sortie : Invité
```

Dans React, cela est utile pour fournir des valeurs par défaut, comme ceci :

```javascript
function UserProfile({ username }) {
  return (
    <div>
      <p>Bonjour, {username || 'Invité'} !</p>
    </div>
  );
}
```

Notez que l'**opérateur de coalescence des nuls** (`??`) est similaire à l'opérateur OU logique (`||`), mais avec une différence clé dans la manière dont ils traitent les valeurs **falsy**.

L'opérateur de coalescence des nuls (`??`) vérifie spécifiquement si le côté gauche est soit `null` **ou** `undefined`. Si la valeur est `null` ou `undefined`, il retourne le côté droit. Cela permet à `0`, `false`, et `''` d'être traités comme des valeurs valides et non remplacées. Vous pouvez lire à ce sujet et plus encore sur ces [nuances associées aux opérateurs JavaScript](https://medium.com/@codenil/javascript-operators-some-nuances-57300eb2c354).

### 3. Combinaison de `&&` et `||` pour une logique complexe

Vous pouvez également combiner `&&` et `||` pour créer une logique conditionnelle plus complexe ou imbriquée.

```javascript
let isAdmin = false;
let isLoggedIn = true;
console.log(isAdmin && 'Panneau d'administration' || isLoggedIn && 'Tableau de bord utilisateur');
// Sortie : Tableau de bord utilisateur
```

Cela peut être utile dans React pour décider quoi rendre en fonction de plusieurs conditions ayant une interaction.

```javascript
function Dashboard({ isAdmin, isLoggedIn }) {
  return (
    <div>
      {isAdmin && <p>Bienvenue dans le Panneau d'administration</p>}
      {!isAdmin && isLoggedIn && <p>Bienvenue dans le Tableau de bord utilisateur</p>}
    </div>
  );
}
```

## 10. Chaînage optionnel

Le **chaînage optionnel** (`?.`) est une fonctionnalité puissante introduite dans JavaScript (ES2020) qui permet d'accéder en toute sécurité aux propriétés profondément imbriquées d'un objet sans craindre de rencontrer des erreurs `undefined` ou `null`.

En JavaScript traditionnel, l'accès aux propriétés imbriquées des objets pouvait entraîner des erreurs si une partie de la chaîne était `undefined` ou `null`, provoquant la rupture de votre code. Le chaînage optionnel offre une manière plus propre et plus sûre de gérer ces scénarios.

L'opérateur de chaînage optionnel court-circuite et retourne `undefined` si la valeur avant lui est `null` ou `undefined`. Cela empêche le code de lancer une erreur lors de la tentative d'accès aux propriétés d'une valeur `null` ou `undefined`.

```javascript
let user = { name: 'Alice', address: { city: 'Pays des Merveilles' } };
console.log(user?.address?.city);
// Sortie : Pays des Merveilles

// Sans chaînage optionnel
let user1 = { name: 'Bill' };
console.log(user1.address.city);
// Sortie : Erreur : Impossible de lire la propriété 'city' de undefined

// Avec chaînage optionnel :
let user2 = { name: 'Caleb' };
console.log(user2?.address?.city); // undefined
```

Le chaînage optionnel peut également être utilisé dans différents scénarios, tels que les appels de fonctions (pour vérifier si une fonction existe avant de l'invoquer), l'accès aux éléments des tableaux (surtout lorsque vous n'êtes pas sûr que le tableau existe ou qu'il a suffisamment d'éléments), ou l'accès aux propriétés dynamiques, comme montré ci-dessous :

```javascript
// Chaînage optionnel avec fonctions :
let user1 = {
  name: 'Alice',
  greet: () => 'Bonjour !'
};

console.log(user1.greet?.()); // Bonjour !
console.log(user1.sayGoodbye?.()); // undefined

// Chaînage optionnel avec tableaux :
let users = [{ name: 'Alice' }, { name: 'Bob' }];
console.log(users[0]?.name); // Alice
console.log(users[2]?.name); // undefined

// Chaînage optionnel avec propriétés dynamiques :
let user2 = { name: 'Bill', preferences: { theme: 'sombre' } };
let property = 'preferences';
console.log(user2?.[property]?.theme); // sombre

property = 'settings';
console.log(user2?.[property]?.theme); // undefined
```

Lorsque vous travaillez avec des objets profondément imbriqués, le chaînage optionnel peut vous éviter d'écrire des vérifications de nullité répétitives à chaque niveau.

```javascript
let user = { profile: { address: { city: 'Pays des Merveilles' } } };

// utilisation sans chaînage optionnel (en utilisant le court-circuit) :
if (user && user.profile && user.profile.address && user.profile.address.city) {
  console.log(user.profile.address.city);
}

// utilisation avec chaînage optionnel (évitant les vérifications de nullité répétitives) :
console.log(user?.profile?.address?.city); // Pays des Merveilles
```

Dans React, le chaînage optionnel est particulièrement utile lorsque vous traitez des props, des réponses d'API, ou toute donnée qui peut ne pas toujours être disponible. Il aide à prévenir les erreurs lors du rendu des composants basés sur des données dynamiques ou incomplètes.

Le chaînage optionnel réduit considérablement la complexité de votre code, le rendant plus propre et plus lisible, surtout lorsque vous traitez des structures profondément imbriquées.

```javascript
// Exemple d'utilisation du chaînage optionnel dans React
function UserProfile({ user }) {
  return (
    <div>
      <p>Nom : {user?.name}</p>
      <p>Ville : {user?.address?.city ?? 'Inconnu'}</p>
    </div>
  );
}
```

## 11. JS asynchrone : Callbacks, Promesses, Async/Await

JavaScript est un langage à thread unique, ce qui signifie qu'il peut exécuter une tâche à la fois. Mais la gestion des opérations asynchrones est cruciale, surtout pour des tâches comme la récupération de données dans React. Les fonctions de **rappel** sont l'un des premiers modèles utilisés pour gérer le comportement asynchrone, comme suit :

```javascript
function fetchData(callback) {
  setTimeout(() => {
    console.log("Données récupérées");
    callback({ user: "John", age: 30 });
  }, 2000);
}

fetchData((data) => {
  console.log("Utilisateur :", data.user);
});

/* Sortie :
Données récupérées
Utilisateur : John
*/
```

Ainsi, comme vous pouvez le voir, les rappels sont efficaces pour gérer des opérations simples qui dépendent de tâches asynchrones, comme dans l'exemple ci-dessus.

Mais lorsque plusieurs tâches asynchrones dépendent les unes des autres, les rappels peuvent conduire à un code profondément imbriqué, communément appelé **l'enfer des rappels**.

Pour résoudre ce problème, les **promesses** ont été introduites. Une **promesse** est un objet qui représente l'achèvement éventuel (ou l'échec) d'une opération asynchrone et sa valeur résultante. Au lieu d'imbriquer plusieurs rappels, les promesses permettent le chaînage, conduisant à un code plus structuré et lisible.

De même, l'API Fetch, qui est couramment utilisée pour gérer les requêtes réseau dans les applications React, retourne une promesse que vous pouvez gérer comme suit :

```javascript
function fetchUserDetails(userId) {
  return fetch(`https://api.example.com/users/${userId}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Échec de la récupération des détails de l\'utilisateur');
      }
      return response.json();
    })
    .then((data) => {
      console.log("Détails de l\'utilisateur récupérés");
      return { id: userId, name: data.name };
    });
}

function fetchPostsByUser(user) {
  return fetch(`https://api.example.com/users/${user.id}/posts`)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Échec de la récupération des posts');
      }
      return response.json();
    })
    .then((posts) => {
      console.log(`Posts récupérés pour ${user.name}`);
      return posts;
    });
}

// Chaînage des promesses
fetchUserDetails(1)
  .then((user) => fetchPostsByUser(user))
  .then((posts) => console.log(posts))
  .catch((error) => console.error("Erreur :", error));
```

Les promesses offrent une manière plus lisible de gérer les tâches asynchrones séquentielles. Elles simplifient également la gestion des erreurs en utilisant `.catch()`. Cependant, bien que les promesses éliminent l'imbrication profonde des rappels, le chaînage de trop nombreux appels `.then()` peut encore devenir verbeux et difficile à suivre.

Introduit dans ES2017, `async/await` rend le travail avec les promesses encore plus simple. Avec **async/await**, le code asynchrone ressemble et se comporte plus comme du code synchrone, ce qui améliore grandement la lisibilité. Voici comment cela fonctionne :

* **Fonction async :** Une fonction `async` retourne une promesse. Le mot-clé `async` permet à la fonction de retourner une promesse résolue implicitement.

* **Expression await :** À l'intérieur d'une fonction `async`, `await` pause l'exécution de la fonction jusqu'à ce que la promesse soit résolue. Cela simplifie la gestion des promesses, car nous pouvons directement assigner la valeur résolue à une variable.

```javascript
async function getUserAndPosts(userId) {
  try {
    const user = await fetchUserDetails(userId); // Attend les détails de l'utilisateur
    const posts = await fetchPostsByUser(user);  // Attend les posts
    console.log("Posts :", posts);
  } catch (error) {
    console.error("Erreur :", error);
  }
}

getUserAndPosts(1);

/* Sortie :
Détails de l'utilisateur récupérés
Posts récupérés pour John
Posts : ["Post 1", "Post 2"]
*/
```

`Async/await` rend le code asynchrone apparent comme synchrone, ce qui améliore grandement la lisibilité et la maintenabilité. Le bloc `try/catch` simplifie également la gestion des erreurs, la rendant cohérente avec la manière dont les erreurs sont attrapées dans le code synchrone.

### **Gestion des erreurs dans le code asynchrone**

La gestion des erreurs dans le code asynchrone peut être délicate. Les rappels nécessitent une gestion des erreurs en premier, tandis que les promesses et `async/await` offrent des approches plus structurées, comme montré ci-dessous :

```javascript
// Gestion des erreurs avec les promesses
fetchUserDetails(1)
  .then((user) => fetchPostsByUser(user))
  .then((posts) => console.log(posts))
  .catch((error) => console.error("Erreur lors de la récupération des données :", error));
```

```javascript
// Gestion des erreurs avec Async/Await
async function getUserAndPosts() {
  try {
    const user = await fetchUserDetails(1);
    const posts = await fetchPostsByUser(user);
    console.log(posts);
  } catch (error) {
    console.error("Erreur lors de la récupération des données :", error);
  }
}
```

Comprendre l'évolution de JavaScript asynchrone vous aide à écrire un code efficace et non bloquant. Pour plus de détails, vous pouvez lire cet article sur [la progression évolutive de JavaScript asynchrone](https://medium.com/stackademic/mastering-asynchronous-javascript-from-callbacks-to-async-await-8449e1f5f9c0).

## 12. Fermetures

Une **fermeture** en JavaScript est créée lorsqu'une fonction "se souvient" des variables de sa portée externe, même après que la fonction externe a fini de s'exécuter. Cela signifie qu'une fonction conserve l'accès à l'environnement dans lequel elle a été créée, rendant les fermetures essentielles pour gérer les données à travers différents contextes.

```javascript
function outerFunction(outerVar) {
  return function innerFunction(innerVar) {
    console.log(`Externe : ${outerVar}, Interne : ${innerVar}`);
  };
}

const newFunction = outerFunction('React');
newFunction('JavaScript'); // Externe : React, Interne : JavaScript
```

Dans React, les fermetures sont cruciales pour gérer l'état et les props au sein des composants fonctionnels. Elles permettent aux fonctions comme les gestionnaires d'événements ou les rappels asynchrones d'accéder aux dernières valeurs d'état même après des re-rendus.

Par exemple, les hooks `useState` et `useEffect` s'appuient sur les fermetures pour "se souvenir" et gérer l'état à travers les rendus.

```javascript
function Counter() {
  const [count, setCount] = useState(0);
  const increment = () => setCount(count + 1); // La fermeture suit le compte
  return <button onClick={increment}>Compte : {count}</button>;
}
```

Comprendre les fermetures garantit que vous pouvez gérer efficacement l'état et les événements dans React, gardant vos composants cohérents et prévisibles.

## **13. Modules (import/export)**

Les projets React sont hautement modulaires, ce qui signifie que le code est divisé en plusieurs fichiers ou composants, chacun gérant une responsabilité spécifique. Cette modularité est rendue possible par les **modules ES6**, qui permettent d'**exporter** des valeurs, des fonctions ou des composants d'un fichier et de les **importer** dans un autre.

Comprendre comment utiliser `import` et `export` est essentiel pour organiser les applications React et rendre le code réutilisable et maintenable.

Dans l'exemple suivant, la fonction `greet` est **exportée** depuis `module.js`, la rendant accessible à d'autres fichiers.

```javascript
// module.js
export const greet = () => console.log('Bonjour');
```

Dans `anotherFile.js`, nous **importons** la fonction `greet` depuis `module.js` et pouvons maintenant l'utiliser comme si elle était définie localement, comme suit :

```javascript
// anotherFile.js
import { greet } from './module';
greet(); // Bonjour
```

Les composants React sont souvent exportés depuis leurs propres fichiers puis importés dans un composant central (comme `App.js`), vous permettant de décomposer votre interface utilisateur en morceaux plus petits et réutilisables.

```javascript
// Button.js
export default function Button() {
  return <button>Cliquez-moi</button>;
}

// App.js
import Button from './Button';
```

Comprendre cette structure d'import/export est fondamental dans React pour gérer les composants, réutiliser la logique et garder le code propre et modulaire.

Ici, vous pouvez noter que CommonJS était un système de modules populaire pour Node.js (JavaScript côté serveur) avant ES6. Il permettait d'exporter des valeurs depuis un fichier en utilisant `module.exports` et de les importer en utilisant `require()`.

Bien qu'il fonctionnait bien dans Node.js, il n'était pas nativement supporté par les navigateurs. Avec l'essor de **React** et d'autres bibliothèques frontend, le besoin d'un système de modules **natif, supporté par les navigateurs** et **standardisé** est devenu essentiel et ES6 a fourni cela.

## **14. Gestion des événements et propagation**

React s'appuie fortement sur la gestion des événements pour répondre aux interactions des utilisateurs. Les événements dans React sont gérés par des **Événements Synthétiques**, qui fournissent une cohérence multi-navigateurs et une optimisation des performances. Comprendre la **propagation des événements**, un processus où les événements se propagent de l'élément cible vers ses parents, est crucial pour contrôler le comportement des composants.

```javascript
// Exemple en JavaScript vanilla :
document.querySelector("button").addEventListener("click", function() {
  console.log("Bouton cliqué");
});
```

Dans l'exemple ci-dessus, cliquer sur le bouton déclenche l'écouteur d'événement, et l'événement "remonte" à travers les éléments parents à moins d'être arrêté. React gère cela de manière similaire avec ses événements `onClick` :

```javascript
// Exemple dans React :
function handleClick() {
  console.log("Bouton cliqué");
}

function App() {
  return <button onClick={handleClick}>Cliquez-moi</button>;
}
```

Dans React, la propagation des événements peut entraîner le déclenchement de plusieurs gestionnaires d'événements dans des éléments imbriqués. Par exemple, le `onClick` d'un parent peut être déclenché lorsque son bouton enfant est cliqué, à moins qu'il ne soit empêché en appelant `event.stopPropagation()` à l'intérieur de la méthode de gestion du bouton enfant, ce qui empêche ensuite l'événement de clic d'atteindre le `div` parent. Cela garantit que seul l'événement souhaité est géré.

```javascript
// Exemple de comment arrêter la propagation des événements :
function handleButtonClick(event) {
  event.stopPropagation(); // Empêche la propagation
  console.log("Bouton cliqué");
}

function handleDivClick() {
  console.log("Div cliqué");
}

function App() {
  return (
    <div onClick={handleDivClick}>
      <button onClick={handleButtonClick}>Cliquez-moi</button>
    </div>
  );
}
```

L'architecture de React, avec sa structure basée sur les composants et son Système d'Événements Synthétiques, réduit le besoin de `stopPropagation()` dans la plupart des cas, par exemple, dans des applications plus simples où un composant parent et un composant enfant ne gèrent pas le même événement comme un `click`.

Mais dans des **structures d'interface utilisateur plus complexes**, où plusieurs éléments gèrent le même événement (par exemple, `onClick`), et où vous souhaitez empêcher l'élément parent de réagir à l'événement de l'enfant, `stopPropagation()` devient crucial pour contrôler le flux des événements. Cela est particulièrement important dans des scénarios comme les **modales imbriquées, les menus déroulants ou les accordéons**, où un clic à l'intérieur de la modale ne doit pas déclencher un gestionnaire de clic sur le conteneur extérieur.

## **15. Classes et prototypes**

Bien que les **composants fonctionnels** soient désormais dominants dans React, comprendre les **classes JavaScript** et les **prototypes** reste précieux, surtout lorsque vous travaillez avec des **composants basés sur des classes** ou que vous maintenez du **code hérité**. Les classes JavaScript fournissent un plan pour créer des objets, et elles fonctionnent en exploitant les prototypes sous le capot.

```javascript
class Person {
  constructor(name) {
    this.name = name;
  }

  greet() {
    console.log(`Bonjour, je suis ${this.name}`);
  }
}

const person = new Person('Alice');
person.greet(); // Bonjour, je suis Alice
```

Dans cet exemple, la classe `Person` définit un constructeur pour initialiser la propriété `name`, et une méthode `greet()` qui imprime un message. Lorsque vous créez une nouvelle instance de `Person`, la méthode est disponible grâce à la **chaîne de prototypes** de JavaScript.

Bien que React se soit tourné vers les composants fonctionnels avec des hooks, les composants basés sur des classes étaient la norme avant React 16.8. Comprendre les classes est utile lorsque vous traitez avec des bases de code qui utilisent des composants de classe ou lorsque vous devez comprendre des fonctionnalités comme les méthodes de cycle de vie (`componentDidMount`, `componentDidUpdate`, etc.) et la liaison de `this`, qui sont plus prévalentes dans les composants de classe.

## Réflexions finales

Maîtriser les concepts clés de JavaScript décrits dans ce tutoriel vous donnera une base solide alors que vous plongez dans le développement React.

React s'appuie fortement sur les fonctionnalités modernes de JavaScript comme `map()`, `filter()`, la destructuration et l'opérateur de propagation, qui rationalisent tous la manière dont les données sont manipulées et les composants sont rendus. Et des concepts comme l'immuabilité, le chaînage optionnel et l'opérateur de coalescence des nuls sont cruciaux pour écrire un code propre et sans bugs qui interagit efficacement avec des données dynamiques.

En comprenant comment ces fonctionnalités JavaScript fonctionnent ensemble, vous serez bien équipé pour écrire des applications React plus efficaces et maintenables.

Ainsi, alors que vous commencez votre voyage avec React, assurez-vous que vos fondamentaux JavaScript sont solides comme le roc, vous trouverez que cela porte ses fruits alors que vous relevez des défis plus complexes dans vos projets React. De plus, si vous trouvez que j'ai oublié un concept important ici, veuillez me le faire savoir. Je l'ajouterai à l'article pour une version mise à jour.