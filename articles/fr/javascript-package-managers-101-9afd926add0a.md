---
title: Une introduction au fonctionnement des gestionnaires de paquets JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-24T20:40:28.000Z'
originalURL: https://freecodecamp.org/news/javascript-package-managers-101-9afd926add0a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t_kMxpLVVL3_hgcDM6cgeQ.gif
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Une introduction au fonctionnement des gestionnaires de paquets JavaScript
seo_desc: 'By Shubheksha Jalan

  Ashley Williams is one of the leaders of the Node.js community. She tweeted about
  a new package managers.

  I didn’t really understand what she meant, so I decided to dig in deeper and read
  about how package managers work.

  This was ...'
---

Par Shubheksha Jalan

Ashley Williams est l'une des leaders de la communauté Node.js. Elle a tweeté à propos de nouveaux gestionnaires de paquets.

Je n'ai pas vraiment compris ce qu'elle voulait dire, alors j'ai décidé d'approfondir et de lire sur le fonctionnement des gestionnaires de paquets.

C'était juste au moment où le nouveau venu sur le bloc des gestionnaires de paquets JavaScript — [Yarn](https://yarnpkg.com/) — venait d'arriver et générait beaucoup de buzz.

J'ai donc utilisé cette opportunité pour comprendre également [comment et pourquoi Yarn fait les choses différemment de npm](https://code.facebook.com/posts/1840075619545360/yarn-a-new-package-manager-for-javascript/).

J'ai eu tellement de plaisir à rechercher cela. J'aurais aimé l'avoir fait il y a longtemps. J'ai donc écrit cette simple introduction à npm et Yarn pour partager ce que j'ai appris.

Commençons par quelques définitions :

#### Qu'est-ce qu'un paquet ?

Un paquet est un morceau de logiciel réutilisable qui peut être téléchargé depuis un registre global vers l'environnement local d'un développeur. Chaque paquet peut ou non dépendre d'autres paquets.

#### **Qu'est-ce qu'un gestionnaire de paquets ?**

Simplement dit — un gestionnaire de paquets est un morceau de logiciel qui vous permet de gérer les **dépendances** (code externe écrit par vous ou quelqu'un d'autre) dont votre projet a besoin pour fonctionner correctement.

La plupart des gestionnaires de paquets jonglent avec les éléments suivants de votre projet :

#### **Code du projet**

Il s'agit du code de votre projet pour lequel vous devez gérer diverses dépendances. Typiquement, tout ce code est vérifié dans un système de contrôle de version comme Git.

#### **Fichier manifest**

Il s'agit d'un fichier qui garde une trace de toutes vos dépendances (les paquets à gérer). Il contient également d'autres métadonnées sur votre projet. Dans le monde JavaScript, ce fichier est votre `[package.json](https://docs.npmjs.com/files/package.json)`

#### **Code de dépendance**

Ce code constitue vos dépendances. Il ne doit pas être muté pendant la durée de vie de votre application, et doit être accessible par votre code de projet en mémoire lorsqu'il est nécessaire.

#### **Fichier de verrouillage**

Ce fichier est écrit automatiquement par le gestionnaire de paquets lui-même. Il contient toutes les informations nécessaires pour reproduire l'arborescence complète des sources de dépendances. Il contient des informations sur chacune des dépendances de votre projet, ainsi que leurs versions respectives.

Il est important de souligner à ce stade que Yarn utilise un fichier de verrouillage, tandis que npm ne le fait pas. Nous parlerons des conséquences de cette distinction dans un instant.

Maintenant que je vous ai présenté les parties d'un gestionnaire de paquets, discutons des dépendances elles-mêmes.

### Dépendances plates versus imbriquées

Pour comprendre la différence entre les schémas de dépendances plates et imbriquées, essayons de visualiser un graphe de dépendances des dépendances dans votre projet.

Il est important de garder à l'esprit que les dépendances dont votre projet dépend peuvent avoir leurs propres dépendances. Et ces dépendances peuvent à leur tour avoir certaines dépendances en commun.

Pour clarifier, disons que notre application dépend des dépendances A, B et C, et que C dépend de A.

#### **Dépendances plates**

