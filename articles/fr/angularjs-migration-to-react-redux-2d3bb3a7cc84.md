---
title: D'AngularJS à React & Redux — comment migrer votre application web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-10T17:59:33.000Z'
originalURL: https://freecodecamp.org/news/angularjs-migration-to-react-redux-2d3bb3a7cc84
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BHCxD-xbmOPDcEMiTXsPxw.jpeg
tags:
- name: Angular
  slug: angularjs
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
seo_title: D'AngularJS à React & Redux — comment migrer votre application web
seo_desc: 'By Panagiotis Vrs

  Some days ago I wanted to start implementing something I had in mind for the past
  4 months: Migrating an AngularJS project to React with Redux state management.

  I did some research around the topic. And although there were some arti...'
---

Par Panagiotis Vrs

Il y a quelques jours, je voulais commencer à implémenter quelque chose que j'avais en tête depuis les 4 derniers mois : migrer un projet AngularJS vers React avec la gestion d'état Redux.

J'ai fait quelques recherches sur le sujet. Et bien qu'il y ait quelques articles sur la migration d'Angular vers React, je me suis perdu. De plus, je n'ai pas trouvé comment utiliser Redux sur le projet uniquement pour React.

Il y a des centaines de projets qui devront décider dans les prochaines années de passer à un autre framework, car AngularJS et ses bibliothèques recevront de moins en moins de support de la communauté.

J'ai pensé que cela pouvait être plus facile, c'est pourquoi je l'ai fait et j'ai pris quelques notes pour partager mes découvertes.

Commencer la migration d'AngularJS vers React n'est pas une tâche facile. Et que se passe-t-il si vous voulez commencer à utiliser Redux pour la gestion d'état également ? Eh bien, cela n'a pas à être un cauchemar !

Mon projet avait déjà été converti en ES6 avec Webpack, ce qui a beaucoup aidé. Je suggère donc, avant de faire une telle migration, de commencer à utiliser Webpack et les dépendances de modules dès que possible.

### Mes besoins

Je voulais commencer à migrer ce projet d'AngularJS vers React afin de pouvoir commencer à utiliser toutes les nouvelles fonctionnalités que le web moderne offre en termes de vitesse, de division du code en composants plus petits et, bien sûr, de tests.

Je ne vais pas mentir — je ne testais pas assez, ou pas du tout, dans ce projet. Deux mois avant cette migration, j'ai commencé à implémenter quelques principes de test autour du projet pour pouvoir suivre certaines tâches. En résumé, il était incroyablement difficile de configurer les tests et la couverture, et cela a pris un certain temps pour exécuter les tâches.

### Commencez à le structurer

La première chose que j'ai faite a été d'installer toutes les dépendances nécessaires comme react, react-dom et react-redux. Vous pouvez également voir les versions que j'utilise ci-dessous.

Le plugin le plus cool de tous était react2angular, que j'ai utilisé pour traduire tous les composants React en composants Angular.

Ensuite, pour le développement, nous devons installer les dépendances babel pour avoir toutes les fonctionnalités ES6. Gardez à l'esprit que j'avais déjà Babel, et je ne faisais que coller ceci pour voir les versions et rester aligné.

```json
{
  "dependencies": {
    "ng-redux": "^3.4.0-beta.1",
    "prop-types": "^15.5.10",
    "react": "^15.5.4",
    "react-dom": "^15.5.4",
    "react-redux": "^5.0.5",
    "react2angular": "^1.1.3",
    "redux": "^3.6.0",
    "redux-devtools": "^3.4.0",
    "redux-thunk": "^2.2.0",
  },
  "devDependencies": {
    "babel-core": "^6.24.1",
    "babel-loader": "^6.4.1",
    "babel-preset-es2015": "^6.24.1",
    "babel-preset-react": "^6.24.1",
    "babel-preset-stage-2": "^6.24.1",
    "webpack": "^2.2.0",
    "webpack-dev-server": "^2.2.0",
  }
}
```

Tout est fait ? Super !

### Structure du projet

