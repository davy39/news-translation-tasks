---
title: Comment créer une application de quiz en utilisant NextJS, Chakra UI et Firebase
subtitle: ''
author: Sharvin Shah
co_authors: []
series: null
date: '2021-04-13T16:31:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-quizapp-using-nextjs-chakra-ui-and-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/How-to-Build-a-QuizApp-using-NextJS--Chakra-UI-and-Firebase-1.png
tags:
- name: app development
  slug: app-development
- name: Firebase
  slug: firebase
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Comment créer une application de quiz en utilisant NextJS, Chakra UI et
  Firebase
seo_desc: 'Hello, everyone! Welcome to this hands-on tutorial. Before we begin you
  should be familiar with the basics of ReactJS, NextJS, and Firebase. If you''re
  not, I would recommend that you go through their documentation.

  Here''s what we''re going to build:


  ...'
---

Bonjour à tous ! Bienvenue dans ce tutoriel pratique. Avant de commencer, vous devez être familiarisé avec les bases de [ReactJS](https://reactjs.org/docs/getting-started.html), [NextJS](https://nextjs.org/docs/getting-started) et [Firebase](https://firebase.google.com/docs/firestore). Si ce n'est pas le cas, je vous recommande de consulter leur documentation.

## **Voici ce que nous allons construire :**

![Image](https://www.freecodecamp.org/news/content/images/2021/04/CPT2104101814-1439x736--1-.gif align="left")

## Et voici les technologies que nous allons utiliser :

1. **TypeScript :** fournit un code typé qui nous aide à trouver des bugs lors de la compilation.
    
2. **NextJS :** un framework basé sur React qui nous permet de rendre les données côté serveur. Cela aide Google à explorer l'application, ce qui entraîne des avantages SEO.
    
3. **Chakra UI :** une bibliothèque de composants simple, modulaire et accessible qui nous fournira les blocs de construction nécessaires pour construire l'application.
    
4. **Firebase :** fournit Firestore et l'authentification que nous allons utiliser dans notre application. Nous utiliserons Firestore pour sauvegarder un quiz, les informations utilisateur et les réponses. Nous utiliserons l'authentification pour fournir la fonctionnalité de connexion avec Google à l'utilisateur.
    
5. **Vercel :** hébergera notre application. Il est bien scalable, sans aucune configuration, et le déploiement est instantané.
    
6. **Formik :** nous fournit divers composants pour construire des formulaires. Il est difficile de développer des formulaires sans Formik.
    
7. **Yup :** Un formulaire doit toujours être validé. Yup est une bibliothèque que nous utiliserons à cette fin. Yup et Formik fonctionnent très bien ensemble, et peu de configuration est requise.
    

Je vais diviser ce tutoriel en quatre sections distinctes. Au début de chaque section, vous trouverez un commit Git qui contient le code développé dans cette section. De plus, si vous souhaitez voir le code complet, il est disponible dans ce [dépôt](https://github.com/Sharvin26/quizApp).

## Contenu

1. [Comment configurer l'authentification et la collection d'utilisateurs](#heading-installation-de-l-authentification-et-de-la-collection-d-utilisateurs).
    
2. [Comment ajouter un quiz et afficher plusieurs quiz](#heading-comment-ajouter-un-quiz-et-afficher-plusieurs-quiz).
    
3. [Comment afficher un quiz unique, comment répondre à un quiz et comment valider la réponse](#heading-comment-afficher-un-quiz-unique-comment-repondre-a-un-quiz-et-comment-valider-la-reponse).
    
4. [Comment déployer l'application sur Vercel et configurer l'authentification Firebase](#heading-comment-deployer-l-application-sur-vercel-et-configurer-l-authentification-firebase).
    

Commençons.

## **Comment configurer l'authentification et la collection d'utilisateurs**

Dans cette section, nous allons implémenter les fonctionnalités suivantes :

1. Comment configurer NextJS et Chakra UI dans notre application de quiz.
    
2. Comment configurer l'authentification Firebase et Firestore.
    
3. Comment configurer la barre de navigation, les mécanismes d'inscription et de déconnexion.
    

Vous pouvez trouver le **code de l'application de quiz** implémenté dans cette section à ce [commit](https://github.com/Sharvin26/QuizApp/tree/11273c2f2ac33607e258c837c69f2473f4910656).

### Comment configurer NextJS et Chakra UI dans notre application de quiz :

Pour créer une application NextJS, vous devez utiliser la commande suivante :

```shell
npx create-next-app quizapp
```

Vous obtiendrez la structure de répertoire suivante :

```shell
+-- node_modules
+-- pages
+-- public
+-- styles
+-- .gitignore
+-- package-lock.json
+-- package.json
+-- README.md
```

**Note :** J'utilise NextJS version 10.1.3 et React version 17.0.2. Vous pouvez confirmer la version dans votre package.json.

Maintenant, convertissons notre base de code en code compatible TypeScript.

Dans le répertoire racine du projet, créez un fichier nommé `tsconfig.json` en utilisant la commande suivante :

```shell
touch tsconfig.json
```

Après cela, installez les dépendances TypeScript à l'intérieur du projet en utilisant la commande suivante :

```shell
npm install --save-dev typescript @types/react @types/node
```

Après cela, convertissez les fichiers suivants comme ceci :

```shell
pages/_app.js => pages/_app.tsx
pages/index.js => pages/index.tsx
```

Supprimez le répertoire `pages/api`. Allez ensuite dans `pages/_app.tsx` et remplacez le code complet comme suit :

```jsx
import { AppProps } from 'next/app'

function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}

export default App
```

Allez dans `pages/index.tsx` et remplacez-le par le code suivant :

```jsx
import Head from 'next/head';

export default function Home() {
  return (
    <div>
      <Head>
        <title>QuizApp</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main></main>
      <footer></footer>
    </div>
  );
}
```

Maintenant, démarrez le serveur de développement en utilisant la commande suivante :

```shell
npm run dev
```

La première fois que vous démarrez le serveur de développement, Next va :

1. Remplir le fichier `tsconfig.json` pour vous.
    
2. Créer le fichier `next-env.d.ts`, qui garantit que les types Next sont pris en compte par le compilateur TypeScript. Vous ne devez **pas** toucher à ce fichier.
    

Supprimez le répertoire `styles` du répertoire racine.

Après avoir suivi les étapes ci-dessus, vous aurez la structure de répertoire suivante :

```shell
+-- node_modules
+-- pages
|   +-- _app.tsx
|   +-- index.tsx
+-- public
+-- .gitignore
+-- package-lock.json
+-- package.json
+-- README.md
+-- tsconfig.json
```

Maintenant, allez sur `http://localhost:3000` et vous trouverez un écran vide.

Installons Chakra UI en utilisant la commande suivante :

```shell
npm i @chakra-ui/react @emotion/react@^11 @emotion/styled@^11 framer-motion@^4
```

**Note :** Si vous utilisez zsh, vous devrez ajouter le caractère d'échappement () après @ comme suit :

```shell
npm i @chakra-ui/react @emotion/react@\^11 @emotion/styled@\^11 framer-motion@\^4
```

Selon la documentation de Chakra, nous devons envelopper `<Component />` avec `ChakraProvider` dans `pages/_app.tsx` comme suit :

```jsx
import { ChakraProvider } from '@chakra-ui/react';
import { AppProps } from 'next/app';

function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <Component {...pageProps} />
    </ChakraProvider>
  );
}

export default App;
```

En gros, cela effectuera une réinitialisation CSS et passera le [thème Chakra](https://chakra-ui.com/docs/theming/theme) au composant.

Maintenant, nous allons créer notre composant `Navbar`.

Pour créer ce composant, nous devons d'abord créer un répertoire nommé `src` dans le répertoire racine et couper/coller le répertoire `pages` à l'intérieur du répertoire `src`.

Après cela, créez un répertoire nommé `common` sous le répertoire `src`.

Sous le répertoire `common`, créez un fichier nommé `Navbar.tsx`. Copiez/collez le code suivant à l'intérieur de ce fichier :

```jsx
import React from 'react';
import { Box, Divider, Flex, Heading, Link } from '@chakra-ui/react';
import { useRouter } from 'next/router';

const Navbar: React.FC<{}> = () => {
  const router = useRouter();

  return (
    <>
      <Flex justify="space-between" m={4}>
        <Heading onClick={() => router.push('/')} as="button">
          QuizApp
        </Heading>
        <Box>
          <Box p={2}>
            <Link
              p={2}
              onClick={() => router.push('/signin')}
              fontWeight={
                router.pathname === '/signin' ? 'extrabold' : 'normal'
              }
            >
              Se connecter
            </Link>
          </Box>
        </Box>
      </Flex>
      <Divider
        css={{
          boxShadow: '1px 1px #888888',
        }}
      />
    </>
  );
};

export default Navbar;
```

Après cela, allez dans `pages/index.tsx` et ajoutez la ligne suivante entre les balises `<main></main>`.

```jsx
<Navbar />
```

Vous devrez également importer la Navbar en utilisant la syntaxe suivante :

```jsx
import Navbar from '../common/Navbar';
```

Allez dans votre navigateur web et ouvrez `http://localhost:3000`, vous verrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-7.26.21-PM.png align="left")

### Comment configurer l'authentification Firebase et Firestore :

Maintenant, configurons Firebase. Allez sur la [console Firebase](https://console.firebase.google.com/u/0/). Cliquez sur Ajouter un projet :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-7.27.47-PM.png align="left")

Après cela, ajoutez le nom de votre projet comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-7.29.36-PM.png align="left")

Ensuite, il vous demandera si vous souhaitez activer Google Analytics ou non. Je préfère le désactiver, mais vous pouvez l'activer si vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-7.29.51-PM.png align="left")

Maintenant, cliquez sur **Créer un projet**. Cela prendra un certain temps pour créer le projet.

Une fois le projet créé, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-7.31.16-PM.png align="left")

Après avoir cliqué sur continuer, vous verrez un tableau de bord qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-7.34.05-PM.png align="left")

Cliquez sur **Paramètres > Paramètres du projet > Général**. Dans l'onglet Général, faites défiler vers le bas et dans la carte **Vos applications**, sélectionnez la troisième option (après l'icône Android).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-7.35.40-PM.png align="left")

Il vous demandera quelques détails pour enregistrer l'application. Ajoutez le surnom de votre application comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-7.37.27-PM.png align="left")

Après avoir cliqué sur **enregistrer l'application**, Firebase vous donnera un extrait de code. Copiez-collez ces détails dans un fichier, puis vous pouvez cliquer sur **continuer vers la console**.

Maintenant, allez dans l'onglet **comptes de service** dans les paramètres du projet et cliquez sur le bouton **Générer une nouvelle clé privée**. Cela téléchargera certaines configurations dont nous aurons besoin pour firebase-admin.

Maintenant, revenez en arrière et cliquez sur l'onglet Authentification :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-8.14.42-PM.png align="left")

Après cela, cliquez sur le bouton **Commencer** et vous obtiendrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-8.15.45-PM.png align="left")

Maintenant, cliquez sur le texte Google et cliquez sur le bouton **Activer** :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-8.16.22-PM.png align="left")

Sélectionnez l'email du projet configuré comme votre identifiant email.

Cliquez sur l'onglet Firestore et cliquez sur le bouton Créer une base de données.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-8.19.05-PM.png align="left")

Une fois que vous avez cliqué sur Créer une base de données, il vous demandera le mode. Sélectionnez le mode test pour développer l'application.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-8.19.37-PM.png align="left")

Cliquez sur Suivant. Il vous demandera l'emplacement. Sélectionnez l'option appropriée, puis cliquez sur le bouton Activer.

### Comment configurer la barre de navigation, l'inscription et les mécanismes de déconnexion :

Maintenant, retournons à notre projet. Installez les dépendances suivantes en utilisant cette commande npm :

```shell
npm i firebase firebase-admin
```

Créez un répertoire nommé `lib` à l'intérieur du répertoire `src`.

Dans le répertoire `lib`, créez deux fichiers nommés `firebase.ts` et `firebase-admin.ts`.

Copiez le code suivant à l'intérieur de `firebase.ts` :

```ts
import firebase from 'firebase/app';
import 'firebase/firestore';
import 'firebase/auth';

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
};

try {
  firebase.initializeApp(firebaseConfig);
} catch (err) {
  if (!/already exists/.test(err.message)) {
    console.error('Firebase initialization error', err.stack);
  }
}

export default firebase;
```

Ici, nous initialisons la bibliothèque Firebase en utilisant `apikey`, `authdomain` et `projectId`.

Collez le code suivant à l'intérieur de `firebase-admin.ts` :

```ts
import admin from 'firebase-admin';

if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert({
      projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
      privateKey: process.env.FIREBASE_PRIVATE_KEY,
      clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
    }),
    databaseURL: process.env.FIREBASE_DATABASE_URL,
  });
}

const db = admin.firestore();
const auth = admin.auth();

export { db, auth };
```

Ici, nous initialisons la bibliothèque `firebase-admin` en utilisant `projectId`, `privateKey`, `clientEmail` et `databaseURL`.

Maintenant, dans le répertoire racine, créez un fichier nommé `.env.local` et collez le code suivant :

```python
NEXT_PUBLIC_FIREBASE_API_KEY=
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=
NEXT_PUBLIC_FIREBASE_PROJECT_ID=

FIREBASE_PRIVATE_KEY=
FIREBASE_CLIENT_EMAIL=
FIREBASE_DATABASE_URL=
```

Vous trouverez `NEXT_PUBLIC_FIREBASE_API_KEY`, `NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN`, `NEXT_PUBLIC_FIREBASE_PROJECT_ID` dans la **Console Firebase** > **Paramètres > Paramètres du projet > Général > Carte Vos applications**.

Vous trouverez `FIREBASE_PRIVATE_KEY`, `FIREBASE_CLIENT_EMAIL` sous l'onglet compte de service. Nous pouvons générer une nouvelle clé privée en utilisant le bouton **Générer une nouvelle clé privée**. Ce fichier contient les deux ensembles de données.

Pour `FIREBASE_DATABASE_URL`, ajoutez `https://<database-name>.firebaseio.com`. Remplacez `database-name` par le nom de votre base de données.

**Note :** Vous pouvez trouver le `database-name` sous **console firebase > firestore** dans l'onglet données (voir la capture d'écran ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-11-at-4.47.36-PM.png align="left")

