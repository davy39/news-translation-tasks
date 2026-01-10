---
title: Modules JavaScript – Un guide pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-15T16:47:38.000Z'
originalURL: https://freecodecamp.org/news/javascript-modules-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/lego.jpg
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: Web Development
  slug: web-development
seo_title: Modules JavaScript – Un guide pour débutants
seo_desc: 'By Madison Kanna

  JavaScript modules (also known as ES modules or ECMAScript modules) were created
  to help make JavaScript code more organized and maintainable.

  Understanding how ES modules work will help you become a better JavaScript developer.
  In t...'
---

Par Madison Kanna

Les modules JavaScript (également connus sous le nom de modules ES ou modules ECMAScript) ont été créés pour aider à rendre le code JavaScript plus organisé et maintenable.

Comprendre comment fonctionnent les modules ES vous aidera à devenir un meilleur développeur JavaScript. Dans cet article, nous allons couvrir :

* [Qu'est-ce qu'un module ?](#heading-qu-est-ce-qu-un-module)
* [Qu'est-ce que les modules ES ? Pourquoi les utilisons-nous ?](#heading-qu-est-ce-que-les-modules-es-pourquoi-les-utilisons-nous)
* [Comment utiliser les modules ES](#heading-comment-utiliser-les-modules-es)
* [Autres systèmes de modules utilisés en JavaScript](#heading-autres-systemes-de-modules-en-javascript)

Commençons.

<h1 id="module">Qu'est-ce qu'un module ?</h1>

Un module en JavaScript est simplement un fichier de code. Vous pouvez considérer un module comme une unité de code réutilisable et indépendante.

Les modules sont les éléments de base de votre base de code. À mesure que votre application grandit, vous pouvez diviser votre code en plusieurs fichiers, également appelés modules.

L'utilisation de modules vous permet de décomposer de grands programmes en morceaux de code plus faciles à gérer.

<h1 id="es-modules">Qu'est-ce que les modules ES ? Pourquoi les utilisons-nous ?</h1>

**Les modules ES sont le système de modules officiel utilisé en JavaScript.** Il existe d'autres systèmes de modules qui peuvent être utilisés en JavaScript, et nous en parlerons plus tard. Mais pour l'instant, sachez que nous apprenons les modules ES plutôt que d'autres systèmes de modules parce qu'ils sont la norme pour les modules en JavaScript.

En tant que développeur JavaScript, vous utiliserez probablement les modules ES dans votre travail quotidien.

Voici quelques-uns des avantages que les développeurs obtiennent en utilisant les modules ES :

1. **Organisation.** En décomposant de grands programmes en morceaux plus petits de code lié, vous gardez votre programme organisé.
2. **Réutilisabilité.** Avec les modules ES, vous pouvez écrire du code à un endroit et réutiliser ce code dans d'autres fichiers de votre base de code. Par exemple, au lieu de réécrire la même fonction partout, vous pouvez écrire une fonction à l'intérieur d'un module et l'importer dans un autre fichier pour l'utiliser là-bas.

Plongeons dans un exemple utilisant les modules ES. Nous allons apprendre comment fonctionnent les modules ES afin que vous puissiez les utiliser dans vos projets à l'avenir. En travaillant avec les modules ES, nous verrons chacun des avantages ci-dessus démontrés.

<h1 id="how-to-use">Comment utiliser les modules ES</h1>

Commençons par créer un projet JavaScript vanilla sur [Replit](https://replit.com/). Vous pouvez également trouver le code complet [ici](https://replit.com/@madisonkanna/ES-Modules).

Une fois sur Replit, nous pouvons créer un nouveau projet et choisir HTML, CSS et JavaScript. Cela créera un projet de démarrage qui contient un fichier `index.html`, un fichier `script.js` et un fichier `style.css`. C'est tout ce dont nous avons besoin pour nous installer.

À l'intérieur de notre fichier index.html, nous allons modifier notre balise script pour inclure `type="module"`. Cela nous permettra de commencer à utiliser les modules ES dans notre code. Modifiez votre balise script pour qu'elle soit :

```javascript
<script type="module" src="script.js"></script>
```

Commençons par écrire une simple fonction d'addition. Cette fonction prendra deux nombres, les additionnera et retournera le résultat de cette addition. Nous appellerons également cette fonction. Nous allons écrire cette fonction dans notre fichier `script.js` :

```javascript
function add(a, b) {
 return a + b;
};
console.log(add(5, 5)); //sortie 10
```

Jusqu'à présent, notre fichier `script.js` est petit avec peu de code. Mais imaginez que cette application grandisse et que nous ayons des dizaines de fonctions comme celle-ci. Ce fichier `script.js` pourrait devenir trop grand et plus difficile à maintenir.

Évitons ce problème en créant un module. Nous pouvons le faire en cliquant sur 'Ajouter un fichier', dans notre replit. N'oubliez pas qu'un module est simplement un fichier de code lié.

Nous appellerons notre module `math.js`. Nous allons supprimer cette fonction d'addition de notre fichier `script.js`, et nous allons créer un nouveau fichier, `math.js`. Ce fichier sera notre module où nous garderons nos fonctions liées aux mathématiques. Placerons notre fonction d'addition à l'intérieur de ce fichier :

```javascript
// math.js

function add(a, b) {
 return a + b;
};
```

Nous avons décidé d'appeler ce module `math.js`, car nous créerons plus de fonctions liées aux mathématiques dans ce fichier plus tard.

Si nous devions ouvrir cette application et la voir d'un coup d'œil, nous saurions que notre logique liée aux mathématiques est à l'intérieur de ce fichier. Nous n'avons pas besoin de perdre du temps à entrer dans cette application et à rechercher nos fonctions mathématiques et à nous demander où elles se trouvent – nous les avons organisées proprement dans un fichier.

Ensuite, utilisons la fonction d'addition à l'intérieur de notre fichier `script.js`, même si la fonction elle-même vit maintenant à l'intérieur du fichier `math.js`. Pour ce faire, nous devons apprendre la syntaxe des modules ES. Parlons des mots-clés `export` et `import`.

## Le mot-clé export

Lorsque vous souhaitez rendre un module disponible dans d'autres fichiers que celui dans lequel il se trouve, vous pouvez utiliser le mot-clé `export`. Utilisons le mot-clé `export` avec notre fonction d'addition afin de pouvoir l'utiliser à l'intérieur de notre fichier `script.js`.

Ajoutons `export default` sous notre fonction d'addition à l'intérieur de math.js :

```javascript
// math.js

function add(a, b) {
 return a + b;
};

export default add;
```

Avec la dernière ligne, nous rendons cette fonction d'addition disponible pour une utilisation dans d'autres endroits que le module `math.js`.

Une autre façon d'utiliser le mot-clé `export` consiste à l'ajouter juste avant de définir notre fonction :

```js
// math.js

export default function add(a, b) {
 return a + b;
};
```

Ce sont deux façons différentes d'utiliser le mot-clé `export`, mais les deux fonctionnent de la même manière.

Vous vous demandez peut-être ce que signifie ce mot-clé `default` qui suit `export`. Nous y viendrons dans un instant. Pour l'instant, utilisons notre fonction `add` dans un autre fichier, maintenant que nous l'avons exportée.

## Le mot-clé import

Nous pouvons utiliser le mot-clé import pour importer notre fonction d'addition dans notre fichier `script.js`. Importer cette fonction signifie simplement que nous aurons accès à cette fonction et pourrons l'utiliser dans le fichier. Une fois la fonction importée, nous pouvons l'utiliser :

```js
// script.js
import add from './math.js';

console.log(add(2, 5)); //sortie 7
```

Ici, avec `./math.js`, nous utilisons une importation relative. Pour en savoir plus sur les chemins relatifs et absolus, consultez cette réponse utile de [StackOverflow](https://stackoverflow.com/questions/21306512/difference-between-relative-path-and-absolute-path-in-javascript).

Lorsque nous exécutons ce code, nous pouvons voir le résultat de l'appel de notre fonction d'addition, `7`. Maintenant, vous pouvez utiliser la fonction d'addition autant de fois que vous le souhaitez dans ce fichier.

Le code de la fonction d'addition elle-même est maintenant hors de vue, et nous pouvons utiliser la fonction d'addition sans nécessairement avoir besoin de regarder le code de la fonction elle-même.

Si nous commentions la ligne `import add from './math.js'` pour un moment, nous obtiendrions soudainement une erreur : `ReferenceError: add is not defined`. Cela est dû au fait que `script.js` n'a pas accès à la fonction d'addition à moins que nous n'importions explicitement cette fonction dans ce fichier.

Nous avons exporté notre fonction d'addition, l'avons importée dans notre fichier `script.js`, puis avons appelé cette fonction.

Regardons à nouveau notre fichier `math.js`. Comme mentionné précédemment, vous avez peut-être été confus lorsque vous avez vu le mot `default` avec le mot-clé `export`. Parlons davantage du mot-clé `default`.

## Exportations nommées versus exportations par défaut en JavaScript

Avec les modules ES, vous pouvez utiliser des exportations nommées ou des exportations par défaut.

Dans notre premier exemple, nous avons utilisé une **exportation par défaut**. Avec une exportation par défaut, nous avons exporté une seule valeur (notre fonction d'addition) de notre module `math.js`.

Lorsque vous utilisez une exportation par défaut, vous pouvez renommer votre importation si vous le souhaitez. Dans notre fichier `script.js`, nous pouvons importer notre fonction d'addition et l'appeler addition (ou tout autre nom) à la place :

```js
// script.js
import addition from './math.js';

console.log(addition(2, 5)); //sortie 7
```

D'autre part, les **exportations nommées** sont utilisées pour exporter _plusieurs valeurs_ d'un module.

Créons un exemple utilisant des exportations nommées. Retournez dans notre fichier `math.js`, créez deux autres fonctions, subtract et multiply, et placez-les sous notre fonction d'addition. Avec une exportation nommée, vous pouvez simplement supprimer le mot-clé `default` :

```js
// math.js

export default function add(a, b) {
 return a + b;
};

export function subtract(a, b) {
 return a - b;
};

export function multiply(a, b) {
 return a * b;
};
```

Dans `script.js`, supprimons tout le code précédent et importons nos fonctions subtract et multiply. Pour importer les exportations nommées, entourez-les de crochets :

```js
import { multiply, subtract } from './math.js';

```

Maintenant, nous pouvons utiliser ces deux fonctions à l'intérieur de notre fichier `script.js` :

```js
// script.js
import { multiply, subtract } from './math.js';

console.log(multiply(5, 5));

console.log(subtract(10, 4))
```

Si vous souhaitez renommer une exportation nommée, vous pouvez le faire avec le mot-clé `as` :

```js
import add, { subtract as substractNumbers } from './math.js';

console.log(substractNumbers(2, 5));
```

Ci-dessus, nous avons renommé notre importation `subtract` en `subtractNumbers`.

Revenons à notre fonction d'addition. Et si nous voulions l'utiliser à nouveau dans notre fichier `script.js`, aux côtés de nos fonctions `multiply` et `subtract` ? Nous pouvons le faire comme ceci :

```js
import add, { multiply, subtract } from './math.js';

console.log(multiply(5, 5));

console.log(subtract(10, 4))

console.log(add(10, 10));
```

Maintenant, nous avons appris comment utiliser les modules ES. Nous avons appris comment utiliser le mot-clé `export`, le mot-clé `import`, et nous avons appris les différences entre les exportations nommées et les exportations par défaut. Et nous avons appris comment renommer à la fois nos exportations par défaut et nos exportations nommées.

<h1 id="other">Autres systèmes de modules en JavaScript</h1>

Lorsque vous apprenez les modules, vous avez peut-être vu ou même utilisé un type d'importation différent, peut-être un qui ressemble à ceci :

```javascript
var models = require('./models')
```

C'est là que l'apprentissage des modules en JavaScript peut devenir confus. Plongeons dans une brève histoire des modules JavaScript pour clarifier la confusion.

L'exemple de code ci-dessus utilisant l'instruction `require` est CommonJS. CommonJS est un autre système de modules qui peut être utilisé en JavaScript.

Lorsque JavaScript a été créé pour la première fois, il n'avait pas de système de modules. Parce que JavaScript n'avait pas de système de modules, les développeurs ont créé leurs propres systèmes de modules au-dessus du langage.

Différents systèmes de modules ont été créés et utilisés au fil des ans, y compris CommonJS. En travaillant dans une base de code dans une entreprise ou dans un projet open source, vous pourriez repérer différents systèmes de modules utilisés.

En fin de compte, les modules ES ont été introduits comme le système de modules standardisé en JavaScript.

Dans cet article, nous avons appris ce que sont les modules et pourquoi les développeurs les utilisent. Nous avons appris comment fonctionnent les modules ES et les différents types de systèmes de modules en JavaScript.

Si vous avez aimé cet article, rejoignez mon [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f), où nous relevons des défis de codage ensemble chaque dimanche et nous soutenons mutuellement tout en apprenant de nouvelles technologies.

Si vous avez des commentaires ou des questions sur cet article, ou trouvez-moi sur Twitter [@madisonkanna](https://twitter.com/Madisonkanna).