---
title: Comment créer une application de recherche de films en utilisant React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-05T17:13:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-movie-search-app-using-react-hooks-24eb72ddfaf7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D9VZ47bgutne4M7LBKmvWg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: reactjs
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment créer une application de recherche de films en utilisant React
  Hooks
seo_desc: 'By Samuel Omole

  React hooks is finally here!!! And I know there has been a whole lot of excitement
  around the possibilities that this new set of APIs present. If you’re still skeptical
  about it, then I urge you to check out this medium article so as ...'
---

Par Samuel Omole

Les hooks React sont enfin [là](https://reactjs.org/blog/2019/02/06/react-v16.8.0.html) !!! Et je sais qu'il y a eu beaucoup d'excitation autour des possibilités que présente ce nouvel ensemble d'API. Si vous êtes encore sceptique à ce sujet, alors je vous invite à consulter cet article sur medium [article](https://medium.com/@dan_abramov/making-sense-of-react-hooks-fdbde8803889) afin de comprendre les problèmes que l'équipe essayait de résoudre lorsqu'ils ont proposé les Hooks.

Initialement, je n'étais pas aussi excité que le reste de la communauté, alors j'ai décidé d'attendre qu'il soit officiellement publié au cas où il y aurait des changements d'API. Donc, le week-end suivant sa sortie, j'ai décidé de lire à ce sujet et, sans surprise, il y avait beaucoup d'articles et de publications sur les hooks et comment commencer à les utiliser.

Je sais que certains pourraient dire « Encore un article sur les hooks, vraiment ? », et à ceux-là, je réponds « Oui… oui et il y en a plus où cela vient ». Pour cet article, nous allons créer une application très simple en utilisant les Hooks. En essence, nous n'allons pas utiliser de composants de classe dans cette application. Et je vais expliquer comment fonctionnent quelques-unes des API et comment elles doivent être utilisées dans toute application que nous pourrions créer.

Ci-dessous se trouve une image de ce à quoi l'application ressemblera une fois terminée :

![Image](https://cdn-media-1.freecodecamp.org/images/kbYsxsxb2D7mBhdlEmUrpMhRmOcQoR79vtT1)
_Je sais, le nom est vraiment créatif…_

En gros, l'application pourra rechercher des films via l'API [OMDB](http://www.omdbapi.com/) et rendre les résultats à l'utilisateur. La raison de la création de cette application est simplement de mieux comprendre l'utilisation des hooks dans une application, ce qui aide à comprendre le rôle que certains des hooks que nous allons utiliser peuvent jouer dans vos propres applications réelles. Certaines choses sont nécessaires avant de commencer à créer l'application :

* Node (⩾ 6)
* Un éditeur de texte cool
* Une clé API de OMDB (Vous pouvez l'obtenir [ici](http://www.omdbapi.com/apikey.aspx) ou utiliser la mienne)

Super, une fois que nous avons cela, l'étape suivante est de configurer l'application React. Pour ce tutoriel, nous allons utiliser **create-react-app** — c'est un outil vraiment génial pour configurer une application React sans avoir à gérer toutes les configurations qui accompagnent le démarrage à partir de zéro. Vous pouvez créer une nouvelle application en tapant :

![Image](https://cdn-media-1.freecodecamp.org/images/itZekSefp8FQezvCnNBJJ-HxtGbESGVb-PNt)

Si vous préférez copier et coller, alors :

```javascript
create-react-app hooked # "hooked" est le nom de notre application

# si vous n'avez pas installé create-react-app, tapez ce qui suit

npm install -g create-react-app
```

Une fois cela fait, nous devrions avoir un dossier appelé « Hooked » avec une structure de répertoire comme indiqué ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/XVEd05SM1ul1KYZ-HWoY3-06cFeeyZS1HemM)
_STRUCTURE INITIALE DU PROJET_

Nous aurons 4 composants dans cette application, alors définissons chacun d'eux et sa fonctionnalité :

* App.js — Il sera le composant parent pour les 3 autres. Il contiendra également la fonction qui gère la demande d'API et il aura une fonction qui appelle l'API lors du rendu initial du composant.
* Header.js — Un composant simple qui rend l'en-tête de l'application et accepte une prop de titre
* Movie.js — Il rend chaque film. L'objet film est simplement passé en tant que props.
* Search.js — Contient un formulaire avec l'élément d'entrée et le bouton de recherche, contient des fonctions qui gèrent l'élément d'entrée et réinitialisent le champ, et contient également une fonction qui appelle la fonction de recherche qui est passée en tant que props.

Commençons à créer, dans le répertoire `src`, un nouveau dossier et nommons-le `components` car c'est là que tous nos composants seront. Nous déplacerons ensuite le fichier `App.js` dans ce dossier. Ensuite, nous créerons le composant `Header`. Créez un fichier appelé `Header.js` et ajoutez le code suivant :

```javascript
import React from "react";

const Header = (props) => {
  return (
    <header className="App-header">
      <h2>{props.text}</h2>
    </header>
  );
};

export default Header;
```

Ce composant ne nécessite pas beaucoup d'explications — c'est essentiellement un composant fonctionnel qui rend la balise `header` avec la prop `text`.

N'oublions pas de mettre à jour l'import dans notre fichier `index.js` :

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './components/App'; // ceci a changé
import * as serviceWorker from './serviceWorker';


ReactDOM.render(<App />, document.getElementById('root'));

// Si vous voulez que votre application fonctionne hors ligne et se charge plus rapidement, vous pouvez changer
// unregister() à register() ci-dessous. Notez que cela comporte quelques pièges.
// En savoir plus sur les service workers : http://bit.ly/CRA-PWA


serviceWorker.unregister();
```

Et mettons également à jour notre `App.css` avec ces styles (non obligatoires) :

```css
.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
  height: 70px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
  padding: 20px;
  cursor: pointer;
}

.spinner {
  height: 80px;
  margin: auto;
}

.App-intro {
  font-size: large;
}

/* nouveau css pour le composant movie */

* {
  box-sizing: border-box;
}

.movies {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
}

.App-header h2 {
  margin: 0;
}

.add-movies {
  text-align: center;
}

.add-movies button {
  font-size: 16px;
  padding: 8px;
  margin: 0 10px 30px 10px;
}

.movie {
  padding: 5px 25px 10px 25px;
  max-width: 25%;
}

.errorMessage {
  margin: auto;
  font-weight: bold;
  color: rgb(161, 15, 15);
}


.search {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 10px;
}


input[type="submit"] {
  padding: 5px;
  background-color: transparent;
  color: black;
  border: 1px solid black;
  width: 80px;
  margin-left: 5px;
  cursor: pointer;
}


input[type="submit"]:hover {
  background-color: #282c34;
  color: antiquewhite;
}


.search > input[type="text"]{
  width: 40%;
  min-width: 170px;
}

@media screen and (min-width: 694px) and (max-width: 915px) {
  .movie {
    max-width: 33%;
  }
}

@media screen and (min-width: 652px) and (max-width: 693px) {
  .movie {
    max-width: 50%;
  }
}


@media screen and (max-width: 651px) {
  .movie {
    max-width: 100%;
    margin: auto;
  }
}
```

Une fois que nous avons cela, la prochaine chose est de créer le composant `Movie`. Nous allons le faire en créant un fichier appelé `Movie.js` et en ajoutant le code suivant :

```javascript
import React from "react";

const DEFAULT_PLACEHOLDER_IMAGE =
  "https://m.media-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SX300.jpg";


const Movie = ({ movie }) => {
  const poster =
    movie.Poster === "N/A" ? DEFAULT_PLACEHOLDER_IMAGE : movie.Poster;
  return (
    <div className="movie">
      <h2>{movie.Title}</h2>
      <div>
        <img
          width="200"
          alt={`The movie titled: ${movie.Title}`}
          src={poster}
        />
      </div>
      <p>({movie.Year})</p>
    </div>
  );
};


export default Movie;
```

Cela nécessite plus d'explications, mais c'est aussi juste un composant de présentation (il n'a pas d'état interne) qui rend le titre du film, l'image et l'année. La raison de `DEFAULT_PLACEHOLDER_IMAGE` est que certains films récupérés de l'API n'ont pas d'images, donc nous allons rendre une image de remplacement au lieu d'un lien brisé.

Maintenant, nous allons créer le composant `Search`. Cette partie est excitante car dans le passé, afin de gérer l'état interne, nous devions créer un composant de classe… mais plus maintenant ! Parce qu'avec les hooks, nous pouvons avoir un composant fonctionnel qui gère son propre état interne. Créons un fichier nommé `Search.js` et dans ce fichier, nous ajouterons le code suivant :

```javascript
import React, { useState } from "react";


const Search = (props) => {
  const [searchValue, setSearchValue] = useState("");
  
  const handleSearchInputChanges = (e) => {
    setSearchValue(e.target.value);
  }

  const resetInputField = () => {
    setSearchValue("")
  }

  const callSearchFunction = (e) => {
    e.preventDefault();
    props.search(searchValue);
    resetInputField();
  }

  return (
      <form className="search">
        <input
          value={searchValue}
          onChange={handleSearchInputChanges}
          type="text"
        />
        <input onClick={callSearchFunction} type="submit" value="RECHERCHER" />
      </form>
    );
}

export default Search;
```

C'est si excitant !!! Je suis sûr que vous venez de voir la première API de hooks que nous allons utiliser, et elle s'appelle `useState`. Comme son nom l'indique, elle nous permet d'ajouter un état React aux composants de fonction. Le hook `useState` accepte un argument qui est l'état initial, puis il retourne un tableau contenant l'état actuel (équivalent à `this.state` pour les composants de classe) et une fonction pour le mettre à jour (équivalent à `this.setState`).

Dans notre cas, nous passons notre état actuel comme valeur pour le champ de saisie de recherche. Lorsque l'événement onChange est appelé, la fonction `handleSearchInputChanges` est appelée, ce qui appelle la fonction de mise à jour de l'état avec la nouvelle valeur. La fonction `resetInputField` appelle essentiellement la fonction de mise à jour de l'état (`setSearchValue`) avec une chaîne vide afin de vider le champ de saisie. Consultez [ceci](https://reactjs.org/docs/hooks-state.html) pour en savoir plus sur l'API `useState`.

Enfin, nous allons mettre à jour le fichier `App.js` avec le code suivant :

```javascript
import React, { useState, useEffect } from "react";
import "../App.css";
import Header from "./Header";
import Movie from "./Movie";
import Search from "./Search";


const MOVIE_API_URL = "https://www.omdbapi.com/?s=man&apikey=4a3b711b"; // vous devriez remplacer ceci par le vôtre


const App = () => {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  const [errorMessage, setErrorMessage] = useState(null);

    useEffect(() => {
    fetch(MOVIE_API_URL)
      .then(response => response.json())
      .then(jsonResponse => {
        setMovies(jsonResponse.Search);
        setLoading(false);
      });
  }, []);

    const search = searchValue => {
    setLoading(true);
    setErrorMessage(null);

    fetch(`https://www.omdbapi.com/?s=${searchValue}&apikey=4a3b711b`)
      .then(response => response.json())
      .then(jsonResponse => {
        if (jsonResponse.Response === "True") {
          setMovies(jsonResponse.Search);
          setLoading(false);
        } else {
          setErrorMessage(jsonResponse.Error);
          setLoading(false);
        }
      });
  	};

    
    return (
     <div className="App">
      <Header text="HOOKED" />
      <Search search={search} />
      <p className="App-intro">Partage de quelques-uns de nos films préférés</p>
      <div className="movies">
        {loading && !errorMessage ? (
         <span>chargement...</span>
         ) : errorMessage ? (
          <div className="errorMessage">{errorMessage}</div>
        ) : (
          movies.map((movie, index) => (
            <Movie key={`${index}-${movie.Title}`} movie={movie} />
          ))
        )}
      </div>
    </div>
  );
};


export default App;
```

Passons en revue le code : nous utilisons 3 fonctions `useState`, donc oui, nous pouvons avoir plusieurs fonctions `useState` dans un composant. La première est utilisée pour gérer l'état de chargement (elle rend un texte 'chargement...' lorsque le chargement est défini sur vrai). La seconde est utilisée pour gérer le tableau de films obtenu du serveur. Et enfin, la troisième est utilisée pour gérer les erreurs qui pourraient survenir lors de la demande d'API.

Et après cela, nous rencontrons la deuxième API de hooks que nous utilisons dans l'application : le hook `useEffect`. Ce hook vous permet essentiellement d'effectuer des effets secondaires dans vos composants de fonction. Par effets secondaires, nous entendons des choses comme la récupération de données, les abonnements et les manipulations manuelles du DOM. La meilleure partie de ce hook est cette citation des docs officiels de React :

> Si vous êtes familier avec les méthodes de cycle de vie des composants React, vous pouvez penser au hook `useEffect` comme à `componentDidMount`, `componentDidUpdate` et `componentWillUnmount` combinés.

C'est parce que `useEffect` est appelé après le premier rendu (`componentDidMount`) et aussi après chaque mise à jour (`componentDidUpdate`).

Je sais que vous vous demandez peut-être comment cela est similaire à `componentDidMount` s'il est appelé après chaque mise à jour. Eh bien, c'est à cause de la fonction `useEffect` qui accepte deux arguments, la fonction que vous voulez exécuter et un deuxième argument qui est un tableau. Dans ce tableau, nous passons simplement une valeur qui indique à React de sauter l'application d'un effet si la valeur passée n'a pas changé.

Selon les docs, c'est similaire à lorsque nous ajoutons une instruction conditionnelle dans notre `componentDidUpdate` :

```javascript

// pour les composants de classe
componentDidUpdate(prevProps, prevState) {
  if (prevState.count !== this.state.count) {
    document.title = `Vous avez cliqué ${this.state.count} fois`;
  }
}


// en utilisant les hooks, cela deviendra
useEffect(() => {
  document.title = `Vous avez cliqué ${count} fois`;
}, [count]); // Ne réexécutez l'effet que si count change
```

Dans notre cas, nous n'avons aucune valeur qui change, donc nous pouvons passer un tableau vide qui indique à React que cet effet doit être appelé une fois.

Comme vous pouvez le voir, nous avons 3 fonctions `useState` qui sont quelque peu liées, et il devrait être possible de les combiner d'une certaine manière. Heureusement, l'équipe React nous a couvert car ils ont créé un hook qui aide avec cela — et ce hook s'appelle `useReducer`. Convertissons notre composant `App` pour utiliser notre nouveau hook, donc notre `App.js` ressemblera maintenant à ceci :

```javascript
import React, { useReducer, useEffect } from "react";
import "../App.css";
import Header from "./Header";
import Movie from "./Movie";
import Search from "./Search";


const MOVIE_API_URL = "https://www.omdbapi.com/?s=man&apikey=4a3b711b";


const initialState = {
  loading: true,
  movies: [],
  errorMessage: null
};


const reducer = (state, action) => {
  switch (action.type) {
    case "SEARCH_MOVIES_REQUEST":
      return {
        ...state,
        loading: true,
        errorMessage: null
      };
    case "SEARCH_MOVIES_SUCCESS":
      return {
        ...state,
        loading: false,
        movies: action.payload
      };
    case "SEARCH_MOVIES_FAILURE":
      return {
        ...state,
        loading: false,
        errorMessage: action.error
      };
    default:
      return state;
  }
};



const App = () => {
  const [state, dispatch] = useReducer(reducer, initialState);

    useEffect(() => {
    
        fetch(MOVIE_API_URL)
            .then(response => response.json())
            .then(jsonResponse => {
        
            dispatch({
                type: "SEARCH_MOVIES_SUCCESS",
                payload: jsonResponse.Search
        	});
      	});
  	}, []);

    const search = searchValue => {
    	dispatch({
      	type: "SEARCH_MOVIES_REQUEST"
    	});
	
        fetch(`https://www.omdbapi.com/?s=${searchValue}&apikey=4a3b711b`)
      	.then(response => response.json())
      	.then(jsonResponse => {
        	if (jsonResponse.Response === "True") {
          	dispatch({
                type: "SEARCH_MOVIES_SUCCESS",
                payload: jsonResponse.Search
          	});
        	} else {
          	dispatch({
                type: "SEARCH_MOVIES_FAILURE",
                error: jsonResponse.Error
          	});
          }
      	});
	  };

    const { movies, errorMessage, loading } = state;

    return (
    <div className="App">
      <Header text="HOOKED" />
      <Search search={search} />
      <p className="App-intro">Partage de quelques-uns de nos films préférés</p>
      <div className="movies">
        {loading && !errorMessage ? (
          <span>chargement... </span>
        ) : errorMessage ? (
          <div className="errorMessage">{errorMessage}</div>
        ) : (
          movies.map((movie, index) => (
            <Movie key={`${index}-${movie.Title}`} movie={movie} />
          ))
        )}
      </div>
    </div>
  );
};

export default App;
```

Donc, si tout s'est bien passé, nous ne devrions voir aucun changement dans le comportement de l'application. Maintenant, passons en revue comment fonctionne le hook `useReducer`.

Le hook prend 3 arguments, mais pour notre cas d'utilisation, nous allons utiliser seulement 2. Un hook `useReducer` typique ressemblera à ceci :

```javascript
const [state, dispatch] = useReducer(
    reducer,
    initialState
);
```

L'argument `reducer` est similaire à ce que nous utilisons dans Redux, qui ressemble à ceci :

```javascript
const reducer = (state, action) => {
  switch (action.type) {
    case "SEARCH_MOVIES_REQUEST":
      return {
        ...state,
        loading: true,
        errorMessage: null
      };
    case "SEARCH_MOVIES_SUCCESS":
      return {
        ...state,
        loading: false,
        movies: action.payload
      };
    case "SEARCH_MOVIES_FAILURE":
      return {
        ...state,
        loading: false,
        errorMessage: action.error
      };
    default:
      return state;
  }
};
```

Le reducer prend l'initialState et l'action, donc en fonction du type d'action, le reducer retourne un nouvel objet d'état. Par exemple, si le type d'action qui est dispatché est `SEARCH_MOVIES_REQUEST`, l'état est mis à jour avec le nouvel objet où la valeur pour `loading` est true et `errorMessage` est null.

Une autre chose à noter est que dans notre `useEffect`, nous dispatchons maintenant une action avec le payload comme le tableau de films que nous obtenons du serveur. De plus, dans notre fonction `search`, nous dispatchons en fait trois actions différentes.

* Une action est l'action `SEARCH_MOVIES_REQUEST` qui met à jour notre objet d'état, rendant `loading=true et errorMessage = null`.
* Si la requête est réussie, nous dispatchons une autre action avec le type `SEARCH_MOVIES_SUCCESS` qui met à jour notre objet d'état rendant `loading=false et movies = action.payload` où le payload est le tableau de films obtenu de OMDB.
* Si une erreur survient, nous dispatchons une action différente avec le type `SEARCH_MOVIES_FAILURE` qui met à jour notre objet d'état rendant `loading=false et errorMessage = action.error` où `action.error` est le message d'erreur obtenu du serveur.

Pour en savoir plus sur le hook `useReducer`, vous pouvez consulter la documentation officielle [documentation](https://reactjs.org/docs/hooks-reference.html#usereducer).

#### Conclusion

Wow !!! Nous avons parcouru un long chemin et je suis sûr que vous êtes aussi excité que moi par les possibilités des hooks. Pour moi personnellement, il est beaucoup plus facile d'initier les débutants à React, car je n'ai pas besoin d'expliquer comment fonctionnent les classes ou comment fonctionne `this`, ou comment fonctionne `bind` en JS, ce qui est génial à mon avis.

Nous n'avons abordé que quelques hooks dans ce tutoriel, et nous n'avons même pas couvert des fonctionnalités comme la création de nos propres hooks [personnalisés](https://reactjs.org/docs/hooks-custom.html). Si vous avez d'autres cas d'utilisation pour les hooks ou si vous avez implémenté votre propre hook personnalisé, n'hésitez pas à laisser un commentaire et à rejoindre l'excitation.

NOTE : Cet article n'est pas lié au précédent sur [Webpack](https://medium.freecodecamp.org/how-to-build-modern-applications-with-webpack-c81ccf6dd54f), un article ultérieur à ce sujet est déjà en construction ?.

Voici le [lien](https://github.com/samie820/hooks-movie-app) vers le dépôt GitHub pour cet article.