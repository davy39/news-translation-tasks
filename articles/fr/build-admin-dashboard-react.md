---
title: Comment créer un tableau de bord d'administration avec React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2024-01-30T19:04:01.000Z'
originalURL: https://freecodecamp.org/news/build-admin-dashboard-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/admin-dashboard-2.png
tags:
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Comment créer un tableau de bord d'administration avec React
seo_desc: 'Have you looked at interactive dashboards on websites like Stripe and thought,
  “How can I build something like this myself?”

  In this full-stack React and Next.js project, you’ll learn how to build a stunning
  admin dashboard from front to back.

  Our fi...'
---

Avez-vous déjà regardé des tableaux de bord interactifs sur des sites comme Stripe et pensé : "Comment puis-je construire quelque chose comme ça moi-même ?"

Dans ce projet full-stack React et Next.js, vous apprendrez à construire un superbe tableau de bord d'administration de A à Z.

Notre tableau de bord d'administration final vous permettra d'afficher et de rechercher des utilisateurs authentifiés dans un tableau d'utilisateurs et d'afficher des données importantes à l'aide de graphiques en barres et en lignes interactifs.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/admin-dashboard-2.png)
_La version finale de notre tableau de bord d'administration_

En plus d'apprendre des concepts importants de Next.js, vous vous familiariserez avec une série d'outils puissants, notamment Prisma, PostgreSQL, Tremor, NextAuth et TailwindCSS.

## Table des matières

