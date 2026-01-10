---
title: Exploration du quoi et du pourquoi de Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-20T09:55:16.000Z'
originalURL: https://freecodecamp.org/news/exploring-the-what-and-the-why-of-redux-6faadab4768b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*K7bBVfi4k9a7wUci_nCg-w.jpeg
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
seo_title: Exploration du quoi et du pourquoi de Redux
seo_desc: 'By Peter Mbanugo


  “What in the world is Redux and why do I need it?”


  I asked myself this question when I started learning how to build single page apps
  (SPA) to include rich interaction on my apps. SPA has the ability to re-render different
  parts of...'
---

Par Peter Mbanugo

> « Qu'est-ce que Redux et pourquoi en ai-je besoin ? »

Je me suis posé cette question lorsque j'ai commencé à apprendre à construire des applications monopages (SPA) pour inclure des interactions riches dans mes applications. Les SPA ont la capacité de réafficher différentes parties de l'interface utilisateur sans nécessiter un aller-retour vers le serveur.

Cela est réalisé en séparant les différentes données, qui représentent l'état de l'application, de la présentation de ces données.

La couche **vue** rend une représentation de ces données à l'interface utilisateur. Une vue peut être composée de différents composants. Par exemple, considérons une boutique en ligne avec une page de liste de produits. La page pourrait contenir des composants qui représentent les différents produits et leurs prix, un compteur visuel du nombre total d'articles dans le panier, et un composant pour suggérer des produits similaires aux articles achetés.

La couche **modèle** contient les données à rendre par la couche vue. Chaque composant de la vue est indépendant des autres, chacun rendant un ensemble prévisible d'éléments d'interface utilisateur pour les données données, mais plusieurs composants peuvent partager les mêmes données. Lorsqu'il y a un changement dans le modèle, la vue se réaffiche et met à jour le composant affecté par la mise à jour du modèle.

### Le Problème

L'état de l'application peut être stocké dans des objets aléatoires en mémoire. Il est également possible de conserver certains états dans le DOM.

Mais avoir l'état dispersé peut facilement conduire à un code ingérable. Il devient difficile à déboguer. Si plusieurs vues ou composants partagent des données similaires, il est possible que ces données soient stockées à un emplacement mémoire différent, et les composants de vue ne seront pas synchronisés les uns avec les autres.

Avec une séparation des vues et des modèles, les données sont transmises du modèle à la vue. Si des changements sont effectués en fonction des interactions de l'utilisateur, cela mettra à jour le modèle et cette mise à jour du modèle pourrait éventuellement déclencher une mise à jour d'un autre modèle et également mettre à jour un autre composant de vue qui peut également déclencher une mise à jour d'un modèle.

L'un des problèmes connus avec ce flux de données imprévisible était le bug de notification sur Facebook. Lorsque vous êtes connecté à Facebook, vous voyez une notification pour de nouveaux messages. Lorsque vous la lisez, la notification disparaît. Après certaines interactions sur le site, la notification réapparaît, puis vous vérifiez et il n'y a pas de nouveaux messages et la notification disparaît. Lorsque vous interagissez davantage avec l'application, la notification réapparaît et cela continue en cycle.

### L'Objectif

Il est facile d'ajouter de la complexité au code si l'état n'est pas géré correctement. Par conséquent, il est préférable d'avoir un seul endroit où les données résident, en particulier lorsque les mêmes données doivent être affichées à plusieurs endroits dans la vue. Avec un flux de données désordonné, il devient difficile de raisonner sur les changements d'état et de prédire le résultat possible d'un changement d'état.

### La solution : Flux de données unidirectionnel et source unique de vérité

Les composants de vue doivent lire les données à partir de cette source unique et ne pas conserver leur propre version du même état séparément. D'où le besoin d'une **source unique de vérité**.

Chez Facebook, ils voulaient un moyen plus facile de prédire les changements d'état et ont donc créé un modèle appelé **Flux**. Flux est un modèle de couche de données pour gérer le flux de données. Il stipule que les données ne doivent circuler que dans une seule direction, avec l'état de l'application contenu dans un seul emplacement — la source de vérité — et la logique pour modifier l'état juste à un seul endroit.

**Flux**

