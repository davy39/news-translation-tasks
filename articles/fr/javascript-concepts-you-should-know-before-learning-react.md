---
title: Les concepts JavaScript à connaître avant d'apprendre React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-26T19:22:52.000Z'
originalURL: https://freecodecamp.org/news/javascript-concepts-you-should-know-before-learning-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-pixabay-417173--1-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Les concepts JavaScript à connaître avant d'apprendre React
seo_desc: 'By Ashutosh Mishra

  React is one of the most popular JavaScript frameworks for building single page
  applications. Needless to say, as a JavaScript framework, it requires you to have
  a good knowledge of JavaScript concepts.

  In this article, we are goin...'
---

Par Ashutosh Mishra

React est l'un des frameworks JavaScript les plus populaires pour créer des applications à page unique (SPA). Il va sans dire qu'en tant que framework JavaScript, il nécessite une bonne connaissance des concepts JavaScript.

Dans cet article, nous allons passer en revue certains de ces concepts JavaScript que vous devez impérativement connaître avant d'apprendre React. Une bonne compréhension de ces sujets est fondamentale pour construire des applications React à grande échelle. Alors, sans plus attendre, commençons.

## 1. Les bases de JavaScript

React est un framework JS et vous utiliserez JavaScript de manière intensive dans votre code React. Il est donc évident que vous devez connaître les concepts de base de JavaScript.

Par bases, j'entends des éléments tels que les variables, les types de données, les opérateurs, les conditions, les tableaux, les fonctions, les objets, les événements, etc.

Avoir une compréhension appropriée de ces concepts est important pour naviguer correctement dans React, car vous les utiliserez à chaque étape de la création d'applications React.

Si vous n'êtes pas sûr de ces éléments ou si vous souhaitez tout réviser rapidement, consultez [certains de ces cours gratuits](https://www.freecodecamp.org/news/learn-javascript-free-js-courses-for-beginners/) ou [le programme JavaScript de freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/). Les documents [MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript) et [JavaScript.info](https://javascript.info/) sont également des références de recherche rapide utiles.

## 2. L'opérateur ternaire

