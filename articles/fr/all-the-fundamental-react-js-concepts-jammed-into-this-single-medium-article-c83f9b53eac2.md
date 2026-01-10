---
title: Tous les concepts fondamentaux de React.js, condensés dans cet article
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-18T16:06:34.000Z'
originalURL: https://freecodecamp.org/news/all-the-fundamental-react-js-concepts-jammed-into-this-single-medium-article-c83f9b53eac2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qUlxDdY3T-rDtJ4LhLGkEg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Tous les concepts fondamentaux de React.js, condensés dans cet article
seo_desc: 'By Samer Buna


  Update: This article is now part of my book “React.js Beyond The Basics”.

  Read the updated version of this content and more about React at jscomplete.com/react-beyond-basics.


  This article is not going to cover what React is or why you...'
---

Par Samer Buna

> **Mise à jour :** Cet article fait maintenant partie de mon livre « React.js Beyond The Basics ».

> Lisez la version mise à jour de ce contenu et plus sur React sur [**_jscomplete.com/react-beyond-basics_**](https://jscomplete.com/g/react-fundamentals)_._

Cet article ne va pas couvrir ce qu'est React ou [pourquoi vous devriez l'apprendre](https://medium.freecodecamp.org/yes-react-is-taking-over-front-end-development-the-question-is-why-40837af8ab76). Au lieu de cela, il s'agit d'une introduction pratique aux fondamentaux de React.js pour ceux qui sont déjà familiers avec JavaScript et connaissent les bases de l'[API DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model).

Tous les exemples de code ci-dessous sont étiquetés pour référence. Ils sont purement destinés à fournir des exemples de concepts. La plupart d'entre eux peuvent être écrits de manière bien meilleure.

### Fondamental #1 : React est tout au sujet des composants

React est conçu autour du concept de composants réutilisables. Vous définissez de petits composants et vous les assemblez pour former des composants plus grands.

Tous les composants, petits ou grands, sont réutilisables, même à travers différents projets.

Un composant React — dans sa forme la plus simple — est une fonction JavaScript ordinaire :

```js
// Exemple 1
// https://jscomplete.com/repl?j=Sy3QAdKHW
function Button (props) {
  // Retourne un élément DOM ici. Par exemple :
  return <button type="submit">{props.label}</button>;
}
// Pour rendre le composant Button dans le navigateur
ReactDOM.render(<Button label="Save" />, mountNode)
```

Les accolades utilisées pour le label du bouton sont expliquées ci-dessous. Ne vous inquiétez pas pour elles maintenant. `ReactDOM` sera également expliqué plus tard, mais si vous souhaitez tester cet exemple et tous les exemples de code à venir, la fonction `render` ci-dessus est ce dont vous avez besoin.

Le deuxième argument de `ReactDOM.render` est l'élément DOM de destination que React va prendre en charge et contrôler. Dans le [jsComplete React Playground](https://jscomplete.com/react/), vous pouvez simplement utiliser la variable spéciale `mountNode`.

[**JavaScript REPL et Playground pour React.js**](https://jscomplete.com/react/)  
[_Testez le code JavaScript moderne et React.js dans le navigateur sans aucune configuration_jscomplete.com/react](https://jscomplete.com/react/)

Notez les points suivants concernant l'Exemple 1 :

* Le nom du composant commence par une majuscule. Cela est requis puisque nous allons traiter un mélange d'éléments HTML et d'éléments React. Les noms en minuscules sont réservés aux éléments HTML. En fait, allez-y et essayez de nommer le composant React simplement « button » et voyez comment ReactDOM ignorera la fonction et rendra un bouton HTML vide régulier.
* Chaque composant reçoit une liste d'attributs, tout comme les éléments HTML. Dans React, cette liste est appelée **props**. Avec un composant fonction, vous pouvez le nommer comme vous le souhaitez.
* Nous avons écrit de manière étrange ce qui ressemble à du HTML dans la sortie retournée de la fonction composant `Button` ci-dessus. Ce n'est ni du JavaScript ni du HTML, et ce n'est même pas React.js. Mais, c'est si populaire que c'est devenu la norme dans les applications React. Cela s'appelle [_JSX_](https://facebook.github.io/jsx/) et c'est une extension JavaScript. JSX est aussi un **compromis** ! Allez-y et essayez de retourner un autre élément HTML à l'intérieur de la fonction ci-dessus et voyez comment ils sont tous supportés (par exemple, retournez un élément de saisie de texte).

### Fondamental #2 : Qu'est-ce que JSX ?

L'Exemple 1 ci-dessus peut être écrit en React.js pur sans JSX comme suit :

```js
// Exemple 2 - Composant React sans JSX
// https://jscomplete.com/repl?j=HyiEwoYB-
function Button (props) {
  return React.createElement(
    "button",
    { type: "submit" },
    props.label
  );
}
// Pour utiliser Button, vous feriez quelque chose comme
ReactDOM.render(
  React.createElement(Button, { label: "Save" }),
  mountNode
);
```

La fonction `createElement` est la fonction principale dans l'API de haut niveau de React. C'est 1 des 8 choses au total dans ce niveau que vous devez apprendre. C'est à quel point l'API React est petite.

Tout comme le DOM lui-même a une fonction `document.createElement` pour créer un élément spécifié par un nom de balise, la fonction `createElement` de React est une fonction de niveau supérieur qui peut faire ce que `document.createElement` fait, mais elle peut aussi être utilisée pour créer un élément pour représenter un composant React. Nous avons fait cela lorsque nous avons utilisé le composant `Button` dans l'Exemple 2 ci-dessus.

Contrairement à `document.createElement`, la fonction `createElement` de React accepte un nombre dynamique d'arguments après le deuxième pour représenter les **enfants** de l'élément créé. Donc `createElement` crée en fait un **arbre**_._

Voici un exemple de cela :

```js
// Exemple 3 - API createElement de React
// https://jscomplete.com/repl?j=r1GNoiFBb
const InputForm = React.createElement(
  "form",
  { target: "_blank", action: "https://google.com/search" },
  React.createElement("div", null, "Enter input and click Search"),
  React.createElement("input", { name: "q", className: "input" }),
  React.createElement(Button, { label: "Search" })
);
// InputForm utilise le composant Button, donc nous en avons aussi besoin :
function Button (props) {
  return React.createElement(
    "button",
    { type: "submit" },
    props.label
  );
}
// Ensuite, nous pouvons utiliser InputForm directement avec .render
ReactDOM.render(InputForm, mountNode);
```

Notez quelques points concernant l'exemple ci-dessus :

* `InputForm` n'est pas un composant React ; c'est juste un **élément** React. C'est pourquoi nous l'avons utilisé directement dans l'appel `ReactDOM.render` et non avec `<InputForm` />.
* La fonction `React.createElement` a accepté plusieurs arguments après les deux premiers. Sa liste d'arguments à partir du 3ème comprend la liste des enfants pour l'élément créé.
* Nous avons pu imbriquer les appels `React.createElement` car c'est tout du JavaScript.
* Le deuxième argument de `React.createElement` peut être null ou un objet vide lorsque aucun attribut ou prop n'est nécessaire pour l'élément.
* Nous pouvons mélanger les éléments HTML avec les éléments React.
* L'API de React essaie d'être aussi proche que possible de l'API DOM, c'est pourquoi nous utilisons `className` au lieu de `class` pour l'élément d'entrée. Secrètement, nous souhaitons tous que l'API de React fasse partie de l'API DOM elle-même. Parce que, vous savez, elle est bien meilleure.

Le code ci-dessus est ce que le navigateur comprend lorsque vous incluez la bibliothèque React. Le navigateur ne traite aucune affaire JSX. Cependant, nous, les humains, aimons voir et travailler avec du HTML au lieu de ces appels `createElement` (imaginez construire un site web avec juste `document.createElement`, ce que vous pouvez faire !). C'est pourquoi le compromis JSX existe. Au lieu d'écrire le formulaire ci-dessus avec des appels `React.createElement`, nous pouvons l'écrire avec une syntaxe très similaire à HTML :

```js
// Exemple 4 - JSX (comparer avec l'Exemple 3)
// https://jscomplete.com/repl?j=SJWy3otHW
const InputForm =
  <form target="_blank" action="https://google.com/search">
    <div>Enter input and click Search</div>
    <input name="q" className="input" />
    <Button label="Search" />
  </form>;
// InputForm "utilise toujours" le composant Button, donc nous en avons aussi besoin.
// Soit JSX ou la forme normale ferait l'affaire
function Button (props) {
  // Retourne un élément DOM ici. Par exemple :
  return <button type="submit">{props.label}</button>;
}
// Ensuite, nous pouvons utiliser InputForm directement avec .render
ReactDOM.render(InputForm, mountNode);
```

Notez quelques points concernant ce qui précède :

* Ce n'est pas du HTML. Par exemple, nous faisons toujours `className` au lieu de `class`.
* Nous considérons toujours ce qui ressemble à du HTML ci-dessus comme du JavaScript. Voyez comment j'ai ajouté un point-virgule à la fin.

Ce que nous avons écrit ci-dessus (Exemple 4) est du JSX. Pourtant, ce que nous avons apporté au navigateur est la version compilée de celui-ci (Exemple 3). Pour que cela se produise, nous devons utiliser un pré-processeur pour convertir la version JSX en version `React.createElement`.

C'est JSX. C'est un compromis qui nous permet d'écrire nos composants React dans une syntaxe similaire à HTML, ce qui est un assez bon marché.

> Le mot « Flux » dans l'en-tête ci-dessus a été choisi pour rimer, mais c'est aussi le nom d'une architecture d'application très populaire [architecture d'application](https://facebook.github.io/flux/) popularisée par Facebook. La mise en œuvre la plus célèbre de celle-ci est Redux. Flux s'adapte parfaitement au modèle réactif de React.

JSX, d'ailleurs, peut être utilisé seul. Ce n'est pas une chose exclusive à React.

### Fondamental #3 : Vous pouvez utiliser des expressions JavaScript n'importe où dans JSX

À l'intérieur d'une section JSX, vous pouvez utiliser n'importe quelle expression JavaScript dans une paire d'accolades.

```js
// Pour l'utiliser :ReactDOM.render(<RandomValue />, mountNode);// Exemple 5 - Utilisation d'expressions JavaScript dans JSX
// https://jscomplete.com/repl?j=SkNN3oYSW
const RandomValue = () => 
  <div>
    { Math.floor(Math.random() * 100) }
  </div>;
// Pour l'utiliser :
ReactDOM.render(<RandomValue />, mountNode);
```

N'importe quelle expression JavaScript peut aller à l'intérieur de ces accolades. Cela est équivalent à la syntaxe d'interpolation `${}` dans les [littéraux de gabarit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) JavaScript.

C'est la seule contrainte à l'intérieur de JSX : uniquement des expressions. Donc, par exemple, vous ne pouvez pas utiliser une instruction `if` régulière, mais une expression ternaire est acceptable.

Les variables JavaScript sont également des expressions, donc lorsque le composant reçoit une liste de props (le composant `RandomValue` ne l'a pas fait, `props` sont optionnels), vous pouvez utiliser ces props à l'intérieur des accolades. Nous l'avons fait dans le composant `Button` ci-dessus (Exemple 1).

Les objets JavaScript sont également des expressions. Parfois, nous utilisons un objet JavaScript à l'intérieur des accolades, ce qui donne l'impression de doubles accolades, mais ce n'est vraiment qu'un objet à l'intérieur des accolades. Un cas d'utilisation de cela est de passer un objet de style CSS à l'attribut spécial `style` dans React :

```js
// Exemple 6 - Un objet passé à la prop style spéciale de React
// https://jscomplete.com/repl?j=S1Kw2sFHb
const ErrorDisplay = ({message}) =>
  <div style={ { color: 'red', backgroundColor: 'yellow' } }>
    {message}
  </div>;
// Utilisez-le :
ReactDOM.render(
  <ErrorDisplay 
    message="These aren't the droids you're looking for" 
  />,
  mountNode
);
```

Notez comment j'ai **destructuré** uniquement le message à partir de l'argument props. Notez également comment l'attribut `style` ci-dessus est spécial (encore une fois, ce n'est pas du HTML, c'est plus proche de l'API DOM). Nous utilisons un objet comme valeur de l'attribut `style`. Cet objet définit les styles comme si nous le faisions avec JavaScript (parce que nous le faisons).

Vous pouvez même utiliser un élément React à l'intérieur de JSX, car cela aussi est une expression. N'oubliez pas qu'un élément React est essentiellement un appel de fonction :

```js
// Exemple 7 - Utilisation d'un élément React dans {}
// https://jscomplete.com/repl?j=SkTLpjYr-
const MaybeError = ({errorMessage}) =>
  <div>
    {errorMessage && <ErrorDisplay message={errorMessage} />}
  </div>;
  
// Le composant MaybeError utilise le composant ErrorDisplay :
const ErrorDisplay = ({message}) =>
  <div style={ { color: 'red', backgroundColor: 'yellow' } }>
    {message}
  </div>;
// Maintenant, nous pouvons utiliser le composant MaybeError :
ReactDOM.render(
  <MaybeError
    errorMessage={Math.random() > 0.5 ? 'Not good' : ''}
  />,
  mountNode
);
```

Le composant `MaybeError` ci-dessus n'affichera le composant `ErrorDisplay` que s'il y a une chaîne `errorMessage` qui lui est passée et une `div` vide. React considère `{true}`, `{false}`, `{undefined}`, et `{null}` comme des enfants d'éléments valides, qui ne rendent rien.

Vous pouvez également utiliser toutes les méthodes fonctionnelles de JavaScript sur les collections (`map`, `reduce`, `filter`, `concat`, etc.) à l'intérieur de JSX. Encore une fois, parce qu'elles retournent des expressions :

```js
// Exemple 8 - Utilisation d'une carte de tableau à l'intérieur de {}
// https://jscomplete.com/repl?j=SJ29aiYH-
const Doubler = ({value=[1, 2, 3]}) =>
  <div>
    {value.map(e => e * 2)}
  </div>;
// Utilisez-le
ReactDOM.render(<Doubler />, mountNode);
```

Notez comment j'ai donné à la prop `value` une valeur par défaut ci-dessus, car c'est tout du JavaScript. Notez également que j'ai sorti une expression de tableau à l'intérieur de la `div`. React est d'accord avec cela ; il placera chaque valeur doublée dans un nœud de texte.

### Fondamental #4 : Vous pouvez écrire des composants React avec des classes JavaScript

Les composants de fonction simples sont excellents pour les besoins simples, mais parfois nous avons besoin de plus. React supporte la création de composants via la [syntaxe de classe JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) également. Voici le composant `Button` (dans l'Exemple 1) écrit avec la syntaxe de classe :

```js
// Exemple 9 - Création de composants en utilisant des classes JavaScript
// https://jscomplete.com/repl?j=ryjk0iKHb
class Button extends React.Component {
  render() {
    return <button>{this.props.label}</button>;
  }
}
// Utilisez-le (même syntaxe)
ReactDOM.render(<Button label="Save" />, mountNode);
```

La syntaxe de classe est simple. Définissez une classe qui étend `React.Component` (une autre chose de l'API de haut niveau de React que vous devez apprendre). La classe définit une seule fonction d'instance `render()`, et cette fonction de rendu retourne l'élément DOM virtuel. Chaque fois que nous utilisons le composant basé sur la classe `Button` ci-dessus (par exemple, en faisant `<Button ...` />), React instanciera un objet à partir de ce composant basé sur la classe et utilisera cet objet pour rendre un élément DOM dans l'arbre DOM.

C'est la raison pour laquelle nous avons utilisé `this.props.label` à l'intérieur du JSX dans la sortie rendue ci-dessus. Parce que chaque élément rendu via un composant de classe obtient une propriété spéciale d'**instance** appelée `props` qui contient toutes les valeurs passées à cet élément lorsqu'il a été créé.

Puisque nous avons une instance associée à une seule utilisation du composant, nous pouvons personnaliser cette instance comme nous le souhaitons. Nous pouvons, par exemple, la personnaliser après sa construction en utilisant la fonction `constructor` JavaScript régulière :

```js
// Exemple 10 - Personnalisation d'une instance de composant
// https://jscomplete.com/repl?j=rko7RsKS-
class Button extends React.Component {
  constructor(props) {
    super(props);
    this.id = Date.now();
  }
  render() {
    return <button id={this.id}>{this.props.label}</button>;
  }
}
// Utilisez-le
ReactDOM.render(<Button label="Save" />, mountNode);
```

Nous pouvons également définir des fonctions de classe et les utiliser où nous le souhaitons, y compris à l'intérieur de la sortie JSX retournée :

```js
// Exemple 11 — Utilisation des propriétés de classe
// https://jscomplete.com/repl?j=H1YDCoFSb
class Button extends React.Component {
  clickCounter = 0;
  handleClick = () => {
    console.log(`Clicked: ${++this.clickCounter}`);
  };
  
  render() {
    return (
      <button id={this.id} onClick={this.handleClick}>
        {this.props.label}
      </button>
    );
  }
}
// Utilisez-le
ReactDOM.render(<Button label="Save" />, mountNode);
```

Notez quelques points concernant l'Exemple 11 ci-dessus :

* La fonction `handleClick` est écrite en utilisant la nouvelle syntaxe proposée [syntaxe des champs de classe](https://github.com/tc39/proposal-class-fields) en JavaScript. Cela est encore au stade 2, mais pour de nombreuses raisons, c'est la meilleure option pour accéder à l'instance montée du composant (grâce aux fonctions fléchées). Mais vous devez utiliser un compilateur comme Babel configuré pour comprendre le stade 2 (ou la syntaxe des champs de classe) pour faire fonctionner le code ci-dessus. Le REPL jsComplete a cela préconfiguré.
* Nous avons également défini les variables d'instance `clickCounter` en utilisant la même syntaxe des champs de classe. Cela nous permet de sauter complètement l'appel au constructeur de classe.
* Lorsque nous avons spécifié la fonction `handleClick` comme valeur de l'attribut spécial `onClick` de React, nous ne l'avons pas appelée. Nous avons passé la **référence** à la fonction `handleClick`. Appeler la fonction à ce niveau est l'une des erreurs les plus courantes lors de la manipulation de React.

```js
// Faux :
onClick={this.handleClick()}
// Correct :
onClick={this.handleClick}
```

### Fondamental #5 : Événements dans React : Deux différences importantes

Lors de la gestion des événements à l'intérieur des éléments React, il y a deux différences très importantes par rapport à la manière dont nous le faisons avec l'API DOM :

* Tous les attributs des éléments React (y compris les événements) sont nommés en utilisant **camelCase**, plutôt qu'en **minuscules**. C'est `onClick`, pas `onclick`.
* Nous passons une référence de fonction JavaScript réelle comme gestionnaire d'événements, plutôt qu'une chaîne. C'est `onClick={**handleClick**}`, pas `onClick="**handleClick"**`.

React enveloppe l'objet d'événement DOM avec un objet qui lui est propre pour optimiser les performances de la gestion des événements. Mais à l'intérieur d'un gestionnaire d'événements, nous pouvons toujours accéder à toutes les méthodes disponibles sur l'objet d'événement DOM. React transmet cet objet d'événement enveloppé à chaque appel de gestionnaire. Par exemple, pour empêcher un formulaire de l'action de soumission par défaut, vous pouvez faire :

```js
// Exemple 12 - Travailler avec des événements enveloppés
// https://jscomplete.com/repl?j=HkIhRoKBb
class Form extends React.Component {
  handleSubmit = (event) => {
    event.preventDefault();
    console.log('Form submitted');
  };
  
  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <button type="submit">Submit</button>
      </form>
    );
  }
}
// Utilisez-le
ReactDOM.render(<Form />, mountNode);
```

### Fondamental #6 : Chaque composant React a une histoire

Ce qui suit s'applique uniquement aux composants de classe (ceux qui étendent `React.Component`). Les composants de fonction ont une histoire légèrement différente.

1. Tout d'abord, nous définissons un modèle pour que React crée des éléments à partir du composant.
2. Ensuite, nous instruisons React de l'utiliser quelque part. Par exemple, à l'intérieur d'un appel `render` d'un autre composant, ou avec `ReactDOM.render`.
3. Ensuite, React instancie un élément et lui donne un ensemble de **props** auxquels nous pouvons accéder avec `this.props`. Ces props sont exactement ce que nous avons passé à l'étape 2 ci-dessus.
4. Puisque c'est tout du JavaScript, la méthode `constructor` sera appelée (si définie). C'est la première de ce que nous appelons : **méthodes de cycle de vie du composant**_._
5. React calcule ensuite la sortie de la méthode de rendu (le nœud DOM virtuel).
6. Puisque c'est la première fois que React rend l'élément, React communiquera avec le navigateur (en notre nom, en utilisant l'API DOM) pour afficher l'élément là-bas. Ce processus est communément appelé **montage**.
7. React invoque ensuite une autre méthode de cycle de vie, appelée `componentDidMount`. Nous pouvons utiliser cette méthode pour, par exemple, faire quelque chose sur le DOM que nous savons maintenant exister dans le navigateur. Avant cette méthode de cycle de vie, le DOM avec lequel nous travaillons était entièrement virtuel.
8. Certaines histoires de composants se terminent ici. D'autres composants sont démontés du DOM du navigateur pour diverses raisons. Juste avant que cela ne se produise, React invoque une autre méthode de cycle de vie, `componentWillUnmount`.
9. L'**état** de tout élément monté peut changer. Le parent de cet élément peut se re-rendre. Dans les deux cas, l'élément monté peut recevoir un ensemble différent de props. La magie de React se produit ici et nous commençons **à avoir besoin** de React à ce stade ! Avant ce point, nous n'avions pas besoin de React du tout, honnêtement.

L'histoire de ce composant continue, mais avant cela, nous devons comprendre cette chose **état** dont je parle.

### Fondamental #7 : Les composants React peuvent avoir un état privé

Ce qui suit s'applique également uniquement aux composants de classe. Ai-je mentionné que certaines personnes appellent les composants uniquement de présentation **stupides** ?

La propriété `state` est une propriété spéciale dans tout composant de classe React. React surveille l'état de chaque composant pour détecter les changements. Mais pour que React le fasse efficacement, nous devons modifier le champ d'état via une autre chose de l'API React que nous devons apprendre, `this.setState` :

```js
// Exemple 13 - l'API setState
// https://jscomplete.com/repl?j=H1fek2KH-
class CounterButton extends React.Component {
  state = {
    clickCounter: 0,
    currentTimestamp: new Date(),
  };
  
  handleClick = () => {
    this.setState((prevState) => {
     return { clickCounter: prevState.clickCounter + 1 };
    });
  };
  
  componentDidMount() {
   setInterval(() => {
     this.setState({ currentTimestamp: new Date() })
    }, 1000);
  }
  
  render() {
    return (
      <div>
        <button onClick={this.handleClick}>Click</button>
        <p>Clicked: {this.state.clickCounter}</p>
        <p>Time: {this.state.currentTimestamp.toLocaleString()}</p>
      </div>
    );
  }
}
// Utilisez-le
ReactDOM.render(<CounterButton />, mountNode);
```

C'est l'exemple le plus important à comprendre. Il complétera essentiellement vos connaissances fondamentales de la méthode React. Après cet exemple, il y a quelques autres petites choses que vous devez apprendre, mais c'est surtout vous et vos compétences en JavaScript à partir de ce point.

Parcourons l'Exemple 13, en commençant par les champs de classe. Il en a deux. Le champ spécial `state` est initialisé avec un objet qui contient un `clickCounter` qui commence à `0`, et un `currentTimestamp` qui commence à `new Date()`.

Le deuxième champ de classe est une fonction `handleClick`, que nous avons passée à l'événement `onClick` pour l'élément bouton à l'intérieur de la méthode de rendu. La méthode `handleClick` modifie l'état de cette instance de composant en utilisant `setState`. Prenez note de cela.

L'autre endroit où nous modifions l'état est à l'intérieur d'un minuteur d'intervalle que nous avons démarré à l'intérieur de la méthode de cycle de vie `componentDidMount`. Il s'exécute toutes les secondes et effectue un autre appel à `this.setState`.

Dans la méthode de rendu, nous avons utilisé les deux propriétés que nous avons sur l'état avec une syntaxe de lecture normale. Il n'y a pas d'API spéciale pour cela.

Maintenant, notez que nous avons mis à jour l'état en utilisant deux méthodes différentes :

1. En passant une fonction qui retourne un objet. Nous l'avons fait à l'intérieur de la fonction `handleClick`.
2. En passant un objet régulier. Nous l'avons fait à l'intérieur du rappel d'intervalle.

Les deux méthodes sont acceptables, mais la première est préférée lorsque vous lisez et écrivez dans l'état en même temps (ce que nous faisons). À l'intérieur du rappel d'intervalle, nous écrivons uniquement dans l'état et ne le lisons pas. En cas de doute, utilisez toujours la première syntaxe de fonction comme argument. Elle est plus sûre avec les conditions de course car `setState` doit toujours être traité comme une méthode asynchrone.

Comment mettons-nous à jour l'état ? Nous retournons un objet avec la nouvelle valeur de ce que nous voulons mettre à jour. Remarquez comment dans les deux appels à `setState`, nous ne passons qu'une seule propriété du champ d'état et non les deux. Cela est parfaitement acceptable car `setState` **fusionne** en fait ce que vous lui passez (la valeur retournée de l'argument de la fonction) avec l'état existant. Donc, ne pas spécifier une propriété lors de l'appel de `setState` signifie que nous ne souhaitons pas changer cette propriété (mais pas la supprimer).

%[https://twitter.com/samerbuna/status/870383561983090689?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fsamerbuna%2Fstatus%2F870383561983090689%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F2489584954%25252Fsyaw8utdaudzc4b00zci_400x400.jpeg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

### Fondamental #8 : React réagira

React tire son nom du fait qu'il **réagit** aux changements d'état (bien que ce ne soit pas réactif, mais selon un calendrier). Il y avait une blague selon laquelle React aurait dû s'appeler **Schedule** !

Cependant, ce que nous voyons à l'œil nu lorsque l'état de n'importe quel composant est mis à jour est que React réagit à cette mise à jour et reflète automatiquement la mise à jour dans le DOM du navigateur (si nécessaire).

Considérez l'entrée de la fonction de rendu comme étant à la fois :

* Les props qui sont passées par le parent
* L'état privé interne qui peut être mis à jour à tout moment

Lorsque l'entrée de la fonction de rendu change, sa sortie peut changer.

React conserve un enregistrement de l'historique des rendus et lorsqu'il voit qu'un rendu est différent du précédent, il calculera la différence entre eux et la traduira efficacement en opérations DOM réelles qui sont exécutées dans le DOM.

### Fondamental #9 : React est votre agent

Vous pouvez considérer React comme l'agent que nous avons embauché pour communiquer avec le navigateur. Prenez l'affichage de l'horodatage actuel ci-dessus comme exemple. Au lieu d'aller manuellement dans le navigateur et d'invoquer des opérations de l'API DOM pour trouver et mettre à jour l'élément `p#timestamp` chaque seconde, nous avons simplement changé une propriété de l'état du composant et React a fait son travail de communication avec le navigateur en notre nom. Je crois que c'est la vraie raison pour laquelle React est populaire. Nous détestons parler à M. Navigateur (et des nombreux dialectes de la langue DOM qu'il parle) et React s'est porté volontaire pour faire toute la conversation pour nous, gratuitement.

### Fondamental #10 : Chaque composant React a une histoire (partie 2)

Maintenant que nous savons ce qu'est l'état d'un composant et comment, lorsque cet état change, une certaine magie se produit, apprenons les derniers concepts de ce processus.

1. Un composant peut avoir besoin de se re-rendre lorsque son état est mis à jour ou lorsque son parent décide de changer les props qu'il a passées au composant.
2. Si ce dernier se produit, React invoque une autre méthode de cycle de vie, `componentWillReceiveProps`.
3. Si l'objet d'état ou les props passées sont modifiés, React a une décision importante à prendre. Le composant doit-il être mis à jour dans le DOM ? C'est pourquoi il invoque une autre méthode de cycle de vie importante ici, `shouldComponentUpdate`. Cette méthode est une question réelle, donc si vous devez personnaliser ou optimiser le processus de rendu par vous-même, vous devez répondre à cette question en retournant **soit** vrai soit faux.
4. Si aucune méthode `shouldComponentUpdate` personnalisée n'est spécifiée, React utilise par défaut une chose très intelligente qui est en fait suffisamment bonne dans la plupart des situations.
5. Tout d'abord, React invoque une autre méthode de cycle de vie à ce stade, `componentWillUpdate`. React calculera ensuite la nouvelle sortie rendue et la comparera avec la dernière sortie rendue.
6. Si la sortie rendue est exactement la même, React ne fait rien (pas besoin de parler à M. Navigateur).
7. S'il y a une différence, React prend cette différence vers le navigateur, comme nous l'avons vu auparavant.
8. Dans tous les cas, puisque un processus de mise à jour s'est produit de toute façon (même si la sortie était exactement la même), React invoque la méthode de cycle de vie finale, `componentDidUpdate`.

Les méthodes de cycle de vie sont en fait des issues de secours. Si vous ne faites rien de spécial, vous pouvez créer des applications complètes sans elles. Elles sont très pratiques pour analyser ce qui se passe dans l'application et pour optimiser davantage les performances des mises à jour de React.

C'est tout. Croyez-le ou non, avec ce que vous avez appris ci-dessus (ou des parties de celui-ci, vraiment), vous pouvez commencer à créer des applications React intéressantes. Si vous en voulez plus, consultez mon livre [Learn React.js by Building Games](http://amzn.to/2peYJZj) !

Merci aux nombreux lecteurs qui ont révisé et amélioré cet article, Łukasz Szewczak, Tim Broyles, Kyle Holden, Robert Axelse, Bruce Lane, Irvin Waldman, et Amie Wilt.

Apprendre React ou Node ? Consultez mes livres :

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)