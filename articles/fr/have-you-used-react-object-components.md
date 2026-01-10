---
title: Comment écrire un composant React sans utiliser de classes ou de hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-20T18:18:23.000Z'
originalURL: https://freecodecamp.org/news/have-you-used-react-object-components
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0bd740569d1a4ca4a7f.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment écrire un composant React sans utiliser de classes ou de hooks
seo_desc: 'By Matt Thorning

  With the release of React Hooks I have seen a lot of posts comparing class components
  to functional components. Functional components are nothing new in React, however
  it was not possible before version 16.8.0 to create a stateful co...'
---

Par Matt Thorning

Avec la sortie des React Hooks, j'ai vu beaucoup de publications comparant les composants de classe aux composants fonctionnels. Les composants fonctionnels ne sont pas nouveaux dans React, cependant, il n'était pas possible avant la version 16.8.0 de créer un composant stateful avec accès aux hooks de cycle de vie en utilisant uniquement une fonction. Ou était-ce possible ?

Appelez-moi un pédant (beaucoup de gens le font déjà !) mais lorsque nous parlons de composants de classe, nous parlons techniquement de composants créés par des fonctions. Dans cet article, j'aimerais utiliser React pour démontrer ce qui se passe réellement lorsque nous écrivons une classe en JavaScript.

## Classes vs Fonctions

Tout d'abord, je voudrais montrer très brièvement comment ce que l'on appelle communément des composants fonctionnels et de classe sont liés. Voici un simple composant écrit sous forme de classe :
```js
class Hello extends React.Component {
  render() {
    return <p>Bonjour !</p>
  }
}
```
Et voici écrit sous forme de fonction :
```js
function Hello() {
  return <p>Bonjour !</p>
}
```
Remarquez que le composant fonctionnel est simplement une méthode de rendu. Pour cette raison, ces composants n'ont jamais pu maintenir leur propre état ou effectuer des effets secondaires à des points spécifiques de leur cycle de vie. Depuis React 16.8.0, il est possible de créer des composants fonctionnels stateful grâce aux hooks, ce qui signifie que nous pouvons transformer un composant comme celui-ci :
```js
class Hello extends React.Component {
  
  state = {
    sayHello: false
  }

  componentDidMount = () => {
    fetch('greet')
      .then(response => response.json())
      .then(data => this.setState({ sayHello: data.sayHello });
  }

  render = () => {
    const { sayHello } = this.state;
    const { name } = this.props;

    return sayHello ? <p>{`Bonjour ${name}!`}</p> : null;
  }
}
```
En un composant fonctionnel comme celui-ci :
```js
function Hello({ name }) {

  const [sayHello, setSayHello] = useState(false);

  useEffect(() => {
    fetch('greet')
      .then(response => response.json())
      .then(data => setSayHello(data.sayHello));
  }, []);

  return sayHello ? <p>{`Bonjour ${name}!`}</p> : null;
}
```
Le but de cet article n'est pas de discuter pour savoir lequel est meilleur que l'autre, car il existe déjà des centaines de publications sur ce sujet ! La raison de montrer les deux composants ci-dessus est de clarifier ce que React fait réellement avec eux.

Dans le cas du composant de classe, React crée une instance de la classe en utilisant le mot-clé `new` :
```js
const instance = new Component(props);
```
Cette instance est un objet. Lorsque nous disons qu'un composant est une classe, ce que nous voulons dire en réalité, c'est qu'il s'agit d'un objet. Ce nouvel objet composant peut avoir son propre état et ses propres méthodes, dont certaines peuvent être des méthodes de cycle de vie (render, componentDidMount, etc.) que React appellera aux points appropriés pendant la durée de vie de l'application.

Avec un composant fonctionnel, React l'appelle simplement comme une fonction ordinaire (parce que c'est une fonction ordinaire !) et il retourne soit du HTML, soit d'autres composants React.

Les méthodes permettant de gérer l'état du composant et de déclencher des effets à des points spécifiques du cycle de vie du composant doivent maintenant être importées si elles sont nécessaires. Ces méthodes fonctionnent entièrement en fonction de l'ordre dans lequel elles sont appelées par chaque composant qui les utilise, car elles ne savent pas quel composant les a appelées. C'est pourquoi vous ne pouvez appeler les hooks qu'au niveau supérieur du composant et ils ne peuvent pas être appelés de manière conditionnelle.

## La Fonction Constructeur

JavaScript n'a pas de classes. Je sais que cela ressemble à des classes, nous venons d'en écrire deux ! Mais sous le capot, JavaScript n'est pas un langage basé sur les classes, il est basé sur les prototypes. Les classes ont été ajoutées avec la spécification ECMAScript 2015 (également appelée ES6) et ne sont qu'une syntaxe plus propre pour une fonctionnalité existante.

