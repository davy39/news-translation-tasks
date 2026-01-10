---
title: Méthode Map de JavaScript – Syntaxe et Exemples de Code
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-15T00:50:30.000Z'
originalURL: https://freecodecamp.org/news/javascript-map-method
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-8-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Méthode Map de JavaScript – Syntaxe et Exemples de Code
seo_desc: "JavaScript's map method, introduced in ECMAScript 5, is a fundamental tool\
  \ for array manipulation and transformation. This method is versatile and simple,\
  \ and has become a staple in modern JavaScript programming. \nIn this article, we'll\
  \ explore the m..."
---

La méthode `map` de JavaScript, introduite dans ECMAScript 5, est un outil fondamental pour la manipulation et la transformation de tableaux. Cette méthode est polyvalente et simple, et est devenue un élément incontournable de la programmation JavaScript moderne. 

Dans cet article, nous explorerons la syntaxe de la méthode `map` et ses nombreuses applications, allant de la manipulation de données de base aux paradigmes avancés de la programmation fonctionnelle.

Vous pouvez obtenir tout le code source à partir d'[ici](https://github.com/dotslashbit/fcc-article-resources/blob/main/js-map-method/index.js).

## Table des Matières

* [Bases de la Méthode `map`](#heading-bases-de-la-methode-map)
* [Syntaxe de la Méthode `map`](#heading-syntaxe-de-la-methode-map)
* [Cas d'Utilisation Courants de `map`](#heading-cas-dutilisation-courants-de-map)
* [Conclusion](#heading-conclusion)

## Bases de la Méthode `map`

La méthode Map en JavaScript est une fonction d'ordre supérieur qui itère sur chaque élément d'un tableau, vous permettant d'appliquer une fonction spécifiée à chaque élément. Cette fonction est communément appelée fonction de rappel (callback). 

La caractéristique clé de la méthode Map est qu'elle crée un nouveau tableau basé sur les résultats de l'application de cette fonction de rappel à chaque élément du tableau original, sans modifier le tableau original lui-même.

### Syntaxe de la Méthode `map`

La syntaxe de la méthode Map est simple :

```javascript
const newArray = array.map(callback(currentValue[, index[, array]]) {
  // retourner l'élément pour newArray, après avoir exécuté quelque chose
}[, thisArg]);

```

* `array` : Le tableau original que vous souhaitez parcourir.
* `callback` : Une fonction qui sera exécutée sur chaque élément du tableau.
* `currentValue` : L'élément actuel en cours de traitement dans le tableau.
* `index` (optionnel) : L'index de l'élément actuel en cours de traitement.
* `array` (optionnel) : Le tableau sur lequel `map` a été appelé.
* `thisArg` (optionnel) : Un objet optionnel auquel `this` peut faire référence dans la fonction `callback`.

## Cas d'Utilisation Courants de `map`

### Transformation de Données

**Scénario :** Vous avez un tableau de nombres et vous souhaitez doubler chaque nombre dans le tableau.

#### Sans Map :

```js
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = [];
for (let i = 0; i < numbers.length; i++) {
  doubledNumbers.push(numbers[i] * 2);
}
// doubledNumbers: [2, 4, 6, 8, 10]

```

Dans l'approche traditionnelle, nous initialisons un tableau vide `doubledNumbers`, nous parcourons chaque élément du tableau `numbers` à l'aide d'une boucle for, et nous doublons manuellement chaque élément en le multipliant par 2. Enfin, nous ajoutons la valeur doublée au tableau `doubledNumbers`.

#### Avec Map :

```javascript
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(num => num * 2);
// doubledNumbers: [2, 4, 6, 8, 10]

```

En utilisant la méthode `map`, nous passons une fonction de rappel qui double chaque élément (`num`) dans le tableau `numbers`. 

La méthode `map` itère sur chaque élément du tableau, applique la fonction de rappel fournie et retourne un nouveau tableau (`doubledNumbers`) contenant les valeurs doublées. Cette approche simplifie le code et améliore la lisibilité.

### Transformation d'Objets

**Scénario :** Vous avez un tableau d'objets utilisateurs et vous souhaitez extraire uniquement leurs identifiants dans un nouveau tableau.

#### Sans Map :

```js
const users = [
  { id: 1, name: 'John' },
  { id: 2, name: 'Jane' },
  { id: 3, name: 'Doe' }
];
const userIds = [];
for (let i = 0; i < users.length; i++) {
  userIds.push(users[i].id);
}
// userIds: [1, 2, 3]

```

Dans la méthode conventionnelle, nous initialisons un tableau vide `userIds`, nous parcourons chaque objet utilisateur dans le tableau `users` à l'aide d'une boucle for, et nous extrayons manuellement la propriété `id` de chaque objet utilisateur. Nous ajoutons ensuite la valeur `id` extraite au tableau `userIds`.

#### Avec Map :

```javascript
const users = [
  { id: 1, name: 'John' },
  { id: 2, name: 'Jane' },
  { id: 3, name: 'Doe' }
];
const userIds = users.map(user => user.id);
// userIds: [1, 2, 3]

```

En employant la méthode `map`, nous fournissons une fonction de rappel qui extrait la propriété `id` de chaque objet utilisateur (`user`) dans le tableau `users`. 

La méthode `map` itère sur chaque élément du tableau, applique la fonction de rappel et retourne un nouveau tableau (`userIds`) contenant uniquement les valeurs `id`. Cette approche simplifie le code et améliore la maintenabilité.

### Manipulation de Chaînes de Caractères

**Scénario :** Vous avez un tableau de noms et vous souhaitez convertir tous les noms en majuscules.

#### Sans Map :

```javascript
const names = ['John', 'Jane', 'Doe'];
const uppercasedNames = [];
for (let i = 0; i < names.length; i++) {
  uppercasedNames.push(names[i].toUpperCase());
}
// uppercasedNames: ['JOHN', 'JANE', 'DOE']

```

Dans l'approche traditionnelle, nous initialisons un tableau vide `uppercasedNames`, nous parcourons chaque élément du tableau `names` à l'aide d'une boucle for, et nous convertissons manuellement chaque nom en majuscules en utilisant la méthode `toUpperCase()`. Enfin, nous ajoutons le nom en majuscules au tableau `uppercasedNames`.

#### Avec Map :

```javascript
const names = ['John', 'Jane', 'Doe'];
const uppercasedNames = names.map(name => name.toUpperCase());
// uppercasedNames: ['JOHN', 'JANE', 'DOE']

```

En utilisant la méthode `map`, nous passons une fonction de rappel qui convertit chaque nom (`name`) dans le tableau `names` en majuscules en utilisant la méthode `toUpperCase()`. 

La méthode `map` itère sur chaque élément du tableau, applique la fonction de rappel et retourne un nouveau tableau (`uppercasedNames`) contenant les noms en majuscules. Cette approche simplifie le code et améliore la lisibilité.

### Travailler avec l'Index

**Scénario :** Vous avez un tableau de nombres et vous souhaitez incrémenter chaque nombre par son index.

#### Sans Map :

```js
const numbers = [1, 2, 3, 4, 5];
const incrementedNumbers = [];
for (let i = 0; i < numbers.length; i++) {
  incrementedNumbers.push(numbers[i] + i);
}
// incrementedNumbers: [1, 3, 5, 7, 9]

```

Dans l'approche traditionnelle, nous initialisons un tableau vide `incrementedNumbers`, nous parcourons chaque élément du tableau `numbers` à l'aide d'une boucle for, nous ajoutons l'index `i` à chaque nombre, et nous ajoutons la valeur incrémentée au tableau `incrementedNumbers`.

#### Avec Map :

```javascript
const numbers = [1, 2, 3, 4, 5];
const incrementedNumbers = numbers.map((num, index) => num + index);
// incrementedNumbers: [1, 3, 5, 7, 9]

```

En utilisant la méthode `map`, nous passons une fonction de rappel qui prend à la fois la valeur actuelle (`num`) et l'index (`index`) comme paramètres. Dans la fonction de rappel, nous ajoutons l'index à chaque nombre. 

La méthode `map` itère sur chaque élément du tableau, applique la fonction de rappel et retourne un nouveau tableau (`incrementedNumbers`) contenant les valeurs incrémentées. Cette approche gère élégamment la logique d'incrémentation de chaque nombre par son index.

## Conclusion

Que ce soit pour la manipulation de données, la transformation d'objets ou la manipulation de chaînes de caractères, la méthode Map offre une solution robuste pour une large gamme de tâches de programmation, ce qui en fait une partie essentielle de la boîte à outils de chaque développeur JavaScript. 

En comparant les approches traditionnelles avec la méthode Map et en explorant divers cas d'utilisation, vous pouvez acquérir une compréhension plus approfondie de ses capacités.

Si vous avez des commentaires, veuillez me contacter en DM sur [Twitter](https://twitter.com/introvertedbot) ou [Linkedin](https://www.linkedin.com/in/sahil-mahapatra/)