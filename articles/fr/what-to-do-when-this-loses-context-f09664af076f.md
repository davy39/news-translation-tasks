---
title: Que faire lorsque "this" perd son contexte
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T18:38:14.000Z'
originalURL: https://freecodecamp.org/news/what-to-do-when-this-loses-context-f09664af076f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IqZ-dx0QZDVvTBqQBNrOhg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Que faire lorsque "this" perd son contexte
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  The best way to avoid this losing context is to not use this at all. However, this
  is not always an option. We may have i...'
---

Par Cristian Salcescu

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

La meilleure façon d'éviter que `this` ne perde son contexte est de ne pas utiliser `this` du tout. Cependant, ce n'est pas toujours une option. Nous pouvons avoir hérité de code qui utilise `this` ou nous pouvons travailler avec une bibliothèque utilisant `this`.

Les littéraux d'objet, les fonctions constructeurs et les `class`es construisent des objets sur le système de prototype. Le pseudo-paramètre `this` est utilisé par le système de prototype pour donner aux fonctions l'accès aux autres propriétés de l'objet.

Examinons quelques situations.

### Fonctions imbriquées

`this` perd son contexte à l'intérieur des fonctions imbriquées. [Considérons le code suivant](https://jsfiddle.net/cristi_salcescu/n7zh5gvw/) :

```
class Service {
  constructor(){
    this.numbers = [1,2,3];
    this.token = "token";
  }
  
  doSomething(){
    setTimeout(function doAnotherThing(){
      this.numbers.forEach(function log(number){
      //Cannot read property 'forEach' of undefined
          console.log(number);
          console.log(this.token);
      });
    }, 100);
  }
}

let service = new Service();
service.doSomething();
```

La méthode `doSomething()` a deux fonctions imbriquées : `doAnotherThing()` et `log()`. Lorsque `service.doSomething()` est appelée, `this` perd son contexte dans les fonctions imbriquées.

#### bind()

Une façon de résoudre le problème est d'utiliser `bind()`. [Regardez le code suivant](https://jsfiddle.net/cristi_salcescu/2r4ncoum/) :

```
doSomething(){
   setTimeout(function doAnotherThing(){
      this.numbers.forEach(function log(number){
         console.log(number);
         console.log(this.token);
      }.bind(this));
    }.bind(this), 100);
  }
```

`bind()` crée une nouvelle version de la fonction qui, lorsqu'elle est appelée, a déjà la valeur de `this` définie. Notez que nous devons utiliser `.bind(this)` pour chaque fonction imbriquée.

`function doAnotherThing(){ /*…*/}.bind(this)` crée une version de `doAnotherThing()` qui prend la valeur de `this` de `doSomething()`.

#### that/self

Une autre option est de déclarer et d'utiliser une nouvelle variable `that/self` qui stocke la valeur de `this` de la méthode `doSomething()`.

