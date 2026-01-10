---
title: Comment utiliser les props dans React
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2021-11-15T23:48:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-props-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/g127.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les props dans React
seo_desc: 'In this tutorial, we''ll talk about an important concept in React – props.
  I''ll show you how to use them to keep the flow of data in your app dynamic.

  Prerequisites

  In other to follow along with this tutorial, you will need:


  A React app.


  Additionall...'
---

Dans ce tutoriel, nous allons parler d'un concept important dans React – les props. Je vais vous montrer comment les utiliser pour garder le flux de données dans votre application dynamique.

### Prérequis

Pour suivre ce tutoriel, vous aurez besoin de :

* Une application React.

De plus, je suppose que vous comprenez déjà :

* Ce que sont les composants dans React et comment les utiliser.
* Comment utiliser les fonctionnalités ES6 dans React (Vous ne savez pas comment ? Lisez [cet](https://www.freecodecamp.org/news/how-to-use-es6-javascript-features-in-react/) article).
* Les bases de la gestion d'état dans React (Vous ne savez pas comment cela fonctionne ? Lisez [cet](https://www.freecodecamp.org/news/introduction-to-react-hooks/) article).

## Qu'est-ce que les props dans React ?

Nous utilisons les props dans React pour passer des données d'un composant à un autre (d'un composant parent à un ou plusieurs composants enfants). Props est simplement une manière abrégée de dire propriétés. Elles sont utiles lorsque vous voulez que le flux de données dans votre application soit dynamique.

Voici à quoi ressemble mon composant `App.js` :

```javascript
function App() {
  return (
    <div className="App">
      
    </div>
  )
}

export default App

```

Créons maintenant un autre composant nommé `Tool.js`. Ce fichier affichera des informations sur l'outil préféré d'un designer de produits. Sans les props, le code ressemblerait à ceci :

```javascript
function Tool() {
    return (
      <div>
        <h1>Je m'appelle Ihechikara.</h1>
        <p>Mon outil de design préféré est Figma.</p>
      </div>
    );
}

export default Tool
```

Nous allons maintenant importer ce composant dans le composant `App`. C'est-à-dire :

```javascript
import Tool from "./Tool"

function App() {
  return (
    <div className="App">
      <Tool/>
    </div>
  )
}

export default App
```

Supposons que le composant `Tool` sera réutilisable dans différents composants pour décrire différents designers et leurs outils préférés.

Bien que React facilite l'importation de la logique d'un composant sans réécrire le code, ce composant particulier a déjà ses données codées en dur. Cela signifie que nous devons soit réécrire cette logique pour chaque autre composant, soit – vous avez deviné – utiliser les props pour modifier les données pour différents composants.

Si vous ne comprenez pas encore comment cela fonctionne, les props nous permettent de réutiliser la logique d'un composant de manière dynamique. Cela signifie que les données dans le composant ne seront pas statiques. Ainsi, pour chaque autre composant utilisant cette logique, ses données peuvent être modifiées pour répondre aux exigences.

## Comment utiliser les props dans React

Dans cette section, vous apprendrez deux façons d'utiliser les props : l'une sans déstructuration et l'autre avec déstructuration.

### Comment utiliser les props sans déstructuration

Pour utiliser les props, vous devez passer `props` en tant qu'argument dans votre fonction. Cela est similaire à passer des arguments dans vos fonctions JavaScript régulières. Voici un exemple :

```javascript
function Tool(props) {
  const name = props.name;
  const tool = props.tool;
    return (
      <div>
        <h1>Je m'appelle {name}.</h1>
        <p>Mon outil de design préféré est {tool}.</p>
      </div>
    );
}

export default Tool
```

Je vais maintenant expliquer tout ce qui s'est passé ci-dessus étape par étape.

#### Étape 1 - Passer les props en tant qu'argument

Nous l'avons fait dans la première ligne du code ci-dessus : `function Tool(props){}`. Cela vous permet automatiquement d'utiliser les props dans le composant de votre application React.

#### Étape 2 - Déclarer les variables de props

```javascript
const name = props.name;
const tool = props.tool;
```

Comme vous pouvez le voir ci-dessus, ces variables sont différentes des variables régulières car les données qu'elles contiennent ont à voir avec les props.

Si vous ne souhaitez pas créer de variables pour vos props, vous pouvez les passer directement dans votre template comme ceci : `<h1> Je m'appelle {props.name} </h1>`

#### Étape 3 - Utiliser les variables dans le template JSX

Maintenant que vous avez déclaré vos variables, vous pouvez les placer où vous le souhaitez dans votre code.

```javascript
return (
      <div>
        <h1>Je m'appelle {name}.</h1>
        <p>Mon outil de design préféré est {tool}.</p>
      </div>
    );
```

#### Étape 4 - Passer des données aux props dans le composant `App`

Nous avons terminé la création de nos props, donc l'étape suivante consiste à leur passer des données. Nous avons déjà importé le composant `Tool` et cela est affiché dans le navigateur pour le moment :

```
Je m'appelle .
Mon outil de design préféré est .
```

Vous pouvez créer des données par défaut pour vos props afin qu'elles n'apparaissent pas vides à la déclaration. Vous verrez comment faire cela dans la dernière section.

Rappelons que c'est l'état actuel du composant `App` :

```javascript
import Tool from "./Tool"

function App() {
  return (
    <div className="App">
      <Tool/>
    </div>
  )
}

export default App
```

Vous devez vous demander où les données seront exactement passées. Pour ce faire, vous passez les données comme des attributs. Cela ressemble à ceci :

```javascript
import Tool from "./Tool"

function App() {
  return (
    <div className="App">
      <Tool name="Ihechikara" tool="Figma"/>
    </div>
  )
}

export default App

```

Remarquez le changement ? Ici : de `<Tool/>` à `<Tool name="Ihechikara" tool="Figma"/>`. Cela ne générera pas d'erreur car ces attributs sont attachés aux props créés dans le composant `Tool`.

Vous devriez avoir ceci affiché dans votre navigateur :

```
Je m'appelle Ihechikara.
Mon outil de design préféré est Figma.
```

Notez que le nom de la variable n'est pas la prop elle-même. Si j'avais créé une variable de cette manière – `const myPropName = _props_.name` – et utilisé la variable dans mon template comme ceci : `<h1>Je m'appelle {myPropName}.</h1>`, alors le code fonctionnerait toujours parfaitement si je faisais ceci : `<Tool name="Ihechikara" tool="Figma"/>`. L'attribut `name` est dérivé de `props.name` et non du nom de la variable contenant la prop.

Maintenant, vous pouvez créer des données dynamiquement pour n'importe quel composant en utilisant la logique définie dans le composant `Tool`. Vous pouvez déclarer autant de props que vous le souhaitez.

Ensuite, vous apprendrez comment utiliser les props avec la déstructuration.

### Comment utiliser les props avec la déstructuration

Le code de cette section est entièrement le même que celui de la section précédente, à l'exception de la méthode de déclaration des props. Si vous ne savez pas comment utiliser la déstructuration en JavaScript, consultez [cet](https://www.freecodecamp.org/news/how-to-use-es6-javascript-features-in-react/) article.

Dans la section précédente, nous avons déclaré nos props de cette manière :

```javascript
const name = props.name;
const tool = props.tool;
```

Mais nous n'avons pas besoin de faire cela avec la déstructuration. Vous faites simplement ceci :

```javascript
function Tool({name, tool}) {
  
    return (
      <div>
        <h1>Je m'appelle {name}.</h1>
        <p>Mon outil de design préféré est {tool}.</p>
      </div>
    );
}

export default Tool
```

La différence se trouve dans la première ligne de code. Au lieu de passer `props` en tant qu'argument, nous avons déstructuré et passé les variables en tant qu'arguments de la fonction.

Tout le reste reste le même.

Notez que vous n'êtes pas limité à des variables uniques en tant que données de props – vous pouvez également passer des fonctions et même des données provenant d'objets.

### Comment définir des valeurs par défaut pour les props

Si vous ne souhaitez pas que les données de vos props soient vides lorsque vous les créez, vous pouvez passer une valeur par défaut. Voici comment faire :

```javascript
function Tool({name, tool}) {

    return (
      <div>
        <h1>Je m'appelle {name}.</h1>
        <p>Mon outil de design préféré est {tool}.</p>
      </div>
    );

  }
  
  Tool.defaultProps = {
    name: "Designer",
    tool: "Adobe XD"
  }
export default Tool

```

Juste à la fin du code avant l'exportation du composant, nous avons déclaré des valeurs par défaut pour nos props. Pour ce faire, nous avons commencé par le nom du composant et un point/une période le reliant à `defaultProps` qui est intégré lorsque vous créez une application React.

Maintenant, partout où nous importons ce composant, ces valeurs seront les valeurs initiales au lieu d'être vides. Lorsque vous passez des données au composant enfant comme nous l'avons fait dans les sections précédentes, cela remplace les valeurs par défaut.

## Conclusion

Cet article a couvert tout ce dont vous avez besoin pour commencer à utiliser les props et à passer des données dynamiquement à travers vos composants.

La meilleure façon de comprendre ces concepts est de pratiquer et de construire des choses géniales avec eux, alors assurez-vous de ne pas vous contenter de lire – allez construire aussi.

Vous pouvez me trouver sur Twitter [@ihechikara2](https://twitter.com/Ihechikara2). Bon codage !