---
title: La meilleure façon de lier les gestionnaires d'événements dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-08T15:52:39.000Z'
originalURL: https://freecodecamp.org/news/the-best-way-to-bind-event-handlers-in-react-282db2cf1530
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2dTkg7JieJTEhRasDst0-A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: La meilleure façon de lier les gestionnaires d'événements dans React
seo_desc: 'By Charlee Li

  Binding event handlers in React can be tricky (you have JavaScript to thank for
  that). For those who know the history of Perl and Python, TMTOWTDI (There’s More
  Than One Way To Do It) and TOOWTDI (There’s Only One Way To Do It) should b...'
---

Par Charlee Li

Lier les gestionnaires d'événements dans React peut être délicat (vous pouvez remercier JavaScript pour cela). Pour ceux qui connaissent l'histoire de Perl et Python, TMTOWTDI (There’s More Than One Way To Do It) et TOOWTDI (There’s Only One Way To Do It) devraient être des termes familiers. Malheureusement, au moins pour la liaison d'événements, JavaScript est une langue TMTOWTDI, ce qui confond toujours les développeurs.

Dans cet article, nous allons explorer les méthodes courantes de création de liaisons d'événements dans React, et je vous montrerai leurs avantages et inconvénients. Et surtout, je vous aiderai à trouver la "Seule Façon" — ou du moins, ma préférée.

Cet article suppose que vous comprenez la nécessité de la liaison, comme pourquoi nous devons faire `this.handler.bind(this)`, ou la différence entre `function() { console.log(this); }` et `() => { console.log(this); }`. Si vous êtes confus à propos de ces questions, Saurabh Misra a écrit un article amazing expliquant cela.

### Liaison dynamique dans render()

Le premier cas couramment utilisé est d'appeler `.bind(this)` dans la fonction `render()`. Par exemple :

```
class HelloWorld extends Component {  handleClick(event) {}  render() {    return (      <p>Bonjour, {this.state.name} !</p>      <button onClick={this.handleClick.bind(this)}>Cliquez</button>    );  }}
```

Bien sûr, cela fonctionnera. Mais réfléchissez à une chose : que se passe-t-il si `this.state.name` change ?

Vous pourriez dire que changer `this.state.name` provoquera un nouveau `render()` du composant. Bien. Le composant se rendra pour mettre à jour la partie du nom. Mais le bouton sera-t-il rendu à nouveau ?

Considérez le fait que React utilise le Virtual DOM. Lorsque le rendu se produit, il comparera le Virtual DOM mis à jour avec le Virtual DOM précédent, puis ne mettra à jour que les éléments modifiés dans l'arbre DOM réel.

Dans notre cas, lorsque `render()` est appelé, `this.handleClick.bind(this)` sera également appelé pour lier le gestionnaire. Cet appel générera un **tout nouveau gestionnaire**, qui est complètement différent du gestionnaire utilisé lorsque `render()` a été appelé pour la première fois !