Voici ce que je voulais faire avec cette structure pour l'ensemble du projet. Je l'ai vu dans un projet MERN complet sur Github car je l'ai utilisé dans un petit projet pour voir comment il se comporterait. C'est très simple et efficace. Diviser chaque page (composant conteneur) et chaque page pour qu'elles aient leurs propres composants. Vous pouvez également avoir un dossier à l'extérieur nommé composants pour y garder tous les composants globaux. Référez-vous ici si les exemples de code n'ont pas de sens ;)

Vous pouvez également voir comment le projet MERN gère le rendu côté serveur lorsque la migration est terminée (une autre grande fonctionnalité que vous pouvez utiliser avec React !) afin de la réaliser.

Je n'ai pas les fichiers index, etc., dans cette structure, elle se concentre uniquement sur les composants React.

```
├── app - contient tous les composants
│   ├── common - n'est pas un module de l'application. Cela contient des utilitaires pour l'application React.
│   │   └── utils
│   ├── ratings
│   │   ├── components 
│   │   │   ├── RatingItem 
│   │   │   │   ├── RatingItem.js 
│   │   │   │   └── RatingItem.less 
│   │   │   ├── RatingList 
│   │   │   │   ├── RatingList.js 
│   │   │   │   └── RatingList.less 
│   │   │   ├── RatingsPage.js 
│   │   │   ├── RatingsReducer.js 
│   │   │   └── RatingsActions.js
├── config - tous les fichiers de configuration pour le développement et la production
└── locales - fichiers de localisation
```

### Créez votre premier composant

Créer votre premier composant est relativement facile. Je suppose que vous êtes déjà familiarisé avec React, alors je vais directement au code. Vous pouvez diviser votre code en autant de composants que vous le souhaitez. Un exemple de composant est comme ci-dessous. C'est ainsi que j'ai régulièrement converti de petits composants (présentationnels) peut-être une ul avec des données ou chaque élément d'une ul.

```js
import React from "react";
import PropTypes from "prop-types";

function RatingsItem(props) {
    return (
        <div>
            {props.rating.text}
        </div>
    );
}

RatingsItem.propTypes = {
    rating: PropTypes.shape({
        id: PropTypes.string.isRequired,
        text: PropTypes.bool.isRequired,
        reported: PropTypes.bool.isRequired,
    }),
};

export default RatingsItem;
```

Ces petits composants peuvent maintenant être importés dans notre projet. Lorsque vous définissez votre module dans l'application AngularJS, vous pouvez importer le composant et avec la dépendance react2angular le transformer en directive/composant AngularJS.

```js
.component("ratingsItem", react2angular(RatingsItem))
```

Maintenant, dans le fichier .html, si vous utilisez <ratings-item></ratings-item>, le composant se chargera. Félicitations, c'est votre premier composant React dans Angular !

J'espère que vous n'êtes pas perdu. Êtes-vous avec moi ? ... bien. Souvenez-vous !

> C'est mon premier écrit donc ... soyez indulgent avec votre jugement !

L'étape suivante est de vouloir changer tout le module en React. Cela va être un composant conteneur dans notre application React. Je les ai divisés en pages. Avant de procéder à cela, nous devons commencer à utiliser les actions et les réducteurs Redux. Cela nous aidera dans l'étape suivante lorsque nous combinerons les réducteurs avec Redux !