Maintenant, dans le répertoire `lib`, créez un troisième fichier nommé `auth.tsx`. Cela contiendra notre mécanisme d'autorisation et d'état. Collez le code suivant dans ce fichier :

```ts
import { Context, createContext, useContext, useEffect, useState } from 'react';
import { addUser } from '../utils/db';
import firebase from './firebase';

interface Auth {
  uid: string;
  email: string | null;
  name: string | null;
  photoUrl: string | null;
  token: string | null;
}

interface AuthContext {
  auth: Auth | null;
  loading: boolean;
  siginWithGoogle: () => Promise<void>;
  signOut: () => Promise<void>;
}

const authContext: Context<AuthContext> = createContext<AuthContext>({
  auth: null,
  loading: true,
  siginWithGoogle: async () => {},
  signOut: async () => {},
});

const formatAuthState = (user: firebase.User): Auth => ({
  uid: user.uid,
  email: user.email,
  name: user.displayName,
  photoUrl: user.photoURL,
  token: null,
});

function useProvideAuth() {
  const [auth, setAuth] = useState<Auth | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  const handleAuthChange = async (authState: firebase.User | null) => {
    if (!authState) {
      setLoading(false);
      return;
    }
    const formattedAuth = formatAuthState(authState);
    formattedAuth.token = await authState.getIdToken();
    setAuth(formattedAuth);
    setLoading(false);
  };

  const signedIn = async (
    response: firebase.auth.UserCredential,
    provider: String = 'google'
  ) => {
    if (!response.user) {
      throw new Error('No User');
    }
    const authUser = formatAuthState(response.user);
    await addUser({ ...authUser, provider });
  };

  const clear = () => {
    setAuth(null);
    setLoading(true);
  };

  const siginWithGoogle = async () => {
    setLoading(true);
    return firebase
      .auth()
      .signInWithPopup(new firebase.auth.GoogleAuthProvider())
      .then(signedIn);
  };
  const signOut = async () => {
    return firebase.auth().signOut().then(clear);
  };

  useEffect(() => {
    const unsubscribe = firebase.auth().onAuthStateChanged(handleAuthChange);
    return () => unsubscribe();
  }, []);

  return {
    auth,
    loading,
    siginWithGoogle,
    signOut,
  };
}

export function AuthProvider({ children }: any) {
  const auth = useProvideAuth();
  return <authContext.Provider value={auth}>{children}</authContext.Provider>;
}

export const useAuth = () => useContext(authContext);
```

