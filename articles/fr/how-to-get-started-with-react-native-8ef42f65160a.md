---
title: Comment commencer avec React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-09T22:48:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-react-native-8ef42f65160a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4FUZ_X3XD3MgqsrpncPhTA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: Comment commencer avec React Native
seo_desc: 'By Spencer Carli

  Before diving in I want to tell you a little story — I’ve been wanting to put together
  a simple website. Not a web app, just a simple website. I haven’t done that in a
  quite a while so I started looking around for how to do it…

  … and...'
---

Par Spencer Carli

Avant de plonger, je veux vous raconter une petite histoire — j'ai voulu créer un simple site web. Pas une application web, juste un simple site web. Je ne l'avais pas fait depuis un moment, alors j'ai commencé à chercher comment faire...

... et puis je me suis retrouvé à tomber dans un terrier de complexité croissante, utilisant différents outils, et oubliant ce que je voulais vraiment construire.

J'ai fini par tout jeter (c'était inutile de toute façon), m'inscrire à un cours, et simplement suivre les instructions pour avoir une idée des choses avant de travailler sur mon projet.

La plupart de mon temps est passé dans le monde de React Native, et sur le web, je vois beaucoup de gens dans la même situation que moi. J'échange des emails et des messages avec quelques dizaines de personnes par semaine qui sont également intéressées par l'apprentissage de React Native. Elles en ont entendu parler par un ami ou un collègue, l'ont vu mentionné sur Twitter, un client **insiste** pour l'utiliser pour un projet, ou pour une douzaine d'autres raisons. Les gens de la tech sont très divers dans la façon et la raison pour lesquelles ils apprennent de nouvelles choses.

Certaines personnes viennent d'un milieu de développement web, d'autres ont utilisé des outils comme Cordova, et d'autres font le saut dans le monde JavaScript pour la première fois. Peu importe le parcours de quelqu'un, beaucoup des mêmes choses reviennent.

### **Les problèmes de syntaxe JavaScript**

```
class App extends React.Component { ... }
```

D'accord, j'ai déjà vu des classes. Pas de gros problème — mais en JavaScript ?

```
const { amount, purchaseDate } = this.props;
```

Hein, `const` et qu'est-ce que c'est que ces accolades à gauche du signe égal ?

```
export default App;export App;
```

Quelle est la différence, cependant ?

Peu importe que vous soyez familier avec JavaScript ou non, l'utilisation de ES2015/ES6 pose problème à beaucoup de gens. Et c'est **très** courant dans React Native. Les personnes qui ont utilisé JavaScript n'ont souvent pas utilisé cette syntaxe (relativement) nouvelle. Et les personnes qui apprennent JavaScript utilisent souvent des tutoriels qui ne l'utilisent pas. Cela conduit à plus de confusion.

Sachez simplement que ce que vous voyez dans les tutoriels JavaScript s'applique toujours, tout comme ce que vous avez appris précédemment. ES2015/ES6 est simplement une extension qui facilite les choses (une fois que vous êtes familier avec).

Pour apprendre ES2015/ES6, consultez cette [introduction sans fioritures par Babel](https://babeljs.io/learn-es2015/). Il y a aussi une [belle série](https://medium.freecodecamp.com/learn-es6-the-dope-way-i-const-let-var-ae828580472b) qui vous introduira et expliquera les choses.

#### Avoir une compréhension de base de React

Je sais que vous voulez plonger directement dans React Native — c'est **génial**. Mais si vous voulez minimiser la confusion, alors je vous suggère de passer un peu de temps à comprendre les bases d'une application React.

Il y a quelques termes que vous voudrez connaître et vous voudrez comprendre comment composer une application. React Native est une extension de React. C'est juste une cible cliente différente qui utilise React et ses principes pour créer l'application.

Avoir une compréhension de React est une bonne utilisation de votre temps. Parcourir la [page d'accueil](https://facebook.github.io/react/) seule vous aidera beaucoup. Je vous suggère également de consulter le [tutoriel officiel](https://facebook.github.io/react/tutorial/tutorial.html) pour avoir une meilleure compréhension.

Vous n'avez pas à passer beaucoup de temps ici à construire une application web complexe avec React, utilisez simplement ce temps pour vous familiariser avec l'idée de React.

### Installation de l'environnement de développement

Vous n'avez pas besoin d'un éditeur de texte spécial. Ce que vous avez utilisé jusqu'à présent fonctionnera probablement bien. Ne stressez pas à propos de l'éditeur pour l'instant.

Maintenant, si vous voulez construire une application React Native, qui fonctionne sur iOS et Android, vous devez installer tous les outils de développement pour ces plateformes, n'est-ce pas ?

Eh bien, non. Pas tout de suite en tout cas.

Il y a un outil appelé [Expo](https://expo.io/) qui prend en charge toutes les choses de l'environnement de développement natif afin que vous puissiez vous concentrer sur l'apprentissage de React Native et la construction d'applications avec.

Mais attendez — ça devient encore mieux ! Il y a un outil en ligne de commande appelé [Create React Native App](https://github.com/react-community/create-react-native-app) qui rend encore **plus facile** de commencer avec React Native. Il est soutenu par Expo, ce qui signifie que tout ce que nous avons à faire est d'installer l'interface en ligne de commande et puis nous sommes prêts à courir avec React Native !

Scannez le code QR généré par l'application Expo et commencez à coder ! Le code sera mis à jour à chaque sauvegarde de fichier.

### Comment faire pour...

Voici une liste rapide et opinionnée d'outils pour répondre aux besoins courants :

* Gérer l'état : [Redux](http://redux.js.org/)
* Travailler avec une API distante : [Redux Saga](https://redux-saga.js.org/)
* Navigation : [React Navigation](https://reactnavigation.org/)
* Partager l'application : [Publier sur Expo](https://docs.expo.io/versions/v17.0.0/guides/exp-cli.html)
* Styliser l'application : [React Native Extended StyleSheet](https://github.com/vitalets/react-native-extended-stylesheet)
* Un éditeur de code : [Visual Studio Code](https://code.visualstudio.com/)

J'espère que cela vous aidera à démarrer avec React Native un peu plus rapidement et avec moins de confusion !

J'ai mis en place un cours vidéo gratuit qui vous guide à travers la construction d'une application React Native, de la configuration de votre environnement de développement à la publication sur Expo. Passez un peu de temps à comprendre ES2015, obtenez une idée générale de React, et plongez dans ce cours. Il a déjà aidé des centaines de personnes et j'espère qu'il pourra vous aider aussi !

[**Les bases de React Native : Construire un convertisseur de devises**](http://learn.handlebarlabs.com/p/react-native-basics-build-a-currency-converter)  
[_Apprenez à utiliser la navigation, configurer Redux, concevoir des composants, travailler avec une API distante, et plus encore_learn.handlebarlabs.com](http://learn.handlebarlabs.com/p/react-native-basics-build-a-currency-converter)

Si vous avez aimé cela, n'oubliez pas de le recommander et de l'envoyer à quelqu'un qui veut apprendre React Native !