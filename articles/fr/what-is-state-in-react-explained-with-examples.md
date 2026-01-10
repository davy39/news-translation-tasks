---
title: Comment fonctionne l'état dans React – Expliqué avec des exemples de code
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-04-05T19:42:56.000Z'
originalURL: https://freecodecamp.org/news/what-is-state-in-react-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/state.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment fonctionne l'état dans React – Expliqué avec des exemples de code
seo_desc: 'State is the most complex thing in React, and it''s something both beginners
  and experienced developers struggle to understand. So in this article, we''ll explore
  all the basics of state in React.

  Before understanding state, let''s first understand some...'
---

L'état est la chose la plus complexe dans React, et c'est quelque chose avec lequel les débutants et les développeurs expérimentés ont du mal à comprendre. Donc dans cet article, nous allons explorer toutes les bases de l'état dans React.

Avant de comprendre l'état, comprenons d'abord quelques fondamentaux pour qu'il soit facile de comprendre l'état plus tard.

## Comment afficher des données dans l'UI dans React

Pour afficher quoi que ce soit à l'écran, nous utilisons la méthode `ReactDOM.render` dans React.

Elle a la syntaxe suivante :

```js
ReactDOM.render(element, container[, callback])

```

* `element` peut être n'importe quel élément HTML, JSX ou un composant qui retourne du JSX
* `container` est l'élément de l'UI à l'intérieur duquel nous voulons afficher les données
* `callback` est la fonction optionnelle que nous pouvons passer qui est appelée une fois que quelque chose est affiché ou réaffiché à l'écran

Regardez le code ci-dessous :

```jsx
import React from "react";
import ReactDOM from "react-dom";

const rootElement = document.getElementById("root");

ReactDOM.render(<h1>Bienvenue dans React !</h1>, rootElement);

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/focused-shockley-oh4tn?file=/src/index.js).

Ici, nous affichons simplement un seul élément h1 à l'écran.

Pour afficher plusieurs éléments, nous pouvons le faire comme montré ci-dessous :

```jsx
import React from "react";
import ReactDOM from "react-dom";

const rootElement = document.getElementById("root");

ReactDOM.render(
  <div>
    <h1>Bienvenue dans React !</h1>
    <p>React est génial.</p>
  </div>,
  rootElement
);

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/white-hooks-dgru0?file=/src/index.js).

Nous pouvons également extraire le JSX et le mettre dans une variable, ce qui est la manière préférée d'afficher le contenu s'il devient plus grand, comme ceci :

```jsx
import React from "react";
import ReactDOM from "react-dom";

const rootElement = document.getElementById("root");

const content = (
  <div>
    <h1>Bienvenue dans React !</h1>
    <p>React est génial.</p>
  </div>
);

ReactDOM.render(content, rootElement);

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/trusting-night-5g825?file=/src/index.js).

Ici, nous avons également ajouté une paire supplémentaire de parenthèses rondes pour aligner correctement le JSX et en faire une seule expression JSX.

Si vous voulez comprendre le JSX en détail et ses diverses fonctionnalités importantes, consultez [mon article ici](https://www.freecodecamp.org/news/jsx-in-react-introduction/).

Maintenant, affichons un bouton et du texte à l'écran :

```jsx
import React from "react";
import ReactDOM from "react-dom";

const rootElement = document.getElementById("root");

let counter = 0;

const handleClick = () => {
  counter++;
  console.log("counter", counter);
};

const content = (
  <div>
    <button onClick={handleClick}>Incrémenter le compteur</button>
    <div>La valeur du compteur est {counter}</div>
  </div>
);

ReactDOM.render(content, rootElement);

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/quizzical-cohen-x55p8?file=/src/index.js).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/counter_initial.gif)

Comme vous pouvez le voir, lorsque nous cliquons sur le bouton, la valeur `counter` est incrémentée comme vous pouvez le voir dans la console. Mais sur l'UI, elle n'est pas mise à jour.

C'est parce que nous affichons le JSX `content` une seule fois en utilisant la méthode `ReactDOM.render` lorsque la page est chargée. Et nous ne l'appelons pas à nouveau – donc même si la valeur de `counter` est mise à jour, elle n'est pas affichée sur l'UI. Alors corrigeons cela.

