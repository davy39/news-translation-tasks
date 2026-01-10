---
title: Apprendre les bases de React.js - Pour les débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T22:43:32.000Z'
originalURL: https://freecodecamp.org/news/start-your-journey-into-the-world-of-react-by-learning-these-basics-d6e05d3655e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PPCTtJ-CMUajEz20YS7d1g.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: reactjs
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprendre les bases de React.js - Pour les débutants
seo_desc: 'By Anchal Nigam

  Today I am going to highlight the basics of the world of React. If you have just
  started your journey in ReactJS, then I would say you have landed in the right place.
  In this article, I have tried to cover the basics of React in a ver...'
---

Par Anchal Nigam

Aujourd'hui, je vais mettre en lumière les bases du monde de React. Si vous venez de commencer votre voyage dans ReactJS, alors je dirais que vous êtes au bon endroit. Dans cet article, j'ai essayé de couvrir les bases de React de manière très simple. J'espère qu'à la fin de l'article, vous connaîtrez les concepts fondamentaux de React.

Commençons.

### ReactJS — Une bibliothèque puissante

Comme vous l'avez peut-être déjà lu dans de nombreux endroits, React est une bibliothèque pour créer des interfaces utilisateur web et mobiles. Elle a été développée par Facebook.

ReactJS est piloté par les composants. Tout est un composant qui est responsable de certaines fonctionnalités. Vous écrivez de petits composants et les combinez ensuite pour former de grands composants. Cela rend le code plus lisible et compréhensible. Les fonctionnalités qui rendent React puissant et beau sont :

1. **Il utilise le concept de DOM virtuel au lieu du DOM réel.**
2. **La lisibilité du code grâce au JSX. L'utilisation de JSX donne l'impression d'écrire des applications web (donne à JavaScript un aspect similaire à HTML).**
3. **Il utilise également le SSR (le SSR aide au référencement).**

