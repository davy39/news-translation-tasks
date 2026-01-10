---
title: Questions d'entretien sur React – Préparation aux entretiens avec réponses
  et exemples
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-06T21:55:16.000Z'
originalURL: https://freecodecamp.org/news/react-interview-questions-and-answers
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template.jpg
tags:
- name: interview questions
  slug: interview-questions
- name: Interviewing
  slug: interviewing
- name: React
  slug: react
seo_title: Questions d'entretien sur React – Préparation aux entretiens avec réponses
  et exemples
seo_desc: 'React is a JavaScript library for creating user interfaces. It''s used
  in over 30,000 live websites and has over 70,000 GitHub stars.

  According to the 2021 Stack Overflow developer survey, React has surpassed jQuery
  as the most popular web framework, ...'
---

React est une bibliothèque JavaScript pour créer des interfaces utilisateur. Elle est utilisée dans plus de 30 000 sites web actifs et compte plus de 70 000 étoiles sur GitHub.

Selon l'[enquête des développeurs 2021 de Stack Overflow](https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-web-frameworks), React a dépassé jQuery en tant que framework web le plus populaire et détient environ 40,14 % de part de marché. React était également le plus recherché, avec un développeur sur quatre l'utilisant.

Plus de 8 000 leaders de l'industrie, dont LinkedIn, Twitter et AirBnB, utilisent React.

Le salaire annuel moyen d'un développeur React aux États-Unis est de 120 000 $. De nombreuses entreprises utilisent React, ce qui les oblige à rechercher constamment de nouveaux talents.

Dans cet article, nous allons passer en revue quelques bases de React, puis examiner quelques questions d'entretien et leurs réponses appropriées pour vous aider à réussir tout entretien sur React que vous pourriez avoir.

## Qu'est-ce que React ?

React est une bibliothèque JavaScript open-source pour créer des interfaces utilisateur. Elle est déclarative, efficace et flexible, et suit une approche basée sur les composants, ce qui nous permet de créer des composants d'interface utilisateur réutilisables.

Les développeurs utilisent principalement React pour créer des applications monopages (Single Page Applications) et la bibliothèque se concentre uniquement sur la couche de vue du MVC. Elle est également extrêmement rapide.

## Fonctionnalités de React

React possède de nombreuses fonctionnalités qui le distinguent, mais voici quelques points forts :

* React utilise le DOM virtuel au lieu d'un DOM réel/navigateur.

* React utilise une liaison de données unidirectionnelle.

