---
title: Comment construire une TodoApp en utilisant ReactJS, NextJS et Supabase
subtitle: ''
author: Sharvin Shah
co_authors: []
series: null
date: '2021-12-07T15:48:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-todoapp-using-react-and-supabase
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-04-at-6.06.45-PM-1.png
tags:
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Comment construire une TodoApp en utilisant ReactJS, NextJS et Supabase
seo_desc: 'Hello folks, welcome to this tutorial. Today we''re going to build a production-ready
  Todo application with React, Next, and Supabase.

  Before we begin, you should be familiar with the basics of React.js and Next.js
  to get the most out of this guide.

  I...'
---

Bonjour à tous, bienvenue dans ce tutoriel. Aujourd'hui, nous allons construire une application Todo prête pour la production avec React, Next et Supabase.

Avant de commencer, vous devriez être familier avec les bases de **React.js** et **Next.js** pour tirer le meilleur parti de ce guide.

Si ce n'est pas le cas et que vous avez besoin de vous rafraîchir la mémoire, je vous recommande de consulter la [documentation ReactJS](https://reactjs.org/docs/getting-started.html) et la [documentation NextJS](https://nextjs.org/docs/getting-started).

## **Voici ce que nous allons construire**

Nous allons construire une application Todo qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-04-at-5.49.41-PM.png align="left")

## Et voici la technologie que nous allons utiliser :

