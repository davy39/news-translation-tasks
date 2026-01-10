---
title: 5 leçons clés sur React que les tutoriels ne vous enseignent pas
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-14T18:02:20.000Z'
originalURL: https://freecodecamp.org/news/5-react-lessons-tutorials-dont-teach
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/5-key-lessons-react-tutorials-dont-teach.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'State Management '
  slug: state-management
seo_title: 5 leçons clés sur React que les tutoriels ne vous enseignent pas
seo_desc: "There are many essential concepts and lessons that React developers need\
  \ to know that simply aren't covered in most tutorials. \nI have handpicked the\
  \ topics I believe are some of the most important for you to know, but that few\
  \ articles have dedicate..."
---

Il existe de nombreux concepts et leçons essentiels que les développeurs React doivent connaître, mais qui ne sont tout simplement pas abordés dans la plupart des tutoriels. 

J'ai soigneusement sélectionné les sujets que je considère comme étant parmi les plus importants à connaître, mais auxquels peu d'articles ont consacré le temps de les couvrir en détail.

Examinons cinq leçons clés sur React qu'il vaut la peine de connaître et que vous ne trouverez peut-être pas ailleurs.

## 1. Comment l'état de React est réellement mis à jour

En tant que développeur React, vous savez que l'état peut être créé et mis à jour avec les hooks `useState` et `useReducer`.

Mais que se passe-t-il exactement lorsque vous mettez à jour l'état d'un composant avec l'un de ces hooks ? L'état est-il mis à jour immédiatement ou à un moment ultérieur ?

Examinons le code suivant, qui est une application de compteur très simple. Comme vous vous y attendez, vous pouvez cliquer sur le bouton et notre compteur augmente de 1.

```js
import React from 'react';

export default function App() {
  const [count, setCount] = React.useState(0)

  function addOne() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Compte : {count}</h1> {/* 1 (comme prévu) */}

      <button onClick={addOne}>+ 1</button>
    </div>
  );
}
```

Mais que se passe-t-il si nous essayons d'ajouter une ligne supplémentaire, qui met également à jour notre compteur de un — que pensez-vous qu'il se passera ? 

Lorsque vous cliquez sur le bouton, notre compteur affiché augmentera-t-il de un ou de deux ?

```js
import React from 'react';

export default function App() {
  const [count, setCount] = React.useState(0)

  function addOne() {
    setCount(count + 1);
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Compte : {count}</h1> {/* 1?! */}

      <button onClick={addOne}>+ 1</button>
    </div>
  );
}
```

Si nous exécutons ce code, nous voyons qu'il n'est incrémenté que de un ! Malgré la tentative d'incrémenter le compteur de un deux fois, avec deux mises à jour d'état séparées. 

_Pourquoi notre compteur affiche-t-il 1, malgré l'incrémentation claire de l'état de 1 deux fois ?_

La raison en est que React planifie une mise à jour d'état à effectuer lorsque nous mettons à jour l'état pour la première fois. Parce qu'elle est simplement planifiée et n'est pas effectuée immédiatement (elle est asynchrone et non synchrone), notre variable `count` n'est pas mise à jour avant que nous essayions de la mettre à jour une deuxième fois. 

En d'autres termes, parce que la mise à jour de l'état est planifiée, et non effectuée immédiatement, la deuxième fois que nous avons appelé `setCount`, `count` est toujours `0`, et non `1`. 

La manière dont nous pouvons corriger cela pour mettre à jour l'état de manière fiable, malgré le fait que les mises à jour d'état soient asynchrones, est d'utiliser la fonction interne disponible dans la fonction de définition de `useState`. 

Cela nous permet d'obtenir l'état précédent et de retourner la valeur que nous voulons qu'il soit dans le corps de la fonction interne. Lorsque nous utilisons ce modèle, nous voyons qu'il est incrémenté de deux comme nous le voulions initialement :

```js
import React from 'react';

export default function App() {
  const [count, setCount] = React.useState(0)

  function addOne() {
    setCount(prevCount => prevCount + 1); // 1
    setCount(prevCount => prevCount + 1); // 2
  }

  return (
    <div>
      <h1>Compte : {count}</h1>
      <button onClick={addOne}>+ 1</button>
    </div>
  );
}
```

## 2. Il est préférable d'utiliser plusieurs effets au lieu d'un seul

Lors de l'exécution d'un effet de bord, la plupart des développeurs React utiliseront `useEffect` une seule fois et tenteront d'effectuer plusieurs effets de bord dans la même fonction d'effet. 

À quoi cela ressemble-t-il ? Ci-dessous, vous pouvez voir où nous récupérons à la fois les données des posts et des commentaires dans un seul hook useEffect pour les mettre dans leurs variables d'état respectives :

