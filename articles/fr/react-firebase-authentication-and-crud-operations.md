---
title: Tutoriel d'authentification React – Comment configurer l'authentification avec
  Firebase V9 et React Router V6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-10T16:22:43.000Z'
originalURL: https://freecodecamp.org/news/react-firebase-authentication-and-crud-operations
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Logout-and-Private-Routes-using-React-and-FIrebase.png
tags:
- name: authentication
  slug: authentication
- name: Firebase
  slug: firebase
- name: React
  slug: react
seo_title: Tutoriel d'authentification React – Comment configurer l'authentification
  avec Firebase V9 et React Router V6
seo_desc: "By Nishant Kumar\nHey everyone, in this tutorial we'll use React with Firebase\
  \ V9 to setup authentication for an application. \nWe will create Firebase functions\
  \ for Login and Register, we will add toast messages for errors, and we will add\
  \ private rou..."
---

Par Nishant Kumar

Salut à tous, dans ce tutoriel, nous allons utiliser React avec Firebase V9 pour configurer l'authentification pour une application. 

Nous allons créer des fonctions Firebase pour la connexion et l'inscription, nous allons ajouter des messages toast pour les erreurs, et nous allons ajouter des routes privées en utilisant l'authentification basée sur les sessions. Ce sera amusant.

Nous allons utiliser les packages ou dépendances suivants :

1. Firebase V9.
2. React Router V6.
3. Material UI.
4. React Toastify.

Alors, commençons.

## Comment configurer le projet 

Commençons par créer une application React. Assurez-vous d'avoir Node installé, mais si ce n'est pas le cas, installez-le depuis [https://nodejs.org/en/download/](https://nodejs.org/en/download/).

Pour créer une application React, nous allons utiliser la commande suivante :

```
npx create-react-app react-firebase-v9
```

Ensuite, allez dans le dossier du projet et tapez npm start pour démarrer le projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-181635.png)

Nous verrons cet écran. Mais nettoyons-le pour le formulaire de connexion et d'inscription.

## Comment créer le formulaire de connexion et d'inscription

Pour ces formulaires, installons Material UI. Rendez-vous sur [https://mui.com/](https://mui.com/) pour lire la documentation.

Pour l'installer, utilisez simplement la commande suivante :

```
// avec npm
npm install @mui/material @emotion/react @emotion/styled

// avec yarn
yarn add @mui/material @emotion/react @emotion/styled
```

Pendant ce temps, créons un dossier à l'intérieur du dossier src, qui s'appellera `components`. Et à l'intérieur de ce composant, nous créerons un autre dossier appelé `common`. Cela contiendra tous nos composants communs que nous utiliserons, comme `Forms`, `Buttons`, et ainsi de suite.

Créez un fichier appelé `Form.js` à l'intérieur du dossier common. Faites-en un composant fonctionnel. Nous utiliserons Form de Material UI. 

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Select-this.-1.png)

Sélectionnez ce champ de texte pour obtenir les champs de saisie, et choisissez le type de champ de saisie que vous voulez.

```
import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

export default function BasicTextFields() {
    return (
        <Box
            component="form"
            sx={{
                '& > :not(style)': { m: 1, width: '25ch' },
            }}
            noValidate
            autoComplete="off"
        >
            <TextField id="outlined-basic" label="Outlined" variant="outlined" />
        </Box>
    );
}

```

Ensuite, importez ce composant dans le fichier `App.js` :

```
import './App.css';
import Form from './Components/Common/Form'

function App() {
  return (
    <div className="App">
      <Form />
    </div>
  );
}

export default App;

```

Voici ce que nous verrons :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-182936.png)

Maintenant, créons nos formulaires de connexion et d'inscription. Nous utiliserons un seul composant, mais les données seront différentes. Et nous passerons les données en tant que props. 

Créons également un titre de formulaire comme ceci :

```
import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';

export default function BasicTextFields() {
    return (
        <div>
            <div className="heading-container">
                <h3>
                    Formulaire de connexion
                </h3>
            </div>

            <Box
                component="form"
                sx={{
                    '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
            >
                <TextField id="email" label="Entrez l'email" variant="outlined" />
                <TextField id="password" label="Entrez le mot de passe" variant="outlined" />
            </Box>
        </div>
    );
}

```

Le titre du formulaire est statique pour l'instant, mais nous allons le changer via les props.

