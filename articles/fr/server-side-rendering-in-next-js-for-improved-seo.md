---
title: Comment utiliser le Server-Side Rendering dans les applications Next.js pour
  un meilleur SEO
date: '2024-07-17T18:02:11.000Z'
author: Joan Ayebola
authorURL: https://www.freecodecamp.org/news/author/joanayebola/
originalURL: https://freecodecamp.org/news/server-side-rendering-in-next-js-for-improved-seo
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/How-to-Use-Server-Side-Rendering-in-Next.js-Apps-for-Better-SEO-Cover-Image.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: SEO
  slug: seo
- name: Server side rendering
  slug: server-side-rendering
seo_desc: "Server-side rendering (SSR) is a web development technique that can help\
  \ improve your site's SEO. It does this by generating HTML content on the server\
  \ in response to a user's request. \nThis approach contrasts with client-side rendering\
  \ (CSR), where ..."
---


Le Server-Side Rendering (SSR) est une technique de développement web qui peut aider à améliorer le SEO de votre site. Elle y parvient en générant le contenu HTML sur le serveur en réponse à la requête d'un utilisateur.

<!-- more -->

Cette approche contraste avec le Client-Side Rendering (CSR), où le contenu est livré sous forme d'une coquille HTML de base, et où le JavaScript récupère et affiche les données dans le navigateur.

Le SSR offre des avantages significatifs en termes de SEO, ce qui en fait un choix idéal pour Next.js, un framework React populaire. Voyons comment l'utilisation du SSR avec Next.js peut améliorer la visibilité de votre site web sur les moteurs de recherche.

### Table des matières