Ce sont des choses que vous avez peut-être lues, mais vous comprendrez et ressentirez lorsque vous suivrez ce tutoriel. Alors, plongeons dans le concept du DOM virtuel (je dirais que c'est la principale fonctionnalité qui rend React plus beau).

### **ReactJS Virtual DOM**

Le DOM virtuel est une copie du DOM réel. Contrairement au DOM réel, le DOM virtuel effectue le minimum de manipulation du DOM pour garder les composants à jour. Il ne met à jour que la partie qui a été mise à jour.

La manipulation du DOM est très facile. Voici une démonstration visuelle de la façon dont le DOM virtuel fonctionne :

1. Le DOM virtuel est une copie du DOM réel.

![Image](https://cdn-media-1.freecodecamp.org/images/BbSeUOIyqaCzKUcpA6KvuNFw8Le1H5PLpW3a)

2. Lorsque les données changent dans un composant, toute l'interface utilisateur est réaffichée dans le DOM virtuel.

![Image](https://cdn-media-1.freecodecamp.org/images/cYrTIngjLltbbiyPito0pPgndqboLpdsznCU)

3. Ensuite, la comparaison entre le DOM réel et le DOM virtuel a lieu.

![Image](https://cdn-media-1.freecodecamp.org/images/0-9bDcRcobQ59vBJqp-OeSmrkaKlyZnc3taH)

4. Une fois le calcul terminé, le DOM réel est mis à jour avec les éléments qui ont changé.

![Image](https://cdn-media-1.freecodecamp.org/images/0SU6QfYqNsaVc7I7vwMYIBkKwz7ofvIN09C8)

Nous avons parlé de l'une des grandes fonctionnalités de React — le DOM virtuel, mais attendez ! Qu'était le JSX dans la deuxième fonctionnalité (points ci-dessus sur les fonctionnalités) ? Vous vous êtes peut-être demandé ce que c'était, quel était son rapport avec React, et comment il nous donne l'impression d'écrire des applications web...

Maintenant, plongeons dans le monde du JSX.

### JSX

Avant d'aller plus loin, jetons un coup d'œil au code ci-dessous :

```
class FirstComponent extends React.Component {  
     render() {    
         return (      
             <span className='customSize'>My First Component</span>    
          );  
      }
}
```

```
class FirstComponent extends React.Component {  
     render() {    
         return (      
            React.createElement('span',{className: 'customSize'},                            'My First Component')    
         );  
      }
}
```

Dans le premier exemple, la fonction render semble retourner du code HTML, mais il s'agit de JSX. **Le premier exemple est une version JSX du second.** JSX est une extension JavaScript qui donne à votre code JS un aspect HTML.

Si vous regardez le deuxième exemple, React.createElement est utilisé pour créer un élément React afin de représenter le composant React. Le deuxième argument peut être null ou vide si aucun prop ou attribut n'est nécessaire pour l'élément. Le troisième argument définit ce qui doit être à l'intérieur (comme tout autre élément React, par exemple <image>, avec l'attribut 'src').

Si vous regardez les deux blocs de code ci-dessus, vous trouverez le premier plus familier car il donne une impression de HTML. JSX augmente également la lisibilité du code. Jetons un coup d'œil à un autre exemple, sans JSX et avec JSX pour avoir une idée de la lisibilité du code.

**ReactJS sans JSX :**

```
React.createElement("div", null,  
      React.createElement("img", {src: "image.jpg", alt: "Random photo"}),
      React.createElement("h3", null, "Hello React"));
```

**ReactJS avec la version JSX :**

```
<div>  
   <img src="image.jpg" alt="Random photo" />  
   <h3>Hello React</h3>
</div>
```

En regardant l'exemple ci-dessus, vous pouvez comprendre ce que je disais concernant la lisibilité du code. À quel point il est facile de lire le code avec JSX, n'est-ce pas ? Je pense que cela suffit pour le JSX et j'espère que vous êtes maintenant en mesure de mieux comprendre la puissance du JSX dans le monde React.

**Note —** *Les navigateurs ne sont pas capables de lire le JSX. Nous devons donc le transpiler en JavaScript à l'aide de transformateurs JSX (comme Babel) afin que le navigateur puisse le comprendre.*

Maintenant, nous savons ce qu'est le JSX. Mais j'aimerais que vous retourniez à l'image précédente où j'ai écrit que React est tout au sujet des composants. C'est piloté par les composants. Comme les composants sont les éléments de base de React, explorons-les.

### Le cœur de ReactJS — Les composants

Vous avez peut-être rencontré le code ci-dessous sur la façon de créer des composants lors de vos recherches sur React :

```
class MyStatefulComponent extends React.Component {   
     state = {       
         title: ''    
     }
     
componentDidMount() {   
    console.log('Component mounted')  
}

render() {    
    return <div>{this.props.name}</div>;  
    }
}
```

Si vous écrivez votre composant de la manière ci-dessus, il est appelé un composant **Class/ Stateful/Container**. Si vous pensez que c'est la seule façon de créer des composants, détrompez-vous. Oui, il existe une autre façon de créer votre composant qui résulte en des **composants fonctionnels / sans état/présentation**. Avant d'aller plus loin, voyons comment les composants fonctionnels sont écrits :

```
const MyStatelessComponent = props => <div>{props.name}</div>;
```

Maintenant, vous vous demandez peut-être quelle est la différence entre les deux et comment choisir lequel créer. Alors, plongeons dans le monde des composants Stateful et Stateless.

Les composants **Stateless (ou présentation ou fonctionnel)** sont ceux qui n'ont pas d'état (vous ne savez pas ce qu'est l'état ? Pas de soucis, je l'explique dans une partie ultérieure). Ils sont utilisés pour la présentation, comme l'apparence de votre composant.

Un composant est une fonction JavaScript simple qui prend un prop comme argument et retourne un élément React (voir l'exemple ci-dessus). Son nom est explicite — il n'a pas d'état. Il n'a pas de méthodes de cycle de vie (comme la méthode **componentDidMount**, etc., que vous avez peut-être lue lors de vos recherches sur les tutoriels React).

Les composants **Stateful (ou conteneur ou classe)** sont ceux qui ont un état — une source de données (vous pouvez appeler this.setState à l'intérieur), des méthodes de cycle de vie (peut être utilisé pour faire un appel API). C'est une classe JavaScript qui étend votre composant React, ce qui signifie que React crée des instances de celui-ci. React initialise la classe de composant afin d'utiliser les méthodes de cycle de vie, pour initialiser l'état et plus encore.

Attendez... maintenant vous vous demandez peut-être lequel est le meilleur, et quoi choisir ? Vous pouvez répondre à cette question si vous avez cette question en tête sur la façon de séparer la partie logique de la partie présentation. Oui, c'est étrange qu'une question réponde à une autre question, mais vous comprendrez bientôt pourquoi j'ai dit cela.

Comme vous l'avez peut-être vu dans d'autres tutoriels React, ils utilisent la classe pour créer leurs composants. Ils mettent la partie logique ainsi que la partie présentation dans le même composant, ce qui rend ce composant plus compliqué et volumineux.

Donc, si vous voulez séparer votre logique des composants de présentation, alors la classe de composant est mieux adaptée pour les choses logiques comme la récupération de données depuis l'API ou les changements de données. D'autre part, si votre composant est axé sur les choses de présentation/fonctionnelles, le composant doit avoir une belle apparence.

En résumé, je dirais utilisez les deux. Utilisez la classe de composant lorsque vous avez besoin de l'une des choses (méthodes de cycle de vie, état) et pour la présentation, utilisez un composant fonctionnel.

C'est tout sur les composants.

Maintenant, nous avons une image de la façon dont nous pouvons écrire des composants, mais je ne vous ai pas dit comment nous pouvons gérer les données dans ceux-ci. Je pense que sans données, les composants seraient inutiles. Nous allons donc voir comment nous pouvons gérer les données d'un composant (comme la récupération de données depuis une API, l'histoire de l'état de React, la définition de l'état, etc.).

Commençons.

### Props

'Prop' est l'abréviation de propriétés, et c'est la seule source de données dans notre composant. Il peut être utilisé pour passer des données à différents composants. Attendez ! J'aimerais que vous retourniez là où je vous ai parlé des composants de présentation et des composants de classe. Je vous ai dit d'utiliser les composants de présentation pour gérer l'apparence de votre composant, et les composants conteneurs pour gérer les données et tout cela. Correct !

Donc, le 'prop' est celui que nous pouvons utiliser pour faire la connexion entre ces deux types de composants. Oui, vous pouvez utiliser les props pour passer des données d'un composant conteneur à un composant de présentation, où le composant de présentation affichera la vue avec vos données dynamiques. Veuillez jeter un coup d'œil au code ci-dessous pour mieux comprendre :

```
import {ButtonView} from './button.presentation';  
class MyContainerComponent extends React.Component {  
    state={      
       text : 'Submit'  
    }
render() {   
    return (    
        <ButtonView btnText={this.state.text}/>
        )
    }
}                     
```

```
export const ButtonView=({btnText})=>(  
     <div>   
         <button className="btn btn-info btn-lg">{btnText}</button>              </div>
)
```

Comme dans l'exemple ci-dessus (en utilisant les props — 'btnText'), vous pouvez séparer la partie logique de la partie présentation. Une autre caractéristique des props est qu'ils sont en lecture seule, c'est-à-dire qu'ils sont immuables. Ils ne vont pas être modifiés à l'intérieur du composant dans lequel ils sont passés. Le flux de données est également unidirectionnel — ce qui nous donne une liaison de données à sens unique (contrairement à Angular).

Mais il peut y avoir des cas où nous voulons changer les données (comme dans un événement par l'utilisateur, etc.). Par conséquent, pour ce cas, l'« État » entre dans le marché React. Plongeons dedans.

### State

Comme je vous l'ai dit, les props sont immuables alors que l'état est pour les données mutables — c'est-à-dire les données qui changeront en réponse à certains événements. Donc, si vous voulez changer la valeur de vos données, alors stockez-les dans l'état. Les états sont des objets qui stockent les données de votre composant. Pour donner une meilleure image de la façon dont l'état est défini et comment l'utiliser, voici un exemple :

```
class LoginContainer extends React.Component {
      constructor(props) {  
          super(props);  
              this.state = {   
                 userName: "",  
               };
      }
onFilluserName = event => {   
     this.setState({    
          userName: event.target.value,   
     });
}
render() {  
    return (  
       <div>    
          <input value={this.state.userName} onChange=          {this.onFilluserName}   
       </div>   
     ); 
   }
}
```

Vous pouvez voir dans l'exemple ci-dessus que l'état représente des objets où les données de votre composant sont stockées. Ils sont initialisés à l'intérieur d'un constructeur. Vous pouvez accéder à l'état en utilisant 'this.state'. C'est la façon d'utiliser l'état pour afficher vos données dans votre composant.

Mais je vous ai dit que ce qui fait de l'état le cœur de vos composants est son comportement mutable. Oui, maintenant vient le point de savoir comment nous pouvons changer la propriété de l'état. La réponse est d'utiliser 'this.setState' (veuillez jeter un coup d'œil à l'exemple ci-dessus). En utilisant this.setState, nous avons changé notre valeur de données lorsque l'utilisateur tape.

En résumé, les props et l'état sont tous deux des sources de données, mais leur utilisation et leur comportement sont différents. Chaque fois qu'il y a un cas où vos données peuvent changer, utilisez l'« état » pour cela — sinon le « prop » est un bon choix.

C'est tout sur les bases du monde React. J'espère que vous avez une meilleure compréhension des bases.

Il y a une partie très importante d'un composant de classe que je n'ai pas discutée : les méthodes de cycle de vie. Oui, les méthodes de cycle de vie sont une autre partie critique de ReactJS, mais ce qu'elles sont et pourquoi elles sont importantes sera dans mon prochain article !

Merci d'avoir lu.