Dans le répertoire `src`, créez un dossier nommé `utils` et sous ce dossier, créez un fichier nommé `db.ts`. Ajoutez le code suivant à l'intérieur de ce fichier :

```ts
import firebase from '../lib/firebase';

export const addUser = async (authUser: any) => {
  const resp = await firebase
    .firestore()
    .collection('users')
    .doc(authUser.uid as string)
    .set({ ...authUser }, { merge: true });
  return resp;
};
```

Allez dans `Navbar.tsx` sous le répertoire des composants et mettez à jour le code précédent avec le code suivant :

```jsx
import { Box, Divider, Flex, Heading, Link } from '@chakra-ui/react';
import { useRouter } from 'next/router';
import React from 'react';
import { useAuth } from '../lib/auth';

const Navbar: React.FC<{}> = () => {
  const { auth, signOut } = useAuth();
  const router = useRouter();

  return (
    <>
      <Flex justify="space-between" m={4}>
        <Heading onClick={() => router.push('/')} as="button">
          QuizApp
        </Heading>
        <Box>
          {auth ? (
            <Box p={2}>
              <Link
                p={2}
                fontWeight={
                  router.pathname === '/quiz/new' ? 'extrabold' : 'normal'
                }
                onClick={() => router.push('/quiz/new')}
              >
                Ajouter un nouveau quiz
              </Link>
              <Link p={2} onClick={() => signOut()}>
                Déconnexion
              </Link>
            </Box>
          ) : (
            <Box p={2}>
              <Link
                p={2}
                onClick={() => router.push('/signin')}
                fontWeight={
                  router.pathname === '/signin' ? 'extrabold' : 'normal'
                }
              >
                Se connecter
              </Link>
            </Box>
          )}
        </Box>
      </Flex>
      <Divider
        css={{
          boxShadow: '1px 1px #888888',
        }}
      />
    </>
  );
};

export default Navbar;
```

Remplacez le `_app.tsx` par le code suivant :

```jsx
import { ChakraProvider } from '@chakra-ui/react';
import { AppProps } from 'next/app';
import { AuthProvider } from '../lib/auth';

function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <AuthProvider>
        <Component {...pageProps} />
      </AuthProvider>
    </ChakraProvider>
  );
}

export default App;
```

Créez un nouveau fichier nommé `signin.tsx` sous le répertoire pages et ajoutez le code suivant :

```jsx
import { Button, Center, Container, Heading, VStack } from '@chakra-ui/react';
import { useRouter } from 'next/router';
import React from 'react';
import { FcGoogle } from 'react-icons/fc';
import Navbar from '../common/Navbar';
import { useAuth } from '../lib/auth';

const signin = () => {
  const { auth, siginWithGoogle } = useAuth();
  const router = useRouter();

  if (auth) {
    router.push((router.query.next as string) || '/');
  }

  return (
    <>
      <Navbar />
      <Container>
        <Center mt={10}>
          <VStack spacing="4">
            <Heading fontSize="3xl" mb={2}>
              Bonjour, bienvenue dans l'application de quiz !!
            </Heading>
            <Button leftIcon={<FcGoogle />} onClick={() => siginWithGoogle()}>
              Se connecter avec Google
            </Button>
          </VStack>
        </Center>
      </Container>
    </>
  );
};

export default signin;
```

