---
title: Pourquoi ClojureScript fonctionne si bien avec NPM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T15:03:32.000Z'
originalURL: https://freecodecamp.org/news/why-clojurescript-works-so-well-with-npm-128221d302ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7BrQfhUCEy_NObCNy3nv0A.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Pourquoi ClojureScript fonctionne si bien avec NPM
seo_desc: 'By Jacek Schae

  Every language that complies/transpiles to JavaScript wants to connect to npm to
  use this huge ecosystem. The master of this is, of course, ECMAScript. The second
  one — in my humble opinion — is ClojureScript, due to shadow-cljs.


  Disc...'
---

Par Jacek Schae

Chaque langage qui compile/transpile vers JavaScript souhaite se connecter à npm pour utiliser cet énorme écosystème. Le maître en la matière est, bien sûr, ECMAScript. Le second — à mon humble avis — est ClojureScript, grâce à [shadow-cljs](https://github.com/thheller/shadow-cljs).

> Avertissement : Je sais qu'il y a beaucoup de travail en cours dans différentes communautés qui exploitent npm. En aucun cas je ne cherche à diminuer cela en affirmant que CLJS (ClojureScript) est le meilleur. Je veux simplement vous donner un aperçu de son fonctionnement dans ClojureScript.

### Installation des packages npm

Dans ClojureScript, nous installons les packages npm comme nous le ferions en JavaScript. Nous utilisons le standard package.json et l'outil de build [shadow-cljs](https://github.com/thheller/shadow-cljs), et vous comprendrez le reste.

![Image](https://cdn-media-1.freecodecamp.org/images/UBPt1Q5nW8lvc4QSIE5Xmflmx17dCaDnvHAf)
_Installer firebase_

Après l'installation, nous devons importer le package. L'instruction `require` est presque identique à `import` en JS. En CLJS, nous inversons l'ordre — d'abord nous indiquons d'où, puis quoi.

![Image](https://cdn-media-1.freecodecamp.org/images/tMBZsomfbJl47awHgNXrbAyj2bE4kVodwpsQ)

Chaque fichier ClojureScript commence par une déclaration de namespace `ns`. Ensuite, nous utilisons `require` au lieu de `import`. Puis nous définissons une fonction avec `defn`. Cette fonction utilisera nos packages firebase requis, et au lieu d'utiliser `.` pour accéder à notre méthode `initializeApp`, nous utilisons `/`. Nous veillons à ce que lorsque nous invoquons la méthode JS `_initializeApp_`, nous convertissons la map CLJS (structure de données) en un objet JS avec `#js`.

Essayons quelques autres packages npm pour mieux comprendre l'interopérabilité entre npm et ClojureScript.

### React

Et si nous utilisions React ? ClojureScript dispose de plusieurs wrappers pour React — le plus populaire est [Reagent](https://github.com/reagent-project/reagent). Voici un exemple simple de compteur avec les hooks React et Reagent.

![Image](https://cdn-media-1.freecodecamp.org/images/tIxelAYrSbrtoDJu5QDZiNTeMODKeHfYnMLe)
_React JavaScript et Reagent ClojureScript_

Dans les deux exemples, nous importons/requérons d'abord React et Reagent. Ensuite, nous définissons l'état dans React en utilisant les hooks (et dans Reagent en utilisant les atomes).

Ce qui suit est un composant JSX (JavaScript) et hiccup (ClojureScript).

C'est cool, mais comment utilisons-nous les bibliothèques d'interface utilisateur React depuis Reagent ?

### Bibliothèques d'interface utilisateur React

L'une des bibliothèques d'interface utilisateur les plus populaires est [material-ui](https://material-ui.com/). Après l'installation, nous requérons cette bibliothèque, puis nous importons notre composant Button ainsi que React. En ClojureScript, nous ne requérons que le Button. Nous n'avons pas besoin de requérir Reagent puisqu'il est dans nos dépendances ClojureScript. Pour interagir avec React, nous utiliserions la forme `:&` et passerions toutes les propriétés que nous voulons dans `{}`.

![Image](https://cdn-media-1.freecodecamp.org/images/qhK96GMfydism4K6VugPXBt5PTAP02UHwpzw)

### Redux

Et Redux, pourriez-vous demander ? Eh bien, il y a une bibliothèque qui est construite sur Reagent, appelée [re-frame](https://github.com/Day8/re-frame/tree/master/docs). Conçue pour la première fois en décembre 2014, elle précède même l'officielle [Architecture Elm](https://guide.elm-lang.org/architecture/).

![Image](https://cdn-media-1.freecodecamp.org/images/qOUTrm4E9RM1wEnC64sQagJ4lm4QkBricVn3)

À ce stade, vous devriez avoir une assez bonne idée de pourquoi CLJS aime l'écosystème npm et de la facilité d'interopérabilité de CLJS vers JS. Peut-être que cela vous intéresse, et vous vous demandez pourquoi ? Pourquoi devriez-vous même essayer ClojureScript ?

### Pourquoi ?

#### Immuable

Toutes les structures de données ClojureScript sont immuables et persistantes. Vous n'avez pas besoin d'apprendre une nouvelle API si vous voulez exploiter quelque chose comme [ImmutableJS](https://immutable-js.github.io/immutable-js/).

#### Fonctionnel

ClojureScript embrasse les idées de la programmation fonctionnelle à son cœur. Vous n'avez pas besoin de [Lodash](https://lodash.com/) ou [Ramda](https://ramdajs.com/).

#### Simple

Avec [shadow-cljs](https://github.com/thheller/shadow-cljs), vous n'avez pas besoin de passer du temps à configurer vos builds. Vous requérez ce dont vous avez besoin et l'outil de build fera le travail.

#### Concis

Votre responsabilité est le nombre de lignes de code que vous écrivez. ClojureScript est l'un des langages de programmation les plus concis qui existent. Consultez la dernière section de [cette comparaison](https://medium.freecodecamp.org/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962).

#### **Puissant**

ClojureScript utilise les [Google Closure Tools](https://developers.google.com/closure/) pour la minification du code et le tree shaking. Les mêmes outils que Google utilise pour construire Gmail, Google Calendar, Google Docs et Google Maps.

#### JavaScript

Il compile/transpile vers JavaScript. Tout comme ES (EcmaScript), ReasonML, PureScript et Elm.

#### Amical

La communauté ClojureScript est le groupe de personnes le plus amical et accueillant que j'ai jamais rencontré en ligne. Nous traîons principalement sur [Slack](http://clojurians.net/) et [ClojureVerse](https://clojureverse.org/).

#### **Full-Stack**

Le grand frère de ClojureScript, Clojure, embrasse toutes ces idées avec Java. Si vous voulez écrire votre serveur sur l'une des plateformes les plus performantes et stables qui existent — la machine virtuelle Java — vous pouvez le faire en utilisant le même langage.

> Si vous aimez cet article, vous devriez me suivre sur [Twitter](https://twitter.com/JacekSchae). Je n'écris/tweete que sur la programmation et la technologie — principalement sur ClojureScript et Clojure.