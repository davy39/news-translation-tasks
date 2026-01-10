---
title: 'Clerk vs Kinde vs Better Auth : Comment choisir la bonne bibliothèque d''authentification
  Next.js'
subtitle: ''
author: Andrew Baisden
co_authors: []
series: null
date: '2025-09-23T02:34:54.472Z'
originalURL: https://freecodecamp.org/news/how-to-choose-the-right-nextjs-authentication-library
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758594098828/8b2e3142-9067-4a02-b1e5-63319dde45de.png
tags:
- name: Next.js
  slug: nextjs
- name: authentication
  slug: authentication
seo_title: 'Clerk vs Kinde vs Better Auth : Comment choisir la bonne bibliothèque
  d''authentification Next.js'
seo_desc: Authentication is an important aspect when building applications, especially
  if they hold financial information or require users to sign into accounts. Building
  an auth library can be a lot of work, and there is no need to reinvent the wheel
  when so ...
---

L'authentification est un aspect crucial lors de la création d'applications, en particulier si elles détiennent des informations financières ou nécessitent que les utilisateurs se connectent à des comptes. Créer une bibliothèque d'authentification peut représenter beaucoup de travail, et il n'est pas nécessaire de réinventer la roue alors que de nombreuses bibliothèques efficaces existent déjà.

Dans cet article, nous allons comparer quelques bibliothèques que vous pouvez utiliser pour l'authentification dans votre application Next.js. Elles incluent : [Clerk](https://clerk.com/), [Kinde](https://kinde.com/) et [Better Auth](https://www.better-auth.com/). Vous apprendrez comment configurer ces outils dans une application Next.js, avec pour objectif de créer au moins une route de page authentifiée et protégée.

Le but ici est simplement de voir comment chaque outil fonctionne en termes de rapidité de configuration et de facilité d'utilisation.

## Table des matières

