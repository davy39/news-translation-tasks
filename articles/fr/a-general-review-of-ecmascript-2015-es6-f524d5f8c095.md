---
title: Une revue générale d'ECMAScript 2015 (ES6)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-24T18:54:53.000Z'
originalURL: https://freecodecamp.org/news/a-general-review-of-ecmascript-2015-es6-f524d5f8c095
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NSN1a2xVtV1exzcD8fpzhA.jpeg
tags:
- name: coding
  slug: coding
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Une revue générale d'ECMAScript 2015 (ES6)
seo_desc: 'By Cem Eygi

  ES6 is the newer standardization/version of Javascript, which was released in 2015.
  It is important to learn ES6, because it has many new features that help developers
  write and understand JavaScript more easily. Modern Frameworks like An...'
---

Par Cem Eygi

ES6 est la **nouvelle standardisation/version de** **JavaScript**, publiée en 2015. Il est important d'apprendre ES6, car il comporte de nombreuses nouvelles fonctionnalités qui aident les développeurs à écrire et à comprendre JavaScript plus facilement. Les frameworks modernes comme Angular et React sont développés avec ES6. Sa syntaxe est également différente de celle du JavaScript classique.

Alors, qu'y a-t-il de nouveau dans ES6 ? Examinons cela.

### 1. Les mots-clés let & const

ES6 introduit deux nouveaux mots-clés pour les déclarations de variables : `let` et `const`.

Auparavant, nous n'avions que le mot-clé `var` en JavaScript pour déclarer des variables :

```js
var name = 'Cem';
```

Dans ES6, nous utilisons le mot-clé `let` à la place.

#### Pourquoi 'let' au lieu de 'var' ?

Parce que l'utilisation de `var` pose des problèmes de **portée**. Par exemple, définissons une chaîne de caractères avec `var` globalement et localement :

```js
var word = 'I am global';

if(true) {  
  var word = 'I am local'; 
}

console.log(word); // Que pensez-vous obtenir ici comme résultat ?
```

Le _console.log_ devrait imprimer la chaîne **globale** : `'I am global'`. Parce que la deuxième déclaration `var word = 'I am local'` est une chaîne **locale** et que _console.log_ est en dehors du bloc _if_ :

