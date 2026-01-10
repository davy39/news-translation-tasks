---
title: Division de code simple avec React et webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-07T22:02:35.000Z'
originalURL: https://freecodecamp.org/news/straightforward-code-splitting-with-react-and-webpack-4b94c28f6c3f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CNeQyaChrTh0H3ovOd9Dgg.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Division de code simple avec React et webpack
seo_desc: 'By Didier FRANC

  Everything seemed perfect until your app size increased too fast …


  Introduction

  You’re a big fan of React and even bigger fan of the modern JavaScript development
  stack. React, Redux, ES6, Babel, and webpack are your favorite toys, s...'
---

Par Didier FRANC

#### Tout semblait parfait jusqu'à ce que la taille de votre application augmente trop vite …

![Image](https://cdn-media-1.freecodecamp.org/images/1*CNeQyaChrTh0H3ovOd9Dgg.png)

### Introduction

Vous êtes un grand fan de **React** et encore plus grand fan de la pile de développement JavaScript moderne. React, Redux, ES6, Babel et webpack sont vos jouets préférés, alors n'ont-ils plus de secrets pour vous ? Bien sûr qu'ils en ont — ce que vous verrez après avoir lu ce qui suit.

Cet article ne vise pas à être exhaustif, mais décrira une méthode moderne et simple pour résoudre un problème lié à la façon dont nous aimons coder.

### Le problème

Voici un bon exemple. Comme vous pouvez le voir, webpack a créé deux fichiers JavaScript : **_bundle.js_** et _vendor.js_. C'est la première étape de la division de code, séparant vos dépendances de votre propre code. Cela est bien documenté dans la [nouvelle documentation de webpack](https://webpack.js.org/guides/code-splitting-libraries/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*u1CSFKmreuN4KjulOJFZAg.png)
_Tapez **yarn build** et vous verrez la tragédie …_

C'est un préalable pour les étapes suivantes. Partager des dépendances comme React et Redux avec tous vos composants est essentiel. Mais comme vous pouvez le voir, la taille de notre application est proche de ~2 Mo sans ses images, polices et autres ressources. Notre application prendra des secondes à charger et encore plus avec une mauvaise connexion mobile. Pourquoi ne pas la diviser en plusieurs morceaux, qui ne se chargeront que lorsque nous en aurons besoin ? Plus facile à dire qu'à faire.

### Par où commencer ?

Il existe de nombreuses façons de s'y prendre lorsque l'on se soucie de la vitesse et des performances : l'une d'entre elles est le rendu côté serveur, mais ce n'est pas le sujet aujourd'hui ?.

Dans cet article, nous explorons la division de code avec webpack, et le meilleur endroit pour commencer est [le dépôt webpack lui-même](https://github.com/webpack/webpack/tree/master/examples). Il existe d'autres solutions également. Cela dit, nous devons faire un choix.. Et le gagnant est … `import()` (anciennement nommé `System.import()`)**_._** Je l'appelle la méthode « moderne ».

[**System.import a été déprécié.**](https://medium.com/@cerny.mrtn/system-import-has-been-deprecated-6806b2f506d)  
[medium.com](https://medium.com/@cerny.mrtn/system-import-has-been-deprecated-6806b2f506d)

#### 1. Soyez intelligent

Il n'y a pas d'outil magique, et pour obtenir le meilleur compromis, vous devrez probablement utiliser votre cerveau ?. Par exemple, vendor.js ne devrait pas contenir toutes les bibliothèques, seulement celles qui sont « globales » comme React, Redux ou moment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KHjkCbjOTrCwaUSdMabdAw.png)
_Ce n'est pas **package.json**_

#### 2. Commencez la division de code (la vraie)

Charger un composant (ou tout module ES) de cette manière sera interprété comme un point de division par webpack.

Maintenant, imaginez que nous avons ce qui suit à la racine de notre application. Le problème est le composant `Home`. Avec sa bibliothèque exotique, il est relativement gros par rapport au reste de l'application. Rappel : pour l'instant, tout est regroupé dans le même bundle et chargé en même temps.

Créons un simple composant wrapper qui chargera et rendra notre composant Home de manière asynchrone. Il ne sera chargé que lorsque vous serez connecté.

Nous pouvons simplifier encore plus en standardisant cette méthode. Je l'ai externalisée sous forme de petit module [react-code-splitting](https://github.com/didierfranc/react-code-splitting). Et le résultat final est visible ici :

Si vous voulez voir ce snippet en contexte, consultez [redux-react-starter](https://github.com/didierfranc/redux-react-starter/blob/master/src/components/App.js#L12).

#### **3. Résultat**

Comme vous pouvez le voir, webpack a créé un nouveau fichier nommé **_0.[chunkhash].js._** C'est notre vieux frère Home ?.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fef7AyiO4ZCxS6gYp0knJg.png)
_Le résultat de [didierfranc/redux-react-starter](https://github.com/didierfranc/redux-react-starter" rel="noopener" target="_blank" title=")_

#### 4. Profitez des avantages

Comme vous pouvez le voir, le composant **Home** (0.bf87aaa616cea4a1ed40.js) a été chargé à la demande, juste après que je me suis connecté. Notez que les performances seront encore meilleures si vous prenez [soin de la mise en cache](https://webpack.js.org/guides/caching/) et utilisez http/2. Vous pouvez faire du [Lighthouse Report](http://react.didierfranc.com/lighthouse.html) votre outil préféré pour évaluer les performances de votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*F4WvfKTOqiQKBw1MbKVmgw.png)
_Chrome > DevTools > Onglet Network_

### Qu'est-ce qui suit ?

N'hésitez pas à explorer le cache à long terme, les capacités hors ligne, et ainsi de suite. Pour faire simple : **comment créer une application web progressive**, encore et encore.

Vous ne voulez pas manquer mes articles ? Suivez-moi sur Twitter [@DidierFranc](http://twitter.com/didierfranc)