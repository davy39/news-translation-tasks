---
title: Comment cloner un tableau en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T16:01:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-clone-an-array-in-javascript-1d3183468f6a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fWhAxeITIQaYWeqE7wogkQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment cloner un tableau en JavaScript
seo_desc: 'By Yazeed Bzadough

  JavaScript has many ways to do anything. I’ve written on 10 Ways to Write pipe/compose
  in JavaScript, and now we’re doing arrays.

  Here''s an interactive scrim that shows various ways to clone arrays in JavaScript:



  1. Spread Operat...'
---

Par Yazeed Bzadough

JavaScript offre de nombreuses façons de faire quoi que ce soit. J'ai écrit sur [10 façons d'écrire pipe/compose en JavaScript](https://www.freecodecamp.org/news/10-ways-to-write-pipe-compose-in-javascript-f6d54c575616/), et maintenant nous traitons des tableaux.

### Voici un scrim interactif qui montre diverses façons de cloner des tableaux en JavaScript :

<iframe src="https://scrimba.com/scrim/cbRbVJud?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="480"></iframe>

### 1. Opérateur de décomposition (Copie superficielle)

Depuis la sortie d'ES6, cette méthode est devenue la plus populaire. Elle offre une syntaxe concise et vous la trouverez incroyablement utile lorsque vous utiliserez des bibliothèques comme React et Redux.

```js
numbers = [1, 2, 3];
numbersCopy = [...numbers];
```

**Note :** Cela ne copie pas en toute sécurité les tableaux multidimensionnels. Les valeurs de tableau/objet sont copiées par _référence_ au lieu de l'être par _valeur_.

Cela est correct

```js
numbersCopy.push(4);
console.log(numbers, numbersCopy);
// [1, 2, 3] et [1, 2, 3, 4]
// numbers est laissé intact
```

Cela n'est pas correct

```js
nestedNumbers = [[1], [2]];
numbersCopy = [...nestedNumbers];

numbersCopy[0].push(300);
console.log(nestedNumbers, numbersCopy);
// [[1, 300], [2]]
// [[1, 300], [2]]
// Les deux ont été modifiés car ils partagent des références
```

### 2. Bonne vieille boucle for() (Copie superficielle)

J'imagine que cette approche est la _moins_ populaire, étant donné à quel point la programmation fonctionnelle est devenue tendance dans nos cercles.

Pure ou impure, déclarative ou impérative, cela fait le travail !

```js
numbers = [1, 2, 3];
numbersCopy = [];

for (i = 0; i < numbers.length; i++) {
  numbersCopy[i] = numbers[i];
}
```

**Note :** Cela ne copie pas en toute sécurité les tableaux multidimensionnels. Puisque vous utilisez l'opérateur `=`, il assignera les objets/tableaux par _référence_ au lieu de par _valeur_.

Cela est correct

```js
numbersCopy.push(4);
console.log(numbers, numbersCopy);
// [1, 2, 3] et [1, 2, 3, 4]
// numbers est laissé intact
```

Cela n'est pas correct

```js
nestedNumbers = [[1], [2]];
numbersCopy = [];

for (i = 0; i < nestedNumbers.length; i++) {
  numbersCopy[i] = nestedNumbers[i];
}

numbersCopy[0].push(300);
console.log(nestedNumbers, numbersCopy);
// [[1, 300], [2]]
// [[1, 300], [2]]
// Les deux ont été modifiés car ils partagent des références
```

### 3. Bonne vieille boucle while() (Copie superficielle)

Même chose que `for`—impure, impérative, blah, blah, blah… cela fonctionne ! 😉

```js
numbers = [1, 2, 3];
numbersCopy = [];
i = -1;

while (++i < numbers.length) {
  numbersCopy[i] = numbers[i];
}
```

**Note :** Cela assignera également les objets/tableaux par _référence_ au lieu de par _valeur_.

Cela est correct

```js
numbersCopy.push(4);
console.log(numbers, numbersCopy);
// [1, 2, 3] et [1, 2, 3, 4]
// numbers est laissé intact
```

Cela n'est pas correct

```js
nestedNumbers = [[1], [2]];
numbersCopy = [];

i = -1;

while (++i < nestedNumbers.length) {
  numbersCopy[i] = nestedNumbers[i];
}

numbersCopy[0].push(300);
console.log(nestedNumbers, numbersCopy);
// [[1, 300], [2]]
// [[1, 300], [2]]
// Les deux ont été modifiés car ils partagent des références
```

### 4. Array.map (Copie superficielle)

De retour en territoire moderne, nous trouvons la fonction `map`. [Enracinée dans les mathématiques](https://en.wikipedia.org/wiki/Morphism), `map` est le concept de transformation d'un ensemble en un autre type d'ensemble, tout en préservant la structure.

En français, cela signifie que `Array.map` retourne un tableau de la même longueur à chaque fois.

Pour doubler une liste de nombres, utilisez `map` avec une fonction `double`.

```js
numbers = [1, 2, 3];
double = (x) => x * 2;

numbers.map(double);
```

#### Et pour le clonage ??

Vrai, cet article parle de cloner des tableaux. Pour dupliquer un tableau, il suffit de retourner l'élément dans votre appel `map`.

```js
numbers = [1, 2, 3];
numbersCopy = numbers.map((x) => x);
```

Si vous souhaitez être un peu plus mathématique, `(x) => x` est appelé [_identité_](https://en.wikipedia.org/wiki/Identity_function). Il retourne quel que soit le paramètre qui lui a été donné.

`map(identity)` clone une liste.

```js
identity = (x) => x;
numbers.map(identity);
// [1, 2, 3]
```

**Note :** Cela assignera également les objets/tableaux par _référence_ au lieu de par _valeur_.

### 5. Array.filter (Copie superficielle)

Cette fonction retourne un tableau, tout comme `map`, mais il n'est pas garanti qu'il soit de la même longueur.

Et si vous filtrez pour les nombres pairs ?

```js
[1, 2, 3].filter((x) => x % 2 === 0);
// [2]
```

La longueur du tableau d'entrée était de 3, mais la longueur résultante est de 1.

Si le prédicat de votre `filter` retourne toujours `true`, cependant, vous obtenez un duplicata !

```js
numbers = [1, 2, 3];
numbersCopy = numbers.filter(() => true);
```

Chaque élément passe le test, donc il est retourné.

**Note :** Cela assignera également les objets/tableaux par _référence_ au lieu de par _valeur_.

### 6. Array.reduce (Copie superficielle)

J'ai presque honte d'utiliser `reduce` pour cloner un tableau, car il est tellement plus puissant que cela. Mais voici…

```js
numbers = [1, 2, 3];

numbersCopy = numbers.reduce((newArray, element) => {
  newArray.push(element);

  return newArray;
}, []);
```

`reduce` transforme une valeur initiale lorsqu'il parcourt une liste.

Ici, la valeur initiale est un tableau vide, et nous le remplissons avec chaque élément au fur et à mesure. Ce tableau doit être retourné par la fonction pour être utilisé dans l'itération suivante.

**Note :** Cela assignera également les objets/tableaux par _référence_ au lieu de par _valeur_.

### 7. Array.slice (Copie superficielle)

`slice` retourne une copie _superficielle_ d'un tableau basée sur les index de début/fin que vous fournissez.

Si nous voulons les 3 premiers éléments :

```js
[1, 2, 3, 4, 5].slice(0, 3);
// [1, 2, 3]
// Commence à l'index 0, s'arrête à l'index 3
```

Si nous voulons tous les éléments, ne donnez aucun paramètre

```js
numbers = [1, 2, 3, 4, 5];
numbersCopy = numbers.slice();
// [1, 2, 3, 4, 5]
```

**Note :** Il s'agit d'une copie _superficielle_, donc elle assignera également les objets/tableaux par _référence_ au lieu de par _valeur_.

### 8. JSON.parse et JSON.stringify (Copie profonde)

`JSON.stringify` transforme un objet en une chaîne.

`JSON.parse` transforme une chaîne en un objet.

Les combiner peut transformer un objet en une chaîne, puis inverser le processus pour créer une toute nouvelle structure de données.

**Note : Celui-ci** **copie en toute sécurité les objets/tableaux profondément imbriqués** !

```js
nestedNumbers = [[1], [2]];
numbersCopy = JSON.parse(JSON.stringify(nestedNumbers));

numbersCopy[0].push(300);
console.log(nestedNumbers, numbersCopy);

// [[1], [2]]
// [[1, 300], [2]]
// Ces deux tableaux sont complètement séparés !
```

### 9. Array.concat (Copie superficielle)

`concat` combine des tableaux avec des valeurs ou d'autres tableaux.

```js
[1, 2, 3].concat(4); // [1, 2, 3, 4]
[1, 2, 3].concat([4, 5]); // [1, 2, 3, 4, 5]
```

Si vous ne donnez rien ou un tableau vide, une copie superficielle est retournée.

```js
[1, 2, 3].concat(); // [1, 2, 3]
[1, 2, 3].concat([]); // [1, 2, 3]
```

**Note :** Cela assignera également les objets/tableaux par _référence_ au lieu de par _valeur_.

### 10. Array.from (Copie superficielle)

Cela peut transformer n'importe quel objet itérable en un tableau. Donner un tableau retourne une copie superficielle.

```js
numbers = [1, 2, 3];
numbersCopy = Array.from(numbers);
// [1, 2, 3]
```

**Note :** Cela assignera également les objets/tableaux par _référence_ au lieu de par _valeur_.

### Conclusion

Eh bien, c'était amusant 😊

J'ai essayé de cloner en utilisant une seule étape. Vous trouverez beaucoup plus de façons si vous employez plusieurs méthodes et techniques.