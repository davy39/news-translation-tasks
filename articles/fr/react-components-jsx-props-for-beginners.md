---
title: Composants Fonctionnels React, Props et JSX – Tutoriel React.js pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-05T20:59:58.000Z'
originalURL: https://freecodecamp.org/news/react-components-jsx-props-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Copy-of-Add-a-heading.png
tags:
- name: JavaScript
  slug: javascript
- name: JSX
  slug: jsx
- name: React
  slug: react
seo_title: Composants Fonctionnels React, Props et JSX – Tutoriel React.js pour Débutants
seo_desc: "By Cem Eygi\nReact is one of the most popular JavaScript libraries for\
  \ building user interfaces. \nIf you want to become a front-end developer or find\
  \ a web development job, you would probably benefit from learning React in-depth.\n\
  In this post, you're ..."
---

Par Cem Eygi

React est l'une des bibliothèques JavaScript les plus populaires pour construire des interfaces utilisateur. 

Si vous souhaitez devenir développeur front-end ou trouver un emploi dans le développement web, vous bénéficieriez probablement d'apprendre React en profondeur.

Dans cet article, vous allez apprendre certaines bases de React comme la création d'un composant, la syntaxe JSX et les Props. Si vous n'avez aucune ou peu d'expérience avec React, cet article est fait pour vous.