Maintenant, ajoutons un bouton pour effectuer certaines actions – connexion et inscription dans notre cas.

Créez un composant appelé `Button.js` dans le dossier common. 

```
import * as React from 'react';
import Button from '@mui/material/Button';

export default function BasicButtons() {
    return (
        <Button variant="contained">Se connecter</Button>
    );
}

```

Et importez-le dans Form.js comme ceci :

```
import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from './Button';
export default function BasicTextFields() {
    return (
        <div>
            <div className="heading-container">
                <h3>
                    Formulaire de connexion
                </h3>
            </div>

            <Box
                component="form"
                sx={{
                    '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
            >
                <TextField id="email" label="Entrez l'email" variant="outlined" />
                <TextField id="password" label="Entrez le mot de passe" variant="outlined" />
            </Box>

            <Button />
        </div>
    );
}

```

Ici, dans Form.js, nous avons deux champs – Email et Mot de passe. Nous avons également un bouton pour déclencher la connexion et l'inscription, selon le scénario.

Et voici à quoi ressemble notre interface utilisateur :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-184136.png)

## Comment créer une application Firebase

Maintenant, installons quelques éléments supplémentaires dont nous avons besoin – React Router et Firebase. Mais avant d'installer ces deux éléments, nous devons créer un projet dans Firebase.

Alors, rendez-vous sur [https://firebase.google.com/](https://firebase.google.com/) et créez un projet.

Cliquez sur "Ajouter un projet" dans la console Firebase.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-184523.png)

Après avoir créé un nouveau projet dans Firebase, vous devez créer une application.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-184708.png)

Cliquez sur Ajouter une application, et choisissez Web. 

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-184807.png)

Donnez un nom à l'application de votre choix, et enregistrez l'application.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-184906.png)

Vous verrez l'écran ci-dessus. Et nous avons besoin d'un fichier où nous pouvons stocker toutes ces données de configuration, alors nous allons créer ce fichier.

Créez un fichier appelé `firebase-config.js` et stockez toutes ces données de configuration dans ce fichier.

```
import { initializeApp } from "firebase/app";

const firebaseConfig = {
    apiKey: "AIzaSyBtRIMLkSVfptH4ASinlEfnKhP-mBwUV24",
    authDomain: "react-register-12564.firebaseapp.com",
    projectId: "react-register-12564",
    storageBucket: "react-register-12564.appspot.com",
    messagingSenderId: "1074586181097",
    appId: "1:1074586181097:web:47236fd450006cd1fabf78",
    measurementId: "G-JSN76LC2EC"
};

export const app = initializeApp(firebaseConfig);

```

Maintenant, installons React Router et Firebase en utilisant la commande suivante.

```
npm install firebase react-router-dom
```

## Comment créer des routes pour les écrans d'inscription et de connexion

Et maintenant, nous devons créer des routes séparées pour les écrans d'inscription et de connexion.

Dans le fichier App.js, importez `BrowerRouter` en tant que Router et enveloppez toute la div à l'intérieur du Router comme ceci :

```
import './App.css';
import Form from './Components/Common/Form'
import { BrowserRouter as Router } from 'react-router-dom'

function App() {
  return (
    <Router>
      <div className="App">
        <Form />
      </div>
    </Router>
  );
}

export default App;

```

En faisant cela, nous nous assurons que toute notre application pourra maintenant utiliser des routes, car nous ajoutons ce Router au niveau racine.

Maintenant, créons des routes pour les pages de connexion et d'inscription.

```
import './App.css';
import Form from './Components/Common/Form'
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <>
          <Routes>
            <Route path='/login' element={<Form />} />
            <Route path='/register' element={<Form />} />
          </Routes>
        </>
      </div>
    </Router>
  );
}

export default App;

```

Si nous allons à la route `/login` dans la barre d'adresse, nous verrons la page de connexion. Et sur `/register`, nous verrons la page d'inscription.

Ici, nous utilisons le même composant Form pour la connexion et l'inscription. Passons des props au composant pour en faire des écrans de connexion et d'inscription.

```
import './App.css';
import Form from './Components/Common/Form'
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <>
          <Routes>
            <Route path='/login' element={<Form title="Login" />} />
            <Route path='/register' element={<Form title="Register" />} />
          </Routes>
        </>
      </div>
    </Router>
  );
}

export default App;

```

