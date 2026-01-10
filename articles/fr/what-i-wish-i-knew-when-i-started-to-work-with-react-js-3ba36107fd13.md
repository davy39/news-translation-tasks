---
title: Ce que j'aurais aimé savoir quand j'ai commencé à travailler avec React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T19:51:32.000Z'
originalURL: https://freecodecamp.org/news/what-i-wish-i-knew-when-i-started-to-work-with-react-js-3ba36107fd13
coverImage: https://cdn-media-1.freecodecamp.org/images/0*nrQ5vVSdulAG3LFO
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: technology
  slug: technology
seo_title: Ce que j'aurais aimé savoir quand j'ai commencé à travailler avec React.js
seo_desc: 'By David Yu

  After its initial release on May 29, 2013, React.js has taken over the internet.
  It’s not a secret that myself and many other developers owe their success to this
  amazing framework.

  With Medium so full of React.js tutorials, I wish one of...'
---

Par David Yu

Depuis sa sortie initiale le 29 mai 2013, React.js a conquis Internet. Ce n'est un secret pour personne que moi-même et de nombreux autres développeurs devons notre succès à ce framework incroyable.

Avec Medium rempli de tutoriels sur React.js, j'aurais aimé que l'un d'eux me donne ces conseils quand j'ai commencé.

### Pas besoin de .bind(this) lors de l'utilisation des fonctions fléchées

Habituellement, vous aurez quelque chose comme ceci lorsque vous avez un composant contrôlé :

```
class Foo extends React.Component{  constructor( props ){    super( props );    this.handleClick = this.handleClick.bind(this);  }
```

```
  handleClick(event){    // votre logique de gestion d'événement  }
```

```
  render(){    return (      <button type="button"       onClick={this.handleClick}>      Cliquez-moi      </button>    );  }}
```

Vous écrivez `.bind(this)` pour chaque méthode qui existe, parce que la plupart des tutoriels vous disent de le faire. Si vous avez plusieurs composants contrôlés, vous vous retrouverez avec une grosse pile de code dans votre `constructor(){}`.

#### Au lieu de cela, vous pouvez :

```
class Foo extends React.Component{
```

```
  handleClick = (event) => {    // votre logique de gestion d'événement  }
```

```
  render(){    return (      <button type="button"       onClick={this.handleClick}>        Cliquez-moi      </button>    );  }}
```

Comment ?

Les fonctions fléchées d'ES6 utilisent le [Lexical Scoping](https://whatis.techtarget.com/definition/lexical-scoping-static-scoping), qui permet à la méthode d'accéder au `this` de l'endroit où elle est déclenchée.

### Quand les service workers travaillent contre vous