Vous devrez installer react-icons. Pour installer react-icons, utilisez la commande suivante :

```shell
npm i react-icons
```

Maintenant, redémarrez le serveur de développement et allez sur `http://localhost:3000`. Cliquez sur le lien Se connecter et vous obtiendrez l'écran suivant.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-04-at-8.12.39-PM.png align="left")

Maintenant, cliquez sur le bouton Se connecter avec Google. Après une connexion réussie, vous serez redirigé vers la page d'accueil.

## **Comment ajouter un quiz et afficher plusieurs quiz**

Dans cette section, nous allons implémenter les fonctionnalités suivantes :

1. Comment configurer le mécanisme d'ajout d'un quiz.
    
2. Comment configurer le mécanisme d'affichage de plusieurs quiz.
    

Vous pouvez trouver le **code de l'application de quiz** dans cette section à ce [commit](https://github.com/Sharvin26/QuizApp/tree/5ff954a606151e9574ac747ae3780d7644561865).

### Comment configurer le mécanisme d'ajout d'un quiz :

Maintenant, nous allons nous concentrer sur l'ajout du quiz. Pour ajouter un nouveau quiz, nous allons utiliser **Formik**. Il nous aidera à configurer le formulaire dynamique et **Yup** nous aidera avec la validation de ces formulaires.

Installons les deux bibliothèques en utilisant la commande suivante.

```shell
npm i formik yup
```

Nous allons également utiliser un package nommé **uuid** pour donner un identifiant unique à nos questions et options. Pour installer le package, utilisez la commande suivante :

```shell
npm i uuid
```

Nous aurons également besoin des icônes Chakra, alors installez-les en utilisant la commande suivante :

```shell
npm i @chakra-ui/icons
```

Nous aurons besoin d'Axios pour faire un appel API à notre environnement serverless Next. Utilisez la commande suivante pour l'installer :

```shell
npm i axios
```

À l'intérieur du répertoire **src > pages**, créez un nouveau répertoire nommé **quiz** et sous ce répertoire, créez un nouveau répertoire nommé **new**.

À l'intérieur du répertoire **new**, créez un fichier nommé `index.tsx` et collez le code suivant à l'intérieur :

```jsx
import { AddIcon, MinusIcon } from '@chakra-ui/icons';
import {
  Box,
  Button,
  Center,
  Container,
  Divider,
  Flex,
  FormControl,
  FormErrorMessage,
  FormLabel,
  IconButton,
  Input,
  SimpleGrid,
  Text,
  Textarea,
} from '@chakra-ui/react';
import { Field, FieldArray, Form, Formik, getIn } from 'formik';
import { useRouter } from 'next/router';
import React, { useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';
import * as yup from 'yup';
import Navbar from '../../../common/Navbar';
import { useAuth } from '../../../lib/auth';
import { addQuizApi } from '../../../utils/service';

const optionData = [
  {
    label: 'Option A:',
  },
  {
    label: 'Option B:',
  },
  {
    label: 'Option C:',
  },
  {
    label: 'Option D:',
  },
];

const answerOption = [
  {
    label: 'A',
    answer: 0,
  },
  {
    label: 'B',
    answer: 1,
  },
  {
    label: 'C',
    answer: 2,
  },
  {
    label: 'D',
    answer: 3,
  },
];

const Index = () => {
  const { auth, loading } = useAuth();

  const router = useRouter();

  useEffect(() => {
    if (!auth && !loading) {
      router.push('/signin?next=/quiz/new');
    }
  }, [auth, loading]);

  const questionsData = {
    title: '',
    options: [{ title: '' }, { title: '' }, { title: '' }, { title: '' }],
    answer: '0',
  };

  const initialValues = {
    title: '',
    description: '',
    questions: [questionsData],
  };

  const validationSchema = yup.object().shape({
    title: yup.string().required('Requis'),
    description: yup.string().required('Requis'),
    questions: yup
      .array()
      .of(
        yup.object().shape({
          title: yup.string().required('Requis !'),
          options: yup.array().of(
            yup.object().shape({
              title: yup.string().required('Requis !'),
            })
          ),
        })
      )
      .required('Vous devez ajouter une question'),
  });

  const submitHandler = async (values, actions) => {
    try {
      values = {
        ...values,
        createdAt: new Date(),
        updatedAt: new Date(),
        questions: values.questions.map((question) => {
          return {
            ...question,
            options: question.options.map((option) => {
              return { ...option, optionId: uuidv4() };
            }),
            questionId: uuidv4(),
          };
        }),
      };
      await addQuizApi(auth, values);
      router.push('/');
    } catch (error) {
      console.log('error', error);
    } finally {
      actions.setSubmitting(false);
    }
  };

  return (
    <>
      <Navbar />
      <Container
        maxW="3xl"
        mt={5}
        mb={5}
        borderWidth="1px"
        borderRadius="lg"
        p={6}
        boxShadow="xl"
      >
        <Formik
          initialValues={initialValues}
          onSubmit={submitHandler}
          validationSchema={validationSchema}
        >
          {(props) => (
            <Form>
              <Field name="title">
                {({ field, form }) => (
                  <FormControl
                    isInvalid={form.errors.title && form.touched.title}
                  >
                    <FormLabel htmlFor="title" fontSize="xl">
                      Titre du quiz
                    </FormLabel>
                    <Input {...field} id="title" />
                    <FormErrorMessage>{form.errors.title}</FormErrorMessage>
                  </FormControl>
                )}
              </Field>
              <Field name="description">
                {({ field, form }) => (
                  <FormControl
                    isInvalid={
                      form.errors.description && form.touched.description
                    }
                  >
                    <FormLabel htmlFor="description" fontSize="xl" mt={4}>
                      Description du quiz
                    </FormLabel>
                    <Textarea {...field} id="description" />
                    <FormErrorMessage>
                      {form.errors.description}
                    </FormErrorMessage>
                  </FormControl>
                )}
              </Field>
              <Field name="questions">
                {({ field }) => (
                  <FormControl>
                    <FormLabel htmlFor="questions" fontSize="xl" mt={4}>
                      Entrez les données de votre question :
                    </FormLabel>
                    <Box ml={4}>
                      <FieldArray {...field} name="questions" id="questions">
                        {(fieldArrayProps) => {
                          const { push, remove, form } = fieldArrayProps;
                          const { values, errors, touched } = form;
                          const { questions } = values;
                          const errorHandler = (name) => {
                            const error = getIn(errors, name);
                            const touch = getIn(touched, name);
                            return touch && error ? error : null;
                          };
                          return (
                            <div>
                              {questions.map((_question, index) => {
                                return (
                                  <Flex key={index} direction="column">
                                    <FormControl
                                      isInvalid={errorHandler(
                                        `questions[${index}][title]`
                                      )}
                                    >
                                      <FormLabel
                                        htmlFor={`questions[${index}][title]`}
                                      >
                                        Titre de la question :
                                      </FormLabel>
                                      <Input
                                        name={`questions[${index}][title]`}
                                        as={Field}
                                        mb={
                                          !errorHandler(
                                            `questions[${index}][title]`
                                          ) && 3
                                        }
                                      />
                                      <FormErrorMessage>
                                        {errorHandler(
                                          `questions[${index}][title]`
                                        )}
                                      </FormErrorMessage>
                                    </FormControl>
                                    <SimpleGrid
                                      minChildWidth="300px"
                                      spacing="10px"
                                      mb={{ base: 4 }}
                                    >
                                      {optionData.map((option, subIndex) => (
                                        <FormControl
                                          mb={2}
                                          key={subIndex}
                                          isInvalid={errorHandler(
                                            `questions[${index}][options][${subIndex}].title`
                                          )}
                                        >
                                          <FormLabel
                                            htmlFor={`questions[${index}][options][${subIndex}].title`}
                                          >
                                            {option.label}
                                          </FormLabel>
                                          <Input
                                            name={`questions[${index}][options][${subIndex}].title`}
                                            as={Field}
                                          />
                                          <FormErrorMessage>
                                            {errorHandler(
                                              `questions[${index}][options][${subIndex}].title`
                                            )}
                                          </FormErrorMessage>
                                        </FormControl>
                                      ))}
                                    </SimpleGrid>
                                    <Box>
                                      <Text mb="8px">Bonne réponse :</Text>
                                      <Field
                                        component="select"
                                        name={`questions[${index}][answer]`}
                                        style={{
                                          width: '100%',
                                          padding: '10px',
                                        }}
                                      >
                                        {answerOption.map((value, key) => (
                                          <option
                                            value={value.answer}
                                            key={key}
                                          >
                                            {value.label}
                                          </option>
                                        ))}
                                      </Field>
                                    </Box>
                                    <Flex
                                      direction="row"
                                      justify="flex-end"
                                      mt={4}
                                    >
                                      {index > 0 && (
                                        <IconButton
                                          onClick={() => remove(index)}
                                          aria-label="Supprimer la question"
                                          icon={<MinusIcon />}
                                          variant="ghost"
                                        >
                                          -
                                        </IconButton>
                                      )}
                                      {index === questions.length - 1 && (
                                        <IconButton
                                          onClick={() => push(questionsData)}
                                          aria-label="Ajouter une question"
                                          icon={<AddIcon />}
                                          variant="ghost"
                                        >
                                          +
                                        </IconButton>
                                      )}
                                    </Flex>
                                    {index !== questions.length - 1 && (
                                      <Divider
                                        mt={2}
                                        mb={4}
                                        css={{
                                          boxShadow: '1px 1px #888888',
                                        }}
                                      />
                                    )}
                                  </Flex>
                                );
                              })}
                            </div>
                          );
                        }}
                      </FieldArray>
                    </Box>
                  </FormControl>
                )}
              </Field>
              <Center>
                <Button
                  colorScheme="green"
                  isLoading={props.isSubmitting}
                  type="submit"
                  disabled={!(props.isValid && props.dirty)}
                >
                  Soumettre le quiz
                </Button>
              </Center>
            </Form>
          )}
        </Formik>
      </Container>
    </>
  );
};

export default Index;
```

