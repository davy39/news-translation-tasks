---
title: REACT – Composant d'introduction simple ne s'affichant pas ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:18:00.000Z'
originalURL: https://freecodecamp.org/news/react-simple-intro-component-not-rendering
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a9b740569d1a4ca269e.jpg
tags:
- name: components
  slug: components
- name: React
  slug: react
- name: toothbrush
  slug: toothbrush
seo_title: REACT – Composant d'introduction simple ne s'affichant pas ?
seo_desc: 'One of the great things about React is its flexible component system. Once
  you get a hang of it, you can break up your application into reusable components
  and include them all over your project.

  The problem is that there are a few gotchas that make ...'
---

L'une des grandes forces de React est son système de composants flexible. Une fois que vous en avez saisi le fonctionnement, vous pouvez diviser votre application en composants réutilisables et les inclure partout dans votre projet.

Le problème est qu'il y a quelques pièges qui rendent le travail avec les composants difficile pour ceux qui débutent avec React.

Par exemple, supposons que vous avez le composant suivant, `mainIntro.js` :

```jsx
const mainIntro = props => (
    <div id="quote-box">
     <h1> Citations Hunter x Hunter </h1>

     <div id="text">
        "Quand je dis que cela ne me fait pas mal, cela signifie que je peux le supporter."
     </div>

     <div id="author">
        - Killua Zoldyck
     </div>

     <button id="new-quote"> Citation suivante </button>

     <a href="#" id="tweet-quote" target="_blank"> Tweeter cette citation </a>

    </div>
)

export default mainIntro;
```

Et vous souhaitez l'importer dans `App.js` :

```jsx
import mainIntro from './components'

class App extends React.Component{
    render(){
        return(
            <mainIntro />
        );
    }
}


const mainNode = document.getElementById("quoter");
ReactDOM.render(<App />,mainNode);
```

Mais `mainIntro` ne se charge pas pour une raison quelconque. Examinons de plus près ce qui se passe.

## Nommer vos composants

Pour ceux qui sont familiers avec la programmation orientée objet, il est courant de nommer chaque classe avec une lettre majuscule. Par exemple, une classe décrivant une personne serait appelée `Person` pour indiquer qu'il s'agit d'une classe.

Dans React, qui utilise JSX plutôt que JavaScript standard, la première lettre d'une balise indique le type d'élément. Les caractères initiaux en majuscule sont utilisés pour spécifier les composants React, donc `mainIntro` devrait plutôt s'appeler `MainIntro` :

```jsx
const MainIntro = props => (
    <div id="quote-box">
     <h1> Citations Hunter x Hunter </h1>

     <div id="text">
        "Quand je dis que cela ne me fait pas mal, cela signifie que je peux le supporter."
     </div>

     <div id="author">
        - Killua Zoldyck
     </div>

     <button id="new-quote"> Citation suivante </button>

     <a href="#" id="tweet-quote" target="_blank"> Tweeter cette citation </a>

    </div>
)

export default MainIntro;
```

Bien que le nom du fichier puisse rester `mainIntro.js`, il est judicieux de mettre une majuscule au premier caractère également. Plus tard, lorsque vous parcourrez le contenu du répertoire, vous pourrez rapidement identifier que `MainIntro.js` contient un composant.

Maintenant, `App.js` devrait ressembler à ceci :

```jsx
import MainIntro from './components/MainIntro.js';

class App extends React.Component{
    render(){
        return(
            <MainIntro />
        );
    }
}


const mainNode = document.getElementById("quoter");
ReactDOM.render(<App />,mainNode);
```

## Comment React est-il installé ?

Il existe deux principales façons d'utiliser React. Premièrement, l'installer et le configurer localement, probablement via `create-react-app`. Deuxièmement, via un CDN.

Vous avez peut-être remarqué ci-dessus que les extraits de code n'incluent pas réellement React dans le projet avec `import React from 'react'`. Cela générera une erreur si vous travaillez avec React localement.

Cependant, si vous utilisez un CDN pour charger React, il est disponible globalement et vous n'avez pas besoin de l'importer comme ci-dessus.

## Fonctions fléchées

Avant de plonger dans React, il est important d'avoir une solide compréhension de JavaScript, en particulier de la syntaxe ES6.

Jetez un autre coup d'œil au composant `MainIntro` :

```jsx
const MainIntro = props => (
    <div id="quote-box">
     <h1> Citations Hunter x Hunter </h1>

     <div id="text">
        "Quand je dis que cela ne me fait pas mal, cela signifie que je peux le supporter."
     </div>

     <div id="author">
        - Killua Zoldyck
     </div>

     <button id="new-quote"> Citation suivante </button>

     <a href="#" id="tweet-quote" target="_blank"> Tweeter cette citation </a>

    </div>
)

export default MainIntro;
```

Si vous regardez de près la première ligne, vous remarquerez une erreur de syntaxe :

```jsx
const MainIntro = props => (
```

Vous écrivez un composant fonctionnel, qui sont généralement des fonctions JavaScript simples pouvant accepter des props comme argument et retourner du JSX valide. Bien sûr, la syntaxe doit être correcte pour qu'il retourne correctement.

Les [fonctions fléchées](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) peuvent s'écrire de nombreuses manières, mais pour cet exemple, vous devrez ajouter les accolades (`{}`) et vous assurer de retourner du JSX depuis le composant lui-même :

```jsx
const MainIntro = props => {
  return (
    <div id="quote-box">
     //... reste du code   
    </div>
  );
}
```

Après avoir implémenté toutes les modifications mentionnées ci-dessus, votre composant devrait maintenant s'afficher correctement.

Bien que la principale distinction entre les composants fonctionnels et les composants de classe dans React était autrefois que les premiers étaient "sans état" tandis que les seconds étaient "avec état", les Hooks React ont brouillé les lignes entre eux. Lisez plus sur les deux types de composants dans cet [aperçu](https://www.freecodecamp.org/news/functional-components-vs-class-components-in-react/) et cette analyse approfondie des [composants fonctionnels avec les Hooks React](https://www.freecodecamp.org/news/a-few-questions-on-functional-components/).