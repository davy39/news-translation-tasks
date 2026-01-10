---
title: Comment sécuriser les routes dans Next.js 13 – Protection côté client, côté
  serveur et basée sur le middleware
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-10-17T14:42:10.000Z'
originalURL: https://freecodecamp.org/news/secure-routes-in-next-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/fly-d-ZNOxwCEj5mw-unsplash.jpg
tags:
- name: Next.js
  slug: nextjs
- name: Security
  slug: security
seo_title: Comment sécuriser les routes dans Next.js 13 – Protection côté client,
  côté serveur et basée sur le middleware
seo_desc: "Web applications often handle sensitive data and admin functionalities\
  \ that should only be accessible to authenticated users. In such cases, route protection\
  \ becomes crucial for safeguarding these routes from unauthorized access. \nIn this\
  \ tutorial, w..."
---

Les applications web traitent souvent des données sensibles et des fonctionnalités d'administration qui ne doivent être accessibles qu'aux utilisateurs authentifiés. Dans de tels cas, la protection des routes devient cruciale pour protéger ces routes contre les accès non autorisés.

Dans ce tutoriel, nous explorerons comment protéger les routes dans Next.js 13 en utilisant trois méthodes différentes. Nous apprendrons comment protéger les routes côté client et côté serveur, et en utilisant le middleware.

## Introduction

La protection des routes est un aspect essentiel du développement d'applications web. Elle est très nécessaire lors de la gestion du processus d'authentification de votre application.

Elle implique de contrôler l'accès à des routes spécifiques en fonction du statut d'authentification de l'utilisateur. Par exemple, vous ne voudriez pas qu'un utilisateur non authentifié accède à un tableau de bord d'administration ou voie des données utilisateur sensibles.

Avant de nous lancer dans ce voyage, voici quelques prérequis pour vous assurer de tirer le meilleur parti de ce tutoriel :

* Compréhension de base de Next.js, Node.js et JavaScript
* Familiarité avec les gestionnaires de paquets comme NPM ou Yarn
* Un éditeur de code de votre choix (comme Visual Studio Code)
* Node.js et npm (ou yarn) sont installés sur votre machine.

Discutons brièvement de ce qu'est Next.js. Selon sa [documentation officielle](https://nextjs.org/docs/getting-started/installation), Vercel a créé Next.js, un framework React principalement utilisé pour construire des applications web full-stack. Next.js offre diverses fonctionnalités, y compris le routage basé sur le système de fichiers, le rendu côté client et côté serveur, les optimisations d'images et un support amélioré pour TypeScript.

Pour commencer à construire des applications web avec Next.js, vous pouvez créer un nouveau projet Next.js en utilisant les commandes suivantes :

```js
npx create-next-app@latest
```

Après une installation réussie, vous recevrez plusieurs invites pour configurer votre application Next.js. Je recommande de sélectionner le routeur d'application, car c'est le choix recommandé pour le routage dans Next.js 13. Pour ce tutoriel, nous utiliserons Tailwind CSS pour le style et TypeScript.

## Routage dans Next.js

Contrairement aux applications React, qui s'appuient souvent sur des paquets tiers comme **react-router-dom** pour le routage, Next.js 13 dispose de son propre routeur d'application intégré. Ce routeur prend en charge les mises en page partagées, le routage imbriqué, les états de chargement, la gestion des erreurs, et plus encore.

Next.js utilise un système de routage basé sur les fichiers. Cela signifie que les dossiers contenant des fichiers page.js définissent les routes. Un dossier peut également contenir un ou plusieurs sous-dossiers.

Next.js simplifie la mise en œuvre des routes protégées. Avant de plonger dans la manière de créer des routes protégées dans Next.js, comprenons comment les routes sont créées.

## Comment créer une route dans Next.js

Pour démontrer les différentes façons dont nous pouvons protéger les routes dans Next.js 13, nous créerons des routes : **Accueil**, **Tableau de bord**, **Admin**, **Paramètres** et **Profil**.

Effectuons un peu de nettoyage de code. Supprimez tout le code trouvé dans le fichier **"page.tsx"** du dossier app et insérez le code suivant :

```tsx
// app/page.tsx
<main className="text-center h-screen flex justify-center items-center">
      <p>Page d'accueil</p>
 </main>

```

Le fichier **"page.tsx"** dans le dossier app servira de page d'accueil pour ce tutoriel. À l'intérieur du dossier app, créez un dossier "Profil", et à l'intérieur, créez un fichier "page.tsx". Ajoutez le code suivant :

```tsx
// profile/page.tsx

<main className="text-center h-screen flex justify-center items-center">
      <div>
        <h1>Page de profil</h1>        
      </div>
 </main>
```

Répétez ce processus pour les dossiers "Tableau de bord", "Admin" et "Paramètres". Chacun doit contenir un fichier "page.tsx". Si vous avez terminé cela, vous avez réussi à configurer vos routes.

Comme mentionné précédemment, nous discuterons des différentes façons de protéger vos routes.

## Protection des routes côté client

La protection des routes côté client est adaptée aux scénarios où vous souhaitez empêcher les utilisateurs non authentifiés d'accéder à certaines parties de votre application côté client.

