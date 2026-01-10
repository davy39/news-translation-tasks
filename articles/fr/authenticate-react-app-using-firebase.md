---
title: Comment authentifier votre application React avec Firebase
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2024-10-02T01:34:26.216Z'
originalURL: https://freecodecamp.org/news/authenticate-react-app-using-firebase
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/Uw_8vSroCSc/upload/a8799e4ad43b3b8fe966910f9171ccd3.jpeg
tags:
- name: authentication
  slug: authentication
- name: Firebase
  slug: firebase
seo_title: Comment authentifier votre application React avec Firebase
seo_desc: Learn how to authenticate your React app using Firebase with this comprehensive
  step-by-step guide for secure user management.
---

L'authentification est un aspect fondamental des applications web et mobiles modernes. Elle garantit que les utilisateurs peuvent accéder en toute sécurité à une application tout en protégeant leurs données.

Firebase, une plateforme développée par Google, offre un moyen simple et efficace d'ajouter l'authentification à votre application.

Dans cet article, je vais vous guider à travers les étapes pour authentifier votre application à l'aide de Firebase. Que vous travailliez sur une application web ou mobile, Firebase offre un moyen simple d'intégrer diverses méthodes d'authentification. 

À la fin de cet article, vous disposerez d'un système d'authentification entièrement fonctionnel qui permet aux utilisateurs de s'inscrire, de se connecter et de gérer leurs comptes en toute sécurité.

## Table des matières

