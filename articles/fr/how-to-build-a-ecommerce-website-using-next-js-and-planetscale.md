---
title: Comment créer un site eCommerce prêt pour la production avec ReactJS, TailwindCSS,
  PlanetScale et Stripe
subtitle: ''
author: Sharvin Shah
co_authors: []
series: null
date: '2022-10-25T16:30:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-ecommerce-website-using-next-js-and-planetscale
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Add-a-heading.png
tags:
- name: ecommerce
  slug: ecommerce
- name: React
  slug: react
- name: stripe
  slug: stripe
- name: tailwind
  slug: tailwind
- name: Web Development
  slug: web-development
seo_title: Comment créer un site eCommerce prêt pour la production avec ReactJS, TailwindCSS,
  PlanetScale et Stripe
seo_desc: 'Hello, welcome to this tutorial. Today we''re going to build a production-ready
  eCommerce website using ReactJS, TailwindCSS, PlanetScale, and Stripe.

  Before we begin, you should be familiar with the basics of React.js and Next.js
  to get the most out ...'
---

Bonjour, bienvenue dans ce tutoriel. Aujourd'hui, nous allons créer un site eCommerce prêt pour la production en utilisant ReactJS, TailwindCSS, PlanetScale et Stripe.

Avant de commencer, vous devriez être familiarisé avec les bases de React.js et Next.js pour tirer le meilleur parti de ce guide.

Si ce n'est pas le cas et que vous avez besoin de vous rafraîchir la mémoire, je vous recommande de consulter la [documentation ReactJS](https://reactjs.org/docs/getting-started.html) et la [documentation NextJS](https://nextjs.org/docs/getting-started).

## La stack que nous allons utiliser :

