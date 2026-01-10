---
title: Comment simplifier votre base de code avec map(), reduce() et filter() en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-16T17:18:02.000Z'
originalURL: https://freecodecamp.org/news/15-useful-javascript-examples-of-map-reduce-and-filter-74cbbb5e0a1f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*An5EH7U1GKo_td9yXY2j4A.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment simplifier votre base de code avec map(), reduce() et filter()
  en JavaScript
seo_desc: 'By Alex Permyakov

  When you read about Array.reduce and how cool it is, the first and sometimes the
  only example you find is the sum of numbers. This is not our definition of ‘useful’.
  ?

  Moreover, I’ve never seen it in a real codebase. But, what I’ve ...'
---

Par Alex Permyakov

Lorsque vous lisez à propos de **Array.reduce** et à quel point c'est génial, le premier et parfois le seul exemple que vous trouvez est la somme de nombres. Ce n'est pas notre définition de utile. ?

De plus, je ne l'ai jamais vu dans une base de code réelle. Mais ce que j'ai souvent vu, ce sont des instructions de boucle for de 7 à 8 lignes pour résoudre une tâche régulière où **Array.reduce** pourrait le faire en une seule ligne.

Récemment, j'ai réécrit quelques modules en utilisant ces fonctions géniales. Cela m'a surpris de voir à quel point la base de code est devenue simplifiée. Voici donc une liste de bonnes pratiques.

Si vous avez un bon exemple d'utilisation de la méthode **map** ou **reduce**, postez-le dans la section des commentaires. ?

Commençons !

#### 1. Supprimer les doublons d'un tableau de nombres/chaînes

Bien, ceci est le seul exemple qui ne concerne pas **map**/**reduce**/**filter**, mais il est si compact qu'il était difficile de ne pas le mettre dans la liste. De plus, nous l'utiliserons dans quelques exemples également.

```js
const values = [3, 1, 3, 5, 2, 4, 4, 4];
const uniqueValues = [...new Set(values)];

// uniqueValues est [3, 1, 5, 2, 4]
```

#### 2. Une recherche simple (sensible à la casse)

La méthode **filter()** crée un nouveau tableau avec tous les éléments qui passent le test implémenté par la fonction fournie.

```js
const users = [
  { id: 11, name: 'Adam', age: 23, group: 'editor' },
  { id: 47, name: 'John', age: 28, group: 'admin' },
  { id: 85, name: 'William', age: 34, group: 'editor' },
  { id: 97, name: 'Oliver', age: 28, group: 'admin' }
];

let res = users.filter(it => it.name.includes('oli'));

// res est []
```

#### 3. Une recherche simple (insensible à la casse)

```js
let res = users.filter(it => new RegExp('oli', "i").test(it.name));

// res est
[
  { id: 97, name: 'Oliver', age: 28, group: 'admin' }
]
```

#### 4. Vérifier si l'un des utilisateurs a des droits d'administrateur

La méthode **some()** teste si au moins un élément du tableau passe le test implémenté par la fonction fournie.

```js
const hasAdmin = users.some(user => user.group === 'admin');

// hasAdmin est true
```

#### 5. Aplanir un tableau de tableaux

Le résultat de la première itération est égal à : [...[], ...[1, 2, 3]] signifie qu'il se transforme en [1, 2, 3] — cette valeur que nous fournissons en tant que '_acc_' lors de la deuxième itération et ainsi de suite.

```js
const nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
let flat = nested.reduce((acc, it) => [...acc, ...it], []);

// flat est [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Nous pouvons légèrement améliorer ce code en omettant un tableau vide `[]` en tant que deuxième argument pour **reduce()**. Ensuite, la première valeur de **nested** sera utilisée comme valeur initiale **acc**. Merci à [Vladimir Efanov](https://medium.com/@vladimir_efanov?source=responses---------2---------------------).

```js
let flat = nested.reduce((acc, it) => [...acc, ...it]);

// flat est [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Notez que l'utilisation de l'[opérateur de décomposition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) à l'intérieur d'un **reduce** n'est pas idéale pour les performances. Cet exemple est un cas où mesurer les performances a du sens pour votre cas d'utilisation. ⚠️