Comprenons le code ci-dessus.

**Note :** Ne copiez/collez pas les extraits de code individuels ci-dessous. J'ai pris des morceaux du grand bloc de code ci-dessus et les ai divisés en morceaux plus petits pour que nous puissions comprendre ce qui se passe.

```jsx
const questionsData = {
  title: '',
  options: [{ title: '' }, { title: '' }, { title: '' }, { title: '' }],
  answer: '0',
};

const initialValues = {
  title: '',
  description: '',
  questions: [questionsData],
};

<Formik
   initialValues={initialValues}
   onSubmit={submitHandler}
   validationSchema={validationSchema}
>
    {(props) => (
       <Form>
         #Champ d'entrée et bouton
       </Form>
    )}
</Formik>
```

`<Formik>` est un wrapper qui prend 3 props. Les `initialValues` qui sont définis ci-dessus et passés ici en tant que props sont ensuite passés aux champs d'entrée définis entre les deux.

```jsx
<FieldArray {...field} name="questions" id="questions">
  {(fieldArrayProps) => {
    const { push, remove, form } = fieldArrayProps;
    const { values, errors, touched } = form;
    const { questions } = values;
    const errorHandler = (name) => {
      const error = getIn(errors, name);
      const touch = getIn(touched, name);
      return touch && error ? error : null;
    };
    return (<div> 
      // Champs d'entrée
    </div>)
  };
</FieldArray>
```

Dans ce formulaire, vous trouverez que le composant `FieldArray` est défini. Ce composant est fourni par Formik lui-même. Lorsque nous voulons des champs d'entrée dynamiques, nous pouvons utiliser ce composant.

Les `fieldArrayProps` se composent de deux éléments importants nommés `push` et `remove` qui nous aident à ajouter un nouveau champ d'entrée et à le supprimer.

Nous utilisons l'utilitaire `getIn` de Formik pour valider nos champs et vérifier s'il y a des erreurs.

```ts
const validationSchema = yup.object().shape({
  title: yup.string().required('Requis'),
  description: yup.string().required('Requis'),
  questions: yup
    .array()
    .of(
      yup.object().shape({
        title: yup.string().required('Requis !'),
        options: yup.array().of(
          yup.object().shape({
            title: yup.string().required('Requis !'),
          })
        ),
      })
    )
    .required('Vous devez ajouter une question'),
});
```

