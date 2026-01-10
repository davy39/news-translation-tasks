---
title: Comment créer un composant d'animation réutilisable avec React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-18T06:50:00.000Z'
originalURL: https://freecodecamp.org/news/animating-visibility-with-css-an-example-of-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/final-multiple-1.gif
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment créer un composant d'animation réutilisable avec React Hooks
seo_desc: "By Christian Sepulveda\nAnimations delight users. And you’d think, by the\
  \ sheer volume of articles, that React Hooks delight developers. But for me, fatigue\
  \ was starting to creep into my opinions on Hooks. \nBut serendipity saved me. I\
  \ found an example..."
---

Par Christian Sepulveda

Les animations ravissent les utilisateurs. Et vous penseriez, vu le nombre d'articles, que React Hooks ravissent les développeurs. Mais pour moi, la fatigue commençait à s'installer dans mes opinions sur les Hooks. 

Mais la sérendipité m'a sauvé. J'ai trouvé un exemple qui était bien adapté à React Hooks, plutôt que simplement « la nouvelle façon ». Comme vous l'avez peut-être deviné par le titre de cet article, cet exemple était une animation.

Je travaillais sur une application React avec des cartes dans une grille. Lorsque qu'un élément était supprimé, je voulais animer sa sortie, comme ceci.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/jd-delete.2019-07-12-19_32_00.gif)
_mon objectif_

Malheureusement, il y a des nuances à faire fonctionner cela. Et ma solution m'a conduit à une bonne utilisation de React Hooks.

## Que allons-nous faire ?

* commencer avec une application exemple de base
* animer progressivement la _disparition_ des éléments, en mettant en évidence certains défis
* une fois que nous avons obtenu l'animation souhaitée, nous allons refactoriser un composant d'animation réutilisable
* nous allons utiliser ce composant pour animer une barre latérale et une barre de navigation
* et … (vous devez lire / sauter à la fin)

