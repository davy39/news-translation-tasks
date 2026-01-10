---
title: Le guide du débutant pour React
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-01-29T13:25:48.000Z'
originalURL: https://freecodecamp.org/news/the-beginners-guide-to-react-9be65f50a55c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uKVfsFREG2HMCL8hJdcZ5Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Le guide du débutant pour React
seo_desc: 'Interested in learning React? Get my React Handbook


  React is a JavaScript library that aims to simplify the development of visual interfaces.

  Developed at Facebook and released to the world in 2013, it drives some of the most
  widely used code in the...'
---

> Intéressé par l'apprentissage de React ? Obtenez mon [React Handbook](https://flaviocopes.com/page/react-handbook/)

React est une bibliothèque JavaScript qui vise à simplifier le développement des interfaces visuelles.

Développée chez Facebook et publiée en 2013, elle alimente certains des codes les plus utilisés au monde. Elle alimente Facebook et Instagram parmi de nombreuses autres entreprises logicielles.

Son objectif principal est de faciliter le raisonnement sur une interface et son état à tout moment en divisant l'UI en une collection de composants.

React est utilisé pour construire des applications web monopages, ainsi que de nombreuses autres bibliothèques et frameworks qui étaient disponibles avant l'arrivée de React.

### Pourquoi React est-il si populaire ?

React a pris d'assaut le monde du développement web frontend. Pourquoi ?

#### Moins complexe que les alternatives

À l'époque où React a été annoncé, Ember.js et Angular 1.x étaient les choix prédominants pour les frameworks. Ces deux frameworks imposaient trop de conventions au code, ce qui rendait le portage d'une application existante peu pratique.

React a été créé pour être très facile à intégrer dans un projet existant. C'est ainsi qu'ils ont dû le faire chez Facebook afin de l'introduire dans la base de code existante. De plus, ces deux frameworks apportaient trop de choses, tandis que React a choisi de n'implémenter que la couche Vue au lieu de la pile MVC complète.

#### Timing parfait

À la même époque, Angular 2.x a été annoncé par Google, avec son incompatibilité ascendante et les changements majeurs qu'il allait apporter. Passer d'Angular 1 à 2 était comme passer à un framework différent. Et ce fait, ainsi que les améliorations de vitesse d'exécution promises par React, ont fait de React quelque chose que les développeurs étaient impatients d'essayer.

#### Soutenu par Facebook

Être soutenu par Facebook bénéficie à un projet s'il s'avère être un succès. Mais ce n'est pas une garantie, et il y a de nombreux projets open source échoués de Facebook et Google (entre autres).

### React est-il vraiment si simple ?

Même si j'ai dit que React est plus simple que les frameworks alternatifs, se plonger dans React reste complexe. Cela est principalement dû aux technologies corollaires qui peuvent être intégrées avec React, comme Redux, Relay ou GraphQL.

React en lui-même a une API très petite.

Il n'y a pas beaucoup plus dans React que ces concepts :

* Composants
* JSX
* État
* Props

Nous verrons chacun d'eux dans mes prochains articles.

### JSX

De nombreux développeurs, y compris moi-même, ont d'abord pensé que JSX était horrible et ont rapidement rejeté React.

Même s'ils disaient que JSX n'était pas obligatoire, utiliser React sans JSX était douloureux.

