---
title: Le routage dans Next.js – Un guide complet pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-05T17:12:51.000Z'
originalURL: https://freecodecamp.org/news/routing-in-nextjs-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/cover-1--2-.png
tags:
- name: Next.js
  slug: nextjs
- name: React
  slug: react
- name: routing
  slug: routing
seo_title: Le routage dans Next.js – Un guide complet pour débutants
seo_desc: "By Ibrahima Ndaw\nNext.js is a React framework that ships with all the\
  \ features you need for production. It enables routing in your app by using the\
  \ file-system-based routing. \nIn this guide, I will show you how routing works\
  \ in Next.js.\n\nHow Routing ..."
---

Par Ibrahima Ndaw

Next.js est un framework React qui inclut toutes les fonctionnalités dont vous avez besoin pour la production. Il permet le routage dans votre application en utilisant le routage basé sur le système de fichiers.

Dans ce guide, je vais vous montrer comment fonctionne le routage dans Next.js.

* [Comment fonctionne le routage dans Next.js](#heading-comment-fonctionne-le-routage-dans-nextjs)
* [Lier les pages entre elles](#lier-les-pages-entre-elles)
* [Passer des paramètres de route](#passer-des-parametres-de-route)
* [Routes dynamiques](#heading-routes-dynamiques)
* [Routes dynamiques imbriquées](#heading-routes-dynamiques-imbriquees)

## Comment fonctionne le routage dans Next.js

Next.js utilise le système de fichiers pour activer le routage dans l'application. Next traite automatiquement chaque fichier avec les extensions `.js`, `.jsx`, `.ts` ou `.tsx` sous le répertoire `pages` comme une route.

Une page dans Next.js est un composant React qui a une route basée sur son nom de fichier.

Prenons cette structure de dossiers comme exemple :

```
├── pages
│  ├── index.js
│  ├── contact.js
│  └── my-folder
│     ├── about.js
│     └── index.js

```

Ici, nous avons quatre pages :

* `index.js` est la page d'accueil accessible sur [http://localhost:3000](http://localhost:3000)
* `contact.js` est la page de contact accessible sur [http://localhost:3000/contact](http://localhost:3000/contact)
* `my-folder/index.js` est la page située dans le sous-dossier _my-folder_ accessible sur [http://localhost:3000/my-folder](http://localhost:3000/my-folder)
* `my-folder/about.js` est la page à propos située dans le sous-dossier _my-folder_ accessible sur [http://localhost:3000/my-folder/about](http://localhost:3000/my-folder/about)

## Comment lier les pages entre elles

Par défaut, Next.js pré-rend chaque page pour rendre votre application rapide et conviviale. Il utilise le composant `Link` fourni par _next/link_ pour permettre les transitions entre les routes.

```jsx
import Link from "next/link"

export default function IndexPage() {
  return (
    <div>
      <Link href="/contact">
        <a>Ma deuxième page</a>
      </Link>
      <Link href="/my-folder/about">
        <a>Ma troisième page</a>
      </Link>
    </div>
  )
}

```

Ici, nous avons deux routes :

* Le premier lien mène à la page `http://localhost:3000/contact`
* Le deuxième lien mène à la page `http://localhost:3000/my-folder/about`

Le composant `Link` peut recevoir plusieurs propriétés, mais seul l'attribut `href` est requis. Ici, nous utilisons une balise `<a></a>` comme composant enfant pour lier les pages. Mais vous pouvez également utiliser n'importe quel élément qui supporte l'événement `onClick` sur le composant `Link`.

## Comment passer des paramètres de route

Next.js vous permet de passer des paramètres de route et de récupérer les données en utilisant le hook `useRouter` ou `getInitialProps`. Cela vous donne accès à l'objet router qui contient les paramètres.

* index.js

```jsx
import Link from "next/link"

export default function IndexPage() {
  return (
    <Link
      href={{
        pathname: "/about",
        query: { id: "test" },
      }}
    >
      <a>Page à propos</a>
    </Link>
  )
}

```

Comme vous pouvez le voir ici, au lieu de fournir une chaîne de caractères à l'attribut `href`, nous passons un objet qui contient une propriété `pathname`. Il s'agit de la route, ainsi qu'un élément query qui contient les données.

* about.js

```jsx
import { useRouter } from "next/router"

export default function AboutPage() {
  const router = useRouter()
  const {
    query: { id },
  } = router
  return <div>À propos de nous : {id}</div>
}

```

Ici, nous importons le hook `useRouter` pour obtenir les données passées. Ensuite, nous les extrayons de l'objet `query` en utilisant la destructuration.

Si vous utilisez le rendu côté serveur, vous devez utiliser `getInitialProps` pour obtenir les données.

```jsx
export default function AboutPage({ id }) {
  return <div>À propos de nous : {id}</div>
}

AboutPage.getInitialProps = ({ query: { id } }) => {
  return { id }
}

```

## Routes dynamiques

Next.js vous permet de définir des routes dynamiques dans votre application en utilisant les crochets (`[param]`). Au lieu de définir un nom statique sur vos pages, vous pouvez utiliser un nom dynamique.

Prenons cette structure de dossiers comme exemple :

```
├── pages
│  ├── index.js
│  ├── [slug].js
│  └── my-folder
│     ├── [id].js
│     └── index.js

```

Next.js récupérera les paramètres de route passés et les utilisera comme nom pour la route.

* index.js

```jsx
export default function IndexPage() {
  return (
    <ul>
      <li>
        <Link href="/">
          <a>Accueil</a>
        </Link>
      </li>
      <li>
        <Link href="/[slug]" as="/my-slug">
          <a>Première route</a>
        </Link>
      </li>
      <li>
        <Link href="/my-folder/[id]" as="/my-folder/my-id">
          <a>Deuxième route</a>
        </Link>
      </li>
    </ul>
  )
}

```

Ici, nous devons définir la valeur sur l'attribut `as` car le chemin est dynamique. Le nom de la route sera ce que vous définissez sur la propriété `as`.

* [slug].js

```jsx
import { useRouter } from "next/router"

export default function DynamicPage() {
  const router = useRouter()
  const {
    query: { id },
  } = router
  return <div>La route dynamique est {id}</div>
}

```

Vous pouvez également obtenir les paramètres de route avec le hook `useRouter` côté client ou `getInitialProps` côté serveur.

* my-folder/[id].js

```jsx
export default function MyDynamicPage({ example }) {
  return <div>Mon exemple est {example}</div>
}

MyDynamicPage.getInitialProps = ({ query: { example } }) => {
  return { example }
}

```

Ici, nous utilisons `getInitialProps` pour obtenir la route dynamique passée.

## Routes dynamiques imbriquées

Avec Next.js, vous pouvez également imbriquer des routes dynamiques avec les crochets (`[param]`).

Prenons cette structure de fichiers :

```
├── pages
│  ├── index.js
│  └── [dynamic]
│     └── [id].js

```

* index.js

```jsx
export default function IndexPage() {
  return (
    <ul>
      <li>
        <Link href="/">
          <a>Accueil</a>
        </Link>
      </li>
      <li>
        <Link href="/[dynamic]/[id]" as="/my-folder/my-id">
          <a>Route dynamique imbriquée</a>
        </Link>
      </li>
    </ul>
  )
}

```

Comme vous pouvez le voir ici, nous définissons les valeurs dynamiques sur l'attribut `as` comme nous l'avons fait dans l'exemple précédent. Mais cette fois, nous devons définir le nom du dossier et de son fichier.

```jsx
import { useRouter } from "next/router"

export default function DynamicPage() {
  const router = useRouter()
  const {
    query: { dynamic, id },
  } = router
  return (
    <div>
      Données : {dynamic} - {id}
    </div>
  )
}

```

Ici, nous extrayons les paramètres de route de l'objet query avec le hook `useRouter`.

C'est tout ! Merci d'avoir lu.

Si vous êtes intéressé à apprendre Next.js de manière complète, je vous recommande vivement ce [cours best-seller](https://click.linksynergy.com/deeplink?id=o1JCNdqL0gw&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Freact-the-complete-guide-incl-redux%2F).

Vous pouvez trouver d'autres contenus intéressants comme celui-ci sur [mon blog](https://www.ibrahima-ndaw.com) ou me suivre [sur Twitter](https://twitter.com/ibrahima92_) pour être notifié.

Photo par [Javier Allegue Barros](https://unsplash.com/@soymeraki?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/route?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)