Pour les impatients, voici le [dépôt GitHub](https://github.com/csepulv/animated-visibility) pour le code de ce projet. Il y a des tags pour chaque étape. (Voir README pour les liens et descriptions de chaque tag.)

## Base de référence

J'ai créé une application simple, en utilisant [_create-react-app_](https://facebook.github.io/create-react-app/)_._ Elle a une grille de cartes simples. Vous pouvez masquer des cartes individuelles.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/baseline.gif)
_pas d'animation — les éléments disparaissent trop vite_

Le code pour cela est basique et les résultats sont peu intéressants. Lorsque qu'un utilisateur clique sur le bouton de l'icône _eye_, nous changeons la propriété `display` de l'élément.

```js
function Box({ word }) {
  const color = colors[Math.floor(Math.random() * 9)];
  const [visible, setVisible] = useState(true);
  function hideMe() {
    setVisible(false);
  }
  let style = { borderColor: color, backgroundColor: color };
  if (!visible) style.display = "none";
  return (
    <div className="box" style={style}>
      {" "}
      <div className="center">{word}</div>{" "}
      <button className="button bottom-corner" onClick={hideMe}>
        {" "}
        <i className="center far fa-eye fa-lg" />{" "}
      </button>{" "}
    </div>
  );
}
```

(Oui, j'utilise des hooks ci-dessus, mais ce n'est pas l'utilisation intéressante des hooks.)

## Ajout de l'animation

Plutôt que de construire ma propre bibliothèque d'animation, j'ai cherché une bibliothèque d'animation comme [_animate.css_](https://daneden.github.io/animate.css/)_._ [_react-animated-css_](https://github.com/digital-flowers/react-animated-css) est une bibliothèque sympa qui fournit un wrapper autour de _animate.css._

`npm install --save react-animated-css`

ajouter _animate.css_ à `index.html`

```
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.css" />
```

Dans le composant `Box` ci-dessus, nous changeons son rendu en

```javascript
return (
  <Animated animationIn="zoomIn" animationOut="zoomOut" isVisible={visible}>
    <div className="box" style={style}>
      <div className="center">{word}</div>
      <button className="button bottom-corner" onClick={hideMe}>
        <i className="center far fa-eye fa-lg" />
      </button>
    </div>
  </Animated>
);
```

### Pas tout à fait ce que nous voulons

Mais _animate.css_ anime `opacity` et d'autres propriétés CSS ; vous ne pouvez pas faire une transition CSS sur la propriété `display`. Donc un objet invisible reste et il prend de la place dans le flux du document.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/animate-holes.gif)

Si vous [googler](https://www.google.com/search?q=animate+css+display+none&oq=animate+css+display) un peu, vous trouverez des solutions qui suggèrent d'utiliser un timer pour définir `display: none` à la fin de l'animation.

Nous pouvons donc ajouter cela,

```javascript
function Box({ word }) {
  const color = colors[Math.floor(Math.random() * 9)];
  const [visible, setVisible] = useState(true);
  const [fading, setFading] = useState(false);

  function hideMe() {
    setFading(true);
    setTimeout(() => setVisible(false), 650);
  }

  let style = { borderColor: color, backgroundColor: color };

  return (
    <Animated
      animationIn="zoomIn"
      animationOut="zoomOut"
      isVisible={!fading}
      style={visible ? null : { display: "none" }}
    >
      <div className="box" style={style}>
        <div className="center">{word}</div>
        <button className="button bottom-corner" onClick={hideMe}>
          <i className="center far fa-eye fa-lg" />
        </button>
      </div>
    </Animated>
  );
}
```

(Note : La durée d'animation par défaut est de 1000ms. J'utilise 650ms pour le timeout, pour minimiser un bégaiement/pause avant de définir la propriété `display`. C'est une question de préférence.)

Et cela nous donnera l'effet souhaité.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/animate-no-holes.gif)
_Youpi !_

## Création d'un composant réutilisable

Nous pourrions nous arrêter ici, mais il y a deux problèmes (pour moi) :

1. Je ne veux pas copier/coller le bloc `Animated`, les styles et les fonctions pour recréer cet effet
2. Le composant `Box` mélange différents types de logique, c'est-à-dire qu'il viole la [_Séparation des préoccuppations_](https://en.wikipedia.org/wiki/Separation_of_concerns)_._ Plus précisément, la fonction essentielle de `Box` est de rendre une carte avec son contenu. Mais les détails de l'animation sont mélangés.

### Composant de classe

Nous pouvons créer un composant de classe React traditionnel pour gérer l'état de l'animation : basculer la visibilité et définir le timeout pour la propriété CSS `display`.

```javascript
class AnimatedVisibility extends Component {
  constructor(props) {
    super(props);
    this.state = { noDisplay: false, visible: this.props.visible };
  }

  componentWillReceiveProps(nextProps, nextContext) {
    if (!nextProps.visible) {
      this.setState({ visible: false });
      setTimeout(() => this.setState({ noDisplay: true }), 650);
    }
  }

  render() {
    return (
      <Animated
        animationIn="zoomIn"
        animationOut="zoomOut"
        isVisible={this.state.visible}
        style={this.state.noDisplay ? { display: "none" } : null}
      >
        {this.props.children}
      </Animated>
    );
  }
}
```

et ensuite l'utiliser

```javascript
function Box({ word }) {
  const color = colors[Math.floor(Math.random() * 9)];
  const [visible, setVisible] = useState(true);

  function hideMe() {
    setVisible(false);
  }

  let style = { borderColor: color, backgroundColor: color };

  return (
    <AnimatedVisibility visible={visible}>
      <div className="box" style={style}>
        <div className="center">{word}</div>
        <button className="button bottom-corner" onClick={hideMe}>
          <i className="center far fa-eye fa-lg" />
        </button>
      </div>
    </AnimatedVisibility>
  );
}
```

Cela crée bien un composant réutilisable, mais c'est un peu compliqué. Nous pouvons faire mieux.

## React Hooks et useEffect

[React Hooks](https://reactjs.org/docs/hooks-intro.html) sont une nouvelle fonctionnalité de React 16.8. Ils offrent une approche plus simple pour la gestion du cycle de vie et de l'état dans les composants React.

Le hook [_useEffect_](https://reactjs.org/docs/hooks-effect.html) fournit un remplacement élégant à notre utilisation de `componentWillReceiveProps`. Le code est plus simple et nous pouvons utiliser à nouveau un composant fonctionnel.

```javascript
function AnimatedVisibility({ visible, children }) {
  const [noDisplay, setNoDisplay] = useState(!visible);
  useEffect(() => {
    if (!visible) setTimeout(() => setNoDisplay(true), 650);
    else setNoDisplay(false);
  }, [visible]);

  const style = noDisplay ? { display: "none" } : null;
  return (
    <Animated
      animationIn="zoomIn"
      animationOut="zoomOut"
      isVisible={visible}
      style={style}
    >
      {children}
    </Animated>
  );
}
```

Il y a quelques subtilités avec le hook _useEffect_. Il est principalement destiné aux effets secondaires : changement d'état, appel de fonctions asynchrones, etc. Dans notre cas, il définit le booléen interne `noDisplay` en fonction de la valeur précédente de `visible`.

En ajoutant `visible` au tableau des dépendances pour `useEffect`, notre hook `useEffect` ne sera appelé que lorsque la valeur de `visible` changera.

Je pense que _useEffect_ est une bien meilleure solution que l'encombrement du composant de classe. 💡

## Réutilisation du composant : barres latérales et barres de navigation

Tout le monde aime les barres latérales et les barres de navigation. Alors ajoutons-en une de chaque.

```javascript
function ToggleButton({ label, isOpen, onClick }) {
  const icon = isOpen ? (
    <i className="fas fa-toggle-off fa-lg" />
  ) : (
    <i className="fas fa-toggle-on fa-lg" />
  );
  return (
    <button className="toggle" onClick={onClick}>
      {label} {icon}
    </button>
  );
}

function Navbar({ open }) {
  return (
    <AnimatedVisibility
      visible={open}
      animationIn="slideInDown"
      animationOut="slideOutUp"
      animationInDuration={300}
      animationOutDuration={600}
    >
      <nav className="bar nav">
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
      </nav>
    </AnimatedVisibility>
  );
}

function Sidebar({ open }) {
  return (
    <AnimatedVisibility
      visible={open}
      animationIn="slideInLeft"
      animationOut="slideOutLeft"
      animationInDuration={500}
      animationOutDuration={600}
      className="on-top"
    >
      <div className="sidebar">
        <ul>
          <li>Item 1</li>
          <li>Item 2</li>
          <li>Item 3</li>
        </ul>
      </div>
    </AnimatedVisibility>
  );
}

function App() {
  const [navIsOpen, setNavOpen] = useState(false);
  const [sidebarIsOpen, setSidebarOpen] = useState(false);

  function toggleNav() {
    setNavOpen(!navIsOpen);
  }

  function toggleSidebar() {
    setSidebarOpen(!sidebarIsOpen);
  }

  return (
    <Fragment>
      <main className="main">
        <header className="bar header">
          <ToggleButton
            label="Sidebar"
            isOpen={sidebarIsOpen}
            onClick={toggleSidebar}
          />
          <ToggleButton label="Navbar" isOpen={navIsOpen} onClick={toggleNav} />
        </header>
        <Navbar open={navIsOpen} />
        <Boxes />
      </main>
      <Sidebar open={sidebarIsOpen} />
    </Fragment>
  );
}

```

![Image](https://www.freecodecamp.org/news/content/images/2019/07/final-multiple.gif)
_réutilisation réussie_

## Mais nous n'avons pas fini…

Nous pourrions nous arrêter ici. Mais comme pour mes commentaires précédents sur la _Séparation des préoccuppations_, je préférerais éviter de mélanger le composant `AnimatedVisibility` dans la méthode de rendu de `Box`, `Sidebar` ou `Navbar`. (C'est aussi une petite quantité de duplication.)

Nous pouvons créer un HOC. (En fait, j'ai écrit un article sur les animations et les HOCs, [_How to Build Animated Microinteractions in React_](https://medium.com/free-code-camp/how-to-build-animated-microinteractions-in-react-aab1cb9fe7c8)_._) Mais les HOCs impliquent généralement des composants de classe, en raison de la gestion de l'état.

Mais avec React Hooks, nous pouvons simplement composer le HOC (approche de programmation fonctionnelle).

```javascript
function AnimatedVisibility({
  visible,
  children,
  animationOutDuration,
  disappearOffset,
  ...rest
})
// ... même chose qu'avant
}


function makeAnimated(
  Component,
  animationIn,
  animationOut,
  animationInDuration,
  animationOutDuration,
  disappearOffset
) {
  return function({ open, className, ...props }) {
    return (
      <AnimatedVisibility
        visible={open}
        animationIn={animationIn}
        animationOut={animationOut}
        animationInDuration={animationInDuration}
        animationOutDuration={animationOutDuration}
        disappearOffset={disappearOffset}
        className={className}
      >
        <Component {...props} />
      </AnimatedVisibility>
    );
  };
}

export function makeAnimationSlideLeft(Component) {
  return makeAnimated(Component, "slideInLeft", "slideOutLeft", 400, 500, 200);
}

export function makeAnimationSlideUpDown(Component) {
  return makeAnimated(Component, "slideInDown", "slideOutUp", 400, 500, 200);
}

export default AnimatedVisibility
```

et ensuite utiliser ces HOCs basés sur des fonctions dans `App.js`

```javascript
function Navbar() {
  return (
    <nav className="bar nav">
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
    </nav>
  );
}

function Sidebar() {
  return (
    <div className="sidebar">
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
      </ul>
    </div>
  );
}

const AnimatedSidebar = makeAnimationSlideLeft(Sidebar);
const AnimatedNavbar = makeAnimationSlideUpDown(Navbar);

function App() {
  const [navIsOpen, setNavOpen] = useState(false);
  const [sidebarIsOpen, setSidebarOpen] = useState(false);

  function toggleNav() {
    setNavOpen(!navIsOpen);
  }

  function toggleSidebar() {
    setSidebarOpen(!sidebarIsOpen);
  }

  return (
    <Fragment>
      <main className="main">
        <header className="bar header">
          <ToggleButton
            label="Sidebar"
            isOpen={sidebarIsOpen}
            onClick={toggleSidebar}
          />
          <ToggleButton label="Navbar" isOpen={navIsOpen} onClick={toggleNav} />
        </header>
          <AnimatedNavbar open={navIsOpen} />
        <Boxes />
      </main>
      <AnimatedSidebar open={sidebarIsOpen} className="on-top"/>
    </Fragment>
  );
}
```

Au risque de promouvoir mon propre travail, je préfère beaucoup le code résultant propre.

Voici un sandbox du résultat final.

%[https://codesandbox.io/s/github/csepulv/animated-visibility]

## Et maintenant ?

Pour des animations simples, l'approche que je décris fonctionne bien. Pour des cas plus complexes, j'utiliserais des bibliothèques comme [_react-motion_](https://github.com/chenglou/react-motion)_._

Mais séparément des animations, React Hooks offre des opportunités de créer un code lisible et simple. Cependant, il y a un ajustement dans la façon de penser. Les hooks comme _useEffect_ ne sont pas un remplacement direct pour toutes les méthodes de cycle de vie. Vous devrez étudier et expérimenter.

Je suggère de regarder des sites comme [useHooks.com](https://usehooks.com/) et des bibliothèques comme [_react-use_](https://github.com/streamich/react-use), une collection de hooks pour une variété de cas d'utilisation.