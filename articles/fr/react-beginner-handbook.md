---
title: React pour Débutants – Un Guide React.js pour les Développeurs Front End
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2020-11-13T17:02:22.000Z'
originalURL: https://freecodecamp.org/news/react-beginner-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/book-2.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: React pour Débutants – Un Guide React.js pour les Développeurs Front End
seo_desc: 'React is one of the most popular JavaScript frameworks ever created, and
  I believe that it''s one of the best tools out there.

  The goal of this handbook is to provide a starter guide to learning React.

  At the end of the book, you''ll have a basic under...'
---

React est l'un des frameworks JavaScript les plus populaires jamais créés, et je crois que c'est l'un des meilleurs outils disponibles.

L'objectif de ce guide est de fournir un guide de démarrage pour apprendre React.

À la fin de ce livre, vous aurez une compréhension de base de :

- Ce qu'est React et pourquoi il est si populaire
- Comment installer React
- Les composants React
- L'état (State) dans React
- Les props dans React
- La gestion des événements utilisateur dans React
- Les événements de cycle de vie dans un composant React

Ces sujets seront la base sur laquelle vous construirez dans d'autres tutoriels React plus avancés.

Ce livre est spécialement écrit pour les programmeurs JavaScript qui sont nouveaux dans React. Alors, commençons.

## Qu'est-ce que React ?

React est une bibliothèque JavaScript qui vise à simplifier le développement des interfaces visuelles.

Développé chez Facebook et publié en 2013, il alimente certaines des applications les plus utilisées, notamment Facebook et Instagram, parmi d'innombrables autres applications.

Son objectif principal est de faciliter la compréhension d'une interface et de son état à tout moment. Il le fait en divisant l'interface utilisateur en une collection de composants.

Vous pourriez rencontrer quelques difficultés initiales lors de l'apprentissage de React. Mais une fois que cela "clique", je garantis que ce sera l'une des meilleures expériences que vous aurez jamais. React simplifie de nombreuses choses, et son écosystème est rempli de bibliothèques et d'outils formidables.

React en lui-même a une API très petite, et vous devez essentiellement comprendre 4 concepts pour commencer :

- Composants
- JSX
- État (State)
- Props

Nous explorerons tous ces concepts dans ce livre, et nous laisserons les concepts plus avancés à d'autres tutoriels. Je vous donnerai quelques conseils dans la dernière section sur la manière de progresser.

