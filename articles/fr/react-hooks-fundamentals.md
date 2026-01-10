---
title: Les fondamentaux des React Hooks pour débutants
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2022-03-15T19:20:16.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-fundamentals
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/freeCodeCamp-Cover.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Les fondamentaux des React Hooks pour débutants
seo_desc: "React.js is an open-source JavaScript-based user interface library. It\
  \ is hugely popular for web and mobile app development. \nReact follows the principle\
  \ of component-based architecture. A component in React is an isolated and reusable\
  \ piece of code...."
---

React.js est une bibliothèque d'interface utilisateur open-source basée sur JavaScript. Elle est extrêmement populaire pour le développement d'applications web et mobiles.

React suit le principe de l'architecture `component-based` (basée sur les composants). Un `composant` dans React est un morceau de code isolé et réutilisable. Les composants peuvent être de deux types : les composants de classe (class components) et les composants fonctionnels (functional components).

Avant la version 16.8 de React, les développeurs ne pouvaient gérer l'état (state) et les autres fonctionnalités de React qu'en utilisant des composants de classe. Mais avec la version 16.8, React a introduit un nouveau modèle appelé `Hooks`.

Avec les React Hooks, nous pouvons utiliser l'état et d'autres fonctionnalités de React dans un composant fonctionnel. Cela permet aux développeurs de faire de la programmation fonctionnelle dans React.

Dans cet article, nous allons apprendre les fondamentaux des `React Hooks`. La motivation derrière la rédaction de cet article est d'encourager les débutants à penser que "les React Hooks sont faciles à apprendre, à créer et à utiliser". Oui, c'est vrai, tant que vous les comprenez fondamentalement.

Si vous aimez aussi apprendre à partir de contenus vidéo, cet article est également disponible sous forme de tutoriel vidéo ici : 🙂

