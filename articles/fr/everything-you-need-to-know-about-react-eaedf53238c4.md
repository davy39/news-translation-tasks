---
title: 'Tout ce que vous devez savoir sur React : Les bases pour commencer à construire'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-12T22:40:59.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-about-react-eaedf53238c4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ayz9rmofYhMCCC1KVuST3w.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Tout ce que vous devez savoir sur React : Les bases pour commencer à construire'
seo_desc: 'By Scott Domes

  Are you curious about React and haven’t had the chance to learn it? Or maybe you’ve
  tried tutorials in the past, but struggled to master the core concepts? Or maybe
  you’ve learned the basics, but want to consolidate your knowledge? Eit...'
---

Par Scott Domes

Êtes-vous curieux à propos de React et n'avez pas encore eu l'occasion de l'apprendre ? Ou peut-être avez-vous essayé des tutoriels par le passé, mais avez eu du mal à maîtriser les concepts de base ? Ou peut-être avez-vous appris les bases, mais souhaitez consolider vos connaissances ? Dans tous les cas, cet article est pour vous.

Nous allons construire un simple lecteur de musique React, en ajoutant de nouveaux concepts React au fur et à mesure.

Voici ce que nous allons couvrir :

* Qu'est-ce qu'un composant React ?
* Le rendu ReactDOM
* Composants de classe vs fonctionnels
* JSX
* État
* Gestion des événements
* setState asynchrone
* Props
* Refs

C'est à peu près tout ce dont vous avez besoin pour construire et maintenir une application React. Mais nous allons l'introduire pièce par pièce.

### Installation

Voici la situation : une petite start-up a fait appel à vous pour obtenir de l'aide. Ils ont créé une page pour que les utilisateurs puissent télécharger de la musique et la visualiser en couleurs lumineuses. Mais ils ont besoin de vous pour faire la partie difficile, c'est-à-dire la faire fonctionner.

