---
title: Comment j'ai construit un récupérateur de profils de joueurs NBA avec React,
  Redux-Saga et Styled Components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-13T09:29:12.000Z'
originalURL: https://freecodecamp.org/news/build-a-nba-player-profile-fetcher-with-react-redux-saga-and-styled-components-680cde2b8254
coverImage: https://cdn-media-1.freecodecamp.org/images/1*799DwILNz4o4I_PrUqVjvw.jpeg
tags:
- name: nba
  slug: nba
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit un récupérateur de profils de joueurs NBA avec React,
  Redux-Saga et Styled Components
seo_desc: 'By Jonathan Puc

  Hello, all! It’s been a while since I built something out of personal enjoyment
  or curiosity, so I surfed the internet exploring cool API’s.

  Since it’s NBA Playoff time (sadly, I’m a Knicks fan), I decided to see if there
  was an exist...'
---

Par Jonathan Puc

Bonjour à tous ! Cela fait un moment que je n'ai pas construit quelque chose par plaisir ou par curiosité, alors j'ai surfé sur internet à la recherche d'API cool.

Puisque c'est la période des playoffs NBA (malheureusement, je suis fan des Knicks), j'ai décidé de voir s'il existait une API contenant les données de tous les joueurs actuellement en NBA — et oui, il y en avait une.

De plus, un projet sur lequel je travaille dans mon emploi m'a fait découvrir deux bibliothèques **formidables** appelées **redux-saga** et **styled components**. Elles sont assez excitantes, et sont deux choses que je prévois d'essayer et d'utiliser dans tous mes futurs projets.

Alors construisons une application React avec ces bibliothèques !

Avant de plonger, parlons un peu de redux-saga et des styled components et pourquoi ils sont pratiques.

### Redux-Saga

Dans Redux, les actions et les réducteurs sont purs, ce qui signifie qu'ils n'ont aucun effet secondaire.

Un exemple d'effet secondaire pourrait être quelque chose comme une requête de service. Lorsque vous faites une requête, elle peut échouer ou retourner un résultat différent même si vous envoyez toujours la même requête.

Alors si vos réducteurs et actions sont purs, où pouvez-vous gérer/mettre les effets secondaires ? Eh bien, redux-saga est une solution. Il vous permet d'écouter les actions, d'effectuer un effet secondaire, puis de dispatcher une autre action.

Je sais, les paroles sont bon marché. Montrez-moi le code.

Êtes-vous prêt à voir un exemple de cette bête en action ?

En résumé, nous avons une fonction qui écoute chaque fois qu'une action de type `IMAGE_FETCH_REQUESTED` est dispatchée. Lorsqu'elle en identifie une, elle appellera la fonction fetchImage.

À l'intérieur de la fonction fetchImage, nous faisons simplement un `call` spécial à une méthode sur notre objet `service`, en passant l'`userId` de l'image de profil que nous voulons récupérer. Le résultat est enregistré dans notre variable profileImage.

Peu après, nous informons notre store que nous avons réussi à récupérer une image et que nous souhaitons transmettre l'image pour qu'elle soit stockée. Nous allons donc simplement dispatcher une action avec `put` avec le type `'IMAGE_FETCH_SUCCEEDED'` et passer l'image comme payload. Notre réducteur gérera le reste.

Mais **si** il y a une sorte d'erreur, nous dispatchons simplement une action avec le type `'IMAGE_FETCH_FAIL'` et passons l'erreur comme payload.

La beauté de cela réside dans la façon dont cela se lit et s'intègre dans un simple bloc try catch.

N'hésitez pas à en lire plus sur [redux-saga](https://github.com/redux-saga/redux-saga).

### Styled Components

Découvrir les styled components a un peu soufflé mon esprit.

J'ai toujours eu du mal à structurer et à écrire du CSS dans les applications React. Quelque chose ne semblait pas juste et cela me semblait désordonné. En particulier, les noms de classe étaient difficiles.

