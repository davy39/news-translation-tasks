---
title: Comment j'ai architecturé une application React monopage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-13T15:21:45.000Z'
originalURL: https://freecodecamp.org/news/how-i-architected-a-single-page-react-application-3ebd90f59087
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XLkAyY1s1ON4sMc3zLC2hQ.png
tags:
- name: Apps
  slug: apps-tag
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Comment j'ai architecturé une application React monopage
seo_desc: 'By Gooi Ying Chyi

  With Data Structures, Components and integration with Redux


  _Background photo by [Unsplash](https://unsplash.com/photos/A-btl_OPYWA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" ...'
---

Par Gooi Ying Chyi

#### Avec des structures de données, des composants et une intégration avec Redux

![Image](https://cdn-media-1.freecodecamp.org/images/nND6eYTLXiJIuT1h3LBvVG3Vk5-UAWrU1NL2)
_Photo de fond par [Unsplash](https://unsplash.com/photos/A-btl_OPYWA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Sven Mieke</a> sur <a href="https://unsplash.com/search/photos/architect?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

J'ai récemment construit une application monopage qui interagit avec un serveur backend JSON API. J'ai choisi d'utiliser React pour approfondir ma compréhension des fondamentaux de React et de la manière dont chaque outil peut aider à construire un frontend évolutif.

La stack de cette application se compose de :

* Frontend avec React/Redux
* Un serveur backend JSON API avec Sinatra, intégré avec Postgres pour la persistance de la base de données
* Un client API qui récupère des données depuis [OMDb API](http://www.omdbapi.com/), écrit en Ruby

Pour cet article, nous supposerons que le backend est terminé. Concentrons-nous donc sur la manière dont les décisions de conception sont prises sur le frontend.

> Note : Les décisions présentées ici sont à titre de référence uniquement et peuvent varier en fonction des besoins de votre application. Une application exemple de suivi de films OMDb est utilisée ici à des fins de démonstration.

### L'Application

L'application se compose d'un formulaire de recherche. Un utilisateur peut saisir un titre de film pour obtenir un résultat de film depuis [OMDb](http://www.omdbapi.com/). L'utilisateur peut également sauvegarder un film avec une note et un court commentaire dans une liste de favoris.

**Pour voir l'application finale, [cliquez ici](https://omdb-tracker.herokuapp.com/).** Pour voir le code source, cliquez [ici](https://github.com/YingCGooi/omdb-tracker/tree/master/public/js).

Lorsque l'utilisateur recherche un film sur la page d'accueil, cela ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0gKNb-YMTg5WJIH7IsZjxZe1ql7mSfRSXvFm)
_L'interface utilisateur contient un formulaire de recherche et un résultat de film en dessous._

Pour simplifier, nous allons nous concentrer uniquement sur la conception des fonctionnalités principales de l'application dans cet article. Vous pouvez également passer à la [**Partie II : Redux**](https://medium.com/p/d6eaf235f4d) de la série.

### Structure de données

Définir des structures de données appropriées devrait être l'un des aspects les plus importants de la conception d'une application. Cela devrait être la première étape, car cela détermine non seulement comment le frontend doit rendre les éléments, mais aussi comment le serveur API doit retourner les réponses JSON.

Pour cette application, nous aurons besoin de deux informations principales pour rendre correctement notre interface utilisateur : **un résultat de film unique** et **une liste de films favoris**.

#### Objet résultat de film

Un résultat de film unique contiendra des informations telles que le titre, l'année, la description et l'image de l'affiche. Avec cela, nous devons définir un objet qui peut stocker ces attributs :

```
{  "title": "Star Wars: Episode IV - A New Hope",  "year": "1977",  "plot": "Luke Skywalker rejoint ses forces avec un chevalier Jedi...",  "poster": "https://m.media-amazon.com/path/to/poster.jpg",  "imdbID": "tt0076759"}
```

La propriété `poster` est simplement une URL vers l'image de l'affiche qui sera affichée dans les résultats. Si aucune affiche n'est disponible pour ce film, elle sera « N/A », ce qui affichera un espace réservé. Nous aurons également besoin d'un attribut `imdbID` pour identifier de manière unique chaque film. Cela est utile pour déterminer si un résultat de film existe déjà dans la liste des favoris. Nous explorerons plus tard comment cela fonctionne.

#### Liste des favoris

La liste des favoris contiendra tous les films enregistrés comme favoris. La liste ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/yePajd0g-58FZyL3VjU4p5FpUIopTxekHRId)
_Chaque film inclut également des informations supplémentaires sur les favoris (note et commentaire)_

```
[  { title: "Star Wars", year: "1977", ..., rating: 4 },  { title: "Avatar", year: "2009", ..., rating: 5 }]
```

Gardez à l'esprit que nous devrons rechercher un film spécifique dans la liste, et la complexité temporelle de cette approche est **O(N)**. Bien que cela fonctionne bien pour des ensembles de données plus petits, imaginez devoir rechercher un film dans une liste de favoris qui croît indéfiniment.

Avec cela à l'esprit, j'ai choisi d'utiliser une table de hachage avec des clés comme `imdbID` et des valeurs comme objets de films favoris :

```
{  tt0076759: {    title: "Star Wars: Episode IV - A New Hope",    year: "1977",    plot: "...",    poster: "...",    rating: "4",    comment: "Que la force soit avec vous !",  },  tt0499549: {    title: "Avatar",    year: "2009",    plot: "...",    poster: "...",    rating: "5",    comment: "Film préféré !",  }}
```

Avec cela, nous pouvons rechercher un film dans la liste des favoris en **O(1)** temps par son `imdbID`.

> Note : la complexité d'exécution n'a probablement pas d'importance dans la plupart des cas, car les ensembles de données sont généralement petits côté client. Nous allons également effectuer des opérations de découpage et de copie (également des opérations O(N)) dans Redux de toute façon. Mais en tant qu'ingénieur, il est bon d'être conscient des optimisations potentielles que nous pouvons effectuer.

### Composants

Les composants sont au cœur de React. Nous devons déterminer lesquels interagiront avec le store Redux et lesquels sont uniquement pour la présentation. Nous pouvons également réutiliser certains des composants de présentation. Notre hiérarchie de composants ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/CQkO-xEK5ZexcrR2ZcxtT4EEssWFfFVfjTHQ)

#### Page principale

Nous désignons notre composant **App** au niveau supérieur. Lorsque le chemin racine est visité, il doit rendre le **SearchContainer**. Il doit également afficher des messages flash à l'utilisateur et gérer le routage côté client.

Le **SearchContainer** récupérera le résultat du film depuis notre store Redux, fournissant des informations en tant que props à **MovieItem** pour le rendu. Il enverra également une action de recherche lorsque l'utilisateur soumet une recherche dans **SearchInputForm**. Plus d'informations sur Redux plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/-vfxKYTuzgfogu4M6eL7rL4JjdDimzZeJgJN)
_Une modale qui permet aux utilisateurs d'ajouter une note et un commentaire lors de l'enregistrement d'un favori._

#### Formulaire Ajouter aux Favoris

Lorsque l'utilisateur clique sur le bouton « Ajouter aux Favoris », nous afficherons le **AddFavoriteForm**, un [composant contrôlé](https://reactjs.org/docs/forms.html).

Nous mettons constamment à jour son état chaque fois qu'un utilisateur change la note ou le texte d'entrée dans la zone de texte du commentaire. Cela est utile pour la validation lors de la soumission du formulaire.

Le **RatingForm** est responsable de l'affichage des étoiles jaunes lorsque l'utilisateur clique dessus. Il informe également la valeur de la note actuelle à **AddFavoriteForm**.

![Image](https://cdn-media-1.freecodecamp.org/images/sI9SYwjKc0LvLer5OQLAsKTnvbA7etM-Of0S)
_Le FavoritesContainer contient une liste de composants MovieItem_

#### Onglet Favoris

Lorsque l'utilisateur clique sur l'onglet « Favoris », l'**App** rend **FavoritesContainer**.

Le **FavoritesContainer** est responsable de la récupération de la liste des favoris depuis le store Redux. Il envoie également des actions lorsque l'utilisateur change une note ou clique sur le bouton « Supprimer ».

Nos composants **MovieItem** et **FavoritesInfo** sont simplement des composants de présentation qui reçoivent des props depuis **FavoritesContainer**.

Nous réutiliserons le composant **RatingForm** ici. Lorsque l'utilisateur clique sur une étoile dans le **RatingForm**, le **FavoritesContainer** reçoit la valeur de la note et envoie une action de mise à jour de la note au store Redux.

### Store Redux

Notre store Redux inclura des reducers qui gèrent les actions de recherche et de favoris. De plus, nous aurons besoin d'inclure un reducer de statut pour suivre les changements d'état lorsqu'un utilisateur initie une action. Nous explorerons plus en détail le reducer de statut plus tard.

```
//store.js
```

```
import { createStore, combineReducers, applyMiddleware } from 'redux';import thunk from "redux-thunk";
```

```
import search from './reducers/searchReducer';import favorites from './reducers/favoritesReducer';import status from './reducers/statusReducer';
```

```
export default createStore(  combineReducers({    search,    favorites,    status  }),  {},  applyMiddleware(thunk))
```

Nous appliquerons également le middleware Redux Thunk immédiatement. Nous entrerons plus en détail sur cela plus tard. Maintenant, déterminons comment nous gérons les changements d'état lorsqu'un utilisateur soumet une recherche.

### Reducer de Recherche

Lorsque l'utilisateur effectue une action de recherche, nous voulons mettre à jour le store avec un nouveau résultat de recherche via **searchReducer**. Nous pouvons ensuite rendre nos composants en conséquence. Le flux général des événements ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0yVmnP0XRxj058OjNxAnsYZ2mLIZCXxVL-tZ)

Nous traiterons « Obtenir le résultat de la recherche » comme une boîte noire pour l'instant. Nous explorerons comment cela fonctionne plus tard avec Redux Thunk. Maintenant, implémentons la fonction de reducer.

```
//searchReducer.js
```

```
const initialState = {  "title": "",  "year": "",  "plot": "",  "poster": "",  "imdbID": "",}
```

```
export default (state = initialState, action) => {  if (action.type === 'SEARCH_SUCCESS') {    state = action.result;  }  return state;}
```

L'**initialState** représentera la structure de données définie précédemment comme un objet de résultat de film unique. Dans la fonction de reducer, nous gérons l'action où une recherche est réussie. Si l'action est déclenchée, nous réassignons simplement l'état au nouvel objet de résultat de film.

```
//searchActions.jsexport const searchSuccess = (result) => ({  type: 'SEARCH_SUCCESS', result});
```

Nous définissons une action appelée **searchSuccess** qui prend un seul argument, l'objet de résultat de film, et retourne un objet d'action de type « **SEARCH_SUCCESS** ». Nous allons envoyer cette action lors d'un appel d'API de recherche réussi.

### Redux Thunk : Recherche

Explorons comment fonctionne le « Obtenir le résultat de la recherche » mentionné précédemment. Tout d'abord, nous devons faire un appel d'API distant à notre serveur backend API. Lorsque la requête reçoit une réponse JSON réussie, nous allons envoyer l'action **searchSuccess** ainsi que la charge utile à **searchReducer**.

Sachant que nous devons envoyer après qu'un appel asynchrone est terminé, nous allons utiliser [Redux Thunk](https://github.com/reduxjs/redux-thunk). Thunk entre en jeu pour effectuer plusieurs envois ou retarder un envoi. Avec Thunk, notre flux d'événements mis à jour ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/yHA6xMauC4xW6a1nEIAdacp5WFVFSdeISmD-)

Pour cela, nous définissons une fonction qui prend un seul argument `title` et sert d'action initiale **search**. Cette fonction est responsable de la récupération du résultat de la recherche et de l'envoi d'une action **searchSuccess** :

```
//searchActions.jsimport apiClient from '../apiClient';
```

```
...
```

```
export function search(title) {  return (dispatch) => {    apiClient.query(title)      .then(response => {        dispatch(searchSuccess(response.data))      });  }}
```

Nous avons configuré notre client API au préalable, et vous pouvez en lire plus sur [comment j'ai configuré le client API ici](https://medium.com/@gooiyingchyi/how-i-architected-a-single-page-react-application-part-i-data-structure-components-and-apis-24386cc78a6#40eb). La méthode `apiClient.query` effectue simplement une requête GET AJAX à notre serveur backend et retourne une promesse avec les données de réponse.

Nous pouvons ensuite connecter cette fonction comme un envoi d'action à notre composant **SearchContainer** :

```
//SearchContainer.js
```

```
import React from 'react';import { connect } from 'react-redux';import { search } from '../actions/searchActions';
```

```
...
```

```
const mapStateToProps = (state) => (  {    result: state.search,  });
```

```
const mapDispatchToProps = (dispatch) => (  {    search(title) {      dispatch(search(title))    },  });
```

```
export default connect(mapStateToProps, mapDispatchToProps)(SearchContainer);
```

Lorsque la requête de recherche réussit, notre composant **SearchContainer** rendra le résultat du film :

![Image](https://cdn-media-1.freecodecamp.org/images/wKuIVFaH6OSKpSeLBSDal3InlrYE90kQ2G7n)
_Gauche : l'application rend le résultat du film | Droite : une requête de recherche réussie_

### Gestion des autres statuts de recherche

Maintenant que notre action **search** fonctionne correctement et est connectée à notre composant **SearchContainer**, nous aimerions gérer d'autres cas que celui d'une recherche réussie.

#### Requête de recherche en attente

Lorsque l'utilisateur soumet une recherche, nous afficherons une animation de chargement pour indiquer que la requête de recherche est en attente :

![Image](https://cdn-media-1.freecodecamp.org/images/21mRK3c6oKbo-jrWRsZJUVKIod0rOiV0aYJY)
_L'application affiche une animation de chargement en attendant le résultat de la recherche_

#### Requête de recherche échouée

Si la recherche échoue, nous afficherons un message d'erreur approprié à l'utilisateur. Cela est utile pour fournir un contexte. Une erreur de recherche peut se produire dans les cas où un titre de film n'est pas disponible, ou notre serveur rencontre des problèmes de communication avec l'API OMDb.

![Image](https://cdn-media-1.freecodecamp.org/images/QaamwSGVP5uJZINbdEe9W4v5j8OpEF3TH2GZ)
_Lorsqu'un titre de film n'est pas trouvé dans OMDb, nous affichons un message d'erreur_

Pour gérer différents statuts de recherche, nous aurons besoin d'un moyen de stocker et de mettre à jour le statut actuel ainsi que les messages d'erreur.

### Reducer de Statut

Le **statusReducer** est responsable du suivi des changements d'état chaque fois qu'un utilisateur effectue une action. L'état actuel d'une action peut être représenté par l'un des trois « statuts » :

* En attente (lorsqu'un utilisateur initie l'action)
* Succès (lorsqu'une requête retourne une réponse réussie)
* Erreur (lorsqu'une requête retourne une réponse d'erreur)

Avec ces statuts en place, nous pouvons rendre différentes interfaces utilisateur en fonction du statut actuel d'un type d'action donné. Dans ce cas, nous allons nous concentrer sur le suivi du statut de l'action **search**.

Nous commencerons par implémenter le **statusReducer**. Pour l'état initial, nous devons suivre le statut de recherche actuel et les erreurs :

```
// statusReducer.jsconst initialState = {  search: '',      // statut de la recherche actuelle  searchError: '', // message d'erreur lorsqu'une recherche échoue}
```

Ensuite, nous devons définir la fonction de reducer. Chaque fois que notre **SearchContainer** envoie une action « SEARCH_[STATUS] », nous mettrons à jour le store en remplaçant les propriétés `search` et `searchError`.

```
// statusReducer.js
```

```
...
```

```
export default (state = initialState, action) => {  const actionHandlers = {    'SEARCH_REQUEST': {      search: 'PENDING',      searchError: '',    },    'SEARCH_SUCCESS': {      search: 'SUCCESS',       searchError: '',          },    'SEARCH_FAILURE': {      search: 'ERROR',      searchError: action.error,     },  }  const propsToUpdate = actionHandlers[action.type];  state = Object.assign({}, state, propsToUpdate);  return state;}
```

Nous utilisons une table de hachage `actionHandlers` ici puisque nous remplaçons uniquement les propriétés de l'état. De plus, cela améliore la lisibilité plus que l'utilisation d'instructions `if/else` ou `case`.

Avec notre **statusReducer** en place, nous pouvons rendre l'interface utilisateur en fonction de différents statuts de recherche. Nous mettrons à jour notre flux d'événements comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/moKAD85gibVfj7nAGAWQ0DOHWGnUCROV1Kvs)

Nous avons maintenant des actions supplémentaires **searchRequest** et **searchFailure** disponibles pour envoyer au store :

```
//searchActions.js
```

```
export const searchRequest = () => ({  type: 'SEARCH_REQUEST'});
```

```
export const searchFailure = (error) => ({  type: 'SEARCH_FAILURE', error});
```

Pour mettre à jour notre action **search**, nous allons envoyer **searchRequest** immédiatement et nous allons envoyer **searchSuccess** ou **searchFailure** en fonction du succès ou de l'échec éventuel de la promesse retournée par Axios :

```
//searchActions.js
```

```
...
```

```
export function search(title) {  return (dispatch) => {    dispatch(searchRequest());
```

```
apiClient.query(title)      .then(response => {        dispatch(searchSuccess(response.data))      })      .catch(error => {        dispatch(searchFailure(error.response.data))      });  }}
```

Nous pouvons maintenant connecter l'état du statut de recherche à notre **SearchContainer**, le passant en tant que prop. Chaque fois que notre store reçoit les changements d'état, notre **SearchContainer** rend une animation de chargement, un message d'erreur ou le résultat de la recherche :

```
//SearchContainer.js
```

```
...(imports omis)
```

```
const SearchContainer = (props) => (  <main id='search-container'>    <SearchInputForm       placeholder='Rechercher un titre de film...'      onSubmit={ (title) => props.search(title) }    />    {      (props.searchStatus === 'SUCCESS')      ? <MovieItem          movie={ props.result }          ...(other props)        />      : null    }    {      (props.searchStatus === 'PENDING')      ? <section className='loading'>          <img src='../../images/loading.gif' />        </section>      : null    }    {      (props.searchStatus === 'ERROR')      ? <section className='error'>           <p className='error'>            <i className="red exclamation triangle icon"></i>            { props.searchError }          </p>        </section>      : null    }  </main>);
```

```
const mapStateToProps = (state) => (  {    searchStatus: state.status.search,    searchError: state.status.searchError,    result: state.search,  });
```

```
...
```

### Reducer de Favoris

Nous devons gérer les actions CRUD effectuées par un utilisateur sur la liste des favoris. En rappelant nos points de terminaison API précédents, nous aimerions permettre aux utilisateurs d'effectuer les actions suivantes et de mettre à jour notre store en conséquence :

* Enregistrer un film dans la liste des favoris
* Récupérer tous les films favoris
* Mettre à jour la note d'un favori
* Supprimer un film de la liste des favoris

Pour garantir que la fonction de reducer est pure, nous copions simplement l'ancien état dans un nouvel objet avec toutes les nouvelles propriétés en utilisant `Object.assign`. Notez que nous ne gérons que les actions avec des types de **_SUCCESS** :

```
//favoritesReducer.js
```

```
export default (state = {}, action) => {  switch (action.type) {    case 'SAVE_FAVORITE_SUCCESS':      state = Object.assign({}, state, action.favorite);      break;
```

```
case 'GET_FAVORITES_SUCCESS':      state = action.favorites;      break;
```

```
case 'UPDATE_RATING_SUCCESS':      state = Object.assign({}, state, action.favorite);      break;
```

```
case 'DELETE_FAVORITE_SUCCESS':      state = Object.assign({}, state);      delete state[action.imdbID];      break;
```

```
default: return state;  }  return state;}
```

Nous laisserons l'**initialState** comme un objet vide. La raison est que si notre **initialState** contient des éléments de film de remplissage, notre application les rendra immédiatement avant d'attendre la réponse réelle de la liste des favoris de notre serveur backend API.

À partir de maintenant, chacune des actions de favoris suivra un flux général d'événements illustré ci-dessous. Le schéma est similaire à l'action de recherche dans la section précédente, sauf que nous allons sauter la gestion de tout statut « PENDING ».

![Image](https://cdn-media-1.freecodecamp.org/images/DEOjBJXFxeZIaQDKMU5Y-4aQbLX98VRy3R4d)

#### Action Enregistrer les Favoris

Prenons l'action d'enregistrement des favoris par exemple. La fonction fait un appel API avec notre **apiClient** et envoie soit une action **saveFavoriteSuccess**, soit une action **saveFavoriteFailure**, selon que nous recevons une réponse réussie ou non :

```
//favoritesActions.jsimport apiClient from '../apiClient';
```

```
export const saveFavoriteSuccess = (favorite) => ({  type: 'SAVE_FAVORITE_SUCCESS', favorite});
```

```
export const saveFavoriteFailure = (error) => ({  type: 'SAVE_FAVORITE_FAILURE', error});
```

```
export function save(movie) {  return (dispatch) => {    apiClient.saveFavorite(movie)      .then(res => {        dispatch(saveFavoriteSuccess(res.data))      })      .catch(err => {        dispatch(saveFavoriteFailure(err.response.data))      });  }}
```

Nous pouvons maintenant connecter l'action **save** favorite à **AddFavoriteForm** via React Redux.

Pour en savoir plus sur la manière dont j'ai géré le flux pour afficher les messages flash, [cliquez ici](https://blog.usejournal.com/how-i-architected-a-single-page-react-application-part-ii-redux-d6eaf235f4d#956b).

### Conclusion

La conception du frontend d'une application nécessite une certaine réflexion préalable, même lorsque l'on utilise une bibliothèque JavaScript populaire comme React. En réfléchissant à la manière dont les structures de données, les composants, les API et la gestion d'état fonctionnent dans leur ensemble, nous pouvons mieux anticiper les cas limites et corriger efficacement les erreurs lorsqu'elles surviennent. En utilisant certains modèles de conception tels que les composants contrôlés, Redux et la gestion du flux AJAX en utilisant Thunk, nous pouvons rationaliser la gestion du flux de retour d'information de l'interface utilisateur aux actions de l'utilisateur. En fin de compte, la manière dont nous abordons la conception aura un impact sur l'utilisabilité, la clarté et l'évolutivité future.

#### Références

[Fullstack React: The Complete Guide to ReactJS and Friends](https://www.fullstackreact.com/#table-of-contents)

### À propos de moi

Je suis un ingénieur logiciel basé à NYC et co-créateur de [SpaceCraft](https://spacecraft-repl.com). J'ai de l'expérience dans la conception d'applications monopages, la synchronisation de l'état entre plusieurs clients et le déploiement d'applications évolutives avec Docker.

**Je suis actuellement à la recherche de ma prochaine opportunité à temps plein ! Veuillez [me contacter](https://gooi.tech) si vous pensez que je pourrais être un bon candidat pour votre équipe.**