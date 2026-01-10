---
title: React.js pour débutants — Props et State expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-10T00:37:12.000Z'
originalURL: https://freecodecamp.org/news/react-js-for-beginners-props-state-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/Ekran-Resmi-2019-11-18-18.08.13.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
seo_title: React.js pour débutants — Props et State expliqués
seo_desc: 'By Cem Eygi

  React.js is one of the most widely used JavaScript libraries that every front-end
  developer should know. Understanding what props and state are and the differences
  between them is a big step towards learning React.

  In this blog post, I wi...'
---

Par Cem Eygi

React.js est l'une des bibliothèques JavaScript les plus utilisées que tout développeur front-end devrait connaître. Comprendre ce que sont les props et le state, ainsi que les différences entre eux, est une grande étape vers l'apprentissage de React.

Dans cet article de blog, je vais expliquer ce que sont les props et le state, et je vais également clarifier certaines des questions les plus fréquentes à leur sujet :

* Qu'est-ce que les props ?
* Comment passer des données avec les props ?
* Qu'est-ce que le state ?
* Comment mettre à jour le state d'un composant ?
* Que se passe-t-il lorsque le state change ?
* Puis-je utiliser le state dans chaque composant ?
* Quelles sont les différences entre les props et le state ?

> Si vous êtes un débutant complet en React, j'ai une série de tutoriels sur [React pour débutants](https://www.youtube.com/watch?v=nvhwG0Yk1AM&list=PLaz1hMFq311wfHYvJbcDpbms36jKpzFk9).

## Qu'est-ce que les props ?

Props est l'abréviation de properties et ils sont utilisés pour passer des données entre les composants React. Le flux de données de React entre les composants est unidirectionnel (du parent à l'enfant uniquement).

### Comment passer des données avec les props ?

Voici un exemple de la façon dont les données peuvent être passées en utilisant les props :

```javascript
class ParentComponent extends Component {    
    render() {    
        return (        
            <ChildComponent name="First Child" />    
        );  
    }
}

const ChildComponent = (props) => {    
    return <p>{props.name}</p>; 
};
```

Tout d'abord, nous devons définir/obtenir certaines données à partir du composant parent et les assigner à l'attribut "prop" d'un composant enfant.

```javascript
<ChildComponent name="First Child" />

```

"Name" est une prop définie ici et contient des données textuelles. Ensuite, nous pouvons passer des données avec des props comme si nous donnions un argument à une fonction :

```javascript
const ChildComponent = (props) => {  
  // instructions
};
```

Et enfin, nous utilisons la notation par points pour accéder aux données de la prop et les rendre :

```javascript
return <p>{props.name}</p>;
```

**Vous pouvez également regarder ma vidéo pour voir comment utiliser les props :**

%[https://www.youtube.com/watch?v=KvapOdsFK5A]

## Qu'est-ce que le state ?

React a un autre objet intégré spécial appelé state, qui permet aux composants de créer et de gérer leurs propres données. Ainsi, contrairement aux props, les composants ne peuvent pas passer de données avec le state, mais ils peuvent les créer et les gérer en interne.

Voici un exemple montrant comment utiliser le state :

```javascript
class Test extends React.Component {    
    constructor() {    
        this.state = {      
            id: 1,      
            name: "test"    
        };  
    }    
    
    render() {    
        return (      
            <div>        
              <p>{this.state.id}</p>        
              <p>{this.state.name}</p>      
            </div>    
        );  
    }
}
```

### Comment mettre à jour le state d'un composant ?

Le state ne doit pas être modifié directement, mais il peut être modifié avec une méthode spéciale appelée `setState()`.

```javascript
this.state.id = "2020"; // incorrect

this.setState({         // correct  
    id: "2020"
});
```

### Que se passe-t-il lorsque le state change ?

D'accord, pourquoi devons-nous utiliser `setState()` ? Pourquoi avons-nous même besoin de l'objet state lui-même ? Si vous vous posez ces questions, ne vous inquiétez pas, vous comprendrez bientôt le state :) Laissez-moi répondre.

Un changement dans le state se produit en fonction de l'entrée de l'utilisateur, du déclenchement d'un événement, etc. De plus, les composants React (avec state) sont rendus en fonction des données dans le state. Le state contient les informations initiales.

Ainsi, lorsque le state change, React est informé et ré-affiche immédiatement le DOM — **pas tout le DOM, mais seulement le composant avec le state mis à jour.** C'est l'une des raisons pour lesquelles React est rapide.

Et comment React est-il informé ? Vous l'avez deviné : avec `setState()`. La méthode `setState()` déclenche le processus de ré-affichage pour les parties mises à jour. React est informé, sait quelles parties changer et le fait rapidement sans ré-afficher tout le DOM.

En résumé, il y a 2 points importants auxquels nous devons prêter attention lors de l'utilisation du state :

* Le state ne doit pas être modifié directement — `setState()` doit être utilisé
* Le state affecte les performances de votre application et ne doit donc pas être utilisé inutilement

### Puis-je utiliser le state dans chaque composant ?

Une autre question importante que vous pourriez poser sur le state est de savoir exactement où nous pouvons l'utiliser. Dans les premiers jours, le state ne pouvait être utilisé que dans les **composants de classe**, et non dans les composants fonctionnels.

C'est pourquoi les composants fonctionnels étaient également connus sous le nom de composants sans état. Cependant, après l'introduction des **React Hooks**, le state peut maintenant être utilisé à la fois dans les composants de classe et fonctionnels.

Si votre projet n'utilise pas les React Hooks, alors vous ne pouvez utiliser le state que dans les composants de classe.

### Quelles sont les différences entre les props et le state ?

Enfin, faisons un récapitulatif et voyons les principales différences entre les props et le state :

* Les composants reçoivent des données de l'extérieur avec les props, alors qu'ils peuvent créer et gérer leurs propres données avec le state
* Les props sont utilisées pour passer des données, alors que le state est pour gérer des données
* Les données des props sont en lecture seule et ne peuvent pas être modifiées par un composant qui les reçoit de l'extérieur
* Les données de state peuvent être modifiées par leur propre composant, mais sont privées (ne peuvent pas être accessibles de l'extérieur)
* Les props ne peuvent être passées que du composant parent à l'enfant (flux unidirectionnel)
* La modification du state doit se faire avec la méthode `setState()`

React.js est aujourd'hui l'une des bibliothèques JavaScript les plus utilisées que tout développeur front-end devrait connaître.

J'espère que cet article vous aide à comprendre les props et le state. Il y a aussi d'autres choses importantes à couvrir sur React, et je continuerai à en écrire plus tard dans mes prochains articles.

**Si vous voulez en savoir plus sur le développement web, n'hésitez pas à** [**me suivre sur YouTube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)** !**

Merci pour votre lecture !