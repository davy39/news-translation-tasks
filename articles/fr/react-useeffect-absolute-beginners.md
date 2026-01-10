---
title: Le Hook useEffect de React pour les Débutants Absolus
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-03-01T20:41:00.000Z'
originalURL: https://freecodecamp.org/news/react-useeffect-absolute-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/react-useeffect-absolute-beginners.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Le Hook useEffect de React pour les Débutants Absolus
seo_desc: 'If you have trouble understanding the useEffect hook, you''re not alone.

  Beginners and experienced developers alike find it to be one of the trickiest hooks
  to understand, because it requires understanding a few unfamiliar programming concepts.

  In thi...'
---

Si vous avez du mal à comprendre le hook useEffect, vous n'êtes pas seul.

Les débutants et les développeurs expérimentés trouvent qu'il s'agit de l'un des hooks les plus difficiles à comprendre, car il nécessite la compréhension de quelques concepts de programmation inhabituels.

Dans ce guide rapide, nous allons expliquer pourquoi ce hook existe, comment mieux le comprendre et comment l'utiliser correctement dans vos projets React dès aujourd'hui.

## Pourquoi s'appelle-t-il useEffect ?

Lorsque les hooks principaux de React ont été ajoutés à la bibliothèque en 2018 (useState, useEffect, etc.), de nombreux développeurs étaient confus par le nom de ce hook : "useEffect".

Qu'est-ce qu'un "effet" exactement ?

Le mot effet fait référence à un terme de programmation fonctionnelle appelé **"effet de bord"**.

Mais pour vraiment comprendre ce qu'est un effet de bord, nous devons d'abord saisir le concept de **fonction pure**.

Vous ne le savez peut-être pas, mais la plupart des composants React sont censés être des fonctions pures.

Il peut être étrange de penser aux composants React comme à des fonctions, mais ils le sont.

Il est utile de voir qu'un composant de fonction React régulier est déclaré comme une fonction JavaScript :

```js
function MyReactComponent() {}
```

La plupart des composants React sont des fonctions pures, ce qui signifie qu'ils reçoivent une entrée et produisent une sortie prévisible de JSX.

L'entrée d'une fonction JavaScript est des arguments. Quelle est l'entrée d'un composant React, cependant ? **Props !**

Ici, nous avons un composant `User` qui a la prop `name` déclarée sur lui. Dans `User`, la valeur de la prop est affichée dans un élément d'en-tête.

```js
export default function App() {
  return <User name="John Doe" />
}

function User(props) {
  return <h1>{props.name}</h1>; // John Doe
}
```

Ceci est pur car, étant donné la même entrée, il **renverra toujours** la même sortie.

Si nous passons à `User` une prop `name` avec la valeur "John Doe", notre sortie sera toujours John Doe.

Vous pourriez dire, "Qu'est-ce que ça peut faire ? Pourquoi avons-nous même un nom pour ça ?"

Les fonctions pures ont le grand avantage d'être **prévisibles, fiables et faciles à tester**.

C'est en comparaison avec le moment où nous devons effectuer un effet de bord dans notre composant.

## Qu'est-ce que les effets de bord dans React ?

Les effets de bord ne sont pas prévisibles car ce sont des actions qui sont effectuées avec le "monde extérieur".

Nous effectuons un effet de bord lorsque nous devons sortir de nos composants React pour faire quelque chose. Effectuer un effet de bord, cependant, ne nous donnera pas un résultat prévisible.

Imaginez si nous devions demander des données (comme des articles de blog) à un serveur qui a échoué et au lieu de nos données d'article, nous donne une réponse de code d'état 500.

Pratiquement toutes les applications dépendent des effets de bord pour fonctionner d'une manière ou d'une autre, à l'exception des applications les plus simples.

Les effets de bord courants incluent :

