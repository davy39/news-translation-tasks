---
title: Développement Full Stack avec Next.js et Supabase – Le Guide Complet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-07T23:33:30.000Z'
originalURL: https://freecodecamp.org/news/the-complete-guide-to-full-stack-development-with-supabas
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/supanext.png
tags:
- name: full stack
  slug: full-stack
- name: Next.js
  slug: nextjs
- name: open source
  slug: open-source
seo_title: Développement Full Stack avec Next.js et Supabase – Le Guide Complet
seo_desc: 'By Nader Dabit

  Supabase is an open source Firebase alternative that lets you create a real-time
  backend in less than two minutes.

  Supabase has continued to gain hype and adoption with developers in my network over
  the past few months. And a lot of th...'
---

Par Nader Dabit

[Supabase](https://twitter.com/supabase_io) est une alternative open source à Firebase qui vous permet de créer un backend en temps réel en moins de deux minutes.

Supabase a continué à gagner en popularité et en adoption parmi les développeurs de mon réseau au cours des derniers mois. Et beaucoup des personnes avec qui j'en ai parlé préfèrent le fait qu'il utilise une base de données de style SQL, et ils aiment aussi qu'il soit open source.

Lorsque vous créez un projet, Supabase vous donne automatiquement une base de données PostgreSQL, une authentification utilisateur et une API. À partir de là, vous pouvez facilement implémenter des fonctionnalités supplémentaires comme des abonnements en temps réel et le stockage de fichiers.

Dans ce guide, vous apprendrez à construire une application full stack qui implémente les fonctionnalités principales dont la plupart des applications ont besoin – comme le routage, une base de données, une API, l'authentification, l'autorisation, les données en temps réel et le contrôle d'accès granulaire. Nous utiliserons une stack moderne incluant [React](https://reactjs.org/docs/getting-started.html), [Next.js](https://nextjs.org/), et [TailwindCSS](https://tailwindcss.com/).

J'ai essayé de distiller tout ce que j'ai appris en me mettant à niveau avec Supabase dans un guide aussi court que possible afin que vous aussi puissiez commencer à construire des applications full stack avec ce framework.

L'application que nous allons construire est une application de blogging multi-utilisateurs qui incorpore tous les types de fonctionnalités que vous voyez dans de nombreuses applications modernes. Cela nous permettra d'aller au-delà du CRUD de base en activant des fonctionnalités comme le stockage de fichiers ainsi que l'autorisation et le contrôle d'accès granulaire.

> Vous pouvez trouver le code de l'application que nous allons construire [ici](https://github.com/dabit3/supabase-next.js).

En apprenant à incorporer toutes ces fonctionnalités ensemble, vous devriez être en mesure de prendre ce que vous apprenez ici et de construire vos propres idées. Comprendre les blocs de construction de base eux-mêmes vous permet ensuite d'utiliser cette connaissance à l'avenir pour l'utiliser de la manière qui vous convient.

## Aperçu de Supabase 

### Comment construire des applications Full Stack

Je suis fasciné par les frameworks Serverless full stack en raison de la puissance et de l'agilité qu'ils offrent aux développeurs cherchant à construire des applications complètes.

Supabase apporte à la table l'importante combinaison de services backend puissants et de bibliothèques et SDK côté client faciles à utiliser pour une solution de bout en bout. 

Cette combinaison vous permet non seulement de construire les fonctionnalités et services individuels nécessaires au backend, mais aussi de les intégrer facilement ensemble au frontend en utilisant les bibliothèques client maintenues par la même équipe.

Parce que Supabase est open source, vous avez la possibilité de l'auto-héberger ou de déployer votre backend en tant que service géré. Et comme vous pouvez le voir, cela sera facile pour nous à faire sur un niveau gratuit qui ne nécessite pas de carte de crédit pour commencer.

## Pourquoi utiliser Supabase ?

J'ai dirigé l'équipe de défense des développeurs Front End Web et Mobile chez AWS, et j'ai écrit un livre sur la construction de ces types d'applications. J'ai donc eu beaucoup d'expérience dans la construction dans cet espace. 

Et je pense que Supabase apporte à la table des fonctionnalités vraiment puissantes qui m'ont immédiatement marqué lorsque j'ai commencé à construire avec.

### Modèles d'accès aux données

L'une des plus grandes limitations de certains des outils et frameworks que j'ai utilisés dans le passé est le manque de capacités de requête. Ce que j'aime beaucoup chez Supabase, c'est que, puisqu'il est construit sur PostgreSQL, il permet un ensemble extrêmement riche de capacités de requête performantes dès la sortie de la boîte sans avoir à écrire de code backend supplémentaire.

Les SDK côté client fournissent des [filtres](https://supabase.io/docs/reference/javascript/using-filters) et des [modificateurs](https://supabase.io/docs/reference/javascript/using-modifiers) faciles à utiliser pour permettre une combinaison presque infinie de modèles d'accès aux données.

Parce que la base de données est SQL, les données relationnelles sont faciles à configurer et à interroger, et les bibliothèques client en tiennent compte comme un citoyen de première classe.

### Permissions

Lorsque vous dépassez "hello world", de nombreux types de frameworks et services tombent en panne très rapidement. Cela est dû au fait que la plupart des cas d'utilisation réels vont bien au-delà de la fonctionnalité CRUD de base que vous voyez souvent mise à disposition par ces outils.

Le problème avec certains frameworks et services gérés est que les abstractions qu'ils créent ne sont pas assez extensibles pour permettre des configurations faciles à modifier ou une logique métier personnalisée. Ces restrictions rendent souvent difficile la prise en compte des nombreux cas d'utilisation ponctuels qui surviennent lors de la construction d'une application dans le monde réel.

En plus de permettre une large gamme de modèles d'accès aux données, Supabase facilite la configuration de l'autorisation et des contrôles d'accès granulaires. Cela est dû au fait qu'il s'agit simplement de PostgreSQL, vous permettant d'implémenter les [politiques de sécurité au niveau des lignes](https://www.postgresql.org/docs/10/ddl-rowsecurity.html) que vous souhaitez directement à partir de l'éditeur SQL intégré (quelque chose que nous couvrirons ici).

### Composants UI

En plus des bibliothèques côté client maintenues par la même équipe qui construit les autres outils Supabase, ils maintiennent également une [bibliothèque de composants UI](https://ui.supabase.io/) (bêta) qui vous permet de démarrer rapidement avec divers éléments UI.

Le plus puissant est [Auth](https://ui.supabase.io/components/auth) qui s'intègre à votre projet Supabase pour créer rapidement un flux d'authentification utilisateur (que j'utiliserai dans ce tutoriel).

### Fournisseurs d'authentification multiples

Supabase permet tous les types de mécanismes d'authentification suivants :

1. Nom d'utilisateur et mot de passe
2. Lien magique par email
3. Google
4. Facebook
5. Apple
6. GitHub
7. Twitter
8. Azure
9. GitLab
10. Bitbucket

### Open Source

L'une des plus grandes choses qu'il a pour lui est qu'il est [complètement open source](https://github.com/supabase) (oui, le backend aussi). Cela signifie que vous pouvez choisir soit l'approche hébergée Serverless, soit l'héberger vous-même.

Cela signifie que si vous le souhaitez, vous pourriez [exécuter Supabase avec Docker et héberger votre application](https://supabase.io/docs/guides/self-hosting) sur AWS, GCP ou Azure. Cela éliminerait le problème de verrouillage par le fournisseur que vous pourriez rencontrer avec les alternatives à Supabase.

## Comment commencer avec Supabase

### Configuration du projet

Pour commencer, créons d'abord l'application Next.js.

```sh
npx create-next-app next-supabase
```

Ensuite, accédez au répertoire et installez les dépendances dont nous aurons besoin pour l'application en utilisant soit NPM soit Yarn :

```sh
npm install @supabase/supabase-js @supabase/ui react-simplemde-editor easymde react-markdown uuid
npm install tailwindcss@latest @tailwindcss/typography postcss@latest autoprefixer@latest
```

Ensuite, créez les fichiers de configuration nécessaires pour Tailwind :

```sh
npx tailwindcss init -p
```

Maintenant, mettez à jour **tailwind.config.js** pour ajouter le plugin de typographie Tailwind au tableau des plugins. Nous utiliserons ce plugin pour styliser le markdown pour notre blog :

```
plugins: [
  require('@tailwindcss/typography')
]
```

Enfin, remplacez les styles dans **styles/globals.css** par ce qui suit :

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Initialisation du projet Supabase

Maintenant que le projet est créé localement, créons le projet Supabase.

Pour ce faire, rendez-vous sur [Supabase.io](https://supabase.io/) et cliquez sur **Start Your Project**. Authentifiez-vous avec GitHub, puis créez un nouveau projet sous l'organisation qui vous est fournie dans votre compte.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/myaccountsorg.jpg)

Donnez au projet un **Nom** et un **Mot de passe**, puis cliquez sur **Create new project**.

Il faudra environ 2 minutes pour que votre projet soit créé.

### Comment créer une table de base de données dans Supabase

Une fois que vous avez créé votre projet, créons la table pour notre application ainsi que toutes les permissions dont nous aurons besoin. Pour ce faire, cliquez sur le lien **SQL** dans le menu de gauche.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-06-at-6.07.00-PM.png)

Dans cette vue, cliquez sur **Query-1** sous **Open queries** et collez la requête SQL suivante, puis cliquez sur **RUN** :

```
CREATE TABLE posts (
  id bigint generated by default as identity primary key,
  user_id uuid references auth.users not null,
  user_email text,
  title text,
  content text,
  inserted_at timestamp with time zone default timezone('utc'::text, now()) not null
);

alter table posts enable row level security;

create policy "Individuals can create posts." on posts for
    insert with check (auth.uid() = user_id);

create policy "Individuals can update their own posts." on posts for
    update using (auth.uid() = user_id);

create policy "Individuals can delete their own posts." on posts for
    delete using (auth.uid() = user_id);

create policy "Posts are public." on posts for
    select using (true);
```

Cela créera la table `posts` que nous utiliserons pour l'application. Cela active également certaines permissions au niveau des lignes :

* Tous les utilisateurs peuvent interroger les posts
* Seuls les utilisateurs connectés peuvent créer des posts, et leur ID utilisateur doit correspondre à l'ID utilisateur passé dans les arguments
* Seul le propriétaire du post peut le mettre à jour ou le supprimer

Maintenant, si nous cliquons sur le lien **Table editor**, nous devrions voir notre nouvelle table créée avec le schéma approprié.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-06-at-6.11.49-PM.png)

C'est tout ! Notre backend est prêt à être utilisé et nous pouvons commencer à construire l'UI. L'authentification par nom d'utilisateur et mot de passe est déjà activée par défaut, donc tout ce que nous avons à faire maintenant est de tout connecter au frontend.

### Configuration de Next.js avec Supabase

Maintenant que le projet a été créé, nous avons besoin d'un moyen pour que notre application Next.js connaisse les services backend que nous venons de créer pour elle.

La meilleure façon pour nous de configurer cela est d'utiliser des variables d'environnement. Next.js permet de définir des variables d'environnement en créant un fichier appelé **.env.local** à la racine du projet et en les stockant là.

Pour exposer une variable au navigateur, vous devez préfixer la variable avec `NEXT_PUBLIC_`.

Créez un fichier appelé **.env.local** à la racine du projet, et ajoutez la configuration suivante :

```
NEXT_PUBLIC_SUPABASE_URL=https://app-id.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-public-api-key
```

Vous pouvez trouver les valeurs de votre URL d'API et de votre clé d'API dans les paramètres du tableau de bord Supabase :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/appurls.jpg)

Ensuite, créez un fichier appelé **api.js** à la racine du projet et ajoutez le code suivant :

```javascript
// api.js
import { createClient } from '@supabase/supabase-js'
export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
)
```

Maintenant, nous pourrons importer l'instance `supabase` et l'utiliser n'importe où dans notre application.

Voici un aperçu de ce à quoi ressemble l'interaction avec l'API en utilisant le client JavaScript Supabase.

**Interrogation des données :**

```javascript
import { supabase } from '../path/to/api'

const { data, error } = await supabase
  .from('posts')
  .select()
```

**Création de nouveaux éléments dans la base de données :**

```javascript
const { data, error } = await supabase
  .from('posts')
  .insert([
    {
      title: "Hello World",
      content: "My first post",
      user_id: "some-user-id",
      user_email: "myemail@gmail.com"
    }
  ])
```

Comme je l'ai mentionné précédemment, les [filtres](https://supabase.io/docs/reference/javascript/using-filters) et les [modificateurs](https://supabase.io/docs/reference/javascript/using-modifiers) rendent vraiment facile l'implémentation de divers modèles d'accès aux données et ensembles de sélection de vos données.

**Authentification – inscription :**

```javascript
const { user, session, error } = await supabase.auth.signUp({
  email: 'example@email.com',
  password: 'example-password',
})
```

**Authentification – connexion :**

```javascript
const { user, session, error } = await supabase.auth.signIn({
  email: 'example@email.com',
  password: 'example-password',
})
```

Dans notre cas, nous n'écrireons pas la logique d'authentification principale à la main, nous utiliserons le composant Auth de [Supabase UI](https://ui.supabase.io/components/auth).

## Comment construire l'application

Maintenant, commençons à construire l'UI !

Pour commencer, mettons d'abord à jour l'application pour implémenter une navigation de base et un style de mise en page.

Nous configurerons également une logique pour vérifier si l'utilisateur est connecté, et afficher un lien pour créer de nouveaux posts s'il l'est.

Enfin, nous implémenterons un écouteur pour tout événement `auth`. Et lorsqu'un nouvel événement `auth` se produit, nous vérifierons qu'il y a actuellement un utilisateur connecté afin d'afficher ou de masquer le lien **Créer un Post**.

Ouvrez **_app.js** et ajoutez le code suivant :

```javascript
// pages/_app.js
import Link from 'next/link'
import { useState, useEffect } from 'react'
import { supabase } from '../api'
import '../styles/globals.css'

function MyApp({ Component, pageProps }) {
  const [user, setUser] = useState(null);
  useEffect(() => {
    const { data: authListener } = supabase.auth.onAuthStateChange(
      async () => checkUser()
    )
    checkUser()
    return () => {
      authListener?.unsubscribe()
    };
  }, [])
  async function checkUser() {
    const user = supabase.auth.user()
    setUser(user)
  }
  return (
  <div>
    <nav className="p-6 border-b border-gray-300">
      <Link href="/">
        <span className="mr-6 cursor-pointer">Accueil</span>
      </Link>
      {
        user && (
          <Link href="/create-post">
            <span className="mr-6 cursor-pointer">Créer un Post</span>
          </Link>
        )
      }
      <Link href="/profile">
        <span className="mr-6 cursor-pointer">Profil</span>
      </Link>
    </nav>
    <div className="py-8 px-16">
      <Component {...pageProps} />
    </div>
  </div>
  )
}

export default MyApp
```

### Comment créer une page de profil utilisateur

Ensuite, créons la page **profil**. Dans le répertoire des pages, créez un nouveau fichier nommé **profile.js** et ajoutez le code suivant :

```javascript
// pages/profile.js
import { Auth, Typography, Button } from "@supabase/ui";
const { Text } = Typography
import { supabase } from '../api'

function Profile(props) {
    const { user } = Auth.useUser();
    if (user)
      return (
        <>
          <Text>Connecté : {user.email}</Text>
          <Button block onClick={() => props.supabaseClient.auth.signOut()}>
            Se déconnecter
          </Button>
        </>
      );
    return props.children 
}

export default function AuthProfile() {
    return (
        <Auth.UserContextProvider supabaseClient={supabase}>
          <Profile supabaseClient={supabase}>
            <Auth supabaseClient={supabase} />
          </Profile>
        </Auth.UserContextProvider>
    )
}
```

La page de profil utilise le composant [`Auth`](https://ui.supabase.io/components/auth) de la [bibliothèque d'interface utilisateur Supabase](https://ui.supabase.io/components/auth). Ce composant affichera un formulaire "s'inscrire" et "se connecter" pour les utilisateurs **non authentifiés**, et un profil utilisateur de base avec un bouton "se déconnecter" pour les utilisateurs **authentifiés**. Il permettra également un lien de connexion magique.

### Comment créer de nouveaux posts

Ensuite, créons la page **create-post**. Dans le répertoire des pages, créez une page nommée **create-post.js** avec le code suivant :

```javascript
// pages/create-post.js
import { useState } from 'react'
import { v4 as uuid } from 'uuid'
import { useRouter } from 'next/router'
import dynamic from 'next/dynamic'
import "easymde/dist/easymde.min.css"
import { supabase } from '../api'

const SimpleMDE = dynamic(() => import('react-simplemde-editor'), { ssr: false })
const initialState = { title: '', content: '' }

function CreatePost() {
  const [post, setPost] = useState(initialState)
  const { title, content } = post
  const router = useRouter()
  function onChange(e) {
    setPost(() => ({ ...post, [e.target.name]: e.target.value }))
  }
  async function createNewPost() {
    if (!title || !content) return
    const user = supabase.auth.user()
    const id = uuid()
    post.id = id
    const { data } = await supabase
      .from('posts')
      .insert([
          { title, content, user_id: user.id, user_email: user.email }
      ])
      .single()
    router.push(`/posts/${data.id}`)
  }
  return (
    <div>
      <h1 className="text-3xl font-semibold tracking-wide mt-6">Créer un nouveau post</h1>
      <input
        onChange={onChange}
        name="title"
        placeholder="Titre"
        value={post.title}
        className="border-b pb-2 text-lg my-4 focus:outline-none w-full font-light text-gray-500 placeholder-gray-500 y-2"
      /> 
      <SimpleMDE
        value={post.content}
        onChange={value => setPost({ ...post, content: value })}
      />
      <button
        type="button"
        className="mb-4 bg-green-600 text-white font-semibold px-8 py-2 rounded-lg"
        onClick={createNewPost}
      >Créer le Post</button>
    </div>
  )
}

export default CreatePost
```

Ce composant affiche un éditeur Markdown, permettant aux utilisateurs de créer de nouveaux posts.

La fonction `createNewPost` utilisera l'instance `supabase` pour créer de nouveaux posts en utilisant l'état du formulaire local. 

Vous pouvez remarquer que nous ne passons aucun en-tête. Cela est dû au fait que si un utilisateur est connecté, les bibliothèques clientes Supabase incluent automatiquement le jeton d'accès dans les en-têtes pour un utilisateur connecté.

### Comment afficher un seul post

Nous devons configurer une page pour afficher un seul post.

Cette page utilise `getStaticPaths` pour créer dynamiquement des pages au moment de la construction en fonction des posts provenant de l'API.

Nous utilisons également le drapeau `fallback` pour activer les routes de secours pour la génération de pages SSG dynamiques.

Nous utilisons `getStaticProps` pour permettre aux données du Post d'être récupérées puis passées à la page en tant que props au moment de la construction.

Créez un nouveau dossier dans le répertoire **pages** appelé **posts** et un fichier appelé **[id].js** dans ce dossier. Dans **pages/posts/[id].js**, ajoutez le code suivant :

```javascript
// pages/posts/[id].js
import { useRouter } from 'next/router'
import ReactMarkdown from 'react-markdown'
import { supabase } from '../../api'

export default function Post({ post }) {
  const router = useRouter()
  if (router.isFallback) {
    return <div>Chargement...</div>
  }
  return (
    <div>
      <h1 className="text-5xl mt-4 font-semibold tracking-wide">{post.title}</h1>
      <p className="text-sm font-light my-4">par {post.user_email}</p>
      <div className="mt-8">
        <ReactMarkdown className='prose' children={post.content} />
      </div>
    </div>
  )
}

export async function getStaticPaths() {
  const { data, error } = await supabase
    .from('posts')
    .select('id')
  const paths = data.map(post => ({ params: { id: JSON.stringify(post.id) }}))
  return {
    paths,
    fallback: true
  }
}

export async function getStaticProps ({ params }) {
  const { id } = params
  const { data } = await supabase
    .from('posts')
    .select()
    .filter('id', 'eq', id)
    .single()
  return {
    props: {
      post: data
    }
  }
}
```

### Comment interroger et afficher la liste des posts

Ensuite, mettons à jour **index.js** pour récupérer et afficher une liste de posts :

```javascript
// pages/index.js
import { useState, useEffect } from 'react'
import Link from 'next/link'
import { supabase } from '../api'

export default function Home() {
  const [posts, setPosts] = useState([])
  const [loading, setLoading] = useState(true)
  useEffect(() => {
    fetchPosts()
  }, [])
  async function fetchPosts() {
    const { data, error } = await supabase
      .from('posts')
      .select()
    setPosts(data)
    setLoading(false)
  }
  if (loading) return <p className="text-2xl">Chargement ...</p>
  if (!posts.length) return <p className="text-2xl">Aucun post.</p>
  return (
    <div>
      <h1 className="text-3xl font-semibold tracking-wide mt-6 mb-2">Posts</h1>
      {
        posts.map(post => (
          <Link key={post.id} href={`/posts/${post.id}`}>
            <div className="cursor-pointer border-b border-gray-300	mt-8 pb-4">
              <h2 className="text-xl font-semibold">{post.title}</h2>
              <p className="text-gray-500 mt-2">Auteur : {post.user_email}</p>
            </div>
          </Link>)
        )
      }
    </div>
  )
}
```

### Testons-le

Nous avons maintenant toutes les pièces de notre application prêtes à être utilisées, alors essayons-la.

Pour exécuter le serveur local, exécutez la commande `dev` depuis votre terminal :

```sh
npm run dev
```

Lorsque l'application se charge, vous devriez voir l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/SS1-1.png)

Pour vous inscrire, cliquez sur **Profil** et créez un nouveau compte. Vous devriez recevoir un lien par email pour confirmer votre compte après votre inscription.

Vous pouvez également créer un nouveau compte en utilisant le lien magique.

Une fois connecté, vous devriez être en mesure de créer de nouveaux posts :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/SS2.png)

En revenant à la page d'accueil, vous devriez être en mesure de voir une liste des posts que vous avez créés et être en mesure de cliquer sur un lien vers le post pour le consulter :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/SS3.png)

## Comment modifier les posts

Maintenant que nous avons l'application en cours d'exécution, apprenons à modifier les posts. Pour commencer, créons une nouvelle vue qui récupérera uniquement les posts que l'utilisateur connecté a créés.

Pour ce faire, créez un nouveau fichier nommé **my-posts.js** à la racine du projet avec le code suivant :

```javascript
// pages/my-posts.js
import { useState, useEffect } from 'react'
import Link from 'next/link'
import { supabase } from '../api'

export default function MyPosts() {
  const [posts, setPosts] = useState([])
  useEffect(() => {
    fetchPosts()
  }, [])

  async function fetchPosts() {
    const user = supabase.auth.user()
    const { data } = await supabase
      .from('posts')
      .select('*')
      .filter('user_id', 'eq', user.id)
    setPosts(data)
  }
  async function deletePost(id) {
    await supabase
      .from('posts')
      .delete()
      .match({ id })
    fetchPosts()
  }
  return (
    <div>
      <h1 className="text-3xl font-semibold tracking-wide mt-6 mb-2">Mes Posts</h1>
      {
        posts.map((post, index) => (
          <div key={index} className="border-b border-gray-300	mt-8 pb-4">
            <h2 className="text-xl font-semibold">{post.title}</h2>
            <p className="text-gray-500 mt-2 mb-2">Auteur : {post.user_email}</p>
            <Link href={`/edit-post/${post.id}`}><a className="text-sm mr-4 text-blue-500">Modifier le Post</a></Link>
            <Link href={`/posts/${post.id}`}><a className="text-sm mr-4 text-blue-500">Voir le Post</a></Link>
            <button
              className="text-sm mr-4 text-red-500"
              onClick={() => deletePost(post.id)}
            >Supprimer le Post</button>
          </div>
        ))
      }
    </div>
  )
}
```

Dans la requête pour les `posts`, nous utilisons l'`id` de l'utilisateur pour sélectionner uniquement les posts créés par l'utilisateur connecté.

Ensuite, créez un nouveau dossier nommé **edit-post** dans le répertoire **pages**. Ensuite, créez un fichier nommé **[id].js** dans ce dossier.

Dans ce fichier, nous accéderons à l'`id` du post à partir d'un paramètre de route. Lorsque le composant se charge, nous utiliserons l'id du post de la route pour récupérer les données du post et les rendre disponibles pour l'édition.

Dans ce fichier, ajoutez le code suivant :

```javascript
// pages/edit-post/[id].js
import { useEffect, useState } from 'react'
import { useRouter } from 'next/router'
import dynamic from 'next/dynamic'
import "easymde/dist/easymde.min.css"
import { supabase } from '../../api'

const SimpleMDE = dynamic(() => import('react-simplemde-editor'), { ssr: false })

function EditPost() {
  const [post, setPost] = useState(null)
  const router = useRouter()
  const { id } = router.query

  useEffect(() => {
    fetchPost()
    async function fetchPost() {
      if (!id) return
      const { data } = await supabase
        .from('posts')
        .select()
        .filter('id', 'eq', id)
        .single()
      setPost(data)
    }
  }, [id])
  if (!post) return null
  function onChange(e) {
    setPost(() => ({ ...post, [e.target.name]: e.target.value }))
  }
  const { title, content } = post
  async function updateCurrentPost() {
    if (!title || !content) return
    await supabase
      .from('posts')
      .update([
          { title, content }
      ])
      .match({ id })
    router.push('/my-posts')
  }
  return (
    <div>
      <h1 className="text-3xl font-semibold tracking-wide mt-6 mb-2">Modifier le post</h1>
      <input
        onChange={onChange}
        name="title"
        placeholder="Titre"
        value={post.title}
        className="border-b pb-2 text-lg my-4 focus:outline-none w-full font-light text-gray-500 placeholder-gray-500 y-2"
      /> 
      <SimpleMDE value={post.content} onChange={value => setPost({ ...post, content: value })} />
      <button
        className="mb-4 bg-blue-600 text-white font-semibold px-8 py-2 rounded-lg"
        onClick={updateCurrentPost}>Mettre à jour le Post</button>
    </div>
  )
}

export default EditPost
```

Maintenant, ajoutez un nouveau lien à notre navigation située dans **pages/_app.js** :

```javascript
// pages/_app.js
{
  user && (
    <Link href="/my-posts">
      <span className="mr-6 cursor-pointer">Mes Posts</span>
    </Link>
  )
}
```

Lorsque vous exécutez l'application, vous devriez être en mesure de voir vos propres posts, de les modifier et de les supprimer depuis l'interface utilisateur mise à jour.

### Comment activer les mises à jour en temps réel

Maintenant que nous avons l'application en cours d'exécution, il est trivial d'ajouter des mises à jour en temps réel.

Par défaut, Realtime est désactivé sur votre base de données. Activons Realtime pour la table **posts**.

Pour ce faire, ouvrez le tableau de bord de l'application et cliquez sur **Databases** -> **Replication** -> **0 Tables** (sous Source). Activez la fonctionnalité Realtime pour la table **posts**. [Voici](https://supabase.io/docs/guides/api#managing-realtime) une vidéo expliquant comment vous pouvez faire cela pour plus de clarté.

Ensuite, ouvrez **src/index.js** et mettez à jour le hook `useEffect` avec le code suivant :

```
  useEffect(() => {
    fetchPosts()
    const mySubscription = supabase
      .from('posts')
      .on('*', () => fetchPosts())
      .subscribe()
    return () => supabase.removeSubscription(mySubscription)
  }, [])
```

Maintenant, nous serons abonnés aux changements en temps réel dans la table **posts**.

> Le code de l'application se trouve [ici](https://github.com/dabit3/supabase-next.js).

## Prochaines étapes

À ce stade, vous devriez avoir une bonne compréhension de la façon de construire des applications full stack avec Supabase et Next.js.

Si vous souhaitez en savoir plus sur la construction d'applications full stack avec Supabase, je vous invite à consulter les ressources suivantes.

* [Documentation Supabase](https://supabase.io/docs)
* [Projets d'exemple Supabase](https://github.com/supabase/supabase/tree/master/examples)
* [Supabase est-il légitime ? Analyse de l'alternative à Firebase](https://www.youtube.com/watch?v=WiwfiVdfRIc)
* [Plongée profonde dans l'authentification Supabase Partie 1 : JWTs](https://www.youtube.com/watch?v=v3Exg5YpJvE)
* [Construire en public 001 - Construire un tutoriel Next.js + Supabase](https://www.youtube.com/watch?v=p561ogKZ63o)
* [Plongée profonde dans l'authentification](https://supabase.io/docs/learn/auth-deep-dive/auth-deep-dive-jwts)
* [Supabase et Sveltekit](https://www.youtube.com/watch?v=j4AV2Liojk0)
* [Utiliser Supabase dans Replit avec node.js](https://www.youtube.com/watch?v=lQ5iIxaYduI)