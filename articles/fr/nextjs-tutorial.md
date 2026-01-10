---
title: Commencez avec Next.js – La bibliothèque React dont votre projet a besoin
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-01-14T21:39:10.000Z'
originalURL: https://freecodecamp.org/news/nextjs-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-14-at-2.17.23-PM.png
tags:
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Commencez avec Next.js – La bibliothèque React dont votre projet a besoin
seo_desc: 'I''ve composed this guide to give you a practical overview of perhaps the
  most important React library you will use to build 90% of your projects: Next.js.

  The goal of this tutorial is to get you started using Next.js as easily as possible.

  This is no...'
---

J'ai rédigé ce guide pour vous donner un aperçu pratique de peut-être la bibliothèque React la plus importante que vous utiliserez pour construire 90% de vos projets : Next.js.

**L'objectif de ce tutoriel est de vous faire commencer à utiliser Next.js aussi facilement que possible.**

Ce n'est pas un guide complet sur Next, mais il vous donnera tout ce dont vous avez besoin pour comprendre :

* Ce qu'est Next.js (et pourquoi vous devriez commencer à l'utiliser pour vos projets React)
* Comment effectuer des tâches essentielles en utilisant Next.js
* Plus comment Next.js vous aidera à construire des applications React globalement meilleures, plus rapidement

Commençons !

## Table des matières