* [Outils à installer](#heading-outils-a-installer)
* [Créer une base de données Postgres](#heading-comment-creer-une-base-de-donnees-postgres)
* [Configurer le schéma Prisma](https://www.freecodecamp.org/news/p/6fe70a96-0bef-4221-b4fd-8b624f7400ea/-comment-configurer-le-schema-prisma)
* [Utiliser le client Prisma](#heading-comment-utiliser-le-client-prisma)
* [Connecter Prisma à NextAuth](#heading-comment-connecter-prisma-a-nextauth)
* [Construire la barre de navigation de l'application](#heading-comment-construire-la-barre-de-navigation-de-lapplication)
* [Afficher les informations du compte](#heading-comment-afficher-les-informations-du-compte)
* [Protéger les routes](#heading-comment-proteger-les-routes)
* [Créer la page d'analytique](#heading-comment-creer-la-page-danalytique)
* [Construire le composant de graphique](#heading-comment-construire-le-composant-de-graphique)
* [Créer le tableau des utilisateurs](#heading-comment-creer-le-tableau-des-utilisateurs)
* [Rechercher des utilisateurs](#heading-comment-rechercher-des-utilisateurs)
* [Conclusion](#heading-conclusion)
* [Devenir un développeur React professionnel](#heading-devenir-un-developpeur-react-professionnel)

## \ud83d\udcc1 Télécharger le code

Vous pouvez récupérer le code de départ et final pour le projet que nous allons construire [ici](https://codebootcamp.nyc3.digitaloceanspaces.com/downloads/react-admin-dashboard-code.zip).

## \ud83d\udee0\ufe0f Outils à installer

Pour commencer à construire le tableau de bord d'administration, vous aurez besoin de :

* [Node.js](https://nodejs.org) installé sur votre ordinateur.
* Vous devriez également avoir un éditeur de code, tel que [Visual Studio Code](https://code.visualstudio.com).
* Enfin, vous aurez besoin d'un [compte Github](https://github.com).

Une fois que vous avez récupéré le code de départ et décompressé le dossier de départ, glissez-le dans Visual Studio Code, ouvrez une fenêtre de terminal et exécutez la commande :

```bash
npm install

```

Cela installera toutes les dépendances de votre application listées dans le fichier package.json.

Après avoir fait cela, vous pouvez démarrer votre serveur de développement en exécutant cette commande :

```bash
npm run dev

```

Vous pouvez visiter localhost:3000 dans votre navigateur pour voir votre application en cours d'exécution.

## \ud83d\udcc0 Comment créer une base de données Postgres

Le backend de votre application consistera en une base de données Postgres. Nous utiliserons Prisma pour interagir avec cette base de données et le service d'authentification sera NextAuth.

Pour créer une nouvelle base de données Postgres, visitez [railway.app/new](https://railway.app/new). Vous pouvez créer une base de données PostgreSQL gratuitement sans créer de compte.

Une fois notre base de données créée, cliquez dessus, puis allez dans l'onglet Variables et copiez la valeur `DATABASE_URL`.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-3.11.11-PM-2.png)
_Page des variables pour la base de données Postgres sur Railway_

Après cela, allez dans le fichier **.env.example** de votre projet, renommez-le en **.env**, et ajoutez l'URL de la base de données à la variable d'environnement `DATABASE_URL`.

## \u270d\ufe0f Comment configurer le schéma Prisma

Maintenant que nous avons une base de données pleinement fonctionnelle, vous devez la connecter avec Prisma. Prisma est ce que nous utiliserons pour modéliser toutes nos données. Vous pouvez voir cela dans le fichier **schema.prisma**.

Le fichier **schema.prisma** s'occupe de la connexion à la base de données, de la configuration d'un client Prisma et de la modélisation de toutes vos données.

Dans votre terminal, exécutez la commande `npx prisma db push`. Cela poussera votre schéma vers votre base de données Postgres Railway.

Cette commande génère également votre client Prisma, qui vous permet d'obtenir et de modifier des données dans votre base de données en utilisant Prisma.

## Comment utiliser le client Prisma

Dans le dossier **lib**, créez un fichier **prisma.ts**. Dans ce fichier, vous passerez le client Prisma à votre application entière en tant que variable globale.

```ts
// lib/prisma.ts
import { PrismaClient } from "@prisma/client";

declare global {
  var prisma: PrismaClient;
}

const client = globalThis.prisma || new PrismaClient();
if (process.env.NODE_ENV !== "production") globalThis.prisma = client;

export default client;

```

Maintenant, vous pouvez simplement importer `client` dans n'importe quel fichier qui a besoin d'utiliser Prisma et obtenir des données de votre base de données.

## \ud83e\ude9d Comment connecter Prisma à NextAuth

L'étape suivante consiste à connecter Prisma à NextAuth, qui sera responsable de l'authentification de nos utilisateurs.

Dans le dossier racine de votre projet, créez un dossier **pages**, qui doit contenir un dossier API, qui doit contenir un dossier **auth**. Dans le dossier auth, placez le fichier `[nextauth].ts`.

Votre structure de dossiers doit ressembler à ceci :

```md
pages
  api
     auth
	    [...nextauth].ts

```

C'est ici que vous configurerez NextAuth, qui doit être connecté à Prisma en utilisant l'adaptateur Prisma.

Dans ce fichier, vous pouvez coller le code suivant :

```ts
// pages/api/auth/[...nextauth].ts
import prisma from "@/lib/prisma";
import { PrismaAdapter } from "@next-auth/prisma-adapter";
import NextAuth, { AuthOptions } from "next-auth";
import GitHub from "next-auth/providers/github";

export const authOptions: AuthOptions = {
  adapter: PrismaAdapter(prisma),
  providers: [
    GitHub({
      clientId: process.env.GITHUB_CLIENT_ID!,
      clientSecret: process.env.GITHUB_CLIENT_SECRET!,
    }),
  ],
  debug: process.env.NODE_ENV === "development",
  secret: process.env.NEXTAUTH_SECRET,
  callbacks: {
    async signIn() {
      return true;
    },
    async redirect() {
      return "/";
    },
  },
};

export default NextAuth(authOptions);

```

Pour authentifier les utilisateurs avec Github, vous utiliserez le fournisseur Github, qui nécessite un ID client et un secret client.

Pour les récupérer, vous devrez vous connecter à votre compte Github et utiliser [ce lien](https://github.com/settings/applications/new) pour créer une nouvelle application OAuth Github.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-4.16.40-PM.png)
_Enregistrement d'une application OAuth Github_

Ajoutez un nom d'application unique tel que "Tableau de bord d'administration". L'URL de la page d'accueil sera [http://localhost:3000](http://localhost:3000), où votre application s'exécute en développement. Ce sera votre URL de production si vous choisissez de déployer cette application.

L'URL de rappel est incluse dans le fichier **.env**. La route catch-all que nous avons configurée permet à cette URL de rappel d'être utilisée.

Ensuite, enregistrez l'application pour recevoir votre ID client, que vous définirez dans la variable d'environnement `GITHUT_CLIENT_ID`. Générez un nouveau secret client, copiez-le et incluez-le sous `GITHUB_CLIENT_SECRET`.

Enfin, nous avons besoin d'un secret. Retournez à votre fichier **.env**. J'ai inclus une commande pour générer une chaîne unique :

```bash
openssl rand -hex 32

```

Exécutez cette commande dans votre terminal, puis collez la chaîne générée pour `NEXT_AUTH_SECRET`.

Avec toutes les variables d'environnement que nous avons fournies, Next Auth est configuré avec succès et peut être utilisé pour authentifier les utilisateurs et protéger les routes dans notre application.

## \ud83e\udded Comment construire la barre de navigation de l'application

Tous les composants de notre application seront placés dans le dossier "components".

Incluons un composant Navbar sur chaque page de l'application. Pour cela, nous pouvons l'ajouter au composant de mise en page racine (`layout.tsx` dans le dossier app).

```tsx
// app/layout.tsx
import Navbar from '@/components/Navbar';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import { Suspense } from 'react';
import './globals.css';

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Tableau de bord d\'administration',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
         <Navbar />
        {children}
      </body>
    </html>
  )
}

```

Créons un lien de connexion dans le composant `Navbar` pour que les utilisateurs puissent s'authentifier.

Dans Navbar, utilisez une fonction de NextAuth pour initier le processus de connexion. Trouvez le texte "sign-in" et implémentez la fonctionnalité pour les vues desktop et mobile.

```tsx
// components/Navbar.tsx

// ...
<Menu.Item>
  {({ active }) => (
    <button
      className={classNames(
        active ? "bg-gray-100" : "",
        "flex w-full px-4 py-2 text-sm text-gray-700"
      )}
      onClick={() => signIn("github")}
    >
      Se connecter
    </button>
  )}
</Menu.Item>
// ...

```

Pour utiliser cette fonction `signIn`, ajoutez au-dessus du composant Navbar :

```tsx
import { signIn, signOut } from "next-auth/react";

```

La sélection de la connexion devrait rediriger vers une page hébergée par GitHub pour que les utilisateurs s'authentifient. Si les utilisateurs sont authentifiés correctement, ils seront redirigés vers la page d'accueil et seront connectés.

Vous pouvez vérifier et voir si un nouvel utilisateur est créé après la connexion en exécutant la commande `npx prisma studio`. Le Prisma Studio vous permet de visualiser et de gérer les données des modèles, y compris les comptes, les sessions et les utilisateurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-11-at-4.22.30-PM.png)
_Prisma Studio_

## Comment afficher les informations du compte

L'étape suivante consiste à afficher les informations du compte GitHub, comme l'email et l'image de l'avatar, à la place de l'avatar factice. Pour cela, nous avons besoin d'un composant client en raison de certaines bibliothèques, telles que les composants headless UI.

Créez un nouveau composant dans le dossier **components** appelé **Nav.tsx** :

```tsx
// components/Nav.tsx
import Navbar from "@/components/Navbar";
import { authOptions } from "@/pages/api/auth/[...nextauth]";
import { getServerSession } from "next-auth";

export default async function Nav() {
  const session = await getServerSession(authOptions);

  return <Navbar user={session?.user} />;
}

```

Ici, nous récupérons la session actuelle de l'utilisateur connecté et la passons au composant Navbar sur la prop user.

Dans `Navbar`, nous devons recevoir cette prop et déclarer son type en utilisant le type `Props`.

```tsx
// components/Navbar.tsx
import { Session } from "next-auth";

type Props = {
  user: Session["user"];
};

export default function Navbar({ user }: Props) {
// ...

```

Puisque `Nav` enveloppe maintenant notre composant `Navbar`, remplacez `Navbar` par `Nav` dans votre fichier **layout.tsx** :

```tsx
// app/layout.tsx
import Nav from '@/components/Nav';

// ...
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Nav />
        {children}
      </body>
    </html>
  )
}

```

Enregistrez tous les fichiers et connectez la session dans `Nav`. Rafraîchissez l'application et vérifiez les logs pour les données utilisateur. La connexion de l'utilisateur dans la barre de navigation devrait afficher les données utilisateur dans la console du navigateur.

Pour afficher les données de l'utilisateur connecté au lieu de l'avatar par défaut, utilisez une instruction ternaire dans la barre de navigation.

Si `user.image` est présent, retournez une image de "next/image" avec les classes et attributs appropriés.

Définissez également la source sur `user.image`, la hauteur et la largeur sur 32, et le texte alternatif sur `user.name` ou "avatar" comme solution de repli.

Si l'image n'est pas présente ou si l'utilisateur n'est pas authentifié, utilisez le composant `Avvvatars` avec la valeur "U".

```tsx
// components/Navbar.tsx

// ...
<Menu.Button className="flex rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-offset-2">
  <span className="sr-only">Ouvrir le menu utilisateur</span>
  {user?.image ? (
    <Image
      className="h-8 w-8 rounded-full"
      src={user.image}
      height={32}
      width={32}
      alt={user?.name ?? 'avatar'}
    />
  ) : (
    <Avvvatars value={'U'} />
  )}
</Menu.Button>
// ...

```

Pour le composant des éléments de menu, ajoutez l'utilisateur à l'instruction ternaire, permettant l'affichage du bouton "déconnexion". Implémentez un événement onClick pour appeler 'sign out' lorsqu'il est cliqué.

```tsx
// components/Navbar.tsx

// ...
<Menu.Items className="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
  {user ? (
    <Menu.Item>
      {({ active }) => (
        <button
          className={classNames(
            active ? "bg-gray-100" : "",
            "flex w-full px-4 py-2 text-sm text-gray-700",
          )}
          onClick={() => signOut()}
        >
          Se déconnecter
        </button>
      )}
    </Menu.Item>
  ) : (
// ...

```

Cette approche démontre la récupération de données sur le serveur et leur passage à un composant client. C'est un moyen efficace de gérer les données utilisateur et de les afficher dans votre application.

## \ud83d\udee1\ufe0f Comment protéger les routes

La dernière étape de l'authentification consiste à protéger les routes. Nous avons un tableau de bord, une page utilisateurs (qui est la page d'accueil), et une page d'analytique. La page d'analytique, que nous allons construire, doit être protégée par mot de passe afin que seuls les utilisateurs authentifiés puissent y accéder.

Pour protéger cette route, récupérez les données sur le serveur en utilisant la fonction `getServerSession`. Mais pour protéger la route `/analytics`, vous devrez la créer dans le dossier app. Ajoutez un dossier nommé **analytics** et à l'intérieur, un fichier **page.tsx**.

Nous devons protéger la `AnalyticsPage` en fonction de l'état de la session. Si aucun utilisateur n'est authentifié, nous redirigeons vers la route de connexion, qui est `/api/auth/sign-in`.

```tsx
// app/analytics/page.tsx
import Analytics from "@/components/Analytics";
import { authOptions } from "@/pages/api/auth/[...nextauth]";
import { getServerSession } from "next-auth";
import { redirect } from "next/navigation";

export default async function AnalyticsPage() {
  const session = await getServerSession(authOptions);

  if (!session) {
    redirect("api/auth/signin");
  }

  return <Analytics />;
}

```

Ce modèle de base est essentiel pour protéger le contenu dans un tableau de bord d'administration. Avec l'authentification maintenant couverte, nous pouvons passer à la construction de l'interface utilisateur.

## \ud83d\udcc8 Comment créer la page d'analytique

Nous allons utiliser une bibliothèque appelée Tremor pour construire des graphiques et des tableaux sur la page d'analytique. Tremor nous permet de créer des tableaux de bord rapidement, bien que nous ne sourcerons pas les données du tableau de bord à partir de notre base de données.

Nous utiliserons les composants Grid, Title et Flex pour la mise en page et le style. Nous utiliserons également les composants Metric et Text de Tremor pour afficher les statistiques et les étiquettes dans une grille de cartes.

```tsx
// components/Analytics.tsx
"use client";

import Chart from "@/components/Chart";
import { BarList, Card, Flex, Grid, Metric, Text, Title } from "@tremor/react";

const app = [
  { name: "/shop", value: 789 },
  { name: "/product-features", value: 676 },
  { name: "/about", value: 564 },
  { name: "/login", value: 234 },
  { name: "/downloads", value: 191 },
];

const data = [
  {
    category: "Application mobile",
    stat: "2,543",
    data: app,
  },
];

export default function Analytics() {
  return (
    <main className="p-4 md:p-10 mx-auto max-w-7xl">
      <Grid numItemsSm={2} numItemsLg={3} className="gap-6">
        {data.map((item) => (
          <Card key={item.category}>
            <Title>{item.category}</Title>
            <Flex
              justifyContent="start"
              alignItems="baseline"
              className="space-x-2"
            >
              <Metric>{item.stat}</Metric>
              <Text>Vues totales</Text>
            </Flex>
            <Flex className="mt-6">
              <Text>Pages</Text>
              <Text className="text-right">Vues</Text>
            </Flex>
            <BarList
              data={item.data}
              valueFormatter={(number: number) =>
                Intl.NumberFormat("us").format(number).toString()
              }
              className="mt-2"
            />
          </Card>
        ))}
      </Grid>
      <Chart />
    </main>
  );
}

```

## \ud83d\udcca Comment construire le composant de graphique

Après avoir configuré la grille supérieure avec des graphiques en barres, configurons le graphique en bas en utilisant le composant AreaChart de Tremor.

Le graphique en aire inclura des données sur différents mois, comparant les ventes et les profits.

```tsx
// components/Chart.tsx
"use client";

import { Card, AreaChart, Title, Text } from "@tremor/react";

const data = [
  {
    Month: "Jan 21",
    Sales: 2890,
    Profit: 2400,
  },
  {
    Month: "Feb 21",
    Sales: 1890,
    Profit: 1398,
  },
  {
    Month: "Jan 22",
    Sales: 3890,
    Profit: 2980,
  },
];

export default function Chart() {
  return (
    <Card className="mt-8">
      <Title>Performance</Title>
      <Text>Comparaison entre les ventes et les profits</Text>
      <AreaChart
        className="mt-4 h-80"
        data={data}
        categories={["Sales", "Profit"]}
        index="Month"
        colors={["indigo", "fuchsia"]}
        valueFormatter={(number: number) =>
          `$ ${Intl.NumberFormat("us").format(number).toString()}`
        }
        yAxisWidth={60}
      />
    </Card>
  );
}

```

## \ud83d\udc65 Comment créer le tableau des utilisateurs

Maintenant que nous avons pris en charge notre page d'analytique, abordons le tableau des utilisateurs.

Ce tableau affichera les utilisateurs de notre base de données Postgres. Nous allons récupérer et interroger tous les utilisateurs en utilisant le client Prisma et montrer comment rechercher des utilisateurs par nom ou d'autres champs.

Nous allons commencer par créer un tableau simple avec l'aide des composants Tremor dans le composant `UsersTable`. Si vous êtes familier avec les éléments de tableau HTML, cela devrait vous sembler très familier.

Nous allons créer des lignes pour les valeurs `name`, `email` et `created_at` pour chacun des utilisateurs et afficher ces valeurs dans le corps du tableau :

```tsx
// components/UsersTable.tsx
import { User } from "@prisma/client";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeaderCell,
  TableRow,
} from "@tremor/react";

type Props = {
  users: User[];
};

export default function UsersTable({ users }: Props) {
  return (
    <Table>
      <TableHead>
        <TableRow>
          <TableHeaderCell>Nom</TableHeaderCell>
          <TableHeaderCell>Email</TableHeaderCell>
          <TableHeaderCell>Créé le</TableHeaderCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {users.map((user) => (
          <TableRow key={user.id}>
            <TableCell>{user.name}</TableCell>
            <TableCell>{user.email}</TableCell>
            <TableCell>
              {new Intl.DateTimeFormat("en-US").format(user.createdAt)}
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}

```

## \ud83d\udd0e Comment rechercher des utilisateurs

Pour rendre notre tableau recherchable, nous allons revenir à la page d'accueil et construire l'interface utilisateur de base pour le composant de recherche.

```tsx
// components/Search
export default function Search({ query }: Props) {
  return (
    <div className="relative mt-5 max-w-md">
      <label htmlFor="search" className="sr-only">
        Rechercher
      </label>
      <div className="rounded-md shadow-sm">
        <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
          <SearchIcon className="mr-3 h-4 w-4 text-gray-400" />
        </div>
        <input
          type="text"
          name="search"
          autoComplete="off"
          id="search"
          className="h-10 block w-full rounded-md border border-gray-200 pl-9 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
          placeholder="Rechercher par nom..."
          onChange={(event) => handleSearch(event.target.value)}
          defaultValue={query}
        />
      </div>
    </div>
  );
}

```

Puisque Next.js utilise des composants serveur par défaut, nous pouvons utiliser l'état de l'URL pour initier des requêtes.

Dans une nouvelle fonction appelée `handleSearch`, nous pouvons mettre à jour l'URL en ajoutant un paramètre de requête appelé `q` et définir la requête que l'utilisateur a tapée dans l'entrée comme valeur.

Cela signifie que lorsque l'utilisateur tape dans l'entrée, la requête de recherche sera ajoutée à l'URL.

```tsx
// components/Search.tsx
import { usePathname, useRouter } from "next/navigation";
import { useTransition } from "react";

type Props = {
  query?: string;
};

export default function Search({ query }: Props) {
  const router = useRouter();
  const pathname = usePathname();
  const [isPending, startTransition] = useTransition();

  function handleSearch(value: string) {
    const params = new URLSearchParams(window.location.search);

    if (value) {
      params.set("q", value);
    } else {
      params.delete("q");
    }

    startTransition(() => {
      router.replace(`${pathname}?${params.toString()}`);
    });
  }
// ...

```

De retour dans notre composant serveur, **app.tsx**, nous utiliserons les paramètres de recherche (qui sont fournis en tant que props dans les composants de page) pour interroger notre base de données avec Prisma.

Nous pouvons modifier la méthode `findMany` pour rechercher des utilisateurs selon `name` et `email` en utilisant le filtre "where". Nous pouvons également le faire de manière insensible à la casse en utilisant `mode: insensitive`.

```tsx
// app/page.tsx
// ...
type Props = {
  searchParams: {
    q?: string;
  };
};

export default async function Home({ searchParams }: Props) {
  const query = searchParams.q;
  const users = await prisma.user.findMany({
    where: {
      name: {
        contains: query,
        mode: "insensitive",
      },
      email: {
        contains: query,
        mode: "insensitive",
      },
    },
  });
// ...

```

Enfin, nous utilisons le hook `useTransition` pour changer l'URL de manière performante.

De retour dans le composant `Search`, vous pouvez ajouter un spinner de chargement à la fin de votre entrée pour indiquer à l'utilisateur que nous sommes en train de changer l'URL.

```tsx
// components/Search.tsx
// ...
  {isPending && (
    <div className="absolute right-0 top-0 bottom-0 flex items-center justify-center">
      <RotateCwIcon className="animate-spin -ml-1 mr-3 h-5 w-5 text-gray-700" />
    </div>
  )}
</div>

```

Cette approche démontre le changement d'état de l'URL à chaque frappe de manière performante, surtout importante lors de l'utilisation de composants serveur dans Next.js.

## Conclusion

En conclusion, la construction de ce tableau de bord d'administration couvre de nombreux aspects, de la configuration de l'authentification avec NextAuth et Prisma à la création d'une interface utilisateur conviviale avec Tremor.

Ces outils et techniques offrent une manière complète de créer des tableaux de bord flexibles et visuellement attrayants. N'hésitez pas à utiliser ce tableau de bord d'administration dans vos projets.

Merci d'avoir suivi et j'espère que ce guide a été utile !

##  \ud83c\udfc6 Devenir un développeur React professionnel

Vous cherchez la ressource ultime pour apprendre React de A à Z ?

\u2728 **[Présentation : Le Bootcamp React](https://www.thereactbootcamp.com)**

Le bootcamp propose toutes les ressources pour vous aider à réussir avec React :

* \ud83c\udfac 200+ vidéos approfondies
* \ud83d\udd79\ufe0f 100+ défis pratiques React
* \ud83d\udee0\ufe0f 5+ projets de portfolio impressionnants
* \ud83d\udcc4 10+ fiches de référence React essentielles
* \ud83e\udd7e Un bootcamp Next.js complet
* \ud83d\uddbc\ufe0f Une série complète de vidéos animées

Cliquez ci-dessous pour essayer le Bootcamp React par vous-même.

[![Cliquez pour rejoindre le Bootcamp React](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)  
_Cliquez pour commencer_