Pour commencer, créez un nouveau répertoire de projet et ajoutez [les trois fichiers suivants](https://gist.github.com/scottdomes/aae01cce0fdb69cea49aa5b3b75f3313).

**Assurez-vous d'utiliser une version à jour de [Chrome](https://www.google.com/intl/en/chrome/browser/desktop/index.html) avec ce tutoriel, sinon les animations dans le code ci-dessus ne fonctionneront pas.**

Merci à [Steven Fabre](https://twitter.com/stevenfabre) pour le CSS du bouton de lecture et à [Justin Windle](https://codepen.io/soulwire/) pour le code de visualisation ([vous pouvez voir l'original ici](https://codepen.io/soulwire/pen/Dscga)).

Ouvrez `index.html` dans un éditeur de code et votre navigateur, et commençons !

### Qu'est-ce que React ?

React est un moyen de construire des interfaces utilisateur. Il ne se préoccupe que de ce que vous voyez sur le front-end. React rend les interfaces utilisateur très faciles à construire en découpant chaque page en morceaux. Nous appelons ces morceaux des _composants_.

Voici un exemple de découpage d'une page en composants :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bvQNHjZOXcl-ds9A4AWYVg.png)

Chaque section mise en évidence ci-dessus est considérée comme un composant. Mais que signifie cela pour un développeur ?

### Qu'est-ce qu'un composant React ?

Un composant React est un morceau de code qui représente une partie de la page. Chaque composant est une fonction JavaScript qui retourne un morceau de code représentant une partie d'une page web.

Pour construire une page, nous appelons ces fonctions dans un certain ordre, assemblons le résultat et le montrons à l'utilisateur.

Écrivons un composant à l'intérieur de la balise `<script>` dans `index.html` avec le type "text/babel" :

```
<script type="text/babel">  function OurFirstComponent() {    return (      // Le code représentant l'élément UI va ici    );  }</script>
```

Lorsque nous appelons la fonction `OurFirstComponent()`, nous obtenons une partie de la page.

Vous pouvez également écrire des fonctions comme ceci :

```
const OurFirstComponent = () => {  return (    // Les éléments pour ce composant vont ici  );}
```

React utilise un langage appelé JSX qui ressemble à HTML mais fonctionne à l'intérieur de JavaScript, ce que HTML ne fait généralement pas.

Vous pouvez ajouter du HTML simple à cette section pour qu'il apparaisse sur l'UI :

```
<script type="text/babel">  function OurFirstComponent() {    return (      <h1>Bonjour, je suis un composant React !</h1>    );  }</script>
```

Lorsque nous appelons la fonction `OurFirstComponent()`, nous obtenons un morceau de JSX. Nous pouvons utiliser quelque chose appelé [ReactDOM](https://www.npmjs.com/package/react-dom) pour le placer sur la page.

```
<script type="text/babel">  function OurFirstComponent() {    return (      <h1>Bonjour, je suis un composant React !</h1>    );  }
```

```
  const placeWeWantToPutComponent = document.getElementById('hook');  ReactDOM.render(OurFirstComponent(), placeWeWantToPutComponent);</script>
```

Maintenant, notre balise `<h1>` sera placée à l'intérieur de l'élément avec l'`ID` de `hook`. Cela devrait ressembler à ceci lorsque vous actualisez votre navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*X3sGgAtXyBDFEcgtbR3tOw.png)

Nous pouvons également écrire notre composant en JSX comme ceci :

```
ReactDOM.render(<OurFirstComponent />, placeWeWantToPutComponent);
```

C'est standard — invoquez vos composants comme si vous écriviez du HTML.

### Assembler les composants

Nous pouvons placer des composants React à l'intérieur d'autres composants.

```
<script type="text/babel">  function OurFirstComponent() {    return (      <h1>Je suis l'enfant !</h1>    );  }
```

```
  function Container() {    return (      <div>        <h1>Je suis le parent !</h1>        <OurFirstComponent />      </div>    );  }
```

```
  const placeWeWantToPutComponent = document.getElementById('hook');  ReactDOM.render(<Container />, placeWeWantToPutComponent);</script>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*p8ZNTE0_mnYkt-5Zq2fRtA.png)

C'est ainsi que nous construisons notre page à partir de morceaux de React — en imbriquant des composants les uns dans les autres.

### Composants de classe

Jusqu'à présent, nous avons écrit des composants sous forme de fonctions. Ceux-ci sont appelés _composants fonctionnels_.

Mais vous pouvez écrire des composants d'une autre manière, en tant que classes JavaScript. Ceux-ci sont appelés composants de classe.

```
class Container extends React.Component {  render() {    return (      <div>        <h1>Je suis le parent !</h1>        <OurFirstComponent />      </div>    );  }}
```

```
const placeWeWantToPutComponent = document.getElementById('hook');ReactDOM.render(<Container />, placeWeWantToPutComponent);
```

Les composants de classe doivent avoir une fonction appelée `render()`. La fonction render retourne le JSX du composant. Ils peuvent être utilisés de la même manière que les composants fonctionnels, comme ceci : `<AClassComponent />`.

Vous devriez utiliser des composants fonctionnels plutôt que des composants de classe car ils sont plus faciles à lire, sauf si vous avez besoin de l'_état_ du composant (plus d'informations à ce sujet bientôt).

### JavaScript dans JSX

Vous pouvez placer des variables JavaScript à l'intérieur de votre JSX comme ceci :

```
class Container extends React.Component {  render() {    const greeting = 'Je suis une chaîne de caractères !';    return (      <div>        <h1>{ greeting }</h1>        <OurFirstComponent />      </div>    );  }}
```

Maintenant, 'Je suis une chaîne de caractères !' sera à l'intérieur du `h1`.

Vous pouvez également faire des choses plus complexes, comme appeler une fonction :

```
class Container extends React.Component {  render() {    const addNumbers = (num1, num2) => {      return num1 + num2;    };    return (      <div>        <h1>La somme est : { addNumbers(1, 2) }</h1>        <OurFirstComponent />      </div>    );  }}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZwlZclRrqtIriczWzPP9-g.png)

### Pièges de JSX

Renommez `OurFirstComponent()` en `PlayButton`. Nous voulons qu'il retourne ce qui suit :

```
<a href="#" title="Lire la vidéo" class="play" />
```

Mais il y a un problème : `class` est un mot-clé en JavaScript, donc nous ne pouvons pas l'utiliser. Alors, comment donner à notre `<a>` une classe de `play` ?

Utilisez une propriété appelée `className` à la place :

```
<script type="text/babel">  function PlayButton() {    return <a href="#" title="Lire la vidéo" className="play" />;  }
```

```
  class Container extends React.Component {    render() {      return (        <div>          <PlayButton />        </div>      );    }  }
```

```
  const placeWeWantToPutComponent = document.getElementById('hook');  ReactDOM.render(<Container />, placeWeWantToPutComponent);</script>
```

### Ce que ce composant devrait faire

Les composants de classe peuvent stocker des informations sur leur situation actuelle. Ces informations sont appelées `state`, qui est stocké dans un objet JavaScript.

Dans le code ci-dessous, nous avons un objet représentant l'état de notre composant. Il a une `clé` de `isMusicPlaying` qui a une `valeur` de `false`. Cet objet est assigné à `this.state` dans la méthode `constructor`, qui est appelée lorsque la classe est utilisée pour la première fois.

```
class Container extends React.Component {  constructor(props) {    super(props);    this.state = { isMusicPlaying: false };  }    render() {    return (      <div>        <PlayButton />      </div>    );  }}
```

Une méthode `constructor` d'un composant React doit toujours appeler `super(props)` avant toute autre chose.

D'accord, alors que faisons-nous avec `state` ? Pourquoi existe-t-il ?

### Changer notre composant React en fonction de l'état

L'état est un moyen de mettre à jour notre UI en fonction des _événements_.

Dans ce tutoriel, nous utiliserons l'état pour changer le bouton de lecture de _pause_ à _lecture_ en fonction du clic de l'utilisateur sur le bouton de lecture.

Lorsque l'utilisateur clique sur le bouton, l'état sera mis à jour, ce qui mettra ensuite à jour l'UI.

Voici comment nous commençons. Nous pouvons regarder l'état du composant avec `this.state`. Dans le code suivant, nous regardons l'état et l'utilisons pour décider quel texte présenter à l'utilisateur.

```
class Container extends React.Component {  constructor(props) {    super(props);    this.state = { isMusicPlaying: false };  }
```

```
  render() {    const status = this.state.isMusicPlaying ? 'Lecture' : 'Pas de lecture';    return (      <div>        <h1>{ status }</h1>        <PlayButton />      </div>    );  }}
```

Dans la fonction render, `this` fait toujours référence au composant dans lequel elle se trouve.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eKhrsYzeEH-eoJbDtrVNpA.png)

Mais ce n'est pas très utile à moins que nous ayons un moyen de changer `this.state.isMusicPlaying`.

### Quand des choses arrivent à notre composant

L'utilisateur peut interagir avec nos composants en cliquant sur le bouton de lecture. Nous voulons réagir (ha... ha...) à ces événements.

Nous le faisons à travers des fonctions qui prennent en charge les événements. Nous appelons celles-ci des _gestionnaires d'événements_.

```
class Container extends React.Component {  constructor(props) {    super(props);    this.state = { isMusicPlaying: false };  }
```

```
  handleClick(event) {    // Faire quelque chose à propos du clic  };
```

```
  render() {    let status = this.state.isMusicPlaying     ? 'Lecture :)'     : 'Pas de lecture :(';    return (      <div>        <h1 onClick={this.handleClick.bind(this)}>{ status }</h1>        <PlayButton />      </div>    );  }}
```

Lorsque l'utilisateur clique sur le `h1`, notre composant exécutera la fonction `handleClick`. La fonction reçoit l'objet événement comme argument, ce qui signifie qu'elle peut l'utiliser si elle le souhaite.

Nous utilisons la méthode `.bind` sur `handleClick` pour nous assurer que `this` fait référence à l'ensemble du composant, plutôt qu'au seul `h1`.

### Ce que ce composant devrait faire

Lorsque nous changeons l'état de notre composant, il appellera à nouveau la fonction render.

Nous pouvons changer l'état avec `this.setState()`, si nous lui donnons un nouvel objet représentant le nouvel état.

Notre composant sur la page représentera toujours son état actuel. React fait cela pour nous.

```
handleClick() {    if (this.state.isMusicPlaying) {      this.setState({ isMusicPlaying: false });    } else {      this.setState({ isMusicPlaying: true });    }  };
```

Mais cliquer sur un `h1` n'est pas aussi bien que cliquer sur notre bouton de lecture. Faisons cela fonctionner.

### Communication entre les composants

Vos composants peuvent communiquer entre eux. Essayons.

Nous pouvons dire à `PlayButton` si la musique est en lecture ou non en utilisant quelque chose appelé `props`. Les props sont des informations partagées d'un composant parent à un composant enfant.

Les props en JSX ressemblent aux propriétés HTML.

Nous donnons à `PlayButton` une prop appelée `isMusicPlaying`, qui est la même que `isMusicPlaying` dans `this.state`.

```
class Container extends React.Component {  constructor(props) {    super(props);    this.state = { isMusicPlaying: false };  }
```

```
  handleClick() {    if (this.state.isMusicPlaying) {      this.setState({ isMusicPlaying: false });    } else {      this.setState({ isMusicPlaying: true });    }  };
```

```
  render() {    return (      <div>        <PlayButton isMusicPlaying={this.state.isMusicPlaying} />      </div>    );  }}
```

Lorsque l'état de `Container` change, la prop `PlayButton` changera également, et la fonction `PlayButton` sera appelée à nouveau. Cela signifie que notre composant sera mis à jour à l'écran.

À l'intérieur de `PlayButton`, nous pouvons réagir au changement, car `PlayButton` reçoit les props comme argument :

```
function PlayButton(props) {  const className = props.isMusicPlaying ? 'play active' : 'play';  return <a href="#" title="Lire la vidéo" className={className} />;}
```

Si nous changeons notre état en `this.state = { isMusicPlaying: true };` et rechargeons la page, vous devriez voir le bouton pause :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TmAo51JtJI-5pUiqUoQyVA.png)

