---
title: Apprendre React en 5 minutes - Un tutoriel React.js pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-10T20:31:12.000Z'
originalURL: https://freecodecamp.org/news/learn-react-js-in-5-minutes-526472d292f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3WTslHrSuJfqlj3qZRRFPQ.png
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
seo_title: Apprendre React en 5 minutes - Un tutoriel React.js pour débutants
seo_desc: 'By Per Harald Borgen

  This tutorial will give you a basic understanding of React by building a very  simple
  application. I’ll leave out everything which I don’t think is core.

  And then if it sparks your interest, and you want to learn more, you can ch...'
---

Par Per Harald Borgen

Ce tutoriel vous donnera une compréhension de base de React en construisant une application **très** simple. Je vais omettre **tout** ce que je ne pense pas être essentiel.

Et si cela suscite votre intérêt et que vous souhaitez en apprendre davantage, vous pouvez consulter notre [cours gratuit sur React](https://scrimba.com/g/glearnreact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_5_minute_article) sur Scrimba.

Mais pour l'instant, concentrons-nous sur les bases !

### L'installation

Lorsque vous commencez avec React, vous devez utiliser la configuration la plus simple possible : un fichier HTML qui importe les bibliothèques `React` et `ReactDOM` en utilisant des balises de script.

Cela ressemble à ceci :

```html
<html>
<head>  
<script src="https://unpkg.com/react@16/umd/react.development.js"></script>  
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>  
<script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>  
</head>  
<body>  
    <div id="root"></div>  
    <script type="text/babel">  
      
    /*   
    AJOUTER LE CODE REACT ICI   
    */  
      
    </script>  
</body>  
</html>

```

Nous avons également importé Babel, car React utilise quelque chose appelé JSX pour écrire le balisage. Nous devons transformer le JSX en JavaScript simple, afin que le navigateur puisse le comprendre.

Il y a deux autres choses que je veux que vous remarquiez :

1. Le `<div>` avec l'id `#root`. C'est le point d'entrée de notre application. C'est là que toute notre application vivra.
2. La balise `<script type="text/babel">` dans le corps. C'est là que nous écrirons notre code React.

Si vous souhaitez expérimenter avec le code, consultez [ce bac à sable Scrimba](https://scrimba.com/c/cmGe8Cp?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_5_minute_article).

### Composants

Tout dans React est un composant, et ceux-ci prennent généralement la forme de classes JavaScript. Vous créez un composant en étendant la classe `React.Component`. Créons un composant appelé `Hello` :

```jsx
class Hello extends React.Component {  
    render() {  
        return <h1>Bonjour le monde !</h1>;  
    }  
}

```

Vous définissez ensuite les méthodes pour le composant. Dans notre exemple, nous n'avons qu'une seule méthode, et elle s'appelle `render()`.

À l'intérieur de `render()`, vous retournerez une description de ce que vous voulez que React dessine sur la page. Dans le cas ci-dessus, nous voulons simplement qu'il affiche une balise `h1` avec le texte _Bonjour le monde !_ à l'intérieur.

Pour que notre petite application s'affiche à l'écran, nous devons également utiliser `ReactDOM.render()` :

```jsx
ReactDOM.render(  
    <Hello />,   
    document.getElementById("root")  
);

```

C'est donc là que nous connectons notre composant `Hello` avec le point d'entrée de l'application (`<div id="root"></div>`).

_Nous disons simplement :_ Hé React ! S'il te plaît, rends le composant **Hello** à l'intérieur du nœud DOM avec l'id **root** !

Cela donne le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*T-bmSzg0KlijyB3dG1M-ow.png)

La syntaxe HTML que nous venons de voir (`<h1>` et `<Hello/>`) est le code JSX dont j'ai parlé plus tôt. Ce n'est pas vraiment du HTML, c'est beaucoup plus puissant. Bien que ce que vous écrivez là se retrouve sous forme de balises HTML dans le DOM.

L'étape suivante consiste à faire en sorte que notre application gère les données.

### Gestion des données

Il existe deux types de données dans React : **props** et **state**. La différence entre les deux est un peu difficile à comprendre au début, alors ne vous inquiétez pas si vous la trouvez un peu confuse. Cela deviendra plus facile une fois que vous commencerez à travailler avec eux.

La différence clé est que le **state** est privé et peut être changé depuis le composant lui-même. Les **props** sont externes et ne sont pas contrôlés par le composant lui-même. Ils sont passés par des composants plus haut dans la hiérarchie, qui contrôlent également les données.

**Un composant peut changer son état interne directement. Il ne peut pas changer ses props directement.**

Examinons d'abord les props.

### Props

Notre composant `Hello` est complètement statique. Il affiche le même message peu importe quoi. Cependant, une grande partie de React est la réutilisabilité, ce qui signifie la capacité d'écrire un composant une fois, puis de le réutiliser dans différents cas d'utilisation. Par exemple, pour afficher différents messages.

Pour atteindre ce type de réutilisabilité, nous allons ajouter des props. Voici comment vous passez des props à un composant :

```jsx
ReactDOM.render(  
    <Hello message="mon ami" />,   
    document.getElementById("root")  
);

```

Cette prop s'appelle `message` et a la valeur « mon ami ». Nous pouvons accéder à cette prop à l'intérieur du composant Hello en référençant `this.props.message`, comme ceci :

```jsx
class Hello extends React.Component {  
    render() {  
        return <h1>Bonjour {this.props.message} !</h1>;  
    }  
}

```

En conséquence, cela est affiché à l'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/1*M0-2Ct0K3SARZLSwIzgdJw.png)

La raison pour laquelle nous écrivons `{this.props.message}` avec des accolades est que nous devons dire au JSX que nous voulons ajouter une expression JavaScript. Cela s'appelle **échappement**.

Nous avons donc maintenant un composant réutilisable qui peut afficher n'importe quel message que nous voulons sur la page. Hourra !

Cependant, que se passe-t-il si nous voulons que le composant puisse changer ses propres données ? Alors nous devons utiliser l'état à la place !

### State

L'autre façon de stocker des données dans React est dans l'état du composant. Et contrairement aux props, qui ne peuvent pas être changées directement par le composant, l'état peut l'être.

Donc, si vous voulez que les données de votre application changent, par exemple, en fonction des interactions de l'utilisateur, elles doivent être stockées dans l'état d'un composant quelque part dans l'application.

#### Initialisation de l'état

Pour initialiser l'état, il suffit de définir `this.state` dans la méthode `constructor()` de la classe. Notre état est un objet qui, dans notre cas, n'a qu'une seule clé appelée `message`.

```jsx
class Hello extends React.Component {  
      
    constructor(){  
        super();  
        this.state = {  
            message: "mon ami (de l'état) !"  
        };  
    }  
      
    render() {  
        return <h1>Bonjour {this.state.message} !</h1>;  
    }  
}

```

Avant de définir l'état, nous devons appeler `super()` dans le constructeur. Cela est dû au fait que `this` n'est pas initialisé avant que `super()` n'ait été appelé.

#### Changer l'état

Pour modifier l'état, il suffit d'appeler **this.setState()**, en passant le nouvel objet d'état comme argument. Nous allons faire cela à l'intérieur d'une méthode que nous appellerons `updateMessage`.

```jsx
class Hello extends React.Component {  
      
    constructor(){  
        super();  
        this.state = {  
            message: "mon ami (de l'état) !"  
        };  
        this.updateMessage = this.updateMessage.bind(this);   
   }

   updateMessage() {  
        this.setState({  
            message: "mon ami (de l'état changé) !"  
        });  
    }

    render() {  
        return <h1>Bonjour {this.state.message} !</h1>;  
    }  
}

```

Remarque : Pour que cela fonctionne, nous avons également dû lier le mot-clé `this` à la méthode `updateMessage`. Sinon, nous n'aurions pas pu accéder à `this` dans la méthode.

### Gestionnaires d'événements

L'étape suivante consiste à créer un bouton à cliquer, afin que nous puissions déclencher la méthode `updateMessage()`.

Ajoutons donc un bouton à la méthode `render()` :

```jsx
render() {  
  return (  
     <div>  
       <h1>Bonjour {this.state.message} !</h1>  
       <button onClick={this.updateMessage}>Cliquez-moi !</button>  
     </div>     
  )  
}

```

Ici, nous accrochons un écouteur d'événement au bouton, à l'écoute de l'événement **onClick**. Lorsque celui-ci est déclenché, nous appelons la méthode **updateMessage**.

Voici l'intégralité du composant :

```jsx
class Hello extends React.Component {  
      
    constructor(){  
        super();  
        this.state = {  
            message: "mon ami (de l'état) !"  
        };  
        this.updateMessage = this.updateMessage.bind(this);  
    }

    updateMessage() {  
        this.setState({  
            message: "mon ami (de l'état changé) !"  
        });  
    }

    render() {  
         return (  
           <div>  
             <h1>Bonjour {this.state.message} !</h1>  
             <button onClick={this.updateMessage}>Cliquez-moi !</button>  
           </div>     
        )  
    }  
}

```

La méthode **updateMessage** appelle ensuite **this.setState()** qui change la valeur de `this.state.message`. Et lorsque nous cliquons sur le bouton, voici comment cela se déroulera :

![Image](https://thepracticaldev.s3.amazonaws.com/i/v2sblyfk5axax0sv77m9.gif)

Félicitations ! Vous avez maintenant une compréhension très basique des concepts les plus importants de React.

Si vous souhaitez en apprendre davantage, assurez-vous de consulter notre [cours gratuit sur React sur Scrimba](https://scrimba.com/g/glearnreact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_5_minute_article).

Bonne chance avec le codage :)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le cofondateur de [Scrimba](https://scrimba.com) – le moyen le plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_5_minute_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=glearnreact_5_minute_article)_