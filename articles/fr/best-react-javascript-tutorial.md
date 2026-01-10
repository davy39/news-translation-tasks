---
title: Les meilleurs tutoriels React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-27T00:39:00.000Z'
originalURL: https://freecodecamp.org/news/best-react-javascript-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f01740569d1a4ca404f.jpg
tags:
- name: React
  slug: react
- name: Tutorial
  slug: tutorial
seo_title: Les meilleurs tutoriels React
seo_desc: 'React is a JavaScript library for building user interfaces. It was voted
  the most loved in the “Frameworks, Libraries, and Other Technologies” category of
  Stack Overflow’s 2017 Developer Survey.

  React is a JavaScript library and React applications bu...'
---

React est une bibliothèque JavaScript pour construire des interfaces utilisateur. Elle a été élue la plus appréciée dans la catégorie "Frameworks, Bibliothèques et Autres Technologies" de l'enquête auprès des développeurs de Stack Overflow en 2017.

React est une bibliothèque JavaScript et les applications React construites sur celle-ci s'exécutent dans le navigateur, PAS sur le serveur. Les applications de ce type ne communiquent avec le serveur que lorsque cela est nécessaire, ce qui les rend très rapides par rapport aux sites web traditionnels qui forcent l'utilisateur à attendre que le serveur ré-renderise des pages entières et les envoie au navigateur.

React est utilisé pour construire des interfaces utilisateur - ce que l'utilisateur voit sur son écran et avec quoi il interagit pour utiliser votre application web. Cette interface est divisée en composants, au lieu d'avoir une seule page énorme, vous la divisez en petits morceaux connus sous le nom de composants. En termes plus généraux, cette approche est appelée Modularité.

* C'est déclaratif : React utilise un paradigme déclaratif qui facilite le raisonnement sur votre application.
* C'est efficace : React calcule l'ensemble minimal de changements nécessaires pour maintenir votre DOM à jour.
* Et c'est flexible : React fonctionne avec les bibliothèques et les frameworks que vous connaissez déjà.

## Les meilleurs tutoriels pour apprendre React

