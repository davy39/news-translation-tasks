---
title: Présentation de React Loads — Un composant React headless pour gérer les états
  des promesses et les données de réponse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T19:24:10.000Z'
originalURL: https://freecodecamp.org/news/introducing-react-loads-a-headless-react-component-to-handle-promise-states-and-response-data-f45cb3621335
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xIBRkg59IQ0ZKkPugO3U6g.gif
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Présentation de React Loads — Un composant React headless pour gérer les
  états des promesses et les données de réponse
seo_desc: 'By Jake Moxey

  Simple, declarative, and lightweight


  Background

  There are so many methods to handle state in React right now. From local state to
  Redux, the new React Context API and new libraries such as Unstated and Copy Write.
  All these methods hav...'
---

Par Jake Moxey

#### Simple, déclaratif et léger

![Image](https://cdn-media-1.freecodecamp.org/images/XuV9yuD-347LsZM-q9Ws71xI4vuLQR0Bp-E7)

### Contexte

Il existe tant de méthodes pour gérer l'état dans React actuellement. Du **state local** à **Redux**, en passant par la nouvelle [**React Context API**](https://reactjs.org/docs/context.html) et les nouvelles bibliothèques telles que [**Unstated**](https://github.com/jamiebuilds/unstated) et [Copy Write](https://github.com/aweary/react-copy-write). Toutes ces méthodes ont d'excellents cas d'utilisation, et il n'y a pas de solution absolue qui me ferait abandonner l'une entièrement au profit d'une autre. Chacune a ses avantages situationnels.

Mais je ne veux pas entrer dans les détails de la gestion d'état dans React. Consultez l'excellent article de Kent C. Dodds sur la [Gestion de l'état de l'application](https://blog.kentcdodds.com/application-state-management-66de608ccb24) pour cela.

Cependant, je souhaite aborder le cas de la gestion des états de chargement et de réponse d'une **promesse**, par exemple les requêtes HTTP et les récupérateurs de ressources. Une promesse a trois états explicites : **en attente**, **résolue** et **rejetée**. Elle a également l'état implicite **inactif**, lorsque la promesse n'a pas encore été déclenchée.

#### Comment l'état des promesses est-il géré dans React ?

Il peut être géré dans l'état local via quelque chose d'aussi simple qu'une variable `isLoading` pour refléter l'état « en attente ». Les variables `response` et `error` sont ensuite utilisées pour refléter les états « résolue » et « rejetée », respectivement.

Il peut être géré dans un store Redux via des actions telles que `GET_DOG_REQUEST`, `GET_DOG_SUCCESS` et `GET_DOG_ERROR`. Celles-ci pourraient alors être mappées aux variables respectives `isLoading`, `response` et `error` dans le store.

#### La gestion de l'état des promesses peut être dangereuse, difficile à lire et poser des problèmes d'UX !

1. Les ternaires imbriqués dans votre fonction `render` peuvent devenir difficiles à interpréter et désordonnés, et peuvent donc être sujets à des erreurs. Voici un exemple d'un tel problème :

Dans cet exemple, il n'est pas clair que `!error && !response` implique l'état « inactif ». Il n'est pas non plus clair que la section `else` de la ternaire `isLoading` implique que la section a été chargée ou a généré une erreur. Et imaginez gérer plus d'une promesse et leurs états respectifs ! Beurk.

2. Voir des flashes de l'état « chargement » dans votre UI est agaçant. Lorsqu'une promesse passe d'un état « inactif » à un état « en attente », ce changement d'état doit être reflété dans l'UI avec un indicateur de chargement. Cependant, il est possible que votre promesse se résolve en un temps minuscule, ce qui fait que votre utilisateur voit un « flash » de l'état de chargement. C'est quelque chose dont de nombreux développeurs ne sont pas conscients lorsqu'ils gèrent les états des promesses.

![Image](https://cdn-media-1.freecodecamp.org/images/yLxb1A-wlpYUtP4kb6DiES2VeVqepaYVwBrV)
_Vous pouvez voir un bref « flash » de l'espace réservé au contenu lorsque ce message Facebook est en cours de chargement._

3. Gérer uniquement les états des promesses dans Redux est inutile. Lorsque Redux a été publié pour la première fois, il était courant pour les développeurs de transférer la majorité de leur état dans un store Redux. Cependant, créer trois actions pour un état de promesse, puis créer trois cas de réducteur pour ces actions, provoque un gonflement inutile dans votre application. Je suis également coupable de cela — mais plus maintenant ! Les actions pour gérer les données de réponse/erreur sont suffisantes à mon avis.

**Évitez de gérer l'état des promesses dans Redux.**

### Présentation de [React Loads](https://github.com/jxom/react-loads)

[React Loads](https://github.com/jxom/react-loads) vise à résoudre les problèmes ci-dessus de manière minimaliste. L'utilisateur fournit au composant `<Loads>` une fonction qui retourne une promesse. Il retournera son état et ses données de réponse sous forme de render props.

[**jxom/react-loads**](https://github.com/jxom/react-loads)
[_react-loads — Un simple composant React pour gérer l'état de chargement_ github.com](https://github.com/jxom/react-loads)

#### Gérer de manière déclarative l'état des promesses et les données de réponse

React Loads vous fournit des `render props` pour charger la promesse. Cela gère également son état et ses données de réponse. Vous pouvez le faire charger la promesse lorsque le composant est monté en passant la prop `loadOnMount` à `<Loads>`.

#### Résultats prévisibles

L'utilisation de variables d'état telles que `isIdle`, `isLoading`, `isTimeout`, `isSuccess` et `isError` à partir des `render props` rendra votre fonction `render` prévisible et facile à lire.

#### Supprime le « flash » de l'état de chargement

React Loads ne passe pas à l'état « chargement » avant 300 ms après le déclenchement de la promesse. Il attendra 300 ms pour que la promesse se **résolve espérons-le** avant de passer à un état en attente. Ce temps peut être modifié en utilisant la prop `delay` pour `<Loads>`.

#### Capacité à mettre en cache les données de réponse

React Loads a la capacité de mettre en cache les données de réponse au niveau du contexte de l'application. Une fois les données chargées à partir d'une invocation de `fn`, il utilisera la réponse retournée par la promesse pour l'invocation suivante de `response`. Les nouvelles données seront alors chargées en arrière-plan, en sautant l'état `isLoading`, et mettront à jour `response` en conséquence. Vous pouvez activer la mise en cache en ajoutant une prop `cacheKey` à `<Loads>`. Lisez plus sur la [mise en cache](https://github.com/jxom/react-loads#caching-response-data) ici.

### Remarques finales

Nous utilisons React Loads en production chez [Medipass](https://medipass.com.au) sur notre application web destinée aux patients et aux praticiens depuis les derniers mois. Cela a rendu notre expérience de développement vraiment facile. Nous avons pu supprimer une tonne de code qui gérait l'état des promesses et les données de réponse, et laisser React Loads faire tout le travail ingrat.

Envisagez de l'utiliser dans l'un de vos projets et faites-moi savoir comment cela se passe ! Si vous avez des suggestions ou repérez un bug, n'hésitez pas à ouvrir une PR (ou un issue) [sur le dépôt](https://github.com/jxom/react-loads) !

Merci pour la lecture !

**Suivez-moi sur [Twitter](https://twitter.com/jxom_) et [GitHub](https://github.com/jxom) (je vous suivrai en retour, je promets).**