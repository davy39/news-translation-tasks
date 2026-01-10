---
title: Comment importer des SVGs dans une application React et Vite
subtitle: ''
author: Israel Oyetunji
co_authors: []
series: null
date: '2022-07-01T22:15:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-import-svgs-in-react-and-vite
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Blog-article-cover-images--3-.png
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: SVG
  slug: svg
- name: vite
  slug: vite
- name: Web Development
  slug: web-development
seo_title: Comment importer des SVGs dans une application React et Vite
seo_desc: 'Are you having difficulties importing SVGs into your React app? This is
  a problem that many developers face, especially when setting up a new React app
  with a module bundler.

  In this article, I will share with you the different ways of importing SVGs...'
---

Avez-vous des difficultés à importer des SVGs dans votre application React ? C'est un problème auquel de nombreux développeurs sont confrontés, surtout lors de la configuration d'une nouvelle application React avec un module bundler.

Dans cet article, je vais partager avec vous les différentes façons d'importer des SVGs dans React, ainsi que le fonctionnement du processus sous le capot.

Commençons.

## Qu'est-ce qu'un SVG ?

SVG, abréviation de Scalable Vector Graphic, est un format d'image utilisé pour rendre des graphiques en deux dimensions (2D) sur Internet.

Le format SVG stocke les images sous forme de **vecteurs**, qui sont des graphiques composés de points, de lignes et de courbes basés sur la géométrie et des formules mathématiques.

Parce qu'ils sont basés sur des nombres et des valeurs plutôt que sur une grille de pixels comme les [images raster](https://en.wikipedia.org/wiki/Raster_graphics) (.png et .jpg), ils ne perdent pas en qualité lorsqu'ils sont zoomés ou redimensionnés.

Ils sont également parfaits pour créer des sites web responsives qui doivent bien paraître et fonctionner sur une variété de tailles d'écran.

Globalement, les SVGs sont excellents car ils sont scalables, légers, personnalisables et peuvent être animés en utilisant CSS lorsqu'ils sont utilisés [inline](#2utilisationsdesvgenlesajoutantdirectementenjsx).

## Comment importer des SVGs dans les applications React

Passons en revue certaines des méthodes les plus utilisées pour importer des SVGs dans les applications React.

### 1. Comment importer des SVGs en utilisant la balise Image

Importer des SVGs en utilisant la balise image est l'une des façons les plus simples d'utiliser un SVG. Si vous initialisez votre application en utilisant CRA (Create React App), vous pouvez importer le fichier SVG dans l'attribut source de l'image, car il le supporte dès le départ.

```jsx
import YourSvg from "/path/to/image.svg";

const App = () => {
  return (
    <div className="App">
      <img src={YourSvg} alt="Your SVG" />
    </div>
  );
};
export default App;
```

Mais si vous n'utilisez pas CRA, vous devez configurer un système de chargeur de fichiers dans le bundler que vous utilisez (Webpack, Parcel, Rollup, etc.).

Webpack, par exemple, dispose d'un chargeur pour gérer les SVGs appelé [file-loader](https://v4.webpack.js.org/loaders/file-loader/).

Pour installer le file-loader, ajoutez la commande suivante :

```bash
npm install file-loader --save-dev
```

Ensuite, ajoutez le chargeur au fichier `webpack.config.js` :

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          {
            loader: "file-loader",
          },
        ],
      },
    ],
  },
};
```

Maintenant, vous pouvez importer vos fichiers SVG et les utiliser :

```jsx
import YourSvg from "/path/to/image.svg";

const App = () => {
  return (
    <div className="App">
      <img src={YourSvg} alt="Your SVG" />
    </div>
  );
};
export default App;
```

NOTE : Bien que cette approche soit simple, elle présente un inconvénient : contrairement aux autres méthodes d'importation, vous ne pouvez pas styliser le SVG importé dans un élément `img`. Par conséquent, il sera adapté pour un SVG qui n'a pas besoin de personnalisation, comme les logos.

### 2. Comment importer des SVGs en les ajoutant directement en JSX

JSX supporte la balise `svg`, donc nous pouvons copier-coller le SVG directement dans nos composants React. Cette méthode est simple car elle vous permet de tirer pleinement parti des SVGs sans utiliser de bundler.

Cette approche est possible car les SVGs sont au format XML, tout comme HTML. Nous pouvons donc le convertir en syntaxe JSX. Vous pouvez également utiliser un [compilateur](https://transform.tools/html-to-jsx) au lieu de convertir manuellement.

```jsx
const App = () => {
  return (
    <div className="App">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        className="ionicon"
        viewBox="0 0 512 512"
      >
        <path
          d="M160 136c0-30.62 4.51-61.61 16-88C99.57 81.27 48 159.32 48 248c0 119.29 96.71 216 216 216 88.68 0 166.73-51.57 200-128-26.39 11.49-57.38 16-88 16-119.29 0-216-96.71-216-216z"
          fill="none"
          stroke="currentColor"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={32}
        />
      </svg>
    </div>
  );
};
export default App;
```

L'avantage d'inclure des SVGs en ligne est que nous avons accès à leurs différentes propriétés, ce qui nous permet de les styliser et de les personnaliser comme nous le souhaitons.

Une chose à garder à l'esprit est que si la taille de votre fichier SVG est grande, votre code peut devenir complexe, réduisant la lisibilité et la productivité. Si c'est le cas, utilisez un fichier png ou jpeg.

### 3. Comment importer des SVGs en tant que composants React

Si vous utilisez CRA, il est possible que vous ayez importé et utilisé des SVGs directement en tant que composant React à un moment donné.

Cette méthode, qui est possible grâce à un chargeur de fichiers, fonctionne en chargeant l'image avec le HTML plutôt que comme un fichier séparé.

```jsx
import { ReactComponent as Logo } from "./logo.svg";

