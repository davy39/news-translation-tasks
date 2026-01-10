---
title: 'Comment intégrer RTK Query avec Redux Toolkit : Un guide étape par étape pour
  les développeurs React'
subtitle: ''
author: Chidera Humphrey
co_authors: []
series: null
date: '2025-02-06T18:13:23.300Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-rtk-query-with-redux-toolkit
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738854615563/3357bd11-3fcd-43b3-b459-b0e8b60e853d.png
tags:
- name: React
  slug: reactjs
- name: redux-toolkit
  slug: redux-toolkit
seo_title: 'Comment intégrer RTK Query avec Redux Toolkit : Un guide étape par étape
  pour les développeurs React'
seo_desc: Redux is a state management library for JavaScript applications. It lets
  you create applications that behave in a predictable manner and run on different
  environments, including server and native environments. Redux Toolkit is the recommended
  way to ...
---

Redux est une bibliothèque de gestion d'état pour les applications JavaScript. Elle vous permet de créer des applications qui se comportent de manière prévisible et s'exécutent dans différents environnements, y compris les environnements serveur et natifs. Redux Toolkit est la manière recommandée d'écrire la logique Redux et a été créé pour faciliter le travail avec Redux.

Traditionnellement, l'écriture de la logique Redux nécessitait beaucoup de code boilerplate, de configuration et d'installations de dépendances. Cela rendait Redux difficile à utiliser. RTK a été créé pour résoudre ces problèmes. RTK contient des utilitaires qui simplifient les tâches Redux courantes telles que la configuration du store, la création de reducers et la logique de mise à jour de l'état immutable.

Redux Toolkit Query (RTK Query) est un module complémentaire optionnel inclus dans le package Redux ToolKit. Il a été créé pour simplifier la récupération et la mise en cache des données dans les applications web. RTK Query est construit sur Redux Toolkit et utilise Redux pour sa conception architecturale interne.

Dans cet article, vous apprendrez comment intégrer RTK Query avec Redux Toolkit dans vos applications React en construisant une simple application CRUD de films.

## Table des matières