![Image](https://cdn-media-1.freecodecamp.org/images/cVxBMtGJhUv9UZBuGq4uZc2KSv3cskx-saW5)
_**Étonnamment, la variable locale a été imprimée.**_

De manière inattendue, la variable locale que nous avons définie avec `var` a ignoré le bloc _if_ et a été imprimée dans la console. Pour éviter ce problème, ES6 nous apporte un nouveau mot-clé : **let.**

Essayons à nouveau avec `let` :

```js
let word = 'I am global';

if(true) {
  let word = 'I am local'; 
}

console.log(word); // Cette fois, que pensez-vous obtenir ?
```

![Image](https://cdn-media-1.freecodecamp.org/images/Dwd8aTI-M0eMOKLLrOB5en7-1SGdc9M2Jx0j)
_**Le résultat de l'utilisation de 'let'**_

Cette fois, la chaîne **globale** a été imprimée comme nous l'attendions, `let` a résolu le problème de portée.

#### Un autre problème de l'instruction 'var'

Nous pouvons réassigner des variables avec `var` et `let`. Mais `let` ne nous permet pas de **redéclarer** les mêmes variables :

```js
var number = 1;
var number = 2;

console.log(number); // Pas d'erreurs ici, 2 est imprimé
```

Essayons à nouveau avec **let** :

```js
let number = 1;
let number = 2;

console.log(number); // let n'autorise pas la redéclaration
```

![Image](https://cdn-media-1.freecodecamp.org/images/VTuifL3QukwZgVbmITOH4rhI1LMpy5ojjfgD)
_**La redéclaration de let génère une erreur :**_

Vous pouvez toujours utiliser **var** dans ES6, mais ce n'est pas recommandé.

#### Le mot-clé const

Continuons avec le mot-clé `const`. `const` signifie _constante_.

> « Constante : quelque chose qui ne change pas. »

Lorsque nous déclarons une variable constante, nous ne pouvons pas la modifier plus tard. Par exemple, la **date de naissance** est une constante.

```js
const birthYear = 1990;

birthYear = 2000; // Vous ne pouvez pas réassigner une variable constante
```

Si vous essayez de modifier ou de redéclarer une variable _const_, cela générera une erreur :

![Image](https://cdn-media-1.freecodecamp.org/images/xVbUNLdmjjbQJkrniCDmf-eyAl4JVuJgB4XV)
_**La réassignation d'une variable const génère une erreur**_

L'utilisation de `const` améliore la qualité de votre code. Utilisez-le uniquement lorsque vous êtes sûr que votre variable ne changera pas plus tard.

### 2. Les littéraux de gabarit

Les littéraux de gabarit sont l'une des nouvelles **syntaxes d'ES6**, pour créer des chaînes de caractères et imprimer des variables dynamiques.

* Pour créer une chaîne de caractères, utilisez des backticks **( `` )** au lieu de guillemets simples ou doubles :

```js
let oldWay = 'A word';  // Méthode JS

let newWay = `A word`;  // Méthode ES6
```

* Utilisez la syntaxe d'interpolation : **${ expression }** pour simplifier la concaténation de chaînes et créer des variables dynamiques

Définissons quelques variables et utilisons les anciennes et nouvelles méthodes pour les imprimer :

```js
let name = 'Cem';
let age = 28;
let profession = 'Software Developer';
```

L'ancienne méthode JavaScript :

```js
console.log("Hello, my name is " + name + ", I'm " + age + " years old and I'm a " + profession);
```

![Image](https://cdn-media-1.freecodecamp.org/images/DmqlgNPaa7B74Bnqumk3t3CseyQPxmahquIy)
_**Sortie avec les signes +**_

La méthode ES6 :

```js
console.log(`Hello, my name is ${name}, I'm ${age} years old and I'm a ${profession}.`);
```

![Image](https://cdn-media-1.freecodecamp.org/images/Uzd--CtKLfVlzdQujxl8VbQCuMcVZfs-pHTP)
_**Sortie avec les littéraux de gabarit**_

Nous pouvons faire beaucoup plus avec les littéraux de gabarit, et vous pouvez consulter [ici](https://css-tricks.com/template-literals/) pour plus de détails.

### 3. Les fonctions fléchées

Les fonctions fléchées utilisent une flèche grasse `=>` plutôt que le mot-clé `function`, lors de la définition d'une fonction :

Fonction JavaScript :

```js
var sum = function addition (firstNum, secondNum) {
    return firstNum + secondNum;
}
```

Fonction ES6 :

```js
let sum = (firstNum, secondNum) => { return firstNum + secondNum };
```

Nous pouvons également omettre le mot-clé `return`, sauf si notre fonction retourne un **bloc de code.**

Puisque cet article est une vue d'ensemble d'ES6, je ne vais pas approfondir les fonctions fléchées. Vous pouvez obtenir plus d'informations sur les fonctions fléchées [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).

### 4. Les opérateurs de décomposition et de repos

Avez-vous déjà vu trois points `...` en programmation ? Cela s'appelle la **syntaxe de décomposition.**

#### Opérateur de décomposition — Utilisation pour les tableaux

Nous avons un tableau de nombres : `let numberArray = [1, 19, 21, 85, 42]`

Nous pouvons utiliser l'opérateur de décomposition :

* pour obtenir les valeurs (nombres) hors du tableau :

```js
console.log(...numberArray);
```

![Image](https://cdn-media-1.freecodecamp.org/images/Z1e3qPXYxxSSKjLlMS6Q2Lv3yTPHzKK2YAsD)
_**Les nombres sont maintenant hors du tableau**_

**L'utilisation de l'opérateur de décomposition n'affecte pas le tableau lui-même.**

* pour concaténer le tableau avec un autre tableau :

```js
let charArray = ['a','b','c'];

charArray.push(...numberArray);

console.log(charArray);
```

![Image](https://cdn-media-1.freecodecamp.org/images/bGTjyMyTgSrg82mgjGSEKGTmhWN3pNa0kq5g)
_**valeurs dans numberArray ajoutées à charArray**_

Sinon, le **numberArray** serait ajouté comme quatrième élément, directement à l'intérieur du **charArray** :

![Image](https://cdn-media-1.freecodecamp.org/images/P2vv2Sq1-oWKuRDrupnWS9N4XZgdHZZGXBgt)
_**Tableau dans un tableau, sans l'opérateur de décomposition**_

#### Opérateur de repos — Utilisation pour les fonctions

L'autre utilisation des trois points `...` est pour les paramètres de fonction.

Un **paramètre** donné après trois points se transforme en un **tableau** qui contiendra le reste des paramètres appelés l'**opérateur de repos.**

```js
function count (...counter) { // le paramètre devient un tableau
  console.log(counter.length);
}

count(); // 0
count(10); // 1
count(1, 10, 24, 99, 3); // 5
```

Puisque `...counter` est maintenant un tableau, nous pouvons obtenir sa longueur. Tous les paramètres donnés à la fonction `count()` sont maintenant des valeurs du tableau **counter** :

![Image](https://cdn-media-1.freecodecamp.org/images/dCKC-Kbux4M-bU7BPbMqDx4MapabhlxwTGic)
_**Nombre de paramètres = Longueur du tableau**_

### 5. Import & Export

Une autre nouvelle fonctionnalité d'ES6 est qu'elle nous permet d'**importer & exporter** nos classes, fonctions, et même variables vers d'autres parties (fichiers) de notre code. Cette approche nous aide beaucoup, nous les programmeurs, lorsque nous voulons diviser le code en morceaux plus petits. Cela augmente la lisibilité et la maintenance du code du projet à l'avenir.

Voyons comment cela fonctionne :

Tout d'abord, nous créons une fonction ES6 et l'**exportons** avec le mot-clé `export`.

```js
export let myFunction = () => { console.log('I am exported!'); }
```

Après cela, pour importer `myFunction` dans un autre fichier, nous devons définir son **chemin de dossier, nom du fichier**, et le mot-clé `import`.

```js
import { myFunction } from './yourFolderPath/fileName';
```

Enfin, appelez la fonction dans le fichier importé et utilisez-la.

```js
myFunction();
```

C'est ainsi que nous pouvons diviser notre code en morceaux plus petits, avec l'aide de l'export et de l'import. Nous pouvons également importer d'autres modules et services comme **HttpService, Router, Axios,** et **Bootstrap** pour les utiliser dans notre code aussi, après les avoir installés dans notre **node_modules**.

J'ai expliqué certaines nouvelles fonctionnalités d'ES6 dans cet article. Il y a beaucoup d'autres fonctionnalités et plus de détails que vous devriez consulter. Si vous trouvez cet article utile, veuillez le partager pour que plus de personnes puissent le lire.

Merci pour votre lecture et pour votre soutien ! 😊