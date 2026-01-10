---
title: Qu'est-ce que Node.js exactement ? Expliqué pour les débutants
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2022-12-05T15:18:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/What-is.png
tags:
- name: Express
  slug: express
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: npm
  slug: npm
seo_title: Qu'est-ce que Node.js exactement ? Expliqué pour les débutants
seo_desc: 'Node.js allows developers to create both front-end and back-end applications
  using JavaScript. It was released in 2009 by Ryan Dahl.

  In this article, you will learn about Node.js. You will learn the following:


  What is Node.js?


  How the Node.js envir...'
---

Node.js permet aux développeurs de créer des applications front-end et back-end en utilisant JavaScript. Il a été publié en 2009 par Ryan Dahl.

Dans cet article, vous apprendrez à connaître Node.js. Vous apprendrez les points suivants :

* Qu'est-ce que Node.js ?

* Comment l'environnement Node.js diffère du navigateur.

* Pourquoi vous devriez apprendre Node.js.

* Comment commencer avec Node.js.

* Ressources pour vous aider à apprendre Node.js.

## Qu'est-ce que Node.js ?

> "Node.js est un environnement d'exécution JavaScript open-source et multiplateforme." - [Nodejs.dev Docs](https://nodejs.dev/en/learn/introduction-to-nodejs/)

Cela semble être une réponse simple et cool. Mais pour un débutant, cette définition peut soulever d'autres questions. Alors, décomposons-la et comprenons ce qu'elle signifie.

**Node.js est open-source :** Cela signifie que le code source de Node.js est disponible publiquement. Et il est maintenu par des contributeurs du monde entier. Le [guide de contribution de Node.js](https://nodejs.org/en/get-involved/contribute/) vous montre comment contribuer.

**Node.js est multiplateforme :** Node.js n'est pas dépendant d'un système d'exploitation spécifique. Il peut fonctionner sur Linux, macOS ou Windows.

**Node.js est un environnement d'exécution JavaScript :** Lorsque vous écrivez du code JavaScript dans votre éditeur de texte, ce code ne peut effectuer aucune tâche à moins que vous ne l'exécutiez (ou ne le lanciez). Et pour exécuter votre code, vous avez besoin d'un environnement d'exécution.

Les navigateurs comme Chrome et Firefox ont des environnements d'exécution. C'est pourquoi ils peuvent exécuter du code JavaScript. Avant la création de Node.js, JavaScript ne pouvait fonctionner que dans un navigateur. Et il était utilisé pour construire uniquement des applications front-end.

Node.js fournit un environnement d'exécution en dehors du navigateur. Il est également basé sur le [moteur JavaScript Chrome V8](https://www.freecodecamp.org/news/javascript-under-the-hood-v8/). Cela permet de construire des applications back-end en utilisant le même langage de programmation JavaScript que vous connaissez peut-être déjà.

## Différences entre les environnements d'exécution du navigateur et de Node.js

Le navigateur et Node.js sont tous deux capables d'exécuter des programmes JavaScript. Mais il existe quelques différences clés que vous devez connaître. Elles incluent les points suivants.

### Accès aux API DOM

Avec l'environnement d'exécution du navigateur, vous pouvez accéder au Document Object Model (DOM). Et vous pouvez effectuer toutes les opérations DOM. Mais Node.js n'a pas accès au DOM.

Node.js expose presque toutes les ressources système à vos programmes. Cela signifie que vous pouvez interagir avec le système d'exploitation, accéder aux systèmes de fichiers, et lire et écrire dans les fichiers. Cependant, vous n'avez pas accès aux systèmes d'exploitation et aux systèmes de fichiers depuis le navigateur.

### Objet Window vs Global

JavaScript dispose d'un objet global intégré. L'objet global JavaScript pour le navigateur s'appelle l'objet `window`. Dans Node.js, l'objet global s'appelle `global`.

L'objet `window` contient des méthodes et des propriétés disponibles uniquement dans l'environnement du navigateur.

### Contrôle des versions d'exécution

Avec Node.js, vous pouvez choisir quelle version utiliser pour exécuter votre application côté serveur. Par conséquent, vous pouvez utiliser des fonctionnalités JavaScript modernes sans vous soucier des incohérences spécifiques à une version.

Contrastez cela avec l'environnement d'exécution du navigateur. En tant que développeur, vous n'avez aucun contrôle sur la version des navigateurs que vos clients utilisent pour accéder à votre application.

### Chargement des modules (mots-clés `import` vs `require`)

Node.js offre un support prêt à l'emploi pour les modules CommonJS et ES. Vous pouvez charger des modules en utilisant le mot-clé `require` (syntaxe CommonJS) et le mot-clé `import` (syntaxe ES).

Certains navigateurs modernes supportent les modules ES. Cela signifie que vous pouvez utiliser `import` pour les modules ES. Mais vous devrez toujours créer des bundles pour prendre en charge les anciens navigateurs qui ne supportent pas les modules ES.

## Combien de JavaScript devez-vous connaître pour commencer avec Node ?

Si vous êtes un débutant absolu en JavaScript, je vous recommande de commencer par les bases.

Familiarisez-vous d'abord avec les concepts de base de JavaScript. Ensuite, vous pourrez passer à l'apprentissage de la construction d'applications côté serveur avec Node.js.

Il n'y a aucun moyen d'épuiser tout ce qu'il y a à apprendre sur JavaScript. Alors, comment déterminer quand vous connaissez suffisamment JavaScript pour commencer avec Node.js ?

La documentation de Node.js fournit une [liste de sujets JavaScript à apprendre](https://nodejs.org/en/learn/getting-started/how-much-javascript-do-you-need-to-know-to-use-nodejs) avant de plonger profondément avec Node.js.

Une fois que vous avez une bonne compréhension des bases de JavaScript, vous pouvez commencer avec Node.js.

## Comment commencer avec Node.js

Voyons comment vous pouvez créer votre première application Node.js. Cette section vous montrera comment exécuter des scripts Node.js depuis la ligne de commande.

### Comment télécharger et installer Node.js

Tout d'abord, vous devez télécharger et installer Node.js. Il existe différentes façons de le faire. Si vous êtes un débutant, je vous suggère de [télécharger Node.js depuis le site officiel](https://nodejs.org/en/download/).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/node1.PNG align="left")

*Capture d'écran du site officiel de Node.js*

Des packages officiels sont disponibles sur le site pour toutes les principales plateformes (Windows, macOS et Linux). Téléchargez et installez le package approprié pour votre système.

### Comment vérifier la version de Node.js

Pour vérifier la version de Node.js, exécutez la commande `node --version` dans votre terminal. 
Si l'installation a réussi, vous verrez la version de Node.js que vous avez installée. Vous devriez obtenir une réponse comme la capture d'écran ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/node2.PNG align="left")

### Comment exécuter Node.js depuis la ligne de commande

Créons une simple application `Hello World`.

Créez un nouveau dossier de projet. Vous pouvez l'appeler `mon-projet`. Ouvrez le projet dans votre éditeur de code. À l'intérieur du dossier, créez un fichier `app.js`.

Ajoutez le code suivant à `app.js`

![Image](https://www.freecodecamp.org/news/content/images/2022/11/node3.PNG align="left")

Comme vous pouvez le voir, il s'agit de code JavaScript.

Vous pouvez exécuter le script dans la ligne de commande en exécutant la commande `node <nomDuFichier>`. Dans ce cas, le nom du fichier est `app.js`.

Exécutez la commande suivante dans votre terminal pour exécuter le programme `Hello world.` :

```bash
node app.js
```

Vous devriez voir la chaîne "Hello world." enregistrée dans votre terminal comme ceci.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/node4.PNG align="left")

Félicitations ! Vous venez d'exécuter votre première application Node.js.

## Devriez-vous apprendre Node.js ?

Voici quelques raisons pour lesquelles vous devriez envisager d'apprendre Node.js.

### Node.js vous permet d'écrire du JavaScript à la fois sur le client et le serveur.

L'un des avantages de Node.js est qu'il vous permet de travailler à la fois sur le front-end et le back-end de votre application. Et vous utilisez un seul langage de programmation - JavaScript - pour le faire.

C'est une bonne nouvelle pour les développeurs front-end qui travaillent avec JavaScript. Si vous souhaitez commencer à travailler sur le côté serveur, c'est plus facile par rapport à l'apprentissage d'un nouveau langage back-end à partir de zéro.

### Node a une communauté dynamique.

Comme je l'ai mentionné plus tôt dans l'article, Node.js est open-source. Il est activement maintenu par des développeurs du monde entier.

Il existe une communauté dynamique autour de Node.js. Vous pouvez trouver d'excellents tutoriels et des solutions aux problèmes lorsque vous êtes bloqué.

### Node est construit sur le moteur V8 de Google Chrome.

Node.js est construit sur le moteur JavaScript Chrome V8. Cela est significatif car le moteur V8 alimente certaines des applications dans le navigateur de Google comme Gmail. Ainsi, Google investit massivement pour garantir qu'il offre des performances élevées.

### Demande sur le marché

De nombreux grands noms comme Netflix, Uber, Paypal, LinkedIn et d'autres utilisent Node.js. En dehors des grands noms, de nombreuses startups utilisent également Node.js pour développer leurs applications.

Apprendre à travailler avec Node.js fera de vous un candidat recherché sur le marché du travail.

### La bibliothèque NPM

La bibliothèque NPM est l'une des excellentes ressources qui accompagne Node.js. 
La bibliothèque contient un registre de plus d'un million de packages. Un package est un morceau de code réutilisable.

Vous pouvez créer un package pour une tâche ou un problème récurrent et partager le code avec d'autres via le registre.

Vous pouvez également télécharger des packages que d'autres ont partagés. Pour de nombreuses tâches que les développeurs effectuent régulièrement, il existe des packages disponibles pour cela.

## Ressources pour apprendre Node

Si vous êtes curieux d'apprendre à construire des applications Node.js, je recommande les ressources suivantes.

* [Cours de 8 heures sur Node.js et Express.js sur la chaîne YouTube freeCodeCamp](https://www.youtube.com/watch?v=Oe421EPjeBE).

* [Le programme de développement back-end et d'APIs de freeCodeCamp](https://www.freecodecamp.org/learn/back-end-development-and-apis/)

* [Documentation Nodejs.dev](https://nodejs.dev/en/learn)

De plus, ci-dessous se trouve un lien vers une vidéo de Ryan Dahl lorsqu'il a présenté Node.js pour la première fois.

[Ryan Dahl : Présentation originale de Node.js à JSConf 2009](https://www.youtube.com/watch?v=ztspvPYybIY)

## Conclusion

Un seul article de blog comme celui-ci n'est pas suffisant pour apprendre tout ce qu'il y a à savoir sur Node.js. Le but de cet article était de vous donner un aperçu de ce qu'est Node.js.

Si vous n'étiez pas sûr de ce qu'est Node.js, j'espère que cet article a répondu à vos préoccupations et clarifié votre confusion.

Merci d'avoir lu. Et bon codage !