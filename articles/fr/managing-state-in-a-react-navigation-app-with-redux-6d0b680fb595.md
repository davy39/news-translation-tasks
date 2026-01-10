---
title: Gestion de l'état dans une application React Navigation avec Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-15T21:12:48.000Z'
originalURL: https://freecodecamp.org/news/managing-state-in-a-react-navigation-app-with-redux-6d0b680fb595
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nSgapkNUSJdrpAVj9AJswg.jpeg
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
seo_title: Gestion de l'état dans une application React Navigation avec Redux
seo_desc: 'By Andrea Bizzotto

  In this tutorial, I will show how to manage navigation and application state by
  building a simple app with React Navigation and Redux.

  Prerequisite: you should already be familiar with React Native, React Navigation,
  and Redux. If ...'
---

Par Andrea Bizzotto

Dans ce tutoriel, je vais montrer comment gérer la **navigation** et l'**état de l'application** en construisant une application simple avec [React Navigation](https://github.com/react-navigation/react-navigation) et [Redux](https://github.com/reactjs/redux).

**Prérequis** : vous devez déjà être familiarisé avec React Native, React Navigation et Redux. Si vous débutez avec React Native, je vous recommande vivement ce cours :

* [The Complete React Native and Redux Course](https://www.udemy.com/the-complete-react-native-and-redux-course/learn/v4/overview)

### Aperçu de l'application

Nous allons construire une application composée de deux pages :

![Image](https://cdn-media-1.freecodecamp.org/images/1*duCfNDcSLqnQafA0SD230Q.png)

* **Page principale** : Elle affiche une vue conteneur avec une couleur de fond spécifique et un bouton. Lorsque le bouton est pressé, la deuxième page est présentée.
* **Page de choix de couleur** : Elle affiche des boutons ROUGE, VERT et BLEU. Lorsqu'une couleur est sélectionnée, l'application revient à la page principale et affiche la couleur de fond mise à jour.

En construisant cette application, vous apprendrez :

* Comment naviguer entre différents écrans avec [React Navigation](https://github.com/react-navigation/react-navigation)
* Comment utiliser les réducteurs et les actions pour mettre à jour l'état de l'application, de sorte que **les actions sur un écran entraînent des changements d'UI sur un autre**

Avec cette connaissance, vous serez en mesure de construire des applications plus complexes.

**Note** : Pour le reste de ce tutoriel, j'utiliserai les termes « page » et « écran » pour signifier la même chose.

### Configuration du projet (Expo)

Nous allons construire cette application avec [Expo XDE](https://expo.io/).

Vous pouvez télécharger Expo pour votre système d'exploitation depuis la [page GitHub d'Expo XDE](https://github.com/expo/xde).

Ensuite, consultez les [instructions d'installation](https://docs.expo.io/versions/latest/introduction/installation.html) sur la documentation d'Expo. Celles-ci vous montreront comment installer l'XDE sur votre bureau et exécuter des applications dans Expo sur un simulateur/appareil.

Comme nous exécuterons l'application sur le simulateur, vous devrez également télécharger [Xcode](https://developer.apple.com/download/) ou [Android Studio](https://developer.android.com/studio/index.html).

Lors du lancement d'Expo, cette page est présentée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yiLE3S0Zd_x0IGQfdv8b6Q.png)

* Sélectionnez « Create new project… »
* Choisissez le modèle vide et nommez le projet `**redux-navigation**`

Le projet sera créé, puis le packager React Native démarrera.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z694c-EY_l3CQylm9Vqxhw.png)

Pour exécuter l'application dans le simulateur, sélectionnez **Device -> Open in iOS Simulator**.

Une fois le simulateur démarré, l'écran suivant apparaît :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7faNeoH7BXTgV0x3H0yCgg.png)

Maintenant que le projet est créé, il peut être ouvert avec l'éditeur de votre choix. J'utilise [Visual Studio Code](https://code.visualstudio.com/Download) avec l'extension [React Native Tools](https://marketplace.visualstudio.com/items?itemName=vsmobile.vscode-react-native).

![Image](https://cdn-media-1.freecodecamp.org/images/1*42j6YEn6EwxRgfT11iT0Bw.png)

### Construction de l'application

Avant de pouvoir coder notre application, nous devons installer toutes les dépendances dont elle a besoin.

Ouvrez un terminal, allez dans le dossier du projet que vous avez créé dans Expo, et tapez :

```
npm install --save react-navigation redux react-reduxnpm install
```

Ensuite, **assurez-vous de cliquer sur le bouton Redémarrer dans Expo**. Si vous ne faites pas cela, les nouvelles dépendances ne seront pas reconnues et le simulateur affichera un écran d'erreur rouge si vous essayez de les utiliser.

Il est temps de construire notre application. J'ai organisé mes dossiers de projet comme ceci :

```
/src  /actions    ColorChangedAction.js  /components    AppNavigator.js    ChooseColorPage.js    MainPage.js  /reducers    AppReducer.js    ColorReducer.js    NavReducer.js  /state    Colors.js
```

Vous pouvez reproduire cette même structure depuis votre terminal :

```
cd redux-navigationmkdir src && cd srcmkdir actions && cd actions && touch ColorChangedAction.js && cd ..mkdir components && cd components && touch AppNavigator.js ChooseColorPage.js MainPage.js && cd ..mkdir reducers && cd reducers && touch AppReducer.js ColorReducer.js NavReducer.js && cd ..mkdir state && cd state && touch Colors.js && cd ..
```

Copiez-collez le code suivant dans le fichier `**Colors.js**` :

Ensuite, créez la `**MainPage**` avec une couleur de fond par défaut et un bouton :

Quelques notes :

* `**MainPage**` est un composant React plutôt qu'un [composant fonctionnel sans état](https://hackernoon.com/react-stateless-functional-components-nine-wins-you-might-have-overlooked-997b0d933dbc), car il devra accéder à l'état de l'application
* J'utilise `flex: 1, alignSelf: 'stretch'` pour faire en sorte que la vue conteneur s'étende à tout l'écran
* La couleur de la vue conteneur est définie dans la méthode `selectedColor()`, qui échantillonne `**RED**` de notre tableau `**COLORS**`, et retourne le code hexadécimal correspondant
* J'ai ajouté un gestionnaire `onChooseColor()` vide pour l'événement de pression du bouton. Nous ajouterons le corps de cette méthode plus tard.

Il est temps d'intégrer notre `**MainPage**` dans notre fichier racine `**App.js**`. Remplacez l'ancien contenu par ceci :

Le rafraîchissement du simulateur donne ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*l2JUVnmS4xNHkmQraqTigw.png)

Ce n'est pas joli, mais cela montre la couleur de fond et notre bouton comme prévu.

Voici un instantané de ce que nous avons construit jusqu'à présent : [Instantané du code GitHub 1](https://github.com/bizz84/redux-navigation-color-picker/releases/tag/01-main-page).

### Ajout de la navigation

Nous sommes maintenant prêts à ajouter de la navigation à notre application.

Pour ce faire, ouvrez le fichier `**AppNavigator.js**` et ajoutez ces contenus :

Ce code est emprunté à l'[Exemple Redux](https://github.com/react-navigation/react-navigation/tree/master/examples/ReduxExample) dans le projet [react-navigation](https://github.com/react-navigation/react-navigation).

Il définit un `StackNavigator`, utilisant notre `**MainPage**` comme écran principal.

Il configure également `AppWithNavigationState`, un conteneur de niveau supérieur contenant l'état de navigation. Si cela semble flou, ne vous inquiétez pas. C'est un code standard dans React Navigation et nous allons simplement l'utiliser pour l'instant pour faire avancer les choses.

Il est temps d'écrire le réducteur de navigation, qui contiendra l'état de navigation dans le magasin Redux. Ouvrez le fichier `**NavReducer.js**` et ajoutez ce qui suit :

Ce réducteur définit l'état de navigation initial de notre application. Encore une fois, du code standard.

Maintenant, ouvrons le fichier `**AppReducer.js**` et ajoutons ceci :

À mesure que notre application grandit, nous pourrions avoir besoin d'autres réducteurs aux côtés de notre `NavReducer`. Nous pouvons donc les combiner tous ensemble dans `AppReducer`.

Enfin, nous sommes en mesure de mettre à jour notre `**App.js**` pour utiliser toutes ces nouvelles fonctionnalités :

La méthode de rendu retourne un fournisseur avec le magasin redux créé, et contient notre composant de niveau supérieur. Encore une fois, il s'agit simplement du code standard nécessaire pour connecter les choses avec Redux.

Si nous rafraîchissons le simulateur, nous voyons maintenant une barre de navigation apparaître en haut :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PlVio74LmlGePNpXH6nNfA.png)

Après tout ce code, vous pourriez obtenir des erreurs sur votre simulateur si quelque chose manque. Si c'est le cas, utilisez cet instantané de code pour revenir sur la bonne voie : [Instantané du code GitHub 2](https://github.com/bizz84/redux-navigation-color-picker/releases/tag/02-add-navigation).

### Afficher la page de choix de couleur

Maintenant que nous avons une `**MainPage**` à l'intérieur d'un `StackNavigator`, nous sommes prêts à ajouter la `**ChooseColorPage**` afin de pouvoir naviguer vers elle.

Ouvrez le fichier `**ChooseColorPage.js**` et ajoutez le code suivant :

Quelques notes :

* Le code dans la méthode `**render()**` itère à travers chaque couleur et la mappe dans un `Button`. Les propriétés `title` et `color` sont définies.
* Lorsque le bouton est tapé, le gestionnaire `onSelectColor()` est appelé avec la clé de couleur appropriée.
* L'objet `navigation` est accessible via `props`. En fait, il est injecté dans tous les écrans de notre `**AppNavigator**`.
* L'appel de `this.props.navigation.goBack()` nous ramène à l'écran précédent dans le `**AppNavigator**`.
* À ce stade, `colorName` n'est pas encore utilisé pour définir un état.

Ensuite, nous devons faire en sorte que notre `**AppNavigator**` prenne conscience de la nouvelle page `**ChooseColorPage**`. Mettons-le à jour dans le fichier `**AppNavigator.js**` :

Enfin, ajoutez le code pour naviguer vers la `ChooseColorPage` lorsque le bouton `**Choose Color**` est tapé sur la `**MainPage**`.

Si nous rafraîchissons le simulateur maintenant et tapons sur `**Choose Color**`, l'application navigue vers le nouvel écran, qui montre trois boutons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*uIezJ7knSC2kFesSSdQBHA.png)

**Note** : L'appel de `navigation.navigate('ChooseColor')` fonctionne parce que nous avons nommé `**ChooseColor**` comme l'une des routes dans notre `**AppNavigator**`.

Taper sur le bouton de retour ou sur l'un des boutons de couleur nous ramène à la page principale, mais la couleur de fond ne change pas selon notre sélection.

Corrigeons cela dans la section suivante.

Encore une fois, si quelque chose ne fonctionne pas, vous pouvez obtenir mon instantané de code sauvegardé à ce stade : [Instantané du code GitHub 3](https://github.com/bizz84/redux-navigation-color-picker/releases/tag/03-add-choose-color-page).

### Gestion de l'état de l'application

Nous allons utiliser Redux pour définir la couleur de fond de notre `**MainPage**` comme état de notre application.

Pour ce faire, nous devons définir une action de changement de couleur et un réducteur de couleur.

Ouvrez le fichier `**ColorChangedAction.js**` et ajoutez ce qui suit :

Ensuite, ouvrez `**ColorReducer.js**` et ajoutez ceci :

Pour que ce réducteur soit utilisé, nous devons l'ajouter au `**AppReducer.js**` comme suit :

Maintenant, nous sommes prêts à appeler notre action `colorChanged` lorsque l'utilisateur sélectionne une couleur dans la `**ChooseColorPage**`. Voici le fichier `**ChooseColorPage.js**` mis à jour :

Notez que nous avons apporté trois modifications :

* Importé l'action `**colorChanged**` en haut
* Connecté avec `connect()` et `**mapStateToProps**`
* Utilisé à l'intérieur de `onSelectColor(colorName)`

À ce stade, nous pouvons rafraîchir le simulateur et exécuter. Si nous choisissons une couleur différente, la couleur de fond de la `**MainPage**` ne change toujours pas.

C'est parce que nous n'avons pas dit à `**MainPage**` d'utiliser le nouvel état.

Facile à corriger. Ouvrez `**MainPage.js**` et ajoutez le code requis :

Quelques notes :

* `**mapStateToProps**` définit maintenant le `colorName` à partir de l'état dans le `**ColorReducer**`
* Celui-ci est ensuite accessible via l'objet `props` et peut être utilisé à l'intérieur de `selectedColor()`
* N'oubliez pas d'importer `{ connect }` depuis 'react-redux' en haut

Si nous essayons à nouveau l'application dans le simulateur, nous sommes maintenant en mesure de changer la couleur de fond. ?

Instantané mis à jour : [Instantané du code GitHub 4](https://github.com/bizz84/redux-navigation-color-picker/releases/tag/04-color-application-state).

### Bonus : Présentation modale de la page de sélection de couleur

Lorsque nous tapons sur le bouton `**Choose Color**` dans la `**MainPage**`, la `**ChooseColorPage**` glisse de la droite. Il s'agit de l'animation de navigation par défaut à l'intérieur de `**StackNavigator**`.

Et si nous voulions présenter la `**ChooseColorPage**` de manière modale à la place ?

Cela se fait facilement en modifiant la configuration de notre `**AppNavigator**` comme suit :

Notez l'ajout de `**navigationOptions**` avec une propriété `**headerLeft: null**` à l'intérieur de `**ChooseColor**`, et le paramètre `**mode: 'modal'**`.

Si nous essayons cela sur le simulateur, la `**ChooseColorPage**` glisse maintenant de bas en haut.

React Navigation est très personnalisable. Je recommande de passer du temps à lire la documentation [du projet](https://github.com/react-navigation/react-navigation), pour apprendre tout ce que vous pouvez faire avec.

### Conclusion

Nous avons appris comment :

* Configurer et utiliser Expo pour exécuter une application mobile sur le simulateur
* Construire une application avec deux pages différentes et naviguer entre elles avec React Navigation
* Utiliser des actions et des réducteurs pour modifier l'état à partir d'un écran et l'utiliser pour mettre à jour l'UI sur un autre

Vous pouvez trouver le code source complet [sur GitHub ici](https://github.com/bizz84/redux-navigation-color-picker).

J'ai également partagé le projet publiquement [sur Expo ici](https://expo.io/@bizz84/redux-navigation).

J'espère que vous avez apprécié ce tutoriel. Une bonne prochaine étape serait de consulter les exemples officiels de [React Navigation](https://github.com/react-navigation/react-navigation/tree/master/examples), ainsi que les autres [tutoriels de la communauté](https://github.com/react-navigation/react-navigation#community-contributions).

Les commentaires et les retours sont appréciés. ?

Et si vous ???, je pourrais même faire un tutoriel vidéo étape par étape. ?

**À propos de moi** : Je suis un développeur iOS freelance, jonglant entre le travail contractuel, l'open source, les projets parallèles et le blogging.

Je suis [@biz84](https://twitter.com/biz84) sur Twitter. Vous pouvez également voir ma page [GitHub](https://github.com/bizz84). Retours, tweets, gifs drôles, tout est bienvenu ! Mon préféré ? Beaucoup de ???. Oh, et des cookies au chocolat.