* [Qu'est-ce que Next.js ?](#heading-quest-ce-que-nextjs)
* [Quelles fonctionnalités Next.js vous offre](#heading-quelles-fonctionnalités-nextjs-vous-offre)
* [Quelles fonctionnalités Next.js n'a pas](#heading-quelles-fonctionnalités-nextjs-na-pas)
* [Comment créer une application Next.js](#heading-comment-créer-une-application-nextjs)
* [Scripts Next.js](#heading-scripts-nextjs)
* [Ajouter TypeScript à Next.js](#heading-ajouter-typescript-à-nextjs)
* [Pages et routes](#heading-pages-et-routes)
* [Liens et navigation](#heading-liens-et-navigation)
* [SEO dans Next.js](#heading-seo-dans-nextjs)
* [Routes API](#heading-routes-api)
* [Demander des données côté client](#heading-demander-des-données-côté-client)
* [Demander des données côté serveur](#heading-demander-des-données-côté-serveur)
* [GetServerSideProps](#heading-getserversideprops)
* [GetStaticProps](#heading-getstaticprops)
* [Où apprendre Next.js](#heading-où-apprendre-nextjs)

## Qu'est-ce que Next.js ?

L'outil ultime pour tout développeur React à apprendre et améliorer ses propres projets est, sans aucun doute, **Next.js**.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-14-at-12.12.20-PM.png)
_La page d'accueil de NextJS.org_

Que je construise un site statique avec de l'interactivité comme un blog, ou un projet full-stack très dynamique comme une application de médias sociaux, _je me tourne presque toujours vers Next_.

La première raison pour vous d'utiliser Next est, comme l'indique le titre de la bannière, parce que c'est un **framework React**.

Pensez-y comme une façon "tout compris" de construire vos applications React, qui vous offre la simplicité d'outils comme Create React App, combinée à une suite d'autres fonctionnalités super puissantes.

Malgré le fait d'être un framework, Next.js conserve une partie de la philosophie React d'être non prescriptif. Next vous donne des fonctionnalités pour améliorer votre expérience de développement globale mais ne limite pas le nombre d'options parmi lesquelles vous pouvez choisir.

En fait, étant donné ce que Next rend possible pour les applications React, je soutiendrais qu'il a vraiment élargi le nombre d'options disponibles pour vous, si vous en avez besoin.

Vous pouvez vous faire une idée plus complète de tout ce dont les applications Next.js sont capables en consultant des centaines d'exemples de projets Next.js sur [nextjs.org/examples](https://nextjs.org/examples) :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-14-at-1.56.57-PM.png)
_Exemples Next.js_

Là, vous pouvez trouver des exemples sur la façon de créer les applications Next (React) suivantes :

* Un blog utilisant Markdown / MDX ou Wordpress
* Une application e-commerce utilisant Shopify
* Un site utilisant des systèmes de gestion de contenu comme Contentful ou Sanity
* Un projet full-stack avec GraphQL et authentification

Et bien plus encore ! Assurez-vous de consulter la liste complète pour stimuler votre imagination.

## Quelles fonctionnalités Next.js vous offre

Ci-dessous se trouve une liste des fonctionnalités que Next offre à vos projets React.

En bref, il fournit la fonctionnalité d'une suite complète de packages dans une seule dépendance `next`.

Next.js vous offre :

* Routage basé sur les pages (créer une page en plaçant des composants dans /pages)
* Un routeur intégré (pas besoin d'installer React Router)
* Routes API (écrire du code backend en utilisant Node.js dans /pages/api)
* Builds ultra-rapides pour le développement / la production (voir les changements sauvegardés instantanément)
* Optimisation des images et des polices
* Support intégré d'ESLint et de TypeScript
* + bien plus (tout est détaillé dans la [documentation Next.js](https://nextjs.org/docs/))

## Quelles fonctionnalités Next.js n'a pas

De plus, il y a beaucoup de choses essentielles que Next.js ne fournit pas directement.

Par exemple, il n'y a pas de moyen intégré pour faire ce qui suit dans Next :

* Authentification (je recommande d'utiliser le package Next-Auth)
* Tests (je recommande d'utiliser Playwright ou Cypress pour vos tests E2E)
* Gestion d'état (je recommande Zustand ou Redux Toolkit)

[La documentation elle-même](https://nextjs.org/docs/authentication) couvre ces lacunes, mais il est important de noter que bien que Next.js vous donne beaucoup **il ne couvrira pas seul tous les cas d'utilisation des applications**.

## Speedrun Next.js 💨

Je vais vous donner les points forts de Next.js pour vous donner une idée de la façon dont le framework vous offre de bonnes valeurs par défaut qui vous rendent plus productif.

## Comment créer une application Next.js

Si vous avez NPM installé, commencez tout nouveau projet Next avec la commande :

```bash
npx create-next-app mon-projet-next
```

`create-next-app` est un package comme Create React App, mais pour les projets Next.js.

En bref, il nous donne un projet Next avec toutes ses dépendances installées (qui sont `next`, `react`, et `react-dom`) plus quelques pages et styles factices.

## Scripts Next.js

Vous trouvez actuellement quatre scripts principaux listés dans votre fichier `package.json` :

```json
"scripts": {
  "dev": "next dev",
  "build": "next build",
  "start": "next start",
  "lint": "next lint"
}
```

* `dev` – exécute un serveur de développement sur localhost:3000
* `build` – crée une application construite prête pour le déploiement
* `start` – démarre votre application Next construite (vous devez d'abord exécuter `next build`)
* `lint` – "lint" votre projet Next en utilisant la dépendance de développement ESLint pour vous avertir si votre code écrit doit être corrigé

Pour exécuter votre projet Next en développement, assurez-vous d'être dans votre dossier de projet (mon-projet-next) et exécutez le script dev :

```bash
npm run dev
```

Après que votre projet soit opérationnel sur localhost:3000, naviguez jusqu'à celui-ci et vous devriez voir une application par défaut :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-14-at-2.41.23-PM.png)
_Page d'index du projet Create-Next-App_

## Ajouter TypeScript à Next.js

Vous voulez ajouter TypeScript ? Rien de plus simple :

```bash
# exécutez 'touch' pour créer un fichier de configuration vide
# Next le remplira automatiquement

touch tsconfig.json 

# puis vous serez invité à exécuter la commande :
npm install -D typescript @types/react @types/node

# maintenant vous pouvez utiliser TypeScript partout ✨
```

## Pages et routes

Vous voulez ajouter une page À propos à votre application ?

Il suffit de déposer votre composant dans /pages/about.js (.tsx si vous utilisez TypeScript) :

```jsx
// Pas besoin d'importer React ici ! 😳

export default function About() {
  return <div>À propos</div>
}
```

Et ça marche !

C'est un grand avantage car nous n'avons plus besoin d'installer une bibliothèque comme React Router qui nécessite du code boilerplate tel qu'un composant Router et Route, entre autres.

Si vous souhaitez des pages dynamiques, qui sont dans le même dossier mais ont des slugs différents (comme des articles de blog), Next nous permet de rendre le même composant de page en enveloppant le nom de fichier dans des crochets.

Par exemple, pour afficher des articles de blog selon un slug particulier, nous pourrions déposer un dossier "blog" dans pages avec le nom de fichier : [slug].js :

```jsx
import { useRouter } from 'next/router'

// si nous naviguons vers localhost:3000/blog/123...
export default function BlogPost() {
  const router = useRouter()
  const { slug } = router.query

  return <p>Poste : {slug}</p> // ...vous verrez "Poste : 123"
}
```

Next expose commodément un hook React `useRouter` pour faciliter l'accès aux informations sur l'emplacement ou l'historique de l'application.

Dans cet exemple, il nous permet d'obtenir les paramètres de requête (la valeur dynamique) à partir de `router.query`. Le nom de la propriété `slug` correspond au nom dynamique que nous avons donné à notre fichier : `[slug].js`.

> Note : Vous pouvez avoir plusieurs paramètres de requête en utilisant des dossiers imbriqués avec des noms dynamiques. Comme /blog/[topic]/[slug].js. À partir de [slug].js, nous pourrions accéder aux paramètres de requête `topic` et `slug`.

## Liens et navigation

Tout comme Next inclut des routes et un routage, le framework nous donne également un composant `Link` utile de `next/link`.

Cela peut sembler un peu inhabituel si vous venez de React Router, car il nécessite de placer un lien d'ancrage traditionnel en tant qu'enfant et de passer l'href en tant que prop.

Si nous voulions lier à la page d'accueil (/) et à une route de blog (c'est-à-dire /blog/123), nous inclurions ce qui suit dans /pages/about.js :

```js
import Link from "next/link";

export default function About() {
  return (
    <div>
      <h1>À propos de moi</h1>
      
      <div>
        <Link href="/">
          <a>Accueil</a>
        </Link>
        <Link href="/blog/123">
          <a>Mon article de blog</a>
        </Link>
      </div>
    </div>
  );
}

```

`href` est la seule prop requise pour le composant `Link` et les données peuvent lui être passées en tant qu'objet également :

```js
import Link from "next/link";

export default function About() {
  return (
    <div>
      <h1>À propos de moi</h1>

      <div>
        <Link href={{ pathname: "/about" }}>
          <a>Accueil</a>
        </Link>
        <Link
          href={{
            pathname: "/blog/[slug]",
            query: { slug: "123" },
          }}
        >
          <a>Mon article de blog</a>
        </Link>
      </div>
    </div>
  );
}

```

Les changements de route peuvent également être effectués en utilisant le hook `useRouter`, principalement en utilisant la méthode `.push()` pour pousser vers une route différente de manière programmatique.

Voici un exemple factice d'une page de connexion où un utilisateur fournit son email pour se connecter et est poussé vers la route '/verify-email' ensuite.

```js
export default function Login() {
  const router = useRouter()
    
  function onSubmit(event) {
    event.preventDefault();
    const email = event.target.elements.email.value;  
    await sendLoginEmail(email);    
    // pousser l'utilisateur vers la page /verify-email
    router.push('/verify-email');
  }
    
  return (
    <div>
      <h1>Connectez-vous ici</h1>

      <form onSubmit={onSubmit}>
        <input name="email" placeholder="Votre adresse email" />
        <button type="submit">Soumettre</button>
      </form>
    </div>
  );
}
```

## SEO dans Next.js

Les pages dans les applications web ont besoin non seulement de données dans le corps HTML, mais aussi de balises meta (head).

Dans une application Create React, cela nécessiterait d'installer une dépendance externe appelée React Helmet.

Dans Next, nous pouvons utiliser le composant `Head` de `next/head` pour ajouter commodément des métadonnées à nos pages web à afficher dans les résultats de recherche et les intégrations :

```js
import Link from "next/link";
import Head from "next/head";

export default function About() {
  return (
    <div>
      <Head>
      	<title>À propos | Mon site cool</title>
        <meta name="description" content="Vous devez vraiment lire ce site web car il est fait avec Next.js" />
      </Head>
      
      <h1>À propos de moi</h1>
      <div>
        <Link href="/">
          <a>Accueil</a>
        </Link>
        <Link href="/blog/123">
          <a>Mon article de blog</a>
        </Link>
      </div>
    </div>
  );
}
```

> Note : Le composant Head doit être inclus dans tout composant de page, généralement juste dans la balise d'ouverture. Vous pouvez créer un composant Head réutilisable qui accepte des valeurs dynamiques via des props.

## Routes API

Besoin d'un backend / API pour votre projet ? Pas de problème.

L'un des changements de jeu concernant Next est la façon dont il fournit une solution tout-en-un pour créer des applications React full-stack en vous donnant la possibilité d'écrire du code serveur en utilisant une fonctionnalité appelée **routes API**.

Pour écrire votre backend, ajoutez un dossier appelé "api" dans /pages pour créer votre propre API qui sont finalement exécutées en tant que fonctions serverless séparées.

Si nous voulions récupérer des données pour notre page à propos depuis /api/about, nous inclurions une page appelée about.js dans /pages/api :

```js
// la syntaxe est très similaire au framework "Express" Node.js

// ici nous répondons à chaque requête avec un code OK (200) et envoyons des données JSON en retour (notre nom)

export default function handler(req, res) {
  res.status(200).json({ name: "Reed Barger" });
}

```

## Demander des données côté client

Maintenant que nous avons une route API, comment l'utiliser ?

Comment demander des données depuis nos routes API et utiliser les données dans nos pages client ?

L'approche traditionnelle serait de les demander en utilisant `useEffect` et `useState` :

```js
import Link from "next/link";
import { useEffect, useState } from "react";

export default function About() {
  const [data, setData] = useState(null);
  const [isLoading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    fetch("api/about")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        setLoading(false);
      });
  }, []);

  if (isLoading) return <p>Chargement...</p>;
  if (!data) return <p>Aucune donnée à propos</p>;

  return (
    <div>
      <h1>Mon nom est : {data.name}</h1>
    </div>
  );
}
```

Cette approche fonctionne, mais nécessite beaucoup de code boilerplate. En plus de cela, elle n'offre pas la meilleure expérience utilisateur.

Bien que ce soit un exemple basique, si nous avions des informations dynamiques nécessaires à récupérer et à afficher dans nos pages, nous montrerions toujours le texte "Chargement" à nos utilisateurs à chaque visite de page.

Une meilleure façon de récupérer des données et de les capturer lors de futures visites est d'utiliser la bibliothèque SWR, qui est également faite par les développeurs de Next.

Elle nous donne un hook pratique `useSWR` pour récupérer plus facilement des données et gérer les états de chargement et d'erreurs, ainsi que mettre en cache les données pour les futures visites si rien n'a changé. Si cela a changé, récupérez les données en arrière-plan tandis que les données obsolètes sont affichées depuis le cache.

> Note : Le hook est nommé d'après cette stratégie de "cache invalidation" : "stale-while-revalidate"

Voici la même requête faite en utilisant SWR :

```js
import useSWR from "swr";

const fetcher = (...args) => fetch(...args).then((res) => res.json())

export default function About() {
  const { data, error } = useSWR("/api/about", fetcher)

  if (error) return <div>Erreur lors de la récupération des données</div>
  if (!data) return <div>Chargement...</div>

  return (
    <div>
      <h1>{data.name}</h1>
    </div>
  )
}
```

## Demander des données côté serveur

Quelle est la meilleure façon de récupérer des données dans Next qui améliore l'expérience utilisateur et le SEO globalement ?

Il y a deux fonctions que vous pouvez inclure directement dans vos fichiers de page qui nous permettent de récupérer des données depuis le serveur :

> Oui, ces fonctions sont dans le même fichier que nos composants React, mais le code pour elles est bundlé séparément de notre client React.

1. `getServerSideProps`
2. `getStaticProps`

## GetServerSideProps

`getServerSideProps` s'exécute à chaque visite de page. Par conséquent, il est très utile sur les pages avec des données dynamiques ou nécessitant des requêtes à chaque fois, comme l'obtention de données d'utilisateur authentifié.

```js
export default function About({ name }) {
  return (
    <div>
      <h1>Mon nom est : {name}</h1>
    </div>
  );
}

export function getServerSideProps() {
  return {
    props: { name: "Reed Barger" },
  };
}
```

La fonction fait exactement ce que son nom indique – elle nous permet d'envoyer des données depuis le serveur et les injecte dans les props de notre composant de page.

Ce qui est génial avec cette fonctionnalité, c'est qu'elle permet à notre client React d'afficher les données immédiatement, sans délai, et sans avoir à gérer un état de chargement ou d'erreur.

Si nous voulions récupérer des données depuis le serveur, nous pourrions le faire en rendant `getServerSideProps` asynchrone en utilisant le mot-clé `async`.

```js
export default function About({ name }) {
  return (
    <div>
      <h1>Mon nom est : {name}</h1>
    </div>
  );
}

export async function getServerSideProps() {
  const data = await fetch("https://randomuser.me/api").then((res) =>
    res.json()
  );

  return {
    props: { name: data.results[0].name.first },
  };
}
```

Ici, nous récupérons dynamiquement des données depuis l'[API random user](https://randomuser.me), et nos données changent à chaque fois que nous actualisons la page.

## GetStaticProps

Renommons notre fonction `getServerSideProps` avec le nom `getStaticProps`.

Encore une fois, la fonction fait ce que son nom dit. Ou est-ce le cas ?

`getStaticProps` est une fonction plus appropriée pour des pages plus statiques qui changent moins fréquemment. Cette fonction exécute notre code serveur et fait une requête GET sur le serveur, mais elle ne le fait qu'une seule fois lorsque notre projet est construit.

Cependant, lorsque vous exécutez l'application en développement, il semble qu'elle demande des données à chaque fois que nous actualisons la page comme `getServerSideProps`.

Il est important de noter que `getStaticProps` _ne fait des requêtes à chaque visite de page qu'en développement_.

Si vous exécutez `yarn build` puis exécutez la version de production de votre projet React en utilisant `yarn start`, vous verrez que peu importe le nombre de fois où nous actualisons, nous continuons à obtenir le même nom – le nom qui a été demandé lorsque le projet a été construit et non à l'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-14-at-3.59.19-PM.png)
_Résultat d'exemple demandé depuis getStaticProps_

Vous pourriez vous demander à ce stade : _"Pourquoi utiliser des routes API du tout avec ces deux fonctions ?"_

Il est important d'être conscient du fait que `getServerSideProps` et `getStaticProps` ne peuvent effectuer que des requêtes GET. Les routes API peuvent gérer tout type de requête pour lire et mettre à jour des données (c'est-à-dire lorsqu'elles sont combinées avec une couche de données comme une base de données).

## Où apprendre Next.js

Ce que nous avons couvert ici ne fait qu'effleurer la surface de Next, mais vous avez déjà acquis tout ce dont vous avez besoin pour commencer à utiliser Next dans vos projets React dès aujourd'hui.

Si vous voulez un guide plus approfondi et technique, le site officiel propose un [cours interactif](https://nextjs.org/learn/basics/create-nextjs-app) sur la façon d'apprendre Next.js dès le début.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-14-at-12.05.33-PM.png)
_Le cours (gratuit) d'apprentissage de Next.js_

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*