Et vous pouvez [télécharger ce guide au format PDF / ePub / Mobi gratuitement](https://flaviocopes.com/page/react-handbook/).

## Sommaire du guide
- [Combien de JavaScript devez-vous connaître pour utiliser React](#heading-combien-de-javascript-devez-vous-connaître-pour-utiliser-react)
- [Pourquoi devriez-vous apprendre React ?](#heading-pourquoi-devriez-vous-apprendre-react)
- [Comment installer React](#heading-comment-installer-react)
- [Composants React](#heading-composants-react)
- [Introduction à JSX](#heading-introduction-à-jsx)
- [Utiliser JSX pour composer une interface utilisateur](#heading-utiliser-jsx-pour-composer-une-interface-utilisateur)
- [La différence entre JSX et HTML](#heading-la-différence-entre-jsx-et-html)
- [Intégrer JavaScript dans JSX](#heading-intégrer-javascript-dans-jsx)
- [Gestion de l'état dans React](#heading-gestion-de-létat-dans-react)
- [Props des composants dans React](#heading-props-des-composants-dans-react)
- [Flux de données dans une application React](#heading-flux-de-données-dans-une-application-react)
- [Gestion des événements utilisateur dans React](#heading-gestion-des-événements-utilisateur-dans-react)
- [Événements de cycle de vie dans un composant React](#heading-événements-de-cycle-de-vie-dans-un-composant-react)
- [Où aller à partir d'ici](#heading-où-aller-à-partir-dici)

## Combien de JavaScript devez-vous connaître pour utiliser React

Avant de vous lancer directement dans React, vous devriez avoir une bonne compréhension de certains concepts fondamentaux de JavaScript.

Vous n'avez pas besoin d'être un expert en JavaScript, mais je pense que vous avez besoin d'une bonne vue d'ensemble de :

- [Variables](https://flaviocopes.com/javascript-variables/)
- [Fonctions fléchées](https://flaviocopes.com/javascript-arrow-functions/)
- [Travailler avec des objets et des tableaux en utilisant Rest et Spread](https://flaviocopes.com/javascript-rest-spread/)
- [Destructuration d'objets et de tableaux](https://flaviocopes.com/javascript-destructuring/)
- [Littéraux de gabarit](https://flaviocopes.com/javascript-template-literals/)
- [Fonctions de rappel](https://flaviocopes.com/javascript-callbacks/)
- [Modules ES](https://flaviocopes.com/es-modules/)

Si ces concepts vous semblent inconnus, je vous ai fourni quelques liens pour en savoir plus sur ces sujets.

## Pourquoi devriez-vous apprendre React ?

Je recommande vivement à tout développeur Web d'avoir au moins une compréhension de base de React.

Cela est dû à plusieurs raisons.

1. React est très populaire. En tant que développeur, il est assez probable que vous allez travailler sur un projet React à l'avenir. Peut-être un projet existant, ou peut-être que votre équipe voudra que vous travailliez sur une toute nouvelle application basée sur React.
2. Beaucoup d'outils aujourd'hui sont construits en utilisant React au cœur. Des frameworks et outils populaires comme Next.js, Gatsby, et bien d'autres utilisent React sous le capot.
3. En tant qu'ingénieur frontend, React est probablement un sujet qui sera abordé lors d'un entretien d'embauche.

Ce sont toutes de bonnes raisons, mais l'une des principales raisons pour lesquelles je veux que vous appreniez React est qu'il est formidable.

Il promeut plusieurs bonnes pratiques de développement, y compris la réutilisabilité du code et le développement basé sur les composants. Il est rapide, il est léger, et la manière dont il vous fait réfléchir au flux de données dans votre application convient parfaitement à de nombreux scénarios courants.


## Comment installer React

Il existe plusieurs façons d'installer React.

Pour commencer, je recommande vivement une approche, et c'est d'utiliser l'outil officiellement recommandé appelé `create-react-app`.

`create-react-app` est une application en ligne de commande, visant à vous familiariser avec React en un rien de temps.

Vous commencez par utiliser `npx`, qui est un moyen facile de télécharger et d'exécuter des commandes Node.js sans les installer.

> Voir mon guide npx ici : <https://flaviocopes.com/npx/>

`npx` est fourni avec `npm` (depuis la version 5.2). Si vous n'avez pas encore npm installé, faites-le maintenant depuis <https://nodejs.org> (npm est installé avec Node).

Si vous n'êtes pas sûr de la version de npm que vous avez, exécutez `npm -v` pour vérifier si vous devez mettre à jour.

> Astuce : consultez mon tutoriel sur le terminal OSX à l'adresse <https://flaviocopes.com/macos-terminal/> si vous n'êtes pas familier avec l'utilisation du terminal. Il s'applique à Mac et Linux.

Lorsque vous exécutez `npx create-react-app <nom-de-lappli>`, `npx` va _télécharger_ la dernière version de `create-react-app`, l'exécuter, puis la supprimer de votre système. 

C'est génial car vous n'aurez jamais une version obsolète sur votre système, et chaque fois que vous l'exécutez, vous obtenez le code le plus récent et le meilleur disponible.

Commençons alors :

```sh
npx create-react-app todolist
```

![cra-start](https://www.freecodecamp.org/news/content/images/2020/11/cra-start.png)

Voici ce que cela donne une fois l'exécution terminée :

![create-react-app-finished](https://www.freecodecamp.org/news/content/images/2020/11/create-react-app-finished.png)

`create-react-app` a créé une structure de fichiers dans le dossier que vous lui avez indiqué (`todolist` dans ce cas), et a initialisé un dépôt [Git](https://flaviocopes.com/git/).

Il a également ajouté quelques commandes dans le fichier `package.json` :

![cra-packagejson](https://www.freecodecamp.org/news/content/images/2020/11/cra-packagejson.png)

Ainsi, vous pouvez immédiatement démarrer l'application en allant dans le dossier de l'application nouvellement créée et en exécutant `npm start`.

![cra-running](https://www.freecodecamp.org/news/content/images/2020/11/cra-running.png)

Par défaut, cette commande lance l'application sur votre port local 3000, et ouvre votre navigateur en affichant l'écran de bienvenue :

![cra-browser](https://www.freecodecamp.org/news/content/images/2020/11/cra-browser.png)

Maintenant, vous êtes prêt à travailler sur cette application !


## Composants React

Dans la dernière section, vous avez vu comment créer votre première application React.

Cette application est livrée avec une série de fichiers qui font diverses choses, principalement liées à la configuration, mais il y a un fichier qui se distingue : `App.js`.

`App.js` est le **premier composant React** que vous rencontrez.

Son code est le suivant :

```js
import React from 'react'
import logo from './logo.svg'
import './App.css'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  )
}

export default App
```

Une application construite en utilisant React, ou l'un des autres frameworks frontend populaires comme Vue et Svelte par exemple, est construite en utilisant des dizaines de composants.

Mais commençons par analyser ce premier composant. Je vais simplifier le code de ce composant comme ceci :

```js
import React from 'react'
import logo from './logo.svg'
import './App.css'

function App() {
  return /* something */
}

export default App
```

Vous pouvez voir quelques choses ici. Nous _importons_ certaines choses, et nous _exportons_ une fonction appelée `App`.

Les choses que nous importons dans ce cas sont une bibliothèque JavaScript (le package npm `react`), une image SVG, et un fichier CSS.

> `create-react-app` est configuré de manière à nous permettre d'importer des images et du CSS pour les utiliser dans notre JavaScript, mais ce n'est pas quelque chose dont vous devez vous soucier maintenant. Ce dont vous devez vous soucier est le concept de **composant**

`App` est une fonction qui, dans l'exemple original, retourne quelque chose qui à première vue semble assez étrange.

Cela ressemble à du **HTML** mais il contient du JavaScript intégré.

C'est du **JSX**, un langage spécial que nous utilisons pour construire la sortie d'un composant. Nous parlerons plus de JSX dans la section suivante.

En plus de définir du JSX à retourner, un composant a plusieurs autres caractéristiques.

Un composant peut avoir son propre **état**, ce qui signifie qu'il encapsule certaines variables que d'autres composants ne peuvent pas accéder sauf si ce composant expose cet état au reste de l'application.

Un composant peut également recevoir des données d'autres composants. Dans ce cas, nous parlons de **props**.

Ne vous inquiétez pas, nous allons examiner en détail tous ces termes (JSX, State et Props) bientôt.


## Introduction à JSX

Nous ne pouvons pas parler de React sans d'abord expliquer JSX.

Dans la dernière section, vous avez rencontré votre premier composant React, le composant `App` défini dans l'application par défaut construite par `create-react-app`.

Son code était le suivant :

```js
import React from 'react'
import logo from './logo.svg'
import './App.css'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  )
}

export default App
```

Nous avons précédemment ignoré tout ce qui était à l'intérieur de l'instruction `return`, mais dans cette section, nous allons en parler.

Nous appelons JSX tout ce qui est enveloppé à l'intérieur des parenthèses retournées par le composant :

```jsx
<div className="App">
  <header className="App-header">
    <img src={logo} className="App-logo" alt="logo" />
    <p>
      Edit <code>src/App.js</code> and save to reload.
    </p>
    <a
      className="App-link"
      href="https://reactjs.org"
      target="_blank"
      rel="noopener noreferrer"
    >
      Learn React
    </a>
  </header>
</div>
```

Cela _ressemble_ à du HTML, mais ce n'est pas vraiment du HTML. C'est un peu différent.

Et c'est un peu étrange d'avoir ce code à l'intérieur d'un fichier JavaScript. Cela ne ressemble pas du tout à du JavaScript !

Sous le capot, React va traiter le JSX et le transformer en JavaScript que le navigateur pourra interpréter.

Nous écrivons donc du JSX, mais à la fin, il y a une étape de traduction qui le rend digestible pour un interpréteur JavaScript.

React nous offre cette interface pour une raison : **il est plus facile de construire des interfaces utilisateur avec JSX**.

Une fois que vous serez plus familier avec cela, bien sûr.

Dans la section suivante, nous parlerons de la manière dont JSX vous permet de composer facilement une interface utilisateur, puis nous examinerons les différences avec le "HTML normal" que vous devez connaître.


## Utiliser JSX pour composer une interface utilisateur


Comme introduit dans la dernière section, l'un des principaux avantages de JSX est qu'il facilite grandement la construction d'une interface utilisateur.

En particulier, dans un composant React, vous pouvez importer d'autres composants React, et vous pouvez les intégrer et les afficher.

Un composant React est généralement créé dans son propre fichier, car c'est ainsi que nous pouvons facilement le réutiliser (en l'important) dans d'autres composants.

Mais un composant React peut également être créé dans le même fichier qu'un autre composant, si vous prévoyez de l'utiliser uniquement dans ce composant. Il n'y a pas de "règle" ici, vous pouvez faire ce qui vous semble le mieux.

Je crée généralement des fichiers séparés lorsque le nombre de lignes dans un fichier devient trop important.

Pour garder les choses simples, créons un composant dans le même fichier `App.js`.

Nous allons créer un composant `WelcomeMessage` :

```js
function WelcomeMessage() {
  return <p>Bienvenue !</p>
}
```

Vous voyez ? C'est une fonction simple qui retourne une ligne de JSX représentant un élément HTML `p`.

Nous allons l'ajouter au fichier `App.js`.

Maintenant, à l'intérieur du JSX du composant `App`, nous pouvons ajouter `<WelcomeMessage />` pour afficher ce composant dans l'interface utilisateur :

```js
import React from 'react'
import logo from './logo.svg'
import './App.css'

function WelcomeMessage() {
  return <p>Bienvenue !</p>
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <WelcomeMessage />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  )
}

export default App
```

Et voici le résultat. Pouvez-vous voir le message "Bienvenue !" à l'écran ?

![new-component](https://www.freecodecamp.org/news/content/images/2020/11/new-component.png)

Nous disons que `WelcomeMessage` est un **composant enfant** de App, et `App` est son composant parent.

Nous ajoutons le composant `<WelcomeMessage />` comme s'il faisait partie du langage HTML.

C'est la beauté des composants React et de JSX : nous pouvons composer une interface d'application et l'utiliser comme si nous écrivions du HTML.

Avec quelques différences, comme nous le verrons dans la section suivante.


## La différence entre JSX et HTML

JSX ressemble un peu à HTML, mais ce n'est pas le cas.

Dans cette section, je veux vous présenter certaines des choses les plus importantes que vous devez garder à l'esprit lorsque vous utilisez JSX.

L'une des différences pourrait être assez évidente si vous avez regardé le JSX du composant `App` : il y a un attribut étrange appelé `className`.

En HTML, nous utilisons l'attribut `class`. C'est probablement l'attribut le plus largement utilisé, pour diverses raisons. L'une de ces raisons est CSS. L'attribut `class` nous permet de styliser facilement les éléments HTML, et les frameworks CSS comme Tailwind placent cet attribut au centre du processus de conception de l'interface utilisateur CSS.

Mais il y a un problème. Nous écrivons ce code d'interface utilisateur dans un fichier JavaScript, et `class` dans le langage de programmation JavaScript est un mot réservé. Cela signifie que nous ne pouvons pas utiliser ce mot réservé comme nous le voulons. Il sert un but spécifique (définir des classes JavaScript) et les créateurs de React ont dû choisir un nom différent pour celui-ci.

C'est ainsi que nous avons obtenu `className` au lieu de `class`.

Vous devez vous en souvenir surtout lorsque vous copiez/collez du HTML existant.

React fera de son mieux pour s'assurer que les choses ne se cassent pas, mais il générera beaucoup d'avertissements dans les outils de développement :

![className](https://www.freecodecamp.org/news/content/images/2020/11/className.png)

Ce n'est pas la seule fonctionnalité HTML qui souffre de ce problème, mais c'est la plus courante.

Une autre grande différence entre JSX et HTML est que HTML est très _tolérant_, nous pouvons dire. Même si vous avez une erreur dans la syntaxe, ou que vous fermez la mauvaise balise, ou que vous avez une incompatibilité, le navigateur fera de son mieux pour interpréter le HTML sans se casser.

C'est l'une des fonctionnalités principales du Web. Il est très indulgent.

JSX n'est pas indulgent. Si vous oubliez de fermer une balise, vous aurez un message d'erreur clair :

![jsx-error](https://www.freecodecamp.org/news/content/images/2020/11/jsx-error.png)

> React donne généralement de très bons messages d'erreur informatifs qui vous indiquent la bonne direction pour résoudre le problème.

Une autre grande différence entre JSX et HTML est que dans JSX nous pouvons intégrer JavaScript.

Parlons-en dans la section suivante.


## Intégrer JavaScript dans JSX

L'une des meilleures fonctionnalités de React est que nous pouvons facilement intégrer JavaScript dans JSX.

D'autres frameworks frontend, par exemple Angular et Vue, ont leurs propres façons spécifiques d'imprimer des valeurs JavaScript dans le modèle, ou d'effectuer des choses comme des boucles.

React n'ajoute pas de nouvelles choses. Au lieu de cela, il nous permet d'utiliser JavaScript dans le JSX, en utilisant des accolades.

Le premier exemple de cela que je vais vous montrer provient directement du composant `App` que nous avons étudié jusqu'à présent.

Nous importons le fichier SVG `logo` en utilisant

```js
import logo from './logo.svg'
```

et ensuite dans le JSX nous attribuons ce fichier SVG à l'attribut `src` d'une balise `img` :

```js
<img src={logo} className="App-logo" alt="logo" />
```

Faisons un autre exemple. Supposons que le composant `App` ait une variable appelée `message` :

```js
function App() {
  const message = 'Bonjour !'
  //...
}
```

Nous pouvons imprimer cette valeur dans le JSX en ajoutant `{message}` n'importe où dans le JSX.

À l'intérieur des accolades `{ }` nous pouvons ajouter n'importe quelle instruction JavaScript, mais _une seule_ instruction pour chaque bloc d'accolades.

Et l'instruction doit retourner quelque chose.

Par exemple, c'est une instruction courante que vous trouverez dans JSX. Nous avons un opérateur ternaire où nous définissons une condition (`message === 'Bonjour !'`), et nous imprimons une valeur si la condition est vraie, ou une autre valeur (le contenu de `message` dans ce cas) si la condition est fausse :

```js
{
  message === 'Bonjour !' ? 'Le message était "Bonjour !"' : message
}
```


## Gestion de l'état dans React

Chaque composant React peut avoir son propre **état**.

Que voulons-nous dire par _état_ ? L'état est l'**ensemble de données qui est géré par le composant**.

Prenons l'exemple d'un formulaire. Chaque élément d'entrée individuel du formulaire est responsable de la gestion de son état : ce qui est écrit à l'intérieur.

Un bouton est responsable de savoir s'il est cliqué ou non. S'il est en focus.

Un lien est responsable de savoir si la souris le survole.

Dans React, ou dans tout autre framework/bibliothèque basé sur des composants, toutes nos applications sont basées et font un usage intensif de l'état des composants.

Nous gérons l'état en utilisant l'utilitaire `useState` fourni par React. C'est techniquement un **hook** (vous n'avez pas besoin de connaître les détails des hooks pour l'instant, mais c'est ce que c'est).

Vous importez `useState` depuis React de cette manière :

```js
import React, { useState } from 'react'
```

En appelant `useState()`, vous obtiendrez une nouvelle variable d'état, et une fonction que nous pouvons appeler pour modifier sa valeur.

`useState()` accepte la valeur initiale de l'élément d'état et retourne un tableau contenant la variable d'état, et la fonction que vous appelez pour modifier l'état.

Exemple :

```js
const [count, setCount] = useState(0)
```

C'est important. Nous ne pouvons pas simplement modifier la valeur d'une variable d'état directement. Nous devons appeler sa fonction modificatrice. Sinon, le composant React ne mettra pas à jour son interface utilisateur pour refléter les changements des données. 

Appeler le modificateur est le moyen par lequel nous pouvons dire à React que l'état du composant a changé.

La syntaxe est un peu étrange, n'est-ce pas ? Puisque `useState()` retourne un tableau, nous utilisons la destructuration de tableau pour accéder à chaque élément individuel, comme ceci : `const [count, setCount] = useState(0)`

Voici un exemple pratique :

```js
import { useState } from 'react'

const Counter = () => {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>Vous avez cliqué {count} fois</p>
      <button onClick={() => setCount(count + 1)}>Cliquez ici</button>
    </div>
  )
}

ReactDOM.render(<Counter />, document.getElementById('app'))
```

Vous pouvez ajouter autant d'appels `useState()` que vous le souhaitez, pour créer autant de variables d'état que vous le souhaitez :

```js
const [count, setCount] = useState(0)
const [anotherCounter, setAnotherCounter] = useState(0)
```


## Props des composants dans React

Nous appelons `props` les valeurs initiales passées à un composant.

Nous avons précédemment créé un composant `WelcomeMessage`

```js
function WelcomeMessage() {
  return <p>Bienvenue !</p>
}
```

et nous l'avons utilisé comme ceci :

```js
<WelcomeMessage />
```

Ce composant n'a aucune valeur initiale. Il n'a pas de props.

Les props peuvent être passées en tant qu'attributs au composant dans le JSX :

```js
<WelcomeMessage myprop={'unevaleur'} />
```

et à l'intérieur du composant nous recevons les props en tant qu'arguments :

```js
function WelcomeMessage(props) {
  return <p>Bienvenue !</p>
}
```

Il est courant d'utiliser la destructuration d'objet pour obtenir les props par leur nom :

```js
function WelcomeMessage({ myprop }) {
  return <p>Bienvenue !</p>
}
```

Maintenant que nous avons la prop, nous pouvons l'utiliser à l'intérieur du composant. Par exemple, nous pouvons imprimer sa valeur dans le JSX :

```js
function WelcomeMessage({ myprop }) {
  return <p>{myprop}</p>
}
```

Les accolades ici ont diverses significations. Dans le cas de l'argument de la fonction, les accolades sont utilisées dans le cadre de la syntaxe de destructuration d'objet.

Ensuite, nous les utilisons pour définir le bloc de code de la fonction, et enfin dans le JSX pour imprimer la valeur JavaScript.

Passer des props aux composants est un excellent moyen de transmettre des valeurs dans votre application.

Un composant contient soit des données (a un état), soit reçoit des données via ses props.

Nous pouvons également envoyer des fonctions en tant que props, de sorte qu'un composant enfant peut appeler une fonction dans le composant parent.

Une prop spéciale est appelée `children`. Elle contient la valeur de tout ce qui est passé entre les balises d'ouverture et de fermeture du composant, par exemple :

```html
<WelcomeMessage> Voici un message </WelcomeMessage>
```

Dans ce cas, à l'intérieur de `WelcomeMessage`, nous pourrions accéder à la valeur `Voici un message` en utilisant la prop `children` :

```js
function WelcomeMessage({ children }) {
  return <p>{children}</p>
}
```


## Flux de données dans une application React

Dans une application React, les données circulent généralement d'un composant parent vers un composant enfant, en utilisant des props comme nous l'avons vu dans la section précédente :

```js
<WelcomeMessage myprop={'unevaleur'} />
```

Si vous passez une fonction au composant enfant, vous pouvez cependant changer l'état du composant parent à partir d'un composant enfant :

```js
const [count, setCount] = useState(0)

<Counter setCount={setCount} />
```

À l'intérieur du composant Counter, nous pouvons maintenant récupérer la prop `setCount` et l'appeler pour mettre à jour l'état `count` dans le composant parent, lorsqu'un événement se produit :

```js
function Counter({ setCount }) {
  //...

  setCount(1)

  //...
}
```

Vous devez savoir qu'il existe des moyens plus avancés de gérer les données, qui incluent l'API Context et des bibliothèques comme Redux. Mais celles-ci introduisent plus de complexité, et 90 % du temps, utiliser ces deux méthodes que je viens d'expliquer est la solution parfaite.


## Gestion des événements utilisateur dans React

React fournit un moyen facile de gérer les événements déclenchés par des événements DOM comme les clics, les événements de formulaire, et plus encore.

Parlons des événements de clic, qui sont assez simples à comprendre.

Vous pouvez utiliser l'attribut `onClick` sur n'importe quel élément JSX :

```js
<button
  onClick={(event) => {
    /* gérer l'événement */
  }}
>
  Cliquez ici
</button>
```

Lorsque l'élément est cliqué, la fonction passée à l'attribut `onClick` est déclenchée.

Vous pouvez définir cette fonction en dehors du JSX :

```js
const handleClickEvent = (event) => {
  /* gérer l'événement */
}

function App() {
  return <button onClick={handleClickEvent}>Cliquez ici</button>
}
```

Lorsque l'événement `click` est déclenché sur le bouton, React appelle la fonction de gestion de l'événement.

React prend en charge une grande quantité de types d'événements, comme `onKeyUp`, `onFocus`, `onChange`, `onMouseDown`, `onSubmit` et bien d'autres.


## Événements de cycle de vie dans un composant React

Jusqu'à présent, nous avons vu comment gérer l'état avec le hook `useState`.

Il y a un autre hook que je veux vous présenter dans ce livre : `useEffect`.

Le hook `useEffect` permet aux composants d'avoir accès aux événements de cycle de vie d'un composant.

Lorsque vous appelez le hook, vous lui passez une fonction. La fonction sera exécutée par React lorsque le composant est rendu pour la première fois, et à chaque nouveau rendu/mise à jour.

React met d'abord à jour le DOM, puis appelle toute fonction passée à `useEffect()`.

Tout cela sans bloquer le rendu de l'interface utilisateur, même avec du code bloquant.

Voici un exemple :

```js
const { useEffect, useState } = React

const CounterWithNameAndSideEffect = () => {
  const [count, setCount] = useState(0)

  useEffect(() => {
    console.log(`Vous avez cliqué ${count} fois`)
  })

  return (
    <div>
      <p>Vous avez cliqué {count} fois</p>
      <button onClick={() => setCount(count + 1)}>Cliquez ici</button>
    </div>
  )
}
```

Puisque la fonction useEffect() est exécutée à chaque nouveau rendu/mise à jour du composant, nous pouvons dire à React de la sauter, pour des raisons de performance. Nous faisons cela en ajoutant un deuxième paramètre qui est un tableau contenant une liste de variables d'état à surveiller. 

React ne réexécutera l'effet de bord que si l'un des éléments de ce tableau change.

```js
useEffect(() => {
  console.log(`Salut ${name} vous avez cliqué ${count} fois`)
}, [name, count])
```

De même, vous pouvez dire à React d'exécuter l'effet de bord une seule fois (au moment du montage), en passant un tableau vide :

```js
useEffect(() => {
  console.log(`Composant monté`)
}, [])
```

Vous pourriez vous retrouver à utiliser cette option souvent.

useEffect() est idéal pour ajouter des logs, accéder à des API tierces, et bien plus encore.


## Où aller à partir d'ici

Maîtriser les sujets expliqués dans cet article est une excellente étape vers votre objectif d'apprendre React.

Je veux vous donner quelques conseils maintenant, car il est facile de se perdre dans la mer de tutoriels et de cours sur React.

Que devriez-vous apprendre ensuite ?

Apprenez plus de théorie sur le [Virtual DOM](https://flaviocopes.com/react-virtual-dom/), [l'écriture de code déclaratif](https://flaviocopes.com/react-declarative/), [le flux de données unidirectionnel](https://flaviocopes.com/react-unidirectional-data-flow/), [l'immutabilité](https://flaviocopes.com/react-immutability/), [la composition](https://flaviocopes.com/react-composition/).

Commencez à construire quelques applications React simples. Par exemple, [construisez un simple compteur](https://flaviocopes.com/react-example-counter/) ou [interagissez avec une API publique](https://flaviocopes.com/react-example-githubusers/).

Apprenez à effectuer un [rendu conditionnel](https://flaviocopes.com/react-conditional-rendering/), comment effectuer des [boucles dans JSX](https://flaviocopes.com/react-how-to-loop/), comment utiliser les [React Developer Tools](https://flaviocopes.com/react-developer-tools/).

Apprenez à appliquer du CSS dans une application React, avec du [CSS simple](https://flaviocopes.com/react-css/) ou des [Styled Components](https://flaviocopes.com/styled-components/).

Apprenez à gérer l'état en utilisant l'[API Context](https://flaviocopes.com/react-context-api/), useContext et [Redux](https://flaviocopes.com/redux/).

Apprenez à interagir avec des [formulaires](https://flaviocopes.com/react-forms/).

Apprenez à utiliser [React Router](https://flaviocopes.com/react-router/).

Apprenez à [tester des applications React](https://flaviocopes.com/react-testing-components/).

Apprenez un framework d'application construit sur React, comme [Gatsby](https://flaviocopes.com/gatsby/) ou [Next.js](https://flaviocopes.com/nextjs/).

Surtout, assurez-vous de pratiquer en construisant des applications d'exemple pour appliquer tout ce que vous avez appris.

## Conclusion

Merci beaucoup d'avoir lu ce guide.

J'espère qu'il vous inspirera à en apprendre davantage sur React et tout ce que vous pouvez faire avec !

N'oubliez pas que vous pouvez [télécharger ce guide au format PDF / ePub / Mobi gratuitement](https://flaviocopes.com/page/react-handbook/) si vous le souhaitez.

Je publie des tutoriels de programmation tous les jours sur mon site web [flaviocopes.com](https://flaviocopes.com) si vous voulez consulter plus de contenu comme celui-ci.

Vous pouvez me joindre sur Twitter [@flaviocopes](https://twitter.com/flaviocopes).