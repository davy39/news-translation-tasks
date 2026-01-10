---
title: 8 décisions clés pour les composants React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-02T13:20:17.000Z'
originalURL: https://freecodecamp.org/news/8-key-react-component-decisions-cc965db11594
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XgHYXVXoyziBKd7Or5IliQ.jpeg
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
seo_title: 8 décisions clés pour les composants React
seo_desc: 'By Cory House

  Standardize your React development with these key decisions

  React was open-sourced in 2013. Since then, it has evolved. As you search the web,
  you’ll stumble across old posts with dated approaches. So, here are eight key decisions
  your ...'
---

Par Cory House

#### Standardisez votre développement React avec ces décisions clés

React a été open-sourcé en 2013. Depuis, il a évolué. En cherchant sur le web, vous tomberez sur des anciens posts avec des approches dépassées. Voici donc huit décisions clés que votre équipe doit prendre lors de l'écriture de composants React aujourd'hui.

### Décision 1 : Environnement de développement

Avant d'écrire votre premier composant, votre équipe doit se mettre d'accord sur un environnement de développement. Beaucoup d'options...

%[https://twitter.com/housecor/status/913382440911212545?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fhousecor%2Fstatus%2F913382440911212545%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F650743198348808192%25252FLT6SeOJr_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Bien sûr, vous pouvez [construire un environnement de développement JS à partir de zéro](https://www.pluralsight.com/courses/javascript-development-environment). 25 % des développeurs React font exactement cela. Mon équipe actuelle utilise un fork de create-react-app avec des fonctionnalités supplémentaires telles qu'une [API mock réaliste qui supporte CRUD](https://medium.freecodecamp.org/rapid-development-via-mock-apis-e559087be066), une [bibliothèque de composants réutilisables](https://www.pluralsight.com/courses/react-creating-reusable-components), et des améliorations de linting (nous lintons également nos fichiers de test, que create-react-app ignore). J'apprécie create-react-app, mais [cet outil vous aidera à comparer de nombreuses alternatives convaincantes](http://andrewhfarmer.com/starter-project/). Vous voulez rendre sur le serveur ? Consultez [Gatsby](http://gatsbyjs.org) ou [Next.js](https://github.com/zeit/next.js/). Vous pouvez même envisager d'utiliser un éditeur en ligne comme [CodeSandbox](https://codesandbox.io).

### Décision 2 : Types

Vous pouvez ignorer les types, utiliser [prop-types](https://reactjs.org/docs/typechecking-with-proptypes.html), utiliser [Flow](https://flow.org), ou utiliser [TypeScript](https://www.typescriptlang.org). Notez que prop-types a été extrait dans une [bibliothèque séparée](https://www.npmjs.com/package/prop-types) dans React 15.5, donc les anciens posts montreront des imports qui ne fonctionnent plus.

La communauté reste divisée sur ce sujet :

%[https://twitter.com/housecor/status/911673327240073216?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fhousecor%2Fstatus%2F911673327240073216%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F650743198348808192%25252FLT6SeOJr_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Je préfère prop-types car je trouve qu'il offre une sécurité de type suffisante dans les composants React avec peu de friction. En utilisant la combinaison de Babel, [Jest tests](https://facebook.github.io/jest/), [ESLint](http://www.eslint.org), et prop-types, je vois rarement des problèmes de type à l'exécution.

### Décision 3 : createClass vs ES Class

React.createClass était l'API originale, mais dans la version 15.5, elle a été dépréciée. Certains pensent [que nous avons sauté le pas en passant aux classes ES](https://medium.com/dailyjs/we-jumped-the-gun-moving-react-components-to-es2015-class-syntax-2b2bb6f35cb3). Quoi qu'il en soit, le style createClass a été retiré du cœur de React et [relégué à une seule page appelée "React sans ES6" dans la documentation React](https://reactjs.org/docs/react-without-es6.html). Il est donc clair : les classes ES sont l'avenir. Vous pouvez facilement convertir de createClass à ES Classes en utilisant [react-codemod](https://github.com/reactjs/react-codemod).

### Décision 4 : Class vs Functional

Vous pouvez déclarer des composants React via une classe ou une fonction. Les classes sont utiles lorsque vous avez besoin de refs et de méthodes de cycle de vie. Voici [9 raisons d'envisager l'utilisation de fonctions lorsque c'est possible](https://hackernoon.com/react-stateless-functional-components-nine-wins-you-might-have-overlooked-997b0d933dbc). Mais il est également intéressant de noter [qu'il y a quelques inconvénients aux composants fonctionnels](https://medium.freecodecamp.org/7-reasons-to-outlaw-reacts-functional-components-ff5b5ae09b7c).

### Décision 5 : State

Vous pouvez utiliser l'état des composants React standard. C'est suffisant. [L'élévation de l'état](https://reactjs.org/docs/lifting-state-up.html) s'adapte bien. Ou, vous pouvez apprécier Redux ou MobX :

%[https://twitter.com/AdamRackis/status/845738250186768385?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fadamrackis%2Fstatus%2F845738250186768385%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F578245151677501440%25252F7RXysXXe_400x400.jpeg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

[Je suis fan de Redux](https://www.pluralsight.com/courses/react-redux-react-router-es6), mais j'utilise souvent React standard car c'est plus simple. Dans mon rôle actuel, nous avons livré environ une douzaine d'applications React, et nous avons décidé que Redux valait la peine pour deux d'entre elles. Je préfère livrer de nombreuses petites applications autonomes plutôt qu'une seule grande application.

Sur une note connexe, si vous êtes intéressé par l'état immutable, il existe au moins [4 façons de garder votre état immutable](https://medium.com/@housecor/handling-state-in-react-four-immutable-approaches-to-consider-d1f5c00249d5).

### Décision 6 : Binding

Il existe au moins [une demi-douzaine de façons de gérer le binding](https://medium.freecodecamp.org/react-binding-patterns-5-approaches-for-handling-this-92c651b5af56) dans les composants React. En défense de React, cela est principalement dû au fait que le JS moderne offre de nombreuses façons de gérer le binding. Vous pouvez binder dans le constructeur, binder dans le render, utiliser une fonction fléchée dans le render, utiliser une propriété de classe, ou utiliser des décorateurs. [Voir les commentaires de ce post](https://medium.freecodecamp.org/react-binding-patterns-5-approaches-for-handling-this-92c651b5af56) pour encore plus d'options ! Chaque approche a ses mérites, mais en supposant que vous êtes à l'aise avec les fonctionnalités expérimentales, [je suggère d'utiliser les propriétés de classe (aka property initializers) par défaut aujourd'hui](https://medium.freecodecamp.org/react-binding-patterns-5-approaches-for-handling-this-92c651b5af56).

Ce sondage date d'août 2016. Depuis, il semble que les propriétés de classe aient gagné en popularité, et que createClass ait perdu en popularité.

%[https://twitter.com/housecor/status/766257218312282113?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fhousecor%2Fstatus%2F766257218312282113%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F650743198348808192%25252FLT6SeOJr_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

**Note de côté** : Beaucoup sont confus sur pourquoi les fonctions fléchées et le bind dans le render sont potentiellement problématiques. La vraie raison ? [Cela rend shouldComponentUpdate et PureComponent grincheux](https://medium.freecodecamp.org/why-arrow-functions-and-bind-in-reacts-render-are-problematic-f1c08b060e36).

### Décision 7 : Styling

Voici où les options deviennent sérieusement intenses. Il existe 50+ façons de styliser vos composants, y compris les styles en ligne de React, le CSS traditionnel, Sass/Less, [CSS Modules](https://github.com/css-modules/css-modules), et [56 options CSS-in-JS](https://github.com/MicheleBertoli/css-in-js). Je ne plaisante pas. J'explore les approches de stylisation React en détail [dans le module de stylisation de ce cours](https://www.pluralsight.com/courses/react-creating-reusable-components), mais voici le résumé :

![Image](https://cdn-media-1.freecodecamp.org/images/EqLlcFfHYN0JZJo9P6bfYDndLbMFviTkKEMN)
_Le rouge est mauvais. Le vert est bon. Le gris est un avertissement._

Voyez-vous pourquoi il y a tant de fragmentation dans les options de stylisation de React ? Il n'y a pas de gagnant clair.

![Image](https://cdn-media-1.freecodecamp.org/images/1Us0a3CAmp3rpQUGiZi6HA4Q82c0-jThyukA)
_Il semble que le CSS-in-JS gagne en popularité. Les CSS modules perdent en popularité._

Mon équipe actuelle utilise Sass avec BEM et en est assez satisfaite, mais j'apprécie également [styled-components](https://www.styled-components.com).

### Décision 8 : Logique réutilisable

React a initialement adopté [les mixins](https://reactjs.org/docs/react-without-es6.html#mixins) comme mécanisme pour partager du code entre les composants. Mais les mixins ont causé des problèmes et sont [maintenant considérés comme nuisibles](https://reactjs.org/blog/2016/07/13/mixins-considered-harmful.html). Vous ne pouvez pas utiliser les mixins avec les composants de classe ES, donc maintenant les gens [utilisent des composants d'ordre supérieur](https://reactjs.org/docs/higher-order-components.html) et [render props](https://cdb.reacttraining.com/use-a-render-prop-50de598f11ce) (aka fonction en tant qu'enfant) pour partager du code entre les composants.

%[https://twitter.com/kentcdodds/status/905093584205914116?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fkentcdodds%2Fstatus%2F905093584205914116%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F759557613445001216%25252F6M2E1l4q_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Les composants d'ordre supérieur sont actuellement plus populaires, mais je préfère les render props car ils sont souvent plus faciles à lire et à créer. [Michael Jackson m'a récemment convaincu avec ceci](https://cdb.reacttraining.com/use-a-render-prop-50de598f11ce) :

%[https://youtu.be/BcVAq3YFiuc]

### Et ce n'est pas tout...

Il y a d'autres décisions :

* Utiliserez-vous une extension [.js ou .jsx](https://github.com/facebookincubator/create-react-app/issues/87#issuecomment-234627904) ?
* Placerez-vous [chaque composant dans son propre dossier](https://medium.com/styled-components/component-folder-pattern-ee42df37ec68) ?
* Imposerez-vous un composant par fichier ? [Rendrez-vous les gens fous en mettant un fichier index.js dans chaque répertoire](https://hackernoon.com/the-100-correct-way-to-structure-a-react-app-or-why-theres-no-such-thing-3ede534ef1ed) ?
* Si vous utilisez propTypes, les déclarerez-vous en bas, ou dans la classe elle-même en utilisant [les propriétés statiques](https://michalzalecki.com/react-components-and-class-properties/#static-fields) ? [Déclarerez-vous les propTypes aussi profondément que possible](https://iamakulov.com/notes/deep-proptypes/?utm_content=buffer57abf&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer) ?
* Initialiserez-vous l'état traditionnellement dans le constructeur ou utiliserez-vous la [syntaxe d'initialisation des propriétés](http://stackoverflow.com/questions/35662932/react-constructor-es6-vs-es7) ?

Et puisque React est principalement du JavaScript, vous avez la longue liste habituelle des décisions de style de développement JS telles que [les points-virgules](https://eslint.org/docs/rules/semi), [les virgules finales](https://eslint.org/docs/rules/comma-dangle), [le formatage](https://github.com/prettier/prettier), et [le nommage des gestionnaires d'événements](https://jaketrent.com/post/naming-event-handlers-react/) à considérer également.

### Choisissez une norme, puis automatisez son application

Et tout cela, il existe des dizaines de combinaisons que vous pouvez voir dans la nature aujourd'hui.

Donc, les prochaines étapes sont clés :

> 1. Discutez de ces décisions en équipe et documentez votre norme.

> 2. Ne perdez pas de temps à surveiller manuellement l'incohérence dans les revues de code. Appliquez vos normes à l'aide d'outils comme [ESLint](https://eslint.org), [eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react), et [prettier](https://github.com/prettier/prettier).

> 3. Besoin de restructurer des composants React existants ? Utilisez [react-codemod](https://github.com/reactjs/react-codemod) pour automatiser le processus.

D'autres décisions clés que j'ai omises ? Faites-le savoir via les commentaires.

### Vous cherchez plus d'informations sur React ? ⚒️

J'ai écrit [plusieurs cours sur React et JavaScript](http://bit.ly/psauthorpageimmutablepost) sur Pluralsight ([essai gratuit](http://bit.ly/pstrialimmutablepost)).

![Image](https://cdn-media-1.freecodecamp.org/images/tSMdNLHieGadHJiqBEOK3ye4YonU2SGbUCvV)

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), architecte logiciel chez VinSolutions, un MVP Microsoft, et forme des développeurs logiciels à l'international sur des pratiques logicielles comme le développement front-end et le code propre. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).