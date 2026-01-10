---
title: Comment utiliser les fonctionnalités ES6 dans React
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2021-10-28T15:23:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-es6-javascript-features-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/g30.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment utiliser les fonctionnalités ES6 dans React
seo_desc: "Many JavaScript frameworks use ES6 features. So to help you learn these\
  \ handy features, I'll introduce you to them and then show you how to apply them\
  \ in React.js. \nHere are the ES6 features we'll cover in this guide:\n\nModules\n\
  Destructuring\nSpread Op..."
---

De nombreux frameworks JavaScript utilisent les fonctionnalités ES6. Pour vous aider à apprendre ces fonctionnalités pratiques, je vais vous les présenter puis vous montrer comment les appliquer dans React.js. 

Voici les fonctionnalités ES6 que nous allons couvrir dans ce guide :

* Modules
* Déstructuration
* Opérateur de décomposition (Spread Operator)
* Fonctions fléchées
* Littéraux de gabarit (Template Literals)

Tous les exemples que nous verrons ici sont assez basiques et devraient être faciles à comprendre pour les débutants.

## Comment utiliser les modules ES6 

Les modules vous aident à diviser les différentes fonctionnalités de votre application en fichiers/scripts séparés. Vous pouvez avoir différents scripts pour la validation de formulaire, la connexion d'un utilisateur, et ainsi de suite. 

Ici, nous aurons deux scripts : un pour additionner des nombres et l'autre pour soustraire des nombres. Nous allons procéder étape par étape.

Voici la structure de notre dossier :

> index.html  
> script.js  
> myModules/  
>  add.js  
>  sub.js

D'abord, nous verrons comment utiliser les modules en JavaScript vanilla. Ensuite, nous verrons comment les appliquer dans React.

### Étape 1 – Créer le fichier HTML et lier votre script

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <title>Modules ES6</title>
</head>
<body>
    <script type="module" src="script.js"></script>
</body>
```

Vous remarquerez que la balise script a un attribut `type` avec la valeur `module`. Ce devrait être la première chose à faire si vous allez utiliser la fonctionnalité Module. 

Vous pourriez rencontrer des ressources qui utilisent une méthode différente, comme ajouter une extension `.mjs` à leurs fichiers, mais pour être du bon côté, je recommande cette méthode. Le fichier `script.js` agira comme le "script parent" dans lequel nous importerons nos modules. 

### Étape 2 – Créer et exporter des fonctions dans des fichiers séparés

Voici la fonction pour l'addition dans `add.js` :

```javascript
export function add(a, b){
    return a + b;
}
```

Voici la fonction pour la soustraction dans `sub.js` :

```javascript
export function sub(a, b){
    return a - b;
}
```

Avez-vous remarqué l'instruction `export` ? Pour pouvoir utiliser ces fonctions dans d'autres scripts, vous devez les exporter en ajoutant l'instruction `export`. 

Ici, nous avons utilisé l'export en ligne en ajoutant l'instruction avant la fonction – mais vous pouvez choisir d'exporter cette fonction en bas du document comme ceci : `export default add;`.

### Étape 3 – Importer les fonctions dans `script.js`

```javascript
import { add } from "./myModules/add.js";
import { sub } from "./myModules/sub.js"

console.log(add(6, 4)); // 10

console.log(sub(6, 4));  // 2
```

Pour importer la fonction `add`, nous avons d'abord tapé l'instruction `import` suivie du nom de la fonction entre accolades et ensuite le chemin vers le fichier où la fonction se trouve. 

Vous pouvez voir comment nous avons utilisé `add(6, 4);` sans réinventer la roue en créant la fonction à partir de zéro. Maintenant, vous pouvez importer cette fonction dans n'importe quel script que vous voulez.

### Étape 4 – Comment appliquer les modules dans React.js

Maintenant que vous avez vu comment nous pouvons utiliser les modules en JavaScript vanilla, voyons comment vous pouvez les utiliser dans une application React. 

Lorsque vous créez une application React, le composant `App.js` agit généralement comme le composant principal. Nous allons créer un autre composant appelé `User.js` avec du contenu sur un utilisateur.

Voici le composant `App.js` :

```javascript
function App() {
  return (
    <div className="App">
      
    </div>
  )
}