Et nous recevrons les props dans le composant Form.js, en tant que titre dans les paramètres de la fonction.

Ensuite, utilisez le titre pour définir quel composant est lequel. Donc, remplacez le formulaire de connexion par le formulaire **`{{title}}`**. Et le titre du bouton aussi.

```
import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from './Button';
export default function BasicTextFields({title}) {
    return (
        <div>
            <div className="heading-container">
                <h3>
                    {title} Form
                </h3>
            </div>

            <Box
                component="form"
                sx={{
                    '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
            >
                <TextField id="email" label="Enter the Email" variant="outlined" />
                <TextField id="password" label="Enter the Password" variant="outlined" />
            </Box>

            <Button title={title}/>
        </div>
    );
}

```

Nous passons les props dans le composant Button. Et nous les recevrons dans le composant Button.

```
import * as React from 'react';
import Button from '@mui/material/Button';

export default function BasicButtons({title}) {
    return (
        <Button variant="contained">{title}</Button>
    );
}

```

Maintenant, si nous allons à `/login`, nous verrons l'écran de connexion comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-193109.png)

Et sur `/register` nous verrons l'écran d'inscription :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-193147.png)

## Comment stocker les données dans les états

Maintenant, créons les états pour les champs de saisie qui stockeront nos données de formulaire. 

Dans le fichier App.js, créez deux états – email et mot de passe – en utilisant le hook useState.

```
import { useState } from 'react';

const [email, setEmail] = useState('');
const [password, setPassword] = useState('')
```

Dans le code ci-dessus, nous avons importé useState de React et créé deux états. Ensuite, nous avons passé les fonctions `setEmail` et `setPassword` au composant Form.

```
<Routes>
            <Route
              path='/login'
              element={
                <Form
                  title="Login"
                  setEmail={setEmail}
                  setPassword={setPassword} />}
            />
            <Route
              path='/register'
              element={
                <Form
                  title="Register"
                  setEmail={setEmail}
                  setPassword={setPassword} />}
            />
          </Routes>
```

Et dans le composant Form.js, nous définirons l'email et le mot de passe en utilisant l'événement `onChange`. Maintenant, vous savez comment fonctionnent les props dans React.

Maintenant, nous avons besoin d'une fonction pour déclencher la fonctionnalité de connexion ou d'inscription, alors créons-la.

```
const handleAction = () => {
    
}
```

Et passez cette fonction dans le composant Form en tant que props. 

```
<Routes>
            <Route
              path='/login'
              element={
                <Form
                  title="Login"
                  setEmail={setEmail}
                  setPassword={setPassword}
                  handleAction={() => handleAction()}
                />}
            />
            <Route
              path='/register'
              element={
                <Form
                  title="Register"
                  setEmail={setEmail}
                  setPassword={setPassword}
                  handleAction={() => handleAction()}
                />}
            />
          </Routes>
```

Et comme avant, recevez-la dans le composant Form.js.

```
import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from './Button';
export default function BasicTextFields({ title, setPassword, setEmail, handleAction }) {
    return (
        <div>
            <div className="heading-container">
                <h3>
                    {title} Form
                </h3>
            </div>

            <Box
                component="form"
                sx={{
                    '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
            >
                <TextField
                    id="email"
                    label="Enter the Email"
                    variant="outlined"
                    onChange={(e) => setEmail(e.target.value)}
                />
                <TextField
                    id="password"
                    label="Enter the Password"
                    variant="outlined"
                    onChange={(e) => setPassword(e.target.value)}
                />
            </Box>

            <Button title={title} />
        </div>
    );
}

```

Et passez ensuite le `handleAction` dans le composant Button en tant que props.

```
<Button title={title} handleAction={handleAction}/>
```

Et recevez-le dans le composant Button.js.

```
import * as React from 'react';
import Button from '@mui/material/Button';

export default function BasicButtons({title, handleAction}) {
    return (
        <Button variant="contained" onClick={handleAction}>{title}</Button>
    );
}

```

Ainsi, lorsqu'un utilisateur clique sur le bouton de connexion ou d'inscription, cela déclenchera la fonction `handleAction`.

Maintenant, revenez au fichier App.js, dans la fonction handleAction. Nous devons déterminer quelle action nous allons entreprendre, qu'il s'agisse de la connexion ou de l'inscription. Nous devons donc passer un identifiant unique pour la connexion et l'inscription, en tant que paramètres de fonction. 

