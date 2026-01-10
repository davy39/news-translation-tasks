---
title: Comment créer une fonctionnalité de recherche GitHub dans React avec RxJS 6
  et Recompose
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T19:08:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-github-search-in-react-with-rxjs-6-and-recompose-e9c6cc727e7f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZeifRZJH1QudGiIiA6En4Q.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer une fonctionnalité de recherche GitHub dans React avec RxJS
  6 et Recompose
seo_desc: 'By Yazeed Bzadough

  This post is intended for those with React and RxJS experience. I’m just sharing
  patterns I found useful while making this UI.

  Here’s what we’re building:


  No classes, lifecycle hooks, or setState.

  Setup

  Everything’s on my GitHub.

  ...'
---

Par Yazeed Bzadough

Cet article s'adresse à ceux qui ont de l'expérience avec React et RxJS. Je partage simplement des modèles que j'ai trouvés utiles en créant cette interface utilisateur.

Voici ce que nous allons construire :

![](https://cdn-media-1.freecodecamp.org/images/1*KeoXx3EaGVrHXaZzK_QBzA.gif)

Pas de classes, de hooks de cycle de vie, ni de `setState`.

### Installation

Tout est sur [mon GitHub](https://github.com/yazeedb/recompose-github-ui).

```
git clone https://github.com/yazeedb/recompose-github-ui
cd recompose-github-ui
yarn install
```

La branche `master` contient le projet terminé, donc vérifiez la branche `start` si vous souhaitez suivre.

`git checkout start`

Et exécutez le projet.

`npm start`

L'application devrait s'exécuter sur `localhost:3000`, et voici notre interface utilisateur initiale.

![](https://cdn-media-1.freecodecamp.org/images/1*_XoqdpqQdmYrXs3q6_063w.png)

Ouvrez le projet dans votre éditeur de texte préféré et consultez `src/index.js`.

![](https://cdn-media-1.freecodecamp.org/images/1*iQy1zXOnGQIIb5noAzYvfw.png)

### Recompose

Si vous ne l'avez pas encore vu, [Recompose](https://github.com/acdlite/recompose/) est une excellente boîte à outils React pour créer des composants dans un style de programmation fonctionnelle. Il dispose d'une tonne de fonctions, et j'aurais du mal à choisir [mes préférées](my-favorite-recompose-functions).

C'est Lodash/Ramda, mais pour React. J'aime aussi qu'ils supportent les observables. Citant [la documentation](https://github.com/acdlite/recompose/blob/master/docs/API.md#observable-utilities) :

> Il s'avère que beaucoup de l'API des composants React peut être exprimée en termes d'observables

Nous allons exercer ce concept aujourd'hui ! 💡

### Diffusion de notre composant

Actuellement, `App` est un composant React ordinaire. Nous pouvons le retourner via un observable en utilisant la fonction [componentFromStream](https://github.com/acdlite/recompose/blob/master/docs/API.md#componentfromstream) de Recompose.

Cette fonction rend initialement [un composant null](https://github.com/acdlite/recompose/blob/master/src/packages/recompose/componentFromStream.js#L8), et _re-rend_ lorsque notre observable retourne une nouvelle valeur.

#### Une touche de configuration

Les flux Recompose suivent la [Proposition d'Observable ECMAScript](https://github.com/tc39/proposal-observable). Elle définit comment les observables doivent fonctionner lorsqu'ils seront finalement intégrés aux navigateurs modernes.

Cependant, jusqu'à ce qu'ils soient pleinement implémentés, nous dépendons de bibliothèques comme RxJS, xstream, most, Flyd, et ainsi de suite.

Recompose ne sait pas quelle bibliothèque nous utilisons, donc il fournit un `setObservableConfig` pour convertir les Observables ES vers/depuis ce dont nous avons besoin.

Créez un nouveau fichier dans `src` appelé `observableConfig.js`.

Et ajoutez ce code pour rendre Recompose compatible avec RxJS 6 :

```js
import { from } from 'rxjs';
import { setObservableConfig } from 'recompose';

setObservableConfig({
  fromESObservable: from
});
```

Importez-le dans `index.js` :

```js
import './observableConfig';
```

Et nous sommes prêts !

#### Recompose + RxJS

Importez `componentFromStream`.

```js
import React from 'react';
import ReactDOM from 'react-dom';
import { componentFromStream } from 'recompose';
import './styles.css';
import './observableConfig';
```

Et commencez à redéfinir `App` avec ce code :

```js
const App = componentFromStream((prop$) => {
  // ...
});
```

Remarquez que `componentFromStream` prend une fonction de rappel attendant un flux `prop$`. L'idée est que nos `props` deviennent un observable, et nous les mappons à un composant React.

Et si vous avez utilisé RxJS, vous connaissez l'opérateur parfait pour _mapper_ les valeurs.

#### Map

Comme son nom l'indique, vous transformez `Observable(quelqueChose)` en `Observable(autreChose)`. Dans notre cas, `Observable(props)` en `Observable(composant)`.

Importez l'opérateur `map` :

```js
import { map } from 'rxjs/operators';
```

Et redéfinissez App :

```js
const App = componentFromStream((prop$) => {
  return prop$.pipe(
    map(() => (
      <div>
        <input placeholder="Nom d'utilisateur GitHub" />
      </div>
    ))
  );
});
```

Depuis RxJS 5, nous utilisons `pipe` au lieu de chaîner les opérateurs.

Enregistrez et vérifiez votre interface utilisateur, même résultat !

![](https://cdn-media-1.freecodecamp.org/images/1*Edm3g3VL9121uIgwkzRiSA.png)

### Ajout d'un gestionnaire d'événements

Maintenant, nous allons rendre notre `input` un peu plus réactif.

Importez `createEventHandler` de Recompose.

```js
import { componentFromStream, createEventHandler } from 'recompose';
```

Et utilisez-le comme suit :

```jsx
const App = componentFromStream((prop$) => {
  const { handler, stream } = createEventHandler();

  return prop$.pipe(
    map(() => (
      <div>
        <input onChange={handler} placeholder="Nom d'utilisateur GitHub" />{' '}
      </div>
    ))
  );
});
```

`createEventHandler` est un objet avec deux propriétés intéressantes : `handler` et `stream`.

[Sous le capot](https://github.com/acdlite/recompose/blob/master/src/packages/recompose/createEventHandler.js), `handler` est un émetteur d'événements poussant des valeurs vers `stream`, qui est un observable diffusant ces valeurs à ses abonnés.

Nous allons donc combiner l'observable `stream` et l'observable `prop$` pour accéder à la valeur actuelle de l'`input`.

`combineLatest` est un bon choix ici.

#### Problème de la poule et de l'œuf

Pour utiliser `combineLatest`, cependant, `stream` et `prop$` doivent tous deux émettre. `stream` n'émettra pas tant que `prop$` n'aura pas émis, et vice versa.

Nous pouvons résoudre cela en donnant à `stream` une valeur initiale.

Importez l'opérateur `startWith` de RxJS :

```js
import { map, startWith } from 'rxjs/operators';
```

Et créez une nouvelle variable pour capturer le `stream` modifié.

```js
const { handler, stream } = createEventHandler();

const value$ = stream.pipe(
  map((e) => e.target.value),
  startWith('')
);
```

Nous savons que `stream` émettra des événements à partir de `input`'s onChange, donc mappons immédiatement chaque `event` à sa valeur textuelle.

En plus de cela, nous initialiserons `value$` comme une chaîne vide — une valeur par défaut appropriée pour un `input` vide.

#### Combiner le tout

Nous sommes prêts à combiner ces deux flux et à importer `combineLatest` comme méthode de création, **pas comme un opérateur**.

```js
import { combineLatest } from 'rxjs';
```

Vous pouvez également importer l'opérateur `tap` pour inspecter les valeurs au fur et à mesure qu'elles arrivent :

```js
import { map, startWith, tap } from 'rxjs/operators';
```

Et l'utiliser comme suit :

```jsx
const App = componentFromStream((prop$) => {
  const { handler, stream } = createEventHandler();
  const value$ = stream.pipe(
    map((e) => e.target.value),
    startWith('')
  );

  return combineLatest(prop$, value$).pipe(
    tap(console.warn),
    map(() => (
      <div>
        <input onChange={handler} placeholder="Nom d'utilisateur GitHub" />
      </div>
    ))
  );
});
```

Maintenant, lorsque vous tapez, `[props, value]` est journalisé.

![](https://cdn-media-1.freecodecamp.org/images/1*E1jAWy0UTDbWFfEh___Psg.png)

### Composant Utilisateur

Ce composant sera responsable de la récupération/de l'affichage du nom d'utilisateur que nous lui donnons. Il recevra la `value` de `App` et la mappers à un appel AJAX.

#### JSX/CSS

Tout est basé sur ce projet incroyable [GitHub Cards](https://lab.lepture.com/github-cards/). La plupart des éléments, surtout les styles, sont copiés/collés ou retravaillés pour s'adapter à React et aux props.

Créez un dossier `src/User`, et mettez [ce code](https://raw.githubusercontent.com/yazeedb/recompose-github-ui/master/src/User/User.css) dans `User.css` :

Et [ce code](https://raw.githubusercontent.com/yazeedb/recompose-github-ui/master/src/User/Component.js) dans `src/User/Component.js` :

Le composant remplit simplement un modèle avec la réponse JSON standard de l'API GitHub.

#### Le Conteneur

Maintenant que le composant "bête" est prêt, faisons le composant "intelligent" :

Voici `src/User/index.js` :

```jsx
import React from 'react';
import { componentFromStream } from 'recompose';
import { debounceTime, filter, map, pluck } from 'rxjs/operators';
import Component from './Component';
import './User.css';

const User = componentFromStream((prop$) => {
  const getUser$ = prop$.pipe(
    debounceTime(1000),
    pluck('user'),
    filter((user) => user && user.length),
    map((user) => <h3>{user}</h3>)
  );

  return getUser$;
});

export default User;
```

Nous définissons `User` comme un `componentFromStream`, qui retourne un flux `prop$` mappé à un `<h3>`.

#### debounceTime

Puisque `User` recevra ses props via le clavier, nous ne voulons pas écouter chaque émission.

Lorsque l'utilisateur commence à taper, `debounceTime(1000)` ignore toutes les émissions pendant 1 seconde. Ce modèle est couramment utilisé dans les [type-aheads](https://www.learnrxjs.io/operators/filtering/debouncetime.html).

#### pluck

Ce composant attend `prop.user` à un moment donné. `pluck` récupère `user`, donc nous n'avons pas besoin de déstructurer nos `props` à chaque fois.

#### filter

Assure que `user` existe et n'est pas une chaîne vide.

#### map

Pour l'instant, placez simplement `user` dans une balise `<h3>`.

#### Connexion

De retour dans `src/index.js`, importez le composant `User` :

<pre name="aa45" id="aa45" class="graf graf--pre graf-after--p">import User from './User';</pre>

Et fournissez `value` comme prop `user` :

```jsx
return combineLatest(prop$, value$).pipe(
  tap(console.warn),
  map(([props, value]) => (
    <div>
      <input onChange={handler} placeholder="Nom d'utilisateur GitHub" />
      <User user={value} />{' '}
    </div>
  ))
);
```

Maintenant, votre valeur est rendue à l'écran après 1 seconde.

![](https://cdn-media-1.freecodecamp.org/images/1*ti-OF_cqiKmQx1iTZZJFrA.gif)

Bon début, mais nous devons réellement récupérer l'utilisateur.

### Récupération de l'utilisateur

L'API Utilisateur de GitHub est disponible [ici](https://api.github.com/users). Nous pouvons facilement l'extraire dans une fonction helper à l'intérieur de `User/index.js` :

```js
const formatUrl = (user) => `https://api.github.com/users/${user}`;
```

Maintenant, nous pouvons ajouter `map(formatUrl)` après `filter` :

![](https://cdn-media-1.freecodecamp.org/images/1*bdCfDgYzFP9laQAg9Y1AKw.png)

Vous remarquerez que le point de terminaison de l'API est rendu à l'écran après 1 seconde maintenant :

![](https://cdn-media-1.freecodecamp.org/images/1*5ZTeqmDCGjnwe-MIP0H83g.png)

Mais nous devons faire une requête API ! Voici `switchMap` et `ajax`.

#### switchMap

Également utilisé dans les type-aheads, `switchMap` est idéal pour littéralement **basculer** d'un observable à un autre.

Supposons que l'utilisateur entre un nom d'utilisateur, et nous le récupérons à l'intérieur de `switchMap`.

Que se passe-t-il si l'utilisateur entre quelque chose de nouveau avant que le résultat ne revienne ? Nous nous soucions de la réponse précédente de l'API ?

Non.

`switchMap` annulera cette récupération précédente et se concentrera sur la actuelle.

#### ajax

RxJS fournit sa propre implémentation de `ajax` qui fonctionne parfaitement avec `switchMap` !

#### Les utiliser

Importons les deux. Mon code ressemble à ceci :

```js
import { ajax } from 'rxjs/ajax';
import { debounceTime, filter, map, pluck, switchMap } from 'rxjs/operators';
```

Et utilisez-les comme suit :

```js
const User = componentFromStream((prop$) => {
  const getUser$ = prop$.pipe(
    debounceTime(1000),
    pluck('user'),
    filter((user) => user && user.length),
    map(formatUrl),
    switchMap((url) =>
      ajax(url).pipe(
        pluck('response'),
        map(Component)
      )
    )
  );

  return getUser$;
});
```

**Basculez** de notre flux `input` vers un flux de requête `ajax`. Une fois la requête terminée, récupérez sa `response` et mappez-la à notre composant `User`.

Nous avons un résultat !

![](https://cdn-media-1.freecodecamp.org/images/1*NIVF7Iq9bjqremAKS2VOYQ.gif)

### Gestion des erreurs

Essayez d'entrer un nom d'utilisateur qui n'existe pas.

![](https://cdn-media-1.freecodecamp.org/images/1*cvF0zqPlndM4VAjyGHgxsQ.png)

Même si vous le changez, notre application est cassée. Vous devez actualiser pour récupérer plus d'utilisateurs.

Ce n'est pas une bonne expérience utilisateur, n'est-ce pas ?

#### catchError

Avec l'opérateur `catchError`, nous pouvons afficher une réponse raisonnable à l'écran au lieu de casser silencieusement.

Importez-le :

```js
import {
  catchError,
  debounceTime,
  filter,
  map,
  pluck,
  switchMap
} from 'rxjs/operators';
```

Et placez-le à la fin de votre chaîne `ajax`.

```jsx
switchMap((url) =>
  ajax(url).pipe(
    pluck('response'),
    map(Component),
    catchError(({ response }) => alert(response.message))
  )
);
```

![](https://cdn-media-1.freecodecamp.org/images/1*krBPGwW4tSv7FOxGaleZxQ.png)

Au moins nous obtenons un retour, mais nous pouvons faire mieux.

#### Un composant d'erreur

Créez un nouveau composant, `src/Error/index.js`.

```jsx
import React from 'react';

const Error = ({ response, status }) => (
  <div className="error">
    <h2>Oups !</h2>
    <b>
      {status}: {response.message}
    </b>
    <p>Veuillez essayer de rechercher à nouveau.</p>
  </div>
);

export default Error;
```

Cela affichera joliment `response` et `status` de notre appel AJAX.

Importons-le dans `User/index.js` :

```jsx
import Error from '../Error';
```

Et `of` de RxJS :

```jsx
import { of } from 'rxjs';
```

Rappelez-vous, notre rappel `componentFromStream` doit retourner un observable. Nous pouvons y parvenir avec `of`.

Voici le nouveau code :

```jsx
ajax(url).pipe(
  pluck('response'),
  map(Component),
  catchError((error) => of(<Error {...error} />))
);
```

Il suffit de répandre l'objet `error` comme props sur notre composant.

Maintenant, si nous vérifions notre interface utilisateur :

![](https://cdn-media-1.freecodecamp.org/images/1*OA8An4fuwA5CK4-ogDRwYw.gif)

Bien mieux !

### Un indicateur de chargement

Normalement, nous aurions maintenant besoin d'une forme de gestion d'état. Comment construire autrement un indicateur de chargement ?

Mais avant d'utiliser `setState`, voyons si RxJS peut nous aider.

La [documentation de Recompose](https://github.com/acdlite/recompose/blob/master/docs/API.md#observable-utilities) m'a fait réfléchir dans cette direction :

> Au lieu de `setState()`, combinez plusieurs flux ensemble.

**Édition** : J'ai initialement utilisé des `BehaviorSubject`s, mais [Matti Lankinen](https://medium.com/@milankinen) a répondu avec une manière brillante de simplifier ce code. Merci Matti !

Importez l'opérateur `merge`.

```jsx
import { merge, of } from 'rxjs';
```

Lorsque la requête est faite, nous fusionnerons notre `ajax` avec un flux de composant de chargement.

À l'intérieur de `componentFromStream` :

```jsx
const User = componentFromStream((prop$) => {
  const loading$ = of(<h3>Chargement...</h3>);
  // ...
});
```

Un simple indicateur de chargement `h3` transformé en observable ! Et l'utiliser comme suit :

```jsx
const loading$ = of(<h3>Chargement...</h3>);

const getUser$ = prop$.pipe(
  debounceTime(1000),
  pluck('user'),
  filter((user) => user && user.length),
  map(formatUrl),
  switchMap((url) =>
    merge(
      loading$,
      ajax(url).pipe(
        pluck('response'),
        map(Component),
        catchError((error) => of(<Error {...error} />))
      )
    )
  )
);
```

J'adore la concision de cela. En entrant dans `switchMap`, fusionnez les observables `loading$` et `ajax`.

Puisque `loading$` est une valeur statique, il émettra en premier. Une fois l'`ajax` asynchrone terminé, cependant, _il_ émettra et sera affiché à l'écran.

Avant de le tester, nous pouvons importer l'opérateur `delay` pour que la transition ne se fasse pas trop rapidement.

```js
import {
  catchError,
  debounceTime,
  delay,
  filter,
  map,
  pluck,
  switchMap,
  tap
} from 'rxjs/operators';
```

Et l'utiliser juste avant `map(Component)` :

```jsx
ajax(url).pipe(
  pluck('response'),
  delay(1500),
  map(Component),
  catchError((error) => of(<Error {...error} />))
);
```

Notre résultat ?

![](https://cdn-media-1.freecodecamp.org/images/1*9ZPxZaVZt5d5TVKbPKGT9w.gif)

Je me demande jusqu'où pousser ce modèle et dans quelle direction. N'hésitez pas à partager vos pensées !