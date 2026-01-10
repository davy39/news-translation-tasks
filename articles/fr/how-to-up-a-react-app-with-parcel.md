---
title: Comment configurer une application React avec Parcel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-29T20:16:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-up-a-react-app-with-parcel
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c997b740569d1a4ca1ff3.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: Productivity
  slug: productivity
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: Comment configurer une application React avec Parcel
seo_desc: "By Bob Ziroll\nFor a long time Webpack was one of the biggest barriers-to-entry\
  \ for someone wanting to learn React. There's a lot of boilerplate configuration\
  \ that can be confusing, especially if you're new to React. \nEven in a talk trying\
  \ to show how..."
---

Par Bob Ziroll

Pendant longtemps, [Webpack](https://webpack.js.org/) a été l'un des plus grands obstacles pour ceux qui voulaient apprendre React. Il y a beaucoup de configuration de base qui peut être confuse, surtout si vous êtes nouveau dans React. 

Même dans [une conférence essayant de montrer à quel point React est facile à configurer](https://youtu.be/BXTU4NmMu8A?t=307), il peut être très difficile d'essayer d'apprendre chaque étape du processus de configuration.

Peu de temps après que React soit sorti de la version bêta, l'équipe de Facebook a créé [create-react-app](https://github.com/facebook/create-react-app). C'était une tentative de rendre le démarrage d'une application React (une version très complète) aussi simple que de taper une seule commande :

```js
npx create-react-app my-app
```

Super ! Et honnêtement, cette méthode de création d'une nouvelle application React est géniale si vous voulez quelque chose avec beaucoup de fonctionnalités dès le départ, **et** vous êtes d'accord pour que votre application commence comme une application assez lourde/volumineuse. 

Cette lourdeur vient des nombreuses dépendances, chargeurs, plugins, etc., automatiquement installés en tant que `node_modules` qui prennent beaucoup de place pour chaque application. L'image de résumé du Finder ci-dessous provient de l'une de mes applications create-react-app. ?

![Image](https://coursework.vschool.io/content/images/2020/07/node_modules.png)

![Image](https://coursework.vschool.io/content/images/2020/07/tfugj4n3l6ez.png)

## Présentation de Parcel

[Parcel](https://parceljs.org/) est un "Bundler d'applications web ultra-rapide, sans configuration". Cela signifie qu'il gère beaucoup de choses difficiles de bundling pour vous sous le capot **et** vous permet de créer une configuration relativement légère de React (ou tout autre projet web nécessitant du [bundling](https://medium.com/madhash/understanding-the-concept-of-bundling-for-beginners-f2db1adad724)).

Alors, voyons ce qu'il faut pour configurer l'application "Hello World" de base React qui affiche un élément `h1`.

### Étape 1 : Créez un nouveau dossier pour votre projet

Assez facile. ?

### Étape 2 : Créez votre fichier `package.json`

Dans le terminal, `cd` dans le nouveau dossier et exécutez :

```bash
npm init -y
```

Cela crée automatiquement le fichier `package.json`.

### Étape 3 : Installez Parcel, React et ReactDOM

```bash
npm install --save-dev parcel-bundler
# Version abrégée : npm i -D parcel-bundler

npm install react react-dom
# Version abrégée : npm i react react-dom
# Notez que npm enregistrera automatiquement les dépendances dans package.json maintenant, donc il n'est plus nécessaire de faire npm install --save ...
```

### Étape 4 : Ajoutez un script "start" à `package.json`

Dans le fichier `package.json`, dans la section "scripts", ajoutez le script "start" suivant :

```json
"start": "parcel index.html --open"
```

### Étape 5 : Créez le fichier `index.html` et ajoutez quelques lignes

Dans VS Code, vous pouvez créer un nouveau fichier appelé `index.html` et utiliser le raccourci intégré [emmet](https://code.visualstudio.com/docs/editor/emmet) pour créer un fichier HTML standard en tapant un point d'exclamation et en appuyant sur la touche Tab de votre clavier.

![Image](https://coursework.vschool.io/content/images/2020/07/Screen-Shot-2020-07-29-at-10.17.34-AM.png)
_Tapez ! et appuyez sur la touche Tab_

![Image](https://coursework.vschool.io/content/images/2020/07/Screen-Shot-2020-07-29-at-10.18.10-AM.png)
_? Abracadabra !_

Avant de continuer, nous devons ajouter 2 choses :

1. Un `div` de remplacement où notre application React sera insérée
2. Un `script` pour lire le fichier JavaScript d'entrée (que nous créerons ensuite)

Dans le `body` de `index.html`, ajoutez :

```html
<body>
    <div id="root"></div>
    <script src="./index.js"></script>
</body>
```

### Étape 6 : Créez le fichier `index.js`

Créez un nouveau fichier appelé `index.js` et entrez votre code React de base :

```js
// index.js
import React from "react"
import ReactDOM from "react-dom"

ReactDOM.render(<h1>Hello world!</h1>, document.getElementById("root"))

```

### Étape 7 : Démarrez !

C'est tout ! Maintenant, depuis le terminal, exécutez :

```bash
npm start
```

Parcel gérera le reste, et vous aurez une application React entièrement fonctionnelle.

## Conclusion

Si vous êtes intéressé, prenez le temps de [parcourir la documentation de Parcel](https://parceljs.org/getting_started.html) pour mieux comprendre toutes les fonctionnalités géniales qui accompagnent l'utilisation de Parcel, sans nécessiter de configuration de votre part. 

Dès la sortie de la boîte, Parcel prend en charge tous types d'extensions, de transpilers, de syntaxes courantes en développement web, et bien plus.

Bien qu'il ne soit pas _minuscule_, les node_modules d'une application Parcel prennent 50 % moins de place sur votre ordinateur :

![Image](https://coursework.vschool.io/content/images/2020/07/Screen-Shot-2020-07-29-at-10.31.58-AM.png)

Merci, Parcel !