Ainsi, pour implémenter Redux pour nos composants conteneurs, vous devrez d'abord définir votre réducteur et votre action pour ce composant Rating. Vous pouvez voir la [structure de l'application](https://gist.github.com/panvourtsis/05a6b1118b348c792f64fb18c2e4a534) ci-dessus pour voir la nomenclature et la position de ceux-ci dans mon projet.

Nous n'expliquerons pas les actions et les réducteurs dans ce sujet, car je considère comme un fait que vous êtes déjà familiarisé avec les actions et les réducteurs Redux.

Mon réducteur ressemble à ceci.

```js
import { ADD_RATINGS } from "./RatingsActions";

const initialState = { list: [] };

const RatingsReducer = (state = initialState, action) => {
    switch (action.type) {

    case ADD_RATINGS :
        return {
            ...state,
            list: action.ratings,
        };

    default:
        return state;
    }
};

/* Sélecteurs */

// Obtenir toutes les évaluations
export const getRatings = state => state.Ratings.list;

// Exporter le réducteur
export default RatingsReducer;
```

Les actions ressemblent à ceci.

```js
import callApi from "../common/utils/apiCaller";

export const ADD_RATINGS = "ADD_RATINGS";

export function addRatings(ratings) {
    return {
        type: ADD_RATINGS,
        ratings,
    };
}

export function fetchRatings() {
    return (dispatch) => {
        return callApi("ratings").then(ratings => {
            dispatch(addRatings(ratings));
        });
    };
}
```

Simple ! Faire deux choses juste pour le plaisir de tester que cela fonctionne. Vous pouvez utiliser les vôtres.

Donc, ce sera ma page de ratings. Voici à quoi ressemble ma page. Vous pouvez également passer un "hi there" à l'intérieur de la div pour être sûr d'avoir quelque chose sans données. Encore une fois, juste pour les tests.

```js
import { connect } from "react-redux";
import React, { Component } from "react";
import PropTypes from "prop-types";
// Importer les composants
import RatingList from "./components/RatingList/RatingList";
// Importer les actions
import { fetchRatings } from "./RatingsActions";
// Importer le réducteur
import { getRatings } from "./RatingsReducer";
class RatingsPage extends Component {
    debugger;
    render() {
        return (
            <div>
                <RatingList ratings={this.props.ratings} />
            </div>
        );
    }
}
// Récupérer les données du store en tant que props
const mapStateToProps = (state) => {
    return {
        ratings: getRatings(state)
    }
};
const mapDispatchToProps = (dispatch) => {
    return {
        dispatch,
        fetchRatings: dispatch(fetchRatings()),
    };
}
RatingsPage.propTypes = {
    ratings: PropTypes.arrayOf(PropTypes.object),
    dispatch: PropTypes.func.isRequired,
};
export default connect(mapStateToProps, mapDispatchToProps)(RatingsPage);
```

Maintenant, nous devons utiliser ng-redux afin de créer un store et de transmettre ce store à nos composants. Ce que nous devons faire, c'est combiner tous les réducteurs de notre application comme nous le faisons dans React, donc j'ai créé un fichier séparé pour cela afin de l'utiliser à l'avenir lorsque je supprimerai AngularJS. Je l'appelle "Reducers" et il ressemble à ceci.

Ce qu'il fait réellement, c'est que vous définissez ici tous les réducteurs de votre application afin de les combiner et, dans l'étape suivante, nous "alimentons" ces réducteurs dans Redux pour l'état. Vous verrez que je n'ai que Ratings pour l'instant, mais vous pouvez (et devez) remplir tout nouveau composant en cours de route ici.

```js
import {combineReducers} from "redux";
import Ratings from "./ratings/RatingsReducer";

// Combiner tous les réducteurs en un seul réducteur racine
export const RootReducer = combineReducers({
    Ratings
});
```

Maintenant, nous devons importer Redux. Dans notre fichier principal, lorsque nous définissons l'ensemble de l'application, nous importons les réducteurs combinés, ngRedux, redux thunk et les passons en tant que dépendance de module.

```js
import ngRedux from "ng-redux";
import thunk from "redux-thunk";
import {RootReducer} from "./Reducers";
angular
    .module(
        "funkmartini",
        [
            ...,
            ngRedux,
            .....
        ]
     )
     .config(configApp)
     .run(runApp);
```

Dans la configuration de votre application, je passe le $ngReduxProvider et je crée mon store. Je passe également les outils de développement Redux si vous souhaitez les mettre dans votre projet, sinon, retirez simplement de la fonction createStoreWith.

```js
$ngReduxProvider.createStoreWith(RootReducer, [thunk], [$window.__REDUX_DEVTOOLS_EXTENSION__()]);
```

Vous êtes maintenant prêt. En utilisant $ngRedux dans vos contrôleurs, vous pouvez maintenant obtenir le store de votre application !

### Résumé jusqu'à présent

Nous avons donc créé un petit composant. Ensuite, nous avons refactorisé l'ensemble du module Angular et créé un composant conteneur pour le remplacer. Maintenant, nous voulions passer certaines données et utiliser Redux, c'est pourquoi nous avons créé le store Redux pour avoir un état initial et utiliser nos réducteurs définis dans le fichier pour le mettre à jour.

### Passez ce store aux composants !!

Parce que j'utilisais le $stateProvider dans Angular et que j'avais quelque chose comme ci-dessous. Ce que j'ai fait, c'est arrêter d'utiliser une importation de la page HTML de template et j'ai utilisé directement la page React que j'ai définie comme un composant auparavant dans AngularJS comme nous l'avons fait précédemment. Donc j'ai pris ceci.

```js
function ratingsConfig($stateProvider) {
    $stateProvider
        .state("ratings", {
            url: "/ratings",
            views: {
                "main@settings": {
                    templateUrl: ratingsTemplate,
                    controller: "RatingsController"
                }
            }
        });
}
```

et je l'ai changé en ceci.

```js
function ratingsConfig($stateProvider) {
    $stateProvider
        .state("ratings", {
            url: "/ratings",
            views: {
                "main@settings": {
                    template: `
                        <Ratings-Page store="store"></Ratings-Page>
                    `,
                    controller: "RatingsController"
                }
            }
        });
}
```

Comme vous pouvez le voir, je passe une variable store dans les props de RatingsPage. Vous l'imaginez bien, je n'utilise le RatingsController que pour obtenir et passer ce store. Donc le contrôleur devrait ressembler à ceci

```js
function ratingsController($scope, $ngRedux) {
    $scope.store = $ngRedux;
}
```

De cette façon, Redux peut identifier que le store dans les props est en fait le store dont il a besoin dans la fonction connect().

### Conclusion

Migrer AngularJS vers React/Redux est difficile et peut prendre du temps, mais cela n'a pas à être un cauchemar. Une fois que vous avez fait quelques configurations de base autour du projet, il peut être facilement étendu et devenir progressivement un projet React. Travailler aussi près que possible du JavaScript pur est vraiment génial. Bien que cela puisse prendre un certain temps pour migrer, je pense qu'à long terme, cela en vaut la peine. Les suggestions que j'ai omises dans cet article sont que vous pouvez commencer à utiliser un linting en cours de route (jslint, eslint — airbnb) et n'oubliez pas de tester les nouveaux composants !

Amusez-vous et faites-moi savoir comment cela se passe !

### Ressources

[**Notre parcours de migration de 100k lignes de code d'AngularJS à React (Chapitre 1)**](https://tech.small-improvements.com/2017/01/25/how-to-migrate-an-angularjs-1-app-to-react/)  
[_Ce post résume notre stratégie, nos modèles et les leçons apprises de la migration d'AngularJS à React/Redux._](https://tech.small-improvements.com/2017/01/25/how-to-migrate-an-angularjs-1-app-to-react/)  
[tech.small-improvements.com](https://tech.small-improvements.com/2017/01/25/how-to-migrate-an-angularjs-1-app-to-react/)

[**Migration vers Redux · Redux**](http://redux.js.org/docs/recipes/MigratingToRedux.html)  
[_Créez une fonction appelée createFluxStore(reducer) qui crée un store Flux compatible avec votre application existante à partir d'un..._](http://redux.js.org/docs/recipes/MigratingToRedux.html)  
[redux.js.org](http://redux.js.org/docs/recipes/MigratingToRedux.html)

[**Hashnode/mern-starter**](https://github.com/Hashnode/mern-starter)  
[_mern-starter - Modèle pour commencer avec la stack MERN_](https://github.com/Hashnode/mern-starter)  
[github.com](https://github.com/Hashnode/mern-starter)