Vous voudrez utiliser cela lorsque vous avez besoin d'une méthode rapide et simple pour protéger les routes sans processus d'authentification complexes. C'est idéal pour les sites web publics ou les zones avec des exigences de sécurité minimales.

Nous n'utiliserons aucun processus d'authentification pour garder le tutoriel simple. Au lieu de cela, nous créerons une fonction qui stocke la valeur d'authentification.

Pour rationaliser l'authentification, créez un fichier "Auth.ts" à l'intérieur du dossier Utils, qui doit être situé à la racine de l'application Next.js. Le fichier doit contenir le code suivant :

```ts
export const isAuthenticated = false;
```

Pour sécuriser votre route `Profil` dans un composant client, nous utiliserons `useLayoutEffect`. Voyons comment cela fonctionne en examinant le code ci-dessous :

```tsx
// profile/page.tsx

"use client";
import {isAuthenticated} from '@/Utils/Auth';
import { redirect } from 'next/navigation';
import { useLayoutEffect } from 'react';


const Profile = () => {

    useLayoutEffect(() => {
      const isAuth = isAuthenticated;
      if(!isAuth){
        redirect("/")
      }
    }, [])
   
  return (
    <main className="text-center h-screen flex justify-center items-center">
      <div>
        <h1>Profil</h1>        
      </div>
    </main>
  );
};


export default Profile;

```

Dans cet exemple de code, nous avons démontré une méthode simple mais efficace pour protéger les routes dans un composant client.

En combinant le hook `useLayoutEffect` avec une vérification d'authentification et la **fonction redirect**, nous avons établi un mécanisme de protection de route de base. Les utilisateurs non authentifiés sont redirigés de la route protégée vers la route "Accueil", améliorant la sécurité de votre application.

À l'intérieur du composant `Profil`, nous utilisons le hook `useLayoutEffect` pour vérifier le statut d'authentification de l'utilisateur lorsque le composant est monté. Nous appelons la fonction `isAuthenticated` et stockons son résultat dans la variable `isAuth`.

Si l'utilisateur est authentifié, `isAuth` sera vrai – sinon, il sera faux. Nous vérifions si l'utilisateur n'est pas authentifié (c'est-à-dire si `isAuth` est faux). Si ce n'est pas le cas, nous utilisons la fonction `redirect` pour les renvoyer à la page d'accueil ou à une autre page de destination. Cela empêche efficacement les utilisateurs non authentifiés d'accéder à la route protégée.

Alternativement, nous pouvons refactoriser le code ci-dessus pour protéger la route `Profil` en utilisant un **Higher Order Component (HOC)**, qui est une manière plus propre de sécuriser votre route côté client.

Pour utiliser un HOC, nous créerons un fichier à l'intérieur du dossier "components" appelé `isAuth` et ajouterons le code suivant :

```tsx
// isAuth.tsx

"use client";
import { isAuthenticated } from "@/Utils/Auth";
import { useEffect } from "react";
import { redirect } from "next/navigation";


export default function isAuth(Component: any) {
  return function IsAuth(props: any) {
    const auth = isAuthenticated;


    useEffect(() => {
      if (!auth) {
        return redirect("/");
      }
    }, []);


    if (!auth) {
      return null;
    }

    return <Component {...props} />;
  };
}

```

Le code ci-dessus définit un Higher Order Component (isAuth) qui vérifie le statut d'authentification de l'utilisateur. Si l'utilisateur n'est pas authentifié, il empêche le rendu du composant protégé et le redirige vers la page d'accueil.

Ce Higher Order Component sera utilisé pour protéger la route "Tableau de bord" dans notre application en enveloppant le composant protégé avec celui-ci, comme montré ci-dessous :

```tsx
// dashboard/page.tsx

import isAuth from "@/Components/isAuth";

const Dashboard = () => {
  return (
    <main className=" h-screen flex justify-center items-center">
      <p>Tableau de bord</p>
    </main>
  );
};


export default isAuth(Dashboard);

```

Le code ci-dessus intègre le HOC `isAuth` avec le composant Dashboard, garantissant que le tableau de bord est protégé et ne peut être accessible que par les utilisateurs authentifiés. Si un utilisateur n'est pas authentifié, il sera redirigé vers une autre route comme défini par le HOC `isAuth`.

Hourra ! Nous avons réussi à protéger nos routes côté client en utilisant à la fois `useLayoutEffect` et les Higher Order Components.

## Protection des routes côté serveur

La protection côté serveur est la méthode par défaut pour les composants Next.js. Elle est idéale pour garantir que le contenu rendu par le serveur est protégé. Vous l'utiliserez généralement lorsque vous devez protéger des routes qui ne doivent pas être accessibles aux utilisateurs non authentifiés, garantissant que les informations sensibles ne sont pas exposées.

Protéger vos routes côté serveur est simple. Nous pouvons convenir que tous les composants dans Next.js sont des composants serveur par défaut. Vous pouvez protéger vos routes côté serveur comme montré ci-dessous :