![Image](https://cdn-media-1.freecodecamp.org/images/1*QFSdXpqBdeuJIJDzr0KfZg.png)
_[Graphe de dépendances en cas de dépendances plates](http://maxogden.com/nested-dependencies.html" rel="noopener" target="_blank" title=")_

Comme le montre l'image, à la fois l'application et C ont A comme dépendance. Pour la résolution des dépendances dans un schéma de dépendances plates, il n'y a qu'une seule couche de dépendances que votre gestionnaire de paquets doit parcourir.

En bref — vous ne pouvez avoir qu'une seule version d'un paquet particulier dans votre arborescence de sources, car il y a un espace de noms commun pour toutes vos dépendances.

Supposons que le paquet A soit mis à niveau vers la version 2.0. Si votre application est compatible avec la version 2.0, mais que le paquet C ne l'est pas, alors nous avons besoin de deux versions du paquet A afin de faire fonctionner correctement notre application. Cela est connu sous le nom de **Dependency Hell**.

#### **Dépendances imbriquées**

![Image](https://cdn-media-1.freecodecamp.org/images/1*GWq1l9Mxe0k7teuJCIOlYw.png)
_[Graphe de dépendances en cas de dépendances imbriquées](http://maxogden.com/nested-dependencies.html" rel="noopener" target="_blank" title=")_

Une solution simple pour traiter le problème de Dependency Hell est d'avoir deux versions différentes du paquet A — version 1.0 et version 2.0.

C'est là que les dépendances imbriquées entrent en jeu. Dans le cas de dépendances imbriquées, chaque dépendance peut isoler ses propres dépendances des autres dépendances, dans un espace de noms différent.

Le gestionnaire de paquets doit parcourir plusieurs niveaux pour la résolution des dépendances.

Nous pouvons avoir plusieurs copies d'une seule dépendance dans un tel schéma.

Mais comme vous l'avez peut-être deviné, cela conduit également à quelques problèmes. Que se passe-t-il si nous ajoutons un autre paquet — paquet D — et qu'il dépend également de la version 1.0 du paquet A ?

Ainsi, avec ce schéma, nous pouvons finir avec une **duplication** de la version 1.0 du paquet A. Cela peut causer de la confusion et prend un espace disque inutile.

Une solution au problème ci-dessus est d'avoir deux versions du paquet A, v1.0 et v2.0, mais une seule copie de v1.0 afin d'éviter une duplication inutile. C'est l'[approche adoptée par npm v3](https://docs.npmjs.com/how-npm-works/npm3-dupe), qui réduit considérablement le temps nécessaire pour parcourir l'arborescence des dépendances.

Comme l'explique [ashley williams](https://www.freecodecamp.org/news/javascript-package-managers-101-9afd926add0a/undefined), [npm v2 installe les dépendances de manière imbriquée](https://docs.npmjs.com/how-npm-works/npm2). C'est pourquoi npm v3 est considérablement plus rapide en comparaison.

### **Déterminisme vs Non-déterminisme**

Un autre concept important dans les gestionnaires de paquets est celui du déterminisme. Dans le contexte de l'écosystème JavaScript, le déterminisme signifie que tous les ordinateurs avec un fichier `package.json` donné auront tous la même arborescence exacte de sources de dépendances installées dans leur dossier `node_modules`.

Mais avec un gestionnaire de paquets non déterministe, cela n'est pas garanti. Même si vous avez le même `package.json` sur deux ordinateurs différents, la disposition de votre `node_modules` peut différer entre eux.

Le déterminisme est souhaitable. Il vous aide à éviter les problèmes de **"fonctionnait sur ma machine mais s'est cassé lorsque nous l'avons déployé"**, qui surviennent lorsque vous avez des `node_modules` différents sur différents ordinateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*i4QK4sSGX7Q4RRgOytkSuw.jpeg)
_Ce meme populaire de développeur illustre les problèmes de non-déterminisme._

[npm v3, par défaut, a des installations non déterministes](https://docs.npmjs.com/how-npm-works/npm3-nondet) et offre une [fonctionnalité de shrinkwrap](https://docs.npmjs.com/cli/shrinkwrap) pour rendre les installations déterministes. Cela écrit tous les paquets sur le disque dans un fichier de verrouillage, avec leurs versions respectives.

Yarn offre des installations déterministes car il utilise un fichier de verrouillage pour verrouiller toutes les dépendances de manière récursive au niveau de l'application. Ainsi, si le paquet A dépend de la v1.0 du paquet C, et que le paquet B dépend de la v2.0 du paquet A, les deux seront écrits séparément dans le fichier de verrouillage.

Lorsque vous connaissez les versions exactes des dépendances avec lesquelles vous travaillez, vous pouvez facilement reproduire les builds, puis suivre et isoler les bugs.

> "Pour le rendre plus clair, votre `package.json` indique **"ce que je veux"** pour le projet tandis que votre fichier de verrouillage indique **"ce que j'avais"** en termes de dépendances. — [Dan Abramov](https://www.freecodecamp.org/news/javascript-package-managers-101-9afd926add0a/undefined)

Nous pouvons donc revenir à la question originale qui m'a lancé dans cette frénésie d'apprentissage en premier lieu : **Pourquoi est-il considéré comme une bonne pratique d'avoir des fichiers de verrouillage pour les applications, mais pas pour les bibliothèques ?**

La raison principale est que vous déployez réellement des applications. Vous avez donc besoin de dépendances déterministes qui conduisent à des builds reproductibles dans différents environnements — test, staging et production.

Mais ce n'est pas vrai pour les bibliothèques. Les bibliothèques ne sont pas déployées. Elles sont utilisées pour construire d'autres bibliothèques, ou dans des applications elles-mêmes. Les bibliothèques doivent être flexibles afin de maximiser la compatibilité.

Si nous avions un fichier de verrouillage pour chaque dépendance (bibliothèque) que nous utilisons dans une application, et que l'application était forcée de respecter ces fichiers de verrouillage, il serait impossible de se rapprocher d'une structure de dépendances plates dont nous avons parlé précédemment, avec la flexibilité de la [version sémantique](http://semver.org/), qui est le meilleur scénario pour la résolution des dépendances.

Voici pourquoi : si votre application doit respecter récursivement les fichiers de verrouillage de toutes vos dépendances, il y aurait des conflits de versions partout — même dans des projets relativement petits. Cela causerait une grande quantité de duplication inévitable due à la [version sémantique](https://docs.npmjs.com/getting-started/semantic-versioning).

Cela ne signifie pas que les bibliothèques ne peuvent pas avoir de fichiers de verrouillage. Elles le peuvent certainement. Mais le principal enseignement est que les gestionnaires de paquets comme Yarn et npm — qui consomment ces bibliothèques — ne respecteront pas ces fichiers de verrouillage.

Merci d'avoir lu ! Si vous pensez que cet article était utile, veuillez appuyer sur le "❤️" pour aider à promouvoir cet article auprès des autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*L-UrDWXiwdc5hHgjzlRDjg.gif)