```jsx
import React from "react";
import ReactDOM from "react-dom";

const rootElement = document.getElementById("root");

let counter = 0;

const handleClick = () => {
  counter++;
  console.log("counter", counter);
  renderContent();
};

const renderContent = () => {
  const content = (
    <div>
      <button onClick={handleClick}>Incrémenter le compteur</button>
      <div>La valeur du compteur est {counter}</div>
    </div>
  );

  ReactDOM.render(content, rootElement);
};

renderContent();

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/adoring-noether-8gsgu?file=/src/index.js).

Ici, nous avons déplacé le JSX `content` et l'appel de la méthode `ReactDOM.render` à l'intérieur d'une fonction `renderContent`. Ensuite, une fois qu'elle est définie, nous appelons la fonction afin qu'elle affiche le contenu sur l'UI au chargement de la page.

Notez que nous avons également ajouté l'appel de la fonction `renderContent` à l'intérieur de la fonction `handleClick`. Ainsi, chaque fois que nous cliquons sur le bouton, la fonction `renderContent` sera appelée et nous verrons le compteur mis à jour sur l'UI.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/counter_updated.gif)

Comme vous pouvez le voir, cela fonctionne comme prévu et la valeur `counter` est correctement affichée sur l'UI.

Vous pourriez penser qu'il est coûteux de réafficher tout le DOM à chaque clic sur le bouton – mais ce n'est pas le cas. C'est parce que React utilise un algorithme de DOM virtuel où il vérifie ce qui a été changé sur l'UI et ne réaffiche que les éléments qui ont été changés. Ainsi, tout le DOM n'est pas réaffiché.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/counter_preview.gif)

Voici un [lien de prévisualisation](https://8gsgu.csb.app/) pour le Code Sandbox pour l'essayer vous-même.

Comme vous pouvez le voir dans la structure HTML, seule la valeur `counter` est réaffichée car c'est la seule chose qui clignote dans la structure HTML. C'est la raison pour laquelle React est si rapide et le DOM virtuel rend React plus utile.

Mais il n'est toujours pas faisable d'appeler la fonction `renderContent` chaque fois que nous voulons mettre à jour l'UI. Donc React a ajouté le concept d'État.

## Introduction à l'État dans React

L'état nous permet de gérer les données changeantes dans une application. Il est défini comme un objet où nous définissons des paires clé-valeur spécifiant diverses données que nous voulons suivre dans l'application.

Dans React, tout le code que nous écrivons est défini à l'intérieur d'un composant.

Il existe principalement deux façons de créer un composant dans React :

* composant basé sur une classe
* composant fonctionnel

> Nous allons commencer avec les composants basés sur une classe maintenant. Plus tard dans cet article, nous verrons une façon de créer des composants avec des composants fonctionnels.

Vous devez savoir comment travailler avec les composants basés sur une classe ainsi qu'avec les composants fonctionnels, y compris les hooks.

Au lieu d'apprendre directement les composants fonctionnels avec les hooks React, vous devez d'abord comprendre les composants basés sur une classe afin qu'il soit facile de clarifier les bases.

Vous pouvez créer un composant en utilisant le mot-clé de classe ES6 et en étendant la classe `Component` fournie par React comme ceci :

```jsx
import React from "react";
import ReactDOM from "react-dom";

class Counter extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      counter: 0
    };

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.state.counter = this.state.counter + 1;

    console.log("counter", this.state.counter);
  }

  render() {
    const { counter } = this.state;

    return (
      <div>
        <button onClick={this.handleClick}>Incrémenter le compteur</button>
        <div>La valeur du compteur est {counter}</div>
      </div>
    );
  }
}

const rootElement = document.getElementById("root");
ReactDOM.render(<Counter />, rootElement);

```

> Notez que le nom du composant commence par une lettre majuscule (`Counter`).

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/nostalgic-burnell-57fhd?file=/src/index.js).

Explorons ce que nous faisons ici.

* À l'intérieur de la fonction constructeur, nous appelons d'abord `super` en lui passant `props`. Ensuite, nous avons défini l'état comme un objet avec `counter` comme propriété de l'objet.
* Nous liaisons également le contexte de `this` à la fonction `handleClick` afin que, à l'intérieur de la fonction `handleClick`, nous obtenions le contexte correct pour `this`.
* Ensuite, à l'intérieur de la fonction `handleClick`, nous mettons à jour le `counter` et le journalisons dans la console.
* Et à l'intérieur de la méthode `render`, nous retournons le JSX que nous voulons afficher sur l'UI.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/counter_mutate_state.gif)

Le `counter` est correctement mis à jour comme vous pouvez le voir dans la console – mais il n'est pas mis à jour sur l'UI.

C'est parce que nous mettons à jour directement l'état à l'intérieur de la fonction `handleClick` comme suit :

```js
this.state.counter = this.state.counter + 1
```

Donc React ne réaffiche pas le composant (et **c'est aussi une mauvaise pratique de mettre à jour directement l'état**).

> Ne mettez jamais à jour/mutatez directement l'état dans React, car c'est une mauvaise pratique et cela causera des problèmes dans votre application. De plus, votre composant ne sera pas réaffiché lors du changement d'état si vous effectuez un changement d'état direct.

## Syntaxe de setState

Pour effectuer le changement d'état, React nous donne une fonction `setState` qui nous permet de mettre à jour la valeur de l'état.

La fonction `setState` a la syntaxe suivante :

```
setState(updater, [callback])