1. [ReactJS](https://reactjs.org/docs/getting-started.html) est une bibliothèque JavaScript pour construire des interfaces utilisateur. Elle est déclarative et basée sur les composants.
    
2. [NextJS](https://nextjs.org/docs/getting-started) est un framework basé sur React qui nous permet de rendre les données côté serveur. Il aide Google à crawler l'application, ce qui entraîne des avantages SEO.
    
3. [PlanetScale](https://planetscale.com/docs) est une base de données en tant que service qui est développée sur Vitess, une technologie open-source qui alimente YouTube et utilise MySQL en interne.
    
4. [TailwindCSS](https://tailwindcss.com/) est un framework CSS basé sur les utilitaires, rempli de classes qui peuvent être composées pour construire n'importe quel design, directement dans notre balisage.
    
5. [Prisma](https://www.prisma.io/docs/) est un ORM construit pour NodeJS et TypeScript qui gère les migrations automatisées, la sécurité des types et l'auto-complétion.
    
6. [Vercel](https://vercel.com/docs) hébergera notre application. Il scale bien, tout cela sans aucune configuration, et le déploiement est instantané.
    
7. [Stripe](https://stripe.com) est une passerelle de paiement, et nous l'utiliserons pour accepter les paiements en ligne sur le site web.
    

## Table des matières

1. [Comment configurer PlanetScale, Stripe, NextJS, Prisma et autres bibliothèques](#heading-configuration-planetscale-prisma-nextjs-et-stripe)
    
2. [Comment implémenter les données mock, l'API Catégorie-Produits et l'UI Toutes Catégories-Catégorie Unique](#heading-implementation-donnees-mock-api-categorie-produits-et-ui-toutes-categories-categorie-unique)
    
3. [Comment implémenter l'UI Produit Unique et le Checkout Stripe](#heading-implementation-ui-produit-unique-et-checkout-stripe)
    
4. [Comment déployer le site web en production](#heading-deploiement-site-web-en-production)
    

Je vais diviser ce tutoriel en quatre sections distinctes.

Au début de chaque section, vous trouverez un commit Git qui contient le code développé dans cette section. De plus, si vous souhaitez voir le code complet, il est disponible dans ce [dépôt](https://github.com/Sharvin26/Ecommerce-Website-ReactJS-TailwindCSS-PlanetScale-Stripe).

## Comment configurer PlanetScale, Stripe, NextJS, TailwindCSS et Prisma.

Dans cette section, nous allons implémenter les fonctionnalités suivantes :

1. Créer un compte PlanetScale et une base de données.
    
2. Créer un compte Stripe.
    
3. Configurer NextJS, TailwindCSS et Prisma.
    

Vous pouvez trouver le **code** du site **eCommerce** implémenté dans cette section à ce [commit](https://github.com/Sharvin26/Ecommerce-Website-ReactJS-TailwindCSS-PlanetScale-Stripe/tree/afa389dc07f565a39eacac5e3801fcc4e8d9041f).

### Comment configurer PlanetScale :

Pour créer un compte PlanetScale, visitez cette [URL](https://planetscale.com/). Cliquez sur le bouton Get started en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-2.01.59-PM.png align="left")

*Page d'accueil de PlanetScale*

Vous pouvez soit créer un compte en utilisant GitHub, soit utiliser un email et un mot de passe traditionnels. Une fois le compte créé, cliquez sur le lien "create".

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-05-at-5.00.59-PM.png align="left")

*Tableau de bord PlanetScale*

Vous recevrez la fenêtre modale suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-05-at-5.08.12-PM.png align="left")

*Nouvelle fenêtre modale de base de données PlanetScale*

Remplissez les détails et cliquez sur le bouton Create database. Une fois la base de données créée, vous serez redirigé vers la page suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-2.06.05-PM.png align="left")

*Page de la base de données du site eCommerce PlanetScale*

Cliquez sur connect et une fenêtre modale s'ouvrira. Cette fenêtre modale contiendra une URL de base de données et ce mot de passe ne peut pas être regénéré. Copiez-le donc et collez-le dans un endroit sûr.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-2.07.27-PM.png align="left")

*Fenêtre modale du nom d'utilisateur et du mot de passe de la base de données PlanetScale*

### Comment configurer Stripe :

Pour créer un compte Stripe, allez sur cette [URL](https://dashboard.stripe.com/register). Une fois que vous avez créé le compte, cliquez sur le bouton Developer dans le menu de navigation. Vous verrez les clés API sur le côté gauche et vous trouverez la clé publiable et la clé secrète sous Standard keys.

Clé publiable : Ce sont les clés qui peuvent être accessibles publiquement dans le code côté client d'une application web ou mobile.

Clé secrète : Il s'agit d'une information d'identification secrète et doit être stockée en toute sécurité dans le code serveur. Cette clé est utilisée pour appeler l'API Stripe.

### Comment configurer NextJS, TailwindCSS et Prisma.

Tout d'abord, nous allons créer une application NextJS en utilisant la commande suivante :

```shell
npx create-next-app ecommerce-tut --ts --use-npm
```

Une fois le projet créé, ouvrez-le avec votre éditeur préféré. Vous obtiendrez la structure suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-05-at-6.03.07-PM.png align="left")

*Structure du projet*

Créons un répertoire nommé `src`. Nous allons déplacer les répertoires `pages` et `styles` dans ce dossier `src`. Vous obtiendrez la structure suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-2.28.16-PM.png align="left")

*Structure du projet après avoir déplacé les pages et les styles.*

Installez les packages suivants :

```shell
npm i @ngneat/falso @prisma/client @stripe/stripe-js @tanstack/react-query currency.js next-connect react-icons react-intersection-observer stripe
```

Nous devons également installer les dépendances de développement :

```shell
npm i --save-dev @tanstack/react-query-devtools autoprefixer postcss tailwindcss
```

Comprenons chaque package :

1. [@ngneat/falso](https://ngneat.github.io/falso/) : Nous utiliserons cette bibliothèque pour créer des données mock pour notre site eCommerce. Dans un monde idéal, vous auriez un panneau d'administration pour ajouter les produits, mais ce n'est pas dans le cadre de ce tutoriel.
    
2. [@prisma/client](https://www.prisma.io/docs/concepts/components/prisma-client) : Nous utiliserons cette bibliothèque pour nous connecter à notre base de données, exécuter des migrations et effectuer toutes les opérations CRUD sur la base de données.
    
3. [@stripe/stripe-js](https://stripe.com/docs/js) : Nous utiliserons cette bibliothèque pour rediriger les utilisateurs vers la page de checkout Stripe et traiter le paiement.
    
4. [@tanstack/react-query](https://tanstack.com/query/v4/) : Nous utiliserons cette bibliothèque pour gérer notre état asynchrone, c'est-à-dire mettre en cache les réponses de l'API.
    
5. [currency.js](https://currency.js.org/) : Nous utiliserons cette bibliothèque pour convertir nos prix en format à deux décimales.
    
6. [next-connect](https://www.npmjs.com/package/next-connect) : Nous utiliserons cette bibliothèque pour le routage sur notre couche API Next.
    
7. [react-icons](https://react-icons.github.io/react-icons/) : Nous utiliserons cette bibliothèque pour ajouter des icônes à nos boutons et liens.
    
8. [react-intersection-observer](https://www.npmjs.com/package/react-intersection-observer) : Avez-vous vu le défilement infini sur de nombreux sites web et vous êtes-vous demandé comment il est implémenté ? Nous utiliserons cette bibliothèque pour l'implémenter en fonction de la viewport.
    
9. [stripe](https://www.npmjs.com/package/stripe) : Nous utiliserons la bibliothèque Stripe pour nous connecter à l'API Stripe depuis notre couche API Next.
    
10. [@tanstack/react-query-devtools](https://tanstack.com/query/v4/docs/devtools) : Nous utiliserons cette bibliothèque comme seule dépendance de développement pour visualiser et gérer notre cache pendant le développement.
    
11. [TailwindCSS](https://www.npmjs.com/package/tailwindcss) : Nous l'utiliserons comme notre bibliothèque CSS qui nécessite également PostCSS et AutoPrefixer.
    

Configurons TailwindCSS dans notre projet en utilisant la commande suivante :

```shell
npx tailwindcss init -p
```

Vous obtiendrez la réponse suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-2.29.52-PM.png align="left")

*Configuration réussie de TailwindCSS*

Maintenant, allez dans `tailwind.config.js` et mettez-le à jour avec le code suivant :

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./src/pages/**/*.{js,ts,jsx,tsx}",
        "./src/components/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};
```

Pour générer le CSS, Tailwind a besoin d'accéder à tous les éléments HTML. Nous allons écrire les composants UI sous les pages et composants uniquement, donc nous le passons sous content.

Si vous avez besoin d'utiliser des plugins, par exemple, la typographie, alors vous devez les ajouter sous le tableau des plugins. Si vous avez besoin d'étendre le thème par défaut fourni par Tailwind, alors vous devez l'ajouter sous la section `theme.extend`.

Maintenant, allez dans `/src/styles/globals.css` et remplacez le code existant par le suivant :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Nous allons ajouter ces trois directives dans notre fichier `globals.css`. La signification de chaque directive est la suivante :

1. @tailwind base : Cela injecte un style de base fourni par Tailwind.
    
2. @tailwind components : Cela injecte des classes et toute autre classe ajoutée par le plugin.
    
3. @tailwind utilities : Cela injecte le hover, le focus, le responsive, le mode sombre et toute autre utilité ajoutée par le plugin.
    

Supprimez le fichier `Home.module.css` du répertoire `src/styles` et allez dans `src/pages/index.ts` et remplacez le code existant par le suivant :

```tsx
import type { NextPage } from "next";
import Head from "next/head";

const Home: NextPage = () => {
    return (
        <div>
            <Head>
                <title>All Products</title>
                <meta name="description" content="All Products" />
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="container mx-auto">
                <h1 className="h-1">Hello</h1>
            </main>
        </div>
    );
};

export default Home;
```

Lorsque nous exécutons la commande `create-next-app` pour créer le projet, elle ajoute un certain code boilerplate. Ici, nous l'avons supprimé dans certains cas tout en remplaçant `index.ts` par un `h1` et un texte qui dit "Hello".

Il est temps d'exécuter le site web en utilisant la commande suivante :

```shell
npm run dev
```

Vous obtiendrez la réponse suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-2.36.15-PM.png align="left")

Ouvrez [http://localhost:3000](http://localhost:3000/) dans votre navigateur, et vous obtiendrez l'écran suivant avec un message hello :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-2.38.49-PM.png align="left")

*Écran avec le message Hello*

Configurons Prisma dans notre projet en utilisant la commande suivante :

```shell
npx prisma init
```

Vous obtiendrez la réponse suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-2.41.15-PM.png align="left")

*Message de configuration réussie de Prisma*

Sous `prisma/schema.prisma`, remplacez le code existant par le code suivant :

```python
// This is your Prisma schema file,
// learn more about it in the docs: https://pris.ly/d/prisma-schema

generator client {
  provider        = "prisma-client-js"
  previewFeatures = ["referentialIntegrity"]
}

datasource db {
  provider             = "mysql"
  url                  = env("DATABASE_URL")
  referentialIntegrity = "prisma"
}

model Category {
  id        String    @id @default(cuid())
  name      String    @unique
  createdAt DateTime  @default(now())
  products  Product[]
}

model Product {
  id          String    @id @default(cuid())
  title       String    @unique
  description String
  price       String
  quantity    Int
  image       String
  createdAt   DateTime  @default(now())
  category    Category? @relation(fields: [categoryId], references: [id])
  categoryId  String?
}
```

Ce fichier contient notre source de base de données qui est MySQL. Nous utilisons MySQL car PlanetScale ne supporte que MySQL.

De plus, nous avons créé deux modèles qui sont :

### Catégorie :

1. name : Chaque catégorie aura un titre unique.
    
2. createdAt : La date à laquelle une catégorie est ajoutée.
    
3. products : Une relation étrangère avec le modèle de produit.
    

### Produit :

1. title : Chaque produit aura un titre unique.
    
2. description : Il s'agit simplement d'informations sur le produit.
    
3. price : Il est de type `String` car il contiendra une valeur décimale.
    
4. quantity : Il est de type `Int` car il contiendra une valeur numérique.
    
5. image : Représentation de l'apparence du produit. Nous utiliserons placeimg à des fins de tutoriel.
    
6. createdAt : La date à laquelle un produit est ajouté.
    
7. category : Une relation étrangère avec le modèle de catégorie.
    

Nous utilisons `cuid()` au lieu de `uuid()` pour l'id car ils sont meilleurs pour la mise à l'échelle horizontale et les performances de recherche séquentielle. Prisma a un support intégré pour CUID. Vous pouvez en lire plus à ce sujet [ici](https://github.com/paralleldrive/cuid).

Il est temps de mettre à jour notre fichier `.env` avec ce qui suit :

```python
DATABASE_URL=

STRIPE_SECRET_KEY=

NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=
```

Vous trouverez la clé secrète Stripe et la clé publiable sous le tableau de bord. L'URL de la base de données est celle que nous avions copiée et collée précédemment et gardée dans un endroit sûr. Mettez à jour ce `.env` avec ces identifiants.

Notez également que le fichier `.gitignore` créé par NextJS n'ignore pas le fichier `.env`. Il est configuré pour ignorer le fichier `.env.local`. Mais Prisma nécessite `.env`, donc nous allons remplacer le contenu du fichier `.gitignore` par ce qui suit :

```python
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# local env files
.env
.env*.local

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
```

Idéalement, Prisma gère la migration de schéma en utilisant la commande `prisma migrate`. Mais comme PlanetScale a son propre mécanisme de migration de schéma intégré, nous allons utiliser celui-ci. Utilisez la commande suivante pour pousser la migration vers notre branche principale actuelle.

Notez que notre branche principale n'est pas encore promue en tant que branche de production.

```shell
npx prisma db push
```

Maintenant, générons le client Prisma en utilisant la commande suivante :

```shell
npx prisma generate
```

Allez dans le tableau de bord PlanetScale, et vous y trouverez deux tables créées :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-2.59.50-PM.png align="left")

*Deux tables créées dans PlanetScale*

Cliquez sur ces tables, et vous serez redirigé vers la page suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-3.00.39-PM.png align="left")

*Schémas de la base de données PlanetScale*

## Comment implémenter les données mock, l'API Catégorie-Produits et l'UI Toutes Catégories-Catégorie Unique.

Dans cette section, nous allons implémenter les fonctionnalités suivantes :

1. Créer des données mock
    
2. Créer une API Catégorie et Produit.
    
3. Créer une UI Toutes Catégories et Catégorie Unique.
    

Vous pouvez trouver le **code** du site **eCommerce** implémenté dans cette section à ce [commit](https://github.com/Sharvin26/Ecommerce-Website-ReactJS-TailwindCSS-PlanetScale-Stripe/tree/18bfb1152cfdeb14ba1a554d88d2b766a319d66a).

### Comment créer les données mock :

Sous le répertoire `prisma`, créez un fichier nommé `seed.ts` et copiez-collez le code suivant :

```ts
import {
    randBetweenDate,
    randNumber,
    randProduct,
    randProductAdjective,
} from "@ngneat/falso";
import { PrismaClient } from "@prisma/client";

const primsa = new PrismaClient();

const main = async () => {
    try {
        await primsa.category.deleteMany();
        await primsa.product.deleteMany();
        const fakeProducts = randProduct({
            length: 1000,
        });
        for (let index = 0; index < fakeProducts.length; index++) {
            const product = fakeProducts[index];
            const productAdjective = randProductAdjective();
            await primsa.product.upsert({
                where: {
                    title: `${productAdjective} ${product.title}`,
                },
                create: {
                    title: `${productAdjective} ${product.title}`,
                    description: product.description,
                    price: product.price,
                    image: `${product.image}/tech`,
                    quantity: randNumber({ min: 10, max: 100 }),
                    category: {
                        connectOrCreate: {
                            where: {
                                name: product.category,
                            },
                            create: {
                                name: product.category,
                                createdAt: randBetweenDate({
                                    from: new Date("10/06/2020"),
                                    to: new Date(),
                                }),
                            },
                        },
                    },
                    createdAt: randBetweenDate({
                        from: new Date("10/07/2020"),
                        to: new Date(),
                    }),
                },
                update: {},
            });
        }
    } catch (error) {
        throw error;
    }
};

main().catch((err) => {
    console.warn("Error While generating Seed: \n", err);
});
```

Ici, nous créons 1000 faux produits et les ajoutons à la base de données.

Nous suivons ces étapes pour ajouter les produits :

1. Supprimer toutes les catégories en utilisant la fonction `deleteMany()`.
    
2. Supprimer tous les produits en utilisant la fonction `deleteMany()`.
    
3. Les étapes ci-dessus sont facultatives, mais il est toujours bon de relancer le script de seed avec une table propre.
    
4. Comme l'attribut `title` du tableau `product` a une propriété unique associée, nous le liaisons avec la sortie de la fonction `randProductAdjective` pour rendre les répétitions moins probables.
    
5. Mais il y a toujours une probabilité que la propriété title créée par `falso` se répète. Nous utilisons donc la méthode upsert de `@prisma/client`.
    
6. Nous créons/associons également la catégorie lorsque nous créons un produit.
    

Maintenant, allez dans `package.json` et mettez à jour le code suivant sous `scripts` :

```shell
"prisma": {
    "seed": "ts-node --compiler-options {\"module\":\"CommonJS\" prisma/seed.ts"
},
```

Nous allons utiliser le package `ts-node` pour exécuter notre commande de script de seed. Le script de seed est écrit en TypeScript tandis que `ts-node` convertit le code TypeScript en JavaScript.

Utilisez la commande suivante pour installer le package :

```shell
npm i --save-dev ts-node
```

Comme `ts-node` convertira le code en JavaScript, nous pouvons exécuter la commande suivante pour ensemencer les tables avec des données mock :

```shell
npx prisma db seed
```

Vous obtiendrez la sortie suivante qui montrera qu'il a commencé à s'exécuter. Il faudra un certain temps pour ensemencer les tables avec des données mock.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-3.18.56-PM.png align="left")

Une fois la commande de seed réussie, vous obtiendrez la réponse suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-3.20.09-PM.png align="left")

L'avantage de Prisma est qu'il dispose également d'un studio, qui peut être utilisé pour visualiser la base de données dans un environnement de développement local. Utilisez la commande suivante pour exécuter ce studio :

```shell
npx prisma studio
```

Ouvrez [http://localhost:5555](http://localhost:5555) dans votre navigateur, et vous obtiendrez l'écran suivant avec toutes les tables :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-3.22.23-PM.png align="left")

*Prisma Studio*

Le nombre de produits et de catégories peut varier de votre côté ou être similaire, car il s'agit de données aléatoires.

### Comment créer les API Catégorie et Produit :

Sous la catégorie `src/pages/api`, vous trouverez un fichier nommé `hello.ts`. Supprimez ce fichier et créez deux répertoires nommés `categories` et `products`.

À l'intérieur de ces catégories, créez un fichier nommé `index.ts` et copiez-collez le code suivant :

```ts
import type { NextApiRequest, NextApiResponse } from "next";
import nc from "next-connect";
import { prisma } from "../../../lib/prisma";
import { TApiAllCategoriesResp, TApiErrorResp } from "../../../types";

const getCategories = async (
    _req: NextApiRequest,
    res: NextApiResponse<TApiAllCategoriesResp | TApiErrorResp>
) => {
    try {
        const categories = await prisma.category.findMany({
            select: {
                id: true,
                name: true,
                products: {
                    orderBy: {
                        createdAt: "desc",
                    },
                    take: 8,
                    select: {
                        title: true,
                        description: true,
                        image: true,
                        price: true,
                    },
                },
            },
            orderBy: {
                createdAt: "desc",
            },
        });
        return res.status(200).json({ categories });
    } catch (error) {
        return res.status(500).json({
            message: "Something went wrong!! Please try again after sometime",
        });
    }
};

const handler = nc({ attachParams: true }).get(getCategories);

export default handler;
```

Dans l'extrait ci-dessus, nous faisons ce qui suit :

1. Lorsque nous créons un fichier sous le répertoire `pages>api`, NextJS le traite comme une API Serverless. Donc, en créant un fichier nommé `categories/index.ts`, nous informons Next qu'il doit convertir cela en l'API `/api/categories`.
    
2. En utilisant la bibliothèque `next-connect`, nous nous assurons que seule l'opération `get` est autorisée pour la fonction `getCategories`.
    
3. Sous cette fonction, nous interrogeons la base de données avec un ordre `desc` pour la propriété `createdAt` et nous ne prenons que les huit dernières lignes de produits pour chaque ligne de catégorie. Nous sélectionnons également une propriété spécifique du produit et de la catégorie qui sont requises par le front-end.
    

Nous n'interrogeons pas tous les produits pour chaque catégorie dans cette API, car cela ralentirait notre temps de réponse.

Vous trouverez que nous avons importé les fichiers `prisma` et `types`. Créons deux répertoires sous `src` nommés `lib` et `types`.

Sous le répertoire `lib`, créez un fichier nommé `prisma.ts`, et sous le répertoire types, créez un fichier nommé `index.ts`.

Créons notre constante globale Prisma sous `prisma.ts`. Copiez-collez le code suivant :

```ts
import { PrismaClient } from "@prisma/client";

declare global {
    var prisma: PrismaClient;
}

export const prisma =
    global.prisma ||
    new PrismaClient({
        log: [],
    });

if (process.env.NODE_ENV !== "production") global.prisma = prisma;
```

Ici, nous créons une variable globale prisma que nous pouvons utiliser dans tout le projet.

Ajoutons les types que nous utiliserons dans toute l'application sous `src/types/index.ts`.

Copiez-collez le code suivant :

```ts
export type TApiAllCategoriesResp = {
    categories: {
        id: string;
        name: string;
        products: {
            title: string;
            description: string;
            image: string;
            price: string;
        }[];
    }[];
};

export type TApiSingleCategoryWithProductResp = {
    category: {
        id: string;
        name: string;
        products: {
            id: string;
            title: string;
            description: string;
            image: string;
            price: string;
            quantity: number;
        }[];
        hasMore: boolean;
    };
};

export type TApiSingleProductResp = {
    product: {
        title: string;
        description: string;
        price: string;
        quantity: number;
        image: string;
    };
};

export type TApiErrorResp = {
    message: string;
};
```

Ici, nous créons quatre types qui seront utilisés dans tout le projet.

Je vais utiliser Postman pour tester cette API. Postman est un utilitaire pour développer des API. Vous pouvez appeler les API, et Postman affichera la réponse en fonction de la manière dont vous la structurez.

Mettez simplement à jour l'URL dans Postman :

```shell
http://localhost:3000/api/categories
```

Et vous obtiendrez la réponse suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-3.58.53-PM.png align="left")

*Réponse de toutes les catégories*

Maintenant, créons une API pour obtenir les informations d'une seule catégorie avec ses produits.

Sous le répertoire `src/pages/api/categories`, créez un fichier nommé `[id].ts` et copiez-collez le code suivant :

```ts
import type { NextApiRequest, NextApiResponse } from "next";
import nc from "next-connect";
import { prisma } from "../../../lib/prisma";
import {
    TApiErrorResp,
    TApiSingleCategoryWithProductResp
} from "../../../types";

const getSingleCategory = async (
    req: NextApiRequest,
    res: NextApiResponse<TApiSingleCategoryWithProductResp | TApiErrorResp>
) => {
    try {
        const id = req.query.id as string;
        const cursorId = req.query.cursorId;
        if (cursorId) {
            const categoriesData = await prisma.category.findUnique({
                where: {
                    id,
                },
                select: {
                    id: true,
                    name: true,
                    products: {
                        orderBy: {
                            createdAt: "desc",
                        },
                        take: 12,
                        skip: 1,
                        cursor: {
                            id: cursorId as string,
                        },
                        select: {
                            id: true,
                            title: true,
                            description: true,
                            image: true,
                            price: true,
                            quantity: true,
                        },
                    },
                },
            });

            if (!categoriesData) {
                return res.status(404).json({ message: `Category not found` });
            }

            let hasMore = true;
            if (categoriesData.products.length === 0) {
                hasMore = false;
            }

            return res
                .status(200)
                .json({ category: { ...categoriesData, hasMore } });
        }

        const categoriesData = await prisma.category.findUnique({
            where: {
                id,
            },
            select: {
                id: true,
                name: true,
                products: {
                    orderBy: {
                        createdAt: "desc",
                    },
                    take: 12,
                    select: {
                        id: true,
                        title: true,
                        description: true,
                        image: true,
                        price: true,
                        quantity: true,
                    },
                },
            },
        });
        if (!categoriesData) {
            return res.status(404).json({ message: `Category not found` });
        }

        let hasMore = true;
        if (categoriesData.products.length === 0) {
            hasMore = false;
        }

        return res
            .status(200)
            .json({ category: { ...categoriesData, hasMore } });
    } catch (error) {
        return res.status(500).json({
            message: "Something went wrong!! Please try again after sometime",
        });
    }
};

const handler = nc({ attachParams: true }).get(getSingleCategory);

export default handler;
```

Dans l'extrait ci-dessus, nous faisons ce qui suit :

1. En créant un fichier nommé `[id].ts` sous `src/pages/api/categories`, nous disons à NextJS de convertir cela en l'API `/api/categories/[id]`.
    
2. Le `[id]` est l'identifiant de la catégorie dans le tableau des catégories.
    
3. En utilisant la bibliothèque `next-connect`, nous nous assurons que seule l'opération `get` est autorisée pour la fonction `getSingleCategory`.
    
4. Sous cette fonction, nous interrogeons la base de données avec un ordre `desc` pour la propriété `createdAt` et nous ne prenons que les douze dernières lignes de produits. Nous sélectionnons également une propriété spécifique du produit qui est requise par le front-end.
    

Dans cette API, vous trouverez que nous avons également implémenté la pagination. Elle nous aide à obtenir plus de produits sous une seule catégorie.

Il existe deux types de pagination. L'une est basée sur un curseur, et l'autre est basée sur un décalage.

Alors pourquoi avons-nous choisi la pagination basée sur un curseur plutôt que la pagination basée sur un décalage ?

[Selon la documentation de Prisma](https://www.prisma.io/docs/concepts/components/prisma-client/pagination),

> "La pagination par décalage ne se met pas à l'échelle au niveau de la base de données. Par exemple, si vous sautez 200 000 enregistrements et prenez les 10 premiers, la base de données doit toujours parcourir les 200 000 premiers enregistrements avant de retourner les 10 que vous avez demandés - cela affecte négativement les performances."

Pour plus d'informations, lisez ce [guide utile](https://www.prisma.io/docs/concepts/components/prisma-client/pagination).

Mettez à jour l'URL dans Postman :

```shell
http://localhost:3000/api/categories/cl91683hp006d0mvlxlg5u176?cursorId=cl91685ht00b00mvllxjwzkqk
```

Notre URL se compose de deux identifiants et vous devrez ajouter `cl91683hp006d0mvlxlg5u176` à partir de la réponse précédente de toutes les catégories. Cet identifiant `cl91685ht00b00mvllxjwzkqk` est simplement le curseur du produit et vous pouvez l'ajouter comme le dernier que vous souhaitez.

Vous obtiendrez la réponse suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-5.07.44-PM.png align="left")

*Réponse de la catégorie unique*

Maintenant, créons une API pour obtenir les informations d'un seul produit.

Sous le répertoire `src/pages/api/products`, créez un fichier nommé `[title].ts` et copiez-collez le code suivant :

```ts
import type { NextApiRequest, NextApiResponse } from "next";
import nc from "next-connect";
import { prisma } from "../../../lib/prisma";
import { TApiErrorResp, TApiSingleProductResp } from "../../../types";

const getSingleProduct = async (
    req: NextApiRequest,
    res: NextApiResponse<TApiSingleProductResp | TApiErrorResp>
) => {
    try {
        const title = req.query.title as string;
        const product = await prisma.product.findUnique({
            where: {
                title,
            },
            select: {
                title: true,
                description: true,
                price: true,
                quantity: true,
                image: true,
            },
        });
        if (!product) {
            return res.status(404).json({ message: `Product not found` });
        }
        return res.status(200).json({ product });
    } catch (error) {
        return res.status(500).json({
            message: "Something went wrong!! Please try again after sometime",
        });
    }
};

const handler = nc({ attachParams: true }).get(getSingleProduct);

export default handler;
```

Dans l'extrait ci-dessus, nous faisons ce qui suit :

1. En créant un fichier nommé `[title].ts` sous `src/pages/api/products`, nous informons NextJS de convertir cela en l'API `/api/products/[title]`.
    
2. Le `[title]` est le titre du produit dans le tableau des produits.
    
3. En utilisant la bibliothèque `next-connect`, nous nous assurons que seule l'opération `get` est autorisée pour la fonction `getSingleProduct`.
    
4. Sous cette fonction, nous interrogeons la base de données en utilisant la requête `findUnique` basée sur le titre.
    

Mettez à jour l'URL dans Postman :

```shell
http://localhost:3000/api/products/Practical Gorgeous Fresh Shoes
```

Ici, `Practical Gorgeous Fresh Shoes` est le titre du produit que nous voulons obtenir. Vous pouvez le remplacer par n'importe quel titre de produit de votre base de données.

Vous obtiendrez la réponse suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-5.12.35-PM.png align="left")

*Réponse du produit unique*

### Comment créer les interfaces utilisateur Toutes Catégories et Catégorie Unique :

Sous `src/pages/_app.tsx`, remplacez le code existant par le suivant :

```jsx
import { QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";
import type { AppProps } from "next/app";
import queryClient from "../lib/query";
import "../styles/globals.css";

function MyApp({ Component, pageProps }: AppProps) {
    return (
        <QueryClientProvider client={queryClient}>
            <ReactQueryDevtools initialIsOpen={false} />
            <Component {...pageProps} />
        </QueryClientProvider>
    );
}

export default MyApp;
```

Ici, nous enveloppons tous nos composants avec le fournisseur QueryClient de React. Mais nous devons également passer le contexte Client.

Sous le répertoire `src/lib`, créez un nouveau fichier nommé `query.ts` et copiez-collez le code suivant :

```jsx
import { QueryClient } from "@tanstack/react-query";

const queryClient = new QueryClient();

export default queryClient;
```

Nous initialisons un nouvel objet `QueryClient` et l'assignons à la variable `queryClient` et l'exportons par défaut. La raison pour laquelle nous faisons cela est que de cette manière nous pouvons garder l'objet `queryClient` comme un contexte global.

Sous `src/pages/index.tsx`, remplacez le code existant par le suivant :

```jsx
import { useQuery } from "@tanstack/react-query";
import type { NextPage } from "next";
import Head from "next/head";
import Navbar from "../components/Navbar";
import ProductGrid from "../components/ProductGrid";
import Skelton from "../components/Skelton";

const Home: NextPage = () => {
    const getAllCategories = async () => {
        try {
            const respJSON = await fetch("/api/categories");
            const resp = await respJSON.json();
            return resp;
        } catch (error) {
            throw error;
        }
    };

    const { isLoading, data } = useQuery(
        ["AllCategoreiesWithProducts"],
        getAllCategories
    );

    const categories = data?.categories;

    return (
        <div>
            <Head>
                <title>All Products</title>
                <meta name="description" content="All Products" />
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="container mx-auto">
                <Navbar />
                {isLoading ? (
                    <Skelton />
                ) : (
                    <>
                        {categories && categories?.length > 0 && (
                            <ProductGrid
                                showLink={true}
                                categories={categories}
                            />
                        )}
                    </>
                )}
            </main>
        </div>
    );
};

export default Home;
```

Comprenons notre code.

Ici, nous récupérons les données de l'endpoint `/api/categories` que nous avons écrit précédemment. Nous utilisons `useQuery` pour mettre en cache ces données avec la clé `AllCategoreiesWithProducts`.

Mais il y a trois composants que nous n'avons pas encore créés. Créons ceux-ci et comprenons chacun d'eux.

Sous le répertoire `src`, créez un répertoire `components`. Sous le répertoire `components` nouvellement créé, créez trois fichiers nommés `Navbar.tsx`, `ProductGrid.tsx` et `Skelton.tsx`.

Sous `Navbar.tsx`, copiez-collez le code suivant :

```jsx
import NextLink from "next/link";

const Navbar = () => {
    return (
        <div className="relative bg-white mx-6">
            <div className="flex items-center justify-between pt-6 md:justify-start md:space-x-10">
                <div className="flex justify-start lg:w-0 lg:flex-1">
                    <h1 className="text-2xl">
                        <NextLink href="/" className="cursor-pointer">
                            Ecomm App
                        </NextLink>
                    </h1>
                </div>
            </div>
        </div>
    );
};

export default Navbar;
```

Ici, nous avons créé un `h1` avec le texte Ecomm App. Nous avons enveloppé ce texte autour de `NextLink` et défini l'emplacement comme `/`. Donc, lorsque l'utilisateur clique dessus, il sera redirigé vers la page d'accueil.

Sous `ProductGrid.tsx`, copiez-collez le code suivant :

```jsx
import NextImage from "next/image";
import NextLink from "next/link";
import { useEffect } from "react";
import { AiOutlineRight } from "react-icons/ai";
import { useInView } from "react-intersection-observer";
import { TApiAllCategoriesResp } from "../types";

interface IProductGrid extends TApiAllCategoriesResp {
    showLink: boolean;
    hasMore?: boolean;
    loadMoreFun?: Function;
}

const ProductGrid = (props: IProductGrid) => {
    const { categories, showLink, loadMoreFun, hasMore } = props;
    const { ref, inView } = useInView();

    useEffect(() => {
        if (inView) {
            if (loadMoreFun) loadMoreFun();
        }
    }, [inView, loadMoreFun]);

    return (
        <div className="bg-white">
            {categories.map((category) => (
                <div className="mt-12  p-6" key={category.name}>
                    <div className="flex flex-row justify-between">
                        <span className="inline-flex items-center rounded-md bg-sky-800 px-8 py-2 text-md font-medium text-white">
                            {category.name}
                        </span>
                        {showLink && (
                            <NextLink href={`/category/${category.id}`}>
                                <p className="flex flex-row gap-2 underline hover:cursor-pointer items-center">
                                    View More
                                    <AiOutlineRight />
                                </p>
                            </NextLink>
                        )}
                    </div>
                    <div className="mt-6  grid grid-cols-1 gap-y-10 gap-x-6 xl:gap-x-8 sm:grid-cols-2 lg:grid-cols-4">
                        {category?.products.map((product) => (
                            <div
                                className="p-6 group rounded-lg border border-gray-200 bg-neutral-200"
                                key={product.title}
                            >
                                <div className="min-h-80 w-full overflow-hidden rounded-md group-hover:opacity-75 lg:aspect-none lg:h-80">
                                    <NextImage
                                        priority={true}
                                        layout="responsive"
                                        width="25"
                                        height="25"
                                        src={`${product.image}`}
                                        alt={product.title}
                                        className="h-full w-full object-cover object-center lg:h-full lg:w-full"
                                    />
                                </div>
                                <div className="relative mt-2">
                                    <h3 className="text-sm font-medium text-gray-900">
                                        {product.title}
                                    </h3>
                                    <p className="mt-1 text-sm text-gray-500">
                                        {product.price}
                                    </p>
                                </div>
                                <div className="mt-6">
                                    <NextLink
                                        href={`/product/${product.title}`}
                                    >
                                        <p className="relative flex items-center justify-center rounded-md border border-transparent bg-sky-800 py-2 px-8 text-sm font-medium text-white hover:bg-sky-900 hover:cursor-pointer">
                                            View More Details
                                        </p>
                                    </NextLink>
                                </div>
                            </div>
                        ))}
                    </div>
                    {!showLink && (
                        <div className="flex items-center justify-center mt-8">
                            {hasMore ? (
                                <button
                                    ref={ref}
                                    type="button"
                                    className="inline-flex items-center rounded-md border border-transparent bg-sky-800 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-900"
                                >
                                    Loading...
                                </button>
                            ) : (
                                <div className="border-l-4 border-yellow-400 bg-yellow-50 p-4 w-full">
                                    <div className="flex">
                                        <div className="ml-3">
                                            <p className="text-sm text-yellow-700">
                                                You have viewed all the Products
                                                under this category.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            )}
                        </div>
                    )}
                    {showLink && (
                        <div className="w-full border-b border-gray-300 mt-24" />
                    )}
                </div>
            ))}
        </div>
    );
};

export default ProductGrid;
```

Ici, nous avons créé une grille qui affichera 1 colonne pour l'écran de base. Pour l'écran sm, elle affichera 2 colonnes et pour l'écran lg, elle affichera 4 colonnes.

Sous celle-ci, nous avons une seule carte qui contient un titre, un prix et un bouton View More Details. Le bouton View More Details redirige l'utilisateur vers une page de produit unique que nous créerons un peu plus tard.

En plus de cela, nous utilisons le hook `useInView` de la bibliothèque `react-intersection-observer` pour trouver le curseur de l'utilisateur sur l'écran. Cette référence est attachée à un bouton `Loading...` et une fois que l'utilisateur est à proximité, nous exécutons la fonction `loadMoreFn`.

Cela effectue un appel API au serveur pour obtenir les douze lignes suivantes à partir du dernier curseur.

Sous `Skelton.tsx`, copiez-collez le code suivant :

```jsx
const Skelton = () => {
    return (
        <>
            <div className="mt-12 h-8 w-40 rounded-lg bg-gray-200" />
            <div className="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
                {Array(16)
                    .fill(0)
                    .map((_val, index) => (
                        <div className="rounded-2xl bg-black/5 p-4" key={index}>
                            <div className="h-60 rounded-lg bg-gray-200" />
                            <div className="space-y-4 mt-6 mb-4">
                                <div className="h-3 w-3/5 rounded-lg bg-gray-200" />
                                <div className="h-3 w-4/5 rounded-lg bg-gray-200" />
                            </div>
                        </div>
                    ))}
            </div>
        </>
    );
};

export default Skelton;
```

Nous utilisons `placeimg` pour obtenir des images fictives pour notre produit et nous utilisons le composant Next Image qui nécessite qu'il soit mentionné sous `next.config.js`.

Remplacez le code existant dans `next.config.js` par le code suivant :

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    swcMinify: true,
    images: {
        domains: ["placeimg.com"],
    },
};

module.exports = nextConfig
```

Nous devons redémarrer notre serveur. Utilisez la commande suivante pour redémarrer votre serveur de développement :

```shell
npm run dev
```

Ouvrez [http://localhost:3000/](http://localhost:3000/) et vous verrez l'interface utilisateur suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-5.31.29-PM.png align="left")

*Page Tous les Produits*

Maintenant, créons une page de catégorie unique que l'utilisateur peut visiter en utilisant un lien `View More`.

Sous `src/pages`, créez un répertoire nommé `category`. Sous ce répertoire, créez un fichier nommé `[id].tsx` et copiez-collez le code suivant :

```jsx
import { useInfiniteQuery } from "@tanstack/react-query";
import Head from "next/head";
import { useRouter } from "next/router";
import Navbar from "../../components/Navbar";
import ProductGrid from "../../components/ProductGrid";
import Skelton from "../../components/Skelton";

const SingleCategory = () => {
    const router = useRouter();

    const getSingleCategory = async ({ pageParam = null }) => {
        try {
            let url = `/api/categories/${router.query.id}`;
            if (pageParam) {
                url += `?cursorId=${pageParam}`;
            }
            const respJSON = await fetch(url);
            const resp = await respJSON.json();
            return resp;
        } catch (error) {
            throw error;
        }
    };

    const { isLoading, data, fetchNextPage, isError } = useInfiniteQuery(
        [`singleCategory ${router.query.id as string}`],
        getSingleCategory,
        {
            enabled: !!router.query.id,
            getNextPageParam: (lastPage) => {
                const nextCursor =
                    lastPage?.category?.products[
                        lastPage?.category?.products?.length - 1
                    ]?.id;
                return nextCursor;
            },
        }
    );

    const allProductsWithCategory: any = {
        name: "",
        products: [],
        hasMore: true,
    };

    data?.pages.map((page) => {
        if (page?.category) {
            if (page.category?.name) {
                allProductsWithCategory.name = page.category?.name;
            }
            if (page.category?.products && page.category?.products.length > 0) {
                allProductsWithCategory.products.push(
                    ...page.category?.products
                );
            }
        }
        return page?.category;
    });

    if (data?.pages[data?.pages.length - 1]?.category?.products.length === 0) {
        allProductsWithCategory.hasMore = false;
    }

    return (
        <div>
            <Head>
                <title>
                    {isLoading
                        ? "Loading..."
                        : `All ${allProductsWithCategory?.name} Product`}
                </title>
                <meta
                    name="description"
                    content="Generated by create next app"
                />
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <main className="container mx-auto">
                <Navbar />
                {isLoading ? (
                    <Skelton />
                ) : (
                    <>
                        {allProductsWithCategory &&
                            allProductsWithCategory.products.length > 0 && (
                                <ProductGrid
                                    hasMore={allProductsWithCategory.hasMore}
                                    showLink={false}
                                    categories={[allProductsWithCategory]}
                                    loadMoreFun={fetchNextPage}
                                />
                            )}
                    </>
                )}
            </main>
        </div>
    );
};

export default SingleCategory;
```

Ici, nous appelons l'API `/api/categories/[id]` pour obtenir les douze derniers produits pour cet identifiant de catégorie.

Nous utilisons le hook `useInfiniteQuery` de `react query` pour récupérer les données. Ce hook est utile pour la pagination basée sur un curseur. Nous allons utiliser le composant `ProductGrid` que nous avons créé précédemment.

Ouvrez [http://localhost:3000/](http://localhost:3000/), cliquez sur le lien View More pour l'une des catégories, et vous verrez l'interface utilisateur suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-5.38.25-PM.png align="left")

*Page de Catégorie Unique*

La différence entre l'interface utilisateur précédente et l'actuelle est que nous n'avons plus le lien View More dans le coin supérieur droit. De plus, lorsque vous faites défiler vers le bas, vous obtenez plus de produits pour cette catégorie.

Une fois que nous avons fait défiler tous les produits de cette catégorie, nous verrons l'alerte d'avertissement suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-5.39.44-PM.png align="left")

## Comment implémenter l'interface utilisateur du produit unique et le checkout Stripe.

Dans cette section, nous allons implémenter les fonctionnalités suivantes :

1. Créer l'interface utilisateur du produit unique
    
2. Créer le checkout Stripe
    

Vous pouvez trouver le **code** du site **eCommerce** implémenté dans cette section à ce [commit](https://github.com/Sharvin26/Ecommerce-Website-ReactJS-TailwindCSS-PlanetScale-Stripe/tree/e4b5426423358479a5bbe91ba17b3febacd5e4a3).

### Comment créer l'interface utilisateur du produit unique :

Sous le répertoire `src/pages`, créez un répertoire nommé `product`.

Sous ce répertoire, créez un fichier nommé `[title].tsx` et copiez-collez le code suivant :

```jsx
import { loadStripe, Stripe } from "@stripe/stripe-js";
import { useMutation, useQuery } from "@tanstack/react-query";
import Head from "next/head";
import NextImage from "next/image";
import { useRouter } from "next/router";
import Navbar from "../../components/Navbar";
import Skelton from "../../components/Skelton";

const stripePromiseclientSide = loadStripe(
    process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY!
);

const SingleProduct = () => {
    const router = useRouter();

    const getSingleProduct = async () => {
        try {
            const title = router?.query?.title;

            const respJSON = await fetch(`/api/products/${title}`);
            const resp = await respJSON.json();
            return resp;
        } catch (error) {
            throw error;
        }
    };

    const { mutate, isLoading: mutationIsLoading } = useMutation(
        async (body: any) => {
            try {
                const respJSON = await fetch("/api/create-checkout-session", {
                    method: "POST",
                    body: JSON.stringify(body),
                });
                const resp = await respJSON.json();
                const stripe = (await stripePromiseclientSide) as Stripe;
                const result = await stripe.redirectToCheckout({
                    sessionId: resp.id,
                });
                return result;
            } catch (error) {
                throw error;
            }
        }
    );

    const { data, isLoading } = useQuery(
        [`singleProduct, ${router?.query?.title}`],
        getSingleProduct,
        {
            enabled: !!router?.query?.title,
        }
    );

    const product = data?.product;

    return (
        <div>
            <Head>
                <title>{isLoading ? "Loading..." : `${product?.title}`}</title>
                <meta
                    name="description"
                    content="Generated by create next app"
                />
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <main className="container mx-6 md:mx-auto">
                <Navbar />
                {isLoading ? (
                    <Skelton />
                ) : (
                    <div className="bg-white">
                        <div className="pt-6 pb-16 sm:pb-24">
                            <div className="mx-auto mt-8">
                                <div className="flex flex-col md:flex-row gap-x-8">
                                    <div className="min-h-80 w-full overflow-hidden rounded-md group-hover:opacity-75 lg:aspect-none lg:h-80">
                                        <NextImage
                                            layout="responsive"
                                            width="25"
                                            height="25"
                                            src={`${product.image}`}
                                            alt={product.title}
                                            className="h-full w-full object-cover object-center lg:h-full lg:w-full"
                                        />
                                    </div>
                                    <div className="lg:col-span-5 lg:col-start-8 mt-8 md:mt-0">
                                        <h1 className="text-xl font-medium text-gray-900 ">
                                            {product.title}
                                        </h1>
                                        <p className="text-xl font-light text-gray-700 mt-4">
                                            {product.description}
                                        </p>
                                        <p className="text-xl font-normal text-gray-500 mt-4">
                                            USD {product.price}
                                        </p>
                                        <button
                                            onClick={() =>
                                                mutate({
                                                    title: product.title,
                                                    image: product.image,
                                                    description:
                                                        product.description,
                                                    price: product.price,
                                                })
                                            }
                                            disabled={mutationIsLoading}
                                            type="button"
                                            className="inline-flex items-center rounded-md border border-transparent bg-sky-800 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-900  mt-4"
                                        >
                                            Buy Now
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
            </main>
        </div>
    );
};

export default SingleProduct;
```

Ici, nous appelons l'API `/api/products/title` pour obtenir le dernier produit. Nous avons également créé une interface Stripe pour créer une méthode de checkout une fois qu'un utilisateur clique sur le bouton Buy Now.

Une fois que l'utilisateur clique sur le bouton Buy Now, nous faisons un appel API à `/api/create-checkout-session` en utilisant le hook `useMutation`. En cas de réponse réussie, nous redirigeons l'utilisateur vers la page de checkout par défaut de Stripe.

Ouvrez [http://localhost:3000/](http://localhost:3000/) et cliquez sur le bouton View More Details pour n'importe quel produit.

Vous verrez l'interface utilisateur suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-5.54.40-PM.png align="left")

*Page du Produit Unique*

Vous pouvez également visiter cette page en cliquant sur le lien View More, puis en cliquant sur le bouton View More Details pour n'importe quel produit.

### Comment configurer le checkout Stripe :

Pour configurer le checkout Stripe, nous devons ajouter un nouveau fichier sous le répertoire lib.

Créez un nouveau fichier nommé `stripe.ts` sous le répertoire lib et copiez-collez le code suivant :

```ts
import Stripe from "stripe";

const stripeServerSide = new Stripe(process.env.STRIPE_SECRET_KEY!, {
    apiVersion: "2022-08-01",
});

export { stripeServerSide };
```

Ici, nous créons des instances côté serveur de Stripe. Maintenant, sous le répertoire `pages/api`, créez un nouveau fichier nommé `create-checkout-session.ts` et copiez-collez le code suivant :

```ts
import currency from "currency.js";
import type { NextApiRequest, NextApiResponse } from "next";
import nc from "next-connect";
import { stripeServerSide } from "../../lib/stripe";
import { TApiErrorResp } from "../../types";

const checkoutSession = async (
    req: NextApiRequest,
    res: NextApiResponse<any | TApiErrorResp>
) => {
    try {
        const host = req.headers.origin;
        const referer = req.headers.referer;
        const body = JSON.parse(req.body);
        const formatedPrice = currency(body.price, {
            precision: 2,
            symbol: "",
        }).multiply(100);
        const session = await stripeServerSide.checkout.sessions.create({
            mode: "payment",
            payment_method_types: ["card"],
            line_items: [
                {
                    price_data: {
                        currency: "usd",
                        product_data: {
                            name: body?.title,
                            images: [body.image],
                            description: body?.description,
                        },
                        unit_amount_decimal: formatedPrice.toString(),
                    },
                    quantity: 1,
                },
            ],
            success_url: `${host}/thank-you`,
            cancel_url: `${referer}?status=cancel`,
        });
        return res.status(200).json({ id: session.id });
    } catch (error) {
        return res.status(500).json({
            message: "Something went wrong!! Please try again after sometime",
        });
    }
};

const handler = nc({ attachParams: true }).post(checkoutSession);

export default handler;
```

Dans l'extrait ci-dessus, nous faisons ce qui suit :

1. Formatage du prix avec une précision de deux et multiplication par 100 car Stripe attend le montant unitaire en cents par défaut.
    
2. Nous créons la session et transmettons l'identifiant comme réponse.
    

Maintenant, nous devons créer une autre page nommée `thank-you.tsx` sous le répertoire `src/pages`. Une fois l'achat du produit réussi, Stripe Checkout redirigera vers cette page.

Copiez-collez le code suivant sous ce fichier :

```jsx
import Head from "next/head";
import { useRouter } from "next/router";
import { HiCheckCircle } from "react-icons/hi";
import Navbar from "../components/Navbar";

const ThankYou = () => {
    const router = useRouter();
    return (
        <div>
            <Head>
                <title>Thank You</title>
                <meta name="description" content="All Products" />
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="container mx-auto">
                <Navbar />
                <div className="rounded-md bg-green-50 p-4 mt-8">
                    <div className="flex">
                        <div className="flex-shrink-0">
                            <HiCheckCircle
                                className="h-5 w-5 text-green-400"
                                aria-hidden="true"
                            />
                        </div>
                        <div className="ml-3">
                            <h3 className="text-sm font-medium text-green-800">
                                Order Placed
                            </h3>
                            <div className="mt-2 text-sm text-green-700">
                                <p>
                                    Thank you for your Order. We have placed the
                                    order and your email will recieve further
                                    details.
                                </p>
                            </div>
                            <button
                                onClick={() => router.push("/")}
                                type="button"
                                className="inline-flex items-center rounded-md border border-transparent bg-sky-800 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-900 mt-4"
                            >
                                Continue Shopping
                            </button>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    );
};

export default ThankYou;
```

Ouvrez [http://localhost:3000/](http://localhost:3000/) et cliquez sur le bouton View More Details de n'importe quel produit.

Cliquez sur le bouton Buy Now et vous serez redirigé vers la page suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-6.09.52-PM.png align="left")

Ajoutez tous les détails pour la carte de test. Vous pouvez utiliser n'importe quelle carte de ce [lien](https://stripe.com/docs/testing?numbers-or-method-or-token=card-numbers#cards). Stripe fournit diverses cartes de test qui fonctionnent uniquement en mode Test. Une fois que vous cliquez sur Pay et que le traitement du paiement est effectué, Stripe vous redirigera vers la page de succès.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-09-at-6.14.51-PM.png align="left")

*Page de Remerciement*

## Comment déployer le site web en production

Dans cette section, nous allons implémenter les fonctionnalités suivantes :

1. Promouvoir notre branche PlanetScale en Main.
    
2. Déployer l'application sur Vercel.
    

### Comment promouvoir la branche PlanetScale en Main :

Pour promouvoir la branche en main, nous pouvons le faire soit via le terminal, soit via le tableau de bord. J'utiliserai le tableau de bord pour ce tutoriel.

Allez dans votre projet sur PlanetScale et vous trouverez le message suivant sur le tableau de bord :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-10-at-4.19.14-PM.png align="left")

*Promotion de la base de données PlanetScale*

Cliquons sur le bouton Promote a branch to production et vous obtiendrez un modèle de confirmation. Cliquez sur le bouton Promote branch. Une fois terminé, vous obtiendrez un toast avec un message de succès.

### Comment déployer sur Vercel :

Si vous n'avez pas de compte sur Vercel, vous pouvez en créer un [ici](https://vercel.com/signup).

Vous pouvez créer un projet sur GitHub et le pousser vers la branche Main. Si vous ne savez pas comment faire, vous pouvez consulter [ce tutoriel](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git).

Une fois le projet poussé sur GitHub, allez sur Vercel et créez un bouton Add New et sélectionnez Project dans le menu déroulant.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-10-at-4.26.04-PM.png align="left")

*Ajouter un nouveau projet Vercel*

Vous obtiendrez l'interface utilisateur suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-10-at-4.26.39-PM.png align="left")

*Sélectionner le fournisseur Git Vercel*

Comme nous avons poussé le code sur GitHub, cliquons sur le bouton Continue with GitHub. Vous obtiendrez l'interface utilisateur suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-10-at-4.28.03-PM.png align="left")

*Sélectionner le dépôt Git Vercel*

Cliquez sur Import et vous obtiendrez l'interface utilisateur suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-10-at-4.29.39-PM.png align="left")

*Configurer le projet Vercel*

Cliquez sur Environment Variables et ajoutez ces trois-là :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-10-at-4.31.02-PM.png align="left")

*Ajouter NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY et DATABASE_URL*

Une fois terminé, cliquez sur le bouton Deploy. Vous obtiendrez l'interface utilisateur suivante une fois le déploiement démarré :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-10-at-4.31.52-PM.png align="left")

*Déploiement Vercel*

Une fois déployé, Vercel vous donnera une URL unique.

Visitez cette URL et vous constaterez qu'elle échoue. Allons dans deployment > functions et vous verrez l'erreur suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-10-at-4.38.08-PM.png align="left")

*Échec de la génération de Prisma*

Nous devons mettre à jour notre commande de build dans `package.json` comme suit :

```shell
"build": "npx prisma generate && next build",
```

Poussez le code à nouveau vers le dépôt Git et vous constaterez que Vercel commence à redéployer votre projet.

Une fois le déploiement terminé, vous pouvez visiter l'URL de votre application et vous constaterez qu'elle affiche tous vos produits.

Avec cela, nous avons créé notre application eCommerce prête pour la production. Si vous avez construit le site web en suivant le tutoriel, alors un très grand bravo pour cette réalisation.

## **Merci d'avoir lu !**

N'hésitez pas à me contacter sur [Twitter](https://twitter.com/sharvinshah26) et [Github](https://github.com/Sharvin26).

Si vous souhaitez que je développe un projet ou si vous souhaitez me consulter, vous pouvez m'envoyer un message direct sur mon Twitter ([@sharvinshah26](https://twitter.com/sharvinshah26)).