export default App

```

Ce composant a simplement une `div` sans aucun contenu.

Et voici le composant `User.js` : 

```javascript
function User() {
    return (
        <div>
            <h1>Je m'appelle Ihechikara.</h1>
            <p>Je suis un développeur web.</p>
            <p>J'aime écrire.</p>
        </div>
    )
}

export default User

```

Si vous vous souvenez, vous pouvez exporter vos fonctions en bas du script comme nous venons de le faire. Ensuite, nous allons importer cette fonction dans le composant `App.js` :

```javascript
import User from "./User"

function App() {
  return (
    <div className="App">
      <User/>
    </div>
  )
}

export default App

```

Seulement deux ajouts au script : `import User from "./User"` qui pointe vers l'emplacement du composant, et `<User/>` étant le composant lui-même. 

Maintenant, vous pouvez réutiliser la logique dans le composant `User.js` à travers votre application et vous pouvez la rendre plus dynamique en utilisant des props au lieu de coder en dur les informations de l'utilisateur – mais cela dépasse le cadre de ce tutoriel.

## Comment utiliser la déstructuration ES6 

Déstructurer signifie démanteler la structure de quelque chose. En JavaScript, cette structure pourrait être un tableau, un objet, ou même une chaîne où les propriétés qui composent la structure seraient utilisées pour créer une nouvelle structure identique (les propriétés peuvent être altérées). 

Si ce que j'ai dit vous semble encore abstrait, ne vous inquiétez pas car vous comprendrez mieux à partir des exemples.

Avant ES6, voici comment vous extrairiez certaines données en JavaScript :

```javascript
var scores = [500, 400, 300];

var x = scores[0],
    y = scores[1],
    z = scores[2];

    console.log(x,y,z); // 500 400 300
```

Mais avec ES6, en utilisant la déstructuration, nous pouvons faire ceci :

```javascript
let scores = [500, 400, 300];

let [x, y, z] = scores;

console.log(x,y,z); //500 400 300
```

Les variables x, y et z hériteront des valeurs du tableau scores dans l'ordre où elles apparaissent, donc `x = 500`, `y = 400` et `z = 300`. Dans une situation où toutes les valeurs du tableau ont été héritées, toute autre valeur laissée sans valeur parente sera retournée comme indéfinie. C'est-à-dire :

```javascript
let scores = [500, 400, 300];

let [x, y, z, w] = scores;

console.log(x,y,z,w); //500 400 300 undefined
```

Voici un exemple utilisant des objets :

```javascript
let scores = {
    pass: 70,
    avg: 50,
    fail: 30
};

let { pass, avg, fail} = scores;

console.log(pass, avg, fail); // 70 50 30
```

Le processus est le même que pour la déstructuration des tableaux. 

Voici un autre exemple, mais avec des chaînes :

```javascript
let [user, interface] = 'UI';

console.log(user); // U

console.log(interface); // I
```

La chaîne a été divisée en lettres individuelles puis assignée aux variables du tableau.

### Comment utiliser la déstructuration dans React.js

Il existe divers scénarios où vous pourriez vouloir utiliser la déstructuration dans React. Mais un cas très courant serait avec le hook `useState`.

```javascript
import { useState } from 'react';

function TestDestructuring() {
    const [grade, setGrade] = useState('A');
    
    return(
        <>
        
        </>
    )
}

export default TestDestructuring

```

Ci-dessus, nous avons créé une variable constante `grade` ainsi qu'une fonction `setGrade` dont le but est de mettre à jour la valeur de la variable. Et nous avons défini la valeur de `grade` à 'A' en utilisant la déstructuration. 

## Comment utiliser l'opérateur de décomposition ES6 

L'opérateur de décomposition `...` vous permet de copier tout ou partie d'un tableau, d'un objet ou d'une chaîne dans un autre tableau, objet ou chaîne. Par exemple :

```javascript
const collectionOne = [10, 20, 30];
const collectionTwo = [40, 50, 60];