1. [ReactJS](https://reactjs.org/docs/getting-started.html) : une bibliothèque JavaScript pour construire des interfaces utilisateur. Elle est déclarative et basée sur les composants.

2. [NextJS](https://nextjs.org/docs/getting-started) : un framework basé sur React qui nous permet de rendre les données côté serveur. Il aide Google à explorer l'application, ce qui entraîne des avantages en matière de SEO.

3. [Supabase](https://supabase.io/docs) : fournit l'authentification, la base de données et le stockage que nous allons utiliser dans notre application.

4. [Chakra UI](https://chakra-ui.com/docs/getting-started) : est une bibliothèque de composants simple, modulaire et accessible qui nous fournira les blocs de construction pour construire l'application.

5. [Vercel](https://vercel.com/docs) : hébergera notre application. Il est bien dimensionné, sans aucune configuration, et le déploiement est instantané.

## Pourquoi utiliser Supabase ?

Selon la documentation de Supabase, Supabase est *"une alternative open source à Firebase".*

Cependant, Supabase n'est pas complètement similaire à Firebase. La différence entre les deux est que Supabase utilise **Postgres** (une base de données relationnelle) pour stocker les données, tandis que Firebase utilise le mécanisme **NoSQL** pour stocker les données.

Personnellement, j'utilise généralement Postgres comme base de données principale et je l'ai trouvé bien dimensionné.

Supabase fournit les services suivants :

1. **Authentification**

2. **Base de données Postgres**

3. **Serveur rest en temps réel**

4. **Sécurité au niveau des lignes**

5. **Bucket de stockage**

Maintenant, comprenons comment cela fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-17-at-1.12.37-PM.png align="left")

*Diagramme architectural de la documentation Supabase*

D'accord, que se passe-t-il ici ?

Comme vous le savez déjà, **Supabase** utilise Postgres comme base de données – mais il possède également de nombreux autres composants qui fournissent différents services.

L'un de mes préférés est **Realtime**. Supabase utilise le serveur Elixir pour établir une connexion web socket afin d'écouter les événements d'insertion, de mise à jour et de suppression.

**PostgRest** convertit directement la base de données Postgres en une API Rest.

**GoTrue** est une API pour gérer les utilisateurs et émettre des jetons SWT.

**Postgres-Meta** est une API Restful pour gérer la base de données Postgres.

**Kong** est une passerelle API.

> **Note :** Toutes ces définitions sont tirées de la documentation de supabase. Pour en savoir plus sur le fonctionnement de Supabase, vous pouvez consulter leur [documentation](https://supabase.io/docs).

Et avec cela, nous sommes prêts à plonger dans notre projet. Voici ce que nous allons couvrir :

## **Table des matières**

1. [Comment configurer les tables Supabase, l'authentification et le stockage](#heading-comment-configurer-les-tables-supabase-l-authentification-et-le-stockage)

2. [Comment implémenter la connexion en utilisant Supabase](#heading-comment-implémenter-la-connexion-en-utilisant-supabase)

3. [Comment afficher tous les todos, ajouter de nouveaux todos, et mettre à jour et supprimer des todos](#heading-comment-afficher-tous-les-todos-ajouter-de-nouveaux-todos-et-mettre-à-jour-et-supprimer-des-todos)

4. [Comment mettre à jour les détails du profil et l'avatar](#heading-comment-mettre-à-jour-les-détails-du-profil-et-les-avatars)

5. [Comment déployer l'application sur Vercel et configurer l'authentification Supabase](#heading-comment-déployer-l-application-sur-vercel-et-configurer-l-authentification-supabase)

Je vais diviser ce tutoriel en quatre sections distinctes. Au début de chaque section, vous trouverez un commit Git qui contient le code développé dans cette section. De plus, si vous souhaitez voir le code complet, il est disponible dans ce [dépôt](https://github.com/Sharvin26/TodoApp-supabase).

## Comment configurer les tables Supabase, l'authentification et le stockage

Dans cette section, nous allons implémenter les fonctionnalités suivantes :

1. **Créer un projet Supabase.**

2. **Configurer l'authentification pour les utilisateurs et les politiques.**

3. **Configurer la base de données et les politiques pour les utilisateurs et les todos.**

Pour créer un projet Supabase, visitez le lien suivant [lien](https://supabase.io/). Cliquez sur le bouton "Start your project" et connectez-vous via GitHub (au moment de la rédaction de cet article, ils ne prennent en charge que GitHub comme fournisseur d'authentification).

Une fois que vous avez créé votre compte, cliquez sur New project où il vous demandera l'organisation. Par défaut, Supabase créera un compte organisationnel pour vous avec votre nom d'utilisateur. J'utiliserai celui par défaut, mais vous pouvez créer le vôtre pour ce projet.

Une fois l'organisation sélectionnée, Supabase vous demandera le nom du projet, le mot de passe de la base de données et la région.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-17-at-12.34.24-PM.png align="left")

*Créer un projet Supabase*

Remplissez ce formulaire et cliquez sur le bouton **Créer un nouveau projet**.

Supabase commencera à configurer l'application. Cela peut prendre quelques minutes.

Dans la section Clés API du projet, vous verrez deux types de clés :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-17-at-12.48.10-PM.png align="left")

*Clés API du projet Supabase*

**anon** est une clé API publique et peut être utilisée côté client.

**service\_role** est une clé API privée et vous l'utilisez uniquement côté serveur. Cette clé peut contourner la sécurité au niveau des lignes et muter les données.

### Qu'est-ce que la sécurité au niveau des lignes dans Supabase ?

Vous vous demandez peut-être – qu'est-ce que la sécurité au niveau des lignes et pourquoi est-elle si importante ?

Eh bien, Supabase dispose d'une bibliothèque cliente pour accéder aux données directement depuis le navigateur et pour cela, nous utilisons la clé **anon**. Comme la clé anon est côté client, n'importe qui peut avoir accès à la clé via l'onglet réseau.

Mais il y a certains cas où nous ne voulons pas que les données soient directement accessibles par le navigateur en utilisant la bibliothèque cliente.

Dans ces cas, nous pouvons configurer la sécurité au niveau des lignes, qui spécifie quelles données peuvent être accessibles en utilisant la clé anon.

Pour en savoir plus sur la sécurité au niveau des lignes, lisez cette [documentation](https://supabase.io/docs/learn/auth-deep-dive/auth-row-level-security).

En revenant à l'application, une fois le projet configuré, vous obtiendrez le message suivant "**Bienvenue dans votre nouveau projet**."

### Comment créer des tables dans la base de données

Maintenant, créons un script pour créer des tables dans notre base de données.

Allez dans la section SQL depuis la barre latérale et cliquez sur Nouvelle requête.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-17-at-12.59.51-PM.png align="left")

*Section SQL du panneau Supabase*

Cliquez sur Nouvelle requête et copiez-collez le code suivant :

```sql
create table profiles (
  id uuid references auth.users not null,
  username text unique,
  avatarUrl text,
  website text,
  bio text,
  joinedAt timestamp with time zone default timezone('utc'::text, now()) not null,

  primary key (id),
  unique(username)
);

alter table profiles enable row level security;

create policy "Profiles are viewable by user only."
  on profiles for select
  using ( auth.uid() = id );

create policy "Users can insert their own profile."
  on profiles for insert
  with check ( auth.uid() = id );

create policy "Users can update own profile."
  on profiles for update
  using ( auth.uid() = id );

begin;
  drop publication if exists supabase_realtime;
  create publication supabase_realtime;
commit;
alter publication supabase_realtime add table profiles;

-- Set up Storage!
insert into storage.buckets (id, name)
values ('avatars', 'avatars');

create policy "Avatar images are publicly accessible."
  on storage.objects for select
  using ( bucket_id = 'avatars');

create policy "Anyone can upload an avatar."
  on storage.objects for insert
  with check ( bucket_id = 'avatars' );

create policy "Anyone can update an avatar."
  on storage.objects for update
  with check ( bucket_id = 'avatars' );
```

Comprenons ce script **Profiles** pièce par pièce.

Tout d'abord, nous créons une table profiles qui se rapporte aux utilisateurs dans notre TodoApp. Pour comprendre comment configurer unique dans une table, nous avons configuré username comme une contrainte unique et primary key comme id.

Après cela, nous configurons la sécurité au niveau des lignes et attribuons des politiques de sorte que chaque individu ne puisse accéder qu'à ses propres données.

Après cela, nous activons le temps réel pour notre base de données. Realtime donne un événement chaque fois qu'il y a des changements dans la ligne, et nous pouvons mettre à jour l'UI en conséquence.

Maintenant, cliquez sur le bouton **RUN** dans le coin droit et vous obtiendrez le message suivant :

```shell
Success. No rows returned
```

Maintenant, créons notre table todos. Pour générer la table, cliquez sur le bouton **Nouvelle requête** et copiez-collez le script suivant :

```sql
create table todos (
  id bigint generated by default as identity primary key,
  user_id uuid references auth.users not null,
  title text,
  description text,
  "isComplete" boolean default false,
  insertedAt timestamp with time zone default timezone('utc'::text, now()) not null
);

alter table todos enable row level security;

create policy "Individuals can create todos." on todos for
    insert with check (auth.uid() = user_id);

create policy "Individuals can view their own todos. " on todos for
    select using (auth.uid() = user_id);

create policy "Individuals can update their own todos." on todos for
    update using (auth.uid() = user_id);

create policy "Individuals can delete their own todos." on todos for
    delete using (auth.uid() = user_id);
```

Maintenant, cliquez sur le bouton **RUN** dans le coin droit, et vous obtiendrez le message suivant :

```shell
Success. No rows returned
```

Pour confirmer que nos tables sont générées, allez dans la section éditeur de table depuis la barre latérale.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-17-at-1.28.59-PM.png align="left")

*Section Éditeur de table du panneau Supabase*

À l'intérieur de l'éditeur de table, vous trouverez nos tables générées avec succès.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-17-at-1.33.43-PM.png align="left")

*Barre latérale des tables Supabase*

Comme vous pouvez le voir dans le script Todos ci-dessus, nous n'avons pas activé le temps réel. Pour activer un serveur en temps réel, nous devons aller dans la section **Base de données > Réplication**.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-17-at-1.36.33-PM.png align="left")

*Section Base de données du panneau Supabase*

Ici, vous verrez la vue suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-17-at-1.38.08-PM.png align="left")

*Section Réplication de la base de données Supabase*

Cliquez sur le bouton **1 table** sous source, puis basculez l'interrupteur pour les todos. Cela activera un serveur en temps réel pour nos todos également.

Maintenant, supposons que nous voulons désactiver la sécurité au niveau des lignes pour les todos **(notez que cela n'est pas conseillé)**, mais juste pour le cadre de cet article pour comprendre comment faire, nous allons la désactiver.

Allez dans la section Authentification et, à l'intérieur, allez dans les Politiques.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-17-at-1.41.50-PM.png align="left")

*Section Authentification du panneau Supabase*

Maintenant, vous verrez la section todos avec RLS activé écrit dans la boîte verte. Cliquez sur l'option Désactiver RLS en haut à droite de cette boîte. Cela désactivera la sécurité au niveau des lignes pour notre application.

## Comment implémenter la connexion en utilisant Supabase

Le **code** de cette section est disponible sous ce **commit** si vous avez besoin de vous y référer à l'avenir.

%[https://github.com/Sharvin26/TodoApp-supabase/tree/b253c904f2f39ac80808620cf51c9584bfa90f4d]

Tout d'abord, créons notre application en utilisant la commande suivante :

```sh
npx create-next-app todo_app
```

Il est temps d'installer nos dépendances et d'avoir une configuration de base en place.

### Comment installer Chakra UI

```sh
npm i @chakra-ui/react @emotion/react@^11 @emotion/styled@^11 framer-motion@^4
```

**Note :** Si vous utilisez zsh, vous devrez ajouter le caractère d'échappement () après @ comme suit :

```sh
npm i @chakra-ui/react @emotion/react@\^11 @emotion/styled@\^11 framer-motion@\^4
```

Maintenant, nettoyons notre code en supprimant le code qui n'est pas requis et en configurant ChakraUI dans notre application.

Selon la documentation de Chakra, nous devons envelopper `<Component />` avec `ChakraProvider` dans le fichier `pages/_app.js`. Allez dans `_app.js` et copiez-collez le code suivant :

```jsx
import { ChakraProvider, extendTheme } from "@chakra-ui/react";
import customTheme from "../lib/theme";

function MyApp({ Component, pageProps }) {
  return (
    <ChakraProvider theme={customTheme}>
      <Component {...pageProps} />
    </ChakraProvider>
  );
}

export default MyApp;
```

Créons un répertoire sous notre répertoire racine et nommons-le **lib**. Sous ce répertoire, créez un fichier nommé `theme.js`.

Copiez-collez le code suivant à l'intérieur de ce fichier :

```js
import { extendTheme } from "@chakra-ui/react"

const config = {
  initialColorMode: "light",
  useSystemColorMode: false,
}

const theme = extendTheme({ config })

export default theme
```

Maintenant, sous le répertoire **pages**, créez un fichier `_document.js` et copiez-collez le code suivant :

```jsx
import { ColorModeScript } from "@chakra-ui/react"
import NextDocument, { Html, Head, Main, NextScript } from "next/document"
import theme from "../lib/theme"

export default class Document extends NextDocument {
  render() {
    return (
      <Html lang="en">
        <Head />
        <body>
          {/* 👇 Voici le script */}
          <ColorModeScript initialColorMode={theme.config.initialColorMode} />
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}
```

En créant `_document.js` et `theme.js`, nous avons simplement défini notre couleur par défaut comme étant **light**.

À partir de la version `1.6.12` de ChakraUI, elle définit la couleur choisie par le système par défaut. Ainsi, pour certains utilisateurs qui ont le mode sombre activé pour le navigateur, l'application aura un thème de couleur sombre. Le mode sombre est bien, mais pour commencer, nous voulons uniquement que la couleur soit claire.

Allez dans `index.js` et copiez-collez le code suivant :

```jsx
import { Box } from "@chakra-ui/react";
import Head from "next/head";

const Home = () => {
  return (
    <div>
      <Head>
        <title>TodoApp</title>
        <meta
          name="description"
          content="Awesome todoapp to store your awesome todos"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <Box>Hello world</Box>
      </main>
    </div>
  );
};

export default Home;
```

### Comment installer la bibliothèque cliente Supabase

```sh
npm i @supabase/supabase-js
```

Sous le répertoire **lib**, créez un fichier nommé `client.js`.

Sous ce fichier, copiez-collez le code suivant :

```js
import { createClient } from "@supabase/supabase-js";

const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL;
const SUPBASE_ANON_KEY = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

const client = createClient(SUPABASE_URL, SUPBASE_ANON_KEY);

export { client as supabaseClient };
```

Ici, nous créons simplement un **client Supabase** qui sera utilisé dans tout le projet.

Maintenant, sous le répertoire racine, créez un fichier `.env.local` et copiez-collez la partie suivante avec l'URL Supabase et la clé anon :

```shell
NEXT_PUBLIC_SUPABASE_URL=#Add_your_supabase_url 
NEXT_PUBLIC_SUPABASE_ANON_KEY=#Add_your_supabase_key
```

Vous pouvez trouver l'URL Supabase et la clé anon sous la section **Paramètres > API**.

Sous les clés API du projet se trouve la clé **anon** et sous Config se trouve l'**URL**.

Avec cela, notre client Supabase est configuré et prêt à être utilisé.

Exécutons notre application en utilisant la commande suivante :

```shell
npm run dev
```

Vous obtiendrez le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-04-at-10.03.31-PM-2.png align="left")

*Écran d'accueil de l'application Todo*

Maintenant, sous le répertoire **pages**, créez un fichier nommé `signin.js` et copiez-collez le code suivant :

```jsx
import {
  Alert,
  AlertIcon,
  Box,
  Button,
  chakra,
  FormControl,
  FormLabel,
  Heading,
  Input,
  Stack,
  Text,
} from "@chakra-ui/react";
import { useState } from "react";
import { supabaseClient } from "../lib/client";

const SignIn = () => {
  const [email, setEmail] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [error, setError] = useState(null);

  const submitHandler = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    setError(null);
    try {
      const { error } = await supabaseClient.auth.signIn({
        email,
      });
      if (error) {
        setError(error.message);
      } else {
        setIsSubmitted(true);
      }
    } catch (error) {
      setError(error.message);
    } finally {
      setIsLoading(false);
    }
  };

  const changeHandler = (event) => {
    setEmail(event.target.value);
  };

  return (
    <Box minH="100vh" py="12" px={{ base: "4", lg: "8" }} bg="gray.50">
      <Box maxW="md" mx="auto">
        <Heading textAlign="center" m="6">
          Bienvenue dans l'application Todo
        </Heading>
        {error && (
          <Alert status="error" mb="6">
            <AlertIcon />
            <Text textAlign="center">{error}</Text>
          </Alert>
        )}
        <Box
          py="8"
          px={{ base: "4", md: "10" }}
          shadow="base"
          rounded={{ sm: "lg" }}
          bg="white"
        >
          {isSubmitted ? (
            <Heading size="md" textAlign="center" color="gray.600">
              Veuillez vérifier {email} pour le lien de connexion
            </Heading>
          ) : (
            <chakra.form onSubmit={submitHandler}>
              <Stack spacing="6">
                <FormControl id="email">
                  <FormLabel>Adresse e-mail</FormLabel>
                  <Input
                    name="email"
                    type="email"
                    autoComplete="email"
                    required
                    value={email}
                    onChange={changeHandler}
                  />
                </FormControl>
                <Button
                  type="submit"
                  colorScheme="blue"
                  size="lg"
                  fontSize="md"
                  isLoading={isLoading}
                >
                  Se connecter
                </Button>
              </Stack>
            </chakra.form>
          )}
        </Box>
      </Box>
    </Box>
  );
};

export default SignIn;
```

Ici, nous avons créé un formulaire et utilisé une **méthode d'authentification supabase** pour connecter l'utilisateur.

> **Note :** Dans la méthode `supabaseClient.auth.signIn`, lorsque vous ne passez pas de mot de passe, elle considère la méthode d'authentification comme le **lien magique**.

Maintenant, allez dans `_app.js` et copiez-collez le code suivant :

```jsx
import { ChakraProvider } from "@chakra-ui/react";
import { useRouter } from "next/router";
import { useEffect } from "react";
import { supabaseClient } from "../lib/client";
import customTheme from "../lib/theme";

function MyApp({ Component, pageProps }) {
  const router = useRouter();
  const user = supabaseClient.auth.user();

  useEffect(() => {
    const { data: authListener } = supabaseClient.auth.onAuthStateChange(
      (event, session) => {
        handleAuthSession(event, session);
        if (event === "SIGNED_IN") {
          const signedInUser = supabaseClient.auth.user();
          const userId = signedInUser.id;
          supabaseClient
            .from("profiles")
            .upsert({ id: userId })
            .then((_data, error) => {
              if (!error) {
                router.push("/");
              }
            });
        }
        if (event === "SIGNED_OUT") {
          router.push("/signin");
        }
      }
    );

    return () => {
      authListener.unsubscribe();
    };
  }, [router]);

  useEffect(() => {
    if (user) {
      if (router.pathname === "/signin") {
        router.push("/");
      }
    }
  }, [router.pathname, user, router]);

  const handleAuthSession = async (event, session) => {
    await fetch("/api/auth", {
      method: "POST",
      headers: new Headers({ "Content-Type": "application/json" }),
      credentials: "same-origin",
      body: JSON.stringify({ event, session }),
    });
  };

  return (
    <ChakraProvider theme={customTheme}>
      <Component {...pageProps} />
    </ChakraProvider>
  );
}

export default MyApp;
```

Maintenant, à l'intérieur du répertoire **API**, supprimez le fichier `hello.js` et créez un nouveau fichier appelé `auth.js`. Copiez-collez le code suivant dans ce nouveau fichier :

```js
import { supabaseClient } from "../../lib/client";

export default function handler(req, res) {
  supabaseClient.auth.api.setAuthCookie(req, res);
}
```

Le code sous `_app.js` est crucial pour l'authentification lorsque l'utilisateur clique sur le lien magique.

Supabase fournit une méthode d'écoute sous le capot `auth.onAuthStateChange` qui donne deux événements `SIGNED_IN` et `SIGNED_OUT`.

Nous utilisons l'événement `SIGNED_IN` pour définir un cookie en appelant `/api/auth` qui utilise une autre méthode exposée par supabase. Cette méthode `auth.api.setAuthCookie` est utile pour définir des cookies via le serveur. Une fois l'utilisateur authentifié, nous le redirigeons vers la page `/` où se trouvent tous les todos.

Maintenant, redémarrons notre serveur en utilisant `npm run dev` puis allons sur `http://localhost:3000/signin`. Vous verrez l'interface utilisateur suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-04-at-10.50.26-PM.png align="left")

*Page de connexion Todo*

Ajoutez votre email et cliquez sur le bouton de soumission. Allez dans l'email et cliquez sur vérifier, et vous serez redirigé vers la page `/`.

## Comment afficher tous les todos, ajouter de nouveaux todos, et mettre à jour et supprimer des todos

Le **code** est disponible sous ce **commit** si vous avez besoin de vous y référer à l'avenir.

%[https://github.com/Sharvin26/TodoApp-supabase/tree/c2d1361b461d301549a813fda350c69a3e23e579]

Avant d'implémenter les opérations CRUD de Todo, implémentons la fonctionnalité de déconnexion. Allez dans `index.js` et remplacez le code existant par le code suivant :

```jsx
import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect } from "react";
import Navbar from "../components/Navbar";
import { supabaseClient } from "../lib/client";

const Home = () => {
  const router = useRouter();
  const user = supabaseClient.auth.user();

  useEffect(() => {
    if (!user) {
      router.push("/signin");
    }
  }, [user, router]);

  return (
    <div>
      <Head>
        <title>TodoApp</title>
        <meta
          name="description"
          content="Awesome todoapp to store your awesome todos"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <Navbar />
      </main>
    </div>
  );
};

export default Home;
```

Créez un répertoire **component** sous le répertoire racine, et à l'intérieur du répertoire **component**, créez un fichier nommé `Navbar.js`. Copiez-collez le contenu suivant sous ce fichier :

```jsx
import { Box, Button, ButtonGroup, Flex, Heading } from "@chakra-ui/react";
import NavLink from "next/link";
import { useRouter } from "next/router";
import { useState } from "react";
import { supabaseClient } from "../lib/client";

const Navbar = () => {
  const router = useRouter();
  const [isLogoutLoading, setIsLogoutLoading] = useState(false);

  const logoutHandler = async () => {
    try {
      setIsLogoutLoading(true);
      await supabaseClient.auth.signOut();
      router.push("/signin");
    } catch (error) {
      router.push("/signin");
    } finally {
      setIsLogoutLoading(false);
    }
  };

  return (
    <Box height="100%" p="5" bg="gray.100">
      <Box maxW="6xl" mx="auto">
        <Flex
          as="nav"
          aria-label="Site navigation"
          align="center"
          justify="space-between"
        >
          <Heading mr="4">TodoApp</Heading>
          <Box>
            <NavLink href="/profile">Profile</NavLink>
            <ButtonGroup spacing="4" ml="6">
              <Button colorScheme="blue">Add Todo</Button>
              <Button
                colorScheme="red"
                onClick={logoutHandler}
                isLoading={isLogoutLoading}
              >
                Logout
              </Button>
            </ButtonGroup>
          </Box>
        </Flex>
      </Box>
    </Box>
  );
};

export default Navbar;
```

Nous avons créé un composant de barre de navigation avec un lien Profile, un bouton Add Todo et un bouton Logout.

Le `logoutHandler` utilise une méthode Supabase appelée `signOut` pour effacer la session et nous déconnecter de l'application.

Allez sur http://localhost:3000 et cliquez sur le bouton **Logout**.

Le cookie sera effacé du navigateur, et l'utilisateur sera redirigé vers la page de **connexion**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-05-at-11.54.09-AM.png align="left")

*Page d'accueil de TodoApp*

### Comment ajouter un Todo

Allez dans `Navbar.js` et copiez-collez le code suivant :

```jsx
import { Box, Button, ButtonGroup, Flex, Heading } from "@chakra-ui/react";
import NavLink from "next/link";
import { useRouter } from "next/router";
import { useState } from "react";
import { supabaseClient } from "../lib/client";

const Navbar = ({ onOpen }) => {
  const router = useRouter();
  const [isLogoutLoading, setIsLogoutLoading] = useState(false);

  const logoutHandler = async () => {
    try {
      setIsLogoutLoading(true);
      await supabaseClient.auth.signOut();
      router.push("/signin");
    } catch (error) {
      router.push("/signin");
    } finally {
      setIsLogoutLoading(false);
    }
  };

  return (
    <Box height="100%" p="5" bg="gray.100">
      <Box maxW="6xl" mx="auto">
        <Flex
          as="nav"
          aria-label="Site navigation"
          align="center"
          justify="space-between"
        >
          <Heading mr="4">TodoApp</Heading>
          <Box>
            <NavLink href="/profile">Profile</NavLink>
            <ButtonGroup spacing="4" ml="6">
              <Button colorScheme="blue" onClick={onOpen}>
                Add Todo
              </Button>
              <Button
                colorScheme="red"
                onClick={logoutHandler}
                isLoading={isLogoutLoading}
              >
                Logout
              </Button>
            </ButtonGroup>
          </Box>
        </Flex>
      </Box>
    </Box>
  );
};

export default Navbar;
```

Ici, nous avons simplement assigné un gestionnaire onClick à notre bouton Add Todo qui ouvrira une modale pour ajouter un todo.

Maintenant, créez un fichier nommé `ManageTodo.js` sous le répertoire **components** et copiez-collez le code suivant :

```jsx
import {
  Alert,
  AlertIcon,
  Button,
  ButtonGroup,
  FormControl,
  FormHelperText,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  Switch,
  Text,
  Textarea,
} from "@chakra-ui/react";
import { useState } from "react";
import { supabaseClient } from "../lib/client";

const ManageTodo = ({ isOpen, onClose, initialRef }) => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [isComplete, setIsComplete] = useState(false);
  const [isLoading, setIsLoading] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const submitHandler = async (event) => {
    event.preventDefault();
    setErrorMessage("");
    if (description.length <= 10) {
      setErrorMessage("Description must have more than 10 characters");
      return;
    }
    setIsLoading(true);
    const user = supabaseClient.auth.user();
    const { error } = await supabaseClient
      .from("todos")
      .insert([{ title, description, isComplete, user_id: user.id }]);
    setIsLoading(false);
    if (error) {
      setErrorMessage(error.message);
    } else {
      closeHandler();
    }
  };

  const closeHandler = () => {
    setTitle("");
    setDescription("");
    setIsComplete(false);
    onClose();
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      isCentered
      initialFocusRef={initialRef}
    >
      <ModalOverlay />
      <ModalContent>
        <form onSubmit={submitHandler}>
          <ModalHeader>Add Todo</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            {errorMessage && (
              <Alert status="error" borderRadius="lg" mb="6">
                <AlertIcon />
                <Text textAlign="center">{errorMessage}</Text>
              </Alert>
            )}
            <FormControl isRequired={true}>
              <FormLabel>Title</FormLabel>
              <Input
                ref={initialRef}
                placeholder="Add your title here"
                onChange={(event) => setTitle(event.target.value)}
                value={title}
              />
            </FormControl>

            <FormControl mt={4} isRequired={true}>
              <FormLabel>Description</FormLabel>
              <Textarea
                placeholder="Add your description here"
                onChange={(event) => setDescription(event.target.value)}
                value={description}
              />
              <FormHelperText>
                Description must have more than 10 characters.
              </FormHelperText>
            </FormControl>

            <FormControl mt={4}>
              <FormLabel>Is Completed?</FormLabel>
              <Switch
                value={isComplete}
                id="is-completed"
                onChange={(event) => setIsComplete(!isComplete)}
              />
            </FormControl>
          </ModalBody>

          <ModalFooter>
            <ButtonGroup spacing="3">
              <Button
                onClick={closeHandler}
                colorScheme="red"
                type="reset"
                isDisabled={isLoading}
              >
                Cancel
              </Button>
              <Button colorScheme="blue" type="submit" isLoading={isLoading}>
                Save
              </Button>
            </ButtonGroup>
          </ModalFooter>
        </form>
      </ModalContent>
    </Modal>
  );
};

export default ManageTodo;
```

Cette partie sera responsable de l'ajout et de la mise à jour des todos. Ici, nous avons créé une modale avec un formulaire et 3 éléments de contrôle de formulaire.

Une fois le formulaire soumis, nous appelons un serveur supabase avec le code suivant :

```js
const { error } = await supabaseClient
      .from("todos")
      .insert([{ title, description, isComplete, user_id: user.id }]);
```

Cela insère simplement un nouveau todo dans notre table supabase.

Maintenant, allons dans **pages > index.js** et copiez-collez le code suivant :

```jsx
import { useDisclosure } from "@chakra-ui/hooks";
import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect, useRef } from "react";
import ManageTodo from "../components/ManageTodo";
import Navbar from "../components/Navbar";
import { supabaseClient } from "../lib/client";

const Home = () => {
  const initialRef = useRef();
  const { isOpen, onOpen, onClose } = useDisclosure();

  const router = useRouter();
  const user = supabaseClient.auth.user();

  useEffect(() => {
    if (!user) {
      router.push("/signin");
    }
  }, [user, router]);

  return (
    <div>
      <Head>
        <title>TodoApp</title>
        <meta
          name="description"
          content="Awesome todoapp to store your awesome todos"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <Navbar onOpen={onOpen} />
        <ManageTodo isOpen={isOpen} onClose={onClose} initialRef={initialRef} />
      </main>
    </div>
  );
};

export default Home;
```

Ici, nous utilisons le hook `useDisclosure` de Chakra pour maintenir l'état de la modale. En outre, vous verrez que nous avons passé `onOpen` à la Navbar et ajouté le composant `ManageTodo`.

Maintenant, allez sur `http://localhost:3000` et cliquez sur le bouton **Add Todo**. Vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-at-7.24.27-PM.png align="left")

*Modale Add Todo*

Remplissez le formulaire, cliquez sur sauvegarder, puis allez dans la table todos de Supabase. Vous trouverez qu'un nouveau todo a été ajouté à notre table.

> **Note :** Supabase nécessite parfois un rafraîchissement manuel lorsqu'un nouvel enregistrement est ajouté.

### Comment obtenir tous les Todos

Nos todos sont donc ajoutés avec succès. Maintenant, travaillons sur l'obtention de tous les todos d'une table Supabase.

Sous le répertoire **components**, créez un fichier nommé `SingleTodo.js` et copiez-collez le code suivant :

```jsx
import { Box, Divider, Heading, Text, Tag } from "@chakra-ui/react";

const SingleTodo = ({ todo }) => {
  const getDateInMonthDayYear = (date) => {
    const d = new Date(date);
    const options = {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
    };
    const n = d.toLocaleDateString("en-US", options);
    const replase = n.replace(new RegExp(",", "g"), " ");
    return replase;
  };

  return (
    <Box
      position="relative"
      maxW="sm"
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
      p="4"
    >
      <Heading size="md" mt="3">{todo.title}</Heading>
      <Tag
        position="absolute"
        top="3"
        right="2"
        bg={todo.isComplete ? "green.500" : "yellow.400"}
        borderRadius="3xl"
        size="sm"
      />
      <Text color="gray.400" mt="1" fontSize="sm">
        {getDateInMonthDayYear(todo.insertedat)}
      </Text>
      <Divider my="4" />
      <Text noOfLines={[1, 2, 3]} color="gray.800">
        {todo.description}
      </Text>
    </Box>
  );
};

export default SingleTodo;
```

Ceci est simplement du code UI avec une fonction utilitaire convertissant la date en format lisible par l'homme.

Allez dans `index.js` et remplacez l'ancien code par le code suivant :

```jsx
import { useDisclosure } from "@chakra-ui/hooks";
import { Box, SimpleGrid, Text, HStack, Tag } from "@chakra-ui/react";
import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect, useRef, useState } from "react";
import ManageTodo from "../components/ManageTodo";
import Navbar from "../components/Navbar";
import SingleTodo from "../components/SingleTodo";
import { supabaseClient } from "../lib/client";

const Home = () => {
  const initialRef = useRef();
  const [todos, setTodos] = useState([]);

  const router = useRouter();
  const { isOpen, onOpen, onClose } = useDisclosure();
  const user = supabaseClient.auth.user();

  useEffect(() => {
    if (!user) {
      router.push("/signin");
    }
  }, [user, router]);

  useEffect(() => {
    if (user) {
      supabaseClient
        .from("todos")
        .select("*")
        .eq("user_id", user?.id)
        .order("id", { ascending: false })
        .then(({ data, error }) => {
          if (!error) {
            setTodos(data);
          }
        });
    }
  }, [user]);

  useEffect(() => {
    const todoListener = supabaseClient
      .from("todos")
      .on("*", (payload) => {
        const newTodo = payload.new;
        setTodos((oldTodos) => {
          const newTodos = [...oldTodos, newTodo];
          newTodos.sort((a, b) => b.id - a.id);
          return newTodos;
        });
      })
      .subscribe();

    return () => {
      todoListener.unsubscribe();
    };
  }, []);

  return (
    <div>
      <Head>
        <title>TodoApp</title>
        <meta
          name="description"
          content="Awesome todoapp to store your awesome todos"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <Navbar onOpen={onOpen} />
        <ManageTodo isOpen={isOpen} onClose={onClose} initialRef={initialRef} />
        <HStack m="10" spacing="4" justify="center">
          <Box>
            <Tag bg="green.500" borderRadius="3xl" size="sm" mt="1" /> Complete
          </Box>
          <Box>
            <Tag bg="yellow.400" borderRadius="3xl" size="sm" mt="1" />{" "}
            Incomplete
          </Box>
        </HStack>
        <SimpleGrid
          columns={{ base: 2, md: 3, lg: 4 }}
          gap={{ base: "4", md: "6", lg: "8" }}
          m="10"
        >
          {todos.map((todo) => (
            <SingleTodo todo={todo} key={todo.id} />
          ))}
        </SimpleGrid>
      </main>
    </div>
  );
};

export default Home;
```

Comprenons le code. Ici, nous avons ajouté deux useEffects :

```js
  useEffect(() => {
    if (user) {
      supabaseClient
        .from("todos")
        .select("*")
        .eq("user_id", user?.id)
        .order("id", { ascending: false })
        .then(({ data, error }) => {
          if (!error) {
            setTodos(data);
          }
        });
    }
  }, [user]);
```

Cet useEffect est utile lorsque la page est rendue pour la première fois. Nous interrogeons les données de la table Supabase pour cet utilisateur particulier de manière descendante.

```js
  useEffect(() => {
    const todoListener = supabaseClient
      .from("todos")
      .on("*", (payload) => {
        const newTodo = payload.new;
        setTodos((oldTodos) => {
          const newTodos = [...oldTodos, newTodo];
          newTodos.sort((a, b) => b.id - a.id);
          return newTodos;
        });
      })
      .subscribe();

    return () => {
      todoListener.unsubscribe();
    };
  }, []);
```

Cet useEffect est un abonnement en temps réel avec le serveur en temps réel de Supabase. Chaque fois qu'un nouveau todo est ajouté, nous obtenons l'événement de charge utile que nous utilisons pour ajouter le todo dans notre état local.

> **Note :** la documentation de Supabase suggère de ne pas utiliser l'abonnement en temps réel sur une application côté serveur.

Maintenant, allez sur `http://localhost:3000` et ajoutez un todo. Vous verrez la vue suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-at-8.09.06-PM.png align="left")

*Tous les Todos*

### Comment mettre à jour un Todo

Le mécanisme de mise à jour du todo peut être complexe pour les débutants. Je vais donc expliquer le processus aussi simplement que possible :

1. Nous créons un état `todo` dans notre composant parent de `index.js`. Cet état todo est mis à jour lorsque l'utilisateur clique sur SingleTodo.

2. Nous passons une fonction `openHandler` pour faire cela. Cette fonction met à jour l'état todo avec les détails du todo cliqué et ouvre la modale.

3. Dans `ManageTodo.js`, nous avons écrit un `useEffect` avec une dépendance de `todo` qui met à jour les valeurs de `title`, `description` et `isComplete` chaque fois que `todo` change.

4. Enfin, nous mettons à jour le todo dans notre table en utilisant la méthode de mise à jour de Supbase sur la base de l'`id` du todo.

Il est temps d'implémenter le code. Sous le répertoire des composants, allez dans `SingleTodo.js` et remplacez le code par le suivant :

```jsx
import { Box, Divider, Heading, Tag, Text } from "@chakra-ui/react";

const SingleTodo = ({ todo, openHandler }) => {
  const getDateInMonthDayYear = (date) => {
    const d = new Date(date);
    const options = {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
    };
    const n = d.toLocaleDateString("en-US", options);
    const replase = n.replace(new RegExp(",", "g"), " ");
    return replase;
  };

  return (
    <Box
      position="relative"
      maxW="sm"
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
      p="4"
      onClick={() => openHandler(todo)}
    >
      <Heading size="md" mt="3">
        {todo.title}
      </Heading>
      <Tag
        position="absolute"
        top="3"
        right="2"
        bg={todo.isComplete ? "green.500" : "yellow.400"}
        borderRadius="3xl"
        size="sm"
      />
      <Text color="gray.400" mt="1" fontSize="sm">
        {getDateInMonthDayYear(todo.insertedat)}
      </Text>
      <Divider my="4" />
      <Text noOfLines={[1, 2, 3]} color="gray.800">
        {todo.description}
      </Text>
    </Box>
  );
};

export default SingleTodo;
```

Sous le répertoire **components**, allez dans `ManageTodo.js` et remplacez le code par le code suivant :

```jsx
import {
  Alert,
  AlertIcon,
  Button,
  ButtonGroup,
  FormControl,
  FormHelperText,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  Switch,
  Text,
  Textarea,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { supabaseClient } from "../lib/client";

const ManageTodo = ({ isOpen, onClose, initialRef, todo, setTodo }) => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [isComplete, setIsComplete] = useState(false);
  const [isLoading, setIsLoading] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    if (todo) {
      setTitle(todo.title);
      setDescription(todo.description);
      setIsComplete(todo.isComplete);
    }
  }, [todo]);

  const submitHandler = async (event) => {
    event.preventDefault();
    setErrorMessage("");
    if (description.length <= 10) {
      setErrorMessage("Description must have more than 10 characters");
      return;
    }
    setIsLoading(true);
    const user = supabaseClient.auth.user();
    let supabaseError;
    if (todo) {
      const { error } = await supabaseClient
        .from("todos")
        .update({ title, description, isComplete, user_id: user.id })
        .eq("id", todo.id);
      supabaseError = error;
    } else {
      const { error } = await supabaseClient
        .from("todos")
        .insert([{ title, description, isComplete, user_id: user.id }]);
      supabaseError = error;
    }

    setIsLoading(false);
    if (supabaseError) {
      setErrorMessage(supabaseError.message);
    } else {
      closeHandler();
    }
  };

  const closeHandler = () => {
    setTitle("");
    setDescription("");
    setIsComplete(false);
    setTodo(null);
    onClose();
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      isCentered
      initialFocusRef={initialRef}
    >
      <ModalOverlay />
      <ModalContent>
        <form onSubmit={submitHandler}>
          <ModalHeader>{todo ? "Update Todo" : "Add Todo"}</ModalHeader>
          <ModalCloseButton onClick={closeHandler} />
          <ModalBody pb={6}>
            {errorMessage && (
              <Alert status="error" borderRadius="lg" mb="6">
                <AlertIcon />
                <Text textAlign="center">{errorMessage}</Text>
              </Alert>
            )}
            <FormControl isRequired={true}>
              <FormLabel>Title</FormLabel>
              <Input
                ref={initialRef}
                placeholder="Add your title here"
                onChange={(event) => setTitle(event.target.value)}
                value={title}
              />
            </FormControl>

            <FormControl mt={4} isRequired={true}>
              <FormLabel>Description</FormLabel>
              <Textarea
                placeholder="Add your description here"
                onChange={(event) => setDescription(event.target.value)}
                value={description}
              />
              <FormHelperText>
                Description must have more than 10 characters.
              </FormHelperText>
            </FormControl>

            <FormControl mt={4}>
              <FormLabel>Is Completed?</FormLabel>
              <Switch
                isChecked={isComplete}
                id="is-completed"
                onChange={(event) => setIsComplete(!isComplete)}
              />
            </FormControl>
          </ModalBody>

          <ModalFooter>
            <ButtonGroup spacing="3">
              <Button
                onClick={closeHandler}
                colorScheme="red"
                type="reset"
                isDisabled={isLoading}
              >
                Cancel
              </Button>
              <Button colorScheme="blue" type="submit" isLoading={isLoading}>
                {todo ? "Update" : "Save"}
              </Button>
            </ButtonGroup>
          </ModalFooter>
        </form>
      </ModalContent>
    </Modal>
  );
};

export default ManageTodo;
```

Comprenons le code ci-dessus. Ici, nous vérifions si l'utilisateur a cliqué sur le bouton de mise à jour (en vérifiant si le todo existe) puis nous affichons les données dans l'objet initial.

En fonction de la condition, nous affichons le texte de mise à jour au lieu du texte de sauvegarde sur le bouton. De plus, en fonction de la condition, nous exécutons la mise à jour de supabase si le todo existe et si ce n'est pas le cas, nous insérons.

Allez dans **pages > index.js** et remplacez le code existant par le code suivant :

```jsx
import { useDisclosure } from "@chakra-ui/hooks";
import { Box, HStack, SimpleGrid, Tag } from "@chakra-ui/react";
import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect, useRef, useState } from "react";
import ManageTodo from "../components/ManageTodo";
import Navbar from "../components/Navbar";
import SingleTodo from "../components/SingleTodo";
import { supabaseClient } from "../lib/client";

const Home = () => {
  const initialRef = useRef();
  const [todos, setTodos] = useState([]);
  const [todo, setTodo] = useState(null);

  const router = useRouter();
  const { isOpen, onOpen, onClose } = useDisclosure();
  const user = supabaseClient.auth.user();

  useEffect(() => {
    if (!user) {
      router.push("/signin");
    }
  }, [user, router]);

  useEffect(() => {
    if (user) {
      supabaseClient
        .from("todos")
        .select("*")
        .eq("user_id", user?.id)
        .order("id", { ascending: false })
        .then(({ data, error }) => {
          if (!error) {
            setTodos(data);
          }
        });
    }
  }, [user]);

  useEffect(() => {
    const todoListener = supabaseClient
      .from("todos")
      .on("*", (payload) => {
        const newTodo = payload.new;
        setTodos((oldTodos) => {
          const exists = oldTodos.find((todo) => todo.id === newTodo.id);
          let newTodos;
          if (exists) {
            const oldTodoIndex = oldTodos.findIndex(
              (obj) => obj.id === newTodo.id
            );
            oldTodos[oldTodoIndex] = newTodo;
            newTodos = oldTodos;
          } else {
            newTodos = [...oldTodos, newTodo];
          }
          newTodos.sort((a, b) => b.id - a.id);
          return newTodos;
        });
      })
      .subscribe();

    return () => {
      todoListener.unsubscribe();
    };
  }, []);

  const openHandler = (clickedTodo) => {
    setTodo(clickedTodo);
    onOpen();
  };

  return (
    <div>
      <Head>
        <title>TodoApp</title>
        <meta
          name="description"
          content="Awesome todoapp to store your awesome todos"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <Navbar onOpen={onOpen} />
        <ManageTodo
          isOpen={isOpen}
          onClose={onClose}
          initialRef={initialRef}
          todo={todo}
          setTodo={setTodo}
        />
        <HStack m="10" spacing="4" justify="center">
          <Box>
            <Tag bg="green.500" borderRadius="3xl" size="sm" mt="1" /> Complete
          </Box>
          <Box>
            <Tag bg="yellow.400" borderRadius="3xl" size="sm" mt="1" />{" "}
            Incomplete
          </Box>
        </HStack>
        <SimpleGrid
          columns={{ base: 2, md: 3, lg: 4 }}
          gap={{ base: "4", md: "6", lg: "8" }}
          m="10"
        >
          {todos.map((todo) => (
            <SingleTodo todo={todo} key={todo.id} openHandler={openHandler} />
          ))}
        </SimpleGrid>
      </main>
    </div>
  );
};

export default Home;
```

Ici, nous ajoutons le composant `ManageTodo` que nous avons créé et passons les props qui sont utilisées par ce composant.

Maintenant, allez sur `http://localhost:3000` et cliquez sur n'importe quel todo pour le mettre à jour et vous verrez la vue suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-06-at-8.10.10-PM.png align="left")

*Mettre à jour le Todo*

### Comment supprimer un Todo

Cette fonctionnalité nécessitera de mettre à jour une partie de notre code existant. D'abord, nous allons le faire, puis comprendre comment cela fonctionne et pourquoi les changements sont nécessaires.

Allez dans `SingleTodo.js` à l'intérieur du répertoire **components** et remplacez le code existant par le code suivant :

```jsx
import {
  Box,
  Divider,
  Heading,
  Tag,
  Text,
  Button,
  Center,
} from "@chakra-ui/react";

const SingleTodo = ({ todo, openHandler, deleteHandler, isDeleteLoading }) => {
  const getDateInMonthDayYear = (date) => {
    const d = new Date(date);
    const options = {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
    };
    const n = d.toLocaleDateString("en-US", options);
    const replase = n.replace(new RegExp(",", "g"), " ");
    return replase;
  };

  return (
    <Box
      position="relative"
      maxW="sm"
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
      p="4"
      onClick={() => openHandler(todo)}
    >
      <Heading size="md" mt="3">
        {todo.title}
      </Heading>
      <Tag
        position="absolute"
        top="3"
        right="2"
        bg={todo.isComplete ? "green.500" : "yellow.400"}
        borderRadius="3xl"
        size="sm"
      />
      <Text color="gray.400" mt="1" fontSize="sm">
        {getDateInMonthDayYear(todo.insertedat)}
      </Text>
      <Divider my="4" />
      <Text noOfLines={[1, 2, 3]} color="gray.800">
        {todo.description}
      </Text>
      <Center>
        <Button
          mt="4"
          size="sm"
          colorScheme="red"
          onClick={(event) => {
            event.stopPropagation();
            deleteHandler(todo.id);
          }}
          isDisabled={isDeleteLoading}
        >
          Delete
        </Button>
      </Center>
    </Box>
  );
};

export default SingleTodo;
```

Ici, nous avons ajouté un bouton de suppression avec un événement onClick. Maintenant, cet événement de suppression est sous un autre événement qui ouvre la modale. Donc chaque fois que nous cliquons sur supprimer, cela ouvrira également la modale.

Nous ne voulons pas ce comportement, donc nous utilisons une méthode de `event` appelée `stopPropagation`. Cette méthode n'autorise pas les événements des enfants à être transmis au parent.

Maintenant, allez dans `index.js` à l'intérieur du répertoire **pages** et remplacez le code existant par le code suivant :

```js
import { useDisclosure } from "@chakra-ui/hooks";
import { Box, HStack, SimpleGrid, Tag } from "@chakra-ui/react";
import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect, useRef, useState } from "react";
import ManageTodo from "../components/ManageTodo";
import Navbar from "../components/Navbar";
import SingleTodo from "../components/SingleTodo";
import { supabaseClient } from "../lib/client";

const Home = () => {
  const initialRef = useRef();
  const [todos, setTodos] = useState([]);
  const [todo, setTodo] = useState(null);
  const [isDeleteLoading, setIsDeleteLoading] = useState(false);

  const router = useRouter();
  const { isOpen, onOpen, onClose } = useDisclosure();
  const user = supabaseClient.auth.user();

  useEffect(() => {
    if (!user) {
      router.push("/signin");
    }
  }, [user, router]);

  useEffect(() => {
    if (user) {
      supabaseClient
        .from("todos")
        .select("*")
        .eq("user_id", user?.id)
        .order("id", { ascending: false })
        .then(({ data, error }) => {
          if (!error) {
            setTodos(data);
          }
        });
    }
  }, [user]);

  useEffect(() => {
    const todoListener = supabaseClient
      .from("todos")
      .on("*", (payload) => {
        if (payload.eventType !== "DELETE") {
          const newTodo = payload.new;
          setTodos((oldTodos) => {
            const exists = oldTodos.find((todo) => todo.id === newTodo.id);
            let newTodos;
            if (exists) {
              const oldTodoIndex = oldTodos.findIndex(
                (obj) => obj.id === newTodo.id
              );
              oldTodos[oldTodoIndex] = newTodo;
              newTodos = oldTodos;
            } else {
              newTodos = [...oldTodos, newTodo];
            }
            newTodos.sort((a, b) => b.id - a.id);
            return newTodos;
          });
        }
      })
      .subscribe();

    return () => {
      todoListener.unsubscribe();
    };
  }, []);

  const openHandler = (clickedTodo) => {
    setTodo(clickedTodo);
    onOpen();
  };

  const deleteHandler = async (todoId) => {
    setIsDeleteLoading(true);
    const { error } = await supabaseClient
      .from("todos")
      .delete()
      .eq("id", todoId);
    if (!error) {
      setTodos(todos.filter((todo) => todo.id !== todoId));
    }
    setIsDeleteLoading(false);
  };

  return (
    <div>
      <Head>
        <title>TodoApp</title>
        <meta
          name="description"
          content="Awesome todoapp to store your awesome todos"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <Navbar onOpen={onOpen} />
        <ManageTodo
          isOpen={isOpen}
          onClose={onClose}
          initialRef={initialRef}
          todo={todo}
          setTodo={setTodo}
        />
        <HStack m="10" spacing="4" justify="center">
          <Box>
            <Tag bg="green.500" borderRadius="3xl" size="sm" mt="1" /> Complete
          </Box>
          <Box>
            <Tag bg="yellow.400" borderRadius="3xl" size="sm" mt="1" />{" "}
            Incomplete
          </Box>
        </HStack>
        <SimpleGrid
          columns={{ base: 2, md: 3, lg: 4 }}
          gap={{ base: "4", md: "6", lg: "8" }}
          m="10"
        >
          {todos.map((todo, index) => (
            <SingleTodo
              todo={todo}
              key={index}
              openHandler={openHandler}
              deleteHandler={deleteHandler}
              isDeleteLoading={isDeleteLoading}
            />
          ))}
        </SimpleGrid>
      </main>
    </div>
  );
};

export default Home;
```

Comprenons d'abord la méthode `deleteHandler`. Dans cette méthode, nous utilisons le client Supabase pour supprimer un enregistrement de la table **todos**. Une fois qu'il est supprimé avec succès, nous utilisons la méthode `filter` pour supprimer le todo de notre état local.

Pour l'useEffect qui contient le `todoListener`, nous ajoutons une condition `if` basée sur un type d'`event`. Nous ne voulons rien faire sur l'événement `DELETE` car nous mettons à jour l'état local dans `deleteHandler`.

Allez sur `http://localhost:3000` et vous verrez la vue suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-07-at-1.37.34-PM.png align="left")

Cliquez sur le bouton **Delete** et vous verrez que le todo a disparu de notre vue todos.

Avec cela, nous avons terminé notre flux d'opérations **TODO CRUD**.

## Comment mettre à jour les détails du profil et les avatars

Le **code de l'opération de mise à jour du profil** est disponible sous ce commit si vous avez besoin de vous y référer à l'avenir.

%[https://github.com/Sharvin26/TodoApp-supabase/tree/fb7055b83c847709cb6cc5c6aa26553ecee4026f]

Avant de travailler sur la section de profil, nous devons faire de notre en-tête **TodoApp** une route afin de pouvoir revenir à la page d'accueil depuis la page de profil.

Dans `Navbar.js` sous le répertoire des composants, remplacez le code existant par le code suivant :

```jsx
import { Box, Button, ButtonGroup, Flex, Heading } from "@chakra-ui/react";
import NavLink from "next/link";
import { useRouter } from "next/router";
import { useState } from "react";
import { supabaseClient } from "../lib/client";

const Navbar = ({ onOpen }) => {
  const router = useRouter();
  const [isLogoutLoading, setIsLogoutLoading] = useState(false);

  const logoutHandler = async () => {
    try {
      setIsLogoutLoading(true);
      await supabaseClient.auth.signOut();
      router.push("/signin");
    } catch (error) {
      router.push("/signin");
    } finally {
      setIsLogoutLoading(false);
    }
  };

  return (
    <Box height="100%" p="5" bg="gray.100">
      <Box maxW="6xl" mx="auto">
        <Flex
          as="nav"
          aria-label="Site navigation"
          align="center"
          justify="space-between"
        >
          <NavLink href="/">
            <Heading mr="4" as="button">
              TodoApp
            </Heading>
          </NavLink>
          <Box>
            <NavLink href="/profile">Profile</NavLink>
            <ButtonGroup spacing="4" ml="6">
              {router.pathname === "/" && (
                <Button colorScheme="blue" onClick={onOpen}>
                  Add Todo
                </Button>
              )}
              <Button
                colorScheme="red"
                onClick={logoutHandler}
                isLoading={isLogoutLoading}
              >
                Logout
              </Button>
            </ButtonGroup>
          </Box>
        </Flex>
      </Box>
    </Box>
  );
};

export default Navbar;
```

Commençons à travailler sur la construction de la dernière partie de notre application, qui est la section de profil. Cette section aura un formulaire qui peut mettre à jour le nom d'utilisateur, le site web, la bio et un avatar.

Pour stocker nos images, nous utiliserons le stockage Supabase. Par défaut, ces buckets de stockage sont privés et peuvent être accessibles en utilisant un jeton. Mais pour les besoins de cet article, nous allons rendre le bucket public. Mais si vous stockez des informations sensibles, assurez-vous de garder ce bucket privé.

Allez sur [https://app.supabase.io/](https://app.supabase.io/) et allez dans l'onglet stockage. Vous y verrez `avatars` listé sous Tous les Buckets.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-07-at-7.43.07-PM.png align="left")

Cliquez sur les trois points et sélectionnez l'option **Rendre public**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-07-at-7.43.31-PM.png align="left")

Retour à notre code : à l'intérieur du répertoire **pages**, créez un fichier nommé `profile.js` et copiez-collez le code suivant :

```jsx
import {
  Avatar,
  Box,
  Button,
  Flex,
  FormControl,
  FormLabel,
  Input,
  Stack,
  Textarea,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import { supabaseClient } from "../lib/client";

const Profile = () => {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [website, setWebsite] = useState("");
  const [bio, setBio] = useState("");
  const [avatarurl, setAvatarurl] = useState("");

  const [isLoading, setIsLoading] = useState(false);
  const [isImageUploadLoading, setIsImageUploadLoading] = useState(false);

  const user = supabaseClient.auth.user();

  useEffect(() => {
    if (user) {
      setEmail(user.email);
      supabaseClient
        .from("profiles")
        .select("*")
        .eq("id", user.id)
        .then(({ data, error }) => {
          if (!error) {
            setUsername(data[0].username || "");
            setWebsite(data[0].website || "");
            setBio(data[0].bio || "");
            setAvatarurl(data[0].avatarurl || "");
          }
        });
    }
  }, [user]);

  const updateHandler = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    const body = { username, website, bio };
    const userId = user.id;
    const { error } = await supabaseClient
      .from("profiles")
      .update(body)
      .eq("id", userId);
    if (!error) {
      setUsername(body.username);
      setWebsite(body.website);
      setBio(body.bio);
    }
    setIsLoading(false);
  };

  function makeid(length) {
    let result = "";
    const characters =
      "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    const charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  }

  const uploadHandler = async (event) => {
    setIsImageUploadLoading(true);
    const avatarFile = event.target.files[0];
    const fileName = makeid(10);

    const { error } = await supabaseClient.storage
      .from("avatars")
      .upload(fileName, avatarFile, {
        cacheControl: "3600",
        upsert: false,
      });
    if (error) {
      setIsImageUploadLoading(false);
      console.log("error", error);
      return;
    }
    const { publicURL, error: publicURLError } = supabaseClient.storage
      .from("avatars")
      .getPublicUrl(fileName);
    if (publicURLError) {
      setIsImageUploadLoading(false);
      console.log("publicURLError", publicURLError);
      return;
    }
    const userId = user.id;
    await supabaseClient
      .from("profiles")
      .update({
        avatarurl: publicURL,
      })
      .eq("id", userId);
    setAvatarurl(publicURL);
    setIsImageUploadLoading(false);
  };

  return (
    <Box>
      <Navbar />
      <Box mt="8" maxW="xl" mx="auto">
        <Flex align="center" justify="center" direction="column">
          <Avatar
            size="2xl"
            src={avatarurl || ""}
            name={username || user?.email}
          />
          <FormLabel
            htmlFor="file-input"
            my="5"
            borderRadius="2xl"
            borderWidth="1px"
            textAlign="center"
            p="2"
            bg="blue.400"
            color="white"
          >
            {isImageUploadLoading ? "Uploading....." : "Upload Profile Picture"}
          </FormLabel>
          <Input
            type="file"
            hidden
            id="file-input"
            onChange={uploadHandler}
            multiple={false}
            disabled={isImageUploadLoading}
          />
        </Flex>
        <Stack
          borderWidth="1px"
          borderRadius="lg"
          overflow="hidden"
          p={5}
          mt="-2"
          spacing="4"
          as="form"
          onSubmit={updateHandler}
        >
          <FormControl id="email" isRequired>
            <FormLabel>Email</FormLabel>
            <Input type="email" isDisabled={true} value={email} />
          </FormControl>
          <FormControl id="username" isRequired>
            <FormLabel>Username</FormLabel>
            <Input
              placeholder="Add your username here"
              type="text"
              value={username}
              onChange={(event) => setUsername(event.target.value)}
            />
          </FormControl>
          <FormControl id="website" isRequired>
            <FormLabel>Website URL</FormLabel>
            <Input
              placeholder="Add your website here"
              type="url"
              value={website}
              onChange={(event) => setWebsite(event.target.value)}
            />
          </FormControl>
          <FormControl id="bio" isRequired>
            <FormLabel>Bio</FormLabel>
            <Textarea
              placeholder="Add your bio here"
              value={bio}
              onChange={(event) => setBio(event.target.value)}
            />
          </FormControl>
          <Button colorScheme="blue" type="submit" isLoading={isLoading}>
            Update
          </Button>
        </Stack>
      </Box>
    </Box>
  );
};

export default Profile;
```

Ici, nous avons 4 éléments `FormControl`, et chacun est pré-rempli si une valeur existe. Cela est possible car au rendu, `useEffect` s'exécute, ce qui utilise le client Supabase pour récupérer l'enregistrement de l'utilisateur depuis les tables `auth` et `profiles`.

**Note :** la table auth est maintenue par Supabase et peut être accessible via le client en utilisant la commande suivante :

```js
supabase.auth.user()
```

Sauf pour les images, les autres enregistrements peuvent être mis à jour en utilisant la fonction `updateHandler`. Cette fonction met à jour l'enregistrement de l'utilisateur en utilisant `id`.

La fonction `uploadHandler` est responsable du téléchargement de l'image dans le bucket de stockage et de la définition de `avatarurl` dans la table des profils pour un enregistrement basé sur `id`.

La méthode `upload` de Supabase télécharge l'image tandis que la méthode `getPublicUrl` nous donne une URL publique de l'image. Nous utilisons la méthode `from('profiles').update` pour mettre à jour l'enregistrement.

Visitez `http://localhost:3000` et cliquez sur le lien de profil. Vous verrez la vue suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-07-at-7.55.59-PM.png align="left")

Maintenant, vous pouvez utiliser la méthode de mise à jour pour mettre à jour votre nom d'utilisateur, l'URL du site web et la bio.

Avec cela, notre TodoApp est terminé et prêt pour la production.

## Comment déployer l'application sur Vercel et configurer l'authentification Supabase

Avant de déployer l'application sur Vercel, nous devons exécuter la commande `npm run build` et vérifier la sortie du terminal pour voir si nous avons des erreurs.

Il existe deux façons de configurer une application sur Vercel :

1. En utilisant la [bibliothèque npm Vercel](https://www.npmjs.com/package/vercel) et en poussant le code localement vers un serveur Vercel

2. En connectant le bot Vercel au dépôt GitHub.

Je vais utiliser la deuxième méthode.

Vous devez créer un dépôt sur GitHub et pousser le code là-bas.

Si vous n'avez pas créé de compte sur Vercel, vous pouvez aller sur [https://vercel.com/](https://vercel.com/) et cliquer sur le bouton d'inscription.

Une fois que vous avez créé votre compte, vous serez redirigé vers un tableau de bord qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-04-10-at-4.07.03-PM.png align="left")

*Tableau de bord Vercel*

Cliquez sur le bouton **Nouveau Projet**. Il vous demandera d'installer le bot Vercel et les permissions.

**Note :** Vous pouvez autoriser le bot Vercel à lire tous les dépôts de votre compte GitHub ou donner la permission pour le dépôt actuellement créé.

Cliquez sur le bouton **Importer** sur le dépôt GitHub créé ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-07-at-8.29.42-PM.png align="left")

*Importer le projet depuis GitHub sur Vercel*

Maintenant, il vous demandera si vous voulez créer une équipe. L'équipe est une fonctionnalité disponible sous le **Plan Pro**. Par défaut, Vercel est sous le **plan hobby**. Pour l'instant, je vais sauter cela.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-07-at-8.33.19-PM.png align="left")

*Créer une équipe sur Vercel*

Maintenant, vous devrez ajouter des variables d'environnement. Ajoutez-les depuis `.env.local`.

Cliquez sur l'accordéon qui se trouve devant les variables d'environnement et ajoutez les variables là-bas comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-07-at-8.34.22-PM.png align="left")

*Configurer les paramètres de construction et d'environnement sur Vercel*

Une fois qu'elles sont ajoutées, cliquez sur le bouton Déployer. Après le déploiement réussi, vous obtiendrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-07-at-8.39.20-PM.png align="left")

*Succès du déploiement sur Vercel*

Maintenant, cliquez sur la boîte grise où votre application est affichée. Elle vous redirigera vers une page où vous pourrez trouver un domaine préconfiguré pour vos applications.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-07-at-8.42.16-PM.png align="left")

*Aperçu du projet Vercel*

Oui, Vercel fournit des sous-domaines pour lesquels nous pouvons également définir un domaine personnalisé. Pour l'instant, nous allons utiliser le domaine Vercel. Copiez le premier domaine sous la section Domaines et allez dans votre projet Supabase.

Allez dans **Authentification > Paramètres** et mettez à jour l'**URL du site** et les **URL de redirection supplémentaires** avec l'URL copiée (assurez-vous d'ajouter `https://` devant l'URL copiée) :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-07-at-8.47.27-PM.png align="left")

*Paramètres d'authentification Supabase*

Avec cela, nous avons créé notre application todo prête pour la production. Si vous avez construit l'application en suivant le tutoriel, alors un très grand félicitations pour cette réalisation.

## Merci d'avoir lu !

N'hésitez pas à me contacter sur [Twitter](https://twitter.com/sharvinshah26) et [Github](https://github.com/Sharvin26).

Si vous souhaitez qu'un projet soit développé ou souhaitez me consulter, vous pouvez m'envoyer un message sur mon Twitter (@sharvinshah26).