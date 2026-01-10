---
title: Comment utiliser les composants React – Props, Default Props et PropTypes expliqués
subtitle: ''
author: Casmir Onyekani
co_authors: []
series: null
date: '2023-09-05T22:21:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/React-compo-2-1.jpg
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment utiliser les composants React – Props, Default Props et PropTypes
  expliqués
seo_desc: 'If you''re curious about web development, you''ve probably heard the buzz
  about React.

  React is an open-source JavaScript library used for building user interfaces (UIs)
  in web applications. It has taken the web development world by storm.

  One of the k...'
---

Si vous vous intéressez au développement web, vous avez probablement entendu parler de React.

React est une bibliothèque JavaScript open-source utilisée pour construire des interfaces utilisateur (UI) dans les applications web. Elle a conquis le monde du développement web.

L'un des concepts clés de React est celui des **composants**. Dans ce tutoriel, nous explorerons ce que sont les composants React, comment leur passer et rendre des données en utilisant les props, et comment améliorer leur fiabilité en utilisant les props par défaut et les PropTypes.

## Qu'est-ce que les composants React ?

Imaginez que vous construisez un chef-d'œuvre numérique en LEGO. Chaque brique LEGO individuelle a un but, mais c'est seulement lorsqu'elles sont combinées que quelque chose de vraiment amazing prend forme.

De manière similaire, les composants React sont comme ces briques LEGO. Ils sont les blocs de construction individuels qui s'assemblent pour créer une interface utilisateur complète. Un composant peut être un bouton, un formulaire, un en-tête, ou toute autre partie de la page web à laquelle vous pouvez penser.

Considérez les composants comme des modèles réutilisables que vous pouvez placer dans toute votre application web pour construire une expérience utilisateur complète.

## Pourquoi les composants sont-ils importants dans React ?

Alors, pourquoi les composants sont-ils si importants dans React ? Il y a plusieurs raisons :

### Modularité et réutilisabilité

En décomposant votre interface utilisateur en composants, vous créez une structure modulaire. Cela signifie que vous pouvez développer, tester et maintenir chaque partie de votre application séparément. De plus, une fois que vous avez créé un composant, vous pouvez le réutiliser dans toute votre application, ce qui vous fait gagner du temps et des efforts.

### Efficacité dans le développement

Les composants encouragent un processus de développement plus efficace. Vous pouvez avoir différents membres de l'équipe travaillant sur différents composants simultanément sans se marcher sur les pieds. Cela accélère le processus de développement et encourage la collaboration.

### Maintenabilité

Imaginez que vous devez mettre à jour le style d'un bouton qui apparaît à plusieurs endroits dans votre application. Avec les composants, vous n'avez besoin de mettre à jour le style qu'à un seul endroit, dans le composant du bouton, et il se reflétera automatiquement partout où il est utilisé.

## Types de composants React

Il existe deux principaux types de composants dans React : les composants fonctionnels et les composants de classe.

### Comment utiliser les composants fonctionnels

C'est la manière la plus simple de définir des composants dans React. Ils sont essentiellement des fonctions JavaScript qui prennent des **props** (données d'entrée) et retournent des éléments **JSX** (JavaScript Syntax Extension).

Voici un exemple de code pour vous montrer comment ils fonctionnent :

```jsx
import React from 'react'; // Importe la bibliothèque React.

// Définir un composant fonctionnel nommé "Button"
const Button = () => {
  return (
    <button>
      Cliquez-moi
    </button>
  );
};

export default Button; // Exporte le composant Button pour le rendre accessible.
```

Dans cet exemple, nous avons défini un composant appelé `Button` en utilisant une fonction JavaScript. Ce composant retourne un élément bouton avec le texte "Cliquez-moi".

### Comment utiliser les composants de classe

Ce sont des classes JavaScript qui étendent la classe **React.Component**. Elles utilisent les classes ES6 et fournissent des fonctionnalités plus avancées, telles que la gestion d'état et les méthodes de cycle de vie.

Voici un exemple de code :

```jsx
import React, { Component } from 'react'; // Crée des composants React basés sur des classes.

// Composant de classe
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  render() {
    return (
      <div>
        <p>Compte : {this.state.count}</p>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          Incrémenter
        </button>
      </div>
    );
  }
}

export default Counter; // Exporte le composant Counter pour le rendre accessible.
```

