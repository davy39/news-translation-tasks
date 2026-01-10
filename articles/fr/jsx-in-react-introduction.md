---
title: JSX dans React – Expliqué avec des Exemples
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-02-01T21:24:17.000Z'
originalURL: https://freecodecamp.org/news/jsx-in-react-introduction
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/jsx.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: JSX
  slug: jsx
- name: React
  slug: react
seo_title: JSX dans React – Expliqué avec des Exemples
seo_desc: 'JSX is one of the core concepts of React. So if you understand it well,
  you''ll be able to write better React code.

  In this article, we''ll explore:


  What is JSX in React and how to use it

  How JSX is transformed to React.createElement

  What is a JSX exp...'
---

JSX est l'un des concepts fondamentaux de React. Ainsi, si vous le comprenez bien, vous pourrez écrire un meilleur code React.

Dans cet article, nous explorerons :

* Qu'est-ce que JSX dans React et comment l'utiliser
* Comment JSX est transformé en `React.createElement`
* Qu'est-ce qu'une expression JSX et ce que nous pouvons écrire à l'intérieur
* Problèmes courants dans JSX

Et bien plus encore. Alors, commençons.

## Qu'est-ce que JSX ?

> JSX est une syntaxe d'extension JavaScript utilisée dans React pour écrire facilement HTML et JavaScript ensemble.

Jetez un œil au code ci-dessous :

```js
const jsx = <h1>Ceci est JSX</h1>
```

Ceci est un simple code JSX dans React. Mais le navigateur ne comprend pas ce JSX car ce n'est pas un code JavaScript valide. Cela est dû au fait que nous attribuons une balise HTML à une variable qui n'est pas une chaîne mais simplement du code HTML.

Ainsi, pour le convertir en code JavaScript compréhensible par le navigateur, nous utilisons un outil comme [Babel](https://babeljs.io/) qui est un compilateur/transpileur JavaScript.

Vous pouvez configurer votre propre configuration Babel en utilisant Webpack comme je le montre dans [cet article](https://medium.com/javascript-in-plain-english/webpack-and-babel-setup-with-react-from-scratch-bef0fe2ae3e7?source=friends_link&sk=880a6b9a35fb638eef19e5e99276428e). Ou vous pouvez utiliser [create-react-app](https://github.com/facebook/create-react-app) qui utilise Babel en interne pour la conversion de JSX en JavaScript.

Nous pouvons utiliser le JSX ci-dessus dans notre code React comme ceci :

```js
class JSXDemo extends React.Component {
    render() {
        return <h1>Ceci est JSX</h1>;
    }
}

ReactDOM.render(<JSXDemo />, document.getElementById('root'));
```

Ici, nous retournons le JSX depuis le composant `JSXDemo` et nous le rendons à l'écran en utilisant la méthode `ReactDOM.render`.

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/awesome-framework-7kr3d?file=/src/index.js).

Lorsque Babel exécute le JSX ci-dessus, il le convertit en le code suivant :

```js
class JSXDemo extends React.Component {
    render() {
        return React.createElement("h1", null, "Ceci est JSX");
    }
}
```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/billowing-dust-b357d?file=/src/index.js).

Comme vous pouvez le voir dans la démonstration Code Sandbox ci-dessus, le code imprime toujours correctement le contenu à l'écran en utilisant `React.createElement`.

C'était l'ancienne façon d'écrire du code dans React – mais il est fastidieux d'écrire `React.createElement` à chaque fois, même pour ajouter une simple div.

Ainsi, React a introduit la manière JSX d'écrire du code, ce qui rend le code facile à écrire et à comprendre.

> Savoir comment convertir JSX en `React.createElement` est très important en tant que développeur React (c'est aussi une question d'entretien populaire).

## Qu'est-ce que la fonction React.createElement ?

Chaque JSX est converti en un appel de fonction `React.createElement` que le navigateur comprend.

La fonction `React.createElement` a la syntaxe suivante :

```js
React.createElement(type, [props], [...children])
```

Examinons les paramètres de la fonction `createElement`.

* **type** peut être une balise HTML comme h1, div ou cela peut être un composant React
* **props** sont les attributs que vous souhaitez que l'élément ait
* **children** contient d'autres balises HTML ou peut être un composant

L'appel `React.createElement` sera également converti en représentation d'objet comme ceci :

```js
{   
 type: 'h1',   
 props: {     
   children: 'Ceci est JSX'   
 }
}

```

Vous pouvez voir cette représentation d'objet si vous attribuez le JSX à une variable locale et que vous l'affichez comme montré ci-dessous :

```js
class JSXDemo extends React.Component {
    render() {
        const jsx = <h1>Ceci est JSX</h1>;
        console.log(jsx);
        return jsx;
    }
}

ReactDOM.render(<JSXDemo />, document.getElementById('root'));
```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/epic-spence-jcp5t?file=/src/index.js).

