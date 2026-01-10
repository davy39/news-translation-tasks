---
title: Comment créer une application Full Stack avec Next.js 13 et Firebase
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2023-02-17T17:38:20.000Z'
originalURL: https://freecodecamp.org/news/create-full-stack-app-with-nextjs13-and-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-sevenstorm-juhaszimrus-443383--1-.jpg
tags:
- name: Firebase
  slug: firebase
- name: full stack
  slug: full-stack
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Comment créer une application Full Stack avec Next.js 13 et Firebase
seo_desc: 'Next.js is a React framework that makes building powerful full stack (front
  end + back end) applications a lot easier.

  The team behind Next.js recently released Next.js 13 which has a whole lot of futures
  like a new app Directory, server and client c...'
---

Next.js est un framework React qui facilite grandement la création d'applications full stack (front end + back end) puissantes.

L'équipe derrière Next.js a [récemment publié Next.js 13](https://nextjs.org/blog/next-13) qui apporte de nombreuses fonctionnalités comme un nouveau répertoire `app`, des composants serveur et client, et bien plus.

Dans cet article, vous apprendrez à utiliser Next.js 13 et la base de données Firebase pour créer une application full stack.

Avant de continuer, cet article suppose que vous avez une connaissance de base de JavaScript, React et Next.js. Si vous avez besoin de vous rafraîchir la mémoire sur ces compétences, voici quelques ressources pour débutants :

