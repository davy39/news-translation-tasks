---
title: Pourquoi nous devons lier les gestionnaires d'événements dans les composants
  de classe en React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-04T18:03:26.000Z'
originalURL: https://freecodecamp.org/news/this-is-why-we-need-to-bind-event-handlers-in-class-components-in-react-f7ea1a6f93eb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kdZr8L9pUOgosVNWqMSmlQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi nous devons lier les gestionnaires d'événements dans les composants
  de classe en React
seo_desc: 'By Saurabh Misra

  While working on React, you must have come across controlled components and event
  handlers. We need to bind these methods to the component instance using .bind()
  in our custom component’s constructor.

  class Foo extends React.Componen...'
---

Par Saurabh Misra

En travaillant sur React, vous avez probablement rencontré des composants contrôlés et des gestionnaires d'événements. Nous devons lier ces méthodes à l'instance du composant en utilisant `.bind()` dans le constructeur de notre composant personnalisé.

```jsx
class Foo extends React.Component{
  constructor( props ){
    super( props );
    this.handleClick = this.handleClick.bind(this);
  }
  
  handleClick(event){
    // votre logique de gestion d'événement
  }
  
  render(){
    return (
      <button type="button" 
      onClick={this.handleClick}>
      Cliquez-moi
      </button>
    );
  }
}

ReactDOM.render(
  <Foo />,
  document.getElementById("app")
);
```

Dans cet article, nous allons découvrir pourquoi nous devons faire cela.

Je vous recommande de lire à propos de `.bind()` [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind) si vous ne savez pas déjà ce qu'il fait.

### **Blâmez JavaScript, pas React**

Eh bien, blâmer semble un peu dur. Ce n'est pas quelque chose que nous devons faire à cause du fonctionnement de React ou de JSX. C'est à cause du fonctionnement de la liaison `this` en JavaScript.

Voyons ce qui se passe si nous ne lions pas la méthode du gestionnaire d'événements avec son instance de composant :

```jsx
class Foo extends React.Component{
  constructor( props ){
    super( props );
  }
    
  handleClick(event){
    console.log(this); // 'this' est undefined
  }
    
  render(){
    return (
      <button type="button" onClick={this.handleClick}>
        Cliquez-moi
      </button>
    );
  }
}

ReactDOM.render(
  <Foo />,
  document.getElementById("app")
);
```

Si vous exécutez ce code, cliquez sur le bouton "Cliquez-moi" et vérifiez votre console. Vous verrez `undefined` imprimé dans la console comme valeur de `this` depuis l'intérieur de la méthode du gestionnaire d'événement. La méthode `handleClick()` semble avoir **perdu** son contexte (instance de composant) ou sa valeur `this`.

### **Comment fonctionne la liaison de 'this' en JavaScript**

Comme je l'ai mentionné, cela se produit à cause du fonctionnement de la liaison `this` en JavaScript. Je ne vais pas entrer dans beaucoup de détails dans cet article, mais [ici](https://www.freecodecamp.org/news/the-complete-guide-to-this-in-javascript/) est une excellente ressource pour comprendre comment la liaison `this` fonctionne en JavaScript.

Mais pertinent pour notre discussion ici, la valeur de `this` à l'intérieur d'une fonction dépend de la manière dont cette fonction est invoquée.

#### **Liaison par défaut**

```js
function display(){
 console.log(this); // 'this' pointera vers l'objet global
}

display(); 
```

C'est un appel de fonction simple. La valeur de `this` à l'intérieur de la méthode `display()` dans ce cas est la fenêtre — ou l'objet global — en mode non strict. En mode strict, la valeur de `this` est `undefined`.

#### **Liaison implicite**

```js
var obj = {
 name: 'Saurabh',
 display: function(){
   console.log(this.name); // 'this' pointe vers obj
  }
};

obj.display(); // Saurabh 
```

Lorsque nous appelons une fonction de cette manière — précédée par un objet de contexte — la valeur de `this` à l'intérieur de `display()` est définie sur `obj`.

Mais lorsque nous assignons cette référence de fonction à une autre variable et invoquons la fonction en utilisant cette nouvelle référence de fonction, nous obtenons une valeur différente de `this` à l'intérieur de `display()`.

