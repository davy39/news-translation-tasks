---
title: 'Gestion de l''état dans React : Quatre approches immuables à considérer'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-13T14:54:29.000Z'
originalURL: https://freecodecamp.org/news/handling-state-in-react-four-immutable-approaches-to-consider-d1f5c00249d5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OEjZQSVvWnGgUF-dTrTS_w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: Web Development
  slug: web-development
seo_title: 'Gestion de l''état dans React : Quatre approches immuables à considérer'
seo_desc: 'By Cory House

  Perhaps the most common point of confusion in React today: state.

  Imagine you have a form for editing a user. It’s common to create a single change
  handler to handle changes to all form fields. It may look something like this:

  updateSta...'
---

Par Cory House

Peut-être le point de confusion le plus courant dans React aujourd'hui : l'état.

Imaginez que vous avez un formulaire pour éditer un utilisateur. Il est courant de créer un seul gestionnaire de changement pour gérer les modifications de tous les champs du formulaire. Cela peut ressembler à ceci :

```js
updateState(event) {
 const {name, value} = event.target;
 let user = this.state.user; // ceci est une référence, pas une copie...
 user[name] = value; // donc cela mute l'état ?
 return this.setState({user});
}
```

Le problème est à la ligne 4. La ligne 4 mute effectivement l'état car la variable user est une _référence_ à l'état. L'état de React doit être traité comme immuable.

D'après la [documentation de React](https://facebook.github.io/react/docs/react-component.html#state) :

> Ne mutez jamais `this.state` directement, car l'appel à `setState()` ensuite peut remplacer la mutation que vous avez faite. Traitez `this.state` comme s'il était immuable.

Pourquoi ?

1. setState regroupe les travaux en arrière-plan. Cela signifie qu'une mutation manuelle de l'état peut être écrasée lorsque setState est traité.
2. Si vous déclarez une méthode shouldComponentUpdate, vous ne pouvez pas utiliser une vérification d'égalité === à l'intérieur car _la référence de l'objet ne changera pas_. Ainsi, l'approche ci-dessus a également un impact potentiel sur les performances.

**Conclusion** : L'exemple ci-dessus fonctionne souvent correctement, mais pour éviter les cas limites, traitez l'état comme immuable.

Voici quatre façons de traiter l'état comme immuable :

### Approche #1 : Object.assign

[Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) crée une copie d'un objet. Le premier paramètre est la cible, puis vous spécifiez un ou plusieurs paramètres pour les propriétés que vous souhaitez ajouter. Ainsi, la correction de l'exemple ci-dessus implique un simple changement à la ligne 3 :

```js
updateState(event) {
 const {name, value} = event.target;
 let user = Object.assign({}, this.state.user);
 user[name] = value;
 return this.setState({user});
}
```

À la ligne 3, je dis « Créez un nouvel objet vide et ajoutez toutes les propriétés de this.state.user ». Cela crée une copie séparée de l'objet utilisateur qui est stocké dans l'état. Maintenant, je peux muter l'objet utilisateur à la ligne 4 — c'est un objet complètement séparé de l'objet dans l'état.

Assurez-vous de polyfill Object.assign puisqu'il est [non supporté dans IE](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) et [non transpilé par Babel](https://babeljs.io/docs/usage/polyfill/). Quatre options à considérer :