freeCodeCamp propose un [tutoriel React sur YouTube](https://www.youtube.com/watch?v=DLX62G4lc44) qui vous enseignera toutes les bases en seulement 5 heures.

![Image](https://img.youtube.com/vi/DLX62G4lc44/maxresdefault.jpg)

Nous avons également un [tutoriel React intermédiaire plus approfondi](https://www.youtube.com/watch?v=m_u6P5k0vP0) qui vous apprend à construire une application complète de réseau social React en utilisant Firebase. Il dure 12 heures, et si vous suivez, vous apprendrez une tonne de subtilités de React.

## **Pourquoi apprendre React ?**

React implique la Composition, c'est-à-dire beaucoup de composants encapsulant les fonctionnalités dans un conteneur encapsulé.

De nombreux sites web populaires utilisent React en implémentant le modèle architectural MVC. Facebook (Partiellement), Instagram (Complètement), Khan Academy (Partiellement), New York Times (Partiellement), Yahoo Mail (Complètement), l'application de galerie photo et vidéo de Dropbox appelée Carousel (Complètement) sont les sites web populaires connus pour utiliser React.

Comment ces grandes applications sont-elles construites en utilisant React ? La réponse simple est en construisant de petites applications ou composants. Exemple :

```jsx
const Component2 = () => {
  return (
    <div></div>
  );
};
const Component3 = () => {
  return (
    <div></div>
  );
};
const Component1 = () => {
  return (
    <div>
      <Component2 />
      <Component3 />
    </div>
  );
};

ReactDOM.render(
  <Component1 />, 
  document.getElementById("app")
);
```

React est Déclaratif, pour la plupart, ce qui signifie que nous nous préoccupons davantage de ce qu'il faut faire plutôt que de la manière de faire une tâche spécifique.

La programmation déclarative est un paradigme de programmation qui exprime la logique d'un calcul sans décrire son flux de contrôle. La programmation déclarative présente certains avantages tels que la réduction des effets secondaires (qui se produit lorsque nous modifions un état ou mutons quelque chose ou faisons une requête API), la mutabilité minimisée (car une grande partie est abstraite), une lisibilité améliorée et moins de bugs.

React a également un flux de données unidirectionnel. L'UI dans React est en fait la fonction de l'état. Cela signifie que lorsque l'état est mis à jour, il met également à jour l'UI. Ainsi, notre UI progresse à mesure que l'état change.

## **Avantages de React**

Quelques raisons d'utiliser React sont :

1. Rapide. Les applications faites en React peuvent gérer des mises à jour complexes et rester rapides et réactives.
2. Modulaire. Au lieu d'écrire de grands fichiers de code denses, vous pouvez écrire de nombreux fichiers plus petits et réutilisables. La modularité de React peut être une belle solution aux problèmes de [maintenabilité de JavaScript](https://en.wikipedia.org/wiki/Spaghetti_code).
3. Évolutif. Les grands programmes qui affichent beaucoup de données changeantes sont là où React performe le mieux.
4. Flexible. Vous pouvez utiliser React pour des projets intéressants qui n'ont rien à voir avec la création d'une application web. Les gens explorent encore le potentiel de React. [Il y a de la place pour explorer](https://medium.mybridge.co/22-amazing-open-source-react-projects-cb8230ec719f).

### **Virtual DOM**

La magie de React vient de son interprétation du DOM et de sa stratégie pour créer des interfaces utilisateur.

React utilise le Virtual DOM pour rendre un arbre HTML virtuellement d'abord. Ensuite, chaque fois qu'un état change et que nous obtenons un nouvel arbre HTML qui doit être pris dans le DOM du navigateur, au lieu d'écrire tout le nouvel arbre, React n'écrira que la différence entre le nouvel arbre et l'arbre précédent (puisque React a les deux arbres en mémoire). Ce processus est connu sous le nom de Réconciliation d'Arbre.

### **Réconciliation**

React dispose d'un algorithme de différenciation intelligent qu'il utilise pour ne régénérer dans son nœud DOM que ce qui doit réellement être régénéré, tout en gardant le reste tel quel. Ce processus de différenciation est possible grâce au DOM virtuel de React.

En utilisant le DOM virtuel, React garde la dernière version du DOM en mémoire. Lorsqu'il a une nouvelle version du DOM à prendre dans le navigateur, cette nouvelle version du DOM sera également en mémoire, de sorte que React peut calculer la différence entre la nouvelle et l'ancienne version.

React instruira ensuite le navigateur de mettre à jour uniquement la différence calculée et non le nœud DOM entier. Peu importe combien de fois nous régénérons notre interface, React ne prendra dans le navigateur que les nouvelles mises à jour "partielles".

## **React à partir de zéro**

Souhaitez-vous commencer à apprendre les bases de React sans vous encombrer de la création d'un environnement de développement ? Il est probable que si vous êtes nouveau dans le développement web, la configuration d'un environnement de développement puisse vous intimider lorsque vous essayez simplement d'apprendre React.

Dans cet article, nous allons voir comment nous pouvons commencer avec React en utilisant uniquement un éditeur de texte et un navigateur, et rien d'autre.

### **1
-
Configurer le code de base avec Emmet**

Commençons par l'étape 1. Nous commencerons par un fichier dans notre navigateur appelé "index.html". Nous commencerons par le code HTML de base. Pour un démarrage rapide, je recommande d'utiliser Emmet avec l'éditeur de texte que vous avez. Sur la première ligne, tapez `html:5` puis appuyez sur la touche majuscule pour obtenir le code ci-dessous. Ou vous pouvez copier et coller le code ci-dessous.

```javascript
html:5
```

Cela donnera le code suivant :

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

Nous pouvons remplir le titre de "Time to React!".

Ce contenu n'apparaîtra pas dans votre page web. Tout ce qui se trouve dans la section head du fichier HTML sera des métadonnées que notre navigateur utilisera pour interpréter notre code dans la section body. Ce titre sera ce qui apparaîtra sur l'onglet de notre page, et non sur la page elle-même.

### **2 - Obtenir des balises de script pour exploiter la puissance des bibliothèques React et Babel**

D'accord, le premier élément est coché sur notre liste. Regardons le deuxième élément. Nous allons configurer notre environnement de développement en utilisant des balises de script pour intégrer React et Babel.

Ce n'est pas un environnement de développement réel. Cela nécessiterait une configuration assez élaborée. Cela nous laisserait également avec beaucoup de code de base et de bibliothèques qui nous éloigneraient du sujet de l'apprentissage des bases de React. L'objectif de cette série est de passer en revue la syntaxe de base de React et de se lancer directement dans le codage. Nous allons utiliser des balises `<script>` pour intégrer la bibliothèque React, la bibliothèque React DOM (pourquoi), et la bibliothèque Babel.

```javascript
<head>
  ...
  <!-- BIBLIOTHÈQUE REACT -->
  <script src="https://unpkg.com/react@15.5.4/dist/react.js"></script>
  <!-- BIBLIOTHÈQUE REACT DOM -->
  <script src="https://unpkg.com/react-dom@15.5.4/dist/react-dom.js"></script>
  <!-- BIBLIOTHÈQUE BABEL -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.25.0/babel.min.js"></script>
  ...
  <title>Time to React!</title>
</head>
```

Vous êtes libre d'utiliser des versions plus récentes de ces bibliothèques à mesure qu'elles sortent. Elles ne devraient pas créer de changements cassants pour le contenu que nous couvrons.

Que faisons-nous ici ? L'élément HTML `<script>` est utilisé pour intégrer ou référencer un script exécutable. L'attribut "src" pointe vers les fichiers de script externes pour la bibliothèque React, la bibliothèque ReactDOM et la bibliothèque Babel.

C'est comme si vous aviez un rasoir électrique. Il ne vous sert littéralement à rien, peu importe à quel point le rasoir électrique est sophistiqué, à moins que vous ne puissiez le brancher au mur et avoir accès à l'électricité. Notre code React que nous allons écrire ne nous servira à rien si notre navigateur ne peut pas se brancher à ces bibliothèques pour comprendre et interpréter ce que nous faisons.

C'est ainsi que notre application va acquérir la puissance de React, c'est ainsi que nous allons insérer React dans le DOM. Nous avons React et ReactDOM comme deux bibliothèques différentes car il existe des cas d'utilisation tels que React Native où le rendu dans le DOM n'est pas nécessaire pour le développement mobile, donc la bibliothèque a été divisée pour que les gens puissent décider de ce dont ils avaient besoin en fonction du projet sur lequel ils travaillaient.

Parce que nous aurons besoin que notre React arrive au DOM, nous utiliserons les deux scripts. Babel est la manière dont nous tirons parti d'ECMA script au-delà d'ES5 et traitons quelque chose appelé JSX (JavaScript en tant que XML) que nous utiliserons dans React. Nous examinerons plus en détail la magie de Babel dans une section à venir :)

D'accord, nous avons terminé les étapes 1 et 2. Nous avons configuré notre code de base et configuré notre environnement de développement.

### **3 - Rendre React dans le DOM**

Nos deux prochaines étapes consisteront à choisir notre emplacement dans le DOM où nous voulons rendre notre contenu React. Et nous utiliserons une autre balise de script pour notre contenu React dans le corps. En général, comme bonne pratique de séparation des préoccupations, cela serait dans son propre fichier puis lié à ce document HTML. Nous ferons cela plus tard dans les sections à venir. Pour l'instant, nous laisserons cela dans le corps du document HTML dans lequel nous nous trouvons.

Maintenant, nous allons voir à quel point il est simple de choisir un endroit dans le DOM pour rendre notre contenu React. Nous irons dans le corps. Et la meilleure pratique n'est pas de simplement jeter React dans la balise body pour l'afficher, mais de créer un élément séparé, souvent une div, que vous pouvez traiter comme un élément racine pour insérer votre contenu React.

```javascript
<body>
  <div id="app">React n'a pas encore rendu</div>
</body>
```

Nous allons créer un simple élément `<div>` et lui donner un id de "app". Nous allons pouvoir cibler cet emplacement pour insérer notre contenu React de la même manière que vous pourriez utiliser CSS pour cibler un id pour le style de votre choix. Tout contenu React sera rendu dans les balises div avec l'id de app. En attendant, nous laisserons un texte disant que "React n'a pas encore rendu". Si nous voyons cela lorsque nous prévisualisons notre page, cela signifie que quelque part nous avons manqué de rendre React.

Maintenant, allons-y et créons une balise de script dans notre corps où nous créerons avec React pour la première fois. La syntaxe dont nous aurons besoin pour notre balise de script est d'ajouter un attribut de "type". Cela spécifie le type de média du script. Au-dessus, dans notre tête, nous avons utilisé un attribut src qui pointait vers les fichiers de script externes pour la bibliothèque React, la bibliothèque ReactDOM et la bibliothèque Babel.

```javascript
<body>
  <div id="app">React n'a pas encore rendu</div>
  <script type="text/babel">
  </script>
</body>
```

Le "type" de script que nous utilisons sera entouré de guillemets et défini sur `"text/babel"`. Nous aurons besoin de la capacité d'utiliser babel immédiatement lorsque nous travaillerons avec JSX.

Tout d'abord, nous allons rendre React dans le DOM. Nous utiliserons la méthode `ReactDOM.render()` pour cela. Ce sera une méthode, et rappelez-vous qu'une méthode est simplement une fonction attachée à un objet. Cette méthode prendra deux arguments.

```javascript
<body>
  <div id="app">React n'a pas encore rendu</div>
  <script type="text/babel">
  ReactDOM.render(React What, React Where);
</script>
</body>
```

Le premier argument est le "what" de React. Le deuxième argument est le "where" de l'emplacement où vous voulez qu'il soit placé dans le DOM. Commençons par appeler notre méthode ReactDOM.render(). Notre premier argument sera notre JSX.

```javascript
<body>
  <div id="app">React n'a pas encore rendu</div>
  <script type="text/babel">
  ReactDOM.render(
    <h1>Hello World</h1>, 
    React Where
  );
</script>
</body>
```

La [documentation officielle de React](https://reactjs.org/docs/introducing-jsx.html) indique : "Cette syntaxe de balise étrange n'est ni une chaîne ni du HTML. Elle est appelée JSX, et c'est une extension de syntaxe à JavaScript. Nous recommandons de l'utiliser avec React pour décrire à quoi l'UI devrait ressembler. JSX peut vous rappeler un langage de template, mais il vient avec toute la puissance de JavaScript. JSX produit des "éléments" React."

Souvent, JSX effraie les gens qui sont développeurs depuis un certain temps parce que cela ressemble à du HTML. Très tôt, les développeurs apprennent la séparation des préoccupations. Le HTML a sa place, le CSS a sa place et JavaScript a sa place. JSX semble brouiller les lignes. Vous utilisez ce qui ressemble à du HTML mais, comme le dit Facebook, il vient avec toute la puissance de JavaScript.

Cela peut effrayer les vétérans, donc de nombreux tutoriels React commencent sans JSX, ce qui peut être assez complexe. Nous ne ferons pas cela. Parce que cet article est destiné à ceux qui sont très jeunes dans leur carrière, vous ne verrez peut-être pas ces drapeaux rouges lorsque vous verrez cette syntaxe.

Et JSX est vraiment intuitif. Vous pouvez probablement lire ce code très facilement et voir que cela va être la plus grande balise d'en-tête affichant le texte "Hello World". Pas de mystère et assez simple. Maintenant, regardons ce que serait notre deuxième argument.

```javascript
<body>
  <div id="app">React n'a pas encore rendu</div>
  <script type="text/babel">
    ReactDOM.render(
      <h1>Hello World</h1>, 
      document.getElementById("app")
    );
  </script>
</body>
```

C'est là que nous voulons que notre contenu React soit rendu dans le DOM. Vous avez probablement fait cela plusieurs fois dans le passé. Nous taperons simplement `document.getElementById()`. Et nous passerons dans l'argument l'id de l'application. Et c'est tout. Nous allons maintenant cibler la div avec l'id de l'application pour insérer notre contenu React.

Nous voulons nous assurer que notre contenu est sauvegardé. Allez-y et ouvrez cela dans le navigateur et vous devriez voir "Hello World". Comme vous pouvez probablement le deviner, utiliser React n'est pas la manière la plus rapide ou la meilleure de créer une application Hello World. Nous ne voyons pas encore les avantages. Mais maintenant, nous savons que tout fonctionne.

Allez-y et ouvrez la console et regardez les "éléments". Vous pouvez le faire sur un Mac avec commande + maj + j ou sur Windows et Linux : Ctrl + Maj + J

Si vous cliquez sur la balise head, nous pouvons voir nos bibliothèques de scripts que nous avons incluses. Ensuite, nous pouvons descendre dans le corps de notre document. Cliquons sur notre div avec l'id de "app". Et lorsque nous le faisons, nous voyons notre balise `<h1>` avec le contenu "Hello World".

[Voir le code entier ici](https://github.com/robgmerrill/hello-react/blob/master/section-one/index.html).

### **Récapitulatif**

Faisons donc un rapide récapitulatif. Dans notre balise head, nous avons récupéré les balises de script pour React, ReactDOM et Babel. Ce sont les outils dont notre navigateur a besoin dans ses métadonnées pour lire notre code React et JSX en particulier.

Nous avons ensuite localisé la position dans le DOM où nous voulions insérer notre React en créant un élément div avec l'id "app".

Ensuite, nous avons créé une balise de script pour entrer notre code React. Nous avons utilisé la méthode ReactDOM.render() qui prend deux arguments. Le "what" du contenu React, dans ce cas notre JSX, et le deuxième argument est le "where" où vous voulez insérer le contenu React dans le DOM. Dans ce cas, il s'agit de l'emplacement avec l'id "app".

En alternative à JSX, vous pouvez utiliser ES6 et le compilateur JavaScript comme Babel. [https://babeljs.io/](https://babeljs.io/)

## **Installation de React**

### **Création d'un nouveau projet React**

Vous pourriez simplement intégrer la bibliothèque React dans votre page web comme suit<sup>2</sup> :

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/16.0.0/cjs/react.production.min.js"></script>
```

Les programmeurs intelligents veulent prendre la voie plus pratique et productive : [Create React App](https://github.com/facebookincubator/create-react-app)

```bash
npm install -g create-react-app
create-react-app my-app

cd my-app
npm start
```

Cela configurera votre environnement de développement afin que vous puissiez utiliser les dernières fonctionnalités de JavaScript, offrir une bonne expérience de développement et optimiser votre application pour la production.

`npm start` démarrera un serveur de développement qui permet le rechargement en direct<sup>3</sup>.

Une fois que vous avez terminé votre projet et que vous êtes prêt à déployer votre application en production, vous pouvez simplement utiliser `npm run build` pour créer une version optimisée de votre application dans le dossier `build`.

## **Votre première application React**

### **Installation**

Comme spécifié dans la section précédente (Installation), exécutez l'outil `Create React App`. Une fois tout terminé, `cd` dans le dossier de votre application et exécutez `npm start`. Cela démarrera un serveur de développement et vous serez prêt à commencer à développer votre application !

```bash
npm install -g react-create-app
create-react-app my-first-app

cd my-first-app
npm start
```

### **Modification du code**

Démarrez votre éditeur ou IDE de choix et modifiez le fichier `App.js` dans le dossier `src`. Lorsque vous créez avec l'outil `react-create-app`, il y aura déjà du code dans ce fichier.

Le code se composera de ces parties :

#### **imports**

```javascript
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
```

Cela est utilisé par [webpack](https://webpack.js.org/) pour importer tous les modules requis afin que votre code puisse les utiliser. Ce code importe 3 modules :

1. `React` et `Component`, qui nous permettent d'utiliser React comme il se doit. (Avec des composants)
2. `logo`, qui nous permet d'utiliser `logo.svg` dans ce fichier.
3. `./App.css`, qui importe la feuille de style pour ce fichier.

#### **classes/composants**

```javascript
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Bienvenue dans React</h1>
        </header>
        <p className="App-intro">
          Pour commencer, modifiez <code>src/App.js</code> et enregistrez pour recharger.
        </p>
      </div>
    );
  }
}
```

React est une bibliothèque qui utilise des Composants, qui vous permettent de diviser votre UI en morceaux indépendants et réutilisables, et de penser à chaque morceau de manière isolée. Il y a déjà 1 composant créé, le composant `App`. Si vous avez utilisé l'outil `create-react-app`, ce composant est le composant principal du projet et vous devriez construire autour de cette classe centrale.

Nous examinerons les composants plus en détail sous peu.

#### **exports**

Lors de la création d'une classe dans React, vous devez les exporter après la déclaration, ce qui vous permet d'utiliser le composant dans un autre fichier en utilisant le mot-clé `import`. Vous pouvez utiliser `default` après le mot-clé `export` pour indiquer à React que c'est la classe principale de ce fichier.

```javascript
export default App;
```

### **Voir les résultats !**

Lorsque vous avez démarré le serveur de développement en émettant la commande `npm start`, vous pouvez voir les modifications que vous ajoutez à votre projet en direct dans votre navigateur. Après avoir émis la commande, npm devrait ouvrir automatiquement un navigateur affichant votre application.

## **React - Composants**

Les composants sont réutilisables dans React. Vous pouvez injecter des valeurs dans les props comme indiqué ci-dessous :

```jsx
function Welcome(props) {
  return <h1>Bonjour, {props.name}</h1>;
}

const element = <Welcome name="Faisal Arkan" />;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```

`name="Faisal Arkan"` donnera une valeur à `{props.name}` à partir de la fonction `Welcome(props)` et retournera le composant qui a la valeur donnée par `name="Faisal Arkan"`. Après cela, React rendra l'élément en HTML.

### **Autres façons de déclarer des composants**

Il existe de nombreuses façons de déclarer des composants lors de l'utilisation de React. Il existe deux types de composants, les composants **_sans état_** et les composants **_avec état_**. 

### **Avec état**

#### **Composants de type Classe**

```jsx
class Cat extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      humor: 'happy'
    }
  }
  render() {
    return(
      <div>
        <h1>{this.props.name}</h1>
        <p>
          {this.props.color}
        </p>
      </div>
    );
  }
}
```

### **Composants sans état**

#### **Composants Fonctionnels (Fonction Fléchée d'ES6)**

```jsx
const Cat = props => {
  return (  
    <div>
      <h1>{props.name}</h1>
      <p>{props.color}</p>
    </div>;
  );
};
```

#### **Composants de Retour Implicite**

```jsx
const Cat = props => 
  <div>
    <h1>{props.name}</h1>
    <p>{props.color}</p>
  </div>;
```