L'idée toute entière de React est d'être modulaire : vous écrivez un composant une fois et vous pouvez l'utiliser partout. Mais lors du stylage de tels composants, nous leur donnons toujours un nom de **classe** pour les cibler avec CSS.

[Max Stoiber](https://twitter.com/mxstbr?lang=en), co-créateur des styled components, l'a parfaitement exprimé lorsqu'il a dit :

> Si vous n'utilisez chaque nom de classe qu'une seule fois, pourquoi avez-vous un nom de classe du tout ?

Ayant entendu ces mots, j'ai su que les styled components étaient faits pour moi.

Alors voyons cela en action maintenant aussi :

Ici nous avons un composant fonctionnel de base : un bouton qui ne fait presque rien, même s'il vous défie de faire votre mouvement.

Cela peut sembler étrange pour les nouveaux venus, mais en réalité c'est assez simple et je suis sûr que vous allez l'adorer en un rien de temps.

Nous importons `styled` de la bibliothèque. Pensez à cela comme une usine qui vous permet de créer les nœuds HTML que vous connaissez et aimez.

Nous créons le nœud de notre choix. Dans ce cas, un bouton et un span, avec ses styles. Nous l'assignons ensuite à une variable de notre choix.

Maintenant nous faisons référence à ces variables et les insérons dans notre composant fonctionnel pour qu'elles soient rendues.

C'est aussi simple que cela.

Ce que j'aime vraiment, c'est que vous pouvez toujours écrire le CSS auquel vous êtes familier dans un fichier JS. De plus, cela garde tout bien et modulaire — tout se trouve dans un seul fichier, facile à lire et à digérer !

Vous pouvez en apprendre plus sur les styled-components [ici](https://github.com/styled-components/styled-components).

### Comment tout cela se lie ensemble

Nous allons construire une application où les utilisateurs peuvent rechercher un joueur en utilisant son prénom et son nom de famille. Notre saga (redux-saga) récupérera les données du joueur, y compris les statistiques et une photo de lui, et les enregistrera dans notre store redux. Et en utilisant les styled components, nous rendrons toutes ces informations un peu plus présentables.

### **Partie 1 — Installation de notre application et react-redux.**

Nous utiliserons create-react-app dans ce projet, donc si vous ne l'avez pas encore installé, exécutez simplement `npm install -g create-react-app`.

Lorsque cela est fait, nous exécuterons `create-react-app nba-players`.

Maintenant, après que toute l'installation et l'échafaudage soient terminées, nous exécuterons `cd nba-players` puis installerons les modules dont nous aurons besoin avec `npm install --save redux react-redux redux-saga styled-components axios`.

#### Configuration de notre store redux

Ce sera un guide rapide pour configurer notre store, puisque ce guide concerne redux-saga et les styled components et non react-redux/redux.

À l'intérieur de votre dossier `src`, nous créerons un dossier appelé `store` et créerons notre fichier `index.js`.

store/index.js

Nous utiliserons Redux DevTools pour voir ce qui se passe sous le capot dans notre store. Vous pouvez télécharger l'extension Chrome [ici](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd?hl=en).

#### **Créons nos réducteurs.**

Créez un dossier appelé `reducers` à la racine de votre dossier `store`, et créez les deux fichiers suivants :

reducers/index.js

reducers/player.js

#### **Créons nos actions**

Créez un dossier appelé `actions` à la racine de votre dossier `store`, et créez les deux fichiers suivants :

actions/actionTypes.js

actions/player.js

Avec toutes ces pièces créées, connectons le store à notre application React !

Naviguez jusqu'à `src/index.js` et ajoutez ce qui suit :

Super, testons et assurons-nous que tout fonctionne comme prévu.

De retour dans notre terminal, nous exécuterons `npm run start` pour lancer notre application React, ouvrir les outils de développement, et naviguer jusqu'à l'onglet 'Redux'. Cliquez sur l'onglet State dans les Redux DevTools.

Vous devriez voir quelque chose comme ceci :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*klP5Nqu0Bwibd-KI9SimWw.png)

Super, nous avons tout ce dont nous avons besoin pour commencer.

### Partie 2 — Redux Saga

Nous sommes prêts à utiliser l'API des joueurs NBA pour récupérer des données et les charger dans notre store !

Écrivons notre première saga.

À l'intérieur de notre dossier `src/store`, nous créerons un dossier appelé `sagas` et créerons un fichier appelé `index.js`.

Cela sert essentiellement de watcher/porteur.

La `ligne 8` est là et écoute certains types d'actions que nous lui donnons. Lorsqu'une action passe qui correspond, elle appellera une fonction, dans ce cas retrievePlayer. Nous allons la créer maintenant.

Dans le même dossier, nous créerons un fichier appelé `player.js` et il contiendra ce qui suit :

La fonction génératrice retrievePlayer est là où la magie opère, alors parcourons-la.

La fonction a accès à l'action qui est passée. Si vous vous souvenez de notre créateur d'action dans `actions/player.js`, nous passons un nom.

Nous utiliserons la destructuration ES6 pour obtenir le nom et le prénom de l'objet nom attaché au payload de l'action.

En utilisant redux-saga, nous `call` notre fonction fetchPlayerData et passons les détails du nom.

fetchPlayerData fera un appel GET à l'API des joueurs NBA et retournera la réponse. La réponse sera enregistrée dans la variable stats.

L'accès à l'image des joueurs est aussi simple que d'ajouter le nom et le prénom à l'endpoint de l'API, alors nous faisons juste cela.

Nous enregistrons nos deux nouvelles pièces de données dans un objet appelé playerProfile.

Nous utilisons ensuite le `put` de redux-saga qui dispatchera une action. Ici, nous lui donnons le type `GET_PLAYER_SUCCESS` avec notre nouveau playerProfile comme payload.

Si quelque chose ne va pas, nous dispatchons simplement une action avec le type `GET_PLAYER_FAIL` et passons l'erreur comme payload.

C'est tout !

Notre réducteur de joueurs que nous avons créé précédemment dans `reducers/player.js` gérera le reste après avoir reçu les actions que nous avons dispatchées.

Il y a une dernière chose que nous devons faire avant que nos sagas fonctionnent, cependant.

À l'intérieur de `store/index.js`, nous devrons faire quelques modifications.

Il devrait maintenant ressembler à ce qui suit

Hourra, nous sommes maintenant prêts à construire quelques composants qui nous permettront de rechercher un joueur et de voir son image et ses statistiques :)

