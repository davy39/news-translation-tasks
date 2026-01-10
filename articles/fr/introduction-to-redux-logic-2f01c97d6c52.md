---
title: Une introduction à Redux-Logic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T17:57:06.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-redux-logic-2f01c97d6c52
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9lDu6F6XfDmzTsF3tCRDVA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Une introduction à Redux-Logic
seo_desc: 'By Sam Ollason

  This article will go through a high-level overview of Redux-Logic. We will look
  at what is it, why it is needed, how it differs from other Redux middleware and
  why I think it’s the best choice. We will then see an example of a simple W...'
---

Par Sam Ollason

Cet article présentera un aperçu de haut niveau de [Redux-Logic](https://github.com/jeffbski/redux-logic). Nous examinerons ce que c'est, pourquoi c'est nécessaire, comment il diffère des autres middlewares Redux et pourquoi je pense que c'est le meilleur choix. Nous verrons ensuite un exemple d'une simple [application météo](https://github.com/SamOllason/weather-app-redux-logic-example) pour démontrer comment les concepts de base sont mis en pratique.

Cet article suppose que vous avez une bonne compréhension de React et Redux.

### **Un rappel rapide sur Redux**

Redux est un conteneur d'état pour les applications JavaScript et est couramment utilisé avec React. Il fournit un endroit central pour stocker les données utilisées dans votre application. Redux fournit également un framework pour effectuer des **mutations d'état prévisibles**. L'utilisation de Redux facilite l'écriture, la compréhension, le débogage et la mise à l'échelle des applications dynamiques et pilotées par les données.

Dans Redux, les composants appellent des **créateurs d'actions** qui dispatchent des **actions**. Les actions sont (généralement !) de petits objets simples qui expriment une intention ou une instruction. Les actions peuvent également contenir des 'payloads' (c'est-à-dire des données).