* [Apprendre JavaScript – curriculum](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) et [cours interactif](https://www.freecodecamp.org/news/learn-javascript-interactive-course/)

* [Apprendre React - cours complet](https://www.freecodecamp.org/news/learn-react-js-in-this-free-7-hour-course/)

* [Apprendre Next.js - manuel complet](https://www.freecodecamp.org/news/the-next-js-handbook/)

Maintenant, si vous êtes prêt, plongeons dans le vif du sujet.

## Comment configurer un projet Next.js 13

Pour configurer Next.js, vous devez avoir Node.js et npm/yarn installés sur votre ordinateur. Si vous ne les avez pas, vous pouvez les installer depuis leurs sites officiels : [site web de Node.js](https://nodejs.org/en/) et [site web de npm](https://www.npmjs.com/) (mais npm est inclus lorsque vous installez Node).

1. Dans le répertoire de votre choix, lancez votre terminal et exécutez la commande suivante : `npx create-next-app@latest --experimental-app`.

2. Entrez le nom de votre projet et cliquez sur Entrée, puis attendez qu'il s'installe.

3. Un nouveau répertoire avec le nom de votre projet sera créé avec les fichiers nécessaires.

4. Accédez à ce nouveau répertoire : `cd my-project-name`

5. Pour démarrer le serveur de développement, exécutez la commande suivante :

    ```plaintext
    // si vous utilisez yarn
    yarn run dev

    // si vous utilisez npm
    npm run dev
    ```

6. L'exécution de cette commande démarrera le serveur de développement et vous pourrez voir votre application Next.js 13 en cours d'exécution sur http://localhost:3000.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-5.33.52-PM.png align="left")

*Application Next.js 13*

### Comment configurer Firebase dans Next.js

Firebase est une plateforme BaaS (Backend-as-a-Service) qui fournit des services backend cloud tels que l'authentification, la base de données en temps réel, le stockage cloud, l'analyse et bien plus.

Dans ce tutoriel, nous allons utiliser Firebase comme base de données. Suivez les étapes ci-dessous pour créer une application Firebase :

1. Allez sur https://console.firebase.google.com/ et connectez-vous avec votre compte Google.

2. Cliquez sur **Ajouter un projet** et donnez un nom à votre projet. Cliquez sur **Continuer**.

3. Sur l'écran suivant, vous pouvez choisir si vous souhaitez activer l'analyse pour votre projet.

4. Cliquez sur **Créer un projet**.

5. Ensuite, vous devez créer une application web. Sur la page d'accueil de votre projet, cliquez sur l'icône web pour créer votre application web :

    ![Screenshot-2023-02-15-at-5.40.33-PM](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-5.40.33-PM.png align="left")

6. Donnez un nom à votre application web et cliquez sur **Enregistrer l'application**.

    ![Screenshot-2023-02-15-at-5.40.48-PM](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-5.40.48-PM.png align="left")

7. Copiez le fichier de configuration dont nous aurons besoin plus tard. Cliquez sur suivant jusqu'à ce que vous ayez terminé.

8. Sur la page d'accueil de votre projet, **choisissez un produit à ajouter à votre application**. Pour ce tutoriel, ajoutez uniquement **Authentification** et **Cloud Firestore**.

    ![Screenshot-2023-02-15-at-6.33.34-PM](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-15-at-6.33.34-PM.png align="left")

9. Pour l'authentification, choisissez **Méthode de connexion** et ajoutez **Email/mot de passe**.

Une fois que vous avez configuré Firebase avec succès, nous pouvons maintenant l'utiliser comme backend pour votre application Next.js 13.

Pour utiliser Firebase avec Next.js, suivez ces étapes :

1. Installez le dernier SDK Firebase sur votre projet Next.js en exécutant la commande suivante dans votre terminal :

    ```js
    yarn add firebase

    // ou si vous utilisez npm
    npm install firebase
    ```

2. Créez un fichier `.env` dans le répertoire racine de votre projet Next.js et ajoutez vos fichiers de configuration Firebase (ceux que vous avez copiés précédemment). Cela devrait ressembler à ceci :

    ```js
    NEXT_PUBLIC_FIREBASE_API_KEY=api-key
    NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=auth-domain
    NEXT_PUBLIC_FIREBASE_PROJECT_ID=project-id
    NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=storage-bucket
    NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=sender-id
    NEXT_PUBLIC_FIREBASE_APP_ID=app-id
    NEXT_PUBLIC_FIREBASE_MEASUREMENT_ID=analytic-id
    ```

3. Ensuite, pour rendre les choses plus organisées, dans votre répertoire **src**, créez un dossier nommé **firebase** et créez un fichier `config.js` avec le code suivant :

    ```js
    // Importez les fonctions dont vous avez besoin depuis les SDK nécessaires
    import { initializeApp, getApps } from "firebase/app";

    const firebaseConfig = {
        apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
        authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
        projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
        storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
        messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
        appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
        measurementId: process.env.NEXT_PUBLIC_FIREBASE_MEASUREMENT_ID,
    };

    // Initialisez Firebase
    let firebase_app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApps()[0];

    export default firebase_app;
    ```

Maintenant, vous êtes prêt à utiliser Firebase comme base de données dans votre application Next.js 13.

## Comment configurer l'authentification

Lorsqu'il s'agit de créer des applications full stack, la première chose qui vient à l'esprit est l'authentification. Nous avons besoin d'un moyen pour inscrire et connecter les utilisateurs, et nous pouvons le faire facilement avec Firebase.

Dans votre répertoire **src > firebase**, créez un nouveau répertoire appelé **auth**. Nous ajouterons tout notre code lié à l'authentification Firebase dans ce répertoire.

Maintenant, créez un fichier `signup.js` dans le répertoire **src > firebase > auth** avec le code suivant :

```js
import firebase_app from "../config";
import { createUserWithEmailAndPassword, getAuth } from "firebase/auth";

const auth = getAuth(firebase_app);


export default async function signUp(email, password) {
    let result = null,
        error = null;
    try {
        result = await createUserWithEmailAndPassword(auth, email, password);
    } catch (e) {
        error = e;
    }

    return { result, error };
}
```

Maintenant, analysons un peu cela. Ce que nous faisons ici, c'est exporter une fonction `signUp()` qui utilise la méthode Firebase **createUserWithEmailAndPassword()** pour inscrire de nouveaux utilisateurs. Maintenant, nous pouvons utiliser cette fonction `signUp()` n'importe où dans notre application.

Dans le même répertoire, ajoutons notre fonction `signIn()`. Créez un fichier `signin.js` avec le code suivant :

```js
import firebase_app from "../config";
import { signInWithEmailAndPassword, getAuth } from "firebase/auth";

const auth = getAuth(firebase_app);

export default async function signIn(email, password) {
    let result = null,
        error = null;
    try {
        result = await signInWithEmailAndPassword(auth, email, password);
    } catch (e) {
        error = e;
    }

    return { result, error };
}
```

### Comment créer les pages de connexion et d'inscription dans Next.js

Dans Next.js 13, vous créez de nouvelles pages dans le répertoire `app`. Chaque page est un dossier avec un fichier `page.js` – vous pouvez en apprendre plus sur la création de [pages à partir de la documentation Next.js.](https://beta.nextjs.org/docs/routing/pages-and-layouts)

Pour créer la page d'inscription, créez un nouveau fichier **signup > page.js** dans votre répertoire **app** et ajoutez le code suivant :

```js
'use client'
import React from "react";
import signUp from "@/firebase/auth/signup";
import { useRouter } from 'next/navigation'

function Page() {
    const [email, setEmail] = React.useState('')
    const [password, setPassword] = React.useState('')
    const router = useRouter()

    const handleForm = async (event) => {
        event.preventDefault()

        const { result, error } = await signUp(email, password);

        if (error) {
            return console.log(error)
        }

        // sinon réussi
        console.log(result)
        return router.push("/admin")
    }
    return (<div className="wrapper">
        <div className="form-wrapper">
            <h1 className="mt-60 mb-30">S'inscrire</h1>
            <form onSubmit={handleForm} className="form">
                <label htmlFor="email">
                    <p>Email</p>
                    <input onChange={(e) => setEmail(e.target.value)} required type="email" name="email" id="email" placeholder="example@mail.com" />
                </label>
                <label htmlFor="password">
                    <p>Mot de passe</p>
                    <input onChange={(e) => setPassword(e.target.value)} required type="password" name="password" id="password" placeholder="mot de passe" />
                </label>
                <button type="submit">S'inscrire</button>
            </form>
        </div>
    </div>);
}

export default Page;`
```

Par défaut, chaque page que vous ajoutez dans le répertoire `app` est un [composant serveur](https://beta.nextjs.org/docs/rendering/server-and-client-components), ce qui signifie que nous ne pouvons pas ajouter d'interactivité côté client comme ajouter un `onSubmit()` à un élément de formulaire. Pour ajouter cette interactivité côté client, nous indiquons à Next.js que nous voulons un composant client en ajoutant ce qui suit en haut du fichier avant toute importation :

```js
'use client'

// code du composant
```

De la même manière, nous pouvons créer notre page de connexion. Pour créer la page de connexion, créez un nouveau fichier **signin > page.js** dans votre répertoire **app** et ajoutez le code suivant :

```js
'use client'
import React from "react";
import signIn from "@/firebase/auth/signin";
import { useRouter } from 'next/navigation'

function Page() {
    const [email, setEmail] = React.useState('')
    const [password, setPassword] = React.useState('')
    const router = useRouter()

    const handleForm = async (event) => {
        event.preventDefault()

        const { result, error } = await signIn(email, password);

        if (error) {
            return console.log(error)
        }

        // sinon réussi
        console.log(result)
        return router.push("/admin")
    }
    return (<div className="wrapper">
        <div className="form-wrapper">
            <h1 className="mt-60 mb-30">Se connecter</h1>
            <form onSubmit={handleForm} className="form">
                <label htmlFor="email">
                    <p>Email</p>
                    <input onChange={(e) => setEmail(e.target.value)} required type="email" name="email" id="email" placeholder="example@mail.com" />
                </label>
                <label htmlFor="password">
                    <p>Mot de passe</p>
                    <input onChange={(e) => setPassword(e.target.value)} required type="password" name="password" id="password" placeholder="mot de passe" />
                </label>
                <button type="submit">Se connecter</button>
            </form>
        </div>

    </div>);
}

export default Page;
```

### Comment écouter les changements d'authentification

Dans toute notre application, nous voulons pouvoir savoir si un certain utilisateur est connecté ou non. Nous pouvons créer des pages protégées et n'afficher certains contenus qu'à l'utilisateur connecté. Firebase nous fournit une méthode `onAuthStateChanged()` que nous pouvons écouter pour les changements.

Pour rendre les données utilisateur de la méthode ci-dessus disponibles dans toute notre application, nous allons utiliser l'API de contexte React. Créez un dossier nommé **context** dans votre répertoire **src**. À l'intérieur du répertoire **context**, créez un fichier appelé `AuthContext.js` et ajoutez le code suivant :

```js
import React from 'react';
import {
    onAuthStateChanged,
    getAuth,
} from 'firebase/auth';
import firebase_app from '@/firebase/config';

const auth = getAuth(firebase_app);

export const AuthContext = React.createContext({});

export const useAuthContext = () => React.useContext(AuthContext);

export const AuthContextProvider = ({
    children,
}) => {
    const [user, setUser] = React.useState(null);
    const [loading, setLoading] = React.useState(true);

    React.useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, (user) => {
            if (user) {
                setUser(user);
            } else {
                setUser(null);
            }
            setLoading(false);
        });

        return () => unsubscribe();
    }, []);

    return (
        <AuthContext.Provider value={{ user }}>
            {loading ? <div>Chargement...</div> : children}
        </AuthContext.Provider>
    );
};
```

Ci-dessus, nous créons simplement un fournisseur qui retourne l'objet utilisateur si l'utilisateur est connecté. Si l'utilisateur n'est pas connecté, nous retournons simplement `null`.

Pour pouvoir utiliser la valeur passée à `<AuthContext.Provider>`, nous exportons `useAuthContext` depuis le fichier. Avec cela, nous pouvons utiliser la valeur `user`.

Avant de pouvoir utiliser ce contexte, nous devons envelopper tous nos composants avec `AuthContextProvider`. Ouvrez le fichier **src > app > layout.js** et modifiez le code avec ce qui suit :

```js
'use client'
import './globals.css'
import { AuthContextProvider } from '@/context/AuthContext'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      {/*
        <head /> contiendra les composants retournés par le parent le plus proche
        head.js. En savoir plus sur https://beta.nextjs.org/docs/api-reference/file-conventions/head
      */}
      <head />
      <body>
        <AuthContextProvider>
          {children}
        </AuthContextProvider>
      </body>
    </html>
  )
}
```

Maintenant, nous pouvons créer des pages protégées et afficher un contenu spécifique à différents utilisateurs.

### Comment créer des pages protégées

Créez le répertoire **admin > page.js** dans votre répertoire `app` et ajoutez le code suivant :

```js
'use client'
import React from "react";
import { useAuthContext } from "@/context/AuthContext";
import { useRouter } from "next/navigation";
function Page() {
    const { user } = useAuthContext()
    const router = useRouter()

    React.useEffect(() => {
        if (user == null) router.push("/")
    }, [user])

    return (<h1>Seuls les utilisateurs connectés peuvent voir cette page</h1>);
}

