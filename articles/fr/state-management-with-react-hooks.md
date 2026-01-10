---
title: Comment gérer l'état dans une application React avec uniquement Context et
  Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-09T07:48:10.000Z'
originalURL: https://freecodecamp.org/news/state-management-with-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/home-page-2.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: react router
  slug: react-router
- name: Redux
  slug: redux
seo_title: Comment gérer l'état dans une application React avec uniquement Context
  et Hooks
seo_desc: 'By Samuel Omole

  Since the announcement of React Hooks, hundreds, if not thousands of articles, libraries,
  and video courses about them have been released. If you look carefully into the
  sea of resources, you''ll find an article I wrote a while back th...'
---

Par Samuel Omole

Depuis l'annonce des React Hooks, des centaines, voire des milliers d'articles, de bibliothèques et de cours vidéo à leur sujet ont été publiés. Si vous regardez attentivement dans l'océan de ressources, vous trouverez un article que j'ai écrit il y a quelque temps et qui impliquait la création d'une application d'exemple utilisant les Hooks. Vous pouvez trouver cet article [ici](https://freecodecamp.org/news/how-to-build-a-movie-search-app-using-react-hooks-24eb72ddfaf7/).

Sur la base de cet article, beaucoup (deux en fait) de personnes ont posé des questions liées à la manière dont l'état peut être géré dans une application React en utilisant uniquement Context et Hooks, ce qui m'a conduit à faire quelques recherches sur le sujet.

Donc pour cet article, nous allons travailler avec un modèle pour gérer l'état en utilisant deux Hooks très importants, useContext et useReducer, pour construire une simple application de galerie musicale. L'application n'aura que deux vues : une pour la connexion et l'autre pour lister les chansons de cette galerie.

La principale raison de la page de connexion est de montrer comment nous pouvons partager l'état d'authentification dans toute l'application, ce qui est un cas d'utilisation courant pour les applications qui utilisent une bibliothèque comme Redux.

Lorsque nous aurons terminé, nous devrions avoir une application qui ressemble aux images ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/login-page-1.png)
_Page de Connexion_

![Image](https://www.freecodecamp.org/news/content/images/2019/09/home-page-1.png)
_Page d'Accueil (J'ai utilisé le nom "hooked" à nouveau, malin, non ?)_

Pour le serveur backend, j'ai configuré une simple application Express et je l'ai hébergée sur Heroku. Elle a deux points de terminaison principaux :

* `/login`

Pour l'authentification. Après une connexion réussie, il retourne un jeton JWT et les détails de l'utilisateur.
* `/songs`

Retourne une liste de chansons.

Au cas où vous voudriez ajouter des fonctionnalités supplémentaires, le dépôt pour l'application backend peut être trouvé [ici](https://github.com/samie820/hooks-state-management-backend).

### RÉCAPITULATIF

Avant de commencer à construire l'application, examinons quelques-uns des hooks que nous allons utiliser :

* `useState`

