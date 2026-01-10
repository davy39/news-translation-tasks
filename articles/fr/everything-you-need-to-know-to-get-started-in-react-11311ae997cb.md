---
title: Tout ce que vous devez savoir pour commencer avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-08T19:36:49.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-to-get-started-in-react-11311ae997cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8ErnbNtq1QtnahH2VSCohQ.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Tout ce que vous devez savoir pour commencer avec React
seo_desc: 'By Abdul Moiz Ansari


  “The hardest thing about getting started, is getting started” - Guy Kawasaki


  React is the most popular Front End Library in use today. But getting started on
  React can be hard at times. There is Component Hierarchy, states, pro...'
---

Par Abdul Moiz Ansari

> « La chose la plus difficile pour commencer, c'est de commencer » - Guy Kawasaki

React est la bibliothèque Front End la plus populaire utilisée aujourd'hui. Mais commencer avec React peut parfois être difficile. Il y a la hiérarchie des composants, les états, les props et la programmation fonctionnelle impliqués. Cet article essaie de résoudre ce problème, en vous donnant une méthode simple et facile pour commencer avec React. Alors sans perdre de temps, plongeons-nous.

### Environnement

Nous allons utiliser un simple fichier HTML dans cet article. Assurez-vous simplement d'inclure les balises de script suivantes dans la section head de votre fichier HTML.

```html
<script src="https://unpkg.com/react@16/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.js"></script>
```

Ainsi, notre fichier de travail devrait ressembler à ceci.

```html
<!DOCTYPE html>
<html>
<head>    
    <title>Mon Application React</title>

    <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.js"></script>    
</head>
<body>
    
    <div id="root"></div>

    <script type="text/babel" >   
    
       //Le code React doit aller ici
    </script>
</body>
</html>
</script></body></html>
```