Supposons que nous passons '1' pour la connexion et '2' pour l'inscription.

```
<Routes>
            <Route
              path='/login'
              element={
                <Form
                  title="Login"
                  setEmail={setEmail}
                  setPassword={setPassword}
                  handleAction={() => handleAction(1)}
                />}
            />
            <Route
              path='/register'
              element={
                <Form
                  title="Register"
                  setEmail={setEmail}
                  setPassword={setPassword}
                  handleAction={() => handleAction(2)}
                />}
            />
          </Routes>
```

Et dans la fonction, recevons-le. Nous vérifierons également dans la console quelle sortie nous obtenons.

```
const handleAction = (id) => {
    console.log(id)
  }
```

Alors, remplissez le formulaire et cliquez sur le bouton. Nous obtiendrons '1' dans la console si nous sommes sur l'écran de connexion, et '2' si nous sommes sur l'écran d'inscription.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-201657.png)

Maintenant, notre formulaire est prêt.

## Comment utiliser les fonctions Firebase pour se connecter et s'inscrire

Pour utiliser les fonctions Firebase, nous devons importer notre fichier `firebase-config` dans App.js.

```
import { app } from './firebase-config';
```

Maintenant, nous avons besoin de quelques autres choses. Alors, importons-les :

```
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword } from 'firebase/auth'
```

Nous utilisons `getAuth` pour l'authentification. Et nous utilisons `signInWithEmailAndPassword` et `createUserWithEmailAndPassword` pour nous connecter et nous inscrire en utilisant l'email et le mot de passe, respectivement.

Dans la console Firebase, allez à Authentication, puis à Sign in Method, et activez la méthode Email/Mot de passe.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-202403.png)

Maintenant, nous devons déstructurer le `getAuth` que nous avons importé. Alors, dans la fonction `handleAction`, faisons-le.

```
 const handleAction = (id) => {
    const authentication = getAuth();
  }
```

Maintenant, créons un utilisateur en utilisant la fonction `createUserWithEmailAndPassword`.

Elle prendra trois paramètres – authentication, l'état de l'email, et l'état du mot de passe – que nous avons créés précédemment.

```
const handleAction = (id) => {
    const authentication = getAuth();

    createUserWithEmailAndPassword(authentication, email, password)
}
```

Maintenant, nous devons créer une vérification en utilisant le paramètre id. Si c'est '1', nous déclencherons la fonction de connexion, et si c'est '2', nous déclencherons la fonction d'inscription. 

Nous avons créé la fonction d'inscription en premier, donc nous utiliserons '2' pour l'id.

```
const handleAction = (id) => {
    const authentication = getAuth();
    if (id === 2) {
      createUserWithEmailAndPassword(authentication, email, password)
    }
 }
```

Maintenant, pour vérifier si toute cette opération fonctionne ou non, nous utiliserons une instruction `then` – c'est-à-dire une promesse.

```
const handleAction = (id) => {
    const authentication = getAuth();
    if (id === 2) {
      createUserWithEmailAndPassword(authentication, email, password)
        .then((response) => {
          console.log(response)
      })
   }
}
```

Maintenant, remplissez l'email et le mot de passe, et cliquez sur le bouton d'inscription.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-203439.png)

Vous voyez que nous obtenons une tonne de données dans notre console. Et si vous vérifiez les utilisateurs Firebase, vous verrez l'email que nous avons utilisé lors de la création du compte.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-203554.png)

Et si nous essayons de créer un compte avec le même email, nous obtiendrons une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-203723.png)

## Comment stocker le jeton dans le stockage de session

Maintenant, stockons la réponse du jeton dans le stockage de session. Nous faisons cela parce que nous allons créer des routes privées maintenant. 

Donc, si ce jeton existe dans le stockage de session, nous serons sur cette route privée, disons une page d'accueil. Mais si le jeton n'existe pas, nous serons renvoyés à l'écran d'inscription ou de connexion.

J'ai choisi le stockage de session parce qu'il est détruit lorsque le navigateur est fermé.

```
const handleAction = (id) => {
    const authentication = getAuth();
    if (id === 2) {
      createUserWithEmailAndPassword(authentication, email, password)
        .then((response) => {
          sessionStorage.setItem('Auth Token', response._tokenResponse.refreshToken)
        })
    }
  }
```