export default Page;
```

Si l'utilisateur est `null`, nous redirigeons simplement l'utilisateur vers la page d'accueil. Si l'utilisateur n'est pas `null`, nous lui montrons la page protégée.

## Comment communiquer avec notre base de données

Maintenant que nous avons terminé la partie authentification, nous pouvons nous concentrer sur la communication avec notre base de données. Pour notre base de données, nous allons utiliser **Firestore**.

Pour rendre les choses plus organisées, créez un nouveau répertoire **firebase > firestore**, à l'intérieur de ce répertoire, nous ajouterons tout notre code lié à Firestore.

### Comment ajouter des documents à Firestore

Créez un fichier appelé `addData.js` à l'intérieur du répertoire **firestore** et ajoutez le code suivant :

```js
import firebase_app from "../config";
import { getFirestore, doc, setDoc } from "firebase/firestore";

const db = getFirestore(firebase_app)
export default async function addData(colllection, id, data) {
    let result = null;
    let error = null;

    try {
        result = await setDoc(doc(db, colllection, id), data, {
            merge: true,
        });
    } catch (e) {
        error = e;
    }

    return { result, error };
}
```

À ce stade, ce type de code devrait vous être familier. Nous exportons une fonction qui ajoute des données à notre base de données Firestore.

Nous pouvons maintenant utiliser cette fonction `addData()` depuis n'importe quel composant pour ajouter des données à notre base de données :

```js
'use client'
import addData from "@/firebase/firestore/addData";

export default function Home() {

  const handleForm = async () => {
    const data = {
      name: 'John snow',
      house: 'Stark'
    }
    const { result, error } = await addData('users', 'user-id', data)

    if (error) {
      return console.log(error)
    }
  }
  
  return (
    ...
  )
}
```

### Comment obtenir un document de Firestore

En utilisant une approche similaire, nous pouvons obtenir un document de notre base de données Firestore.

Créez un fichier `getData.js` dans le répertoire **Firestore** et ajoutez le code suivant :

```js
import firebase_app from "../config";
import { getFirestore, doc, getDoc } from "firebase/firestore";

const db = getFirestore(firebase_app)
export default async function getDoument(collection, id) {
    let docRef = doc(db, collection, id);

    let result = null;
    let error = null;

    try {
        result = await getDoc(docRef);
    } catch (e) {
        error = e;
    }

    return { result, error };
}
```

Vous pouvez également utiliser `getData()` dans n'importe quel composant de votre choix.

## Conclusion

Dans cet article, nous avons appris à créer une application full stack en utilisant Firebase et Next.js 13 en intégrant l'authentification et en interagissant avec notre base de données.

Bon codage !