Il m'a fallu quelques années de regard occasionnel pour commencer à digérer JSX, et maintenant je le préfère largement à l'alternative (c'est-à-dire, utiliser des templates).

Le principal avantage de l'utilisation de JSX est que vous n'interagissez qu'avec des objets JavaScript, et non avec des chaînes de templates.

JSX n'est pas du HTML intégré.

De nombreux tutoriels pour les débutants en React aiment reporter l'introduction de JSX pour plus tard, car ils supposent que le lecteur serait mieux sans. Puisque je suis maintenant un fan de JSX, cependant, je vais immédiatement me plonger dedans.

Voici comment vous définissez une balise h1 contenant une chaîne :

```jsx
const element = <h1>Bonjour, le monde !</h1>
```

Cela ressemble à un étrange mélange de JavaScript et de HTML, mais en réalité, c'est tout du JavaScript.

Ce qui ressemble à du HTML est en fait une syntaxe sucrée pour définir des composants et leur positionnement dans le balisage.

Dans une expression JSX, les attributs peuvent être insérés très facilement :

```jsx
const myId = 'test' 
const element = <h1 id={myId}>Bonjour, le monde !</h1>
```

Vous devez simplement faire attention lorsque qu'un attribut contient un tiret (`-`), qui est converti en syntaxe camelCase, ainsi qu'à ces deux cas spéciaux :

* `class` devient `className`
* `for` devient `htmlFor`

car ils sont des mots réservés en JavaScript.

Voici un extrait JSX qui enveloppe deux composants dans une balise `div` :

```jsx
<div> 
  <BlogPostsList />
  <Sidebar /> 
</div>
```

Une balise doit toujours être fermée, car cela ressemble plus à du XML qu'à du HTML (si vous vous souvenez des jours de XHTML, cela sera familier, mais depuis, la syntaxe lâche de HTML5 a gagné). Dans ce cas, une balise auto-fermante est utilisée.

JSX, lorsqu'il a été introduit avec React, n'est plus une technologie exclusive à React.

### Composants React

#### Qu'est-ce qu'un composant React ?

Un composant est une pièce isolée de l'interface. Par exemple, dans une page d'accueil de blog typique, vous pourriez trouver le composant Sidebar et le composant Blog Posts List. Ils sont à leur tour composés de composants eux-mêmes, donc vous pourriez avoir une liste de composants Blog post, chacun pour chaque article de blog, et chacun avec ses propres propriétés.

![Image](https://cdn-media-1.freecodecamp.org/images/Ok51aJciCr9ybh8lww0UL2Hl7g37lC2MJjne)

React rend cela très simple : tout est un composant.

Même les balises HTML simples sont des composants à part entière, et elles sont ajoutées par défaut.

Les deux lignes suivantes sont équivalentes — elles font la même chose. L'une avec **JSX**, l'autre sans, en injectant `<h1>Bonjour le monde !</h1>` dans un élément avec l'id app.

```jsx
import React from 'react' 
import ReactDOM from 'react-dom' 

ReactDOM.render( 
  <h1>Bonjour le monde !</h1>, 
  document.getElementById('app') 
)

ReactDOM.render( 
  React.DOM.h1(null, "Bonjour le monde !"), 
  document.getElementById('app') 
)
```

Voyez, `React.DOM` nous expose un composant `h1`. Quelles autres balises HTML sont disponibles ? Toutes ! Vous pouvez inspecter ce que `React.DOM` offre en le tapant dans la console du navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/9DaF1EtL86DXgUhe2wvb92sjYFLx6S5nxcIr)

(la liste continue…)

Les composants intégrés sont bien, mais vous les dépasserez rapidement. Ce que React excelle à faire, c'est de nous permettre de composer une UI en composant des composants personnalisés.

### Composants personnalisés

Il y a 2 façons de définir un composant dans React :

Un composant sans état ne gère pas d'état interne, et est simplement une fonction :

```jsx
const BlogPostExcerpt = () => {
 return (
    <div>
      <h1>Titre</h1>
      <p>Description</p>
    </div> 
  ) 
}
```

Un composant avec état est une classe, qui gère l'état dans ses propres propriétés :

```jsx
import React, { Component } from 'react'

class BlogPostExcerpt extends Component { 
  render() { 
    return ( 
      <div>
        <h1>Titre</h1> 
        <p>Description</p> 
      </div> 
    ) 
  } 
}
```

Tel qu'ils sont, ils sont équivalents car il n'y a pas encore de gestion d'état (à venir dans les prochains articles).

Il existe une troisième syntaxe qui utilise la syntaxe `ES5` / `ES2015` sans les classes :

```jsx
import React from 'react'

React.createClass({ 
  render() { 
    return ( 
      <div> 
        <h1>Titre</h1>
        <p>Description</p> 
      </div> 
    ) 
  } 
})
```

Vous verrez rarement cela dans les bases de code modernes `> ES6`.

Props est la manière dont les composants obtiennent leurs propriétés. En partant du composant parent, chaque composant enfant reçoit ses props du parent. Dans un composant sans état, props est tout ce qui est passé, et ils sont disponibles en ajoutant `props` comme argument de la fonction :

```jsx
const BlogPostExcerpt = (props) => { 
  return ( 
    <div> 
      <h1>{props.title}</h1> 
      <p>{props.description}</p> 
    </div> 
  ) 
}
```

Dans un composant avec état, les props sont passées par défaut. Il n'est pas nécessaire d'ajouter quoi que ce soit de spécial, et elles sont accessibles en tant que `this.props` dans une instance de composant.

```jsx
import React, { Component } from 'react'

class BlogPostExcerpt extends Component { 
  render() { 
    return ( 
      <div>
        <h1>{this.props.title}</h1>  
        <p>{this.props.description}</p> 
      </div> 
    ) 
  } 
}
```

### PropTypes

Puisque JavaScript est un langage à typage dynamique, nous n'avons pas vraiment de moyen de forcer le type d'une variable au moment de la compilation. Si nous passons des types invalides, ils échoueront à l'exécution ou donneront des résultats étranges si les types sont compatibles mais pas ceux que nous attendons.

Flow et TypeScript aident beaucoup, mais React a un moyen de directement aider avec les types de props. Même avant d'exécuter le code, nos outils (éditeurs, linters) peuvent détecter lorsque nous passons les mauvaises valeurs :

```jsx
import PropTypes from 'prop-types';
import React from 'react' 

class BlogPostExcerpt extends Component { 
  render() { 
    return ( 
      <div> 
        <h1>{this.props.title}</h1> 
        <p>{this.props.description}</p> 
      </div> 
    ) 
  } 
}

BlogPostExcerpt.propTypes = { 
  title: PropTypes.string, 
  description: PropTypes.string 
};

export default BlogPostExcerpt
```

### Quels types pouvons-nous utiliser

Ce sont les types fondamentaux que nous pouvons accepter :

* PropTypes.array
* PropTypes.bool
* PropTypes.func
* PropTypes.number
* PropTypes.object
* PropTypes.string
* PropTypes.symbol

Nous pouvons accepter l'un des deux types :

```jsx
PropTypes.oneOfType([ PropTypes.string, PropTypes.number ]),
```

Nous pouvons accepter l'une des nombreuses valeurs :

```jsx
PropTypes.oneOf(['Test1', 'Test2']),
```

Nous pouvons accepter une instance d'une classe :

```jsx
PropTypes.instanceOf(Something)
```

Nous pouvons accepter n'importe quel nœud React :

```jsx
PropTypes.node
```

ou même n'importe quel type du tout :

```jsx
PropTypes.any
```

Les tableaux ont une syntaxe spéciale que nous pouvons utiliser pour accepter un tableau d'un type particulier :

```jsx
PropTypes.arrayOf(PropTypes.string)
```

Nous pouvons composer une propriété d'objet en utilisant :

```jsx
PropTypes.shape({ 
  color: PropTypes.string, 
  fontSize: PropTypes.number 
})

```

### Exiger des propriétés

Ajouter `isRequired` à n'importe quelle option PropTypes fera en sorte que React retourne une erreur si cette propriété est manquante :

```jsx
PropTypes.arrayOf(PropTypes.string).isRequired, PropTypes.string.isRequired,
```

### Valeurs par défaut pour les props

Si une valeur n'est pas requise, nous devons spécifier une valeur par défaut pour elle si elle est manquante lorsque le composant est initialisé.

```jsx
BlogPostExcerpt.propTypes = { 
  title: PropTypes.string, 
  description: PropTypes.string 
}

BlogPostExcerpt.defaultProps = { 
  title: '', 
  description: '' 
}
```

Certains outils, comme ESLint, ont la capacité de forcer la définition des defaultProps pour un composant avec certains propTypes non explicitement requis.

### Comment les props sont passées

Lors de l'initialisation d'un composant, passez les props de manière similaire aux attributs HTML :

```jsx
const desc = 'Une description' 
//... 
<BlogPostExcerpt title="Un article de blog" description={desc} />

```

Nous avons passé le titre en tant que chaîne simple (quelque chose que nous pouvons faire uniquement avec des chaînes !), et la description en tant que variable.

### Children

Une prop spéciale est `children`. Elle contient la valeur de tout ce qui est passé dans le `body` du composant. Par exemple :

```jsx
<BlogPostExcerpt title="Un article de blog" description={desc}> 
  Quelque chose 
</BlogPostExcerpt>

```

Dans ce cas, à l'intérieur de `BlogPostExcerpt`, nous pourrions accéder à « Quelque chose » en regardant `this.props.children`.

Alors que les Props permettent à un composant de recevoir des propriétés de son parent (ils pourraient être « instruits » pour imprimer certaines données par exemple), l'état permet à un composant de prendre vie par lui-même, et d'être indépendant de l'environnement environnant.

Rappelez-vous : seuls les composants basés sur des classes peuvent avoir un état. Donc si vous devez gérer l'état dans un composant sans état (basé sur une fonction), vous devez d'abord le « mettre à niveau » vers un composant de classe :

```jsx
const BlogPostExcerpt = () => { 
  return ( 
    <div>
      <h1>Titre</h1>
      <p>Description</p> 
    </div> 
  )
}

```

devient :

```jsx
import React, { Component } from 'react'

class BlogPostExcerpt extends Component { 
  render() { 
    return (
      <div>  
        <h1>Titre</h1> 
        <p>Description</p>
      </div>
    ) 
  } 
}

```

### Définir l'état par défaut

Dans le constructeur du composant, initialisez `this.state`. Par exemple, le composant BlogPostExcerpt pourrait avoir un état `clicked` :

```jsx
class BlogPostExcerpt extends Component {
  constructor(props) { 
    super(props) 
    this.state = { clicked: false } 
  }

  render() { 
    return (
      <div> 
        <h1>Titre</h1>
        <p>Description</p> 
      </div> 
    ) 
  } 
}
```

### Accéder à l'état

L'état _clicked_ peut être accédé en référençant `this.state.clicked` :

```jsx
class BlogPostExcerpt extends Component {
  constructor(props) { 
    super(props)
    this.state = { clicked: false }
  }

  render() { 
    return (
      <div> 
        <h1>Titre</h1> 
        <p>Description</p> 
        <p>Cliqué : {this.state.clicked}</p> 
      </div> 
    ) 
  } 
}
```

### Mutating the state

Un état ne doit jamais être muté en utilisant

```jsx
this.state.clicked = true
```

Au lieu de cela, vous devez toujours utiliser `setState()` à la place, en lui passant un objet :

```jsx
this.setState({ clicked: true })
```

L'objet peut contenir un sous-ensemble, ou un sur-ensemble, de l'état. Seules les propriétés que vous passez seront mutées. Celles omises seront laissées dans leur état actuel.

#### Pourquoi vous devez toujours utiliser `setState()`

La raison est que, en utilisant cette méthode, React sait que l'état a changé. Il déclenchera alors la série d'événements qui mèneront à la ré-exécution du composant, ainsi qu'à toute mise à jour du DOM.

### L'état est encapsulé

Un parent d'un composant ne peut pas savoir si l'enfant est avec état ou sans état. Il en va de même pour les enfants d'un composant.

Être avec état ou sans état (fonctionnel ou basé sur une classe) est entièrement un détail d'implémentation dont les autres composants n'ont pas besoin de se soucier.

Cela nous amène au flux de données unidirectionnel.

### Flux de données unidirectionnel

Un état appartient toujours à un composant. Toute donnée affectée par cet état ne peut affecter que les composants en dessous : ses enfants.

Changer un état sur un composant n'affectera jamais son parent, ou ses frères et sœurs, ou tout autre composant dans l'application — juste ses enfants.

C'est la raison pour laquelle, de nombreuses fois, l'état est déplacé vers le haut dans l'arborescence des composants.

### Déplacer l'état vers le haut dans l'arborescence

En raison des règles de flux de données unidirectionnel, si deux composants doivent partager un état, l'état doit être déplacé vers un ancêtre commun.

Souvent, l'ancêtre le plus proche est le meilleur endroit pour gérer l'état, mais ce n'est pas une règle obligatoire.

L'état est passé aux composants qui ont besoin de cette valeur via les props :

```jsx
class Converter extends React.Component { 
  constructor(props) { 
    super(props)
    this.state = { currency: '€' } 
  }

  render() { 
    return ( 
      <div> 
        <Display currency={this.state.currency} />
        <CurrencySwitcher currency={this.state.currency} />
      </div> 
    ) 
  } 
}

```

L'état peut être muté par un composant enfant en passant une fonction de mutation en tant que prop :

```jsx
class Converter extends React.Component { 
  constructor(props) { 
    super(props) 
    this.state = { currency: '€' } 
  }

  handleChangeCurrency = (event) => { 
    this.setState({ 
      currency: this.state.currency === '€' ? '$' : '€' 
    }) 
  }

  render() { 
    return ( 
      <div> 
        <Display currency={this.state.currency} /> 
        <CurrencySwitcher currency={this.state.currency} handleChangeCurrency={this.handleChangeCurrency} /> 
      </div> 
    ) 
  } 
}

const CurrencySwitcher = (props) => { 
  return ( 
    <button onClick={props.handleChangeCurrency}> 
      La devise actuelle est {props.currency}. Changez-la ! 
    </button> 
  ) 
}

const Display = (props) => { 
  return ( 
    <p>La devise actuelle est {props.currency}.</p> 
  ) 
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/W5hfnSrCoSOqkbTNbDn0b1bOocYiHkO70ZgB)

### Événements

React fournit un moyen facile de gérer les événements. Préparez-vous à dire adieu à `addEventListener` :)

Dans l'article précédent sur l'État, vous avez vu cet exemple :

```jsx
const CurrencySwitcher = (props) => { 
  return ( 
    <button onClick={props.handleChangeCurrency}> 
      La devise actuelle est {props.currency}. Changez-la ! 
    </button> 
  ) 
}

```

Si vous avez utilisé JavaScript pendant un certain temps, cela ressemble à de vieux gestionnaires d'événements JavaScript. Mais cette fois, vous définissez tout en JavaScript, pas dans votre HTML, et vous passez une fonction, pas une chaîne.

Les noms réels des événements sont un peu différents, car dans React vous utilisez camelCase pour tout. Donc `onclick` devient `onClick`, `onsubmit` devient `onSubmit`.

Pour référence, voici l'ancien HTML avec des événements JavaScript mélangés :

```jsx
<button onclick="handleChangeCurrency()"> ... <;/button>
```

### Gestionnaires d'événements

Il est conventionnel d'avoir des gestionnaires d'événements définis comme des méthodes sur la classe de composant :

```jsx
class Converter extends React.Component { handleChangeCurrency = (event) => { this.setState({ currency: this.state.currency === '€' ? '$' : '€' }) } }

```

Tous les gestionnaires reçoivent un objet événement qui adhère, multi-navigateur, à la [spécification des événements UI W3C](https://www.w3.org/TR/DOM-Level-3-Events/).

### Lier `this` dans les méthodes

N'oubliez pas de lier les méthodes. Les méthodes des classes ES6 ne sont pas liées par défaut. Cela signifie que `this` n'est pas défini à moins que vous ne définissiez les méthodes comme

```jsx
class Converter extends React.Component { 
  handleClick = (e) => { /* ... */ } 
  //... 
}

```

lors de l'utilisation de la syntaxe d'initialisation de propriété avec Babel (activée par défaut dans `create-react-app`).

Sinon, vous devez le lier manuellement dans le constructeur :

```jsx
class Converter extends React.Component { 
  constructor(props) { 
    super(props); 
    this.handleClick = this.handleClick.bind(this); 
  }

  handleClick(e) {} 
}

```

### La référence des événements

Il y a beaucoup d'événements supportés, donc voici une liste de résumé.

#### Presse-papiers

* onCopy
* onCut
* onPaste

#### Composition

* onCompositionEnd
* onCompositionStart
* onCompositionUpdate

#### Clavier

* onKeyDown
* onKeyPress
* onKeyUp

#### Focus

* onFocus
* onBlur

#### Formulaire

* onChange
* onInput
* onSubmit

#### Souris

* onClick
* onContextMenu
* onDoubleClick
* onDrag
* onDragEnd
* onDragEnter
* onDragExit
* onDragLeave
* onDragOver
* onDragStart
* onDrop
* onMouseDown
* onMouseEnter
* onMouseLeave
* onMouseMove
* onMouseOut
* onMouseOver
* onMouseUp

#### Sélection

* onSelect

#### Tactile

* onTouchCancel
* onTouchEnd
* onTouchMove
* onTouchStart

#### UI

* onScroll

#### Roue de la souris

* onWheel

#### Médias

* onAbort
* onCanPlay
* onCanPlayThrough
* onDurationChange
* onEmptied
* onEncrypted
* onEnded
* onError
* onLoadedData
* onLoadedMetadata
* onLoadStart
* onPause
* onPlay
* onPlaying
* onProgress
* onRateChange
* onSeeked
* onSeeking
* onStalled
* onSuspend
* onTimeUpdate
* onVolumeChange
* onWaiting

#### Image

* onLoad
* onError

#### Animation

* onAnimationStart
* onAnimationEnd
* onAnimationIteration

#### Transition

* onTransitionEnd

### L'approche déclarative de React

Vous rencontrerez des articles décrivant React comme une **approche déclarative pour construire des UIs**.

Voir [programmation déclarative](https://flaviocopes.com/functional-programming-js/declarative) pour en savoir plus sur la programmation déclarative.

### Approche déclarative de React

React a rendu son « approche déclarative » assez populaire et directe, de sorte qu'elle a imprégné le monde du frontend avec React.

Ce n'est vraiment pas un nouveau concept, mais React a rendu la construction d'UIs beaucoup plus déclarative qu'avec les templates HTML. Vous pouvez construire des interfaces Web sans même toucher directement au DOM, et vous pouvez avoir un système d'événements sans avoir à interagir avec les événements DOM réels.

Par exemple, rechercher des éléments dans le DOM en utilisant jQuery ou des événements DOM est une approche itérative.

L'approche déclarative de React abstrait cela pour nous. Nous disons simplement à React que nous voulons qu'un composant soit rendu d'une certaine manière, et nous n'avons jamais à interagir avec le DOM pour le référencer plus tard.

### Le DOM virtuel

De nombreux frameworks existants, avant l'arrivée de React, manipulaient directement le DOM à chaque changement.

### Le « vrai » DOM

Qu'est-ce que le DOM, tout d'abord ? Le DOM (_Document Object Model_) est une représentation arborescente de la page, commençant par la balise `<html>`, descendant dans chacun des enfants, appelés nœuds.

Il est conservé dans la mémoire du navigateur, et directement lié à ce que vous voyez dans une page. Le DOM a une API que vous pouvez utiliser pour le parcourir, accéder à chaque nœud, les filtrer et les modifier.

L'API est la syntaxe familière que vous avez probablement vue de nombreuses fois, si vous n'utilisiez pas l'API abstraite fournie par jQuery et ses amis :

```jsx
document.getElementById(id) 
document.getElementsByTagName(name) 
document.createElement(name) 
parentNode.appendChild(node) 
element.innerHTML 
element.style.left 
element.setAttribute()
element.getAttribute() 
element.addEventListener() 
window.content 
window.onload 
window.dump()
window.scrollTo()
```

React conserve une copie de la représentation du DOM, car le DOM virtuel concerne le rendu de React.

### Le DOM virtuel

Chaque fois que le DOM change, le navigateur doit effectuer deux opérations intensives : repaint (changements visuels ou de contenu d'un élément qui n'affectent pas la mise en page et le positionnement par rapport aux autres éléments) et reflow (recalculer la mise en page d'une partie de la page — ou la mise en page de la page entière).

React utilise un DOM virtuel pour aider le navigateur à utiliser moins de ressources lorsque des changements doivent être effectués sur une page.

Lorsque vous appelez `setState()` sur un composant, en spécifiant un état différent de celui précédent, React marque ce composant comme **dirty**. C'est la clé : React ne met à jour que lorsqu'un composant change l'état explicitement.

Ce qui se passe ensuite est :

* React met à jour le DOM virtuel relatif aux composants marqués comme dirty (avec quelques vérifications supplémentaires, comme le déclenchement de `shouldComponentUpdate()`)
* Exécute l'algorithme de différenciation pour réconcilier les changements
* Met à jour le vrai DOM

### Pourquoi le DOM virtuel est-il utile : le batching

L'essentiel est que React regroupe beaucoup de changements et effectue une mise à jour unique du vrai DOM. Il le fait en changeant tous les éléments qui doivent être changés en même temps, de sorte que le repaint et le reflow que le navigateur doit effectuer pour rendre les changements sont exécutés une seule fois.

> Intéressé par l'apprentissage de React ? Obtenez mon [React Handbook](https://flaviocopes.com/page/react-handbook/)