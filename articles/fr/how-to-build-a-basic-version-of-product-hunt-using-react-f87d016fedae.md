---
title: Comment construire une version basique de Product Hunt en utilisant React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-01T20:16:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-basic-version-of-product-hunt-using-react-f87d016fedae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OcJzrdQWZSd07hYpHnBf2A.png
tags:
- name: JavaScript
  slug: javascript
- name: product hunt
  slug: product-hunt
- name: React
  slug: react
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: Comment construire une version basique de Product Hunt en utilisant React
seo_desc: 'By Emmanuel Yusufu

  This example and design shares what I’ve learned from the book Fullstack React.
  I highly recommend it as a good resource for learning React and it’s ecosystem technologies.
  check it out here: fullstackreact.com.

  Imagine that as a d...'
---

Par Emmanuel Yusufu

Cet exemple et ce design partagent ce que j'ai appris du livre _Fullstack React_. Je le recommande vivement comme une bonne ressource pour apprendre React et ses technologies d'écosystème. Consultez-le ici : [fullstackreact.com](https://fullstackreact.com).

Imaginez que, en tant que développeur, vous avez été chargé de créer un MVP pour un produit de startup qui doit être démontré à des investisseurs potentiels.

L'application est une application de vote inspirée par Product Hunt et Reddit. Dans l'application, les produits sont affichés dans une collection. Les utilisateurs peuvent voter pour les meilleurs produits, et l'application les triera automatiquement selon le nombre de votes, en plaçant les plus élevés avant les plus bas.

Les fonctionnalités de l'application que nous allons construire sont très simples :

* Les utilisateurs peuvent voir les produits existants/affichés.
* Les utilisateurs peuvent voter pour les produits qui les ravissent.
* Les produits sont triés automatiquement selon le nombre de votes.

**Vous pouvez [voir la démo ici](http://reactdemo.emmanuelyusufu.com).**

#### Étape 1 : d'abord les premières choses

Tout d'abord, rendez-vous sur Github et téléchargez le dossier de démarrage que j'ai déjà créé avec la configuration nécessaire pour notre application [ici](https://github.com/emmyyusufu/react-product-voting-app-with-bootstrap/tree/starter). Copiez l'**URL** fournie par le bouton de clonage/téléchargement vert et exécutez-la dans votre chemin préféré sur votre ligne de commande. Vous devez avoir git déjà installé.

```
git clone URL
```

Une fois le dossier téléchargé, ouvrez-le dans votre éditeur de code et observez les fichiers et la structure du dossier. Cela ressemble à ceci :

```
├───src
│   ├───app.js
│   ├───seed.js
│   ├───style.css
└───vendor
    ├───bootstrap-3.3.7-dist
    ├───font-awesome-4.7.0
    ├───react.js
    ├───react-dom.js
    └───babel-standalone.js
```

**Note :** Votre éditeur de code doit avoir un serveur live. Cela nous permet de servir les fichiers à notre navigateur pour visualiser notre travail. Assurez-vous d'installer l'extension pour votre éditeur de code préféré.

Sous le dossier src, il y a les fichiers **app.js** et **seed.js**. Le fichier app.js est l'endroit où nous écrirons la plupart du code pour notre application. Le fichier seed.js contient déjà la collection de données des produits à afficher.

Notre fichier seed.js contient le code suivant :

```js
window.Seed = (function () {
    function generateVoteCount() {
      return Math.floor((Math.random() * 50) + 15);
    }
    
    const products = [
      {
        id: 1,
        title: 'Yellow Pail',
        description: 'On-demand sand castle construction expertise.',
        url: '#',
        votes: generateVoteCount(),
        submitterAvatarUrl: 'images/avatars/daniel.jpg',
        productImageUrl: 'images/products/image-aqua.png',
      },
                                ...
    ];
    
    return { products: products };
    
  }());
```

Ce code crée une fonction `generateVoteCount()` que nous expliquerons plus tard et un tableau `products` qui contient les données de nos produits. Ils sont enveloppés dans une fonction auto-invocatrice et sont attachés à l'objet `window` de notre navigateur. De cette manière, nous pouvons y accéder où nous le souhaitons.

La fonction `Seed` retourne finalement un objet avec une propriété de produits et une valeur de `products`. Cela signifie que, si nous exécutons `Seed.products`, nous devrions avoir chaque objet produit retourné.

Le fichier **react.js** est le code contenant le cœur de React lui-même. De plus, **react-dom.js** est le code qui nous aide à rendre les composants React que nous avons créés dans le DOM HTML. Enfin, **babel-standalone.js** est le code Babel qui transpile le code JSX et ES6 avancé avec lequel nous allons travailler en code ES5 (la spécification JavaScript la plus courante que la plupart des anciens et actuels navigateurs supportent aujourd'hui).

#### Étape 2 : créer des composants

Nous devons créer deux composants React. Nous appellerons le composant parent `ProductList`, et la collection de composants enfants qu'il abrite sera `Product`.

À l'intérieur du fichier app.js, créez le composant parent en faisant ceci :

```jsx
class ProductList extends React.Component {
    render() {
        const products = Seed.products.map((product) => (
            <Product 
            id={product.id}
            title={product.title}
            description={product.description}
            url={product.url}
            votes={product.votes}
            submitterAvatarUrl={product.submitterAvatarUrl}
            productImageUrl={product.productImageUrl}
            />
        ));
        return (
            <div className="container">
                <h1>Produits populaires</h1>
                <hr />
                {products}
            </div>
        );
    }
}
ReactDOM.render(<ProductList />, document.getElementById('content'));
```

Dans le composant parent, nous avons l'intention de créer un composant enfant basé sur chaque objet accessible depuis `Seed.products`. Nous avons donc configuré quelques props. Maintenant, déclarons le composant enfant toujours dans le même fichier appelé `Product` :

```jsx
class Product extends React.Component {
    render() {
        return (
          <div className='container'>
            <div className="row">
            <div className='col-md-12'>
                <div className="main">
                <div className="image">  
                    <img src={this.props.productImageUrl} />
                </div> 
                <div className='header'>
                    <a>
                        <i className='fa fa-2x fa-caret-up' />
                    </a>
                    {this.props.votes}
                </div>
                <div className='description'>
                    <a href={this.props.url}>
                        {this.props.title}
                    </a>
                    <p>{this.props.description}
                    </p>
                </div>
              <div className='extra'>
                <span>Soumis par :</span>
                <img
                  className='avatar'
                  src={this.props.submitterAvatarUrl}
                />
              </div>
              </div>
            </div>
            </div>
          </div>
        );
      }
}
```

Nous sommes capables de référencer `React.Component` et `ReactDOM.render` parce que nous avons déjà chargé les fichiers react.js et react-dom.js. Ils sont disponibles pour une utilisation même si nous sommes actuellement dans le fichier app.js. Ayant créé le composant, `ReactDOM.render(whatComponent, where)` le rend dans le DOM.

En exécutant votre serveur live, vous devriez avoir l'écran suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/n8J6LzTA2DTnLI43sXzHnbJJjpDdfd8BVyeJ)
_composants statiques_

#### Étape 3 : ajouter de l'interactivité

Jusqu'à présent, nous avons pu coder les composants de notre application — mais ils sont encore statiques. Comment pouvons-nous les rendre interactifs ?

Dans la programmation d'applications React, suivez ce processus général :

* Divisez l'UI de l'application en composants
* Construisez une version statique de l'application
* Déterminez quelles données sont un état
* Déterminez dans quels composants chaque partie de l'état doit vivre
* Codez en dur les états initiaux
* Ajoutez un flux de données inverse de l'enfant au parent via les props
* Ajoutez la communication avec le serveur

Nous ne ferons pas tout ce qui précède, mais commençons avec l'**état**. La seule partie des données dans notre application qui peut être considérée comme étatique ou changeante est le nombre de votes. Rappelez-vous : c'est une propriété dans la collection de produits dans notre fichier seed.js. Les votes sont dans chaque objet `product`, donc ils représentent notre état.

Connaissant notre état, où l'initialisons-nous ? Les états dans React sont auto-contenus dans certains composants, contrairement aux props qui sont passés. Le nombre de votes en tant qu'état est possédé par `<Product />`, mais puisque la collection de produits que nous avons est générée à partir de `<ProductList />`, nous initialisons l'état là. Dans `<ProductList />`, faites ceci avant la méthode `render()` :

```
constructor() {
        super();
        this.state = {
            products: []
        }
    }
```

Lors de l'initialisation de l'état dans un composant, nous essayons de définir à quoi il devrait ressembler tout en le gardant vide. Nos produits sont un tableau, donc nous utilisons un tableau vide. Nous l'initialisons à l'intérieur de `constructor() {}` , car c'est la partie du code qui s'exécute lorsque notre composant est créé.

Faisons en sorte que notre composant lise `products` à partir de son propre état au lieu de le lire à partir d'un fichier. Ajoutez :

```jsx
 componentDidMount() { 
   this.setState({ products: Seed.products }) 
 }
```

pour définir l'état à utiliser. Mettez également à jour `const products = Seed.products` en `const products = this.state.products`. Pour faire en sorte que JavaScript les trie selon le nombre de votes le plus élevé, écrivez ceci à la place :

```jsx
const products = this.state.products.sort((a, b) {
    b.votes - a.votes
});
```

La fonction `sort();` de JavaScript utilise une **fonction de comparaison** à l'intérieur. Vous pourriez trouver des informations à ce sujet dans une documentation.

#### Étape 4 : gérer les votes positifs

Rendons-nous sur le lien hypertexte entourant l'icône font-awesome, caret-up, et créons une fonction en utilisant onClick.

```jsx
<a onClick={passTheId}>
    <i className='fa fa-2x fa-caret-up' />
 </a>
```

Après avoir défini la fonction, créons-la réellement. À l'intérieur du composant Product, créez une fonction `passTheId();` :

```jsx
constructor() {
        super();
        this.passTheId = this.passTheId.bind(this);
    }
    passTheId() {
        console.log('Id will be passed');
    }
```

Nous avons lié la fonction au mot-clé `this`, car seules les fonctions intégrées comme render() ont accès à ce mot.

Créons une autre fonction dans le composant ProductList. Celle-ci mettra à jour l'état en travaillant avec la fonction `handleUpVote` du composant Product.

```jsx
handleProductUpVote = (productId) => {
    const nextProducts = this.state.products.map((product) => {
      if (product.id === productId) {
        return Object.assign({}, product, {
          votes: product.votes + 1,
        });
      } else {
        return product;
      }
    });
    this.setState({
      products: nextProducts,
    });
  }
```

Les états dans React doivent être traités comme immuables. C'est-à-dire qu'ils ne doivent pas être modifiés directement. La fonction ci-dessus le fera en utilisant `Object.assign();` de JavaScript en créant un tableau apparemment nouveau appelé `nextProducts`. Cela est similaire à l'état existant, mais avec un changement dans le nombre de votes. `nextProducts` est ensuite défini comme le nouvel état. Cela semble étrange de faire les choses de cette manière, mais c'est ce que l'équipe React recommande pour améliorer les performances.

Nous voulons passer l'ID du produit du composant enfant `Product` au composant parent `ProductList`, alors rendons `handleProductUpVote` disponible pour l'enfant en tant que props :

```jsx
const productComponents = products.map((product) => (
      <Product
        key={'product-' + product.id}
        id={product.id}
        title={product.title}
        description={product.description}
        url={product.url}
        votes={product.votes}
        submitterAvatarUrl={product.submitterAvatarUrl}
        productImageUrl={product.productImageUrl}
        onVote={this.handleProductUpVote}
      />
    ));
```

Nous avons ajouté `onVote={this.handleProductUpVote}`. Ainsi, au niveau de l'enfant, nous pouvons y accéder via `this.props`

```jsx
passTheId() {
        console.log('Id will be passed');
        this.props.onVote(this.props.id)
    }
```

Votre fichier `app.js` entier devrait ressembler à ceci :

```jsx
class ProductList extends React.Component {
    state = {
        products: [],
      };
      componentDidMount() {
        this.setState({ products: Seed.products });
      }
      handleProductUpVote = (productId) => {
        const nextProducts = this.state.products.map((product) => {
          if (product.id === productId) {
            return Object.assign({}, product, {
              votes: product.votes + 1,
            });
          } else {
            return product;
          }
        });
        this.setState({
          products: nextProducts,
        });
      }
    render() {
        const products = this.state.products.sort((a, b) => (
            b.votes - a.votes
        ));
        const productComponents = products.map((product) => (
            <Product
              key={'product-' + product.id}
              id={product.id}
              title={product.title}
              description={product.description}
              url={product.url}
              votes={product.votes}
              submitterAvatarUrl={product.submitterAvatarUrl}
              productImageUrl={product.productImageUrl}
              onVote={this.handleProductUpVote}
            />
          ));
        return (
            <div className="container">
                <h1>Produits populaires</h1>
                <hr />
                {productComponents}
            </div>
        );
    }
}
class Product extends React.Component {
    constructor() {
        super();
        this.passTheId = this.passTheId.bind(this);
    }
    passTheId() {
        console.log('Id will be passed');
        this.props.onVote(this.props.id);
    }
    render() {
        return (
          <div className='container'>
            <div className="row">
            <div className='col-md-12'>
                <div className="main">
                <div className="image">  
                    <img src={this.props.productImageUrl} />
                </div> 
                <div className='header'>
                    <a onClick={this.passTheId}>
                        <i className='fa fa-2x fa-caret-up' />
                    </a>
                    {this.props.votes}
                </div>
                <div className='description'>
                    <a href={this.props.url}>
                        {this.props.title}
                    </a>
                    <p>
                        {this.props.description}
                    </p>
                </div>
              <div className='extra'>
                <span>Soumis par :</span>
                <img
                  className='avatar'
                  src={this.props.submitterAvatarUrl}
                />
              </div>
              </div>
            </div>
            </div>
          </div>
        );
      }
}
ReactDOM.render(<ProductList />, document.getElementById('content'));
```

Actualisez votre navigateur et vous devriez voir l'application fonctionnelle. [**Voir la démo**](http://reactdemo.emmanuelyusufu.com).

N'hésitez pas à partager, commenter ou poser des questions. Pour le code final, visitez ce [lien github](https://github.com/emmyyusufu/react-product-voting-app-with-bootstrap) et clonez-le sur votre ordinateur.

Si vous avez aimé cet article, donnez-moi quelques applaudissements pour que plus de gens le voient. Merci d'avoir lu.

Vous pouvez lire plus de mes écrits sur mon blog : [Stellar Code](http://stellarcode.co/build-a-product-hunt-inspired-app-with-react-2/).