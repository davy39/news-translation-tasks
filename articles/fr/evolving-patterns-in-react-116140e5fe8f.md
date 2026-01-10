---
title: Évolution des motifs dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-04T17:19:41.000Z'
originalURL: https://freecodecamp.org/news/evolving-patterns-in-react-116140e5fe8f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rJr_bOm3mD5V8_C5JaPrsQ.jpeg
tags:
- name: design patterns
  slug: design-patterns
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
seo_title: Évolution des motifs dans React
seo_desc: 'By Alex Moldovan

  Let’s take a closer look at some of the patterns that are emerging in the React
  ecosystem. These patterns improve readability, code clarity, and push your code
  towards composition and reusability.

  I started working with React roughly...'
---

Par Alex Moldovan

Examinons de plus près certains des motifs qui émergent dans l'écosystème React. Ces motifs améliorent la lisibilité, la clarté du code et poussent votre code vers la composition et la réutilisabilité.

J'ai commencé à travailler avec [**React**](https://reactjs.org/) il y a environ 3 ans. À cette époque, il n'y avait pas de pratiques établies à partir desquelles apprendre afin de tirer parti de ses capacités.

Il a fallu environ 2 ans à la communauté pour se rallier autour de quelques idées. Nous sommes passés de `React.createClass` à la classe ES6 et aux composants fonctionnels purs. Nous avons abandonné les mixins et [nous avons simplifié nos APIs](https://reactjs.org/blog/2016/04/07/react-v15.html).

Maintenant que la communauté est plus grande que jamais, nous commençons à voir quelques beaux motifs **évoluer**.

Pour comprendre ces motifs, vous avez besoin d'une compréhension de base des concepts **React** et de son écosystème. Veuillez noter, cependant, que je ne les couvrirai pas dans cet article.

Alors, commençons !

#### Rendu conditionnel

J'ai vu le scénario suivant dans beaucoup de projets.

Lorsque les gens pensent à **React** et **JSX**, ils pensent encore en termes de **HTML** et **JavaScript**.

Donc, l'étape naturelle est de **séparer** la logique conditionnelle du code de retour réel.

```javascript
const condition = true;

const App = () => {
  const innerContent = condition ? (
    <div>
      <h2>Montre-moi</h2>
      <p>Description</p>
    </div>
  ) : null;
  
  return (
    <div>
      <h1>Ceci est toujours visible</h1>
      { innerContent }
    </div>
  );
};
```

Cela tend à devenir ingérable, avec plusieurs [ternaires](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) au début de chaque fonction `render`. Vous devez constamment sauter à l'intérieur de la fonction pour comprendre quand un certain élément est rendu ou non.

En alternative, essayez le motif suivant, où vous bénéficiez du modèle d'exécution du langage.

```javascript
const condition = true;

const App = () => (
  <div>
    <h1>Ceci est toujours visible</h1>
    {
      condition && (
        <div>
          <h2>Montre-moi</h2>
          <p>Description</p>
        </div>
      )
    }
  </div>
);
```

Si `condition` est faux, le deuxième opérande de l'opérateur `&&` n'est pas évalué. Si c'est vrai, le deuxième opérande — **ou le JSX que nous souhaitons rendre** — est retourné.

Cela nous permet de **mélanger** la logique de l'UI avec les éléments de l'UI d'une manière **déclarative** !

Traitez JSX comme s'il faisait partie intégrante de votre code ! Après tout, ce n'est que du **JavaScript**.

#### Transmission des props

Lorsque votre application grandit, vous avez des composants plus petits qui agissent comme des conteneurs pour d'autres composants.

Lorsque cela se produit, vous devez transmettre un bon nombre de props à travers un composant. Le composant n'en a pas besoin, mais ses enfants en ont besoin.

Une bonne façon de contourner cela est d'utiliser la **destructuration des props** avec la **diffusion JSX**, comme vous pouvez le voir ici :

```javascript
const Details = ( { name, language } ) => (
  <div>
    <p>{ name } travaille avec { language }</p>
  </div>
);

const Layout = ( { title, ...props } ) => (
  <div>
    <h1>{ title }</h1>
    <Details { ...props } />
  </div>
);

const App = () => (
  <Layout 
    title="Je suis là pour rester"
    language="JavaScript"
    name="Alex"
  />
);
```

Ainsi, vous pouvez changer les props nécessaires pour `Details` et être sûr que ces props ne sont pas référencées dans plusieurs composants.

#### Destructuration des props

Une application change avec le temps, et il en va de même pour vos composants. Un composant que vous avez écrit il y a deux ans pourrait être stateful, mais maintenant il peut être transformé en un composant stateless. L'inverse arrive aussi très souvent !

Puisque nous avons parlé de la destructuration des props, voici un bon truc que j'utilise pour me faciliter la vie à long terme. Vous pouvez destructurer vos props de manière similaire pour les deux types de composants, comme vous pouvez le voir ci-dessous :

```javascript
const Details = ( { name, language } ) => (
  <div>
    <p>{ name } travaille avec { language }</p>
  </div>
);

class Details extends React.Component {
  render() {
    const { name, language } = this.props;
    return (
      <div>
        <p>{ name } travaille avec { language }</p>
      </div>
    )
  }
}
```

Remarquez que les lignes `2–4` et `11–13` sont **identiques**. La transformation des composants est beaucoup plus facile en utilisant ce motif. De plus, vous limitez l'utilisation de `this` à l'intérieur du composant.

#### Motif du fournisseur

Nous avons examiné un exemple où les props doivent être envoyées à travers un autre composant. Mais que se passe-t-il si vous devez les envoyer à travers 15 composants ?

Entrez [React Context](https://reactjs.org/docs/context.html) !

Ce n'est pas nécessairement la fonctionnalité la plus recommandée de React, mais elle fait le travail quand c'est nécessaire.

Il a été [récemment annoncé](https://twitter.com/acdlite/status/956390180637650944) que le Context obtient une nouvelle API, qui implémente le **motif du fournisseur** dès la sortie de la boîte.

Si vous utilisez des choses comme [React Redux](https://github.com/reactjs/react-redux) ou [Apollo](https://github.com/apollographql/react-apollo), vous êtes peut-être familier avec le motif.

Voir comment cela fonctionne avec l'API d'aujourd'hui vous aidera à comprendre la nouvelle API également. Vous pouvez jouer avec le bac à sable suivant.

%[https://codesandbox.io/s/rww6k3mq94?fontsize=14]

Le composant de niveau supérieur — appelé **Provider** — définit certaines valeurs sur le contexte. Les composants enfants — appelés **Consumers** — récupéreront ces valeurs à partir du contexte.

La syntaxe actuelle du contexte est un peu étrange, mais la version à venir implémente exactement ce motif.

#### Composants d'ordre supérieur

Parlons de réutilisabilité. Avec l'abandon de l'ancienne usine `React.createElement()`, l'équipe React a également abandonné le support des [mixins](https://reactjs.org/blog/2016/07/13/mixins-considered-harmful.html). Ils étaient, à un moment donné, la manière standard de composer des composants par composition d'objets simples.

Les [Composants d'Ordre Supérieur](https://reactjs.org/docs/higher-order-components.html) — HOCs à partir de maintenant — sont sortis pour combler le besoin de réutiliser le comportement à travers plusieurs composants.

Un HOC est une fonction qui prend un composant d'entrée et retourne une version **améliorée/modifiée** de ce composant. Vous trouverez des HOCs sous différents noms, mais j'aime les considérer comme des **décorateurs**.

Si vous utilisez Redux, vous reconnaîtrez que la fonction `connect` est un HOC — elle prend votre composant et y ajoute un tas de _props_.

Implémentons un HOC de base qui peut ajouter des props aux composants existants.

```javascript
const withProps = ( newProps ) => ( WrappedComponent ) => {
  const ModifiedComponent = ( ownProps ) => ( // la version modifiée du composant
    <WrappedComponent { ...ownProps } { ...newProps } /> // props originales + nouvelles props
  );

  return ModifiedComponent;
};

const Details = ( { name, title, language } ) => (
  <div>
    <h1>{ title }</h1>
    <p>{ name } travaille avec { language }</p>
  </div>
);

const newProps = { name: "Alex" }; // ceci est ajouté par le hoc
const ModifiedDetails = withProps( newProps )( Details ); // hoc est curryfié pour la lisibilité

const App = () => (
  <ModifiedDetails 
    title="Je suis là pour rester"
    language="JavaScript"
  />
);
```

Si vous aimez la programmation fonctionnelle, vous allez adorer travailler avec des composants d'ordre supérieur. [Recompose](https://github.com/acdlite/recompose) est un excellent package qui vous donne toutes ces belles utilités HOCs comme `**withProps**`, `**withContext**`, `**lifecycle**`, et ainsi de suite.

Regardons un exemple très utile de **réutilisation de fonctionnalités**.

```javascript
function withAuthentication(WrappedComponent) {
  const ModifiedComponent = (props) => {
    if (!props.isAuthenticated) {
      return <Redirect to="/login" />;
    }

    return (<WrappedComponent { ...props } />);
  };

  const mapStateToProps = (state) => ({
    isAuthenticated: state.session.isAuthenticated
  });

  return connect(mapStateToProps)(ModifiedComponent);
}
```

Vous pouvez utiliser `withAuthentication` lorsque vous souhaitez rendre du contenu sensible à l'intérieur d'une route. Ce contenu ne sera disponible que pour les utilisateurs connectés.

Ceci est une [préoccupation transversale](https://en.wikipedia.org/wiki/Cross-cutting_concern) de votre application implémentée en un seul endroit et réutilisable dans toute l'application.

Cependant, il y a un inconvénient aux HOCs. Chaque HOC introduira un composant React supplémentaire dans votre structure DOM/vDOM. Cela peut entraîner des problèmes de performance potentiels à mesure que votre application se développe.

Certains problèmes supplémentaires avec les HOCs sont résumés dans [cet excellent article](https://cdb.reacttraining.com/use-a-render-prop-50de598f11ce) par [Michael Jackson](https://twitter.com/mjackson). Il prône le remplacement des HOCs par le motif dont nous allons parler ensuite.

#### Props de rendu

Bien qu'il soit vrai que les **props de rendu** et les **HOCs** soient interchangeables, je ne favorise pas l'un par rapport à l'autre. Les deux motifs sont utilisés pour améliorer la réutilisabilité et la clarté du code.

L'idée est que vous **transmettez** le contrôle de votre fonction de rendu à un autre composant qui vous renvoie ensuite le contrôle via une prop de fonction.

Certaines personnes préfèrent utiliser une **prop dynamique** pour cela, d'autres utilisent simplement `**this.props.children**`.

Je sais, c'est encore très confus, mais regardons un exemple simple.

```javascript
class ScrollPosition extends React.Component {
  constructor( ) {
    super( );
    this.state = { position: 0 };
    this.updatePosition = this.updatePosition.bind(this);
  }
  
  componentDidMount( ) {
    window.addEventListener( "scroll", this.updatePosition );
  }

  updatePosition( ) {
    this.setState( { position: window.pageYOffset } )
  }

  render( ) {
    return this.props.children( this.state.position )
  }
}

const App = () => (
  <div>
    <ScrollPosition>
      { ( position ) => (
        <div>
          <h1>Bonjour le monde</h1>
          <p>Vous êtes à { position }</p>
        </div>
      ) }
    </ScrollPosition>
  </div>
);
```

Ici, nous utilisons `children` comme prop de rendu. À l'intérieur du composant `_<ScrollPosition>`, nous enverrons une fonction qui reçoit la position comme paramètre.

Les props de rendu peuvent être utilisées dans des situations où vous avez besoin d'une logique réutilisable **à l'intérieur** du composant et où vous ne souhaitez pas envelopper votre composant dans un HOC.

[React-Motion](https://github.com/chenglou/react-motion) est l'une des bibliothèques qui offrent de bons exemples d'utilisation des props de rendu.

Enfin, regardons comment nous pouvons intégrer des flux **asynchrones** avec les props de rendu. Voici un bon exemple de création d'un composant `Fetch` réutilisable.

Je partage un lien vers un bac à sable afin que vous puissiez jouer avec et voir les résultats.

%[https://codesandbox.io/s/myv3nywvp?fontsize=14]

Vous pouvez avoir **plusieurs** props de rendu pour le même composant. Avec ce motif, vous avez des possibilités infinies de composer et de réutiliser des fonctionnalités.

Quels motifs utilisez-vous ? Lesquels d'entre eux conviendraient à cet article ? Laissez-moi un message ci-dessous ou écrivez vos pensées sur [Twitter](https://twitter.com/alexnmoldovan).

Si vous avez trouvé cet article utile, aidez-moi à le partager avec la communauté !