Ci-dessus se trouve la syntaxe Yup qui définit la forme de l'objet. Pour plus d'informations, veuillez vous référer à la [documentation de yup](https://github.com/jquense/yup).

Nous combinons le schéma de validation avec Yup et le passons à Formik. Formik les mappe en interne avec le nom défini dans le champ d'entrée.

```ts
const submitHandler = async (values, actions) => {
  try {
    values = {
      ...values,
      createdAt: new Date(),
      updatedAt: new Date(),
      questions: values.questions.map((question) => {
        return {
          ...question,
          options: question.options.map((option) => {
            return { ...option, optionId: uuidv4() };
          }),
          questionId: uuidv4(),
        };
      }),
    };
    await addQuizApi(auth, values);
    router.push('/');
  } catch (error) {
    console.log('error', error);
  } finally {
    actions.setSubmitting(false);
  }
};
```

La fonction **onSubmit** est appelée lorsqu'un utilisateur appuie sur Entrée sur le clavier ou sur le bouton de soumission sur le site web. Nous devons passer `submitHandler` comme référence à celle-ci.

À l'intérieur de cette fonction, nous définissons un identifiant unique pour nos questions et options et faisons un appel API pour le stocker dans notre collection Firestore.

Maintenant, à l'intérieur du répertoire **src > utils**, créez un nouveau fichier nommé `service.ts` et ajoutez le code suivant :

```ts
import axios from 'axios';

export const addQuizApi = async (auth, values) => {
  try {
    const header = {
      'Content-Type': 'application/json',
      token: auth.token,
    };
    const resp = await axios.post('/api/quiz', values, { headers: header });
    return resp;
  } catch (error) {
    throw error;
  }
};
```

À l'intérieur du répertoire **src > pages**, créez un nouveau répertoire nommé **api**. Tous les fichiers sous ce répertoire s'exécuteront comme environnement serverless par défaut.

À l'intérieur du répertoire **api**, créez un **répertoire** nommé **quiz**. Ici, créez un nouveau fichier nommé index.ts et collez le code suivant :

```ts
import { NextApiRequest, NextApiResponse } from 'next';
import { auth } from '../../../lib/firebase-admin';
import { addQuiz as addQuizFb } from '../../../utils/db';

export default async (req: NextApiRequest, res: NextApiResponse) => {
  switch (req.method) {
    case 'POST':
      await addQuiz(req, res);
      break;
    default:
      res.status(405).json({ status: false, message: 'Méthode non trouvée' });
      break;
  }
};

const addQuiz = async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    const user = await auth.verifyIdToken(req.headers.token as string);
    const quizData = { ...req.body, userId: user.uid };
    await addQuizFb(quizData);
    return res
      .status(200)
      .json({ status: true, message: 'Quiz ajouté avec succès...' });
  } catch (error) {
    return res
      .status(500)
      .json({ status: false, message: 'Quelque chose s\'est mal passé' });
  }
};
```

Maintenant, allez dans le répertoire **src > utils > db.ts** et ajoutez le code suivant après la fonction `addUser` :

```ts
export const addQuiz = async (quizData) => {
  let response = await firebase.firestore().collection('quiz').add(quizData);
  return response;
};
```

Maintenant, exécutons notre serveur de développement et essayons d'ajouter un nouveau quiz.

```shell
npm run dev
```

Allez sur `http://localhost:3000` et cliquez sur le lien `Ajouter un nouveau quiz` dans la barre de navigation. Vous obtiendrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/screencapture-localhost-3000-quiz-new-2021-04-10-13_41_52.png align="left")

Maintenant, remplissez le formulaire et cliquez sur le bouton **Soumettre le quiz**. Allez dans la console Firebase et vous verrez qu'une nouvelle collection nommée **quiz** a été créée.

**Note :** Pour `FIREBASE_PRIVATE_KEY` dans `.env.local`, n'oubliez pas d'ajouter des guillemets autour ou vous obtiendrez l'erreur suivante :

```shell
FirebaseAppError: Failed to parse private key: Error: Invalid PEM formatted message.
```

### Comment configurer le mécanisme d'affichage de plusieurs quiz :

Maintenant, affichons notre liste de quiz sur la route `/`. Allez dans **pages > index.js** et mettez à jour le code existant avec le code suivant :

```jsx
import { Box, Container, Divider, Flex, Heading, SimpleGrid, Text } from '@chakra-ui/react';
import Head from 'next/head';
import { useRouter } from 'next/router';
import React from 'react';
import Navbar from '../common/Navbar';
import { getAllQuiz, getAllUsers } from '../utils/db';

const Home = (props) => {
  const quiz = JSON.parse(props.quiz);
  const router = useRouter();

  const generateQuizCard = (singleQuiz) => {
    return (
      <Box m={3} borderWidth="1px" borderRadius="lg" p={6} boxShadow="xl">
        <Heading as="h3" size="lg">
          {singleQuiz.title}
        </Heading>
      
          <Text color="gray.500" mt={2}>
            Posté par : {singleQuiz.user.name}
          </Text>
          <Text color="gray.500" mt={2}>
            Nombre de questions : {singleQuiz.questions.length}
          </Text>
   
        <Divider mt={3} mb={3} />
        <Text noOfLines={[1, 2, 3]}>{singleQuiz.description}</Text>
      </Box>
    );
  };

  return (
    <Box>
      <Head>
        <title>QuizApp</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <header>
          <Navbar />
          <Container maxW="6xl">
            {quiz.length > 0 && (
              <SimpleGrid minChildWidth="400px">
                {quiz.map((singleQuiz) => (
                  <Box
                    key={singleQuiz.id}
                    onClick={() => router.push(`/quiz/${singleQuiz.id}`)}
                    as="button"
                    textAlign="start"
                    m={2}
                  >
                    {generateQuizCard(singleQuiz)}
                  </Box>
                ))}
              </SimpleGrid>
            )}
          </Container>
        </header>
      </main>
      <footer></footer>
    </Box>
  );
};

export async function getServerSideProps(_context) {
  const quiz = await getAllQuiz();
  const users = await getAllUsers();
  const data = quiz.map((singleQuiz: any) => {
    return { ...singleQuiz, user: users.find((user) => user.id === singleQuiz.userId)};
  });
  return { props: { quiz: JSON.stringify(data) } };
}

export default Home;
```

Maintenant, allez dans **src > utils > db.ts** et ajoutez le code suivant après la fonction `addQuiz` :

```ts
export const getAllQuiz = async () => {
  const snapshot = await firebase.firestore().collection('quiz').get();
  const quiz = snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }));
  return quiz;
};

export const getAllUsers = async () => {
  const snapshot = await firebase.firestore().collection('users').get();
  const users = snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }));
  return users;
}
```

Allez sur `http://localhost:3000` et actualisez la page. Vous obtiendrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/screencapture-localhost-3000-2021-04-10-14_49_25.png align="left")

## Comment afficher un quiz unique, comment répondre à un quiz et comment valider la réponse

Dans cette section, les fonctionnalités suivantes seront implémentées :

1. Comment configurer les mécanismes d'affichage d'un quiz unique et de réponse à un quiz.
    
2. Comment configurer le mécanisme de validation de la réponse.
    

Vous pouvez trouver le **code de l'application de quiz** implémenté dans cette section à ce [commit](https://github.com/Sharvin26/QuizApp/tree/ebc092727b9346b796a1d14fec6234e498403710).

### **Comment configurer les mécanismes d'affichage d'un quiz unique et de réponse à un quiz :**

Créez un nouveau répertoire nommé **\[id\]** sous **src > pages > quiz.** À l'intérieur de ce répertoire, créez un fichier nommé `index.tsx` et collez le code suivant :