1. [Prérequis](#heading-prerequisites)
    
2. [Comprendre RTK Query et les concepts de base](#heading-understanding-rtk-query-and-core-concepts)
    
3. [Intégration de RTK Query avec Redux Toolkit](#heading-integrating-rtk-query-with-redux-toolkit)
    
4. [Gestion de la mise en cache des données avec RTK Query](#heading-handling-data-caching-with-rtk-query)
    
5. [Gestion des erreurs et états de chargement](#heading-error-handling-and-loading-states)
    
6. [Bonnes pratiques](#heading-best-practices)
    
7. [Conclusion](#heading-conclusion)
    

## Prérequis

Pour cet article, je suppose que vous êtes familier avec React.

## Comprendre RTK Query et les concepts de base

Au cœur de RTK Query se trouve la fonction `createApi`. Cette fonction vous permet de définir une tranche d'API, qui inclut l'URL de base du serveur et un ensemble de points de terminaison qui décrivent comment récupérer et mutuer les données du serveur.

RTK Query génère automatiquement un hook personnalisé pour chacun des points de terminaison définis. Ces hooks personnalisés peuvent être utilisés dans votre composant React pour rendre conditionnellement le contenu en fonction de l'état de la requête API.

Le code ci-dessous montre comment créer une tranche d'API en utilisant la fonction `createApi` :

```js
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const apiSlice = createApi({
    reducerPath: 'api',
    baseQuery: fetchBaseQuery({ baseUrl: 'https://server.co/api/v1/'}),
    endpoints: (builder) => ({
        getData: builder.query({
            query: () => '/data',
        })
    })
})

export const { useGetDataQuery } = apiSlice;
```

`fetchBaseQuery` est un wrapper léger autour de la fonction native JavaScript `fetch` qui simplifie les requêtes API. La propriété `reducerPath` spécifie le répertoire où votre tranche d'API est stockée. Une convention courante est de nommer le répertoire `api`. La propriété `baseQuery` utilise la fonction `fetchBaseQuery` pour spécifier l'URL de base de votre serveur. Vous pouvez la considérer comme l'URL racine à laquelle vos points de terminaison sont ajoutés.

`useGetDataQuery` est un hook généré automatiquement que vous pouvez utiliser dans vos composants.

## Comment intégrer RTK Query avec Redux Toolkit

Dans cette section, vous apprendrez comment intégrer RTK Query avec Redux Toolkit en construisant une simple application de films. Dans cette application, les utilisateurs pourront voir les films stockés dans votre backend (bien que ce soit un backend simulé), ajouter des films, et mettre à jour et supprimer n'importe quel film. En essence, vous allez construire une application CRUD en utilisant RTK Query.

De plus, j'utiliserai TypeScript pour ce tutoriel. Si vous utilisez JavaScript, ignorez les annotations de type et/ou les `interface`s et remplacez `.tsx`/`.ts` par `.jsx`/`.js`.

### **Configuration de l'environnement de développement**

Créez un nouveau projet React en utilisant la commande suivante :

```sh
npm create vite@latest
```

Suivez les invites pour créer votre application React.

Installez les packages `react-redux` et `@reduxjs/toolkit` en utilisant la commande suivante :

```sh
# npm
npm install @reduxjs/toolkit react-redux

# yarn
yarn add @reduxjs/toolkit react-redux
```

Pour le backend, vous allez utiliser `json-server`. `json-server` est un outil léger Node.js qui simule une API RESTful en utilisant des fichiers JSON comme source de données. Il permet aux développeurs frontend de créer des API simulées sans écrire de code côté serveur.

Vous pouvez en savoir plus sur `json-server` [ici](https://github.com/typicode/json-server/tree/v0).

Utilisez la commande suivante pour installer `json-server` :

```sh
npm install -g json-server
```

### **Structure des dossiers**

Dans le répertoire racine de votre application, créez un dossier **data**. À l'intérieur de ce dossier, créez un fichier `db.json`. Ce sera là où votre "backend" sera stocké.

Dans le dossier `src`, créez deux dossiers : **component** et **state**.

À l'intérieur du dossier `component`, créez deux dossiers : **CardComponent** et **Modal**, et un fichier : `Movies.tsx`.

À l'intérieur du dossier state, créez un dossier **movies** et un fichier : `store.ts`.

Après avoir créé les dossiers et les fichiers, la structure de votre application devrait ressembler à ceci :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734786998116/7708adad-06b1-41bd-ab22-d6efb745246b.png align="center")

### **Construction de l'application**

Tout d'abord, vous allez configurer votre **JSON server**.

Ouvrez le fichier `db.json` et collez le code suivant :

```json
{
  "movies": [
    {
      "title": "John Wick",
      "description": "L'ancien assassin John Wick est ramené dans le monde criminel lorsque des gangsters tuent son chien bien-aimé, un cadeau de sa défunte femme. Avec ses compétences de combat inégalées et une soif de vengeance, Wick affronte seul un syndicat criminel entier.",
      "year": 2014,
      "thumbnail": "https://m.media-amazon.com/images/M/MV5BNTBmNWFjMWUtYWI5Ni00NGI2LWFjN2YtNDE2ODM1NTc5NGJlXkEyXkFqcGc@._V1_.jpg",
      "id": "2"
    },
    {
      "id": "3",
      "title": "The Dark Knight",
      "year": 2008,
      "description": "Batman affronte son ennemi juré, le Joker, un criminel de génie qui plonge Gotham City dans le chaos. Alors que le Joker teste les limites de Batman, le héros doit affronter ses propres dilemmes éthiques pour sauver la ville de la destruction.",
      "thumbnail": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_FMjpg_UX1000_.jpg"
    },
    {
      "title": "Die Hard",
      "description": "L'officier du NYPD John McClane se retrouve dans une situation d'otage mortelle lorsqu'un groupe de terroristes prend le contrôle d'un gratte-ciel de Los Angeles lors d'une fête de Noël. Armé seulement de son esprit et d'un pistolet, McClane doit surpasser les intrus lourdement armés pour sauver sa femme et les autres.",
      "year": 1988,
      "thumbnail": "https://m.media-amazon.com/images/M/MV5BMGNlYmM1NmQtYWExMS00NmRjLTg5ZmEtMmYyYzJkMzljYWMxXkEyXkFqcGc@._V1_.jpg",
      "id": "4"
    },
    {
      "title": "Mission: Impossible – Fallout",
      "description": "Ethan Hunt et son équipe de la IMF doivent traquer du plutonium volé tout en étant traqués par des assassins et d'anciens alliés. Avec des cascades incroyables et des séquences d'action non-stop, Hunt court contre la montre pour empêcher une catastrophe mondiale.",
      "year": 2018,
      "thumbnail": "https://m.media-amazon.com/images/M/MV5BMTk3NDY5MTU0NV5BMl5BanBnXkFtZTgwNDI3MDE1NTM@._V1_.jpg",
      "id": "5"
    },
    {
      "title": "Gladiator",
      "description": "Trahi par le fils de l'Empereur et laissé pour mort, l'ancien général romain Maximus se lève en tant que gladiateur pour chercher vengeance et restaurer l'honneur de sa famille. Son voyage de l'esclavage à devenir un champion capture les cœurs des citoyens de Rome.",
      "year": 2010,
      "thumbnail": "https://m.media-amazon.com/images/M/MV5BZmExODVmMjItNzFlZC00MDA0LWJkYjctMmQ0ZTNkYTcwYTMyXkEyXkFqcGc@._V1_.jpg",
      "id": "6"
    }
  ]
}
```

Démarrez votre JSON server en utilisant la commande suivante :

```sh
json-server --watch data\db.json --port 8080
```

Cette commande démarrera votre JSON server et enveloppera le point de terminaison de l'API s'exécutant sur le port 8080. Votre terminal devrait ressembler à ceci :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734787039082/8331fca3-74ac-45aa-9fac-904af53cc961.png align="center")

Ensuite, vous allez créer une tranche d'API. Cette tranche d'API sera utilisée pour configurer votre store Redux.

Accédez au dossier **movies** et créez un fichier `movieApiSlice.ts`. Ouvrez le fichier `movieApiSlice.ts` et collez le code suivant :

```ts
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const moviesApiSlice = createApi({
  reducerPath: "movies",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://localhost:8080",
  }),
  endpoints: (builder) => {
    return {
      getMovies: builder.query({
        query: () => `/movies`,
      }),
      
      addMovie: builder.mutation({
        query: (movie) => ({
          url: "/movies",
          method: "POST",
          body: movie,
        }),
      }),

      updateMovie: builder.mutation({
        query: (movie) => {
          const { id, ...body } = movie;
          return {
            url: `movies/${id}`,
            method: "PUT",
            body
          }
        },
      }),

      deleteMovie: builder.mutation({
        query: ({id}) => ({
          url: `/movies/${id}`,
          method: "DELETE",
          body: id,
        }),
      }),
    };
  },
});

export const {
  useGetMoviesQuery,
  useAddMovieMutation,
  useDeleteMovieMutation,
  useUpdateMovieMutation,
} = moviesApiSlice;
```

Dans le code ci-dessus, vous avez créé une `movieApiSlice` en utilisant la fonction `createApi` de RTK Query, qui prend un objet comme paramètre.

La propriété `reducerPath` spécifie le chemin de la tranche d'API.

La `baseQuery` utilise `fetchBaseQuery`. La fonction `fetchBaseQuery` prend un objet comme paramètre, qui a une propriété `baseURL`. La propriété `baseURL` spécifie l'URL racine de notre API.

Dans ce cas, vous utilisez [`http://localhost:8080`](http://localhost:8080), qui est l'URL du JSON server.

La propriété `endpoints` est ce avec quoi votre API interagit. C'est une fonction qui prend un paramètre `builder` et retourne un objet avec des méthodes (`getMovies`, `addMovie`, `updateMovie`, et `deleteMovie`) pour interagir avec votre API.

Enfin, vous exportez des hooks personnalisés générés automatiquement par RTK Query. Le hook personnalisé commence par "use" et se termine par "query" et est nommé en fonction des méthodes définies dans la propriété `endpoints`.

Ces hooks personnalisés vous permettent d'interagir avec l'API depuis vos composants fonctionnels.

Ensuite, vous allez configurer votre store Redux. Accédez au fichier `store.ts` situé dans le dossier state et collez le code suivant :

```ts
import { configureStore } from "@reduxjs/toolkit";
import { moviesApiSlice } from "./movies/moviesApiSlice";

export const store = configureStore({
    reducer: {
        [moviesApiSlice.reducerPath]: moviesApiSlice.reducer,
    },
    middleware: (getDefaultMiddleware) => {
        return getDefaultMiddleware().concat(moviesApiSlice.middleware);
    }
})
```

Dans le code ci-dessus, vous configurez un store Redux en utilisant la fonction `configureStore` de Redux Toolkit. La propriété `reducer` spécifie un reducer pour mettre à jour l'état dans le store Redux. Le `moviesApiSlice.reducer` est le reducer pour mettre à jour l'état de votre API.

Pour la propriété `middleware`, vous créez un middleware pour gérer les mises à jour d'état asynchrones. Vous n'avez pas à vous soucier trop de cette partie et de ce qu'elle fait. Cela est requis pour toutes les fonctionnalités de mise en cache et tous les autres avantages que RTK Query fournit.

Avant d'aller plus loin, vous devez ajouter votre store Redux à votre application. Pour ce faire, accédez à votre fichier `main.tsx` ou `index.tsx` (selon ce qu'il est appelé dans votre application) et remplacez le code par le code suivant :

```tsx
// main.tsx

import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import { Provider } from "react-redux";
import { store } from "./state/store.ts";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </StrictMode>
);
```

Dans le code ci-dessus, vous importez le composant `Provider` de `react-redux` et le `store` que vous avez créé précédemment. De plus, vous enveloppez le composant `Provider` autour de votre composant `App`. La prop `store` est utilisée pour passer votre store Redux à votre application.

### **Construction du composant Movie**

Dans cette section, vous allez construire le composant `Movies.tsx`, qui est là où toute la logique de votre application réside.

Accédez à votre fichier `Movies.tsx` et collez le code suivant :

```tsx
import "../movie.css";
import { ChangeEvent, FormEvent, useState } from "react";

import {
  useGetMoviesQuery,
  useAddMovieMutation,
  useDeleteMovieMutation,
} from "../state/movies/moviesApiSlice";
import MovieCard from "./CardComponent/MovieCard";

export interface Movie {
  title: string;
  description: string;
  year: number;
  thumbnail: string;
  id: string;
}


export default function Movies() {
  // États des entrées du formulaire
  const [title, setTitle] = useState<string>("");
  const [year, setYear] = useState<string>("");
  const [thumbnail, setThumbnail] = useState<string>("");
  const [description, setDescription] = useState<string>("");

  const { data: movies = [], isLoading, isError } = useGetMoviesQuery({});

  const [ addMovie ] = useAddMovieMutation();
  const [ deleteMovie ] = useDeleteMovieMutation();

  // Gérer la soumission du formulaire pour ajouter un nouveau film
  const handleSubmit = (e: FormEvent<HTMLFormElement>): void => {
    e.preventDefault();
    console.log("Nouveau film soumis :", { title, thumbnail, description, year });
    addMovie({ title, description, year: Number(year), thumbnail, id: String(movies.length + 1) })
    // Réinitialiser les entrées du formulaire après la soumission
    setTitle("");
    setThumbnail("");
    setDescription("");
    setYear("");
  };

  if (isError) {
    return <div>Erreur</div>;
  }

  if (isLoading) {
    return <div>Chargement...</div>;
  }

  return (
    <div className="movie-container">
      <h2>Films à regarder</h2>

      {/* Formulaire pour ajouter un nouveau film */}
      <div className="new-movie-form">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="title">Titre</label>
            <input
              type="text"
              name="title"
              id="title"
              placeholder="Entrez le titre du film"
              value={title}
              onChange={(e: ChangeEvent<HTMLInputElement>) => setTitle(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="imageAddress">Lien de l'image :</label>
            <input
              type="text"
              name="imageAddress"
              id="imageAddress"
              placeholder="Entrez le lien de l'image"
              value={thumbnail}
              onChange={(e: ChangeEvent<HTMLInputElement>) => setThumbnail(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="year">Année de sortie :</label>
            <input
              type="text"
              name="year"
              id="year"
              placeholder="Entrez l'année de sortie"
              value={year}
              onChange={(e: ChangeEvent<HTMLInputElement>) => setYear(e.target.value)}
            />
          </div>

          <div className="form-group">
            <label htmlFor="description">Description</label>
            <textarea
              name="description"
              id="description"
              placeholder="Entrez la description du film"
              value={description}
              onChange={(e: ChangeEvent<HTMLTextAreaElement>) => setDescription(e.target.value)}
              required
            ></textarea>
          </div>

          <button type="submit">Ajouter un film</button>
        </form>
      </div>

      {/* Afficher la liste des films */}
      <div className="movie-list">
        {movies.length === 0 ? (
          <p>Aucun film ajouté pour l'instant.</p>
        ) : (
          movies.map((movie: Movie) => (
            <div key={movie.id}>
              <MovieCard movie={movie} deleteMovie={deleteMovie} />
            </div>
          ))
        )}
      </div>
    </div>
  );
}
```

Dans le code ci-dessus, vous créez un composant `Movies` et utilisez RTK Query pour gérer les opérations CRUD.

Passons en revue ce que chaque partie du code fait.

Dans la partie supérieure, vous avez importé les fonctions `useGetMoviesQuery`, `useAddMovieMutation` et `useDeleteMovie` depuis le `moviesApiSlice` que vous avez créé précédemment. Les fonctions seront utilisées pour récupérer, ajouter et supprimer des films, respectivement.

Vous avez également importé un composant `MovieCard`, que vous utiliserez pour afficher chaque film. Vous allez créer le composant `MovieCard` dans un instant.

L'interface `Movie` définit la forme de chaque objet film. Elle assure la cohérence de la structure des données de film dans le composant. Encore une fois, ignorez si vous utilisez JavaScript.

Vous avez défini quelques variables d'état : `title`, `year`, `thumbnail` et `description` pour stocker les valeurs des entrées du formulaire.

Le hook `useGetMoviesQuery` récupère les données des films lorsque le composant est monté. Le hook retourne un objet avec plusieurs propriétés, mais nous nous concentrons sur trois propriétés : `data` aliasé comme `movies`, `isLoading` et `isError`.

Les hooks `useAddMovieMutation` et `useDeleteMovieMutation` retournent deux fonctions : `addMovie` et `deleteMovie`, respectivement.

La fonction `handleSubmit` gère la soumission du formulaire. Lorsque le formulaire est soumis, la fonction `addMovie` est appelée avec les détails du nouveau film. L'année est convertie en nombre, et l'ID est généré en fonction de la longueur actuelle du tableau de films.

Si une erreur se produit lors de la récupération des films (`isError`), un simple message d'erreur est affiché.

Si la requête API est toujours en cours de chargement (`isLoading`), un message de chargement est affiché.

Si tout se passe bien, la structure JSX principale du composant est retournée, qui inclut :

* un formulaire pour ajouter de nouveaux films.
    
* une liste de films rendue en utilisant le composant `MovieCard`. Chaque `MovieCard` reçoit les données individuelles du `movie` ainsi que la fonction `deleteMovie` pour gérer les suppressions.
    

Maintenant, créons notre composant `MovieCard`.

À l'intérieur du dossier **CardComponent**, créez un fichier `MovieCard.tsx`. Ouvrez `MovieCard.tsx` et collez le code suivant :

```tsx
import { useRef, useState } from "react";
import EditModal from "../Modal/EditModal";
import { Movie } from "../Movies";

type DeleteMovie = (movie:{id:string}) => void;

interface MovieCardProps {
  movie: Movie;
  deleteMovie: DeleteMovie;
}

function MovieCard({ movie, deleteMovie }: MovieCardProps) {

  const dialogRef = useRef<HTMLDialogElement | null>(null);
  const [selectedMovie, setSelectedMovie] = useState<Movie>(movie);

  const handleSelectedMovie = () => {
    setSelectedMovie(movie);
    dialogRef.current?.showModal();
    document.body.style.overflow = 'hidden';
  }

  const closeDialog = (): void => {
    dialogRef.current?.close();
    document.body.style.overflow = 'visible';
  }

  return (
    <div className="movie-wrapper" key={movie.id}>
      <div className="img-wrapper">
        <img src={movie.thumbnail} alt={`${movie.title} poster`} />
      </div>
      <h3>
        {movie.title} ({movie.year})
      </h3>
      <p>{movie.description}</p>
      <div className="button-wrapper">
        <button onClick={handleSelectedMovie}>Modifier</button>
        <button onClick={() => deleteMovie({ id: movie.id })}>Supprimer</button>
      </div>

      <EditModal dialogRef={dialogRef} selectedMovie={selectedMovie} closeDialog={closeDialog} />
      
    </div>
  );
}

export default MovieCard;
```

Dans le code ci-dessus, vous créez un composant `MovieCard` pour afficher les films à l'écran.

Vous importez les hooks `useRef` et `useState` de React pour gérer l'état et les références du composant. Vous importez également le composant `EditModal`, qui gérera la modification des détails du film, et le type `Movie` pour imposer la forme de l'objet film (ceci est pour TypeScript).

Le composant `MovieCard` accepte deux props : `movie` et `deleteMovie`.

La variable `dialogRef` est utilisée pour gérer la référence à l'élément de dialogue modal.

L'état `selectedMovie` est initialisé avec la prop `movie`. Cela sera utilisé pour suivre le film actuellement sélectionné à des fins de modification.

La fonction `handleSelectedMovie` est appelée lorsque le bouton **Modifier** est cliqué. Elle fait ce qui suit :

* Définit `selectedMovie` sur l'objet film actuel.
    
* Ouvre la boîte de dialogue `EditModal` en utilisant `dialogRef.current?.showModal()`.
    
* Empêche la page de défiler pendant que la modale est ouverte en définissant `document.body.style.overflow` sur `'hidden'`.
    

La fonction `closeDialog` ferme la boîte de dialogue modale en utilisant `dialogRef.current?.close()` et réinitialise le comportement de défilement de la page en définissant `document.body.style.overflow` sur `'visible'`.

Dans l'instruction `return`, une structure JSX est retournée qui affiche :

* une image pour la miniature du film,
    
* le titre du film et l'année de sortie dans un élément `h3`,
    
* une courte description du film,
    
* deux boutons :
    
    * Le bouton "Modifier" déclenche la fonction `handleSelectedMovie` pour ouvrir le `EditModal`.
        
    * Le bouton "Supprimer" appelle la fonction `deleteMovie`, en passant l'ID de requête du film pour supprimer le film spécifié de votre API.
        

Le composant `EditModal` est également rendu, en passant `dialogRef`, `closeDialog` et `selectedMovie` comme props. Cela garantit que le `EditModal` a accès aux détails du film sélectionné et à une fonction pour se fermer.

Ensuite, vous allez créer le composant `EditModal`.

À l'intérieur du dossier **Modal**, créez un fichier : `EditModal.tsx`, qui abritera le composant modal.

Ouvrez le fichier `EditModal.tsx` et collez le code suivant :

```tsx
import { useUpdateMovieMutation } from "../../state/movies/moviesApiSlice";
import { Movie } from "../Movies";
import "./modal.css";
import { useState, RefObject, FormEvent } from "react";

interface EditModalProps {
  dialogRef: RefObject<HTMLDialogElement>;
  selectedMovie: Movie;
  closeDialog: () => void;
}

function EditModal({ dialogRef, selectedMovie, closeDialog }: EditModalProps) {
  const [title, setTitle] = useState<string>(selectedMovie.title);
  const [year, setYear] = useState<string | number>(selectedMovie.year);
  const [description, setDescription] = useState<string>(selectedMovie.description);
  const [thumbnail, setThumbnail] = useState<string>(selectedMovie.thumbnail);

  const [updateMovie] = useUpdateMovieMutation();

  async function handleUpdateMovie(e: FormEvent<HTMLFormElement>){
    e.preventDefault();
    try {
      await updateMovie({title, description, year: Number(year), thumbnail, id: selectedMovie.id});
      closeDialog();
    } catch (error) {
      alert(`${error} s'est produit`);
    }
  }

  return (
    <dialog ref={dialogRef} className="modal-dialog">
      <form onSubmit={handleUpdateMovie}>
        <div className="form-group">
          <label htmlFor="title">Titre :</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="year">Année de sortie :</label>
          <input
            type="text"
            id="year"
            value={year}
            onChange={(e) => setYear(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="thumbnail">URL de l'image :</label>
          <input
            type="text"
            id="thumbnail"
            value={thumbnail}
            onChange={(e) => setThumbnail(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Description :</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          ></textarea>
        </div>
        <button type="submit">Enregistrer</button>
      </form>
      <button className="close-btn" onClick={closeDialog}>
        Fermer
      </button>
    </dialog>
  );
}

export default EditModal;
```

Dans le code ci-dessus, vous créez simplement une boîte de dialogue modale en utilisant l'élément HTML natif `<dialog>`. À l'intérieur de l'élément `dialog` se trouve un champ `form` rempli avec les détails du film sélectionné, obtenus à partir des variables d'état : `title`, `year`, `description` et `thumbnail`.

Vous avez importé le hook `useUpdateMovieMutation` depuis votre `moviesApiSlice`. Le hook `useUpdateMovieMutation` retourne une fonction `updateMovie` que vous pouvez utiliser pour mettre à jour les détails du film.

La fonction `handleUpdateMovie` est appelée lorsque le bouton **Enregistrer** est cliqué. Elle fait ce qui suit :

* met à jour les détails du film en appelant la fonction `updateMovie`
    
* ferme la boîte de dialogue en utilisant la fonction `closeDialog`
    

### **Montage de notre composant**

Accédez à votre fichier `App.tsx` et ajoutez votre composant `Movies` avec le code suivant :

```tsx
import "./App.css";
import Movies from "./components/Movies";

function App() {
  return (
    <div>
      <Movies />
    </div>
  );
}

export default App;
```

Dans votre navigateur, ouvrez votre [localhost](http://localhost) et vous devriez voir quelque chose comme ceci :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734787096281/f4f87b33-d5ba-4537-acd1-39dfa740410a.gif align="center")

Félicitations ! Vous avez intégré avec succès RTK Query avec Redux Toolkit.

Dans la section suivante, vous apprendrez comment fonctionne la mise en cache dans RTK Query et comment invalider les caches.

## Comment gérer la mise en cache des données avec RTK Query

Dans cette section, vous apprendrez comment fonctionne la mise en cache dans RTK Query et comment invalider les caches.

En programmation, la mise en cache est l'une des choses les plus difficiles à faire. Mais RTK Query facilite la gestion de la mise en cache pour nous.

Lorsque vous appelez votre API, RTK Query met automatiquement en cache le résultat de l'appel réussi de votre API. Cela signifie que les appels ultérieurs à l'API retournent le résultat mis en cache.

Par exemple, si vous essayez de modifier un film dans votre application, vous remarquerez que rien ne change. Cela ne signifie pas que cela ne fonctionne pas – en fait, cela fonctionne. Et les résultats retournés sont la version mise en cache (les résultats lorsque vous avez appelé l'API pour la première fois, c'est-à-dire au montage du composant).

Pour arrêter ce comportement, vous devez invalider le cache chaque fois que vous apportez des modifications à votre backend. Cela amènera RTK Query à récupérer automatiquement les données pour refléter vos modifications.

Accédez à votre fichier `moviesApiSlice.ts` et remplacez ce code par le code suivant :

```tsx

import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const moviesApiSlice = createApi({
  reducerPath: "movies",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://localhost:8080",
  }),
  tagTypes: ['Movies'],
  endpoints: (builder) => {
    return {
      getMovies: builder.query({
        query: () => `/movies`,
        providesTags: ['Movies']
      }),
      
      addMovie: builder.mutation({
        query: (movie) => ({
          url: "/movies",
          method: "POST",
          body: movie,
        }),
        invalidatesTags: ['Movies']
      }),

      updateMovie: builder.mutation({
        query: (movie) => {
          const { id, ...body } = movie;
          return {
            url: `movies/${id}`,
            method: "PUT",
            body
          }
        },
        invalidatesTags: ['Movies']
      }),

      deleteMovie: builder.mutation({
        query: ({id}) => ({
          url: `/movies/${id}`,
          method: "DELETE",
          body: id,
        }),
        invalidatesTags: ['Movies']
      }),
    };
  },
});

export const {
  useGetMoviesQuery,
  useAddMovieMutation,
  useDeleteMovieMutation,
  useUpdateMovieMutation,
} = moviesApiSlice;
```

Dans le code ci-dessus, vous avez ajouté la propriété `tagTypes` à votre `moviesApiSlice` et l'avez définie sur `[Movies]`. Cela sera utilisé pour invalider les résultats mis en cache lorsque vous apportez des modifications à votre backend.

Dans la fonction `getMovies`, vous avez ajouté la propriété `providesTags`. Cela signifie que vous fournissez un tag à votre appel API, que vous pouvez invalider avec les fonctions de mutation.

Dans les fonctions de mutation (`addMovie`, `updateMovie` et `deleteMovie`), vous avez ajouté la propriété `invalidatesTags` définie sur la valeur de la propriété `tagTypes`. Cela invalide le cache chaque fois que l'une de ces fonctions de mutation est appelée, ce qui amène RTK Query à récupérer automatiquement les données.

Avec ces modifications, vous pouvez mettre à jour et supprimer des films et voir le résultat de vos modifications.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734787129856/983cd55d-9714-4c0e-a038-2b7c9f60f881.gif align="center")

## Gestion des erreurs et états de chargement

Lorsque vous construisiez votre application, vous avez géré les erreurs qui pourraient survenir lors de l'appel de votre API en affichant simplement un texte "Erreur...".

Dans les applications réelles, vous souhaitez afficher quelque chose de significatif, comme une interface utilisateur qui indique à vos utilisateurs ce qui s'est mal passé exactement.

De même, lorsque votre requête API est en cours de chargement, vous souhaitez afficher un spinner de chargement ou une interface utilisateur squelette de chargement afin que vos utilisateurs sachent que les données de votre application sont en cours de chargement.

Pour les besoins de cet article, nous n'allons pas plonger dans la gestion avancée des erreurs ou la gestion des états de chargement – mais ce sont des choses que vous voudriez explorer.

## Bonnes pratiques

Voici quelques-unes des meilleures pratiques à considérer lors de l'utilisation de RTK Query :

1. **Séparer les tranches d'API multiples** : si vous avez plusieurs tranches d'API pour différentes API, envisagez de les séparer en différentes tranches d'API. Cela garde vos tranches d'API modulaires, ce qui facilite la maintenance et le débogage.
    
2. **Utiliser les Redux Devtools** : les Redux Devtools vous permettent de voir ce qui se passe dans votre store Redux ainsi que dans vos requêtes et mutations. Cela facilite grandement le débogage. Les Redux Devtools sont disponibles en tant qu'extension Chrome.
    
3. **Précharger les données** : utilisez le hook `usePrefetch` pour effectuer une récupération de données avant qu'un utilisateur ne navigue vers une page de votre site web ou ne charge un contenu connu. Cela réduit le temps de chargement et rend l'interface utilisateur plus rapide.
    
4. **Utiliser le middleware pour la logique complexe** : implémentez le middleware lorsque vous devez intercepter et modifier les actions ou les réponses, comme l'ajout de jetons d'authentification aux en-têtes ou la journalisation d'erreurs spécifiques.
    
5. **Utiliser les mises à jour optimistes** : lors de l'utilisation de `useMutation` pour mettre à jour ou modifier des données existantes, vous pouvez implémenter une mise à jour optimiste de l'interface utilisateur. Cela aide à donner l'impression de changements immédiats. Si la requête échoue, vous pouvez annuler la mise à jour.
    

## Conclusion

Dans cet article, vous avez appris ce qu'est RTK Query et comment intégrer RTK Query avec Redux Toolkit en construisant une application React CRUD de films. Vous avez également appris les stratégies de mise en cache de RTK Query et comment invalider les caches.

Merci d'avoir lu !