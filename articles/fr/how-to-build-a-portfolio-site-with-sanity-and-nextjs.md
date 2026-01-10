---
title: Comment créer un site portfolio avec Sanity et Next.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-28T16:30:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-portfolio-site-with-sanity-and-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Sanity-1.png
tags:
- name: headless cms
  slug: headless-cms
- name: Next.js
  slug: nextjs
- name: portfolio
  slug: portfolio
seo_title: Comment créer un site portfolio avec Sanity et Next.js
seo_desc: "By Victor Eke\nKnowing how to handle content is important when creating\
  \ a personal website for yourself or a client. \nThis is because maintaining and\
  \ updating a site can result in substantial expenses if you don't do it correctly.\
  \ This is even more th..."
---

Par Victor Eke

Savoir gérer le contenu est important lors de la création d'un site web personnel pour vous-même ou pour un client. 

C'est parce que la maintenance et la mise à jour d'un site peuvent entraîner des dépenses substantielles si vous ne le faites pas correctement. C'est encore plus le cas si vous construisez pour quelqu'un avec un background non technique.

Pour résoudre ce problème, vous pouvez intégrer votre site web avec un service [headless CMS](https://www.sanity.io/headless-cms) qui offre une API pour la gestion et les mises à jour de contenu. Dans ce cas, nous utiliserons [Sanity](https://sanity.io) à cette fin.

## Table des matières:

1. [Qu'est-ce que Sanity ?](#heading-quest-ce-que-sanity)
2. [Étape 1 : Installer Next.js](#heading-etape-1-installer-nextjs)
3. [Étape 2 : Configurer Sanity Studio](#heading-etape-2-configurer-sanity-studio)
4. [Étape 3 : Monter Sanity Studio dans Next.js](#heading-etape-3-monter-sanity-studio-dans-nextjs)
5. [Étape 4 : Créer des schémas de contenu](#heading-etape-4-creer-des-schemas-de-contenu)
6. [Étape 5 : Interroger les données en utilisant GROQ](#heading-etape-5-interroger-les-donnees-en-utilisant-groq)
7. [Étape 6 : Afficher le contenu dans votre application Next.js](#heading-etape-6-afficher-le-contenu-dans-votre-application-nextjs)
8. [Corriger la disposition du Studio](#heading-corriger-la-disposition-du-studio)
9. [Étape 7 : Déploiement](#heading-etape-7-deploiement)
10. [Configurer les Webhooks Sanity pour la mise à jour du Studio](#heading-configurer-les-webhooks-sanity-pour-la-mise-a-jour-du-studio)
11. [Et ensuite ?](#heading-et-ensuite)

## Qu'est-ce que Sanity ?

Sanity est un framework CMS headless pour gérer le contenu. Il fournit des outils pour exploiter les API afin de se connecter à votre application web, offrant une infrastructure instantanée, riche et automatisée pour gérer le contenu dans le cloud.

Avec Sanity, vous pouvez connecter des pages ou du contenu nécessitant des mises à jour régulières au studio et les gérer à partir du lac de contenu sans avoir à toucher fréquemment au code. Cela rend le processus de création et de gestion de contenu accessible à plus de personnes, indépendamment de leur background technique.

Dans cet article, vous apprendrez à utiliser Sanity comme source de données pour créer un site portfolio avec Next.js 13 et Tailwind CSS. Vous apprendrez également à l'héberger sur [Vercel](https://vercel.com) et à configurer des webhooks pour déclencher des déploiements.

Voici une capture d'écran de ce à quoi ressemblera le site portfolio. Certains des designs de ce site ont été inspirés par le [modèle de portfolio Spotlight de Tailwind](https://tailwindui.com/templates/spotlight).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/final-result-3.png)
_Projet personnel terminé_

Vous voulez l'essayer ? Consultez la [démo en direct](https://sanity-nextjs-site.vercel.app). Vous pouvez également trouver le code source du projet sur [GitHub](https://github.com/Evavic44/sanity-nextjs-site).

## Étape 1 : Installer Next.js

Ouvrez un terminal et exécutez cette commande pour installer la dernière version de Next.js :

```bash
npx create-next-app@latest
```

Sélectionnez toutes vos options d'installation préférées. À l'exception du nom du projet, je vais utiliser les options par défaut.

```bash
√ What is your project named? ... sanity-nextjs-site
√ Would you like to use TypeScript with this project? ... Yes
√ Would you like to use ESLint with this project? ... Yes
√ Would you like to use Tailwind CSS with this project? ... Yes
√ Would you like to use `src/` directory with this project? ... No
√ Would you like to use App Router? (recommended) ... Yes
√ Would you like to customize the default import alias? ... No
```

Cela devrait installer toutes les dépendances requises, y compris Tailwind CSS, dans le dossier du projet. Pour le voir en direct, exécutez la commande ci-dessous :

```bash
cd sanity-nextjs-site

npm run dev
```

Visitez [http://localhost:3000](https://localhost:3000) pour voir le site.

## Étape 2 : Configurer Sanity Studio

Sanity Studio est l'application monopage open source de Sanity pour gérer vos données et opérations. C'est l'interface à partir de laquelle vous pouvez créer, supprimer et mettre à jour vos données dans Sanity.

### Installer Sanity Studio

Ouvrez un nouveau terminal en dehors de votre application Next.js et tapez les commandes ci-dessous :

```bash
mkdir sanity-studio

cd sanity-studio

npm create sanity@latest
```

Une fois que vous avez exécuté la commande dans votre terminal, vous serez invité à sélectionner un fournisseur de connexion parmi la liste des options. Si vous avez déjà un compte, il authentifiera votre compte et vous connectera automatiquement, sinon vous pouvez créer un nouveau compte sur Sanity.

Une fois que votre compte a été authentifié avec succès, d'autres invites seront fournies dans le terminal pour configurer votre projet. Voici les options définies pour le studio :

```bash
$ Project name: Sanity Next.js Site
$ Use the default dataset configuration?: Yes
$ Project output path: C:\Users\USER\Desktop\sanity-studio
$ Select project template: Clean project with no predefined schemas
$ Do you want to use TypeScript? Yes
$ Package manager to use for installing dependencies?: npm
```

Une fois terminé, cela devrait installer Sanity Studio localement. Pour voir le studio, exécutez `npm run dev` et visitez [localhost:3333](http://localhost:3333), connectez-vous à votre compte en utilisant la même méthode utilisée pour créer votre compte, et vous devriez voir le studio fonctionner localement.

## Étape 3 : Monter Sanity Studio dans Next.js

Vous pouvez choisir d'héberger votre studio séparément, mais dans ce tutoriel, vous allez le monter avec votre application Next.js en utilisant l'outil [next-sanity](https://github.com/sanity-io/next-sanity). 

Arrêtez le serveur qui exécute votre application Next et exécutez cette commande :

```bash
npm install sanity next-sanity
```

Ensuite, dans le répertoire `sanity-studio` qui exécute le studio localement, copiez le dossier `schema` et le fichier `sanity.config.ts` et collez-les à la racine de votre application Next.js.

La structure des dossiers devrait ressembler à ceci :

```bash
├── .next
├── app/
├── node_modules/
├── public/
├── schemas/
│   └── index.ts
├── .eslintrc.json
├── .gitignore
├── next-env.d.ts
├── next.config.js
├── package-lock.json
├── package.json
├── postcss.config.js
├── README.md
├── sanity.config.ts
├── tailwind.config.js
└── tsconfig.json
```

Ensuite, à l'intérieur du fichier `sanity.config.ts`, ajoutez une clé `basePath` et donnez-lui une valeur de `/studio` ou tout autre chemin d'URL valide où vous souhaitez que votre studio soit accessible.

```js
// sanity.config.ts

import { defineConfig } from "sanity";
import { deskTool } from "sanity/desk";
import { schemaTypes } from "./schemas";

export default defineConfig({
  name: "sanity-nextjs-site",
  title: "Sanity Next.js Site",
  projectId: "ga8lllhf",
  dataset: "production",
  basePath: "/studio",
  plugins: [deskTool()],
  schema: { types: schemaTypes },
});

```

Voici une description de chaque propriété :

* `name` : Utilisé pour différencier les espaces de travail. Non obligatoire pour une configuration à espace de travail unique.
* `title` : Titre de votre projet. Cela s'affichera sur le Studio.
* `projectId` : Il s'agit d'un identifiant unique qui pointe vers le projet Sanity avec lequel vous travaillez.
* `dataset` : Le nom du jeu de données à utiliser pour votre studio. Les noms courants sont _production_ et _development_.
* `basePath` : Il s'agit du chemin URL où votre studio sera monté.
* `schema` : L'objet où vos fichiers de schéma seront définis.

### Créer le composant Studio

C'est ici que la page du studio sera montée dans votre application Next. Vous pouvez nommer ce fichier comme vous le souhaitez, mais il doit correspondre à la clé `basePath` spécifiée dans le fichier `sanity.config.ts`. Dans mon cas, le nom du fichier sera `studio`.

Pour créer la route du studio, nous allons utiliser les segments dynamiques de Next.js. À l'intérieur du répertoire app, créez un fichier `studio/[[...index]]/page.tsx`. 

```bash
app/
└── studio/
    └── [[...index]]/
         └── page.tsx
```

Avec cela, lorsque vous visitez une route qui correspond à `/studio`, le composant studio `page.tsx` sera rendu.

Pour compléter cette configuration, collez ce code à l'intérieur du composant :

```js
// app/studio/[[...index]]/page.tsx

"use client";

import { NextStudio } from "next-sanity/studio";
import config from "@/sanity.config";

export default function Studio() {
  return <NextStudio config={config} />;
}

```

Tout d'abord, `NextStudio` est importé de la bibliothèque `next-sanity` et le fichier de configuration est importé du fichier `sanity.config.ts` que vous avez créé précédemment.

Maintenant, exécutez `npm run dev` et visitez `localhost:3000/studio`. Vous obtiendrez une invite pour ajouter `localhost:3000` comme origine CORS à votre projet Sanity. Cliquez simplement sur continuer pour ajouter l'URL. 

Une fois ajouté, connectez-vous à votre compte Sanity en utilisant la même méthode que vous avez utilisée pour créer votre compte et vous devriez voir le Studio monté dans votre application Next.js comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sanity-studio-admin-page-3.png)

Avec le studio maintenant en cours d'exécution dans votre application Next.js, vous n'avez plus besoin du répertoire `sanity-studio` séparé. Vous pouvez le supprimer ou le fermer.

Par défaut, le studio sera vide car vous n'avez pas encore créé de fichiers de schémas. Faisons cela dans la section suivante.

## Étape 4 : Créer des schémas de contenu

Les schémas sont essentiellement un moyen d'organiser des ensembles de données dans une base de données en fonction du type de contenu dont vous avez besoin. 

Puisque nous construisons un site portfolio, nous allons créer des schémas pour gérer les projets, le profil, et ainsi de suite. Pour être plus précis, vous allez créer trois fichiers de schémas pour ce projet de portfolio :

* `profile` : Fichier de schéma pour définir vos informations personnelles comme le nom, à propos, compétences, et ainsi de suite.
* `project` : Fichier de schéma pour vos projets.
* `work` : Fichier de schéma pour définir votre expérience professionnelle.

Commençons par le schéma de profil.

### Schéma de profil

À l'intérieur du répertoire schemas, créez un fichier `profile.ts`. 

```bash
touch schemas/profile.ts
```

Commençons par définir les propriétés de base d'un fichier de schéma.

```js
// schemas/profile.ts

import { defineField } from "sanity";
import { BiUser } from "react-icons/bi";

const profile = {
  name: "profile",
  title: "Profile",
  type: "document",
  icon: BiUser,
  fields: [],
};

export default profile;

```

Chaque fichier de schéma doit contenir une propriété `name`, `title`, et `type`. Voici un bref aperçu de la fonction de chaque propriété :

* La clé `name` est la propriété utilisée pour référencer un schéma dans le langage de requête. La valeur doit être une [valeur unique](https://www.sanity.io/help/schema-object-fields-invalid) pour éviter de confondre les schémas.
* `title` définit ce que le type de schéma est appelé dans l'interface utilisateur du Studio.
* `type` définit le type de schéma avec lequel vous travaillez. La valeur `document` indiquera au studio qu'il doit permettre de créer de nouveaux documents.
* L'`icon` est une propriété optionnelle que vous pouvez ajouter avec le `title`. Pour utiliser l'icône, installez la bibliothèque [react-icons](https://react-icons.github.io/react-icons) avec la commande `npm install -D react-icons`
* Le tableau `fields` est l'endroit où les champs de saisie individuels seront définis. Voici les champs pour le schéma de profil :

```js
fields: [
    defineField({
      name: "fullName",
      title: "Full Name",
      type: "string",
      validation: (rule) => rule.required(),
    }),
    defineField({
      name: "headline",
      title: "Headline",
      type: "string",
      description: "In one short sentence, what do you do?",
      validation: (Rule) => Rule.required().min(40).max(50),
    }),
    {
      name: "profileImage",
      title: "Profile Image",
      type: "image",
      description: "Upload a profile picture",
      options: { hotspot: true },
      fields: [
        {
          name: "alt",
          title: "Alt",
          type: "string",
        },
      ],
    },
    {
      name: "shortBio",
      title: "Short Bio",
      type: "text",
      rows: 4,
    },
    {
      name: "email",
      title: "Email Address",
      type: "string",
    },
    {
      name: "location",
      title: "Location",
      type: "string",
    },
    {
      name: "fullBio",
      title: "Full Bio",
      type: "array",
      of: [{ type: "block" }],
    },
    {
      name: "resumeURL",
      title: "Upload Resume",
      type: "file",
    },
    {
      name: "socialLinks",
      title: "Social Links",
      type: "object",
      description: "Add your social media links:",
      fields: [
        {
          name: "github",
          title: "Github URL",
          type: "url",
          initialValue: "https://github.com/",
        },
        {
          name: "linkedin",
          title: "Linkedin URL",
          type: "url",
          initialValue: "https://linkedin.com/in/",
        },
        {
          name: "twitter",
          title: "Twitter URL",
          type: "url",
          initialValue: "https://twitter.com/",
        },
        {
          name: "twitch",
          title: "Twitch URL",
          type: "url",
          initialValue: "https://twitch.com/",
        },
      ],
      options: {
        collapsed: false,
        collapsible: true,
        columns: 2,
      },
    },
    {
      name: "skills",
      title: "Skills",
      type: "array",
      description: "Add a list of skills",
      of: [{ type: "string" }],
    },
 ],
```

Pour comprendre comment fonctionnent les champs, visualisez chaque objet de champ comme un `<input>` HTML qui sera disponible dans le studio. La valeur de chaque entrée sera exportée vers un objet JSON que vous pouvez utiliser pour injecter vos données. Vous pouvez ajouter autant de champs que vous le souhaitez, mais chacun doit contenir une propriété `name`, `title`, et `type`.

La fonction d'assistance `defineField()` permet l'auto-complétion des types de champs dans votre fichier de schéma.

Sanity dispose de ses propres types de schémas intégrés : `number`, `datetime`, `image`, `array`, `object`, `string`, `url`, et bien d'autres. Vous pouvez consulter la liste complète des [types de schémas ici](https://www.sanity.io/docs/schema-types).

Pour exposer ce fichier de schéma nouvellement créé au Studio, vous devez l'importer dans le tableau des schémas à l'intérieur du fichier `schemas/index.ts` :

```js
// schemas/index.ts

import profile from "./profile";

export const schemaTypes = [profile];

```

Maintenant, vous pouvez commencer à travailler avec lui depuis le studio. Visitez votre studio à l'adresse `localhost:3000/studio` ou tout autre chemin que vous avez utilisé pour le monter. Ensuite, cliquez sur l'onglet Profile et sélectionnez le bouton d'édition dans le coin supérieur pour commencer à modifier les champs.

Voici à quoi cela ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/profile-schema-filled.png)

Remplissez tous les champs et cliquez sur publier une fois terminé. Cela ajoutera les données dans un document JSON analysé. Pour voir cette sortie JSON, cliquez sur le bouton de menu dans le coin supérieur droit et appuyez sur "Inspect" ou maintenez simplement `Ctrl Alt I` sur votre clavier.

Voici à quoi ressemble la structure du schéma de profil :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/inspect-schema-types-3.png)
_Inspecter le document de schéma_

Avec cela, vous pouvez facilement interroger les données pour récupérer le contenu exact dont vous avez besoin dans votre front-end. Faisons cela dans la section suivante.

## Étape 5 : Interroger les données en utilisant GROQ

[GROQ (Graph-Relational Object Queries)](https://www.sanity.io/docs/groq) est le langage de requête de Sanity conçu pour interroger des collections de documents JSON largement sans schéma. L'idée derrière le langage de requête est de pouvoir décrire exactement quelles informations vous avez besoin de votre schéma, ou filtrer certaines données, et retourner uniquement des éléments spécifiques de vos données.

Pour commencer à utiliser GROQ, créez d'abord un fichier `sanity/sanity.client.ts` dans le répertoire racine de votre projet.

```bash
mkdir sanity && touch sanity/sanity.client.ts
```

Collez le code dans ce fichier :

```js
// sanity/sanity.client.ts

import { createClient, type ClientConfig } from "@sanity/client";

const config: ClientConfig = {
  projectId: "ga8lllhf",
  dataset: "production",
  apiVersion: "2023-07-16",
  useCdn: false,
};

const client = createClient(config);

export default client;
```

* `apiVersion` : La version de l'API Sanity que vous utilisez. Pour la dernière version de l'API, utilisez votre date actuelle dans ce format `YYYY-MM-DD`.
* `useCdn` est utilisé pour désactiver les cas limites

Ce que fait ce fichier, c'est fournir quelques configurations qui seront définies dans chaque requête afin d'éviter de les répéter à chaque fois. Maintenant, pour la requête principale, créez un fichier `sanity/sanity.query.ts`.

```bash
touch sanity/sanity.query.ts
```

Remarque : Il n'y a pas de manière claire de disposer ou de nommer ces fichiers, alors n'hésitez pas à les modifier selon vos besoins.

Voici la requête de base pour le schéma de profil :

```js
// sanity/sanity.query.ts

import { groq } from "next-sanity";
import client from "./sanity.client";

export async function getProfile() {
  return client.fetch(
    groq`*[_type == "profile"]{
      _id,
      fullName,
      headline,
      profileImage {alt, "image": asset->url},
      shortBio,
      location,
      fullBio,
      email,
      "resumeURL": resumeURL.asset->url,
      socialLinks,
      skills
    }`
  );
}

```

Ici, nous avons créé une fonction asynchrone exportée appelée `getProfile()` qui retourne une requête de récupération groq enveloppée avec la configuration du client créée dans la première étape.

La requête groq commence par un astérisque (`*`) qui représente chaque document dans votre jeu de données suivi d'un filtre entre crochets. Le filtre ci-dessus retourne le schéma qui a un `_type` de "profile".

![Image](https://www.freecodecamp.org/news/content/images/2023/07/profile-type-1.png)
_Schéma JSON montrant le type de schéma de profil_

Le filtre est suivi d'accolades qui contiennent un contenu spécifique du jeu de données nécessaire comme : `fullName`, `headline`, `profileImage` et ainsi de suite. Cela s'appelle [projections](https://www.sanity.io/docs/how-queries-work#727ecb6f5e15) dans la documentation de Sanity et cela retourne toutes les données sous forme de tableau.

Si vous souhaitez en savoir plus sur les requêtes utilisant GROQ, je vous suggère de consulter la section [comment fonctionnent les requêtes](https://www.sanity.io/docs/how-queries-work) dans la documentation. Pour la coloration syntaxique de votre requête GROQ, installez l'[extension sanity.io](https://marketplace.visualstudio.com/items?itemName=sanity-io.vscode-sanity) disponible sur le marché Visual Studio Code.

Nous avons terminé la configuration dont vous avez besoin pour commencer à utiliser votre contenu. Voyons comment afficher ce contenu dans votre application Next.

## Étape 6 : Afficher le contenu dans votre application Next.js

Cette section est divisée en deux parties distinctes : Afficher la section héroïque et le contenu de la page à propos.

### Ajouter des types au contenu des données

Puisque vous utilisez TypeScript pour ce projet, il est important de fournir d'abord les types pour les données provenant du studio.

Créez un fichier `types/index.ts` dans le répertoire racine et ajoutez le type de profil ci-dessous :

```js
// types/index.ts

import { PortableTextBlock } from "sanity";

export type ProfileType = {
  _id: string,
  fullName: string,
  headline: string,
  profileImage: {
    alt: string,
    image: string
  },
  shortBio: string,
  email: string,
  fullBio: PortableTextBlock[],
  location: string,
  resumeURL: string,
  socialLinks: string[],
  skills: string[],
};
```

`PortableTextBlock` est un type unique provenant de Sanity qui définit correctement le type de données pour l'éditeur de texte riche.

Maintenant que vous avez défini les types pour votre contenu, il est plus facile de visualiser les données que vous attendez dans votre studio.

### Afficher la section héroïque

Tout d'abord, supprimez tous les styles à l'intérieur du fichier `global.css`, à l'exception des importations Tailwind nécessaires en haut. Ensuite, effacez tout ce qui se trouve à l'intérieur du fichier `page.tsx` racine de votre application Next.js et collez le code suivant à l'intérieur :

```js
// app/page.tsx

import { getProfile } from "@/sanity/sanity.query";
import type { ProfileType } from "@/types";
import HeroSvg from "./icons/HeroSvg";;

export default async function Home() {
  const profile: ProfileType[] = await getProfile();

  return (
    <main className="max-w-7xl mx-auto lg:px-16 px-6">
      <section className="flex xl:flex-row flex-col xl:items-center items-start xl:justify-center justify-between gap-x-12 lg:mt-32 mt-20 mb-16">
        {profile &&
          profile.map((data) => (
            <div key={data._id} className="lg:max-w-2xl max-w-2xl">
              <h1 className="text-3xl font-bold tracking-tight sm:text-5xl mb-6 lg:leading-[3.7rem] leading-tight lg:min-w-[700px] min-w-full">
                {data.headline}
              </h1>
              <p className="text-base text-zinc-400 leading-relaxed">
                {data.shortBio}
              </p>
              <ul className="flex items-center gap-x-6 my-10">
                {Object.entries(data.socialLinks)
                  .sort()
                  .map(([key, value], id) => (
                    <li key={id}>
                      <a
                        href={value}
                        rel="noreferer noopener"
                        className="flex items-center gap-x-3 mb-5 hover:text-purple-400 duration-300"
                      >
                        {key[0].toUpperCase() + key.toLowerCase().slice(1)}
                      </a>
                    </li>
                  ))}
              </ul>
            </div>
          ))}
        <HeroSvg />
      </section>
    </main>
  );
}
```

* Tout d'abord, la requête `getProfile` est importée du fichier `sanity.query.ts`, qui est une version filtrée de nos données provenant du schéma.
* `ProfileType` est importé pour ajouter des types aux données.
* Le tableau `profile` est mappé à l'intérieur du composant pour retourner le `headline`, `shortBio`, et `socialLinks`.
* `<HeroSvg />` est essentiellement un élément `svg` importé en tant que composant React ajouté uniquement pour l'esthétique de l'interface utilisateur. Vous pouvez télécharger le [composant d'icône HeroSVG](https://github.com/Evavic44/sanity-nextjs-site/blob/main/app/(site)/icons/HeroSvg.tsx).

Voici le résultat obtenu :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/hero-section-content-result-2.png)
_section héroïque de sortie_

Pour accélérer les choses, j'ai créé les composants de navigation de la barre de navigation et du pied de page. Téléchargez simplement [le répertoire](https://github.com/Evavic44/sanity-nextjs-site/tree/main/app/(site)/components/global) et importez-les dans le fichier `layout.tsx` comme suit :

```js
// app/layout.tsx

import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Navbar from "./components/global/Navbar";
import Footer from "./components/global/Footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Sanity Next.js Portfolio Site",
  description: "A personal portfolio site built with Sanity and Next.js",
  openGraph: {
    images: "add-your-open-graph-image-url-here",
  },
};

export default function RootLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="en">
      <body className={`${inter.className} bg-zinc-900 text-white`}>
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  );
}
```

Avec ces composants, la page d'accueil devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/hero-section-with-component-2.png)
_page d'accueil avec les composants de barre de navigation et de pied de page_

### Afficher la page À propos

Construisons la page À propos en utilisant le contenu de la requête `getProfile` également. Dans cette section, vous devrez installer une bibliothèque React appelée `PortableTextBlock` par Sanity. Cette bibliothèque vous permettra de déstructurer facilement le contenu de bloc de l'éditeur de texte riche.

Pour installer ce package, exécutez `npm install -D @portabletext/react` et je vais expliquer comment l'utiliser plus tard. 

Créez un dossier `about` à l'intérieur du répertoire `app` et ajoutez un fichier `page.tsx` à l'intérieur de ce nouveau dossier. Vous pouvez également faire cela rapidement en utilisant la commande suivante :

```js
mkdir app/about && touch app/about/page.tsx
```

Voici le code pour la page À propos :

```js
// app/about/page.tsx

import Image from "next/image";
import { getProfile } from "@/sanity/sanity.query";
import type { ProfileType } from "@/types";
import { PortableText } from "@portabletext/react";
import { BiEnvelope, BiFile } from "react-icons/bi";

export default async function About() {
  const profile: ProfileType[] = await getProfile();

  return (
    <main className="lg:max-w-7xl mx-auto max-w-3xl md:px-16 px-6">
      {profile &&
        profile.map((data) => (
          <div key={data._id}>
            <section className="grid lg:grid-cols-2 grid-cols-1 gap-x-6 justify-items-center">
              <div className="order-2 lg:order-none">
                <h1 className="lg:text-5xl text-4xl lg:leading-tight basis-1/2 font-bold mb-8">
                  I&apos;m {data.fullName}. I live in {data.location}, where I
                  design the future.
                </h1>

                <div className="flex flex-col gap-y-3 text-zinc-400 leading-relaxed">
                  <PortableText value={data.fullBio} />
                </div>
              </div>

              <div className="flex flex-col lg:justify-self-center justify-self-start gap-y-8 lg:order-1 order-none mb-12">
                <div>
                  <Image
                    className="rounded-2xl mb-4 object-cover max-h-96 min-h-96 bg-top bg-[#1d1d20]"
                    src={data.profileImage.image}
                    width={400}
                    height={400}
                    quality={100}
                    alt={data.profileImage.alt}
                  />

                  <a
                    href={`${data.resumeURL}?dl=${data.fullName}_resume`}
                    className="flex items-center justify-center gap-x-2 bg-[#1d1d20] border border-transparent hover:border-zinc-700 rounded-md duration-200 py-2 text-center cursor-cell font-medium"
                  >
                    <BiFile className="text-base" /> Download Resumé
                  </a>
                </div>

                <ul>
                  <li>
                    <a
                      href={`mailto:${data.email}`}
                      className="flex items-center gap-x-2 hover:text-purple-400 duration-300"
                    >
                      <BiEnvelope className="text-lg" />
                      {data.email}
                    </a>
                  </li>
                </ul>
              </div>
            </section>

            <section className="mt-24 max-w-2xl">
              <h2 className="font-semibold text-4xl mb-4">Expertise</h2>
              <p className="text-zinc-400 max-w-lg">
                I&apos;ve spent few years working on my skills. In no particular
                order, here are a few of them.
              </p>

              <ul className="flex flex-wrap items-center gap-3 mt-8">
                {data.skills.map((skill, id) => (
                  <li
                    key={id}
                    className="bg-[#1d1d20] border border-transparent hover:border-zinc-700 rounded-md px-2 py-1"
                  >
                    {skill}
                  </li>
                ))}
              </ul>
            </section>
          </div>
        ))}
    </main>
  );
}

```

* Similaire à la page d'accueil, nous récupérons également les données de la requête `getProfile` et attribuons le `ProfileType` pour la sécurité des types.
* Les données de profil sont également mappées pour obtenir les propriétés individuelles : `fullName`, `location`, `fullBio`, `profileImage`, `resumeURL`, `email`, et le tableau `skills`.
* L'éditeur de texte portable a été déstructuré en utilisant le composant `<PortableText />` qui prend une valeur prop qui reçoit le contenu de l'éditeur de texte riche.

L'ajout de l'image depuis le CDN de Sanity devrait générer une erreur dans Next.js puisque vous n'avez pas ajouté le nom d'hôte de la source d'image de Sanity dans votre fichier `next.config.ts`. Voici comment faire dans Next.js 13 :

```js
// next.config.ts

/** @type {import('next').NextConfig} */
const nextConfig = {};

module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "cdn.sanity.io",
        port: "",
      },
    ],
  },
};

```

Voici le résultat obtenu :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/about-3.png)
_Page À propos_

### Expérience professionnelle

Dans un site portfolio typique, vous devrez peut-être créer une liste d'expériences professionnelles passées. Voici à quoi ressemblerait le schéma :

Créez un fichier `schemas/job.ts` et collez le code suivant :

```js
// schemas/job.ts

import { BiBriefcase } from "react-icons/bi";

const job = {
  name: "job",
  title: "Job",
  type: "document",
  icon: BiBriefcase,
  fields: [
    {
      name: "name",
      title: "Company Name",
      type: "string",
      description: "What is the name of the company?",
    },
    {
      name: "jobTitle",
      title: "Job Title",
      type: "string",
      description: "Enter the job title. E.g: Software Developer",
    },
    {
      name: "logo",
      title: "Company Logo",
      type: "image",
    },
    {
      name: "url",
      title: "Company Website",
      type: "url",
    },
    {
      name: "description",
      title: "Job Description",
      type: "text",
      rows: 3,
      description: "Write a brief description about this role",
    },
    {
      name: "startDate",
      title: "Start Date",
      type: "date",
    },
    {
      name: "endDate",
      title: "End Date",
      type: "date",
    },
  ],
};

export default job;

```

Pour exposer ce nouveau fichier de schéma au studio, ajoutez-le au tableau `schemaTypes` à l'intérieur du fichier `schemas/index.ts` et vous devriez le voir dans votre studio. 

Voici le résultat obtenu :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/job-schema-7.png)
_champs de schéma de travail dans le studio sanity_

Cliquez sur le bouton de création et ajoutez autant d'enregistrements que vous le souhaitez. Vous pouvez maintenant passer à l'interrogation des données. 

De la même manière que le schéma `profile` a été interrogé dans le fichier `sanity.query.ts`, vous ferez de même pour le schéma de travail : 

```js
// sanity/sanity.query.ts

export async function getJob() {
  return client.fetch(
    groq`*[_type == "job"]{
      _id,
      name,
      jobTitle,
      "logo": logo.asset->url,
      url,
      description,
      startDate,
      endDate,
    }`
  );
}
```

Ensuite, ajoutez les types pour le jeu de données retourné :

```js
// types/index.ts

export type JobType = {
  _id: string;
  name: string;
  jobTitle: string;
  logo: string;
  url: string;
  description: string;
  startDate: Date;
  endDate: Date;
};
```

Et ensuite, pour l'afficher dans votre front-end, créez un fichier `Job.tsx` à l'intérieur du répertoire `components` et ajoutez le code suivant :

```js
// app/components/Job.tsx

import Image from "next/image";
import { getJob } from "@/sanity/sanity.query";
import type { JobType } from "@/types";

export default async function Job() {
  const job: JobType[] = await getJob();

  return (
    <section className="mt-32">
      <div className="mb-16">
        <h2 className="font-semibold text-4xl mb-4">Work Experience</h2>
      </div>

      <div className="flex flex-col gap-y-12">
        {job.map((data) => (
          <div
            key={data._id}
            className="flex items-start lg:gap-x-6 gap-x-4 max-w-2xl relative before:absolute before:bottom-0 before:top-[4.5rem] before:left-7 before:w-[1px] before:h-[calc(100%-50px)] before:bg-zinc-800"
          >
            <a
              href={data.url}
              rel="noreferrer noopener"
              className="min-h-[60px] min-w-[60px] rounded-md overflow-clip relative"
            >
              <Image
                src={data.logo}
                className="object-cover"
                alt={`${data.name} logo`}
                fill
              />
            </a>
            <div className="flex flex-col items-start">
              <h3 className="text-xl font-bold">{data.name}</h3>
              <p>{data.jobTitle}</p>
              <small className="text-sm text-zinc-500 mt-2 tracking-widest uppercase">
                {data.startDate.toString()} - {data.endDate.toString()}
              </small>
              <p className="text-base text-zinc-400 my-4">{data.description}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
```

Pour voir le composant, vous pouvez l'importer dans la page d'accueil :

```js
// Note : Il s'agit d'une version tronquée de la page d'accueil (app/page.tsx) pour illustrer comment le composant Job est déclaré.

import { getProfile } from "@/sanity/sanity.query";
import type { ProfileType } from "@/types";
import HeroSvg from "./icons/HeroSvg";
import Job from "./components/Job"; // import job component

export default async function Home() {
  const profile: ProfileType[] = await getProfile();

  return (
    <main className="max-w-7xl mx-auto lg:px-16 px-6">
      <section> // code tronqué pour plus de concision
        <HeroSvg />
      </section>
      <Job /> // déclare le composant job
    </main>
  );
}
```

Voici le résultat obtenu :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/job-description-result-output-3.png)
_section expérience professionnelle_

À ce stade, vous devriez avoir une compréhension claire des étapes nécessaires pour présenter du contenu avec Sanity : **Créer un fichier de schéma, > Interroger le jeu de données > Afficher le contenu dans votre application**. 

Concentrons-nous maintenant sur la configuration des données pour les routes dynamiques dans votre application et exploitons-les pour construire la page des projets.

### Schéma de projet

Comme toujours, vous allez commencer par créer le fichier de schéma :

```bash
touch schemas/project.ts
```

Voici le code pour les champs du schéma :

```js
import { BiPackage } from "react-icons/bi";
import { defineField } from "sanity";

const project = {
  name: "project",
  title: "Project",
  description: "Project Schema",
  type: "document",
  icon: BiPackage,
  fields: [
    {
      name: "name",
      title: "Name",
      type: "string",
      description: "Enter the name of the project",
    },
    defineField({
      name: "tagline",
      title: "Tagline",
      type: "string",
      validation: (rule) => rule.max(60).required(),
    }),
    defineField({
      name: "slug",
      title: "Slug",
      type: "slug",
      description:
        "Add a custom slug for the URL or generate one from the name",
      options: { source: "name" },
      validation: (rule) => rule.required(),
    }),
    {
      name: "logo",
      title: "Project Logo",
      type: "image",
    },
    {
      name: "projectUrl",
      title: "Project URL",
      type: "url",
    },
    {
      name: "coverImage",
      title: "Cover Image",
      type: "image",
      description: "Upload a cover image for this project",
      options: { hotspot: true },
      fields: [
        {
          name: "alt",
          title: "Alt",
          type: "string",
        },
      ],
    },
    {
      name: "description",
      title: "Description",
      type: "array",
      description: "Write a full description about this project",
      of: [{ type: "block" }],
    },
  ],
};

export default project;

```

Ensuite, exposez le schéma au tableau `schemaTypes` :

```js
import job from "./job";
import profile from "./profile";
import project from "./project";

export const schemaTypes = [profile, job, project];
```

Visitez votre studio, cliquez sur le schéma de projet et ajoutez autant de projets que vous le souhaitez. Vous pouvez télécharger les [fichiers d'actifs](https://github.com/Evavic44/sanity-nextjs-site/tree/main/public) utilisés pour chaque projet depuis le dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/project-schema-3.png)
_Studio Sanity montrant les champs de schéma de projet_

Voici la requête pour obtenir tous les projets :

```js
// sanity/sanity.query.ts

export async function getProjects() {
  return client.fetch(
    groq`*[_type == "project"]{
      _id, 
      name,
      "slug": slug.current,
      tagline,
      "logo": logo.asset->url,
    }`
  );
}
```

Ensuite, ajoutez les types.

```js
// types/index.ts

export type ProjectType = {
  _id: string;
  name: string;
  slug: string;
  tagline: string;
  projectUrl: string;
  logo: string;
  coverImage: {
    alt: string | null;
    image: string;
  };
  description: PortableTextBlock[];
};
```

Et ensuite, affichez le contenu dans votre front-end.

```bash
mkdir app/projects && touch app/projects/page.tsx
```

Cela créera un fichier `page.tsx` à l'intérieur d'un répertoire appelé projet. Voici le code pour les projets :

```js
// app/projects/page.tsx

import Image from "next/image";
import Link from "next/link";
import { getProjects } from "@/sanity/sanity.query";
import type { ProjectType } from "@/types";

export default async function Project() {
  const projects: ProjectType[] = await getProjects();

  return (
    <main className="max-w-7xl mx-auto md:px-16 px-6">
      <section className="max-w-2xl mb-16">
        <h1 className="text-3xl font-bold tracking-tight sm:text-5xl mb-6 lg:leading-[3.7rem] leading-tight">
          Featured projects I&apos;ve built over the years
        </h1>
        <p className="text-base text-zinc-400 leading-relaxed">
          I&apos;ve worked on tons of little projects over the years but these
          are the ones that I&apos;m most proud of. Many of them are
          open-source, so if you see something that piques your interest, check
          out the code and contribute if you have ideas for how it can be
          improved.
        </p>
      </section>

      <section className="grid xl:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-5 mb-12">
        {projects.map((project) => (
          <Link
            href={`/projects/${project.slug}`}
            key={project._id}
            className="flex items-center gap-x-4 bg-[#1d1d20] border border-transparent hover:border-zinc-700 p-4 rounded-lg ease-in-out"
          >
            <Image
              src={project.logo}
              width={60}
              height={60}
              alt={project.name}
              className="bg-zinc-800 rounded-md p-2"
            />
            <div>
              <h2 className="font-semibold mb-1">{project.name}</h2>
              <div className="text-sm text-zinc-400">{project.tagline}</div>
            </div>
          </Link>
        ))}
      </section>
    </main>
  );
}
```

Voici le résultat obtenu :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/project-page-4.png)
_page de projet_

### Afficher les routes dynamiques

Chaque carte de projet est enveloppée dans un lien qui pointe vers leur page respective en fonction du slug : `/projects/${project.slug}`. Avec cela, le composant dynamique peut être facilement créé dans next.js

Créez un dossier appelé `[project]` (entouré de crochets) à l'intérieur du répertoire projects, et ajoutez un fichier `page.tsx`.

Vous pouvez également faire cela via le terminal :

```bash
mkdir app/projects/[project] && touch app/projects/[project]/page.tsx
```

Ce dossier entouré de crochets est connu sous le nom de [segment dynamique](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#convention) dans Next.js, et il permet au composant d'être monté en fonction de la propriété params. 

Puisque vous avez déjà créé le type de schéma de projet, il ne reste plus qu'à interroger le jeu de données pour récupérer les projets individuels.

Voici la requête pour obtenir des projets individuels :

```js
// sanity/sanity.query.ts

export async function getSingleProject(slug: string) {
  return client.fetch(
    groq`*[_type == "project" && slug.current == $slug][0]{
      _id,
      name,
      projectUrl,
      coverImage { alt, "image": asset->url },
      tagline,
      description
    }`,
    { slug }
  );
}
```

Pour récupérer le slug de la route, nous avons ajouté un paramètre appelé `slug` dans la fonction, ce qui permettra à la fonction `getSingleProject` d'être appelée avec le slug respectif en utilisant la propriété [params](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#context-parameter) de Next.js.

```js
// app/projects/[project]/page.tsx

import Image from "next/image";
import { Metadata } from "next";
import { getSingleProject } from "@/sanity/sanity.query";
import type { ProjectType } from "@/types";
import { PortableText } from "@portabletext/react";
import fallBackImage from "@/public/project.png";

type Props = {
  params: {
    project: string;
  };
};

// Dynamic metadata for SEO
export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const slug = params.project;
  const project: ProjectType = await getSingleProject(slug);

  return {
    title: `${project.name} | Project`,
    description: project.tagline,
    openGraph: {
      images: project.coverImage?.image || "add-a-fallback-project-image-here",
      title: project.name,
      description: project.tagline,
    },
  };
}

export default async function Project({ params }: Props) {
  const slug = params.project;
  const project: ProjectType = await getSingleProject(slug);

  return (
    <main className="max-w-6xl mx-auto lg:px-16 px-8">
      <div className="max-w-3xl mx-auto">
        <div className="flex items-start justify-between mb-4">
          <h1 className="font-bold lg:text-5xl text-3xl lg:leading-tight mb-4">
            {project.name}
          </h1>

          <a
            href={project.projectUrl}
            rel="noreferrer noopener"
            className="bg-[#1d1d20] text-white hover:border-zinc-700 border border-transparent rounded-md px-4 py-2"
          >
            Explore
          </a>
        </div>

        <Image
          className="rounded-xl border border-zinc-800"
          width={900}
          height={460}
          src={project.coverImage?.image || fallBackImage}
          alt={project.coverImage?.alt || project.name}
        />

        <div className="flex flex-col gap-y-6 mt-8 leading-7 text-zinc-400">
          <PortableText value={project.description} />
        </div>
      </div>
    </main>
  );
}
```

Puisque les données provenant du jeu de données sont un projet unique et non un tableau, aucune déstructuration n'est requise.

Voici le résultat obtenu :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/dynamic-project-page-2.gif)
_page de projet dynamique_

### Ajouter des états de chargement

Next.js 13 a introduit un fichier spécial `loading.js` qui vous aide à créer un état de chargement instantané à partir du serveur pendant que le contenu d'un segment de route se charge. Cela aide les utilisateurs à comprendre que l'application répond et offre une meilleure expérience utilisateur.

Avec ce fichier spécial, vous pouvez créer un état de chargement qui imite l'interface utilisateur de la page de projet unique facilement.

Créez un fichier `loading.tsx` à l'intérieur du répertoire `[project]` et ajoutez le code suivant :

```js
// projects/[project]/loading.tsx

export default function Loading() {
  return (
    <div className="max-w-3xl mx-auto lg:px-0 px-8">
      <div className="flex items-center justify-between mb-6">
        <span className="w-52 h-11 bg-[#1d1d20] rounded-sm animate-pulse"></span>
        <span className="w-20 h-11 bg-[#1d1d20] rounded-sm animate-pulse"></span>
      </div>
      <div className="w-full h-96 mb-8 bg-[#1d1d20] rounded-sm animate-pulse"></div>
      <div className="flex flex-col gap-y-2">
        <span className="w-full h-5 bg-[#1d1d20] rounded-sm animate-pulse"></span>
        <span className="w-full h-5 bg-[#1d1d20] rounded-sm animate-pulse"></span>
      </div>
    </div>
  );
}
```

Voici le résultat obtenu :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/loading-state-2.gif)
_page de projet dynamique montrant l'état de chargement instantané de next.js_

## Corriger la disposition du Studio

Vous avez peut-être remarqué que les composants `navbar` et `footer` s'affichent dans la route du studio. Cela est dû au fait que ces composants ont été définis dans la disposition racine, qui s'applique à toutes les routes de l'application.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/studio-component-ui-error-2.png)
_composants de la barre de navigation et du pied de page dans la page du studio_

Pour corriger cela, vous devrez créer un fichier `layout.tsx` séparé pour le composant studio :

Créez deux dossiers entourés de parenthèses à l'intérieur du répertoire `app`. Nommez un dossier `(site)`, et l'autre `(studio)`. Ces dossiers sont entourés de parenthèses pour empêcher Next.js de les monter en tant que routes.

Déplacez tous les fichiers dans le répertoire app qui concernent l'application next à l'exception du dossier `studio`, `global.css` et `favicon.ico` dans le dossier `(site)`, puis déplacez le dossier studio dans le dossier `(studio)`.

Les seuls fichiers qui vivront dans la racine de l'application sont `global.css` et `favicon.ico`.

Voici à quoi devrait ressembler votre nouvelle structure de dossiers :

```bash
app/
├── (site)/
│   ├── about/
│   ├── components/
│   ├── icons/
│   ├── projects/
│   ├── layout.tsx
│   └── page.tsx
├── (studio)/
│   └── studio/
├── favicon.ico
└── global.css
```

Une fois terminé, créez un fichier `layout.tsx` à l'intérieur du répertoire `(studio)` et collez le code suivant à l'intérieur :

```js
import "../globals.css";

export default function StudioLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

```

Mettez à jour toutes les importations qui ont pu changer, relancez votre serveur et vous devriez voir votre studio en cours d'exécution, sans les composants.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sanity-studio-without-navbar-components-1.png)
_Page Studio sans les composants de barre de navigation et de pied de page_

## Étape 7 : Déploiement

Déployer une application Next.js alimentée par Sanity est un processus assez simple. Suivez ce guide pour [configurer votre compte et déployer avec Vercel](https://vercel.com/docs/getting-started-with-vercel/import).

Après avoir déployé votre site avec succès, visitez la route du studio ; `your-site-name/studio`, et vous devriez obtenir une invite pour ajouter l'URL au paramètre CORS dans Sanity :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/add-hosted-site-URL-to-sanity-cors-settings.png)
_Invite des paramètres CORS de Sanity_

Cliquez simplement sur "continuer" et suivez les instructions à l'écran pour le faire. Si tout se passe bien, vous devriez pouvoir voir votre studio.

## Configurer les Webhooks Sanity pour la mise à jour du Studio

Les mises à jour apportées à votre site ne seraient déclenchées qu'au moment de la construction. Cela signifie que si vous mettez à jour un champ dans votre studio en utilisant le lien hébergé, vous devrez déclencher manuellement un déploiement sur Vercel pour voir les changements.

Devoir déclencher le serveur de déploiement à chaque fois peut être une tâche fastidieuse, surtout lorsque vous construisez pour un client. 

Dans cette section, je vais vous guider à travers les étapes pour déployer manuellement votre site chaque fois qu'un changement est apporté à votre studio en utilisant les [Web Hooks alimentés par GROQ de Sanity](https://www.sanity.io/docs/webhooks).

### Créer un Hook de Déploiement sur Vercel

Tout d'abord, vous aurez besoin de l'URL de l'endpoint de votre service d'hébergement pour déclencher le déploiement.

Naviguez vers les paramètres de votre projet sur Vercel et cliquez sur l'onglet **Git**. Dans la section **Deploy Hooks**, choisissez un nom pour votre hook et sélectionnez la branche qui sera déployée lorsque l'URL générée sera demandée.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/create-hook-endpoint-on-vercel-1.png)
_création du hook_

Soumettez le formulaire et copiez l'URL de l'endpoint générée par Vercel.

### Déclencher le Hook en utilisant les Webhooks alimentés par GROQ de Sanity

Visitez [sanity.io/manage](https://www.sanity.io/manage), choisissez votre projet, naviguez vers la section **API** et cliquez sur le bouton "Create webhook".

![Image](https://www.sanity.io/manage)
_Webhooks alimentés par GROQ de Sanity_

Remplissez le formulaire avec les informations concernant le hook que vous souhaitez créer. 

* `Name` : Déploiement du Portfolio.
* `Description` : Déclencher une reconstruction lorsque le contenu du portfolio est créé, mis à jour et supprimé.
* `URL` : [Collez ici l'URL de l'endpoint générée par Vercel].
* `Dataset` : Le jeu de données auquel appliquer le hook.
* `Trigger on` : Cochez les cases **"create"**, **"update"**, et **"delete"**.

Laissez les champs `filter` et `projection` vides afin que le hook soit appliqué à tous les documents, et pour le reste des champs, laissez-les tels quels et cliquez sur enregistrer.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sanity-groq-powered-hook-created-2.png)
_hook alimenté par groq de sanity créé_

Maintenant, visitez votre studio hébergé et mettez à jour n'importe quel document. Une fois que vous cliquez sur publier, cela devrait déclencher le hook de déploiement et mettre à jour votre site une fois terminé.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sanity-hook-trigger-build-on-vercel-2.png)
_hook de déploiement déclenchant le déploiement sur Vercel_

Une autre bonne alternative pour configurer les mises à jour en direct dans votre application Sanity/Next.js est d'utiliser [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/pages/building-your-application/data-fetching/incremental-static-regeneration), qui est une meilleure option si vous construisez une application à grande échelle.

Et c'est tout ! Vous pouvez voir l'[Aperçu en direct ici](https://sanity-nextjs-site.vercel.app) et trouver l'[URL GitHub ici](https://github.com/Evavic44/sanity-nextjs-site).

## Et ensuite ?

Bien que ce tutoriel ait couvert beaucoup d'informations utiles, il existe encore de nombreuses autres possibilités avec Sanity que vous pouvez explorer. 

Vous pouvez personnaliser votre studio, intégrer des API tierces, construire une vitrine avec Shopify, et bien plus encore.

Si vous avez trouvé cet article agréable et souhaitez approfondir le monde de Sanity, je vous recommande de consulter les ressources suivantes :

* [Personnalisation de l'éditeur de texte portable](https://www.sanity.io/docs/customizing-the-portable-text-editor)
* [Comment créer un document singleton](https://www.sanity.io/guides/singleton-document)
* [Surligner la syntaxe du bloc de code](https://www.sanity.io/plugins/code-input)

Merci d'avoir lu. Partagez et abonnez-vous à mon blog pour les mises à jour futures.

[GitHub](https://github.com/Evavic44) | [Twitter](https://twitter.com/victorekea) | [Blog](https://eke.hashnode.dev) | [LinkedIn](https://www.linkedin.com/in/victorekeawa/)