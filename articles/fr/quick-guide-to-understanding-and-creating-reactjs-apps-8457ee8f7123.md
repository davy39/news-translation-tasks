---
title: Un guide rapide pour vous aider à comprendre et créer des applications ReactJS
date: '2018-08-18T13:11:00.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/quick-guide-to-understanding-and-creating-reactjs-apps-8457ee8f7123
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://cdn-media-1.freecodecamp.org/images/0*XGhE7haLzzQeM1xo
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_desc: 'By Aditya Sridhar

  This Post is divided into 2 parts


  The First Part demonstrates how to create a simple React app using ‘create-react-app’
  CLI and explains the project structure.

  The Second Part explains an existing code that I have posted in Github....'
---


Par Aditya Sridhar

<!-- more -->

### Cet article est divisé en 2 parties

1.  La première partie démontre comment créer une application React simple en utilisant l'interface de ligne de commande (CLI) `create-react-app` et explique la structure du projet.
2.  La deuxième partie explique un code existant que j'ai publié sur Github. Ce code démontre l'utilisation des composants, la communication entre les composants, les appels HTTP et React Bootstrap (une version de bootstrap écrite pour React).

### Partie 1

#### Installer NodeJS s'il n'est pas déjà présent

NodeJS est nécessaire car les bibliothèques requises pour React sont téléchargées via le gestionnaire de paquets node ( npm ). Référez-vous à [https://nodejs.org/en/][1] pour installer NodeJS.

#### Installer le package Node create-react-app

Le package node **create-react-app** aide à configurer un projet React. Installez le package node create-react-app globalement en utilisant la commande suivante.

```
npm install -g create-react-app
```

#### Créer le projet

Le projet peut être créé en utilisant **create-react-app.** Utilisez la commande suivante pour créer le projet.

```
npx create-react-app first-react-app
```

**first-react-app** est le nom de l'application. La commande ci-dessus crée un dossier nommé **first-react-app** qui est le dossier du projet. Afin de tester si tout a été configuré correctement, allez dans le dossier du projet et démarrez l'application en utilisant la commande suivante.

```
cd first-react-app
npm start
```

Ouvrez votre navigateur et allez à l'URL suivante **localhost:3000**  
Vous devriez voir que votre application est en cours d'exécution. L'application ressemblera à ceci dans votre navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/w1SbWWOdE5XDpq25D6aYcw6e7RjJSJupdp1T)

#### Explication de la structure de base des dossiers

Lorsque vous avez créé le projet, vous avez remarqué qu'il a créé un ensemble de fichiers. Je vais lister ici certains des fichiers et dossiers importants que vous devriez connaître.

1.  **package.json :** Ce fichier contient la liste des dépendances node nécessaires.
2.  **public/index.html :** Lorsque l'application démarre, c'est la première page qui est chargée. Ce sera le seul fichier html de toute l'application car React est généralement écrit en **JSX**, que je couvrirai plus tard. De plus, ce fichier contient une ligne de code. Cette ligne est très importante car tous les composants de l'application sont chargés dans ce div.
3.  **src/index.js** : C'est le fichier javascript correspondant à index.html. Ce fichier contient la ligne de code suivante qui est très importante : **ReactDOM.render(<App />, document.getElementById(‘root’));**
4.  La ligne de code ci-dessus indique que le composant **App** (nous couvrirons le composant App bientôt) doit être chargé dans un élément html avec l'id **root**. Il s'agit simplement de l'élément **div** présent dans **index.html.**
5.  **src/index.css** : Le fichier CSS correspondant à index.js.
6.  **src/App.js** : C'est le fichier du composant **App**. Le composant **App** est le composant principal de React qui sert de conteneur pour tous les autres composants.
7.  **src/App.css** : C'est le fichier CSS correspondant au composant **App**.
8.  **build :** C'est le dossier où sont stockés les fichiers compilés. Les applications React peuvent être développées soit en JSX, soit en JavaScript normal, mais l'utilisation de JSX facilite définitivement le codage pour le développeur :). Cependant, les navigateurs ne comprennent pas le JSX. Le JSX doit donc être converti en javascript avant le déploiement. Ces fichiers convertis sont stockés dans le dossier build après le regroupement (bundling) et la minification. Pour voir le dossier build, lancez la commande suivante :