```jsx
import {
  Button,
  Center,
  Container,
  Divider,
  FormControl,
  FormLabel,
  Heading,
  HStack,
  RadioGroup,
  SimpleGrid,
  Text,
} from '@chakra-ui/react';
import { Field, Form, Formik } from 'formik';
import { NextPageContext } from 'next';
import { useRouter } from 'next/router';
import React, { useEffect } from 'react';
import Navbar from '../../../common/Navbar';
import { useAuth } from '../../../lib/auth';
import { getSingleQuiz } from '../../../utils/db';
import { addAnswerApi } from '../../../utils/service';

const ShowQuiz = (quiz, onSubmit) => {
  return (
    <Container
      maxW="7xl"
      mt={5}
      mb={5}
      borderWidth="1px"
      borderRadius="lg"
      p={6}
      boxShadow="xl"
    >
      <Center flexDirection="column">
        <Heading>{quiz.title}</Heading>
      </Center>
      <Text mt={4}>{quiz.description}</Text>
      <Heading mt={4} size="lg">
        Questions :
      </Heading>
      <Divider
        mt={4}
        mb={4}
        css={{
          boxShadow: '1px 1px #888888',
        }}
      />
      <Formik initialValues={{}} onSubmit={onSubmit}>
        {(props) => (
          <Form>
            {quiz.questions.map((singleQuiz, key) => (
              <Field name={singleQuiz.questionId} key={key}>
                {({ field, _form }) => (
                  <FormControl
                    as="fieldset"
                    isRequired={true}
                    mb={{ base: 4, md: 0 }}
                  >
                    <FormLabel as="legend">{singleQuiz.title}</FormLabel>
                    <RadioGroup>
                      <SimpleGrid minChildWidth="120px" mb={2}>
                        {singleQuiz.options.map((option, subkey) => (
                          <HStack key={subkey}>
                            <Field
                              {...field}
                              type="radio"
                              name={singleQuiz.questionId}
                              value={option.optionId}
                            />
                            <Text>{option.title}</Text>
                          </HStack>
                        ))}
                      </SimpleGrid>
                    </RadioGroup>
                  </FormControl>
                )}
              </Field>
            ))}
            <Center mt={10}>
              <Button
                type="submit"
                isLoading={props.isSubmitting}
                colorScheme="green"
              >
                Soumettre
              </Button>
            </Center>
          </Form>
        )}
      </Formik>
    </Container>
  );
};

const SingleQuiz = (props) => {
  const { auth, loading } = useAuth();

  const router = useRouter();

  useEffect(() => {
    if (!auth && !loading) {
      router.push(`/signin?next=/quiz/${props.quizId}`);
    }
  }, [auth, loading]);

  const quiz = JSON.parse(props.quiz);

  const onSubmit = async (values, actions) => {
    try {
      const resp = await addAnswerApi(auth, props.quizId, values);
      const answerId = resp.data.data.answerId;
      router.push(`/quiz/${props.quizId}/answer/${answerId}`);
    } catch (error) {
      console.log('error', error);
    } finally {
      actions.setSubmitting(false);
    }
  };

  return (
    <>
      <Navbar />
      {quiz && ShowQuiz(quiz, onSubmit)}
    </>
  );
};

export async function getServerSideProps(context: NextPageContext) {
  const quizId = context.query.id;
  const quizData = await getSingleQuiz(quizId);
  return { props: { quiz: quizData, quizId } };
}

export default SingleQuiz;
```

Dans **src > utils >** `db.ts`, ajoutez le code suivant sous la fonction `getAllUsers` :

```ts
export const getSingleQuiz = async (quizId) => {
  const snapshot = await firebase
    .firestore()
    .collection('quiz')
    .doc(String(quizId))
    .get();
  const quizData = snapshot.exists ? JSON.stringify(snapshot.data()) : null;
  return quizData;
};
```

Dans **src > utils >** `service.ts`, ajoutez le code suivant sous la fonction `addQuizApi` :

```ts
export const addAnswerApi = async (auth, quizId, values) => {
  try {
    const header = {
      'Content-Type': 'application/json',
      token: auth.token,
    };
    const resp = await axios.post(
      `/api/quiz/${quizId}/answer`,
      {
        questions: values,
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      { headers: header }
    );
    return resp;
  } catch (error) {
    throw error;
  }
};
```

Dans le répertoire **src > pages > api > quiz**, créez un nouveau répertoire nommé **\[id\]**.

### Comment configurer le mécanisme de validation de la réponse :

À l'intérieur de ce répertoire, créez un fichier nommé `answer.ts` et collez le code suivant :

```ts
import { NextApiRequest, NextApiResponse } from 'next';
import { auth } from '../../../../lib/firebase-admin';
import { addAnswer as addAnswerFb } from '../../../../utils/db';

export default async (req: NextApiRequest, res: NextApiResponse) => {
  switch (req.method) {
    case 'POST':
      await addAnswer(req, res);
      break;
    default:
      res.status(405).json({ status: false, message: 'Méthode non trouvée' });
      break;
  }
};

const addAnswer = async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    const user = await auth.verifyIdToken(req.headers.token as string);
    const data = {
      ...req.body,
      quizId: req.query.id,
      userId: user.uid,
    };
    const response = await addAnswerFb(data);
    return res
      .status(200)
      .json({ status: true, data: { answerId: response.id } });
  } catch (error) {
    return res
      .status(500)
      .json({ status: false, message: 'Quelque chose s\'est mal passé' });
  }
};
```

Dans **src > utils >** `db.ts`, ajoutez le code suivant sous la fonction `getSingleQuiz` :

```ts
export const addAnswer = async (data) => {
  const response = await firebase.firestore().collection('answer').add(data);
  return response;
};
```

Allez sur `http://localhost:3000`, actualisez la page et cliquez sur le quiz. Vous obtiendrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/screencapture-localhost-3000-quiz-1VrjhRht5LFdA3a2all5-2021-04-10-15_13_15.png align="left")

Maintenant, vous pouvez répondre à la question et appuyer sur soumettre. Pour l'instant, cela vous mènera à une page 404. Nous devons créer une page où nous pouvons afficher la bonne réponse.

À l'intérieur du répertoire **src > pages > quiz > \[id\]**, créez un nouveau répertoire appelé **answer**. À l'intérieur de ce répertoire, créez un nouveau fichier appelé `[answerId].tsx` et collez le code suivant :