```

* `updater` peut être une fonction ou un objet
* `callback` est une fonction optionnelle qui est exécutée une fois que l'état est mis à jour avec succès

> L'appel de `setState` réaffiche automatiquement tout le composant et tous ses composants enfants. Nous n'avons pas besoin de réafficher manuellement comme vu précédemment en utilisant la fonction `renderContent`.

## Comment utiliser une fonction pour mettre à jour l'état dans React

Modifions la [Démonstration Code Sandbox ci-dessus](https://codesandbox.io/s/nostalgic-burnell-57fhd?file=/src/index.js) pour utiliser la fonction `setState` pour mettre à jour l'état.

Voici une [Démonstration Code Sandbox mise à jour](https://codesandbox.io/s/withered-dust-p3emg?file=/src/index.js).

Si vous regardez la fonction `handleClick` mise à jour, elle ressemble à ceci :

```js
handleClick() {
  this.setState((prevState) => {
    return {
      counter: prevState.counter + 1
    };
  });

  console.log("counter", this.state.counter);
}

```

Ici, nous passons une fonction comme premier argument à la fonction `setState` et nous retournons un nouvel objet d'état avec `counter` incrémenté de 1 basé sur la valeur précédente de `counter`.

Nous utilisons la fonction fléchée dans le code ci-dessus, mais l'utilisation d'une fonction normale fonctionnera également.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/counter_updated_async.gif)

Si vous remarquez, nous obtenons correctement la valeur mise à jour du `counter` sur l'UI. Mais dans la console, nous obtenons la valeur précédente du `counter` même si nous avons ajouté console.log après l'appel de `this.setState`.

> C'est parce que la fonction `setState` est asynchrone par nature.

Cela signifie que même si nous avons appelé `setState` pour incrémenter la valeur du `counter` de 1, cela ne se produit pas immédiatement. C'est parce que lorsque nous appelons la fonction `setState`, tout le composant est réaffiché – donc React doit vérifier ce qui doit être changé en utilisant l'algorithme du DOM virtuel et puis effectuer diverses vérifications pour une mise à jour efficace de l'UI.

C'est la raison pour laquelle vous ne pouvez pas obtenir la valeur mise à jour du `counter` immédiatement après l'appel de `setState`.

> C'est une chose très importante à garder à l'esprit dans React, car vous rencontrerez des problèmes difficiles à déboguer si vous n'écrivez pas votre code en gardant à l'esprit que `setState` est asynchrone dans React.

Si vous voulez obtenir la valeur mise à jour de l'état immédiatement après l'appel de `setState`, vous pouvez passer une fonction comme second argument à l'appel de `setState` qui sera exécutée une fois que l'état est mis à jour.

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/jolly-dawn-65wis?file=/src/index.js) avec ce changement.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/counter_updated_sync.gif)

Comme vous pouvez le voir, nous obtenons la valeur correcte du `counter` dans la console dès qu'il est mis à jour sur l'UI.

Dans la démonstration ci-dessus, la fonction `handleClick` ressemble à ceci :

```js
handleClick() {
  this.setState(
    (prevState) => {
      return {
        counter: prevState.counter + 1
      };
    },
    () => console.log("counter", this.state.counter)
  );
}

```

Donc ici, pour l'appel de la fonction `setState`, nous passons deux arguments. Le premier est une fonction qui retourne un nouvel état et le second est une fonction de rappel qui sera appelée une fois que l'état est mis à jour. Nous journalisons simplement la valeur mise à jour du compteur dans la console dans la fonction de rappel.

> Même si React fournit une fonction de rappel pour obtenir la valeur mise à jour de l'état immédiatement, il est recommandé de l'utiliser uniquement pour des tests rapides ou des journalisations.

Au lieu de cela, React recommande d'utiliser la méthode `componentDidUpdate`, qui est une méthode de cycle de vie de React qui ressemble à ceci :

```js
componentDidUpdate(prevProps, prevState) {
  if (prevState.counter !== this.state.counter) {
    // faire quelque chose
    console.log("counter", this.state.counter);
  }
}

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/youthful-pine-txb1o?file=/src/index.js).

