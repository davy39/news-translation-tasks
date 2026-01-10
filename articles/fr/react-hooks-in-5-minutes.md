---
title: Apprendre les Hooks React en 5 minutes - Un tutoriel pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-06T18:14:18.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-in-5-minutes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f8f740569d1a4ca4339.jpg
tags:
- name: speedrun
  slug: speedrun
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Apprendre les Hooks React en 5 minutes - Un tutoriel pour débutants
seo_desc: 'By Bob Ziroll

  Sometimes 5 minutes is all you''ve got. So in this article, we''re just going to
  touch on two of the most used hooks in React: useState and useEffect.

  If you''re not famliar with hooks, here''s the TL;DR: because of hooks, there''s
  almost no...'
---

Par Bob Ziroll

Parfois, 5 minutes sont tout ce que vous avez. Alors dans cet article, nous allons simplement aborder deux des hooks les plus utilisés dans React : `useState` et `useEffect`.

Si vous n'êtes pas familier avec les hooks, voici le TL;DR : grâce aux hooks, il n'y a presque plus besoin de composants basés sur des classes. Les hooks vous permettent de "vous accrocher" aux changements d'état et au cycle de vie sous-jacent d'un composant au sein d'un composant fonctionnel. De plus, ils améliorent souvent la lisibilité et l'organisation de vos composants.

