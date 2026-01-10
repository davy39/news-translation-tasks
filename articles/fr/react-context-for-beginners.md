---
title: React Context pour débutants – Le guide complet (2021)
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-07-21T15:39:28.000Z'
originalURL: https://freecodecamp.org/news/react-context-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/react-context-for-beginners.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React context
  slug: react-context
- name: Web Development
  slug: web-development
seo_title: React Context pour débutants – Le guide complet (2021)
seo_desc: 'React context is an essential tool for every React developer to know. It
  lets you easily share state in your applications.

  In this comprehensive guide, we will cover what React context is, how to use it,
  when and when not to use context, and lots mor...'
---

React context est un outil essentiel que tout développeur React doit connaître. Il permet de partager facilement l'état dans vos applications.

Dans ce guide complet, nous allons couvrir ce qu'est React context, comment l'utiliser, quand et quand ne pas l'utiliser, et bien plus encore.

Même si vous n'avez jamais travaillé avec React context auparavant, vous êtes au bon endroit. Vous apprendrez tout ce que vous devez savoir avec des exemples simples et étape par étape.

Commençons !

## Table des matières

* [Qu'est-ce que React context ?](#heading-qu-est-ce-que-react-context)
* [Quand devez-vous utiliser React context ?](#heading-quand-devez-vous-utiliser-react-context)
* [Quels problèmes React context résout-il ?](#heading-quels-problemes-react-context-resout-il)
* [Comment utiliser React context ?](#heading-comment-utiliser-react-context)
* [Qu'est-ce que le hook useContext ?](#heading-quest-ce-que-le-hook-usecontext)
* [Vous n'avez peut-être pas besoin de context](#heading-vous-n-avez-peut-etre-pas-besoin-de-context)
* [React context remplace-t-il Redux ?](#heading-react-context-remplace-t-il-redux)
* [Précautions avec React context](#heading-precautions-avec-react-context)

## Qu'est-ce que React context ?

React context nous permet de transmettre et d'utiliser (consommer) des données dans n'importe quel composant dont nous avons besoin dans notre application React sans utiliser de props.

_En d'autres termes, React context nous permet de partager des données (état) entre nos composants plus facilement._

## Quand devez-vous utiliser React context ?

React context est idéal lorsque vous transmettez des données qui peuvent être utilisées dans n'importe quel composant de votre application.

**Ces types de données incluent :**

* Les données de thème (comme le mode sombre ou clair)
* Les données utilisateur (l'utilisateur actuellement authentifié)
* Les données spécifiques à la localisation (comme la langue ou la locale de l'utilisateur)

Les données doivent être placées sur React context qui n'ont pas besoin d'être mises à jour souvent.

Pourquoi ? Parce que le context n'a pas été conçu comme un système complet de gestion d'état. Il a été conçu pour faciliter la consommation de données.

_Vous pouvez penser à React context comme l'équivalent des variables globales pour nos composants React._

## Quels problèmes React context résout-il ?

React context nous aide à éviter le problème de "props drilling".

**Props drilling** est un terme pour décrire lorsque vous transmettez des props à plusieurs niveaux vers un composant imbriqué, à travers des composants qui n'en ont pas besoin.

Voici un exemple de props drilling. Dans cette application, nous avons accès aux données de thème que nous voulons transmettre en tant que prop à tous les composants de notre application.

Comme vous pouvez le voir, cependant, les enfants directs de `App`, tels que `Header`, doivent également transmettre les données de thème en utilisant des props.

```js
export default function App({ theme }) {
  return (
    <>
      <Header theme={theme} />
      <Main theme={theme} />
      <Sidebar theme={theme} />
      <Footer theme={theme} />
    </>
  );
}

function Header({ theme }) {
  return (
    <>
      <User theme={theme} />
      <Login theme={theme} />
      <Menu theme={theme} />
    </>
  );
}
```

_Quel est le problème avec cet exemple ?_

Le problème est que nous transmettons la prop `theme` à travers plusieurs composants qui n'en ont pas immédiatement besoin.

Le composant `Header` n'a pas besoin de `theme` autre que pour le transmettre à son composant enfant. En d'autres termes, il serait préférable que `User`, `Login` et `Menu` consomment directement les données `theme`.

C'est l'avantage de React context – nous pouvons contourner l'utilisation des props entièrement et ainsi éviter le problème de props drilling.

## Comment utiliser React context ?

Context est une API intégrée à React, à partir de la version 16 de React.

Cela signifie que nous pouvons créer et utiliser le context directement en important React dans n'importe quel projet React.

**Il y a quatre étapes pour utiliser React context :**

1. Créer le context en utilisant la méthode `createContext`.
2. Prenez votre context créé et enveloppez le fournisseur de context autour de votre arbre de composants.
3. Placez n'importe quelle valeur que vous aimez sur votre fournisseur de context en utilisant la prop `value`.
4. Lisez cette valeur dans n'importe quel composant en utilisant le consommateur de context.

_Tout cela semble-t-il confus ?_ C'est plus simple que vous ne le pensez.

Regardons un exemple très basique. Dans notre `App`, transmettons notre propre nom en utilisant Context et lisons-le dans un composant imbriqué : `User`.

```js
import React from 'react';

export const UserContext = React.createContext();

export default function App() {
  return (
    <UserContext.Provider value="Reed">
      <User />
    </UserContext.Provider>
  )
}

function User() {
  return (
    <UserContext.Consumer>
      {value => <h1>{value}</h1>} 
      {/* affiche : Reed */}
    </UserContext.Consumer>
  )
}
```

Décomposons ce que nous faisons, étape par étape :

1. Au-dessus de notre composant `App`, nous créons un context avec `React.createContext()` et mettons le résultat dans une variable, `UserContext`. Dans presque tous les cas, vous voudrez l'exporter comme nous le faisons ici car votre composant sera dans un autre fichier. Notez que nous pouvons passer une valeur initiale à notre prop `value` lorsque nous appelons `React.createContext()`.
2. Dans notre composant `App`, nous utilisons `UserContext`. Plus précisément `UserContext.Provider`. Le context créé est un objet avec deux propriétés : `Provider` et `Consumer`, toutes deux étant des composants. Pour transmettre notre valeur à tous les composants de notre App, nous enveloppons notre composant Provider autour (dans ce cas, `User`).
3. Sur `UserContext.Provider`, nous plaçons la valeur que nous voulons transmettre à tout notre arbre de composants. Nous la définissons égale à la prop `value` pour ce faire. Dans ce cas, il s'agit de notre nom (ici, Reed).
4. Dans `User`, ou partout où nous voulons consommer (ou utiliser) ce qui a été fourni sur notre context, nous utilisons le composant consommateur : `UserContext.Consumer`. Pour utiliser notre valeur transmise, nous utilisons ce qu'on appelle le **modèle de props de rendu**. Il s'agit simplement d'une fonction que le composant consommateur nous donne en tant que prop. Et dans le retour de cette fonction, nous pouvons retourner et utiliser `value`.

## Qu'est-ce que le hook useContext ?

En regardant l'exemple ci-dessus, le modèle de props de rendu pour consommer le context peut vous sembler un peu étrange.

Une autre façon de consommer le context est devenue disponible dans React 16.8 avec l'arrivée des hooks React. Nous pouvons maintenant consommer le context avec le **hook useContext**.

Au lieu d'utiliser les props de rendu, nous pouvons passer l'objet context entier à `React.useContext()` pour consommer le context en haut de notre composant.

Voici l'exemple ci-dessus utilisant le hook useContext :

```js
import React from 'react';

export const UserContext = React.createContext();

export default function App() {
  return (
    <UserContext.Provider value="Reed">
      <User />
    </UserContext.Provider>
  )
}

function User() {
  const value = React.useContext(UserContext);  
    
  return <h1>{value}</h1>;
}
```

_L'avantage du hook useContext est qu'il rend nos composants plus concis et nous permet de créer nos propres hooks personnalisés._

Vous pouvez soit utiliser le composant consommateur directement, soit le hook useContext, selon le modèle que vous préférez.

## Vous n'avez peut-être pas besoin de context

L'erreur que font de nombreux développeurs est de se tourner vers le context dès qu'ils doivent transmettre des props à plusieurs niveaux vers un composant.

Voici une application avec un composant `Avatar` imbriqué qui nécessite deux props `username` et `avatarSrc` du composant `App`.

```js
export default function App({ user }) {
  const { username, avatarSrc } = user;

  return (
    <main>
      <Navbar username={username} avatarSrc={avatarSrc} />
    </main>
  );
}

function Navbar({ username, avatarSrc }) {
  return (
    <nav>
      <Avatar username={username} avatarSrc={avatarSrc} />
    </nav>
  );
}

function Avatar({ username, avatarSrc }) {
  return <img src={avatarSrc} alt={username} />;
}

```

Si possible, nous voulons éviter de transmettre plusieurs props à travers des composants qui n'en ont pas besoin.

_Que pouvons-nous faire ?_

Au lieu de recourir immédiatement au context parce que nous faisons du props drilling, nous devrions mieux composer nos composants.

Puisque seul le composant le plus haut, `App`, doit connaître le composant `Avatar`, nous pouvons le créer directement dans `App`.

Cela nous permet de transmettre une seule prop, `avatar`, au lieu de deux.

```js
export default function App({ user }) {
  const { username, avatarSrc } = user;

  const avatar = <img src={avatarSrc} alt={username} />;

  return (
    <main>
      <Navbar avatar={avatar} />
    </main>
  );
}

function Navbar({ avatar }) {
  return <nav>{avatar}</nav>;
}
```

_En bref : ne vous tournez pas vers le context tout de suite. Voyez si vous pouvez mieux organiser vos composants pour éviter le props drilling._

## React context remplace-t-il Redux ?

Oui et non.

Pour de nombreux débutants en React, Redux est un moyen de transmettre plus facilement des données. Cela est dû au fait que Redux vient avec React context lui-même.

Cependant, si vous ne mettez pas également à jour l'état, mais que vous le transmettez simplement dans votre arbre de composants, vous n'avez pas besoin d'une bibliothèque de gestion d'état globale comme Redux.

## Précautions avec React context

_Pourquoi n'est-il pas possible de mettre à jour la valeur que React context transmet ?_

Bien qu'il soit possible de combiner React context avec un hook comme useReducer et de créer une bibliothèque de gestion d'état de fortune sans aucune bibliothèque tierce, cela n'est généralement pas recommandé pour des raisons de performance.

Le problème avec cette approche réside dans la manière dont React context déclenche un re-rendu.

Si vous transmettez un objet sur votre fournisseur de context React et qu'une propriété de celui-ci est mise à jour, que se passe-t-il ? _Tout composant qui consomme ce context sera re-rendu._

Cela peut ne pas être un problème de performance dans les petites applications avec peu de valeurs d'état qui ne sont pas mises à jour très souvent (comme les données de thème). Mais c'est un problème si vous allez effectuer de nombreuses mises à jour d'état dans une application avec beaucoup de composants dans votre arbre de composants.

## Conclusion

J'espère que ce guide vous a donné une meilleure compréhension de la façon d'utiliser React context de bout en bout.

Si vous voulez une compréhension encore plus approfondie de la façon d'utiliser React context pour construire des projets React incroyables, consultez [The React Bootcamp](https://www.thereactbootcamp.com).

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*