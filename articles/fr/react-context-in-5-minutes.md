---
title: Apprendre React Context en 5 Minutes - Un Tutoriel pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-08T21:47:33.000Z'
originalURL: https://freecodecamp.org/news/react-context-in-5-minutes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f7c740569d1a4ca42d5.jpg
tags:
- name: React
  slug: react
- name: React context
  slug: react-context
- name: Tutorial
  slug: tutorial
seo_title: Apprendre React Context en 5 Minutes - Un Tutoriel pour Débutants
seo_desc: 'By Bob Ziroll

  React''s Context API has become the state management tool of choice for many, oftentimes
  replacing Redux altogether. In this quick 5-minute tutorial, you''ll see an introduction
  to what Context is and how to use it!

  If you want a proper i...'
---

Par Bob Ziroll

L'API Context de React est devenue l'outil de gestion d'état de choix pour beaucoup, remplaçant souvent Redux. Dans ce tutoriel rapide de 5 minutes, vous verrez une introduction à ce qu'est Context et comment l'utiliser !

Si vous voulez une introduction appropriée à ce sujet, vous pouvez rejoindre la liste d'attente pour mon [prochain cours avancé sur React](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=context_article), ou si vous êtes encore débutant, consultez mon [cours d'introduction gratuit sur React.](https://scrimba.com/g/glearnreact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=context_article)

Considérez cet arbre, dans lequel les boîtes du bas représentent des composants séparés :

![Arbre de composants](https://thepracticaldev.s3.amazonaws.com/i/gevur92qwoxvdjnm12dw.png)

Nous pouvons facilement ajouter un état aux composants du bas, mais jusqu'à présent, la seule façon de passer des données à un frère d'un composant était de déplacer l'état vers un composant parent plus haut, puis de le redescendre vers le frère via les props.

![Passage de données via props](https://thepracticaldev.s3.amazonaws.com/i/u20r26dtxyr6ek6krzsb.png)

Si nous découvrons plus tard que le frère du composant avec état a également besoin des données, nous devons à nouveau remonter l'état et le redescendre :

![Passage d'état à travers plusieurs niveaux](https://thepracticaldev.s3.amazonaws.com/i/wtlykrxnx8xi12h4wek4.png)

Bien que cette solution fonctionne, des problèmes commencent si un composant sur une autre branche a besoin des données :

![Composant plus distant nécessite des données](https://thepracticaldev.s3.amazonaws.com/i/g3xrvthcw24izllvb58w.png)

Dans ce cas, nous devons passer l'état du niveau supérieur de l'application à travers tous les composants intermédiaires jusqu'à celui qui a besoin des données en bas, même si les niveaux intermédiaires n'en ont pas besoin. Ce processus fastidieux et chronophage est connu sous le nom de _prop drilling_.

![Prop drilling](https://thepracticaldev.s3.amazonaws.com/i/ey25z0hvmy31xiiqqwgq.png)

C'est là que l'API Context intervient. Elle fournit un moyen de passer des données à travers l'arbre des composants via une paire Provider-Consumer sans avoir à passer des props à travers chaque niveau. Pensez-y comme les composants jouant à se passer des données - les composants intermédiaires ne "savent" peut-être même pas que quelque chose se passe :

![Contexte en action](https://thepracticaldev.s3.amazonaws.com/i/ckfpokb2cz3ffmn8238i.png)

Pour démontrer cela, nous allons créer cette image de commutation jour-nuit (et super utile).

<a href="https://imgflip.com/gif/3evdww"><img src="https://i.imgflip.com/3evdww.gif" title="made at imgflip.com"/></a>

Si vous voulez voir le code complet, assurez-vous de consulter [le terrain de jeu Scrimba pour cet article](https://scrimba.com/c/czkvE4sw).

# Créer un Contexte

Pour commencer, nous créons un nouveau Contexte. Comme nous voulons que toute l'application ait accès à cela, nous allons dans `index.js` et enveloppons l'application dans `ThemeContext.Provider`.

Nous passons également la prop `value` à notre Provider. Cela contient les données que nous voulons sauvegarder. Pour l'instant, nous codons simplement `'Day'`.

```js
import React from "react";
import ReactDOM from "react-dom";
import ThemeContext from "./themeContext";

import App from "./App";

ReactDOM.render(
  <ThemeContext.Provider value={"Day"}>
    <App />
  </ThemeContext.Provider>,
  document.getElementById("root")
);
```

# Consommer le Contexte avec contextType

Actuellement, dans `App.js`, nous retournons simplement le composant `<Image />`.

```js
import React from "react";
import Image from "./Image";

class App extends React.Component {
  render() {
    return (
      <div className="app">
        <Image />
      </div>
    );
  }
}

export default App;
```

Notre objectif est d'utiliser le Contexte pour basculer les classNames dans `Image.js` de `Day` à `Night`, selon l'image que nous voulons rendre. Pour cela, nous ajoutons une propriété statique à notre composant appelée `ContextType`, puis utilisons l'interpolation de chaînes pour l'ajouter aux classNames dans le composant `<Image />`.

Maintenant, les classNames contiennent la chaîne de la prop `value`. **Note :** J'ai déplacé `ThemeContext` dans son propre fichier pour éviter un bug.

```js
import React from "react";
import Button from "./Button";
import ThemeContext from "./themeContext";

class Image extends React.Component {
  render() {
    const theme = this.context;
    return (
      <div className={`${theme}-image image`}>
        <div className={`${theme}-ball ball`} />
        <Button />
      </div>
    );
  }
}

Image.contextType = ThemeContext;

export default Image;
```

# Context.Consumer

Malheureusement, cette approche ne fonctionne qu'avec les composants basés sur des classes. Si vous avez déjà appris les [Hooks dans React](https://www.freecodecamp.org/news/react-hooks-in-5-minutes/), vous savez que nous pouvons faire presque tout avec des composants fonctionnels ces jours-ci. Donc, par mesure de précaution, nous devrions convertir nos composants en composants fonctionnels, puis utiliser le composant `ThemeContext.Consumer` pour passer des informations à travers l'application.

Cela se fait en enveloppant nos éléments dans une instance de `<ThemeContext.Consumer>` et, à l'intérieur (où vont les `children`), en fournissant une fonction qui retourne les éléments. Cela utilise le motif "render prop" où nous fournissons une fonction régulière en tant qu'enfant qui retourne du JSX à rendre.

```js
import React from "react";
import Button from "./Button";
import ThemeContext from "./themeContext";

function Image(props) {
  // Nous n'avons plus besoin de cela
  // const theme = this.context
  
  return (
    <ThemeContext.Consumer>
      {theme => (
        <div className={`${theme}-image image`}>
          <div className={`${theme}-ball ball`} />
          <Button />
        </div>
      )}
    </ThemeContext.Consumer>
  );
}

// Nous n'avons plus besoin de cela
// Image.contextType = ThemeContext;

export default Image;
```

**Note :** Nous devons également envelopper le composant `<Button />` dans `<ThemeContext.Consumer>` - cela nous permet d'ajouter des fonctionnalités au bouton plus tard.

```js
import React from "react";
import ThemeContext from "./themeContext";

function Button(props) {
  return (
    <ThemeContext.Consumer>
      {context => (
        <button className="button">
          Basculer
          <span role="img" aria-label="soleil">
            ?
          </span>
          <span role="img" aria-label="lune">
            ?
          </span>
        </button>
      )}
    </ThemeContext.Consumer>
  );
}

export default Button;
```

# Extraire le Provider de Contexte

Nous passons actuellement une valeur codée en dur à travers le Provider, cependant, notre objectif est de basculer entre nuit et jour avec notre bouton.

Cela nécessite de déplacer notre Provider vers un fichier séparé et de le mettre dans son propre composant, dans ce cas, appelé `ThemeContextProvider`.

```js
import React, { Component } from "react";
const { Provider, Consumer } = React.createContext();

class ThemeContextProvider extends Component {
  render() {
    return <Provider value={"Day"}>{this.props.children}</Provider>;
  }
}

export { ThemeContextProvider, Consumer as ThemeContextConsumer };
```

**Note :** la propriété value est maintenant gérée dans le nouveau fichier ThemeContext.js, et doit donc être supprimée de index.js.

**Changer le Contexte**

Pour connecter le bouton, nous ajoutons d'abord un état à `ThemeContextProvider` :

```js
import React, { Component } from "react";
const { Provider, Consumer } = React.createContext();

// Note : Vous pourriez également utiliser des hooks pour fournir un état et convertir cela en un composant fonctionnel.
class ThemeContextProvider extends Component {
  state = {
    theme: "Day"
  };
  render() {
    return <Provider value={"Day"}>{this.props.children}</Provider>;
  }
}

export { ThemeContextProvider, Consumer as ThemeContextConsumer };
```

Ensuite, nous ajoutons une méthode pour basculer entre jour et nuit :

```js
toggleTheme = () => {
  this.setState(prevState => {
    return {
      theme: prevState.theme === "Day" ? "Night" : "Day"
    };
  });
};
```

Maintenant, nous changeons notre propriété `value` en `this.state.theme` afin qu'elle retourne les informations de l'état.

```js
 render() {
    return <Provider value={this.state.theme}>{this.props.children}</Provider>;
  }
}
```

Ensuite, nous changeons `value` en un objet contenant `{theme: this.state.theme, toggleTheme: this.toggleTheme}`, et mettons à jour tous les endroits où nous utilisons une seule valeur pour chercher `theme` dans un objet. Cela signifie que chaque `theme` devient `context` et chaque référence à `theme` en tant que valeur devient `context.theme`.

Enfin, nous disons au bouton d'écouter l'événement `onClick` puis de déclencher `context.toggleTheme` - cela met à jour les Consumers qui utilisent l'état du Provider. Le code pour le bouton ressemble à ceci :

```js
import React from "react";
import { ThemeContextConsumer } from "./themeContext";

function Button(props) {
  return (
    <ThemeContextConsumer>
      {context => (
        <button onClick={context.toggleTheme} className="button">
          Basculer
          <span role="img" aria-label="soleil">
            ?
          </span>
          <span role="img" aria-label="lune">
            ?
          </span>
        </button>
      )}
    </ThemeContextConsumer>
  );
}

export default Button;
```

Notre bouton bascule maintenant l'image entre nuit et jour en un clic !

<a href="https://imgflip.com/gif/3evdww"><img src="https://i.imgflip.com/3evdww.gif" title="made at imgflip.com"/></a>

# Avertissements concernant le Contexte

Comme toutes les bonnes choses en code, il y a quelques avertissements à utiliser le Contexte :

- **N'utilisez pas le Contexte pour éviter de passer des props à travers seulement un ou deux niveaux.** Le Contexte est idéal pour gérer l'état nécessaire à de grandes parties d'une application. Cependant, le passage de props est plus rapide si vous passez simplement des informations à travers quelques niveaux.

- **Évitez d'utiliser le Contexte pour sauvegarder l'état qui devrait être conservé localement.** Donc, si vous devez sauvegarder les entrées de formulaire d'un utilisateur, par exemple, utilisez l'état local et non le Contexte.

- **Enveloppez toujours le Provider autour du parent commun le plus bas possible dans l'arbre - pas le composant de plus haut niveau de l'application.** Pas besoin d'en faire trop.

- **Enfin, si vous passez un objet en tant que prop value, surveillez les performances et refactorisez si nécessaire.** Cela ne sera probablement pas nécessaire sauf si une baisse de performance est perceptible.

# Conclusion

Cet exemple est assez simple et il serait probablement plus facile de mettre l'état dans l'application et de le passer via les props. Cependant, il montre espérons-le la puissance d'avoir des Consumers qui peuvent accéder aux données indépendamment des composants au-dessus d'eux dans l'arbre.

Pour en savoir plus sur React Context et d'autres grandes fonctionnalités de React, vous pouvez rejoindre la liste d'attente pour mon [prochain cours avancé sur React.](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=context_article) Ou si vous cherchez quelque chose de plus adapté aux débutants, vous pouvez consulter mon [cours d'introduction gratuit sur React.](https://scrimba.com/g/greact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=context_article)

Bon codage :)