Vous verrez le journal affiché comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/log.png)

Maintenant, jetez un œil au code ci-dessous :

```js
class JSXDemo extends React.Component {
  render() {
    const jsx = <h1 id="jsx">Ceci est JSX</h1>;
    console.log(jsx);
    return jsx;
  }
}

ReactDOM.render(<JSXDemo />, document.getElementById("root"));

```

Ici, nous avons utilisé le JSX comme ceci :

```js
<h1 id="jsx">Ceci est JSX</h1>
```

Ainsi, React convertira ce JSX en le code suivant :

```js
React.createElement("h1", { id: "jsx" }, "Ceci est JSX");
```

Si des attributs sont ajoutés à la balise HTML comme dans notre cas, ils seront passés en tant que deuxième paramètre pour l'appel `React.createElement`. La représentation d'objet ressemblera à ceci :

```js
{ 
  type: 'h1', 
  props: { 
   id: 'jsx',
   children: 'Ceci est JSX'
  } 
}
```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/infallible-lake-rz7vj?file=/src/index.js).

Vous verrez le journal affiché comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/create_element.png)

Maintenant, ajoutons une certaine complexité au JSX pour voir comment il est converti en appel `React.createElement`.

```js
class JSXDemo extends React.Component {
  handleOnClick = () => {
    console.log("cliqué");
  };
  render() {
    return (
      <button id="btn" onClick={this.handleOnClick}>
        Cliquez ici
      </button>
    );
  }
}

ReactDOM.render(<JSXDemo />, document.getElementById("root"));
```

Ici, nous avons ajouté un gestionnaire `onClick` au bouton.

Pour le code ci-dessus, l'appel `React.createElement` ressemblera à ceci :

```js
React.createElement("button", {
  id: "btn", 
  onClick: function() {}
}, "Cliquez ici")
```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/new-dew-sc2rp?file=/src/index.js).

La représentation d'objet ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/id_children.png)

Ainsi, à partir de tous les exemples ci-dessus, il est clair que JSX est converti en un appel `React.createElement` et qu'il est ensuite converti en sa représentation d'objet.

