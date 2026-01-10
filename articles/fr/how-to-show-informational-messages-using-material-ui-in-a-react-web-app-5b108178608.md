---
title: Comment afficher des messages in-app en utilisant Material-UI dans une application
  web React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-27T23:33:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-show-informational-messages-using-material-ui-in-a-react-web-app-5b108178608
coverImage: https://cdn-media-1.freecodecamp.org/images/1*awO-09f5MGtVvnkbVLoBDA.png
tags:
- name: Material Design
  slug: material-design
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Comment afficher des messages in-app en utilisant Material-UI dans une
  application web React
seo_desc: 'By Kelly Burke

  In some situations, your web app needs to show an informational message to tell
  users whether an event was successful or not. For example, a “Success” message after
  a user clicks a button and successfully completes some action.

  In this...'
---

Par Kelly Burke

Dans certaines situations, votre application web doit afficher un message informatif pour indiquer aux utilisateurs si un événement a réussi ou non. Par exemple, un message « Succès » après qu'un utilisateur a cliqué sur un bouton et a réussi à effectuer une action.

Dans ce tutoriel, je vais vous montrer comment créer un composant simple pour des messages informatifs in-app avec React et Material-UI. Nous l'appellerons un composant `Notifier`.

Voici les principales sections de ce tutoriel :

* Installation
* Composant Notifier
* Importer le composant Notifier dans la page Index
* Test