Définissez-le comme ceci dans le stockage de session.

Ensuite, créez un composant appelé Home.js, et donnez-lui un titre ou un texte.

```
import React from 'react'

export default function Home() {
    return (
        <div>
            Page d'accueil
        </div>
    )
}

```

Ensuite, si nous nous inscrivons avec succès, nous devrions être sur le composant Home. Et pour cela, nous utiliserons `useNavigate` de React Router.

```
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate 
} from "react-router-dom";
```

```
const navigate = useNavigate();


```

Et la navigation dans la fonction `handleAction`.

```
navigate('/home')
```

Mais avant cela, nous devons apporter quelques modifications. Puisque nous utilisons React Router v6, nous ne pouvons pas utiliser `useNavigate` dans la configuration actuelle, car useNavigate doit également être dans Routes. Donc, déplacez les routes dans le fichier index.js.

```
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {
  BrowserRouter as Router,
} from "react-router-dom";
ReactDOM.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

```

Et maintenant, configurons la route pour la page d'accueil.

```
<Route
            path='/home'
            element={
              <Home />}
          />
```

Voici le fichier App.js complet à ce stade : 

```
import { useState } from 'react';
import './App.css';
import Form from './Components/Common/Form';
import Home from './Components/Home';
import {
  Routes,
  Route,
  useNavigate
} from "react-router-dom";
import { app } from './firebase-config';
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword } from 'firebase/auth'
function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  let navigate = useNavigate();
  const handleAction = (id) => {
    const authentication = getAuth();
    if (id === 2) {
      createUserWithEmailAndPassword(authentication, email, password)
        .then((response) => {
          navigate('/home')
          sessionStorage.setItem('Auth Token', response._tokenResponse.refreshToken)
        })
    }
  }
  return (
    <div className="App">
      <>
        <Routes>
          <Route
            path='/login'
            element={
              <Form
                title="Login"
                setEmail={setEmail}
                setPassword={setPassword}
                handleAction={() => handleAction(1)}
              />}
          />
          <Route
            path='/register'
            element={
              <Form
                title="Register"
                setEmail={setEmail}
                setPassword={setPassword}
                handleAction={() => handleAction(2)}
              />}
          />

          <Route
            path='/home'
            element={
              <Home />}
          />
        </Routes>
      </>
    </div>
  );
}

export default App;

```

Allez à la route Home en utilisant la barre d'adresse. Vous verrez ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-210037.png)

Maintenant, essayez de vous inscrire en utilisant un email et un mot de passe différents. Vous serez redirigé vers la page d'accueil.

## Comment créer la fonctionnalité des routes privées

Mais le problème est que les routes de la page d'accueil ne sont pas privées. Alors, changeons cela. Nous utiliserons le jeton stocké dans le stockage de session.

Dans le composant Home.js, créez un hook `useEffect`. useEffect est une fonction qui s'exécute chaque fois que notre composant se charge ou se monte.

```
import React, { useEffect } from 'react'

export default function Home() {
    useEffect(() => {
        
    }, [])
    return (
        <div>
            Page d'accueil
        </div>
    )
}

```

Et à l'intérieur de useEffect, nous créerons une vérification de jeton.

```
import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

export default function Home() {
    let navigate = useNavigate();
    useEffect(() => {
        let authToken = sessionStorage.getItem('Auth Token')

        if (authToken) {
            navigate('/home')
        }

        if (!authToken) {
            navigate('/login')
        }
    }, [])
    return (
        <div>
            Page d'accueil
        </div>
    )
}

```

Si le jeton existe, nous resterons sur la page d'accueil. Sinon, nous serons renvoyés à l'écran de connexion, sauf si nous trouvons un moyen de détruire le jeton.

Maintenant, nous créerons la même vérification dans le fichier App.js.

```
useEffect(() => {
    let authToken = sessionStorage.getItem('Auth Token')

    if (authToken) {
      navigate('/home')
    }
  }, [])
```

Essayez de revenir à la route `/register` après vous être inscrit avec succès. Vous serez renvoyé à la page `/home` (et vice versa pour `/home` à `/register`).

## Comment créer la fonctionnalité de connexion

Et maintenant, créons la fonctionnalité de connexion. C'est très simple. Tout comme nous l'avons fait avec `createUserWithEmailAndPassword`, nous utiliserons la fonction `signInWithEmailAndPassword`.