[L'opérateur ternaire](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) est un opérateur conditionnel court, sur une seule ligne, qui remplace if/else. Il est vraiment utile lorsqu'il s'agit de vérifier rapidement une condition pour rendre un composant, mettre à jour un état ou afficher du texte.

Comparons le fonctionnement de l'opérateur ternaire avec l'instruction If/Else :

```javascript
// Exemple d'opérateur ternaire
condition ? 'Vrai' : 'Faux'

```

```javascript
// Exemple d'instruction If/Else
if(condition) {
    'Vrai'
}
else {
    'Faux'
}:

```

Vous pouvez constater par vous-même à quel point l'utilisation de l'opérateur ternaire est plus propre et plus courte que celle de If/Else.

Son fonctionnement est le suivant : vous écrivez une condition, et si la condition est vraie, votre programme exécutera l'instruction après `?`. Si la condition est fausse, le programme exécutera l'instruction après `:`.

Simple, n'est-ce pas ?

## 3. La déstructuration

La [déstructuration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) nous aide à extraire des valeurs de tableaux et d'objets et à les affecter à des variables distinctes de manière simple et fluide. Comprenons cela avec du code :

```javascript
// Avec la déstructuration
const objects = ['table', 'iPhone', 'apple']
const [furniture, mobile, fruit] = objects

// Sans la déstructuration
const furniture = objects[0]
const mobile = objects[1]
const fruit = objects[2]

```

Dans l'exemple ci-dessus, la déstructuration nous a fait gagner 3 lignes de code et a rendu le code plus propre. Voyons maintenant un autre exemple de passage de props dans React avec la déstructuration :

```javascript
// Avec la déstructuration Ex-1
function Fruit({apple}) {
    return (
        <div>
            Ceci est une {apple}
        </div>
    )
}

// Avec la déstructuration Ex-2

function Fruit(props) {
    const {apple, iphone, car} = props
    return (
        <div>
            Ceci est une {apple}
        </div>
    )
}

// Sans la déstructuration
function Fruit(props) {
    return (
        <div>
            Ceci est une {props.apple}
        </div>
    )
}

```

Remarquez comment vous devez utiliser `props` encore et encore lorsque vous n'utilisez pas la déstructuration pour vos props.

La déstructuration rend notre code plus propre et nous évite d'utiliser le mot-clé **props** à chaque fois que vous utilisez une variable de prop. Il y a [plus à apprendre sur la déstructuration](https://www.freecodecamp.org/news/destructuring-patterns-javascript-arrays-and-objects/) et vous découvrirez ces choses lorsque vous commencerez à créer des applications en JavaScript et React.

## 4. L'opérateur Spread

L' [opérateur Spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) a été introduit dans JavaScript avec l'ES6. Il prend un [itérable](https://www.freecodecamp.org/news/demystifying-es6-iterables-iterators-4bdd0b084082/) et le décompose en éléments individuels.

Un cas d'utilisation courant de l'opérateur spread dans React est la copie des valeurs d'un objet dans un autre objet lors d'une mise à jour d'état pour fusionner les propriétés des deux objets. Regardez la syntaxe ci-dessous :

```javascript
const [person, setPerson] = useState({
    id: '',
    name: '',
    age: ''
});

 setPerson([
            ...person,
            {
                id:"1",
                name: "Steve",
                age:"25"
            }
        ]);

```

Dans l'exemple ci-dessus, `...person` copie toutes les valeurs de l'objet person dans le nouvel objet d'état qui est ensuite remplacé par d'autres valeurs personnalisées avec les mêmes propriétés, ce qui met à jour l'objet d'état.

C'était l'un des nombreux cas d'utilisation de l'opérateur spread dans React. À mesure que votre application s'agrandit, des outils comme l'opérateur spread s'avèrent utiles pour gérer les données de manière plus efficace.

## 5. Les méthodes de tableau

Les méthodes de tableau sont très courantes lors de la création d'une application de taille moyenne à grande en React. Vous utiliserez toujours une sorte de méthode de tableau dans presque chaque application React que vous construirez.

Prenez donc le temps d'apprendre ces méthodes. Certaines méthodes sont extrêmement courantes comme **map()**. Vous utilisez map() chaque fois que vous récupérez des données d'une ressource externe pour les afficher sur l'interface utilisateur.

Il existe d'autres méthodes comme filter, reduce, sort, includes, find, forEach, splice, concat, push et pop, shift et unshift, etc.

Certaines sont d'usage courant, d'autres seront rarement utilisées. La clé est de très bien comprendre les méthodes de tableau courantes et d'être simplement conscient de l'existence des autres afin de pouvoir les apprendre rapidement dès que vous en aurez besoin.

[Voici un manuel utile](https://www.freecodecamp.org/news/the-javascript-array-handbook/) sur les méthodes de tableau et le travail avec les tableaux en général en JavaScript pour en savoir plus.

## 6. Les fonctions fléchées

Les [fonctions fléchées](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) nous permettent de créer des fonctions de manière simple avec une syntaxe plus courte.

```javascript
// Fonctions régulières
function hello() {
    return 'hello'
}

// Fonctions fléchées
let hello = () => 'hello'

```

Les deux fonctions dans l'extrait de code ci-dessus fonctionnent de la même manière, mais vous pouvez voir que la fonction fléchée est beaucoup plus propre et plus courte. Les parenthèses vides () dans la syntaxe ci-dessus servent aux arguments. Même s'il n'y a pas d'arguments, ces parenthèses doivent être présentes.

Cependant, vous pouvez omettre ces parenthèses s'il n'y a qu'un seul argument présent dans la fonction, comme ceci :

```javascript
let square = num => num * num

```

Dans les fonctions fléchées d'une seule ligne, vous pouvez omettre l'instruction **return**. Vous pouvez également déclarer une fonction fléchée multiligne en utilisant des accolades {} comme pour les fonctions régulières.

```javascript
let square = num => {
    return num * num
}

```

## 7. Les promesses

Vous utilisez les [promesses](https://www.freecodecamp.org/news/what-is-promise-in-javascript-for-beginners/) pour gérer les [opérations asynchrones](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous) en JavaScript moderne. Une fois que vous créez une promesse en JavaScript, elle peut soit réussir, soit échouer – ce que l'on appelle être résolue (resolved) ou rejetée (rejected) dans la terminologie JavaScript.

Les promesses en JavaScript peuvent également, d'une certaine manière, être comparées aux promesses que nous faisons, nous les humains. Tout comme les promesses humaines sont motivées par la mise en œuvre future d'une certaine action, les promesses en JavaScript concernent la mise en œuvre future du code, aboutissant soit à sa résolution, soit à son rejet.

Il existe 3 états d'une promesse :

1. **En attente (Pending)** – Lorsque le résultat final de la promesse n'a pas encore été déterminé.
2. **Résolue (Resolved)** – Lorsque la promesse est résolue avec succès.
3. **Rejetée (Rejected)** – Lorsque la promesse est rejetée.

Une fois qu'une promesse est résolue ou rejetée avec succès, vous pouvez utiliser une méthode **.then()** ou **.catch()** sur celle-ci.

* La méthode **.then()** est appelée lorsqu'une promesse est soit résolue, soit rejetée. Elle prend 2 fonctions de rappel (callback) comme arguments. La première est exécutée lorsque la promesse est résolue et que le résultat est reçu, et la seconde est un argument optionnel au cas où la promesse serait rejetée.
* La méthode **.catch()** est utilisée comme gestionnaire d'erreurs et est appelée lorsque la promesse est rejetée ou présente une erreur d'exécution.

Assez de théorie, terminons cette section avec un exemple de promesse, incluant l'utilisation des méthodes `.then()` et `.catch()` :

```javascript
let promise = new Promise((resolve, reject) => {
  const i = "Promise";
  i === "Promise" ? resolve() : reject(); // Consultez la section sur l'opérateur ternaire ci-dessus pour mieux comprendre la syntaxe
  }
);

promise.
    then(() => {
        console.log('Votre promesse est résolue');
    }).
    catch(() => {
        console.log('Votre promesse est rejetée');
    });

```

## 8. L'API Fetch

L' [API Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) nous permet d'effectuer des requêtes asynchrones vers des serveurs web depuis le navigateur. Elle renvoie une promesse à chaque fois qu'une requête est faite, laquelle est ensuite utilisée pour récupérer la réponse de la requête.

Un fetch() de base prend un argument, l'URL de la ressource que vous souhaitez récupérer. Il renvoie ensuite une autre promesse qui se résout avec un objet `Response`. Cet objet **Response** est la représentation de la réponse HTTP.

Ainsi, pour obtenir le contenu JSON de cette promesse, vous devez utiliser la méthode **.json()** sur l'objet Response. Cela finira par renvoyer une promesse qui se résout avec le résultat des données JSON analysées du corps de la réponse.

Cela peut être un peu déroutant, alors portez une attention particulière à l'exemple ci-dessous :

```javascript
fetch('http://example.com/books.json') // récupération de l'URL de la ressource
  .then(response => response.json()); // appel de la méthode .json() sur la promesse
  .then(data => setState(data)); // mise à jour de l'état avec les données JSON

```

## 9. Async/Await

La fonctionnalité [Async/Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) offre un moyen plus efficace et plus propre de gérer les promesses. JavaScript est synchrone par nature et async/await nous aide à écrire des fonctions basées sur des promesses de manière à ce qu'elles paraissent synchrones en arrêtant l'exécution du code suivant jusqu'à ce que la promesse soit résolue ou rejetée.

Pour que cela fonctionne, vous devez d'abord utiliser le mot-clé **async** avant de déclarer une fonction. Par exemple, `async function promise() {}`. Placer **async** avant une fonction signifie que la fonction renverra toujours une promesse.

À l'intérieur d'une fonction async, vous pouvez utiliser le mot-clé `await` pour suspendre l'exécution ultérieure du code jusqu'à ce que cette promesse soit résolue ou rejetée. Vous ne pouvez utiliser **await** qu'à l'intérieur d'une fonction **async**.

Maintenant, terminons rapidement cette section avec un exemple :

```javascript
async function asyncFunction() {
    let promise = new Promise(resolve => {
        resolve();
    });
    let response = await promise; // la suite de l'exécution sera arrêtée jusqu'à ce que la promesse soit résolue ou rejetée
    return console.log(response);
}

```

Vous pouvez en apprendre davantage sur async et await [dans ce guide approfondi](https://www.freecodecamp.org/news/javascript-async-await-tutorial-learn-callbacks-promises-async-await-by-making-icecream/).

## 10. Les modules ES et Import/Export

Les [modules](https://www.freecodecamp.org/news/javascript-modules-beginners-guide/) ont été introduits dans JavaScript avec l'ES6. Chaque fichier est un module en soi. Vous pouvez extraire des objets, des variables, des tableaux, des fonctions, etc., d'un fichier et les utiliser dans un autre. C'est ce qu'on appelle l'importation et l'exportation de modules.

Dans React, nous utilisons les modules ES6 pour créer des fichiers séparés pour les composants. Chaque composant est exporté de son module et importé dans le fichier où il doit être rendu. Apprenons cela avec un exemple :

```javascript
function Component() {
    return(
        <div>Ceci est un composant</div>
    )
}

export default Component

```

```javascript
import Component from './Component'

function App() {
    return (
        <Component />
    )
}

```

Dans React, vous devez rendre chaque composant que vous déclarez dans le composant App.js.

Dans l'exemple ci-dessus, nous avons créé un composant appelé **Component** et l'avons exporté avec notre code `export default Component`. Ensuite, nous allons dans **App.js** et importons le **Component** avec le code suivant : `import Component from './Component'`.

## **Conclusion**

Vous êtes arrivé à la fin de l'article ! Jusqu'à présent, nous avons couvert les bases de JavaScript, notamment l'opérateur ternaire, la déstructuration, l'opérateur Spread, les méthodes de tableau, les fonctions fléchées, les promesses, l'API Fetch, Async/Await, ainsi que les modules ES6 et l'import/export.

J'espère que vous avez beaucoup appris de cet article et que vous comprenez certains des concepts JavaScript importants et pourquoi vous devez les apprendre en profondeur avant de vous lancer dans React.

Cet article ne remplace pas l'apprentissage approfondi de ces concepts par vous-même. Je n'ai donné qu'une introduction générale et expliqué pourquoi ils sont importants. C'est maintenant à vous de voir comment vous apprenez ces choses et développez vos connaissances à partir d'ici. Bonne chance dans votre parcours !

Vous pouvez utiliser les ressources tout au long de l'article pour approfondir ces concepts importants.

Consultez mon [blog](https://fullstackstage.com) pour lire plus de contenus de qualité comme celui-ci. Contactez-moi sur [Twitter](https://twitter.com/ashutoshmishrae) si vous avez une question à poser ou si vous voulez dire 'salut'.