const allCollections = [...collectionOne, ...collectionTwo];

console.log(allCollections); //10, 20, 30, 40, 50, 60
```

Il n'y a vraiment pas grand-chose à cela. En utilisant le symbole `...`, toutes les valeurs des deux premières collections ont été assignées à la troisième collection. 

Maintenant que nous avons toutes les collections dans un tableau, nous allons utiliser l'opérateur de décomposition pour copier le tableau et obtenir le nombre le plus élevé. C'est-à-dire :

```
const allCollections = [10, 20, 30, 40, 50, 60];

const maxNumber = Math.max(...allCollections);
console.log(maxNumber) //60
```

### Comment combiner l'opérateur de décomposition avec la déstructuration

Dans la dernière section, nous avons vu l'application de la déstructuration en JavaScript. Maintenant, voyons comment nous pouvons combiner la déstructuration et l'opérateur de décomposition :

```javascript
let scores = [500, 400, 300];

let [x, ...y] = scores;

console.log(x); // 500

console.log(y); // [400, 300]
```

Ici, la variable `x` a hérité du premier nombre du tableau, puis la variable `y` s'est étendue sur le tableau et a copié tout ce qui restait.

## Comment utiliser les fonctions fléchées ES6 

En gros, les fonctions fléchées nous permettent d'écrire nos fonctions en utilisant une syntaxe plus courte. Avant ES6, voici comment vous écriviez une fonction :

```javascript
var greetings = function() {
  console.log("Hello World!")
}

//OU

function greetings2() {
  console.log("HI!")
}
```

Avec ES6, une syntaxe différente a été introduite :

```javascript
var greetings = () => {
  console.log("Hello World!")
}

var greetings = () => {
  console.log("HI!")
}

```

Le mot-clé `function` a été supprimé tandis que l'opérateur de flèche grasse `=>` a été introduit. 

Notez que les fonctions fléchées sont anonymes.

### Comment utiliser les fonctions fléchées avec des paramètres

Les paramètres dans les fonctions fléchées sont passés entre les parenthèses qui précèdent l'opérateur de flèche grasse. Exemple :

```javascript
var add = (a,b)=>{
  return a + b;
}
console.log(add(2,2)) //4
```

## Comment utiliser les littéraux de gabarit ES6

Les littéraux de gabarit vous permettent d'utiliser des backticks (``) au lieu de guillemets ("") pour définir une chaîne. Cela présente divers avantages.

Avant ES6 :

```
var name = "My name is Ihechikara" 

console.log(fullname);
```

Avec ES6 :

```javascript
var name = `My name is Ihechikara` 

console.log(fullname);
```

### Interpolation dans les littéraux de gabarit

L'interpolation de chaînes vous permet d'inclure des variables et des instructions dans vos chaînes sans les casser avec l'opérateur `+`. C'est-à-dire :

```javascript
var me = 'Ihechikara';

var fullname = `My name is Abba ${me}`;

console.log(fullname);
```

Pour interpoler une variable dans votre chaîne, vous utilisez `${}` avec le nom de la variable passé entre les accolades. N'oubliez pas que votre chaîne doit être imbriquée entre des backticks et non des guillemets. 

Il en va de même lorsque vous créez vos éléments DOM dynamiquement avec JavaScript. Vous feriez quelque chose comme ceci :

```javascript
let name = 'Ihechikara';
let myHtmlTemplate = `<h1> This is a paragraph created by ${name}</h1>`;
```

## Conclusion

Cet article a couvert certaines des fonctionnalités ES6 les plus importantes comme les modules, la déstructuration, l'opérateur de décomposition, les fonctions fléchées et les littéraux de gabarit. 

Vous verrez ces fonctionnalités utilisées fréquemment lors de l'apprentissage ou de la compréhension des frameworks JavaScript, donc cela devrait vous aider à saisir leur application dans n'importe quel framework où elles apparaissent. 

Si vous avez des questions sur ces fonctionnalités, vous pouvez me trouver sur Twitter [@ihechikara2](https://twitter.com/Ihechikara2). Merci d'avoir lu !