1. [object-assign](https://www.npmjs.com/package/object-assign)
2. [Les docs MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)
3. [Babel Polyfill](https://babeljs.io/docs/usage/polyfill/)
4. [Polyfill.io](https://polyfill.io/v2/docs/features/#Object_assign)

### Approche #2 : Object Spread

Object spread est actuellement une [fonctionnalité de stade 3](https://github.com/tc39/proposal-object-rest-spread), et peut être [transpilé par Babel](http://babeljs.io/docs/plugins/transform-object-rest-spread/#example). Cette approche est plus concise :

```js
updateState(event) {
 const {name, value} = event.target;
 let user = {...this.state.user, [name]: value};
 this.setState({user});
}
```

À la ligne 3, je dis « Utilisez toutes les propriétés de this.state.user pour créer un nouvel objet, puis définissez la propriété représentée par [name] à une nouvelle valeur passée sur event.target.value ». Ainsi, cette approche fonctionne de manière similaire à l'approche Object.assign, mais a deux avantages :

1. Aucun polyfill requis, puisque Babel peut transpiler
2. Plus concis

Vous pouvez même utiliser la destructuration et l'inlining pour en faire une ligne :

```js
updateState({target}) {
 this.setState({user: {...this.state.user, [target.name]: target.value}});
}
```

Je destructure l'événement dans la signature de la méthode pour obtenir une référence à event.target. Ensuite, je déclare que l'état doit être défini sur une copie de this.state.user avec la propriété pertinente définie sur une nouvelle valeur. J'aime la concision de cela. C'est actuellement mon approche préférée pour écrire des gestionnaires de changement. ?

Ces deux approches ci-dessus sont les moyens les plus courants et simples de gérer l'état immuable. Vous voulez plus de puissance ? Consultez les deux autres options ci-dessous.

### Approche #3 : Immutability Helper

[Immutability-helper](https://github.com/kolodny/immutability-helper) est une bibliothèque pratique pour muter une copie de données sans changer la source. Cette bibliothèque est suggérée dans la [documentation de React](https://facebook.github.io/react/docs/update.html).

```js
// Import en haut :
import update from 'immutability-helper';

updateState({target}) {
 let user = update(this.state.user, {$merge: {[target.name]: target.value}});
 this.setState({user});
}
```

À la ligne 5, j'appelle merge, qui est [l'une des nombreuses commandes](https://github.com/kolodny/immutability-helper#available-commands) fournies par immutability-helper. Comme Object.assign, je lui passe l'objet cible comme premier paramètre, puis spécifie la propriété que je souhaite fusionner.

Il y a beaucoup plus à immutability helper que cela. Il utilise une syntaxe inspirée du langage de requête de MongoDB et offre une [variété de moyens puissants de travailler avec des données immuables](https://github.com/kolodny/immutability-helper#available-commands).

### Approche #4 : Immutable.js

Vous voulez appliquer l'immuabilité de manière programmatique ? Considérez [immutable.js](https://facebook.github.io/immutable-js/). Cette bibliothèque fournit des structures de données immuables.

Voici un exemple, utilisant une map immuable :

```js

// En haut, importer immutable
import { Map } from 'immutable';

// Plus tard, dans le constructeur...
this.state = {
  // Créez une map immuable dans l'état en utilisant immutable.js
  user: Map({ firstName: 'Cory', lastName: 'House'})
};

updateState({target}) {
 // cette ligne retourne un nouvel objet utilisateur en supposant qu'une map immuable est stockée dans l'état.
 let user = this.state.user.set(target.name, target.value);
 this.setState({user});
}
```

Il y a trois étapes de base ci-dessus :

1. Importer immutable.
2. Définir l'état sur une map immuable dans le constructeur
3. Utiliser la méthode set dans le gestionnaire de changement pour créer une nouvelle copie de l'utilisateur.

La beauté de immutable.js : **Si vous essayez de muter l'état directement, cela échouera**. Avec les autres approches ci-dessus, il est facile d'oublier, et React ne vous avertira pas lorsque vous mutez l'état directement.

Les inconvénients de immutable ?

1. **Gonflement**. Immutable.js ajoute 57K minifiés à votre bundle. Considérant que des bibliothèques comme [Preact peuvent remplacer React en seulement 3K](https://preactjs.com), c'est difficile à accepter.
2. **Syntaxe**. Vous devez référencer les propriétés des objets via des chaînes de caractères et des appels de méthode au lieu de directement. Je préfère user.name plutôt que user.get('name').
3. **YATTL** (Yet another thing to learn) — Toute personne rejoignant votre équipe doit apprendre une autre API pour obtenir et définir des données, ainsi qu'un nouvel ensemble de types de données.

Quelques autres alternatives intéressantes à considérer :

* [seamless-immutable](https://github.com/rtfeldman/seamless-immutable)
* [react-copy-write](https://github.com/aweary/react-copy-write)

### Avertissement : Attention aux objets imbriqués !

Les options #1 et #2 ci-dessus (Object.assign et Object spread) ne font qu'un clonage _superficiel_. Donc si votre objet contient des objets imbriqués, **ces objets imbriqués seront copiés par référence au lieu de par valeur**. Donc si vous changez l'objet imbriqué, vous muterez l'objet original. ?

Soyez précis sur ce que vous clonez. Ne clonez pas tout. Clonez les objets qui ont changé. Immutability-helper (mentionné ci-dessus) facilite cela. Tout comme les alternatives comme [immer](https://github.com/mweststrate/immer), [updeep](https://github.com/substantial/updeep), ou une [longue liste d'alternatives](https://github.com/markerikson/redux-ecosystem-links/blob/master/immutable-data.md#immutable-update-utilities).

Vous pourriez être tenté d'utiliser des outils de fusion profonde comme [clone-deep](https://www.npmjs.com/package/clone-deep), ou [lodash.merge](https://lodash.com/docs/#merge), mais **évitez de cloner profondément de manière aveugle**.

Voici pourquoi :

1. Le clonage profond est coûteux.
2. Le clonage profond est généralement gaspilleur (au lieu de cela, ne clonez que ce qui a réellement changé)
3. Le clonage profond provoque des rendus inutiles puisque React pense que tout a changé alors qu'en fait peut-être seulement un objet enfant spécifique a changé.

Merci à Dan Abramov pour les suggestions que j'ai mentionnées ci-dessus :

%[https://twitter.com/dan_abramov/status/988546679115800577?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E988546679115800577%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fdan_abramov%2Fstatus%2F988546679115800577%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F906557353549598720%25252FoapgW_Fp_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

### Dernier conseil : Considérez l'utilisation de setState fonctionnel

Un autre problème peut vous mordre :

> setState() ne mute pas immédiatement this.state mais crée une transition d'état en attente. L'accès à this.state après l'appel de cette méthode peut potentiellement retourner la valeur existante.

Puisque les appels à setState sont regroupés, un code comme celui-ci conduit à un bug :

```js
updateState({target}) {
 this.setState({user: {...this.state.user, [target.name]: target.value}});
 doSomething(this.state.user) // Oups, setState planifie simplement un changement d'état, donc this.state.user peut encore avoir l'ancienne valeur
}
```

Si vous voulez exécuter du code après qu'un appel à setState ait été complété, utilisez la forme de rappel de setState :

```js
updateState({target}) {
   this.setState((prevState) => {
     const updatedUser = {...prevState.user, [target.name]: target.value}; // utilisez la valeur précédente dans l'état pour construire un nouvel état...
     
     return { user: updatedUser }; // Et ce que je retourne ici sera défini comme le nouvel état
   }, () => this.doSomething(this.state.user); // Maintenant, je peux utiliser en toute sécurité le nouvel état que j'ai créé pour appeler d'autres fonctions...
     );
 }
```

### Mon avis

J'admire la simplicité et la légèreté de l'option #2 ci-dessus : Object spread. Elle ne nécessite pas de polyfill ou de bibliothèque séparée, je peux déclarer un gestionnaire de changement en une seule ligne, et je peux être précis sur ce qui a changé. ? Travailler avec des structures d'objets imbriqués ? Je préfère actuellement [Immer.](https://github.com/mweststrate/immer)

Avez-vous d'autres façons que vous aimez pour gérer l'état dans React ? N'hésitez pas à commenter !

### Vous cherchez plus sur React ? F52E

J'ai écrit [plusieurs cours sur React et JavaScript](http://bit.ly/psauthorpageimmutablepost) sur Pluralsight ([essai gratuit](http://bit.ly/pstrialimmutablepost)). Mon dernier, « [Création de composants React réutilisables](http://bit.ly/psreactcomponentsimmutablepost) » vient d'être publié ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*BkPc3o2d2bz0YEO7z5C2JQ.png)

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), architecte logiciel chez VinSolutions, un MVP Microsoft, et forme des développeurs logiciels à l'international sur des pratiques logicielles comme le développement front-end et le code propre. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).