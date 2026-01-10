---
title: Composants React à positionnement automatique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-04T21:57:26.000Z'
originalURL: https://freecodecamp.org/news/self-positioning-react-components-2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca22d740569d1a4ca5305.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Composants React à positionnement automatique
seo_desc: 'By Benjamin Schachter

  While React has ways to break the hatch and directly manipulate the DOM there are
  very few reasons to do this. We shouldn’t directly manipulate the DOM unless we
  have a really good reason to. When we need to we should use the re...'
---

Par Benjamin Schachter

Bien que React offre des moyens de briser la coque et de manipuler directement le DOM, il y a très peu de raisons de le faire. Nous ne devrions pas manipuler directement le DOM sauf si nous avons une très bonne raison de le faire. Lorsque nous en avons besoin, nous devrions utiliser la propriété `ref`. Ce n'est qu'en dernier recours que nous devrions manipuler directement le DOM ainsi que changer l'état pendant un rendu.

### Le Problème

La grille se verrouille à 1024px d'une grille fixe à une grille fluide. Nous voulions que nos conseils de tutoriel soient à 20px de leur élément parent et il n'y avait pas moyen de faire cela avec juste du CSS. Si le conseil était positionné correctement dans la grille fixe, il serait décalé lorsque la grille passerait à une vue fluide.

%[https://youtu.be/9VkbXWANxvQ]

Les métadonnées du tutoriel sont appliquées directement dans les styles en ligne du composant qui a la spécificité CSS la plus élevée. Cela signifiait que les requêtes média ne pouvaient pas résoudre ce problème car les requêtes média seraient remplacées par du CSS avec une spécificité plus élevée.

### La Solution

La solution devait être un ensemble unique de métadonnées et un composant qui savait où il se trouvait afin qu'il puisse changer son positionnement à la volée. Voici une vidéo des styles de composant final qui changent.

%[https://youtu.be/BFkJ4KjBWPo]

et le composant se déplaçant avec le redimensionnement de la fenêtre.

%[https://youtu.be/OwGAaxtAmaQ]

### Element.getClientRects()

Tout d'abord, nous devons savoir où se trouve l'élément parent sur la page avant de pouvoir faire quoi que ce soit avec. La méthode `.getClientRects()` [méthode](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) fait exactement cela. Si vous interrogez un élément sur le DOM et appelez `.getClientRects()`, il retournera un objet de valeurs avec la position, la hauteur et la largeur de cet élément par rapport à la fenêtre du navigateur. Essayez-le de votre côté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EkU_yoIB4aWoSRX11jYIiw.png)
_interrogation d'un élément sur NYTimes.com_

### Utilisation d'un composant avec état pour stocker le positionnement

Nous avons besoin que le composant sache où il se trouve à tout moment. En réfléchissant à cette exigence, nous avons besoin d'un composant `class` qui peut maintenir son propre état, et non d'un composant fonctionnel sans état. Cela est dû au fait que l'utilisateur peut réduire ou agrandir sa fenêtre au-delà ou en dessous du seuil de 1024px, ce qui change notre grille en position fluide ou fixe. Le composant doit être conscient de la taille de la fenêtre afin de pouvoir conserver son positionnement généré dynamiquement chaque fois que la taille de l'écran change.

### Getters et Setters

Le composant dispose de deux fonctions principales autour du positionnement dynamique. Définir les styles dynamiquement en fonction de l'emplacement de l'élément parent sur l'écran et obtenir ces styles définis pour rendre la position du conseil. Nous avons nommé ces méthodes de fonction `getStyles` et `setStyles`.

```javascript
/**
 * Méthode pour que le conseil de tutoriel définisse dynamiquement la position en fonction de l'état.
 *
 * @return {object} avec les valeurs de style de position dynamique de tutorialTip
 */
, getStyles: function () {
  var self = this
    , styles = {
      top      : self.state.top    || 'auto'
      , bottom   : self.state.bottom || 'auto'
      // (Nous parlerons de ce positionnement plus tard)     
      , left     : self.state.left   || -9999
      , right    : self.state.right  || 'auto'
    }
    ;
  // Masquer le conseil de tutoriel pendant les transitions pour éviter le scintillement. (Nous en parlerons plus tard)
  if (!this.state.display) {
    styles.display = 'none';
  }
  
  return styles;
}
view raw
```

```javascript
/**
 * Interroge le DOM et génère dynamiquement des valeurs pour mettre à jour l'état. Ces valeurs sont passées à getStyles
 * pour mettre à jour le positionnement.
 *
 * @return {void} la fonction modifie l'état.
 */
  , setStyles: function () {
    var {step} = this.props
      , meta = tutorialMeta[step]
      // (Nous en parlerons plus tard)
      , el = document.querySelector('.step' + step)
      // Obtenir les valeurs de l'élément DOM interrogé (top, right, left, width, etc.)
      , bounds = el && el.getBoundingClientRect()
      ;

    if (bounds) {
      switch (meta.position) {
        case 'right':
          this.setState({
            top: Math.floor(bounds.top - meta.offsetTop)
            , left: Math.floor((bounds.right) + meta.offsetLeft)
            , display: true
          });
          break;
        case 'left':
          this.setState({
            top: Math.floor(bounds.top - meta.offsetTop)
            , left: Math.floor((bounds.left) + meta.offsetLeft)
            , display: true
          });
          break;
        case 'bottom':
          this.setState({
            top: Math.floor(bounds.top - meta.offsetTop)
            , left: Math.floor((bounds.right - bounds.width) + meta.offsetLeft)
            , display: true
          });
          break;
        case 'bottom-left':
          this.setState({
            top: Math.floor(bounds.top - meta.offsetTop)
            , left: Math.floor((bounds.right - bounds.width) + meta.offsetLeft)
            , display: true
          });
          break;
        default:
          break;
      }
    }
  }
```

Dans ce cas d'utilisation particulier, nous chargeons les données JSON `tutorialMeta` pour chaque conseil de tutoriel et définissons `setState` en conséquence pour chaque type de positionnement de conseil. **Note :** Ceci n'est pas une exigence pour un composant à positionnement automatique en soi. Juste des informations pour le tutoriel. Les exemples sont le texte d'instruction et le positionnement décalé afin que le conseil soit à 20px de son élément parent et centré.

Maintenant, il est temps de prendre cette fonctionnalité et de la connecter aux méthodes du cycle de vie de React afin que le composant sache quand mettre à jour son propre positionnement.

### Connexion aux méthodes du cycle de vie de React

Connectons nos getters et setters afin que notre composant sache quand les déclencher et mettre à jour ses props et son état.

Initialisation et Destruction :

```javascript
componentDidMount: function () {
  window.addEventListener('resize', this.setStyles);
  this.setStyles();
}
, componentWillUnmount: function () {
  window.removeEventListener('resize', this.setStyles);
}
```

Au chargement du composant, nous devons `setStyles` puisque nous n'avons actuellement aucun style à obtenir ! N'oubliez pas que le composant va appeler `.getClientRect()` qui va définir dynamiquement les valeurs de positionnement. De plus, nous ne voulons pas interroger le DOM chaque fois que nous redimensionnons la fenêtre.

```javascript
  , shouldComponentUpdate: function (nextProps, nextState) {
    // Nous utilisons lodash au travail pour des méthodes pratiques comme isEqual
    return !_.isEqual(nextProps, this.props) || !_.isEqual(nextState, this.state);
  }

  , componentWillReceiveProps: function (nextProps) {
    if (nextProps.step !== this.props.step) {
      // L'étape a changé, masquer la boîte de tutoriel
      this.replaceState({
        display: false
      });
    }
  }
```

Nous vérifions si nos props ou notre état a changé. Par défaut, `shouldComponentUpdate` retourne vrai si un état a changé selon la [documentation](https://facebook.github.io/react/docs/react-component.html#shouldcomponentupdate) de React. Puisque nous recevons également des données de notre composant conteneur en tant que props, nous devons également vérifier les mises à jour des props. **Note :** Il y a un dispatch global et des données pour l'ensemble du tutoriel comme `nextStep` et `currentStep`, ce n'est pas une exigence pour chaque cas d'utilisation, juste celui que nous résolvons.

Ensuite, `componentWillReceiveProps` est déclenché avant qu'un composant monté ne reçoive de nouvelles props ([docs](https://facebook.github.io/react/docs/react-component.html#componentwillreceiveprops)). L'utilisation de `replaceState` plutôt que `setState` efface l'état et définit le composant pour ne pas s'afficher. Cela est également très spécifique et délibéré pour notre cas d'utilisation, le problème de scintillement.

### Il y avait un problème de scintillement

Le redoutable scintillement ! Il était très subtil, mais il faisait tiquer notre équipe. Il y avait un flash au chargement initial et lors de la transition du conseil de tutoriel, il restait juste une étape de rendu avant d'être à sa place.

**Le Flash Scintillant :** C'est là que la position `-9999` est intervenue. Si nous n'avons pas de positionnement à donner à notre composant, assurons-nous simplement qu'il est complètement hors de la page.

**Le Scintillement Suspendu :** Chaque fois que nous recevons de nouvelles props, le composant définit notre affichage sur false, supprimant complètement le composant du DOM pendant les transitions. Si vous regardez dans `componentWillReceiveProps`, `setStyles` et `getStyles`, vous verrez des références à la façon dont le composant est supprimé et ajouté avec `display` défini sur false ou true.

### Le Render

C'est la fonction qui va obtenir nos styles générés dynamiquement, appelée dans les styles `props`. **Note :** `_.getClassNameFromObject` est notre propre fonction personnalisée qui créera une chaîne que nous pouvons ajouter aux styles de classe d'un composant. Nous ne allons pas approfondir cette fonction car elle est hors du cadre de cet article. Mais si vous êtes intéressé, laissez un commentaire en bas de l'article et j'essaierai de répondre à vos questions.

```javascript
, render: function () {
    let {step} = this.props;
    var props = this.props
      , meta = tutorialMeta[step]
      , parentClass = _.getClassNameFromObject({
        'tutorial-wrap': true
      })
      , childClass = _.getClassNameFromObject({
        'tutorial-tip': true
        , 'top'     : _.isEqual(_.get(meta, 'position'), 'top')
        , 'right'   : _.isEqual(_.get(meta, 'position'), 'right')
        , 'bottom'  : _.isEqual(_.get(meta, 'position'), 'bottom')
        , 'left'    : _.isEqual(_.get(meta, 'position'), 'left')
        , 'bottom-left':  _.isEqual(_.get(meta, 'position'), 'bottom-left')
      })
      , text = props.error ? meta.error : meta.text
      , btnCls = _.getClassNameFromObject({
        'btn btn-special btn--short next': meta.nextButton
        , 'hidden': !meta.nextButton
      })
      ;

    if (!props.visible) return null;

    return (
      <div className={parentClass}>
        <div className={childClass} style={this.getStyles()}>
          <div>
            <div className="step-info">
              <span><span className="step"><i className="fa fa-question-circle" aria-hidden="true"></i>
              &nbsp; Étape {props.step + 1}</span> sur {tutorialMeta.length}</span>
            </div>
            <div className="step-text">
              <span dangerouslySetInnerHTML={{__html: text}}></span>
            </div>
            <div className="end-tutorial">
              <a className="clickable" onClick={props.onTutorialFinish}>Terminer le tutoriel</a>
                <button className={btnCls} onClick={props.onTutorialNext}>Suivant</button>
            </div>
          </div>
        </div>
      </div>
    );
  }
```

Voici un diagramme de notre cycle de vie du composant, des getters, des setters et des méthodes de rendu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nMWbkf4UI35QyiTOTl1WWA.png)

### Le Composant Entier

```javascript
var React  = require('react')
  , _      = require('lodash')
  , tutorialMeta = require('./tutorialMeta.json').tutorial
  ;

/**
 * Composant de Tutoriel
 * @class TutorialTip
 * @param {props} objet qui contient les données globales pour rendre le composant.
 * @param {element} élément pour placer le conseil de tutoriel autour.
 *
 * @return {element} avec tutorialTip
 */

module.exports = React.createClass({
  getInitialState: function () {
    return {display: true};
  }
  , componentDidMount: function () {
    window.addEventListener('resize', this.setStyles);
    this.setStyles();
  }
  , componentWillUnmount: function () {
    window.removeEventListener('resize', this.setStyles);
  }
  , shouldComponentUpdate: function (nextProps, nextState) {
    return !_.isEqual(nextProps, this.props) || !_.isEqual(nextState, this.state);
  }

  , componentWillReceiveProps: function (nextProps) {
    if (nextProps.step !== this.props.step) {
      // L'étape a changé, masquer la boîte de tutoriel
      this.replaceState({
        display: false
      });
    }
  }
/**
 * Méthode pour que le conseil de tutoriel définisse dynamiquement la position en fonction de l'état.
 *
 * @return {object} avec les valeurs de style de position dynamique de tutorialTip
 */
  , getStyles: function () {
    var self = this
      , styles = {
        top      : self.state.top    || 'auto'
        , bottom   : self.state.bottom || 'auto'
        , left     : self.state.left   || -9999
        , right    : self.state.right  || 'auto'
      }
      ;
    // Masquer le conseil de tutoriel pendant les transitions pour éviter le scintillement.
    if (!this.state.display) {
      styles.display = 'none';
    }

    return styles;
  }
  , componentDidUpdate: function () {
    this.setStyles();
  }
/**
 * Interroge le DOM et génère dynamiquement des valeurs pour mettre à jour l'état. Ces valeurs sont passées à getStyles
 * pour mettre à jour le positionnement.
 *
 * @return {void} la fonction modifie l'état.
 */
  , setStyles: function () {
    var {step} = this.props
      , meta = tutorialMeta[step]
      , el = document.querySelector('.step' + step)
      // Obtenir les valeurs de l'élément DOM interrogé (top, right, left, width, etc.)
      , bounds = el && el.getBoundingClientRect()
      ;

    if (bounds) {
      switch (meta.position) {
        case 'right':
          this.setState({
            top: Math.floor(bounds.top - meta.offsetTop)
            , left: Math.floor((bounds.right) + meta.offsetLeft)
            , display: true
          });
          break;
        case 'left':
          this.setState({
            top: Math.floor(bounds.top - meta.offsetTop)
            , left: Math.floor((bounds.left) + meta.offsetLeft)
            , display: true
          });
          break;
        case 'bottom':
          this.setState({
            top: Math.floor(bounds.top - meta.offsetTop)
            , left: Math.floor((bounds.right - bounds.width) + meta.offsetLeft)
            , display: true
          });
          break;
        case 'bottom-left':
          this.setState({
            top: Math.floor(bounds.top - meta.offsetTop)
            , left: Math.floor((bounds.right - bounds.width) + meta.offsetLeft)
            , display: true
          });
          break;
        default:
          break;
      }
    }
  }
  , render: function () {
    let {step} = this.props;
    var props = this.props
      , meta = tutorialMeta[step]
      , parentClass = _.getClassNameFromObject({
        'tutorial-wrap': true
      })
      , childClass = _.getClassNameFromObject({
        'tutorial-tip': true
        , 'top'     : _.isEqual(_.get(meta, 'position'), 'top')
        , 'right'   : _.isEqual(_.get(meta, 'position'), 'right')
        , 'bottom'  : _.isEqual(_.get(meta, 'position'), 'bottom')
        , 'left'    : _.isEqual(_.get(meta, 'position'), 'left')
        , 'bottom-left':  _.isEqual(_.get(meta, 'position'), 'bottom-left')
      })
      , text = props.error ? meta.error : meta.text
      , btnCls = _.getClassNameFromObject({
        'btn btn-special btn--short next': meta.nextButton
        , 'hidden': !meta.nextButton
      })
      ;

    if (!props.visible) return null;

    return (
      <div className={parentClass}>
        <div className={childClass} style={this.getStyles()}>
          <div>
            <div className="step-info">
              <span><span className="step"><i className="fa fa-question-circle" aria-hidden="true"></i>
              &nbsp; Étape {props.step + 1}</span> sur {tutorialMeta.length}</span>
            </div>
            <div className="step-text">
              <span dangerouslySetInnerHTML={{__html: text}}></span>
            </div>
            <div className="end-tutorial">
              <a className="clickable" onClick={props.onTutorialFinish}>Terminer le tutoriel</a>
                <button className={btnCls} onClick={props.onTutorialNext}>Suivant</button>
            </div>
          </div>
        </div>
      </div>
    );
  }
});
```

### Mais attendez, il y a plus !

Nous avons également trouvé une solution intéressante pour éviter d'ajouter des composants partout dans notre application. Cela est utile si vous devez ajouter une série de composants à votre application comme un tutoriel.

Dans `setStyles`, nous interrogeons le DOM pour une étape spécifique plutôt que d'inclure le composant plusieurs fois. Le composant conteneur rend le composant une fois, puis à chaque changement d'étape, nous cherchons une classe d'étape différente pour rendre le composant de tutoriel.

### C'est tout, les amis

Espérons que cela aide toute personne ayant besoin de cette fonctionnalité de positionnement dynamique dans son application React.

Un grand merci à l'équipe d'ingénierie de [Dexter](https://medium.com/@rundexter), en particulier [Daniel Ilkovich](https://medium.com/@ilkovich) et [David Hu](https://medium.com/@octopi), pour m'avoir permis de partager ce code et pour tout leur aide et soutien lors de la création de la fonctionnalité de tutoriel utilisateur sur notre [site](http://rundexter.com/).