Dans cet exemple, `Counter` est un composant de classe qui maintient un `count` dans son état et le met à jour lorsque le bouton est cliqué.

### Composants fonctionnels vs composants de classe – quand utiliser chacun

En regardant les deux extraits de code ci-dessus, vous pouvez les différencier en fonction de quelques facteurs.

* Syntaxe : les composants fonctionnels sont moins verbeux et plus faciles à lire grâce à leur syntaxe concise. Les composants de classe sont plus verbeux en raison de la structure de classe et de la nécessité de lier les gestionnaires d'événements dans le constructeur.

* État : jusqu'à l'introduction des [hooks](https://www.freecodecamp.org/news/full-guide-to-react-hooks/), les composants fonctionnels ne pouvaient pas contenir d'[état](https://www.freecodecamp.org/news/react-state/#:~:text=In%20our%20React%20app%2C%20once,similarly%20to%20regular%20JavaScript%20functions.). Avec les hooks, vous pouvez maintenant utiliser le hook **useState** pour gérer l'état dans les composants fonctionnels. Les composants de classe peuvent contenir un état en utilisant la propriété `this.state`. Les mises à jour de l'état sont effectuées en utilisant `this.setState()`.

* Cycle de vie : les composants fonctionnels n'ont pas de méthodes de cycle de vie. Des hooks comme **useEffect** peuvent être utilisés pour obtenir des effets similaires. Les composants de classe supportent diverses [méthodes de cycle de vie](https://www.freecodecamp.org/news/react-component-lifecycle-methods/) comme `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`, et ainsi de suite.

* Performance : les composants fonctionnels performant mieux car ils n'ont pas besoin du travail supplémentaire requis pour créer des classes. Les composants de classe peuvent être un peu plus lents en raison du travail supplémentaire requis pour créer des classes.

* Utilisation recommandée : les composants fonctionnels sont préférés pour la plupart des cas d'utilisation dans le développement React moderne en raison de leur simplicité et de leur nature fonctionnelle. Les composants de classe restent pertinents pour des scénarios plus complexes qui nécessitent une gestion d'état et des méthodes de cycle de vie (bien que les hooks aient rendu les composants de classe moins nécessaires).

React évolue continuellement, et de nouveaux modèles et fonctionnalités peuvent émerger. Restez à jour avec la dernière documentation React et les meilleures pratiques.

## Comment passer des données aux composants en utilisant les Props

Les props (propriétés) sont comme des instructions que vous donnez à vos composants. Elles vous permettent de passer des données d'un composant parent à un composant enfant. Ainsi, vous pouvez personnaliser l'apparence et le comportement des composants.

En termes simples, les props sont comme les paramètres que vous passez à une fonction. Vous pouvez utiliser les props pour personnaliser le contenu et le comportement d'un composant en fonction des valeurs que vous fournissez lorsque vous utilisez ou rendez ce composant.

Voici un exemple de code pour vous montrer comment ils fonctionnent :

```jsx
// ParentComponent.js
import React from 'react';
import ChildComponent from './ChildComponent';

const ParentComponent = () => {
  return <ChildComponent name="Cas" />;
};

export default ParentComponent;
```

```jsx
// ChildComponent.js
import React from 'react';

const ChildComponent = (props) => {
  return <p>Bonjour, {props.name} !</p>;
};

export default ChildComponent;
```

Dans cet exemple, le `ParentComponent` passe la prop `name` à `ChildComponent`, qui affiche un message de salutation personnalisé, Bonjour, Cas !.

### Comment rendre avec les props

Le rendu avec les props vous permet de créer des interfaces utilisateur flexibles et interactives en passant et en personnalisant des données dans vos composants. Une fois que vous avez accès aux données dans le composant enfant, vous pouvez les utiliser pour rendre du contenu dynamique dans le JSX du composant. Cela signifie que vous pouvez afficher différents éléments d'interface utilisateur en fonction des valeurs des props.

Dans le `ParentComponent` utilisé ci-dessus, vous pouvez passer différentes valeurs à la prop `name` pour personnaliser le message affiché.

Voici un exemple de code :

```jsx
// ParentComponent.js
import React from 'react';
import ChildComponent from './ChildComponent';

const ParentComponent = () => {
  return (
<div>
<ChildComponent name="Cas" />;
<ChildComponent name="Nuel" />;
<ChildComponent name="Abbey" />;
</div>
)
};

export default ParentComponent;
```

Dans cet exemple, différentes valeurs sont fournies pour la prop `name`. Les messages affichés seront :

* `Bonjour, Cas !`

* `Bonjour, Nuel !`

* `Bonjour, Abbey !`

### Qu'est-ce que le rendu dynamique ?

Le rendu avec les props devient puissant lorsqu'il est combiné avec des expressions JavaScript. Vous pouvez utiliser les props avec d'autres variables, fonctions ou logique pour rendre du contenu dynamique. Cette flexibilité vous permet de créer des interfaces utilisateur polyvalentes et interactives.

Voici un exemple de code pour vous montrer comment cela fonctionne :

```jsx
import React from 'react';

const Product = (props) => {
  return (
    <div>
      <h2>{props.name}</h2>
      <p>Prix : ${props.price}</p>
      {props.isOnSale && <p>En promotion !</p>}
    </div>
  );
};

export default Product;
```

Dans cet exemple, le composant `Product` prend plusieurs props pour rendre les détails d'un produit, y compris son nom, son prix et s'il est en promotion. L'expression `{props.isOnSale && <p>En promotion !</p>}` rend conditionnellement le message "En promotion !" si la prop `isOnSale` est vraie.

### Qu'est-ce que les props par défaut ?

Dans certains cas, vous pourriez vouloir fournir des valeurs par défaut pour les props au cas où elles ne seraient pas explicitement passées. Cela garantit que votre composant ne se casse pas en raison de données manquantes.

Voici un exemple de code :

```jsx
const ChildComponent = (props) => {
  return <p>Bonjour, {props.name} !</p>;
};

ChildComponent.defaultProps = {
  name: "Invité",
};
```

Dans cet exemple, si une valeur n'est pas fournie pour la propriété `name`, elle utilise sa valeur par défaut "Invité".

### Comment utiliser les PropTypes

Pour maintenir l'intégrité de votre application, vous pouvez spécifier les types attendus pour vos props en utilisant PropTypes.

Voici un exemple de code :

```jsx
import PropTypes from 'prop-types';

ChildComponent.propTypes = {
  name: PropTypes.string.isRequired,
};
```

Dans cet exemple, si la chaîne n'est pas fournie pour la valeur de la propriété, elle générera un message d'erreur.

## Conclusion

Comprendre les différences entre les composants fonctionnels et les composants de classe est crucial. Les composants fonctionnels, avec leur syntaxe plus propre et l'utilisation des hooks, sont favorisés pour la plupart des cas d'utilisation. Les composants de classe restent pertinents pour les scénarios complexes nécessitant une gestion d'état et des méthodes de cycle de vie.

Les composants prospèrent grâce au principe de passage de données via les props. Les props sont similaires à des instructions, permettant la personnalisation du contenu et du comportement des composants. La capacité à rendre avec les props permet des interfaces utilisateur dynamiques et personnalisées. Lorsqu'elles sont utilisées en conjonction avec des expressions JavaScript, les props permettent des interfaces utilisateur polyvalentes et interactives.

Les props par défaut et les PropTypes sont des outils supplémentaires qui améliorent la fiabilité des composants. Les props par défaut fournissent des valeurs de repli pour éviter les pannes dues à des données manquantes, tandis que les PropTypes renforcent la validation des types de données, consolidant l'intégrité de l'application.

Alors que React continue d'évoluer, rester à jour avec la dernière documentation et les meilleures pratiques est essentiel. Avec la connaissance des composants, des props, des props par défaut et des PropTypes, vous êtes bien équipé pour commencer votre voyage avec React.

Intéressé à en apprendre davantage sur React ? [React pour les débutants](https://www.freecodecamp.org/news/react-beginner-handbook/#howmuchjavascriptyouneedtoknowtousereact) couvre presque tous les aspects de React. Je le recommande pour une compréhension plus approfondie.

Si vous avez trouvé ce guide utile et agréable, n'hésitez pas à le liker. Pour plus de tutoriels instructifs, suivez-moi sur [X](https://twitter.com/casweb_dev) pour les mises à jour 👍.

Bon codage !