%[https://www.youtube.com/watch?v=CvNvRaS3u60]

## Avant d'apprendre les Hooks...

Avant de penser aux hooks, pensez aux bonnes vieilles `fonctions JavaScript` (alias vanilla).

Dans le langage de programmation JavaScript, les fonctions sont une logique de code réutilisable pour effectuer des tâches répétées. Les fonctions sont composables. Cela signifie que vous pouvez invoquer une fonction dans une autre fonction et utiliser son résultat.

Dans l'image ci-dessous, la fonction `someFunction()` compose (utilise) les fonctions `a()` et `b()`. La fonction `b()` utilise la fonction `c()`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-13.png)
_Composabilité des fonctions_

Si nous écrivons cela en code, cela ressemblera à ceci :

```js
function a() {
    // du code
}

function c() {
    // du code
}

function b() {
    // du code
    
    c();
    
    // du code
}

function someFunction() {
    // du code
    
	a();
    b();
    
    // du code
}
```

Ce n'est pas un secret que les composants fonctionnels dans React ne sont que de simples fonctions JavaScript ! Donc, si les fonctions ont une composabilité, les composants React peuvent également avoir une composabilité. Cela signifie que nous pouvons utiliser (composer) un ou plusieurs composants dans un autre composant, comme le montre l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-14.png)
_Composabilité des composants_

## Composants avec état (Stateful) vs sans état (Stateless)

Les composants dans React peuvent être avec état (stateful) ou sans état (stateless).

* Un composant stateful déclare et gère un état local en son sein.
* Un composant stateless est une fonction pure qui n'a pas d'état local ni d'effets secondaires à gérer.

Une [fonction pure](https://blog.greenroots.info/what-are-pure-functions-and-side-effects-in-javascript) est une fonction sans aucun effet secondaire. Cela signifie qu'une fonction retourne toujours la même sortie pour la même entrée.

Si nous retirons la logique d'état et d'effets secondaires d'un composant fonctionnel, nous obtenons un composant stateless. De plus, la logique d'état et d'effets secondaires peut être réutilisable ailleurs dans l'application. Il est donc logique de les isoler d'un composant autant que possible.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-15.png)
_Composant Stateful car le composant possède une logique d'état_

## React Hooks et logique d'état

Avec les React Hooks, nous pouvons isoler la logique d'état (stateful logic) et les effets secondaires d'un composant fonctionnel. Les Hooks sont des fonctions JavaScript qui gèrent le comportement de l'état et les effets secondaires en les isolant d'un composant.

Ainsi, nous pouvons désormais isoler toute la logique d'état dans des hooks et les utiliser (les composer, car les hooks sont aussi des fonctions) dans les composants.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-16.png)
_Logique d'état isolée dans des Hooks_

La question est : qu'est-ce que cette logique d'état ? Cela peut être tout ce qui nécessite de déclarer et de gérer une variable d'état localement.

Par exemple, la logique pour récupérer des données et gérer ces données dans une variable locale est une logique d'état. Nous pourrions également vouloir réutiliser la logique de récupération (fetching) dans plusieurs composants.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-17.png)

## Alors, que sont exactement les React Hooks ?

Alors, comment pouvons-nous définir les React Hooks en termes simples ? Maintenant que nous comprenons les fonctions, la composabilité, les composants, les états et les effets secondaires, voici une définition des React Hooks :

> Les React Hooks sont de simples fonctions JavaScript que nous pouvons utiliser pour isoler la partie réutilisable d'un composant fonctionnel. Les Hooks peuvent avoir un état et peuvent gérer des effets secondaires.

React fournit un ensemble de hooks standards intégrés :

* `useState` : Pour gérer les états. Retourne une valeur d'état et une fonction de mise à jour pour la modifier.
* `useEffect` : Pour gérer les effets secondaires comme les appels API, les abonnements, les minuteurs, les mutations, et plus encore.
* `useContext` : Pour retourner la valeur actuelle d'un contexte.
* `useReducer` : Une alternative à `useState` pour aider à la gestion d'états complexes.
* `useCallback` : Retourne une version mémoïsée d'un callback pour aider un composant enfant à ne pas se re-rendre inutilement.
* `useMemo` : Retourne une valeur mémoïsée qui aide aux optimisations de performance.
* `useRef` : Retourne un objet ref avec une propriété `.current`. L'objet ref est mutable. Il est principalement utilisé pour accéder à un composant enfant de manière impérative.
* `useLayoutEffect` : Se déclenche à la fin de toutes les mutations du DOM. Il est préférable d'utiliser `useEffect` autant que possible à la place de celui-ci car `useLayoutEffect` se déclenche de manière synchrone.
* `useDebugValue` : Aide à afficher une étiquette dans les React DevTools pour les hooks personnalisés.

Vous pouvez en savoir plus sur ces hooks en détail [ici](https://reactjs.org/docs/hooks-reference.html). Veuillez noter que chaque nom de hook commence par `use`. Oui, c'est une pratique standard pour identifier rapidement un hook dans la base de code React.

Nous pouvons également créer des hooks personnalisés (custom hooks) pour nos cas d'utilisation uniques comme la récupération de données, la journalisation sur disque, les minuteurs, et bien d'autres.

La prochaine fois que vous rencontrerez des React Hooks dans une base de code ou que l'on vous demandera d'en écrire un, restez zen. C'est juste une autre fonction JavaScript pour gérer l'état et les effets secondaires en dehors des composants fonctionnels.

Si vous recherchez un guide étape par étape pour concevoir et créer un hook personnalisé, vous pourriez trouver [cet article utile](https://blog.greenroots.info/how-to-create-a-countdown-timer-using-react-hooks).

## Avant de terminer...

J'espère que vous avez trouvé cette introduction aux React Hooks utile. Après avoir passé de nombreuses années avec React, j'ai lancé une [série de vidéos YouTube](https://www.youtube.com/watch?v=ODKIxaSMgpU&list=PLIJrr73KDmRyrDnDFy-hHvQ24rRjz6e_J) qui vise à couvrir tous les aspects de React de bout en bout. N'hésitez pas à vous [abonner](https://www.youtube.com/tapasadhikary?sub_confirmation=1) si vous trouvez cela utile.

Restons connectés. Je partage mes apprentissages sur JavaScript, le développement Web et le blogging sur ces plateformes également :

* [Suivez-moi sur Twitter](https://twitter.com/tapasadhikary)
* [Projets personnels sur GitHub](https://github.com/atapas)
* [Communauté React.JS sur Showwcase](https://www.showwcase.com/community/react.js)

À bientôt pour mon prochain article. D'ici là, prenez soin de vous et restez heureux.