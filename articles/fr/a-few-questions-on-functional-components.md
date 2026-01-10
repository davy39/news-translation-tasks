---
title: Comment utiliser les composants fonctionnels dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-03T08:11:26.000Z'
originalURL: https://freecodecamp.org/news/a-few-questions-on-functional-components
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/kelvyn-ornettte-sol-marte-86DcFWVMp0g-unsplash.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment utiliser les composants fonctionnels dans React
seo_desc: "By Cristian Salcescu\nHave you wondered how to create a component in React?\
  \ \nTo answer, it is as simple as creating a function returning an HTML-like syntax.\n\
  import React from 'react';\n\nfunction Counter({n}) {\n  return (\n    <div>{n}</div>\n\
  \  );\n}\n\nexp..."
---

Par Cristian Salcescu

Vous êtes-vous déjà demandé comment créer un composant dans React ?

Pour répondre, c'est aussi simple que de créer une fonction retournant une syntaxe de type HTML.

```js
import React from 'react';

function Counter({n}) {
  return (
    <div>{n}</div>
  );
}

export default Counter;
```

Voyons maintenant ce qui s'est passé dans le code ci-dessus. `Counter` est une fonction qui transforme un nombre en HTML. Et si vous regardez plus attentivement, `Counter` est une fonction pure. C'est exact, le genre de fonction qui retourne le résultat en fonction de ses entrées et n'a pas d'effets secondaires.

Cette explication amène une nouvelle question. Qu'est-ce qu'un effet secondaire ?

En résumé, un effet secondaire est toute modification de l'environnement à l'extérieur de la fonction ou toute lecture d'information de l'environnement extérieur qui peut changer.

Vous avez peut-être remarqué que j'ai utilisé la [syntaxe d'affectation par décomposition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) dans la liste des paramètres pour extraire le nombre d'entrée `n`. C'est parce que les composants prennent en entrée un seul objet appelé "props" qui contient toutes les propriétés qui leur sont envoyées.

Voici comment le paramètre `n` peut être défini à partir de n'importe quel autre composant :

```js
<Counter n={1} />
```

Dans un sens, cette syntaxe peut être imaginée comme un appel de fonction `Counter({n: 1})`. N'est-ce pas ?

Continuons notre voyage.

Les composants fonctionnels peuvent-ils avoir un état ? Comme le suggère le nom du composant, je veux stocker et modifier un compteur. Et si nous déclarions simplement une variable contenant un nombre à l'intérieur du composant ? Est-ce que cela fonctionnera ?

Découvrons-le.

Je vais commencer par déclarer la variable à l'intérieur du composant fonctionnel.

```js
import React from 'react';

function Counter() {
  let n = 0;
  return (
    <div>{n}</div>
  );
}

export default Counter;
```

Ajoutons maintenant la fonction qui incrémente le nombre et l'affiche dans la console. J'utiliserai la fonction comme gestionnaire d'événement pour l'événement clic.

```js
import React from 'react';

function Counter() {
  let n = 0;
  
  function increment(){
    n = n + 1;
    console.log(n)
  }
  
  return (
      <div>
        <span>{n}</span>
        <button onClick={increment}>Incrémenter </button>
      </div>
  );
}

export default Counter;
```

Si nous regardons la console, nous voyons que le nombre est effectivement incrémenté, mais cela ne se reflète pas à l'écran. Une idée ?

Vous avez raison… nous devons changer le nombre, mais nous devons aussi le restituer (re-render) à l'écran.

C'est ici que la fonction utilitaire des [React Hooks](https://reactjs.org/docs/hooks-intro.html) entre en jeu. Au fait, ces fonctions utilitaires sont appelées hooks et elles commencent par le mot "use". Nous allons utiliser l'un d'entre eux, [useState](https://reactjs.org/docs/hooks-state.html). Je vais également afficher le texte "re-render" dans la console pour voir combien de fois la fonction `Counter` est réellement appelée.

```js
import React, { useState } from 'react';

function Counter() {
  const [n, setN] = useState(0);
  
  console.log('re-render');
  
  function increment(){
    setN(n + 1);
    console.log(n)
  }
  
  return (
    <div>
        <span>{n}</span>
        <button onClick={increment}>Incrémenter </button>
    </div>
  );
}

export default Counter;
```

Lisons ce que fait `useState()`.

**Que retourne** `**useState**` **?** Il retourne une paire de valeurs : l'état actuel et une fonction qui le met à jour.

Dans notre cas, `n` est l'état actuel et `setN()` est la fonction qui le met à jour. Avez-vous vérifié la console pour voir combien de fois le texte "re-render" s'affiche ? Je vous laisse le soin de le découvrir.

Nous pouvons mettre à jour l'état non seulement en définissant la nouvelle valeur, mais aussi en fournissant une fonction qui retourne la nouvelle valeur.

Dans notre cas, la fonction qui fournit la nouvelle valeur s'appellera `increment()`. Comme vous le voyez, `increment()` est une fonction pure.

```js
import React, { useState } from 'react';

function increment(n){
  return n + 1;
}

function Counter() {
  const [n, setN] = useState(0);
  
  return (
    <div>
        <span>{n}</span>
        <button 
         onClick={() => setN(increment)}>
           Incrémenter 
        </button>
    </div>
  );
}

export default Counter;
```

Pour comprendre ce que fait `setN(increment)`, lisons la documentation.

_Passer une fonction de mise à jour vous permet d'accéder à la valeur de l'état actuel à l'intérieur de la fonction de mise à jour._

D'accord, donc `increment()` est appelée avec l'état `n` actuel et elle est utilisée pour calculer la nouvelle valeur de l'état.

# Dernières réflexions

Résumons ce que nous avons découvert.

Dans React, nous pouvons simplement définir un composant à l'aide d'une fonction qui retourne une syntaxe de type HTML.

Les React Hooks nous permettent de définir un état dans de tels composants fonctionnels.

Et enfin, nous nous sommes enfin débarrassés du pseudo-paramètre `this` dans les composants. Peut-être avez-vous remarqué que `this` devient ennuyeux en changeant de contexte quand on ne s'y attend pas. Ne vous inquiétez pas pour ça. Nous n'allons pas utiliser `this` dans les composants fonctionnels.

Si vous êtes arrivé jusqu'ici, vous pouvez également jeter un œil à mes livres.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/best-functional-programming-books) **!**

Pour en savoir plus sur l'application des techniques de programmation fonctionnelle à React, jetez un œil à **[Functional React](https://www.amazon.com/dp/B088FZQ1XN).**

Apprenez le **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2).

[Envoyez-moi vos commentaires sur Twitter](https://twitter.com/cristi_salcescu).