Nous sommes prêts à commencer maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/Dgrr7QYoN3uYtpLisYwkUzzXyuj-oQhyZdNH)
_credits : [https://www.pexels.com](https://www.pexels.com/photo/flight-sky-earth-space-2166/" rel="noopener" target="_blank" title=")_

### Composants

Les composants sont l'essentiel d'une application React.

Ils sont des blocs de code indépendants et réutilisables qui construisent une application React.

Regardons notre premier composant.

```js
class App extends React.Component{
 render(){
  return <h3>Bonjour le monde React.</h3>
 }
}
ReactDOM.render(            
 <App />,
 document.getElementById('root')
);
```

Notre composant App est une classe ES6 qui étend la classe Component de React. Il a une seule méthode pour l'instant appelée `render`, qui retourne un élément **h3** retournant le texte 'Bonjour le monde React'. Le navigateur ne rendra que les éléments retournés par la méthode `render()`.

#### **Mais attendez une minute, cette méthode render est-elle nécessaire ?**

Oui, un composant de classe doit inclure une méthode render. Toutes les autres méthodes sont facultatives.

`ReactDOM.render()` rend le composant App dans un élément div avec l'id 'root'. Il prend le composant comme premier paramètre et le div parent comme second paramètre.

#### Extension de Syntaxe JavaScript (JSX)

L'élément h3 que nous avons déclaré dans le composant App n'est pas du HTML, c'est une extension de syntaxe JavaScript (JSX). JSX est une extension de syntaxe en JavaScript. Il nous permet d'écrire des objets JavaScript similaires à du HTML (JSX) en JavaScript.

```js
class App extends React.Component{
 render(){
  const element = <h3>Bonjour le monde React</h3>;
  return <div>{element}</div>;
 }
}
```

JSX nous donne le pouvoir de JavaScript tout en écrivant du HTML. Ces accolades `{}` dans l'exemple ci-dessus indiquent au compilateur React que **element** est une variable JavaScript. Regardons un autre exemple plus pratique.

```js
render() {
 const users = ['Abdul Moiz','Linda Lee','John Frank'];
 const listItems = users.map(user => <li>{user}</li>);
 return <ul>{listItems}</ul>; 
}
```

Dans l'exemple ci-dessus, nous avons une liste d'utilisateurs dans un tableau que nous avons mappé sur la liste et créé un tableau d'éléments `li`. Nous utiliserons cela dans notre élément `ul` plus tard.

JSX est la méthode recommandée et le standard de facto de l'industrie pour déclarer votre UI dans React.

### Props

Les props sont les propriétés passées par le composant parent aux composants enfants.

C'est un modèle courant dans React d'abstraire la logique UI commune dans les composants enfants. Dans ces cas, il est courant que le composant parent passe certaines données en tant que propriétés dans les composants enfants.

```js
class App extends React.Component {
 render() {
  return <Greet greeting="Bonjour" />;  
 }
}
class Greet extends React.Component{
 render(){
  return <h3>{this.props.greeting} le monde</h3>;
 }
}
```

Dans l'exemple ci-dessus, nous avons passé une prop de salutation au composant Greet et l'avons utilisée dans notre composant App. Nous pouvons accéder à toutes les props à partir de l'objet _this.props_ de notre classe. Dans ce cas, nous accédons à _greeting_ en tant que _this.props.greeting_.

#### **OK, mais quel type de données puis-je passer dans les props ?**

Pratiquement toutes les structures de données par défaut en JavaScript : littéraux de chaîne, nombres, tableau, objets, et même fonctions. Oui, nous pouvons passer des fonctions, mais nous n'allons pas entrer dans cela pour l'instant.

### État

L'état, comme les props, contient également des données, mais de types différents.

Les props contiennent les données envoyées par le composant parent. L'état contient les données privées et dynamiques du composant. L'état contient les données qui changent entre plusieurs rendus du composant.

> Les props sont passées au composant (comme les paramètres de fonction), tandis que l'état est géré au sein du composant (comme les variables déclarées dans une fonction) - Documentation React

Complexe ? Ne vous inquiétez pas, tout cela aura du sens dans un instant.

```js
class App extends React.Component {
 constructor(){
  super();
  this.state = {name :"Abdul Moiz"};
 }
 changeName(){
  this.setState({name : "John Doe"});
 }
 
 render(){
  return (
   <div>
     <h3>Bonjour {this.state.name}</h3>
     <button type='button' onClick=this.changeName.bind(this)}>
      Changer
     </button>
   </div>
  );
 }
}
```

Comme nous pouvons le voir, nous devons initialiser l'état dans un constructeur et ensuite nous pouvons l'utiliser dans la méthode render. Comme les props, nous accédons à l'état avec l'objet 'this.state'. Et lors de l'événement de clic de notre bouton _Changer_, nous changeons la valeur du nom dans l'état en 'John Doe'.

#### **setState()**

Nous utilisons la méthode _setState()_ pour changer notre état. _setState()_ est disponible par défaut dans React Component et est le seul moyen de changer l'état. Nous passons un objet comme paramètre à _setState()_. React regardera l'objet passé et ne changera que les clés fournies de l'état avec les valeurs fournies.

**Mais attendez une minute, si _setState()_ est le seul moyen de changer l'état, cela signifie-t-il que je ne peux pas changer l'état directement ?**

Oui, nous ne pouvons pas changer l'état directement comme ceci :

```
this.state.name = "John Doe";
```

Parce que lorsque nous appelons _setState()_, cela indique à React que les données ont été modifiées et que nous devons re-rendre le composant avec les données mises à jour. La mise à jour de l'état directement n'aura aucun effet sur l'UI.

### Gestionnaires d'événements

Les gestionnaires d'événements dans React ne sont pas très différents des gestionnaires d'événements dans le DOM. Mais ils ont quelques petites différences importantes.

Dans le DOM, les gestionnaires d'événements sont en minuscules, mais dans React, les gestionnaires d'événements sont en camelCase. Deuxièmement, dans le DOM, les gestionnaires d'événements prennent la valeur comme une chaîne, mais dans React, les gestionnaires d'événements prennent la référence de fonction comme valeur.

Voici un exemple de la façon dont nous gérons un événement dans le DOM :

```
<button type="submit" onclick="doSomething()"></button>
```

Et voici comment cela se fait dans React :

```
<button type="submit" onClick=doSomething></button>
```

Si vous remarquez, dans le DOM, nous gérons l'événement de clic en utilisant la propriété DOM `onclick` (minuscules). Alors que dans React, nous utilisons le gestionnaire d'événements `onClick` (camelCase) de React. De plus, nous passons une valeur de chaîne `doSomething()` dans le DOM. Mais dans React, nous passons la référence de la fonction `doSomething` comme valeur.

Si vous souhaitez lire la liste complète des événements fournis par React (comme d'habitude, il y en a des tonnes), envisagez de lire [cet article](https://reactjs.org/docs/events.html#supported-events) de la documentation officielle.

Fatigué ? Moi aussi, mais nous y sommes presque — continuez l'apprentissage !

### Méthodes du Cycle de Vie (Hooks du Cycle de Vie)

React nous donne quelques méthodes spéciales appelées Hooks du Cycle de Vie. Ces hooks du cycle de vie s'exécutent à des moments particuliers dans le cycle de vie d'un composant. Heureusement, nous pouvons mettre notre propre fonctionnalité dans ces hooks du cycle de vie, en les écrasant dans notre composant. Regardons quelques-uns des hooks du cycle de vie couramment utilisés.

#### componentDidMount()

Le montage est le moment où le composant est rendu pour la première fois dans le navigateur. `componentDidMount()` s'exécute après que le composant soit monté. C'est un bon endroit pour récupérer des données ou initier quoi que ce soit.

#### componentDidUpdate()

Comme son nom l'indique, `componentDidUpdate()` s'exécute après que le composant soit mis à jour. C'est l'endroit pour gérer les changements de données. Peut-être voulez-vous gérer certaines requêtes réseau, ou effectuer des calculs basés sur les données modifiées. `componentDidUpdate()` est l'endroit pour faire tout cela.

Regardons cela en action :

```js
class App extends React.Component {
 constructor(){
  super(); 
  this.state = {
   person : {name : "" , city : ""}
  };
 }
 componentDidMount(){
  //faire une requête ajax
  this.setState({
   person : {name : "Abdul Moiz",city : "Karachi"}
  });
 }
 componentDidUpdate(){
  //parce que je n'ai pas pu trouver un exemple plus simple de //componentDidUpdate
  console.log('le composant a été mis à jour',this.state);
 }
 render(){
  return (
   <div>
    <p>Nom : {this.state.person.name}</p>
    <p>Ville : {this.state.person.city}</p>
   </div>
  );
 }
}
```

Notre état initial a deux propriétés, name et city, et toutes deux ont une chaîne vide comme valeur. Dans `componentDidMount()` nous définissons l'état et changeons name en 'Abdul Moiz' et city en 'Karachi'. Parce que nous avons changé l'état, le composant a été mis à jour suite à l'exécution de `componentDidUpdate()`.

### Conclusion

React est là pour rester. Apprendre React peut être difficile, mais vous l'aimerez une fois que vous aurez surmonté la courbe d'apprentissage initiale. Cet article était destiné à rendre ce processus d'apprentissage un peu plus facile pour vous.

Et n'oubliez pas de me suivre sur [Twitter](http://twitter.com/@aamoizansari).

#### Ressources

* [https://reactjs.org/docs](https://reactjs.org/docs/faq-state.html)
* [http://lucybain.com/blog](http://lucybain.com/blog/2016/react-state-vs-pros/)
* [https://thinkster.io](https://thinkster.io)