[Voir le code ci-dessous](https://jsfiddle.net/cristi_salcescu/6ajx1hbp/) :

```
doSomething(){
   let that = this;
   setTimeout(function doAnotherThing(){
      that.numbers.forEach(function log(number){
         console.log(number);
         console.log(that.token);
      });
    }, 100);
  }
```

Nous devons déclarer `let that = this` dans toutes les méthodes utilisant `this` dans les fonctions imbriquées.

#### Fonction fléchée

La fonction fléchée offre une autre façon de résoudre ce problème. [Voici le code](https://jsfiddle.net/cristi_salcescu/ejdb19su/) :

```
doSomething(){
   setTimeout(() => {
     this.numbers.forEach(number => {
         console.log(number);
         console.log(this.token);
      });
    }, 100);
  }
```

La fonction fléchée n'a pas son propre `this`. Elle prend la valeur de `this` de son parent. Le seul problème avec cette solution est que nous avons tendance à perdre le nom de la fonction. Le nom de la fonction est important, car il améliore la lisibilité en exprimant l'intention de la fonction.

[Voici le même code](https://jsfiddle.net/cristi_salcescu/by096fza/), avec des fonctions inférant le nom de la variable :

```
doSomething(){    
   let log = number => {
     console.log(number);
     console.log(this.token);
   }
    
   let doAnotherThing = () => {
     this.numbers.forEach(log);
   }
    
   setTimeout(doAnotherThing, 100);
}
```

Méthode en tant que rappel

`this` perd son contexte lorsque la méthode est utilisée comme rappel.

[Considérons la classe suivante](https://jsfiddle.net/cristi_salcescu/f3t2vmex/) :

```
class Service {
  constructor(){
    this.token = "token"; 
  }
  
  doSomething(){
    console.log(this.token);//undefined
  } 
}
let service = new Service();
```

Maintenant, examinons quelques situations où la méthode `service.doSomething()` est utilisée comme rappel.

```
//rappel sur événement DOM
$("#btn").click(service.doSomething);

//rappel pour timer
setTimeout(service.doSomething, 0);

//rappel pour fonction personnalisée
run(service.doSomething);

function run(fn){
  fn();
}
```

Dans toutes les situations précédentes, `this` perd son contexte.

#### bind()

Nous pouvons utiliser `bind()` pour résoudre le problème. [Consultez l'extrait de code suivant](https://jsfiddle.net/cristi_salcescu/1904jbh8/) :

```
//rappel sur événement DOM
$("#btn").click(service.doSomething.bind(service));

//rappel pour timer
setTimeout(service.doSomething.bind(service), 0);

//rappel pour fonction personnalisée
run(service.doSomething.bind(service));
```

#### Fonction fléchée

Une autre option est de créer une nouvelle fonction qui appelle `service.doSomething()`.

```
//rappel sur événement DOM
$("#btn").click(() => service.doSomething());

//rappel pour timer
setTimeout(() => service.doSomething(), 0);

//rappel pour fonction personnalisée
run(() => service.doSomething());
```

### Composants React

Dans les composants React, `this` perd son contexte lorsque les méthodes sont utilisées comme rappels pour les événements de l'interface utilisateur.

[Considérons le composant suivant](https://jsfiddle.net/cristi_salcescu/q59zjx1p/) :

```
class TodoAddForm extends React.Component {
  constructor(){
      super();
      this.todos = [];
  }
  
  componentWillMount() {
    this.setState({desc: ""});
  }
  
  add(){
    let todo = {desc: this.state.desc}; 
    //Cannot read property 'state' of undefined
    this.todos.push(todo);
  }
  
  handleChange(event) {
     //Cannot read property 'setState' of undefined
     this.setState({desc: event.target.value});
  }
  
  render() {
    return <form>
      <input onChange={this.handleChange} value={this.state.desc} type="text"/>
      <button onClick={this.add} type="button">Save</button>
    </form>;
  }
}

ReactDOM.render(
  <TodoAddForm />,
  document.getElementById('root'));
```

Une façon de résoudre le problème est de créer de nouvelles fonctions dans le constructeur en utilisant `bind(this)`.

```
constructor(){
   super();
   this.todos = [];
   this.handleChange = this.handleChange.bind(this);
   this.add = this.add.bind(this);
}
```

### Ne pas utiliser "`this`"

Pas de `this`, pas de problèmes de perte de contexte. Les objets peuvent être créés en utilisant des fonctions de fabrication. [Consultez ce code](https://jsfiddle.net/cristi_salcescu/xvsk6twc/) :

```
function Service() {  
  let numbers = [1,2,3];
  let token = "token";
  
  function doSomething(){
   setTimeout(function doAnotherThing(){
     numbers.forEach(function log(number){
        console.log(number);
        console.log(token);
      });
    }, 100);
  }
  
  return Object.freeze({
    doSomething
  });
}
```

Cette fois, le contexte n'est pas perdu lorsque la méthode est utilisée comme rappel.

```

let service = Service();
service.doSomething();

//rappel sur événement DOM
$("#btn").click(service.doSomething);

//rappel pour timer
setTimeout(service.doSomething, 0);

//rappel pour fonction personnalisée
run(service.doSomething);
```

### Conclusion

`this` peut perdre son contexte dans différentes situations.

`bind()`, le motif that/self et les fonctions fléchées sont des outils à notre disposition pour résoudre les problèmes de contexte.

Les fonctions de fabrication donnent l'option de créer des objets sans utiliser `this` du tout.

[**Découvrez Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la programmation fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour en savoir plus sur l'application des techniques de programmation fonctionnelle dans React, consultez** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Apprenez le **React fonctionnel**, de manière basée sur des projets, avec [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)