### Événements en tant que props

Vos props n'ont pas besoin d'être uniquement des informations. Elles peuvent être des fonctions.

```
function PlayButton(props) {  const className = props.isMusicPlaying ? 'play active' : 'play';  return <a onClick={props.onClick} href="#" title="Lire la vidéo" className={className} />;}
```

```
class Container extends React.Component {  constructor(props) {    super(props);    this.state = { isMusicPlaying: false };  }
```

```
  handleClick() {    if (this.state.isMusicPlaying) {      this.setState({ isMusicPlaying: false });    } else {      this.setState({ isMusicPlaying: true });    }  };
```

```
  render() {    return (      <div>        <PlayButton           onClick={this.handleClick.bind(this)}           isMusicPlaying={this.state.isMusicPlaying}         />      </div>    );  }}
```

Maintenant, lorsque nous cliquons sur `PlayButton`, il changera l'état de `Container`, ce qui changera les `props` de `PlayButton`, ce qui provoquera sa mise à jour sur la page.

### Le problème avec setState

`setState` est mauvais car il ne fait pas les choses immédiatement. React attend un peu pour voir s'il y a d'autres changements à faire, puis il effectue les changements d'état.

Cela signifie que vous ne savez pas avec certitude quel sera votre état lorsque vous appelez `setState`.

