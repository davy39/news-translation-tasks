---
title: Tutoriel d'application de films React - Construisez un projet de portfolio
  amusant avec React et l'API OMBD
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2020-11-18T22:25:56.000Z'
originalURL: https://freecodecamp.org/news/react-movie-app-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/react-movie-app--2-.png
tags:
- name: api
  slug: api
- name: portfolio
  slug: portfolio
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: Tutoriel d'application de films React - Construisez un projet de portfolio
  amusant avec React et l'API OMBD
seo_desc: 'In this React movie app tutorial, we''re going to:


  Use a real API to search for movies as we type

  Create a "Netflix style" horizontal scroll effect

  Add movies to and remove them from our favourites

  Save our favourites to local storage to they appear ...'
---

Dans ce tutoriel d'application de films React, nous allons :

* Utiliser une vraie API pour rechercher des films au fur et à mesure que nous tapons
* Créer un effet de défilement horizontal "style Netflix"
* Ajouter des films à nos favoris et les supprimer
* Sauvegarder nos favoris dans le stockage local pour qu'ils apparaissent lorsque l'application se rafraîchit

### Voici ce que nous allons construire :   


![Image](https://www.freecodecamp.org/news/content/images/2020/11/Nov-10-2020-07-21-23.gif)



Et voici une visite guidée en vidéo si vous souhaitez compléter votre lecture. 

%[https://www.youtube.com/watch?v=jc9_Bqzy2YQ]



Enfin, au cas où vous vous perdriez en suivant, [vous pouvez récupérer le code final ici](https://github.com/chrisblakely01/react-movie-app) (sur GitHub).

## C'est parti !

Notre application de films ne serait pas très utile si nous n'avions aucun film à afficher.

Nous allons utiliser l'[API OMDB](http://www.omdbapi.com/) comme source pour les films. Cette API est gratuite, et tout ce que nous avons à faire est de nous inscrire et d'obtenir une clé API.

## Comment obtenir une clé API 

Allez sur [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx) et remplissez le formulaire. Vous devriez recevoir un email comme celui-ci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-10-at-07.37.11.png)

Cliquez sur le lien d'activation (surligné en vert) et vous êtes prêt à partir. Hourra !

## Explorer l'API avec PostMan

Cette étape est facultative, donc si vous préférez passer directement à la partie React, n'hésitez pas à sauter à la section suivante.  
  
Nous allons utiliser Postman ([téléchargez-le ici si vous ne l'avez pas](https://www.postman.com/downloads/)) pour jouer avec l'API. 

Lancez Postman et collez l'URL de l'API "OMBb" que vous avez reçue dans votre email (surlignée en jaune dans l'image ci-dessus). Cliquez sur "envoyer" et vous devriez obtenir du JSON dans la section "body" comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-10-at-07.53.58.png)

Mission réussie ! Enfin, une partie de la mission est un succès – nous ne faisons que commencer après tout. Mais cela signifie que notre URL de l'email fonctionne correctement et que notre application React pourra récupérer des films.

## Comment rechercher des films par titre

Jusqu'à présent, nous avons utilisé l'API pour récupérer un film, mais ce que nous voulons faire, c'est rechercher des "Titres contenant un terme de recherche". Pour ce faire, nous changeons le paramètre de requête `i` en `s` comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-10-at-07.58.19.png)

Cela interrogera l'API pour tous les films contenant "star wars" dans le titre. Cliquez à nouveau sur "envoyer", et cette fois vous verrez que la réponse est différente :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-10-at-08.01.02.png)

Remarquez comment nous recevons **un tableau d'éléments**. Chaque élément du tableau contient quelques détails sur un film (titre, année, etc.). Nous allons prendre l'image **Poster** de chaque objet et l'afficher dans notre application.

## Comment configurer un projet React 

D'accord, cela étant fait, nous pouvons passer aux bonnes choses – créer un projet React. Nous allons utiliser `create-react-app` pour nous lancer rapidement.

Lancez un terminal et tapez :

`npx create-react-app movie-app`

Lorsque cela a fini de faire son travail, nous allons ajouter Bootstrap pour nous aider à positionner les choses joliment sans avoir besoin de beaucoup de notre propre CSS. 

Exécutez les commandes suivantes :

```js
cd movie-app
npm install bootstrap
```

C'est tout ce dont nous avons besoin, alors allez-y et lancez l'application :

`npm start`

## Comment ajouter des films à l'état

Le composant **App** contiendra l'état de l'application. De cette façon, nous pouvons garder tout organisé en un seul endroit et passer différentes parties de l'état à différents composants.

Ouvrez `App.js`, supprimez tout et remplacez-le par ce qui suit :

```jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

const App = () => {
	const [movies, setMovies] = useState([        {
            "Title": "Star Wars: Episode IV - A New Hope",
            "Year": "1977",
            "imdbID": "tt0076759",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg"
        },
        {
            "Title": "Star Wars: Episode V - The Empire Strikes Back",
            "Year": "1980",
            "imdbID": "tt0080684",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg"
        },
        {
            "Title": "Star Wars: Episode VI - Return of the Jedi",
            "Year": "1983",
            "imdbID": "tt0086190",
            "Type": "movie",
            "Poster": "https://m.media-amazon.com/images/M/MV5BOWZlMjFiYzgtMTUzNC00Y2IzLTk1NTMtZmNhMTczNTk0ODk1XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg"
        }]);
	
	return (
		<div className='container-fluid movie-app'>
			<div className='row'>

			</div>
		</div>
	);
};

export default App;

```

* Nous créons un objet d'état pour contenir notre liste de films. Cela proviendra de l'API éventuellement, mais pour l'instant, nous allons simplement coder en dur quelques données – qui sont prises de la réponse dans Postman.
* Nous ajoutons le CSS de Bootstrap et ajoutons quelques balises de base

Si vous sauvegardez/exécutez l'application, vous verrez que même si nous avons configuré un état, nous ne rendons rien pour l'instant – donc l'écran sera vide.

## Comment créer un composant MovieList 

Ah, notre premier composant ! Nous allons créer un composant **MovieList** pour afficher la liste de films qui revient dans la requête de recherche.

Créez un nouveau dossier appelé **components** sous le dossier **src**. Créez un nouveau fichier dans le dossier components appelé **MovieList.js** :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-10-at-08.21.57.png)

Ouvrez MovieList.js et ajoutez ce qui suit :

```jsx
import React from 'react';

const MovieList = (props) => {
	return (
		<>
			{props.movies.map((movie, index) => (
				<div className='image-container d-flex justify-content-start m-3'>
					<img src={movie.Poster} alt='movie'></img>
				</div>
			))}
		</>
	);
};

export default MovieList;

```

* Nous allons passer une liste de films en tant que **props**
* Nous allons utiliser la fonction map pour **boucler** sur ces films
* Pour chaque film, nous allons afficher une **image** en utilisant l'URL Poster comme source de l'image

## Comment rendre notre MovieList 

Juste une étape de plus avant de voir les choses fonctionner dans le navigateur – êtes-vous excité ?!

Retournez dans **App.js** et mettez-le à jour avec ce qui suit :

```jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import MovieList from './components/MovieList';

const App = () => {
	const [movies, setMovies] = useState([
		{
			Title: 'Star Wars: Episode IV - A New Hope',
			Year: '1977',
			imdbID: 'tt0076759',
			Type: 'movie',
			Poster:
				'https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg',
		},
		{
			Title: 'Star Wars: Episode V - The Empire Strikes Back',
			Year: '1980',
			imdbID: 'tt0080684',
			Type: 'movie',
			Poster:
				'https://m.media-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg',
		},
		{
			Title: 'Star Wars: Episode VI - Return of the Jedi',
			Year: '1983',
			imdbID: 'tt0086190',
			Type: 'movie',
			Poster:
				'https://m.media-amazon.com/images/M/MV5BOWZlMjFiYzgtMTUzNC00Y2IzLTk1NTMtZmNhMTczNTk0ODk1XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg',
		},
	]);

	return (
		<div className='container-fluid movie-app'>
			<div className='row'>
				<MovieList movies={movies} />
			</div>
		</div>
	);
};

export default App;

```

* Nous importons le composant MovieList (ligne 4 dans votre IDE)
* Nous **rendons** le MovieList et passons les films que nous avons stockés dans l'état en tant que props (ligne 37 dans votre IDE)

Sauvegardez et exécutez l'application, puis si vous allez dans le navigateur, vous devriez voir ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-10-at-08.30.39.png)
_Ces films sont pris de notre objet d'état **movies** dans App.js_

Nous avons quelques affiches de films. Magnifique !

## Comment ajouter un appel à l'API 

Maintenant que nous savons que notre application est capable de rendre les films que nous recevons de l'API, nous pouvons ajouter une logique pour faire une requête afin d'obtenir des films et les rendre à l'écran. 

Mettez à jour **App.js** avec ce qui suit :

```jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import MovieList from './components/MovieList';

const App = () => {
	const [movies, setMovies] = useState([]);

	const getMovieRequest = async () => {
		const url = `http://www.omdbapi.com/?s=star wars&apikey=263d22d8`;

		const response = await fetch(url);
		const responseJson = await response.json();

		if (responseJson.Search) {
			setMovies(responseJson.Search);
		}
	};

	useEffect(() => {
		getMovieRequest();
	}, []);

	return (
		<div className='container-fluid movie-app'>
			<div className='row'>
				<MovieList movies={movies} />
			</div>
		</div>
	);
};

export default App;

```

* Nous supprimons les films codés en dur de notre valeur d'état de film (ligne 7 dans votre IDE)
* Nous avons ajouté une fonction qui appelle l'API. Cela utilise l'API Fetch (ligne 9 dans votre IDE)
* Nous codons en dur une valeur de recherche pour l'instant – plus tard nous ajouterons une entrée que l'utilisateur pourra taper une valeur de recherche (ligne 10 dans votre IDE)
* Si nous obtenons des films dans la recherche, nous allons les définir dans notre état de film
* Nous utilisons un **useEffect** pour nous assurer que l'appel API ne se produit que lorsque l'application se charge pour la première fois (ligne 20 dans votre IDE)

Puisque nous passons déjà la valeur d'état `movie` au `MovieList` en tant que props, cela fonctionne automatiquement sans que nous ayons à changer notre JSX. C'est bien !

## Comment ajouter un défilement horizontal

Pendant que nous y sommes, nous allons ajouter l'effet de défilement horizontal élégant et un fond sombre – style Netflix.

Allez dans `App.css` et supprimez tout ce qui s'y trouve. Ensuite, ajoutez ce qui suit :

```css
body {
	background: #141414;
	color: #ffffff;
}

.movie-app > .row {
	overflow-x: auto;
	flex-wrap: nowrap;
}

```

C'est tout ! Essayez de faire défiler horizontalement les films dans le navigateur.

## Comment ajouter un titre et une entrée de recherche 

Jusqu'à présent, nous avons utilisé des valeurs de recherche codées en dur, mais cela pourrait ne pas plaire aux non-fans de Star Wars.

Ensuite, nous allons ajouter un titre et une entrée de recherche qui permet à l'utilisateur de rechercher ce qu'il veut.

### Comment ajouter le titre

Ajoutez un nouveau composant au dossier **components** appelé **MovieListHeading.js.** Ouvrez-le et ajoutez ce qui suit :

```jsx
import React from 'react';

const MovieListHeading = (props) => {
	return (
		<div className='col'>
			<h1>{props.heading}</h1>
		</div>
	);
};

export default MovieListHeading;

```

* Cela accepte une **prop de titre** qui est rendue dans une colonne Bootstrap
* Cela nous permet de le réutiliser plus tard

### Comment ajouter l'entrée de recherche

Ajoutez un nouveau composant au dossier **components** appelé **SearchBox.js.** Ouvrez-le et ajoutez ce qui suit :

```react
import React from 'react';

const SearchBox = (props) => {
	return (
		<div className='col col-sm-4'>
			<input
				className='form-control'
				value={props.value}
				onChange={(event) => props.setSearchValue(event.target.value)}
				placeholder='Tapez pour rechercher...'
			></input>
		</div>
	);
};

export default SearchBox;

```

* Cela rend une entrée
* Prend une valeur de **props**, et lorsque l'utilisateur tape, appelle une fonction qui met à jour la valeur. Cela est également pris de props.

### Comment sauvegarder l'entrée de recherche dans l'état

Maintenant que nous avons de nouveaux composants, nous devons savoir ce que l'utilisateur a tapé afin de pouvoir l'envoyer à l'API. Mettez à jour **App.js** avec ce qui suit :

```jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import MovieList from './components/MovieList';
import MovieListHeading from './components/MovieListHeading';
import SearchBox from './components/SearchBox';

const App = () => {
	const [movies, setMovies] = useState([]);
	const [searchValue, setSearchValue] = useState('');

	const getMovieRequest = async () => {
		const url = `http://www.omdbapi.com/?s=star wars&apikey=263d22d8`;

		const response = await fetch(url);
		const responseJson = await response.json();

		if (responseJson.Search) {
			setMovies(responseJson.Search);
		}
	};

	useEffect(() => {
		getMovieRequest();
	}, []);

	return (
		<div className='container-fluid movie-app'>
			<div className='row d-flex align-items-center mt-4 mb-4'>
				<MovieListHeading heading='Movies' />
				<SearchBox searchValue={searchValue} setSearchValue={setSearchValue} />
			</div>
			<div className='row'>
				<MovieList movies={movies} />
			</div>
		</div>
	);
};

export default App;

```

* Nous ajoutons une nouvelle **valeur d'état** pour stocker ce que l'utilisateur tape (ligne 10 dans votre IDE)
* Nous importons nos composants (lignes 5/6 dans votre IDE)
* Nous ajoutons une nouvelle "ligne" qui contient nos composants **MovieListHeading** et **Searchbox** (ligne 29 dans votre IDE)
* Et nous passons la valeur **searchValue** et la fonction **setSearchValue** au composant **SearchBox** (ligne 31)

En sauvegardant l'état de l'entrée dans App.js, cela nous facilite le passage de la valeur de recherche à la fonction `getMovieRequest`.

### Comment appeler l'API lorsque la valeur de recherche change

Maintenant que nous savons ce que l'utilisateur a tapé, nous devons appeler l'API avec cette valeur. Mettez à jour App.js avec ce qui suit :

```jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import MovieList from './components/MovieList';
import MovieListHeading from './components/MovieListHeading';
import SearchBox from './components/SearchBox';

const App = () => {
	const [movies, setMovies] = useState([]);
	const [searchValue, setSearchValue] = useState('');

	const getMovieRequest = async (searchValue) => {
		const url = `http://www.omdbapi.com/?s=${searchValue}&apikey=263d22d8`;

		const response = await fetch(url);
		const responseJson = await response.json();

		if (responseJson.Search) {
			setMovies(responseJson.Search);
		}
	};

	useEffect(() => {
		getMovieRequest(searchValue);
	}, [searchValue]);

	return (
		<div className='container-fluid movie-app'>
			<div className='row d-flex align-items-center mt-4 mb-4'>
				<MovieListHeading heading='Movies' />
				<SearchBox searchValue={searchValue} setSearchValue={setSearchValue} />
			</div>
			<div className='row'>
				<MovieList movies={movies} />
			</div>
		</div>
	);
};

export default App;

```

* Nous mettons à jour notre fonction **getMovieRequest** pour accepter un paramètre : **searchValue** (ligne 12 dans votre IDE)
* Nous passons cette valeur à la requête en utilisant une chaîne de modèle (ligne 13 dans votre IDE)
* Nous mettons à jour le hook **useEffect** pour qu'il s'exécute chaque fois que **searchValue change** (ligne 25 dans votre IDE)
* Lorsque le hook useEffect s'exécute, il passe le nouveau **searchValue** à notre fonction **getMovieRequest** (ligne 24 dans votre IDE)
* Cela effectue un appel à l'API et met à jour l'état si nous obtenons des résultats comme d'habitude

Essayez cela dans le navigateur – et vous verrez les résultats se mettre à jour en temps réel.

## Comment ajouter des favoris

Pouvoir rechercher des films est bien et tout, mais comment sommes-nous censés nous souvenir de regarder tous ces films fantastiques ? En les ajoutant aux favoris, bien sûr !

Nous allons ajouter un bel effet de "zoom" qui montre un bouton "Ajouter aux favoris" lorsque l'utilisateur survole l'affiche, comme vous le voyez ci-dessous. 

Nous allons également ajouter une logique pour ajouter/afficher les films préférés que l'utilisateur sélectionne :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Nov-10-2020-15-47-40.gif)

### Comment ajouter le calque de superposition 

Nous allons commencer par ajouter le calque de superposition et l'effet de zoom. Allez dans **MovieList.js** et mettez-le à jour avec ce qui suit :

```jsx
import React from 'react';

const MovieList = (props) => {
	return (
		<>
			{props.movies.map((movie, index) => (
				<div className='image-container d-flex justify-content-start m-3'>
					<img src={movie.Poster} alt='movie'></img>
					<div className='overlay d-flex align-items-center justify-content-center'>
						Add to Favourites
					</div>
				</div>
			))}
		</>
	);
};

export default MovieList;

```

* Nous ajoutons une nouvelle classe à la div parente : **image-container.** Cela nous permettra d'ajouter l'effet de zoom (ligne 7 dans votre IDE)
* Nous ajoutons une nouvelle div qui sera le calque de superposition. Nous allons masquer cette div initialement et la montrer lorsque l'utilisateur survole (ligne 9 dans votre IDE)
* Nous ajoutons du texte (ligne 10 dans votre IDE)

Maintenant, si vous sauvegardez et exécutez cela, rien ne se passera. Nous devons ajouter du CSS pour que la magie opère. Allez dans **App.css et ajoutez ce qui suit au fichier :**

```

.image-container {
	position: relative;
	transition: transform 0.2s;
}

.image-container:hover {
	cursor: pointer;
	transform: scale(1.1);
}

.image-container:hover .overlay {
	opacity: 1;
}

.overlay {
	position: absolute;
	background: rgba(0, 0, 0, 0.8);
	width: 100%;
	transition: 0.5s ease;
	opacity: 0;
	bottom: 0;
	font-size: 20px;
	padding: 20px;
	text-align: center;
}

```

* Nous ajoutons un effet de transition au conteneur d'image pour le "mettre à l'échelle" lorsque l'utilisateur survole (nous donnant l'effet de zoom)
* Nous ajoutons un style au **calque de superposition** qui est masqué initialement
* Nous augmentons l'**opacité** (c'est-à-dire, nous montrons le calque de superposition) lorsque l'utilisateur survole

Si vous exécutez cela dans le navigateur, vous pouvez voir que l'image "zoome" et que le calque de superposition apparaît lorsque vous survolez. Bien joué !

### Comment créer le composant "Ajouter aux favoris"

Ensuite, nous allons créer un composant "Ajouter aux favoris" que nous passons à la MovieList, que nous allons ensuite rendre dans le calque de superposition. 

Créez un nouveau fichier dans le dossier **components** appelé **AddToFavourites.js.** Ajoutez ce qui suit :

```jsx
import React from 'react';

const AddFavourite = () => {
	return (
		<>
			<span className='mr-2'>Add to Favourites</span>
			<svg
				width='1em'
				height='1em'
				viewBox='0 0 16 16'
				class='bi bi-heart-fill'
				fill='red'
				xmlns='http://www.w3.org/2000/svg'
			>
				<path
					fill-rule='evenodd'
					d='M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z'
				/>
			</svg>
		</>
	);
};

export default AddFavourite;

```

Cela retournera le texte "Ajouter aux favoris" et une icône "Cœur" (prise de www.icons.getbootstrap.com).

Ensuite, nous allons importer ce composant dans **App.js** et le passer à notre **composant MovieList**. Mettez à jour App.js avec ce qui suit :

```jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import MovieList from './components/MovieList';
import MovieListHeading from './components/MovieListHeading';
import SearchBox from './components/SearchBox';
import AddFavourites from './components/AddFavourites';

const App = () => {
	const [movies, setMovies] = useState([]);
	const [searchValue, setSearchValue] = useState('');

	const getMovieRequest = async (searchValue) => {
		const url = `http://www.omdbapi.com/?s=${searchValue}&apikey=263d22d8`;

		const response = await fetch(url);
		const responseJson = await response.json();

		if (responseJson.Search) {
			setMovies(responseJson.Search);
		}
	};

	useEffect(() => {
		getMovieRequest(searchValue);
	}, [searchValue]);

	return (
		<div className='container-fluid movie-app'>
			<div className='row d-flex align-items-center mt-4 mb-4'>
				<MovieListHeading heading='Movies' />
				<SearchBox searchValue={searchValue} setSearchValue={setSearchValue} />
			</div>
			<div className='row'>
				<MovieList movies={movies} favouriteComponent={AddFavourites} />
			</div>
		</div>
	);
};

export default App;

```

* Nous importons notre nouveau composant **AddFavourites** (ligne 7 dans votre IDE)
* Nous le passons en tant que **prop** (favouriteComponent) à notre composant **MovieList** (ligne 35)

Maintenant que notre composant MovieList accepte ce composant en tant que prop, nous pouvons le rendre dans notre calque de superposition

N'oubliez pas que les composants React sont simplement des fonctions - donc nous pouvons les passer comme nous le faisons pour les fonctions normales !

Ouvrez **MovieList.js** et mettez-le à jour avec ce qui suit :

```jsx
import React from 'react';

const MovieList = (props) => {
	const FavouriteComponent = props.favouriteComponent;
	return (
		<>
			{props.movies.map((movie, index) => (
				<div className='image-container d-flex justify-content-start m-3'>
					<img src={movie.Poster} alt='movie'></img>
					<div className='overlay d-flex align-items-center justify-content-center'>
						<FavouriteComponent />
					</div>
				</div>
			))}
		</>
	);
};

export default MovieList;

```

* Nous prenons notre **favouriteComponent** des props et l'assignons à une variable. Cela nous permet de l'utiliser comme un composant react (ligne 4 dans votre IDE)
* Nous rendons notre **favouriteComponent** dans le calque de superposition (ligne 15 dans votre IDE)

Cette approche nous permet de personnaliser ce qui est rendu dans le calque de superposition. Nous pouvons passer n'importe quel composant react et le composant MovieList le rendra. Cela rend notre composant MovieList réutilisable.

### Comment sauvegarder les favoris dans l'état

Nous avons donc notre composant de favoris en place, et bien qu'il ait l'air bien, il ne fait encore rien. 

Lorsque l'utilisateur clique sur le composant "Ajouter aux favoris", nous voulons prendre le film sur lequel il a cliqué et le sauvegarder dans un nouvel objet d'état appelé **favoris**. Nous allons ensuite rendre cette liste dans l'interface utilisateur.

Ouvrez **App.js** et mettez-le à jour avec ce qui suit :

```jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import MovieList from './components/MovieList';
import MovieListHeading from './components/MovieListHeading';
import SearchBox from './components/SearchBox';
import AddFavourites from './components/AddFavourites';

const App = () => {
	const [movies, setMovies] = useState([]);
	const [searchValue, setSearchValue] = useState('');
	const [favourites, setFavourites] = useState([]);

	const getMovieRequest = async (searchValue) => {
		const url = `http://www.omdbapi.com/?s=${searchValue}&apikey=263d22d8`;

		const response = await fetch(url);
		const responseJson = await response.json();

		if (responseJson.Search) {
			setMovies(responseJson.Search);
		}
	};

	const addFavouriteMovie = (movie) => {
		const newFavouriteList = [...favourites, movie];
		setFavourites(newFavouriteList);
	};

	useEffect(() => {
		getMovieRequest(searchValue);
	}, [searchValue]);

	return (
		<div className='container-fluid movie-app'>
			<div className='row d-flex align-items-center mt-4 mb-4'>
				<MovieListHeading heading='Movies' />
				<SearchBox searchValue={searchValue} setSearchValue={setSearchValue} />
			</div>
			<div className='row'>
				<MovieList
					movies={movies}
					favouriteComponent={AddFavourites}
					handleFavouritesClick={addFavouriteMovie}
				/>
			</div>
		</div>
	);
};

export default App;

```

* Nous ajoutons un nouvel objet d'état pour contenir nos favoris. Nous allons ajouter le film sur lequel l'utilisateur a cliqué à ce tableau (ligne 12 dans votre IDE)
* Nous créons une fonction appelée **addFavouriteMovie**, qui accepte un **movie**. Cela prend le tableau actuel des favoris, le copie, ajoute le nouveau film à celui-ci, et sauvegarde tout dans l'état (ligne 25 dans votre IDE)
* Nous passons cette fonction en tant que **prop (handleFavouritesClick)** à notre composant **MovieList** (ligne 44 dans votre IDE)

Maintenant que nous avons notre objet d'état, et un moyen de mettre à jour cet objet d'état, nous devons appeler cela depuis notre **favouritesComponent** dans **MovieList**.

Ouvrez **MovieList.js** et mettez-le à jour avec ce qui suit :

```jsx
import React from 'react';

const MovieList = (props) => {
	const FavouriteComponent = props.favouriteComponent;

	return (
		<>
			{props.movies.map((movie, index) => (
				<div className='image-container d-flex justify-content-start m-3'>
					<img src={movie.Poster} alt='movie'></img>
					<div
						onClick={() => props.handleFavouritesClick(movie)}
						className='overlay d-flex align-items-center justify-content-center'
					>
						<FavouriteComponent />
					</div>
				</div>
			))}
		</>
	);
};

export default MovieList;

```

* Tout ce que nous faisons ici, c'est prendre la fonction **handleFavouritesClick** des props et l'ajouter à une propriété **onClick** dans le calque de superposition
* Nous passons le film actuel sur lequel la fonction map est en train de travailler à la fonction handleFavouritesClick

Maintenant, si vous exécutez l'application, cliquez sur "Ajouter aux favoris" pour n'importe quel film, et ouvrez les outils de développement React (dans Chrome), vous verrez qu'il se met à jour dans l'état. 

Malheureusement, les hooks ne sont pas nommés de la même manière que ce que nous les avons appelés, mais nous pouvons deviner lequel c'est :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-11-at-05.38.48.png)

### Comment rendre les films favoris

Les choses ont l'air bien jusqu'à présent. Nous avons la capacité de sauvegarder des choses dans les favoris, mais nous ne les avons pas encore affichés.

Nous allons réutiliser le **composant MovieList** pour afficher nos favoris. C'est bien !

Ouvrez **App.js** et mettez-le à jour avec ce qui suit : 

```jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import MovieList from './components/MovieList';
import MovieListHeading from './components/MovieListHeading';
import SearchBox from './components/SearchBox';
import AddFavourites from './components/AddFavourites';

const App = () => {
	const [movies, setMovies] = useState([]);
	const [searchValue, setSearchValue] = useState('');
	const [favourites, setFavourites] = useState([]);

	const getMovieRequest = async (searchValue) => {
		const url = `http://www.omdbapi.com/?s=${searchValue}&apikey=263d22d8`;

		const response = await fetch(url);
		const responseJson = await response.json();

		if (responseJson.Search) {
			setMovies(responseJson.Search);
		}
	};

	const addFavouriteMovie = (movie) => {
		const newFavouriteList = [...favourites, movie];
		setFavourites(newFavouriteList);
	};

	useEffect(() => {
		getMovieRequest(searchValue);
	}, [searchValue]);

	return (
		<div className='container-fluid movie-app'>
			<div className='row d-flex align-items-center mt-4 mb-4'>
				<MovieListHeading heading='Movies' />
				<SearchBox searchValue={searchValue} setSearchValue={setSearchValue} />
			</div>
			<div className='row'>
				<MovieList
					movies={movies}
					favouriteComponent={AddFavourites}
					handleFavouritesClick={addFavouriteMovie}
				/>
			</div>
			<div className='row d-flex align-items-center mt-4 mb-4'>
				<MovieListHeading heading='Favourites' />
			</div>
			<div className='row'>
				<MovieList movies={favourites} favouriteComponent={AddFavourites} />
			</div>
		</div>
	);
};

export default App;

```

* Nous ajoutons une nouvelle **ligne** et à l'intérieur, nous ajoutons un nouveau titre en utilisant le composant **MovieListHeading** (ligne 47 dans votre IDE)
* Nous ajoutons une nouvelle ligne en dessous, et rendons nos **favoris** en utilisant le composant **MovieList** (ligne 51)

C'est un exemple de la façon de créer un composant réutilisable. Si un composant utilise une logique similaire mais affiche différentes données pour différentes situations, vous pouvez probablement le réutiliser.

Lancez cela dans le navigateur et tout devrait fonctionner :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Nov-11-2020-05-49-25.gif)



## Comment supprimer des favoris

Ensuite, nous voulons ajouter la possibilité de supprimer des films des favoris. Nous allons adopter une approche similaire à celle que nous avons utilisée pour ajouter des favoris :

* Créer un **composant de suppression** que nous passons à notre **MovieList**, qui est rendu dans le calque de superposition
* Créer une fonction appelée **clicked** pour supprimer le film cliqué de l'état.
* Passer une fonction pour gérer l'événement **onClick** lorsque l'utilisateur clique sur le composant de suppression

### Comment créer le composant RemoveFavourites

Créez un nouveau fichier dans le dossier components appelé **RemoveFavourites.js** et ajoutez ce qui suit :

```jsx
import React from 'react';

const RemoveFavourites = () => {
	return (
		<>
			<span className='mr-2'>Remove from favourites</span>
			<svg
				width='1em'
				height='1em'
				viewBox='0 0 16 16'
				class='bi bi-x-square'
				fill='currentColor'
				xmlns='http://www.w3.org/2000/svg'
			>
				<path
					fill-rule='evenodd'
					d='M14 1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z'
				/>
				<path
					fill-rule='evenodd'
					d='M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z'
				/>
			</svg>
		</>
	);
};

export default RemoveFavourites;

```

* Nous ajoutons le texte "remove from favourites" (ligne 6 dans votre IDE)
* Nous ajoutons une icône "remove" que nous obtenons de icons.getbootstrap.com (ligne 7 dans votre IDE)

### Comment supprimer les favoris de l'état

Similaire à ce que nous avons fait avant, nous devons écrire une fonction qui **supprime** un film sélectionné de notre **état des favoris.**

Ouvrez **App.js** et mettez-le à jour avec ce qui suit :

```jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import MovieList from './components/MovieList';
import MovieListHeading from './components/MovieListHeading';
import SearchBox from './components/SearchBox';
import AddFavourites from './components/AddFavourites';
import RemoveFavourites from './components/RemoveFavourites';

const App = () => {
	const [movies, setMovies] = useState([]);
	const [searchValue, setSearchValue] = useState('');
	const [favourites, setFavourites] = useState([]);

	const getMovieRequest = async (searchValue) => {
		const url = `http://www.omdbapi.com/?s=${searchValue}&apikey=263d22d8`;

		const response = await fetch(url);
		const responseJson = await response.json();

		if (responseJson.Search) {
			setMovies(responseJson.Search);
		}
	};

	const addFavouriteMovie = (movie) => {
		const newFavouriteList = [...favourites, movie];
		setFavourites(newFavouriteList);
	};

	const removeFavouriteMovie = (movie) => {
		const newFavouriteList = favourites.filter(
			(favourite) => favourite.imdbID !== movie.imdbID
		);

		setFavourites(newFavouriteList);
	};

	useEffect(() => {
		getMovieRequest(searchValue);
	}, [searchValue]);

	return (
		<div className='container-fluid movie-app'>
			<div className='row d-flex align-items-center mt-4 mb-4'>
				<MovieListHeading heading='Movies' />
				<SearchBox searchValue={searchValue} setSearchValue={setSearchValue} />
			</div>
			<div className='row'>
				<MovieList
					movies={movies}
					favouriteComponent={AddFavourites}
					handleFavouritesClick={addFavouriteMovie}
				/>
			</div>
			<div className='row d-flex align-items-center mt-4 mb-4'>
				<MovieListHeading heading='Favourites' />
			</div>
			<div className='row'>
				<MovieList
					movies={favourites}
					handleFavouritesClick={removeFavouriteMovie}
					favouriteComponent={RemoveFavourites}
				/>
			</div>
		</div>
	);
};

export default App;

```

* Nous importons notre composant **RemoveFavourites** (ligne 8 dans votre IDE)
* Nous créons une fonction appelée **removeFavouriteMovie** pour supprimer un film donné de notre état des favoris (ligne 31 dans votre IDE)
* Pour supprimer, nous utilisons la fonction filter. Cela retourne une nouvelle version du tableau **favoris** qui n'inclut pas le film que nous souhaitons supprimer
* Nous passons notre composant **RemoveFavourites** et notre fonction **removeFavouriteMovie** à notre composant **MovieList** (ligne 60 dans votre IDE)

Parce que nous avons déjà codé notre composant MovieList pour accepter un composant à rendre et une fonction à appeler, tout fonctionne simplement !

Maintenant, si vous exécutez cela dans votre navigateur, vous devriez pouvoir supprimer des favoris :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Nov-11-2020-06-09-31.gif)



## Comment sauvegarder ou supprimer des films du stockage local

La dernière chose que nous allons faire est de sauvegarder dans le stockage local. Cela nous permet de conserver nos films préférés lorsque la page se recharge ou si nous ouvrons l'application dans une fenêtre différente.

Nous allons sauvegarder nos favoris dans le **stockage local** lorsque quelque chose change, et nous allons récupérer nos **favoris** du stockage local lorsque l'application se charge, en les sauvegardant dans notre **état des favoris**.

Ouvrez **App.js** pour la dernière fois et mettez-le à jour avec ce qui suit :

```jsx
import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import MovieList from './components/MovieList';
import MovieListHeading from './components/MovieListHeading';
import SearchBox from './components/SearchBox';
import AddFavourites from './components/AddFavourites';
import RemoveFavourites from './components/RemoveFavourites';

const App = () => {
	const [movies, setMovies] = useState([]);
	const [favourites, setFavourites] = useState([]);
	const [searchValue, setSearchValue] = useState('');

	const getMovieRequest = async (searchValue) => {
		const url = `http://www.omdbapi.com/?s=${searchValue}&apikey=263d22d8`;

		const response = await fetch(url);
		const responseJson = await response.json();

		if (responseJson.Search) {
			setMovies(responseJson.Search);
		}
	};

	useEffect(() => {
		getMovieRequest(searchValue);
	}, [searchValue]);

	useEffect(() => {
		const movieFavourites = JSON.parse(
			localStorage.getItem('react-movie-app-favourites')
		);

		setFavourites(movieFavourites);
	}, []);

	const saveToLocalStorage = (items) => {
		localStorage.setItem('react-movie-app-favourites', JSON.stringify(items));
	};

	const addFavouriteMovie = (movie) => {
		const newFavouriteList = [...favourites, movie];
		setFavourites(newFavouriteList);
		saveToLocalStorage(newFavouriteList);
	};

	const removeFavouriteMovie = (movie) => {
		const newFavouriteList = favourites.filter(
			(favourite) => favourite.imdbID !== movie.imdbID
		);

		setFavourites(newFavouriteList);
		saveToLocalStorage(newFavouriteList);
	};

	return (
		<div className='container-fluid movie-app'>
			<div className='row d-flex align-items-center mt-4 mb-4'>
				<MovieListHeading heading='Movies' />
				<SearchBox searchValue={searchValue} setSearchValue={setSearchValue} />
			</div>
			<div className='row'>
				<MovieList
					movies={movies}
					handleFavouritesClick={addFavouriteMovie}
					favouriteComponent={AddFavourites}
				/>
			</div>
			<div className='row d-flex align-items-center mt-4 mb-4'>
				<MovieListHeading heading='Favourites' />
			</div>
			<div className='row'>
				<MovieList
					movies={favourites}
					handleFavouritesClick={removeFavouriteMovie}
					favouriteComponent={RemoveFavourites}
				/>
			</div>
		</div>
	);
};

export default App;

```

* Nous ajoutons une fonction appelée **saveToLocalStorage.** Cette fonction prend une liste d'éléments et les sauvegarde dans le stockage local contre une **clé.** Dans ce cas, la clé est **react-movie-app-favourites.** (ligne 38 dans votre IDE)
* Nous sauvegardons dans le stockage local lorsque nous **ajoutons un film favori** (ligne 45 dans votre IDE)
* Nous sauvegardons dans le stockage local lorsque nous **supprimons un film favori** (ligne 54 dans votre IDE)
* Nous utilisons le hook **useEffect** pour récupérer les favoris du stockage local lorsque l'application se charge, et nous définissons cela dans l'état (ligne 30 dans votre IDE)

Lancez cela dans votre navigateur et vous devriez pouvoir sauvegarder des films préférés - même si vous fermez le navigateur !

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Nov-11-2020-06-21-58.gif)



## La Fin - Et ensuite ?

Merci d'avoir lu, et plus important encore - félicitations pour être arrivé à la fin ! 

Si vous avez aimé cet article, assurez-vous de consulter [reactbeginnerprojects.com](https://www.freecodecamp.org/news/p/e8fd6f73-03c1-48b3-8988-b3a47691577b/reactbeginnerprojects.com). Vous y trouverez un tas de projets gratuits que vous pouvez essayer pour apprendre les compétences clés dont vous aurez besoin pour décrocher un emploi en tant que développeur React et booster votre portfolio.