Merci à [Paweł Wolak](https://medium.com/@pawewolak?source=responses---------0---------------------), voici une méthode plus courte sans **Array.reduce** :

```js
let flat = [].concat.apply([], nested);
```

De plus, [_Array.flat_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat) arrive, mais c'est encore une fonctionnalité expérimentale.

#### 6. Créer un objet qui contient la fréquence de la clé spécifiée

Regroupons et comptons la propriété 'age' pour chaque élément du tableau :

```js
const users = [
  { id: 11, name: 'Adam', age: 23, group: 'editor' },
  { id: 47, name: 'John', age: 28, group: 'admin' },
  { id: 85, name: 'William', age: 34, group: 'editor' },
  { id: 97, name: 'Oliver', age: 28, group: 'admin' }
];

const groupByAge = users.reduce((acc, it) => {
  acc[it.age] = acc[it.age] + 1 || 1;
  return acc;
}, {});

// groupByAge est {23: 1, 28: 2, 34: 1}
```

Merci à [sai krishna](https://medium.com/@krishnasai952?source=responses---------8-31--------------------) pour avoir suggéré celui-ci !

#### 7. Indexer un tableau d'objets (table de recherche)

Au lieu de traiter tout le tableau pour trouver un utilisateur par son id, nous pouvons construire un objet où l'id de l'utilisateur représente une clé (avec un temps de recherche constant).

```js
const uTable = users.reduce((acc, it) => (acc[it.id] = it, acc), {})

// uTable est égal à :
{
  11: { id: 11, name: 'Adam', age: 23, group: 'editor' },
  47: { id: 47, name: 'John', age: 28, group: 'admin' },
  85: { id: 85, name: 'William', age: 34, group: 'editor' },
  97: { id: 97, name: 'Oliver', age: 28, group: 'admin' }
}
```

C'est utile lorsque vous devez accéder à vos données par id comme `uTable[85].name` souvent.

#### 8. Extraire les valeurs uniques pour la clé donnée de chaque élément du tableau

Créons une liste des groupes d'utilisateurs existants. La méthode **map()** crée un nouveau tableau avec les résultats de l'appel d'une fonction fournie sur chaque élément du tableau appelant.

```js
const listOfUserGroups = [...new Set(users.map(it => it.group))];

// listOfUserGroups est ['editor', 'admin'];
```

#### 9. Inversion de la carte clé-valeur d'un objet

```js
const cities = {
  Lyon: 'France',
  Berlin: 'Germany',
  Paris: 'France'
};

let countries = Object.keys(cities).reduce(
  (acc, k) => (acc[cities[k]] = [...(acc[cities[k]] || []), k], acc) , {});
  
// countries est
{
  France: ["Lyon", "Paris"],
  Germany: ["Berlin"]
}
```

Cette ligne unique semble assez trompeuse. Nous utilisons l'[opérateur virgule](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_Operator) ici, et cela signifie que nous retournons la dernière valeur entre parenthèses — `acc`. Réécrivons cet exemple de manière plus adaptée à la production et performante :

```js
let countries = Object.keys(cities).reduce((acc, k) => {
  let country = cities[k];
  acc[country] = acc[country] || [];
  acc[country].push(k);
  return acc;
}, {});
```

Ici, nous n'utilisons pas l'[opérateur de décomposition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) — il crée un nouveau tableau à chaque appel de **reduce()**, ce qui entraîne une grande pénalité de performance : O(n²). Au lieu de cela, la bonne vieille méthode **push()**.

#### 10. Créer un tableau de valeurs Fahrenheit à partir d'un tableau de valeurs Celsius

Pensez à cela comme à traiter chaque élément avec une formule donnée ?

```js
const celsius = [-15, -5, 0, 10, 16, 20, 24, 32]
const fahrenheit = celsius.map(t => t * 1.8 + 32);

// fahrenheit est [5, 23, 32, 50, 60.8, 68, 75.2, 89.6]
```

#### 11. Encoder un objet en chaîne de requête

```js
const params = {lat: 45, lng: 6, alt: 1000};

const queryString = Object.entries(params).map(p => encodeURIComponent(p[0]) + '=' + encodeURIComponent(p[1])).join('&')

// queryString est "lat=45&lng=6&alt=1000"
```

#### 12. Imprimer un tableau d'utilisateurs sous forme de chaîne lisible uniquement avec des clés spécifiées

Parfois, vous voulez imprimer votre tableau d'objets avec des clés sélectionnées sous forme de chaîne, mais vous réalisez que **JSON.stringify** n'est pas si génial ?

```js
const users = [
  { id: 11, name: 'Adam', age: 23, group: 'editor' },
  { id: 47, name: 'John', age: 28, group: 'admin' },
  { id: 85, name: 'William', age: 34, group: 'editor' },
  { id: 97, name: 'Oliver', age: 28, group: 'admin' }
];

users.map(({id, age, group}) => `\n${id} ${age} ${group}`).join('')

// cela retourne :
"
11 23 editor
47 28 admin
85 34 editor
97 28 admin"
```

**JSON.stringify** peut rendre la sortie de chaîne plus lisible, mais pas sous forme de tableau :

```js
JSON.stringify(users, ['id', 'name', 'group'], 2);

// cela retourne :
"[
  {
    "id": 11,
    "name": "Adam",
    "group": "editor"
  },
  {
    "id": 47,
    "name": "John",
    "group": "admin"
  },
  {
    "id": 85,
    "name": "William",
    "group": "editor"
  },
  {
    "id": 97,
    "name": "Oliver",
    "group": "admin"
  }
]"
```

#### 13. Trouver et remplacer une paire clé-valeur dans un tableau d'objets

Disons que nous voulons changer l'âge de John. Si vous connaissez l'index, vous pouvez écrire cette ligne : `users[1].age = 29`. Cependant, regardons une autre façon de faire :

```js
const updatedUsers = users.map(
  p => p.id !== 47 ? p : {...p, age: p.age + 1}
);

// John a maintenant 29 ans
```

Ici, au lieu de changer le seul élément dans notre tableau, nous créons un nouveau avec un seul élément différent. Maintenant, nous pouvons comparer nos tableaux simplement par référence comme `updatedUsers == users` ce qui est super rapide ! React.js utilise cette approche pour accélérer le processus de réconciliation. [Voici une explication.](https://blog.logrocket.com/immutability-in-react-ebe55253a1cc)

#### 14. Union (A ∪ B) de tableaux

Moins de code que d'importer et d'appeler la [méthode union de lodash](https://lodash.com/docs/4.17.11#union).

```js
const arrA = [1, 4, 3, 2];
const arrB = [5, 2, 6, 7, 1];

[...new Set([...arrA, ...arrB])]; // retourne [1, 4, 3, 2, 5, 6, 7]
```

#### 15. Intersection (A ∩ B) de tableaux

Le dernier !

```js
const arrA = [1, 4, 3, 2];
const arrB = [5, 2, 6, 7, 1];

arrA.filter(it => arrB.includes(it)); // retourne [1, 2]
```

En tant qu'exercice, essayez d'implémenter la différence (A \ B) des tableaux. Indice : utilisez un point d'exclamation.

Merci à [Asmor](https://www.reddit.com/user/Asmor) et [incarnatethegreat](https://www.reddit.com/user/incarnatethegreat) pour leurs commentaires sur le #9.

### C'est tout !

Si vous avez des questions ou des commentaires, faites-le moi savoir dans les commentaires ci-dessous ou contactez-moi sur [Twitter](https://twitter.com/AlexDevBB).

#### Si cela vous a été utile, veuillez cliquer sur le bouton d'applaudissements ? ci-dessous plusieurs fois pour montrer votre soutien ! ⬇️⬇️ ??

Voici d'autres articles que j'ai écrits :

[**Comment commencer avec l'internationalisation en JavaScript**  
_En adaptant notre application pour différentes langues et pays, nous offrons une meilleure expérience utilisateur. C'est plus simple pour les utilisateurs_](https://www.freecodecamp.org/news/how-to-get-started-with-internationalization-in-javascript-c09a0d2cd834/)

[**Configuration d'API REST Node.js prêtes pour la production en utilisant TypeScript, PostgreSQL et Redis.**](https://medium.com/@alex.permyakov/production-ready-node-js-rest-apis-setup-using-typescript-postgresql-and-redis-a9525871407)  
[_Il y a un mois, on m'a donné la tâche de construire une simple API de recherche. Tout ce qu'elle devait faire était de récupérer des données depuis un tiers_](https://medium.com/@alex.permyakov/production-ready-node-js-rest-apis-setup-using-typescript-postgresql-and-redis-a9525871407)

Merci pour la lecture ❤️