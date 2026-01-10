---
title: Le chemin vers Redux et retour
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-05T21:48:28.000Z'
originalURL: https://freecodecamp.org/news/the-road-to-redux-and-back-d9987c7bb894
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb401740569d1a4cacccc.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le chemin vers Redux et retour
seo_desc: 'By Jeff M Lowery

  Why I decided to go back to vanilla React

  I’ve done some prototype work to demonstrate the benefits of a data access layer
  between client logic and persistence. Along the way, I’ve become a big fan of GraphQL.
  Though I like React, it...'
---

Par Jeff M Lowery

#### _Pourquoi j'ai décidé de revenir à React vanilla_

J'ai fait quelques travaux de prototype pour démontrer les avantages d'une couche d'accès aux données entre la logique client et la persistance. En cours de route, je suis devenu un grand fan de GraphQL. Bien que j'aime React, ce n'était pas l'approche low(er)-code que j'espérais (mais, hey : pas de jQuery !). J'ai essayé de mélanger Redux pour simplifier davantage le codage, mais il y a eu des déceptions là aussi.

React est conceptuellement simple : un composant peut contenir un _état_ et recevoir des _props_. React surveillera les changements d'état et re-rendra ce composant et _tout composant enfant_ qui pourrait être affecté par le changement d'état. L'état est passé aux enfants via les props (attributs d'élément). Certaines méthodes de composant React intégrées sont appelées dans le processus, chacune pouvant être remplacée si nécessaire (pour éviter, par exemple, des re-rendus inutiles).