```js
var name = "uh oh! global";
var outerDisplay = obj.display;
outerDisplay(); // uh oh! global
```

Dans l'exemple ci-dessus, lorsque nous appelons `outerDisplay()`, nous ne spécifions pas d'objet de contexte. C'est un appel de fonction simple sans objet propriétaire. Dans ce cas, la valeur de `this` à l'intérieur de `display()` revient à la **liaison par défaut**. Elle pointe vers l'objet global ou `undefined` si la fonction invoquée utilise le mode strict.

Cela est particulièrement applicable lors du passage de telles fonctions en tant que rappels à une autre fonction personnalisée, une fonction de bibliothèque tierce ou une fonction JavaScript intégrée comme `setTimeout`.

Considérez la définition factice de `setTimeout` comme montré ci-dessous, puis invoquez-la.

```js
// Une implémentation factice de setTimeout
function setTimeout(callback, delay){

   //attendre 'delay' millisecondes
   callback();
   
}

setTimeout( obj.display, 1000 );
```

Nous pouvons comprendre que lorsque nous appelons `setTimeout`, JavaScript assigne internement `obj.display` à son argument `callback`.

```js
callback = obj.display;
```

Cette opération d'assignation, comme nous l'avons vu auparavant, fait perdre à la fonction `display()` son contexte. Lorsque ce rappel est finalement invoqué à l'intérieur de `setTimeout`, la valeur de `this` à l'intérieur de `display()` revient à la **liaison par défaut**.

```js
var name = "uh oh! global";
setTimeout( obj.display, 1000 );

// uh oh! global
```

#### **Liaison explicite et dure**

Pour éviter cela, nous pouvons **lier explicitement et durablement** la valeur de `this` à une fonction en utilisant la méthode `bind()`.

```js
var name = "uh oh! global";
obj.display = obj.display.bind(obj); 
var outerDisplay = obj.display;
outerDisplay();

// Saurabh
```

Maintenant, lorsque nous appelons `outerDisplay()`, la valeur de `this` pointe vers `obj` à l'intérieur de `display()`.

Même si nous passons `obj.display` comme un rappel, la valeur de `this` à l'intérieur de `display()` pointera correctement vers `obj`.

### **Recréer le scénario en utilisant uniquement JavaScript**

Au début de cet article, nous avons vu cela dans notre composant React appelé `Foo`. Si nous n'avons pas lié le gestionnaire d'événements avec `this`, sa valeur à l'intérieur du gestionnaire d'événements était définie comme `undefined`.

Comme je l'ai mentionné et expliqué, cela est dû au fonctionnement de la liaison `this` en JavaScript et non lié au fonctionnement de React. Alors, enlevons le code spécifique à React et construisons un exemple similaire en JavaScript pur pour simuler ce comportement.

```jsx
class Foo {
  constructor(name){
    this.name = name
  }
  
  display(){
    console.log(this.name);
  }
}

var foo = new Foo('Saurabh');
foo.display(); // Saurabh

// L'opération d'assignation ci-dessous simule la perte de contexte
// similaire au passage du gestionnaire en tant que rappel dans le
// composant React réel
var display = foo.display; 
display(); // TypeError: this is undefined
```

Nous ne simulons pas d'événements et de gestionnaires réels, mais nous utilisons un code synonyme. Comme nous l'avons observé dans l'exemple du composant React, la valeur de `this` était `undefined` car le contexte a été perdu après le passage du gestionnaire en tant que rappel — synonyme d'une opération d'assignation. C'est ce que nous observons ici dans cet extrait JavaScript non-React également.

"Attendez une minute ! La valeur de `this` ne devrait-elle pas pointer vers l'objet global, puisque nous exécutons cela en mode non strict selon les règles de la liaison par défaut ?" pourriez-vous demander.

**Non.** Voici pourquoi :

> Les corps des déclarations de classe et des expressions de classe sont exécutés en [mode strict](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode), c'est-à-dire le constructeur, les méthodes statiques et les méthodes de prototype. Les fonctions getter et setter sont exécutées en mode strict.

Vous pouvez lire l'article complet [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes).

Donc, pour éviter l'erreur, nous devons lier la valeur de `this` comme ceci :