Si vous souhaitez voir le code de conversion de JSX en `React.createElement`, vous pouvez naviguer vers [cette application](https://babel-repl-clone.now.sh/) que j'ai créée dans [cet article](https://levelup.gitconnected.com/create-a-clone-of-babel-repl-site-to-convert-es6-react-code-to-es5-93cdc9ad98ea?source=friends_link&sk=517cfac3dfc4b451610eb298f36a428c). Là, vous pouvez écrire du code JSX à gauche et voir le code converti à droite comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/conversion.png)

## Comment retourner du JSX complexe

Jetez un œil au code ci-dessous :

```js
import React from "react";
import ReactDOM from "react-dom";

const App = () => {
  return (
      <p>Ceci est le premier élément JSX !</p>
      <p>Ceci est un autre élément JSX</p>
  );
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);

```

Voici une [démonstration Code Sandbox](https://codesandbox.io/s/objective-thunder-3hqqz?file=/src/index.js).

Ici, nous retournons deux paragraphes depuis le composant App. Mais si vous exécutez le code, vous obtiendrez cette erreur :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/adjacent_error.png)

Nous obtenons une erreur car React exige que les éléments adjacents soient enveloppés dans une balise parente.

Comme nous l'avons vu, `<p>Ceci est le premier élément JSX !</p>` sera converti en `React.createElement("p", null, "Ceci est le premier élément JSX !")` et `<p>Ceci est un autre élément JSX</p>` sera converti en `React.createElement("p", null, "Ceci est un autre élément JSX")`.

Le code converti ressemblera maintenant à ceci :

```js
import React from "react";
import ReactDOM from "react-dom";

const App = () => {
  return (
            React.createElement("p", null, "Ceci est le premier élément JSX !"); React.createElement("p", null, "Ceci est un autre élément JSX");
        );
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
```

Ici, nous retournons deux éléments depuis le composant `App`, ce qui ne fonctionnera pas car il n'y a pas d'élément parent pour les envelopper tous les deux.

Pour que cela fonctionne, la solution évidente est de les envelopper tous les deux dans un élément parent, probablement une `div` comme ceci :

```js
import React from "react";
import ReactDOM from "react-dom";

const App = () => {
  return (
    <div>
      <p>Ceci est le premier élément JSX !</p>
      <p>Ceci est un autre élément JSX</p>
    </div>
  );
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/stoic-khorana-vnrt6?file=/src/index.js).

Mais il existe également d'autres moyens de faire en sorte que cela fonctionne.

Tout d'abord, vous pouvez essayer de le retourner sous forme de tableau comme montré ci-dessous :

```js
import React from "react";
import ReactDOM from "react-dom";

const App = () => {
  return (
    [<p>Ceci est le premier élément JSX !</p>,<p>Ceci est un autre élément JSX</p>]
  );
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/crazy-banach-wy756?file=/src/index.js).

Cela fera le travail, mais comme vous pouvez le voir dans la console du navigateur, vous obtiendrez un avertissement disant `Avertissement : Chaque enfant dans une liste doit avoir une prop "key" unique.`

> Car dans React, chaque élément dans le tableau (lorsqu'il est affiché en utilisant JSX) doit avoir une clé unique ajoutée.

Nous pouvons le corriger en ajoutant une clé unique pour les éléments adjacents :

```js
import React from "react";
import ReactDOM from "react-dom";

const App = () => {
  return (
    [<p key="first">Ceci est le premier élément JSX !</p>,<p key="second">Ceci est un autre élément JSX</p>]
  );
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/relaxed-resonance-ljzzf?file=/src/index.js).

L'autre moyen de le corriger est d'utiliser le composant `React.Fragment` :

```js
import React from "react";
import ReactDOM from "react-dom";

const App = () => {
  return (
    <React.Fragment>
      <p>Ceci est le premier élément JSX !</p>
      <p>Ceci est un autre élément JSX</p>
    </React.Fragment>
  );
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/fervent-morse-gsvk8?file=/src/index.js).

`React.Fragment` a été ajouté dans la version 16.2 de React car nous devons toujours envelopper plusieurs éléments adjacents dans une balise (comme div) à l'intérieur de chaque JSX retourné par un composant. Mais cela ajoute des balises div inutiles.

Cela est acceptable la plupart du temps, mais il existe certains cas où ce n'est pas acceptable.

Par exemple, si nous utilisons Flexbox, alors il existe une relation parent-enfant spéciale dans la structure de Flexbox. Et l'ajout de divs au milieu rend difficile le maintien de la mise en page souhaitée.

Ainsi, l'utilisation de `React.Fragment` résout ce problème.

> Les _Fragments_ vous permettent de regrouper une liste d'enfants sans ajouter de nœuds supplémentaires au DOM.

## Comment ajouter des commentaires au code JSX

Si vous avez une ligne de code comme ceci :

```js
<p>Ceci est un texte</p>
```

et que vous souhaitez ajouter un commentaire pour ce code, alors vous devez envelopper ce code dans la syntaxe d'expression JSX à l'intérieur des symboles de commentaire `/*` et `*/` comme ceci :

```js
{/* <p>Ceci est un texte</p> */}
```

_Astuce :_ Au lieu de taper manuellement le commentaire, vous pouvez utiliser les raccourcis clavier `Cmd + /` (Mac) ou `Ctrl + /` pour ajouter ou supprimer le commentaire.

## Comment ajouter du code JavaScript dans JSX

Jusqu'à présent, nous n'avons utilisé que des balises HTML dans JSX. Mais JSX devient plus utile lorsque nous ajoutons réellement du code JavaScript à l'intérieur.

Pour ajouter du code JavaScript à l'intérieur de JSX, nous devons l'écrire entre accolades comme ceci :

```js
const App = () => {
 const number = 10;
 return (
  <div>
   <p>Nombre : {number}</p>
  </div>
 );
};
```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/keen-leftpad-jygwo?file=/src/index.js).

> À l'intérieur des accolades, nous ne pouvons écrire qu'une expression qui évalue une valeur.

Ainsi, souvent cette syntaxe utilisant des accolades est connue sous le nom de Syntaxe d'Expression JSX.

Voici les éléments valides que vous pouvez avoir dans une Expression JSX :

* Une chaîne comme "bonjour"
* Un nombre comme 10
* Un tableau comme [1, 2, 4, 5]
* Une propriété d'objet qui évaluera une valeur
* Un appel de fonction qui retourne une valeur qui peut être JSX
* Une méthode map qui retourne toujours un nouveau tableau
* JSX lui-même

Voici les éléments invalides qui ne peuvent pas être utilisés dans une Expression JSX :

* Une boucle for ou while ou toute autre boucle
* Une déclaration de variable
* Une déclaration de fonction
* Une condition if
* Un objet

Nous pouvons écrire des tableaux dans les Expressions JSX car `<p>{[1, 2, 3, 4]}</p>` est finalement converti en `<p>{1}{2}{3}{4}</p>` lors du rendu (ce qui peut être rendu sans aucun problème).

Dans le cas d'un objet, il n'est pas clair comment l'objet doit être affiché. Par exemple, doit-il être des paires clé-valeur séparées par des virgules ou doit-il être affiché comme JSON ? Vous obtiendrez donc une erreur si vous essayez d'afficher l'objet dans une expression JSX. Mais nous pouvons utiliser des propriétés d'objet à la place.

> Notez également que undefined, null et boolean ne sont pas affichés sur l'interface utilisateur lorsqu'ils sont utilisés à l'intérieur de JSX.

Ainsi, si vous avez une valeur booléenne et que vous souhaitez l'afficher sur l'interface utilisateur, vous devez l'envelopper dans la syntaxe de littéral de gabarit ES6 comme ceci :

```js
const App = () => {
  const isAdmin = true;
  return (
    <div>
      <p>isAdmin est {`${isAdmin}`} </p>
    </div>
  );
};
```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/ecstatic-shamir-7b5z6?file=/src/index.js).