Ce hook nous permet d'utiliser l'état dans les composants de fonction (l'équivalent de `this.state` et `this.setState` dans les composants de classe)
* `useContext`

Ce hook prend un objet de contexte et retourne ce qui est passé en tant que prop de valeur dans `MyContext.Provider`. Si vous ne connaissez pas le contexte, c'est un moyen de passer l'état d'un composant parent à n'importe quel autre composant dans l'arborescence (peu importe la profondeur) sans avoir à le passer à travers d'autres composants qui n'en ont pas besoin (un problème aptement nommé prop drilling). Vous pouvez en lire plus sur le contexte [ici](https://reactjs.org/docs/context.html).
* `useReducer`

C'est une alternative à `useState` et il peut être utilisé pour une logique d'état complexe. C'est mon hook préféré car il fonctionne exactement comme la bibliothèque Redux. Il accepte un réducteur de type :

```javascript
(state, action) => newState
```

Et aussi un objet d'état initial avant de retourner le nouvel état.

### COMMENCER

Pour commencer, nous allons utiliser la bibliothèque [create-react-app](https://github.com/facebook/create-react-app) pour démarrer le projet. Mais avant cela, voici quelques-unes des exigences nécessaires pour suivre :

* Node (
 6)
* Un éditeur de texte

Dans votre terminal, entrez la commande :

```bash
npx create-react-app hooked
```

Si vous n'avez pas `npx` disponible, vous pouvez installer create-react-app globalement sur votre système :

```javascript
npm install -g create-react-app
create-react-app hooked
```

Vous créerez cinq composants à la fin de cet article :

* Header.js

Ce composant contiendra l'en-tête de l'application (évidemment), et affichera également un bouton de déconnexion qui contient le prénom de l'utilisateur. Le bouton ne s'affichera que si l'utilisateur est authentifié.
* App.js

Il s'agit du composant de haut niveau où nous créerons le contexte d'authentification (j'en parlerai plus tard). Ce composant affichera également conditionnellement soit le composant Login si l'utilisateur n'est pas connecté, soit le composant Home si l'utilisateur est authentifié.
* Home.js

Ce composant récupérera une liste de chansons depuis le serveur et les affichera sur la page.
* Login.js

Ce composant contiendra le formulaire de connexion pour l'utilisateur. Il sera également responsable de l'envoi d'une requête POST au point de terminaison de connexion et de la mise à jour du contexte d'authentification avec la réponse du serveur.
* Card.js

Il s'agit d'un composant de présentation (UI) qui affiche les détails d'une chanson qui lui est passée.

Maintenant, créons des composants vides auxquels nous ajouterons plus tard de la logique. Dans le dossier `src`, créez un dossier et nommez-le `components`, puis créez ces quatre fichiers, à savoir, `Header.js`, `Home.js`, `Login.js`, et `Card.js` :

####   
Header.js

```javascript
import React from "react";
export const Header = () => {
  return (
    <nav id="navigation">
      <h1 href="#" className="logo">
        HOOKED
      </h1>
    </nav>
  );
};
export default Header;
```

[**Home.js**](https://www.freecodecamp.org/news/state-management-with-react-hooks/Home.js)

```javascript
import React from "react";
export const Home = () => {
return (
    <div className="home">
    </div>
  );
};
export default Home;
```

#### Login.js

```javascript
import React from "react";
import logo from "../logo.svg";
import { AuthContext } from "../App";
export const Login = () => {
return (
    <div className="login-container">
      <div className="card">
        <div className="container">
        </div>
      </div>
    </div>
  );
};
export default Login;
```

Et le fichier `App.js` devrait ressembler à ceci :

```javascript
import React from "react";
import "./App.css";
function App() {
return (
      <div className="App"></div>
  );
}
export default App;
```

Dans le fichier `App.js`, nous allons créer le contexte Auth qui passera l'état d'authentification de ce composant à tout autre composant qui en a besoin. Créez un contexte d'authentification comme ceci :

```javascript
import React from "react";
import "./App.css";
import Login from "./components/Login";
import Home from "./components/Home";
import Header from "./components/Header";
export const AuthContext = React.createContext(); // ajouté ceci
function App() {
return (
    <AuthContext.Provider>
      <div className="App"></div>
    </AuthContext.Provider>
  );
}
export default App;
```

Ensuite, nous ajoutons le hook `useReducer` pour gérer notre état d'authentification, et nous affichons conditionnellement soit le composant **Login**, soit le composant **Home**.

Rappelez-vous que le hook `useReducer` prend deux paramètres, un réducteur (qui est simplement une fonction qui prend l'état et l'action en tant que paramètres et retourne un nouvel état basé sur une action) et un état initial qui sera passé dans le réducteur. Ajoutons donc le hook dans notre composant `App` comme montré ci-dessous :

```javascript
import React from "react";
import "./App.css";
import Login from "./components/Login";
import Home from "./components/Home";
import Header from "./components/Header";
export const AuthContext = React.createContext();
const initialState = {
  isAuthenticated: false,
  user: null,
  token: null,
};
const reducer = (state, action) => {
  switch (action.type) {
    case "LOGIN":
      localStorage.setItem("user", JSON.stringify(action.payload.user));
      localStorage.setItem("token", JSON.stringify(action.payload.token));
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload.user,
        token: action.payload.token
      };
    case "LOGOUT":
      localStorage.clear();
      return {
        ...state,
        isAuthenticated: false,
        user: null
      };
    default:
      return state;
  }
};
function App() {
  const [state, dispatch] = React.useReducer(reducer, initialState);
return (
    <AuthContext.Provider
      value={{
        state,
        dispatch
      }}
    >
      <Header />
      <div className="App">{!state.isAuthenticated ? <Login /> : <Home />}</div>
    </AuthContext.Provider>
  );
}
export default App;
```

Il se passe beaucoup de choses dans l'extrait ci-dessus, mais laissez-moi expliquer chaque partie :

```javascript
const initialState = {
  isAuthenticated: false,
  user: null,
  token: null,
};
```

L'extrait ci-dessus est notre objet d'état initial qui sera utilisé dans notre réducteur. Les valeurs de cet objet dépendent principalement de votre cas d'utilisation. Dans notre cas, nous devons vérifier si un utilisateur est authentifié, contient les données de l'utilisateur, et si un jeton a été envoyé par le serveur après la connexion.

```javascript
const reducer = (state, action) => {
  switch (action.type) {
    case "LOGIN":
      localStorage.setItem("user", JSON.stringify(action.payload.user));
      localStorage.setItem("token", JSON.stringify(action.payload.token));
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload.user,
        token: action.payload.token
      };
    case "LOGOUT":
      localStorage.clear();
      return {
        ...state,
        isAuthenticated: false,
        user: null,
        token: null,
      };
    default:
      return state;
  }
};
```

La fonction de réduction contient une instruction switch qui, en fonction de certaines actions, retourne un nouvel état. Les actions dans le réducteur sont :

* `LOGIN`

Lorsque ce type d'action est dispatché, il sera également dispatché avec une charge utile (contenant `user` et `token`). Il sauvegarde l'utilisateur et le jeton dans localStorage et retourne ensuite un nouvel état, définissant `isAuthenticated` sur `true`, et définit également les clés `user` et `token` sur leurs valeurs respectives basées sur la charge utile de l'action.
* `LOGOUT`

Lorsque cette action est dispatchée, nous effaçons localStorage de toutes les données et définissons `user` et `token` sur `null`.

Si aucune action n'est dispatchée, il retourne l'état initial.

```javascript
const [state, dispatch] = React.useReducer(reducer, initialState);
```

Le hook `useReducer` retourne deux paramètres, `state` et `dispatch`. `state` contient l'état qui est utilisé dans le composant et il est mis à jour en fonction des actions dispatchées. `Dispatch` est une fonction qui est utilisée dans l'application pour appeler/dispatcher des actions qui transforment ou changent l'état.

```javascript
<AuthContext.Provider
      value={{
        state,
        dispatch
      }}
    >
      <Header />
      <div className="App">{!state.isAuthenticated ? <Login /> : <Home />}</div>
 </AuthContext.Provider>
```

Ici, dans le composant `Context.Provider`, nous passons un objet dans la prop `value`. L'objet contient le `state` et la fonction `dispatch` afin qu'il puisse être utilisé par tout autre composant qui nécessite ce contexte. Ensuite, nous affichons conditionnellement les composants
si l'utilisateur est authentifié, nous affichons le composant `Home`, sinon nous affichons le composant `Login`.

#### Composant de Connexion

Dans le composant de connexion, ajoutons les éléments nécessaires pour le formulaire comme montré ci-dessous :

```javascript
import React from "react";
export const Login = () => {
return (
    <div className="login-container">
      <div className="card">
        <div className="container">
          <form>
            <h1>Login</h1>
			
    		<label htmlFor="email">
              Email Address
              <input
                type="text"
                name="email"
                id="email"
              />
            </label>
			
    		<label htmlFor="password">
              Password
              <input
                type="password"
                name="password"
                id="password"
              />
            </label>
			
    		<button>
                "Login"
            </button>
          
    	  </form>
        </div>
      </div>
    </div>
  );
};
export default Login;
```

Dans le code ci-dessus, nous avons ajouté le JSX qui affiche le formulaire, ensuite nous allons ajouter le hook `useState` pour gérer l'état du formulaire. Une fois que nous avons ajouté le hook, notre code devrait ressembler à ceci :

```javascript
import React from "react";
export const Login = () => {
  const initialState = {
    email: "",
    password: "",
    isSubmitting: false,
    errorMessage: null
  };
const [data, setData] = React.useState(initialState);
const handleInputChange = event => {
    setData({
      ...data,
      [event.target.name]: event.target.value
    });
  };
return (
    <div className="login-container">
      <div className="card">
        <div className="container">
          <form>
            <h1>Login</h1>

    		<label htmlFor="email">
              Email Address
              <input
                type="text"
                value={data.email}
                onChange={handleInputChange}
                name="email"
                id="email"
              />
            </label>

			<label htmlFor="password">
              Password
              <input
                type="password"
                value={data.password}
                onChange={handleInputChange}
                name="password"
                id="password"
              />
            </label>

		{data.errorMessage && (
              <span className="form-error">{data.errorMessage}</span>
            )}

            <button disabled={data.isSubmitting}>
              {data.isSubmitting ? (
                "Loading..."
              ) : (
                "Login"
              )}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};
export default Login;
```

Dans le code ci-dessus, nous avons passé un objet `initialState` dans le hook `useState`. Dans l'objet, nous gérons l'état de l'email, l'état du mot de passe, un état qui est utilisé pour vérifier si le formulaire est en cours d'envoi au serveur et également une valeur `errorMessage` qui gère les erreurs du serveur.

Ensuite, nous allons ajouter une fonction qui gère la soumission du formulaire à l'API backend. Dans cette fonction, nous utiliserons l'API `fetch` pour envoyer la charge utile au serveur. Si la réponse est réussie, nous allons dispatcher une action `LOGIN` et également passer la réponse du serveur en tant que charge utile dans l'action dispatchée. Si une erreur provient du serveur (si les informations d'identification de connexion ne sont pas valides), nous appelons `setData` et passons le `errorMessage` du serveur qui sera affiché sur le formulaire. Afin d'appeler dispatch, nous devons importer le `AuthContext` du composant `App` dans notre composant `Login` et ensuite utiliser la fonction `dispatch` dans l'application. Votre composant `Login` final devrait ressembler à ceci :

```javascript
import React from "react";
import { AuthContext } from "../App";
export const Login = () => {
  const { dispatch } = React.useContext(AuthContext);
  const initialState = {
    email: "",
    password: "",
    isSubmitting: false,
    errorMessage: null
  };
const [data, setData] = React.useState(initialState);
const handleInputChange = event => {
    setData({
      ...data,
      [event.target.name]: event.target.value
    });
  };
const handleFormSubmit = event => {
    event.preventDefault();
    setData({
      ...data,
      isSubmitting: true,
      errorMessage: null
    });
    fetch("https://hookedbe.herokuapp.com/api/login", {
      method: "post",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: data.email,
        password: data.password
      })
    })
      .then(res => {
        if (res.ok) {
          return res.json();
        }
        throw res;
      })
      .then(resJson => {
        dispatch({
            type: "LOGIN",
            payload: resJson
        })
      })
      .catch(error => {
        setData({
          ...data,
          isSubmitting: false,
          errorMessage: error.message || error.statusText
        });
      });
  };
return (
    <div className="login-container">
      <div className="card">
        <div className="container">
          <form onSubmit={handleFormSubmit}>
            <h1>Login</h1>

			<label htmlFor="email">
              Email Address
              <input
                type="text"
                value={data.email}
                onChange={handleInputChange}
                name="email"
                id="email"
              />
            </label>

			<label htmlFor="password">
              Password
              <input
                type="password"
                value={data.password}
                onChange={handleInputChange}
                name="password"
                id="password"
              />
            </label>

			{data.errorMessage && (
              <span className="form-error">{data.errorMessage}</span>
            )}

           <button disabled={data.isSubmitting}>
              {data.isSubmitting ? (
                "Loading..."
              ) : (
                "Login"
              )}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};
export default Login;
```

#### Composant Home

Le composant `Home` gérera la récupération des chansons depuis le serveur et leur affichage. Puisque le point de terminaison de l'API nécessite que nous envoyions le jeton d'authentification, nous devrons trouver un moyen de l'obtenir depuis le composant `App` où il a été stocké.

Construisons le balisage pour ce composant. Nous voulons récupérer les chansons et parcourir la liste des chansons retournées, puis rendre un composant `Card` pour chaque chanson. Le composant `Card` est un simple composant fonctionnel auquel sont passés des `props` à rendre. Créez un fichier `Card.js` dans le dossier `components`, et dans ce fichier, ajoutez le code suivant :

```javascript
import React from "react";
export const Card = ({ song }) => {
    
  return (
    <div className="card">
      <img
        src={song.albumArt}
        alt=""
      />
      <div className="content">
        <h2>{song.name}</h2>
        <span>BY: {song.artist}</span>
      </div>
    </div>
  );
};
export default Card;
```

Puisqu'il ne gère aucune logique personnalisée mais rend plutôt les props qui lui sont passés, nous l'appelons un **Composant de Présentation**.

De retour dans notre composant `Home`, lors de la gestion des requêtes réseau dans la plupart des applications, nous essayons de visualiser trois états principaux. Tout d'abord, lorsque la requête est en cours de traitement (en utilisant un chargeur de quelque sorte), puis lorsque la requête est réussie (en rendant la charge utile ou en montrant une notification de succès), et enfin, lorsque la requête échoue (en montrant une notification d'erreur). Afin de faire une requête lorsque le composant est monté et également de gérer ces trois états, nous utiliserons les hooks `useEffect` et `useReducer`.

Pour notre hook `useReducer`, nous allons d'abord créer un objet pour contenir l'état initial pour notre réducteur, l'objet d'état initial ressemblera à l'extrait ci-dessous :

```javascript
const initialState = {
  songs: [],
  isFetching: false,
  hasError: false,
};
```

`songs` contiendra la liste des chansons récupérées depuis le serveur et elle est initialement vide. `isFetching` est utilisé pour représenter l'état de chargement et est initialement défini sur `false`. `hasError` est utilisé pour représenter l'état d'erreur et est également initialement défini sur `false`.

Nous pouvons maintenant créer le réducteur pour ce composant, il ressemblera à l'extrait ci-dessous :

```javascript
const reducer = (state, action) => {
  switch (action.type) {
    case "FETCH_SONGS_REQUEST":
      return {
        ...state,
        isFetching: true,
        hasError: false
      };
    case "FETCH_SONGS_SUCCESS":
      return {
        ...state,
        isFetching: false,
        songs: action.payload
      };
    case "FETCH_SONGS_FAILURE":
      return {
        ...state,
        hasError: true,
        isFetching: false
      };
    default:
      return state;
  }
};
```

Décomposons cela. Si nous dispatchons une action `FETCH_SONGS_REQUEST` dans notre application, nous retournons un nouvel état avec la valeur de `isFetching` définie sur `true`. Si nous dispatchons une action `FETCH_SONGS_SUCCESS` dans notre application, nous retournons un nouvel état avec la valeur de `isFetching` définie sur `false`, puis `songs` défini sur la charge utile renvoyée par le serveur. Enfin, si nous dispatchons une action `FETCH_SONGS_FAILURE` dans notre application, nous retournons un nouvel état avec la valeur de `isFetching` définie sur `false` et `hasError` défini sur `false`.

Maintenant que nous avons le hook useReducer, notre composant `Home` devrait ressembler à ceci :

```javascript
import React from "react";
import { AuthContext } from "../App";
import Card from "./Card";
const initialState = {
  songs: [],
  isFetching: false,
  hasError: false,
};
const reducer = (state, action) => {
  switch (action.type) {
    case "FETCH_SONGS_REQUEST":
      return {
        ...state,
        isFetching: true,
        hasError: false
      };
    case "FETCH_SONGS_SUCCESS":
      return {
        ...state,
        isFetching: false,
        songs: action.payload
      };
    case "FETCH_SONGS_FAILURE":
      return {
        ...state,
        hasError: true,
        isFetching: false
      };
    default:
      return state;
  }
};
export const Home = () => {
  const [state, dispatch] = React.useReducer(reducer, initialState);
return (
    <div className="home">
      {state.isFetching ? (
        <span className="loader">LOADING...</span>
      ) : state.hasError ? (
        <span className="error">AN ERROR HAS OCCURED</span>
      ) : (
        <>
          {state.songs.length > 0 &&
            state.songs.map(song => (
              <Card key={song.id.toString()} song={song} />
            ))}
        </>
      )}
    </div>
  );
};
export default Home;
```

Pour passer rapidement en revue ce qui se passe, à l'intérieur de la fonction `Home`, nous ajoutons le hook `useReducer` et passons le `reducer` et `initialState` qui à leur tour retournent deux variables, à savoir, `state` et `dispatch`.

Ensuite, dans notre fonction de rendu, nous affichons conditionnellement une `span` avec un texte "loading..." si `state.isFetching = true`, ou nous affichons une `span` avec un message d'erreur si `state.hasError = true`. Sinon, nous parcourons la liste des chansons et rendons chacune comme un composant `Card`, en passant les `props` nécessaires.

Pour tout rassembler, nous allons ajouter la fonction `useEffect` qui gérera les appels réseau et dispatchera l'`ACTION` nécessaire en fonction de la réponse du serveur. L'ajout du hook devrait faire ressembler notre composant `Home` à l'extrait ci-dessous :

```javascript
import React from "react";
import { AuthContext } from "../App";
import Card from "./Card";
const initialState = {
  songs: [],
  isFetching: false,
  hasError: false,
};
const reducer = (state, action) => {
  switch (action.type) {
    case "FETCH_SONGS_REQUEST":
      return {
        ...state,
        isFetching: true,
        hasError: false
      };
    case "FETCH_SONGS_SUCCESS":
      return {
        ...state,
        isFetching: false,
        songs: action.payload
      };
    case "FETCH_SONGS_FAILURE":
      return {
        ...state,
        hasError: true,
        isFetching: false
      };
    default:
      return state;
  }
};
export const Home = () => {
  const { state: authState } = React.useContext(AuthContext);
  const [state, dispatch] = React.useReducer(reducer, initialState);
React.useEffect(() => {
    dispatch({
      type: "FETCH_SONGS_REQUEST"
    });
    fetch("https://hookedbe.herokuapp.com/api/songs", {
      headers: {
        Authorization: `Bearer ${authState.token}`
      }
    })
      .then(res => {
        if (res.ok) {
          return res.json();
        } else {
          throw res;
        }
      })
      .then(resJson => {
        console.log(resJson);
        dispatch({
          type: "FETCH_SONGS_SUCCESS",
          payload: resJson
        });
      })
      .catch(error => {
        console.log(error);
        dispatch({
          type: "FETCH_SONGS_FAILURE"
        });
      });
  }, [authState.token]);

  return (
    <React.Fragment>
    <div className="home">
      {state.isFetching ? (
        <span className="loader">LOADING...</span>
      ) : state.hasError ? (
        <span className="error">AN ERROR HAS OCCURED</span>
      ) : (
        <>
          {state.songs.length > 0 &&
            state.songs.map(song => (
              <Card key={song.id.toString()} song={song} />
            ))}
        </>
      )}
    </div>
    </React.Fragment>
  );
};
export default Home;
```

Si vous remarquez, dans le code ci-dessus, nous avons utilisé un autre hook, le hook `useContext`. La raison est que, afin de récupérer les chansons depuis le serveur, nous devons également passer le jeton qui nous a été donné sur la page de connexion. Mais puisque c'était un autre composant, nous avons stocké le jeton dans le `AuthContext` et nous utilisons le hook `useContext` pour obtenir cette valeur de contexte et l'utiliser dans notre propre composant.

À l'intérieur de la fonction `useEffect`, nous dispatchons initialement `FETCH_SONGS_REQUEST` afin que la span de chargement s'affiche, puis nous effectuons la requête réseau en utilisant l'API `fetch` et en passant le jeton que nous avons obtenu du `AuthContext` en tant qu'en-tête. Si la réponse est réussie, nous dispatchons l'action `FETCH_SONGS_SUCCESS` et passons la liste des chansons obtenues du serveur en tant que charge utile dans l'action. Si une erreur provient du serveur, nous dispatchons l'action `FETCH_SONGS_FAILURE` afin que la span d'erreur soit affichée à l'écran.

La dernière chose à noter dans notre hook `useEffect` est que nous passons le jeton dans le tableau de dépendances du hook (lisez plus sur `useEffect` [ici](https://reactjs.org/docs/hooks-effect.html)). Cela signifie que notre hook ne sera appelé que lorsque ce jeton changera, ce qui ne peut se produire que si le jeton expire et que nous devons en récupérer un nouveau ou que nous nous connectons en tant que nouvel utilisateur. Donc pour cet utilisateur, le hook ne sera appelé qu'une seule fois.

D'accord, nous avons terminé avec la logique. Il ne reste plus que le CSS. Puisque entrer dans les détails du style de l'application dépasse le cadre de cet article, vous pouvez copier l'extrait CSS ci-dessous et le coller dans le fichier `App.css` :

```javascript
/******  PAGE DE CONNEXION  ******/
.login-container{
  display: flex;
  align-items: center;
  background-image: url("./assets/carry-on-colour.svg");
  height: calc(100vh - 70px);
  background-repeat: no-repeat;
  background-position: right;
  padding-left: 5%;
  padding-right: 5%;
  margin-top: 70px;
}
.card {
  /* Add shadows to create the "card" effect */
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  height: 70%;
  width: 45%;
}
/* On mouse-over, add a deeper shadow */
.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
/* Add some padding inside the card container */
.login-container .container {
  padding-left: 7%;
  padding-right: 7%;
  height: 100%;
}
.login-container .container h1{
  font-size: 2.5rem;
}
.login-container .container form{
  display: flex;
  height: 80%;
  flex-direction: column;
  justify-content: space-around;
  align-self: center;
}
input[type="text"], input[type="password"]{
  padding-left: 1px;
  padding-right: 1px;
  height: 40px;
  border-radius: 5px;
  border: .5px solid rgb(143, 143, 143);
  font-size: 15px;
}
label{
  display: flex;
  flex-direction: column;
}
.login-container button{
  height: 40px;
  font-weight: bold;
  font-size: 15px;
  background-color: #F42B4B;
  color: rgb(255, 255, 255);
}
.login-container button:hover{
  background-color: rgb(151, 25, 46);
  cursor: pointer;
}
.login-container button:focus{
  outline: none !important;
}


.spinner {
  animation: spinner infinite .9s linear;
  height: 90%;
}
.spinner:focus{
  border:none;
}
@keyframes spinner {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
.form-error{
  color: #F42B4B;
  text-align: center;
}
@media screen and (max-width: 700px){
  .login-container{
    justify-content: center;
    background-image: none;
  }
  .card {
    width: 80%;
    align-self: center;
  }
  
}
@media screen and (max-width: 350px){
  .card {
    width: 100%;
  }
  
}
/******  PAGE DE CONNEXION  ******/


/******  EN-TÊTE  ******/
#navigation{
  width: 100%;
  position: fixed;
  z-index: 10;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  background-color: #F42B4B;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  height: 70px;
  top: 0;
  padding-right: 5px;
  padding-left: 5px;
}
#navigation h1{
  color: white;
}
#navigation button{
  background-color: transparent;
  border: none;
  align-self: center;
}
#navigation button:hover{
  cursor: pointer;
}
#navigation button:focus{
  outline: none !important;
}
/******  EN-TÊTE  ******/


/******  PAGE D'ACCUEIL  ******/
.home {
  margin-top: 100px;
  margin-left: 2%;
  margin-right: 2%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
.home .loader{
  align-self: center;
  width: 100%;
  text-align: center;
}
.home .error{
  width: 100%;
  align-self: center;
  color: #F42B4B;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
}
.home>.card {
  /* Add shadows to create the "card" effect */
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  height: 400px;
  width: 30%;
  position: relative;
  margin-bottom: 2%;
}
/* On mouse-over, add a deeper shadow */
.home .card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
.home .card>img{
  width: 100%;
  height: 100%;
}
.home .content{
  bottom: 0;
  z-index: 9;
  position: absolute;
  background-color: rgba(255, 255, 255, 0.7);
  display: flex;
  flex-direction: column;
  width: 100%;
  align-items: center;
  height: 35%;
  padding-bottom: 5px;
  transition: 0.5s;
}
.home .content:hover{
  background-color: rgba(255, 255, 255, 1);
  height: 50%;
  cursor: pointer;
}
.content>h2{
  text-align: center;
  font-size: 2rem;
}
@media screen and (max-width: 780px){
.home{
    justify-content: space-around;
  }
  .home .card {
    width: 45%;
  }
}
@media screen and (max-width: 500px){
  .home .card {
    width: 90%;
  }
}
@media screen and (min-width: 1400px){
  .home {
    margin: auto;
    width: 1400px;
  }
  .toggle-button{
    margin-bottom: 10px;
  }
}
/******  PAGE D'ACCUEIL  ******/
```

Cet article était un peu long, mais j'espère qu'il couvre un cas d'utilisation courant avec l'utilisation de hooks pour gérer l'état dans notre application.

Vous pouvez accéder au dépôt GitHub en cliquant sur ce [lien](https://github.com/samie820/hooks-state-management). Notez que le dépôt contient certaines fonctionnalités supplémentaires comme la création d'une nouvelle chanson.