Donc vous ne devriez pas faire ceci :

```
handleClick() {  this.setState({ isMusicPlaying: !this.state.isMusicPlaying });};
```

Si vous changez votre état en fonction de l'ancien état, vous devez faire les choses différemment.

Vous devez donner à `setState` une fonction, pas un objet. Cette fonction reçoit l'ancien état comme argument et retourne un objet qui est le nouvel état.

Cela ressemble à ceci :

```
handleClick() {  this.setState(prevState => {    return {       isMusicPlaying: !prevState.isMusicPlaying       };  });};
```

C'est plus difficile, mais nécessaire uniquement lorsque vous utilisez l'ancien état pour créer le nouvel état. Sinon, vous pouvez simplement donner à `setState` un objet.

### Qu'est-ce que les Refs ?

Faisons en sorte que de la musique se produise.

Tout d'abord, nous ajoutons une balise `<audio>` :

```
class Container extends React.Component {  constructor(props) {    super(props);    this.state = { isMusicPlaying: false };  }
```

```
  handleClick() {    this.setState(prevState => {      return {         isMusicPlaying: !prevState.isMusicPlaying         };    });  };
```

```
  render() {    return (      <div>        <PlayButton           onClick={this.handleClick.bind(this)}           isMusicPlaying={this.state.isMusicPlaying}         />        <audio id="audio" />      </div>    );  }}
```