1.  [Qu'est-ce que le Server-Side Rendering ?][1]
2.  [Comment débuter avec Next.js et le SSR][2]
3.  [Comment Next.js permet le Server-Side Rendering][3]
4.  [Récupération de données avec getStaticProps et getServerSideProps][4]
5.  [Avantages du SSR pour le SEO avec Next.js et comment optimiser][5]
6.  [Conclusion][6]

## Qu'est-ce que le Server-Side Rendering ?

Le Server-Side Rendering (SSR) est une technique de développement web où le serveur web génère le contenu HTML complet d'une page web avant de l'envoyer au navigateur de l'utilisateur.

Cela diffère du Client-Side Rendering (CSR), où le navigateur télécharge une structure HTML de base puis utilise JavaScript pour récupérer et afficher le contenu.

## Comment débuter avec Next.js et le SSR

Débuter avec Next.js et le Server-Side Rendering (SSR) implique quelques étapes. Voici un guide étape par étape pour vous aider à configurer un projet Next.js et à implémenter le SSR.

### Étape 1 : Installer Next.js

Tout d'abord, vous devez installer Next.js. Vous pouvez le faire en utilisant `create-next-app`, qui configure un nouveau projet Next.js avec une configuration par défaut. Exécutez la commande suivante dans votre terminal :

```
npx create-next-app my-next-app
cd my-next-app
npm run dev
```

Cette commande crée une nouvelle application Next.js dans un dossier nommé `my-next-app` et démarre le serveur de développement.

### Étape 2 : Comprendre la structure du projet

Next.js organise le projet avec certains dossiers et fichiers par défaut :

-   **`pages/`** : Ce dossier contient toutes les pages de votre application. Chaque fichier représente une route dans votre application.
-   **`public/`** : Les ressources statiques comme les images peuvent être placées ici.
-   **`styles/`** : Contient les fichiers CSS pour le stylisage de votre application.

### Étape 3 : Créer une page simple avec le SSR

Maintenant, créons une page simple qui utilise le SSR.

Créez un nouveau fichier `pages/index.js` :

```
// pages/index.js
import React from 'react';

const Home = ({ data }) => {
  return (
    <div>
      <h1>Welcome to Next.js with SSR</h1>
      <p>Data fetched from the server: {data.message}</p>
    </div>
  );
};

export async function getServerSideProps() {
  // Fetch data from an API or other sources
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();

  // Return the data as props to the Home component
  return {
    props: {
      data,
    },
  };
}

export default Home;
```

Analysons ce code en détail. Pour le composant `home` :

-   Le composant `Home` est un composant fonctionnel qui accepte des `props`.
-   La prop `data` contient les données récupérées depuis le serveur.
-   À l'intérieur du composant, nous affichons un message de bienvenue et les données récupérées.

La fonction `getServerSideProps` :

-   Cette fonction est exportée depuis le fichier `pages/index.js`.
-   Elle s'exécute sur le serveur pour chaque requête vers cette page.
-   À l'intérieur de cette fonction, vous pouvez effectuer des opérations asynchrones telles que la récupération de données depuis une API externe.
-   Les données récupérées sont renvoyées sous forme d'objet avec une clé `props`. Cet objet sera transmis au composant `Home` en tant que props.

Vous pouvez ajouter une gestion des erreurs à la fonction `getServerSideProps` pour gérer les problèmes qui pourraient survenir lors de la récupération des données. Voici un exemple :

```
export async function getServerSideProps() {
  try {
    const res = await fetch('https://api.example.com/data');
    if (!res.ok) {
      throw new Error('Failed to fetch data');
    }
    const data = await res.json();
    return {
      props: {
        data,
      },
    };
  } catch (error) {
    console.error(error);
    return {
      props: {
        data: { message: 'Error fetching data' },
      },
    };
  }
}
```

#### Étape 4 : Exécuter l'application

Démarrez votre serveur de développement s'il n'est pas déjà en cours d'exécution :

```
npm run dev
```

Ouvrez votre navigateur et allez sur `http://localhost:3000`. Vous devriez voir le message récupéré de l'API affiché sur la page.

## Comment Next.js permet le Server-Side Rendering

Next.js offre un moyen fluide d'activer le SSR et le Static Site Generation (SSG). Il pré-rend chaque page par défaut. Selon le cas d'utilisation, vous pouvez choisir entre le SSR et le SSG :

-   **Server-Side Rendering (SSR)** : Les pages sont rendues à chaque requête.
-   **Static Site Generation (SSG)** : Les pages sont générées au moment du build.

Next.js détermine quelle méthode de rendu utiliser en fonction des fonctions que vous implémentez dans vos composants de page (`getStaticProps` et `getServerSideProps`).

### Composants de page Next.js

Next.js utilise le répertoire `pages/` pour définir les routes. Chaque fichier dans ce répertoire correspond à une route dans votre application.

-   `pages/index.js` → `/`
-   `pages/about.js` → `/about`
-   `pages/posts/[id].js` → `/posts/:id`

Voici un exemple basique d'un composant de page :

```
// pages/index.js
import React from 'react';

const Home = () => {
  return (
    <div>
      <h1>Welcome to Next.js</h1>
      <p>This is the home page.</p>
    </div>
  );
};

export default Home;
```

### Récupération de données avec `getStaticProps` et `getServerSideProps`

`getStaticProps` est utilisé pour la génération statique. Il s'exécute au moment du build et vous permet de récupérer des données et de les transmettre à votre page en tant que props. Utilisez ceci pour les données qui ne changent pas souvent.

Exemple :

```
// pages/index.js
import React from 'react';

const Home = ({ posts }) => {
  return (
    <div>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
};

// This function runs at build time
export async function getStaticProps() {
  // Fetch data from an API
  const res = await fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = await res.json();

  return {
    props: {
      posts,
    },
  };
}

export default Home;
```

`getServerSideProps` est utilisé pour le Server-Side Rendering. Il s'exécute à chaque requête et vous permet de récupérer des données au moment de la requête.

Exemple :

```
// pages/index.js
import React from 'react';

const Home = ({ data }) => {
  return (
    <div>
      <h1>Server-Side Rendering with Next.js</h1>
      <p>Data fetched from the server: {data.message}</p>
    </div>
  );
};

// This function runs on every request
export async function getServerSideProps() {
  // Fetch data from an external API
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();

  return {
    props: {
      data,
    },
  };
}

export default Home;
```

## Avantages du SSR pour le SEO avec Next.js et comment optimiser

Dans cette section, nous examinerons les principaux avantages de l'utilisation du SSR pour le SEO et donnerons des conseils faciles à suivre sur la manière de tirer le meilleur parti de ces avantages avec votre application Next.js.

### 1. Indexation améliorée par les moteurs de recherche

Le Client-Side Rendering (CSR) peut causer des problèmes, car les moteurs de recherche ont parfois du mal à indexer correctement le contenu puisqu'il est rendu dans le navigateur de l'utilisateur via JavaScript.

Le SSR, en revanche, rend le contenu sur le serveur avant de l'envoyer au navigateur de l'utilisateur, garantissant que le HTML est complet et peut être facilement exploré et indexé par les moteurs de recherche.

**Utilisez le SSR pour les pages importantes :** Assurez-vous que les pages clés, telles que les pages d'atterrissage (landing pages), les articles de blog et les pages de produits, sont rendues sur le serveur pour faciliter une meilleure indexation.

Exemple – Utilisation du SSR pour une page d'article de blog :

```
// pages/blog/[id].js
import React from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';

const BlogPost = ({ post }) => {
  const router = useRouter();
  if (router.isFallback) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <Head>
        <title>{post.title}</title>
        <meta name="description" content={post.excerpt} />
      </Head>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </div>
  );
};

export async function getServerSideProps({ params }) {
  const res = await fetch(`https://api.example.com/posts/${params.id}`);
  const post = await res.json();

  return {
    props: {
      post,
    },
  };
}