```jsx
class Foo {
  constructor(name){
    this.name = name
    this.display = this.display.bind(this);
  }
  
  display(){
    console.log(this.name);
  }
}

var foo = new Foo('Saurabh');
foo.display(); // Saurabh

var display = foo.display;
display(); // Saurabh
```

Nous n'avons pas besoin de faire cela dans le constructeur, et nous pouvons le faire ailleurs également. Considérez ceci :

```jsx
class Foo {
  constructor(name){
    this.name = name;
  }
  display(){
    console.log(this.name);
  }
}

var foo = new Foo('Saurabh');
foo.display = foo.display.bind(foo);
foo.display(); // Saurabh

var display = foo.display;
display(); // Saurabh
```

Mais le constructeur est l'endroit le plus optimal et efficace pour coder nos instructions de liaison des gestionnaires d'événements, étant donné que c'est là que toute l'initialisation a lieu.

#### **Pourquoi n'avons-nous pas besoin de lier 'this' pour les fonctions fléchées ?**

Nous avons deux autres façons de définir les gestionnaires d'événements à l'intérieur d'un composant React.

* [**Syntaxe des champs de classe publics (Expérimental)**](https://babeljs.io/docs/plugins/transform-class-properties/)

```jsx
class Foo extends React.Component{
  handleClick = () => {
    console.log(this); 
  }
 
  render(){
    return (
      <button type="button" onClick={this.handleClick}>
        Cliquez-moi
      </button>
    );
  }
} 

ReactDOM.render(
  <Foo />,
  document.getElementById("app")
);
```

* [**Fonction fléchée dans le rappel**](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

```jsx
class Foo extends React.Component{
 handleClick(event){
    console.log(this);
  }
 
  render(){
    return (
      <button type="button" onClick={(e) => this.handleClick(e)}>
        Cliquez-moi
      </button>
    );
  }
}

ReactDOM.render(
  <Foo />,
  document.getElementById("app")
);
```

Ces deux méthodes utilisent les fonctions fléchées introduites dans ES6. Lorsque nous utilisons ces alternatives, notre gestionnaire d'événements est déjà automatiquement lié à l'instance du composant, et nous n'avons pas besoin de le lier dans le constructeur.

La raison est que dans le cas des fonctions fléchées, `this` est lié **lexicalement**. Cela signifie qu'il utilise le contexte de la fonction englobante — ou globale — comme sa valeur `this`.

Dans le cas de l'exemple de syntaxe des champs de classe publics, la fonction fléchée est englobée à l'intérieur de la classe `Foo` — ou de la fonction constructeur — donc le contexte est l'instance du composant, ce que nous voulons.

Dans le cas de l'exemple de fonction fléchée en tant que rappel, la fonction fléchée est englobée à l'intérieur de la méthode `render()`, qui est invoquée par React dans le contexte de l'instance du composant. C'est pourquoi la fonction fléchée capturera également ce même contexte, et la valeur de `this` à l'intérieur pointera correctement vers l'instance du composant.

Pour plus de détails concernant la liaison lexicale de `this`, consultez [cette excellente ressource](https://github.com/getify/You-Dont-Know-JS/blob/master/this%20%26%20object%20prototypes/ch2.md#lexical-this).

### **Pour faire court**

Dans les composants de classe en React, lorsque nous passons la référence de la fonction du gestionnaire d'événements en tant que rappel comme ceci

```jsx
<button type="button" onClick={this.handleClick}>Cliquez-moi</button>
```

la méthode du gestionnaire d'événements perd son contexte **lié implicitement**. Lorsque l'événement se produit et que le gestionnaire est invoqué, la valeur de `this` revient à la **liaison par défaut** et est définie sur `undefined`, car les déclarations de classe et les méthodes de prototype s'exécutent en mode strict.

Lorsque nous lions le `this` du gestionnaire d'événements à l'instance du composant dans le constructeur, nous pouvons le passer en tant que rappel sans nous soucier de perdre son contexte.

Les fonctions fléchées sont exemptes de ce comportement car elles utilisent la liaison **lexicale** de `this` qui les lie automatiquement à la portée dans laquelle elles sont définies.