---
title: Comment utiliser l'authentification Firebase dans une application React
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-10-31T14:54:20.000Z'
originalURL: https://freecodecamp.org/news/use-firebase-authentication-in-a-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/ferenc-almasi-tvHtIGbbjMo-unsplash.jpg
tags:
- name: authentication
  slug: authentication
- name: Firebase
  slug: firebase
- name: React
  slug: react
seo_title: Comment utiliser l'authentification Firebase dans une application React
seo_desc: "Almost every web application requires some form of authentication. This\
  \ prevents unauthorized users from having access to the app's inner workings. \n\
  In this tutorial, you will learn how to authenticate your React app with the Firebase\
  \ SDK.\nHow to Aut..."
---

Presque toutes les applications web nécessitent une forme d'authentification. Cela empêche les utilisateurs non autorisés d'avoir accès au fonctionnement interne de l'application. 

Dans ce tutoriel, vous apprendrez à authentifier votre application React avec le SDK Firebase.

## Comment s'authentifier avec Firebase

L'authentification avec Firebase facilite les choses pour les utilisateurs finaux et les développeurs. Firebase Authentication fournit des services backend, des SDK faciles à utiliser et des bibliothèques d'interface utilisateur prêtes à l'emploi. Cela vous permet de vous concentrer sur vos utilisateurs, et non sur une infrastructure complexe pour les soutenir. 

Firebase prend en charge de nombreuses méthodes d'authentification pour les utilisateurs. Elles incluent l'authentification par adresse e-mail, des fournisseurs tiers tels que Twitter, Facebook, Github, Google, Microsoft, et bien plus encore.

## Comment configurer l'authentification Firebase

Avant de configurer et d'initialiser le SDK Firebase pour votre application React, vous devrez vous inscrire à Firebase en utilisant votre compte Google. 

Si vous avez déjà un compte Firebase, connectez-vous et suivez les invites pour créer un nouveau projet. Choisissez un nom approprié pour votre projet et cliquez sur **Continuer.**

Pour ce tutoriel, nous nommerons notre projet **Focus-app.** Votre écran suivant sera une invite pour activer Google Analytics. Nous n'en aurons pas besoin. Vous pouvez choisir de le désactiver.

Félicitations, vous avez réussi à configurer votre console Firebase. Votre écran suivant sera le tableau de bord de la console Firebase qui ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot--197-.png)

Il existe de nombreuses façons d'authentifier les utilisateurs en utilisant Firebase. Pour ce tutoriel, nous authentifierons nos utilisateurs avec leurs adresses e-mail et mots de passe. 

Pour commencer à utiliser l'authentification du SDK Firebase, sélectionnez le SDK d'authentification parmi les catégories **Build**.

Ensuite, nous configurerons notre méthode de connexion. Cliquez sur **Configurer la méthode de connexion** et sélectionnez **Email/Mot de passe** dans la liste des fournisseurs de connexion.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot--209--3.png)

Activez l'option **Email/Mot de passe** pour permettre aux utilisateurs de s'inscrire en utilisant leur adresse e-mail et leur mot de passe, puis cliquez sur **Enregistrer**.

## Comment configurer votre application React avec React Router

L'authentification est une fonctionnalité dont la plupart des applications ont besoin. Nous allons configurer notre application React en utilisant la commande suivante :

```js
$ npx create-react-app focus-app
```

Avant de démarrer notre application, nous devons configurer notre react-router-dom. Vous pouvez installer votre **react-router-dom** en exécutant la commande suivante :

```js
$ npm i -D react-router-dom
```

