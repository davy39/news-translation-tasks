---
title: 'Le Guide du voyageur à React Router v4 : chemins récursifs, à l''infini et
  au-delà !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-08T13:14:22.000Z'
originalURL: https://freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-21c99a878bf8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*lXTz6U5B8ySl0skc
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: 'Le Guide du voyageur à React Router v4 : chemins récursifs, à l''infini
  et au-delà !'
seo_desc: 'By Eduardo Vedes

  Welcome to the third part of the Hitchhiker’s Guide to React Router v4. In this
  article we’re going to focus on recursive paths. If you’ve missed the first two
  parts, you can find part 1 here and part 2 here.

  What are recursive paths...'
---

Par Eduardo Vedes

Bienvenue dans la troisième partie du Guide du voyageur à React Router v4. Dans cet article, nous allons nous concentrer sur les chemins récursifs. Si vous avez manqué les deux premières parties, vous pouvez trouver la partie 1 [ici](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/) et la partie 2 [ici](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-4b12e369d10/).

### Qu'est-ce que les chemins récursifs ?

Les chemins récursifs ne sont rien de plus que des chemins composés de routes imbriquées qui rendent le même composant pour afficher des vues imbriquées.

**Exemple :** `http://evedes.rockz/Topics/1/2/3/2/1`

Ils sont couramment utilisés pour créer des "fil d'Ariane" sur les sites web — un modèle de navigation qui montre où se trouve l'utilisateur dans la structure organique d'un site, un arbre de relations d'amis sur un réseau social, résoudre de nombreux problèmes de graphes complexes, des analyses, ou tracer tout type d'information qui dépend du dernier chemin. Cela peut être le cas, par exemple, d'un jeu vidéo où vous passez d'une pièce à une autre et le chemin que vous avez pris pour y arriver doit être suivi pour une raison quelconque.

Excité ? Dites "ouais" ! ?

Alors, faisons quelques changements dans notre application pour tester ce modèle appliqué dans React Router v4.

### L'objectif

L'idée ici est de transformer notre liste de sujets.

Au lieu d'avoir une liste de sujets qui sont appariés et que l'utilisateur peut naviguer pour voir chaque détail de sujet et revenir en arrière (vu dans la [Partie I](https://medium.freecodecamp.org/hitchhikers-guide-to-react-router-v4-a957c6a5aa18) de ce guide), faisons une route imbriquée qui commence au Sujet 1 et montre à l'utilisateur quels sujets sont liés à celui-ci — en affichant une liste de liens qui peuvent être cliqués pour naviguer vers le détail du sujet lié suivant. Chaque fois que vous choisissez un sujet, vous pouvez naviguer vers celui-ci, voir ses détails et voir quels sujets sont liés à celui-ci.

### routes.js

![Image](https://cdn-media-1.freecodecamp.org/images/olKeKVQse2SAHuFm3EhWOXHR58bT0sBPsD6Z)
_routes.js_

Donc dans **routes.js**, nous avons supprimé l'import du composant **TopicDetails** et corrigé les routes pour rendre le composant **TopicList** lorsque le chemin est **/Topics/:topicId**, en plus de la **Route** existante vers **/Topics**.

Les deux rendront le même composant avec différentes propriétés de correspondance.

### TopicList.js

En plus de la petite correction ci-dessus, j'ai fortement refactorisé le fichier **TopicList.js**. Jetons un coup d'œil à ce que nous avons là :

![Image](https://cdn-media-1.freecodecamp.org/images/TjrHUIdtieZDPOCHLv3e4us0G7OaHyMgRs68)
_fig 1.-imports et définitions de const_

Nous avons importé **Route** et **Link** du package **react-router-dom** parce que nous allons les invoquer plus tard dans le code.

Nous avons créé un tableau d'objets qui contient la liste des sujets. Chaque sujet a un tableau **relatedTopics** qui promeut la relation entre eux.

Nous avons créé une fonction **find** qui reçoit l'id du sujet comme argument et retourne l'élément ou le sujet qui correspond sans équivoque à l'id passé.

L'utilisation de **parseInt(id, 10)** garantit que même si l'argument passé à la fonction **find** est une chaîne, il devient un entier en base 10 (système de numération décimal).

Observez que les valeurs **id** et **relatedTopics** de nos sujets sont des entiers primitifs.

Pour en savoir plus sur **parseInt**, consultez [ICI](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt).

![Image](https://cdn-media-1.freecodecamp.org/images/bd3vrUgWPZrDDw7o2WsuOO14as9VFlHS4Jqs)
_fig.2-Composant TopicDetail sans état_

Le composant **TopicDetail** commence par définir la variable **topic**. Cela stockera le résultat de la fonction **find** qui récupère l'**id** qui provient de l'objet **match** (routeur) lorsque le composant est invoqué. Il retourne ensuite l'objet **topic** qui correspond à cet **id**.

Avec cet objet **topic** stocké, il retourne les **Details** du sujet et crée une liste non ordonnée dynamique avec l'**id** et le **name** des sujets liés.

Voyons cela dans le navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/3xH6KmVJ6-OZkNAZBBABE65iZ8ViYFr784Ab)
_**Détails du Sujet 1 (Info et Sujets Liés)**_

Bien ! Cela fonctionne !

Donc, lorsque vous cliquez sur l'un des liens affichés, il vous dirige vers l'**id** du sujet suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/JEBsBuYFBBdKTMjr0NjHe3RMNYjGPhDxaNzu)
_**Route à invoquer à l'intérieur du composant TopicDetail**_

Wow ! Cette route est en dehors du fichier **routes.js** ! C'est nouveau. Observez que techniquement vous pouvez créer des routes à l'intérieur de n'importe quel composant.

N'oubliez pas que **isExact** est faux parce que l'**url** ne correspond pas entièrement au chemin de **/Topics/:topicId** tel que défini précédemment dans le composant **routes.js**.

![Image](https://cdn-media-1.freecodecamp.org/images/tubC6XVUSQmFdxIu7-QmfYcqaZnM4QYrYXj2)
_**fig.3-Composant TopicList sans état**_

En fin de compte, nous définissons et exportons le composant **TopicList** qui invoque **TopicDetail** avec l'objet match ci-dessus. Mais, comme dans chaque instance de **TopicDetails** lorsque vous déclenchez une **Route**, **TopicDetail** est réaffiché avec de nouvelles propriétés **match** fournies par le **Router** à chaque instance.

Nous avons donc terminé ! ?

### Dernier point mais non des moindres

Je pense qu'à ce stade, vous avez déjà une bonne idée de la façon de commencer à implémenter des routes récursives.

J'ai choisi cet exemple parce qu'il est facile à comprendre et très utile pour certaines choses de base.

Les changements que j'ai apportés à l'application, pour produire cet article, peuvent être trouvés dans mon dépôt GitHub [repo](https://github.com/evedes/ReactRouter_BoilerPlate_03).

### Bibliographie

Pour écrire cet article, j'ai utilisé la documentation de React Router que vous pouvez trouver [ici](https://reacttraining.com/react-router/core/guides/philosophy).

Tous les autres sites que j'ai utilisés sont liés tout au long du document pour ajouter des informations ou fournir un contexte à ce que j'ai essayé de vous expliquer.

Cet article fait partie d'une série intitulée "Le Guide du voyageur à React Router v4".

* **[Partie I : Comprendre React Router en 20 min](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/)**
* **[Partie II : [match, location, history] — vos meilleurs amis !](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/)**
* **[Partie IV : configuration de route, la valeur cachée de la définition d'un tableau de configuration de route](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-c98c39892399/)**

? Merci beaucoup !