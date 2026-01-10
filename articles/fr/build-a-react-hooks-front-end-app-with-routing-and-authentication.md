---
title: Comment créer une application front-end React Hooks avec routage et authentification
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-30T20:10:37.000Z'
originalURL: https://freecodecamp.org/news/build-a-react-hooks-front-end-app-with-routing-and-authentication
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/photo-1551373802-aec2b9a165aa.jpg
tags:
- name: react hooks
  slug: react-hooks
seo_title: Comment créer une application front-end React Hooks avec routage et authentification
seo_desc: "By Mohammad Iqbal\nIn this tutorial, we will go over how to build a complete\
  \ front end app with routing and authentication. \nI have structured this tutorial\
  \ and project as basically a boilerplate project with basic routing and auth that\
  \ can be used as..."
---

Par Mohammad Iqbal

Dans ce tutoriel, nous allons voir comment créer une application front-end complète avec routage et authentification. 

J'ai structuré ce tutoriel et ce projet comme un projet de base avec un routage et une authentification de base qui peut être utilisé comme projet de départ. 

Si vous voulez simplement le code de base sans les explications, le voici : 
[https://github.com/iqbal125/react-hooks-routing-auth-starter](https://github.com/iqbal125/react-hooks-routing-auth-starter)

J'utiliserai Auth0 pour l'authentification, mais cette configuration fonctionnera également avec tout autre système d'authentification basé sur des tokens.  
  
Vous pouvez regarder une version vidéo fullstack de ce tutoriel ici  
[https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5](https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5)

> Connectez-vous avec moi sur Twitter pour plus de mises à jour sur les futurs tutoriels : [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf)

### Table des matières

1. Structure du projet
2. useReducer vs useState pour l'état du contexte global
3. État global avec Context
4. Authentification et vérification d'authentification
5. Composants React Hooks
6. Routage
7. App.js

## Structure du projet

Je vais d'abord passer en revue la structure de notre application. Notre application peut être divisée en 4 parties : 

* Composants fonctionnels React hooks
* Réducteurs et Actions 
* Fichiers utilitaires 
* Fichiers principaux

Nous aurons également besoin de 4 bibliothèques pour construire notre application

 `npm install auth0-js react-router react-router-dom history`

### Structure des répertoires :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-148.png)



### Composants fonctionnels React Hooks

Ici, nous avons nos composants fonctionnels React Hooks. Nous avons une configuration assez simple et nous n'utiliserons aucun composant de classe React dans cette application.

**callback.js :** sera utilisé comme le composant vers lequel Auth0 redirigera après que l'utilisateur se soit authentifié.

**header.js :** contiendra les liens vers les composants et un bouton de connexion ou de déconnexion basé sur l'état d'authentification de l'utilisateur.

**home.js :** affichera simplement le texte de la page d'accueil.

**hook1.js :** contiendra les trois façons de mettre à jour l'état avec les hooks React, `useState`, `useReducer` et `useContext`. Avoir les trois façons de mettre à jour l'état dans un seul composant vous permettra de mieux comprendre les différences entre chacune.

**hooks_form1.js :** Aura un formulaire qui utilise les trois façons de mettre à jour l'état avec `useState`, `useReducer` et `useContext`.

**privatecomponent.js :** Un composant qui n'est accessible que par les utilisateurs authentifiés.

**profile.js :** Un tableau de bord utilisateur qui affiche les données du profil utilisateur.

### Fichiers Réducteurs et Actions

**action_types.js :** Contiendra tous les types d'actions sous forme de chaînes dans des variables. Cela permettra de modifier facilement vos types d'actions puisque vous n'aurez à les changer que ici au lieu de devoir les rechercher partout où vous avez utilisé l'action dans votre code.

**actions.js :** Contiendra les actions réelles qui seront utilisées dans le réducteur pour mettre à jour l'état.

**auth_reducer.js :** Contiendra le réducteur pour lire et mettre à jour les propriétés d'état liées à l'authentification.

**form_reducer.js :** Contiendra le réducteur pour lire et mettre à jour les propriétés d'état liées à notre formulaire.

**plain_reducer.js :** Servira de réducteur de base.

### Fichiers utilitaires

Nous aurons également besoin de 4 fichiers utilitaires pour aider à configurer notre application.

**context.js :** Contiendra l'objet Context et sera importé dans chaque composant qui utilise le hook useContext().

**auth.js :** Ce sera la seule classe de l'application. Notez que ce n'est pas un composant de classe React, mais une classe javascript vanilla. J'ai essayé de configurer ce fichier comme une fonction fléchée mais cela n'a pas bien fonctionné. Ce fichier est mieux configuré comme une classe. Ce fichier contiendra toutes nos fonctions et variables associées à l'authentification.

**history.js :** Contiendra l'objet history que nous utiliserons pour la navigation.

**authcheck.js :** Sera utilisé pour mettre à jour l'état d'authentification de l'utilisateur et récupérer les données du profil utilisateur et les sauvegarder dans l'état global.

### Fichiers principaux

Ce sont les fichiers principaux et ils se trouveront dans le **répertoire racine /src**. J'ai mis toute la logique métier pour la lecture et la mise à jour de l'état global dans un seul fichier, le `context_state_config.js`. Ma raison de faire cela est la suivante.

Avoir toute la complexité dans un seul fichier rend en fait votre application plus simple et plus facile à déboguer puisque c'est facile de suivre où faire les changements et les corrections. 

Avoir de nombreux composants légèrement complexes, selon mon expérience, rendra en fait votre application plus difficile à déboguer et à changer. Donc pour cette raison, j'ai mis tout le code d'état global dans ce fichier. 

De plus, dans le `context_state_config.js`, le composant `<Routes />` sera enveloppé par le `<Context.Provider />`. Cela permettra de lire et de mettre à jour l'état d'être passé à travers la propriété `value` à tous les composants, créant un état global.

**context_state_config.js :** Ce fichier contiendra toute la logique pour lire et mettre à jour l'état global avec le hook `useReducer` et le `context`. 

**routes.js :** Contiendra toute notre logique de routage et aura également une authentification silencieuse ici.

**App.js :** Notre composant racine, nous importerons et afficherons simplement notre composant `context_state_config.js`.

**index.js :** Notre fichier racine, rendra simplement App.js ici.

## useRedux vs useState pour l'état du contexte global

Pour gérer l'état global, nous utiliserons **Réducteurs et Actions**. L'utilisation de Réducteurs et Actions avec le hook `useReducer()` et **Context** nous permettra d'atteindre une fonctionnalité similaire à **Redux** sans utiliser Redux.

Il est possible de gérer notre état global avec le hook `useState` et **Context**, mais l'utilisation de `useReducer` rend la gestion de l'état global beaucoup plus organisée. Le hook `useState` est bien meilleur pour gérer l'état local des composants. 

Avoir des propriétés d'état liées et toutes les fonctions de mise à jour d'état dans le même hook `useReducer` rend les choses très simples et compartimentées par rapport à l'utilisation du hook `useState` qui peut être beaucoup plus décentralisé.  

**L'envoi d'actions** rend également le flux de données plus facile à suivre par rapport à l'utilisation de la fonction `setState` de `useState` puisque chaque action décrira exactement comment l'état sera modifié.

Nous n'avons pas non plus besoin d'utiliser la fonction combine reducer ou de combiner nos réducteurs de quelque manière que ce soit. Chaque réducteur sera passé dans son propre hook useReducer.

## Configuration de l'état global avec Context

Nous pouvons commencer par configurer l'état global, ce qui, à mon avis, facilite grandement la création des composants React. 

Si vous avez déjà configuré l'état global, vous pouvez créer le composant de manière très simple au lieu d'avoir à aller et venir entre la configuration du composant et la configuration de son état.

Pour configurer l'état global, nous devrons créer nos **actions, réducteurs et contexte.**

Commençons par nos types d'actions :

```javascript

//action_types.js

export const SUCCESS = "SUCCESS"

export const FAILURE = "FAILURE"

export const LOGIN_SUCCESS = "LOGIN_SUCCESS"

export const LOGIN_FAILURE = "LOGIN_FAILURE"

export const ADD_PROFILE = "ADD_PROFILE"

export const REMOVE_PROFILE = "REMOVE_PROFILE"

export const USER_INPUT_CHANGE = "USER_INPUT_CHANGE"

export const USER_INPUT_SUBMIT = "USER_INPUT_SUBMIT"

```

**SUCCESS** et **FAILURE :** Seront utilisés comme nos actions de base.

**LOGIN_SUCCESS** et **LOGIN_FAILURE :** Utilisés pour mettre à jour l'état d'authentification de l'utilisateur. LOGIN_SUCCESS et LOGOUT_SUCCESS fonctionneraient également ici, mais j'aime la dichotomie de succès et d'échec.

**ADD_PROFILE** et **REMOVE_PROFILE :** Utilisés pour sauvegarder les données de profil d'Auth0 dans l'état global.

**USER_INPUT_CHANGE** et **USER_INPUT_SUBMIT :** Utilisés pour suivre les changements et la soumission du texte soumis par l'utilisateur dans le formulaire.

### Actions :

```javascript
//actions.js

import * as ACTION_TYPES from './action_types'

export const SUCCESS = {
  type: ACTION_TYPES.SUCCESS
}

export const FAILURE = {
  type: ACTION_TYPES.FAILURE
}


export const success = () => {
  return {
    type: ACTION_TYPES.SUCCESS
  }
}

export const failure = () => {
  return {
    type: ACTION_TYPES.FAILURE
  }
}



export const login_success = () => {
  return {
    type: ACTION_TYPES.LOGIN_SUCCESS
  }
}

export const login_failure = () => {
  return {
    type: ACTION_TYPES.LOGIN_FAILURE
  }
}

export const add_profile = (profile) => {
  return {
    type: ACTION_TYPES.ADD_PROFILE,
    payload: profile
  }
}

export const remove_profile = () => {
  return {
    type: ACTION_TYPES.REMOVE_PROFILE
  }
}

export const user_input_change = (text) => {
  return {
    type: ACTION_TYPES.USER_INPUT_CHANGE,
    payload: text
  }
}

export const user_input_submit = (text) => {
  return {
    type: ACTION_TYPES.USER_INPUT_SUBMIT,
    payload: text
  }
}

```

Pour garder les choses simples, j'ai fait de toutes les actions des créateurs d'actions au lieu d'en avoir certaines comme actions et d'autres comme créateurs d'actions. 

Les deux premières variables `SUCCESS` et `FAILURE` sont des actions régulières. 

### Réducteur d'authentification :

```javascript
//auth_reducer.js

import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  is_authenticated: false,
  profile: null
}

export const AuthReducer = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.LOGIN_SUCCESS:
        return {
          ...state,
          is_authenticated: true
        }
      case ACTION_TYPES.LOGIN_FAILURE:
        return {
          ...state,
          is_authenticated: false
        }
      case ACTION_TYPES.ADD_PROFILE:
        return {
          ...state,
          profile: action.payload
        }
      case ACTION_TYPES.REMOVE_PROFILE:
        return {
          ...state,
          profile: null
        }
      default:
        return state
    }
}

```

Ici, nous avons notre `auth_reducer.js` qui contiendra nos propriétés d'état et les actions associées pour **l'état d'authentification de l'utilisateur** et **les données de profil de l'utilisateur.**

Il est important de noter que nous exportons à la fois le réducteur et l'état initial au lieu d'exporter uniquement le réducteur comme nous le faisons dans React Redux.

### form_reducer :

```javascript
//form_reducer.js

import * as ACTION_TYPES from '../actions/action_types'


export const initialState = {
  user_textChange: '',
  user_textSubmit: ''
}


export const FormReducer = (state, action) => {
    switch(action.type) {
      case ACTION_TYPES.USER_INPUT_CHANGE:
        return {
          ...state,
          user_textChange: action.payload
        }
      case ACTION_TYPES.USER_INPUT_SUBMIT:
        return {
          ...state,
          user_textSubmit: action.payload
        }
      default:
        throw new Error();
    }
}

```

Ici, nous avons 2 propriétés pour un formulaire. Notre première propriété suit les changements de l'élément d'entrée et notre deuxième propriété ajoute le formulaire soumis à l'état global.

### plain_reducer : 

```javascript
//plain_reducer.js


import * as ACTION_TYPES from '../actions/action_types'

export const initialState = {
  stateprop1: false,
  stateprop2: false
}

export const Reducer1 = (state = initialState, action) => {
    switch(action.type) {
      case ACTION_TYPES.SUCCESS:
        return {
          ...state,
          stateprop1: true,
          stateprop2: true
        }
      case ACTION_TYPES.FAILURE:
        return {
          ...state,
          stateprop1: false,
          stateprop2: false
        }
      default:
        throw new Error();
    }
}
```

Comme nos actions SUCCESS et FAILURE, ce réducteur servira de modèle si nous voulons créer de nouveaux réducteurs.

### Configuration de l'objet Context

Nous devons maintenant initialiser notre objet Context. Nous pouvons le faire dans un fichier `context.js` dans le répertoire **utils**.

```javascript
import React from 'react';

const Context = React.createContext()

export default Context;

```

C'est tout ce que nous avons à faire pour initialiser notre variable Context. Nous pouvons maintenant l'utiliser en l'important dans notre fichier `context_state_config.js`.

## État global avec Context

```jsx
import React, { useReducer } from 'react';
import Context from './utils/context';
import * as ACTIONS from './store/actions/actions';

import * as Reducer1 from './store/reducers/plain_reducer';
import * as AuthReducer from './store/reducers/auth_reducer';
import * as FormReducer from './store/reducers/form_reducer';
import Routes from './routes';

import Auth from './utils/auth';


const auth = new Auth()


const ContextState = () => {
    /*
        Plain Reducer
    */
    const [stateReducer1, dispatchReducer1] = useReducer(Reducer1.Reducer1,
                                                         Reducer1.initialState)


    const handleDispatchTrue = () => {
      //    dispatchReducer1(type: "SUCCESS")
      //    dispatchReducer1(ACTIONS.SUCCESS)
      dispatchReducer1(ACTIONS.success())
    }

    const handleDispatchFalse = () => {
      //     dispatchReducer1(type: "FAILURE")
      //    dispatchReducer1(ACTIONS.FAILURE)
      dispatchReducer1(ACTIONS.failure())
    }

    /*
      Auth Reducer
    */
    const [stateAuthReducer, dispatchAuthReducer] =                      useReducer(AuthReducer.AuthReducer,
                                                           AuthReducer.initialState)


    const handleLogin = () => {
      dispatchAuthReducer(ACTIONS.login_success())
    }

    const handleLogout = () => {
      dispatchAuthReducer(ACTIONS.login_failure())
    }

    const handleAddProfile = (profile) => {
      dispatchAuthReducer(ACTIONS.add_profile(profile))
    }

    const handleRemoveProfile = () => {
      dispatchAuthReducer(ACTIONS.remove_profile())
    }



    /*
      Form Reducer
    */

        const [stateFormReducer, dispatchFormReducer] = useReducer(FormReducer.FormReducer, FormReducer.initialState)


    const handleFormChange = (event) => {
      dispatchFormReducer(ACTIONS.user_input_change(event.target.value))
    };

    const handleFormSubmit = (event) => {
      event.preventDefault();
      event.persist();             dispatchFormReducer(ACTIONS.user_input_submit(event.target.useContext.value))
    };

    //Handle authentication from callback
    const handleAuthentication = (props) => {
      if(props.location.hash) {
        auth.handleAuth()
      }
    }



    return(
      <div>
      <Context.Provider
          value={{
            //Reducer1
            stateProp1: stateReducer1.stateprop1,
            stateProp2: stateReducer1.stateprop2,
            dispatchContextTrue: () => handleDispatchTrue(),
            dispatchContextFalse: () => handleDispatchFalse(),

            //Form Reducer
            useContextChangeState: stateFormReducer.user_textChange,
            useContextSubmitState: stateFormReducer.user_textSubmit,
            useContextSubmit: (event) => handleFormSubmit(event),
            useContextChange: (event) => handleFormChange(event),

            //Auth Reducer
            authState: stateAuthReducer.is_authenticated,
            profileState:  stateAuthReducer.profile,
            handleUserLogin: () => handleLogin(),
            handleUserLogout: () => handleLogout(),
            handleUserAddProfile: (profile) => handleAddProfile(profile),
            handleUserRemoveProfile: () => handleRemoveProfile(),

            //Handle auth
            handleAuth: (props) => handleAuthentication(props),
            authObj: auth
          }}>
          <Routes />
      </Context.Provider>
      </div>
    )
}


export default ContextState;
```

> * Notez que vous ne voulez probablement pas avoir autant de variables et de fonctions dans le contexte dans une vraie application, ceci est juste à des fins de démonstration. Supprimez simplement les propriétés dont vous n'avez pas besoin. 

> **Note : Vous pouvez également utiliser la destructuration d'objet sur les propriétés à l'intérieur de la prop value pour rendre le code un peu plus propre. Ex :  `{ handlelogin }` au lieu de `handleUserLogin: () => handleLogin()`. Mais je les ai gardés séparés pour qu'il soit plus facile de voir comment les propriétés du contexte sont accessibles dans les composants enfants pour les personnes qui ne sont pas familières avec la destructuration. 

### Importation des réducteurs et useReducer()

Je vais expliquer comment cela fonctionne en utilisant Reducer1 comme exemple, mais cela s'applique également aux autres réducteurs. 

Nous commençons tout en haut en important toutes nos actions et réducteurs. Nous passons ensuite notre `Reducer1` et son état initial au hook `useReducer()`. Nous utilisons la syntaxe `import * as Reducer1` car nous voulons importer à la fois le `Reducer1` et l'`initialState`. Ensuite, nous utilisons la syntaxe `Reducer1.Reducer1` pour accéder à `Reducer1` et l'`intialState` peut être accédé en utilisant `Reducer1.initailState`. 

Après cela, nous sauvegardons le résultat du hook `useReducer()` en utilisant la destructuration de tableau.

Dans l'exemple ci-dessus, `stateReducer1` est la façon dont nous accédons aux propriétés d'état que nous avons définies dans l'`intialState` de `Reducer1`.

`dispatchReducer1` est notre fonction de dispatch qui nous permet de mettre à jour l'état avec des actions.

### Schéma de nommage des réducteurs

Comme vous pouvez probablement le constater, mon schéma de nommage préféré sont les mots "state" et "dispatch" suivis du nom de leur réducteur respectif. 

J'ai trouvé que c'était le schéma de nommage le plus efficace car il n'y a pas d'ambiguïté sur quel état et quelle fonction de dispatch appartient à quel réducteur, ce qui est important car nous ne combinons pas les réducteurs.

### Actions

Nos actions proviennent du même fichier d'actions que nous avons configuré dans la dernière section. Nous les importons toutes ici et pouvons accéder à chaque action avec la syntaxe ACTIONS.name_of_action(). 

C'est ce que nous passons dans notre fonction `dispatch`, qui indique à notre réducteur comment mettre à jour l'état.  

Après notre appel au hook `useReducer()`, nous avons nos fonctions `handleDispatchTrue()` et `handleDispatchFalse()` qui envoient nos actions `SUCCESS` et `FAILURE` pour changer notre `stateprop1` et `stateprop2` de false à true et vice versa.

Vous pouvez passer les fonctions de dispatch directement dans la prop "value" mais les avoir dans une fonction juste sous leur hook `useReducer` respectif rend le code plus organisé et lisible.

J'ai également laissé 2 autres façons d'envoyer des actions. Les trois façons d'envoyer des actions font la même chose, envoyer un objet javascript avec une propriété type qui a une valeur de la chaîne "SUCCESS".

### AuthReducer

Ensuite, nous avons notre `AuthReducer`. Nous avons configuré cela de manière similaire au réducteur simple. Nous mettons à jour notre état d'authentification de l'utilisateur s'ils sont connectés ou non et ajoutons et supprimons également leurs données de profil utilisateur de l'état global. N'oubliez pas de passer le paramètre de profil au créateur d'action.

### FormReducer

Après cela, nous avons notre `FormReducer`, qui sera également configuré de manière similaire aux réducteurs précédents.

Puisque ces actions vont être utilisées avec un formulaire, nous devons passer le mot-clé `event` comme paramètre à nos deux fonctions. Pour accéder au texte que notre utilisateur entre, nous devons utiliser la syntaxe `event.target.value`. Cela fait partie de javascript vanilla et est la manière standard d'accéder aux données de formulaire. 

Notre fonction `handleFormSubmit()` est un peu différente. Tout d'abord, nous devons utiliser la fonction `event.preventDefault()` pour empêcher la page de se recharger.

Ensuite, nous utilisons la fonction `event.persist()`. Puisque nous utilisons Context et que ces données proviennent d'un composant enfant, nous devons utiliser cette fonction pour que le formulaire fonctionne correctement. Ensuite, pour accéder au texte soumis par l'utilisateur, nous utilisons la syntaxe `event.target.useContext.value`

"useContext" ne fait pas référence au hook, c'est la propriété `id` définie par l'utilisateur fournie à l'élément d'entrée du formulaire. J'ai décidé de nommer l'id "useContext" parce que le composant a 2 autres formulaires ainsi et ils utilisent les hooks "useState" et "useReducer" pour sauvegarder l'état et ont donc l'id de "useState" et "useReducer".

### Fournisseur de contexte

Après avoir configuré les hooks `useReducer`, nous avons notre composant `<Context.Provider />` dans le JSX. Nous passons maintenant toutes les fonctions et valeurs d'état que nous venons de définir à la prop `value`.

Nous commençons par `stateprop1` et `stateprop2`. Il est important de noter qu'ils doivent chacun être accessibles en utilisant la notation par points séparément puisque `stateReducer1` contient l'objet `initialState` entier.

Nous définissons également 2 autres propriétés, `dispatchContextTrue` et `dispatchContextFalse`, et passons une fonction fléchée pour chacune qui appelle nos fonctions `handleDispatchTrue()` et `handleDispatchFalse()`. Il peut être utile pour vous de nommer les propriétés différemment des noms des fonctions. Cela vous aide à mieux voir ce qui se passe dans les composants enfants.

Ensuite, nous continuerons à construire notre application en configurant l'authentification.

## Authentification et vérification d'authentification

Ici, nous avons notre fichier `auth.js` qui sera configuré comme une classe Javascript. Et nous utiliserons Auth0 et la bibliothèque `auth0-js` pour nous aider avec l'authentification.

Le fichier utilitaire d'authentification sera configuré comme suit : 

```javascript
import auth0 from 'auth0-js'
import history from './history';

export default class Auth {
  auth0 = new auth0.WebAuth({
    domain: 'webapp1.auth0.com',
    clientID: '',
    redirectUri: 'http://localhost:3000/callback',
    responseType: 'token id_token',
    scope: 'openid profile email'
  })

  userProfile = {}

  login = () => {
      this.auth0.authorize()
  }

  handleAuth = () => {
    this.auth0.parseHash((err, authResult) => {
      if(authResult) {
        localStorage.setItem('access_token', authResult.accessToken)
        localStorage.setItem('id_token', authResult.idToken)

        let expiresAt = JSON.stringify((authResult.expiresIn * 1000 + new Date().getTime()))
        localStorage.setItem('expiresAt', expiresAt)

        this.getProfile();
        setTimeout(() => { history.replace('/authcheck') }, 600);
      } else {
        console.log(err)
      }
    })
  }

  getAccessToken = () => {
    if(localStorage.getItem('access_token')) {
      const accessToken = localStorage.getItem('access_token')
      return accessToken
    } else {
      return null
    }
  }


  getProfile = () => {
    let accessToken = this.getAccessToken()
    if(accessToken) {
      this.auth0.client.userInfo(accessToken, (err, profile) => {
          if(profile) {
            this.userProfile = { profile }
          }
      } )
    }
  }


  logout = () => {
    localStorage.removeItem('access_token')
    localStorage.removeItem('id_token')
    localStorage.removeItem('expiresAt')
    setTimeout(() => { history.replace('/authcheck') }, 200);
  }

  isAuthenticated = () => {
    let expiresAt = JSON.parse(localStorage.getItem('expiresAt'))
    return new Date().getTime() < expiresAt
  }

}

```

`auth0`**:** C'est la propriété que nous utiliserons pour initialiser notre application Auth0.

`userProfile`**:** C'est un objet vide qui contiendra les données de profil utilisateur que nous obtenons d'Auth0.

`login`: Cela fait apparaître le widget de connexion Auth0, permettant à l'utilisateur de se connecter avec la fonction `.authorize()` donnée.  

`handleAuth`: Cette fonction sauvegarde les jetons d'identification et d'accès que nous obtenons d'Auth0 dans le stockage local du navigateur. Cette fonction définit également l'heure d'expiration du jeton.

`getAccessToken`**:**  Obtenir le jeton d'accès depuis le stockage local

`getProfile`: Analyser le jeton d'accès pour extraire les données du profil utilisateur

`logout`**:** Déconnecte l'utilisateur en supprimant les jetons du stockage local

`isAuthenticated`**:** s'assure que l'utilisateur est connecté en comparant l'heure d'expiration à l'heure actuelle.

Maintenant, nous pouvons initialiser cet objet d'authentification et ajouter l'authentification au fichier `context_state_config.js`.

```jsx
....


import Auth from './utils/auth';


const auth = new Auth()


const ContextState = () => {

....


//Handle authentication from callback
    const handleAuthentication = (props) => {
      if(props.location.hash) {
        auth.handleAuth()
      }
    }

....

        //Handle auth
        handleAuth: (props) => handleAuthentication(props),
        authObj: auth
        }}>
       <Routes />
     </Context.Provider>

....

```

`new Auth ()` est la façon dont nous initialisons notre classe puis la sauvegardons dans la variable `auth`. 

Ensuite, nous créons une fonction `handleAuthentication()`. Si `props.location.hash` est vrai, alors nous appelons la fonction `auth.handleAuth()` que nous venons de configurer dans la classe Auth. `props.location.hash` est une fonctionnalité donnée de react-router qui vérifie s'il y a une valeur dans le fragment de hachage de l'URL. 

Si Auth0 authentifie avec succès un utilisateur, les jetons d'accès et d'identification seront inclus après un hachage dans l'URL, rendant `props.location.hash` vrai, ce qui appelle notre fonction `handleAuth()` dans la classe Auth.

Dans le `<Context.Provider />`  nous avons 2 propriétés, `handleAuth` qui appelle notre fonction `handleAuthentication()` et `authObj` que nous utilisons pour transmettre toute notre classe Auth et permettre à tous les composants d'accéder à nos fonctions et variables d'authentification.

Voici notre composant utilitaire `authcheck.js`:

```jsx
import React, { useEffect, useContext } from 'react';
import history from './history';
import Context from './context';
import * as ACTIONS from '../store/actions/actions';



const AuthCheck = () => {
  const context = useContext(Context)

  useEffect(() => {
    if(context.authObj.isAuthenticated()) {
      context.handleUserLogin()
      context.handleUserAddProfile(context.authObj.userProfile)
      history.replace('/')
    }
    else {
      context.handleUserLogout()
      context.handleUserRemoveProfile()
      history.replace('/')
      }
    }, [])

    return(
        <div>
        </div>
    )}




export default AuthCheck;

```

Ce composant est essentiellement la façon dont nous mettons à jour l'état d'authentification en utilisant le hook `useEffect()`. 

Ce composant sera rendu à chaque fois qu'un utilisateur se connecte et se déconnecte. Avoir un composant rendu après chaque connexion et déconnexion nous évitera d'avoir à gérer et mettre à jour l'état d'authentification du contexte dans chaque composant.

Dans notre composant `AuthCheck`, nous commençons par configurer le hook `useContext()`. Ensuite, nous définissons une instruction conditionnelle pour vérifier si la fonction `isAuthenticated()` que nous avons configurée dans la classe Auth retourne vrai, indiquant que les jetons d'authentification dans le stockage local n'ont pas expiré et que l'utilisateur est toujours authentifié. 

Et nous accédons à cette fonction avec la syntaxe `context.authObj.isAuthenticated`. 

Et nous pouvons faire cela parce que nous avons passé toute la classe `Auth` comme une propriété appelée `authObj` à la prop `value` dans Context. 

Si `isAuthentciated()` est vrai, nous appelons nos propriétés pour changer notre **état de connexion** à vrai et sauvegarder les **données de profil utilisateur** dans l'état global.  

Si un utilisateur se déconnecte, nous faisons le contraire. 

Nous retournons une div vide puisque nous mettons simplement à jour l'état et n'avons pas besoin d'afficher quoi que ce soit dans l'UI. Un écran de chargement serait bien ici, mais c'est pour un autre tutoriel.

Mais c'est tout, nous avons terminé la configuration de notre état global et de notre système d'authentification, nous pouvons maintenant configurer nos composants React Hooks.

## Composants React Hooks

Tout d'abord, nous commencerons par notre composant **callback.js**

```jsx
import React from 'react'

const Callback = props => (
    <div>
      Callback
    </div>
);

export default Callback;

```

Ce composant est celui vers lequel l'utilisateur est redirigé après s'être connecté avec Auth0. De là, l'utilisateur est redirigé vers la page authcheck puis vers la page d'accueil

### Header.js

```jsx
import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import Context from '../utils/context';

const Header = () => {
  const context = useContext(Context)

    return(
        <div>
          <Link to='/' style={{padding: '5px'}}>
            Accueil
          </Link>
          <Link to='/profile' style={{padding: '5px'}}>
            Profil
          </Link>
          <Link to='/hooksform' style={{padding: '5px'}}>
            Formulaire Hooks
          </Link>
          <Link to='/hookscontainer' style={{padding: '5px'}}>
            Conteneur Hooks
          </Link>
          <Link to='/privateroute' style={{padding: '5px'}}>
            Route Privée
          </Link>
          {!context.authState
            ? <button onClick={() => context.authObj.login()}>Connexion</button>
            : <button onClick={() => context.authObj.logout()}>Déconnexion</button>
          }
        </div>
  )};


export default Header;
```

Ici, nous avons des liens vers tous nos composants. Nous avons également une expression ternaire qui affiche soit un bouton de connexion soit un bouton de déconnexion selon que l'utilisateur est authentifié ou non.

### home.js

```jsx
import React from 'react'

const Home = props => (
    <div>
      Accueil
    </div>
);

export default Home;

```

Un simple composant home.js

### hooks1.js

```jsx
import React, { useContext, useState, useEffect, useReducer } from 'react';
import * as ACTIONS from '../store/actions/actions';
import * as Reducer1 from '../store/reducers/plain_reducer';
import Context from '../utils/context';


const HooksContainer1 = () => {
  const context = useContext(Context)

  const [value, setValue] = useState(0)

  const [useEffectValue, setUseEffectValue] = useState(null)

  const [state, dispatch] = useReducer(Reducer1.Reducer1, Reducer1.initialState)

  useEffect(() => {
      setTimeout(() => setUseEffectValue("useEffect a fonctionné"), 3000 );
  }, [value])

  const incrementValue = () => {
    setValue(value + 1 )
  }

  const decrementValue = () => {
    setValue(value - 1 )
  }

  const handleuseEffectValue = () => {
    setUseEffectValue("une chaîne de caractères")
  }

  const handleDispatchTrue = () => {
    //    dispatch2(type: "SUCCESS")
    //    dispatch2(ACTIONS.SUCCESS)
    dispatch(ACTIONS.success())
  }

  const handleDispatchFalse = () => {
    //     dispatch2(type: "FAILURE")
    //    dispatch2(ACTIONS.FAILURE)
    dispatch(ACTIONS.failure())
  }

  return (
    <div>
      <div>
      <button onClick={() => handleuseEffectValue()}> Gérer la valeur  </button>
      <button onClick={() => handleDispatchTrue()}>Dispatch True </button>
      <button onClick={() => handleDispatchFalse()}>Dispatch False </button>
      <button onClick={() => context.dispatchContextTrue()}>Dispatch Context True </button>
      <button onClick={() => context.dispatchContextFalse()}>Dispatch Context False </button>
      <button onClick={() => incrementValue()}> Ajouter une valeur locale </button>
      <button onClick={() => decrementValue()}> Décrémenter la valeur locale </button>
      <br />
      <br />
      {context.useContextSubmitState
        ? <h3> {context.useContextSubmitState} </h3>
        : <h3> Aucun texte utilisateur </h3>
      }
      <br />
      {state.stateprop1
        ? <p> stateprop1 est vrai </p>
        : <p> stateprop1 est faux </p>
      }
      <br />
      {context.stateProp2
        ? <p> stateprop2 est vrai </p>
        : <p> stateprop2 est faux </p>
      }
      <br />
      {useEffectValue
        ? <p> { useEffectValue }</p>
        : <p> Aucune valeur </p>
      }
      <br />
      <p>Valeur locale : {value}</p>
      <br />
      <br />
      </div>
    </div>
  )
}

export default HooksContainer1;
```

J'ai créé ce composant comme un modèle pour avoir toutes les façons de lire et de mettre à jour l'état dans un seul composant. Cela rend beaucoup plus facile de voir les différences de syntaxe.

**`incrementValue`** et **`decrementValue`** est la façon dont nous mettons à jour l'état local avec le hook `useState()`.

**`handleuseEffectValue`** est la façon dont nous mettons à jour la propriété `useEffectValue` de l'état local.

**`handleDispatchTrue`** et **`handleDispatchFalse`** est la façon dont nous envoyons nos actions pour changer notre `stateprop1` dans `Reducer1` de vrai à faux, et vice versa. Notez que cela reste un état local même si nous utilisons des réducteurs et des actions. 

**`handleContextDispatchTrue`** et **`handleContextDispatchFalse`** est la façon dont nous mettons à jour notre état global en utilisant les mêmes actions et réducteur que les fonctions `handleDispatchTrue` et `handleDispatchFalse`.

Dans notre JSX, nous voyons également que chaque fonction a son propre bouton.

**`context.useContextSubmitState`** est la façon dont nous affichons le texte d'un formulaire qui sauvegarde les valeurs dans l'état global, que nous verrons ensuite

**`state.stateprop1`** est la propriété `stateprop1` de l'`initialState` de `Reducer1` que nous avons configuré il y a un moment et `state` est le mot-clé défini par l'utilisateur du hook `useRedcuer` en haut. L'ensemble de l'`initialState` est contenu dans `state`. 

**`context.stateProp2`** est la valeur `stateprop2` que nous obtenons de notre état global de contexte.

**`useEffectValue`** est l'état local de l'appel du hook `useState`.

### hooks_form1.js

Ici, nous avons notre `hooks1_form.js` qui montre comment sauvegarder l'état d'un formulaire en utilisant les hooks `useReducer`, `useState` et `useContext`.

```jsx
import React, { useContext, useState, useReducer } from 'react';
import * as ACTIONS from '../store/actions/actions';
import * as FormReducer from '../store/reducers/form_reducer';
import Context from '../utils/context';


const HooksForm1 = () => {
  const context = useContext(Context)

  const [valueChange, setValueChange] = useState('')
  const [valueSubmit, setValueSubmit] = useState('')

  const [state, dispatch] = useReducer(FormReducer.FormReducer,
                                       FormReducer.initialState)


  const handleuseStateChange = (event) => (
    setValueChange(event.target.value)
  );

  const handleuseStateSubmit = (event) => {
    event.preventDefault();
    setValueSubmit(event.target.useState.value)
  };

  const handleuseReducerChange = (event) => (
    dispatch(ACTIONS.user_input_change(event.target.value))
  );

  const handleuseReducerSubmit = (event) => {
    event.preventDefault();
    dispatch(ACTIONS.user_input_submit(event.target.useReducer.value))
  };


    return (
      <div>
        <form onSubmit={handleuseStateSubmit}>
          <label> React useState: </label>
          <input id="useState" onChange={handleuseStateChange} type="text" />
          <button type="submit"> Soumettre </button>
        </form>
        <br />
        <form onSubmit={handleuseReducerSubmit}>
          <label> React useReducer: </label>
          <input id="useReducer" onChange={handleuseReducerChange} type="text" />
          <button type="submit"> Soumettre </button>
        </form>
        <br />
        <form onSubmit={context.useContextSubmit}>
          <label> React useContext: </label>
          <input id="useContext" onChange={context.useContextChange} type="text" />
          <button type="submit"> Soumettre </button>
        </form>
        <br />

        <h3>React useState:</h3>
        <p>Changement : {valueChange}</p>
        <p>Soumission : {valueSubmit}</p>
        
        <h3>React useReducer:</h3>
        <p>Changement : {state.user_textChange}</p>
        <p>Soumission : {state.user_textSubmit}</p>
        <br />
        <h3>React useContext:</h3>
        <p>Changement : {context.useContextChangeState}</p>
        <p>Soumission : {context.useContextSubmitState}</p>
        <br />
        <br />
      </div>
    )
}


export default HooksForm1;

```

Ce formulaire montre les trois façons de mettre à jour l'état et suit la même méthodologie exacte que nous avons vue dans le composant précédent.  

### privatecomponent.js

```jsx
import React from 'react'

const PrivateComponent = props => (
    <div>
      Composant Privé
    </div>
);

export default PrivateComponent;
```

Ce composant privé sera utilisé dans une route privée et ne sera accessible que par les utilisateurs authentifiés.

### profile.js

```jsx
import React, { useContext } from 'react';
import Context from '../utils/context';


const Profile = () => {
  const context = useContext(Context)


  const RenderProfile = (props) => {
    return(
      <div>
        <h1>{props.profile.profile.nickname}</h1>
        <br />
        <img src={props.profile.profile.picture} alt="" />
        <br />
        <h4> {props.profile.profile.email}</h4>
        <br />
        <h5> {props.profile.profile.name} </h5>
        <br />
        <h6> Email Verifié: </h6>
        {props.profile.profile.email_verified ? <p>Oui</p> : <p>Non</p> }
        <br />
      </div>
     )
   }


    return(
      <div>
        <RenderProfile profile={context.authObj.userProfile} />
      </div>
  )}



export default (Profile);
```

Ici, nous affichons les données du profil utilisateur. Les données du profil utilisateur sont disponibles depuis Auth0 et nous n'avons pas à les configurer manuellement. Nous obtenons ces données de profil utilisateur depuis notre `authObj` que nous avons passé à travers `context`.

## Routage

Avant de pouvoir configurer notre routage, nous devons d'abord configurer le fichier `history.js`, ce qui est heureusement très facile à faire.

```javascript
import { createBrowserHistory } from 'history'

export default createBrowserHistory()

```

Enfin, nous pouvons configurer notre routage :

```jsx
import React, { useContext, useEffect } from 'react';
import { Router, Route, Switch, Redirect } from 'react-router';
import history from './utils/history';
import Context from './utils/context';
import AuthCheck from './utils/authcheck';

import Home from './hooks/home';
import Header from './hooks/header';
import HooksContainer1 from './hooks/hook1';
import Callback from './hooks/callback';
import HooksForm from './hooks/hooks_form1';
import PrivateComponent from './hooks/privatecomponent';
import Profile from './hooks/profile';



const PrivateRoute = ({component: Component, auth }) => (
  <Route render={props => auth === true
    ? <Component auth={auth} {...props} />
    : <Redirect to={{pathname:'/'}} />
  }
  />
)



const Routes = () => {
    const context = useContext(Context)


      return(
        <div>
          <Router history={history} >
          <Header />
          <br />
          <br />
          <div>
            <Switch>
              <Route exact path='/' component={Home} />
              <Route path='/hooksform' component={HooksForm} />
              <Route path='/profile' component={Profile} />
              <Route path='/hookscontainer' component={HooksContainer1} />
              <Route path='/authcheck' component={AuthCheck} />

              <PrivateRoute path='/privateroute'
                            auth={context.authState}
                            component={PrivateComponent} />
              <PrivateRoute path="/profile"
                            auth={context.authState}
                            component={Profile} />
              <Route path='/callback'
					 render={(props) => {
                         context.handleAuth(props);                                                            return <Callback />}} />


            </Switch>
          </div>
          </Router>
        </div>
  )}

export default Routes;
```

Nous commençons par importer tous nos fichiers utilitaires et composants. Et aussi les composants Router de React Router.

Nous avons ensuite un composant d'ordre supérieur `PrivateRoute` qui sera responsable de nos routes privées.

Un **HOC** prend un composant et retourne un autre composant. Ici, nous passons un composant et retournons soit un composant `<Route />` soit un composant `<Redirect />` en fonction de l'état d'authentification de l'utilisateur. Nous vérifions l'état d'authentification à l'intérieur de notre prop `render` avec une expression ternaire.  

Ensuite, nous avons notre fonctionnalité Router réelle. Nous commençons par notre composant principal `<Router />` qui enveloppera toutes nos routes et notre en-tête.

Nous voulons toujours que l'en-tête soit affiché, nous le mettrons donc bien sûr à l'extérieur du composant `<Switch />`. Notre composant `<Switch />` enveloppera ensuite toutes nos routes. Nous pouvons définir les routes et les composants en utilisant les props `path` et `component` du composant `<Route />`.

Notre composant `<PrivateRoute />` est un peu différent. Nous devons spécifier les props `path` et `component` comme nous l'avons fait pour le `<Route />` régulier, mais nous devons également créer une prop `auth` qui contient l'état d'authentification de l'utilisateur. Nous obtenons cette valeur de notre état global de contexte que nous avons vu dans la section d'authentification, mais en gros cette prop `auth` contient la valeur de la propriété `is_authenticated` de notre `AuthReducer` de l'état global.

Enfin, nous avons notre route `/callback` qui est configurée un peu différemment. Puisque c'est le composant vers lequel Auth0 redirige, nous devons appeler la fonction `handleAuth()` ici, mais nous devons également rendre le composant `<Callback />`. 

Nous contournons cela en appelant 2 fonctions dans la prop `render`, ce que nous pouvons faire en enveloppant le corps de la fonction fléchée dans des accolades `{}` et en séparant chaque fonction par un point-virgule `;`.

Assurez-vous également d'envelopper toutes les routes avec le `<Context.Provider />`

```jsx
//context_state_config.js
...    
     <Context.Provider>
    	 <Routes />
     </Context.Provider>
      
 ...     
```

Envelopper toutes les routes avec le `<Context.Provider />` est essentiellement la façon dont l'état est transmis à tous les composants, et devient global.

### App.js

```jsx
import React from 'react';
import ContextState from './context_state_config';

const App = () => {

    return(
      <div>
     	 <ContextState />
      </div>
    )
}

export default App;
```

Maintenant, la seule chose qu'il nous reste à faire est d'importer notre composant `<ContextState />` dans notre fichier `App.js` pour terminer notre application.

Et nous avons terminé ! Merci d'avoir lu. 

> Connectez-vous avec moi sur Twitter pour plus de mises à jour sur les futurs tutoriels : [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf)