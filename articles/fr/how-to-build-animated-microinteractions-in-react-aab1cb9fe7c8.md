---
title: Comment créer des micro-interactions animées dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-16T22:22:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-animated-microinteractions-in-react-aab1cb9fe7c8
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/WcvtLCXbGR92P6AIGR-GuGg9UXccQi9Oha57.gif
tags:
- name: animation
  slug: animation
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer des micro-interactions animées dans React
seo_desc: 'By Christian Sepulveda

  Microinteractions guide a user through your application. They reinforce your user
  experience and provide delight.

  You may have seen some of the slick examples of microinteractions on Dribble or
  CodePen. But do you know how to b...'
---

Par Christian Sepulveda

Les micro-interactions guident un utilisateur à travers votre application. Elles renforcent votre expérience utilisateur et procurent du plaisir.

Vous avez peut-être vu certains des exemples élégants de micro-interactions sur [Dribble](https://dribbble.com/search?q=microinteraction) ou [CodePen](https://codepen.io/search/pens?q=microinteraction&limit=all&type=type-pens). Mais savez-vous comment construire votre propre bibliothèque de widgets UI similaires ?

Dans cet article, je me concentrerai sur les micro-interactions animées en utilisant [React](https://facebook.github.io/react/), le framework UI populaire et orienté composants de Facebook. Je vais construire trois interactions pour une boîte de recherche :

* ouvrir et fermer la boîte de texte
* monter en haut de l'écran
* secouer (indiquant une erreur)

![Image](https://cdn-media-1.freecodecamp.org/images/mOwSS529Asj03ezAFoiuYU2eqTgHdywuGGHY)

J'utiliserai quelques implémentations différentes :

* [Transitions CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)
* [react-motion](https://github.com/chenglou/react-motion)
* [react-animations](https://github.com/FormidableLabs/react-animations)

Voici une [démo en direct](https://search-animation.firebaseapp.com) et [le code qui l'alimente](https://github.com/csepulv/search-box-animation).

> Ceci est l'un des plusieurs articles sur les composants d'ordre supérieur (HOC) et les composants fonctionnels sans état. Le premier [article](https://hackernoon.com/code-reuse-using-higher-order-hoc-and-stateless-functional-components-in-react-and-react-native-6eeb503c665) traite de la réutilisation du code dans React et React Native, via ces techniques.

### Qu'est-ce qu'une micro-interaction ?

[Dan Saffer](https://www.freecodecamp.org/news/how-to-build-animated-microinteractions-in-react-aab1cb9fe7c8/undefined) (qui a écrit le livre) nous donne cette [définition](http://microinteractions.com/what-is-a-microinteraction/) : « Les micro-interactions sont des moments de produit contenus qui tournent autour d'un cas d'utilisation unique — elles ont une tâche principale. »

Des exemples pourraient être plus clairs. Certaines micro-interactions sont partout, comme un changement de curseur lors du survol d'un lien ou la vibration de votre téléphone lorsque vous passez en mode silencieux. D'autres, comme un article ajouté à un panier d'achat, ne sont pas si courantes (encore).

#### Pourquoi devrais-je me soucier des micro-interactions ?

Les micro-interactions peuvent fournir des commentaires et rendre votre application mémorable. Lorsque les utilisateurs ont tant de choix d'applications, de meilleures micro-interactions pourraient être le piège à souris cliché que vous devriez construire.

Mais je ne suis pas un designer UX. Je suggère donc de lire l'article de [Nick Babich](https://www.freecodecamp.org/news/how-to-build-animated-microinteractions-in-react-aab1cb9fe7c8/undefined) sur les micro-interactions.

### Getting Started

J'utiliserai [create-react-app](https://github.com/facebookincubator/create-react-app) pour démarrer une application React, mais toute méthode de configuration React fonctionnera. De plus, j'aime [Material-UI](http://www.material-ui.com/#/), donc je vais l'importer aussi. (Ce choix est arbitraire — vous pourriez utiliser une autre bibliothèque de widgets ou styliser manuellement vos éléments.)

```bash
create-react-app search-box-animation
cd search-box-animation
npm install --save material-ui react-tap-event-plugin
```

#### Le composant : une boîte de recherche simple

Je vais créer une boîte de recherche simple. Elle comprendra deux éléments : un bouton icône de recherche et une boîte de texte. Je vais créer un composant fonctionnel sans état pour la boîte de recherche. (Les composants fonctionnels sans état sont des fonctions qui rendent des composants React et ne maintiennent pas d'état, c'est-à-dire utilisent `setState`. Vous pouvez en apprendre plus dans ce [tutoriel](https://hackernoon.com/react-stateless-functional-components-nine-wins-you-might-have-overlooked-997b0d933dbc#.673o1dbcj) ou mon précédent [article](https://hackernoon.com/code-reuse-using-higher-order-hoc-and-stateless-functional-components-in-react-and-react-native-6eeb503c665#c825).)

`SearchBox.js`

```javascript
import React from 'react';
import {TextField, IconButton} from 'material-ui'
import SearchIcon from 'material-ui/svg-icons/action/search';
const SearchBox = ({isOpen, onClick}) => {
    const baseStyles = {
        open: {
            width: 300,
        },
        closed: {
            width: 0,
        },
        smallIcon: {
            width: 30,
            height: 30
        },
        icon: {
            width: 40,
            height: 40,
            padding: 5,
            top: 10
        },
        frame: {
            border: 'solid 1px black',
            borderRadius: 5
        }
    };
const textStyle = isOpen ? baseStyles.open : baseStyles.closed;
const divStyle = Object.assign({}, textStyle, baseStyles.frame);
    divStyle.width += baseStyles.icon.width + 5;
return (
        <div style={divStyle}>
            <IconButton iconStyle={baseStyles.smallIcon} style={baseStyles.icon} onClick={() => onClick()}>
                <SearchIcon />
            </IconButton>
            <TextField name='search' style={textStyle}/>
        </div>
    );
};
export  default SearchBox;

```

(J'utiliserai le callback `onClick` plus tard.)

La prop `isOpen` définit le rendu ouvert ou fermé de `SearchBox`.

![Image](https://cdn-media-1.freecodecamp.org/images/muQzhipEBn8Aq6IjQmukr7NJDAoJhx53vxmC)
_isOpen=true / isOpen=false_

### Utilisation des composants d'ordre supérieur pour séparer les préoccupations

Je pourrais changer `SearchBox` en un composant régulier et ajouter du code qui ouvrirait et fermerait la boîte de texte lorsqu'on clique dessus, par exemple.

Mais je préfère séparer l'animation de la fonction principale de la boîte de recherche. La boîte de recherche affiche/capture une valeur de requête et soumet cette requête à un autre contrôleur. C'est une décision de conception subjective, mais elle a des avantages pratiques : je peux réutiliser la logique de micro-interaction avec un autre composant d'entrée utilisateur.

Les [composants d'ordre supérieur](https://facebook.github.io/react/docs/higher-order-components.html) (HOC) sont des fonctions qui retournent un nouveau composant. Ce composant enveloppe un ou plusieurs composants et ajoute des fonctionnalités. Je vais créer un HOC pour ajouter le comportement d'ouverture/fermeture à `SearchBox`.

Créer `expanding-animation.js`

```javascript
import React, {Component} from 'react';
const makeExpanding = (Target) => {
    return class extends Component {
        constructor(props) {
            super(props);
            this.state = {isOpen: false};
        }

        onClick = () => {
            this.setState({isOpen: !this.state.isOpen});
        };

        render() {
            return (
                <Target {...this.props}
                        isOpen={this.state.isOpen}
                        onClick={this.onClick}
                />
            );
        }
    }
};
export default makeExpanding;
```

Mettre à jour `App.js` comme suit :

```javascript
import React, {Component} from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

// (Rendre material-ui heureux)
// Nécessaire pour onTouchTap
// http://stackoverflow.com/a/34015469/988941
import injectTapEventPlugin from 'react-tap-event-plugin';
injectTapEventPlugin();

import SearchBox from './SearchBox'
import makeExpanding from './expanding-animation';

const ExpandingSearchBox = makeExpanding(SearchBox);

class App extends Component {
    render() {
        //https://css-tricks.com/quick-css-trick-how-to-center-an-object-exactly-in-the-center/
        const style = {
            position: 'fixed',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
        };

        return (
            <MuiThemeProvider>
                <div style={style}>
                    <ExpandingSearchBox/>
                </div>
            </MuiThemeProvider>
        );
    }
}
export default App;

```

Si vous exécutez `npm start`, vous aurez une icône de recherche sur laquelle vous pouvez cliquer pour ouvrir et fermer la boîte de texte.

Cela fonctionne, mais l'ouverture et la fermeture sont brutales. Une animation peut lisser l'effet.

### Animations

Il existe trois approches générales pour les animations.

1. Transitions CSS
2. Animations CSS
3. rendu rapide et répété d'un élément pour simuler le mouvement (cadrage clé manuel)

Les [transitions CSS](http://www.w3schools.com/css/css3_transitions.asp) changent une valeur de propriété (comme la largeur) sur une certaine durée. Le changement n'a pas à être linéaire ; vous pouvez spécifier des fonctions pour changer les valeurs.

Les [animations CSS](http://www.w3schools.com/css/css3_animations.asp) changent le style d'un élément (comme la taille, la couleur et la position). Chaque style incrémental est une image clé. Vous créez une série d'images clés pour obtenir un effet souhaité.

Les deux tactiques CSS rendent répétitivement les éléments pour simuler le mouvement. Vous pouvez faire les calculs vous-même, c'est-à-dire l'option (3). Plusieurs frameworks d'animation Javascript utilisent cette approche, gérant les calculs. (J'utiliserai react-motion dans un exemple ultérieur.)

J'utiliserai toutes ces techniques dans les exemples ci-dessous, mais je commencerai par les transitions CSS.

#### Expansion de la boîte de recherche

L'animation de la boîte de texte en expansion nécessite une propriété CSS : `transition`

Modifiez `expanding-animation.js` comme suit,

```javascript
import React, {Component} from 'react';
const animationStyle = {
    transition: 'width 0.75s cubic-bezier(0.000, 0.795, 0.000, 1.000)'
};
const makeExpanding = (Target) => {
    return class extends Component {
        constructor(props) {
            super(props);
            this.state = {isOpen: false};
        }

        onClick = () => {
            this.setState({isOpen: !this.state.isOpen});
        };

        render() {
            return (
                <Target {...this.props}
                        isOpen={this.state.isOpen}
                        onClick={this.onClick}
                        additionalStyles={{text: animationStyle, frame: animationStyle}}/>
            );
        }
    }
};
export default makeExpanding;
```

En regardant le changement à la ligne 21, `additionalStyles`, `SearchBox` fusionnera ce style avec ses styles existants aux lignes 29 et 31 ci-dessous. (Je reviendrai à la propriété CSS de transition à la ligne 2 dans un instant.)

Mettre à jour `SearchBox.js`

```javascript
import React from 'react';
import {TextField, IconButton} from 'material-ui'
import SearchIcon from 'material-ui/svg-icons/action/search';
const SearchBox = ({isOpen, onClick, additionalStyles}) => {
    const baseStyles = {
        open: {
            width: 300,
        },
        closed: {
            width: 0,
        },
        smallIcon: {
            width: 30,
            height: 30
        },
        icon: {
            width: 40,
            height: 40,
            padding: 5,
            top: 10
        },
        frame: {
            border: 'solid 1px black',
            borderRadius: 5
        }
    };
    
    let textStyle = isOpen ? baseStyles.open : baseStyles.closed;
    textStyle = Object.assign(textStyle, additionalStyles ? additionalStyles.text : {});
    
    const divStyle = Object.assign({}, textStyle, baseStyles.frame, additionalStyles ? additionalStyles.frame : {});
    divStyle.width += baseStyles.icon.width + 5;
    
    return (
        <div style={divStyle}>
            <IconButton iconStyle={baseStyles.smallIcon} style={baseStyles.icon} onClick={() => onClick()}>
                <SearchIcon />
            </IconButton>
            <TextField name='search' style={textStyle}/>
        </div>
    );
};
export  default SearchBox;

```

Avec les styles fusionnés, l'animation prendra effet.

![Image](https://cdn-media-1.freecodecamp.org/images/LpKVWFAxw2Ui03GJVCMC-rbPbZKo2r0hxTV2)
_Transition CSS : width_

Le résultat est une expansion fluide de la largeur de la boîte de texte, donnant l'apparence qu'elle s'ouvre. La propriété CSS `transition` contrôle cela (de la ligne 2 dans `expanding-animation.js`).

```
transition: 'width 0.75s cubic-bezier(0.000, 0.795, 0.000, 1.000)'
```

Je vous encourage à lire la [documentation](http://www.w3schools.com/css/css3_transitions.asp) pour la propriété de transition CSS, car il existe une variété d'options. Dans l'exemple, il y a trois paramètres :

1. propriété à changer : `width`
2. durée de la transition : `0.75s`
3. fonction pour contrôler le timing : `cubic-bezier(0.000, 0.795, 0.000, 1.000)'

Bien que j'aie choisi `cubic-bezier` comme fonction, `linear` ou `ease` sont parmi les autres options. Il existe des outils interactifs qui vous aident à sélectionner ces valeurs, comme ce [constructeur cubic-bezier](http://cubic-bezier.com/).

#### Déplacement de la boîte de recherche

Consultez l'animation conceptuelle suivante que j'ai trouvée sur Dribble :

![Image](https://cdn-media-1.freecodecamp.org/images/hm5SU07TXKkmqccw-bgsVclkH7Ygy-afBJ4E)
_[https://dribbble.com/shots/2751256-Google-Search](https://dribbble.com/shots/2751256-Google-Search" rel="noopener" target="_blank" title=")_

Il y a plusieurs éléments dans l'interaction ; mais je voudrais me concentrer sur le mouvement de la boîte de recherche en haut de l'écran.

Je peux déplacer ma modeste boîte de recherche avec une transition CSS. Créez un nouveau HOC, `move-up-animation.js`

```javascript

import React, {Component} from 'react';
const animationStyle = {
    transform: 'translateY(-150px)',
    transition: 'transform 1s ease'
};
const makeMoveUp = (Target) => {
    return class extends Component {
        constructor(props) {
            super(props);
            this.state = {moveTop: false};
        }

        onClick = () => {
            this.setState({moveTop: !this.state.moveTop});
        };

        render() {
            return (
                <Target isOpen={true}
                        onClick={this.onClick}
                        additionalStyles={{text: {}, frame: this.state.moveTop ? animationStyle : {}}}/>
            );
        }
    }
};
export default makeMoveUp;
view rawmove-up-animation.js hosted with ❤ by GitHub
```

Cela ressemble à la fonction HOC `makeExpanding`, sauf qu'elle fait une translation (monter). De plus, le style d'animation s'applique uniquement au cadre extérieur (`div`).

Mettre à jour `App.js`,

```javascript

import React, {Component} from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

// (Rendre material-ui heureux)
// Nécessaire pour onTouchTap
// http://stackoverflow.com/a/34015469/988941
import injectTapEventPlugin from 'react-tap-event-plugin';
injectTapEventPlugin();

import SearchBox from './SearchBox'
import makeMoveUp from './move-up-animation';
const MoveUpSearchBox = makeMoveUp(SearchBox);
class App extends Component {
    render() {
        //https://css-tricks.com/quick-css-trick-how-to-center-an-object-exactly-in-the-center/
        const style = {
            position: 'fixed',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
        };

        return (
            <MuiThemeProvider>
                <div style={style}>
                    <MoveUpSearchBox/>
                </div>
            </MuiThemeProvider>
        );
    }
}
export default App;
view rawApp.js-2 hosted with ❤ by GitHub
```

et vous devriez voir

![Image](https://cdn-media-1.freecodecamp.org/images/8a64RIYlqHBpWfYtXVpXMgKGte0vY9336wLr)
_Transition CSS. transform: translateY_

Peut-être voulez-vous un effet rebondissant. Vous pourriez utiliser [react-motion](https://github.com/chenglou/react-motion). C'est une bibliothèque React populaire qui utilise la dynamique des ressorts pour contrôler les animations. (Une bonne introduction, par [Nash Vail](https://www.freecodecamp.org/news/how-to-build-animated-microinteractions-in-react-aab1cb9fe7c8/undefined), est [ici](https://medium.com/@nashvail/a-gentle-introduction-to-react-motion-dc50dd9f2459#.8hkkdl9pi).)

```
npm install --save react-motion
```

Créer `spring-up-animation.js`

```javascript

import React, {Component} from 'react';
import {Motion, spring, presets} from 'react-motion'
const makeSpringUp = (Target) => {
    return class extends Component {
        constructor(props) {
            super(props);
            this.state = {moveTop: false};
        }

        onClick = () => {
            this.setState({moveTop: !this.state.moveTop});
        };

        render() {
            const style = {
                translateY: this.state.moveTop ? spring(-150, presets.wobbly) : spring(0)
            };
            return (
                <Motion style={style}>
                    {({translateY}) => (
                        <Target isOpen={true}
                                onClick={this.onClick}
                                additionalStyles={{
                                    text: {},
                                    frame: {
                                        transform: `translateY(${translateY}px)`
                                    }
                                }}/>
                    )}
                </Motion>
            );
        }
    }
};
export default makeSpringUp;
view rawspring-up-animation.js hosted with ❤ by GitHub
```

Comme ceci n'est pas un tutoriel sur react-motion, je vais brièvement résumer comment cela fonctionne. React-motion enveloppe le composant animé, `Target`, avec son propre composant, `Motion`. (Il existe d'autres composants react-motion, tels que `[TransitionMotion](https://github.com/chenglou/react-motion#transitionmotion-)` et `[Staggered Motion](https://github.com/chenglou/react-motion#staggeredmotion-)`.)

React-motion interpole, en utilisant la dynamique des ressorts, une série de valeurs intermédiaires. Il fournit les valeurs au composant animé sous forme de style. Ce style détermine la transition visuelle dans l'animation.

L'image ci-dessous montre le résultat (avec un ressort vacillant pour mettre en évidence l'effet).

![Image](https://cdn-media-1.freecodecamp.org/images/pi5bMtpY7TEEgUzyq6SCBo7K5XpdrEs7nFsu)
_dynamique des ressorts react-motion_

Vous pourriez utiliser react-motion pour une gamme d'effets. Par exemple, vous pourriez changer la boîte de texte pour qu'elle s'expande comme un ressort.

(`spring-up-animation.js` et `move-up-animation.js` ont la même logique d'état `onClick`, donc j'ai refactorisé les parties communes. Les détails sont [ici](https://github.com/csepulv/search-box-animation/blob/master/src/move-up-animations.js).)

#### Secouer la boîte de recherche

Je veux fournir un retour à l'utilisateur sur les requêtes erronées. Vous pourriez utiliser des messages d'erreur, mais j'aimerais faire quelque chose de plus fantaisiste : secouer la boîte de recherche.

Je pourrais utiliser react-motion, mais j'aimerais examiner une autre technique : l'animation par images clés.

[React-animations](https://github.com/FormidableLabs/react-animations/) est une bibliothèque React pour les animations par images clés. Elle injecte des images clés CSS dans une feuille de style DOM. (Les autres exemples n'ont utilisé que des styles en ligne.)

```
npm install --save react-animations
```

J'ai également besoin d'une bibliothèque, comme [Radium](https://github.com/FormidableLabs/radium) ou [Aphrodite](https://github.com/Khan/aphrodite), pour gérer l'injection de la feuille de style CSS. J'ai choisi Aphrodite, car je l'ai déjà utilisée.

```
npm install --save aphrodite
```

Créer un autre HOC, `shake-animation.js`

```javascript
import React, {Component} from 'react';
import {headShake} from 'react-animations';
import {StyleSheet, css} from 'aphrodite';
const styles = StyleSheet.create({
    headShake: {
        animationName: headShake,
        animationDuration: '1s'
    }
});
const makeValidationErrorAnimation = (Target) => {
    return class extends Component {
        constructor(props) {
            super(props);
            this.state = {shouldShake: false};
        }

        onClick = () => {
            this.setState({shouldShake: true}, () => {
                const self = this;
                setTimeout(() => self.setState({shouldShake: false}), 1000);
            });
        };

        render() {
            return (
                <Target isOpen={true}
                        onClick={this.onClick}
                        additionalStyles={{text: {}, frame: {}}}
                        frameClass={this.state.shouldShake ? css(styles.headShake) : ''}/>
            );
        }
    }
};
export default makeValidationErrorAnimation;

```

Il y a quelques sections clés. La ligne 4 utilise Aphrodite pour créer la feuille de style pour l'effet react-animations, `head-shake`. La ligne 29 définit la classe CSS pour l'animation sur `Target`. (Cela nécessite une modification de `SearchBox` pour utiliser la classe CSS. Regardez l'utilisation de `frameClass` dans la [source](https://github.com/csepulv/search-box-animation/blob/master/src/SearchBox.js) de `SearchBox.js`.) Le gestionnaire `onClick` à la ligne 17 est plus compliqué.

#### Redémarrer une animation

J'aimerais faire le 'head shake' à chaque erreur de validation (ou quel que soit le déclencheur utilisé). Mais comme l'animation est une classe CSS, je ne peux pas simplement définir la même classe à nouveau ; cela n'aurait aucun effet. Ce [post](https://css-tricks.com/restart-css-animation/) de CSS Tricks décrit quelques options. La plus simple est un délai qui supprime la classe d'animation CSS. Lorsque vous l'ajoutez à nouveau (pour un nouvel événement), vous verrez le 'head shake'.

![Image](https://cdn-media-1.freecodecamp.org/images/oESGN1McQrUoZ-1UpbatEYcENgWSPaLS5sKP)
_react-animations (utilise des images clés, animation CSS)_

### Mettre tout ensemble : composer un composant complexe

J'ai créé plusieurs HOC pour différentes animations. Mais vous pouvez également enchaîner les HOC pour créer un composant composé. Il ouvrira la boîte de texte lorsqu'on clique dessus et secouera en cas d'entrée erronée.

Tout d'abord, vous devrez apporter quelques modifications à `SearchBox`

```javascript
import React from 'react';
import {TextField, IconButton} from 'material-ui'
import SearchIcon from 'material-ui/svg-icons/action/search';
const baseStyles = {
    open: {
        width: 300,
    },
    closed: {
        width: 0,
    },
    smallIcon: {
        width: 30,
        height: 30
    },
    icon: {
        width: 40,
        height: 40,
        padding: 5,
        top: 10
    },
    frame: {
        border: 'solid 1px black',
        borderRadius: 5
    }
};
const SearchBox = ({isOpen, query, onClick, onSubmit, onQueryUpdate, additionalStyles, frameClass}) => {
    const handleKeyDown = (event) => {
        const ENTER_KEY = 13;
        if (event.keyCode === ENTER_KEY) {
            event.preventDefault();
            onSubmit();
        }
    };
    let textStyle = isOpen ? baseStyles.open : baseStyles.closed;
    textStyle = Object.assign(textStyle, additionalStyles ? additionalStyles.text : {});
    const divStyle = Object.assign({}, textStyle, baseStyles.frame, additionalStyles ? additionalStyles.frame : {});
    divStyle.width += baseStyles.icon.width + 5;
    return (
        <div style={divStyle} className={frameClass ? frameClass : ''}>
            <IconButton iconStyle={baseStyles.smallIcon} style={baseStyles.icon} onClick={() => onClick()}>
                <SearchIcon />
            </IconButton>
            <TextField name='search'
                       style={textStyle}
                       value={query}
                       onKeyDown={handleKeyDown}
                       onChange={(event, value) => onQueryUpdate(value)}/>
        </div>
    );
};
export  default SearchBox;

```

`SearchBox` est maintenant un [composant contrôlé](https://facebook.github.io/react/docs/forms.html) (terme fantaisiste pour utiliser React pour gérer la valeur d'entrée de la boîte de texte). Il fournit également un callback, `onSubmit`, pour soumettre la requête de recherche (quand un utilisateur appuie sur la touche _Entrée_).

Vous devez également changer `shake-animation.js`. Cliquer sur l'icône de recherche ne devrait pas provoquer la secousse. Au lieu de cela, je veux qu'un autre composant détermine quand 'secouer'. Cela sépare la logique de validation du code qui contrôle l'animation.

`startShake` est un drapeau pour réinitialiser l'animation. Mais c'est un détail d'implémentation. Il devrait être encapsulé, en tant qu'état interne, dans le HOC `makeShakeAnimation`.

```javascript
import React, {Component} from 'react';
import {headShake} from 'react-animations';
import {StyleSheet, css} from 'aphrodite';
const styles = StyleSheet.create({
    headShake: {
        animationName: headShake,
        animationDuration: '1s'
    }
});
const makeShakeAnimation = (Target) => {
    return class extends Component {
        constructor(props) {
            super(props);
            this.state = {startShake: props.shouldShake};
        }

        componentWillReceiveProps(nextProps) {
            this.setState({startShake: nextProps.shouldShake}, () => {
                const self = this;
                setTimeout(() => self.setState({startShake: false}), 1000);
            });
            //https://css-tricks.com/restart-css-animation/ pour la discussion sur le redémarrage
        }

        render() {
            return (
                <Target {...this.props}
                        frameClass={this.state.startShake ? css(styles.headShake) : ''}/>
            );
        }
    }
};
export default makeShakeAnimation;
```

`startShake` dépend de `shouldShake`. Je peux utiliser [componentWillReceiveProps](https://facebook.github.io/react/docs/react-component.html#componentwillreceiveprops) pour répondre aux changements de props. (C'est le parent, le composant de validation, qui fournit ces props.) J'ai donc déplacé la logique précédente `onClick` vers `componentWillReceiveProps`.

Le changement à la ligne 27, `{...this.props}`, passe toutes les props au composant enveloppé, `Target`. (Je dois également changer la méthode `render` dans `expanding-animation.js`. Les détails sont [ici](https://github.com/csepulv/search-box-animation/blob/master/src/expanding-animation.js).)

Je peux maintenant ajouter un composant qui contrôlera quand secouer.

Créer `search-box-controller.js`

```javascript
import React, {Component} from 'react';

import makeExpanding from './expanding-animation';
import makeShakingAnimation from './shake-animation';

const makeAnimatedValidationSearchBox = (Target) => {
    const WrappedComponent = makeShakingAnimation(makeExpanding(Target));

    return class extends Component {
        constructor(props) {
            super(props);
            this.state = {query: '', hasError: false};
        }

        onQueryUpdate = (value) => {
            this.setState({query: value, hasError:false});
        };

        onSubmit = () => {
            this.setState({hasError: true});
        };

        render() {
            return (
                <WrappedComponent
                    onQueryUpdate={this.onQueryUpdate}
                    query={this.state.query}
                    onSubmit={this.onSubmit}
                    shouldShake={this.state.hasError}
                />
            );
        }
    }
};

export default makeAnimatedValidationSearchBox;
```

C'est un autre HOC. Il n'a pas d'éléments visuels, mais il contrôle le comportement logique du composant enveloppé. ([Dan Abramov](https://www.freecodecamp.org/news/how-to-build-animated-microinteractions-in-react-aab1cb9fe7c8/undefined) a un bon [article](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0#.2660qau6m) expliquant une telle séparation.) Dans ce cas, toutes les requêtes sont erronées, mais dans une application réelle, je validerais les requêtes et me connecterais à des API.

Enfin, je veux souligner que `makeAnimatedValidationSearchBox` est un HOC qui enchaîne deux autres HOC.

```
const WrappedComponent =makeShakingAnimation(makeExpanding(Target));
```

Une autre petite mise à jour de `App.js`

```javascript
import React, {Component} from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

// (Rendre material-ui heureux)
// Nécessaire pour onTouchTap
// http://stackoverflow.com/a/34015469/988941
import injectTapEventPlugin from 'react-tap-event-plugin';
injectTapEventPlugin();
import SearchBox from './SearchBox'

import makeAnimatedValidationSearchBox from './search-box-controller';
const AnimatedSearchBox = makeAnimatedValidationSearchBox(SearchBox);

class App extends Component {
    render() {
        //https://css-tricks.com/quick-css-trick-how-to-center-an-object-exactly-in-the-center/
        const style = {
            position: 'fixed',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
        };
        return (
            <MuiThemeProvider>
                <div style={style}>
                    <AnimatedSearchBox/>
                </div>
            </MuiThemeProvider>
        );
    }
}
export default App;
```

(La ligne 12 utilise le nouveau HOC)

et exécuter `run npm start`

![Image](https://cdn-media-1.freecodecamp.org/images/WcvtLCXbGR92P6AIGR-GuGg9UXccQi9Oha57)
_un composant composé, fait en enchaînant trois HOC_

J'ai créé un composant composé qui utilise plusieurs micro-interactions. Elles sont réutilisables et discrètes.

### Conclusion

J'ai échantillonné chacune des approches : transitions CSS, react-motion et react-animations. Je souhaite que vous puissiez choisir une seule approche, mais il est difficile de tordre une seule approche pour tous les cas d'utilisation. Heureusement, vous pouvez mélanger et assortir les bibliothèques et les techniques. Et vous pouvez encapsuler les détails dans des HOC réutilisables.

Vous pourriez vouloir vérifier des bibliothèques comme [recompose](https://github.com/acdlite/recompose), qui rendent la création de HOC plus facile.

Le dépôt GitHub pour ce projet est [ici](https://github.com/csepulv/search-box-animation).

Veuillez ❤ cet article et me suivre pour de futures histoires. Merci d'avoir lu.