```js
import React from "react";

export default function App() {
  const [posts, setPosts] = React.useState([]);
  const [comments, setComments] = React.useState([]);

  React.useEffect(() => {
    // récupération des données des posts
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((res) => res.json())
      .then((data) => setPosts(data));

    // récupération des données des commentaires
    fetch("https://jsonplaceholder.typicode.com/comments")
      .then((res) => res.json())
      .then((data) => setComments(data));
  }, []);

  return (
    <div>
      <PostsList posts={posts} />
      <CommentsList comments={comments} />
    </div>
  );
}
```

Au lieu d'essayer d'entasser tous vos effets de bord dans un seul hook d'effet, tout comme vous pouvez utiliser le hook d'état plus d'une fois, vous pouvez utiliser plusieurs effets. 

Faire cela nous permet de séparer nos différentes actions en différents effets pour une meilleure séparation des préoccupations. 

Une meilleure séparation des préoccupations est un avantage majeur que les hooks React offrent par rapport à l'utilisation des méthodes de cycle de vie dans les composants de classe. 

Dans des méthodes comme `componentDidMount`, par exemple, il était nécessaire d'inclure toute action que nous voulions effectuer après le montage de notre composant. Vous ne pouviez pas diviser vos effets de bord en plusieurs méthodes — chaque méthode de cycle de vie dans les classes peut être utilisée une fois et une seule. 

L'avantage majeur des hooks React est que nous sommes capables de diviser notre code en fonction de ce qu'il fait. Non seulement nous pouvons séparer les actions que nous effectuons après le rendu en plusieurs effets, mais nous pouvons également co-localiser notre état :

```js
import React from "react";

export default function App() {
  const [posts, setPosts] = React.useState([]);
  React.useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((res) => res.json())
      .then((data) => setPosts(data));
  }, []);

  const [comments, setComments] = React.useState([]);
  React.useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/comments")
      .then((res) => res.json())
      .then((data) => setComments(data));
  }, []);

  return (
    <div>
      <PostsList posts={posts} />
      <CommentsList comments={comments} />
    </div>
  );
}
```

Cela signifie que nous pouvons mettre le hook d'état avec le hook d'effet auquel il est lié. Cela aide à organiser notre code beaucoup mieux et à mieux comprendre ce qu'il fait au premier coup d'œil.

## 3. Ne pas optimiser les fonctions qui mettent à jour l'état (useState, useReducer)

Une tâche courante chaque fois que nous passons une fonction de rappel d'un composant parent à un composant enfant est de l'empêcher d'être recréée, sauf si ses arguments ont changé. 

Nous pouvons effectuer cette optimisation avec l'aide du hook `useCallback`. 

useCallback a été créé spécifiquement pour les fonctions de rappel qui sont passées aux composants enfants pour s'assurer qu'elles ne sont pas recréées inutilement, ce qui entraîne une perte de performance sur nos composants chaque fois qu'il y a un re-rendu. 

C'est parce que chaque fois que notre composant parent est re-rendu, il provoquera également le re-rendu de tous les composants enfants. C'est ce qui provoque la recréation de nos fonctions de rappel à chaque re-rendu. 

Cependant, si nous utilisons une fonction de définition pour mettre à jour l'état que nous avons créé avec les hooks useState ou useReducer, nous n'avons pas besoin de l'envelopper avec useCallback. 

En d'autres termes, il n'est pas nécessaire de faire ceci :

```js
import React from "react";

export default function App() {
  const [text, setText] = React.useState("")

  // Ne pas envelopper setText dans useCallback (il ne changera pas tel quel)
  const handleSetText = React.useCallback((event) => {
    setText(event.target.value);
  }, [])

  return (
    <form>
      <Input text={text} handleSetText={handleSetText} />
      <button type="submit">Submit</button>
    </form>
  );
}

function Input({ text, handleSetText }) {
  return(
    <input type="text" value={text} onChange={handleSetText}  />
  )
}
```

 La raison vient directement de la documentation React :

> React garantit que l'identité de la fonction setState est stable et ne changera pas lors des re-rendus. C'est pourquoi il est sûr de l'omettre de la liste des dépendances de useEffect ou useCallback. 

Par conséquent, non seulement nous n'avons pas besoin de l'optimiser inutilement avec useCallback, mais nous n'avons pas non plus besoin de l'inclure comme dépendance dans useEffect car il ne changera pas.

C'est important à noter car dans de nombreux cas, cela peut réduire le code que nous devons utiliser. Et surtout, c'est une tentative improductive d'optimiser votre code car elle peut entraîner des problèmes de performance propres.

## 4. Le hook useRef peut préserver l'état à travers les rendus