Pour commencer, [voici comment vous pouvez installer React](https://www.freecodecamp.org/news/install-react-with-create-react-app/).

## Qu'est-ce que JSX ?

La première chose que vous remarquerez après avoir installé votre premier projet React est qu'une fonction JavaScript retourne du code HTML :

```jsx
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Modifiez <code>src/App.js</code> et enregistrez pour recharger.
        </p>
      </header>
    </div>
  );
}
```

Il s'agit d'une extension de syntaxe spéciale et valide pour React appelée JSX (JavaScript XML). Normalement, dans les projets liés au front-end, nous gardons le code HTML, CSS et JavaScript dans des fichiers séparés. Cependant, dans React, cela fonctionne un peu différemment.

Dans les projets React, nous ne créons pas de fichiers HTML séparés, car JSX nous permet d'écrire du HTML et du JavaScript combinés ensemble dans le même fichier, comme dans l'exemple ci-dessus. Vous pouvez cependant séparer votre CSS dans un autre fichier.

Au début, JSX peut sembler un peu étrange. Mais ne vous inquiétez pas, vous vous y habituerez. 

JSX est très pratique, car nous pouvons également exécuter n'importe quel code JavaScript (logique, fonctions, variables, etc.) directement à l'intérieur du HTML en utilisant des accolades {
0}, comme ceci :

```jsx
function App() {
  const text = 'Bonjour le Monde';
  
  return (
    <div className="App">
      <p> {text} </p>
    </div>
  );
}
```

De plus, vous pouvez assigner des balises HTML à des variables JavaScript :

```jsx
const message = <h1>React est génial !</h1>;
```

Ou vous pouvez retourner du HTML à l'intérieur d'une logique JavaScript (comme des cas if-else) :

```jsx
render() {
    if(true) {
        return <p>OUI</p>;
    } else {
        return <p>NON</p>;
    }
}
```

Je ne vais pas entrer dans plus de détails sur JSX, mais assurez-vous de considérer les règles suivantes lors de l'écriture de JSX :

* Les balises HTML et les composants doivent toujours être fermées < />
* Certains attributs comme **"class"** deviennent **"className"** (car class fait référence aux classes JavaScript), **"tabindex"** devient **"tabIndex"** et doit être écrit en camelCase
* Nous ne pouvons pas retourner plus d'un élément HTML à la fois, alors assurez-vous de les envelopper dans une balise parente :

```jsx
return (
  <div>
    <p>Bonjour</p>
    <p>Monde</p>
  </div>
);
```

* ou comme alternative, vous pouvez les envelopper avec des balises vides :

```jsx
return (
  <>
    <p>Bonjour</p>
    <p>Monde</p>
  </>
);
```

Vous pouvez également regarder mon tutoriel React pour Débutants pour plus d'informations :

%[https://youtu.be/QJZ-xgt4SJo]

## Qu'est-ce que les Composants Fonctionnels et de Classe ?

Après vous être habitué à la syntaxe JSX, la prochaine chose à comprendre est la structure basée sur les composants de React. 

Si vous revisitez l'exemple de code en haut de cet article, vous verrez que le code JSX est retourné par une fonction. Mais la fonction App() n'est pas une fonction ordinaire – c'est en fait un composant. Alors, qu'est-ce qu'un composant ?

### Qu'est-ce qu'un Composant ?

Un composant est un bloc de code indépendant et réutilisable qui divise l'interface utilisateur en plus petites parties. Par exemple, si nous construisions l'interface utilisateur de Twitter avec React :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/twit.png)
_Les composants du Fil d'Actualités de Twitter_

Plutôt que de construire toute l'interface utilisateur sous un seul fichier, nous pouvons et nous devons diviser toutes les sections (marquées en rouge) en plus petites parties indépendantes. En d'autres termes, ce sont des composants.

React a deux types de composants : fonctionnels et de classe. Examinons chacun d'eux plus en détail.

### Composants Fonctionnels

Le premier et recommandé type de composant dans React est le composant fonctionnel. Un composant fonctionnel est essentiellement une fonction JavaScript/ES6 qui retourne un élément React (JSX). Selon la documentation officielle de React, la fonction ci-dessous est un composant fonctionnel valide :

```jsx
function Welcome(props) {
  return <h1>Bonjour, {props.name}</h1>;
}
```

Alternativement, vous pouvez également créer un composant fonctionnel avec la définition de fonction fléchée :

```jsx
const Welcome = (props) => { 
  return <h1>Bonjour, {props.name}</h1>; 
}
```

> Cette fonction est un composant React valide car elle accepte un seul objet argument "props" (qui signifie propriétés) avec des données et retourne un élément React. — [**reactjs.org**](https://reactjs.org/)

Pour pouvoir utiliser un composant plus tard, vous devez d'abord l'exporter afin de pouvoir l'importer ailleurs :

```jsx
function Welcome(props) {
  return <h1>Bonjour, {props.name}</h1>;
}

export default Welcome;
```

Après l'avoir importé, vous pouvez appeler le composant comme dans cet exemple :

```jsx
import Welcome from './Welcome';

function App() { 
  return (
    <div className="App">
      <Welcome />
    </div>
  );
}
```

Ainsi, un Composant Fonctionnel dans React :

* est une fonction JavaScript/ES6
* doit retourner un élément React (JSX)
* commence toujours par une majuscule (convention de nommage)
* prend props comme paramètre si nécessaire

### Qu'est-ce que les Composants de Classe ?

Le deuxième type de composant est le composant de classe. Les composants de classe sont des classes ES6 qui retournent du JSX. Ci-dessous, vous voyez notre même fonction Welcome, cette fois comme un composant de classe :

```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Bonjour, {this.props.name}</h1>;
  }
}
```

Différents des composants fonctionnels, les composants de classe doivent avoir une méthode supplémentaire render() pour retourner du JSX.

### Pourquoi Utiliser les Composants de Classe ?

Nous utilisions les composants de classe à cause de "l'état". Dans les anciennes versions de React (version < 16.8), il n'était pas possible d'utiliser l'état à l'intérieur des composants fonctionnels.

Par conséquent, nous avions besoin de composants fonctionnels pour le rendu de l'interface utilisateur uniquement, tandis que nous utilisions des composants de classe pour la gestion des données et certaines opérations supplémentaires (comme les méthodes de cycle de vie). 

Cela a changé avec l'introduction des Hooks React, et maintenant nous pouvons également utiliser des états dans les composants fonctionnels. (Je couvrirai l'état et les hooks dans mes prochains articles, alors ne vous en souciez pas pour l'instant).

Un Composant de Classe :

* est une classe ES6, deviendra un composant une fois qu'elle 'étend' un composant React.
* prend des Props (dans le constructeur) si nécessaire
* doit avoir une méthode render() pour retourner du JSX

## Qu'est-ce que les Props dans React ?

Un autre concept important des composants est la manière dont ils communiquent. React a un objet spécial appelé prop (pour propriété) que nous utilisons pour transporter des données d'un composant à un autre.

Mais attention – les props ne transportent des données que dans un flux à sens unique (uniquement du parent vers les composants enfants). Il n'est pas possible avec les props de passer des données de l'enfant au parent, ou à des composants au même niveau.

Revisons la fonction App() ci-dessus pour voir comment passer des données avec les props. 

Tout d'abord, nous devons définir une prop sur le composant Welcome et lui assigner une valeur :

```jsx
import Welcome from './Welcome';

function App() { 
  return (
    <div className="App">
      <Welcome name="John"/>
      <Welcome name="Mary"/>
      <Welcome name="Alex"/>
    </div>
  );
}
```

Les props sont des valeurs personnalisées et elles rendent également les composants plus dynamiques. Puisque le composant Welcome est l'enfant ici, nous devons définir les props sur son parent (App), afin que nous puissions passer les valeurs et obtenir le résultat simplement en accédant à la prop "name" :

```jsx
function Welcome(props) {
  return <h1>Bonjour, {props.name}</h1>;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/props.png)

### Les Props React Sont Vraiment Utiles

Ainsi, les développeurs React utilisent les props pour passer des données et elles sont utiles pour ce travail. Mais qu'en est-il de la gestion des données ? Les props sont utilisées pour passer des données, pas pour les manipuler. Je vais couvrir la gestion des données avec React dans mes futurs articles ici sur freeCodeCamp.

En attendant, si vous souhaitez en apprendre davantage sur React et le développement web, n'hésitez pas à [vous abonner à ma chaîne YouTube](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q).

Merci d'avoir lu !