Essayons de réécrire un composant React de classe sans utiliser la syntaxe de classe. Voici le composant que nous allons recréer :
```js
class Counter extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      count: 0
    }
    this.handleClick = this.handleClick.bind(this);
  }
  
  handleClick() {
    const { count } = this.state;
    this.setState({ count: count + 1 });
  }

  render() {
    const { count } = this.state;
    return (
      <>
        <button onClick={this.handleClick}>+1</button>
        <p>{count}</p>
      </>
    );
  }

}
```
Cela rend un bouton qui incrémente un compteur lorsqu'il est cliqué, c'est un classique ! La première chose que nous devons créer est la fonction constructeur, qui effectuera les mêmes actions que la méthode `constructor` dans notre classe, à l'exception de l'appel à `super` car c'est une chose spécifique aux classes.
```js
function Counter(props) {
  this.state = {
    count: 0
  }
  this.handleClick = this.handleClick.bind(this);
}
```
C'est la fonction que React appellera avec le mot-clé `new`. Lorsqu'une fonction est appelée avec `new`, elle est traitée comme une fonction constructeur ; un nouvel objet est créé, la variable `this` est pointée vers celui-ci et la fonction est exécutée avec le nouvel objet étant utilisé partout où `this` est mentionné.

Ensuite, nous devons trouver un endroit pour les méthodes `render` et `handleClick` et pour cela, nous devons parler de la chaîne de prototypes.

## La Chaîne de Prototypes

JavaScript permet l'héritage des propriétés et des méthodes entre objets grâce à ce que l'on appelle la chaîne de prototypes.

