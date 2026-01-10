---
title: Surlignage de saisie de texte, style TripAdvisor
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-02T23:35:50.000Z'
originalURL: https://freecodecamp.org/news/text-input-highlight-tripadvisor-style-2a44477de1b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0ugZlIdc2z-kl8O7Pjmq_Q.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Surlignage de saisie de texte, style TripAdvisor
seo_desc: 'By Petr Gazarov

  I was recently asked by a designer to create a text input style like the search
  input on TripAdvisor. I liked it a lot. I’m going to share my solution as a step-by-step
  guide so you can build it yourself.


  The implementation involves ...'
---

Par Petr Gazarov

Un designer m'a récemment demandé de créer un style de saisie de texte similaire à celui de la barre de recherche sur [TripAdvisor](https://www.tripadvisor.com/). J'ai beaucoup aimé. Je vais partager ma solution sous forme de guide étape par étape afin que vous puissiez le construire vous-même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wrX3xu1-98RjaZbHTezQuQ.png)

L'implémentation implique à la fois du CSS et du JavaScript. Pour notre version, je vais supposer que vous avez une connaissance de base de SCSS et React.

Voici le CodePen finalisé :

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="Surlignage de saisie Tripadvisor" src="//codepen.io/petrgazarov/embed/JyXvzB/?height=265&theme-id=0&default-tab=css,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  Voir le Pen <a href='https://codepen.io/petrgazarov/pen/JyXvzB/'>Surlignage de saisie Tripadvisor</a> par Petr Gazarov
  (<a href='https://codepen.io/petrgazarov'>@petrgazarov</a>) sur <a href='https://codepen.io'>CodePen</a>.
</iframe>

### Construisons-le

Tout d'abord, nous allons créer un simple composant React et le rendre dans le DOM :

```js
class App extends React.Component {
  render() {
    return (
      <div className='input-wrapper'>
        <input
          placeholder='Rechercher...'
          spellCheck={false}
        />
      </div>
    );
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

Ajoutons un peu de CSS :

```scss
$input-font-size: 30px;
$input-line-height: 70px;
$font-family: Roboto Slab, sans-serif;

body {
  background-color: #222222;
}

.input-wrapper {
  width: 500px;
  margin: 50px auto;
}

input {
  height: 60px;
  width: 100%;
  min-width: 100%;
  padding: 0;
  border-radius: 0;
  line-height: $input-line-height;
  background-color: transparent;
  color: white;
  font-size: $input-font-size;
  border: none;
  outline: none;
  border-bottom: 3px solid #333333;
  font-family: $font-family;
}
```

Ajoutez un conteneur HTML pour que ReactDOM puisse y rendre :

```html
<div id="root"></div>
```

Cela nous donne la saisie de texte de base avec une bordure inférieure.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rwd4CnYTGdL7hJ6J3YgUFg.png)

### Maintenant, donnons vie à la bordure !

La difficulté avec l'implémentation du surlignage est que la largeur doit être alignée avec la fin du texte. Elle doit également fonctionner avec n'importe quelle `font-family` et `font-size`.

Puisque la largeur de l'élément `input` est fixe, nous avons besoin d'une autre astuce pour détecter où se termine le texte à tout moment.

Disons que nous pouvons utiliser un deuxième élément avec une largeur **dynamique** — dans notre exemple, ce sera un élément `span` avec la classe `input-highlight`. Ensuite, nous allons copier le texte de l'input et le placer à l'intérieur du `span`.

J'ai basculé l'input de [non contrôlé à contrôlé](https://gist.github.com/markerikson/d71cfc81687f11609d2559e8daee10cc), en fournissant une prop `value`.

Notre composant React ressemble maintenant à ceci :

```js
class App extends React.Component {
  render() {
    return (
      <div className='input-wrapper'>
        <input
          placeholder='Rechercher...'
          spellCheck={false}
          value='saisie de base, bordure inférieure'
        />
        <span className='input-highlight'>
          saisie de base, bordure inférieure
        </span>
      </div>
    );
  }
}
```

Ajoutez les règles CSS suivantes pour `input-highlight`

**Note :** nous utilisons ici des variables SCSS pour nous assurer que les propriétés de `font` sont les mêmes entre `input` et `span` :

```scss
.input-highlight {
  font-size: $input-font-size;
  line-height: $input-line-height;
  font-family: $font-family;
  max-width: 100%;
}
```

Cela nous amène ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-HPjO9pbMNrmCtfX3JaP6Q.png)

Ensuite, ajoutons une bordure supérieure sur le `span` et positionnons-le de sorte que sa bordure se superpose à la bordure inférieure de l'input. De plus, puisque `input-highlight` a maintenant `position: absolute`, l'élément parent aura besoin de la règle `position: relative`.

```scss
.input-highlight {
  font-size: $input-font-size;
  line-height: $input-line-height;
  font-family: $font-family;
  max-width: 100%;
  
  border-top: 3px solid white;
  position: absolute;
  left: 0;
  bottom: 0;
  height: 0;
}