En tant que développeurs React, il est parfois très utile de pouvoir référencer un élément React donné avec l'aide d'une référence. Nous créons des références dans React avec l'aide du hook `useRef`. 

Il est important de noter, cependant, que `useRef` n'est pas seulement utile pour référencer un certain élément du DOM. La documentation React le dit elle-même : 

> L'objet ref qui est créé par useRef est un conteneur générique avec une propriété current qui est mutable et peut contenir n'importe quelle valeur. 

Il y a certains avantages à pouvoir stocker et mettre à jour des valeurs avec `useRef`. Il nous permet de stocker une valeur qui ne sera pas en mémoire et qui ne sera pas effacée à travers les re-rendus. 

Si nous voulions suivre une valeur à travers les rendus avec l'aide d'une simple variable, elle serait réinitialisée chaque fois que le composant est rendu. Cependant, si vous utilisez une référence, la valeur stockée dans celle-ci restera constante à travers les rendus de votre composant. 

_Quel est un cas d'utilisation pour tirer parti de useRef de cette manière ?_ 

Cela pourrait être utile dans le cas où nous voulons effectuer un effet de bord donné uniquement lors du rendu initial, par exemple :

```js
import React from "react";

export default function App() {
  const [count, setCount] = React.useState(0);
  const ref = React.useRef({ hasRendered: false });

  React.useEffect(() => {
    if (!ref.current.hasRendered) {
      ref.current.hasRendered = true;
      console.log("effectuer l'action une seule fois !");
    }
  }, []);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Compte : {count}</button>
    </div>
  );
}
```

Essayez d'exécuter ce code vous-même.

Comme vous le verrez, peu importe le nombre de fois où le bouton est cliqué, l'état est mis à jour, et un re-rendu a lieu, l'action que nous voulons effectuer (voir `console.log`) n'est effectuée qu'une seule fois.

## 5. Comment empêcher votre application React de planter

L'une des leçons les plus importantes pour les développeurs React à connaître, surtout s'ils n'ont pas encore poussé une application React sur le web, est de savoir quoi faire avec les erreurs non capturées. 

Dans l'exemple ci-dessous, nous essayons d'afficher un composant Header dans notre application, mais nous effectuons une action qui entraîne une erreur. À savoir, essayer d'obtenir une propriété à partir d'une valeur nulle :

```js
import React from "react";

export default function App() {
  return (
    <>
      <Header />
    </>
  );
}

function Header() {
  const user = null;

  return <h1>Bonjour {user.name}</h1>; // erreur !
}
```

Si nous poussons ce code en production, nous verrons un écran blanc exactement comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/5-key-lessons-1.png)

_Pourquoi ne voyons-nous rien ?_ 

Encore une fois, nous pouvons trouver la réponse à cela dans la documentation React : 

> À partir de React 16, les erreurs qui n'ont pas été capturées par une limite d'erreur entraîneront le démontage de tout l'arbre des composants React. 

Alors qu'en développement, vous voyez un grand message d'erreur rouge avec une trace de pile qui vous indique où l'erreur peut être trouvée. Lorsque votre application est en ligne, cependant, vous allez simplement voir un écran blanc. 

Ce n'est pas le comportement souhaité que vous voulez pour votre application. 

Mais il y a un moyen de le corriger, ou au moins de montrer à vos utilisateurs quelque chose qui leur indique qu'une erreur s'est produite si l'application plante accidentellement. Vous pouvez envelopper votre arbre de composants dans ce qu'on appelle une limite d'erreur. 

Les limites d'erreur sont des composants qui nous permettent de capturer les erreurs et de montrer aux utilisateurs un message de repli qui leur indique qu'un problème s'est produit. Cela peut inclure des instructions sur la façon de dismiss l'erreur (comme recharger la page). 

Nous pouvons utiliser une limite d'erreur avec l'aide du package `react-error-boundary`. Nous pouvons l'envelopper autour du composant que nous pensons être sujet aux erreurs. Il peut également être enveloppé autour de tout notre arbre de composants d'application :

```js
import React from "react";
import { ErrorBoundary } from "react-error-boundary";

export default function App() {
  return (
    <ErrorBoundary FallbackComponent={ErrorFallback}>
      <Header />
    </ErrorBoundary>
  );
}

function Header() {
  const user = null;

  return <h1>Bonjour {user.name}</h1>;
}

function ErrorFallback({ error }) {
  return (
    <div role="alert">
      <p>Oups, une erreur s'est produite :</p>
      <p style={{ color: "red" }}>{error.message}</p>
    </div>
  );
}
```

Vous pouvez également afficher le message d'erreur comme vous le souhaitez et le styliser comme vous le feriez pour n'importe quel composant normal. 

Le résultat que nous obtenons lorsqu'une erreur se produit est bien meilleur :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/5-key-lessons-2.png)

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*