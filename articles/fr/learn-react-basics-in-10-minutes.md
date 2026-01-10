---
title: Apprendre les bases de React en 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-18T01:26:43.000Z'
originalURL: https://freecodecamp.org/news/learn-react-basics-in-10-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/intro-to-react.jpg
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: 'State Management '
  slug: state-management
seo_title: Apprendre les bases de React en 10 minutes
seo_desc: 'By Joe Liang

  If you want to learn the basics of React in the time it takes you to drink a cup
  of coffee, this post is for you.

  This article aims to provide a beginner-friendly introduction to React, what it
  is, and why we need it. It assumes you have...'
---

Par Joe Liang

Si vous voulez apprendre les bases de React dans le temps qu'il vous faut pour boire une tasse de café, cet article est pour vous.

Cet article vise à fournir une introduction conviviale pour les débutants à React, ce qu'il est et pourquoi nous en avons besoin. Il suppose que vous avez une certaine compréhension du [JavaScript de base](https://1000mileworld.com/learn-javascript-6-golden-knowledge-nuggets-for-beginners/).

Nous allons discuter de certains de ses concepts de base et passer en revue ce que vous pouvez construire avec React.

Nous allons également discuter de certains codes, mais l'objectif global est d'acquérir une compréhension intuitive de ce qu'est React afin que vous soyez à l'aise avec les bases.

<h2>Qu'est-ce que React ?</h2>

Développé par Facebook en 2011, React est rapidement devenu l'une des bibliothèques JavaScript les plus largement utilisées. Selon [HackerRank](https://research.hackerrank.com/developer-skills/2018/), 30 % des employeurs recherchent des développeurs qui connaissent React, mais seulement environ la moitié des candidats possèdent réellement les connaissances requises.

Clairement, React est très demandé sur le marché de l'emploi.

Alors, qu'est-ce que React exactement ?

React est une bibliothèque JavaScript efficace et flexible pour construire des interfaces utilisateur (et React lui-même est écrit en utilisant JavaScript). Il décompose les interfaces utilisateur complexes en petits morceaux de code isolés appelés « composants ». En utilisant ces composants, React ne se préoccupe que de ce que vous voyez sur la page d'accueil d'un site web.