Vous pouvez trouver plus d'informations sur pourquoi utiliser `componentDidUpdate` au lieu du rappel `setState` [ici](https://stackoverflow.com/questions/56501409/what-is-the-advantage-of-using-componentdidupdate-over-the-setstate-callback#answer-56502614).

## Comment simplifier la déclaration de l'état et des méthodes

Si vous regardez le code du constructeur dans les démonstrations Code Sandbox ci-dessus, vous verrez qu'il ressemble à ceci :

```js
constructor(props) {
  super(props);

  this.state = {
    counter: 0
  };

  this.handleClick = this.handleClick.bind(this);
}

```

Pour utiliser le mot-clé `this` à l'intérieur du gestionnaire d'événements `handleClick`, nous devons le lier dans le constructeur comme ceci :

```js
this.handleClick = this.handleClick.bind(this);

```

De plus, pour déclarer l'état, nous devons créer un constructeur, ajouter un appel `super` à l'intérieur, et ensuite nous pouvons déclarer l'état.

Cela n'est pas seulement fastidieux, mais rend également le code inutilement compliqué.

À mesure que le nombre de gestionnaires d'événements augmente, le nombre d'appels `.bind` augmente également. Nous pouvons éviter de faire cela en utilisant la syntaxe des propriétés de classe.

