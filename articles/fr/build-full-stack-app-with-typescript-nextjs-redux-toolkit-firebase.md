---
title: Comment construire une application de gestion de tâches Kanban Full-Stack avec
  TypeScript, Next.js, Redux-toolkit et Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-03-26T21:44:04.000Z'
originalURL: https://freecodecamp.org/news/build-full-stack-app-with-typescript-nextjs-redux-toolkit-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Option-1.png
tags:
- name: Firebase
  slug: firebase
- name: full stack
  slug: full-stack
- name: handbook
  slug: handbook
- name: Next.js
  slug: nextjs
- name: TypeScript
  slug: typescript
seo_title: Comment construire une application de gestion de tâches Kanban Full-Stack
  avec TypeScript, Next.js, Redux-toolkit et Firebase
seo_desc: 'By Olasunkanmi Balogun

  In this in-depth tutorial, you''ll learn how to build a full-stack Kanban task management
  app. Along the way, we''ll explore the synergies between technologies like Next.js
  (featuring a dive into the app router), Next-auth for us...'
---

Par Olasunkanmi Balogun

Dans ce tutoriel approfondi, vous apprendrez à construire une application de gestion de tâches Kanban full-stack. En cours de route, nous explorerons les synergies entre des technologies comme [`Next.js`](https://nextjs.org) (avec une plongée dans le routeur d'application), [`Next-auth`](https://next-auth.js.org) pour l'authentification des utilisateurs, et [Firebase](https://firebase.google.com/), une plateforme backend en tant que service pour sauvegarder les données utilisateur dans une base de données. 

Nous aborderons également comment intégrer Firebase Firestore avec [`Redux Toolkit`](https://redux-toolkit.js.org/), ce qui vous permet de mettre en cache les données que vous avez récupérées de la base de données pour améliorer les performances. Vous apprendrez également à gérer l'état avec Redux Toolkit.

Pour conclure, nous utiliserons [`React-beautiful-dnd`](https://www.npmjs.com/package/react-beautiful-dnd), une bibliothèque qui intègre facilement les interactions de glisser-déposer dans nos tableaux Kanban pour améliorer l'expérience utilisateur.

Voici ce que nous allons couvrir :

1. Comment implémenter l'authentification avec la bibliothèque `next-auth.js`
2. Comment configurer et intégrer le magasin `Redux` avec Firestore dans Next.js.
3. Comment construire et remplir la marque de l'application Kanban avec des données
4. Comment implémenter les opérations Create, Read, Update et Delete (CRUD) sur les tableaux et les tâches.
5. Comment implémenter le glisser-déposer avec la bibliothèque `react-beautiful-dnd`.

## Prérequis
- Vous devez avoir une expérience préalable avec le framework `Reactjs/Next.js`.
- Vous devez comprendre les annotations de type dans TypeScript, et finalement, travailler avec `TypeScript` dans React.
- Une compréhension des DSA en `JavaScript` est un plus.
- L'expérience avec la bibliothèque `Redux-toolkit` sera également un plus. 


Quelques notes : 
- Cet article se concentrera principalement sur la fonctionnalité, mais nous utiliserons `Tailwind CSS` pour le style.
- J'inclurai également des commentaires avec chaque extrait de code fourni dans cet article pour mieux expliquer le code. Gardez un œil sur eux. 

## Table des matières

1. [Comment implémenter l'authentification avec next-auth.js](#heading-comment-implementer-l-authentification-avec-next-authjs)
2. [Comment configurer le magasin Redux](#heading-comment-configurer-le-magasin-redux)
3. [Comment créer la marque de votre application Kanban](#heading-comment-creer-la-marque-de-votre-application-kanban)
4. [Comment configurer Firebase Firestore](#heading-comment-configurer-firebase-firestore)
5. [Comment ajouter des données initiales à la base de données Firestore](#heading-comment-ajouter-des-donnees-initiales-a-la-base-de-donnees-firestore)
6. [Comment utiliser RTK Query pour récupérer des données de Cloud Firestore](#heading-comment-utiliser-rtk-query-pour-recuperer-des-donnees-de-cloud-firestore)
7. [Comment récupérer et remplir les données](#heading-comment-recuperer-et-remplir-les-donnees)
    - [Comment remplir la barre de navigation](#heading-comment-remplir-la-barre-de-navigation)
    - [Comment remplir la barre latérale](#heading-comment-remplir-la-barre-laterale)
    - [Comment remplir le composant BoardTasks](#heading-comment-remplir-le-composant-boardtasks)
8. [Comment implémenter les opérations CRUD](#heading-comment-implementer-les-operations-crud)
    - [Comment ajouter et modifier un tableau](#heading-comment-ajouter-et-modifier-un-tableau)
    - [Comment ajouter et modifier des tâches](#heading-comment-ajouter-et-modifier-des-taches)
    - [Comment supprimer des tableaux et des tâches](#heading-comment-supprimer-des-tableaux-et-des-taches)
9. [Comment implémenter la fonctionnalité de glisser-déposer](#heading-comment-implementer-la-fonctionnalite-de-glisser-deposer)
10. [Conclusion](#heading-conclusion)

Lorsque vous êtes prêt, plongeons dans le vif du sujet.

## Comment implémenter l'authentification avec `next-auth.js`

Commencez par exécuter la commande suivante dans votre terminal pour créer un nouveau projet `Next.js` :

```npm
npx create-next-app@latest kanban-app-tutorial
```

Tout au long du processus d'installation, vous rencontrerez des invites. Assurez-vous d'activer `TypeScript` et `Tailwind CSS`, car les deux seront intégrés à notre développement de projet.

![Invites d'installation du projet Nextjs](https://www.freecodecamp.org/news/content/images/2024/01/1-3.png)

Allez-y et nettoyez le code redondant qui accompagne le projet. Supprimez le contenu du fichier `page.tsx` et collez le code ci-dessous comme espace réservé :

```tsx
export default function Home() {
  return (
    <main>
      <p>Bonjour</p>
    </main>
  )
}
```
Également, modifiez le contenu du fichier `global.css` et laissez uniquement les imports de `Tailwind CSS`. 

Une fois ces modifications terminées, installez la bibliothèque `next-auth.js` avec la commande suivante :

```
npm install next-auth
```

Après une installation réussie, créez un dossier `api` dans votre dossier racine `app`, et à l'intérieur, créez un dossier `auth`. Ensuite, créez un dossier `[...nextauth]` à l'intérieur du dossier `auth`.

Enfin, créez deux fichiers nommés `route.ts` et `options.ts` à l'intérieur du dossier `[...nextauth]`. 

Votre structure de fichiers devrait ressembler à ce qui suit :

![Structure de fichiers de l'application Nextjs](https://www.freecodecamp.org/news/content/images/2024/01/2-2.png)

Parmi les différents fournisseurs `next-auth.js`, nous utiliserons exclusivement le fournisseur Google pour exécuter le processus d'authentification.

Dans le fichier `option.ts`, collez le code suivant :

```tsx
import type { NextAuthOptions } from "next-auth";
import GoogleProvider from "next-auth/providers/google";

export const options: NextAuthOptions = {
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID as string,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET as string,
    }),
  ],
  secret: process.env.NEXTAUTH_URL,
};
```

Ici, nous avons importé le type `NextAuthOptions` fourni par `next-auth` pour la sécurité des types concernant la variable `options`.

Dans le code ci-dessus, l'objet `options` est l'endroit où le fournisseur que nous voulons utiliser sera hébergé (le fournisseur Google dans ce cas). 

Vous pouvez obtenir vos valeurs `clientId` et `clientSecret` depuis la plateforme Google Cloud. Si vous avez besoin d'un guide étape par étape sur la façon de les obtenir, référez-vous à ce guide. 

Une fois que vous les avez obtenus, créez un fichier `.env` dans le dossier racine de votre application et collez les valeurs dans leurs variables respectives.

Enfin, créez une clé secrète pour la variable `NEXTAUTH_SECRET` en utilisant la commande terminal suivante :

```
openssl rand -base64 32
```

En fin de compte, votre fichier `.env` devrait contenir ces variables et valeurs :

```
GOOGLE_CLIENT_ID = <valeur de l'ID client>
GOOGLE_CLIENT_SECRET = <valeur du secret client>
NEXT_AUTH_SECRET = <secret next auth>
```

Important : Vous aurez également besoin de ces variables d'environnement en production. Donc, n'oubliez pas de mettre à jour votre variable d'environnement de production dans les paramètres de votre projet sur Vercel.

Passez au fichier `route.ts` et collez le code suivant :

```
import NextAuth from "next-auth/next";
import { options } from "./options";

const handler = NextAuth(options);

export { handler as GET, handler as POST };
```

Ici, nous avons importé la variable `options` du fichier `option.ts` et l'avons passée en tant que paramètre à la fonction `NextAuth`, en assignant le résultat à la variable `handler`.

La dernière instruction garantit que toute requête GET ou POST envoyée à la route `api/auth/[...nextauth]` sera gérée par `next-auth.js`.

Cependant, l'authentification ne sera pas encore initiée car nous n'avons pas informé `next-auth.js` des pages qui doivent être protégées. 

Pour implémenter des routes protégées, générez un fichier `middleware.ts` dans le dossier racine `src` et insérez le code suivant :

```ts
export { default } from 'next-auth/middleware'

export const config = { matcher: ['/'] }
```

La propriété `matcher` dans l'objet `config` est un tableau contenant les routes que vous souhaitez que le `middleware` protège. Dans ce cas, `'/'` désigne la page d'accueil, indiquant que le `middleware` protège la page d'accueil.

Lorsque vous exécutez votre serveur de projet (avec `npm run dev`), vous devriez voir une page d'authentification comme illustré ci-dessous :

![Page d'authentification Nextauth.js](https://www.freecodecamp.org/news/content/images/2024/01/3-3.png)

Maintenant, configurons le magasin `Redux` dans notre application.

## Comment configurer le magasin Redux

Pour configurer le magasin Redux dans votre application, suivez ces étapes :

1. Commencez par installer les packages nécessaires. Exécutez la commande suivante dans votre terminal :

```npm
npm install @reduxjs/toolkit react-redux
```

Cela installe le `Redux Toolkit` et `react-redux` pour les liaisons React.

2. Dans le répertoire racine `src`, créez un dossier nommé `redux`. À l'intérieur de ce dossier, créez un fichier `store.ts`. Collez le code suivant dans le fichier `store.ts` :

```tsx
   // store.ts

   import { configureStore } from "@reduxjs/toolkit";
   import { setupListeners } from "@reduxjs/toolkit/dist/query";

   // Créer le magasin Redux
   export const store = configureStore({
     reducer: {}, // Ajoutez vos réducteurs ici
   });

   // Configurer les écouteurs pour les comportements de rafraîchissement
   setupListeners(store.dispatch);

   // Définir les types RootState et AppDispatch
   export type RootState = ReturnType<typeof store.getState>;
   export type AppDispatch = typeof store.dispatch;
```
   
Dans cet extrait de code, `configureStore` est utilisé pour créer le magasin Redux, et `setupListeners` est appelé pour gérer les comportements `refetchOnFocus` et `refetchOnReconnect`.

3. Maintenant, créez un autre fichier dans le même dossier `redux` nommé `hooks.ts` et ajoutez le code suivant :

```tsx
// hooks.ts
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";
import type { RootState, AppDispatch } from "./store";
// Versions typées des hooks useDispatch et useSelector

export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
```
   
Ce code crée des versions typées des hooks `useDispatch` et `useSelector` pour assurer la sécurité des types lors de l'interaction avec le magasin Redux.

4. Toujours dans le dossier `redux`, créez un fichier nommé `provider.tsx` avec l'extrait de code suivant :

```tsx
// provider.tsx
'use client'
import { store } from "./store";
import { Provider } from "react-redux";

// Composant fournisseur personnalisé
export function Providers({ children }: { children: React.ReactNode }) {
   return <Provider store={store}>{children}</Provider>;
 }
```
   
Ce fichier définit un composant fournisseur personnalisé à envelopper autour de vos composants d'application.

5. Dans votre fichier de mise en page d'application (`src/app/layout.tsx`), importez le composant `Providers` et enveloppez-le autour de votre mise en page principale comme vu ci-dessous :

```tsx
// layout.tsx

import type { Metadata } from 'next'
import { Plus_Jakarta_Sans } from "next/font/google";
import './globals.css'
import { Providers } from "@/components/redux/provider";
   
// police que nous utiliserons dans tout le projet
const pjs = Plus_Jakarta_Sans({ subsets: ["latin"], display: "swap" });
// Définition des métadonnées
export const metadata: Metadata = {
   title: 'Créer une application Next',
   description: 'Généré par créer une application next',
  }

// Composant RootLayout
export default function RootLayout({
   children,
   }: {
   children: React.ReactNode
 }) {
   return (
      <html lang="en" className={pjs.className}>
        <body>
          <Providers>
            {children}
          </Providers>
        </body>
      </html>
  );
}
```

En enveloppant vos composants avec le composant `Providers`, vous garantissez que chaque composant de votre application a accès au magasin Redux.
   
Jusqu'à ce point, votre structure de dossiers devrait ressembler à ceci :

![Structure de dossiers de l'application nextjs](https://www.freecodecamp.org/news/content/images/2024/01/4-1.png)

Avec ces étapes, vous avez intégré avec succès le magasin Redux dans votre application, et vous êtes prêt à créer des [slices](https://redux-toolkit.js.org/tutorials/quick-start#create-a-redux-state-slice) pour votre application.

Avant de plonger dans l'implémentation des slices, créons la marque de notre application.

## Comment créer la marque de votre application Kanban

Cette section vous guide à travers le processus de création de la marque pour votre application Kanban. À la fin de cette section, votre marque devrait ressembler à l'image ci-dessous :

![Marque de l'application Kanban](https://www.freecodecamp.org/news/content/images/2024/01/8-1.png)

Commençons par créer le composant de la barre de navigation.

1. Commencez par établir un dossier `components` dans le répertoire `app`. À l'intérieur, créez un fichier `Navbar.tsx` et insérez le code suivant :

```tsx
// src/app/components/Navbar.tsx
   
export default function Navbar() {

return (
  <nav className="bg-white border flex h-24">
    <div className="flex-none w-[18.75rem] border-r-2 flex items-center pl-[2.12rem]">
      <p className="font-bold text-3xl"> Application Kanban </p>
    </div>

   <div className="flex justify-between w-full items-center pr-[2.12rem]">
       <p className="text-black text-2xl font-bold pl-6">
         Nom du tableau
       </p>

      <div className="flex items-center space-x-3">
        <button className="bg-blue-500 text-black px-4 py-2 flex rounded-3xl items-center space-x-2">
           <p>+ Ajouter une nouvelle tâche</p>
        </button>
          <div className="flex items-center">
            <button className="text-3xl mb-4">...</button>
          </div>
        </div>
      </div>
    </nav>
  )}
```

2. Ensuite, rendez le composant `Navbar` dans le fichier `src/app/layout.tsx` :

```tsx
   import type { Metadata } from 'next'
   import { Providers } from "@/components/redux/provider";
   import Navbar from './components/Navbar';
   import { Plus_Jakarta_Sans } from "next/font/google";
   import './globals.css'

   const pjs = Plus_Jakarta_Sans({ subsets: ["latin"], display: "swap" });

   export const metadata: Metadata = {
    title: 'Créer une application Next',
    description: 'Généré par créer une application next',
   }

   export default function RootLayout({
    children,
   }: {
    children: React.ReactNode
   }) {
   return (
    <html lang="en" className={pjs.className}>
      <body>
        <Providers>
          <Navbar />  {/* Rendre le composant ici */}
          {children}
        </Providers>
      </body>
    </html>
    )}
```

Maintenant, le composant `Navbar` est disponible globalement dans toutes les pages de l'application puisqu'il est rendu dans le composant de mise en page racine.

Après avoir implémenté ces changements, lors de la connexion à votre application sur `localhost:3000`, vous devriez observer l'interface utilisateur comme illustré dans l'image ci-dessous. 

![Marque de la barre de navigation](https://www.freecodecamp.org/news/content/images/2024/01/5-4.png)

Le texte de remplacement "Nom du tableau actuel" dans la barre de navigation sera finalement remplacé par le nom d'un tableau actif une fois que nous aurons rempli l'application avec des données.

Le bouton "Ajouter une nouvelle tâche" est conçu pour ouvrir la modale "Ajouter de nouvelles tâches", et les points de suspension à côté ouvriront un menu déroulant pour modifier et supprimer un tableau. L'implémentation de ce menu déroulant est le sujet de l'étape suivante.

3. Créez un fichier `Dropdown.tsx` dans le même dossier `components`, et collez le code suivant :

```tsx
   //src/app/components/Dropdown.tsx
   
   interface IDropdown {
    show: boolean
   }

   export default function Dropdown({ show }: IDropdown) {

    return (
      <div
        className={`${
          show ? "block" : "hidden"
        } w-48 absolute top-full bg-white
         border shadow-lg right-0 py-2 rounded-2xl`}
      >
        <div className="hover:bg-gray-300">
          <button className="text-sm px-4 py-2">Modifier le tableau</button>
        </div>
        <div className="hover:bg-gray-300">
          <button className="text-sm px-4 py-2">
            Supprimer le tableau
          </button>
        </div>
      </div>
    )}
```

Ce composant prend un paramètre `show` de type `boolean` comme prop. Le contenu du menu déroulant est affiché lorsque `show` est `true` et caché lorsqu'il est `false`.
   
Maintenant, passez au fichier `Navbar.tsx` et mettez à jour le code pour rendre le composant `Dropdown`. Faites attention aux commentaires dans l'extrait de code ci-dessous pour comprendre les mises à jour ici :
   
```tsx
   //src/app/components/Navbar.tsx
   
   'use client' // nous avons fait de ce composant un composant client puisque nous devons utiliser useState

   import Dropdown from "./Dropdown";
   import { useState } from 'react'

   export default function Navbar() {

   const [show, setShow] = useState<boolean>(false); // ceci gérera l'état de la variable show

   return (
    <nav className="bg-white border flex h-24">
      <div className="flex-none w-[18.75rem] border-r-2 flex items-center pl-[2.12rem]">
        <p className="font-bold text-3xl"> Application Kanban </p>
      </div>

      <div className="flex justify-between w-full items-center pr-[2.12rem]">
        <p className="text-black text-2xl font-bold pl-6">Nom actuel du tableau</p>

        <div className="flex items-center space-x-3">
          <button className="bg-blue-500 text-black px-4 py-2 flex rounded-3xl items-center space-x-2">
            <p>+ Ajouter une nouvelle tâche</p>
          </button>
          <div className="relative flex items-center">
            <button 
            onClick={() => setShow(!show)} // déclencher la fonction qui montre le menu déroulant ici
            className="text-3xl mb-4">...</button>
            <Dropdown show={show}/>  {/* rendre le menu déroulant ici et passer show comme prop */}
          </div>
        </div>
      </div>
    </nav>
    )}
```

Après avoir apporté ces ajustements dans votre composant `Navbar`, vous pouvez maintenant basculer le menu déroulant en cliquant sur les points de suspension :

![Basculer le menu déroulant](https://www.freecodecamp.org/news/content/images/2024/01/6-1.gif)

Dans l'étape suivante, nous implémenterons les composants qui constituent le corps de notre application, spécifiquement les composants de la barre latérale et le tableau qui affiche les tâches.

4. Pour implémenter la barre latérale, créez un fichier `Sidebar.tsx` dans le même répertoire `components`. Collez le code suivant :

```tsx
   // src/app/components/Sidebar.tsx

   export default function Sidebar() {
   return (
    <aside className="w-[18.75rem] flex-none dark:bg-dark-grey h-full py-6 pr-6">
      <p className="text-medium-grey pl-[2.12rem] text-[.95rem] font-semibold uppercase pb-3">
        {`Tous les tableaux (0)`}
      </p>
      <div className="cursor-pointer flex items-center rounded-tr-full rounded-br-full bg-blue-500 space-x-2 pl-[2.12rem] py-3 pb-3">
        <p className="text-white text-lg capitalize">Nom actuel du tableau</p>
      </div>
      <button className="flex items-center space-x-2 pl-[2.12rem] py-3">
        <p className="text-base font-bold capitalize text-main-purple">
          + Créer un nouveau tableau
        </p>
      </button>
    </aside>
   );
   }
```

5. Ensuite, créez un autre fichier nommé `BoardTasks.tsx` et collez le code ci-dessous. Ce composant contiendra le contenu d'une tâche de tableau active. Comme l'application n'est pas encore remplie de données, nous utiliserons un espace réservé qui sera remplacé par des tâches réelles plus tard.

```tsx
   // src/app/components/BoardTasks.tsx

   export default function BoardTasks() {
   return (
    <div className="overflow-x-auto overflow-y-auto w-full bg-stone-200">
      <div className="w-full h-full flex justify-center items-center">
        <div className="flex flex-col items-center">
          <p className="text-black text-sm">
            Ce tableau est vide. Créez une nouvelle colonne pour commencer.
          </p>
          <button className="bg-blue-500 text-black px-4 py-2 flex mt-6 rounded-3xl items-center space-x-2">
            <p>+ Ajouter une nouvelle colonne</p>
          </button>
        </div>
      </div>
    </div>
    );
   }
```

6. Ensuite, collez le code suivant dans votre fichier `src/app/page.tsx` pour rendre à la fois les composants `Sidebar` et `BoardTasks` :

```tsx
   import Sidebar from "./components/Sidebar";
   import BoardTasks from "./components/BoardTasks";

   export default function Home() {
   return (
    <main className="flex h-full">
      <Sidebar />
      <BoardTasks />
    </main>
   );
   }
```

Jusqu'à présent, votre structure de fichiers devrait ressembler à ce qui suit :

![Structure de fichiers de l'application Nextjs](https://www.freecodecamp.org/news/content/images/2024/01/7-2.png)

7. Enfin, dans le fichier `layout.tsx` racine, mettez à jour le style de la balise `body` comme indiqué ci-dessous :

```tsx
 // src/app/layout.tsx
   // reste du code ici
   export default function RootLayout({
   children,
   }: {
   children: React.ReactNode;
   }) {
   return (
    <html lang="en" className={pjs.className}>
      <body className='pb-24 h-screen overflow-hidden'> {/* mettre à jour le style ici*/}
        {/* reste du code ici */}
      </body>
    </html>
   );
   }
```

Cet ajustement garantit que le contenu dans le composant `BoardTasks` est défilable sur les axes x et y s'il dépasse la longueur et la largeur de l'écran.

Avec cela, la marque de notre application est complète. Votre interface utilisateur devrait ressembler à ceci si vous avez suivi :

![Marque complète de l'application Kanban](https://www.freecodecamp.org/news/content/images/2024/01/8-2.png)

La barre latérale affichera le nombre de tableaux et les noms des tableaux disponibles dans l'application. En cliquant sur différents tableaux dans la barre latérale, vous passerez au tableau sélectionné, et en cliquant sur "Créer un nouveau tableau" dans la barre latérale, vous ouvrirez la modale "Ajouter un nouveau tableau".

Juste à côté de la barre latérale, les tâches de chaque tableau seront affichées en colonnes. L'écran actuel sera affiché si le tableau n'a pas encore de tâches. Le bouton "+Ajouter une nouvelle colonne" ouvrira une modale utilisée pour ajouter une colonne à un tableau.

Toutes ces fonctionnalités seront activées lorsque nous remplirons l'application avec des données.

En continuant, la section suivante vous guidera dans l'intégration de Firebase Firestore dans votre application.

## Comment configurer Firebase Firestore

Pour intégrer Firestore dans votre application, vous devrez créer un projet Firebase en utilisant la [console Firebase](https://console.firebase.google.com/u/0/?_gl=1*1r24b4a*_ga*MTkyMjc0OTE3NC4xNjc4MDIwMDMw*_ga_CW55HF8NVT*MTcwMDMxMTAwNC4xNjUuMS4xNzAwMzExNDU0LjQ3LjAuMA..). N'hésitez pas à nommer le projet selon votre préférence, mais pour le bien de ce tutoriel, nommons-le "Kanban-app-tutorial."

Une fois le projet créé, vous serez invité à enregistrer votre application. Après l'enregistrement, installez Firebase dans votre application. Installez le package Firebase avec la commande suivante dans votre terminal :

```npm
npm install firebase
```

Maintenant, vous devez initialiser Cloud Firestore dans votre application. Créez un dossier nommé `utils` et à l'intérieur, créez un fichier `firebaseConfig.ts`. Collez votre configuration Firebase dedans comme montré ci-dessous :

```tsx
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

// Configuration Firebase de votre application web
const firebaseConfig = {
 // Collez votre configuration Firebase ici
};

// Initialiser Firebase
const app = initializeApp(firebaseConfig);
// Initialiser Firestore et l'exporter
export const db = getFirestore(app);
```

Enfin, accédez à votre projet nouvellement créé sur la plateforme cloud et créez une base de données Cloud Firestore. Ensuite, accédez à l'onglet "Règles" et modifiez les règles de lecture et d'écriture de false à true comme illustré dans l'image :

![Onglet des règles de Firestore](https://www.freecodecamp.org/news/content/images/2024/01/9-1.png)

Cela permettra à quiconque d'ajouter des données à la base de données sans restrictions. Notez que cela n'est pas recommandé pour la production - nous l'implémentons ainsi pour les besoins de cet article.  

Avec cette configuration complète, nous pouvons maintenant commencer à ajouter des données à Cloud Firestore.

## Comment ajouter des données initiales à la base de données Firestore

Notre objectif est de nous assurer que les utilisateurs ne sont pas accueillis avec un tableau vide lorsqu'ils terminent le processus d'authentification. Au lieu de cela, nous voulons leur présenter des données de tâches factices avec lesquelles ils peuvent interagir, leur permettant d'explorer les fonctionnalités de l'application.

De plus, nous visons à rendre ces données spécifiques à l'utilisateur, formant la base pour que chaque utilisateur construise en créant de nouveaux tableaux et tâches. 

Pour y parvenir, lorsqu'un nouvel utilisateur se connecte, nous générerons un nouveau document dans la base de données pour cet utilisateur.

Voici une décomposition de notre approche :

1. **Vérifier si l'utilisateur est nouveau** :
Nous devons déterminer si l'utilisateur se connecte pour la première fois. Ainsi, nous pouvons automatiquement créer un nouveau document pour l'utilisateur dans la base de données.

2. **Créer un nouveau document utilisateur** :
Si l'utilisateur est nouveau, nous procédons à la création d'une nouvelle entrée de données dans la base de données spécifiquement pour cet utilisateur.

Pour commencer, créez un fichier `data.js` à l'intérieur du dossier `utils` que nous avons créé précédemment (celui-ci contiendra nos données factices pour un tableau). Collez le code de données fourni dedans.

```tsx
//utilisé pour générer un nouvel id
export const id = () => Math.random().toString(36).substring(2, 10);

export const data = {
  "boards": [
    {
      id: id(),
      name: "Roadmap",
      columns: [
        {
          id: id(),
          name: "Now",
          tasks: [
            {
              id: id(),
              title: "Launch version one",
              status: "Now"
            },
            {
              id: id(),
              title: "Review early feedback and plan next steps for roadmap",
              status: "Now"
            }
          ]
        },
        {
          id: id(),
          name: "Next",
          tasks: []
        },
        {
          id: id(),
          name: "Later",
          tasks: []
        }
      ]
    }
  ]
}
```

Maintenant, accédez au fichier `src/app/page.tsx` et modifiez-le comme démontré ci-dessous :

```tsx
"use client";
import Sidebar from "./components/Sidebar";
import BoardTasks from "./components/BoardTasks";
// Méthodes Firestore : collection et getDocs pour la référence de document, addDoc pour ajouter un document
import { collection, getDocs, addDoc } from "firebase/firestore";
// Connecter notre application à Firestore
import { db } from "./utils/firebaseConfig";
import { useEffect, useState } from "react";
// Importer getSession de la bibliothèque next-auth pour récupérer les détails de l'utilisateur connecté
import { getSession } from "next-auth/react";
// Importer les données de data.json, utilisées pour initialiser la base de données Firestore pour les nouveaux utilisateurs
import { data } from "./utils/data.json";

export default function Home() {
  // Gérer les détails de l'utilisateur dans cet état. L'index clé dans TypeScript assure la sécurité des types.
  const [userDetails, setUserDetails] = useState<{ [key: string]: any }>();

  // Obtenir la session de l'utilisateur en utilisant getSession. Contient le nom et l'email de l'utilisateur, puis passé à l'état des détails de l'utilisateur.
  const getUserSession = async () => {
    const session = await getSession();
    if (session) {
      setUserDetails(session.user);
    }
  };

  const handleAddDoc = async () => {
    if (userDetails) {
      // Exécuter le code à l'intérieur des accolades uniquement lorsque `userDetails` est vrai.

      // Référence au document avec l'email de l'utilisateur pour vérifier son existence dans la base de données.
      const docRef = collection(db, "users", userDetails.email, "tasks");
      const getDos = await getDocs(docRef);

      // Si le document existe, terminer le programme.
      if (getDos.docs.length > 0) {
   ;     return;
      } else {
        // Si ce n'est pas le cas, soumettre un nouveau document contenant les données de data.json pour l'utilisateur dans la base de données.
        try {
          await addDoc(
            collection(db, "users", userDetails.email, "tasks"),
            data
          );
        } catch (e) {
          console.error("Erreur lors de l'ajout du document : ", e);
        }
      }
    }
  };

  useEffect(() => {
    getUserSession(); // Appeler la fonction getUserSession après le rendu de la page.
  }, []);

  useEffect(() => {
    handleAddDoc(); // Appeler la fonction handleAddDoc après la mise à jour des détails de l'utilisateur.
  }, [userDetails]);

  return (
    <main className="flex h-full">
      <Sidebar />
      <BoardTasks />
    </main>
  );
}
```

Ce code garantit que lorsqu'un utilisateur se connecte, ses détails sont récupérés et vérifiés. Si c'est un nouvel utilisateur, un nouveau document avec des données factices initiales est ajouté à la base de données Firestore sous l'email de l'utilisateur. Assurez-vous d'avoir lu les commentaires que j'ai ajoutés si vous avez besoin d'explications supplémentaires.

En visitant votre console de projet, vous remarquerez la présence d'un document créé pour l'utilisateur connecté (qui est vous) :

![Présence du document Firestore](https://www.freecodecamp.org/news/content/images/2024/01/10-1.png)

La configuration initiale est maintenant complète, nous permettant de récupérer des données et de commencer le remplissage de notre application. Mais avant d'interagir directement avec les données, nous utiliserons RTK query, qui est inclus dans le package Redux toolkit, comme intermédiaire.

Cette approche non seulement élimine le besoin d'écrire la logique de récupération et de mise en cache des données dans divers composants de manière répétée, mais élimine également la révalidation en arrière-plan, donc nous n'avons pas besoin de rafraîchissements manuels explicites. 

La section suivante explorera ce processus. 

## Comment utiliser `RTK Query` pour récupérer des données de Cloud Firestore
Ici, nous commencerons le processus de création de slices pour le réducteur, en commençant par le développement de la slice dédiée à la récupération de données.

Dans le répertoire `src/redux`, créez un nouveau dossier nommé `services`.

À l'intérieur du dossier `services` nouvellement créé, établissez un fichier nommé `apiSlice.ts`. Copiez et collez le code fourni dans ce fichier :

```tsx
   import { createApi, fakeBaseQuery } from "@reduxjs/toolkit/query/react";
   import { getSession } from "next-auth/react";
   import { collection, getDocs } from "firebase/firestore";
   import { db } from "@/components/app/utils/firebaseConfig";

   // Créer l'API Firestore en utilisant createApi
   export const fireStoreApi = createApi({
   reducerPath: "firestoreApi", // Spécifie le chemin pour le réducteur
   baseQuery: fakeBaseQuery(), // Utilise fakeBaseQuery car Firebase n'a pas de point de terminaison REST API traditionnel
   tagTypes: ["Tasks"], // Définit les types de balises pour les besoins de mise en cache
   endpoints: (builder) => ({
    fetchDataFromDb: builder.query<{ [key: string]: any }[], void>({
      // Utilise builder.query pour faire des requêtes ; builder.mutation peut être utilisé pour les opérations CRUD
      async queryFn() {
        // Utilise queryFn puisque nous ne récupérons pas de données depuis une API conventionnelle ;
        // Cela nous permet d'inclure du code arbitraire, tant que nous retournons nos données au format { data: results }

        try {
          const session = await getSession();
          const { user } = session!;
            const ref = collection(db, `users/${user?.email}/tasks`);
            const querySnapshot = await getDocs(ref);
            return { data: querySnapshot.docs.map((doc) => doc.data()) };
            // Les données doivent être retournées dans ce format lors de l'utilisation de queryFn
          
        } catch (e) {
          return { error: e };
        }
      },
      providesTags: ["Tasks"], // Spécifie les balises pour la mise en cache
    }),
   }),
   });

   // Exporter les hooks pour utiliser le point de terminaison créé
   export const { useFetchDataFromDbQuery } = fireStoreApi;
```
   
Ce code établit une API Firestore en utilisant `createApi`, définissant un point de terminaison pour la récupération de données. L'utilisation de `fakeBaseQuery` est intentionnelle, considérant que Firebase n'a pas d'URL de base conventionnelle. 

Le code intègre également la mise en cache et l'invalidation via des balises. Dans cette slice, nous avons spécifié `tagTypes` comme `'Tasks'`. Dans les sections suivantes, nous explorerons comment l'invalidation et le rafraîchissement peuvent être effectués via des balises.

Dans la slice, `endpoints` peut être perçu comme des points de terminaison d'API. Les fonctions définies dans cette fonction `endpoints` seront exportées sous la forme `use...Query` si c'est une fonction `builder.query` (comme dans ce cas, `useFetchDataFromDbQuery`), et `use...Mutation` si c'est une fonction `builder.mutation` (plus d'informations à ce sujet plus tard).

Maintenant, nous allons poser les bases pour incorporer les slices que nous générons dans le magasin Redux. Puisque nous créerons plusieurs `slices` à l'avenir, il est prudent de les compiler dans un fichier dédié en utilisant `combineReducers`.

Ensuite, créez un fichier `rootReducer.ts` dans le dossier `src/redux`. Intégrez l'extrait de code suivant dans ce fichier pour intégrer le `apiSlice` précédemment créé :

```tsx
  import { combineReducers } from "@reduxjs/toolkit";
   import { fireStoreApi } from "./services/apiSlice";

   export const rootReducer = combineReducers({
    [fireStoreApi.reducerPath]: fireStoreApi.reducer,
   });
```

Dans cet extrait, nous avons importé le `apiSlice` créé précédemment et l'avons inclus dans la fonction `combineReducers`, en spécifiant la paire clé-valeur comme `[fireStoreApi.reducerPath]: fireStoreApi.reducer`. 

Cette configuration garantit que l'état géré par le `apiSlice` est effectivement intégré dans le magasin Redux. 
   
Enfin, nous ajouterons le `rootReducer` au magasin Redux ici. Accédez à `src/redux/store.ts` et modifiez-le comme suit :
  
```tsx  
import { configureStore } from "@reduxjs/toolkit";
   import { setupListeners } from "@reduxjs/toolkit/dist/query";
   import { rootReducer } from "./rootReducer";
   import { fireStoreApi } from "./services/apiSlice";

   export const store = configureStore({
    reducer: rootReducer,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(fireStoreApi.middleware),
   });
   setupListeners(store.dispatch)
   export type RootState = ReturnType<typeof store.getState>;
   export type AppDispatch = typeof store.dispatch;
```

Ici, nous intégrons notre `rootReducer` dans le magasin et passons le `fireStoreApi.middleware` à la prop `middleware` de la fonction `configureStore`. Cela garantit que le magasin Redux utilise le `middleware` pour faire des requêtes à Firestore.
   
Maintenant, nous pouvons commencer en toute sécurité le processus de récupération et de remplissage de notre application avec des données, ce qui sera le sujet de la section à venir.

## Comment récupérer et remplir les données

Notre approche commence par le remplissage des données dans le composant `Navbar`, suivi de la `Sidebar`, et enfin, le `BoardTasks`.

### Comment remplir la barre de navigation

Pour la barre de navigation, nous voulons afficher le nom du tableau actuel. Mais comme nous aurons besoin de cette information dans d'autres parties de l'application, nous la stockerons également de manière centrale dans le magasin Redux.

Pour y parvenir, nous créerons une nouvelle slice appelée `appSlice`, qui gérera l'état lié au nom du tableau actuel. Cette slice sera également responsable de la gestion de la logique et de l'état non liés aux appels API.

Tout d'abord, créez un dossier `features` dans le répertoire `src/redux`.

À l'intérieur du dossier features, créez un fichier nommé `appSlice.ts` et collez le code suivant :

```tsx
   import { createSlice, PayloadAction } from "@reduxjs/toolkit";
   import { RootState } from "../store";

   // Définir l'état initial pour la slice
   const initialState = {
    currentBoardName: "",
   };

   export const features = createSlice({
   // Nom de la slice
   name: "features",
   initialState,
   // Les fonctions qui mettent à jour l'initialState sont écrites à l'intérieur de l'objet reducers
   reducers: {
    // Cette fonction met à jour le nom du tableau lorsqu'elle est appelée
    setPageTitle: (state, action: PayloadAction<string>) => {
      state.currentBoardName = action.payload;
    },
   },
   });

   // Exporter les fonctions définies à l'intérieur des reducers ici
   export const { setPageTitle } = features.actions;

   // Fonction sélecteur pour récupérer le nom du tableau actuel depuis l'état
   export const getPageTitle = (state: RootState) => state.features.currentBoardName;

   // Exporter le reducer pour une utilisation dans le magasin Redux
   export default features.reducer;
```

Ce code définit la slice `appSlice`, qui inclut l'état initial, les `reducers` et les `actions` pour gérer le nom du tableau actuel.

Pour rendre la `appSlice` disponible globalement, nous devons l'intégrer dans le magasin Redux. Ouvrez le fichier `src/redux/rootReducer.ts` et modifiez-le comme suit :

```tsx
   // src/redux/rootReducer.ts
   import { combineReducers } from "@reduxjs/toolkit";
   import { fireStoreApi } from "./services/apiSlice";
   import  featuresReducer  from "./features/appSlice";

   export const rootReducer = combineReducers({
   //ajoutez la slice features ici
   features: featuresReducer,
   [fireStoreApi.reducerPath]: fireStoreApi.reducer,
   });
```
  
Ce `rootReducer` mis à jour inclut désormais le `featuresReducer`, rendant la `appSlice` disponible dans toute l'application.

Ensuite, nous devons mettre à jour le composant `Navbar` pour récupérer le nom du tableau actuel depuis le magasin Redux et l'afficher. Ouvrez le fichier `app/components/Navbar.tsx` et apportez les modifications suivantes :

```tsx
  'use client' 

   import Dropdown from "./Dropdown";
   import { useState, useEffect } from 'react'
   // Importer les fonctions et sélecteurs Redux pour gérer les noms des tableaux
   import { setCurrentBoardName, getCurrentBoardName } from '../../redux/features/appSlice'
   import { useAppDispatch, useAppSelector } from '@/components/redux/hooks'
   // Importer le hook de récupération de données depuis la slice API
   import { useFetchDataFromDbQuery } from "@/components/redux/services/apiSlice";

   export default function Navbar() {
    const [show, setShow] = useState<boolean>(false);
   // Déstructuration pour extraire les données du hook useFetchDataFromDbQuery
   const { data } = useFetchDataFromDbQuery();
   // Accéder à la fonction dispatch de Redux pour appeler des actions
   const dispatch = useAppDispatch();

   // Hook d'effet pour exécuter lorsque les données sont mises à jour
   useEffect(() => {
    if (data) {
      // Lorsque l'utilisateur se connecte, définir le currentBoardName sur le nom du premier tableau
      const activeBoard = data[0].boards[0];
      dispatch(setCurrentBoardName(activeBoard.name));
    }
   }, [data]);

   // Sélectionner le nom du tableau actuel depuis le magasin Redux
   const currentBoardName = useAppSelector(getCurrentBoardName);

   return (
    <nav className="bg-white border flex h-24">
      <div className="flex-none w-[18.75rem] border-r-2 flex items-center pl-[2.12rem]">
        <p className="font-bold text-3xl"> Application Kanban </p>
      </div>

      <div className="flex justify-between w-full items-center pr-[2.12rem]">
        {/* remplir le nom du tableau actuel dans la barre de navigation */}
        <p className="text-black text-2xl font-bold pl-6">{currentBoardName}</p>

        <div className="flex items-center space-x-3">
          <button className="bg-blue-500 text-black px-4 py-2 flex rounded-3xl items-center space-x-2">
            <p>+ Ajouter une nouvelle tâche</p>
          </button>
          <div className="relative flex items-center">
            <button onClick={() => setShow(!show)} className="text-3xl mb-4">
              ...
            </button>
            <Dropdown show={show} />
          </div>
        </div>
      </div>
    </nav>
   );
   }
```
   
Après ces mises à jour, votre barre de navigation devrait maintenant afficher le nom du tableau actuel, qui est "Roadmap" :

![Afficher le nom du tableau sur la barre de navigation](https://www.freecodecamp.org/news/content/images/2024/01/11-1.png)

### Comment remplir la barre latérale

Une fois remplie avec des données, la barre latérale affichera le nombre de tableaux et les noms des tableaux disponibles dans l'application. En cliquant sur différents tableaux dans la barre latérale, vous basculerez vers le tableau sélectionné. 

Bien que nous n'ayons actuellement qu'un seul tableau disponible dans les données, nous poserons les bases de ces fonctionnalités pour prendre en charge plusieurs tableaux à l'avenir. 

Accédez au composant `Sidebar` et apportez les modifications suivantes comme indiqué ci-dessous :

```tsx
import { useState } from "react";
import { useAppDispatch } from "@/components/redux/hooks";
import { useFetchDataFromDbQuery } from "@/components/redux/services/apiSlice";
import { setCurrentBoardName } from "@/components/redux/features/appSlice";

export default function Sidebar() {
  // État pour suivre l'index du tableau actif pendant la navigation
  const [active, setActive] = useState<number>(0);

  const { data } = useFetchDataFromDbQuery();
  const dispatch = useAppDispatch();

  // Fonction pour gérer la navigation à travers les tableaux
  const handleNav = (index: number, name: string) => {
    setActive(index);
    dispatch(setCurrentBoardName(name));
  };

  return (
    <aside className="w-[18.75rem] flex-none dark:bg-dark-grey h-full py-6 pr-6">
      {data && (
        <>
          {/* Afficher le nombre de tableaux disponibles dans les données */}
          <p className="text-medium-grey pl-[2.12rem] text-[.95rem] font-semibold uppercase pb-3">
            {`Tous les tableaux (${data[0]?.boards.length})`}
          </p>
          {/* Afficher les noms de chaque tableau */}
          {data[0]?.boards.map(
            (board: { [key: string]: any }, index: number) => {
              const { name, id } = board;
              const isActive = index === active; // Vérifier si le tableau est actif
              return (
                <div
                  key={id}
                  onClick={() => handleNav(index, name)} // Gérer la navigation à travers les tableaux au clic
                  className={`${
                    isActive ? 'rounded-tr-full rounded-br-full bg-blue-500 text-white' : 'text-black'
                  } cursor-pointer flex items-center 
                  space-x-2 pl-[2.12rem] py-3 pb-3`}
                >
                  <p className="text-lg capitalize">{name}</p>
                </div>
              );
            }
          )}
        </>
      )}
      <button className="flex items-center space-x-2 pl-[2.12rem] py-3">
        <p className="text-base font-bold capitalize text-main-purple">
          + Créer un nouveau tableau
        </p>
      </button>
    </aside>
  );
}
```

Avec le code ci-dessus, nous avons préparé la barre latérale pour gérer plusieurs tableaux à l'avenir. Lorsque plusieurs tableaux sont disponibles dans les données, la barre latérale les affichera dynamiquement, permettant aux utilisateurs de basculer entre eux de manière transparente.

Jusqu'à présent, votre interface utilisateur de la barre latérale devrait refléter ces mises à jour :

![Barre latérale remplie](https://www.freecodecamp.org/news/content/images/2024/01/12-1.png)

En continuant, dans la section suivante, nous remplirons le composant `BoardTasks`.

### Comment remplir le composant `BoardTasks`

Dans cette section, l'objectif est de présenter un maximum de sept colonnes de tâches à l'écran. S'il y a moins de sept colonnes, nous afficherons une option pour en ajouter davantage. De plus, nous voulons avoir une indication d'une colonne vide pour les colonnes sans tâches.

Chaque carte de tâche doit comporter des icônes d'édition et de suppression. Celles-ci serviront de placeholders pour les fonctionnalités de modales à venir.

Pour implémenter ces changements, allez dans le composant `BoardTasks` et apportez les mises à jour suivantes :

```tsx
import { useEffect, useState } from "react";
import { useFetchDataFromDbQuery } from "@/components/redux/services/apiSlice";
import { useAppSelector } from "@/components/redux/hooks";
import { getCurrentBoardName } from "@/components/redux/features/appSlice";
import { MdEdit, MdDelete } from "react-icons/md";

// Définir les types pour les données des tâches
interface ITask {
  title: string;
  description: string;
  status: string;
}

// Définir les types pour les données dans chaque colonne
interface Column {
  name: string;
  tasks?: ITask[];
}

export default function BoardTasks() {
  // Obtenir l'état de chargement et les données de l'endpoint useFetchDataFromDbQuery
  const { isLoading, data } = useFetchDataFromDbQuery();
  // Gérer les données des colonnes dans l'état des colonnes
  const [columns, setColumns] = useState<Column[]>([]);
  // Obtenir le nom du tableau actif depuis le magasin redux
  const activeBoard = useAppSelector(getCurrentBoardName);

  // Une fois que les données sont récupérées avec succès, cette fonction dans le useEffect s'exécute
  useEffect(() => {
    if (data !== undefined) {
      const [boards] = data;
      if (boards) {
        // Obtenir les données du tableau actif
        const activeBoardData = boards.boards.find(
          (board: { name: string }) => board.name === activeBoard
        );
        if (activeBoardData) {
          const { columns } = activeBoardData;
          setColumns(columns);
        }
      }
    }
  }, [data, activeBoard]);

  return (
    <div className="overflow-x-auto overflow-y-auto w-full p-6 bg-stone-200">
      {/* Si les données n'ont pas été récupérées avec succès, afficher un état de chargement, sinon afficher la colonne des tâches */}
      {isLoading ? (
        <p className="text-3xl w-full text-center font-bold">Chargement des tâches...</p>
      ) : (
        <>
          {/* Si les colonnes de tâches ne sont pas vides : afficher les tâches, sinon afficher l'invitation à ajouter une nouvelle colonne */}
          {columns.length > 0 ? (
            <div className="flex space-x-6">
              {columns.map((column) => {
                const { id, name, tasks } = column;
                return (
                  <div key={id} className="w-[17.5rem] shrink-0">
                    <p className="text-black">{`${name} (${
                      tasks ? tasks?.length : 0
                    })`}</p>

                    {tasks &&
                      // Afficher les tâches s'il y a des tâches dans la colonne, sinon afficher une colonne vide
                      (tasks.length > 0 ? (
                        tasks.map((task) => {
                          const { id, title, status } = task;

                          return (
                            <div
                              key={id}
                              className="bg-white p-6 rounded-md mt-6 flex items-center justify-between border"
                            >
                              <p>{title}</p>
                              <div className="flex items-center space-x-1">
                                <MdEdit className="text-lg cursor-pointer" />
                                <MdDelete className="text-lg cursor-pointer text-red-500" />
                              </div>
                            </div>
                          );
                        })
                      ) : (
                        <div className="mt-6 h-full rounded-md border-dashed border-4 border-white" />
                      ))}
                  </div>
                );
              })}
              {/* Si le nombre de colonnes de tâches est inférieur à 7, afficher une option pour ajouter plus de colonnes */}
              {columns.length < 7 ? (
                <div className="rounded-md bg-white w-[17.5rem] mt-12 shrink-0 flex justify-center items-center">
                  <p className="cursor-pointer font-bold text-black text-2xl">
                    + Nouvelle colonne
                  </p>
                </div>
              ) : (
                ""
              )}
            </div>
          ) : (
            <div className="w-full h-full flex justify-center items-center">
              <div className="flex flex-col items-center">
                <p className="text-black text-sm">
                  Ce tableau est vide. Créez une nouvelle colonne pour commencer.
                </p>
                <button className="bg-blue-500 text-black px-4 py-2 flex mt-6 rounded-3xl items-center space-x-2">
                  <p>+ Ajouter une nouvelle colonne</p>
                </button>
              </div>
            </div>
          )}
        </>
      )}
    </div>
  );
}
```

Après avoir apporté ces modifications, votre interface utilisateur devrait maintenant refléter les changements comme démontré dans le GIF ci-dessous :

![Composant BoardTasks rempli](https://www.freecodecamp.org/news/content/images/2024/01/13.gif)

Ensuite, nous nous concentrerons sur l'implémentation des opérations CRUD (Create, Read, Update, et Delete) dans notre application.

## Comment implémenter les opérations CRUD

Avant de plonger dans l'implémentation des fonctionnalités CRUD dans notre application, nous devons établir le point de terminaison de mutation `updateBoardToDb` dans le `apiSlice`. Ce point de terminaison nous permettra d'apporter les mises à jour nécessaires à notre base de données pour les actions CRUD.

Intégrez le code suivant dans votre fichier `redux/services/apiSlice.ts` pour inclure le point de terminaison de mutation :

```tsx
import { createApi, fakeBaseQuery } from "@reduxjs/toolkit/query/react";
import { getSession } from "next-auth/react";
// importation supplémentaire de la méthode doc et updateDoc de firestore pour obtenir la référence du document utilisateur et mettre à jour le document, respectivement
import { collection, doc, getDocs, updateDoc } from "firebase/firestore";
import { db } from "@/components/app/utils/firebaseConfig";

export const fireStoreApi = createApi({
  reducerPath: "firestoreApi",
  baseQuery: fakeBaseQuery(),
  tagTypes: ["Tasks"],
  endpoints: (builder) => ({
    fetchDataFromDb: builder.query<{ [key: string]: any }[], void>({
      async queryFn() {
        try {
          const session = await getSession();
          if (session?.user) {
            const { user } = session;
            const ref = collection(db, `users/${user.email}/tasks`);
            const querySnapshot = await getDocs(ref);
            return { data: querySnapshot.docs.map((doc) => doc.data()) };
          }
        } catch (e) {
          return { error: e };
        }
      },
      providesTags: ["Tasks"],
    }),
    // point de terminaison pour les actions CRUD
    updateBoardToDb: builder.mutation({
      async queryFn(boardData) {
        try {
          const session = await getSession();
          if (session?.user) {
            const { user } = session;
            const ref = collection(db, `users/${user.email}/tasks`);
            const querySnapshot = await getDocs(ref);
            const boardId = querySnapshot.docs.map((doc) => {
              return doc.id;
            });
            await updateDoc(doc(db, `users/${user.email}/tasks/${boardId}`), {
              boards: boardData,
            });
          }
          return { data: null };
        } catch (e) {
          return { error: e };
        }
      },
      invalidatesTags: ["Tasks"], // ceci sera utilisé pour invalider les données initialement récupérées. 
      // Les données devront être récupérées à nouveau une fois que ce point de terminaison a été appelé
    }),
  }),
});

// Exporter les hooks pour utiliser le point de terminaison créé
export const { useFetchDataFromDbQuery, useUpdateBoardToDbMutation } =
  fireStoreApi;
```

Lors de l'appel du point de terminaison `useUpdateBoardToDbMutation`, nos données de base de données seront mises à jour en conséquence. 

Après chaque mise à jour, Redux effectue automatiquement des rafraîchissements en arrière-plan pour garantir que nous travaillons avec les dernières données. Cette fonctionnalité est activée par la propriété `invalidatesTags` que nous avons passée au point de terminaison `updateBoardToDb`.

Ayant implémenté avec succès le point de terminaison CRUD, notre prochaine étape consiste à implémenter les fonctionnalités d'ajout et d'édition de tableaux.

### Comment ajouter et éditer un tableau

Une fois que nous avons terminé l'implémentation de l'interface utilisateur, la modale pour ajouter un nouveau tableau devrait ressembler à ce qui suit :

![modale d'ajout de tableau](https://www.freecodecamp.org/news/content/images/2024/01/14.png)

De même, pour éditer un tableau :

![modale d'édition de tableau](https://www.freecodecamp.org/news/content/images/2024/01/15.png)

Si vous regardez les images ci-dessus, vous pouvez voir que les deux modales se ressemblent beaucoup, différant seulement par leurs titres. 

Cela présente une excellente opportunité d'implémenter le concept DRY (Don't Repeat Yourself) en programmation. En quelques étapes, nous explorerons comment exploiter une seule modale pour remplir les deux objectifs.

Tout d'abord, nous utiliserons la bibliothèque [`react-modal`](https://www.npmjs.com/package/react-modal) pour créer un composant de modale personnalisé. Cela nous permet d'éviter de construire à partir de zéro. 
  
Pour commencer, installez la bibliothèque `react-modal` en exécutant la commande suivante :
 
 ```npm
 npm i react-modal
 ```
     
Ensuite, créez un fichier `Modal.tsx` dans le répertoire `app/components` et ajoutez le code fourni. Ce code définit un composant de modale personnalisé avec un style.
 
```tsx 
import ReactModal from "react-modal";

interface ModalProps {
  children?: React.ReactNode;
  isOpen: boolean;
  onRequestClose: () => void;
}

ReactModal.setAppElement("*");

export function Modal({ children, isOpen, onRequestClose }: ModalProps) {
  const modalStyle = {
    overlay: {
      zIndex: "900000",
      backgroundColor: "rgba(0,0,0,0.45)",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
    },
    content: {
      top: "50%",
      left: "50%",
      right: "auto",
      bottom: "auto",
      marginRight: "-50%",
      transform: "translate(-50%, -50%)",
      padding: "0px",
      borderRadius: ".5rem",
      width: "auto",
      backgroundColor:  "#fff",
      border: "none",
    },
  };

  return (
    <ReactModal
      onRequestClose={onRequestClose}
      isOpen={isOpen}
      style={modalStyle}
    >
      {children}
    </ReactModal>
  );
}

interface ModalBody {
  children: React.ReactNode;
}

export function ModalBody({ children }: ModalBody) {
  return <form className="w-[21.4rem] md:w-[30rem] p-8">{children}</form>;
}
```
	
Dans ce code, nous avons implémenté et stylisé le calque et le corps (contenu) de la modale.
	
Maintenant, créez un dossier nommé `AddAndEditBoardModal.tsx` et collez le code fourni dedans comme espace réservé. Ne vous inquiétez pas des lignes ondulées rouges que vous obtenez dans votre éditeur de code pour l'instant - nous les aborderons dans un instant.

```tsx
   import { Modal, ModalBody } from "./Modal";

   export default function AddAndEditBoardModal() {

    return (
      <Modal isOpen onRequestClose>
        <ModalBody>
         <p>Ajouter et Modifier la Modale du Tableau</p>
        </ModalBody>
      </Modal>
    );
   }
```

Dans ce code, nous avons importé notre composant de modale personnalisé, et nous l'avons enveloppé autour d'un texte espace réservé.
	
Ensuite, rendez le composant de modale nouvellement créé dans le composant `app/page.tsx` :

```tsx
   // reste des imports ici
   import AddAndEditBoardModal from "./components/AddAndEditBoardModal";
   // reste du code ici
   export default function Home() {
   return (
    <main className="flex h-full">
      <Sidebar />
      <BoardTasks />
      {/* rendre le composant de modale ici */}
      <AddAndEditBoardModal />
    </main>
   );
   }
```
	
Dans cette étape, nous avons créé un espace réservé pour le composant `AddAndEditBoardModal` et l'avons rendu dans le composant `Page.tsx`. 

Ensuite, nous implémenterons les fonctions pour déclencher la modale et gérer l'état d'ouverture et de fermeture dans le magasin redux afin de maintenir un code propre et d'éviter le perçage de props.

Accédez à votre fichier `redux/features/appSlice.ts` et mettez-le à jour avec le code ci-dessous :

   ```tsx
   import { createSlice, PayloadAction } from "@reduxjs/toolkit";
   import { RootState } from "../store";

   const initialState = {
   currentBoardName: "",
   // Gérer l'état pour l'ouverture et la fermeture de la modale Ajouter et Modifier le Tableau
   isAddAndEditBoardModal: { isOpen: false, variant: "" },
   };

   export const features = createSlice({
    name: "features",
    initialState,

    reducers: {
     setCurrentBoardName: (state, action: PayloadAction<string>) => {
      state.currentBoardName = action.payload;
    },
    // Ouvrir la modale Ajouter et Modifier le Tableau avec une variante spécifiée (ajouter ou modifier)
    openAddAndEditBoardModal: (state, { payload }) => {
      state.isAddAndEditBoardModal.isOpen = true;
      // Définir le type de modale à ouvrir (ajouter un tableau ou modifier un tableau) en fonction du paramètre variant
      state.isAddAndEditBoardModal.variant = payload;
    },
    // Fermer la modale Ajouter et Modifier le Tableau
    closeAddAndEditBoardModal: (state) => {
      state.isAddAndEditBoardModal.isOpen = false;
      state.isAddAndEditBoardModal.variant = "";
    },
   },
   });
   export const {
   setCurrentBoardName,
   openAddAndEditBoardModal,
   closeAddAndEditBoardModal,
   } = features.actions;
   export const getCurrentBoardName = (state: RootState) => state.features.currentBoardName;
   // Fonctions sélecteurs pour récupérer la valeur isOpen de l'état de l'état isAddAndRditBoardModal
   export const getAddAndEditBoardModalValue = (state: RootState) => state.features.isAddAndEditBoardModal.isOpen;
   // Fonctions sélecteurs pour récupérer la valeur isOpen de l'état de l'état isAddAndRditBoardModal
   export const getAddAndEditBoardModalVariantValue = (state: RootState) => state.features.isAddAndEditBoardModal.variant;
   // Exporter le réducteur pour une utilisation dans le magasin Redux
   export default features.reducer;
   ```

Ensuite, revenez au composant `AddAndEditBoardModal.tsx` et mettez-le à jour comme indiqué ci-dessous :
    
   ```tsx  
   import { Modal, ModalBody } from "./Modal";
   import { useAppSelector, useAppDispatch } from "@/components/redux/hooks";
   //import des fonctions nécessaires depuis appSlice
   import {
   getAddAndEditBoardModalValue,
   getAddAndEditBoardModalVariantValue,
   closeAddAndEditBoardModal,
   } from "@/components/redux/features/appSlice";

   export default function AddAndEditBoardModal() {
   // obtenir la variante de la modale
   const modalVariant = useAppSelector(getAddAndEditBoardModalVariantValue);
   const dispatch = useAppDispatch();
   // ouvre cette modale si isOpen est évalué à vrai
   const isOpen = useAppSelector(getAddAndEditBoardModalValue);
   // fermer la modale
   const closeModal = () => dispatch(closeAddAndEditBoardModal());

   return (
    <Modal isOpen={isOpen} onRequestClose={closeModal}>
      <ModalBody>
        {/* afficher la variante(titre) de la modale */}
        <p>{modalVariant}</p>
      </ModalBody>
    </Modal>
   );
   }
   ```
   
Après ces mises à jour, nous pouvons implémenter en toute sécurité le déclencheur pour la modale d'ajout et d'édition de tableau.
   
Ensuite, accédez au composant `Sidebar` et mettez à jour le bouton avec le texte "+ Créer un nouveau tableau" pour qu'il ouvre la modale "Ajouter un tableau" lorsqu'il est cliqué : 
    
   ```tsx
   // ajoutez ceci aux imports
   import { openAddAndEditBoardModal } from "@/components/redux/features/appSlice";

   export default function Sidebar() {
    // reste du code ici
   return (
     <aside className="w-[18.75rem] flex-none dark:bg-dark-grey h-full py-6 pr-6">
       {/* reste du code ici */}
       {/* déclencher la modale de création d'un nouveau tableau */}
       <button
         onClick={() => dispatch(openAddAndEditBoardModal("Ajouter un nouveau tableau"))}
         className="flex items-center space-x-2 pl-[2.12rem] py-3"
       >
         <p className="text-base font-bold capitalize text-main-purple">
           + Créer un nouveau tableau
         </p>
       </button>
     </aside>
   );
   }
   ```
 
Maintenant, en cliquant sur le bouton "+ Créer un nouveau tableau" dans la barre latérale, la modale contenant le texte "Ajouter un nouveau tableau" devrait apparaître. Vous devriez également pouvoir la fermer en cliquant sur le calque :

![La modale d'ajout d'un nouveau tableau apparaît](https://www.freecodecamp.org/news/content/images/2024/01/16.gif)

Ensuite, nous implémenterons le déclencheur pour la modale d'édition de tableau.
   
Accédez au composant `app/components/Dropdown.tsx` et mettez à jour le bouton "Modifier le tableau" comme suit :

   ```tsx   
   import { useAppDispatch } from '@/components/redux/hooks'
   import { openAddAndEditBoardModal } from '@/components/redux/features/appSlice';

   interface IDropdown {
    show: boolean
   }
   
   export default function Dropdown({ show }: IDropdown) {

    const dispatch = useAppDispatch()
    
    return (
      <div
        className={`${
          show ? "block" : "hidden"
        } w-48 absolute top-full bg-white
         border shadow-lg right-0 py-2 rounded-2xl`}
      >
        <div className="hover:bg-gray-300">
		{/* déclencher la modale Modifier le tableau ici */}
          <button
           onClick={() => dispatch(openAddAndEditBoardModal('Modifier le tableau'))}
           className="text-sm px-4 py-2">Modifier le tableau</button>
        </div>
        <div className="hover:bg-gray-300">
          <button className="text-sm px-4 py-2">
            Supprimer le tableau
          </button>
        </div>
      </div>
    );
   } 
   ```
   
Après cette mise à jour, en cliquant sur le bouton "Modifier le tableau" dans le menu déroulant, la modale d'édition de tableau s'ouvrira, comme illustré dans le GIF ci-dessous :

![La modale d'édition de tableau apparaît](https://www.freecodecamp.org/news/content/images/2024/01/17.gif)

L'option d'ajouter une nouvelle colonne au composant `BoardTasks` devrait également ouvrir cette modale lorsqu'elle est cliquée. Donc, accédez au composant `BoardTasks` et importez la fonction `openAddEditBoardModal` et le hook `useAppDispatch` depuis `appSlice` et les hooks redux, respectivement. 
   
Ensuite, déclarez la fonction dispatch dans le composant avec cette instruction : `const dispatch = useAppDispatch()`
   
Enfin, mettez à jour l'élément `div` "+Nouvelle colonne" pour ouvrir la modale "Modifier le tableau" lorsqu'il est cliqué :

 ```tsx  
   // reste du code 
    <div
    onClick={() => dispatch(openAddAndEditBoardModal("Modifier le tableau"))
    className="rounded-md bg-white w-[17.5rem] mt-12 shrink-0 flex justify-center items-center">
   <p className="cursor-pointer font-bold text-black text-2xl">  + Nouvelle colonne </p>
   </div>
   //reste du code
```

Après ces mises à jour, la modale "Modifier le tableau" devrait s'ouvrir lorsque la carte "+Nouvelle colonne" est cliquée :
   
![La modale d'édition de tableau apparaît](https://www.freecodecamp.org/news/content/images/2024/01/18.gif)

Dans les étapes à venir, nous construirons la marque complète et les fonctionnalités de notre modale.

En se référant aux images des deux modales présentées au début de cette section, dans la modale "Ajouter un nouveau tableau", les champs pour le nom du tableau et des colonnes doivent être vides. En revanche, la modale "Modifier le tableau" doit afficher le nom et les colonnes existants du tableau et doit être modifiable.

Le bouton "+ Ajouter une nouvelle colonne" dans les deux modales permet l'ajout de plus de champs aux colonnes du tableau, et ensuite, les données mises à jour sont envoyées à la base de données.  
   
Gardez à l'esprit que, étant donné la nature centrée sur le frontend de ce projet, une partie importante de la logique métier sera gérée sur le frontend. Cependant, ne vous inquiétez pas ; nous prendrons ce code snippet par snippet jusqu'à ce que nous implémentions toutes les fonctionnalités.

Pour commencer, mettez à jour le composant `AddAndEditBoardModal` en collant le code ci-dessous :

```tsx
import { useState, useEffect } from "react";
import { Modal, ModalBody } from "./Modal";
import { useAppSelector, useAppDispatch } from "@/components/redux/hooks";
//import des fonctions nécessaires depuis appSlice
import {
  getAddAndEditBoardModalValue,
  getAddAndEditBoardModalVariantValue,
  closeAddAndEditBoardModal,
  getCurrentBoardName,
} from "@/components/redux/features/appSlice";
import {
  useFetchDataFromDbQuery,
  useUpdateBoardToDbMutation,
} from "@/components/redux/services/apiSlice";
import { FaTimes } from "react-icons/fa";
import { id } from '../utils/data'
// définir les types pour boarddata
interface IBoardData {
  id: string,
  name: string;
  columns: {
    id: string;
    name: string;
    columns?: { name: string; tasks?: { [key: string]: any }[] };
  }[];
}
// données factices pour ajouter un tableau pour la modale "Ajouter un tableau"
let addBoardData = {
  id: id(),
  name: "",
  columns: [
    {
      id: id(),
      name: "",
      tasks:
 [],
    },
  ],};

export default function AddAndEditBoardModal() {
// reste du code
}
 ```

Ici, nous avons fait les imports nécessaires et défini un type pour les données du tableau - que nous utiliserons lors du remplissage de la modale. Nous avons également implémenté des données factices pour la modale d'ajout de tableau. Nous verrons comment cela sera utile dans un instant. 

Ensuite, allez dans la fonction `AddAndEditBoardModal` et collez le code suivant pour déclarer les variables et les valeurs d'état. Les commentaires expliquent l'utilisation future de chacune des déclarations.

```tsx
 //gérer l'état des données du tableau
  const [boardData, setBoardData] = useState<IBoardData>();
  // vérifier si le champ du nom du tableau est vide
  const [isBoardNameEmpty, setIsBoardNameEmpty] = useState<boolean>(false);
  // sera utilisé pour vérifier si l'un des champs de colonne du tableau est vide
  const [emptyColumnIndex, setEmptyColumnIndex] = useState<number>();

  // obtenir la variante de la modale
  const modalVariant = useAppSelector(getAddAndEditBoardModalVariantValue);
  // vérifier le type de la modale ouverte, qu'il s'agisse d'ajouter un nouveau tableau ou de modifier un tableau
  const isVariantAdd = modalVariant === "Ajouter un nouveau tableau";
  const dispatch = useAppDispatch();
  // ouvre cette modale si isOpen est évalué à vrai
  const isOpen = useAppSelector(getAddAndEditBoardModalValue);
  const currentBoardTitle = useAppSelector(getCurrentBoardName);
  // fermer la modale
  const closeModal = () => dispatch(closeAddAndEditBoardModal());
  // Récupérer les données de la base de données pour remplir la modale d'édition du tableau
  let { data } = useFetchDataFromDbQuery();
  // Hook de mutation pour mettre à jour le tableau dans la base de données
  const [updateBoardToDb, { isLoading }] = useUpdateBoardToDbMutation();
```

Ici, nous implémenterons les fonctions qui seront responsables de la fonctionnalité de la modale. Collez le code suivant juste en dessous des déclarations ci-dessus :

```tsx
  // Effet pour définir les données initiales de la modale en fonction de la variante
  useEffect(() => {
    if (data) {
      
      if (isVariantAdd) {
        setBoardData(addBoardData);
      } else {
        const activeBoard = data[0].boards.find(
          (board: { name: string }) => board.name === currentBoardTitle
        );
        setBoardData(activeBoard);
      }
    }
  }, [data, modalVariant]);

  // Effet pour effacer les messages d'erreur après un certain temps
  useEffect(() => {
    const timeoutId = setTimeout(() => {
      setIsBoardNameEmpty(false);
      setEmptyColumnIndex(undefined);
    }, 3000);
    return () => clearTimeout(timeoutId);
  }, [emptyColumnIndex, isBoardNameEmpty]);

  // Gestionnaire de changement de nom de tableau
  const handleBoardNameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (boardData) {
      const newName = { ...boardData, name: e.target.value };
      setBoardData(newName);
    }
  };

  // Gestionnaire de changement de nom de colonne. Ces types de fonctions sont appelés fermetures

  const handleColumnNameChange = (index: number) => {
    return function (e: React.ChangeEvent<HTMLInputElement>) {
      // gérer le changement pour la modale de création d'un nouveau tableau
      if (boardData) {
        const modifyColumns = boardData.columns.map((column, columnIndex) => {
          if (columnIndex === index) {
            return { ...column, name: e.target.value };
          }
          return column;
        });
        const modifiedColumn = { ...boardData, columns: modifyColumns };
        setBoardData(modifiedColumn);
      }
    };
  };

  // Gestionnaire pour ajouter une nouvelle colonne au formulaire
  const handleAddNewColumn = () => {
    // nombre maximum de colonnes que nous voulons avoir dans un tableau est de 7
    if (boardData && boardData.columns.length < 6) {
      // Faire une copie des boardData existants
      const updatedBoardData = { ...boardData };
      // Créer un nouvel objet colonne
      const newColumn = { id: id(), name: "", tasks: [] };
      // Pousser la nouvelle colonne dans le tableau des colonnes dans la copie
      updatedBoardData.columns = [...updatedBoardData.columns, newColumn];
      // Mettre à jour l'état avec la copie modifiée
      setBoardData(updatedBoardData);
    }
  };

  // Gestionnaire pour supprimer une colonne dans le formulaire
  const handleDeleteColumn = (index: number) => {
    if (boardData) {
      const filteredColumns = boardData.columns.filter(
        (_column, columnIndex) => columnIndex !== index
      );
      setBoardData({ ...boardData, columns: filteredColumns });
    }
  };

  // Gestionnaire pour ajouter un nouveau tableau à la base de données
  const handleAddNewBoardToDb = (e: React.FormEvent<HTMLButtonElement>) => {
    e.preventDefault();
    
    // vérifier si l'un des noms de colonne est vide avant de soumettre
    const emptyColumnStringChecker = boardData?.columns.some(
      (column) => column.name === ""
    ); 

    // condition à exécuter si le nom du tableau est vide
    if (boardData?.name === "") {
      setIsBoardNameEmpty(true);
    }

    // si l'un des noms de colonne est vide, mettre à jour l'index de la colonne vide avec son index
    if (emptyColumnStringChecker) {
      const emptyColumn = boardData?.columns.findIndex(
        (column) => column.name == ""
      );
      setEmptyColumnIndex(emptyColumn);
    }

    if (boardData?.name !== "" && !emptyColumnStringChecker) {
      // soumettre à la base de données après avoir vérifié que le nom du tableau et aucun des noms de colonne ne sont vides
      if (data) {
        let [boards] = data;
        const addBoard = [...boards.boards, boardData];
        boards = addBoard;
        updateBoardToDb(boards);
      }
    }
  };

  // Gestionnaire pour éditer un tableau dans la base de données
  const handleEditBoardToDb = (e: React.FormEvent<HTMLButtonElement>) => {
    e.preventDefault();
    const emptyColumnStringChecker = boardData?.columns.some(
      (column) => column.name === ""
    );
    // condition à exécuter si le nom du tableau est vide
    if (boardData?.name === "") {
      setIsBoardNameEmpty(true);
    }
    // si l'un des noms de colonne est vide, mettre à jour l'index de la colonne vide avec son index
    if (emptyColumnStringChecker) {
      const emptyColumn = boardData?.columns.findIndex(
        (column) => column.name == ""
      );
      setEmptyColumnIndex(emptyColumn);
    }
    // soumettre à la base de données après avoir vérifié que le nom du tableau et aucun des noms de colonne ne sont vides
    if (boardData?.name !== "" && !emptyColumnStringChecker) {
      if (data) {
        const [boards] = data;
        const boardsCopy = [...boards.boards]; 
        const activeBoardIndex = boardsCopy.findIndex(
          (board: { name: string }) => board.name === currentBoardTitle
        );
        const updatedBoard = {
          ...boards.boards[activeBoardIndex],
          name: boardData!.name,
          columns: boardData!.columns,
        } ;
        boardsCopy[activeBoardIndex] = updatedBoard;
        updateBoardToDb(boardsCopy);
      }
    }
  };
```

Enfin, mettez à jour l'instruction return du composant en collant l'extrait de code ci-dessous :

```tsx
return (
    <Modal isOpen={isOpen} onRequestClose={closeModal}>
      <ModalBody>
        {boardData && (
          <>
            {/* afficher la variante(titre) de la modale */}
            <p className="text-lg font-bold">{modalVariant}</p>
            <div className="py-6">
              <div>
                <label htmlFor="boardName" className="text-sm">
                  Nom du tableau
                </label>
                <div className="pt-2">
                  <input
                    id="boardName"
                    className={`${
                      isBoardNameEmpty ? "border-red-500" : "border-stone-200"
                    } border w-full p-2 rounded text-sm cursor-pointer focus:outline-none`}
                    placeholder="Nom"
                    value={boardData.name}
                    onChange={handleBoardNameChange}
                  />
                </div>
                {/* afficher cette erreur si le nom du tableau est vide */}
                {isBoardNameEmpty ? (
                  <p className="text-xs text-red-500">
                    Le nom du tableau ne peut pas être vide
                  </p>
                ) : (
                  ""
                )}
              </div>

              <div className="mt-6">
                <label htmlFor="" className="text-sm">
                  Colonne du tableau
                </label>
                {boardData &&
                  boardData.columns.map(
                    (column: { name: string, id: string }, index: number) => {
                      let { name, id } = column;
                      return (
                        <div key={id} className="pt-2">
                          <div className="flex items-center space-x-2">
                            <input
                              className={`${
                                emptyColumnIndex === index
                                  ? "border-red-500"
                                  : "border-stone-200"
                              } border border-stone-200 focus:outline-none text-sm cursor-pointer w-full p-2 rounded`}
                              placeholder="e.g Doing"
                              onChange={(e) => handleColumnNameChange(index)(e)}
                              value={name!}
                            />
                            <div>
                              <FaTimes
                                onClick={() => handleDeleteColumn(index)}
                              />
                            </div>
                          </div>
                          {/* afficher cette erreur si le nom du tableau est vide */}
                          {emptyColumnIndex === index ? (
                            <p className="text-xs text-red-500">
                              Le nom de la colonne ne peut pas être vide
                            </p>
                          ) : (
                            ""
                          )}
                        </div>
                      );
                    }
                  )}
                <div className="mt-3">
                  <button
                    type="button"
                    onClick={handleAddNewColumn}
                    className="bg-stone-200 rounded-3xl py-2 w-full text-sm font-bold"
                  >
                    <p>+ Ajouter une nouvelle colonne</p>
                  </button>
                </div>
              </div>
              <div className="pt-6">
                <button
                  type="submit"
                  onClick={(e: React.FormEvent<HTMLButtonElement>) => {
                    // fonction à exécuter en fonction de la variante des modales
                    isVariantAdd
                      ? handleAddNewBoardToDb(e)
                      : handleEditBoardToDb(e);
                  }}
                  className="bg-blue-500 rounded-3xl py-2 w-full text-sm font-bold"
                >
                  {/* texte à afficher en fonction de la variante de la modale */}
                  <p>
                    {isLoading
                      ? "Chargement"
                      : `${isVariantAdd ? "Créer un nouveau tableau" : "Enregistrer les modifications"}`}
                  </p>
                </button>
              </div>
            </div>
          </>
        )}
      </ModalBody>
    </Modal>
  );
```


![Ajouter un tableau à la base de données](https://www.freecodecamp.org/news/content/images/2024/01/19.gif)

Dans le GIF ci-dessus, nous avons introduit un tableau "Marketing" avec des colonnes "Todo" et "Doing" dans notre application. Vous pouvez également voir la mise à jour en temps réel des tableaux dans la barre latérale.
   
De même, vous pouvez effectuer des modifications sur un tableau :

![Modifier le tableau](https://www.freecodecamp.org/news/content/images/2024/01/20.gif)

Ici, une nouvelle colonne, "After," a été ajoutée au tableau "Roadmap".

Dans la section suivante, nous implémenterons les fonctionnalités "Ajouter une nouvelle tâche" et "Modifier une tâche".

### Comment ajouter et modifier des tâches

Une fois que vous avez terminé cette section, la modale "Ajouter une nouvelle tâche" devrait ressembler à ce qui suit :

![Modale complète d'ajout de nouvelle tâche](https://www.freecodecamp.org/news/content/images/2024/01/21.png)

De même, pour la modale "Modifier une tâche" :

![Modale complète de modification de tâche](https://www.freecodecamp.org/news/content/images/2024/01/22.png)

Vous verrez que ces modales partagent des similitudes, donc nous les implémenterons en utilisant la même approche que celle employée dans la section précédente.
   
Nous commencerons par mettre à jour l'objet `initialState` dans notre `appSlice` pour gérer l'état de la modale "Ajouter et Modifier des tâches". 

```ts
   const initialState = {
   //ajouter et modifier l'état de la modale des tâches
   isAddAndEditTaskModal: { isOpen: false, variant: "", title: "", index: -1, name: ""},
   };
```
   
Les clés `title` et `index` stockent respectivement le titre et l'index de la tâche en cours de modification, tandis que la clé `name` récupère le nom de la colonne de la tâche. Nous explorerons comment utiliser ces informations pour modifier une tâche dans les étapes à venir.

Ensuite, incluez les fonctions suivantes dans l'objet `reducers`. Ce seront les fonctions qui seront appelées pour ouvrir et fermer la modale :

```ts
    // Ouvrir la modale Ajouter et Modifier une tâche avec une variante spécifiée (ajouter ou modifier), un titre, une description, un statut
    openAddAndEditTaskModal: (state, { payload }) => {
      state.isAddAndEditTaskModal.isOpen = true;
      state.isAddAndEditTaskModal.variant = payload.variant;
      state.isAddAndEditTaskModal.title = payload.title;
	  state.isAddAndEditTaskModal.index = payload.index;
     state.isAddAndEditTaskModal.name = payload.name;
    },
    // Fermer la modale Ajouter et Modifier une tâche
    closeAddAndEditTaskModal: (state) => {
      state.isAddAndEditTaskModal.isOpen = false;
      state.isAddAndEditTaskModal.variant = "";
      state.isAddAndEditTaskModal.title = "";
	  state.isAddAndEditTaskModal.index = "";
	  state.isAddAndEditTaskModal.name = "";
    },
```

Enfin, incluez les fonctions nouvellement implémentées et les fonctions sélecteurs dans les exports :

  ```ts 
   export const {
   openAddAndEditTaskModal,
   closeAddAndEditTaskModal,
   //reste des imports
   } = features.actions;

   // Fonction sélecteur pour récupérer la valeur isOpen de l'état 
   export const getAddAndEditTaskModalValue = (state: RootState) => state.features.isAddAndEditTaskModal.isOpen;
   // Fonction sélecteur pour récupérer la valeur de l'état variant 
   export const getAddAndEditTaskModalVariantValue = (state: RootState) => state.features.isAddAndEditTaskModal.variant;
   // Fonction sélecteur pour récupérer la valeur de l'état title
   export const getAddAndEditTaskModalTitleValue = (state: RootState) => state.features.isAddAndEditTaskModal.title;
   // Fonction sélecteur pour récupérer la valeur de l'état index
   export const getAddAndEditTaskModalIndexValue = (state: RootState) => state.features.isAddAndEditTaskModal.index;
   // Fonction sélecteur pour récupérer la valeur de l'état name
   export const getAddAndEditTaskModalNameValue = (state: RootState) => state.features.isAddAndEditTaskModal.name;
   //reste des imports
   ```
    
Maintenant, nous implémenterons les fonctions `onClick` qui permettent aux utilisateurs d'interagir avec la modale et d'effectuer des actions liées aux tâches. Ces fonctions permettront aux utilisateurs d'ouvrir la modale "Ajouter une nouvelle tâche" depuis la barre de navigation et la modale "Modifier une tâche" en cliquant sur l'icône d'édition dans les cartes de tâches individuelles.

Dans `components/Navbar`, incluez `openAddAndEditTaskModal` parmi les fonctions importées depuis `appSlice` :

```ts
 import { setCurrentBoardName, getCurrentBoardName, openAddAndEditTaskModal } from '../../redux/features/appSlice'
```

Ensuite, modifiez le bouton "+Ajouter une nouvelle tâche" pour incorporer une fonction `onClick` qui déclenche la modale "Ajouter une nouvelle tâche" :

 ```tsx   
    <button 
     type='button'
     onClick={() => dispatch(openAddAndEditTaskModal({variant: 'Ajouter une nouvelle tâche'}))}
     className="bg-blue-500 text-black px-4 py-2 flex rounded-3xl items-center space-x-2">
         <p>+ Ajouter une nouvelle tâche</p>
    </button>
```

Ensuite, accédez au composant `BoardTasks`, où nous implémenterons également le déclencheur pour la modale "Modifier une tâche".

Ici, incluez la fonction `openAddAndEditTaskModal` parmi les fonctions importées depuis `appSlice` :

```tsx
import { openAddAndEditBoardModal, openAddAndEditTaskModal } from "@/components/redux/features/appSlice";
```  

Ensuite, mettez à jour l'icône React `<MdEdit/>` pour incorporer la fonction `onClick` qui déclenche la modale "Modifier une tâche" :

```tsx
    <MdEdit
    onClick={() =>
    dispatch(
      openAddAndEditTaskModal({
        variant: "Modifier une tâche", title, index, name
      }),
    )
   }
   className="text-lg cursor-pointer"
   />;
```

Ensuite, nous créerons le composant de modale Ajouter et Modifier une tâche, en intégrant également ses fonctionnalités.
   
Comme illustré dans les images des modales présentées au début de cette section, dans la modale "Ajouter une nouvelle tâche", le champ de titre est destiné au titre de la tâche qu'un utilisateur souhaite ajouter, et le champ de statut doit contenir exclusivement les noms exacts des colonnes. Toute tentative de saisie d'un nom de colonne qui n'existe pas entraînera une erreur.

Dans la modale "Modifier une tâche", les champs de titre et de statut afficheront le titre et le statut actuels d'une tâche. La modification du titre mettra à jour le titre de la tâche tandis que la modification du statut la déplacera vers la colonne souhaitée.

Pour commencer, dans votre répertoire `src/app/components`, créez un fichier nommé `AddAndEditTaskModal.tsx`, et tout d'abord, insérez le code fourni pour effectuer les imports nécessaires, les définitions de types et les données initiales pour la modale d'ajout de tâche :

 ```tsx  
 "use client";

import { useEffect, useState } from "react";
import { Modal, ModalBody } from "./Modal";
import { useAppDispatch, useAppSelector } from "@/components/redux/hooks";
import {
  getAddAndEditTaskModalValue,
  getAddAndEditTaskModalVariantValue,
  getAddAndEditTaskModalTitle,
  closeAddAndEditTaskModal,
  getCurrentBoardName,
  getAddAndEditTaskModalIndex,
  getAddAndEditTaskModalName,
} from "@/components/redux/features/appSlice";
import {
  useFetchDataFromDbQuery,
  useUpdateBoardToDbMutation,
} from "@/components/redux/services/apiSlice";
import { id } from '../utils/data'

interface ITaskData {
  id: string,
  title: string;
  status: string;
}
// données initiales de la tâche pour la modale d'ajout de tâche
let initialTaskData: ITaskData = {
  id: id(),
  title: "",
  status: "",
};

export default function AddOrEditTaskModal() {
//déclarations de variables, fonctions, JSX
}
```

Ensuite, allez dans la fonction `AddAndEditTaskModal` et collez le code suivant pour déclarer les variables et les valeurs d'état. Les commentaires fournis expliquent l'utilisation future de chacune des déclarations.

```tsx
  let { data } = useFetchDataFromDbQuery();
  let [updateBoardToDb, { isLoading }] = useUpdateBoardToDbMutation();
  const [taskData, setTaskData] = useState<ITaskData>();
  const [isTaskTitleEmpty, setIsTaskTitleEmpty] = useState<boolean>();
  const [isTaskStatusEmpty, setIsTaskStatusEmpty] = useState<boolean>();
  const [statusExists, setStatusExists] = useState<boolean>(true);
  const [columnNames, setColumnNames] = useState<[]>();
  const dispatch = useAppDispatch();
  const isModalOpen = useAppSelector(getAddAndEditTaskModalValue);
  const modalVariant = useAppSelector(getAddAndEditTaskModalVariantValue);
  const isVariantAdd = modalVariant === "Ajouter une nouvelle tâche";
  const closeModal = () => dispatch(closeAddAndEditTaskModal());
  const currentBoardTitle = useAppSelector(getCurrentBoardName);
  // obtenir le titre, l'index et le nom de la tâche depuis le magasin redux
  const currentTaskTitle = useAppSelector(getAddAndEditTaskModalTitle);
  const currentTaskIndex = useAppSelector(getAddAndEditTaskModalIndex);
  const initialTaskColumn = useAppSelector(getAddAndEditTaskModalName);
```

Ici, nous implémenterons les fonctions responsables de la fonctionnalité de la modale. Juste en dessous des définitions de variables ci-dessus, collez les fonctions suivantes :

```tsx
  // Effet pour définir les données initiales de la modale en fonction de la variante
  useEffect(() => {
    if (data) {
      const activeBoard = data[0].boards.find(
        (board: { name: string }) => board.name === currentBoardTitle
      );
      if (activeBoard) {
        const { columns } = activeBoard;
        const columnNames = columns.map(
          (column: { name: string }) => column.name
        );

        if (columnNames) {
          setColumnNames(columnNames);
        }

        if (isVariantAdd) {
          setTaskData(initialTaskData);
        }
        
        else {
          const activeTask = columns
            .map((column: { tasks: [] }) => column.tasks)
            .flat()
            .find((task: { title: string }) => task.title === currentTaskTitle);
          setTaskData(activeTask);
        }
      }
    }
  }, [data, modalVariant]);

  // Effet pour effacer les messages d'erreur après un certain temps
  useEffect(() => {
    const timeoutId = setTimeout(() => {
      setIsTaskStatusEmpty(false);
      setIsTaskStatusEmpty(false);
      setStatusExists(true);
    }, 3000);
    return () => clearTimeout(timeoutId);
  }, [isTaskStatusEmpty, isTaskTitleEmpty, statusExists]);

  // Gestionnaire de changement de titre de tâche
  const handleTaskTitleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (taskData) {
      const newTitle = { ...taskData, title: e.target.value };
      setTaskData(newTitle);
    }
  };

  // Gestionnaire de changement de statut de tâche
  const handleTaskStatusChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (taskData) {
      const newTitle = { ...taskData, status: e.target.value };
      setTaskData(newTitle);
    }
  };

  // Gestionnaire pour ajouter une nouvelle tâche à la base de données
  const handleAddNewTaskToDb = (e: React.FormEvent<HTMLButtonElement>) => {

    e.preventDefault();
    const { title, status } = taskData!;

    if (!title) {
      setIsTaskTitleEmpty(true);
    }

    if (!status) {
      setIsTaskStatusEmpty(true);
    }

    // vérifier si l'entrée de statut existe parmi les colonnes existantes
    const doesStatusExists = columnNames?.some(
      (column) => column === taskData?.status
    );

    if (!doesStatusExists) {
      setStatusExists(false);
    }

    // si toutes les conditions sont remplies
    if (title && status && doesStatusExists) {
      if (data) {
        const [boards] = data;
        const boardsCopy = [...boards.boards];
        const activeBoard = boardsCopy.find(
          (board: { name: string }) => board.name === currentBoardTitle
        );
        const activeBoardIndex = boardsCopy.findIndex(
          (board: { name: string }) => board.name === currentBoardTitle
        );
        const { columns } = activeBoard;
        // trouver la colonne dans le tableau à mettre à jour
        const getStatusColumn = columns?.find(
          (column: { name: string }) => column.name === status
        );
        const getStatusColumnIndex = columns?.findIndex(
          (column: { name: string }) => column.name === status
        );
        // déstructurer les tâches dans une colonne. "Now" par exemple.
        const { tasks } = getStatusColumn;
        const addNewTask = [...tasks, { id: id(), title, status }]; //ajouter une nouvelle tâche
        const updatedStatusColumn = { ...getStatusColumn, tasks: addNewTask };
        //mettre à jour les colonnes dans un tableau
        const columnsCopy = [...columns];
        columnsCopy[getStatusColumnIndex] = updatedStatusColumn;
        const updatedBoard = {
          ...boards.boards[activeBoardIndex],
          columns: columnsCopy,
        };
        //mettre à jour le tableau dans la base de données
        boardsCopy[activeBoardIndex] = updatedBoard;
        updateBoardToDb(boardsCopy);
      }
    }
  };

  const handleEditTaskToDb = (e: React.FormEvent<HTMLButtonElement>) => {
    e.preventDefault();
    const { title, status } = taskData!;
    if (!title) {
      setIsTaskTitleEmpty(true);
    }
    if (!status) {
      setIsTaskStatusEmpty(true);
    }
    // vérifier si l'entrée de statut existe parmi les statuts existants
    const doesStatusExists = columnNames?.some(
      (column) => column === taskData?.status
    );
    if (!doesStatusExists) {
      setStatusExists(false);
    }
    if (title && status && doesStatusExists) {
      if (data) {
        const [boards] = data;
        const boardsCopy = [...boards.boards];
        const activeBoard = boardsCopy.find(
          (board: { name: string }) => board.name === currentBoardTitle
        );
        const activeBoardIndex = boardsCopy.findIndex(
          (board: { name: string }) => board.name === currentBoardTitle
        );
        const { columns } = activeBoard;
        const getStatusColumnIndex = columns?.findIndex(
          (column: { name: string }) => column.name === status
        );

        // Vérifier si le statut de la tâche à modifier est égal à column.name
        if (status === initialTaskColumn) {
          const updatedStatusColumn = {
            ...columns[getStatusColumnIndex],
            tasks: columns[getStatusColumnIndex]?.tasks?.map(
              (task: any, index: number) => {
                if (index === currentTaskIndex) {
                  return { title, status };
                }
                return task;
              }
            ),
          };
          const columnsCopy = [...columns];
          columnsCopy[getStatusColumnIndex] = updatedStatusColumn;
          const updatedBoard = {
            ...boards.boards[activeBoardIndex],
            columns: columnsCopy,
          };
          //mettre à jour le tableau dans la base de données
          boardsCopy[activeBoardIndex] = updatedBoard;
          updateBoardToDb(boardsCopy);
        } else {
          // Trouver la colonne avec le nom dans le statut de la tâche et ajouter la tâche modifiée
          const getStatusColumn = columns?.find(
            (column: { name: string }) => column.name === status
          );
          // supprimer la tâche de la colonne précédente
          const getPrevStatusColumn = columns?.find(
            (column: { name: string }) => column.name === initialTaskColumn
          );
          const getPrevStatusColumnIndex = columns?.findIndex(
            (column: { name: string }) => column.name === initialTaskColumn
          );
          //mettre à jour la colonne précédente de la tâche
          const updatedPrevStatusColumn = {
            ...getPrevStatusColumn,
            tasks: getPrevStatusColumn?.tasks.filter(
              (_task: [], index: number) => index !== currentTaskIndex
            ),
          };
          // mettre à jour la nouvelle colonne de la tâche
          const updatedStatusColumn = {
            ...getStatusColumn,
            tasks: [...getStatusColumn?.tasks, { title, status }],
          };
          const columnsCopy = [...columns];
          columnsCopy[getStatusColumnIndex] = updatedStatusColumn;
          columnsCopy[getPrevStatusColumnIndex] = updatedPrevStatusColumn;
          const updatedBoard = {
            ...boards.boards[activeBoardIndex],
            columns: columnsCopy,
          };
          //mettre à jour le tableau dans la base de données
          boardsCopy[activeBoardIndex] = updatedBoard;
          updateBoardToDb(boardsCopy);
        }
      }
    }
  };
```

Enfin, dans ce composant, collez le code ci-dessous pour implémenter le JSX de la modale :

```tsx
return (
    <Modal isOpen={isModalOpen} onRequestClose={closeModal}>
      <ModalBody>
        <p className="font-bold text-lg">{modalVariant}</p>
        <div className="py-6">
          <div>
            <label htmlFor="title" className="text-sm">
              Titre
            </label>
            <div className="pt-2">
              <input
                id="title"
                className={`${
                  isTaskTitleEmpty ? "border-red-500" : "border-stone-200"
                } border w-full p-2 rounded text-sm cursor-pointer focus:outline-none`}
                placeholder="Nom"
                value={taskData?.title}
                onChange={handleTaskTitleChange}
              />
            </div>
            {isTaskTitleEmpty ? (
              <p className="text-xs text-red-500">Le titre de la tâche ne peut pas être vide</p>
            ) : (
              ""
            )}
          </div>

          <div className="mt-3">
            <label htmlFor="status" className="text-sm">
              Statut
            </label>
            <div className="pt-2">
              <input
                id="status"
                className={`${
                  isTaskStatusEmpty || !statusExists
                    ? "border-red-500"
                    : "border-stone-200"
                } border w-full p-2 rounded text-sm cursor-pointer focus:outline-none`}
                placeholder={columnNames?.join(", ")}
                value={taskData?.status}
                onChange={handleTaskStatusChange}
              />
            </div>
            {isTaskStatusEmpty ? (
              <p className="text-xs text-red-500">
                Le statut de la tâche ne peut pas être vide
              </p>
            ) : !statusExists ? (
              <p className="text-xs text-red-500">La colonne n'existe pas</p>
            ) : (
              ""
            )}
          </div>
          <div className="pt-6">
            <button
              type="submit"
              onClick={(e: React.FormEvent<HTMLButtonElement>) => {
                // fonction à exécuter en fonction de la variante des modales
                isVariantAdd ? handleAddNewTaskToDb(e) : handleEditTaskToDb(e);
              }}
              className="bg-blue-500 rounded-3xl py-2 w-full text-sm font-bold"
            >
              <p>
                {isLoading
                  ? "Chargement"
                  : `${isVariantAdd ? "Créer une tâche" : "Enregistrer les modifications"}`}
              </p>
            </button>
          </div>
        </div>
      </ModalBody>
    </Modal>
  );
```

Enfin, importez et rendez le composant dans votre fichier `src/app/page.tsx` comme indiqué ci-dessous :
   
   ```tsx
   //reste des imports
   import AddAndEditTaskModal from "./components/AddAndEditTaskModal";
     //reste du code
     return (
    <main className="flex h-full">
      <Sidebar />
      <BoardTasks />
      <AddAndEditBoardModal />
      <AddAndEditTaskModal/>  //rendre ici
    </main>
    );
```
 
Avec cette fonctionnalité, vous pouvez facilement ajouter des tâches à n'importe quelle colonne souhaitée. Par exemple, ajoutons une nouvelle tâche intitulée "Acheter des tomates" à la colonne "Next" :

![Ajouter la tâche d'achat de tomates au tableau](https://www.freecodecamp.org/news/content/images/2024/01/23.gif)

De même, nous illustrerons la fonctionnalité d'édition de tâche en changeant la colonne de "Lancer la version deux" de "Now" à "Later" :

![Modifier la colonne de la tâche](https://www.freecodecamp.org/news/content/images/2024/01/24.gif)

Enfin, dans la section suivante, nous implémenterons les fonctionnalités de suppression pour les tableaux et les tâches. 

### Comment supprimer des tableaux et des tâches

À la fin de cette section, la modale "Supprimer le tableau" devrait ressembler à ceci :

![Marque de la modale de suppression du tableau](https://www.freecodecamp.org/news/content/images/2024/01/25.png)

De même, la modale "Supprimer la tâche" :

![Marque de la modale de suppression de la tâche](https://www.freecodecamp.org/news/content/images/2024/01/26.png)

Comme vous pouvez le voir, ces modales partagent des similitudes, donc nous utiliserons la même méthodologie que celle que nous avons utilisée pour les implémentations de modales précédentes.

Pour commencer, mettons à jour l'objet `initialState` dans notre `appSlice` pour gérer l'état de la modale "Supprimer les tableaux et les tâches". Intégrez l'état `isDeleteBoardAndTaskModal` dans l'objet `initialState` comme illustré ci-dessous :

```ts
    const initialState = {
      //reste de l'état
      isDeleteBoardAndTaskModal: { isOpen: false, variant: "",  title:'', status: "", index: -1 },
```
  
Ensuite, incluez les fonctions suivantes dans l'objet `reducers`. Ces fonctions seront appelées pour ouvrir et fermer la modale :
   
```ts
    // Ouvrir la modale de suppression de tableau et de tâche avec une variante spécifiée (supprimer le tableau ou la tâche)
   openDeleteBoardAndTaskModal: (state, { payload }) => {
      state.isDeleteBoardAndTaskModal.isOpen = true;
      state.isDeleteBoardAndTaskModal.variant = payload.variant;
	  state.isDeleteBoardAndTaskModal.title = payload.title;
      state.isDeleteBoardAndTaskModal.status = payload.status;
      state.isDeleteBoardAndTaskModal.index = payload.index;
    },
   // Fermer la modale de suppression de tableau et de tâche
   closeDeleteBoardAndTaskModal: (state) => {
      state.isDeleteBoardAndTaskModal.isOpen = false;
      state.isDeleteBoardAndTaskModal.variant = "";
	  state.isDeleteBoardAndTaskModal.title = "";
      state.isDeleteBoardAndTaskModal.status = "";
      state.isDeleteBoardAndTaskModal.index = -1;
    },
```
  
Enfin, incluez les fonctions nouvellement implémentées et les fonctions sélecteurs dans les exports :
 
 ```ts
 export const {
    openDeleteBoardAndTaskModal,
    closeDeleteBoardAndTaskModal,
   } = features.actions;

   // Supprimer la tâche et le tableau
   export const getDeleteBoardAndTaskModalValue = (state: RootState) => state.features.isDeleteBoardAndTaskModal.isOpen;
   // Fonction sélecteur pour récupérer la valeur de l'état variant 
   export const getDeleteBoardAndTaskModalVariantValue = (state: RootState) => state.features.isDeleteBoardAndTaskModal.variant;
   // Fonction sélecteur pour récupérer la valeur de l'état title 
   export const getDeleteBoardAndTaskModalTitle = (state: RootState) => state.features.isDeleteBoardAndTaskModal.title;
   // Fonction sélecteur pour récupérer la valeur de l'état status
   export const getDeleteBoardAndTaskModalStatus = (state: RootState) => state.features.isDeleteBoardAndTaskModal.status;
   // Fonction sélecteur pour récupérer la valeur de l'état index
   export const getDeleteBoardAndTaskModalIndex = (state: RootState) => state.features.isDeleteBoardAndTaskModal.index;
```

Ensuite, nous implémenterons les fonctions `onClick` pour permettre aux utilisateurs d'interagir avec la modale et d'exécuter des actions de suppression. Ces fonctions permettront aux utilisateurs d'ouvrir la modale "Supprimer le tableau" depuis le menu déroulant dans la barre de navigation et la modale "Supprimer la tâche" en cliquant sur l'icône de suppression dans les cartes de tâches individuelles.

Dans le fichier `components/Dropdown.tsx`, ajoutez la fonction `openDeleteBoardAndTaskModal` à la liste des fonctions importées depuis `appSlice` :

```ts
import { openDeleteBoardAndTaskModal } from '@/components/redux/features/appSlice';
```   

Ensuite, ajustez le bouton "Supprimer le tableau" pour incorporer la fonction `onClick` afin d'ouvrir la modale. Cette action déclenchera la modale "Supprimer le tableau" :

```ts
      <div className="hover:bg-gray-300">
         <button
            onClick={() => dispatch(openDeleteBoardAndTaskModal({variant: "Supprimer ce tableau ?"}))}
            className="text-sm px-4 py-2">
            Supprimer le tableau
         </button>
      </div>
```
     
Passez au composant `BoardTasks`, et de même, incluez la fonction de suppression des tâches et des tableaux parmi les imports depuis `appSlice` :

```ts
      import {
         //autres imports
         openDeleteBoardAndTaskModal
      } from "@/components/redux/features/appSlice";
```
   
Ajustez l'icône React de suppression pour inclure la fonction `onClick` afin d'ouvrir la modale :

```tsx
      <MdDelete
         onClick={() =>
            dispatch(
               openDeleteBoardAndTaskModal({
                  variant: "Supprimer cette tâche ?",
                  status,
                  index,
               }),
            )
         }
         className="text-lg cursor-pointer text-red-500"
      />;
```
     
Maintenant, nous commencerons à construire la marque de la modale de suppression de tableau et de tâche, couplée avec l'implémentation de ses fonctionnalités.

Dans votre dossier `app/components`, créez un fichier nommé `DeleteBoardAndTask` modal et collez le code fourni à l'intérieur :

```tsx
   import { Modal, ModalBody } from "./Modal";
   import { useAppDispatch, useAppSelector } from "@/components/redux/hooks";
   import {
   closeDeleteBoardAndTaskModal,
   getDeleteBoardAndTaskModalValue,
   getDeleteBoardAndTaskModalVariantValue,
   getDeleteBoardAndTaskModalTitle,
   getDeleteBoardAndTaskModalIndex,
   getDeleteBoardAndTaskModalStatus,
   getCurrentBoardName,
   } from "@/components/redux/features/appSlice";
   import {
   useFetchDataFromDbQuery,
   useUpdateBoardToDbMutation,
   } from "@/components/redux/services/apiSlice";
   
   export default function DeleteBoardAndTaskModal() {
     //déclarations de variables, fonctions, JSX
   }
```

Ensuite, allez dans la fonction `DeleteBoardAndTaskModal` et collez le code suivant pour déclarer les variables et les valeurs d'état. Les commentaires fournis expliquent l'utilisation future de chacune des déclarations.

```tsx
   const dispatch = useAppDispatch();
   const isModalOpen = useAppSelector(getDeleteBoardAndTaskModalValue);
   const closeModal = () => dispatch(closeDeleteBoardAndTaskModal());
   const currentBoardName = useAppSelector(getCurrentBoardName);
   const modalVariant = useAppSelector(getDeleteBoardAndTaskModalVariantValue);
   const taskTitle = useAppSelector(getDeleteBoardAndTaskModalTitle);
   const taskIndex = useAppSelector(getDeleteBoardAndTaskModalIndex);
   const taskStatus = useAppSelector(getDeleteBoardAndTaskModalStatus);
   let { data } = useFetchDataFromDbQuery();
   const [updateBoardToDb, { isLoading }] = useUpdateBoardToDbMutation();
```

Ici, nous implémenterons la fonction responsable de la fonctionnalité de la modale. Juste en dessous des définitions de variables ci-dessus, collez la fonction suivante :

```tsx
   const handleDelete = (e: React.FormEvent<HTMLButtonElement>) => {
    e.preventDefault();
    if (data) {
      if (modalVariant === "Supprimer ce tableau ?") {
        // Implémenter la logique pour supprimer le tableau
        if (currentBoardName) {
          //  En supposant que les données sont disponibles, vous devez gérer la logique pour mettre à jour les données
          const [boards] = data;
          const updatedBoards = boards.boards.filter(
            (board: { name: string }) => board.name !== currentBoardName
          );
          updateBoardToDb(updatedBoards);
        }
      } else {
        // Implémenter la logique pour supprimer une tâche
        if (taskIndex !== undefined && taskStatus && currentBoardName) {
          const [boards] = data;
          //  Gérer la logique pour mettre à jour les tâches
          const updatedBoards = boards.boards.map(
            (board: {
              name: string;
              columns: [{ name: string; tasks: [] }];
            }) => {
            // vérifier le tableau actif
              if (board.name === currentBoardName) {
                // parcourir les colonnes du tableau pour trouver la colonne dans laquelle se trouve la tâche à modifier
                const updatedColumns = board.columns.map((column) => {
                  if (column.name === taskStatus) {
                    // supprimer la tâche
                    const updatedTasks = column.tasks.filter(
                      (_, index: number) => index !== taskIndex
                    );
                    return { ...column, tasks: updatedTasks };
                  }
                  return column;
                });
                return { ...board, columns: updatedColumns };
              }
              return board;
            }
          );
          updateBoardToDb(updatedBoards);
        }
      }
    }
   };
```    

Enfin, dans ce composant, collez le code ci-dessous pour implémenter le JSX de la modale :
 
 ```   
   return (
    <Modal isOpen={isModalOpen} onRequestClose={closeModal}>
      <ModalBody>
        <p className="text-red font-bold text-lg">{modalVariant}</p>
        <div className="pt-6">
          <p className="text-sm text-medium-grey leading-6">
            {modalVariant === "Supprimer ce tableau ?"
              ? `Êtes-vous sûr de vouloir supprimer le tableau '${currentBoardName}' ? Cette action supprimera toutes les colonnes
                et tâches et ne pourra pas être annulée.`
              : `Êtes-vous sûr de vouloir supprimer les tâches '${taskTitle}' ? Cette action ne pourra pas être annulée.`}
          </p>
        </div>
        <div className="pt-6 flex space-x-2">
          <div className="w-1/2">
            <button
              type="submit"
              onClick={(e: React.FormEvent<HTMLButtonElement>) =>
                handleDelete(e)
              }
              className="bg-red-500 rounded-3xl py-2 w-full text-sm font-bold"
            >
              {" "}
              {isLoading ? "Chargement" : "Supprimer"}
            </button>
          </div>
          <div className="w-1/2">
            <button
              onClick={closeModal}
              className="bg-stone-200 rounded-3xl py-2 w-full text-sm font-bold"
            >
              Annuler
            </button>
          </div>
        </div>
      </ModalBody>
    </Modal>
   );
   }
```
  
Après cette mise à jour, importez le composant dans `page.tsx` et rendez-le comme indiqué ci-dessous :

```tsx
	 //reste des imports
	 import DeleteBoardOrTaskModal from "./components/DeleteBoardAndTaskModal";
	 //reste du code
	   return (
    <main className="flex h-full">
      <Sidebar />
      <BoardTasks />
      <AddAndEditBoardModal />
      <AddAndEditTaskModal/>
      <DeleteBoardAndTaskModal/>
    </main>
    );
```

Après avoir rendu le composant, vous pouvez maintenant supprimer un tableau. Par exemple, nous allons supprimer le tableau "Marketing" que nous avons créé précédemment :

![Fonctionnalité de suppression de tableau](https://www.freecodecamp.org/news/content/images/2024/01/27.gif)

De même, vous pouvez supprimer une tâche :

![Fonctionnalité de suppression de tâche](https://www.freecodecamp.org/news/content/images/2024/01/28.gif)

Dans la section suivante, nous explorerons l'implémentation de la fonctionnalité de glisser-déposer avec la bibliothèque `react-beautiful-dnd`.

## Comment implémenter la fonctionnalité de glisser-déposer

À la fin de cette section, vous devriez être en mesure de déplacer des tâches entre les colonnes et à travers les colonnes. 

Pour commencer, installez la bibliothèque `react-beautiful-dnd` avec la commande suivante :

```npm
npm i react-beautiful-dnd 
```
 
Il est important de noter que [la bibliothèque react-beautiful-dnd ne fonctionne pas à l'intérieur du wrapper `StrictMode`](https://github.com/atlassian/react-beautiful-dnd/issues/2399#issuecomment-1111169234) qui est [activé par défaut dans le routeur d'application](https://nextjs.org/docs/pages/api-reference/next-config-js/reactStrictMode). Nous devons donc créer un hook personnalisé qui nous permettra d'utiliser la bibliothèque `react-beautiful-dnd` en toute sécurité avec `StrictMode`. 

Créez un fichier nommé `StrictModeDroppable.tsx` à l'intérieur de votre dossier `src/app/components` et collez le code fourni ci-dessous à l'intérieur :

```tsx
import { useEffect, useState } from "react";
import { Droppable, DroppableProps } from "react-beautiful-dnd";

export const StrictModeDroppable = ({ children, ...props }: DroppableProps) => {
  const [enabled, setEnabled] = useState(false);

  useEffect(() => {
    const animation = requestAnimationFrame(() => setEnabled(true));

    return () => {
      cancelAnimationFrame(animation);
      setEnabled(false);
    };
  }, []);

  if (!enabled) {
    return null;
  }

  return <Droppable {...props}>{children}</Droppable>;
};
```

De cette manière, nous l'avons rendu compatible avec `StrictMode`, nous permettant d'implémenter en toute sécurité la fonctionnalité de glisser-déposer.

Ensuite, accédez au composant `BoardTasks.tsx` et mettez-le à jour avec le code ci-dessous :

Tout d'abord, importez les composants nécessaires depuis la bibliothèque `react-beautiful-dnd` et également depuis notre composant personnalisé `StrictModeDroppable.tsx` :

```tsx
//importer le hook useRef
import { useEffect, useState, useRef } from "react";
import { DragDropContext, Draggable } from "react-beautiful-dnd";
// importer Droppable depuis le hook personnalisé
import { StrictModeDroppable as Droppable } from "./StrictModeDroppable";
```

Après avoir mis à jour les imports, allez dans la fonction BoardTasks et incluez les fonctions suivantes :

```tsx
// vérifier si c'est le premier rendu
const initialRender = useRef(true);


  const handleDragEnd = async ({ destination, source }: any) => {
    // Vérifier si la destination n'est pas nulle (c'est-à-dire qu'elle a été déposée dans un Droppable valide)
    if (!destination) return;


    // obtenir une copie profondément imbriquée de l'état des colonnes
    const newColumns = columns.map((column) => ({
      ...column,
      tasks: [...column.tasks], // Créer un nouveau tableau pour les tâches
    }));


    // Trouver les colonnes source et destination en fonction de leurs droppableIds
    const sourceColumnIndex = newColumns.findIndex(
      (col) => col.id === source.droppableId
    );
    const destinationColumnIndex = newColumns.findIndex(
      (col) => col.id === destination.droppableId
    );


    // Tâche qui a été glissée
    const itemMoved = newColumns[sourceColumnIndex]?.tasks[source.index];


    // Supprimer de sa source
    newColumns[sourceColumnIndex].tasks.splice(source.index, 1);


    // Insérer dans sa destination
    newColumns[destinationColumnIndex].tasks.splice(
      destination.index,
      0,
      itemMoved
    );


    // Mettre à jour l'état
    setColumns(newColumns);
  };


  useEffect(() => {
    // Vérifier si c'est le rendu initial, pour éviter d'envoyer les données au backend au montage
    if (!initialRender.current) {
      // Mettre à jour le backend avec le nouvel ordre
      try {
        if (data) {
          const [boards] = data;
          const boardsCopy = [...boards.boards];
          const activeBoardIndex = boardsCopy.findIndex(
            (board: { name: string }) => board.name === currentBoardTitle
          );
          const updatedBoard = {
            ...boards.boards[activeBoardIndex],
            columns,
          };
          boardsCopy[activeBoardIndex] = updatedBoard;
          updateBoardToDb(boardsCopy);
        }
      } catch (error) {
        // Gérer l'erreur
        console.error("Erreur lors de la mise à jour du tableau :", error);
      }
    } else {
      // Définir le rendu initial à false après le premier rendu
      initialRender.current = false;
    }
  }, [columns]);
```

Jusqu'à présent, nous avons implémenté une fonction qui sera déclenchée après qu'une tâche a été glissée. Après chaque déclenchement de cette fonction, les données des colonnes sont mises à jour et envoyées à Cloud Firestore via le hook `useEffect`. J'ai ajouté plus de commentaires dans le code pour vous aider à mieux comprendre. 

Enfin, mettez à jour le JSX dans l'instruction return comme indiqué ci-dessous :

```tsx
 return (
    <div className="overflow-x-auto overflow-y-auto w-full p-6 bg-stone-200">
      {/* Si les données n'ont pas été récupérées avec succès, afficher un état de chargement, sinon afficher la colonne des tâches */}
      {isLoading ? (
        <p className="text-3xl w-full text-center font-bold">
          Chargement des tâches...
        </p>
      ) : (
        <>
          {/* Si les colonnes de tâches ne sont pas vides : afficher les tâches, sinon afficher l'invitation à ajouter une nouvelle colonne */}
          {columns.length > 0 ? (
            <DragDropContext onDragEnd={handleDragEnd}>
              <div className="flex space-x-6">
                {columns.map((column, index) => {
                  const { id, name } = column;
                  return (
                    <div key={id} className="w-[17.5rem] shrink-0">
                      <p className="text-black">{`${column.name} (${
                        column.tasks ? column.tasks?.length : 0
                      })`}</p>
                      <Droppable droppableId={id}>
                        {(provided) => (
                          <div
                            ref={provided.innerRef}
                            {...provided.droppableProps}
                            className="h-full"
                          >
                            {column.tasks &&
                              // Afficher les tâches s'il y a des tâches dans la colonne, sinon afficher une colonne vide
                              (column.tasks.length > 0 ? (
                                column.tasks.map((task, index) => {
                                  const { id, title, status } = task;
                                  return (
                                    <Draggable
                                      key={id}
                                      draggableId={id}
                                      index={index}
                                    >
                                      {(provided) => (
                                        <div
                                          ref={provided.innerRef}
                                          {...provided.draggableProps}
                                          {...provided.dragHandleProps}
                                          className="bg-white p-6 rounded-md mt-6 flex items-center justify-between border"
                                        >
                                          <p>{task.title}</p>
                                          <div className="flex items-center space-x-1">
                                            <MdEdit
                                              onClick={() =>
                                                dispatch(
                                                  openAddAndEditTaskModal({
                                                    variant: "Modifier une tâche",
                                                    title,
                                                    index,
                                                    name,
                                                  })
                                                )
                                              }
                                              className="text-lg cursor-pointer"
                                            />
                                            <MdDelete
                                              onClick={() =>
                                                dispatch(
                                                  openDeleteBoardAndTaskModal({
                                                    variant:
                                                      "Supprimer cette tâche ?",
                                                    title,
                                                    status,
                                                    index,
                                                  })
                                                )
                                              }
                                              className="text-lg cursor-pointer text-red-500"
                                            />
                                          </div>
                                        </div>
                                      )}
                                    </Draggable>
                                  );
                                })
                              ) : (
                                <div className="mt-6 h-full rounded-md border-dashed border-4 border-white" />
                              ))}
                            {provided.placeholder}
                          </div>
                        )}
                      </Droppable>
                    </div>
                  );
                })}
                {/* Si le nombre de colonnes de tâches est inférieur à 7, afficher une option pour ajouter plus de colonnes */}
                {columns.length < 7 ? (
                  <div
                    onClick={() =>
                      dispatch(openAddAndEditBoardModal("Modifier le tableau"))
                    }
                    className="rounded-md bg-white w-[17.5rem] mt-12 shrink-0 flex justify-center items-center"
                  >
                    <p className="cursor-pointer font-bold text-black text-2xl">
                      + Nouvelle colonne
                    </p>
                  </div>
                ) : (
                  ""
                )}
              </div>
            </DragDropContext>
          ) : (
            <div className="w-full h-full flex justify-center items-center">
              <div className="flex flex-col items-center">
                <p className="text-black text-sm">
                  Ce tableau est vide. Créez une nouvelle colonne pour commencer.
                </p>
                <button className="bg-blue-500 text-black px-4 py-2 flex mt-6 rounded-3xl items-center space-x-2">
                  <p>+ Ajouter une nouvelle colonne</p>
                </button>
              </div>
            </div>
          )}
        </>
      )}
    </div>
  );

```

Dans l'extrait de code ci-dessus, nous avons enveloppé `DragDropContext` autour des colonnes de tâches avec son attribut `onDragEnd`, qui accepte la fonction `handleDragEnd`, qui sera déclenchée après qu'une tâche a été glissée. 

N'oubliez pas que après chaque déclenchement de cette fonction, les données des colonnes sont mises à jour et envoyées à Cloud Firestore via le hook `useEffect`. 

Chaque colonne de tâche est également enveloppée autour du composant `Droppable`. Cela signifie que c'est un emplacement où vous pouvez déposer une tâche. Il accepte également un attribut `droppableId` auquel nous avons passé l'`id` de chaque colonne.

Chaque carte de tâche est également enveloppée autour du composant `Draggable`, ce qui les rend glissables à l'intérieur et entre les colonnes. 

Avec ces changements, nous avons facilement implémenté la fonctionnalité de glisser-déposer pour notre application :

![Fonctionnalité de glisser-déposer](https://www.freecodecamp.org/news/content/images/2024/01/29.gif)

## Conclusion

Ce tutoriel vous a guidé à travers l'implémentation de l'authentification en utilisant la bibliothèque `next-auth`, la configuration d'un magasin Redux, et l'intégration de Firebase avec son `RTK Query` dans les applications Next.js. 

Vous avez également appris à implémenter les opérations CRUD dans une application de gestion de tâches Kanban, et vous avez exploré les validations de formulaire avec JavaScript. 

Et enfin, nous avons couvert l'implémentation de la fonctionnalité de glisser-déposer en utilisant la bibliothèque `react-beautiful-dnd`.

Tout au long du tutoriel, nous avons également tiré parti des bibliothèques existantes pour rationaliser le développement plutôt que de tout construire à partir de zéro.

Si vous souhaitez voir tout le code, vous pouvez visiter le dépôt GitHub du projet [ici](https://github.com/SiR-PENt/kanban-app-tutorial). N'hésitez pas à forker le projet et à ouvrir une PR si vous ressentez le besoin d'améliorations. Si vous souhaitez également explorer le site en direct, vous pouvez le trouver [ici](https://kanban-app-tutorial.vercel.app). 

Si vous souhaitez également explorer ce projet avec des fonctionnalités plus avancées, comme le mode sombre, un design d'interface utilisateur plus élégant et de meilleures fonctionnalités, visitez-le [ici](https://kanban-task-management-app-delta.vercel.app).