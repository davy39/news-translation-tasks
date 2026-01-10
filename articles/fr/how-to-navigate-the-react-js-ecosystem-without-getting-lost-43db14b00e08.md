---
title: Comment naviguer dans l'écosystème React.js sans se perdre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-26T21:11:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-navigate-the-react-js-ecosystem-without-getting-lost-43db14b00e08
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aD0tWP4vXjrs1FTFlgkKAg.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment naviguer dans l'écosystème React.js sans se perdre
seo_desc: 'By Marius Espejo

  In the world of software development it’s often hard to find one direct path for
  learning something new. Should you read a book? Follow a tutorial? Watch a video?
  Ask for advice?

  With so many possible paths and options to take, getti...'
---

Par Marius Espejo

Dans le monde du développement logiciel, il est souvent difficile de trouver un chemin direct pour apprendre quelque chose de nouveau. Devriez-vous lire un livre ? Suivre un tutoriel ? Regarder une vidéo ? Demander des conseils ?

Avec tant de chemins et d'options possibles, il est facile de se perdre.

Apprendre React.js est en réalité assez simple, il suffit de savoir quel chemin prendre.

### **Prérequis**

Voici quelques choses que je vous recommande de bien maîtriser avant de commencer à apprendre React.

![Image](https://cdn-media-1.freecodecamp.org/images/m9Mq6ljGw8tWFtazZfkl3znHvg2v-0FUmQMr)
_[Photo par Alice Donovan Rouse](https://unsplash.com/@alicekat?photo=z9F_yK4Nmf8" rel="noopener" target="_blank" title=")_

#### Assurez-vous d'avoir une certaine compréhension de HTML et CSS

Presque tous les développements web nécessiteront une certaine connaissance de ces deux technologies. Si vous êtes un débutant absolu dans ce domaine, je vous recommande de consulter les vidéos de [Travis Neilson](https://www.freecodecamp.org/news/how-to-navigate-the-react-js-ecosystem-without-getting-lost-43db14b00e08/undefined) comme [HTML5 Basics](https://www.youtube.com/playlist?list=PLqGj3iMvMa4KlJn1pMYPVV3eYzxJlWcON) et [CSS Basics](https://www.youtube.com/playlist?list=PLqGj3iMvMa4IOmy04kDxh_hqODMqoeeCy). Ensuite, passez à [freeCodeCamp.org](https://www.freecodecamp.org) ou [codeacademy.com](https://www.codecademy.com/learn/learn-html-css) pour vous entraîner.

Votre objectif ultime devrait être de prendre une conception ou une structure de base pour une page web, de la transformer en code et de voir visuellement ce que vous espériez qu'elle ressemble. Idéalement, elle ressemblera beaucoup à votre conception.

#### Ayez une bonne maîtrise de JavaScript lui-même

Je ne recommande pas d'essayer d'apprendre des frameworks et des bibliothèques avant d'avoir passé du temps à apprendre le langage JavaScript. Il existe une quantité énorme de ressources pour apprendre JavaScript en fonction de votre expérience.

Pour un débutant absolu, [freeCodeCamp](https://medium.freecodecamp.org/) dispose d'un ensemble impressionnant de ressources, y compris une [playlist vidéo](https://www.youtube.com/playlist?list=PLWKjhJtqVAbk2qRZtWSzCIN38JC_NdhW5) de toutes les bases de JavaScript et un endroit interactif pour apprendre et pratiquer directement [sur leur site web](https://www.freecodecamp.com).

La meilleure façon d'apprendre à coder est d'écrire du code !

Si vous avez déjà utilisé JavaScript dans le passé et avez besoin d'un rappel, consultez cette [réintroduction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript).

Si vous n'êtes pas sûr de connaître JavaScript, alors je parie que [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS) est fait pour vous. C'est en fait une série de livres populaires qui est utile pour ceux qui cherchent à mieux comprendre le langage.

> « Lorsque vous vous efforcez de comprendre votre code, vous créez un meilleur travail et devenez meilleur dans ce que vous faites. Le code n'est plus seulement votre travail, c'est votre art. »

> — Jenn Lukas

#### Au-delà de l'apprentissage des bases de JavaScript, vous devrez également acquérir une compréhension décente de certaines fonctionnalités d'ECMAScript 2015 (ES6)

Plus précisément, concentrez-vous sur la compréhension des éléments suivants :

* Modules (import/export)
* let et const
* Fonctions fléchées
* Classes
* Déstructuration
* Rest/Spread

Ces éléments sont garantis d'apparaître dans votre code React et en avoir une certaine compréhension vous permettra de consulter la documentation beaucoup plus facilement.

Pour un démarrage rapide sur ces sujets, je vous recommande la [feuille de triche ES6](https://www.youtube.com/playlist?list=PLoYCgNOIyGACDQLaThEEKBAlgs4OIUGif) de LearnCode.academy ou l'une des [ressources de Babel](https://babeljs.io/learn-es2015/).

#### Apprenez à utiliser le Node Package Manager (npm)

[Installez Node.js](https://nodejs.org/en/) et npm sera inclus avec. Pour le moment, npm est l'un des meilleurs moyens de télécharger des dépendances de développement JavaScript.

Par exemple, cette simple commande vous permettra d'installer et de télécharger React pour un projet :

```
npm install --save react
```

La plupart de ce que vous devez savoir au début est comment installer des packages. Cela seul vous ouvrira un ensemble étendu d'outils et de bibliothèques qui vous permettront de faire plus en moins de temps.

#### (Facultatif) Apprenez les bases de la programmation fonctionnelle

Bien que ce ne soit pas nécessaire pour apprendre React, comprendre les concepts de base de la programmation fonctionnelle sera utile à de nombreuses reprises dans votre développement React.

Je vous recommande de comprendre la composition de fonctions, la pureté et les fonctions d'ordre supérieur. Le but ici n'est pas de devenir un expert sur le sujet, mais au moins d'y être exposé. Pour une introduction rapide, voici une excellente conférence d'un grand [orateur](https://www.youtube.com/watch?v=e-5obm1G_FY). Ou vous pouvez apprendre directement depuis votre [boîte de réception](https://medium.freecodecamp.com/learning-the-fundamentals-of-functional-programming-425c9fd901c6) si vous le souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/B4Egk68DIZnCDJq3h8rnH-C1rgjHSX14pCe6)
_[Photo par Luke Pamer](https://unsplash.com/search/hiking?photo=KBpnPk44tOA" rel="noopener" target="_blank" title=")_

> « Chaque sommet est à portée de main si vous continuez simplement à grimper. »

> — **Barry Finlay**

Selon votre expérience en développement, vous pouvez apprendre les bases de React en **quelques heures à quelques jours**. Au-delà de cela, il suffit d'un peu plus d'expérience et vous serez en mesure de créer des applications en un rien de temps.

Comment est-ce possible ? Eh bien...

### Tout d'abord, n'apprenez pas Redux ou d'autres bibliothèques pour l'instant

La plus grande erreur que beaucoup de gens commettent lorsqu'ils apprennent React pour la première fois est de chercher un modèle de démarrage ou un tutoriel qui inclut déjà Redux et une série d'autres bibliothèques.

Les gens me demandent souvent quelle est la meilleure façon d'apprendre React. Pour une raison quelconque, il ne leur vient jamais à l'esprit que la [documentation officielle](https://facebook.github.io/react/docs/hello-world.html) est en fait un excellent point de départ car elle se concentre sur l'enseignement de React uniquement.

Oubliez Redux pour l'instant. Vous n'en aurez peut-être même pas [besoin](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367).

Oubliez les autres bibliothèques et les modèles de démarrage.

> « Apprendre React en copiant des modèles de démarrage, c'est comme apprendre à cuisiner en mangeant de la nourriture dans des restaurants chic. Cela ne fonctionne pas. Vous devez commencer par les bases et ignorer la peur de manquer quelque chose. » — [Dan Abramov](https://www.freecodecamp.org/news/how-to-navigate-the-react-js-ecosystem-without-getting-lost-43db14b00e08/undefined)

#### **Concentrez-vous sur React et uniquement sur React.**

Je recommanderais cela pour la même raison que vous ne voudriez peut-être pas apprendre le calcul avant de vous sentir à l'aise avec l'algèbre. Ou vous n'aurez peut-être même pas besoin de calcul pour résoudre un problème mathématique simple.

Découvrez quels problèmes React peut et ne peut pas résoudre pour vous seul. Cela vous donnera un guide de base pour savoir quand il est temps d'intégrer plus de bibliothèques, et finalement plus de choses à apprendre, dans votre projet.

### Voici la manière la plus simple de commencer

Commencez avec [create-react-app](https://github.com/facebookincubator/create-react-app). Il vous donnera tout ce dont vous avez besoin pour commencer petit sans être freiné par le code de démarrage et la configuration.

Il vous permet la liberté de vous concentrer sur l'apprentissage de React seul sans avoir à vous soucier de l'apprentissage et de la configuration de Webpack, Babel et diverses autres configurations.

```
npm install -g create-react-app create-react-app my-app  
```

```
cd my-app npm start
```

Ces quatre commandes simples vous donneront tout ce dont vous avez besoin pour démarrer un projet. Il inclut des outils qui actualiseront votre navigateur lorsque vous modifierez votre code.

Il offre également une commande de construction qui compilera votre code en quelques actifs statiques que vous pouvez facilement déployer n'importe où et un guide utilisateur [incroyable](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md) qui vous guidera tout au long de ce processus.

Je considère create-react-app comme une sorte de chaussures de randonnée. Vous n'avez pas nécessairement besoin de chaussures de randonnée pour gravir une montagne, mais elles vous aideront certainement et pourraient même faciliter l'ascension de certaines surfaces. Et si vous réalisez que vous n'en avez pas besoin, vous pouvez toujours les "[éjecter](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#npm-run-eject)" de vos pieds !

Avec les outils mis de côté, revenons sur le chemin de l'apprentissage de React.

### Maîtrisez les fondamentaux de React

Consultez cet excellent article sur les principaux [concepts de React](https://medium.freecodecamp.com/the-5-things-you-need-to-know-to-understand-react-a1dbd5d114a3). Il n'y a en fait pas beaucoup de choses que vous devez apprendre.

En général, vous devriez comprendre les éléments suivants :

* JSX : [ce que c'est](https://facebook.github.io/react/docs/introducing-jsx.html), comment il diffère de HTML traditionnel, et comment le configurer de manière déclarative pour gérer les changements dynamiques

```
/* Remarquez comment vous devez utiliser className au lieu de class     Et comment l'expression à l'intérieur des accolades permet de    gérer dynamiquement tout nom passé via props */
```

```
<h1 className="greeting">Bonjour, {this.props.name}</h1>
```

* Apprenez à écrire des composants fonctionnels sans état. [Voici pourquoi](https://hackernoon.com/react-stateless-functional-components-nine-wins-you-might-have-overlooked-997b0d933dbc).

```
// Ce ne sont vraiment que des fonctions simples qui retournent du JSX
function MyComponent(props) {      return <h1 className="greeting">Bonjour, {props.name}</h1>; }
```

```
// Alternativement, écrivez-les en utilisant des fonctions fléchées
const MyComponent = (props) => (<h1 className="greeting">Bonjour, {props.name}</h1>);
```

* Apprenez à écrire des composants en utilisant la syntaxe de classe ES6. Cela vous permet d'écrire des composants plus complexes avec accès aux hooks de cycle de vie et à l'[état local](https://facebook.github.io/react/docs/state-and-lifecycle.html#adding-local-state-to-a-class)

```
class MyComponent extends React.Component {      render() {          return <h1 className="greeting">Bonjour, {this.props.name}</h1>;      } }
```

* Assurez-vous d'avoir une bonne compréhension de l'[état](https://facebook.github.io/react/docs/state-and-lifecycle.html#using-state-correctly) et de la manière de l'utiliser correctement. Comprendre les avantages et les inconvénients de l'utilisation de l'état local d'un composant vous donnera les bases mentales pour savoir quand, et quand ne pas, utiliser une autre solution de gestion d'état
* Apprenez à écrire et à utiliser les [hooks de cycle de vie des composants](https://facebook.github.io/react/docs/react-component.html#the-component-lifecycle) et quand chacun peut être utile

```
class MyComponent extends React.Component {   // Quelques exemples de hooks que j'ai dû utiliser beaucoup :
```

```
   componentDidMount() {      /* utile pour initialiser ou déclencher des événements après que          le composant est rendu dans le DOM */                                   }          shouldComponentUpdate() {     /* utile à des fins de performance et pour éviter les re-rendus redondants */   }      componentWillReceiveProps() {     /* utile lorsque vous devez déclencher des changements lorsque de nouvelles props             arrivent */   }      render() {          return <h1 className="greeting">Bonjour, {this.props.name}</h1>;      } }
```

* Apprenez à utiliser [PropTypes](https://facebook.github.io/react/docs/typechecking-with-proptypes.html). C'est un moyen facile d'ajouter une vérification de type de base à vos composants

```
import PropTypes from 'prop-types';  
```

```
class MyComponent extends React.Component {      render() {          return <h1 className="greeting">Bonjour, {this.props.name}</h1>;      } }Greeting.propTypes = {    name: PropTypes.string };
```

### Apprenez à structurer votre code

Une fois que vous maîtrisez les fondamentaux, vous voudrez commencer à réfléchir à la manière dont votre code est structuré.

Explorez le concept de composants Conteneur et Présentation. Cela vous aidera à comprendre comment mieux séparer les préoccupations au sein de votre code React.

Si vous décidez d'incorporer une solution de gestion d'état à l'avenir, comme Redux, alors les composants Conteneur vous aideront dans cette transition. Vous saurez que la plupart des données transmises dans votre application proviennent des conteneurs.

Si vous ne l'avez pas déjà fait, réfléchissez également à votre structure de dossiers. À mesure que votre base de code commence à croître, considérez à quel point votre structure de dossiers est évolutive.

Les fichiers sont-ils faciles à trouver ?

Si vous travaillez avec une équipe, sont-ils capables de savoir intuitivement où se trouvent les composants spécifiques ?

Notez que vous n'avez pas besoin d'avoir votre code dans une structure spécifique immédiatement. Essayez de prendre l'habitude de **refactoriser** et d'améliorer votre code au fur et à mesure que vous apprenez chacun de ces concepts.

> « Je ne suis pas un grand programmeur ; je suis juste un bon programmeur avec de grandes habitudes. »

> — Kent Beck

### Construisez une application qui résout un problème réel

La meilleure et vraie façon de comprendre profondément React est de construire quelque chose avec.

Essayez de construire quelque chose qui vous motivera réellement à travailler dessus et évitez de créer des choses dont vous connaissez probablement déjà la solution.

* Essayez d'incorporer une sorte de données externes (peut-être faire un appel d'API) et découvrez comment faire circuler ces données correctement dans votre application, en tirant pleinement parti de l'état et des props
* Envisagez d'intégrer [react-router](https://reacttraining.com/react-router/) une fois que vous avez besoin d'avoir plusieurs pages dans votre application
* Utilisez certaines bibliothèques de composants pour démarrer rapidement avec une apparence et une convivialité de base. Sachez que cet écosystème JavaScript incroyable que nous avons avec npm et Github vous permet d'incorporer facilement des composants prêts à l'emploi dans votre application
* Déployez votre application quelque part. Il existe de nombreuses façons différentes de déployer votre code gratuitement. Essayez-en une. Il n'y a rien de plus cool que de voir votre travail déployé sur Internet et de pouvoir partager ce lien avec quelqu'un d'autre

![Image](https://cdn-media-1.freecodecamp.org/images/XWdjQuB3Kpn7IwJB8-tN-EhdPXcBOtohv3qE)
_[Photo par Kalen Emsley](https://unsplash.com/@kalenemsley?photo=mgJSkgIo_JI" rel="noopener" target="_blank" title=")_

Si vous êtes arrivé jusqu'ici, c'est génial ! Regardez en arrière votre progression et soyez fier de vous.

Vous en voulez plus ? Voici quelques conseils.

### Testez votre code !

Assurez-vous d'apprendre à tester votre code dès que possible. Utilisez [Jest](https://facebook.github.io/jest/) (ou votre test runner préféré) et [Enzyme](http://airbnb.io/enzyme/).

Jest et Enzyme sont assez faciles à apprendre et peuvent en fait vous aider à comprendre comment vos composants fonctionnent en isolation.

En plus de cela, les tests rendent votre code plus sûr à refactoriser et à améliorer, tout en servant de documentation dynamique pour vos composants.

### Utilisez une gestion d'état avancée

Avez-vous l'impression que votre gestion d'état avec `setState` devient trop complexe ? Passez-vous constamment des props à plusieurs niveaux de composants descendants ?

Il est temps d'apprendre Redux ou une autre variante de Flux ! Vous devrez comprendre les avantages qu'un système de gestion d'état apporte, et quand l'utiliser ou non.

### Ne vous répétez pas

Si vous vous retrouvez à écrire le même code à plusieurs endroits, voyez si vous pouvez plutôt tirer parti d'autres stratégies pour réutiliser la logique. Apprenez à créer et à utiliser des [composants d'ordre supérieur](https://facebook.github.io/react/docs/higher-order-components.html). Il s'agit d'une technique avancée pour réutiliser la logique des composants. Cela améliorera vos connaissances en matière de composition de composants.

![Image](https://cdn-media-1.freecodecamp.org/images/jtMq5nE8zr2SMCxlbawxtqtwSwT3oL1QY6k4)
_[Photo par Justin Luebke](https://unsplash.com/@jluebke?photo=Gcl6jcB1r9g" rel="noopener" target="_blank" title=")_

### Monter de niveau

En réalité, la liste ne s'arrête jamais.

Il y a constamment de nouvelles choses que vous pouvez apprendre pour améliorer et ajouter à vos applications et à votre ensemble de compétences.

Si vous vous concentrez sur les bases et faites la plupart des choses ci-dessus, je crois que vous serez déjà sur une bonne voie non seulement avec React, mais aussi avec le développement front-end et JavaScript en général.

L'écosystème JavaScript est en constante évolution. Gardez-vous dans l'état d'esprit de l'**apprentissage continu**. Continuez à essayer des choses et découvrez ce qui fonctionne le mieux pour vous.

À l'avenir, votre expérience vous aidera à vous guider sur ce qu'il faut faire ensuite.

Merci d'avoir lu ! **Si vous avez trouvé cet article utile, laissez quelques ?? ???? sur cet article pour que d'autres puissent le trouver !**