Voici une [Démonstration Code Sandbox mise à jour](https://codesandbox.io/s/sad-bassi-7fxnl?file=/src/index.js) avec la syntaxe des propriétés de classe.

Ici, nous avons déplacé l'état directement à l'intérieur de la classe comme ceci :

```js
state = {
   counter: 0
};

```

et le gestionnaire d'événements `handlerClick` est changé en syntaxe de fonction fléchée comme ceci :

```js
handleClick = () => {
  this.setState((prevState) => {
    return {
      counter: prevState.counter + 1
    };
  });
};

```

Comme les fonctions fléchées n'ont pas leur propre contexte `this`, elles prendront le contexte comme la classe, donc il n'est pas nécessaire d'utiliser la méthode `.bind`.

Cela rend le code beaucoup plus simple et plus facile à comprendre car nous n'avons pas besoin de continuer à lier chaque gestionnaire d'événements.

> [create-react-app](https://github.com/facebook/create-react-app) a déjà un support intégré pour cela et vous pouvez commencer à utiliser cette syntaxe dès maintenant.

Nous utiliserons cette syntaxe à partir de maintenant, car c'est la manière la plus populaire et préférée d'écrire des composants React.

Si vous voulez en savoir plus sur cette syntaxe des propriétés de classe, consultez [mon article ici](https://javascript.plainenglish.io/how-to-write-clean-and-easy-to-understand-react-code-using-class-properties-syntax-5b375b0618d3?source=friends_link&sk=c170992cab9025fddb7b34b8894ea993).

## Comment utiliser la syntaxe ES6 raccourcie

Si vous regardez l'appel de la fonction `setState` dans le bac à sable de code ci-dessus, il ressemble à ceci :

```js
this.setState((prevState) => {
  return {
    counter: prevState.counter + 1
  };
});

```

C'est beaucoup de code. Juste pour retourner un objet d'une fonction, nous utilisons 5 lignes de code.

Nous pouvons le simplifier en une seule ligne comme ci-dessous :

```js
this.setState((prevState) => ({ counter: prevState.counter + 1 }));

```

Ici, nous avons enveloppé l'objet dans des parenthèses rondes pour le faire retourner implicitement. Cela fonctionne parce que si nous avons une seule instruction dans une fonction fléchée, nous pouvons sauter le mot-clé return et les accolades comme ceci :

```js
const add = (a, b) => { 
 return a + b;
}

// le code ci-dessus est le même que le code ci-dessous :

const add = (a, b) => a + b;

```

Mais comme l'accolade ouvrante est considérée comme le début du corps de la fonction, nous devons envelopper l'objet à l'intérieur de parenthèses rondes pour qu'il fonctionne correctement.

Voici une [Démonstration Code Sandbox mise à jour](https://codesandbox.io/s/zen-galois-pew17?file=/src/index.js) avec ce changement.

## Comment utiliser un objet comme mise à jour d'état dans React

Dans le code ci-dessus, nous avons utilisé une fonction comme premier argument pour `setState`, mais nous pouvons également passer un objet comme argument.

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/zealous-nobel-yvvmw?file=/src/index.js).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/updated_name.gif)

Le code du composant ressemble à ceci :

```js
class User extends React.Component {
  state = {
    name: "Mike"
  };

  handleChange = (event) => {
    const value = event.target.value;
    this.setState({ name: value });
  };

  render() {
    const { name } = this.state;

    return (
      <div>
        <input
          type="text"
          onChange={this.handleChange}
          placeholder="Entrez votre nom"
          value={name}
        />
        <div>Bonjour, {name}</div>
      </div>
    );
  }
}

```

Ici, nous avons ajouté une zone de texte d'entrée où l'utilisateur tape son nom et il est affiché sous la zone de texte au fur et à mesure que l'utilisateur tape dans la zone de texte.

Dans l'état, nous avons initialisé la propriété name à `Mike` et nous avons ajouté un gestionnaire `onChange` à la zone de texte d'entrée comme ceci :

```js
state = {
  name: "Mike"
};

...

<input
  type="text"
  onChange={this.handleChange}
  placeholder="Entrez votre nom"
  value={name}
/>

```

Ainsi, lorsque nous tapons quelque chose dans la zone de texte, nous mettons à jour l'état avec la valeur tapée en passant un objet à la fonction `setState`.

```js
handleChange = (event) => {
  const value = event.target.value;
  this.setState({ name: value });
}

```

> Mais quelle forme de `setState` devons-nous utiliser – quelle est la préférée ? Nous devons décider si nous devons passer un objet ou une fonction comme premier argument à la fonction `setState`.

**La réponse est :** passez un objet si vous n'avez pas besoin du paramètre `prevState` pour trouver la valeur de l'état suivant. Sinon, passez la fonction comme premier argument à `setState`.

Mais vous devez être conscient d'un problème avec le passage d'un objet comme argument.

Regardez cette [Démonstration Code Sandbox](https://codesandbox.io/s/eloquent-panini-u2ooe?file=/src/index.js).

Dans la démonstration ci-dessus, la méthode `handleClick` ressemble à ceci :

```js
handleClick = () => {
  const { counter } = this.state;
  this.setState({
    counter: counter + 1
  });
}

```

Nous prenons la valeur actuelle du `counter` et l'incrémentons de 1. Cela fonctionne bien, comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/object_setstate_correct.gif)

Maintenant, regardez cette [Démonstration Code Sandbox](https://codesandbox.io/s/busy-johnson-oqvfn?file=/src/index.js) qui est une version modifiée de la démonstration Code Sandbox précédente.

Notre méthode `handleClick` ressemble maintenant à ceci :

```js
handleClick = () => {
  this.setState({
    counter: 5
  });

  const { counter } = this.state;

  this.setState({
    counter: counter + 1
  });
}

```

Ici, nous définissons d'abord la valeur du `counter` à 5, puis nous l'incrémentons de 1. Donc la valeur attendue du `counter` est 6. Voyons si c'est le cas.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/object_setstate_wrong.gif)

Comme vous pouvez le voir, lorsque nous cliquons sur le bouton pour la première fois, nous nous attendions à ce que la valeur du `counter` devienne 5 – mais elle devient 1, et à chaque clic suivant, elle est incrémentée de 1.

C'est parce que, comme nous l'avons vu précédemment, la fonction `setState` est asynchrone par nature. Lorsque nous appelons `setState`, la valeur du `counter` ne devient pas 5 immédiatement, donc à la ligne suivante, nous obtenons la valeur du `counter` de 0 à laquelle nous avons initialisé l'état au début.

Ainsi, elle devient 1 lorsque nous appelons à nouveau `setState` pour incrémenter le `counter` de 1, et elle continue à s'incrémenter de 1 seulement.

Pour corriger ce problème, nous devons utiliser la syntaxe de mise à jour de `setState` où nous passons une fonction comme premier argument.

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/strange-silence-qhykz?file=/src/index.js).

Dans la démonstration ci-dessus, la méthode `handleClick` ressemble maintenant à ceci :

```js
handleClick = () => {
  this.setState({
    counter: 5
  });

  this.setState((prevState) => {
    return {
      counter: prevState.counter + 1
    };
  });

  this.setState((prevState) => {
    return {
      counter: prevState.counter + 1
    };
  });
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/04/object_setstate_updater.gif)

Comme vous pouvez le voir, lorsque nous cliquons pour la première fois sur le bouton, la valeur du `counter` devient 7. C'est comme prévu, car nous l'avons d'abord définie à 5, puis nous l'avons incrémentée deux fois, donc elle devient 7. Et elle reste à 7 même si nous cliquons plusieurs fois sur le bouton, car à chaque clic, nous la réinitialisons à 5 et nous l'incrémentons deux fois.

C'est parce qu'à l'intérieur de `handleClick`, nous appelons `setState` pour définir la valeur du `counter` à 5 en passant un objet comme premier argument à la fonction `setState`. Après cela, nous avons appelé deux appels `setState` où nous utilisons la fonction comme premier argument.

Alors, comment cela fonctionne-t-il correctement ?

Lorsque React voit un appel `setState`, il planifie une mise à jour pour apporter une modification à l'état car il est asynchrone. Mais avant qu'il ne termine la modification de l'état, React voit qu'il y a un autre appel `setState`.

À cause de cela, React ne réaffichera pas immédiatement avec une nouvelle valeur de `counter`. Au lieu de cela, il fusionne tous les appels `setState` et met à jour le `counter` en fonction de la valeur précédente du `counter` comme nous avons utilisé `prevState.counter` pour calculer la valeur du `counter`.

Et une fois que tous les appels `setState` sont terminés avec succès, React réaffiche le composant. Donc même s'il y a trois appels `setState`, React ne réaffichera le composant qu'une seule fois, ce que vous pouvez confirmer en ajoutant une instruction `console.log` à l'intérieur de la méthode `render`.

> Donc le point à retenir est que vous devez être prudent lorsque vous utilisez un objet comme premier argument d'un appel `setState`, car cela pourrait entraîner un résultat imprévisible. Utilisez la fonction comme premier argument pour obtenir le résultat correct basé sur le résultat précédent.

Vous ne pouvez pas appeler `setState` encore et encore comme nous l'avons fait dans la démonstration ci-dessus, mais vous pouvez l'appeler à l'intérieur d'une autre fonction comme montré ci-dessous :

```js
state = {
 isLoggedIn: false
};

...

doSomethingElse = () => {
 const { isLoggedIn } = this.state;
 if(isLoggedIn) {
   // faire quelque chose de différent 
 }
};

handleClick = () => {
  // du code
  this.setState({ isLoggedIn: true);
  doSomethingElse();
}

```

Dans le code ci-dessus, nous avons défini un état `isLoggedIn` et nous avons deux fonctions `handleClick` et `doSomethingElse`. À l'intérieur de la fonction `handleClick`, nous mettons à jour la valeur de l'état `isLoggedIn` à `true` et immédiatement nous appelons la fonction `doSomethingElse` à la ligne suivante.

Ainsi, à l'intérieur de `doSomethingElse`, vous pourriez penser que vous allez obtenir l'état `isLoggedIn` comme `true` et que le code à l'intérieur de la condition if sera exécuté. Mais il ne sera pas exécuté car `setState` est asynchrone et l'état ne sera peut-être pas mis à jour immédiatement.

C'est pourquoi React a ajouté des méthodes de cycle de vie comme `componendDidUpdate` pour faire quelque chose lorsque l'état ou les props sont mis à jour.

> Surveillez pour vérifier si vous utilisez la même variable `state` à nouveau dans la ligne suivante ou la fonction suivante pour effectuer une opération afin d'éviter ces résultats indésirables.

## Comment fusionner les appels setState dans React

Regardez cette [Démonstration CodeSandbox](https://codesandbox.io/s/bold-cache-zcj4u?file=/src/index.js).

Ici, nous avons les propriétés `username` et `counter` déclarées dans l'état comme ceci :

```js
state = {
  counter: 0,
  username: ""
};

```

et les gestionnaires d'événements `handleOnClick` et `handleOnChange` déclarés comme ceci :

```js
handleOnClick = () => {
  this.setState((prevState) => ({
    counter: prevState.counter + 1
  }));
};

handleOnChange = (event) => {
  this.setState({
    username: event.target.value
  });
};

```

Vérifiez les appels `setState` dans les fonctions ci-dessus. Vous pouvez voir qu'à l'intérieur de la fonction `handleOnClick`, nous définissons uniquement l'état pour `counter`, et à l'intérieur de la fonction `handleOnChange`, nous définissons uniquement l'état pour `username`.

Ainsi, nous n'avons pas besoin de définir l'état pour les deux variables d'état en même temps comme ceci :

```js
this.setState((prevState) => ({
    counter: prevState.counter + 1,
    username: "somevalue"
}));

```

Nous pouvons mettre à jour uniquement celui que nous voulons mettre à jour. React fusionnera manuellement les autres propriétés d'état, donc nous n'avons pas besoin de nous soucier de les fusionner manuellement nous-mêmes.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/state_merged-1.gif)

Comme vous pouvez le voir, nous changeons avec succès le `counter` et le `username` indépendamment l'un de l'autre.

## Comment utiliser l'état dans les composants fonctionnels dans React

Jusqu'à présent, nous avons vu comment utiliser l'état dans les composants basés sur des classes. Voyons maintenant comment l'utiliser dans les composants fonctionnels.

Les composants fonctionnels sont similaires aux composants de classe, sauf qu'ils n'ont pas d'état et de méthodes de cycle de vie. C'est pourquoi vous les avez peut-être entendus appeler des composants fonctionnels sans état.

Ces composants n'acceptent que les props et retournent du JSX.

Les composants fonctionnels rendent le code plus court et plus facile à comprendre et à tester.

Ils sont également un peu plus rapides à exécuter, car ils n'ont pas de méthodes de cycle de vie. Ils n'ont pas non plus les données supplémentaires apportées par la classe `React.Component` que nous étendons dans les composants basés sur des classes.

Regardez cette [Démonstration Code Sandbox](https://codesandbox.io/s/sleepy-pascal-8ugh3?file=/src/index.js).

Ici, nous chargeons une liste de 20 utilisateurs aléatoires à partir de l'[API de générateur d'utilisateurs aléatoires](https://randomuser.me/), lorsque le composant est chargé à l'intérieur de la méthode `componentDidMount` comme ceci :

```js
componentDidMount() {
  axios
    .get("https://randomuser.me/api/?page=0&results=20")
    .then((response) => this.setState({ users: response.data.results }))
    .catch((error) => console.log(error));
}

```

Et une fois que nous avons obtenu ces utilisateurs, nous les définissons dans l'état `users` et les affichons sur l'UI.

```jsx
{users.map((user) => (
  <User key={user.login.uuid} name={user.name} email={user.email} />
))}

```

Ici, nous passons toutes les données dont nous avons besoin pour l'affichage au composant `User`.

Le composant `User` ressemble à ceci :

```jsx
const User = (props) => {
  const { name, email } = props;
  const { first, last } = name;

  return (
    <div>
      <p>
        Nom : {first} {last}
      </p>
      <p>Email : {email} </p>
      <hr />
    </div>
  );
};

```

**Ce composant `User` est un composant fonctionnel.**

Un composant fonctionnel est une fonction qui commence par une lettre majuscule et retourne du JSX.

N'oubliez jamais de commencer le nom de votre composant par une lettre majuscule comme `User`, qu'il s'agisse d'un composant basé sur une classe ou d'un composant fonctionnel. C'est ainsi que React le différencie des éléments HTML normaux lorsque nous les utilisons comme `<User />`.

Si nous utilisons `<user />`, React recherchera l'élément HTML avec le nom `user`. Comme il n'existe pas d'élément HTML de ce type, vous n'obtiendrez pas le résultat souhaité.

Dans le composant fonctionnel `User` ci-dessus, nous obtenons les props passées au composant à l'intérieur du paramètre `props` de la fonction.

Ainsi, au lieu d'utiliser `this.props` comme dans les composants de classe, nous utilisons simplement `props`.

Nous n'utilisons jamais le mot-clé `this` dans les composants fonctionnels, ce qui évite les divers problèmes associés à la liaison de `this`.

Par conséquent, les composants fonctionnels sont préférés aux composants de classe.

Une fois que nous avons `props`, nous utilisons la syntaxe de déstructuration d'objet pour obtenir les valeurs et les afficher sur l'UI.

## Comment utiliser l'état dans les hooks React

À partir de la version 16.8.0, React a introduit les hooks. Et ils ont complètement changé la façon dont nous écrivons du code dans React. En utilisant les hooks React, nous pouvons utiliser l'état et les méthodes de cycle de vie à l'intérieur des composants fonctionnels.

> Les hooks React sont des composants fonctionnels avec état et méthodes de cycle de vie ajoutés.

Ainsi, il y a maintenant très peu ou pas de différence entre les composants basés sur des classes et les composants fonctionnels.

Les deux peuvent avoir un état et des méthodes de cycle de vie.

Mais les hooks React sont maintenant préférés pour écrire des composants React car ils rendent le code plus court et plus facile à comprendre.

Vous trouverez rarement des composants React écrits en utilisant des composants de classe de nos jours.

Pour déclarer un état en utilisant les hooks React, nous devons utiliser le hook `useState`.

Le hook `useState` accepte un paramètre qui est la valeur initiale de l'état.

Dans les composants basés sur des classes, l'état est toujours un objet. Mais lorsque vous utilisez `useState`, vous pouvez fournir n'importe quelle valeur comme valeur initiale, comme un nombre, une chaîne, un booléen, un objet, un tableau, null, etc.

Le hook `useState` retourne un tableau dont la première valeur est la valeur actuelle de l'état. La deuxième valeur est la fonction que nous utiliserons pour mettre à jour l'état, similaire à la méthode `setState`.

Prenons un exemple de composant basé sur une classe qui utilise l'état. Nous allons le convertir en un composant fonctionnel en utilisant des hooks.

```jsx
import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  state = {
    counter: 0
  };

  handleOnClick = () => {
    this.setState(prevState => ({
      counter: prevState.counter + 1
    }));
  };

  render() {
    return (
      <div>
        <p>La valeur du compteur est : {this.state.counter} </p>
        <button onClick={this.handleOnClick}>Incrémenter</button>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('root'));

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/delicate-thunder-xdpri?file=/src/index.js) qui est écrite en utilisant des composants de classe.

Convertissons le code ci-dessus pour utiliser des hooks.

```jsx
import React, { useState } from "react";
import ReactDOM from "react-dom";

const App = () => {
  const [counter, setCounter] = useState(0);

  return (
    <div>
      <div>
        <p>La valeur du compteur est : {counter} </p>
        <button onClick={() => setCounter(counter + 1)}>Incrémenter</button>
      </div>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/elegant-heyrovsky-3qco5?file=/src/index.js) qui est écrite en utilisant des hooks React.

Comme vous pouvez le voir, l'utilisation des hooks React rend le code beaucoup plus court et plus facile à comprendre.

Comprenons le code ci-dessus.

* Pour utiliser le hook `useState`, nous devons l'importer comme nous l'avons fait dans la première ligne.
* À l'intérieur du composant App, nous appelons `useState` en passant `0` comme valeur initiale et en utilisant la syntaxe de déstructuration. Nous avons stocké les valeurs de tableau retournées par `useState` dans les variables `counter` et `setCounter`.
* Il est courant de préfixer le nom de la fonction utilisée pour mettre à jour l'état avec le mot-clé `set` comme dans `setCounter`.
* Lorsque nous cliquons sur le bouton d'incrémentation, nous définissons une fonction en ligne et appelons la fonction `setCounter` en passant la valeur mise à jour du compteur.
* Notez que comme nous avons déjà la valeur du compteur, nous l'avons utilisée pour incrémenter le compteur en utilisant `setCounter(counter + 1)`
* Comme il y a une seule instruction dans le gestionnaire de clic en ligne, il n'est pas nécessaire de déplacer le code dans une fonction séparée. Bien que vous puissiez le faire si le code à l'intérieur du gestionnaire devient complexe.

Si vous voulez en savoir plus sur `useState` et les autres hooks React (avec des exemples), consultez mon article [Introduction aux hooks React](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54).

### Merci d'avoir lu !

Vous voulez apprendre toutes les fonctionnalités ES6+ en détail, y compris let et const, les promesses, diverses méthodes de promesses, la déstructuration de tableaux et d'objets, les fonctions fléchées, async/await, import et export, et bien plus encore à partir de zéro ?

**Consultez mon livre [Maîtriser le JavaScript moderne](https://modernjavascript.yogeshchavan.dev/). Ce livre couvre tous les prérequis pour apprendre React et vous aide à devenir meilleur en JavaScript et React.**

> Consultez le contenu gratuit de l'aperçu du livre [ici](https://www.freecodecamp.org/news/learn-modern-javascript/).

De plus, vous pouvez consulter mon cours **gratuit** [Introduction à React Router](https://yogeshchavan.podia.com/react-router-introduction) pour apprendre React Router à partir de zéro.

Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

<a href="https://bit.ly/3w0DGum" target="_blank" rel="noreferrer noopener"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/c3e4265df4396d639a7938a83bffd570130483b1/banner.jpg" /></a>