```
if (id === 1) {
      signInWithEmailAndPassword(authentication, email, password)
        .then((response) => {
          navigate('/home')
          sessionStorage.setItem('Auth Token', response._tokenResponse.refreshToken)
        })
    }
```

Si l'id est '1', cette fonction sera déclenchée.

Essayons de nous connecter en utilisant l'email et le mot de passe que nous avons utilisés lors de l'inscription. Vous verrez que nous sommes sur la page d'accueil.

## Comment gérer les erreurs en utilisant le bloc Catch et React Toastify

Si nous essayons de nous connecter avec un email ou un mot de passe incorrect, nous obtiendrons des erreurs.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-213046.png)

Alors, gérons ces erreurs en utilisant un bloc `catch`.

Tout d'abord, gérons les erreurs de la méthode d'inscription. Et nous allons utiliser un autre package pour gérer les messages d'erreur toast appelé React Toastify. Installez-le en utilisant cette commande :

```
npm i react-toastify
```

Ensuite, créez un bloc catch dans les deux fonctions, qui sont Login et Register.

```
.catch((error) => {
         console.log(error)
})
```

Tout d'abord, essayez de saisir le mauvais email et le mauvais mot de passe. Vous obtiendrez cette erreur :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-214356-1.png)

Et si l'ID de l'email est correct, mais que le mot de passe est incorrect, vous obtiendrez cette erreur :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-214322-1.png)

Maintenant, ajoutons les messages toast pour nos erreurs.

Tout d'abord, nous devons importer quelques éléments :

```
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
```

Ensuite, ajoutez le `<ToastContainer />` dans le retour de la fonction.

Maintenant, nous vérifierons quel est le code d'erreur. Si c'est `auth/wrong-password`, nous afficherons une erreur toast de **Veuillez vérifier le mot de passe.** 

Ou si c'est `auth/user-not-found`, nous afficherons l'erreur **Veuillez vérifier l'email.**

```
.catch((error) => {
          if(error.code === 'auth/wrong-password'){
            toast.error('Veuillez vérifier le mot de passe');
          }
          if(error.code === 'auth/user-not-found'){
            toast.error('Veuillez vérifier l\'email');
          }
        })
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-215839.png)
_Erreur pour un email incorrect_

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-215922.png)
_Erreur pour un mot de passe incorrect_

Nous pouvons faire de même pour la fonction d'inscription. Si nous essayons de nous inscrire avec le même email deux fois, cela nous renverra cette erreur :

```
.catch((error) => {
          if (error.code === 'auth/email-already-in-use') {
            toast.error('Email déjà utilisé');
          }
        })
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-220420-1.png)

## Comment créer la fonctionnalité de déconnexion

Créons la fonctionnalité qui permet aux utilisateurs de se déconnecter.

Dans le composant Home, créez un bouton. Et créez une fonction appelée `handleLogout`.

Attribuez un événement `onClick` au bouton, avec la fonction `handleLogout`. Ainsi, lorsque quelqu'un clique sur le bouton, ce bouton sera déclenché.

Et dans le corps de la fonction, nous ne ferons rien sauf détruire le jeton de la session, et cela nous renverra à la page de connexion.

```
import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

export default function Home() {
    const handleLogout = () => {
        sessionStorage.removeItem('Auth Token');
        navigate('/login')
    }
    let navigate = useNavigate();
    useEffect(() => {
        let authToken = sessionStorage.getItem('Auth Token')
        console.log(authToken)
        if (authToken) {
            navigate('/home')
        }

        if (!authToken) {
            navigate('/register')
        }
    }, [])
    return (
        <div>
            Page d'accueil

            <button onClick={handleLogout}>Se déconnecter</button>
        </div>
    )
}

```

Essayez-le pour vous assurer qu'il fonctionne – il devrait.

## **Conclusion**

Maintenant, vous savez comment ajouter l'authentification à une application React en utilisant Firebase.

Vous pouvez consulter ma playlist sur le même sujet à l'adresse [Firebase Authentication and CRUD Operations using React](https://www.youtube.com/playlist?list=PLWgH1O_994O8B_HVG2iuyqBEWPGa5Lhoj), qui se trouve sur ma chaîne YouTube.

Et voici le code complet sur [GitHub](https://github.com/nishant-666/React-Firebase-Auth-V2) pour référence.

> Bon apprentissage.