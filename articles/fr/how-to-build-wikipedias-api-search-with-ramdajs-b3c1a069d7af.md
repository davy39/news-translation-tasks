---
title: Comment utiliser l'API de recherche de Wikipédia pour construire une interface
  utilisateur avec RamdaJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T01:49:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-wikipedias-api-search-with-ramdajs-b3c1a069d7af
coverImage: https://cdn-media-1.freecodecamp.org/images/0*JFmZsramtJjAI0yJ.png
tags:
- name: api
  slug: api
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Ramda
  slug: ramda
- name: technology
  slug: technology
seo_title: Comment utiliser l'API de recherche de Wikipédia pour construire une interface
  utilisateur avec RamdaJS
seo_desc: 'By Yazeed Bzadough

  In this tutorial, we’ll build a UI using Wikipedia’s public search API along with
  some JavaScript + RamdaJS.

  Getting Started

  Here’s the GitHub link and Codesandbox link. Open your terminal and pick a directory
  to clone it.

  git clon...'
---

Par Yazeed Bzadough

Dans ce tutoriel, nous allons construire une interface utilisateur en utilisant l'API de recherche publique de Wikipédia ainsi que JavaScript + RamdaJS.

### Installation

Voici le [lien GitHub](https://github.com/yazeedb/ramda-wikipedia-search) et le [lien Codesandbox](https://codesandbox.io/s/y2zpq2xw39). Ouvrez votre terminal et choisissez un répertoire pour le cloner.

```
git clone https://github.com/yazeedb/ramda-wikipedia-search
cd ramda-wikipedia-search
yarn install (ou npm install)
```

La branche `master` contient le projet terminé, donc vérifiez la branche `start` si vous souhaitez coder en parallèle.

`git checkout start`

Et lancez le projet !

`npm start`

Votre navigateur devrait automatiquement ouvrir [localhost:1234](http://localhost:1234/).

### **Obtenir la valeur de l'entrée**

Voici l'application initiale.

![](https://cdn-media-1.freecodecamp.org/images/0*Wu4Qmu5newQZWGzt.png)

Pour capturer l'entrée de l'utilisateur au fur et à mesure qu'il tape, notre élément `input` a besoin d'un écouteur d'événement.

Votre fichier `src/index.js` est déjà configuré et prêt à l'emploi. Vous remarquerez que nous avons importé Bootstrap pour le style.

![](https://cdn-media-1.freecodecamp.org/images/0*qHfza67WgAEMZ-by.png)

Ajoutons un écouteur d'événement factice pour commencer.

```js
import 'bootstrap/dist/css/bootstrap.min.css';

const inputElement = document.querySelector('input');

inputElement.addEventListener('keyup', (event) => {
  console.log('valeur :', event.target.value);
});
```

Nous savons que `event.target.value` est la méthode standard pour accéder à la valeur d'une entrée. Maintenant, cela affiche la valeur.

![](https://cdn-media-1.freecodecamp.org/images/0*NLxwt8JdO7YkAUNV.png)

Comment Ramda peut-il nous aider à réaliser ce qui suit ?

- Récupérer `event.target.value`
- Supprimer les espaces (supprimer les espaces de début/fin)
- Par défaut, chaîne vide si `undefined`

La fonction `pathOr` peut en fait gérer les premier et troisième points. Elle prend trois paramètres : la valeur par défaut, le chemin et les données.

Donc, ce qui suit fonctionne parfaitement

```js
import { pathOr } from 'ramda';

const getInputValue = pathOr('', ['target', 'value']);
```

Si `event.target.value` est `undefined`, nous obtiendrons une chaîne vide !

Ramda a également une fonction `trim`, ce qui résout notre problème d'espaces.

```js
import { pathOr, trim } from 'ramda';

const getInputValue = (event) => trim(pathOr('', ['target', 'value'], event));
```

Au lieu d'imbriquer ces fonctions, utilisons `pipe`. Voir [mon article sur pipe](a-quick-intro-to-pipe-and-compose) si c'est nouveau pour vous.

```js
import { pathOr, pipe, trim } from 'ramda';

const getInputValue = pipe(
  pathOr('', ['target', 'value']),
  trim
);
```

Nous avons maintenant une fonction composée qui prend un objet `event`, récupère sa valeur `target.value`, la définit par défaut sur `''` et supprime les espaces.

Magnifique.

Je recommande de stocker cela dans un fichier séparé. Peut-être l'appeler `getInputValue.js` et utiliser la syntaxe d'exportation par défaut.

![](https://cdn-media-1.freecodecamp.org/images/1*EKKGBfZBV5jhZRl9S7wORw.png)

### Obtenir l'URL de Wikipédia

Au moment de la rédaction, l'URL de recherche de l'API de Wikipédia est [https://en.wikipedia.org/w/api.php?origin=*&action=opensearch&search=](https://en.wikipedia.org/w/api.php?origin=*&action=opensearch&search=)

Pour une recherche réelle, il suffit d'ajouter un sujet. Si vous avez besoin d'ours, par exemple, l'URL ressemble à ceci :

[https://en.wikipedia.org/w/api.php?origin=*&action=opensearch&search=bears](https://en.wikipedia.org/w/api.php?origin=*&action=opensearch&search=bears)

Nous aimerions une fonction qui prend un sujet et retourne l'URL complète de recherche Wikipédia. Au fur et à mesure que l'utilisateur tape, nous construisons l'URL basée sur son entrée.

La fonction `concat` de Ramda fonctionne bien ici.

```js
import { concat } from 'ramda';

const getWikipediaSearchUrlFor = concat(
  'https://en.wikipedia.org/w/api.php?origin=*&action=opensearch&search='
);
```

`concat`, fidèle à son nom, concatène les chaînes et les tableaux. Elle est curryfiée, donc fournir l'URL comme premier argument retourne une fonction attendant une deuxième chaîne. Voir [mon article sur le currying](https://medium.com/front-end-hacking/how-does-javascripts-curry-actually-work-8d5a6f891499) si c'est nouveau !

Placez ce code dans un module appelé `getUrl.js`.

![](https://cdn-media-1.freecodecamp.org/images/1*K-qJqHr60zKPUe_-5ql5cw.png)

Maintenant, mettons à jour `index.js`. Importez nos deux nouveaux modules, ainsi que `pipe` et `tap` de Ramda.

```js
import 'bootstrap/dist/css/bootstrap.min.css';
import { pipe, tap } from 'ramda';
import getInputValue from './getInputValue';
import getUrl from './getUrl';

const makeUrlFromInput = pipe(
  getInputValue,
  getUrl,
  tap(console.warn)
);

const inputElement = document.querySelector('input');

inputElement.addEventListener('keyup', makeUrlFromInput);
```

Ce nouveau code construit notre URL de requête à partir de l'entrée de l'utilisateur et la journalise via `tap`.

Vérifiez cela.

![](https://cdn-media-1.freecodecamp.org/images/1*xZxxcq2MpNutqcfvzTUXKQ.png)

### **Faire la requête AJAX**

L'étape suivante consiste à mapper cette URL à une requête AJAX et à collecter la réponse JSON.

Remplacez `makeUrlFromInput` par une nouvelle fonction, `searchAndRenderResults`.

```js
const searchAndRenderResults = pipe(
  getInputValue,
  getUrl,
  (url) =>
    fetch(url)
      .then((res) => res.json())
      .then(console.warn)
);
```

N'oubliez pas de changer également votre écouteur d'événement !

```js
inputElement.addEventListener('keyup', searchAndRenderResults);
```

Voici notre résultat.

![](https://cdn-media-1.freecodecamp.org/images/1*gMD8q10P6eFtW7qLNz7uXQ.png)

### **Créer un composant de résultats**

Maintenant que nous avons du JSON, créons un composant qui l'embellit.

Ajoutez `Results.js` à votre répertoire.

![](https://cdn-media-1.freecodecamp.org/images/1*5L38JxtvqbyjxfVeM2lRvA.png)

Revenez à notre réponse JSON de recherche Wikipédia. Notez sa forme. C'est un tableau avec les index suivants :

1. Requête (ce que vous avez recherché)
2. Tableau des noms des résultats
3. Tableau des résumés
4. Tableau des liens vers les résultats

Notre composant peut prendre un tableau de cette forme et retourner une liste bien formatée. Grâce à la destructuration de tableau ES6, nous pouvons utiliser cela comme signature de notre fonction.

Éditez `Results.js`

```js
export default ([query, names, summaries, links]) => `
  <h2>Recherche pour "${query}"</h2>
  <ul class="list-group">
    ${names.map(
      (name, index) => `
        <li class="list-group-item">
          <a href=${links[index]} target="_blank">
            <h4>${name}</h4>
          </a>
          <p>${summaries[index]}</p>
        </li>
      `
    )}
  </ul>
`;
```

Allons étape par étape.

- C'est une fonction qui prend un tableau de nos éléments attendus : `query`, `names`, `summaries` et `links`.
- En utilisant les [littéraux de gabarit ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals), elle retourne une chaîne HTML avec un titre et une liste.
- À l'intérieur de la balise `<ul>`, nous mappons `names` à des balises `<li>`, une pour chaque.
- À l'intérieur de celles-ci se trouvent des balises `<a>` pointant vers chaque lien de résultat. Chaque lien s'ouvre dans un nouvel onglet.
- Sous le lien se trouve un paragraphe de résumé.

Importez cela dans `index.js` et utilisez-le comme suit :

```js
// ...

import Results from './Results';

// ...

const searchAndRenderResults = pipe(
  getInputValue,
  getUrl,
  (url) =>
    fetch(url)
      .then((res) => res.json())
      .then(Results)
      .then(console.warn)
);
```

Cela passe le JSON de Wikipédia à `Results` et journalise le résultat. Vous devriez voir un tas de HTML dans votre console DevTools !

![](https://cdn-media-1.freecodecamp.org/images/0*_A5qIZOpTB3HPsga.png)

Il ne reste plus qu'à le rendre dans le DOM. Une simple fonction `render` devrait faire l'affaire.

```js
const render = (markup) => {
  const resultsElement = document.getElementById('results');

  resultsElement.innerHTML = markup;
};
```

Remplacez `console.warn` par la fonction `render`.

```js
const searchAndRenderResults = pipe(
  getInputValue,
  getUrl,
  (url) =>
    fetch(url)
      .then((res) => res.json())
      .then(Results)
      .then(render)
);
```

Et vérifiez cela !

![](https://cdn-media-1.freecodecamp.org/images/0*v6by39wYex3-NwIl.png)

Chaque lien devrait s'ouvrir dans un nouvel onglet.

### **Supprimer ces virgules étranges**

Vous avez peut-être remarqué quelque chose d'étrange dans notre nouvelle interface utilisateur.

![](https://cdn-media-1.freecodecamp.org/images/0*ZAeJJS-ZP1YNAv5f.png)

Elle a des virgules supplémentaires ! Pourquoi ??

### Littéraux de gabarit

C'est tout à propos de la façon dont les littéraux de gabarit joignent les choses. Si vous insérez un tableau, il le joindra en utilisant la méthode `toString()`.

Voyez comment cela devient joint ?

```js
const joined = [1, 2, 3].toString();

console.log(joined);
// 1,2,3

console.log(typeof joined);
// string
```

Les littéraux de gabarit font cela si vous mettez des tableaux à l'intérieur.

```js
const nums = [1, 2, 3];
const msg = `Mes numéros préférés sont ${nums}`;

console.log(msg);
// Mes numéros préférés sont 1,2,3
```

Vous pouvez corriger cela en joignant le tableau sans virgules. Utilisez simplement une chaîne vide.

```js
const nums = [1, 2, 3];
const msg = `Mes numéros préférés sont ${nums.join('')}`;

console.log(msg);
// Mes numéros préférés sont 123
```

Éditez `Results.js` pour utiliser la méthode `join`.

```jsx
export default ([query, names, summaries, links]) => `
  <h2>Recherche pour "${query}"</h2>
  <ul class="list-group">
    ${names
      .map(
        (name, index) => `
        <li class="list-group-item">
          <a href=${links[index]} target="_blank">
            <h4>${name}</h4>
          </a>
          <p>${summaries[index]}</p>
        </li>
      `
      )
      .join('')}
  </ul>
`;
```

Maintenant, votre interface utilisateur est beaucoup plus propre.

![](https://cdn-media-1.freecodecamp.org/images/0*JFmZsramtJjAI0yJ.png)

### **Corriger un petit bug**

J'ai trouvé un petit bug en construisant cela. L'avez-vous remarqué ?

![](https://cdn-media-1.freecodecamp.org/images/0*8qwAFsWU_6nKuXUH.png)

Vider l'`input` lance cette erreur.

![](https://cdn-media-1.freecodecamp.org/images/0*-aUVIsS0rtQoVomy.png)

C'est parce que nous envoyons une requête AJAX sans sujet de recherche. Vérifiez l'URL dans votre onglet Réseau.

![](https://cdn-media-1.freecodecamp.org/images/0*4cDzbOBm8Sw7KDwy.png)

Ce lien pointe vers une page HTML par défaut. Nous n'avons pas obtenu de JSON en retour parce que nous n'avons pas spécifié de sujet de recherche.

Pour empêcher cela de se produire, nous pouvons éviter d'envoyer la requête si l'`input` est vide.

Nous avons besoin d'une fonction qui **ne fait rien** si l'`input` est vide, et **effectue la recherche** s'il est rempli.

Créons d'abord une fonction appelée `doNothing`. Vous pouvez deviner à quoi elle ressemble.

```js
const doNothing = () => {};
```

Cela est mieux connu sous le nom de `noOp`, mais j'aime `doNothing` dans ce contexte.

Ensuite, retirez `getInputValue` de votre fonction `searchAndRenderResults`. Nous avons besoin d'un peu plus de sécurité avant de l'utiliser.

```js
const searchAndRenderResults = pipe(
  getUrl,
  (url) =>
    fetch(url)
      .then((res) => res.json())
      .then(Results)
      .then(render)
);
```

Importez `ifElse` et `isEmpty` de Ramda.

```js
import { ifElse, isEmpty, pipe, tap } from 'ramda';
```

Ajoutez une autre fonction, `makeSearchRequestIfValid`.

```js
const makeSearchRequestIfValid = pipe(
  getInputValue,
  ifElse(isEmpty, doNothing, searchAndRenderResults)
);
```

Prenez un moment pour absorber cela.

Si la valeur de l'entrée est vide, ne faites rien. Sinon, recherchez et affichez les résultats.

Vous pouvez rassembler ces informations simplement en lisant la fonction. _C'est_ expressif.

La fonction [isEmpty](https://ramdajs.com/docs/#isEmpty) de Ramda fonctionne avec les chaînes, les tableaux, les objets.

![](https://cdn-media-1.freecodecamp.org/images/0*VSddS4PKGUKcW_NC.png)

Cela la rend parfaite pour tester notre valeur d'entrée.

`ifElse` convient ici car lorsque `isEmpty` retourne vrai, `doNothing` s'exécute. Sinon, `searchAndRenderResults` s'exécute.

Enfin, mettez à jour votre gestionnaire d'événements.

```js
inputElement.addEventListener('keyup', makeSearchRequestIfValid);
```

Et vérifiez les résultats. Plus d'erreurs lors de la suppression de l'`input` !

![](https://cdn-media-1.freecodecamp.org/images/0*rKRi-EEHpN0FaRER.png)

Ce tutoriel provient de **mon** **cours entièrement gratuit** sur Educative.io, [Functional Programming Patterns With RamdaJS](https://www.educative.io/collection/5070627052453888/5738600293466112?authorName=Yazeed%20Bzadough) !

Veuillez envisager de le suivre/partager si vous avez apprécié ce contenu.

Il est rempli de leçons, de graphiques, d'exercices et d'exemples de code exécutables pour vous enseigner un style de programmation fonctionnelle de base en utilisant RamdaJS.

Merci d'avoir lu ❤️