L'une des premières ressources auxquelles je me suis tourné lors de l'apprentissage de React était [la série de Bucky Roberts](https://www.youtube.com/watch?v=4ZAEBxGipoA). Bucky fait un bon travail en expliquant les concepts simplement et informellement. Vous comprenez l'essentiel de React, ce dont vous avez besoin pour commencer.

Ainsi armé, j'ai écrit du code React. Au début, cela s'est très bien passé. Pourtant, à mesure que ma hiérarchie de composants devenait plus complexe, suivre la hiérarchie des relations de chaque composant, ainsi que toutes les props transmises, est devenu confus.

![Image](https://cdn-media-1.freecodecamp.org/images/xol0AVVLsH43U7J7T0AUC57qUZZsvReKvZkk)
_<section> et <aside> sont-ils dans le même conteneur ? Et <nav> ?_

Lors de l'apprentissage de React, il est utile de faire une distinction claire entre les **composants de présentation** et les **composants conteneurs**. Les composants de présentation sont les éléments affichés sur la page. Les composants conteneurs sont ceux qui maintiennent l'état pour leurs composants enfants. Les composants conteneurs peuvent être de présentation, conteneurs, ou les deux. Les conteneurs sont intelligents et ont une logique d'état. Les composants de présentation sont simples et sont principalement des modèles HTML qui gèrent la présentation des props transmises.

Au début, il peut être difficile de voir quels composants s'influencent mutuellement et partagent un état, et doivent donc appartenir au même conteneur. Vous devrez réorganiser l'état et refaire le passage des propriétés, à mesure qu'il devient plus clair quels composants doivent travailler ensemble. C'est ce qu'on appelle le "[refactoring](http://erikaybar.name/refactoring-react-extracting-layout-components/)".

### Props, props, et encore des props

Tous les changements passent par les propriétés. La plupart des tutoriels montrent cela en passant chaque prop par son nom depuis le composant conteneur racine vers tous les enfants, où chaque composant enfant sélectionne les propriétés qu'il veut et ignore le reste.

Prenons un exemple des docs de React :

```js
function Welcome(props) {
  return <h1>Bonjour, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}
```

Le composant **Welcome** prend un ensemble de propriétés ou props. Il utilise la prop appelée **name** pour afficher un message de bienvenue personnalisé. Le composant conteneur est un <div> anonyme. Il passe les noms au composant **Welcome** pour trois personnes.

C'est très bien. Mais que se passe-t-il lorsque vous voulez afficher non seulement le prénom, mais aussi le nom, l'adresse, l'email et le numéro de téléphone dans le composant **Welcome** ?

```js
function Welcome(props) {
  return <div>
     <h1>Bonjour, {props.first_name} {props.last_name}</h1>
     <ul>
       <li> email: {props.email} </li>
       <li> téléphone: {props.phone} </li>
       <li> adresse: /* omis par pitié */ </li>
     </ul>
  </div>;
}

function App() {
  return (
    <div>
      <Welcome first_name="Sara" last_name="Smith" email="...", phone="...", address={/* objet adresse */}/>
      <Welcome first_name="Cahal" last_name="Murthi" email="...", phone="...", address={/* objet adresse */}/>
      <Welcome first_name="Edite" last_name="Franco" email="...", phone="...", address={/* objet adresse */}/>
    </div>
  );
}
```

Passer explicitement les props est bruyant. De plus, si le composant Welcome est une composition de plusieurs autres composants, chacun avec son propre ensemble de propriétés nécessaires, vous devez également les passer au composant Welcome.

Les props ne sont pas seulement des données, mais aussi des méthodes. Les props sont **immuables** par convention.

Si un enfant veut changer une propriété, cela doit être fait via une méthode de définition transmise depuis un conteneur qui détient l'état. L'enfant appelle la méthode de définition de l'état, met à jour l'état et génère de nouvelles valeurs de prop. Ensuite, chaque enfant est notifié des changements de propriété. L'enfant qui effectue la mutation de l'état ne sait pas quel conteneur détient l'état, mais n'a pas besoin de le savoir. Il appelle la méthode de définition qui lui est donnée depuis un conteneur parent anonyme.

Voici un autre exemple des docs de React :

```js
class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};
    
// Cette liaison est nécessaire pour que `this` fonctionne dans le callback
    this.handleClick = this.handleClick.bind(this);
  }
  
  handleClick() {
    this.setState(prevState => ({
      isToggleOn: !prevState.isToggleOn
    }));
  }
  
  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}

ReactDOM.render(
  <Toggle />,
  document.getElementById('root')
);
```

Bien que dans ce cas le bouton ait un accès direct à l'état, le cas courant est que l'état est passé en tant que propriétés au composant de présentation enfant Button, avec une méthode de définition supplémentaire pour changer isToggleOn dans l'état de ce composant.

```js
handleClick() {
    this.setState(prevState => ({
      isToggleOn: !prevState.isToggleOn
    }));
  }

render() => <Button 
  onclick=handleClick.bind(this)
  isToggleOn=this.state.isToggleOn />;

ReactDOM.render(
  <Toggle />,
  document.getElementById('root')
);
```

### Arrggh, refactoring

Vous faites donc toute cette propagation de propriétés à travers tous les composants enfants et tout est beau. Ensuite, vous ajoutez un composant de plus, et vous réalisez qu'il dépend d'un état qui n'est pas dans le conteneur où vous voulez mettre le nouveau composant.

Commençons par une application simple Liste et Détails :

![Image](https://cdn-media-1.freecodecamp.org/images/CunCd6YnnGJxF2tXBUz2tQVPQeY1Eu6BQUEf)
_Alors que je choisis des éléments dans la Liste, cela met à jour les Détails (je ne suis pas un web designer)_

Alors que des éléments sont choisis dans la Liste, une notification est envoyée au Conteneur via un mutateur qui a été envoyé en tant que prop, et l'état du Conteneur est changé. Cela provoque le re-rendu de la Liste et des Détails. Les Détails sont notifiés de l'élément sélectionné dans la Liste dans le cadre de cette opération de re-rendu, et sont mis à jour avec les nouvelles informations de l'élément.

Maintenant, nous décidons plus tard que nous voulons ajouter un Filtre à la Liste. Nous ajoutons un nouveau conteneur pour gérer l'état du Filtre, comme un contrôle radio. Lorsqu'un Filtre est changé, il met à jour l'état du Sous-conteneur, ce qui provoque le re-rendu de la Liste. Le conteneur le plus externe contient maintenant le Sous-conteneur au lieu de la Liste. Il contient toujours le composant Détails, mais la gestion de l'état de l'élément Liste sélectionné reste la même. Le Conteneur ne sait rien du Filtre.

![Image](https://cdn-media-1.freecodecamp.org/images/Fv624PMr61S23V7Z1y1lZLJa6IugDfwaGsox)
_Ajout d'un Filtre et d'un nouveau Sous-conteneur_

Rien n'a beaucoup changé. Le Conteneur a maintenant un Sous-conteneur plutôt qu'une Liste, mais les mêmes props sont passées au nouveau composant enfant. Chaque conteneur a son propre état qu'il gère.

Cependant... plus tard, nous réalisons que savoir quel Filtre est appliqué affectera les Détails que nous affichons, mais comme le Filtre est un frère des Détails, les Détails n'auront pas accès à l'état du Filtre. Donc maintenant le choix est :

1. faire en sorte que les éléments de la Liste contiennent des informations sur ce par quoi ils sont filtrés
2. pousser l'état du Filtre du Sous-conteneur vers le Conteneur

C'est le refactoring React. Tout ce qui partage un état doit être dans le même conteneur (à un certain niveau). Il n'y a rien de mal avec le concept, mais vous ne le faites jamais correctement du premier coup. De plus, les composants ne restent pas longtemps au même endroit à mesure que l'application évolue.

#### Porter de l'eau

Les conteneurs sont des facilitateurs, passant des connaissances entre les composants enfants. Lorsque les faits changent, les composants sont redessinés. Mais ils sont aussi indiscrets que bruyants. Ils savent tout ce qui intéresse leurs enfants, mais cela ne fait pas d'eux de bons parents. [J'ai déjà écrit à ce sujet](https://medium.com/@jefflowery/carrying-water-4dee1ddb7eae), où une telle connaissance n'est pas toujours une bonne chose.

### Solution 1 : Redux

Une solution est de ne pas avoir autant d'états. Pourquoi ne pas en avoir qu'un seul ? Eh bien, si vous vous souvenez, chaque changement d'état notifiera les enfants qu'une propriété a changé. C'est au composant enfant de savoir si cette propriété affecte ce qu'ils affichent. Mais la notification est envoyée quoi qu'il arrive.

Plutôt que le conteneur suppose qu'il sait quelles propriétés sont passées aux enfants, pourquoi ne pas avoir une inversion de contrôle où les enfants disent quelles propriétés les intéressent, et s'abonnent donc à ces changements d'état et à ces changements d'état uniquement.

#### Un état pour les gouverner tous

C'est là que Redux intervient. Il fournit à tous les composants un seul état, maintenu indépendamment mais accessible par tous les composants React.

Redux introduit plusieurs nouveaux éléments. Le premier est le conteneur d'état, appelé le Store. Le Store est connecté à votre application via un Provider. Ces deux éléments sont "définis et oubliés". Une fois que quelques lignes de code sont écrites, vous ne les touchez plus jamais.

```js
import React from 'react'
import ReactDOM from 'react-dom'
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import RootReducer from './app/reducers'
import App from './app/app'

const store = createStore(RootReducer)

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)
```

Les deux autres parties sont un peu plus impliquées : Actions et Reducers. Un événement tel qu'une frappe de touche ou un résultat de requête de base de données crée une Action. L'Action est ensuite dispatchée pour être gérée par un Résolveur, en fonction du type d'Action. Si vous lisez [ma série précédente](https://medium.freecodecamp.org/follow-the-rules-with-seneca-b3cf3d08fe5d) sur les microservices Seneca, vous remarquerez comment les Actions Redux sont similaires aux motifs Seneca, et les Reducers sont similaires aux Actions Seneca.

Les Reducers, une fois déclenchés, modifieront l'état Redux selon les données dans le message d'Action. Ainsi, un composant peut lancer une Action qui pourrait invoquer une requête de base de données ou une récupération de fichier, les résultats de laquelle sont attachés à l'Action en tant que payload et ensuite dispatchés au nuage de Reducers, dont l'un (espérons-le) reprendra là où l'Action s'est arrêtée et modifiera une partie de l'État afin que les composants écoutant des parties de celui-ci aient l'opportunité d'être re-rendus.

Il n'y a pas de passage de props des conteneurs aux enfants, mais les props sont toujours impliqués.

```js
import { connect } from 'react-redux'
import { setVisibility } from '../actions'
import Popup from '../components/Popup'
const mapStateToProps = (state, ownProps) => {
  return {
    active: ownProps.toggle === state.visibilityToggle
  }
}
const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    onClick: () => {
      dispatch(setVisibility(ownProps.toggle))
    }
  }
}
const Toggle = connect(
  mapStateToProps,
  mapDispatchToProps
)(Popup)
export default Toggle
```

Dans l'exemple ci-dessus, un composant Popup est lié à l'État via des mappages de propriétés utilisant les méthodes de l'API Redux mapDispatchToProps et mapStateToProps. Ce code serait très probablement inclus dans un conteneur du composant Popup. Plus d'informations à ce sujet plus tard.

La manière traditionnelle d'organiser cela est d'avoir des Actions dans un dossier **/actions**. Habituellement, un fichier index.js se trouve dans ce dossier qui importe toutes les actions afin qu'elles puissent être importées en une seule ligne dans les dépendants qui en ont besoin. Les Reducers se trouvent dans un dossier **/reducers**. Les composants se trouvent dans un dossier **/components** ou sont divisés entre les composants de "présentation" **/components** et **/containers**. Et l'application sera dans le dossier racine.

#### Tout ce câblage, cependant

Vous vous retrouvez donc avec des fichiers d'action avec des constantes qui identifient les Actions dans le fichier, et des Reducers qui utilisent ces constantes pour recevoir et gérer les types d'Action. Chaque composant traitant l'état est câblé pour déclencher ces actions, ainsi que les propriétés qui sont affectées par le changement d'état.

C'est très bien, jusqu'à ce que vous commenciez à construire des composants et que les choses ne fonctionnent pas correctement et que vous vous demandez des choses comme :

* Ai-je pensé à définir l'action ?
* Ai-je pensé à exporter l'action ?
* Ai-je défini le reducer ?
* Ai-je inclus la constante d'action dans mon composant ?
* L'ai-je importée dans mon reducer ?
* Ai-je fait une faute de frappe ?
* Quel était le nom de ce fichier qui avait cette chose que j'ai oubliée maintenant ?

Yeesh ! Vous finissez par faire beaucoup de recherches dans votre code, en supposant que vous pouvez vous souvenir de ce que vous recherchez. Une solution au problème [est de rendre les Actions et les Reducers co-localisés](https://medium.com/@TuckerConnelly/simplifying-redux-architecture-cd50426c941a). Ils sont codépendants, donc les définir dans un fichier commun a du sens.

### Solution 2 : Retour à React avec ES6

Alors que je commençais à maîtriser Redux, j'ai remarqué que d'autres utilisaient des techniques qui, si je les avais eues à l'esprit à l'époque, auraient rendu le travail avec React vanilla beaucoup plus facile. Donc, avec Redux n'étant pas moins low-code que React seul (rappelons, je travaille juste sur un simple prototype), j'abandonne Redux.

#### Spread et rest

Dans [Carrying Water](https://medium.com/@jefflowery/carrying-water-4dee1ddb7eae), je mentionne la différence entre le transport actif et passif des données en transit. Le premier est mauvais, mais le second est acceptable, car il évite le couplage serré. Les données sont simplement transmises au destinataire prévu. C'est la différence entre le bureau de poste ouvrant un colis et réemballant tout ce qu'il contient dans leurs propres colis, versus simplement envoyer le colis sur son chemin.

[En utilisant l'opérateur de propagation d'objet](https://zhenyong.github.io/react/docs/transferring-props.html), il est possible de transmettre des propriétés aux enfants sans référence explicite aux propriétés elles-mêmes. Bien que cela "porte toujours de l'eau" du conteneur aux sous-composants, cela le fait de manière implicite. Tout ce que le conteneur sait, c'est qu'il a des props à envoyer. S'il a un état, il envoie aussi ceux-ci.

Il faut cependant mentionner que l'opérateur de propagation pour les objets n'est pas encore une partie officielle d'ECMAScript. Le transpileur Babel le supporte, s'il est configuré pour le faire.

```js
{
 "presets": [
  "latest",
  "react"
 ],
 "plugins": ["transform-object-rest-spread", "syntax-object-rest-spread"]
}
```

#### Sélection des propriétés

Une préoccupation est celle de transmettre trop d'informations aux composants enfants. Une façon d'éviter cela est que les conteneurs et composants de niveau supérieur "sélectionnent" les propriétés qui les intéressent, et ne transmettent que le reste. Cela peut être fait par la déstructuration d'objet :

```js
var { checked, ...other } = props;
```

Ici, la prop checked est extraite des autres props, puis other est transmise (sans la prop checked [exemple de [le lien](https://zhenyong.github.io/react/docs/transferring-props.html) ci-dessus]) :

```js
function FancyCheckbox(props) {
  var { checked, ...other } = props;
  var fancyClass = checked ? 'FancyChecked' : 'FancyUnchecked';
  // `other` contient { onClick: console.log } mais pas la propriété checked
  return (
    <div {...other} className={fancyClass} />
  );
}
```

### React ou Redux ?

Lors de la construction d'un prototype pour démontrer un concept ou une fonctionnalité, plus simple est mieux. React est conceptuellement plus facile à gérer. Redux a beaucoup de choses qui se passent sous le capot, et il a été noté à quel point les actions peuvent devenir fines. Besoin d'afficher un spinner ? Déclenchez une action !).

Les outils entourant Redux [s'améliorent](http://dev.apollodata.com/react/redux.html), et [simplifieront](https://github.com/anshulsahni/simplify-redux) la surcharge de maintenance des actions, des reducers, de mapStateToProps et de matchDispatchToProps, en utilisant [une approche plus déclarative](https://github.com/nstraub/simple-react-redux) pour assembler les pièces et en utilisant des règles implicites pour le câblage fastidieux.