![Composants React](https://www.freecodecamp.org/news/content/images/2020/03/React-components.png)
_Une application de calculatrice qui peut être divisée en composants React._

Les composants sont indépendants et réutilisables. Ils peuvent être soit des fonctions JavaScript, soit des classes. Dans les deux cas, ils retournent un morceau de code qui représente une partie d'une page web.

Voici un exemple de composant fonctionnel qui rend un élément `<h2>` sur la page :

```js
function Name() {
  return <h2>Salut, je m'appelle Joe !</h2>;
}
```

Et voici un composant de classe faisant le même rendu :

```js
class Person extends React.Component {
  render() {
    return <h2>Salut à nouveau de Joe !</h2>;
  }
}
```

L'utilisation d'un composant de classe demande un peu plus d'effort dans le sens où vous devez étendre React.Component (une partie de la bibliothèque React) tandis qu'un composant fonctionnel est principalement du JavaScript simple. Cependant, les composants de classe fournissent certaines fonctionnalités critiques que les composants fonctionnels n'ont pas (voir [Composants fonctionnels vs composants de classe dans React](https://medium.com/@Zwenza/functional-vs-class-components-in-react-231e3fbd7108)).

Vous avez peut-être remarqué qu'il y a un étrange mélange de HTML et de JavaScript à l'intérieur de chaque composant. React utilise en fait un langage appelé JSX qui permet de mélanger HTML avec JavaScript.

Non seulement vous pouvez utiliser JSX pour retourner des éléments HTML prédéfinis, mais vous pouvez également créer les vôtres. Par exemple, au lieu de rendre des éléments `<h2>` directement dans le composant de classe, vous pouvez rendre le composant fonctionnel qui retourne la même chose :

```js
class Person extends React.Component {
  render() {
    return <Name />;
  }
}
```

Notez la fermeture automatique `/>` du composant.

La puissance de React commence à devenir plus évidente lorsque vous pouvez imaginer rendre de nombreux composants simples pour en former un plus complexe.

Pour construire une page, nous pouvons appeler ces composants dans un certain ordre, utiliser les résultats qu'ils retournent et les afficher à l'utilisateur.

<h2>Pourquoi choisir React plutôt que JavaScript Vanilla ?</h2>

Pouvoir décomposer des interfaces utilisateur complexes grâce à l'utilisation de composants donne à React un avantage sur JavaScript Vanilla (JS simple sans aucune bibliothèque ou framework externe). Mais que peut faire d'autre React qui le place en si forte demande parmi les employeurs ?

Examinons les différences entre la manière dont React et Vanilla JS gèrent les choses.

Dans la section précédente, nous avons discuté de la manière dont React utilise des composants pour rendre les interfaces utilisateur. Nous n'avons pas approfondi ce qui se passait du côté HTML des choses. Il peut être surprenant d'apprendre que le code HTML qui s'associe à React est vraiment simple :

```html
<div id="root"></div>
```

Il s'agit généralement d'un élément `<div>` avec un identifiant qui sert de conteneur pour une application React. Lorsque React rend ses composants, il recherchera cet identifiant pour effectuer le rendu. La page est vide avant ce rendu.

Vanilla JS, en revanche, définit l'interface utilisateur initiale directement dans le HTML.

De plus, Vanilla JS gère la fonctionnalité tandis que HTML gère l'affichage du contenu (balisage).

Dans les premiers jours du web, la séparation de la fonctionnalité et du balisage semblait logique car les applications étaient plus simples. Cependant, à mesure que la complexité augmentait, les maux de tête liés à la maintenance de grands morceaux de code JS augmentaient également.

Le code JS qui met à jour un morceau de HTML peut être réparti sur plusieurs fichiers, et les développeurs peuvent avoir du mal à suivre l'origine du code. Ils doivent garder les choses claires dans leur tête de toutes les interactions entre le code qui réside dans différents fichiers.

React trie le code en composants, où chaque composant maintient tout le code nécessaire à la fois pour afficher et mettre à jour l'interface utilisateur.

La mise à jour de l'interface utilisateur nécessite la mise à jour du DOM, ou modèle d'objet de document (voir [Manipulation du DOM en utilisant JavaScript](https://1000mileworld.com/dom-manipulation-using-javascript/)). C'est là que React brille vraiment.

Si vous voulez accéder au DOM en Vanilla JS, vous devez d'abord le trouver avant de pouvoir l'utiliser. React stocke les données dans des variables JS régulières et maintient son propre DOM _virtuel_.

Si vous voulez ensuite mettre à jour le DOM en Vanilla JS, vous devez localiser le nœud approprié et ensuite ajouter ou supprimer manuellement des éléments. React met automatiquement à jour l'interface utilisateur en fonction de l'état de l'application, que nous allons discuter plus en détail dans la section suivante.

Ainsi, la raison principale pour laquelle nous pourrions vouloir utiliser React plutôt que Vanilla JS peut être résumée en un mot : simplicité.

Avec Vanilla JS, il est facile de se perdre dans un labyrinthe de recherches et de mises à jour du DOM. React vous oblige à décomposer votre application en composants, ce qui produit un code plus maintenable.

Ainsi, pour les applications complexes, vous voudrez définitivement apprendre React.

<h2>Concepts de base de React</h2>

Nous avons déjà discuté de la manière dont React utilise des composants pour décomposer des interfaces utilisateur complexes et JSX pour rendre ces composants.

Dans cette section, nous allons parler de quelques concepts plus fondamentaux de React.

<h3>État</h3>

Comme mentionné précédemment, React met à jour l'interface utilisateur en fonction de l'état de l'application. Cet état est en fait stocké comme une propriété d'un composant de classe React :

```js
class Counter extends React.Component {
  state = {
    value: 0
  };
}
```

Supposons que nous avons un compteur et 2 boutons qui soit incrémentent, soit décrémentent. La valeur du compteur est rendue sur la page via JSX.

La valeur du compteur affichée est basée sur l'état et nous changeons l'état en cliquant sur l'un des boutons. Vanilla JS traite un clic de bouton comme un événement et React aussi. Lorsqu'un tel événement se produit, nous allons appeler des fonctions qui soit incrémentent, soit décrémentent le compteur en fonction du bouton cliqué. Ces fonctions contiennent le code qui change l'état du composant.

Voici un exemple d'un tel compteur :

```js
class Counter extends React.Component {
  state = {
    value: 0
  };

  handleIncrement = () => {
    this.setState(state => ({
      value: state.value + 1
    }));
  };

  handleDecrement = () => {
    this.setState(state => ({
      value: state.value - 1
    }));
  };

  render() {
    return (
      <div>
        <h2>{this.state.value}</h2>
        <button onClick={this.handleDecrement}>Décrémenter</button>
        <button onClick={this.handleIncrement}>Incrémenter</button>
      </div>
    );
  }
}
```

Nous avons mis à jour l'état en appelant `setState` dans chacune des fonctions gérant un clic de bouton. Le compteur affiché sur la page sera mis à jour en temps réel. Ainsi, React tire son nom du fait qu'il _réagit_ aux changements d'état.

En bref, React surveille automatiquement chaque état de composant pour les changements et met à jour le DOM de manière appropriée.

<h3>Props</h3>

Nous pouvons utiliser les props (abréviation de "propriétés") pour permettre aux composants de communiquer entre eux.

Supposons que le compteur dans notre exemple précédent représente la quantité d'un produit qu'un client souhaite acheter. Le magasin veut limiter à 2 produits achetés par client. À la caisse, nous voulons afficher un message approprié si le client essaie d'acheter plus de 2.

Voici comment nous pourrions le faire avec les props :

```js
const Display = (props) => {
   let message;
   if(props.number > 2){
	message = 'Vous êtes limité à l'achat de 2 maximum !';
   }else{
	message = 'Tout va bien.';
   }
   return(
	<p>{message}</p>
   );
};

class Timer extends React.Component {
   state = {
	quantity: 0
   }
   //...code pour gérer les clics de bouton, mettre à jour l'état, etc.
    render(){
        return(
          <Display number={this.state.quantity} />
          //...code pour d'autres composants
       );
    }
};
```

Nous créons un composant fonctionnel appelé `Display` et passons les props comme paramètre. Lorsque nous rendons ce composant, nous lui passons le nombre comme attribut défini sur la quantité du produit qu'un client veut acheter. Cela ressemble à la définition d'un attribut d'une balise HTML. Nous appelons cette valeur avec `props.number` dans `Display` pour déterminer quel message retourner.

<h3>Cycle de vie des composants</h3>

Alors que React met à jour le DOM en fonction des états des composants, des méthodes spéciales appelées méthodes de cycle de vie existent pour fournir des opportunités d'effectuer des actions à des points spécifiques dans le cycle de vie d'un composant.

Elles vous permettent de capturer les composants à un certain moment pour appeler des fonctions appropriées. Ces moments peuvent être avant que les composants soient rendus, après qu'ils soient mis à jour, etc. Vous pourriez vouloir explorer les [méthodes de cycle de vie d'un composant](https://www.freecodecamp.org/news/how-to-understand-a-components-lifecycle-methods-in-reactjs-e1a609840630/).

Pour voir les méthodes de cycle de vie en action, vous pouvez consulter cette [Horloge Pomodoro](https://codepen.io/1000mileworld/full/qBEwRvK) que j'ai créée.

Le minuteur de la session est initialement défini sur la durée de la session. Lorsque le minuteur de la session atteint zéro, le minuteur doit passer à la durée de la pause et commencer à compter à partir de là.

Puisque le minuteur est un composant, j'ai utilisé la méthode de cycle de vie `componentDidUpdate` dans ma classe principale pour gérer les changements avec `handleChange()` :

```js
componentDidUpdate() {
    this.handleChange();
}
```

Vous pouvez penser aux méthodes de cycle de vie comme ajoutant des écouteurs d'événements en Vanilla JS à un composant React.

<h2>Que pouvez-vous construire avec React ?</h2>

Maintenant que vous avez une compréhension de base de React, que pouvez-vous construire avec ?

Nous avons déjà mentionné au début de cet article que Facebook a développé React en 2011, donc naturellement la plateforme Facebook est basée sur React. D'autres applications célèbres qui utilisent complètement ou partiellement React incluent Instagram, Netflix et Whatsapp.

Mais en tant que débutants avec React, nous ne cherchons pas à construire immédiatement le prochain Facebook, donc voici une liste de [10 idées de projets de démarrage React pour vous faire coder](https://medium.com/@dtkatz/10-react-starter-project-ideas-to-get-you-coding-5b35782e1831).

Si vous voulez en savoir plus sur le développement web et consulter quelques exemples de projets React conviviaux pour les débutants, visitez mon blog à [1000 Mile World](https://www.1000mileworld.com/).

Merci d'avoir lu et bon codage !