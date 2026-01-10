---
title: 'Comment commencer avec les React Hooks : Formulaires contrôlés'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T17:23:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-react-hooks-controlled-forms-826c99943b92
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0MgGEfZfLO91g1Oa2h3ebQ@2x.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'tech '
  slug: tech
seo_title: 'Comment commencer avec les React Hooks : Formulaires contrôlés'
seo_desc: 'By Kevin Okeh

  React Hooks are a shiny new proposal that will allow you to write 90% cleaner React.
  According to Dan Abramov, Hooks are the future of React.

  That sounds good and all but what are Hooks and how will they help me write better
  code? Glad ...'
---

Par Kevin Okeh

Les React Hooks sont une nouvelle proposition passionnante qui vous permettra d'écrire du React 90 % plus propre. Selon [Dan Abramov](https://overreacted.io/), les [Hooks](https://reactjs.org/docs/hooks-intro.html) sont l'avenir de React.

Cela semble bien et tout, mais qu'est-ce que les Hooks et comment vont-ils m'aider à écrire un meilleur code ? Je suis content que vous ayez posé la question.

Les Hooks vous permettent d'accéder à l'`état` et aux méthodes du cycle de vie dans un composant fonctionnel. Si la phrase précédente vous semble étrange, alors vous devriez rafraîchir votre mémoire de React [ici](https://medium.freecodecamp.org/the-react-handbook-b71c27b0a795#b70b).

L'équipe React dit qu'ils vous aideront à écrire du code propre sans le bagage des composants avec état. Après avoir implémenté un formulaire minimaliste en utilisant les Hooks, je suis d'accord avec eux.

Allons-y et codons d'abord un formulaire simple dans un composant avec état. Nous réécrirons le même formulaire en utilisant les Hooks et vous pourrez décider lequel vous préférez.

### INSTALLATION

Rendez-vous sur [codesandbox.io](https://codesandbox.io/), créez un compte, connectez-vous et créez un nouveau Sandbox. Sélectionnez React lors de la création du Sandbox.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iR8iWv8UppVwLdRFyy5Mtw.png)
_sélectionnez React dans la liste des modèles_

Maintenant, avec le Sandbox ouvert, nous devons nous assurer que nous utilisons une version de React qui prend en charge les Hooks. Cela est dû au fait que les Hooks ne sont accessibles que dans les versions Alpha pour l'instant.

**MISE À JOUR : Les Hooks sont maintenant dans la version publique et stable de React v16.8.**

Regardez l'éditeur de fichiers sur le côté gauche du Sandbox et :

* Cliquez sur 'Dependencies'
* Supprimez à la fois 'react' et 'react-dom'
* Maintenant, cliquez sur 'Add Dependency'
* Tapez 'react' dans la boîte d'entrée et cliquez sur la liste déroulante à droite du premier résultat.
* Sélectionnez la version 16.8.0-alpha.1.
* Maintenant, cliquez sur la description pour l'installer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HrTkGB8k6v-9Yf0NLKxDAw.png)
_assurez-vous de sélectionner la dernière version alpha_

Répétez les mêmes étapes pour 'react-dom' et nous devrions être prêts à partir.

### CODE

Maintenant que nous avons terminé la configuration, il est temps d'écrire du code. Allez dans le Sandbox que vous avez créé, créez un nouveau fichier appelé Form.jsx et collez le code suivant :

```
import React, { Component } from "react";
```

```
class Form extends Component {  constructor(props) {    super(props);
```

```
this.state = {      firstName: "",      lastName: "",      email: "",      password: "",    };
```

```
this.handleInputChange = this.handleInputChange.bind(this);  }
```

```
handleInputChange(event) {    this.setState({      [event.target.name]: event.target.value    });  }
```

```
render() {    const { firstName, lastName, email, password } = this.state;
```

```
return (      <form>        <input          value={firstName}          onChange={this.handleInputChange}          placeholder="Prénom"          type="text"          name="firstName"          required        />        <input          value={lastName}          onChange={this.handleInputChange}          placeholder="Nom de famille"          type="text"          name="lastName"          required        />        <input          value={email}          onChange={this.handleInputChange}          placeholder="Adresse email"          type="email"          name="email"          required        />        <input          value={password}          onChange={this.handleInputChange}          placeholder="Mot de passe"          type="password"          name="password"          required        />
```

```
<button type="submit">Soumettre</button>      </form>    );  }}
```

```
export default Form;
```

Maintenant, ouvrez index.js et remplacez le contenu par le code suivant :

```
import React from "react";import ReactDOM from "react-dom";
```

```
import Form from "./Form.jsx";import "./styles.css";
```

```
function App() {  return (    <div className="App">      <h1>Un formulaire simple en React</h1>      <Form />    </div>  ); }
```

```
const rootElement = document.getElementById("root");
```

```
ReactDOM.render(<App />, rootElement);
```

Testez le formulaire pour voir que tout fonctionne bien. C'était la méthode "old-school" d'implémenter un formulaire contrôlé en React.

Remarquez la quantité de code standard que nous avons dû mettre en place pour l'état et la méthode de mise à jour à chaque changement d'entrée.

Codons le même formulaire en utilisant les React Hooks (enfin !) mais d'abord, supprimez tout le code de Form.jsx et commençons à nouveau.

Commencez par ajouter la ligne suivante en haut du fichier :

```
import React, { useState } from 'react';
```

Il y a donc une méthode non familière importée ici appelée `useState`. Qu'est-ce que c'est et comment l'utilisons-nous ?

Eh bien, `useState` est le React Hook qui nous permettra d'accéder et de manipuler l'`état` dans notre composant. Cela signifie que nous n'aurons pas à `étendre Component` comme le fait notre code précédent.

C'est l'un des plusieurs nouveaux Hooks arrivant dans l'API React pour nous aider à écrire du code plus propre. Maintenant, utilisons-le.

```
import React, { useState } from "react";import "./styles.css";
```

```
function Form() {  const [firstName, setFirstName] = useState("");  const [lastName, setLastName] = useState("");  const [email, setEmail] = useState("");  const [password, setPassword] = useState("");
```

```
return (    <form>      <input        value={firstName}        onChange={e => setFirstName(e.target.value)}        placeholder="Prénom"        type="text"        name="firstName"        required      />      <input        value={lastName}        onChange={e => setLastName(e.target.value)}        placeholder="Nom de famille"        type="text"        name="lastName"        required      />      <input        value={email}        onChange={e => setEmail(e.target.value)}        placeholder="Adresse email"        type="email"        name="email"        required      />      <input        value={password}        onChange={e => setPassword(e.target.value)}        placeholder="Mot de passe"        type="password"        name="password"        required      />
```

```
<button type="submit">Soumettre</button>    </form>  );}
```

```
export default Form;
```

Nous avons créé notre composant fonctionnel, mais il y a du code non familier que je vais expliquer. Plus précisément, les quatre déclarations en haut de notre composant.

Bien que cette partie du code semble étrange au premier abord, elle est simple à comprendre. Nous ne déclarons plus un seul objet appelé `state` qui contient l'état de notre composant. Au lieu de cela, nous divisons maintenant `state` en plusieurs déclarations.

Supposons que nous voulions déclarer une variable d'état appelée `firstName` de la manière familière `extends React.Component`, nous le ferions généralement dans le constructeur et y accéderions en écrivant `this.state.firstName`.

Mais avec `useState`, nous initialisons deux variables appelées `firstName` et `setFirstName`. Nous définissons ensuite leurs valeurs à ce que `useState()` retourne.

Pourquoi devons-nous déclarer `setFirstName` aussi ?

Eh bien, puisque c'est un composant fonctionnel, nous n'avons pas `setState` pour nous aider à modifier la valeur de la variable d'état. Ce que nous avons, c'est `setFirstName` dont le seul but est de mettre à jour `firstName` chaque fois que nous l'appelons.

Donc, lorsque vous voyez :

```
const [firstName, setFirstName] = useState("")
```

Nous déclarons essentiellement une variable d'état et une fonction pour nous permettre de modifier la variable d'état plus tard. La chaîne vide dans l'appel `useState` est la valeur initiale de `firstName` et peut être définie à n'importe quelle valeur requise. Nous allons la définir à une chaîne vide pour l'instant.

Notez que vous pouvez nommer la fonction `setFirstName` comme vous le souhaitez. C'est une convention, cependant, d'ajouter 'set' avant le nom de la variable d'état que nous modifions.

Nous savons maintenant comment créer une variable d'état dans un composant fonctionnel et comment la mettre à jour. Continuons en expliquant le reste du code.

Dans notre première balise input, nous définissons sa valeur à la variable d'état que nous avons déclarée en haut de notre composant. Quant au gestionnaire `onChange`, nous le définissons à une [fonction fléchée](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Functions/Arrow_functions) qui appelle la fonction qui met à jour notre variable d'état pour nous.

Là où nous avions une méthode dans notre précédent composant de classe appelée `handleInputChange`, nous avons maintenant une fonction anonyme qui met à jour notre état pour nous.

Vérifiez que tout fonctionne comme il se doit en essayant de saisir du texte dans votre formulaire. Si tout fonctionne, félicitations, vous venez d'utiliser un React Hook. Si ce n'est pas le cas, alors parcourez à nouveau ce tutoriel et assurez-vous de ne pas sauter d'instructions.

Ajoutez du style comme vous le souhaitez et amusez-vous.

### RÉFLEXIONS

**MISE À JOUR :** Certains d'entre nous peuvent être alarmés à l'idée d'utiliser des fonctions en ligne dans le gestionnaire onClick. J'ai tweeté à Dan Abramov à ce sujet et il a répondu avec [cette partie de la documentation des Hooks](https://reactjs.org/docs/hooks-faq.html#are-hooks-slow-because-of-creating-functions-in-render) qui explique pourquoi l'utilisation de fonctions en ligne avec les Hooks n'est pas une mauvaise chose.

En parcourant notre nouveau code et en le comparant à l'ancien, il est évident comment les React Hooks peuvent nous aider à écrire un meilleur code.

En comparant le composant de classe et le composant fonctionnel côte à côte, il est clair que le composant fonctionnel est plus facile à comprendre, utilise moins de code et semble généralement plus propre.

Si vous aimez les React Hooks, vous pouvez en apprendre plus en explorant la [documentation officielle](https://reactjs.org/docs/hooks-intro.html) et en essayant de réimplémenter certains de vos projets en les utilisant.

Cela dit, j'aimerais avoir vos impressions. Pensez-vous que les Hooks sont l'avenir de React ou pensez-vous qu'ils ne sont que des gadgets inutiles ? Laissez un commentaire ci-dessous.

Cet article est d'abord apparu sur [The Andela Way](https://medium.com/the-andela-way/how-to-get-started-with-react-hooks-controlled-forms-9b47e9fb8c8d).