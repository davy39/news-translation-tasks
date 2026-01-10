---
title: Qu'est-ce que JavaScript ? Une définition du langage de programmation JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-29T23:35:23.000Z'
originalURL: https://freecodecamp.org/news/what-is-javascript-definition-of-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6060ec269618b008528a8ce1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que JavaScript ? Une définition du langage de programmation JS
seo_desc: 'By Dillion Megida

  JavaScript is a dynamic programming language that''s used for web development, in
  web applications, for game development, and lots more. It allows you to implement
  dynamic features on web pages that cannot be done with only HTML and ...'
---

Par Dillion Megida

JavaScript est un langage de programmation dynamique utilisé pour le développement web, dans les applications web, pour le développement de jeux, et bien plus encore. Il vous permet d'implémenter des fonctionnalités dynamiques sur les pages web qui ne peuvent pas être réalisées avec uniquement HTML et CSS.

De nombreux navigateurs utilisent JavaScript comme langage de script pour effectuer des actions dynamiques sur le web. Chaque fois que vous voyez un menu déroulant qui s'affiche au clic, du contenu supplémentaire ajouté à une page, et des couleurs d'éléments qui changent dynamiquement sur une page, pour ne citer que quelques fonctionnalités, vous voyez les effets de JavaScript.

## À quoi ressemblerait le Web sans JavaScript ?

Sans JavaScript, tout ce que vous auriez sur le web serait HTML et CSS. Ces deux langages seuls vous limitent à quelques implémentations de pages web. 90 % (sinon plus) de vos pages web seraient statiques, et vous n'auriez que les changements dynamiques comme les animations que CSS fournit.

## Comment JavaScript rend les choses dynamiques

HTML définit la structure de votre document web et le contenu qui s'y trouve. CSS déclare divers styles pour les contenus fournis sur le document web.

HTML et CSS sont souvent appelés langages de balisage plutôt que langages de programmation, car ils fournissent, à leur cœur, des balisages pour des documents avec très peu de dynamisme.

JavaScript, en revanche, est un langage de programmation dynamique qui prend en charge les calculs mathématiques, vous permet d'ajouter dynamiquement des contenus HTML au [DOM](https://thewebfor5.com/p/javascript/the-dom/), crée des déclarations de style dynamiques, récupère des contenus depuis un autre site web, et bien plus encore.

Avant d'aborder comment JavaScript fait toutes ces choses, regardons un exemple rapide.

Consultez ce codepen : https://codepen.io/Dillion/full/XWjvdMG

Dans le codepen, vous verrez que lorsque vous tapez dans le champ de saisie, le texte s'affiche à l'écran. Cela est rendu possible par JavaScript. Vous ne pouvez pas obtenir cela avec HTML, CSS, ni même les deux ensemble.

JavaScript peut faire bien plus que ce que je peux couvrir dans cet article. Mais pour vous initier à JS, nous allons examiner :

- comment utiliser JavaScript dans HTML
- les types de données
- les variables
- les commentaires
- les fonctions

## Comment utiliser JavaScript dans HTML

Tout comme avec CSS, JavaScript peut être utilisé dans HTML de diverses manières, telles que :

### 1. JavaScript en ligne

Ici, vous avez le code JavaScript dans des balises HTML dans certains attributs spéciaux basés sur JS.

