---
title: Comment styliser vos applications React avec moins de code en utilisant Tailwind
  CSS, Styled Components et Twin Macro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-15T10:45:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-style-your-react-apps-with-less-code-using-tailwind-css-and-styled-components
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/cover-1.png
tags:
- name: React
  slug: react
- name: styled-components
  slug: styled-components
- name: tailwind
  slug: tailwind
seo_title: Comment styliser vos applications React avec moins de code en utilisant
  Tailwind CSS, Styled Components et Twin Macro
seo_desc: 'By Ibrahima Ndaw

  Tailwind is a utility-first CSS framework for rapidly building custom designs. It
  can be used alone to style React Apps. However, it can be better combined with Styled
  Components. That combination brings the magic of Tailwind into CS...'
---

Par Ibrahima Ndaw

Tailwind est un framework CSS basé sur les utilitaires pour construire rapidement des designs personnalisés. Il peut être utilisé seul pour styliser des applications React. Cependant, il peut être mieux combiné avec Styled Components. Cette combinaison apporte la magie de Tailwind dans le CSS-in-JS.

Dans ce guide, nous allons construire un composant de formulaire sans écrire une seule ligne de CSS en utilisant Tailwind CSS, Styled Components et Twin Macro.

Plongeons-nous dedans !

* [Pourquoi l'utiliser ?](#heading-pourquoi-lutiliser)
* [Installation](#heading-installation)
* [Configuration de Tailwind CSS](#heading-configuration-de-tailwind-css)
* [Tailwind CSS et Styled Components](#heading-tailwind-css-et-styled-components)
* [Conclusion](#heading-conclusion)
* [Ressources](#heading-ressources)

## Pourquoi l'utiliser ?

Le "Pourquoi" est assez légitime et important, puisque nous pouvons utiliser soit Tailwind CSS, soit Styled Components. Alors pourquoi les combiner et utiliser les deux en même temps ?

Eh bien, les classes Tailwind peuvent être assez longues, et cela pose des problèmes de lisibilité à nos composants. Leur maintenance peut être difficile.

Dans le cas de Styled Components, il n'y a pas de problème sauf le fait que nous devons écrire le style. Ce n'est pas si problématique – mais pourquoi devrions-nous écrire quelque chose que Tailwind offre déjà ?

Il est donc logique d'utiliser Tailwind CSS en combinaison avec Styled Components. Tailwind CSS aide avec les classes utilitaires, et Styled Components garde nos composants propres avec l'aide du CSS-in-JS.

## Installation

Dans ce guide, nous allons construire un formulaire simple comme exemple. Et pour ce faire, nous avons besoin d'une nouvelle application React.

Alors, exécutons dans le terminal la commande suivante.

```shell
    npx create-react-app react-styled-tailwind

```

Ensuite, structurez votre dossier comme suit :

```
├── src
│  ├── App.js
│  ├── App.test.js
│  ├── assets
│  │  └── tailwind.css
│  ├── index.js
│  ├── serviceWorker.js
│  ├── setupTests.js
│  ├── tailwind.config.js
│  └── styles
│     └── index.js
├── babel.plugin.js
├── package.json
├── postcss.config.js
├── README.md
├── yarn-error.log
└── yarn.lock

```

Je vais expliquer chaque fichier au fur et à mesure, mais pour l'instant, installons les dépendances.

```shell
    yarn add -D tailwindcss twin.macro autoprefixer babel-plugin-macros postcss-cli

```

Ensuite, installez Styled Components en exécutant cette commande :

```shell
    yarn add styled-components

```

Une fois ces bibliothèques installées, nous pouvons maintenant passer à la configuration de Tailwind CSS.

## Configuration de Tailwind CSS

Pour le configurer, nous devons ajouter manuellement un fichier de configuration ou exécuter la commande suivante pour en générer un nouveau :

```shell
    npx tailwind init src/tailwind.config.js

```

Ici, au lieu de générer le fichier de configuration dans le répertoire racine, vous devez le placer dans le dossier `src` – sinon une erreur sera lancée par Tailwind Macro.

Et le fichier généré ressemblera à ceci :

* `tailwind.config.js`

```js
module.exports = {
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
}

```

Comme vous pouvez le voir, le fichier de configuration est "vide" puisque aucune configuration n'est présente. Pour ce tutoriel, nous n'avons pas besoin de configurer quoi que ce soit ici. Mais vous pouvez le personnaliser pour répondre à vos besoins ou exécuter la commande avec l'option `--full` pour obtenir la configuration complète de Tailwind.

Ensuite, nous devons créer un nouveau fichier `postcss.config.js` dans le répertoire racine.

* `postcss.config.js`

```js
module.exports = {
  plugins: [
    require("tailwindcss")("./src/tailwind.config.js"),
    require("autoprefixer"),
  ],
}

```

Cette configuration indique au fichier `postcss.config.js` d'utiliser la bibliothèque Tailwind CSS et le fichier `tailwind.config.js` pendant la compilation. Avec l'aide d'`autoprefixer`, il suit les propriétés qui doivent être préfixées.

Avec cette configuration, nous pouvons maintenant passer au fichier `babel.plugin.js` qui aide à transformer les classes Tailwind en code CSS-in-JS.

* `babel.plugin.js`

```js
module.exports = {
  tailwind: {
    plugins: ["macros"],
    config: "./src/tailwind.config.js",
    format: "auto",
  },
}

```

Plus tard, nous verrons en action ce que fait ce fichier. Mais pour l'instant, retenez simplement qu'il fait le lien entre Tailwind CSS et Styled Components.

_Il ne reste que trois dernières étapes à faire pour terminer l'installation._

![still](https://media.giphy.com/media/tXL4FHPSnVJ0A/source.gif)

Tout d'abord, dans le fichier `tailwind.css`, nous devons importer certaines utilités de la bibliothèque Tailwind.

* `src/assets/tailwind.css`

```css
@tailwind base;

@tailwind components;

@tailwind utilities;

```

Ici, comme vous pouvez le voir, il n'y a rien de compliqué, juste quelques imports qui nous permettent d'utiliser les classes utilitaires de Tailwind.

La deuxième étape consiste à connecter notre application React avec Tailwind CSS.

* `index.js`

```js
import React from "react"
import ReactDOM from "react-dom"
import App from "./App"
import "./assets/styles.css"
import * as serviceWorker from "./serviceWorker"

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
)

serviceWorker.unregister()

```

Ici, nous importons `assets/styles.css` qui contient le style CSS. Et plus tard, nous modifierons légèrement le script par défaut pour construire le CSS et l'ajouter au fichier `assets/styles.css` pendant la compilation.

Et enfin, mais non des moindres, nous devons mettre à jour le fichier `package.json`.

* `package.json`

```js
"scripts": {
    "build:css": "postcss src/assets/tailwind.css -o src/assets/styles.css",
    "watch:css": "postcss src/assets/tailwind.css -o src/assets/styles.css",
    "start": "npm run watch:css & react-scripts start",
    "build": "npm run build:css react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
 }

```

Ces deux scripts `build:css` et `watch:css` construiront respectivement le CSS et surveilleront les changements pour le reconstruire si nécessaire. Et comme je l'ai dit plus tôt, le fichier de sortie sera situé dans le dossier `assets`.

Avec ce changement, nous pouvons maintenant utiliser Tailwind dans notre application. Combinons-le maintenant avec Styled Components.

## Tailwind CSS et Styled Components

Plus tôt, dans notre structure de dossier, nous avions un dossier `styles`. Il est temps de le modifier avec le code suivant.

* `styles/index.js`

```js
import styled from "styled-components"
import tw from "twin.macro"

const StyledForm = styled.main.attrs({
  className: "flex flex-col h-screen justify-center items-center bg-gray-100",
})`
  & {
    form {
      ${tw`bg-white text-center rounded py-8 px-5 shadow max-w-xs`}
    }
    input {
      ${tw`border-gray-300 mb-4 w-full border-solid border rounded py-2 px-4`}
    }
    button {
      ${tw`bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 border border-blue-700 rounded`}
    }
  }
`
export default StyledForm

```

Nous commençons par importer `tw` qui nous permet d'utiliser les classes Tailwind dans les propriétés imbriquées. Il est parfaitement acceptable d'utiliser les classes utilitaires avec l'attribut `className`, mais si vous souhaitez imbriquer des propriétés, vous devez utiliser la bibliothèque `twin.macro`.

Cette bibliothèque utilisera la configuration du plugin babel macros (`babel.plugin.js`) pour transformer les classes utilitaires Tailwind CSS utilisées par les sélecteurs imbriqués en code lisible que Styled Components peut comprendre.

Vous pouvez voir dans cet exemple ci-dessous comment la transformation est effectuée.

```js
// entrée
const test = ${tw`text-center bg-red w-full`}
// sortie
const test = {
    background: 'red',
    textAlign: 'center',
    width: '100%'
}

```

Super ! Maintenant que nous avons combiné Tailwind avec Styled Components, ajoutons le composant stylisé au fichier `App.js`.

* `App.js`

```js
import React from "react"
import StyledForm from "./styles"

function App() {
  return (
    <StyledForm>
      <form>
        <input type="text" placeholder="Nom complet" />
        <input type="text" placeholder="Email" />
        <input type="text" placeholder="Mot de passe" />
        <button>S'inscrire</button>
      </form>
    </StyledForm>
  )
}

export default App

```

Ici, nous avons simplement importé le composant stylisé et tout enveloppé avec pour rendre notre formulaire beau.

![Image d'un formulaire React stylisé avec Tailwind](https://www.freecodecamp.org/news/content/images/2021/10/react-tailwind-form.png)

Super ! Vous pouvez déjà voir à quel point cette combinaison est puissante. Nous avons construit un composant de formulaire sans écrire une ligne de CSS et le composant reste lisible.

## Conclusion

Il y a un peu de tracas pour configurer Tailwind CSS. Mais une fois que c'est fait et combiné avec CSS-in-JS, c'est vraiment puissant et flexible. Cela est en partie dû au fait que nous pouvons personnaliser le fichier `tailwind.config.js` pour répondre à nos besoins ou simplement écrire du CSS normal comme nous le faisons habituellement avec Styled Components. C'est définitivement quelque chose à considérer dans votre prochaine application React.

Merci d'avoir lu !

Vous pouvez trouver le [Code Source ici](https://github.com/ibrahima92/react-styled-tailwind).

[Lire plus de mes articles](https://www.ibrahima-ndaw.com/)

[Abonnez-vous à ma newsletter](https://ibrahima-ndaw.us5.list-manage.com/subscribe?u=8dedf5d07c7326802dd81a866&id=5d7bcd5b75)

[Suivez-moi sur twitter](https://twitter.com/ibrahima92_)

## Ressources

[Documentation de Tailwind CSS](https://tailwindcss.com/docs/installation/)

[Feuille de triche Tailwind CSS](https://nerdcave.com/tailwind-cheat-sheet)

[Documentation de Twin Macro](https://github.com/ben-rogerson/twin.macro)

[Documentation de Styled Components](https://styled-components.com/docs)