export default BlogPost
```

-   **Composant BlogPost :** Ce composant affiche un article de blog. Il utilise `next/head` pour gérer les balises meta, qui sont cruciales pour le SEO.
-   **Fonction getServerSideProps :** Cette fonction récupère les données de l'article de blog depuis une API. Elle s'exécute sur le serveur pour chaque requête vers cette page, garantissant que le contenu est prêt pour l'indexation par les moteurs de recherche lorsqu'ils explorent la page.

### 2. Temps de chargement plus rapides

Les moteurs de recherche comme Google utilisent la vitesse de chargement des pages comme facteur de classement. Le SSR peut améliorer le temps de chargement initial car le serveur envoie une page entièrement rendue au navigateur, améliorant ainsi la performance perçue et l'expérience utilisateur.

**Optimisez le temps de réponse du serveur :** Assurez-vous que votre serveur est optimisé pour des réponses rapides. Utilisez des stratégies de mise en cache pour réduire la charge du serveur.

Exemple – en-tête cache-control pour le SSR :

```
export async function getServerSideProps({ res }) {
  res.setHeader('Cache-Control', 'public, s-maxage=10, stale-while-revalidate=59');

  const resData = await fetch('https://api.example.com/data');
  const data = await resData.json();

  return {
    props: {
      data,
    },
  };
}
```

-   **Fonction `getServerSideProps` :** Cette fonction définit des en-têtes cache-control pour mettre en cache la réponse pendant 10 secondes et servir un contenu périmé tout en revalidant pendant 59 secondes. Cela améliore le temps de réponse du serveur et la vitesse de chargement de la page, contribuant à un meilleur SEO.

### 3. Partage amélioré sur les réseaux sociaux

Lors du partage de liens sur les réseaux sociaux, des plateformes comme Facebook et Twitter analysent (scrappent) le contenu de l'URL pour générer des aperçus. Le SSR garantit que les métadonnées nécessaires sont disponibles dans le HTML initial, ce qui permet d'obtenir de meilleurs aperçus et d'augmenter les taux de clics.

**Gérez les balises meta avec `next/head` :** Utilisez le composant `next/head` pour ajouter des balises meta pour les réseaux sociaux et le SEO.

Exemple – Ajout de balises meta à une page :

```
import Head from 'next/head';

const Page = ({ data }) => (
  <div>
    <Head>
      <title>{data.title}</title>
      <meta name="description" content={data.description} />
      <meta property="og:title" content={data.title} />
      <meta property="og:description" content={data.description} />
      <meta property="og:image" content={data.image} />
      <meta name="twitter:card" content="summary_large_image" />
    </Head>
    <h1>{data.title}</h1>
    <p>{data.content}</p>
  </div>
);
```

-   **Composant `Page` :** Ce composant utilise `next/head` pour ajouter des balises meta SEO, y compris des balises Open Graph pour les aperçus sur les réseaux sociaux. Cela garantit que lorsque la page est partagée, les plateformes sociales peuvent générer des aperçus riches avec les métadonnées fournies.

### 4. Expérience utilisateur améliorée

Un site web plus rapide et plus réactif améliore l'expérience utilisateur globale, ce qui conduit à des durées de visite plus longues et à des taux de rebond plus faibles. Ces deux facteurs influencent positivement vos classements SEO.

**Pré-rendez les pages avec la génération statique (SSG) pour le contenu moins dynamique :** Utilisez le SSG pour les pages qui ne changent pas souvent afin de réduire la charge du serveur et d'améliorer les performances.

Exemple – Utilisation du SSG pour une page statique :

```
export async function getStaticProps() {
  const res = await fetch('https://api.example.com/static-data');
  const data = await res.json();

  return {
    props: {
      data,
    },
    revalidate: 10, // Revalidate at most once every 10 seconds
  };
}

const StaticPage = ({ data }) => (
  <div>
    <h1>{data.title}</h1>
    <p>{data.content}</p>
  </div>
);

export default StaticPage;
```

-   **Composant `StaticPage` :** Ce composant affiche un contenu statique récupéré depuis une API.
-   **Fonction `getStaticProps` :** Cette fonction récupère les données au moment du build et les revalide toutes les 10 secondes, garantissant que le contenu est toujours frais tout en réduisant la charge du serveur.

## Conclusion

L'utilisation conjointe du Server-Side Rendering et de Next.js revient à donner un coup de pouce supplémentaire à votre site web pour les moteurs de recherche. Avec un contenu pré-construit pour les robots et une expérience fluide pour les visiteurs, votre site est paré pour être vu par plus de personnes naturellement.

Cela fonctionne parfaitement pour tout type de site web, des boutiques en ligne aux blogs. Next.js avec SSR facilite la création d'un site web que les moteurs de recherche adorent et que les utilisateurs apprécient.

C'est tout pour cet article ! Si vous souhaitez poursuivre la conversation ou si vous avez des questions, des suggestions ou des commentaires, n'hésitez pas à me contacter sur [LinkedIn][7]. Et si vous avez apprécié ce contenu, n'hésitez pas à [m'offrir un café][8] pour soutenir la création de contenus plus adaptés aux développeurs.

[1]: #heading-qu-est-ce-que-le-server-side-rendering
[2]: #heading-comment-debuter-avec-nextjs-et-le-ssr
[3]: #heading-comment-nextjs-permet-le-server-side-rendering
[4]: #heading-recuperation-de-donnees-avec-getstaticprops-et-getserversideprops
[5]: #heading-avantages-du-ssr-pour-le-seo-avec-nextjs-et-comment-optimiser
[6]: #heading-conclusion
[7]: https://ng.linkedin.com/in/joan-ayebola
[8]: https://www.buymeacoffee.com/joanayebola