```tsx
// admin/page.tsx

import {isAuthenticated} from '@/Utils/Auth';
import { redirect } from 'next/navigation';


const Admin = () => {
    const isAuth = isAuthenticated;


    if(!isAuth) {
        redirect("/");
    }
  return (
    <main className="text-center h-screen flex justify-center items-center">
      <div>
        <h1>Page Admin</h1>
      </div>
    </main>
  );
};


export default Admin;
```

Le code ci-dessus démontre la protection des routes sur les composants serveur, garantissant que seuls les utilisateurs authentifiés peuvent accéder à la page d'administration. Si un utilisateur non authentifié tente d'accéder à cette route, il sera redirigé vers la page d'accueil.

## Protection des routes basée sur le middleware

La protection des routes basée sur le middleware dans Next.js est une approche puissante pour sécuriser et contrôler l'accès à des routes spécifiques au sein d'une application Next.js. Elle implique l'utilisation de fonctions middleware pour intercepter les requêtes entrantes et appliquer des règles concernant l'accessibilité des routes.

C'est une approche puissante adaptée aux scénarios où vous avez besoin d'un contrôle fin sur l'accès aux routes. Elle est souvent utilisée pour des applications plus complexes, surtout lorsqu'on traite des données sensibles ou des rôles et permissions des utilisateurs.

Le middleware vous permet d'intercepter les requêtes et d'appliquer des règles personnalisées, ce qui le rend parfait pour appliquer des politiques de sécurité strictes.

Ce concept est crucial pour garantir que seuls les utilisateurs autorisés peuvent accéder aux routes protégées, qui contiennent souvent des données sensibles ou nécessitent des privilèges spécifiques. La protection des routes basée sur le middleware peut être utilisée à la fois sur les composants serveur et client.

Nous allons protéger la route "Paramètres" en utilisant le middleware. Pour ce faire, nous créerons un fichier `middleware.ts`. Il est conventionnel de créer le fichier middleware dans le dossier racine (au même niveau que le dossier app ou page) ou à l'intérieur du dossier **src**, si applicable.

Nous protégerons ensuite notre route `Paramètres` en ajoutant le code suivant :

```ts
//middleware.ts

import { isAuthenticated } from "@/Utils/Auth";
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";


const protectedRoutes = ["/settings"];


export default function middleware(req: NextRequest) {
  if (!isAuthenticated && protectedRoutes.includes(req.nextUrl.pathname)) {
    const absoluteURL = new URL("/", req.nextUrl.origin);
    return NextResponse.redirect(absoluteURL.toString());
  }
}

```

Le code ci-dessus fournit une approche basée sur le middleware pour protéger la page "Paramètres" dans une application Next.js. Il vérifie si un utilisateur n'est pas authentifié et si le chemin demandé correspond à l'une des routes protégées.

Dans le code ci-dessus, `isAuthenticated` est importé du module @/Utils/Auth. Cette fonction est responsable de la vérification du statut d'authentification d'un utilisateur. Si un utilisateur est authentifié, elle retourne vrai – sinon, elle retourne faux.

`NextResponse` et `NextRequest` font partie de l'API des fonctions serverless de Next.js pour la gestion des requêtes et réponses HTTP.

Un tableau `protectedRoutes` est défini, contenant le ou les chemins des routes qui nécessitent une protection. Dans ce cas, il inclut la route `/settings`. La fonction middleware est exécutée avant de traiter une requête et sert de middleware responsable de la protection des routes.

Dans la fonction middleware, elle vérifie si l'utilisateur n'est pas authentifié (`!isAuthenticated`) et si le chemin demandé (`req.nextUrl.pathname`) correspond à l'une des routes protégées. Si les deux conditions sont remplies, elle construit une URL absolue qui pointe vers le chemin racine ("/") de l'application en utilisant une nouvelle URL ("/", req.nextUrl.origin). Elle utilise ensuite `NextResponse.redirect` pour effectuer une redirection vers l'URL absolue construite.

## Conclusion

La protection des routes est un aspect indispensable du développement d'applications web, surtout lorsqu'on traite des données sensibles ou qu'on restreint l'accès à des fonctionnalités spécifiques.

Dans ce tutoriel, nous avons exploré trois méthodes complètes pour sécuriser les routes dans Next.js 13, garantissant que les utilisateurs non autorisés sont tenus à distance. En mettant en œuvre ces techniques, vous pouvez renforcer la sécurité de votre application et améliorer l'expérience utilisateur globale.

Avec les connaissances acquises dans ce tutoriel, vous êtes bien équipé pour protéger les routes de votre application Next.js, créant une expérience plus sécurisée et conviviale. Que vous choisissiez la protection côté client, côté serveur ou basée sur le middleware, l'objectif reste le même : protéger l'intégrité de votre application et les données de vos utilisateurs.

Si vous avez des questions ou avez besoin d'aide supplémentaire, n'hésitez pas à explorer des ressources supplémentaires ou à contacter la communauté Next.js. Vous pouvez également accéder au CodeSandbox pour ce tutoriel [ici](https://codesandbox.io/p/sandbox/next-private-route-tutorial-456dmq?file=%2Fmiddleware.ts%3A9%2C2).

Bon codage et routage sécurisé dans vos applications Next.js !