* Il est utilisé pour développer des applications web ainsi que des applications mobiles en utilisant [React Native](https://reactnative.dev/), ce qui nous permet de créer des applications multiplateformes.

## Comment démarrer un nouveau projet dans React

Nous pouvons créer une application React à partir de zéro en initialisant un projet et en installant toutes les dépendances. Mais la manière la plus simple est d'utiliser [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app) via la commande suivante :

```bash
npx create-react-app mon-application
```

**Note :** mon-application est le nom de l'application que nous créons, mais vous pouvez le changer pour n'importe quel nom de votre choix.

Vous pouvez lire plus sur comment [commencer avec React dans cet article](https://www.freecodecamp.org/news/get-started-with-react-for-beginners/).

## Que signifie DOM ?

Le terme « DOM » signifie **D**ocument **O**bject **M**odel et fait référence à la représentation de l'ensemble de l'interface utilisateur d'une application web sous forme de structure de données arborescente.

### Types de DOM

Nous avons deux types de DOM : le DOM virtuel et le DOM réel.

## Avantages et inconvénients de React

Voici quelques avantages et inconvénients de React :

### Avantages de React

1. Il a une courbe d'apprentissage plus courte pour les développeurs JavaScript et un grand nombre de manuels, tutoriels et matériaux de formation sont disponibles grâce à sa communauté active.

2. React est compatible avec les moteurs de recherche.

3. Il facilite la création d'interfaces utilisateur riches et de composants personnalisés.

4. React a un rendu rapide.

5. L'utilisation de JSX nous permet d'écrire du code plus simple, plus attrayant et plus facile à comprendre.

### Inconvénients de React

1. Parce que React est une bibliothèque frontend, d'autres langages et bibliothèques sont nécessaires pour construire une application complète.

2. Il peut être difficile pour les programmeurs inexpérimentés de comprendre parce qu'il utilise JSX.

3. La documentation existante devient rapidement obsolète en raison des cycles de développement courts.

## Qu'est-ce que JSX ?

JavaScript XML est abrégé en JSX. JSX permet et simplifie la création de HTML dans React, ce qui donne un balisage plus lisible et compréhensible.

Par exemple :

```javascript
const App = () => {
  return (
    <div>
       <h1>Bonjour le monde</h1>
    </div>
  )
}
```

Vous pouvez lire plus sur [JSX dans React dans cet article](https://www.freecodecamp.org/news/jsx-in-react-introduction/).

## Pourquoi les navigateurs ne peuvent-ils pas lire JSX ?

JSX n'est pas un code JavaScript valide, et il n'existe aucune implémentation intégrée qui permet au navigateur de le lire et de le comprendre. Nous devons transpiler le code de JSX en code JavaScript valide que le navigateur peut comprendre, et nous utilisons [Babel](https://babeljs.io/), un compilateur/transpileur JavaScript, pour y parvenir.

Note : [create-react-app](https://github.com/facebook/create-react-app) utilise Babel en interne pour la conversion de JSX en JavaScript, mais vous pouvez également configurer votre propre configuration Babel en utilisant Webpack.

Vous pouvez lire plus sur [JSX dans React dans cet article](https://www.freecodecamp.org/news/jsx-in-react-introduction/).

## Qu'est-ce que les composants ?

Un composant est un bloc de code autonome et réutilisable qui divise l'interface utilisateur en plus petits morceaux plutôt que de construire toute l'interface utilisateur dans un seul fichier.

Il existe deux types de composants dans React : les composants fonctionnels et les composants de classe.

### Qu'est-ce qu'un composant de classe ?

Les composants de classe sont des classes ES6 qui retournent du JSX et nécessitent l'utilisation d'extensions React. Parce qu'il n'était pas possible d'utiliser l'état à l'intérieur des composants fonctionnels dans les versions antérieures de React (16.8), les composants fonctionnels n'étaient utilisés que pour le rendu de l'interface utilisateur.

Exemple :

```javascript
import React, { Component } from 'react'
export default class App extends Component {
  render() {
    return (
      <div>
         <h1>Bonjour le monde</h1>
      </div>
    )
  }
}
```

Lisez plus sur les [composants React et les types de composants](https://www.freecodecamp.org/news/react-components-jsx-props-for-beginners/) dans cet article.

### Qu'est-ce qu'un composant fonctionnel ?

Un composant fonctionnel est une fonction JavaScript/ES6 qui retourne un élément React (JSX).

Depuis l'introduction des Hooks React, nous pouvons utiliser des états dans les composants fonctionnels, ce qui a conduit de nombreuses personnes à les adopter en raison de leur syntaxe plus propre.

Exemple :

```javascript
import React from 'react'
const App = () => {
  return (
    <div>
       <h1>Bonjour le monde</h1>
    </div>
  )
}
export default App;
```

Lisez plus sur les [composants React et les types de composants](https://www.freecodecamp.org/news/react-components-jsx-props-for-beginners/) dans cet article.

### Différence entre les composants fonctionnels et les composants de classe

| **Composants fonctionnels** | **Composants de classe** |
| --- | --- |
| Un composant fonctionnel est une fonction JavaScript/ES6 qui prend un argument, props, et retourne du JSX. | Vous devez étendre React pour utiliser un composant de classe. Créez un composant et une fonction render qui retourne un élément React. |
| Il n'y a pas de méthode render utilisée dans les composants fonctionnels. | Il doit avoir la méthode render() retournant du JSX |
| Les composants fonctionnels s'exécutent de haut en bas et ne peuvent pas être maintenus en vie une fois la fonction retournée. | Le composant de classe est instancié, et diverses méthodes de cycle de vie sont maintenues en vie et sont exécutées et invoquées en fonction de la phase du composant de classe. |
| Ils sont également connus sous le nom de composants sans état car ils n'acceptent que des données et les affichent sous une certaine forme, et ils sont principalement responsables du rendu de l'interface utilisateur. | Ils sont également appelés composants avec état car ils implémentent la logique et l'état. |
| Les méthodes de cycle de vie React ne peuvent pas être utilisées dans les composants fonctionnels. | Les méthodes de cycle de vie React peuvent être utilisées à l'intérieur des composants de classe. |
| Des hooks comme useState() ont été créés pour être utilisés dans les composants fonctionnels afin de les rendre avec état. | Il nécessite une syntaxe différente à l'intérieur d'un composant de classe pour implémenter des hooks. |
| Les constructeurs ne sont pas utilisés. | Les constructeurs sont utilisés car ils doivent stocker l'état. |

## Comment utiliser CSS dans React

Il existe 3 façons de styliser une application React avec CSS :

* Styles en ligne

* Stylisation externe

* CSS dans JS

Lisez plus sur [comment styliser une application React dans cet article](https://www.freecodecamp.org/news/how-to-style-react-apps-with-css/).

## À quoi sert render() dans React ?

`render()` est utilisé dans le composant de classe pour retourner le HTML qui sera affiché dans le composant. Il est utilisé pour lire les props et l'état et retourner notre code JSX au composant racine de notre application.

## Qu'est-ce que les Props ?

Les props sont également appelées propriétés. Elles sont utilisées pour transférer des données d'un composant à l'autre (composant parent à composant enfant). Elles sont généralement utilisées pour rendre des données générées dynamiquement.

Note : Un composant enfant ne peut jamais envoyer de props à un composant parent car ce flux est unidirectionnel (parent à enfant).

Exemple :

```javascript
function App({name, hobby}) {
    return (
      <div>
        <h1>Mon nom est {name}.</h1>
        <p>Mon hobby est {hobby}.</p>
      </div>
    );
}

export default App;
```

Lisez plus sur [comment fonctionnent les props dans React ici](https://www.freecodecamp.org/news/how-to-use-props-in-react/).

## Qu'est-ce que l'État dans React ?

L'état est un objet React intégré qui est utilisé pour créer et gérer des données au sein de nos composants. Il diffère des props en ce sens qu'il est utilisé pour stocker des données plutôt que pour transmettre des données.

L'état est mutable (les données peuvent changer) et accessible via `this.state()`.

Exemple :

```javascript
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "John Doe"
    };
  }

  render() {
    return (
      <div>
        <h1>Mon nom est {this.state.name}</h1>
      </div>
    );
  }
}
```

## Comment mettre à jour l'état d'un composant dans React

Il est important de savoir que lorsque nous mettons à jour un état directement, il ne ré-affiche pas le composant – ce qui signifie que nous ne voyons pas la mise à jour.

Si nous voulons qu'il se ré-affiche, alors nous devons utiliser la méthode `setState()` qui met à jour l'objet d'état du composant et ré-affiche le composant.

Exemple :

```javascript
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "John Doe"
    };
  }
  changeName = () => {
    this.setState({name: "Jane Doe"});
  }
  render() {
    return (
      <div>
        <h1>Mon {this.state.name}</h1>
        <button
          type="button"
          onClick={this.changeName}
        >Changer le nom</button>
      </div>
    );
  }
}
```

Vous pouvez en apprendre plus [ici](https://www.freecodecamp.org/news/react-js-for-beginners-props-state-explained/).

## Comment différencier l'État et les Props

L'état et les props sont des objets JavaScript avec des fonctions distinctes.

Les props sont utilisées pour transférer des données du composant parent au composant enfant, tandis que l'état est un stockage de données local qui n'est disponible que pour le composant et ne peut pas être partagé avec d'autres composants.

## Qu'est-ce qu'un Événement dans React ?

Dans React, un événement est une action qui peut être déclenchée par une action de l'utilisateur ou un événement généré par le système. Les clics de souris, le chargement de pages web, la pression de touches, le redimensionnement de fenêtres, les défilements et autres interactions sont des exemples d'événements.

Exemple :

```javascript
// Pour un composant de classe
<button type="button" onClick={this.changeName} >Changer le nom</button>

// Pour un composant fonctionnel
<button type="button" onClick={changeName} >Changer le nom</button>
```

## Comment gérer les Événements dans React

Les événements dans React sont gérés de manière similaire aux éléments DOM. Une différence que nous devons considérer est le nommage de nos événements, qui sont nommés en camelCase plutôt qu'en minuscules.

Exemple :

### Composant de classe

```javascript
class App extends Component {
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    console.log('Ce bouton a été cliqué');
  }
  render() {
    return (
      <div>
         <button onClick={this.handleClick}>Cliquez-moi</button>
      </div>
   );
  }
}
```

### Composant fonctionnel

```javascript
const App = () => {
   const handleClick = () => {
      console.log('Clic détecté');
   };
   return (
      <div>
         <button onClick={handleClick}>Cliquez-moi</button>
      </div>
   );
};
export default App;
```

## Comment passer des paramètres à un gestionnaire d'événements

Dans les composants fonctionnels, nous pouvons faire ceci :

```javascript
const App = () => {
   const handleClick = (name) => {
      console.log(`Mon nom est ${name}`);
   };
   return (
      <div>
         <button onClick={() => handleClick('John Doe')}>Cliquez-moi</button>
      </div>
   );
};
export default App;
```

Et dans les composants de classe, nous pouvons faire ceci :

```javascript
class App extends React.Component {
  call(name) {
    console.log(`Mon nom est ${name}`);
  }
  render() {
    return (
      <button onClick= {this.call.bind(this,"John Doe")}>
        Cliquez sur le bouton !
      </button>
    );
  }
}
export default App;
```

## Qu'est-ce que Redux ?

Redux est une bibliothèque JavaScript open-source populaire pour gérer et centraliser l'état de l'application. Elle est couramment utilisée avec React ou toute autre bibliothèque de vue.

En savoir plus sur [Redux ici](https://www.freecodecamp.org/news/redux-tutorial-for-beginners/#:~:text=Redux%20is%20a%20popular%20open,you%20how%20to%20use%20Redux.).

## Qu'est-ce que les Hooks React ?

Les hooks React ont été ajoutés dans la version 16.8 pour nous permettre d'utiliser l'état et d'autres fonctionnalités de React sans avoir à écrire une classe.

Ils ne fonctionnent pas au sein des classes, mais nous aident plutôt à nous connecter à l'état et aux fonctionnalités du cycle de vie de React à partir de composants fonctionnels.

### Quand avons-nous commencé à utiliser les Hooks dans React ?

L'équipe React a présenté pour la première fois les Hooks React au monde fin octobre 2018, lors de la React Conf, puis début février 2019, avec React v16.8.0.

## Expliquer le Hook useState()

Le Hook useState est un magasin qui permet l'utilisation de variables d'état dans les composants fonctionnels. Vous pouvez passer l'état initial à cette fonction, et elle retournera une variable contenant la valeur actuelle de l'état (pas nécessairement l'état initial) et une autre fonction pour mettre à jour cette valeur.

Exemple :

```javascript
import React, { useState } from 'react';

const App = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      // ...
    </div>
  );
}
```

## Expliquer le Hook useEffect()

Le Hook useEffect vous permet d'effectuer des effets secondaires dans vos composants comme la récupération de données, des mises à jour directes du DOM, des minuteurs comme setTimeout(), et bien plus encore.

Ce hook accepte deux arguments : le callback et les dépendances, qui vous permettent de contrôler quand l'effet secondaire est exécuté.

Note : Le deuxième argument est facultatif.

Exemple :

```javascript
import React, {useState, useEffect} from 'react';

const App = () => {
  const [loading, setLoading] = useState(false);
  
  useEffect(() => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 2000);
  }, []);
  
  return(
    <div>
      // ...
    </div>
  )
}

export default App;
```

## À quoi sert le Hook useMemo() ?

Le hook `useMemo()` est utilisé dans les composants fonctionnels pour mémoriser des fonctions coûteuses afin qu'elles ne soient appelées que lorsqu'un ensemble d'entrées change plutôt qu'à chaque rendu.

Exemple :

```javascript
const result = useMemo(() => expensivesunction(input), [input]);
```

Cela est similaire au hook useCallback, qui est utilisé pour optimiser le comportement de rendu de vos composants fonctionnels React. useMemo est utilisé pour mémoriser des fonctions coûteuses afin qu'elles n'aient pas à être appelées à chaque rendu.

## Qu'est-ce que le Hook useRefs ?

Le hook `useRefs()`, également connu sous le nom de hook References, est utilisé pour stocker des valeurs mutables qui ne nécessitent pas de ré-affichage lorsqu'elles sont mises à jour. Il est également utilisé pour stocker une référence à un élément ou composant React spécifique, ce qui est utile lorsque nous avons besoin de mesures DOM ou pour ajouter directement des méthodes aux composants.

Lorsque nous devons faire ce qui suit, nous utilisons useRefs :

* Ajuster le focus et choisir entre le texte et la lecture multimédia.

* Travailler avec des bibliothèques DOM tierces.

* Initiation d'animations impératives

Exemple :

```javascript
import React, {useEffect, useRef} from 'react';

const App = () => {
  const inputRef = useRef(null)
  
  useEffect(()=>{
    inputElRef.current.focus()
  }, [])
  
  return(
    <div>
      <input type="text" ref={inputRef} />
    </div>
  )
}

export default App;
```

## Qu'est-ce que les Hooks personnalisés ?

Les Hooks personnalisés sont une fonction JavaScript que vous écrivez pour vous permettre de partager la logique entre plusieurs composants, ce qui était auparavant impossible avec les composants React.

Si vous êtes intéressé à apprendre comment cela fonctionne, voici un [guide étape par étape pour vous aider à créer votre propre Hook React personnalisé](https://www.freecodecamp.org/news/how-to-create-react-hooks/).

## Qu'est-ce que le Contexte dans React ?

Le contexte est destiné à partager des données « globales » pour un arbre de composants React en permettant aux données d'être transmises et utilisées (consommées) dans n'importe quel composant dont nous avons besoin dans notre application React sans utiliser de props. Il nous permet de partager des données (état) plus facilement entre nos composants.

Lisez plus sur [React Context dans ce guide](https://www.freecodecamp.org/news/react-context-for-beginners/).

## Qu'est-ce que React Router ?

React Router est une bibliothèque standard utilisée dans les applications React pour gérer le routage et permettre la navigation entre les vues de divers composants.

L'installation de cette bibliothèque dans votre projet React est aussi simple que de taper la commande suivante dans votre terminal :

```bash
npm install --save react-router-dom
```

## Conclusion

Dans ce tutoriel, nous avons passé en revue quelques questions d'entretien sur React pour vous aider à vous préparer à vos entretiens. Toute l'équipe de FreeCodeCamp vous souhaite bonne chance et succès dans votre entretien.

Au lieu d'essayer de suivre plusieurs cours à la fois, trouvez un tutoriel utile et terminez-le si vous voulez en apprendre plus et maîtriser React pour bien performer lors des sessions d'entretien pratiques. Consultez le [Cours gratuit sur React pour 2022](https://www.freecodecamp.org/news/free-react-course-2022/) de freeCodeCamp ou [Apprendre React - Cours complet pour débutants](https://www.freecodecamp.org/news/learn-react-course/).