* Faire une demande à une API pour des données depuis un serveur backend
* Interagir avec les API du navigateur (c'est-à-dire utiliser `document` ou `window` directement)
* Utiliser des fonctions de timing imprévisibles comme `setTimeout` ou `setInterval`

C'est pourquoi useEffect existe : pour fournir un moyen de gérer l'exécution de ces effets de bord dans ce qui sont autrement des composants React purs.

Par exemple, si nous voulions changer la balise meta title pour afficher le nom de l'utilisateur dans son onglet de navigateur, nous _pourrions_ le faire dans le composant lui-même, mais nous ne devrions pas.

```js
function User({ name }) {
  document.title = name;
  // Ceci est un effet de bord. Ne faites pas cela dans le corps du composant !

  return <h1>{name}</h1>;
}
```

Si nous effectuons un effet de bord directement dans le corps de notre composant, cela entrave le rendu de notre composant React.

Les effets de bord doivent être séparés du processus de rendu. Si nous devons effectuer un effet de bord, cela doit strictement être fait _après_ que notre composant se rende.

C'est ce que useEffect nous donne.

En bref, **useEffect est un outil qui nous permet d'interagir avec le monde extérieur sans affecter le rendu ou la performance du composant dans lequel il se trouve.**

## Comment utiliser useEffect ?

La syntaxe de base de useEffect est la suivante :

```js
// 1. importer useEffect
import { useEffect } from 'react';

function MyComponent() {
  // 2. l'appeler au-dessus du JSX retourné
  // 3. lui passer deux arguments : une fonction et un tableau
  useEffect(() => {}, []);

  // return ...
}
```

La bonne façon d'effectuer l'effet de bord dans notre composant `User` est la suivante :

1. Nous importons `useEffect` depuis "react"
2. Nous l'appelons au-dessus du JSX retourné dans notre composant
3. Nous lui passons deux arguments : une fonction et un tableau

```js
import { useEffect } from 'react';

function User({ name }) {
  useEffect(() => {
    document.title = name;
  }, [name]);

  return <h1>{name}</h1>;
}
```

La fonction passée à useEffect est une fonction de rappel. Celle-ci sera appelée après le rendu du composant.

Dans cette fonction, nous pouvons effectuer nos effets de bord ou plusieurs effets de bord si nous le souhaitons.

Le deuxième argument est un tableau, appelé le tableau des dépendances. Ce tableau doit inclure toutes les valeurs dont notre effet de bord dépend.

Dans notre exemple ci-dessus, puisque nous changeons le titre en fonction d'une valeur dans la portée externe, `name`, nous devons inclure celle-ci dans le tableau des dépendances.

Ce que ce tableau fera, c'est vérifier si une valeur (dans ce cas, name) a changé entre les rendus. Si c'est le cas, il exécutera notre fonction d'effet à nouveau.

Cela a du sens car si le nom change, nous voulons afficher ce nom changé et donc exécuter notre effet de bord à nouveau.

## Comment corriger les erreurs courantes avec useEffect

Il y a quelques détails subtils à connaître pour éviter les erreurs avec useEffect.

Si vous ne fournissez pas du tout le tableau des dépendances et que vous ne fournissez qu'une fonction à useEffect, **il s'exécutera après chaque rendu**.

Cela peut entraîner des problèmes lorsque vous essayez de mettre à jour l'état dans votre hook useEffect.

Si vous oubliez de fournir vos dépendances correctement et que vous définissez une partie de l'état local lorsque l'état est mis à jour, le comportement par défaut de React est de re-rendre le composant. Et donc, puisque useEffect s'exécute après chaque rendu sans le tableau des dépendances, nous aurons une boucle infinie.

```js
function MyComponent() {
  const [data, setData] = useState([])

  useEffect(() => {
    fetchData().then(myData => setData(myData))
    // Erreur ! useEffect s'exécute après chaque rendu sans le tableau des dépendances, causant une boucle infinie
  });
}
```

Après le premier rendu, useEffect sera exécuté, l'état sera mis à jour, ce qui provoquera un re-rendu, ce qui provoquera l'exécution de useEffect à nouveau, commençant le processus à nouveau ad infinitum.

Cela s'appelle une **boucle infinie** et cela brise effectivement notre application.

Si vous mettez à jour l'état dans votre useEffect, assurez-vous de fournir un tableau de dépendances vide. Si vous fournissez un tableau vide, ce que je recommande de faire par défaut chaque fois que vous utilisez useEffect, cela fera que la fonction d'effet ne s'exécutera qu'une seule fois après que le composant a rendu la première fois.

Un exemple courant pour cela est de récupérer des données. Pour un composant, vous pouvez simplement vouloir récupérer des données une fois, les mettre dans l'état, puis les afficher dans votre JSX.

```js
function MyComponent() {
  const [data, setData] = useState([])

  useEffect(() => {
    fetchData().then(myData => setData(myData))
    // Correct ! S'exécute une fois après le rendu avec un tableau vide
  }, []);

  return <ul>{data.map(item => <li key={item}>{item}</li>)}</ul>
}
```

## Qu'est-ce que la fonction de nettoyage dans useEffect ?

La dernière partie de l'exécution correcte des effets de bord dans React est la **fonction de nettoyage de l'effet**.

Parfois, nos effets de bord doivent être arrêtés. Par exemple, si vous avez un compte à rebours utilisant la fonction `setInterval`, cet intervalle ne s'arrêtera pas sauf si nous utilisons la fonction `clearInterval`.

Un autre exemple est l'utilisation de subscriptions avec WebSockets. Les subscriptions doivent être "désactivées" lorsque nous ne les utilisons plus, et c'est à cela que sert la fonction de nettoyage.

Si nous définissons un état en utilisant `setInterval` et que cet effet de bord n'est pas nettoyé, lorsque notre composant est démonté et que nous ne l'utilisons plus, l'état est détruit avec le composant – mais la fonction `setInterval` continuera à s'exécuter.

```js
function Timer() {
  const [time, setTime] = useState(0);

  useEffect(() => {
    setInterval(() => setTime(1), 1000);
    // compte jusqu'à 1 chaque seconde
    // nous devons arrêter d'utiliser setInterval lorsque le composant est démonté
  }, []);
}
```

Le problème avec cela si le composant est détruit, c'est que `setInterval` essaiera de mettre à jour une variable, un morceau d'état `time` qui n'existe plus. Cela est une erreur appelée une fuite de mémoire.

Pour utiliser la fonction de nettoyage, nous devons retourner une fonction depuis la fonction useEffect.

Dans cette fonction, nous pouvons effectuer notre nettoyage, dans ce cas, utiliser `clearInterval` et arrêter `setInterval`.

```js
function Timer() {
  const [time, setTime] = useState(0);

  useEffect(() => {
    let interval = setInterval(() => setTime(1), 1000);

    return () => {
      // setInterval est nettoyé lorsque le composant est démonté
      clearInterval(interval);
    }
  }, []);
}
```

La fonction de nettoyage sera appelée lorsque le composant sera démonté.

Un exemple courant de démontage d'un composant est d'aller à une nouvelle page ou à une nouvelle route dans notre application où le composant n'est plus rendu.

Lorsque le composant est démonté, notre fonction de nettoyage s'exécute, notre intervalle est nettoyé, et nous n'avons plus d'erreur de tentative de mise à jour d'une variable d'état qui n'existe pas.

Enfin, le nettoyage de l'effet de bord n'est pas requis dans tous les cas. Il n'est requis que dans quelques cas, comme lorsque vous devez arrêter un effet de bord répété lorsque votre composant est démonté.

## Devenez un Développeur React Professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*