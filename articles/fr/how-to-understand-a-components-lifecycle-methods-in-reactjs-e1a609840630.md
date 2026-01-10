---
title: Comment comprendre les méthodes du cycle de vie d'un composant dans ReactJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:48:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-a-components-lifecycle-methods-in-reactjs-e1a609840630
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_drMYY_IEgboMS4RhvC-lQ.png
tags:
- name: JavaScript
  slug: javascript
- name: lifecycle methods
  slug: lifecycle-methods
- name: General Programming
  slug: programming
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: Comment comprendre les méthodes du cycle de vie d'un composant dans ReactJS
seo_desc: 'By Anchal Nigam

  In this article, we are going to explore the lifecycle methods of ReactJS. But,
  before moving ahead to React’s different lifecycle methods, we should understand
  what it is.

  As we know, everything in this world follows a cycle (say hum...'
---

Par Anchal Nigam

Dans cet article, nous allons explorer les méthodes du cycle de vie de ReactJS. Mais avant de passer aux différentes méthodes du cycle de vie de React, nous devons comprendre ce que c'est.

Comme nous le savons, tout dans ce monde suit un cycle (comme les humains ou les arbres). Nous naissons, grandissons et puis mourons. Presque tout suit ce cycle dans sa vie, et les composants React aussi. Les composants sont créés (montés sur le DOM), grandissent en étant mis à jour, et puis meurent (démontés du DOM). Cela est appelé **le cycle de vie d'un composant**.

Il existe différentes méthodes du cycle de vie que React fournit à différentes phases de la vie d'un composant. React appelle automatiquement la méthode responsable selon la phase dans laquelle se trouve le composant. Ces méthodes nous donnent un meilleur contrôle sur notre composant et nous pouvons les manipuler en utilisant ces méthodes.

Maintenant, nous savons ce que sont les méthodes du cycle de vie et pourquoi elles sont importantes. Alors, quelles sont ces différentes méthodes ? Jetons un coup d'œil.

### Méthodes du cycle de vie

Le cycle de vie d'un composant est généralement classé en quatre parties :

* **initialisation**
* **montage**
* **mise à jour, et**
* **démontage**.

Discutons des différentes méthodes du cycle de vie disponibles à ces différentes phases (c'est-à-dire, initialisation, montage, mise à jour et démontage).

#### **Initialisation**

C'est la phase dans laquelle le composant va commencer son parcours en configurant l'état (voir ci-dessous) et les props. Cela est généralement fait à l'intérieur de la méthode constructeur (voir ci-dessous pour mieux comprendre la phase d'initialisation).

```
class Initialize extends React.Component {
    constructor(props)
    {
    // Appel du constructeur de
    // la classe parente React.Component
    super(props);
    // processus d'initialisation
    this.state = {
       date : new Date(),
       clickedStatus: false
     };
}
```

#### **Montage**

Le nom est explicite. Le montage est la phase dans laquelle notre composant React est monté sur le DOM (c'est-à-dire, créé et inséré dans le DOM).

Cette phase intervient après que la phase d'initialisation soit terminée. Dans cette phase, notre composant est rendu pour la première fois. Les méthodes disponibles dans cette phase sont :

**1. componentWillMount()**

Cette méthode est appelée juste avant qu'un composant soit monté sur le DOM ou que la méthode render soit appelée. Après cette méthode, le composant est monté.

Note : Vous ne devriez pas faire d'appels API ou de modifications de données en utilisant this.setState dans cette méthode car elle est appelée avant la méthode render. Donc, rien ne peut être fait avec le DOM (c'est-à-dire, mettre à jour les données avec la réponse de l'API) car il n'a pas encore été monté. Par conséquent, nous ne pouvons pas mettre à jour l'état avec la réponse de l'API.

**2. componentDidMount()**

Cette méthode est appelée après que le composant soit monté sur le DOM. Comme componentWillMount, elle est appelée une fois dans un cycle de vie. Avant l'exécution de cette méthode, la méthode render est appelée (c'est-à-dire, nous pouvons accéder au DOM). Nous pouvons faire des appels API et mettre à jour l'état avec la réponse de l'API.

Jetez un coup d'œil pour comprendre ces méthodes de montage :

```
class LifeCycle extends React.Component {
  componentWillMount() {
      console.log('Le composant va être monté !')
   }
  componentDidMount() {
      console.log('Le composant a été monté !')
      this.getList();
   }
  getList=()=>{
   /*** méthode pour faire un appel API ***/
  }
  render() {
      return (
         <div>
            <h3>Bonjour les méthodes de montage !</h3>
         </div>
      );
   }
}
```

#### **Mise à jour**

C'est la troisième phase par laquelle passe notre composant. Après la phase de montage où le composant a été créé, la phase de mise à jour entre en scène. C'est là que l'état du composant change et donc, un nouveau rendu a lieu.

Dans cette phase, les données du composant (état et props) sont mises à jour en réponse à des événements utilisateur comme des clics, de la saisie, etc. Cela entraîne le nouveau rendu du composant. Les méthodes disponibles dans cette phase sont :

1. **shouldComponentUpdate()**

Cette méthode détermine si le composant doit être mis à jour ou non. Par défaut, elle retourne vrai. Mais à un moment donné, si vous voulez re-rendre le composant sous certaines conditions, alors la méthode shouldComponentUpdate est le bon endroit.

Supposons, par exemple, que vous voulez seulement re-rendre votre composant lorsqu'il y a un changement dans une prop — alors utilisez le pouvoir de cette méthode. Elle reçoit des arguments comme nextProps et nextState qui nous aident à décider si nous devons re-rendre en faisant une comparaison avec la valeur actuelle de la prop.

**2. componentWillUpdate()**

Comme les autres méthodes, son nom est également explicite. Elle est appelée avant que le nouveau rendu du composant ait lieu. Elle est appelée une fois après la méthode '**shouldComponentUpdate**'. Si vous voulez effectuer un calcul avant le nouveau rendu du composant et après la mise à jour de l'état et des props, alors c'est le meilleur endroit pour le faire. Comme la méthode '**shouldComponentUpdate**', elle reçoit également des arguments comme nextProps et nextState.

**3. ComponentDidUpdate()**

Cette méthode est appelée juste après le nouveau rendu du composant. Après que le nouveau composant (mis à jour) soit mis à jour sur le DOM, la méthode '**componentDidUpdate**' est exécutée. Cette méthode reçoit des arguments comme prevProps et prevState.

Jetez un coup d'œil pour mieux comprendre les méthodes de mise à jour :

```
class LifeCycle extends React.Component {
      constructor(props)
      {
        super(props);
         this.state = {
           date : new Date(),
           clickedStatus: false,
           list:[]
         };
      }
      componentWillMount() {
          console.log('Le composant va être monté !')
       }
      componentDidMount() {
          console.log('Le composant a été monté !')
          this.getList();
       }
      getList=()=>{
       /*** méthode pour faire un appel API ***/
       fetch('https://api.mydomain.com')
          .then(response => response.json())
          .then(data => this.setState({ list:data }));
      }
       shouldComponentUpdate(nextProps, nextState){
         return this.state.list!==nextState.list
        }
       componentWillUpdate(nextProps, nextState) {
          console.log('Le composant va être mis à jour !');
       }
       componentDidUpdate(prevProps, prevState) {
          console.log('Le composant a été mis à jour !')
       }
      render() {
          return (
             <div>
                <h3>Bonjour les méthodes du cycle de vie de montage !</h3>
             </div>
          );
       }
}
```

#### **Démontage**

C'est la dernière phase du cycle de vie du composant. Comme le nom l'indique clairement, le composant est démonté du DOM dans cette phase. La méthode disponible dans cette phase est :

**1. componentWillUnmount()**

Cette méthode est appelée avant que le démontage du composant ait lieu. Avant la suppression du composant du DOM, '**componentWillUnMount**' est exécutée. Cette méthode marque la fin du cycle de vie du composant.

Voici une représentation schématique des méthodes du cycle de vie :

![Image](https://cdn-media-1.freecodecamp.org/images/NpWCjYyzfnJkn7rXwDmyWwK2DqInFJu6-g1O)

C'est tout sur cette partie importante du monde React — les méthodes du cycle de vie. J'espère que vous avez apprécié la lecture.

Merci !