Si vous souhaitez une introduction appropriée à ce sujet, vous pouvez rejoindre la liste d'attente pour mon [prochain cours avancé sur React](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=hooks_article), ou si vous êtes encore débutant, consultez mon [cours d'introduction à React](https://scrimba.com/g/glearnreact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=hooks_article).


## `useState`

Commençons par un composant fonctionnel.

```js
import React from 'react';

function App() {
  return (
    <div>
      <h1>0</h1>
      <button>Changer !</button>
    </div>
  );
}
```

![Compteur à 0](https://thepracticaldev.s3.amazonaws.com/i/sj6psapai8j9pawqx8hd.png)

Comme vous pouvez le voir, rien de spécial pour le moment. Nous rendons simplement du texte et un bouton (inutile).

Maintenant, importons notre tout premier hook, `useState`, pour apprendre à gérer l'état dans notre composant fonctionnel.

Comme ce hook est une fonction, faisons un `console.log` de ce que nous obtenons en retour.

```js
import React, { useState } from 'react';

function App() {
  const value = useState();
  console.log(value);

  return (
    <div>
      <h1>0</h1>
      <button>Changer !</button>
    </div>
  );
}
```

Dans la console, nous obtenons un tableau

```js
> [null, ()]
```

Et lorsque nous passons un argument à `useState`

```js
const value = useState(true);
```

Dans la console, nous obtenons un tableau avec notre valeur comme premier membre.

```js
> [true, ()]
```

Maintenant, dans notre composant, nous pouvons accéder à notre état à `value[0]` et le rendre dans `<h1>` au lieu d'une valeur codée en dur.

```js
import React, { useState } from 'react';

function App() {
  const value = useState(0);
  console.log(value); // [0, ()]

  return (
    <div>
      <h1>{value[0]}</h1>
      <button>Changer !</button>
    </div>
  );
}
```

![Compteur à 0](https://thepracticaldev.s3.amazonaws.com/i/sj6psapai8j9pawqx8hd.png)

Nous pouvons améliorer notre code en utilisant la destructuration de tableau pour stocker la valeur du hook `useState`. C'est similaire à la destructuration d'objet, qui tend à être un peu plus couramment vue. Au cas où vous ne seriez pas très familier avec la destructuration d'objet, voici un rapide récapitulatif :

```js
const person = {
  name: 'Joe',
  age: 42
};

// crée 2 valeurs const à partir de l'objet person
const { name, age } = person;
console.log(name); // 'Joe'
console.log(age); // 42
```

La destructuration de tableau est presque la même, mais utilise des crochets `[]` au lieu d'accolades `{}`.

Un petit conseil : dans la destructuration d'objet, les noms des variables créées doivent correspondre aux noms des propriétés dans l'objet. Pour la destructuration de tableau, ce n'est pas le cas. Tout est une question d'ordre. L'avantage ici est que nous pouvons nommer les éléments comme nous le souhaitons.

En utilisant la destructuration de tableau, nous pouvons obtenir la valeur initiale de l'état à partir du hook `useState()`.

```js
import React, { useState } from 'react';

function App() {
  // rappelez-vous, il y a un deuxième élément du tableau qui manque ici, mais nous allons bientôt l'utiliser
  const [count] = useState(0);  

  return (
    <div>
      <h1>{count}</h1>
      <button>Changer !</button>
    </div>
  );
}
```

OK, nous avons la valeur initiale de l'état. Comment changeons-nous la valeur dans l'état avec les hooks ?

Rappelez-vous que le hook `useState()` retourne un tableau avec 2 membres. Le deuxième membre est une fonction qui met à jour l'état !

```js
const [count, setCount] = useState(0);
```

Vous pouvez, bien sûr, l'appeler comme vous le souhaitez, mais par convention, elle est normalement appelée avec le préfixe "set-", et ensuite le nom de la variable d'état que nous souhaitons mettre à jour, donc `setCount` c'est.

Il est simple d'utiliser cette fonction. Il suffit de l'appeler et de passer la nouvelle valeur que vous souhaitez pour cet état ! Ou, tout comme `this.setState` dans un composant de classe, vous pouvez passer une fonction qui reçoit l'ancien état et retourne le nouvel état. Règle générale : faites cela chaque fois que vous devez vous baser sur l'état passé pour déterminer le nouvel état.

Pour l'appeler, nous allons la passer à l'écouteur d'événement `onClick`. Et tout comme avec un `setState` régulier dans un composant basé sur une classe, nous pouvons passer notre mise à jour d'état à `setCount`.

```js
function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={() => setCount(prevCount => prevCount + 1)}>
        Changer !
      </button>
    </div>
  );
}
```

Nous pouvons nettoyer cela un peu, en extrayant notre mise à jour d'état dans une fonction séparée.

```js
function App() {
  const [count, setCount] = useState(0);

  function change() {
    setCount(prevCount => prevCount + 1);
  }

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={change}>Changer !</button>
    </div>
  );
}
```

Super ! Et maintenant, nous pouvons voir le compteur augmenter lorsque nous cliquons sur le bouton.

![Compteur à 1](https://thepracticaldev.s3.amazonaws.com/i/c7hobmvn77cp79bs4n4k.png)

Bien sûr, `useState` peut devenir beaucoup plus compliqué que cela, mais nous n'avons que 5 minutes ici, alors passons au hook suivant pour l'instant.

## `useEffect`

Les hooks ont simplifié plusieurs choses, par rapport à la manière dont les choses étaient dans les composants basés sur des classes. Auparavant, nous devions connaître un peu les méthodes de cycle de vie et laquelle était la mieux adaptée à quelle situation. Le hook `useEffect` a simplifié cette situation. Si vous souhaitez effectuer des effets secondaires, des requêtes réseau, des manipulations manuelles du DOM, des écouteurs d'événements ou des délais et intervalles.

Le hook `useEffect` peut être importé tout comme `useState`.

```js
import React, { useState, useEffect } from 'react';
```

Pour faire faire quelque chose à `useEffect`, nous lui passons une fonction anonyme comme argument. Chaque fois que React re-rend ce composant, il exécutera la fonction que nous passons à `useEffect`.

```js
useEffect(() => {
  /* toute mise à jour peut se produire ici */
});
```

Voici à quoi pourrait ressembler tout le code.

```js
import React, { useState, useEffect } from 'react';

function App() {
  const [count, setCount] = useState(0);

  function change() {
    setCount(prevCount => prevCount + 1);
  }

  useEffect(() => {
    /* toute mise à jour peut se produire ici */
  });

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={change}>Changer !</button>
    </div>
  );
}

export default App;
```

Par exemple, nous allons utiliser un joli package `npm` qui génère une couleur aléatoire. N'hésitez pas à écrire le vôtre si vous le souhaitez, bien sûr, mais pour ce tutoriel, nous allons simplement l'installer, `npm i randomcolor`, et l'importer.

```js
import randomcolor from 'randomcolor';
```

Utilisons maintenant nos connaissances sur le hook `useState` pour stocker une couleur aléatoire dans l'état.

```js
const [color, setColor] = useState(''); // la valeur initiale peut être une chaîne vide
```

Nous pouvons ensuite attribuer la couleur du compteur que nous avons déjà.

```js
<h1 style={{ color: color }}>{count}</h1>
```

Maintenant, juste pour le plaisir, changeons la couleur du compteur à chaque clic sur le bouton `Changer !`. `useEffect` s'exécutera chaque fois que le composant sera re-rendu, et le composant sera re-rendu chaque fois que l'état sera changé.

Donc si nous écrivons le code suivant, nous serions coincés dans une boucle infinie ! C'est un piège très courant avec `useEffect`

```js
useEffect(() => {
  setColor(randomcolor());
});
```

`setColor` met à jour l'état, ce qui re-rend le composant, ce qui appelle `useEffect`, ce qui exécute `setColor` pour mettre à jour l'état, ce qui re-rend le composant... Aïe !

Nous voulons probablement *uniquement* exécuter ce `useEffect` lorsque la variable `count` change.

Pour dire à `useEffect` quelle(s) variable(s) suivre, nous donnons un tableau de telles variables comme deuxième argument.

```js
useEffect(() => {
  setColor(randomcolor());
}, [count]);
```

![Compteur à 2](https://thepracticaldev.s3.amazonaws.com/i/pqxm4uxhbi2sygovu3gn.png)

Cela signifie essentiellement "n'exécutez cet effet que **si** l'état `count` change. De cette façon, nous pouvons changer la couleur et éviter que notre effet ne s'exécute indéfiniment.

## Conclusion

Il y a beaucoup plus à apprendre sur les hooks, mais j'espère que vous avez apprécié ce rapide aperçu de 5 minutes sur les hooks.

Pour en savoir plus sur les React Hooks et d'autres grandes fonctionnalités de React, vous pouvez rejoindre la liste d'attente pour mon [prochain cours avancé sur React](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=hooks_article). Ou si vous cherchez quelque chose de plus adapté aux débutants, vous pouvez consulter mon [cours d'introduction à React](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=hooks_article).


Bon codage 😊