---
title: Comment afficher des modales dans React
subtitle: ''
author: Zubin Pratap
co_authors: []
series: null
date: '2018-12-20T17:12:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-render-modals-in-react-bbe9685e947e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*u_CfjHWpbDQH9ayWj8pwKg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment afficher des modales dans React
seo_desc: 'Modals can be a tricky topic in React because of the way React structures
  the DOM. If you’re familiar with the basics of React, you will know that the entire
  App is a component, usually called <App/> that gets gets appended as a child <div>
  called #r...'
---

Les modales peuvent être un sujet délicat dans React en raison de la manière dont React structure le DOM. Si vous êtes familier avec les bases de React, vous savez que l'ensemble de l'application est un composant, généralement appelé `<App/>` qui est ajouté en tant qu'enfant `<div>` appelé #root. Le fichier index.html ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*Oyb_sJ8t8xI4n7A3.png align="left")

*Fichier public/index.html de create-react-app*

Une fois que le composant `<App/>` est rendu dans le DOM, l'élément `<div>` réel avec l'id "#root" contient toute l'application React rendue à l'intérieur.

Par conséquent, il est assez courant que les composants de l'application React soient très profondément imbriqués. Nous parlons de dizaines de niveaux de profondeur, et souvent plus. Donc, si l'un de ces composants profondément imbriqués doit afficher une modale, il va rencontrer des problèmes sérieux de CSS.

Les modales placent une superposition sur l'écran et prennent donc une priorité visuelle plus élevée que *tous* les autres éléments. Si vous deviez le traduire en termes de z-index, il devrait avoir le nombre le plus élevé de tous les éléments à l'écran. Mais comme il est si profondément imbriqué, les éléments parents bien plus haut dans l'arborescence prennent la priorité CSS.

Plutôt que de toucher au CSS qui peut être finement réglé, et donc le modifier pourrait casser l'application, nous devons trouver un moyen de rendre dans le DOM — mais *en dehors de l'imbrication profonde*.

### **Solution — React Portals**

Une stratégie consiste à utiliser les portails ReactDOM et à placer la modale dans une div qui est un composant frère de la div avec l'id "#root". En faisant cela, les styles CSS appliqués au wrapper de la div de la modale s'appliqueront uniquement par rapport à son frère (la div "#root"), et cela ne cassera pas le style CSS de "#root".

Pour ce faire, nous devons utiliser la méthode `createPortal()` de ReactDOM. Un portail est effectivement une telle div frère, qui contourne la règle selon laquelle *tous* les composants React doivent être des descendants de `<div id="root">`. Pour ce faire, nous devons faire ce qui suit :

1. **Dans index.html, à l'intérieur de la balise** `<body>` :

```html
<body>
    <noscript>
      Vous devez activer JavaScript pour exécuter cette application.
    </noscript>
    
    <div id="root"></div>
    
    <div id="modal"></div> .   // AJOUTEZ CECI
    
  </body>
</html>
```

**2. Créez un composant Modal.js (les classNames proviennent de semantic-UI) :**

```js
import React from "react";
import ReactDOM from "react-dom";

const JSX_MODAL = (
  <div className="ui dimmer modals visible active">  
    <div className="ui standard modal visible active">
      CECI EST DU TEXTE DANS LA MODALE // ajoutez ici quelques fonctionnalités UI
    </div>
  </div>
);


function Modal(props) {
  return ReactDOM.createPortal(JSX_MODAL, document.querySelector("#modal"));
}


export default Modal;
```

Vous verrez que `createPortal` prend deux arguments : du JSX qui est rendu, et similaire à `ReactDOM.render`, l'élément cible sous lequel le JSX est rendu.

Si vous rendez le composant et naviguez vers celui-ci, vous devriez constater qu'il s'affiche plutôt bien. Vous devez maintenant ajouter le gestionnaire `onClick()` approprié pour gérer les événements de clic à l'intérieur de l'UI de la modale ainsi que pour naviguer hors de la modale si l'utilisateur clique à l'extérieur de l'UI de la modale.

Vous voudrez faire cela en écoutant les clics dans la bonne zone puis en stoppant la propagation afin que les bons comportements se produisent en fonction de la région où l'utilisateur clique.

### **Réutilisabilité**

L'exemple ci-dessus est extrêmement basique et n'est pas destiné à être un extrait de code prêt à l'emploi. Il s'agit plutôt d'une solution pour aborder les modales. Vous devriez absolument personnaliser le composant selon vos besoins. Utilisez les principes de réutilisabilité de React pour vous assurer que vous ne codez pas en dur les données dans la modale, et transmettez le contenu et même les widgets plus petits selon les besoins.

Par exemple, dans l'un de mes projets, je présente une modale lorsque l'utilisateur va supprimer quelque chose de la base de données. Donc mon composant est, disons, appelé `<DeleteThis />`. Il rend `<Modal />`, qui est la superposition qui assombrit l'écran sous-jacent `<DeleteThis />`.

```js
render() {
    return (
      <div>
        <Modal
          content={this.renderContentProp()}   
          header="Supprimer ceci ?"                
          actions={this.renderActionButtons()}
          onDismiss={this.onDismiss}
        />
      </div>
    );
  }
  
  renderActionButtons = () => {
    // retournez du JSX qui rend les boutons d'action...
    return (
      <div>
        <div className="ui button primary">Supprimer</div>
        <div className="ui button">Annuler</div>
      </div>
    );
  };
```

À l'intérieur de `<Modal />` se trouve un composant interne appelé `<InnerModal />` et celui-ci contient le composant interactif réel, avec des en-têtes, du contenu et du texte.

Ainsi, mon composant `<DeleteThis />` crée des props à transmettre dans `<Modal />` qui sont à leur tour transmises dans `<InnerModal />`, et donc la méthode `render` ressemble à :

...avec le composant Modal réel ressemblant à :

```js
import React from "react";
import ReactDOM from "react-dom";
import ModalInner from './modal-inner'

function Modal(props) {
  return ReactDOM
    .createPortal(
       <ModalInner {...props} />,
       document.querySelector("#modal")                      // élément DOM cible
     );
}
export default Modal;
```

et maintenant, vous êtes enfin en mesure de rendre :

![Image](https://cdn-media-1.freecodecamp.org/images/0*5JKvjljbrEzTxnNa.png align="left")

Voilà, vous y êtes ! Des modales, avec React Portal ! J'espère que vous avez apprécié cela !

Et j'espère que cela vous a fait gagner du temps...

Si vous souhaitez en savoir plus sur mon parcours dans le code, consultez l'[épisode 53](http://podcast.freecodecamp.org/53-zubin-pratap-from-lawyer-to-developer) du [podcast freeCodeCamp](http://podcast.freecodecamp.org/), où Quincy (fondateur de freeCodeCamp) et moi partageons nos expériences en tant que reconvertis professionnels, ce qui pourrait vous aider dans votre parcours. Vous pouvez également accéder au podcast sur [iTunes](https://itunes.apple.com/au/podcast/ep-53-zubin-pratap-from-lawyer-to-developer/id1313660749?i=1000431046274&mt=2), [Stitcher](https://www.stitcher.com/podcast/freecodecamp-podcast/e/59201373?autoplay=true) et [Spotify](https://open.spotify.com/episode/4lG0RGpzriG5vXRMgza05C).

Je vais également organiser quelques AMAs et webinaires dans les mois à venir. Si cela vous intéresse, faites-le moi savoir en allant [ici](http://www.matchfitmastery.com/). Et bien sûr, vous pouvez également me tweeter à [@ZubinPratap](https://twitter.com/zubinpratap).