Les service workers sont excellents pour une [application web progressive](https://developers.google.com/web/progressive-web-apps/), qui permet un accès hors ligne et optimise l'expérience pour les utilisateurs avec des connexions Internet médiocres.

Mais lorsque vous n'êtes pas conscient que le service worker met en cache vos fichiers statiques, vous déployez vos correctifs à répétition.

Pour vous rendre compte que votre site ne se met pas à jour. 😱

Ne paniquez pas, assurez-vous dans votre `src/index.js` :

```
// Assurez-vous qu'il est défini pour désenregistrer
serviceWorker.unregister();
```

À partir de la version 16.8, cette ligne devrait être `serviceWorker.unregister()` par défaut.

Mais s'ils décident de changer à nouveau, vous saurez où regarder.

### 99 % du temps, vous n'avez pas besoin d'éjecter

[Create React App](https://github.com/facebook/create-react-app) offre une option pour `yarn eject` votre projet afin de personnaliser votre processus de construction.

Je me souviens avoir essayé de personnaliser le processus de construction pour avoir des images SVG automatiquement intégrées dans notre code. J'ai passé des heures à essayer de comprendre le processus de construction. Nous avons fini par avoir un fichier d'importation qui injecte des balises SVG, et nous avons augmenté la vitesse de chargement du site de 0,0001 milliseconde.

Éjecter votre projet React, c'est comme ouvrir le capot de votre voiture en marche et changer le moteur à la volée pour qu'elle roule 1 % plus vite.

Bien sûr, si vous êtes déjà un maître de Webpack, il est utile de personnaliser le processus de construction pour répondre aux besoins du projet.

Lorsque vous essayez de livrer à temps, concentrez vos efforts là où cela fait avancer les choses.

### ESlint Auto Fix On Save fait gagner beaucoup de temps

Vous avez peut-être copié du code quelque part qui a un formatage désordonné. Parce que vous ne supportez pas à quel point c'est laid, vous passez du temps à ajouter manuellement des espaces.

![Image](https://cdn-media-1.freecodecamp.org/images/qgo75N8UaqNzG19swDAd2jYfVAm4qXjbsymk)

Avec ESLint et le plugin Visual Studio Code, il peut le corriger pour vous à l'enregistrement.

![Image](https://cdn-media-1.freecodecamp.org/images/4x9nM8yWctSfdfylIJCDvlT7uZ5VecV5w-jL)

#### Comment ?

1. Dans votre `package.json`, ajoutez quelques dépendances de développement et faites `npm i` ou `yarn` :

```
"devDependencies": {
```

```
 "eslint-config-airbnb": "^17.1.0",
```

```
 "eslint-config-prettier": "^3.1.0",
```

```
 "eslint-plugin-import": "^2.14.0",
```

```
 "eslint-plugin-jsx-a11y": "^6.1.1",
```

```
 "eslint-plugin-prettier": "^3.0.0",
```

```
 "eslint-plugin-react": "^7.11.0"
```

```
}
```

2. Installez l'extension ESLint

![Image](https://cdn-media-1.freecodecamp.org/images/6V--Oc6mlGYunud2K1tsoK6oYikoxrc96ZT7)

3. Activez Auto Fix On Save

![Image](https://cdn-media-1.freecodecamp.org/images/eQRNCCmrM2q8V5ZU9NArLLfGQXuN06Njl0yD)

### Vous n'avez pas besoin de Redux, styled-components, etc...

Chaque outil a son but. Cela dit, il est bon de connaître les différents outils.

> Si tout ce que vous avez est un marteau, tout ressemble à un clou — Abraham Maslow

Vous devez penser au temps de configuration pour certaines des bibliothèques que vous utilisez et le comparer à :

* Quel est le problème que j'essaie de résoudre ?
* Ce projet vivra-t-il assez longtemps pour bénéficier de cette bibliothèque ?
* React offre-t-il déjà quelque chose prêt à l'emploi ?

Avec [Context](https://reactjs.org/docs/context.html) et [Hooks](https://reactjs.org/docs/hooks-intro.html) maintenant disponibles pour React, avez-vous encore besoin de Redux ?

Je recommande vivement [Redux Offline](https://github.com/redux-offline/redux-offline) pour lorsque vos utilisateurs sont dans un environnement avec une mauvaise connexion Internet.

### Réutiliser le gestionnaire d'événements

Si vous n'avez pas envie de taper la même chose encore et encore, réutiliser un gestionnaire d'événements pourrait être une option :

```
class App extends Component {
```

```
 constructor(props) {  super(props);  this.state = {   foo: "",   bar: "",  }; }
```

```
 // Réutilisable pour toutes les entrées  onChange = e => {  const {   target: { value, name },  } = e;    // name sera le nom de l'état  this.setState({   [name]: value  });
```

```
 };  render() {  return (   <div>    <input name="foo" onChange={this.onChange} />    <input name="bar" onChange={this.onChange} />      </div>  ); }}
```

### setState est asynchrone

Le moi naïf écrirait quelque chose comme :

```
 constructor(props) {  super(props);  this.state = {   isFiltered: false  }; }
```

```
 toggleFilter = () => {  this.setState({   isFiltered: !this.state.isFiltered  });  this.filterData(); };  filterData = () => {  // this.state.isFiltered devrait être vrai, mais ce n'est pas le cas  if (this.state.isFiltered) {   // Faire un peu de filtrage  } };
```

#### Option 1 : Passer l'état vers le bas

```
toggleFilter = () => { const currentFilterState = !this.state.isFiltered; this.setState({  isFiltered: currentFilterState }); this.filterData(currentFilterState);};
```

```
filterData = (currentFilterState) => { if (currentFilterState) {  // Faire un peu de filtrage }};
```

#### Option 2 : La fonction secondaire pour le callback de setState

```
toggleFilter = () => { this.setState((prevState) => ({  isFiltered: !prevState.isFiltered }), () => {  this.filterData(); });};
```

```
filterData = () => {  if (this.state.isFiltered) {   // Faire un peu de filtrage  }};
```

### Conclusion

Ces conseils m'ont fait gagner beaucoup de temps, et je suis sûr qu'il y en a d'autres. N'hésitez pas à les partager dans la section des commentaires.

Si vous cherchez à intégrer votre site web avec WeChat et à atteindre plus d'un milliard d'utilisateurs en Chine, inscrivez-vous pour obtenir un [glossaire gratuit des termes couramment utilisés sur WeChat](https://pages.convertkit.com/b2469604dd/0c671fdd2d).