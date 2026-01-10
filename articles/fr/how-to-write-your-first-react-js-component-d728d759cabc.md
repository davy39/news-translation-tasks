---
title: Comment écrire votre premier composant React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-24T02:25:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-your-first-react-js-component-d728d759cabc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N2KU7pOcwZwKeOi3B-YBLQ.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment écrire votre premier composant React.js
seo_desc: 'By Samer Buna

  React’s function and class components, props, state, and event handlers



  Update: This article is now part of my book “React.js Beyond The Basics”.

  Read the updated version of this content and more about React at jscomplete.com/react-be...'
---

Par Samer Buna

#### Les composants fonctionnels et de classe de React, les props, l'état et les gestionnaires d'événements

![Image](https://cdn-media-1.freecodecamp.org/images/1*QlwpBT5qXRN1F55aiPoxdw.png)

> **Mise à jour :** Cet article fait maintenant partie de mon livre « React.js Beyond The Basics ».

> Lisez la version mise à jour de ce contenu et plus sur React à [**_jscomplete.com/react-beyond-basics_**](https://jscomplete.com/g/first-component).

Le concept le plus important à comprendre dans React.js est le composant. Un composant React peut être de deux types. Il peut être soit un composant **fonction**, soit un composant **classe**. Parfois, vous entendrez différents termes pour décrire ces deux types, comme **sans état** et **avec état**. Les composants fonctionnels sont également souvent associés au concept **présentationnel**. Je les désignerai dans cet article comme composants fonctionnels et composants de classe.

**Un composant fonctionnel** est la forme la plus simple d'un composant React. C'est une simple fonction avec un contrat simple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*XL5uu7lggaRZdKRpWhU3Gw.png)
_Capture d'écran tirée de mon cours Pluralsight — [React.js: Getting Started](https://www.pluralsight.com/courses/react-js-getting-started" rel="noopener" target="_blank" title=")_

Le composant fonctionnel reçoit un objet de propriétés qui est généralement nommé **props**. Il retourne ce qui ressemble à du HTML, mais qui est en réalité une syntaxe JavaScript spéciale appelée [JSX](https://facebook.github.io/react/docs/introducing-jsx.html).

Un **composant de classe** est une manière plus avancée de définir un composant React. Il agit également comme une fonction qui reçoit des props, mais cette fonction considère également un état interne privé comme entrée supplémentaire qui contrôle le JSX retourné.

![Image](https://cdn-media-1.freecodecamp.org/images/1*N2KU7pOcwZwKeOi3B-YBLQ.png)
_Capture d'écran tirée de mon cours Pluralsight — [React.js: Getting Started](https://www.pluralsight.com/courses/react-js-getting-started" rel="noopener" target="_blank" title=")_

Cet état interne privé est ce qui donne à React sa nature **réactive**. Lorsque l'état d'un composant de classe change, React réaffichera ce composant dans le navigateur.

Les objets State et Props ont une différence importante. À l'intérieur d'un composant de classe, l'objet State peut être modifié tandis que l'objet Props représente des valeurs fixes. Les composants de classe ne peuvent changer que leur état interne, pas leurs propriétés. C'est une idée centrale à comprendre dans React et cet article en donnera un exemple.

Regardons un exemple concret de composant. Un exemple très simple, sans aucune entrée et avec un simple `h1` dans une sortie `div`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iEMbKsYd4nCFiZ_yoRJvoA.png)
_Capture d'écran tirée de mon cours Pluralsight — [React.js: Getting Started](https://www.pluralsight.com/courses/react-js-getting-started" rel="noopener" target="_blank" title=")_

Sur le côté gauche, le composant est écrit dans la syntaxe spéciale JSX.

JSX nous permet de décrire nos interfaces utilisateur (UI) dans une syntaxe très proche du HTML auquel nous sommes habitués. Cependant, il est facultatif. React peut être utilisé sans JSX, comme vous pouvez le voir sur le côté droit. En fait, React compile simplement le JSX que vous voyez à gauche en JavaScript pur que vous voyez à droite. Ensuite, il travaille avec le JavaScript compilé dans le navigateur.

L'appel `React.createElement` sur le côté droit est une représentation JavaScript du Document Object Model ([DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)). React traduit efficacement cela en opérations DOM qu'il effectue dans le navigateur.

### Écrivons un composant React.

J'utiliserai le [React Playground](https://jscomplete.com/react) de jsComplete pour les exemples de cet article. C'est un outil où vous pouvez tester votre code JavaScript et React directement dans le navigateur. Il n'est pas nécessaire d'installer ou de configurer quoi que ce soit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RmSo6MSOYmz4DKn9q8iX1w.png)

L'outil a une interface simple à deux panneaux. Le panneau de gauche est l'éditeur où vous écrivez votre code JavaScript et React. Les dernières versions de React et ReactDOM sont déjà préchargées. L'éditeur comprend également l'extension JSX et toutes les fonctionnalités modernes de JavaScript. Cela nous permettra de nous concentrer sur l'API React elle-même plutôt que sur la configuration et la compilation d'une application React.

Le panneau de droite est le panneau de prévisualisation. Vous avez un élément `mountNode` prédéfini dans l'éditeur. Lorsque vous exécutez votre code JavaScript, tout ce que vous mettez dans l'élément `mountNode` apparaît dans le panneau de prévisualisation. Le panneau de prévisualisation affichera également toute erreur que vous rencontrez lors de l'exécution de votre code. Le terrain de jeu est également un simple _REPL_ JavaScript (Run, Eval, Print, Loop) où vous pouvez tester des fonctions et des expressions JavaScript rapides. Pour exécuter le code à tout moment, appuyez sur `CTRL+Enter`.

Essayez ce qui suit dans le REPL, par exemple :

```
mountNode.innerHTML = 'Bonjour!!';
```

Ou le mode REPL simple

```
3 == '3'
```

Pour créer un composant React, définissez une nouvelle fonction. Faisons en sorte que cette fonction retourne un élément de bouton HTML :

```
function Button() {  return (    <button>Go</button>  );}
```

Ce que nous avons retourné ici ressemble à du HTML, mais rappelez-vous que ce n'est pas le cas. Il sera compilé en JavaScript. Le JavaScript réel que le navigateur voit lorsque nous utilisons cet élément de bouton en JSX est un appel à la fonction `React.createElement` :

```
function Button() {  return (    React.createElement("button", null, "Go")  );}
```

Bien que vous puissiez utiliser React de cette manière sans JSX, cela serait beaucoup plus difficile à coder et à maintenir. Alors, restons avec JSX.

La fonction ci-dessus est un composant React complet et très simple. Utilisons-le !

Nous utilisons un composant en le montant dans le navigateur. La fonction conçue pour cela est `ReactDOM.render`, qui prend deux arguments :

* Le premier est le composant à rendre, dans notre cas, c'est `Button`.
* Le deuxième argument est l'élément dans lequel ce composant doit être rendu. Dans l'environnement du REPL, nous pouvons utiliser la variable spéciale `mountNode`.

```
ReactDOM.render(<Button />, mountNode);
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*L866_1BuscPjUtqExbP0tA.png)
_[https://jscomplete.com/repl?j=Skl5GngO-](https://jscomplete.com/repl?j=Skl5GngO-" rel="noopener" target="_blank" title=")_

Tous les exemples de code dans cet article ont un lien dans la légende de la capture d'écran où vous pouvez modifier l'exemple dans le REPL de jsComplete.

Un composant fonctionnel React reçoit en tant que premier argument l'objet `props`. Cet argument nous permet de rendre le composant réutilisable. Par exemple, au lieu de coder en dur l'étiquette « Go » du bouton ci-dessus, nous pouvons passer au composant `Button` un attribut `label`, comme nous le faisons avec les éléments HTML réguliers :

```
ReactDOM.render(<Button label="Enregistrer" />, mountNode);
```

Ensuite, nous pouvons accéder à cet attribut à l'intérieur du composant avec des accolades pour `props.label`.

```
function Button(props) {  return (    <button>{props.label}</button>  );}
```

L'argument `props` est un objet qui contient toutes les valeurs qui ont été passées au composant lorsqu'il a été rendu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HvOTyzJNb2I3bm7AKpVqVw.png)
_[https://jscomplete.com/repl?j=ByQm4nl_Z](https://jscomplete.com/repl?j=ByQm4nl_Z" rel="noopener" target="_blank" title=")_

### Rendre le composant interactif

Nous avons un élément bouton et il est rendu via un composant React.

Ajoutons maintenant un peu d'interactivité à cet exemple jusqu'à présent ennuyeux. Faisons en sorte que cet élément bouton incrémente une valeur de compteur à chaque clic et affiche cette valeur comme étiquette du bouton lui-même. Ainsi, l'étiquette de ce bouton commencera par le nombre 1 et, lorsque l'utilisateur cliquera sur le bouton, son étiquette changera en 2, 3, 4 et ainsi de suite.

Puisque cela doit être reflété dans la sortie rendue du composant, cela appartient à l'état du composant. Nous avons besoin que le composant se réaffiche chaque fois que le compteur change. Nous ne pouvons pas utiliser une propriété ici car les props d'un composant ne peuvent pas être modifiées. En utilisant l'objet d'état spécial de React, nous utiliserons la nature **réactive** de React et nous n'aurons pas à nous soucier de **comment** apporter les modifications au navigateur. React le fera pour nous.

Cependant, notre composant Button est actuellement un composant fonctionnel. Les composants fonctionnels ne peuvent pas avoir d'état, nous devons donc d'abord mettre à niveau ce composant en un composant de classe.

C'est très simple. Nous définissons d'abord une classe qui étend `React.Component`

```
class Button extends React.Component { }
```

Dans cette classe, nous définissons une fonction `render`, qui retourne le JSX du composant ; le bouton HTML dans notre cas.

```
render() {  return (    <button>1</button>  );}
```

C'est un peu plus de code, mais nous pouvons maintenant utiliser un état privé sur le composant Button !

![Image](https://cdn-media-1.freecodecamp.org/images/1*XQwiawVuQKD7VOqVcHXl8g.png)
_[https://jscomplete.com/repl?j=BJCWI2gd-](https://jscomplete.com/repl?j=BJCWI2gd-" rel="noopener" target="_blank" title=")_

Pour utiliser un objet d'état, nous devons d'abord l'initialiser. L'objet d'état est une simple propriété d'instance, nous pouvons donc l'initialiser à l'intérieur de la fonction constructeur de la classe `Button`. Nous définissons simplement la fonction constructeur normale (qui reçoit un objet `props` dans React) et appelons la méthode `super` pour honorer l'héritage du composant.

```
constructor(props) {  super(props);  this.state = { counter: 1 };}
```

Après cela, nous initialisons `this.state` à ce que nous voulons. Les clés de cet objet d'état sont les divers éléments de l'état. Pour notre cas, nous avons besoin d'un état `counter`, qui commence à 1.

À l'intérieur de la fonction render, puisque nous pouvons écrire n'importe quelle expression JavaScript dans des accolades, nous pouvons lire la valeur du nouvel élément d'état `counter` que nous avons initialisé sur l'état en utilisant `this.state.counter`.

```
render() {  return (    <button>{this.state.counter}</button>  );}
```

Le mot-clé « `this` » fait référence à l'instance de composant que nous transmettons à `ReactDOM`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IgGVPxvwOdz_7AdlJj-new.png)
_[https://jscomplete.com/repl?j=SJfwu2xuZ](https://jscomplete.com/repl?j=SJfwu2xuZ" rel="noopener" target="_blank" title=")_

Vous pouvez essayer de changer cet état de compteur pour voir comment le bouton affichera les valeurs que vous mettez sur l'état.

Il existe une autre syntaxe plus courte pour définir l'état initial, qui consiste simplement à utiliser une propriété de classe sans appel de constructeur :

```
class Button extends React.Component {  state = { counter: 1 };    render() {    return (      <button>{this.state.counter}</button>    );  }}
```

Cela ne fait pas encore partie du langage JavaScript officiel, mais cela le sera bientôt. La syntaxe fonctionne dans le terrain de jeu REPL de jsComplete car cet outil utilise Babel pour le transpiler en JavaScript pris en charge que le navigateur comprendra.

Lorsque vous configurez votre propre application React, vous devrez utiliser quelque chose comme Babel de toute façon pour compiler JSX en JavaScript. C'est une victoire facile que d'inclure et d'utiliser également les fonctionnalités JavaScript qui sont bien en voie de devenir une partie officielle du langage.

Dans l'exemple `Button` jusqu'à présent, nous avons un objet d'état et un élément de bouton HTML qui affiche une valeur de compteur que nous avons initialisée sur l'état. Maintenant, nous devons changer cette valeur lorsque nous cliquons sur le bouton. Nous devons définir un gestionnaire de clic sur ce bouton.

React vient avec des événements normalisés qui sont faciles à utiliser. Pour ce cas, nous avons besoin de l'événement `onClick`, que nous définissons sur l'élément de bouton HTML lui-même :

```
function F() {}
```

```
<button onClick={F} />
```

Contrairement aux gestionnaires d'événements DOM, qui utilisent une chaîne, les gestionnaires d'événements React utilisent une fonction JavaScript réelle. Cette fonction peut être une fonction globale (comme `F` ci-dessus), ou une fonction en ligne :

```
<button onClick={() => {}} />
```

Cependant, la pratique standard consiste à définir une fonction sur le composant de classe lui-même. Appelons-la `handleClick` et nous pouvons la définir sur le composant comme une propriété d'instance :

```
class Button extends React.Component {  state = { counter: 1 };    handleClick = () => {    console.log('Le bouton est cliqué!!');  };    render() {    return (      <button onClick={this.handleClick}>        {this.state.counter}      </button>    );  }}
```

Nous utilisons la syntaxe moderne des champs de classe, qui nous permet d'utiliser des fonctions fléchées qui sont liées à l'instance du composant. `handleClick` agira maintenant comme une fonction prototype sur cette classe. À l'intérieur de `handleClick`, le mot-clé « `this` » fait référence à l'instance du composant que nous montons dans le DOM.

Le travail de `handleClick` est simple : lire la valeur actuelle du compteur à partir de l'objet d'état en utilisant `this.state.counter`. Ensuite, incrémentez cette valeur et mettez à jour l'état du composant avec la nouvelle valeur incrémentée.

Nous pouvons utiliser la méthode intégrée `setState` de React, qui est disponible sur chaque instance de composant de classe, pour mettre à jour un état de composant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A61aPxQK-fx7Mw2nLbpPbg.png)
_[https://jscomplete.com/repl?j=Sy-u46l_Z](https://jscomplete.com/repl?j=Sy-u46l_Z" rel="noopener" target="_blank" title=")_

Le bouton incrémentera maintenant son étiquette à chaque clic.

C'était simple et puissant ! Nous avons défini un gestionnaire d'événements pour la méthode `onClick`. Chaque fois que l'utilisateur clique sur le bouton, la fonction `handleClick` sera exécutée. La fonction lit l'état actuel de la valeur du compteur, l'incrémente, puis définit l'état à la nouvelle valeur incrémentée. React s'occupe de tout le rendu nécessaire après ces changements, vous n'avez donc pas à vous en soucier.

Notez que nous n'avons pas mis à jour directement l'objet d'état. Nous devons utiliser la méthode `setState` de React lorsque nous voulons mettre à jour un élément sur l'état. Vous ne pouvez pas, par exemple, faire ceci :

```
// FAUX : this.state.counter = this.state.counter + 1;
```

La méthode `setState` de React est asynchrone et planifie une mise à jour. Plusieurs appels à `setState` peuvent potentiellement être regroupés pour des raisons de performance. Puisque nous lisons et écrivons dans l'objet d'état à l'intérieur de la fonction `handleClick`, nous pourrions rencontrer une condition de course. La règle générale est que chaque fois que vous devez mettre à jour l'état en utilisant une valeur de l'état actuel, utilisez l'autre contrat de la méthode `setState`. Cela reçoit une référence de fonction au lieu d'un objet comme premier argument :

```
this.setState((prevState) => {});
```

Cette fonction reçoit un objet `prevState` que nous pouvons utiliser en toute confiance sans nous soucier des conditions de course. La fonction retourne l'objet que nous voulons que React utilise pour définir l'état. Notre exemple de valeur `counter` ci-dessus devient :

```
this.setState((prevState) => ({  counter: prevState.counter + 1 }));
```

Vous n'avez besoin d'utiliser cette deuxième syntaxe de `setState` que si votre mise à jour dépend de l'état actuel. Cependant, il peut être judicieux de prendre l'habitude d'utiliser toujours la syntaxe du deuxième argument de fonction.

Voici le code final :

```
class Button extends React.Component {  state = { counter: 1 };    handleClick = () => {    this.setState((prevState) => ({      counter: prevState.counter + 1     }));  };    render() {    return (      <button onClick={this.handleClick}>        {this.state.counter}      </button>    );  }}
```

```
ReactDOM.render(<Button />, mountNode);
```

[Testez-le](https://jscomplete.com/repl?j=rJgDsTgdb) et si vous avez des questions, faites-le moi savoir dans les commentaires ci-dessous.

> Cet article est une rédaction d'une partie de mon cours Pluralsight — [React.js: Getting Started](https://www.pluralsight.com/courses/react-js-getting-started). Je couvre un contenu similaire en format vidéo là-bas.

Apprendre React ou Node ? Consultez mes livres :

* [Apprendre React.js en construisant des jeux](http://amzn.to/2peYJZj)
* [Node.js Au-delà des bases](http://amzn.to/2FYfYru)