* [Table des matières](#heading-table-des-matieres)
    
* [Prérequis](#heading-prerequis)
    
* [Pourquoi utiliser Firebase pour l'authentification ?](#heading-pourquoi-utiliser-firebase-pour-lauthentification)
    
* [Étape 1 : Comment configurer un projet Firebase](#heading-etape-1-comment-configurer-un-projet-firebase)
    
* [Étape 2 : Comment installer Firebase dans votre projet](#heading-etape-2-comment-installer-firebase-dans-votre-projet)
    
* [Étape 3 : Comment initialiser Firebase dans votre application](#heading-etape-3-comment-initialiser-firebase-dans-votre-application)
    
* [Étape 4 : Comment configurer les méthodes d'authentification](#heading-etape-4-comment-configurer-les-methodes-dauthentification)
    
* [Méthode d'authentification avec Google](#heading-methode-dauthentification-avec-google)
    
* [Étape 5 : Comment téléverser sur GitHub](#heading-etape-5-comment-televerser-sur-github)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, vous devez disposer des éléments suivants :

* **Un compte Google** : Firebase est un produit Google, et vous avez besoin d'un compte Google pour accéder à la Console Firebase et utiliser les services Firebase. Si vous n'avez pas de compte Google, [vous pouvez en créer un ici](https://support.google.com/mail/answer/56256?hl=en).
    

## **Pourquoi utiliser Firebase pour l'authentification ?**

Firebase Authentication fournit des services backend et des SDK faciles à utiliser pour authentifier les utilisateurs sur votre application. Il prend en charge diverses méthodes d'authentification, notamment :

* **Authentification par e-mail et mot de passe**
    
* **Authentification Google, Facebook, Twitter et GitHub**
    
* **Authentification par numéro de téléphone**
    
* **Authentification anonyme**
    

Ces fonctionnalités font de Firebase un excellent choix pour les développeurs qui souhaitent implémenter une authentification sécurisée et fiable sans avoir à gérer la complexité de la création d'un système d'authentification personnalisé.

Commençons par la configuration !

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727802131211/b57dce67-663e-4c03-baa2-21668b543d68.jpeg align="center")

## Étape 1 : Comment configurer un projet Firebase

Avant d'utiliser Firebase Authentication, vous devez configurer un projet Firebase.

**i. Créer un projet Firebase**

* Allez sur la [Console Firebase.](https://firebase.google.com/)
    

![Site web Firebase](https://cdn.hashnode.com/res/hashnode/image/upload/v1723410569746/560dfa39-e8d5-4b22-bb84-94946daeac08.png align="center")

* Cliquez sur "Ajouter un projet" et suivez les instructions à l'écran pour créer un nouveau projet.
    

![Création d'un projet de base](https://cdn.hashnode.com/res/hashnode/image/upload/v1727812540013/eceb505e-ea69-43f0-a845-ad26d86d5c26.gif align="center")

Une fois votre projet créé, vous serez dirigé vers le tableau de bord du projet Firebase.

**ii. Ajouter votre application au projet**

* Dans la console Firebase, cliquez sur l'icône "Web" (&lt;/&gt;) pour ajouter une application web à votre projet Firebase.
    
* Enregistrez votre application avec un surnom, et cliquez sur "Enregistrer l'application".
    
* Vous recevrez un extrait du SDK Firebase (Software Development Kit), que vous devrez ajouter à votre application.
    
* ![Enregistrement de votre projet sur firebase](https://cdn.hashnode.com/res/hashnode/image/upload/v1723412408046/4bf3956f-1d7d-4dff-8a70-72a757c01d2b.gif align="center")
    

## **Étape 2 : Comment installer Firebase dans votre projet**

Pour commencer avec Firebase Authentication, vous devez d'abord installer Firebase dans votre projet. Voici comment faire :

* Dans votre éditeur de code, ouvrez le terminal de votre projet.
    
* Exécutez la commande suivante pour installer Firebase :
    

```javascript
npm install firebase
```

Cette commande ajoutera Firebase à votre projet, vous permettant d'utiliser son authentification et d'autres fonctionnalités.

## **Étape 3 : Comment initialiser Firebase dans votre application**

Après avoir installé Firebase, l'étape suivante consiste à l'initialiser dans votre projet en utilisant l'extrait de configuration fourni dans la console Firebase, communément appelé extrait du SDK Firebase.

**Pour configurer cela :**

1. Créez un dossier nommé **config** dans le répertoire de votre projet.
    
2. À l'intérieur du dossier, créez un fichier appelé **firebase.js**.
    
3. Collez l'extrait du SDK que vous avez obtenu de la console Firebase dans le fichier **firebase.js**.
    

Voici à quoi devrait ressembler la configuration de votre projet :

![Collage du SDK dans votre projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1723459271302/4773d484-b5a2-4cbe-9626-76765cafd9b8.png align="center")

Ce code initialise Firebase dans votre application, vous permettant d'utiliser l'authentification Firebase et d'autres services, tels que le stockage Firebase, pour gérer vos données.

**Note :** Assurez-vous de générer votre propre clé d'application unique pour que votre application fonctionne correctement.

## **Étape 4 : Comment configurer les méthodes d'authentification**

Firebase prend en charge plusieurs méthodes d'authentification, comme l'utilisation de Google, Facebook, GitHub, etc.

Mais configurons l'authentification par e-mail et mot de passe comme exemple :

* Allez dans "Authentication" dans le menu de gauche de la console Firebase.
    
* Cliquez sur l'onglet "Sign-in method".
    
* Activez "Email/Password" dans la section "Sign-in providers".
    
    ![Authentification avec email et mot de passe](https://cdn.hashnode.com/res/hashnode/image/upload/v1723457322104/6914efdc-87cf-4fce-b84f-bd407b6b4918.gif align="center")
    
    Maintenant que vous avez activé l'authentification par e-mail/mot de passe, vous pouvez créer une fonction d'inscription (sign-up) et une fonction de connexion (sign-in) dans votre application.
    
    Créons un exemple fonctionnel de fonction d'inscription :
    
    * Dans votre projet, créez un fichier nommé **sign-up.jsx**.
        
    * Importez la fonction nécessaire pour créer un utilisateur depuis Firebase. La fonction que vous utiliserez pour créer un utilisateur est `createUserWithEmailAndPassword`.
        
    * Avant de créer un utilisateur, assurez-vous d'importer l'instance auth initialisée dans **firebase.js** dans le fichier **sign-up.jsx**.
        
    
    ```javascript
    import { auth } from '../../../config/firebase';
    import { createUserWithEmailAndPassword } from 'firebase/auth';
    
    const SignUp = () => {
      // Pour créer l'utilisateur avec l'e-mail et le mot de passe
      const handleUser = async (e) => {
        e.preventDefault();
        try {
          await createUserWithEmailAndPassword(auth, email, password);
          alert('Utilisateur créé avec succès');
        } catch (err) {
          console.error(err);
        }
      };
    
      // ... (reste de votre composant SignUp)
    };
    ```
    
    Dans l'instruction return, j'utiliserai un formulaire, nous devons donc importer le Hook `useState()` pour gérer et suivre les modifications dans les champs de saisie du formulaire.
    
    ```javascript
    <div>
      <h2>Créez votre compte</h2>
      <form onSubmit={handleCreateUser}>
        <div>
          <label>Nom</label>
          <input
            type="text"
            id="name"
            name="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
    
        <div>
          <label htmlFor="email">E-mail</label>
          <input
            type="email"
            id="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
    
        <div>
          <label htmlFor="password">Mot de passe</label>
          <input
            type="password"
            id="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
    
        <div>
          <label htmlFor="confirm_password" className={styles.label}>
            Confirmer le mot de passe
          </label>
          <input
            type="password"
            id="confirm_password"
            name="confirm_password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
        </div>
    
        <div>
          <div>
            <input type="checkbox" id="terms" name="terms" className="mr-2" />
            <label htmlFor="terms">
              J'accepte les <a href="#">Conditions Générales</a>
            </label>
          </div>
        </div>
    
        <button type="submit">S'inscrire</button>
      </form>
    </div>
    ```
    
    Assemblage de tout le code (**Sign-up.jsx**) :
    
    ```javascript
    
    import { useState } from 'react';
    import { auth } from '../../config/firebase';
    import { createUserWithEmailAndPassword } from 'firebase/auth';
    
    const SignUp = () => {
      const [name, setName] = useState('');
      const [email, setEmail] = useState('');
      const [password, setPassword] = useState('');
      const [confirmPassword, setConfirmPassword] = useState('');
    
      const handleCreateUser = async (e) => {
        e.preventDefault();
        try {
          await createUserWithEmailAndPassword(auth, email, password);
          alert('Utilisateur créé avec succès');
        } catch (error) {
          console.log(error);
        }
      };
    
      return (
        <div>
          <h2>Créez votre compte</h2>
          <form onSubmit={handleCreateUser}>
            <div>
              <label>Nom</label>
              <input
                type='text'
                id='name'
                name='name'
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </div>
    
            <div>
              <label htmlFor='email'>E-mail</label>
              <input
                type='email'
                id='email'
                name='email'
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
    
            <div>
              <label htmlFor='password'>Mot de passe</label>
              <input
                type='password'
                id='password'
                name='password'
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
    
            <div>
              <label htmlFor='confirm_password'>
                Confirmer le mot de passe
              </label>
              <input
                type='password'
                id='confirm_password'
                name='confirm_password'
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
              />
            </div>
    
            <div>
              <div>
                <input
                  type='checkbox'
                  id='terms'
                  name='terms'
                  className='mr-2'
                />
                <label htmlFor='terms'>
                  J'accepte les{' '}
                  <a href='#'>
                    Conditions Générales
                  </a>
                </label>
              </div>
            </div>
    
            <button type='submit'>S'inscrire</button>
          </form>
        </div>
      );
    };
    
    export default SignUp;
    ```
    
    Maintenant que vous avez créé la fonction d'inscription, il est temps d'ajouter une fonction de connexion pour que les utilisateurs puissent se connecter à votre application.
    
    Voici comment créer une fonction de connexion simple :
    
    * Dans votre projet, créez un nouveau fichier nommé **sign-in.jsx**.
        
    * Importez l'instance `auth` initialisée de **firebase.js** dans **sign-in.jsx**.
        
    * Utilisez la fonction `signInWithEmailAndPassword` de Firebase pour permettre aux utilisateurs de se connecter.
        

Voici la structure de la fonction de connexion :

```javascript
import { useState } from 'react';
import { auth } from '../../config/firebase';
import { signInWithEmailAndPassword } from 'firebase/auth';

const SignIn = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSignIn = async (e) => {
    e.preventDefault();
    try {
      await signInWithEmailAndPassword(auth, email, password);
      alert('Connexion réussie');
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Se connecter</h2>
      <form onSubmit={handleSignIn}>
        <div>
          <label htmlFor="email">E-mail</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>

        <div>
          <label htmlFor="password">Mot de passe</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <button type="submit">Se connecter</button>
      </form>
    </div>
  );
};

export default SignIn;
```

L'affichage visuel du résultat du code ci-dessus, avec l'inscription et la connexion réunies :

![Résultat visuel de l'inscription et de la connexion](https://cdn.hashnode.com/res/hashnode/image/upload/v1727813072045/5a91493d-69a0-4a90-98b2-61905b23e460.gif align="center")

## Méthode d'authentification avec Google

Comme mentionné précédemment, vous pouvez collecter les e-mails des utilisateurs directement via un formulaire ou utiliser d'autres moyens pour authentifier les utilisateurs.

**Pour utiliser l'authentification Google :**

* Dans la console Firebase, accédez à "Authentication" dans le menu de gauche.
    
* Cliquez sur l'onglet "Sign-in method".
    
* Activez "Google" dans la section "Sign-in providers" (pour ce tutoriel, nous resterons sur Google, bien que vous puissiez choisir d'autres fournisseurs).
    

![Activation de Google Auth](https://cdn.hashnode.com/res/hashnode/image/upload/v1727813344687/f1838b83-9af9-42a7-bf98-6a7d617cedc3.gif align="center")

Maintenant que vous avez activé l'authentification Google, vous pouvez créer une fonction d'inscription et de connexion Google pour votre application.

Voyons comment configurer une fonction d'inscription Google :

* Tout d'abord, créez un fichier nommé **Google.jsx** dans votre projet.
    
* Importez `auth` et `GoogleAuthProvider` depuis le fichier **firebase.js**
    

```javascript
// Importez les fonctions dont vous avez besoin depuis les SDK
import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider } from 'firebase/auth';


const firebaseConfig = {
  apiKey: ....,
  authDomain: ....,
  projectId:.... ,
  storageBucket: .... ,
  messagingSenderId: .... ,
  appId: ....,
  measurementId: ....,
};
// Initialiser Firebase
const app = initializeApp(firebaseConfig);
export const auth= getAuth(app);
export const googleProvider = new GoogleAuthProvider(app);
```

* Initialisez le fournisseur Google et exportez-le pour l'utiliser dans d'autres parties de votre application.
    

```javascript
import { auth, googleProvider } from './firebase';  // Ajustez le chemin vers votre fichier de configuration Firebase
import { signInWithPopup } from 'firebase/auth';
```

* Importez la fonction Firebase nécessaire pour authentifier un utilisateur. Utilisez la méthode `signInWithPopup` pour authentifier les utilisateurs avec Google.
    

Bien qu'il existe d'autres méthodes d'authentification, `signInWithPopup` est préférable car elle maintient les utilisateurs dans l'application, évitant ainsi d'avoir à ouvrir un nouvel onglet de navigateur.

```javascript
const signInWithGoogle = async () => {
  try {
    await signInWithPopup(auth, googleProvider);
    alert('Connexion réussie avec Google');
  } catch (error) {
    console.error('Erreur lors de la connexion avec Google', error);
  }
};
```

* Dans votre instruction return, créez un bouton pour déclencher la connexion Google.
    

```javascript
return (
  <div>
    <button onClick={signInWithGoogle}>Se connecter avec Google</button>
  </div>
);
```

L'affichage visuel du résultat du code ci-dessus :

![Utilisation de signInWithPop()](https://cdn.hashnode.com/res/hashnode/image/upload/v1727813634035/14c00c73-f289-480a-a396-3abd839b3a75.gif align="center")

Firebase vous permet de déconnecter facilement les utilisateurs de votre application. Voici comment vous pouvez implémenter une fonction de déconnexion :

* Tout d'abord, importez la fonction `signOut` de Firebase.
    
* Une fois importée, vous pouvez appeler `signOut` pour déconnecter l'utilisateur de l'application.
    

Voici un exemple simple :

```javascript
import { auth } from './config/firebase'; // Ajustez le chemin en fonction de la structure de vos fichiers
import { signOut } from 'firebase/auth';

const handleSignOut = async () => {
  try {
    await signOut(auth);
    alert('Utilisateur déconnecté avec succès');
  } catch (error) {
    console.error('Erreur lors de la déconnexion :', error);
  }
};
```

Avec cette fonction, les utilisateurs peuvent facilement se déconnecter de l'application.

Dans l'instruction return, vous aurez généralement un bouton qui déclenche la fonction **handleSignOut** lorsqu'il est cliqué.

```javascript
return (
  <div>
    <h2>Bienvenue dans l'application !</h2>
    <button onClick={handleSignOut}>Se déconnecter</button>
  </div>
```

L'affichage visuel du résultat du code ci-dessus :

![Affichage visuel de signOut()](https://cdn.hashnode.com/res/hashnode/image/upload/v1727813736679/21c2162b-b376-43b7-87cb-242d78acef38.gif align="center")

Assurez-vous que votre projet Firebase est configuré pour gérer correctement l'authentification, y compris la connexion Google, afin de garantir une expérience de connexion et de déconnexion fluide.

## **Étape 5 : Comment téléverser sur GitHub**

Avant de pousser votre projet vers GitHub, assurez-vous de stocker votre clé API Firebase dans une variable d'environnement pour la sécuriser. Cela empêchera l'exposition d'informations sensibles dans votre code partagé.

**Création d'un fichier .env**

* À la racine de votre application, créez un fichier **.env**.
    

![Stockage des clés API dans le fichier .env](https://cdn.hashnode.com/res/hashnode/image/upload/v1727813941388/5e647b8c-c76b-4671-b44b-21ac4dcddc89.png align="center")

* Ajoutez votre clé API Firebase au fichier **firebase.js**.
    
* Utilisez `import` ou `process.env` pour accéder à votre clé API Firebase. Comme l'application a été créée avec Vite, j'ai utilisé `import`.
    

![Fichier Firebase](https://cdn.hashnode.com/res/hashnode/image/upload/v1727814253953/514db02f-44f8-44fc-b03c-4cf77cb5c4ba.png align="center")

* Enfin, mettez à jour votre fichier **.gitignore** pour inclure le fichier **.env**. Cette étape protège également d'autres fichiers et répertoires sensibles, comme **node_modules**.
    

```javascript
# Journaux
logs
node_modules
.env
```

## Conclusion

En conclusion, ce guide explique comment intégrer Firebase Authentication dans votre application. Firebase simplifie l'ajout de fonctionnalités d'authentification telles que l'e-mail/mot de passe et la connexion Google.

En configurant un projet Firebase, en l'installant et en l'initialisant dans votre application, vous pouvez créer efficacement des fonctionnalités sécurisées d'inscription et de connexion sans avoir besoin de partir de zéro ou de configurer un serveur.

Si vous avez trouvé cet article utile, partagez-le avec d'autres personnes qu'il pourrait intéresser.

Restez à jour avec mes projets en me suivant sur [Twitter](https://https//twitter.com/ijaydimples), [LinkedIn](https://www.linkedin.com/in/ijeoma-igboagu/) et [GitHub](https://github.com/ijayhub).

Le code que j'ai utilisé pour cet article de tutoriel se trouve sur mon [GitHub](https://github.com/ijayhub/authentication-example-tutorial).

Merci de m'avoir lu.