### Partie 3 — Styled Components

`components/Search.js`

`components/StatBox.js`

`components/PlayerPhoto.js`

`components/Player.js`

Avec tous nos composants construits, il est temps de les importer dans notre `App.js`

Tout est connecté et prêt à partir. Il suffit de taper le nom complet d'un joueur à votre convenance, comme Lebron James ou Stephen Curry, et vous devriez voir quelque chose comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oVmg6dXWrMrl87VnXUxwog.png)

Ce n'est pas la chose la plus jolie à regarder, mais c'est une opportunité pour vous d'appliquer le style comme vous le souhaitez. Allez-y avec la bibliothèque styled-components.

N'oubliez pas non plus que nous avons ajouté une propriété `loading` dans notre store redux `state.player.loading` ? Pourquoi ne pas rendre l'UX un peu plus agréable en affichant un message de chargement lorsque loading est défini sur true ?

Nous avons créé ensemble la fondation de l'application — maintenant, allez-y et donnez-lui votre touche personnelle :)

Si nécessaire, vous pouvez trouver le code source [ici](https://github.com/jonathanpuc/nba-mania).

Comme toujours, ma boîte de réception est ouverte à toute personne ayant besoin de conseils supplémentaires ou si vous avez des questions.

N'hésitez pas à me contacter sur l'une des plateformes ci-dessous !

[Instagram](https://www.instagram.com/jonathanpucc/) | [LinkedIn](https://www.linkedin.com/in/jonathan-puc-549531b3/) | [Twitter](https://twitter.com/jonathanpuc7)