```
npm run build
```

#### Création de composants

Un composant dans React remplit une fonctionnalité spécifique. Une application n'est rien d'autre qu'une collection de composants. Chaque composant peut avoir plusieurs composants enfants et les composants peuvent communiquer entre eux.

Créons maintenant un composant React.

À l'intérieur du dossier **src**, créez un fichier nommé **FirstComponent.js** et copiez le code suivant dans **FirstComponent.js.**

```
import React, {Component} from 'react';

export default class FirstComponent extends Component {

constructor(props) {
    super(props)
    }

render() {
    const element = (<div>Text from Element</div>)
    return (<div className="comptext">
    <h3>First Component</h3>
        {this.props.displaytext}
        {element}
    </div>)
    }
}
```

1.  Le nom du composant est **FirstComponent**, ce qui est indiqué par le nom du fichier ainsi que dans la déclaration `export default class FirstComponent extends Component`.
2.  L'attribut **props** dans le constructeur contiendra tous les paramètres qui sont passés en entrée à ce composant.
3.  **render() :** La valeur de retour de cette fonction est rendue (affichée) à l'écran. Chaque fois que la fonction render() est appelée, l'écran est re-rendu. Cela se fait généralement automatiquement par l'application. Le code qui ressemble beaucoup à du html dans cette fonction n'est rien d'autre que du **JSX.**

#### JSX

Le **JSX** ressemble beaucoup au HTML mais possède toute la puissance de javascript. Je vais expliquer ici le code JSX et ce qu'il essaie de faire.

```
render() {
    const element = (<div>Text from Element</div>)
    return (<div className="comptext">
    <h3>First Component</h3>
        {this.props.displaytext}
        {element}
    </div>)
    }
```

La première ligne `const element = (<div>Text from Element</div>)` crée un élément div et l'assigne à une constante appelée element. Cette syntaxe particulière que vous voyez n'est rien d'autre que du JSX.

À l'intérieur de l'instruction Return, vous voyez la syntaxe de code suivante.

```
<div className="comptext">
    <h3>First Component</h3>
        {this.props.displaytext}
        {element}
</div>
```

Ici, **className** est utilisé pour pointer vers une classe CSS. `<h3>First Component</h3>` est juste une syntaxe html normale. `{this.props.displaytext}` est utilisé pour accéder à un attribut appelé displaytext à partir des props (ainsi, displaytext est passé en entrée chaque fois que ce composant est appelé). Ici, **displaytext** est juste un nom personnalisé que j'ai donné. `{element}` est la constante qui a été créée, qui contient à son tour l'élément div.

#### Utilisation du composant

**FirstComponent** a été créé mais n'est pas encore utilisé. Ajoutons **FirstComponent** au composant **App**. Voici le code modifié pour **App.js**

```
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import FirstComponent from './FirstComponent'
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <FirstComponent displaytext="First Component Data"/>
      </div>
);
  }
}
export default App;
```

**FirstComponent** doit d'abord être importé dans le composant App, ce qui est fait à la ligne `import FirstComponent from ‘./FirstComponent’`.

Ensuite, **FirstComponent** est ajouté au composant **App** en utilisant la ligne `<FirstComponent displaytext=”First Component Data”/>`.

Ici, **displaytext** est passé comme un attribut au FirstComponent.

Vous pouvez maintenant lancer l'application en utilisant la commande `npm start`.

Vous devriez voir le résultat suivant dans le navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1HRMdkexuXF6YgrAp1NwPXyzZsIuebRpiFjB)

#### Félicitations ?

