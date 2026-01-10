---
title: Comment construire un visualiseur Markdown avec React.js
subtitle: ''
author: Ashutosh K Singh
co_authors: []
series: null
date: '2020-06-02T17:48:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-markdown-previewer-with-react-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/markdown-previewer.png
tags:
- name: markdown
  slug: markdown
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: Comment construire un visualiseur Markdown avec React.js
seo_desc: Building actual projects is a great way to learn React and solidify some
  of its basic principles. So in this post we will be building a simple Markdown Previewer
  like what you see in the image above. This will be a simple react app which will
  contain...
---

Construire des projets concrets est une excellente façon d'apprendre React et de solidifier certains de ses principes de base. Dans cet article, nous allons donc construire un simple visualiseur Markdown comme celui que vous voyez dans l'image ci-dessus. Ce sera une application React simple qui contiendra une zone de texte pour l'entrée Markdown et un onglet de prévisualisation où le texte converti apparaîtra.

Si vous souhaitez plonger directement dans le code, consultez le dépôt GitHub ici : [https://github.com/lelouchB/markdown-previewer/tree/master](https://github.com/lelouchB/markdown-previewer/tree/master)

Et voici un lien vers la version déployée : [https://markdown-previewer.lelouch-b.now.sh/](https://markdown-previewer.lelouch-b.now.sh/).

Maintenant, commençons.

## Prérequis

1. Connaissance de HTML, CSS, Javascript et Bootstrap.
2. Connaissance de base de React.
3. Node et NPM installés sur votre machine de développement locale.
4. Un éditeur de code de votre choix.

Si vous avez l'impression que votre progression est entravée parce que vous ne connaissez pas suffisamment ces sujets, consultez [https://www.freecodecamp.org/learn](https://www.freecodecamp.org/learn). Il y a des modules géniaux là-bas qui vous feront démarrer en un rien de temps.

## Installation

Nous allons construire cette application avec l'aide de `npx create-react-app`. **Create React App** est un moyen officiellement soutenu de créer des applications React à page unique. Il offre une configuration de construction moderne sans configuration.

Dans votre répertoire de projet, exécutez la commande suivante dans le terminal :

```
npx create-react-app markdown-previewer
cd markdown-previewer
npm start
```

Ensuite, ouvrez [http://localhost:3000/](http://localhost:3000/) pour voir votre application. Elle ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot_2020-05-30-React-App.png)
_http://localhost:3000/_

Maintenant, voyons la **Structure du Projet** ici :

```
markdown-previewer
├── README.md
├── node_modules
├── package.json
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    └── serviceWorker.js
```

Aucune configuration ou structures de dossiers compliquées – seulement les fichiers dont vous avez besoin pour construire votre application.

Maintenant, avant de continuer, nettoyons ces fichiers :

1. Supprimez `index.css` et `App.css`.
2. Puisque nous avons supprimé `index.css` et `App.css`, retirez `import './index.css';` et `import './App.css';` de `index.js` et `App.js` respectivement.
3. Supprimez `logo.svg` et retirez `import logo from './logo.svg';` dans `App.js`.
4. À l'intérieur de `App.js`, retirez la fonction `App()`. Nous allons exporter un composant de classe plutôt qu'un composant fonctionnel. Changez donc `App.js` pour qu'il ressemble à ceci :

```js
import React from 'react';

export default class App extends React.Component{
  render(){
    return (
      <div className="App">
      
      </div>
    );}
}

```

Allez sur [http://localhost:3000](http://localhost:3000) et il sera maintenant vide.

## Conception

Mais une chose de plus avant de nous lancer... Il est toujours bon d'avoir un plan de ce que vous allez construire avant de commencer à taper. Surtout lorsque vous construisez une interface utilisateur avec React.

Nous voulons avoir une idée de ce à quoi ressemblera l'interface afin de savoir quels composants nous devons construire et quelles données chaque composant sera responsable de gérer.

Pour commencer, j'ai dessiné un croquis rapide de ce à quoi ressemblera l'application markdown-previewer. J'ai également étiqueté tous les composants que nous devrons créer :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-177.png)
_Conception_

Il semble donc que nous devrons construire trois composants principaux :

1. **Titre et Sous-titre** — Cela affichera simplement nos titres et sous-titres.
2. **Zone de texte d'entrée Markdown** — C'est la zone de texte d'entrée où le markdown que nous voulons prévisualiser sera écrit.
3. **Prévisualisation Markdown** — C'est un conteneur avec un fond grisâtre où la sortie sera affichée.

### Quelques points à noter :

1. Nous aurons un composant « App » qui contient tout. Ce projet est petit, il est donc facile de maintenir tous les composants dans un seul fichier. Mais à mesure que la taille de votre projet augmente (par exemple, lors de la construction d'une plateforme e-Commerce), vous devrez séparer les composants dans différents fichiers et dossiers par leurs types.
2. Puisque cet article ne traite pas de CSS et de conception, j'utiliserai la bibliothèque [React-Bootstrap](https://react-bootstrap.github.io/) et les styles en ligne. Toute discussion à leur sujet sera brève.

### Styles en ligne dans React

Lorsque vous utilisez des styles en ligne, cela signifie qu'au lieu de créer des fichiers CSS séparés, les composants sont stylisés en passant les propriétés CSS sous forme d'objet. Par exemple :

```js
var divStyle = {
  color: 'white',
  backgroundImage: 'url(' + imgUrl + ')',
  WebkitTransition: 'all', // notez le 'W' majuscule ici
  msTransition: 'all' // 'ms' est le seul préfixe de fournisseur en minuscules
};

ReactDOM.render(<div style={divStyle}>Hello World!</div>, document.getElementById("root");
```

Les clés de style sont en camelCase afin d'être cohérentes avec l'accès aux propriétés sur les nœuds DOM depuis JS (par exemple, `node.style.backgroundImage`). Les préfixes de fournisseur autres que `ms` doivent commencer par une lettre majuscule. C'est pourquoi `WebkitTransition` a un "W" majuscule.

L'objet de style est ensuite passé dans le composant DOM en utilisant `{}` . Nous pouvons exécuter du code Javascript à l'intérieur de notre méthode `return` en utilisant `{}`.

## Code

D'accord, il est temps de commencer à écrire du code ! Si à un moment donné vous êtes bloqué, n'hésitez pas à vous référer à l'application terminée ici : [https://github.com/lelouchB/markdown-previewer/tree/master](https://github.com/lelouchB/markdown-previewer/tree/master) et [https://markdown-previewer.lelouch-b.now.sh/](https://markdown-previewer.lelouch-b.now.sh/)

### Installation des dépendances

Commençons par installer les dépendances de notre projet. À l'intérieur du répertoire du projet, exécutez les commandes suivantes :

```
npm install react-bootstrap bootstrap 
npm install marked
```

Maintenant, discutons d'eux :

1. La première commande installe [React-Bootstrap](https://react-bootstrap.github.io/getting-started/introduction) et Bootstrap que nous utiliserons pour styliser notre projet.
2. La deuxième commande installe [Marked.js](https://marked.js.org), qui est un compilateur markdown de bas niveau pour analyser le markdown sans mise en cache ou blocage pendant de longues périodes. Cela exécutera la logique réelle derrière la conversion du markdown.

Avant de commencer à utiliser React-Bootstrap dans notre projet, nous devrons ajouter le fichier CSS bootstrap minifié à notre `index.js` :

```js
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

```

Avec cela, les dépendances ont été installées et sont prêtes à être utilisées.

### Titres

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-178.png)

Notre première tâche sera d'ajouter un titre à notre application React et de le centrer. Pour cela, nous utiliserons [Badge](https://react-bootstrap.github.io/components/badge/), un composant de la bibliothèque React-Bootstrap. Voici les étapes à suivre :

1. Importez Badge dans `App.js`. À l'intérieur de `App.js`, ajoutez ce qui suit :

```js
import Badge from "react-bootstrap/Badge";

```

2. Dans `App.js`, à l'intérieur de return et sous le `div` avec le `className="App"`, ajoutez un autre `div` avec le `className="container"`.

```js
import React from "react";
import Badge from "react-bootstrap/Badge";

export default class App extends React.Component {
  render() {
    return (
      <div className="App">
        <div className="container">
   
        </div>
      </div>
    );
  }
}

```

3. Ensuite, à l'intérieur du div avec le `className="container"`, nous ajouterons le titre comme suit :

```
 <h1>
 <Badge className="text-align-center" variant="light">
 Visualiseur Markdown
</Badge>
 </h1>
```

4. Vous pouvez maintenant voir un titre sur [http://localhost:3000](http://localhost:3000), mais il n'est pas centré. Pour centrer le titre, nous utiliserons bootstrap et envelopperons le bloc de code ci-dessus dans deux divs.

```
<div className="row mt-4">
  <div className="col text-center">
    <h1>
     <Badge className="text-align-center" variant="light">
        Visualiseur Markdown
     </Badge>
    </h1>
  </div>
</div>
```

Avec cela, nous avons ajouté un titre à notre application.

### Sous-titres

Si vous regardez la conception dont nous parlons ci-dessus, vous verrez que l'étape suivante sera d'ajouter deux colonnes avec les sous-titres **Entrée Markdown** et **Prévisualisation**. L'une contiendra la zone de texte d'entrée et l'autre la prévisualisation.

1. Tout d'abord, nous devrons créer deux colonnes placées côte à côte dans notre application. Nous le ferons en utilisant bootstrap. À l'intérieur du div conteneur, ajoutez ce qui suit :

```js

<div className="row mt-4">
  <div className="col-md-6">
    <h2>Lorem Ipsum</h2>
  </div>

  <div className="col-md-6">
    <h2>Lorem Ipsum</h2>
  </div>
</div>;

```

J'ai utilisé Lorem Ipsum pour l'instant, et je le supprimerai à l'étape suivante. Les colonnes sont créées en utilisant les classes bootstrap, et le premier `div` avec `className="row mt-4"` crée une **ligne**. Le `m` indique `margin`. Le `t` indique `top`. Les deux autres `div` avec `className="col-md-6"` créent **deux colonnes**.

L'application ressemblera maintenant à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-180.png)

2. L'étape suivante sera d'ajouter des titres à ces colonnes et de les centrer. Cela peut être fait en ajoutant un div avec le className="col text-center" à l'intérieur de ce Badge, aux deux divs avec le `className="col-md-6"`.

```
<div className="col text-center">
  <h1>
    <Badge className="text-align-center" variant="light">
    // Sous-titre réel : Ce bloc de code sera le même pour les deux colonnes
    </Badge>
  </h1>
</div>

```

3. Votre `App.js` ressemblera maintenant à ceci :

<script src="https://gist.github.com/lelouchB/a9c1d79cca4ec36fe02328feb245d6f8.js"></script>

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-181.png)

### Zone de texte

Ensuite, nous allons ajouter une zone de texte dans notre application. Nous utiliserons la simple balise HTML `<textarea>` pour ce faire.

1. Ajoutez un autre div avec le `classname="mark-input"` et ajoutez `textarea` avec `className="input"` à l'intérieur.

```
<div className="mark-input">
  <textarea className="input"> </textarea>
</div>;

```

2. Personnalisons un peu la zone de texte. Comme discuté ci-dessus, nous utiliserons les styles en ligne, donc pour cela, initialisons d'abord un **Objet**. Toutes les variables seront déclarées à l'intérieur de la fonction `render()` mais à l'extérieur de `return`. Par exemple,

```
render(){
 var variableOne = "Lorem Ipsum"
 var variableTwo = "Lorem Ipsum"

  return(
   // Code
   )
}
```

3. Voici l'objet `inputStyle` :

```
 var inputStyle = {
      width: "400px",
      height: "50vh",
      marginLeft: "auto",
      marginRight: "auto",
      padding:"10px"
    };
```

4. Ajoutons l'objet `inputStyle` à notre `textarea` :

```
<div className="mark-input" style={inputStyle}>
<textarea
  className="input"
  style={inputStyle}></textarea>
```

Avec cela, nous avons ajouté une zone de texte à notre application et elle ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-182.png)

### Prévisualisation

Pour séparer notre prévisualisation du reste de l'application et pour l'enfermer dans un conteneur, nous suivrons le processus ci-dessus. Nous créerons un div à l'intérieur de la deuxième colonne et ajouterons un objet de style, comme ceci :

```
  var outputStyle = {
      width: "400px",
      height: "50vh",
      backgroundColor: "#DCDCDC",
      marginLeft: "auto",
      marginRight: "auto",
      padding:"10px"
    };

```

Ajoutez l'objet au `div` :

```
<div className="col-md-6">
  <div className="col text-center">
    <h4>
      <Badge className="text-align-center" variant="secondary">
        Prévisualisation
      </Badge>
    </h4>
  </div>
  <div style={outputStyle}>
  </div>
</div>

```

Voici à quoi ressemblera l'application maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-183.png)

Nous avons maintenant terminé l'apparence de notre application, mais il lui manque sa fonctionnalité, alors ajoutons cela. Le processus à partir d'ici peut être divisé en trois étapes :

1. Prendre l'entrée de la zone de texte.
2. Passer l'entrée à la bibliothèque Marked.js et afficher les données traitées dans la colonne **Prévisualisation**.

## Prendre l'entrée de la zone de texte

Nous utiliserons l'objet `state`.

### [State](https://reactjs.org/docs/state-and-lifecycle.html)

Dans React, le « state » est un objet qui représente les parties de l'application qui peuvent changer. Chaque composant peut maintenir son propre état, qui vit dans un objet appelé `this.state`. L'objet `state` est l'endroit où vous stockez les valeurs de propriété qui appartiennent au composant.

En termes simples, si vous voulez que votre application fasse quoi que ce soit — si vous voulez de l'interactivité, ajouter et supprimer des choses, vous connecter et vous déconnecter — cela impliquera l'état.

Ici, la **valeur** de notre zone de texte change, et notre état changera avec elle. Nous ajouterons l'objet state à l'intérieur de notre **classe App**, au-dessus de la fonction `render()`.

Il est considéré comme une bonne pratique d'initialiser `state` à l'intérieur du `constructor`. Cela peut fonctionner sans `constructor`, mais vous devriez éviter cela. Voici comment nous allons l'initialiser avec la propriété `markdown`, initialement avec une chaîne vide :

```
export default class App extends React.Component {
constructor(props){
    super(props)
    this.state = {
      markdown: "",
    };
  }
  render(){
  // méthode et autre code
  }
  }
```

Dans ce projet ou dans tout autre projet React, initialisez toujours `state` à l'intérieur de `constructor(props)` et en dessous de `super(props)`.

Typiquement, dans React, les constructeurs ne sont utilisés que pour deux objectifs :

* Initialiser l'état local en assignant un objet à `this.state`.
* Lier les méthodes de gestion d'événements à une instance.

Gardez à l'esprit que le Constructeur est le seul endroit où vous devez assigner `this.state` directement. Dans toutes les autres méthodes, vous devez utiliser `this.setState()` à la place.

Les changements d'état sont asynchrones. Pour de meilleures performances perçues, React peut le retarder, puis mettre à jour plusieurs composants en une seule passe. React ne garantit pas que les changements d'état sont appliqués immédiatement.

Comme discuté ci-dessus, nous ne pouvons pas changer l'état directement. Au lieu de cela, nous devons utiliser `this.setState()`, alors créons une méthode qui fait cela et qui est appelée chaque fois que la valeur de la zone de texte est changée.

```
  updateMarkdown(markdown) {
    this.setState({ markdown });
  }
```

Cette méthode est créée à l'intérieur du composant de classe mais au-dessus de la fonction `render()`.

Mais nous allons d'abord définir la valeur de la zone de texte sur la propriété `markdown` dans l'état.

```
<textarea className="input" style={inputStyle} value={this.state.markdown}></textarea>

```

Maintenant, nous pouvons ajouter `updateMarkdown()` à l'événement `onChange()` à l'intérieur de `<textarea>` et l'appeler `this.updateMarkdown()`.

```
<textarea
  className="input"
  style={inputStyle}
  value={this.state.markdown}
  onChange={(e) => {
    this.updateMarkdown(e.target.value);
  }}
></textarea>;

```

Ensuite, nous pouvons vérifier si l'état est correctement assigné en passant un code Javascript et en faisant un `console.log()` de notre état.

```
<textarea
  className="input"
  style={inputStyle}
  value={this.state.markdown}
  onChange={(e) => {
    this.updateMarkdown(e.target.value);
  }}
>
  {console.log(this.state.markdown)}
</textarea>;

```

Maintenant, ouvrez votre console et essayez d'écrire dans la zone de texte, et espérons que vous verrez la même chose être ajoutée à la console.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-184.png)
_Vérification_

Avec cela, nous avons réussi à assigner l'entrée de la zone de texte à notre propriété markdown de l'état. Voici à quoi ressemblera votre `App.js` maintenant :

<script src="https://gist.github.com/lelouchB/5bcc4540e7dbde9f4f4415c0a3dff3c8.js"></script>

## Marked.js

Marked.js est le cerveau derrière la conversion du markdown et est très simple à utiliser.

Importation de `marked`, ajoutez ce qui suit juste en dessous de l'endroit où vous avez importé Badge depuis `react-bootstrap/Badge`

```
let marked = require("marked");

```

Pour utiliser la bibliothèque Marked.js, nous devons simplement passer la chaîne à convertir à l'intérieur de la fonction `marked()`. Nous avons déjà les données stockées dynamiquement à l'intérieur de l'objet state, donc cela se fera comme ceci :

```
marked(this.state.markdown)
```

Maintenant, l'étape suivante consiste à afficher réellement les données converties sur la page web. Pour ce faire, nous utiliserons `dangerouslySetInnerHTML`, qui est un attribut sous les éléments DOM dans React. Selon la documentation officielle :

> `_dangerouslySetInnerHTML_` est le remplacement de React pour utiliser `_innerHTML_` dans le DOM du navigateur.

Cela signifie que si dans React vous devez définir le HTML **par programme** ou à partir d'une **source externe**, vous devrez utiliser `dangerouslySetInnerHTML` au lieu de `innerHTML` traditionnel en Javascript.

**En termes simples, en utilisant** `**dangerouslySetInnerHTML**` **vous pouvez définir le HTML directement depuis React.**

Lorsque vous utilisez `dangerouslySetInnerHTML`, vous devrez passer un **objet** avec une clé `__html`. **(Notez que la clé se compose de deux underscores.)**

Voici comment nous allons procéder :

```
<div
style={outputStyle}
dangerouslySetInnerHTML={{ __html: marked(this.state.markdown) }}
>
</div>

```

Avec cela, nous avons terminé notre projet et maintenant vous verrez votre `Visualiseur Markdown` en action.

Voici le `App.js` complet

<script src="https://gist.github.com/lelouchB/9795597f96f4bad44e0264ec73f93137.js"></script>

## Nous l'avons fait ! 🎉

Félicitations pour avoir construit ce visualiseur Markdown React.

## Et ensuite ?

Alors, quel est l'avenir de ce projet ? Vous êtes l'avenir. **Créez votre propre version** du visualiseur Markdown, ajoutez différents designs, mises en page, fonctionnalités personnalisées. Par exemple, vous pourriez ajouter un **bouton de réinitialisation** pour effacer la zone de texte — tout dépend de votre imagination. J'espère que vous avez pris plaisir à coder.

Quels autres projets ou tutoriels aimeriez-vous voir ? Contactez-moi sur [Twitter](https://twitter.com/noharashutosh), et je ferai plus de tutoriels ! Si vous êtes inspiré pour ajouter des fonctionnalités vous-même, n'hésitez pas à les partager et à [me taguer](https://twitter.com/noharashutosh) — j'adorerais en entendre parler 😊