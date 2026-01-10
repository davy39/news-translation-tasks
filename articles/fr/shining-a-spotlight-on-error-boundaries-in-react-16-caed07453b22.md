---
title: Mise en lumière des Error Boundaries dans React 16
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T16:35:51.000Z'
originalURL: https://freecodecamp.org/news/shining-a-spotlight-on-error-boundaries-in-react-16-caed07453b22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fQhvR9UVrNLee-95ZCNcXQ.jpeg
tags:
- name: coding
  slug: coding
- name: error handling
  slug: error-handling
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Mise en lumière des Error Boundaries dans React 16
seo_desc: 'By Mae Capozzi

  React 16 has better error handling than previous React versions. If an error occurred
  inside of a component, it would “corrupt React’s internal state.” Then, we would
  end up with “cryptic” error messages, or just a blank screen. React ...'
---

Par Mae Capozzi

React 16 bénéficie d'une meilleure gestion des erreurs que les versions précédentes de React. Si une erreur survenait à l'intérieur d'un composant, elle « [corrompait l'état interne de React](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html) ». Nous nous retrouvions alors avec des messages d'erreur « cryptiques » ou simplement un écran blanc. React manquait d'un moyen expressif et éloquent pour gérer ces erreurs.

Cela a changé dans React 16, grâce aux Error Boundaries. [La documentation de React](https://reactjs.org/blog/2017/07/26/error-handling-in-react-16.html) explique leur fonctionnement :

> Les Error Boundaries sont des composants React qui **capturent les erreurs JavaScript n'importe où dans leur arbre de composants enfants, enregistrent ces erreurs et affichent une interface utilisateur de secours** au lieu de l'arbre de composants qui a planté.

J'ai élaboré un scénario de la vie réelle qui peut décrire le fonctionnement des Error Boundaries :

### Un scénario de la vie réelle

Imaginez que vous êtes un parent à la piscine et que vous avez un enfant. La piscine représente l'application, vous représentez un composant Parent, et votre enfant représente un composant Child.

Il y a aussi un maître-nageur, qui représente un composant Error Boundary.

À la piscine, votre enfant saute du plongeoir avec ses amis (n'importe quel tiers comme un utilisateur, une bibliothèque ou une requête HTTP).

![Image](https://cdn-media-1.freecodecamp.org/images/NthYEZyaGRw2rAq36wM61oVrC6zLMeeP2Nkx)

Vous êtes en train de bronzer quand votre enfant tombe du plongeoir et se blesse à la jambe.

Sans maître-nageur, vous ne sauriez jamais ce qui a causé la chute de votre enfant. Est-ce que ses amis l'ont poussée ? Le plongeoir était-il glissant ? A-t-elle soudainement perdu connaissance ?

Comme nous sommes dans React 16, le maître-nageur a tout surveillé. Après avoir secouru votre enfant, le maître-nageur peut vous dire exactement ce qui s'est passé. Dans ce cas, son ami l'a poussée du plongeoir.

Maintenant, il est facile de dire ce qui a réellement causé l'erreur. L'établissement propriétaire de la piscine (le développeur) peut désormais facilement atténuer les risques futurs en s'assurant qu'une seule personne se tient sur le plongeoir à la fois.

### Étape 1 : Lancer une application React avec create-react-app

Nous allons commencer par lancer une application React en utilisant create-react-app. Si vous ne l'avez jamais fait auparavant, j'ai rédigé un [aide-mémoire](https://gist.github.com/maecapozzi/41e249c24e683647babf451c675b22c8) que vous pouvez suivre. Si vous avez besoin d'un peu plus de conseils, vous pouvez suivre les instructions du [Tutoriel : Comment faire des requêtes HTTP dans React, Partie 1.](https://hackernoon.com/tutorial-how-to-make-http-requests-in-react-part-1-f7afa3cd0cc8)

Une fois que vous avez configuré votre application et que vous savez qu'elle fonctionne localement, nous pouvons commencer le codage proprement dit.

### Étape 2 : Commencer à construire les composants

J'ai supprimé une grande partie du code passe-partout inclus dans `create-react-app`, donc mon fichier `App.js` ressemble à ceci :

```
import React, { Component } from 'react'import './App.css'
```

```
class App extends Component {  render () {    return (      <div className='App'>              <h1>Hello World</h1>      </div>        )  }}
```

```
export default App
```

N'hésitez pas à copier/coller mon code dans votre fichier `App.js`, afin que nous puissions nous assurer que nous sommes sur la même longueur d'onde ! Lorsque vous vérifiez dans votre navigateur, vous devriez voir « Hello World » en grosses lettres.

Créez un nouveau fichier nommé `Parent.js` et copiez/collez ce code dans ce fichier :

```
import React from 'react'import Child from './Child'
```

```
const Parent = () => (  <div>    <h1>Parent</h1>    <Child />  </div>)
```

```
export default Parent
```

Ensuite, créez un autre fichier nommé `Child.js` et copiez/collez ce code dans **ce** fichier :

```
import React, { Component } from 'react'
```

```
class Child extends Component {  constructor () {    super()  }
```

```
  render () {    return (      <div>        <h3>Child</h3>      </div>    )  }}
```

```
export default Child
```

Normalement, si je construisais un composant comme celui-ci, j'utiliserais un composant fonctionnel sans état. La seule raison pour laquelle je ne le fais pas est que je veux lever une erreur dans mon constructeur à des fins d'exemple.

Maintenant, importons le composant `Parent` dans le fichier `App.js` et affichons-le sur la page. Votre fichier `App.js` ressemblera à ceci :

```
import React, { Component } from 'react'import Parent from './Parent'
```

```
import './App.css'
```

```
class App extends Component {  render () {    return (      <div className='App'>        <Parent />      </div>    )  }}
```

```
export default App
```

Sur votre écran, vous devriez voir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/pIuDTagXiJleGofowvb-V9cv1UcHk03QnUfM)

### Étape 3 : Déclencher une erreur dans le composant Child

Maintenant, je vais lever une erreur dans le constructeur de notre composant `Child` afin que nous puissions voir ce qui se passe lorsque nous obtenons ce genre d'erreur sans utiliser les Error Boundaries.

Dans `Child.js`, ajoutez `throw new Error('This is an error')` à votre fonction `constructor`.

```
constructor () {  super()   throw new Error('This is an error')}
```

Si nous rafraîchissons notre page, nous verrons un message d'erreur comme celui-ci en développement :

![Image](https://cdn-media-1.freecodecamp.org/images/-DdczflKjbNCKMDkesEj5AR3gpDJIn-KO3LM)

Si nous supprimons l'erreur en cliquant sur le « x » dans le coin supérieur droit, tout ce que nous voyons est un écran blanc !

### Étape 4 : Construire un composant Error Boundary

Voici un exemple de composant Error Boundary :

```
import React, { Component } from 'react'  class ErrorBoundary extends Component {  constructor (props) {    super(props)    this.state = { hasError: false }  }
```

```
  componentDidCatch (error, info) {    this.setState({ hasError: true })  }
```

```
  render () {    if (this.state.hasError) {      return <h1>Something went wrong.</h1>    }
```

```
    return this.props.children  }}
```

```
export default ErrorBoundary
```

Voyons comment ce composant fonctionne :

1. Dans le constructeur, j'ai défini un attribut sur l'état (`state`) appelé `hasError`. Je l'ai initialisé à `false`.
2. J'utilise la méthode de cycle de vie `componentDidCatch`, qui peut prendre deux arguments, `error` et `info`. 
Si `componentDidCatch` est déclenché, je règle l'état de `hasError` sur `true`.
3. Dans la méthode `render`, j'indique que `si hasError` est `true`, on informe l'utilisateur que « **Quelque chose s'est mal passé** ».
`Sinon`, on continue de fonctionner comme d'habitude.

### 4. Configurer l'Error Boundary

Enfin, nous devons placer l'Error Boundary autour du composant qui déclenche l'erreur.

Dans ce cas, c'est le composant `Child` qui déclenche l'erreur, nous devons donc placer la limite autour de lui, à l'intérieur du composant `Parent`.

```
import React from 'react'import Child from './Child'import ErrorBoundary from './ErrorBoundary'
```

```
const Parent = props => (  <div>    <h1>Parent</h1>    <ErrorBoundary>      <Child />    </ErrorBoundary>  </div>)
```

```
export default Parent
```

Maintenant, si nous rafraîchissons la page, nous verrons cette erreur en développement, comme auparavant :

![Image](https://cdn-media-1.freecodecamp.org/images/Yd88gvxtLedqaMLNzDcpEZwevQkOhwpML3td)

La différence est que si nous fermons l'erreur, nous voyons ceci sur la page à la place :

![Image](https://cdn-media-1.freecodecamp.org/images/fC8w6endl647qpQrgcBmg40CNOGvyVoZ57hF)

C'est bien mieux qu'un simple écran blanc !

N'hésitez pas à me poser vos questions dans la section des commentaires ci-dessous.

? **_Si vous avez aimé cet article,_** **_assurez-vous de me f[ollow sur Medium,](https://medium.com/@MCapoz) me f[ollow sur Twitter,](https://twitter.com/MCapoz) et de me soutenir sur P[atreon !](https://www.patreon.com/maecapozzi)?_**