Pour configurer votre application React pour utiliser **react-router-dom**, vous pouvez lire leur [documentation](https://reactrouter.com/en/6.4.2/start/tutorial). Après avoir configuré vos routes, votre fichier app.js doit contenir le code suivant :

```js
import React, {useState, useEffect} from 'react';
import Home from './page/Home';
import Signup from './page/Signup';
import Login from './page/Login';
import { BrowserRouter as Router} from 'react-router-dom';
import {Routes, Route} from 'react-router-dom';
 
function App() {
 
  return (
    <Router>
      <div>
        <section>                              
            <Routes>                                                                        <Route path="/" element={<Home/>}/>
               <Route path="/inscription" element={<Signup/>}/>
               <Route path="/connexion" element={<Login/>}/>
            </Routes>                    
        </section>
      </div>
    </Router>
  );
}
 
export default App;
```

Nous avons configuré notre application React pour avoir trois routes : **Accueil**, **Connexion** et la page **Inscription**.

## Comment configurer et initialiser le SDK Firebase

Vous avez deux options pour configurer votre SDK Firebase. Nous allons installer et configurer Firebase en utilisant l'option **npm**. 

Avant d'installer le SDK Firebase, vous devez avoir [npm](https://nodejs.org/en/download/) installé sur votre machine. Vous pouvez installer le dernier SDK Firebase en exécutant la commande suivante :

```js
$ npm install firebase
```

Pour initialiser Firebase, créez un fichier **firebase.js** dans votre répertoire **src**. Obtenez votre configuration Firebase dans la partie paramètres du projet de votre tableau de bord et copiez votre configuration Firebase dans votre fichier **firebase.js**. Votre fichier **firebase.js** doit contenir le code suivant :

```js
// Importez les fonctions dont vous avez besoin depuis les SDK dont vous avez besoin
import { initializeApp } from "firebase/app";
// TODO: Ajoutez les SDK pour les produits Firebase que vous souhaitez utiliser
// https://firebase.google.com/docs/web/setup#available-libraries
// Configuration Firebase de votre application web

const firebaseConfig = {
  apiKey: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  authDomain: "XXXXXXXXXXXXXXXXXXXXXXXX",
  projectId: "XXXXXXXXX",
  storageBucket: "XXXXXXXXXXXXXXXXXX",
  messagingSenderId: "XXXXXXXXXXXX",
  appId: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
};

// Initialisez Firebase
const app = initializeApp(firebaseConfig);

```

Félicitations, vous avez réussi à initialiser Firebase. 

Pour commencer à utiliser le SDK Firebase, vous devrez importer les produits que vous souhaitez utiliser. Après avoir importé le SDK Firebase pour l'authentification, votre fichier **firebase.js** doit contenir le code suivant :

```js
// Importez les fonctions dont vous avez besoin depuis les SDK dont vous avez besoin
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// TODO: Ajoutez les SDK pour les produits Firebase que vous souhaitez utiliser
// https://firebase.google.com/docs/web/setup#available-libraries
// Configuration Firebase de votre application web

const firebaseConfig = {
  apiKey: "AIzaSyAAx_knJ_qqxPkJQ_xoIZnxt_c6gb6Wdys",
  authDomain: "todoapp-eeeb7.firebaseapp.com",
  projectId: "todoapp-eeeb7",
  storageBucket: "todoapp-eeeb7.appspot.com",
  messagingSenderId: "1072574112522",
  appId: "1:1072574112522:web:65fc4e184aed9894dc90f3"
};
 
// Initialisez Firebase
const app = initializeApp(firebaseConfig);

// Initialisez l'authentification Firebase et obtenez une référence au service
export const auth = getAuth(app);
export default app;
```

## Comment authentifier votre application React

Firebase dispose d'un certain nombre de produits intégrés, dont l'authentification. Selon sa [documentation](https://firebase.google.com/docs/auth),

> pour authentifier les utilisateurs de votre application, Firebase Authentication fournit des fonctionnalités intéressantes comme des services backend, des SDK faciles à utiliser et des bibliothèques d'interface utilisateur prêtes à l'emploi. 

Firebase Authentication permet aux utilisateurs de se connecter à votre application en utilisant différentes méthodes de connexion. Dans ce tutoriel, nous allons apprendre à authentifier les utilisateurs en utilisant leur adresse e-mail et leur mot de passe pour se connecter à votre application. Nous n'utiliserons aucun style pour cet article.

Pour créer un utilisateur, vous devez créer un formulaire qui prend des entrées et crée de nouveaux utilisateurs en utilisant la méthode **createUserWithEmailAndPassword** de Firebase. 

Le formulaire doit prendre l'adresse e-mail et le mot de passe du nouvel utilisateur comme entrée et les passer dans la méthode **createUserWithEmailAndPassword**. Si un utilisateur est créé avec succès, vous serez redirigé vers l'écran de connexion. 

Voici le code complet pour créer un utilisateur :

```js
import React, {useState} from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import {  createUserWithEmailAndPassword  } from 'firebase/auth';
import { auth } from '../firebase';
 
const Signup = () => {
    const navigate = useNavigate();
 
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('');
 
    const onSubmit = async (e) => {
      e.preventDefault()
     
      await createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Connecté
            const user = userCredential.user;
            console.log(user);
            navigate("/connexion")
            // ...
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.log(errorCode, errorMessage);
            // ..
        });
 
   
    }
 
  return (
    <main >        
        <section>
            <div>
                <div>                  
                    <h1> FocusApp </h1>                                                                            
                    <form>                                                                                            
                        <div>
                            <label htmlFor="email-address">
                                Adresse e-mail
                            </label>
                            <input
                                type="email"
                                label="Adresse e-mail"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}  
                                required                                    
                                placeholder="Adresse e-mail"                                
                            />
                        </div>

                        <div>
                            <label htmlFor="password">
                                Mot de passe
                            </label>
                            <input
                                type="password"
                                label="Créer un mot de passe"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)} 
                                required                                 
                                placeholder="Mot de passe"              
                            />
                        </div>                                             
                        
                        <button
                            type="submit" 
                            onClick={onSubmit}                        
                        >  
                            S'inscrire                                
                        </button>
                                                                     
                    </form>
                   
                    <p>
                        Vous avez déjà un compte ?{' '}
                        <NavLink to="/connexion" >
                            Se connecter
                        </NavLink>
                    </p>                   
                </div>
            </div>
        </section>
    </main>
  )
}
 
export default Signup

```

Firebase permet aux utilisateurs existants de se connecter en utilisant l'**e-mail** et le **mot de passe** qu'ils ont initialement utilisés pour l'inscription. 

Pour permettre aux utilisateurs existants de se connecter, vous devez créer un formulaire qui collecte à la fois leur e-mail et leur mot de passe. Le formulaire a un bouton de soumission qui appelle la méthode **signInWithEmailAndPassword** chaque fois qu'il est cliqué. 

Vous pouvez vous connecter en utilisant le code suivant :

```js
import React, {useState} from 'react';
import {  signInWithEmailAndPassword   } from 'firebase/auth';
import { auth } from '../firebase';
import { NavLink, useNavigate } from 'react-router-dom'
 
const Login = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
       
    const onLogin = (e) => {
        e.preventDefault();
        signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Connecté
            const user = userCredential.user;
            navigate("/accueil")
            console.log(user);
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.log(errorCode, errorMessage)
        });
       
    }
 
    return(
        <>
            <main >        
                <section>
                    <div>                                            
                        <p> FocusApp </p>                       
                                                       
                        <form>                                              
                            <div>
                                <label htmlFor="email-address">
                                    Adresse e-mail
                                </label>
                                <input
                                    id="email-address"
                                    name="email"
                                    type="email"                                    
                                    required                                                                                
                                    placeholder="Adresse e-mail"
                                    onChange={(e)=>setEmail(e.target.value)}
                                />
                            </div>

                            <div>
                                <label htmlFor="password">
                                    Mot de passe
                                </label>
                                <input
                                    id="password"
                                    name="password"
                                    type="password"                                    
                                    required                                                                                
                                    placeholder="Mot de passe"
                                    onChange={(e)=>setPassword(e.target.value)}
                                />
                            </div>
                                                
                            <div>
                                <button                                    
                                    onClick={onLogin}                                        
                                >      
                                    Connexion                                                                  
                                </button>
                            </div>                               
                        </form>
                       
                        <p className="text-sm text-white text-center">
                            Pas encore de compte ? {' '}
                            <NavLink to="/inscription">
                                S'inscrire
                            </NavLink>
                        </p>
                                                   
                    </div>
                </section>
            </main>
        </>
    )
}
 
export default Login
```

Firebase Authentication fournit d'autres méthodes de connexion, y compris l'utilisation de GitHub, Microsoft, Apple, ou un fournisseur d'identité fédérée, tel que [Google Sign-In](https://firebase.google.com/docs/auth/web/google-signin) ou [Facebook Login](https://firebase.google.com/docs/auth/web/facebook-login). 

Après une connexion réussie, les informations d'un utilisateur peuvent être accessibles et peuvent être utilisées pour ajouter plus de fonctionnalités à votre application, y compris la protection de vos routes.

Pour obtenir un utilisateur actuellement inscrit, nous définissons un observateur sur l'objet Auth. Nous pouvons obtenir un utilisateur actuellement connecté en utilisant le code suivant dans le composant **Home** :

```js
import React, { useState, useEffect } from 'react';
import { onAuthStateChanged } from "firebase/auth";
import { auth } from '../firebase';
 
const Home = () => {
 
    useEffect(()=>{
        onAuthStateChanged(auth, (user) => {
            if (user) {
              // L'utilisateur est connecté, voir la documentation pour une liste des propriétés disponibles
              // https://firebase.google.com/docs/reference/js/firebase.User
              const uid = user.uid;
              // ...
              console.log("uid", uid)
            } else {
              // L'utilisateur est déconnecté
              // ...
              console.log("l'utilisateur est déconnecté")
            }
          });
         
    }, [])
 
  return (
    <section>        
      
    </section>
  )
}
 
export default Home
 

```

Pour compléter notre authentification Firebase, après avoir créé un utilisateur et s'être connecté, il doit y avoir un moyen de déconnecter les utilisateurs. 

Pour déconnecter un utilisateur, la méthode **signOut** est appelée depuis Firebase. Après s'être connecté à la route **Home**, il y aura un bouton pour se déconnecter chaque fois que le bouton **Déconnexion** est cliqué. Le bouton doit avoir un événement **onClick** qui appelle la méthode **signOut** depuis Firebase auth. Un message de succès sera affiché sur la console si la déconnexion est réussie. 

Voici le code complet pour déconnecter un utilisateur :

```js
import React from 'react';
import {  signOut } from "firebase/auth";
import {auth} from '../../firebase';
import { useNavigate } from 'react-router-dom';
 
const Home = () => {
    const navigate = useNavigate();
 
    const handleLogout = () => {               
        signOut(auth).then(() => {
        // Déconnexion réussie.
            navigate("/");
            console.log("Déconnecté avec succès")
        }).catch((error) => {
        // Une erreur s'est produite.
        });
    }
   
    return(
        <>
            <nav>
                <p>
                    Bienvenue à la maison
                </p>
 
                <div>
        			<button onClick={handleLogout}>
                        Déconnexion
                    </button>
        		</div>
            </nav>
        </>
    )
}
 
export default Home;

```

## Conclusion

L'authentification Firebase vous permet de créer l'identité d'un utilisateur. Elle authentifie les utilisateurs de manière transparente. 

À travers cet article, j'espère que vous avez acquis suffisamment de connaissances pour construire des applications qui authentifient les utilisateurs. Vous pouvez consulter la [documentation](https://firebase.google.com/docs/auth) pour en savoir plus.

Voici un [lien](https://github.com/IsraelChidera/focus-app) vers le dépôt GitHub qui utilise l'authentification Firebase. Il utilise également **TailwindCSS** pour le style et **React Router** pour le routage.

Bon codage !