```jsx
import {
  Box,
  Center,
  Container,
  Divider,
  Heading,
  Radio,
  RadioGroup,
  SimpleGrid,
  Text,
} from '@chakra-ui/react';
import { NextPageContext } from 'next';
import React from 'react';
import Navbar from '../../../../common/Navbar';
import { getAnswer, getSingleQuiz } from '../../../../utils/db';

const answer = (props) => {
  const quiz = JSON.parse(props.quiz);
  const answer = JSON.parse(props.answer);

  return (
    <>
      <Navbar />
      {quiz && answer && (
        <Container maxW="3xl" mt={5}>
          <Center flexDirection="column">
            <Heading>Bonne réponse pour {quiz.title}</Heading>
            <Text mt={4}>{quiz.description}</Text>
          </Center>
          <Divider
            mt={4}
            mb={4}
            css={{
              boxShadow: '1px 1px #888888',
            }}
          />
          {quiz.questions.map((singleQuiz, index) => {
            return (
              <Box
                mt={index !== 0 && 4}
                key={index}
                borderWidth="1px"
                borderRadius="lg"
                p={6}
                boxShadow="xl"
                backgroundColor={
                  answer.questions[singleQuiz.questionId] &&
                  singleQuiz.options[singleQuiz.answer].optionId ===
                    answer.questions[singleQuiz.questionId]
                    ? 'green.200'
                    : 'red.200'
                }
              >
                <Text>
                  {index + 1}) {singleQuiz.title}
                </Text>
                <RadioGroup>
                  <SimpleGrid minChildWidth="120px" mt={2}>
                    {singleQuiz.options.map((option, index) => (
                      <Radio value={option.title} isDisabled key={index}>
                        {option.title}
                      </Radio>
                    ))}
                  </SimpleGrid>
                </RadioGroup>
                <Text mt={3}>
                  Bonne réponse : {singleQuiz.options[singleQuiz.answer].title}
                </Text>
                {answer.questions[singleQuiz.questionId] ? (
                  <Text>
                    Réponse sélectionnée :{' '}
                    {
                      singleQuiz.options.find(
                        (option) =>
                          option.optionId ===
                          answer.questions[singleQuiz.questionId]
                      ).title
                    }
                  </Text>
                ) : (
                  <Text>Non répondu</Text>
                )}
              </Box>
            );
          })}
        </Container>
      )}
    </>
  );
};

export async function getServerSideProps(context: NextPageContext) {
  const quizId = context.query.id;
  const answerId = context.query.answerId;
  const quizData = await getSingleQuiz(quizId);
  const answerData = await getAnswer(answerId);
  return { props: { answer: answerData, quiz: quizData } };
}

export default answer;
```

Dans **src > utils >** `db.ts`, ajoutez le code suivant sous la fonction `addAnswer` :

```ts
export const getAnswer = async (answerId) => {
  const answerSnapshot = await firebase
    .firestore()
    .collection('answer')
    .doc(String(answerId))
    .get();
  let answerData = answerSnapshot.exists
    ? JSON.stringify(answerSnapshot.data())
    : null;
  return answerData;
};
```

Allez sur `http://localhost:3000`, actualisez la page, cliquez sur le quiz et répondez à la question. Vous obtiendrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/screencapture-localhost-3000-quiz-1VrjhRht5LFdA3a2all5-answer-jyZ3cOPbfyPX4DyGduUD-2021-04-10-15_40_40.png align="left")

Avec cela, nous avons terminé notre application et elle est prête à être déployée sur Vercel. Dans la section suivante, nous allons configurer le mécanisme de déploiement.

## Comment déployer l'application sur Vercel et configurer l'authentification Firebase

Il existe deux façons de configurer une application sur Vercel :

1. En utilisant la [bibliothèque npm Vercel](https://www.npmjs.com/package/vercel) et en poussant le code localement vers un serveur Vercel
    
2. En connectant le bot Vercel au dépôt GitHub.
    

Je vais utiliser la deuxième méthode.

Vous devez créer un dépôt sur GitHub et y pousser le code.

Si vous n'avez pas créé de compte sur Vercel, vous pouvez aller sur [https://vercel.com/](https://vercel.com/) et cliquer sur le bouton d'inscription.

Une fois que vous avez créé votre compte, vous serez dirigé vers un tableau de bord qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-10-at-4.07.03-PM.png align="left")

Cliquez sur le bouton **Nouveau projet**. Il vous demandera d'installer le bot Vercel et les permissions.

**Note :** Vous pouvez autoriser le bot Vercel à lire tous les dépôts de votre compte GitHub ou donner la permission pour le dépôt actuellement créé.

Cliquez sur le bouton Importer sur le dépôt GitHub créé ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-10-at-4.12.06-PM.png align="left")

Maintenant, vous devrez ajouter des variables d'environnement. Ajoutez-les à partir de `.env.local`.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/screencapture-vercel-new-settings-2021-04-10-16_18_04.png align="left")

Une fois qu'elles sont ajoutées, cliquez sur le bouton Déployer. Après le déploiement réussi, vous obtiendrez l'écran suivant.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-10-at-4.22.02-PM.png align="left")

**Note :** l'URL peut être dans ce format -&lt;username-or\_something\_random&gt;.vercel.app.

Notre connexion ne fonctionnera pas maintenant. Nous devons ajouter notre nouvelle URL aux URL autorisées dans la console Firebase.

Allez dans **Console Firebase > Authentification** et cliquez sur **Méthodes de connexion** et faites défiler vers le bas. Vous verrez le tableau **Domaines autorisés**.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-10-at-4.32.41-PM.png align="left")

Cliquez sur le bouton Ajouter un domaine, copiez la nouvelle URL générée et cliquez sur ajouter. Maintenant, ouvrez l'application de quiz déployée et testez-la.

**Note :** Si vous recevez une erreur lors de l'ajout d'un nouveau quiz ou de la réponse au quiz, allez dans **Tableau de bord Vercel > Sélectionnez le projet > Sélectionnez l'onglet paramètres > Sélectionnez Variables d'environnement** et mettez à jour votre `FIREBASE_PRIVATE_KEY` une fois de plus.

Avec cela, nous avons créé notre application de quiz prête pour la production. Si vous avez construit l'application avec le tutoriel, alors un très grand félicitations pour cette réalisation.

## Prochaines étapes :

Si vous souhaitez ajouter plus de fonctionnalités à cette application, voici quelques prochaines étapes que vous pouvez envisager :

1. Tableau de bord pour les utilisateurs. (Afficher les informations de profil, mettre à jour et supprimer. Afficher le quiz ajouté, mettre à jour et supprimer. Afficher la réponse au quiz.)
    
2. Modification des règles de sécurité Firestore.
    
3. Texte riche markdown pour les questions et options de quiz.
    

Merci d'avoir lu !

> N'hésitez pas à me contacter sur [Twitter](https://twitter.com/sharvinshah26) et [Github](https://github.com/Sharvin26).

> Si vous souhaitez qu'un projet soit développé ou souhaitez me consulter, vous pouvez me DM sur mon Twitter (@sharvin26).