Vous savez maintenant comment créer une application React et comment créer et utiliser des composants React. Vous en savez aussi un peu plus sur le JSX :)

La partie suivante expliquera un code React existant provenant de Github. Le code de la partie 2 est différent de celui que nous avons écrit dans la partie 1.

### Partie 2

#### Code

Le code suivant est expliqué ici, donc clonez le dépôt sur votre ordinateur. Le dépôt contient des instructions sur la façon de cloner et de configurer le code sur votre machine.

#### [https://github.com/aditya-sridhar/simple-reactjs-app][2]

#### URL de l'application

Pour voir à quoi ressemble l'application finale, vous pouvez cliquer sur l'URL suivante. Cela vous donnera une bonne idée de ce que l'application essaie de faire.

#### [https://aditya-sridhar.github.io/simple-reactjs-app][3]

L'application ressemblerait à ceci sur un écran de mobile :

![Image](https://cdn-media-1.freecodecamp.org/images/0aE6v5BOa389ObdKL-9oglyr4KLYhBTKhrTm)

#### Que fait cette application

Cette application affiche une liste de clients. Lorsqu'un client est sélectionné, elle affiche les détails du client sélectionné. Il s'agit d'une application monopage (SPA). **React est particulièrement adapté aux applications monopages**. Les applications monopages affichent tout au sein d'une seule page.

#### **Explication de la structure de l'application**

#### Composant **Customers**

Ce composant affiche la liste des clients. Il correspond au fichier **src/Customers.js**. Ce composant possède le constructeur suivant.

```
constructor(props) {
    super(props)
    this.state = {
        selectedCustomer: 1
    }
}
```

Les **props** ont déjà été expliquées. Mais ici vous voyez aussi **this.state**. Chaque fois que l'état (state) change, le composant est re-rendu. Ici, **state** possède un paramètre appelé **selectedCustomer** qui sert à suivre quel client est sélectionné. Si **selectedCustomer** change, alors le **composant et ses composants enfants** sont re-rendus. Le constructeur est utilisé uniquement pour définir les **props** et l'**état**. De plus, les **props** ne doivent **jamais être modifiées** à l'intérieur d'un composant.

La chose suivante que vous remarquez est le code suivant.

```
componentDidMount() {
    this.getCustomerData();
}
```

**componentDidMount()** est une fonction qui est appelée dès que le composant est rendu. Elle peut donc être utilisée pour définir des valeurs initiales ainsi que pour charger des données. Ici, elle appelle une fonction nommée **getCustomerData()**.

Le morceau de code suivant que vous voyez est :

```
getCustomerData() {
    axios.get('assets/samplejson/customerlist.json').then(response => {
        this.setState({customerList: response})
    })
};
```

Cette fonction **getCustomerData()** effectue un appel HTTP pour lire le json d'exemple contenant la liste des clients à partir de **assets/samplejson/customerlist.json.** En cas de réponse positive, l'état du système est modifié en assignant la **réponse** à **customerList.** Vous vous demandez peut-être pourquoi nous n'avons jamais ajouté customerList dans le constructeur. La raison est que vous pouvez ajouter des paramètres dynamiquement dans l'état à n'importe quel moment du code. La seule exigence est que dans le constructeur, au moins un état vide doit être défini.

Ici, la bibliothèque **axios** est utilisée pour effectuer l'appel HTTP. J'ai fourni la documentation pour axios dans la section Références.

La fonction suivante est la fonction **render()** qui renvoie les éléments qui doivent être rendus à l'écran. Les principaux points d'attention dans la fonction render sont :

```
<Button bsStyle="info" onClick={() => this.setState({selectedCustomer: customer.id})}>

Click to View Details

</Button>
```

Chaque client de la liste possède un bouton appelé **Click to View Details**. L'extrait de code ci-dessus indique que chaque fois que le bouton est cliqué, l'état de **selectedCustomer** doit être remplacé par l'id du client sélectionné. Puisque l'état change ici, le composant et son composant enfant seront re-rendus.

L'autre extrait de code important est :

```
<CustomerDetails val={this.state.selectedCustomer}/>
```

Cet extrait indique que **CustomerDetails** est un composant enfant du composant **Customers** et passe également l'id **selectedCustomer** en tant qu'entrée au composant **CustomerDetails**.

#### Composant CustomerDetails

Ce composant affiche les détails du client sélectionné. Certains extraits de code importants de ce composant seront expliqués ici :

```
componentDidUpdate(prevProps) {

//get Customer Details only if props has changed
//(props is the input) 
    if (this.props.val !== prevProps.val) {
        this.getCustomerDetails(this.props.val)
    }
}
```

La fonction **componentDidUpdate()** est appelée chaque fois que le composant est re-rendu. Ici, nous appelons la fonction **getCustomerDetails()** si l'entrée de ce composant a changé lors du re-rendu du composant. L'entrée passée à la fonction **getCustomerDetails()** est **this.props.val**. **this.props.val**, à son tour, obtient sa valeur du composant **Customers** (selectedCustomer a été passé en entrée à celui-ci). Pour savoir si l'entrée a changé, l'extrait de code utilisé est `this.props.val !== prevProps.val`.

```
getCustomerDetails(id) {
    axios.get('assets/samplejson/customer' + id + '.json').then(response => {
        this.setState({customerDetails: response})
    })
};
```

La fonction **getCustomerDetails()** effectue un appel HTTP pour obtenir le json d'exemple qui contient les détails du client. Le paramètre **id** est utilisé pour savoir quels détails de client sont requis. **id** n'est rien d'autre que **this.props.val.** Lorsque la réponse est reçue avec succès, l'état de ce composant est modifié en assignant la **réponse** à **customerDetails**.

La fonction **render()** de ce composant est assez directe et simple, elle ne sera donc pas couverte ici.

### Références

**create-react-app :** Référez-vous à [https://github.com/facebook/create-react-app][4] pour apprendre tout ce qui peut être fait avec create-react-app.

**ReactJS :** Référez-vous à [https://reactjs.org/][5] pour comprendre les concepts de ReactJS. La documentation est très bonne.

**React Bootstrap :** Référez-vous à [https://react-bootstrap.github.io/getting-started/introduction/][6] pour comprendre comment utiliser React Bootstrap.

**axios :** Référez-vous à [https://www.npmjs.com/package/axios][7] pour en savoir plus sur l'utilisation de la bibliothèque axios pour effectuer des requêtes HTTP.

### Encore félicitations ?

Vous savez maintenant comment utiliser les composants, comment communiquer d'un composant parent à un composant enfant et vous en savez aussi un peu sur le rendu.

Les concepts de base ont été couverts dans cet article et j'espère que cela vous sera utile.

### À propos de l'auteur

Je suis passionné par la technologie et je suis ses avancées. J'aime aussi aider les autres avec les connaissances que je possède dans le domaine technologique.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/][8]

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18][9]

Mon site web : [https://adityasridhar.com/][10]

### Autres articles pertinents de ma part

[Un guide rapide pour vous aider à comprendre et créer des applications Angular 6][11]

[Une introduction rapide à Vue.js][12]

[1]: https://nodejs.org/en/
[2]: https://github.com/aditya-sridhar/simple-reactjs-app
[3]: https://aditya-sridhar.github.io/simple-reactjs-app
[4]: https://github.com/facebook/create-react-app
[5]: https://reactjs.org/
[6]: https://react-bootstrap.github.io/getting-started/introduction/
[7]: https://www.npmjs.com/package/axios
[8]: https://www.linkedin.com/in/aditya1811/
[9]: https://twitter.com/adityasridhar18
[10]: https://adityasridhar.com/
[11]: https://medium.freecodecamp.org/quick-guide-to-understanding-and-creating-angular-6-apps-2f491dffca1c
[12]: https://medium.freecodecamp.org/a-quick-introduction-to-vue-js-72937ee8880d