* [Que sont Clerk, Kinde et Better Auth ?](#heading-que-sont-clerk-kinde-et-better-auth)
    
* [Prérequis](#heading-prerequis)
    
* [Comment configurer l'authentification avec Clerk](#heading-comment-configurer-lauthentification-avec-clerk)
    
* [Comment configurer l'authentification avec Kinde](#heading-comment-configurer-lauthentification-avec-kinde)
    
* [Comment configurer l'authentification avec Better Auth](#heading-comment-configurer-lauthentification-avec-better-auth)
    
* [Quand utiliser chaque bibliothèque](#heading-quand-utiliser-chaque-bibliotheque)
    
* [Conclusion](#heading-conclusion)
    

## Que sont Clerk, Kinde et Better Auth ?

Clerk, Kinde et Better Auth sont essentiellement des fournisseurs d'authentification modernes, tout comme [Auth.js](https://authjs.dev/), qui ont été conçus pour les développeurs. Bien qu'ils partagent des similitudes, ils présentent certains aspects qui les différencient les uns des autres.

Pour commencer, Clerk est le plus complet. Il s'agit plutôt d'une solution hébergée qui propose des composants prêts à l'emploi, ainsi qu'une gestion des utilisateurs et d'autres intégrations, ce qui vous permet d'être opérationnel assez rapidement.

Kinde, en revanche, est davantage une plateforme pour développeurs, qui regroupe l'authentification, les feature flags et la gestion d'équipe en un seul endroit.

Better Auth est plutôt une solution open-source et "code-first" qui donne aux développeurs les briques de base pour créer une authentification sans être enfermé dans un écosystème (vendor lock-in).

## Prérequis

Les prérequis pour ce tutoriel sont minimaux, et les bases de données ainsi que l'ORM Prisma ne sont requis que pour Better Auth. Alternativement, vous pouvez utiliser n'importe quelle base de données dans un conteneur Docker au lieu de les installer localement, mais cela dépasse le cadre de ce tutoriel.

Vous aurez besoin de ces éléments pour suivre :

* Node et npm installés
    
* [Prisma ORM](https://www.prisma.io/)
    
* Base de données SQLite, PostgreSQL ou MySQL configurée localement
    
* Éditeur de code/IDE
    

Voyons comment configurer l'authentification avec ces trois plateformes dans une application Next.js. Nous utiliserons des applications Next.js distinctes pour configurer chaque bibliothèque afin que la base de code reste propre et que vous puissiez expérimenter ce que c'est que de les configurer de zéro.

Tout d'abord, choisissez un emplacement pour votre projet, par exemple sur le bureau, puis utilisez la commande `npx create-next-app@latest` pour configurer un projet Next.js. Vous pouvez simplement utiliser la configuration par défaut. Voici les paramètres que j'ai utilisés :

✔ What is your project named? … my-app  
✔ Would you like to use TypeScript? … No / **Yes**  
✔ Which linter would you like to use? › ESLint  
✔ Would you like to use Tailwind CSS? … No / **Yes**  
✔ Would you like your code inside a `src/` directory? … No / **Yes**  
✔ Would you like to use App Router? (recommended) … No / **Yes**  
✔ Would you like to use Turbopack? (recommended) … No / **Yes**  
✔ Would you like to customize the import alias (`@/*` by default)? … **No** / Yes

Nous créons trois applications, c'est donc à vous de décider si vous voulez dupliquer les bases de code maintenant et leur donner des noms différents comme `my-app`, `my-app2` et `my-app3` ou le faire plus tard lorsque nous atteindrons chaque section.

## Comment configurer l'authentification avec Clerk

Une fois votre projet Next.js configuré, faites un `cd` dans le dossier `my-app` ou le nom que vous avez donné au projet et lancez la commande suivante pour installer le SDK Next.js pour Clerk :

```shell
npm install @clerk/nextjs
```

Maintenant, nous devons créer un fichier middleware qui nous donnera accès à l'authentification utilisateur dans toute notre application.

Créez un fichier `middleware.ts` avec ce code à l'intérieur du dossier `/src` :

```typescript
import { clerkMiddleware } from '@clerk/nextjs/server'

export default clerkMiddleware()

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}
```

Avec ce fichier, l'authentification est configurée pour différentes routes de pages.

Il ne reste plus qu'à ajouter le composant `<ClerkProvider>` au fichier `layout.tsx` de votre application afin que l'authentification soit disponible dans toute votre application.

Remplacez simplement tout le code à l'intérieur de `src/app/layout.tsx` par ce code ici :

```typescript
import type { Metadata } from 'next';
import { Geist, Geist_Mono } from 'next/font/google';
import './globals.css';
import {
  ClerkProvider,
  SignInButton,
  SignUpButton,
  SignedIn,
  SignedOut,
  UserButton,
} from '@clerk/nextjs';

const geistSans = Geist({
  variable: '--font-geist-sans',
  subsets: ['latin'],
});

const geistMono = Geist_Mono({
  variable: '--font-geist-mono',
  subsets: ['latin'],
});

export const metadata: Metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body
          className={`${geistSans.variable} ${geistMono.variable} antialiased`}
        >
          <header className="flex justify-end items-center p-4 gap-4 h-16">
            <SignedOut>
              <SignInButton />
              <SignUpButton>
                <button className="bg-[#6c47ff] text-white rounded-full font-medium text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 cursor-pointer">
                  Sign Up
                </button>
              </SignUpButton>
            </SignedOut>
            <SignedIn>
              <UserButton />
            </SignedIn>
          </header>
          {children}
        </body>
      </html>
    </ClerkProvider>
  );
}
```

Ce que nous avons fait, c'est importer le `ClerkProvider`, ainsi que les boutons pour se connecter et s'inscrire en utilisant l'authentification Clerk. Ces ajouts ont été faits au fichier `layout.tsx`, ce qui signifie qu'ils sont disponibles dans toute notre application. Ainsi, chaque page devrait afficher le flux de connexion en haut de la page.

Le composant `ClerkProvider` est nécessaire pour intégrer Clerk à l'intérieur de notre application, nous pouvons donc maintenant utiliser le contexte de session et d'utilisateur avec les hooks et composants de Clerk.

Vous pouvez maintenant lancer votre application Next.js avec `npm run dev`, et vous devriez voir la page d'accueil, ainsi qu'un bouton de connexion et d'inscription en haut de la page, comme montré ici :

![Page d'accueil Next.js avec configuration de l'authentification Clerk](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428533274/31f43e8f-7826-4d4c-bf10-99b5ea7d8a76.png align="center")

Cliquer sur le bouton d'inscription vous mènera à un formulaire d'inscription où vous pourrez utiliser une adresse e-mail ou vous connecter avec Google, ce qui est assez facile.

![Formulaire d'inscription Clerk](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428605871/94e754e7-897f-42f2-84df-361d97226617.png align="center")

Une fois connecté, vous devriez voir votre photo de profil et les informations de votre compte dans le coin supérieur droit de l'écran. La partie difficile est faite - il ne reste plus qu'à créer une page puis à rendre la route protégée afin que seul un utilisateur connecté puisse y accéder.

Pour commencer, mettons à jour notre fichier `middleware.ts` avec du code qui nous permet de protéger une route :

```typescript
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isProtectedRoute = createRouteMatcher(['/dashboard(.*)'])

export default clerkMiddleware(async (auth, req) => {
  if (isProtectedRoute(req)) await auth.protect()
})

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}
```

Nous avons ajouté de nouveaux imports pour `createRouteMatcher`, qui est une fonction utilitaire de Clerk nous donnant le pouvoir de protéger plusieurs routes. Dans ce cas, la route de la page dashboard de notre application nécessite qu'un utilisateur soit connecté pour accéder à la route. Maintenant, nous devons créer une page dashboard. Créez ce dossier et ce fichier à l'intérieur du dossier `app` : `dashboard/page.tsx`. Complétez ensuite la page en y ajoutant un code comme celui-ci :

```typescript
export default function Dashboard() {
  return (
    <>
      <h1>Dashboard Page</h1>
    </>
  );
}
```

Nous avons créé une page simple qui possède un titre indiquant "Dashboard Page".

Félicitations, vous avez ajouté avec succès l'authentification à votre application Next et protégé une route de page, et cela n'a pris que quelques étapes ! Lorsque vous naviguez vers [http://localhost:3000/dashboard](http://localhost:3000/dashboard) en tant qu'utilisateur non connecté, vous devriez être redirigé vers un formulaire de connexion comme indiqué ci-dessous :

![Page du formulaire de connexion Clerk](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428660606/5ac6984d-7f8c-46e2-bd0b-732920d5743e.png align="center")

Si vous êtes déjà connecté, vous devriez voir la page Dashboard. Vous pouvez en apprendre plus en utilisant la [documentation officielle de Clerk](https://clerk.com/docs).

## Comment configurer l'authentification avec Kinde

Créez une autre application Next.js pour ce projet si vous ne l'avez pas déjà fait. Kinde vous demandera de créer un compte sur leur plateforme avant d'utiliser leur bibliothèque d'authentification. Passons par le processus d'inscription.

Premièrement, allez sur le site de [Kinde](https://kinde.com/), et vous devriez voir un bouton indiquant "Start for free" ou similaire.

![Page d'accueil du site Kinde](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428704023/dd6bf59e-2858-4f0a-8aa4-90645641ebe8.png align="center")

Cliquer sur ce bouton devrait vous mener à une page où vous pouvez créer un compte :

![Kinde créer votre compte](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428737190/0cd172f6-ed9a-4a54-b599-182a8becfcfa.png align="center")

Une vérification du code par e-mail peut être requise :

![Kinde vérification du code e-mail](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428803166/8a883160-6e95-4611-91d3-efbabd74653c.png align="center")

Sur l'écran suivant, vous devriez pouvoir entrer les détails de votre entreprise, qui peuvent être ce que vous voulez. Chaque fois que vous configurez l'authentification pour une application, vous devrez créer une application pour celle-ci sur votre compte. Donnez-lui le nom que vous voulez, comme `app-clerk-test3272346214`. Le même nom sera utilisé pour l'entreprise et le domaine.

![Formulaire Kinde entreprise et domaine](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428845977/7d365554-9c15-41e0-b317-a12d58f3e7a6.png align="center")

Sur l'écran suivant, nous choisirons d'utiliser une base de code existante car nous avons un projet local :

![Kinde sélection de base de code existante](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428896749/cd468f14-1b36-4025-8459-b51509519fa0.png align="center")

La base de code est en Next.js, sélectionnez-le donc dans la liste :

![Kinde sélection de la pile technique](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428936691/cf13041f-bc74-4432-a7ba-4234daf7c2a3.png align="center")

La prochaine étape importante est de choisir comment les utilisateurs vont se connecter. J'ai choisi l'e-mail et Google. Vous pouvez sélectionner les options que vous désirez :

![Formulaire de connexion utilisateur Kinde](https://cdn.hashnode.com/res/hashnode/image/upload/v1757428976433/2885ed25-d4d0-496e-ac46-2f8b96c35a20.png align="center")

Maintenant, sur le dernier écran, choisissez d'explorer à votre propre rythme.

![Écran Kinde explorer à son rythme](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429011937/23a9d95f-2935-4a9c-947f-91d7adaf452e.png align="center")

Et enfin, nous avons atteint l'écran du tableau de bord.

![Écran du tableau de bord Kinde](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429051925/2250e252-e84d-4ae9-bff8-a9e687692f70.png align="center")

Consulter les détails vous permet de voir vos clés d'application et vos variables d'environnement, entre autres informations utiles.

C'en est fini pour la partie longue, passons au code. Naviguez vers votre dossier de projet puis installez le package pour Kinde :

```shell
npm i @kinde-oss/kinde-auth-nextjs
```

Maintenant, créez un fichier `.env.local` et placez-le dans le dossier racine de votre projet avec vos variables d'environnement. Vous pouvez trouver vos variables d'environnement dans la page Quick Start de votre application.

Voici un exemple :

```shell
KINDE_CLIENT_ID=<votre_kinde_client_id>
KINDE_CLIENT_SECRET=<votre_kinde_client_secret>
KINDE_ISSUER_URL=https://<votre_sous_domaine_kinde>.kinde.com
KINDE_SITE_URL=http://localhost:3000
KINDE_POST_LOGOUT_REDIRECT_URL=http://localhost:3000
KINDE_POST_LOGIN_REDIRECT_URL=http://localhost:3000/dashboard
```

Ensuite, vous devez créer l'endpoint API suivant ainsi que la structure de dossiers et les fichiers comme indiqué ici `src/app/api/auth/[kindeAuth]/route.ts`.

Voici le code nécessaire pour le fichier `route.ts` :

```shell
import {handleAuth} from "@kinde-oss/kinde-auth-nextjs/server";

export const GET = handleAuth();
```

Avec ce code, Kinde peut désormais gérer les endpoints d'authentification à l'intérieur de notre application.

Une fois de plus, vous aurez besoin d'un fichier `middleware.ts` pour que l'authentification puisse être configurée correctement dans votre application. Le fichier doit se trouver dans le répertoire racine et nécessite l'ajout de ce code :

```typescript
import { withAuth } from "@kinde-oss/kinde-auth-nextjs/middleware";

export default function middleware(req) {
  return withAuth(req);
}

export const config = {
  matcher: [
    // Run on everything but Next internals and static files
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
  ]
};
```

Comme précédemment, nous pouvons maintenant protéger les routes de pages avec ce fichier. Votre application doit être enveloppée dans un Kinde Auth Provider afin que vous puissiez accéder aux données dans toute votre application.

Créez un fichier `AuthProvider.tsx` à l'intérieur du répertoire `app` avec ce code :

```typescript
"use client";
import {KindeProvider} from "@kinde-oss/kinde-auth-nextjs";

export const AuthProvider = ({children}) => {
  return <KindeProvider>{children}</KindeProvider>;
};
```

Kinde utilise un React Context Provider pour maintenir son état interne dans toute notre application en utilisant le composant `KindeProvider`.

Ensuite, remplacez et mettez à jour le fichier `layout.tsx`, afin qu'il soit enveloppé dans l'Auth Provider :

```typescript
import type { Metadata } from 'next';
import { Geist, Geist_Mono } from 'next/font/google';
import './globals.css';
import { AuthProvider } from './AuthProvider';
import {
  RegisterLink,
  LoginLink,
  LogoutLink,
} from '@kinde-oss/kinde-auth-nextjs/components';

const geistSans = Geist({
  variable: '--font-geist-sans',
  subsets: ['latin'],
});

const geistMono = Geist_Mono({
  variable: '--font-geist-mono',
  subsets: ['latin'],
});

export const metadata: Metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <AuthProvider>
      <div className="grid grid-flow-col gap2">
        <LoginLink>Sign in</LoginLink>
        <RegisterLink>Sign up</RegisterLink>
        <LogoutLink>Log out</LogoutLink>
      </div>
      <html lang="en">
        <body
          className={`${geistSans.variable} ${geistMono.variable} antialiased`}
        >
          {children}
        </body>
      </html>
    </AuthProvider>
  );
}
```

Dans ce fichier, nous avons également ajouté des boutons pour s'inscrire, se connecter et se déconnecter qui seront affichés en haut de chaque page car il s'agit du fichier `layout.tsx` principal. Notre composant `AuthProvider` est enveloppé autour de notre application, ce qui signifie que nous pouvons maintenant utiliser Kinde partout.

La configuration de base est maintenant terminée ! Lancez la commande habituelle pour démarrer l'application Next.js, et vous devriez voir les boutons du flux de connexion en haut de l'écran.

Vous devriez pouvoir vous inscrire et créer un compte. Cela vous redirigera vers l'écran du tableau de bord, qui affiche une page d'erreur 404. C'est parce que nous n'avons pas encore créé de page dashboard.

Voici à quoi ressemble le formulaire d'inscription Kinde :

![Formulaire d'inscription Kinde](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429157871/c7344f32-cf4e-48d3-b43e-225f81912988.png align="center")

Et voici à quoi ressemble le formulaire de connexion Kinde :

![Formulaire de connexion Kinde](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429447577/3d30476a-9269-49a9-811c-dff0c16225d9.png align="center")

Il ne reste qu'une étape : créer une route protégée pour votre authentification.

Créez la structure de fichiers et le fichier suivants pour votre page dashboard : `src/app/dashboard/page.tsx`.

Ajoutez ensuite ce code au fichier :

```typescript
'use client';

import { useKindeBrowserClient } from '@kinde-oss/kinde-auth-nextjs';
import { LoginLink } from '@kinde-oss/kinde-auth-nextjs/components';

export default function Dashboard() {
  const { isAuthenticated, isLoading } = useKindeBrowserClient();

  if (isLoading) return <div>Loading...</div>;

  return isAuthenticated ? (
    <div>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ut
        ante enim. Maecenas ut eros nec diam vulputate sollicitudin. Cras ut
        quam leo. Pellentesque semper, lacus sodales gravida suscipit, metus
        quam congue eros, nec sagittis est dolor eu turpis. Nulla congue
        tristique venenatis. Donec ac venenatis mauris. Donec commodo cursus
        magna, vitae tincidunt magna vestibulum eget.
      </p>
    </div>
  ) : (
    <div>
      You have to <LoginLink>Login</LoginLink> to see this page
    </div>
  );
}
```

Ce fichier de page vérifie si l'utilisateur est authentifié et connecté. S'il est connecté, il voit le texte Lorem ipsum, et s'il n'est pas connecté, il verra un message lui indiquant qu'il doit se connecter pour voir la page.

Tout ce que vous avez à faire est d'aller sur la [route dashboard](http://localhost:3000/dashboard) en tant qu'utilisateur connecté ou déconnecté pour le voir par vous-même. Et c'est à peu près tout pour les bases de l'authentification en utilisant la plateforme Kinde. Consultez la [documentation en ligne](https://docs.kinde.com/) pour apprendre tout ce qu'il y a à savoir à ce sujet.

## Comment configurer l'authentification avec Better Auth

Et enfin, créons un projet qui utilise Better Auth. Better Auth nécessite une base de données pour stocker les données utilisateur, la configuration nécessitera donc quelques étapes supplémentaires. Vous pouvez trouver le guide d'installation [ici](https://www.better-auth.com/docs/installation), mais nous allons également le parcourir ici.

Ok, tout comme avant, créez un projet Next.js si vous ne l'avez pas encore fait, puis installez le package `better-auth` avec cette commande :

```shell
npm install better-auth
```

Ensuite, vous devez configurer vos variables d'environnement, créez donc un fichier `.env` avec ces valeurs :

```shell
BETTER_AUTH_SECRET= #Créez votre propre clé secrète !
BETTER_AUTH_URL=http://localhost:3000 # URL de base de votre application
```

Assurez-vous de créer une clé secrète robuste, comme si vous génériez un mot de passe sécurisé avec des majuscules, des minuscules et des chiffres.

Configurons notre package Prisma et notre base de données PostgreSQL, lancez donc ces scripts pour les initialiser :

```shell
npm install prisma --save-dev
npx prisma init
npm install @prisma/client
```

Dans l'étape suivante, nous devons créer une instance better auth. Dans ce cas, nous placerons le fichier dans `src/lib/auth.ts`.

Créez donc un fichier `auth.ts` avec ce code :

```typescript
import { betterAuth } from 'better-auth';
import { anonymous } from 'better-auth/plugins';
import { prismaAdapter } from 'better-auth/adapters/prisma';
// Si votre fichier Prisma est situé ailleurs, vous pouvez changer le chemin
import { PrismaClient } from '@/generated/prisma';

const prisma = new PrismaClient();
export const auth = betterAuth({
  database: prismaAdapter(prisma, {
    provider: 'postgresql', // ou "mysql", "postgresql", ...etc
  }),
  plugins: [anonymous()],
});
```

Dans ce fichier, nous avons configuré Better Auth pour utiliser l'ORM Prisma pour notre connexion à la base de données, et nous nous connecterons à une base de données PostgreSQL. Si vous le souhaitez, vous pouvez passer à une autre base de données, mais la configuration pourrait être différente, gardez cela à l'esprit. Vous pourriez également utiliser Docker si vous savez comment le configurer. La connexion anonyme est activée par défaut pour les utilisateurs.

Maintenant, nous devons créer nos tables de base de données pour sauvegarder les informations utilisateur, utilisez donc cette commande dans le terminal pour le faire :

```shell
npx @better-auth/cli generate
```

Vous pourriez voir cet avertissement, sélectionnez simplement oui avec "y" :

```shell
prisma:warn In production, we recommend using `prisma generate --no-engine` (See: `prisma generate --help`)
✔ The file ./prisma/schema.prisma already exists. Do you want to overwrite the schema to the file? … yes
```

Pour gérer les requêtes API, nous devons avoir un gestionnaire de route configuré sur notre serveur. Créez une structure de dossiers et un fichier pour le fichier `route.ts`, comme indiqué ici `/app/api/auth/[...all]/route.ts`.

Ajoutez ce code au fichier :

```typescript
import { auth } from '@/lib/auth'; // chemin vers votre fichier auth
import { toNextJsHandler } from 'better-auth/next-js';

export const { POST, GET } = toNextJsHandler(auth);
```

Ce fichier vous permet de gérer les requêtes POST et GET pour votre fichier auth.

Enfin, nous devons créer un fichier `lib/auth-client.ts`. Ce fichier vous permet d'interagir avec le serveur d'authentification, et il possède un plugin pour que les utilisateurs puissent se connecter anonymement.

Et voici le code à mettre dans ce fichier :

```typescript
import { createAuthClient } from 'better-auth/react';
import { anonymousClient } from 'better-auth/client/plugins';
export const authClient = createAuthClient({
  /** L'URL de base du serveur (optionnel si vous utilisez le même domaine) */
  baseURL: 'http://localhost:3000',
  plugins: [anonymousClient()],
});
```

Avec ce fichier, il est possible pour les utilisateurs de se connecter anonymement sans même avoir à créer un compte ou utiliser une connexion sociale, grâce au plugin.

Il ne reste plus qu'à créer une autre page dashboard, qui possède une authentification comme précédemment. Créez une autre page dashboard avec cette structure : `app/dashboard/page.tsx`, puis ajoutez ce code au fichier :

```typescript
'use client';

import { useState, useEffect } from 'react';
import { authClient } from '@/lib/auth-client';

type User = {
  id: string;
  email: string;
  emailVerified: boolean;
  name: string;
  createdAt: Date;
  updatedAt: Date;
  image?: string | null;
  isAnonymous?: boolean | null;
};

export default function Dashboard() {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isSigningIn, setIsSigningIn] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const session = await authClient.getSession();
        if (session.data?.user) {
          setUser(session.data.user);
        }
      } catch (err) {
        console.error('Auth check error:', err);
      } finally {
        setIsLoading(false);
      }
    };

    checkAuth();
  }, []);

  const handleAnonymousSignIn = async () => {
    try {
      setIsSigningIn(true);
      setError(null);

      const result = await authClient.signIn.anonymous();

      if (result.data) {
        setUser(result.data.user);
        console.log('Anonymous user signed in:', result.data.user);
      } else if (result.error) {
        setError(result.error.message || 'Failed to sign in anonymously');
      }
    } catch (err) {
      setError('An unexpected error occurred');
      console.error('Anonymous sign-in error:', err);
    } finally {
      setIsSigningIn(false);
    }
  };

  const handleSignOut = async () => {
    try {
      await authClient.signOut();
      setUser(null);
    } catch (err) {
      console.error('Sign out error:', err);
    }
  };

  if (isLoading) {
    return (
      <div className="max-w-4xl mx-auto p-6">
        <div className="flex items-center justify-center min-h-[400px]">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto mb-4"></div>
            <p className="text-gray-600">Checking authentication...</p>
          </div>
        </div>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="max-w-4xl mx-auto p-6">
        <div className="text-center">
          <h1 className="text-3xl font-bold mb-6">Access Required</h1>
          <p className="text-gray-600 mb-8">
            You need to be signed in to access our dashboard. Choose an option
            below to continue.
          </p>

          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6 max-w-md mx-auto">
              {error}
            </div>
          )}

          <div className="bg-gray-50 p-8 rounded-lg border max-w-md mx-auto">
            <h2 className="text-xl font-semibold mb-4 text-black">
              Sign In Options
            </h2>

            <button
              onClick={handleAnonymousSignIn}
              disabled={isSigningIn}
              className="w-full bg-blue-500 hover:bg-blue-600 disabled:bg-blue-300 text-white px-6 py-3 rounded font-medium mb-4"
            >
              {isSigningIn ? 'Signing in...' : 'Sign In Anonymously'}
            </button>

            <p className="text-sm text-gray-500 mb-4">
              Anonymous access allows you to use our dashboard without creating
              an account. You can always link your account later.
            </p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-lg font-semibold text-green-800">
              Welcome, {user.isAnonymous ? 'Anonymous User' : user.name}!
            </h2>
            <p className="text-sm text-green-600">
              {user.isAnonymous
                ? 'You are signed in anonymously'
                : `Signed in as ${user.email}`}
            </p>
          </div>
          <button
            onClick={handleSignOut}
            className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded text-sm"
          >
            Sign Out
          </button>
        </div>
      </div>

      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

      {process.env.NODE_ENV === 'development' && (
        <div className="mt-8 bg-gray-100 p-4 rounded-lg">
          <h3 className="font-semibold mb-2 text-black">Debug Info:</h3>
          <pre className="text-xs text-gray-600 overflow-auto">
            {JSON.stringify(user, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
```

Ce code crée une page dashboard qui nécessite qu'un utilisateur soit authentifié et connecté pour l'utiliser. Après qu'un utilisateur se soit connecté anonymement, il peut voir des informations de débogage sur son profil. Fondamentalement, cette page est un flux d'authentification pour notre vue dashboard qui s'intègre à notre `authClient` personnalisé. Cette page gère également l'état de chargement, les erreurs et la déconnexion pour les utilisateurs anonymes.

Ok, maintenant nous devons probablement réinitialiser notre base de données Prisma, sinon nous pourrions avoir des erreurs de schéma et de table.

Tout d'abord, assurez-vous que votre base de données de développement Prisma fonctionne avec cette commande :

```shell
npx prisma dev
```

Puis lancez ces commandes pour réinitialiser la base de données et appliquer les nouvelles migrations pour le schéma :

```shell
npx prisma migrate reset
npx prisma migrate dev
```

Vous pourriez avoir besoin de redémarrer le serveur de développement Prisma puis de le lancer avec la commande `npx prisma dev`.

our application Better Auth nécessite que deux serveurs fonctionnent.

1. Le serveur de développement Prisma
    
2. L'application Next.js
    

Avec le serveur de développement Prisma en cours d'exécution, vous pouvez maintenant démarrer l'application Next.js avec la commande habituelle `npm run dev`.

Si vous rencontrez des problèmes avec l'ORM Prisma ou la base de données, comme des tables manquantes ou des discordances de schéma, voici quelques commandes utiles qui pourraient, espérons-le, les résoudre.

```shell
# ⚠️ ATTENTION : Cela supprimera la base de données, la recréera et appliquera toutes les migrations de zéro.
npx prisma migrate reset

# Applique toutes les nouvelles migrations qui n'ont pas encore été exécutées (ou en crée une nouvelle si votre schéma a changé).
npx prisma migrate dev

# Démarre Prisma Studio (une interface graphique pour explorer et éditer votre base de données).
npx prisma dev

# Exécute les migrations CLI de Better Auth (configure toutes les tables/changements de base de données requis pour l'authentification).
npx @better-auth/cli migrate
```

Ces commandes sont explicites et nous permettent d'exécuter des migrations sur notre base de données lorsqu'il y a des changements, et nous pouvons voir notre base de données à l'intérieur de Prisma Studio.

Voici à quoi ressemble la page dashboard lorsqu'un utilisateur n'est pas connecté :

![Page Dashboard de l'application Better Auth](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429500439/9c0846fc-cfc5-4232-9a02-4e313c2c4698.png align="center")

Se connecter affichera l'écran du tableau de bord. Pour en savoir plus sur Better Auth, vous pouvez lire leur [documentation officielle](https://www.better-auth.com/).

## Quand utiliser chaque bibliothèque

Chacune de ces bibliothèques d'authentification a ses avantages et ses inconvénients, et peut répondre à divers besoins selon votre projet. Savoir quand utiliser chacune d'elles peut mieux vous préparer aux conditions réelles et lors de la création pour la production, passons-les donc en revue et voyons comment elles se comparent.

### Quand utiliser Clerk

Clerk excelle lorsque vous avez besoin d'utiliser l'authentification rapidement sans vous soucier de la gestion de plusieurs serveurs, et lorsque vous avez besoin d'interfaces et de systèmes de gestion pré-conçus. C'est idéal pour les start-ups et les équipes qui veulent donner la priorité à l'expérience développeur et à une mise en œuvre rapide.

Il possède une configuration simplifiée et conviviale, qui est tout de même capable de supporter le strict nécessaire, c'est donc une très bonne option pour les petites équipes et les projets qui doivent avoir une mise en œuvre facile. Si vous construisez un SaaS qui nécessite une bonne interface et des composants dès le départ, ou si vous avez besoin de connexions sociales sans une tonne de code, c'est une très bonne solution, surtout si vous voulez de la rapidité et de la rentabilité dans un projet plus petit.

### Quand utiliser Kinde

Kinde est un choix fantastique lorsque vous tenez à avoir une tarification transparente et une intégration rapide de l'authentification dans davantage de frameworks. Kinde a été conçu pour être une alternative rentable à Clerk et offre une tarification plus transparente et un niveau gratuit plus généreux.

C'est idéal pour les équipes qui ont besoin d'une option d'authentification fiable mais qui veulent des coûts inférieurs et un meilleur support des frameworks. Kinde est efficace lorsqu'il est utilisé dans des projets de taille moyenne qui ont besoin de plus qu'un système d'authentification de base, mais qui n'ont pas non plus besoin d'outillage de classe entreprise.

### Quand utiliser Better Auth

Better Auth est une excellente solution lorsque vous avez besoin d'un ensemble étendu de fonctionnalités prêtes à l'emploi. Il convient également de noter que Better Auth possède un écosystème de plugins qui peut simplifier l'ajout de fonctionnalités plus avancées avec seulement quelques lignes de code. De toutes les options discutées dans cet article, Better Auth est de loin la plus propre ; cependant, elle nécessite plus de connaissances et de compétences en programmation.

C'est une bonne option si vous construisez une application TypeScript et que vous voulez avoir un contrôle total sur la personnalisation et les flux de données d'authentification. Le framework est agnostique et possède des fonctionnalités telles que la 2FA, le support multi-tenant et d'autres fonctionnalités complexes afin que les développeurs puissent tirer le meilleur parti de l'outil, car il n'y a pas de dépendance vis-à-vis d'un fournisseur (vendor lock-in). Les fonctionnalités peuvent être facilement étendues avec l'écosystème de plugins, afin que les développeurs puissent l'adapter à leurs besoins.

## Conclusion

Les trois plateformes sont assez bonnes dans leur domaine, et je ne doute pas qu'elles resteront des options populaires pour ajouter l'authentification à nos applications. Auth.js est l'une des plus connues ; cependant, Clerk, Kinde et Better Auth semblent également avoir une base d'utilisateurs croissante et, à en juger par les conversations sur les réseaux sociaux, elles semblent être le premier choix de nombreux développeurs en ce moment.

Après avoir expérimenté ce que c'est que de les configurer pour la première fois, je dirais que Clerk est le plus facile à configurer car vous n'avez pas besoin de créer un compte (pour commencer les tests locaux rapidement) et vous pouvez faire fonctionner l'authentification assez vite avec peu de dépannage. Kinde serait le deuxième plus facile à configurer, à mon avis. Vous devez vous inscrire pour un compte pour utiliser la plateforme ; cependant, la configuration était également assez facile et n'a nécessité aucun dépannage.

Better Auth est une excellente plateforme, mais la configuration nécessite un peu plus de travail car une base de données est requise pour stocker les informations des utilisateurs, ce qui rend le processus légèrement plus difficile. J'ai également trouvé plus facile de créer des routes authentifiées avec les deux autres options d'authentification. Cependant, le fait que la plateforme soit open-source sans dépendance vis-à-vis d'un fournisseur joue en sa faveur car les développeurs peuvent l'auto-héberger et c'est complètement gratuit, ce qui signifie qu'il n'y a pas de plans payants.