Eh bien, je dis héritage, mais en réalité, je veux dire délégation. Contrairement à d'autres langages avec des classes, où les propriétés sont copiées d'une classe à ses instances, les objets JavaScript ont un lien de prototype interne qui pointe vers un autre objet. Lorsque vous appelez une méthode ou essayez d'accéder à une propriété sur un objet, JavaScript vérifie d'abord la propriété sur l'objet lui-même. Si elle ne la trouve pas là, elle vérifie le prototype de l'objet (le lien vers l'autre objet). Si elle ne la trouve toujours pas, elle vérifie le prototype du prototype et ainsi de suite jusqu'à ce qu'elle la trouve ou qu'il n'y ait plus de prototypes à vérifier.

En général, tous les objets en JavaScript ont `Object` au sommet de leur chaîne de prototypes ; c'est ainsi que vous avez accès à des méthodes telles que `toString` et `hasOwnProperty` sur tous les objets. La chaîne se termine lorsqu'un objet est atteint avec `null` comme prototype, ce qui est normalement le cas pour `Object`.

Essayons de clarifier les choses avec un exemple.

```js
const parentObject = { name: 'parent' };
const childObject = Object.create(parentObject, { name: { value: 'child' } });
console.log(childObject);
```
Tout d'abord, nous créons `parentObject`. Parce que nous avons utilisé la syntaxe littérale d'objet, cet objet sera lié à `Object`. Ensuite, nous utilisons `Object.create` pour créer un nouvel objet en utilisant `parentObject` comme prototype.

Maintenant, lorsque nous utilisons `console.log` pour imprimer notre `childObject`, nous devrions voir :

![console output of childObject](https://www.freecodecamp.org/news/content/images/2019/08/childObject-1.jpg)

L'objet a deux propriétés, il y a la propriété `name` que nous venons de définir et la propriété `__proto___`. `__proto__` n'est pas une propriété réelle comme `name`, c'est une propriété d'accès au prototype interne de l'objet. Nous pouvons les développer pour voir notre chaîne de prototypes :

![expanded output of childObject](https://www.freecodecamp.org/news/content/images/2019/08/childObject_expanded-1.jpg)

Le premier `__proto___` contient le contenu de `parentObject` qui a son propre `__proto___` contenant le contenu de `Object`. Ce sont toutes les propriétés et méthodes disponibles pour `childObject`.

Il peut être assez déroutant que les prototypes soient trouvés sur une propriété appelée `__proto__` ! Il est important de réaliser que `__proto__` n'est qu'une référence à l'objet lié. Si vous utilisez `Object.create` comme nous l'avons fait ci-dessus, l'objet lié peut être n'importe quoi que vous choisissez, si vous utilisez le mot-clé `new` pour appeler une fonction constructeur, alors ce lien se fait automatiquement vers la propriété `prototype` de la fonction constructeur.

D'accord, revenons à notre composant. Puisque React appelle notre fonction avec le mot-clé `new`, nous savons maintenant que pour rendre les méthodes disponibles dans la chaîne de prototypes de notre composant, nous devons simplement les ajouter à la propriété `prototype` de la fonction constructeur, comme ceci :

```js
Counter.prototype.render = function() {
  const { count } = this.state;
  return (
    <>
      <button onClick={this.handleClick}>+1</button>
      <p>{count}</p>
    </>
  );
},

Counter.prototype.handleClick = function () {
  const { count } = this.state;
  this.setState({ count: count + 1 });
}
```

## Méthodes Statiques

Cela semble être un bon moment pour mentionner les méthodes statiques. Parfois, vous pourriez vouloir créer une fonction qui effectue une action liée aux instances que vous créez - mais il n'est pas vraiment logique que la fonction soit disponible sur chaque objet `this`. Lorsqu'elles sont utilisées avec des classes, elles sont appelées Méthodes Statiques. Je ne suis pas sûr qu'elles aient un nom lorsqu'elles ne sont pas utilisées avec des classes !

Nous n'avons pas utilisé de méthodes statiques dans notre exemple, mais React en a quelques-unes et nous en avons utilisé une plus tôt avec `Object.create`. Il est facile de déclarer une méthode statique sur une classe, vous devez simplement préfixer la méthode avec le mot-clé `static` :
```js
class Example {
  static staticMethod() {
    console.log('ceci est une méthode statique');
  }
}
```
Et il est tout aussi facile d'en ajouter une à une fonction constructeur :
```js
function Example() {}
Example.staticMethod = function() { 
  console.log('ceci est une méthode statique');
}
```
Dans les deux cas, vous appelez la fonction comme ceci :
```js
Example.staticMethod()
```

## Étendre React.Component

Notre composant est presque prêt, il reste juste deux problèmes à résoudre. Le premier problème est que React doit pouvoir déterminer si notre fonction est une fonction constructeur ou simplement une fonction régulière. Cela est dû au fait qu'il doit savoir s'il doit l'appeler avec le mot-clé `new` ou non.

Dan Abramov a écrit un excellent article de blog [à ce sujet](https://overreacted.io/how-does-react-tell-a-class-from-a-function/), mais pour faire court, React recherche une propriété sur le composant appelée `isReactComponent`. Nous pourrions contourner cela en ajoutant `isReactComponent: {}` à `Counter.prototype` (je sais, vous vous attendriez à ce que ce soit un booléen mais la valeur de `isReactComponent` est un objet vide. Vous devrez lire son article si vous voulez savoir pourquoi !) mais cela ne serait que tricher le système et cela ne résoudrait pas le deuxième problème.

Dans la méthode `handleClick`, nous faisons un appel à `this.setState`. Cette méthode n'est pas sur notre composant, elle est "héritée" de `React.Component` ainsi que `isReactComponent`. Si vous vous souvenez de la [section sur la chaîne de prototypes](#la-chaine-de-prototypes) précédente, nous voulons que notre instance de composant hérite d'abord des méthodes sur `Counter.prototype` puis des méthodes de `React.Component`. Cela signifie que nous voulons lier les propriétés sur `React.Component.prototype` à `Counter.prototype.__proto__`.

Heureusement, il y a une méthode sur `Object` qui peut nous aider avec cela :
```js
Object.setPrototypeOf(Counter.prototype, React.Component.prototype);

```

## Ça Marche !
C'est tout ce que nous devons faire pour que ce composant fonctionne avec React sans utiliser la syntaxe de classe. Voici le code du composant en un seul endroit si vous souhaitez le copier et l'essayer vous-même :
```js
function Counter(props) {
  this.state = {
    count: 0
  };
  this.handleClick = this.handleClick.bind(this);
}

Counter.prototype.render = function() {
  const { count } = this.state;
  return (
    <>
      <button onClick={this.handleClick}>+1</button>
      <p>{count}</p>
    </>
  );
}

Counter.prototype.handleClick = function() {
  const { count } = this.state;
  this.setState({ count: count + 1 });
}

Object.setPrototypeOf(Counter.prototype, React.Component.prototype);
```
Comme vous pouvez le voir, ce n'est pas aussi agréable à regarder qu'avant. En plus de rendre JavaScript plus accessible aux développeurs habitués à travailler avec des langages traditionnels basés sur les classes, la syntaxe de classe rend également le code beaucoup plus lisible.

Je ne suggère pas que vous devriez commencer à écrire vos composants React de cette manière (en fait, je vous le déconseillerais activement !). Je pensais simplement que ce serait un exercice intéressant qui fournirait un aperçu du fonctionnement de l'héritage JavaScript.

---

Bien que vous n'ayez pas besoin de comprendre tout cela pour écrire des composants React, cela ne peut certainement pas faire de mal. Je m'attends à ce qu'il y ait des occasions où vous corrigez un bug délicat où la compréhension du fonctionnement de l'héritage prototypal fera toute la différence.

J'espère que vous avez trouvé cet article intéressant et/ou agréable. Vous pouvez trouver d'autres articles que j'ai écrits sur mon blog à l'adresse [hellocode.dev](https://hellocode.dev). Merci.