### Opérateurs conditionnels dans les Expressions JSX

Nous ne pouvons pas écrire de _conditions if_ dans les expressions JSX, ce que vous pourriez considérer comme un problème. Mais React nous permet d'écrire des opérateurs conditionnels, comme les opérateurs ternaires ainsi que l'opérateur de court-circuit logique && comme ceci :

```js
<p>{a > b ? "Plus grand" : "Plus petit"}</p>
<p>{shouldShow && "Affiché"}</p>
```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/condescending-wind-4rwtl) décrivant diverses façons d'écrire des expressions JSX.

## Comment imbriquer des Expressions JSX

Vous pouvez même faire de l'imbrication d'expressions JSX comme ceci :

```js
const App = () => {
  const number = 10;
  return (
    <div>
      {number > 0 ? (
        <p>Le nombre {number} est positif</p>
      ) : (
        <p>Le nombre {number} est négatif</p>
      )}
    </div>
  );
};
```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/frosty-dew-mj351?file=/src/index.js).

## Comment ajouter une classe dans JSX

Nous pouvons ajouter des attributs aux éléments JSX, par exemple `id` et `class`, de la même manière qu'en HTML.

```js
import React from "react";
import ReactDOM from "react-dom";

const App = () => {
  const id = "some-id";
  return (
    <div>
      <h1 id={id}>Ceci est un titre</h1>
      <h2 className="active">Ceci est un autre titre</h2>
    </div>
  );
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);

```

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/great-chandrasekhar-i48t2).

Notez que dans React, nous devons utiliser `className` au lieu de `class`.

Cela est dû au fait que si vous utilisez `class` au lieu de `className`, vous obtiendrez un avertissement dans la console comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/class_warning.png)

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/happy-smoke-ecbtl?file=/src/index.js).

Pour comprendre pourquoi l'avertissement est affiché, imprimez la représentation d'objet et vous verrez ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/class_info-1.png)

Voici une [Démonstration Code Sandbox](https://codesandbox.io/s/epic-frost-e64ll?file=/src/index.js).

Comme vous pouvez le voir, l'objet props a la propriété `class` avec une valeur `active`. Mais en JavaScript, `class` est un mot réservé, donc l'accès à `props.class` entraînera une erreur.

C'est pourquoi React a décidé d'utiliser `className` au lieu de `class`.

Cette utilisation de `className` au lieu de `class` est une question fréquemment posée lors des entretiens React.

> Notez que dans React, tous les noms d'attributs sont écrits en camelCase.

Vous pouvez trouver la liste de tous les attributs modifiés et inchangés [ici](https://reactjs.org/docs/dom-elements.html#all-supported-html-attributes).

## Conclusion

Dans cet article, nous avons vu comment utiliser JSX dans React. Voici quelques points clés à retenir :

* Chaque balise JSX est convertie en appel `React.createElement` et sa représentation d'objet.
* Les Expressions JSX, qui sont écrites entre accolades, permettent uniquement les éléments qui évaluent une valeur comme une chaîne, un nombre, un tableau, une méthode map, etc.
* Dans React, nous devons utiliser `className` au lieu de `class` pour ajouter des classes à l'élément HTML
* Tous les noms d'attributs dans React sont écrits en camelCase.
* `undefined`, `null` et `boolean` ne sont pas affichés sur l'interface utilisateur lorsqu'ils sont utilisés à l'intérieur de JSX.

### Merci d'avoir lu !

Consultez mon cours gratuit [Introduction à React Router](https://yogeshchavan.podia.com/react-router-introduction).

Consultez également mon livre [Maîtriser le JavaScript Moderne](https://modernjavascript.yogeshchavan.dev/) pour apprendre toutes les dernières fonctionnalités ES6+ en détail afin de devenir meilleur en JavaScript et React.

**Abonnez-vous à ma [newsletter hebdomadaire](https://yogeshchavan.dev/) pour rejoindre plus de 1000 autres abonnés et recevoir des conseils, astuces, articles et offres de réduction directement dans votre boîte de réception.**