L'état de l'application est géré par des **réducteurs**. Ils semblent plus compliqués qu'ils ne le sont ! Les actions sont traitées par un réducteur racine qui transmet ensuite l'action et le payload à un réducteur particulier. Ce réducteur **prendra une copie** de l'état de l'application, **mutera** **la copie** (en fonction de l'action et de son payload) puis mettra à jour l'état dans le **Store** de l'application.

### **Pourquoi le besoin de Redux Logic ?**

Par défaut, toutes les actions dans Redux sont dispatchées de manière synchrone. Cela pose un défi pour toute application nécessitant un comportement asynchrone, comme la récupération de données depuis une API... soit pratiquement n'importe quelle application !

Pour gérer le comportement asynchrone avec Redux, nous avons besoin d'un type de [middleware](https://en.wikipedia.org/wiki/Middleware) qui effectue un traitement entre le moment où l'action est dispatchée et le moment où l'action atteint les réducteurs. Plusieurs bibliothèques populaires fournissent cette fonctionnalité.

Après avoir exploré les différentes options, j'utilise Redux-Logic dans divers projets depuis un certain temps et je le trouve excellent !

### **Cycle de vie de Redux-Logic**

Redux-Logic fournit un middleware qui effectue un traitement entre le moment où une action est dispatchée depuis un composant et le moment où l'action atteint un réducteur.

Nous utilisons la bibliothèque [redux-logic](https://github.com/jeffbski/redux-logic) pour créer une 'Logique'. Ce sont essentiellement des fonctions qui interceptent des actions d'**objets simples**, effectuent un traitement asynchrone, puis dispatchent une autre action d'**objet simple**. Les fonctions de logique sont vraiment déclaratives et flexibles, comme nous allons le voir !

Une chose importante à retenir ici est que toutes les actions avec lesquelles Redux-Logic travaille sont des **objets simples**. L'action dispatchée par le composant UI et l'action dispatchée par la Logique seront **toujours** un objet simple (contrairement, par exemple, à une fonction). Nous reviendrons sur ce point ci-dessous lorsque nous comparerons différentes options de middleware.

Sous le capot, Redux-Logic utilise des 'observables' et la programmation réactive. [En savoir plus à ce sujet ici](https://github.com/jeffbski/redux-logic).

### **Flux de données**

Ci-dessous, à titre de comparaison, un diagramme que j'ai créé montrant les points importants dans le cycle de vie d'un processus Redux synchrone. Aucun middleware n'est inclus (car aucun n'est nécessaire !).

![Image](https://cdn-media-1.freecodecamp.org/images/gK7CP25zZc5gLL7FhvRdImhFclj3yyxSMZy6)

Voici maintenant un diagramme montrant les parties importantes d'un projet utilisant la bibliothèque redux-logic pour gérer les actions asynchrones. Cela sera utile à consulter plus tard avec l'exemple ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/9BNnOO6ZOIeBuMyS69YEnSWhd5WKtRfXVR9n)

Vous pouvez voir comment le middleware opère entre le moment où une action est dispatchée et le moment où elle est traitée par un réducteur.

### Principales différences avec d'autres solutions

[**Redux-Thunk**](https://github.com/reduxjs/redux-thunk) est un choix populaire pour le middleware Redux qui permet également de prendre en charge le comportement asynchrone. Pour gérer le comportement asynchrone avec Redux-Thunk, vos créateurs d'actions doivent **retourner des fonctions** au lieu de retourner des objets simples avec Redux-Logic. Je pense que le fait de dispatcher des objets simples avec Redux-Logic rend votre code beaucoup plus facile à écrire et à comprendre.

De plus, je pense que l'approche 'objet simple' pour gérer le comportement asynchrone s'intègre plus naturellement avec le reste de l'architecture (synchrone) de Redux, ce qui rend ce middleware plus organiquement intégré à Redux.

Un autre middleware Redux populaire est [**Redux-Saga**](https://redux-saga.js.org/docs/introduction/BeginnerTutorial.html). J'ai trouvé la courbe d'apprentissage pour comprendre les sagas (une fonctionnalité relativement nouvelle d'ES6) assez raide lorsque j'ai examiné cette option. Cela serait amplifié si vous vouliez introduire cette bibliothèque dans une application gérée par une équipe de plusieurs personnes. De plus, je pense que si elles ne sont pas bien gérées, les sagas peuvent créer un code compliqué par rapport à la Logique que vous créez avec redux-logic. Cela peut avoir un impact sur la vitesse de développement et la maintenabilité du code.

### **Aperçu de l'exemple**

Ci-dessous se trouvent des extraits simples d'une application React simple qui peut récupérer les conditions météo actuelles dans une ville et les présenter à l'utilisateur. L'exemple utilise Redux-Logic pour prendre en charge le comportement asynchrone afin de récupérer des données à l'aide d'une API gratuite [OpenWeatherMap](https://openweathermap.org/api).

Pour comparaison, j'ai inclus un processus Redux synchrone qui affiche le nombre de requêtes qu'un utilisateur a faites.

[Voici](https://github.com/SamOllason/weather-app-redux-logic-example) le code source.

![Image](https://cdn-media-1.freecodecamp.org/images/abgtDbvHZYsuvjiSrJBKFZ71fovCsLHkTgcP)

### Configuration de l'environnement de développement

Voici les commandes que j'ai exécutées pour commencer à créer mon application :

```
npx create-react-app appnpm install --save reduxnpm install --save react-reduxnpm install --save redux-logicnpm install --save axios
```

Et pour voir l'application :

```
npm start
```

Heureux de pouvoir voir la page d'accueil par défaut de Create React App à l'adresse _localhost:3000_, j'ai ensuite commencé à écrire du code !

Ci-dessous se trouvent des extraits de code qui montrent les points importants concernant l'intégration de Redux-Logic dans le projet.

### Ajout de middleware à notre Store Redux

Dans _appStore.js_, si nous n'utilisions aucun middleware, nous fournirions normalement uniquement notre réducteur racine à la méthode createStore. C'est ici que nous relions notre middleware Redux-Logic au reste de notre application.

Nous spécifions que nous voulons utiliser _axios_ comme client pour effectuer des requêtes HTTP.

Nous utilisons ensuite une méthode de redux-logic pour créer notre middleware et enfin nous l'ajoutons comme paramètre à la méthode createStore. Cela signifie que notre code Redux pourra accéder à notre middleware. Super !

![Image](https://cdn-media-1.freecodecamp.org/images/r0NZWYDdi3ZvOmUku2zR2t8F45z8YHnPDudw)
_appStore.js — utilisé pour créer notre Store et intégrer notre Logique_

### Dispatch d'actions asynchrones

Avec Redux-Logic, les actions qui déclenchent un comportement asynchrone sont dispatchées de la même manière que les actions qui déclenchent des mises à jour d'état synchrones. Il n'y a rien de différent !

Pour être complet, vous pouvez voir ci-dessous que lorsqu'un utilisateur clique sur un bouton, nous appelons un créateur d'action qui a été passé à notre composant en tant que props.

![Image](https://cdn-media-1.freecodecamp.org/images/DOnX38UsPeOd50wgdeuFRTA6dcFzYLu-n6bN)

### Interception des actions asynchrones

C'est ici que nous voyons pour la première fois l'émergence du middleware redux-logic entrer en jeu. Nous utilisons la bibliothèque redux-logic pour créer une 'Logique' qui intercepta des actions spécifiées.

Dans nos propriétés de Logique, nous indiquons à redux-logic quelle action nous voulons qu'il intercepte. Nous spécifions que nous voulons que redux-logic ne fournisse des données que depuis la dernière action de ce type que le composant a dispatchée. Dans notre exemple, ce comportement déclaratif est utile si les gens continuent de cliquer sur un bouton, car ils obtiendront la valeur de la dernière action qu'ils ont dispatchée, pas nécessairement la dernière promesse à retourner !

Ensuite, nous spécifions que lorsque le processus asynchrone retourne, nous **dispatchons immédiatement** l'une des deux actions. Si la promesse est retournée avec succès, nous retournons une action _GET_WEATHER_FOR_CITY_SUCCESSFUL_. C'est ce que nous voulons !

Alternativement, si la promesse retournée est rejetée, nous dispatchons _GET_WEATHER_FOR_CITY_FAILURE_.

**C'est ici que redux-logic brille vraiment**. Il est clair quelle est l'intention du code de Logique, et ce qui est émis sont des objets simples qui sont faciles à lire et à interpréter ! Je trouve cela vraiment facile à lire, à comprendre et à déboguer.

En bas, nous clarifions ce que nous voulons que notre processus asynchrone fasse. Nous voulons retourner la valeur d'une promesse. Remarquez comment nous passons le payload qui est venu avec notre action dans l'URL.

![Image](https://cdn-media-1.freecodecamp.org/images/kY3GKXhgCYVKaxZ2FgVRA1MExoxEzUr7pHzc)

### Traitement des actions asynchrones

Vous pouvez voir à partir du réducteur _weatherDataHandling.js_ que les actions dispatchées depuis notre Logique sont ensuite traitées comme des actions d'objets simples. Les réducteurs mutent l'état **de la même manière que pour les actions synchrones**. Donc, la capture d'écran ci-dessous est ce à quoi vous vous attendriez en travaillant avec Redux auparavant. Super !

![Image](https://cdn-media-1.freecodecamp.org/images/B58wMGADSPhShrZznOcsMNRicqSo5l52pZo-)

### Résumé

Redux est un conteneur d'état prévisible populaire pour les applications JavaScript. Par défaut, toutes les actions Redux ne prennent en charge que le comportement synchrone, et vous aurez besoin d'une sorte de solution de middleware pour le comportement asynchrone.

Redux-Logic fournit un middleware **clair** et **puissant** qui vous permet d'utiliser des actions asynchrones dans votre application Redux. Vous ajoutez votre middleware à votre **Store** Redux pour permettre à votre application d'utiliser Redux-Logic. Vous utilisez la bibliothèque [redux-logic](https://github.com/jeffbski/redux-logic) pour créer une **Logique** qui intercepte des actions particulières et dispatch des actions supplémentaires après qu'un certain traitement asynchrone (comme la récupération de données depuis une API) est terminé.

Toutes les actions impliquées sont des actions d'**objets simples**. Je pense que cela les rend **plus faciles à écrire** et **plus faciles à comprendre** par rapport à d'autres solutions. De plus, redux-logic semble être une intégration plus organique avec les autres parties de l'architecture Redux.

Merci d'avoir lu, je suis ouvert à tous commentaires ou questions ci-dessous !