Nous avons besoin d'un moyen d'obtenir cette balise `<audio>` et d'appeler soit `play()` soit `pause()` dessus. Nous pourrions le faire avec `document.getElementById('audio').play()` mais il y a une meilleure façon avec React.

Nous lui donnons une prop appelée `ref`, qui est appelée avec l'élément `<audio>` comme premier argument. Elle prend cet élément `<audio>` et l'assigne à `this.audio`.

```
<audio id="audio" ref={(audioTag) => { this.audio = audioTag }} />
```

Cette fonction sera appelée chaque fois que le `Container` est rendu, ce qui signifie que `this.audio` sera toujours à jour et égal à la balise `<audio>`.

Nous pouvons ensuite lire et mettre en pause la musique :

```
handleClick() {  if (this.state.isMusicPlaying) {    this.audio.pause();  } else {    this.audio.play();  }  this.setState(prevState => {    return {       isMusicPlaying: !prevState.isMusicPlaying       };  });};
```

Téléchargez un fichier musical (de préférence un fichier mp3) en utilisant le bouton `Choisir des fichiers` et appuyez sur lecture, et regardez-le fonctionner !

### Sortir de index.html

Comme vous l'avez peut-être deviné, notre React ne devrait pas vivre éternellement à l'intérieur d'une balise `<script>`.

React nécessite beaucoup de configuration de build. Heureusement, des outils comme [Create React App](https://github.com/facebookincubator/create-react-app) s'occupent de tout cela pour vous.

Installez-le pour créer votre propre projet React. Suivez leur bref tutoriel et commencez à modifier le JavaScript à l'intérieur du répertoire `src`, en appliquant toutes les connaissances React que vous avez apprises ici !

### Félicitations !

Vous pouvez maintenant créer des choses avec React.

Ensuite, consultez quelques articles pour plus d'informations. L'un porte sur les [bonnes pratiques React](https://engineering.musefind.com/our-best-practices-for-writing-react-components-dec3eb5c3fc8), l'autre sur une partie utile de React appelée [méthodes de cycle de vie](https://engineering.musefind.com/react-lifecycle-methods-how-and-when-to-use-them-2111a1b692b1).

Si vous avez appris quelque chose de cet article, veuillez cliquer sur ces mains qui applaudissent et le partager avec vos amis.

Vous pouvez également me suivre sur [Medium](https://medium.com/@scottdomes) et [Twitter](https://twitter.com/scottdomes).