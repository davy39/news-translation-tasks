---
title: Pourquoi j'ai créé le boilerplate universel async React Redux le plus simple
  possible
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-23T23:46:38.000Z'
originalURL: https://freecodecamp.org/news/why-i-built-the-simplest-async-universal-react-redux-boilerplate-i-could-1b5ef6206d3d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VeM-5lsAtrrJ4jXH96h5kg.png
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Pourquoi j'ai créé le boilerplate universel async React Redux le plus simple
  possible
seo_desc: 'By William Woodhead

  I set myself a task last week.

  I was checking out some “Get Started” Universal React Redux Boilerplates and found
  that a lot of them are really complex. They include heaps of dependencies, and have
  functionality that can take week...'
---

Par William Woodhead

Je me suis fixé une tâche la semaine dernière.

J'examinais certains boilerplates universels "Get Started" pour [React](https://reactjs.org/) [Redux](https://redux.js.org/) et j'ai constaté que beaucoup d'entre eux sont vraiment complexes. Ils incluent des tonnes de dépendances et ont des fonctionnalités qui peuvent prendre des semaines à démêler.

**En général, les boilerplates servent deux fonctions pour moi :**

1. Commencer plus rapidement, puisque l'application est déjà échafaudée
2. Apprendre comment échafauder une application

Je suis beaucoup plus intéressé par le deuxième point. En tant que développeur, j'aime comprendre comment les choses s'emboîtent, comment les choses fonctionnent **sous le capot**.

Par conséquent, je me suis fixé la tâche suivante :

> Créer le boilerplate universel async React Redux le plus simple possible.

Ça a l'air génial, mais que signifie tout cela ?

**Vous voulez juste voir le code ?** Consultez ce [dépôt GitHub](https://github.com/william-woodhead/simple-universal-react-redux).

### Qu'est-ce qu'un boilerplate universel async React Redux ?

Démêlons chaque mot, un par un.

#### Universel

Essentiellement, Universel décrit une application qui est à la fois rendue côté serveur et qui a un routage dynamique côté client.

**Pourquoi est-ce important ?** Le rendu côté serveur est important pour le SEO et pour les liens riches et les métadonnées — comme lorsque vous postez un lien web dans Twitter ou Slack.

Le routage côté client offre à vos utilisateurs une expérience fluide sur votre site web, car le navigateur n'a pas besoin de se recharger lorsque l'utilisateur navigue entre les pages.

#### Async

Async signifie que nous voulons récupérer des données à partir d'API externes avant de rendre la page. Nous voulons rendre la page côté serveur avec des données qui sont à une requête asynchrone.

**Pourquoi est-ce important ?** Cela est vraiment important pour les applications où les données ou le contenu sont stockés séparément du code du site web. Supposons que nous avons des données dans une base de données, ou que nous demandons des données à l'API Twitter. Nous voulons obtenir ces données avant de rendre la page.

#### React

React est la bibliothèque de rendu fonctionnel qui a été développée par l'équipe de Facebook pour fonctionner à la fois côté serveur et côté client. React nous donne la fonctionnalité dont nous avons besoin pour rendre une page côté serveur, mais toujours initialiser l'application côté client.

#### Redux

Redux est un package de gestion d'état qui a été développé pour être facile à utiliser à la fois côté serveur et côté client. Redux nous donne la fonctionnalité dont nous avons besoin pour passer l'état entre le serveur et le client.

#### Boilerplate

Définis par le [Cambridge Dictionary](https://dictionary.cambridge.org/dictionary/english/boilerplate) comme :

> Texte qui peut être copié et utilisé ... dans des programmes informatiques, avec seulement de très petites modifications.

### Pourquoi avez-vous besoin d'applications universelles ?

Beaucoup de sites web ne rendent que côté client. Google Search peut maintenant indexer les pages qui rendent côté client, alors pourquoi devons-nous passer par la douleur de créer des applications universelles ?

#### Liens riches et métadonnées

La principale raison est pour les liens riches et les métadonnées. Lorsque vous postez une page dans Twitter ou LinkedIn, ils scrapent le HTML brut de la page retournée par le serveur pour trouver des métadonnées.

Si votre application est rendue côté client, ces métadonnées ne seront pas disponibles pour les scrapers, car aucun JavaScript n'est exécuté.

Cela peut être un énorme problème. Imaginez la différence entre votre lien web rendu sous forme de texte et votre lien web rendu avec des images riches et des métadonnées. Voici un exemple :

**Post Slack de [Pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=boilerplate&utm_campaign=awareness) sans métadonnées**

![Image](https://cdn-media-1.freecodecamp.org/images/KNIboYOszuVHPmRe-6S6WJ030391L31ffecy)

**Post Slack de [Pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=boilerplate&utm_campaign=awareness) avec métadonnées — repérez la différence**

![Image](https://cdn-media-1.freecodecamp.org/images/cNfmlcRQDHXFiE-i4AkJEOrXTj0i8HPwwT-B)

**Note :** Consultez [howdoesitlookonsocial.com](http://howdoesitlookonsocial.com) pour voir comment vos métadonnées sont rendues sur les sites sociaux.

### Le boilerplate le plus simple que j'ai pu créer

Créer des applications universelles est vraiment complexe. Il n'y a pas encore de méthode standardisée pour l'aborder. Beaucoup des boilerplates existants sont hideusement complexes.

C'est pourquoi j'ai essayé de créer le boilerplate le plus simple possible qui fonctionne à la fois sur Mac et Windows.

Il n'y a rien de superflu dans le code source. La page web ne pourrait pas être plus simple. Elle ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/BsPNbL90GiJ4iuQFnZRLUPPsn2YFa9adSYmC)

Je veux que les développeurs puissent démêler toutes les différentes fonctions et packages utilisés, bidouiller avec, tester différentes parties, et finalement construire de grandes applications universelles sur le dessus.

Alors voici le [lien du dépôt GitHub](https://github.com/William-Woodhead/simple-universal-react-redux).

Consultez-le — clonez-le, installez-le, exécutez-le. Voyez ce que vous en pensez. J'adorerais avoir des retours. Et si vous l'aimez, assurez-vous de le marquer avec une étoile et de le partager !

*Si vous avez aimé cette histoire, veuillez ? et veuillez partager avec les autres. Veuillez également consulter mon entreprise [pilcro.com](https://www.pilcro.com/?utm_source=medium&utm_medium=boilerplate&utm_campaign=awareness). Pilcro est l'application de gestion de marque pour G-Suite.*

![Image](https://cdn-media-1.freecodecamp.org/images/CsWVmNZ2bnvwrdu3apMKDKvdhxOCY1awxFvU)