Par exemple, les balises HTML ont des [attributs d'événement](https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Event_handlers) qui vous permettent d'exécuter du code en ligne lorsqu'un événement est déclenché. Voici ce que je veux dire :

```html
<button onclick="alert('Vous venez de cliquer sur un bouton')">Cliquez-moi !</button>
```

Ceci est un exemple de JavaScript en ligne. La valeur de `onclick` peut être un calcul, une addition dynamique au DOM – n'importe quel code JavaScript syntaxiquement valide.

### 2. JavaScript interne, avec la balise `script`

Tout comme la balise `style` pour les déclarations de style dans une page HTML, la balise `script` existe pour JavaScript. Voici comment elle est utilisée :

```html
<script>
	function(){
	    alert("Je suis à l'intérieur d'une balise script")
	}
</script>
```

### 3. JavaScript externe

Vous pouvez vouloir avoir votre code JavaScript dans un fichier différent. JavaScript externe permet cela. Pour de tels cas d'utilisation, voici comment cela se fait :

```html
<!-- index.html -->
<script src="./script.js"></script>
```

```js
// script.js
alert("Je suis à l'intérieur d'un fichier externe");
```

L'attribut `src` de la balise `script` vous permet d'appliquer une source pour le code JavaScript. Cette référence est importante car elle notifie le navigateur de également récupérer le contenu de `script.js`.

`script.js` peut être dans le même répertoire que `index.html`, ou il peut être obtenu depuis un autre site web. Pour ce dernier cas, vous devrez passer l'URL complète (`https://.../script.js`).

Remarquez l'extension `.js` ? C'est l'extension pour les fichiers JavaScript, tout comme HTML a `.html`.

Maintenant que nous avons examiné les moyens d'appliquer JavaScript à notre HTML, regardons quelques-unes des fonctionnalités de JavaScript.

## Types de données en JavaScript

En JavaScript, les données doivent être d'un type ou d'un autre. JavaScript doit le savoir afin de savoir comment les utiliser avec d'autres données ou comment opérer sur de telles données.

Voici les types de données de base que JavaScript prend en charge :

- Nombre (par exemple, `6`, `7`, `8.9`) : sur lesquels vous pouvez appliquer des opérations arithmétiques (comme l'addition) et bien plus encore
- Chaîne de caractères (comme `"javascript"`, `'une longue phrase'`, `un court paragraphe`) : tout ce qui se trouve entre des guillemets simples (`'...'`), des guillemets doubles (`"..."`) et des backticks (`...`). Il n'y a pas de différence entre les guillemets simples et doubles, mais les backticks ont plus de fonctionnalités, telles que :
  - interpoler des variables dans des chaînes, comme ceci : `Mon nom est ${name}`. `name` ici est une variable, injectée dans la chaîne.
  - chaînes multilignes. Avec des guillemets normaux, vous devriez ajouter des caractères d'échappement comme `\n` pour un saut de ligne, mais les backticks vous permettent de continuer votre chaîne sur une autre ligne, comme ceci :

```js
let str = `Je suis une
    chaîne multiligne`;
```

- Booléen (ne peut être que de deux valeurs : `true` ou `false`) : plus comme oui (`true`) ou non (`false`)
- Tableau (par exemple, `[1, 2, "bonjour", false]`) : un groupe de données (qui peuvent être de n'importe quel type, y compris des tableaux) séparées par une virgule. L'indexation commence à 0. L'accès au contenu d'un tel groupe peut se faire comme suit : `array[0]`, qui pour cet exemple retournera `1`, puisque c'est le premier élément.
- Objet (par exemple `{name: 'javascript', age: 5}`) : également un groupe de données mais sous la forme d'une paire `clé:valeur`. La `clé` doit être une chaîne de caractères, et la valeur peut être de n'importe quel type, y compris un autre objet. L'accès au contenu du groupe se fait avec la clé, par exemple `obj.age` ou `obj["age"]` retournera `5`.
- Indéfini (le seul type de données que ce type prend en charge est `undefined`) : Cette donnée peut être assignée à une variable explicitement, ou implicitement (par JavaScript) si une variable a été déclarée mais qu'aucune valeur ne lui a été assignée. Plus tard dans cet article, nous examinerons la déclaration de variables et l'assignation de valeurs.
- Null (le seul type de données que ce type prend en charge est `null`) : Null signifie qu'il n'y a pas de valeur. Il contient une valeur, mais pas une vraie valeur – plutôt, null.
- Fonction (par exemple, `function(){ console.log("fonction") }`) : Une fonction est un type de données qui invoque un bloc de code lorsqu'elle est appelée. Plus sur les fonctions plus tard dans cet article.

Les types de données JavaScript peuvent être un peu compliqués à comprendre. Vous avez peut-être entendu dire que les tableaux et les fonctions sont également des objets, et c'est vrai.

Comprendre cela implique de comprendre [la nature des prototypes JavaScript](https://dillionmegida.com/p/understanding-the-prototype-chain-in-javascript/). Mais, à un niveau de base, ce sont les types de données que vous devez d'abord connaître en JavaScript.

## Variables en JavaScript

Les variables sont des conteneurs pour des valeurs de n'importe quel type de données. Elles contiennent des valeurs de sorte que lorsque les variables sont utilisées, JavaScript utilise la valeur qu'elles représentent pour cette opération.

Les variables peuvent être déclarées et peuvent se voir assigner une valeur. Lorsque vous déclarez une variable, vous faites ceci :

```js
let name;
```

Pour ce qui précède, `name` a été déclaré, mais il n'a pas encore de valeur.

Comme vous vous en doutez à partir de la section sur les types de données, JavaScript assigne automatiquement une valeur de `undefined` à `name`. Donc, si vous essayez d'utiliser `name` n'importe où, `undefined` sera utilisé pour cette opération.

Voici ce que signifie assigner une valeur à une variable :

```js
let name;
name = "JavaScript";
```

Maintenant, si vous utilisez `name`, il représentera `JavaScript`.

Les déclarations et les assignations peuvent être faites en une seule ligne comme ceci :

```js
let name = "JavaScript";
```

Pourquoi `let` ? vous vous êtes peut-être demandé, et voici pourquoi : JavaScript prend en charge trois méthodes de déclaration de variables, qui sont :

- l'opérateur `var` : cela existe depuis la création de JavaScript. Vous pouvez déclarer des variables et leur assigner des valeurs qui peuvent être modifiées plus tard dans le code. Voici ce que je veux dire :

```js
var name = "JavaScript";
name = "Langage";
```

- l'opérateur `let` : cela est également très similaire à `var` – il déclare et assigne des valeurs à des variables qui peuvent être modifiées plus tard dans le code. La différence majeure entre ces opérateurs est que `var` hisse de telles variables, tandis que `let` ne hisse pas. Le concept de hissing peut être brièvement expliqué avec le code suivant :

```js
function print() {
	console.log(name);
	console.log(age);
	var name = "JavaScript";
	let age = 5;
}

print();
```

En appelant la fonction `print` (`print()`), le premier `console.log` imprime `undefined` tandis que le second `console.log` lance une erreur indiquant qu'il "Ne peut pas accéder à `age` avant l'initialisation".

Cela est dû au fait que la déclaration de la variable `name` est hissée (remontée) en haut de la fonction et l'assignation pour la variable reste à la même ligne tandis que la déclaration et l'assignation de `age` restent à la même ligne.

Voici comment le code ci-dessus est compilé :

```js
function print() {
	var name;
	console.log(name);
	console.log(age);
	name = "JavaScript";
	let age = 5;
}

print();
```

Les problèmes de hissing peuvent survenir de manière inattendue, et c'est pourquoi vous devriez utiliser `let` au lieu de `var`.

- l'opérateur `const` : cela ne hisse pas non plus les variables, mais il fait une chose de plus : il garantit qu'une variable ne peut pas se voir assigner une autre valeur que celle qui lui a été assignée lors de l'initialisation.

Par exemple :

```js
let name = "JavaScript"
name = "Langage" // pas d'erreurs

const age = 5
age = 6 // erreur, ne peut pas réassigner la variable
```

## Commentaires en JavaScript

Tout comme en HTML, parfois nous pouvons vouloir mettre une note à côté de notre code qui n'a pas besoin d'être exécutée.

Nous pouvons faire cela en JavaScript de deux manières :

- avec des commentaires sur une seule ligne, comme ceci : `// un commentaire sur une seule ligne`
- ou avec des commentaires multilignes, comme ceci :

```js
/*
un commentaire
multiligne
*/
```

## Fonctions en JavaScript

Avec les fonctions, vous pouvez stocker un bloc de code qui peut être utilisé à d'autres endroits dans votre code. Supposons que vous vouliez imprimer "JavaScript" et "Langage" à différents endroits dans votre code. Au lieu de faire ceci :

```js
console.log("JavaScript")
console.log("Langage")

// quelques choses ici

console.log("JavaScript")
console.log("Langage")

// plus de choses ici

console.log("JavaScript")
console.log("Langage")
```

Vous pouvez faire ceci :

```js
function print() {
    console.log("JavaScript")
    console.log("Langage")
}

print()

// quelques choses ici

print()

// plus de choses ici

print()
```

De cette manière, nous avons stocké le bloc de code répété dans une fonction qui peut être utilisée où nous le voulons. Mais ce n'est pas tout. Supposons que nous voulions trouver la moyenne de trois nombres. Le code pour cela serait :

```js
let num1 = 5
let num2 = 6
let num3 = 8
let average = (num1 + num2 + num3) / 3
```

Faire cela en dehors d'une fonction peut ne pas poser de problème, mais si nous devions faire cela à de nombreux endroits ? Alors, nous aurions une fonction comme ceci :

```js
function findAverage(n1, n2, n3) {
    let aver = (n1 + n2 + n3) / 3
    return aver
}

let num1 = 5
let num2 = 6
let num3 = 8
let average = findAverage(num1, num2, num3)

// plus tard, ailleurs
let average2 = findAverage(...)

// plus tard, ailleurs
let average3 = findAverage(...)
```

Comme vous le remarquerez dans la déclaration de `findAverage`, nous avons `n1, n2, n3` entre parenthèses. Ce sont des paramètres, qui servent de **placeholders** pour les valeurs qui seraient fournies lorsque la fonction doit être appelée.

Le bloc de code utilise ces placeholders pour trouver la moyenne, et le mot-clé `return` retourne la moyenne de la fonction.

Les placeholders rendent vos fonctions réutilisables de sorte que différentes valeurs à différents moments peuvent être passées aux fonctions pour utiliser la même logique.

## Conclusion

JavaScript a de nombreuses autres fonctionnalités que nous pourrions discuter, mais j'espère que cet article vous a donné un point de départ clair pour aller plus loin. Maintenant, vous devriez savoir ce qu'est le langage et comment vous pouvez l'utiliser sur le web.

Dans cet article, nous avons examiné comment ajouter du code JavaScript à nos fichiers HTML, les différents types de données que JavaScript prend en charge, les variables qui servent de conteneurs pour les valeurs, comment écrire des commentaires en JavaScript, et un peu sur la façon de déclarer et d'utiliser des fonctions.

Il y a tant d'endroits où aller à partir de ici, mais je recommanderais d'apprendre sur [Le DOM et comment JavaScript interagit avec lui](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) ensuite.