![Image](https://cdn-media-1.freecodecamp.org/images/u0GzKJdrXoomFQqomNjOV3UecQV8tHrTj9UM)
_Virtual DOM pour la liaison dynamique. Les éléments en bleu seront re-rendus._

Comme dans le diagramme ci-dessus, lorsque `render()` a été appelé précédemment, `this.handleClick.bind(this)` a retourné `funcA` afin que React sache que `onChange` était `funcA`.

Plus tard, lorsque `render()` est appelé à nouveau, `this.handleClick.bind(this)` a retourné `funcB` (notez qu'il retourne une nouvelle fonction à chaque appel). De cette manière, React sait que `onChange` n'est plus `funcA`, ce qui signifie que le `button` doit être re-rendu.

Un bouton peut ne pas poser de problème. Mais que se passe-t-il si vous avez 100 boutons rendus dans une liste ?

```
render() {  return (    {this.state.buttons.map(btn => (      <button key={btn.id} onChange={this.handleClick.bind(this)}>        {btn.label}      </button>    ))}  );}
```

Dans l'exemple ci-dessus, tout changement d'étiquette de bouton entraînera le re-rendu de tous les boutons, car tous les boutons généreront un nouveau gestionnaire `onChange`.

### Liaison dans le constructeur()

Une méthode ancienne consiste à faire la liaison dans le constructeur. Rien de compliqué :

```
class HelloWorld extends Component {  constructor() {    this.handleClick = this.handleClickFunc.bind(this);  }  render() {    return (<button onClick={this.handleClick}/>);  }}
```

Cette méthode est bien meilleure que la précédente. Appeler `render()` ne générera pas un nouveau gestionnaire pour `onClick`, donc le `<button>` ne sera pas re-rendu tant que le bouton ne change pas.

![Image](https://cdn-media-1.freecodecamp.org/images/iTs98nwnYdvxE2fFoO5N1Rzcg-u-cD7LL9g1)
_Virtual DOM pour la liaison dans le constructeur. Les éléments en bleu seront re-rendus._

### Liaison avec la fonction fléchée

Avec les propriétés de classe ES7 (actuellement supportées avec [Babel](https://babeljs.io/docs/plugins/transform-class-properties/)), nous pouvons faire des liaisons au niveau de la définition de la méthode :

```
class HelloWorld extends Component {  handleClick = (event) => {    console.log(this.state.name);  }  render() {    return (<button onClick={this.handleClick}/>)  }}
```

Dans le code ci-dessus, `handleClick` est une affectation qui est équivalente à :

```
constructor() {  this.handleClick = (event) => { ... }；}
```

Ainsi, une fois le composant initialisé, `this.handleClick` ne changera plus jamais. De cette manière, cela garantit que `<button>` ne sera pas re-rendu. Cette approche est probablement la meilleure façon de faire des liaisons. Elle est simple, facile à lire, et surtout, elle fonctionne.

### Liaison dynamique avec la fonction fléchée pour plusieurs éléments

En utilisant le même truc de fonction fléchée, nous pouvons utiliser le même gestionnaire pour plusieurs entrées :

```
class HelloWorld extends Component {  handleChange = name => event => {    this.setState({ [name]: event.target.value });  }  render() {    return (      <input onChange={this.handleChange('name')}/>      <input onChange={this.handleChange('description')}/>    )  }}
```

À première vue, cela semble assez amazing grâce à sa simplicité. Cependant, si vous réfléchissez bien, vous constaterez qu'il a le même problème que la première approche : chaque fois que `render()` est appelé, les deux `<input>` seront re-rendus.

En effet, je pense que cette approche est intelligente, et je ne veux pas non plus écrire plusieurs `handleXXXChange` pour chaque champ. Heureusement, ce type de "gestionnaire multi-usage" est moins susceptible d'apparaître à l'intérieur d'une liste. Cela signifie qu'il n'y aura que quelques composants `<input>` qui seront re-rendus, et il n'y aura probablement pas de problème de performance.

Quoi qu'il en soit, les avantages qu'il nous apporte sont bien plus grands que la perte de performance. Par conséquent, je vous suggérerais d'utiliser directement cette approche.

Au cas où ces problèmes de performance deviendraient significatifs, je suggérerais de mettre en cache les gestionnaires lors de la liaison (mais cela rendra le code moins lisible) :

```
class HelloWorld extends Component {  handleChange = name => {    if (!this.handlers[name]) {      this.handlers[name] = event => {        this.setState({ [name]: event.target.value });      };    }    return this.handlers[name];    }   render() {    return (      <input onChange={this.handleChange('name')}/>      <input onChange={this.handleChange('description')}/>    )  }}
```

### Conclusion

Lorsque vous faites des liaisons d'événements dans React, vous devez vérifier très soigneusement si les gestionnaires sont générés dynamiquement. Habituellement, ce n'est pas un problème lorsque les composants affectés n'apparaissent qu'une ou deux fois. Mais lorsque les gestionnaires d'événements apparaissent dans une liste, cela peut entraîner de graves problèmes de performance.

#### Solutions

* Utilisez la liaison avec les fonctions fléchées chaque fois que possible
* Si vous devez générer des liaisons dynamiquement, envisagez de mettre en cache les gestionnaires si les liaisons deviennent un problème de performance

Merci d'avoir lu ! J'espère que cet article a été utile. Si vous trouvez cet article utile, veuillez le partager avec plus de personnes en le recommandant.

_Mise à jour :_

[Omri Luzon](https://www.freecodecamp.org/news/the-best-way-to-bind-event-handlers-in-react-282db2cf1530/undefined) et [Shesh](https://www.freecodecamp.org/news/the-best-way-to-bind-event-handlers-in-react-282db2cf1530/undefined) ont mentionné les packages `lodash-decorators` et `react-autobind` pour des liaisons plus pratiques. Personnellement, je ne suis pas un grand fan de faire quoi que ce soit automatiquement (j'essaie toujours de garder des choses comme les liaisons minimales), mais l'auto-liaison est absolument un excellent moyen d'écrire du code propre et de gagner plus d'efforts. Le code serait comme suit :

```
import autoBind from 'react-autobind';class HelloWorld() {  constructor() {    autoBind(this);  }
```

```
  handleClick() {    ...  }  render() {    return (<button onClick={this.handleClick}/>);  }}
```

Puisque `autoBind` gérera les liaisons automatiquement, il n'est pas nécessaire d'utiliser le truc de la fonction fléchée (`handleClick = () => {}`) pour faire la liaison, et dans la fonction `render()`, `this.handleClick` peut être utilisé directement.