![Image](https://cdn-media-1.freecodecamp.org/images/s4L26593yAq7tsGDmN8h03mSiso2epkS78dY)

Le diagramme ci-dessus décrit le flux de données dans Flux :

* Les données circulent du **store** — source de vérité — vers la **vue**. La vue lit les données et les présente à l'utilisateur, l'utilisateur interagit avec différents composants de vue et s'il doit modifier l'état de l'application, il exprime son intention de le faire par une **action**.
* L'action capture les façons dont quelque chose pourrait interagir avec votre application. C'est un objet simple avec un champ « type » et certaines données. Le **dispatcher** est responsable de l'émission de l'action vers le store. Il ne contient pas la logique pour changer l'état, mais plutôt, le store lui-même fait cela en interne.
* Vous pouvez avoir plusieurs stores, chacun contenant des données pour les différents domaines de l'application. Le store répond aux actions pertinentes pour l'état qu'il maintient. S'il met à jour l'état, il notifie également les vues connectées à ce store en émettant un événement.
* La vue reçoit la notification et récupère les données du store, puis se réaffiche. Lorsque l'état doit être mis à jour à nouveau, il passe par le même cycle, permettant une manière facile de raisonner sur votre application et de rendre les changements d'état prévisibles.

En implémentant une architecture d'application qui permet aux données de circuler uniquement dans une seule direction, vous créez des états d'application plus prévisibles. Si un bug apparaît, un flux de données unidirectionnel facilitera grandement l'identification de l'erreur, car les données suivent un canal strict.

**Redux**
Il existe diverses implémentations de ce modèle. Nous avons [Fluxxor](http://fluxxor.com/), [Flummox](https://github.com/acdlite/flummox/), [Reflux](https://github.com/spoike/refluxjs), et plus encore. Mais Redux se distingue parmi eux tous.

Redux a pris les concepts de Flux et les a fait évoluer pour créer une bibliothèque de gestion d'état prévisible.

Dan Abramov, le créateur de Redux, l'a créé avec l'intention d'obtenir un meilleur support des outils de développement, [le rechargement à chaud et le débogage de voyage dans le temps](https://www.youtube.com/watch?v=xsSnOQynTHs) tout en conservant la prévisibilité qui vient avec Flux. Redux tente de rendre les mutations d'état prévisibles.

Redux, suivant les traces de Flux, a trois concepts :

* **Source Unique de Vérité** : J'ai mentionné le besoin de cela. Redux a ce qu'il appelle le **store**. Le store est un objet qui contient tout l'état de votre application. Les différentes parties de l'état sont stockées dans un arbre d'objets. Cela facilite la mise en œuvre de l'annulation/du rétablissement.

Par exemple, nous pouvons stocker et suivre les articles dans un panier d'achat ainsi que le produit actuellement sélectionné avec Redux, et cela peut être modélisé dans le store comme suit :

```
{        "cartItem" : [            {                "productName" : "laser",                "quantity" : 2            },            {                "productName" : "shirt",                "quantity" : 2            }        ],        "selectedProduct" : {            "productName" : "Smiggle",            "description" : "Lorem ipsum ... ",            "price" : "$30.04"        }    }
```

* **L'état est en lecture seule** : L'état ne peut pas être modifié directement par la vue ou tout autre processus (peut-être à la suite d'un rappel réseau ou d'un autre événement).

Pour changer l'état, vous devez exprimer votre intention en émettant une action. Une action est un objet simple décrivant votre intention, et il contient une propriété de type et certaines autres données. Les actions peuvent être enregistrées et rejouées plus tard, ce qui est bon pour le débogage et les tests.

En suivant notre exemple de panier d'achat, nous pouvons déclencher une action comme suit :

```
store.dispatch({      type: 'New_CART_ITEM',      payload: {                   "productName" : "Samsung S4",                   "quantity" : 2                }    })    dispatch(action) émet l'action, et est le seul moyen de déclencher un changement d'état. Pour récupérer l'arbre d'état, vous appelez store.getState().
```

* **Réducteur** : Les réducteurs sont responsables de déterminer quels changements d'état doivent se produire et de les transformer pour refléter les nouveaux changements.

Le réducteur est une fonction pure qui prend l'état précédent (l'état actuel sur le point d'être changé) et une action, détermine comment mettre à jour l'état en fonction du type d'action, le transforme et retourne l'état suivant (l'état mis à jour).

En continuant avec notre exemple de panier d'achat, disons que nous voulons ajouter un nouvel article au panier. Nous envoyons une action de type `**NEW_CART_ITEM**` et, dans le réducteur, nous déterminons comment traiter cette nouvelle demande de changement en lisant le type d'action et en agissant en conséquence.

Pour le panier d'achat, il ajoutera un nouveau produit au panier :

```
function shoppingCart(state = [], action) {      switch (action.type) {        case 'New_CART_ITEM':          return [...state, action.payload]        default:          return state      }    }
```

Ce que nous avons fait, c'est retourner un nouvel état qui est une collection des anciens articles du panier, en plus du nouveau provenant de l'action. Plutôt que de muter l'état précédent, vous devez retourner un nouvel objet d'état, et cela aide vraiment pour le débogage de voyage dans le temps.

Il y a des choses que vous ne devez jamais faire à l'intérieur d'un réducteur, et ce sont :

* Muter ses arguments.
* Effectuer des effets secondaires comme des appels API et des transitions de routage.
* Appeler des fonctions non pures.

### Un Exemple Pratique

Pour démontrer le fonctionnement de Redux, nous allons créer une SPA simple pour montrer comment nous pouvons gérer les données dans Redux et présenter les données en utilisant React.

Pour configurer, exécutez les commandes suivantes dans le terminal :

```
$ git clone git@github.com:StephenGrider/ReduxSimpleStarter.git    $ cd ReduxSimpleStarter    $ npm install
```

Nous venons de cloner un modèle de démarrage pour ce que nous allons construire dans cette section. Nous avons configuré React et téléchargé les packages npm Redux et react-redux. Nous allons construire une application qui nous permet de prendre des notes courtes sous forme d'éléments à faire ou de mots-clés qui nous rappellent quelque chose.

Les actions sont des objets JavaScript simples qui doivent avoir un type, et les réducteurs déterminent quoi faire en fonction de l'action spécifiée. Définissons des constantes pour contenir les différentes actions.

Créez un nouveau fichier appelé `types.js` dans `./src/actions` avec le contenu suivant :

```
export const FETCH = 'FETCH';    export const CREATE = 'CREATE';    export const DELETE = 'DELETE';
```

Ensuite, nous devons définir des actions et les envoyer lorsque nécessaire. Les créateurs d'actions sont des fonctions qui aident à créer des actions, et le résultat est passé à `dispatch()`.

Modifiez le fichier `index.js` dans le dossier des actions avec le contenu suivant :

```
import { FETCH, DELETE, CREATE } from './types';
```

```
    export function fetchItems() {      return {        type: FETCH      }    }
```

```
    export function createItem(item) {      let itemtoAdd = {        [Math.floor(Math.random() * 20)]: item      };
```

```
      return {        type: CREATE,        payload: itemtoAdd      }    }
```

```
    export function deleteItem(key) {      return {        type: DELETE,        payload: key      }    }
```

Nous avons défini trois actions pour créer, supprimer et récupérer des éléments du store. Ensuite, nous devons créer un réducteur. `Math.floor(Math.random() * 20` est utilisé pour attribuer une clé unique au nouvel élément ajouté. Ce n'est pas optimal, mais nous l'utiliserons ici juste pour cette démonstration.

Ajoutez un nouveau fichier dans le répertoire des réducteurs appelé `item-reducer.js` :

```
import _ from 'lodash';    import { FETCH, DELETE, CREATE } from '../actions/types';
```

```
    export default function(state = {}, action) {      switch (action.type) {        case FETCH:          return state;        case CREATE:          return { ...state, ...action.payload };        case DELETE:          return _.omit(state, action.payload);      }
```

```
      return state;    }
```

Ayant défini un réducteur, nous devons le connecter à notre application en utilisant la fonction `**combineReducer()**`.

Dans le dossier des réducteurs, ouvrez et modifiez le fichier `index.js` :

```
import { combineReducers } from 'redux';    import ItemReducer from './item-reducer';
```

```
    const rootReducer = combineReducers({      items: ItemReducer    });
```

```
    export default rootReducer;
```

Nous passons le réducteur que nous avons créé à la fonction `combinedReducer`, où la clé est la partie de l'état dont ce réducteur est responsable.

Rappelez-vous, les réducteurs sont des fonctions pures qui retournent une partie de l'état de l'application. Pour une application plus grande, nous pourrions avoir différents réducteurs, chacun pour un domaine d'application spécifique.

Avec la fonction `**combineReducer**`, nous disons à Redux comment créer notre état d'application. Donc, réfléchir et concevoir comment modéliser l'état de votre application dans Redux est quelque chose que vous devriez faire au préalable.

Avec Redux configuré pour gérer notre état, la prochaine chose est de connecter la Vue (qui est gérée par React) à Redux.

Créez un nouveau fichier `item.js` dans le répertoire **components**. Ce sera un composant intelligent car il sait comment interagir avec Redux pour lire l'état et demander un changement d'état.

Ajoutez le contenu ci-dessous à ce fichier :

```
import React, { Component } from 'react';    import { connect } from 'react-redux';    import * as actions from '../actions';
```

```
    class Item extends Component {      handleClick() {        this.props.deleteItem(this.props.id);      }
```

```
      render() {        return (          <li className="list-group-item">            {this.props.item}            <button              onClick={this.handleClick.bind(this)}              className="btn btn-danger right">              Delete            </button>          </li>        );      }    }
```

```
    export default connect(null, actions)(Item);
```

Ce composant affiche un élément et nous permet de le supprimer. La fonction `connect()` prend le composant React dans son état simple (il n'a aucune connaissance de Redux ni de la façon d'interagir avec lui) et produit un composant intelligent. Elle connecte les créateurs d'actions au composant de sorte que si un créateur d'action est appelé, l'action retournée est envoyée aux réducteurs.

Nous allons également créer un deuxième composant intelligent qui affichera le composant précédent sous forme de liste d'éléments et nous permettra également d'ajouter de nouveaux éléments.

Mettez à jour le fichier `app.js` dans le dossier des composants avec le contenu ci-dessous :

```
import _ from 'lodash';    import React, { Component } from 'react';    import { connect } from 'react-redux';    import * as actions from '../actions';    import Item from './item';
```

```
    class App extends Component {      state = { item: '' };
```

```
      componentWillMount() {        this.props.fetchItems();      }
```

```
      handleInputChange(event) {        this.setState({ item: event.target.value });      }
```

```
      handleFormSubmit(event) {        event.preventDefault();
```

```
        this.props.createItem(this.state.item, Math.floor(Math.random() * 20))      }
```

```
      renderItems() {        return _.map(this.props.items, (item, key) => {          return <Item key={key} item={item} id={key} />        });      }
```

```
      render() {        return (          <div>            <h4>Add Item</h4>            <form onSubmit={this.handleFormSubmit.bind(this)} className="form-inline">              <div className="form-group">                <input                  className="form-control"                  placeholder="Add Item"                  value={this.state.item}                  onChange={this.handleInputChange.bind(this)} />                <button action="submit" className="btn btn-primary">Add</button>              </div>            </form>            <ul className="list-group">              {this.renderItems()}            </ul>          </div>        );      }    }
```

```
    function mapStateToProps(state) {      return { items: state.items };    }
```

```
    export default connect(mapStateToProps, actions)(App)
```

Il s'agit d'un composant intelligent (ou **conteneur**) qui appelle le créateur d'action `fetchItems()` une fois que le composant est chargé. Nous avons également utilisé la fonction `connect` pour lier l'état de l'application dans Redux à notre composant React. Cela est réalisé en utilisant la fonction `mapStateToProps` qui prend l'objet de l'arbre d'état Redux comme paramètre d'entrée et mappe une partie de celui-ci (items) aux props du composant React. Cela nous permet d'y accéder en utilisant `this.props.items`. Le reste du fichier nous permet d'accepter l'entrée de l'utilisateur et de l'ajouter à l'état de l'application.

Exécutez l'application en utilisant `npm start` et essayez d'ajouter quelques éléments, comme dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/lM02K5jSbKEBTdtx11XowQmN5NNqxdCnm5e5)

### Résumé

Prendre en charge des interactions riches avec plusieurs composants sur une page signifie que ces composants ont de nombreux états intermédiaires. Les SPA ont la capacité de rendre et de redessiner n'importe quelle partie de l'interface utilisateur sans nécessiter un rechargement complet de la page et un aller-retour vers le serveur.

Si les données ne sont pas gérées correctement, dispersées dans l'interface utilisateur ou placées dans des objets aléatoires en mémoire, les choses peuvent facilement s'entremêler. Il est donc beaucoup mieux de séparer la vue et les modèles pour la vue.

Redux fait un bon travail en définissant clairement une manière de gérer vos données et la façon dont elles changent.

Il est guidé par trois principes fondamentaux, qui sont :

* Une source unique de vérité pour l'état de votre application.
* Un état en lecture seule pour garantir que ni les vues ni les rappels réseau n'écriront jamais directement dans l'état.
* Et transformer l'état par des fonctions pures, appelées réducteurs, pour la prévisibilité et la fiabilité.

Cela en fait un conteneur d'état prévisible pour les applications JavaScript.

### Lectures Complémentaires

* [Concepts Flux](https://github.com/facebook/flux/tree/master/examples/flux-concepts)
* [Commencer avec Redux](https://egghead.io/series/getting-started-with-redux)
* [Débogage de voyage dans le temps](https://www.youtube.com/watch?v=xsSnOQynTHs)

### Code Source

Trouvez le code source [ici](https://github.com/pmbanugo/Simple-Redux-Example).

Ceci a été initialement publié sur [Pusher](https://blog.pusher.com/the-what-and-why-of-redux/).