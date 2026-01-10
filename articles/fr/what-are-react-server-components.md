---
title: Qu'est-ce que les React Server Components ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-07T02:43:23.000Z'
originalURL: https://freecodecamp.org/news/what-are-react-server-components
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/English-Header-3.png
tags:
- name: React
  slug: react
seo_title: Qu'est-ce que les React Server Components ?
seo_desc: 'By Matías Hernández

  The team behind React thought it''d be a great way to end the year by dangling a
  new feature for the already popular library out in front of developers.

  On December 21st the team revealed a talk that was showing off this new featur...'
---

Par Matías Hernández

L'équipe derrière React a pensé qu'il serait formidable de terminer l'année en présentant une nouvelle fonctionnalité pour la bibliothèque déjà populaire aux développeurs.

Le 21 décembre, l'équipe a révélé une [conférence](https://reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html) qui présentait cette nouvelle fonctionnalité, appelée React Server Components (RSC). Dans cette conférence, [Dan Abramov](https://twitter.com/dan_abramov), [Lauren Tan](https://twitter.com/sugarpirate_), [Joseph Savona](https://twitter.com/en_JS) et [Sebastian Markbåge](https://twitter.com/sebmarkbage) ont expliqué la raison d'être de cette fonctionnalité et certains de ses cas d'utilisation.

Gardez à l'esprit que cette fonctionnalité est une expérience complète qui n'a même pas de documentation publique au-delà de la [RFC](https://github.com/reactjs/rfcs/blob/bf51f8755ddb38d92e23ad415fc4e3c02b95b331/text/0000-server-components.md) que l'équipe a publiée.

> Nous partageons ce travail dans un esprit de transparence et pour obtenir les premiers retours de la communauté React. Il y aura beaucoup de temps pour cela, alors ne vous sentez pas obligé de vous mettre à jour tout de suite !

Alors, de quoi s'agit-il ?

Commençons par clarifier certains des principaux concepts derrière les React Server Components afin que nous puissions comprendre la proposition et quelques techniques similaires disponibles aujourd'hui.

## Qu'est-ce que les React Server Components ?

Les React Server Components (RSC) sont similaires au **server-side rendering (SSR)** mais ils fonctionnent légèrement différemment.

En gros, le SSR prend un composant React et le rend sur le serveur lorsqu'une requête est faite. Cela génère une **chaîne** HTML qui est envoyée au navigateur pour être affichée à l'écran. Ensuite, si nécessaire, il chargera le JavaScript associé via le processus d'hydratation. Enfin, il passe par le cycle standard de l'application : **Client Side Rendering**.

Les React Server Components sont similaires à ce que fait Next.js avec **getInitialProps**. Les **Server Components** peuvent récupérer des données et transmettre ces données aux composants client, mais cette nouvelle technique est plus "dynamique". Elle vous permet de récupérer un arbre complet de composants depuis le serveur et de l'injecter dans l'application client sans perdre l'état du client.

Une autre différence avec le SSR est que, avec cette implémentation, le code JavaScript génère et rend une chaîne de HTML sur le serveur. Cela crée la partie visible du site web, une sorte de modèle HTML. Ce modèle est ensuite envoyé au serveur avec le code JavaScript requis pour l'interactivité.

Cela permet à l'application d'avoir un chargement et un rendu initiaux ultra-rapides. Mais d'un autre côté, elle dispose d'un code interactif qui pourrait prendre un peu plus de temps en raison du processus d'hydratation.

Les composants serveur complètent le SSR, créant une abstraction de terrain intermédiaire qui permet le processus de rendu sans ajouter de taille ou de code au bundle JavaScript.

En d'autres termes, les composants serveur ne sont pas ajoutés en tant que code JavaScript dans le bundle. Cela diminue considérablement - d'environ 19 % à 29 % - la quantité de JavaScript que le navigateur doit analyser et exécuter.

> [RFC] : Si nous migrons l'exemple ci-dessus vers un Server Component, nous pouvons utiliser exactement le même code pour notre fonctionnalité mais éviter de l'envoyer au client - une économie de code de plus de 240 Ko (non compressé).

## Le SSR sera-t-il remplacé par les React Server Components ?

Il existe actuellement certains meta-frameworks qui permettent une très bonne implémentation de la technique SSR. Et le plus connu dans ce domaine est [Next.js](https://nextjs.org). Vous vous demandez peut-être - Next.js sera-t-il remplacé par les server components ?

Non, car les deux impliquent des solutions et des implémentations différentes. L'adoption initiale des RSC sera probablement par un meta framework comme Next ou Gatsby.

* Le composant serveur n'arrive jamais au client. L'implémentation SSR utilisée par React livre le code du composant au client, augmentant ainsi la taille du code dans le navigateur.
* Les composants serveur peuvent accéder aux données backend dans n'importe quelle partie de l'arbre des composants. Les solutions actuelles comme Next.js peuvent accéder à ces données de manière limitée en utilisant la méthode `getServerProps()` (qui a ses propres limitations - elle ne peut être utilisée que dans une page de premier niveau, vous ne pouvez pas récupérer les données du serveur à partir d'autres composants ou d'un package npm tiers, etc.).
* Les Server Components peuvent être réinterrogés tout en conservant l'état du client à l'intérieur de l'arbre. Cela peut être fait parce que le mécanisme de transport n'est pas seulement du HTML, mais plutôt similaire à la définition des nœuds VDOM.

## Vous voulez en savoir plus sur les React Server Components ?

Je recommande de regarder la [conférence originale](https://reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html), de lire la [RFC](https://github.com/reactjs/rfcs/blob/bf51f8755ddb38d92e23ad415fc4e3c02b95b331/text/0000-server-components.md) et de consulter la [démo](https://github.com/reactjs/server-components-demo) de la proposition.

Et n'oubliez pas : **vous n'avez pas besoin d'utiliser ou d'apprendre** cette proposition pour l'instant. Mais il est bon de garder un œil dessus et de voir comment elle évolue et se développe.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/English-Footer-Social-Card.jpg)

🐙 [Suivez-moi sur Twitter](https://twitter.com/matiasfha)            ✉️ [Rejoignez ma newsletter](https://matiashernandez.ck.page)            ❤️ [Soutenez mon travail](https://buymeacoffee.com/matiasfha)