const App = () => {
  return (
    <div className="App">
      <Logo />
    </div>
  );
};

export default App;
```

### 4. Comment convertir des SVGs en composants React

Cette approche est similaire à celle mentionnée précédemment. Ici, nous pouvons convertir un SVG en un composant React en le retournant depuis l'intérieur d'une classe ou d'un composant fonctionnel.

Pour ce faire, ouvrez le fichier SVG dans un éditeur de texte, et copiez-collez le code dans un nouveau composant :

```jsx
export const ArrowUndo = () => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      className="ionicon"
      viewBox="0 0 512 512"
    >
      <path d="M245.09 327.74v-37.32c57.07 0 84.51 13.47 108.58 38.68 5.4 5.65 15 1.32 14.29-6.43-5.45-61.45-34.14-117.09-122.87-117.09v-37.32a8.32 8.32 0 00-14.05-6L146.58 242a8.2 8.2 0 000 11.94L231 333.71a8.32 8.32 0 0014.09-5.97z" />
      <path
        d="M256 64C150 64 64 150 64 256s86 192 192 192 192-86 192-192S362 64 256 64z"
        fill="none"
        stroke="currentColor"
        strokeMiterlimit={10}
        strokeWidth={32}
      />
    </svg>
  );
};
```

Maintenant, vous pouvez importer et rendre le composant SVG dans un autre composant comme ceci :

```jsx
import { ArrowUndo } from "./path/to/ArrowUndo.jsx";

export const Button = () => {
  return (
    <button>
      <ArrowUndo />
    </button>
  );
};
```

Encore une fois, cette approche n'est possible que si votre application React dispose d'un chargeur comme le [Webpack loader](https://www.npmjs.com/package/@svgr/webpack) de SVGR.

### 5. Comment importer des SVGs en utilisant SVGR

[SVGR](https://react-svgr.com/) est un outil qui prend des fichiers SVG bruts et les transforme en composants React. Il dispose également d'un large écosystème avec support pour Create React App, Gatsby, Parcel, Rollup et d'autres technologies.

Alors, comment le configurer ?

Tout d'abord, installez le package en exécutant le code ci-dessous :

```bash
# avec npm
npm install --save-dev @svgr/webpack

# avec yarn
yarn add --dev @svgr/webpack
```

Ensuite, mettez à jour votre `webpack.config.js` :

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.svg$/i,
        issuer: /\.[jt]sx?$/,
        use: ["@svgr/webpack"],
      },
    ],
  },
};
```

Maintenant, vous pouvez importer un fichier SVG en tant que composant React :

```jsx
import Logo from "./logo.svg";

const App = () => {
  return (
    <div className="App">
      <Logo />
    </div>
  );
};

export default App;
```

### 6. Comment importer des SVGs en utilisant le plugin Vite pour SVGR

[`vite-plugin-svgr`](https://www.npmjs.com/package/vite-plugin-svgr) est un plugin pour Vite qui utilise svgr sous le capot pour transformer les SVGs en composants React.

Vous pouvez l'installer en exécutant la commande suivante :

```bash
# avec npm
npm i vite-plugin-svgr

# avec yarn
yarn add vite-plugin-svgr
```

Ensuite, ajoutez le plugin dans le fichier `vite.config.js` de votre application :

```js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import svgr from "vite-plugin-svgr";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svgr(), react()],
});
```

Maintenant, vous pouvez importer les fichiers SVG en tant que [composants React](#3importationsdesvgencomposantsreact) :

```jsx
import { ReactComponent as Logo } from "./logo.svg";
```

## Conclusion

Et c'est tout ! Dans cet article, nous avons couvert comment importer des SVGs dans une application React en utilisant une configuration personnalisée à partir de packages spécifiques, comment fonctionne l'importation de composants React et comment les utiliser dans une configuration Vite.

Lorsque je travaille avec Vite, j'utilise le plugin vite svgr, qui fonctionne sans faille. Vous pouvez également expérimenter avec les autres méthodes discutées dans cet article.

J'espère que vous avez trouvé cet article instructif. Si vous avez des questions, n'hésitez pas à envoyer un message sur [Twitter](https://twitter.com/israelmitolu) ou [LinkedIn](https://www.linkedin.com/in/israeloyetunji/).

Merci d'avoir lu, et bon codage !

Avant de partir, consultez ces ressources :

* [Pourquoi vous devriez abandonner Create-React-App pour Vite](https://israelmitolu.hashnode.dev/why-you-should-ditch-create-react-app-for-vite)

* [Travailler avec des SVGs dans React](https://rossbulat.medium.com/working-with-svgs-in-react-d09d1602a219)

* [Communauté Twitter pour les Devs](https://twitter.com/i/communities/1532313139810906114)