Si vous trouvez cet article utile, envisagez de mettre une étoile à notre [dépôt Github](https://github.com/builderbook/builderbook) et de consulter notre [livre](https://builderbook.org/book) où nous couvrons ce sujet et bien d'autres en détail.

### **Installation**

Pour ce tutoriel, j'ai créé une simple application web pour que vous puissiez suivre. Nous utiliserons le code situé dans le dossier [tutorials/4-start](https://github.com/builderbook/builderbook/tree/master/tutorials/4-start) de notre [dépôt builderbook](https://github.com/builderbook/builderbook).

Si vous n'avez pas le temps d'exécuter l'application localement, j'ai déployé cette application exemple [ici](https://notifier.builderbook.org).

Pour exécuter l'application localement :

* Clonez le dépôt builderbook sur votre machine locale avec :

```
git clone git@github.com:builderbook/builderbook.git
```

* Dans le dossier `4-start`, exécutez `yarn` ou `npm install` pour installer tous les packages listés dans `package.json`.
* Exécutez `yarn dev` pour démarrer l'application.

#### Page Index

Sur votre navigateur, allez à [http://localhost:3000](http://localhost:3000). C'est notre page `Index`, qui a la route `/`. Next.js fournit un routage automatique pour les pages situées dans un dossier `/pages`. Le nom de chaque fichier de page devient la route de cette page.

Notre page `Index` est un simple composant de page qui rend un formulaire, une entrée et un bouton (plus d'explications ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/1*I50gTzdSn6aPSI3JYk9Hqw.png)

Voici le code de notre page `Index` à `pages/index.js` :

Quelques notes :

* Nous aurions pu définir cette page comme un composant fonctionnel sans état, car elle n'a pas d'état, de hooks de cycle de vie ou de refs ([lire plus](https://www.jstwister.com/post/react-stateless-functional-components-best-practices/) sur quand utiliser les composants fonctionnels sans état versus les classes ES6 de React). Vous verrez cet avertissement Eslint : `Component should be written as a pure function`. Cependant, la page `Index` **finale** que nous écrivons dans ce tutoriel aura une ref. Par conséquent, nous avons écrit cette page `Index` **initiale** comme un enfant de [classe ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) en utilisant [extends](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends).
* Nous avons importé [Head](https://github.com/zeit/next.js/#populating-head) de Next.js afin de personnaliser l'élément `<Head>` de la page. À l'intérieur de `<Head>`, nous avons ajouté un `<title>` de page et une description `<meta>` pour un indexation correcte par les robots des moteurs de recherche (bon pour le SEO). Le texte à l'intérieur de `<title>` s'affiche sur votre onglet de navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QtsMfsiewcSAb5AOE8LvsA.png)

* Nous avons utilisé les composants [TextField](https://material-ui-next.com/api/text-field/#textfield) et [Button](https://material-ui-next.com/demos/buttons/#buttons) de Material-UI, qui se rendent respectivement en éléments HTML `<input>` et `<button>`.
* Nous avons enveloppé notre page avec un composant d'ordre supérieur `withLayout`. Notre application utilise Next.js, et `withLayout` garantit que le rendu côté serveur fonctionne correctement pour Material-UI à l'intérieur de notre application React-Next. `withLayout` ajoute également notre composant `Header` (situé à `components/Header.js`) à chaque page que `withLayout` enveloppe. Le rendu côté serveur n'est pas nécessaire pour Material-UI ou React, mais c'est une fonctionnalité principale de Next.js. Nous avons discuté du [rendu côté serveur vs. côté client](https://hackernoon.com/server-side-vs-client-side-rendering-in-react-apps-443efd6f2e87) dans les applications React dans un autre tutoriel.

Nous avons terminé la description de notre page `Index` initiale. Maintenant, discutons du composant `Notifier` que nous importerons plus tard dans la page `Index` pour afficher des messages informatifs à nos utilisateurs d'application web.

### Composant Notifier

Commençons par définir le composant `Notifier`. Nous définissons `Notifier` comme un `React.Component` au lieu d'une fonction sans état, car `Notifier` aura un état, une méthode de cycle de vie et quelques fonctions de gestion d'événements.

Pour nos messages informatifs, nous utiliserons le [Snackbar](https://material-ui-next.com/demos/snackbars/#snackbars) de Material-UI. Consultez les [exemples](https://material-ui-next.com/demos/snackbars/#snackbars) d'utilisation de Snackbar sur le site officiel de Material-UI.

Voici un aperçu de haut niveau de notre composant `Notifier` :

Créez un fichier `Notifier.js` à l'intérieur du dossier `/components` de `4-start`. Ajoutez l'aperçu de haut niveau ci-dessus à ce fichier. Ci-dessous, nous remplacerons les commentaires numérotés par du code.

1. Nous utiliserons les props `open` et `message` du Snackbar de Material-UI pour l'état de notre `Notifier`. Consultez la [liste complète des props](https://material-ui-next.com/api/snackbar/#props) pour Snackbar.

Initialement, notre `Notifier` doit être dans un état fermé avec une chaîne vide comme message. Nous définissons l'état initial du `Notifier` comme suit :

2. Maintenant, écrivons une fonction qui met à jour l'état du composant Notifier. La fonction changera la valeur de la prop `open` à `true` et définira la valeur de la prop `message` à une chaîne non vide. Appelons cette fonction `openSnackbar()`.

Avant de pouvoir exécuter `openSnackbar()`, notre composant `Notifier` doit être monté dans le DOM. Ainsi, nous plaçons la fonction `openSnackbar()` dans une méthode de cycle de vie `componentDidMount` qui s'exécute juste après que le composant `Notifier` est monté dans le DOM.

Afin d'accéder à la fonction `openSnackbar()` **n'importe où** dans notre application, nous devons définir sa valeur à une autre fonction qui est disponible en dehors du composant `Notifier`. Par conséquent, nous écrivons `let openSnackbarFn` au-dessus de `class Notifier extends React.Component`.

En mettant ces morceaux ensemble :

Maintenant, définissons la fonction `openSnackbar()`. Cette fonction mettra à jour les propriétés `open` et `message` de l'état de notre `Notifier`. Une fois l'état mis à jour, le composant `Notifier` sera réaffiché pour afficher un message (`open:true` affiche le Snackbar, et `message:message` définit le message).

À l'intérieur de `this.setState`, nous aurions pu écrire `message` comme `message:message`. Au lieu de cela, nous avons utilisé la syntaxe abrégée ES6 (imposée par Eslint) pour rendre le code plus concis.

3. Lorsque l'utilisateur clique en dehors de la zone Snackbar, le Snackbar doit se fermer. La prop `onClose` du Snackbar est responsable de ce comportement. Écrivons une fonction appelée `handleSnackbarClose()` qui définit `open` à `false` et `message` à une chaîne vide.

4. Enfin, écrivons le code pour que notre composant `Notifier` affiche le composant Snackbar avec toutes les props nécessaires.

En plus des props `message`, `onClose` et `open` décrites ci-dessus, nous ajouterons les props suivantes à notre composant Snackbar :

* `anchorOrigin` : spécifie l'emplacement du Snackbar
* `autoHideDuration` : spécifie la durée du Snackbar en millisecondes
* `SnackbarContentProps` : lie le Snackbar à un élément à l'intérieur du DOM qui contient `message` ; dans notre cas, l'élément a l'id `snackbar-message-id`, et le Snackbar affichera le texte de cet élément.

Voici la méthode `render()` de notre composant `Notifier` :

Dans l'élément `<span>`, nous aurions pu écrire `message={this.state.message}`, mais au lieu de cela, nous avons écrit `dangerouslySetInnerHTML={{ __html: this.state.message }}`. Cela nous permet d'ajouter du code HTML à la prop `message` du Snackbar. Par exemple, vous pouvez vouloir afficher un hyperlien aux utilisateurs. [Lisez plus](https://reactjs.org/docs/dom-elements.html#dangerouslysetinnerhtml) sur l'utilisation de `dangerouslySetInnerHTML` dans React.

Après avoir assemblé le code des étapes 1 à 4, voici notre composant `Notifier` final :

Note importante : remarquez comment nous avons exporté notre fonction `openSnackbar()` en plus du composant `Notifier`. Nous importerons **à la fois** `openSnackbar()` et `Notifier` dans notre page `Index`.

### Importer le composant Notifier dans la page Index

Retour à notre page `Index`, où nous importerons notre composant `Notifier` et la fonction `openSnackbar()`.

Sans déclencher la fonction `openSnackbar()`, notre composant `Notifier` restera toujours dans son état initial fermé avec une chaîne vide comme message. Nous devons exécuter `openSnackbar()` après qu'un utilisateur a soumis le formulaire en cliquant sur le bouton de notre page `Index`. Définissons une fonction `showNotifier()` qui fait exactement cela.

#### Fonction showNotifier

Nous appellerons `showNotifier()` à l'intérieur de l'élément `<form>`. Nous ferons en sorte que `showNotifier()` s'exécute lorsque l'utilisateur entre un nombre dans le formulaire et clique sur le bouton « Submit ».

Voici le `<form>` actuel sur notre page `Index` :

Apportons deux modifications :

1. Pour appeler `showNotifier()` lorsque le formulaire est soumis, nous utilisons l'événement [onsubmit](https://www.w3schools.com/jsref/event_onsubmit.asp) de JavaScript :

2. Un utilisateur entrera un nombre à l'intérieur de `TextField`. Pour que notre fonction `showNotifier()` puisse accéder à la valeur de `TextField`, nous ajoutons l'attribut [ref](https://reactjs.org/docs/refs-and-the-dom.html#adding-a-ref-to-a-dom-element) de React à `TextField`.

Il existe deux façons d'obtenir la valeur de `TextField` : avec `this.state` et avec `ref`. Nous avons choisi `ref`, car `this.state` est plus concis. Voici une [explication](https://stackoverflow.com/questions/36683770/react-how-to-get-the-value-of-an-input-field?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa) de l'écriture avec `this.state`, et voici [plus d'informations](https://reactjs.org/docs/refs-and-the-dom.html#callback-refs) sur l'utilisation de `ref` dans React.

Maintenant, définissons la fonction `showNotifier()`. Voici l'aperçu de haut niveau pour `showNotifier()` :

Ci-dessous, nous écrivons le code pour chacun des trois commentaires ci-dessus.

1. Nous définissons `answer` comme :

Cette ligne de code dit que SI `answerInput` existe (ce qui signifie que l'élément `<input>` est ajouté au DOM), ALORS `answer` est égal à la valeur de `answerInput`, qui est accessible avec `answerInput.value`.

SI `answerInput` n'existe pas, ALORS toute la condition entre parenthèses est fausse et `answer` est égal à `null`.

2. Si un utilisateur ne saisit pas de réponse dans notre formulaire mais clique sur le bouton « Submit », nous afficherons ce message : `Champ vide. Entrez un nombre.`

3. Si un utilisateur entre 4 et clique sur le bouton « Submit », alors notre fonction `openSnackbar()` s'exécutera et affichera ce message : `Bonne réponse !`. Sinon, elle affichera `Mauvaise réponse.`

Nous utilisons `parseInt(answer, 10)` pour analyser `answer`, qui est une chaîne, et retourner un entier. Le paramètre `10` spécifie que l'entier est au format décimal.

Assemblons le code des étapes 1 à 3 ci-dessus pour notre fonction `showNotifier`. Nous placerons le code juste sous la ligne `class Index extends React.Component` :

Vous remarquerez que nous avons ajouté une ligne `event.preventDefault();`. Cela empêchera notre élément `<form>` de son comportement par défaut d'envoyer les données du formulaire à un serveur.

Maintenant, nous avons tout le code pour notre page `Index` finale :

### Test

Testons que notre `Notifier` fonctionne comme prévu. Exécutez l'application localement avec `yarn dev` et naviguez vers [http://localhost:3000](http://localhost:3000). Si vous n'exécutez pas l'application, allez à celle que j'ai déployée : [https://notifier.builderbook.org](https://notifier.builderbook.org).

Tout d'abord, cliquez sur « Submit » sans ajouter quoi que ce soit dans le champ de texte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tFZ2EbE513_ACJqNMPiHYw.png)

Ensuite, ajoutez le nombre 4 et cliquez sur « Submit ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*ov1Nt7TI_VcHWOgn-zb9WQ.png)

Maintenant, ajoutez un autre nombre et cliquez sur « Submit ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*61lDH0rzRRsReG4X36GV8A.png)

Rappelez-vous que nous avons écrit du code pour fermer le Snackbar lorsque l'utilisateur clique ailleurs (nous avons écrit une fonction `handleSnackbarClose()` et l'avons passée à la prop `onClose` du Snackbar). Après avoir vu le Snackbar, cliquez n'importe où ailleurs que sur le Snackbar lui-même sur votre écran. Le Snackbar devrait se fermer immédiatement.

Une belle fonctionnalité de Material-UI est l'optimisation mobile. Nous n'avons pas à écrire de code supplémentaire pour que notre message informatif ait l'air bien sur les appareils mobiles. Voyez par vous-même en allant dans les DevTools de Chrome et en changeant la vue de bureau à mobile. Notre message apparaît en haut de l'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3t4ur9VU3LOw2ytbKHrvAQ.png)

Hourra ! Vous avez ajouté avec succès un message informatif in-app à une application web React ! Votre code final devrait correspondre au code dans le dossier [tutorials/4-end](https://github.com/builderbook/builderbook/tree/master/tutorials/4-end) de notre [dépôt builderbook](https://github.com/builderbook/builderbook).

#### Personnaliser le composant Notifier

Maintenant que vous avez un composant `Notifier` fonctionnel, voyons comment nous pouvons modifier l'UX en changeant les props du composant SnackBar de Material-UI. Voici la [liste complète](https://material-ui-next.com/api/snackbar/#props) des props que vous pouvez utiliser.

Tout d'abord, changeons la durée du Snackbar. Dans votre composant `Notifier`, trouvez la prop `autoHideDuration`. Changez sa valeur de `3000` à `1000` et comparez. Vous verrez qu'à `1000`, le Snackbar se ferme plus rapidement.

Deuxièmement, changeons la position du Snackbar. Trouvez la prop `anchorOrigin` et changez ses valeurs de `top` et `right` à `bottom` et `left`, respectivement. Vérifiez où le Snackbar apparaît maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*9ANw1zxyhHSQBOECUR_G2Q.png)

Enfin, faisons en sorte que le `message` du Snackbar inclue un hyperlien. Rappelez-vous que nous avons ajouté `dangerouslySetInnerHTML={{ __html: this.state.message }}` à notre prop `message` dans le Snackbar afin que nous puissions écrire du HTML à l'intérieur.

Changez le code pour nos messages `Bonne réponse !` et `Mauvaise réponse.` comme ceci :

Maintenant, les utilisateurs verront les messages ci-dessous. Remarquez les hyperliens bleus foncés pour le texte à l'intérieur des balises `<a>`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fGzjKrwd2noPg34wQUOTCw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*lYm3vmPuDAx4klVt33BwWw.png)

Si vous apprenez à construire des applications web avec JavaScript, consultez notre [dépôt Github](https://github.com/builderbook/builderbook) et notre [livre](https://builderbook.org/book), où nous couvrons ce sujet et bien d'autres en détail.

Pour recevoir des mises à jour par email sur nos tutoriels, abonnez-vous [ici](https://builderbook.org/tutorials).