.input-wrapper {
  width: 500px;
  margin: 50px auto;
  position: relative;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*0ugZlIdc2z-kl8O7Pjmq_Q.png)
_Cool, n'est-ce pas ?_

L'élément span se termine avec le texte. Cela fait de sa largeur une mesure parfaite de la largeur du texte dans l'input !

Maintenant, la partie facile : utilisons JavaScript pour mettre à jour le texte dans le span chaque fois que le contenu de l'input change. Nous allons utiliser l'`state` de React pour mettre à jour la valeur de l'input et du span simultanément.

Voici notre composant mis à jour :

```js
class App extends React.Component {
  constructor() {
    super();
    
    this.state = {
      inputValue: ''
    };
    
    this.onInputChange = this.onInputChange.bind(this);
  }
  
onInputChange(e) {
    const { value } = e.target;
    
    this.setState({
      inputValue: value
    });
  }
  
render() {
    const { inputValue } = this.state;
    
    return (
      <div className='input-wrapper'>
        <input
          onChange={this.onInputChange}
          placeholder='Rechercher...'
          value={inputValue}
          spellCheck={false}
          />
        <span className='input-highlight'>
          { inputValue.replace(/ /g, "\u00a0") }
        </span>
      </div>
    );
  }
}
```

La partie `.replace(/ /g, "\u00a0")` est nécessaire pour que React gère correctement les espaces.

Ensuite, masquez le span en ajoutant les lignes suivantes au sélecteur CSS `input-highlight` :

```scss
color: transparent;
user-select: none;
overflow: hidden;
```

Nous avons besoin de `overflow: hidden` sur le span afin de limiter sa largeur (sinon, il fera s'étirer horizontalement le conteneur — merci à [Prasanna](https://www.freecodecamp.org/news/text-input-highlight-tripadvisor-style-2a44477de1b2/undefined) et [Andrea](https://www.freecodecamp.org/news/text-input-highlight-tripadvisor-style-2a44477de1b2/undefined) pour l'avoir souligné dans les commentaires !)

![Image](https://cdn-media-1.freecodecamp.org/images/1*WzFkT5CIV5W9Y7JUJpMRog.gif)

### Finalisons

Cela fonctionne déjà très bien. La dernière touche est d'ajouter une couleur différente pour le surlignage lors du `onFocus`.

Pour y parvenir, nous avons besoin d'un moyen de styliser le span en fonction de l'état de focus de l'input. L'input et le span sont des frères et sœurs, nous allons donc utiliser le sélecteur de frères et sœurs CSS (`+`).

Voici le code pour le sélecteur complet `input`, y compris le sélecteur de frères et sœurs pour `input-highlight` :

```scss
input {
  height: 60px;
  width: 100%;
  min-width: 100%;
  padding: 0;
  border-radius: 0;
  line-height: $input-line-height;
  background-color: transparent;
  color: white;
  font-size: $input-font-size;
  border: none;
  outline: none;
  border-bottom: 3px solid #333333;
  font-family: $font-family;
  
  &:focus {
    + .input-highlight {
      border-top: 3px solid #fbc91b;
    }
  }
}
```

Merci d'être resté jusqu'à la fin ! Si vous aimez cet article, partagez-le avec plus de personnes en le recommandant.