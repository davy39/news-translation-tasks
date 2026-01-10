---
title: Comment annuler facilement les appels HTTP useEffect avec RxJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-07T17:25:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-cancel-useeffect-http-calls-with-rxjs-d1be418014e8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0P3r47A-UCKu5JgYjANzcA.png
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
seo_title: Comment annuler facilement les appels HTTP useEffect avec RxJS
seo_desc: 'By Yazeed Bzadough

  Now that React Hooks have been officially released, even more patterns are emerging
  across the Internet.

  useEffect

  The useEffect hook’s among the most popular, as it can replace componentDidMount,
  componentDidUpdate, and componentW...'
---

Par Yazeed Bzadough

Maintenant que les [React Hooks](https://reactjs.org/docs/hooks-overview.html) ont été officiellement publiés, encore plus de modèles émergent sur Internet.

### useEffect

Le hook `useEffect` est parmi les plus populaires, car il peut remplacer `componentDidMount`, `componentDidUpdate` et `componentWillUnmount`.

La plupart de la logique d'initialisation, de mise à jour et de nettoyage dont un composant peut avoir besoin peut être placée à l'intérieur de `useEffect`.

### Une mauvaise expérience utilisateur

Dans un projet récent, j'ai rencontré un scénario où `useEffect` agissait sur des requêtes HTTP qui ne m'intéressaient plus.

Conceptuellement, l'interface utilisateur était comme ceci :

![](https://cdn-media-1.freecodecamp.org/images/1*0P3r47A-UCKu5JgYjANzcA.png)

- Au premier chargement, récupérer la liste des fruits et rendre un `<button>` pour chacun.
- Cliquer sur un `<button>` pour récupérer les détails de ce fruit.

Mais regardez ce qui se passe lorsque je clique sur plusieurs fruits à la suite

![](https://cdn-media-1.freecodecamp.org/images/1*GFxf5hJp35gNFE_D_EuRAA.gif)

Bien après avoir arrêté de cliquer, la section des détails du fruit continuait à changer !

### Le Code

Voyons mon hook personnalisé qui utilise `useEffect`.

Voici les liens [Codesandbox](https://codesandbox.io/s/l5l746yll7) et [GitHub](https://github.com/yazeedb/useEffect-rxjs-cancel-fetch/) si vous souhaitez suivre. Le fichier est `useFruitDetail.js`.

```js
import { useEffect, useState } from 'react';
import { getFruit } from './api';

export const useFruitDetail = (fruitName) => {
  const [fruitDetail, setFruitDetail] = useState(null);

  useEffect(() => {
    if (!fruitName) {
      return;
    }

    getFruit(fruitName).then(setFruitDetail);
  }, [fruitName]);

  return fruitDetail;
};
```

Chaque fois que `fruitName` change, nous demandons ses détails. Et nous n'avons aucun moyen d'annuler une requête ! Donc, relancer cela rapidement entraîne de nombreux changements d'état qui ne nous intéressent plus.

Si vous rendez cela dans l'interface utilisateur, vous obtenez une expérience utilisateur désordonnée où la section des détails continue de clignoter jusqu'à ce que la dernière requête soit résolue.

### Entrez RxJS

Ignorer les anciennes requêtes est trivial avec RxJS.

Il peut faire bien plus que ce que je vais démontrer ici, donc je vous recommande vivement de [plonger dedans](https://www.learnrxjs.io/) !

Cette portion de notre code, le code _effect_, doit changer.

```js
() => {
  if (!fruitName) {
    return;
  }

  getFruit(fruitName).then(setFruitDetail);
};
```

Au lieu d'une Promesse, convertissons `getFruit` en un Observable en utilisant la fonction `defer` de RxJS. Et au lieu de `.then`, nous appellerons `.subscribe`.

```js
import { defer } from 'rxjs';

// ...

() => {
  if (!fruitName) {
    return;
  }

  defer(() => getFruit(fruitName)).subscribe(setFruitDetail);
};
```

Cela ne résout pas encore le problème. Nous devons toujours nous _désabonner_ si `fruitName` change.

Selon la [documentation de React](https://reactjs.org/docs/hooks-reference.html#cleaning-up-an-effect), nous pouvons retourner une fonction qui sera exécutée à la fin de notre effet. Cela agit comme la logique de nettoyage.

Donc quelque chose comme ceci :

```js
() => {
  if (!fruitName) {
    return;
  }

  const subscription = defer(() => getFruit(fruitName)).subscribe(
    setFruitDetail
  );

  return () => {
    subscription.unsubscribe();
  };
};
```

### Ça marche !

![](https://cdn-media-1.freecodecamp.org/images/1*DUS5ubg4kUxCbPk5nHRxvQ.gif)

Cette expérience est beaucoup plus propre !

En cliquant sur un autre fruit, `useEffect` voit que `fruitName` change et exécute la logique de nettoyage de l'effet précédent. Par conséquent, nous nous désabonnons de l'appel de récupération précédent et nous concentrons sur celui en cours.

Maintenant, notre interface utilisateur attend patiemment jusqu'à ce que l'utilisateur ait fini de cliquer et que les détails du dernier fruit soient retournés.

Merci d'avoir suivi ce tutoriel jusqu'à la fin !