---
title: 'La nouvelle API de contexte de React : basculer entre l''état local et global'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-07T02:21:51.000Z'
originalURL: https://freecodecamp.org/news/reacts-new-context-api-how-to-toggle-between-local-and-global-state-c6ace81443d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XlDCO_6ml5lRCbxJZnkzow.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: 'La nouvelle API de contexte de React : basculer entre l''état local et
  global'
seo_desc: 'By Diego Haz

  Consider a component that handles a visibility state and passes it down to its children
  via render props:

  const PopoverContainer = () => (  <VisibilityContainer>    {({ toggle, hidden })
  => (      <div>        <button onClick={toggle}>Po...'
---

Par Diego Haz

Considérez un composant qui gère un état de visibilité et le transmet à ses enfants via [render props](https://reactjs.org/docs/render-props.html) :

```
const PopoverContainer = () => (  <VisibilityContainer>    {({ toggle, hidden }) => (      <div>        <button onClick={toggle}>PopoverButton</button>        <div hidden={hidden}>PopoverContent</div>      </div>    )}  </VisibilityContainer>);
```

![Image](https://cdn-media-1.freecodecamp.org/images/bR7Wyd-qYPxK46wEMMsZyBwQuj8ZZc4pHrQy)

Que penseriez-vous de pouvoir rendre cet état **global** simplement en changeant une propriété `context` sur le composant ?

```
const PopoverButton = () => (  <VisibilityContainer context="popover1">    {({ toggle }) => (      <button onClick={toggle}>PopoverButton</button>    )}  </VisibilityContainer>);
```

```
const PopoverContent = () => (  <VisibilityContainer context="popover1">    {({ hidden }) => (      <div hidden={hidden}>PopoverContent</div>    )}  </VisibilityContainer>);
```

C'est ce que nous allons réaliser dans cet article.

### Contexte et État

Tout d'abord, avant de parler de **contexte** et d'**état** dans React, laissez-moi vous donner un peu de **contexte** sur l'**état** de ce sujet (!).

Il y a quelques mois, j'ai publié [reas](https://github.com/diegohaz/reas), une boîte à outils UI expérimentale alimentée par React et [styled-components](https://www.styled-components.com).

En plus des composants eux-mêmes, je voulais fournir des helpers pour gérer leur état. L'approche que j'ai prise à l'époque était d'exporter quelques [composants d'ordre supérieur](https://reactjs.org/docs/higher-order-components.html) (HOC), tels que `withPopoverContainer`, afin de contrôler l'état de visibilité d'un composant `Popover`. Jetez un œil à cet exemple :

```
import { Popover, withPopoverContainer } from "reas";
```

```
const MyComponent = ({ toggle, visible }) => (  <div>    <button onClick={toggle}>Toggle</button>    <Popover visible={visible}>Popover</Popover>  </div>);
```

```
export default withPopoverContainer(MyComponent);
```

Mais les HOC ont quelques problèmes, comme les collisions de noms. Que se passe-t-il si un autre HOC ou un composant parent passe sa propre propriété `toggle` à `MyComponent` ? Les choses vont certainement casser.

Même avant cela, inspiré par [Michael Jackson](https://www.freecodecamp.org/news/reacts-new-context-api-how-to-toggle-between-local-and-global-state-c6ace81443d0/undefined) et son [excellent discours](https://www.youtube.com/watch?v=BcVAq3YFiuc), la communauté React a commencé à adopter les [render props](https://reactjs.org/docs/render-props.html) plutôt que les HOC.

De plus, React v16.3.0 a introduit une nouvelle [API de contexte](https://reactjs.org/docs/context.html), remplaçant l'ancienne [instable](https://reactjs.org/docs/legacy-context.html), en utilisant les render props.

J'ai appris à regarder tout ce qui est hypé, surtout les choses apportées par la communauté JavaScript, avec un œil critique. Cela garde mon esprit sain et m'empêche de devoir refactoriser mon code tous les jours avec de nouvelles bibliothèques cool.

Enfin, j'ai posté un [tweet](https://twitter.com/diegohaz/status/978335493023821824) demandant aux gens ce qu'ils préféraient : les render props ou les HOC. Tous les commentaires étaient favorables aux render props, ce qui m'a finalement fait transformer tous les HOC dans [reas](https://github.com/diegohaz/reas) en composants avec render props :

```
import { Popover } from "reas";
```

```
const MyComponent = () => (  <Popover.Container>    {({ toggle, visible }) => (      <div>        <button onClick={toggle}>Toggle</button>        <Popover visible={visible}>Popover</Popover>      </div>    )}  </Popover.Container>);
```

```
export default MyComponent;
```

`Popover.Container` était une classe de composant React régulière avec une méthode `toggle` utilisant `this.setState` pour changer `this.state.visible`. Simple comme bonjour.

C'était bien et ça fonctionnait plutôt bien. Cependant, dans l'un de mes projets, j'avais un `button` qui était censé contrôler le composant `Popover` placé dans un chemin complètement différent dans l'arbre React.

Soit j'avais besoin d'avoir une sorte de gestionnaire d'état global comme [Redux](https://redux.js.org/), soit je devais déplacer `Popover.Container` vers le haut dans l'arbre dans un parent commun et passer les props jusqu'à ce qu'ils touchent à la fois `button` et `Popover`. Mais cela semblait être une terrible idée.

De plus, configurer Redux et réécrire toute la logique que j'avais déjà avec `this.setState` en actions et réducteurs juste pour avoir cette fonctionnalité aurait été un travail horrible.

Je pense que ce besoin imminent d'état partagé est l'une des raisons pour lesquelles les gens [optimisent prématurément](http://wiki.c2.com/?PrematureOptimization) leurs applications. C'est-à-dire, configurer toutes les bibliothèques dont ils **pourraient** avoir besoin à l'avance, ce qui inclut une bibliothèque de gestion d'état global.

La nouvelle API de contexte de React arrive à point nommé pour résoudre ce problème. Je voulais continuer à utiliser l'état local régulier de React et ne passer à l'état global que lorsque nécessaire, sans avoir besoin de réécrire ma logique d'état. C'est pourquoi j'ai construit [constate](https://github.com/diegohaz/constate).

### Constate

![Image](https://cdn-media-1.freecodecamp.org/images/pvU1j2TKHu1rm1dVouIoSLZpuwYhU8elzO3e)

Voyons à quoi ressemblerait `PopoverContainer` avec [constate](https://github.com/diegohaz/constate) :

```
import React from "react";import { Container } from "constate";
```

```
const PopoverContainer = props => (  <Container    initialState={{ visible: false }}    actions={{      toggle: () => state => ({ visible: !state.visible })    }}    {...props}  />);
```

```
export default PopoverContainer;
```

Maintenant, nous pouvons envelopper notre composant avec `PopoverContainer` afin d'avoir accès aux membres `visible` et `toggle` déjà passés par `Container` à la fonction `children` en tant qu'argument.

De plus, notez que nous passons toutes les props reçues de `PopoverContainer` à `Container`. Cela signifie que nous pouvons le composer pour créer un nouveau composant d'état dérivé, tel que `AdvancedPopoverContainer`, avec un nouvel `initialState` et des `actions`.

#### Sous le capot

Si vous êtes comme moi, et que vous aimez savoir comment les choses ont été implémentées sous le capot, vous vous demandez probablement comment `Container` a été implémenté. Alors, recréons un composant `Container` simple :

```
import React from "react";
```

```
class Container extends React.Component {  state = this.props.initialState;
```

```
  render() {    return this.props.children({      ...this.state,      ...mapStateToActions(...)    });  }}
```

```
export default Container;
```

`[mapStateToActions](https://github.com/diegohaz/constate/blob/93b7b5b469be4521784b51380f49e6589c3e56b9/src/utils.js#L1-L8)` est une fonction utilitaire qui passe l'état à chaque membre de `actions`. C'est ce qui permet de définir notre fonction `toggle` comme ceci :

```
const actions = {  toggle: () => state => ({ visible: !state.visible})};
```

Notre objectif, cependant, est de pouvoir utiliser le même `PopoverContainer` comme un état global. Avec [constate](https://github.com/diegohaz/constate), nous devons simplement passer une prop `context` à `Container` :

```
<PopoverContainer context="popover1">  {({ toggle }) => (    <button onClick={toggle}>PopoverToggle</button>  )}</PopoverContainer>
```

Maintenant, chaque `Container` avec `context="popover1"` partagera le même état.

Bien sûr, vous êtes curieux de savoir comment `Container` gère cette prop `context`. Alors voici :

```
import React from "react";import Consumer from "./Consumer";
```

```
class Container extends React.Component {  state = this.props.initialState;
```

```
  render() {    if (this.props.context) {      return <Consumer {...this.props} />;    }
```

```
    return this.props.children({      ...this.state,      ...mapStateToActions(...)    });  }}
```

```
export default Container;
```

D'accord, je suis désolé. Ces quatre lignes ajoutées ne vous disent pas grand-chose. Pour créer `Consumer`, nous devons comprendre comment gérer la nouvelle API de contexte React.

#### Contexte React

Nous pouvons diviser la nouvelle API de contexte React en trois parties : `Context`, `Provider` et `Consumer`.

Créons le contexte :

```
import React from "react";
```

```
const Context = React.createContext();
```

```
export default Context;
```

Ensuite, nous créons notre `Provider`, qui utilise `Context.Provider` et passe `state` et `setState` :

```
import React from "react";import Context from "./Context";
```

```
class Provider extends React.Component {  handleSetState = fn => {    this.setState(state => ({      state: fn(state.state)    }));  };
```

```
  state = {    state: this.props.initialState,    setState: this.handleSetState  };
```

```
  render() {    return (      <Context.Provider value={this.state}>        {this.props.children}      </Context.Provider>    );  }}
```

```
export default Provider;
```

Cela peut être un peu délicat. Nous ne pouvons pas simplement passer `{ state, setState }` comme un objet littéral à la `value` de `Context.Provider` car cela recréerait cet objet à chaque rendu. En savoir plus [ici](https://github.com/diegohaz/constate/issues/2).

Enfin, notre `Consumer` doit utiliser `Context.Consumer` pour accéder à `state` et `setState` passés par `Provider` :

```
import React from "react";import Context from "./Context";
```

```
const Consumer = ({ context, children, actions }) => (  <Context.Consumer>    {({ state, setState }) => children({      ...state[context],      ...mapContextToActions(...)    })}  </Context.Consumer>);
```

```
export default Consumer;
```

`[mapContextToActions](https://github.com/diegohaz/constate/blob/93b7b5b469be4521784b51380f49e6589c3e56b9/src/Consumer.js#L27-L35)` est similaire à `mapStateToActions`. La différence est que le premier mappe `state[context]` au lieu de simplement `state`.

La dernière étape consiste à envelopper notre application avec `Provider` :

```
import React from "react";import ReactDOM from "react-dom";import Provider from "./Provider";
```

```
const App = () => (  <Provider>    ...  </Provider>);
```

```
ReactDOM.render(<App />, document.getElementById("root"));
```

Enfin, nous avons réécrit [constate](https://github.com/diegohaz/constate). Maintenant, vous pouvez utiliser le composant `Container` pour basculer entre l'état local et global avec facilité.

### Conclusion

Vous pourriez penser que commencer un projet avec quelque chose comme [constate](https://github.com/diegohaz/constate) pourrait aussi être une optimisation prématurée. Et vous avez probablement raison. Vous devriez rester avec `this.setState` sans abstractions tant que vous le pouvez.

Cependant, toutes les _optimisations prématurées ne sont pas la racine de tous les maux_. Vous devriez trouver un bon équilibre entre simplicité et évolutivité. C'est-à-dire, vous devriez poursuivre des implémentations simples, surtout si vous construisez de petites applications. Mais, si vous prévoyez de grandir, vous devriez chercher des implémentations simples qui sont aussi faciles à évoluer.

### Merci d'avoir lu ceci !

Si vous aimez cela et que vous le trouvez utile, voici quelques choses que vous pouvez faire pour montrer votre soutien :

* Cliquez sur le bouton d'applaudissements 👏 quelques fois (jusqu'à 50)
* Donnez une étoile ⭐ sur GitHub : [https://github.com/diegohaz/constate](https://github.com/diegohaz/constate)
* Suivez-moi sur GitHub : [https://github.com/diegohaz](https://github.com/diegohaz)
* Suivez-moi sur Twitter : [https://twitter.com/diegohaz](https://twitter.com/diegohaz)