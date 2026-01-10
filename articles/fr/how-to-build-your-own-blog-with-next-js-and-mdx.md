---
title: Comment créer votre propre blog avec Next.js et MDX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-21T02:28:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-own-blog-with-next-js-and-mdx
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/thoughts.jpg
tags:
- name: blog
  slug: blog
- name: mdx
  slug: mdx
- name: Next.js
  slug: nextjs
seo_title: Comment créer votre propre blog avec Next.js et MDX
seo_desc: "By Caleb Olojo\nWhen I decided to build my blog, I found many tools out\
  \ there that were readily available. I looked at Gastby along with content management\
  \ systems like Ghost, Contentful, Sanity dot io, and HUGO. \nBut I needed something\
  \ that I could h..."
---

Par Caleb Olojo

Lorsque j'ai décidé de créer mon blog, j'ai trouvé de nombreux outils disponibles. J'ai examiné [Gastby](https://www.gatsbyjs.com/) ainsi que des systèmes de gestion de contenu comme [Ghost](https://ghost.org/), [Contentful](https://www.contentful.com/), [Sanity dot io](https://www.sanity.io/), et [HUGO](https://gohugo.io/).

Mais j'avais besoin de quelque chose que je pouvais contrôler totalement. J'ai toujours été quelqu'un qui aime la flexibilité d'écrire mon propre code personnalisé. Lorsque je fais cela, je peux facilement revenir là où des problèmes pourraient survenir.

Gatsby offre cette flexibilité, et c'est quelque chose que je pourrais maîtriser assez facilement puisque c'est construit sur une bibliothèque que j'utilise tous les jours (React.js). Mais j'ai découvert que je pouvais faire exactement la même chose avec [Next.js](https://nextjs.org) en intégrant [MDX](https://mdxjs.com/).

_"Qu'est-ce que MDX ?"_ Vous pourriez me demander.

Eh bien... MDX est plus ou moins comme les fichiers markdown que nous voyons toujours dans les dépôts GitHub. MDX apporte cette flexibilité dans un fichier markdown en vous permettant d'écrire littéralement ou d'importer des composants JavaScript (React) dans vos articles. Cela vous évite d'écrire du code répétitif.

Dans cet article, je vais vous montrer comment j'ai construit mon blog avec ces outils, afin que vous puissiez également essayer de construire quelque chose de similaire. Vous aimerez cette pile simple si vous êtes une personne qui aime la flexibilité que cette approche apporte.

Alors, installez-vous confortablement, et commençons.

## Comment commencer à construire – Mes essais et erreurs

Pour construire un blog avec Next.js et MDX, il y a quatre options populaires parmi lesquelles vous pouvez choisir.

Elles sont :

* [@next/mdx](https://www.npmjs.com/package/@next/mdx), qui est l'outil officiel construit par l'équipe Next.js
* [mdx-bundler](https://github.com/kentcdodds/mdx-bundler) de Kent C. Dodds
* [next-mdx-remote](https://github.com/hashicorp/next-mdx-remote), qui est un outil construit par l'équipe Hashicorp
* [next-mdx-enhanced](https://github.com/hashicorp/next-mdx-enhanced), qui est également un outil construit par Hashicorp (je ne sais honnêtement pas pourquoi ils ont décidé d'en construire deux)

Au début, j'ai commencé par utiliser le mdx-bundler de Kent, mais j'ai ensuite rencontré beaucoup de problèmes avec l'outil. C'est une bibliothèque basée sur les nouvelles normes ECMAScript qui nous permettent de créer des ESModules dans le navigateur, et j'utilisais une très ancienne version de Next.js (V10.1.3, ma faute honnêtement, je ne savais pas mieux).

J'ai fait beaucoup de rétrogradations et de mises à jour de Next.js pour résoudre ce problème, sans succès. Il y avait une certaine erreur qui est restée avec moi et a refusé de disparaître pendant des jours. _Oui, pendant des jours !_ J'avais envie de pleurer pendant cette période. Jetez un coup d'œil à l'erreur ci-dessous :

> module not found: can't resolve 'builtin-modules'

Apparemment, pour que mdx-bundler fonctionne, il a besoin d'un autre package npm appelé esbuild pour effectuer les processus de compilation nécessaires qui fonctionnent sous le capot.

```bash
npm i mdx-bundler esbuild

```

Heureusement pour moi — au moins je pensais être chanceux — [Cody Brunner a soumis un problème concernant cette erreur particulière](https://github.com/kentcdodds/mdx-bundler/issues/18). En parcourant les discussions sur le problème, de nombreuses solutions possibles ont été suggérées, certaines d'entre elles étaient liées à Webpack, à la modification de votre fichier `next.config.js`, et ainsi de suite.

```js
module.exports = {
  future: {
    // Opt-in to webpack@5
    webpack5: true,
  },
  reactStrictMode: true,
  webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
    if (!isServer) {
      // https://github.com/vercel/next.js/issues/7755
      config.resolve = {
        ...config.resolve,
        fallback: {
          ...config.resolve.fallback,
          child_process: false,
          fs: false,
          'builtin-modules': false,
          worker_threads: false,
        },
      }
    }

    return config
  },
}

```

Dans l'extrait ci-dessus, il montre que Webpack5 était encore une fonctionnalité en cours pour Next.js — d'où l'extrait ci-dessous dans la config :

```js
future: {
  webpack5: true
}

```

Mais maintenant, la dernière version de Next.js supporte Webpack5 par défaut, donc il n'est pas nécessaire d'ajouter cet objet — si cela fonctionne pour vous — dans la config.

Après avoir parcouru les discussions, j'ai trouvé un commentaire (de Kent) qui dit que l'exécution de `npm update` résoudrait le problème, et cela a fonctionné pour Cody Brunner. Mais pas pour moi, apparemment.

Lorsque je n'ai pas pu trouver de solution possible à cette erreur, j'ai décidé d'utiliser next-mdx-remote, et le seul problème auquel j'ai été confronté était le changement de rupture qui a été ajouté à l'outil. Avant la version 3 de next-mdx-remote, vous rendiez normalement le contenu markdown analysé en faisant ce qui suit :

```jsx
import renderToString from 'next-mdx-remote/render-to-string'
import hydrate from 'next-mdx-remote/hydrate'
import Test from '../components/test'

export default function TestPage({ source }) {
  const content = hydrate(source, { components })

  return <div className="content">{content}</div>
}

export async function getStaticProps() {
  // MDX text - can be from a local file, database, anywhere
  const source = 'Some **mdx** text, with a component <Test />'
  const mdxSource = await renderToString(source, { components })

  return {
    props: {
      source: mdxSource,
    },
  }
}

```

Le changement de rupture qui a été ajouté dans la version 3 du package a supprimé beaucoup de code interne qui était perçu comme causant de mauvaises expériences pour les personnes qui l'utilisaient à l'époque.

L'équipe a ensuite annoncé la raison derrière ce changement et les principaux changements. Jetez un coup d'œil à eux ci-dessous.

> Cette version inclut une réécriture complète des internes de next-mdx-remote pour le rendre plus rapide, plus léger et se comporter de manière plus prévisible ! La migration devrait être assez rapide pour la plupart des cas d'utilisation, mais elle nécessitera quelques changements manuels. Merci à notre communauté pour avoir testé cette version et fourni des retours précoces. cœur.

#### Principaux changements apportés à next-mdx-remote :

* `renderToString` a été remplacé par `serialize`
* `hydrate` a été remplacé par `<MDXRemote />`
* Suppression de la configuration du fournisseur. L'utilisation du contexte React devrait maintenant fonctionner sans effort supplémentaire.
* Le contenu sera maintenant hydraté immédiatement par défaut
* Abandon du support pour IE11 par défaut

Avec ce nouveau changement, la mise en œuvre précédente deviendra maintenant :

```jsx
import { serialize } from 'next-mdx-remote/serialize'
import { MDXRemote } from 'next-mdx-remote'

import { Test, Image, CodeBlock } from '../components/'

const components = { Test }

export default function TestPage({ source }) {
  return (
    <div className="content">
      <MDXRemote {...source} components={{ Test, Image, CodeBlock }} />
    </div>
  )
}

export async function getStaticProps() {
  // MDX text - can be from a local file, database, anywhere
  const source = 'Some **mdx** text, with a component <Test />'
  const mdxSource = await serialize(source)

  return {
    props: {
      source: mdxSource,
    },
  }
}

```

## Comment construire le blog

Dans la section précédente, je vous ai guidé à travers certains des problèmes que j'ai rencontrés en choisissant un outil approprié à utiliser.

Dans cette section, nous allons couvrir comment vous pouvez construire un blog similaire au mien.

Nous allons commencer par créer une application Next.js avec la commande suivante :

```bash
npx create-next-app blog

```

La commande ci-dessus vous donnera un modèle de base d'une application Next.js typique. Pour faire court, je vais me concentrer davantage sur les dossiers `pages` et `src/utils` de cette application.

```bash
|--pages
|   |-- blog
|   |   |-- index.js
|   |   |-- [slug].js
|   |-- _app.js
|   |-- index.js
|--src
|   |-- utils
|        |-- mdx.js
|--data
|   |-- articles
|        |-- example-post.mdx
|        |-- example-post2.mdx

```

Dans un blog typique, nous aurions besoin d'écrire des articles de blog. Dans ce blog, nous utilisons le markdown (MDX) pour écrire nos articles, c'est pourquoi vous pouvez voir que nous avons deux fichiers `.mdx` dans le répertoire `data/articles`. Vous pouvez en avoir plus, selon le nombre d'articles que vous souhaitez écrire.

## Comment lire les fichiers Markdown (MDX)

Dans cette section, nous allons commencer par écrire quelques fonctions réutilisables dans `src/utils/mdx.js`.

Les fonctions que nous écrivons ici utiliseront l'API FileSystem de Node.js. Nous appellerons les fonctions côté serveur dans le dossier des pages car Next.js dispose de certaines [méthodes de récupération de données](https://nextjs.org/docs/basic-features/data-fetching/overview) qui s'exécutent sur le serveur.

Commençons par installer les dépendances dont nous avons besoin pour l'instant. Au fur et à mesure que nous progresserons, nous ajouterons d'autres dépendances :

```bash
npm install gray-matter reading-time next-mdx-remote glob dayjs

```

La commande ci-dessus obtiendra tous les packages listés ci-dessus comme dépendances dans notre projet de blog.

`gray-matter` analysera le contenu des fichiers `.mdx` en contenu HTML lisible.

`reading-time` attribue un temps approximatif pour lire un article de blog ou un article en fonction du nombre de mots.

`next-mdx-remote` effectue la compilation en arrière-plan des fichiers MDX en permettant leur chargement dans les méthodes de récupération de données `getStaticProps` ou `getServerSideProps` de Next.js, et hydrate correctement sur le client.

`glob` nous donne accès à la correspondance des motifs de fichiers dans `data/articles`, que nous utiliserons comme slug de l'article.

`dayjs` est une bibliothèque JavaScript qui aide à analyser, manipuler, valider et afficher les dates que nous ajouterons aux métadonnées de chaque article.

Nous avons vu les fonctions de base des packages que nous avons installés. Maintenant, commençons à écrire les fonctions qui liront les fichiers dans le répertoire des articles.

```js
import path from 'path'
import fs from 'fs'
import matter from 'gray-matter'
import readingTime from 'reading-time'
import { sync } from 'glob'

const articlesPath = path.join(process.cwd(), 'data/articles')

export async function getSlug() {
  const paths = sync(`${articlesPath}/*.mdx`)

  return paths.map((path) => {
    // contient les chemins vers le répertoire de l'article
    const pathContent = path.split('/')
    const fileName = pathContent[pathContent.length - 1]
    const [slug, _extension] = fileName.split('.')

    return slug
  })
}

```

Dans l'extrait ci-dessus, nous avons importé le FileSystem de Node.js depuis son module et les autres packages. La première déclaration de variable, `articlesPath`, contient le chemin vers l'endroit où tous les articles peuvent être trouvés.

```js
const articlesPath = path.join(process.cwd(), 'data/articles')

```

Nous utilisons le module `path` pour obtenir l'accès à l'endroit où se trouvent les articles en utilisant l'API `process` de Node.js qui nous donne un accès direct à l'objet `cwd()` (Current Working Directory).

La fonction `getSlug` obtiendra un article unique lorsqu'il sera cliqué par l'utilisateur sur la page du blog. Vous verrez que nous faisons référence à la variable `articlesPath` qui a été déclarée auparavant, et nous la passons à la fonction `sync` du package `glob`. Cela correspondra à tout fichier ayant l'extension `.mdx`, et nous donnera un tableau avec une liste de ces fichiers.

```js
const paths = sync(`${articlesPath}/*.mdx`)

```

Cela dit, nous retournerons un tableau de noms de fichiers modifiés. La variable `pathContent` contient le chemin vers tous les articles dans le répertoire des articles, donc nous utilisons JavaScript pour supprimer toutes les "barres obliques" avec la méthode `split()` de JavaScript.

```js
const fileName = pathContent[pathContent.length - 1]
const [slug, _extension] = fileName.split('.')

```

La déclaration de la variable `fileName` obtient la dernière partie du chemin, par exemple `"/data/articles/example-post.mdx"`, puisque c'est un tableau, et retourne la dernière partie qui est `/example-post.mdx`. La variable suivante supprime le point `(.)` du nom de fichier lui-même, donc nous serons laissés avec `example-post` comme slug.

## Comment analyser le contenu de l'article à partir du slug

La fonction suivante obtient et analyse le contenu de nos fichiers MDX à partir des slugs. Elle retourne un objet de métadonnées que nous utiliserons au fur et à mesure.

```js
export async function getArticleFromSlug(slug) {
  const articleDir = path.join(articlesPath, `${slug}.mdx`)
  const source = fs.readFileSync(articleDir)
  const { content, data } = matter(source)

  return {
    content,
    frontmatter: {
      slug,
      excerpt: data.excerpt,
      title: data.title,
      publishedAt: data.publishedAt,
      readingTime: readingTime(source).text,
      ...data,
    },
  }
}

```

Dans l'extrait ci-dessus, nous utilisons la fonction `readFileSync` de Node.js depuis l'API FileSystem pour lire les fichiers dans `articleDir` de manière synchrone.

Ce que nous faisons avec cette fonction — `readFileSync` — c'est dire à Node d'arrêter les autres processus qui sont en cours et d'effectuer cette opération pour nous.

Vous pouvez en apprendre plus à ce sujet [ici](https://www.geeksforgeeks.org/node-js-fs-readfilesync-method/) si vous le souhaitez.

Si vous allez de l'avant et `console.log(source)` dans votre terminal, vous obtiendrez un `<Buffer>` — qui n'est pas lisible — type de données dans votre console.

C'est là que le package `gray-matter` vient sauver la journée. Il aide à analyser le contenu markdown dans la source en quelque chose — HTML lisible — que vous et moi pouvons comprendre.

Ici, nous déstructurons les variables `content` et `data`, les assignons au package `matter` (qui analyse la source) et retournons un objet qui contient nos variables `content` et `frontmatter: data` :

```js
const { content, data } = matter(source)

return {
  content,
  frontmatter: {
    slug,
    excerpt: data.excerpt,
    title: data.title,
    publishedAt: data.publishedAt,
    readingTime: readingTime(source).text,
    ...data,
  },
}

```

Nous avons besoin d'un moyen d'afficher tous les articles sur la page du blog. La fonction ci-dessous le fait pour nous, en utilisant la méthode `reduce()` de JavaScript pour retourner un tableau de tous les articles dans le répertoire des articles.

```js
export async function getAllArticles() {
  const articles = fs.readdirSync(path.join(process.cwd(), 'data/articles'))

  return articles.reduce((allArticles, articleSlug) => {
    // obtenir les données analysées des fichiers mdx dans le répertoire "articles"
    const source = fs.readFileSync(
      path.join(process.cwd(), 'data/articles', articleSlug),
      'utf-8'
    )
    const { data } = matter(source)

    return [
      {
        ...data,
        slug: articleSlug.replace('.mdx', ''),
        readingTime: readingTime(source).text,
      },
      ...allArticles,
    ]
  }, [])
}

```

Vous pouvez voir comment nous utilisons `readdirSync()` pour lire de manière synchrone tous les fichiers à l'intérieur de `data/articles`. La variable `source` peut être accessible en lisant tous les fichiers avec leurs slugs respectifs et en obtenant leur contenu analysé avec le package `gray-matter`.

```js
const source = fs.readFileSync(
  path.join(process.cwd(), 'data/articles', articleSlug),
  'utf-8'
)
const { data } = matter(source)

```

Si vous regardez l'extrait ci-dessous, vous verrez comment nous utilisons le package `reading-time` pour obtenir le temps approximatif qu'il faudra pour lire cet article. Nous obtenons le slug qui sera attaché à cet article en supprimant la dernière partie de l'article — `blog/example-post.mdx` — et en la remplaçant par une chaîne vide. Cela le rend accessible via "blog/example-post".

```js
{
  slug: articleSlug.replace('.mdx', ''),
  readingTime: readingTime(source).text,
}

```

Le `readingTime` a certaines méthodes que vous pouvez lui assigner, l'une d'elles est la méthode `text`. Vous pouvez essayer de supprimer cette valeur, sauvegarder votre code et permettre à Next.js de lancer une erreur, afin que vous puissiez avoir un aperçu des valeurs que vous pouvez utiliser.

## Comment afficher une liste d'articles

Dans les sections précédentes, nous avons vu comment nous pouvons utiliser l'API FileSystem de Node.js et quelques autres outils pour accéder à l'endroit où se trouvent tous nos articles.

Dans cette section, nous allons afficher les articles sur une page web.

Nous allons commencer avec le fichier `index` dans le dossier blog. Dans ce fichier, nous allons utiliser la méthode de récupération de données — `getStaticProps` — pour rendre les articles sur la page.

```js
import { getAllArticles } from '../../src/utils/mdx'

export async function getStaticProps() {
  const articles = await getAllArticles()

  articles
    .map((article) => article.data)
    .sort((a, b) => {
      if (a.data.publishedAt > b.data.publishedAt) return 1
      if (a.data.publishedAt < b.data.publishedAt) return -1

      return 0
    })

  return {
    props: {
      posts: articles.reverse(),
    },
  }
}

```

Dans l'extrait ci-dessus, nous avons importé la fonction `getAllArticles` et l'avons utilisée dans la méthode de récupération de données de Next.js.

Vous remarquerez comment nous trions les articles en fonction de la date à laquelle ils ont été publiés. Nous allons finalement mapper la liste des articles qui seront retournés en tant que props à la page d'index (blog).

```js
articles
  .map((article) => article.data)
  .sort((a, b) => {
    if (a.data.publishedAt > b.data.publishedAt) return 1
    if (a.data.publishedAt < b.data.publishedAt) return -1

    return 0
  })

```

De peur d'oublier, voici à quoi ressemble le contenu de votre fichier d'article typique en syntaxe markdown ci-dessous :

```md
---
title: 'Erreur d'optimisation d'image Next.js sur Netlify'
publishedAt: '2022-04-16'
excerpt: 'Next.js dispose d'un composant Image intégré qui offre de nombreuses fonctionnalités d'optimisation des performances lorsque vous l'utilisez.'
cover_image: 'path/to/where/image/is/stored'
---

le reste du contenu se trouve ici

```

Vous pourriez me demander, _"pourquoi avons-nous besoin de trier les articles par date si nous pouvons simplement utiliser la méthode `reverse()` pour réorganiser le tableau des articles ?"_.

Je pense qu'il est approprié pour nous de trier la liste des articles en les comparant avec la date à laquelle ils ont été publiés et d'appliquer toujours la méthode `reverse` au tableau.

Disons, par exemple, que nous oublions d'ajouter les dates de publication aux articles. Ensuite, la méthode `reverse()` effectuera simplement l'opération sur le tableau sans comparer les dates dans un motif LIFO — Last-In-First-Out — si la fonction de tri est manquante. Il est donc préférable de trier les articles et de toujours inverser le contenu du tableau.

Maintenant que nous avons retourné la liste des articles en tant que props, nous pouvons continuer à les mapper sur la page.

```jsx
import React from 'react'
import Head from 'next/head'
import Link from "next/link"
import { getAllArticles } from '../../src/utils/mdx'

export default function BlogPage({ posts }) {
  return (
    <React.Fragment>
      <Head>
        <title>Mon Blog</title>
      </Head>
      <div>
        {posts.map((frontMatter) => {
          return (
            <Link href={`/blog/${frontMatter.slug}`} passHref>
              <div>
                <h1 className="title">{frontMatter.title}</h1>
                <p className="summary">{frontMatter.excerpt}</p>
                <p className="date">
                  {dayjs(frontMatter.publishedAt).format('MMMM D, YYYY')} &mdash;{' '}
                  {frontMatter.readingTime}
                </p>
              </div>
            </Link>
          )
        })}
      </div>
    </React.Fragment>
  )
}

export async function getStaticProps() {
  ...
}

```

Dans l'extrait ci-dessus, nous utilisons le composant `Link` pour rediriger l'utilisateur vers une page dynamique avec le slug unique de l'article. C'est la raison pour laquelle nous avons créé un fichier appelé `[slug].js`, si vous vous en souvenez. C'est une route dynamique, et vous pouvez en lire plus à ce sujet [ici](https://nextjs.org/docs/routing/dynamic-routes).

## Comment afficher un article unique

Dans la dernière section, nous avons pu rendre la liste des articles sur la page web. Dans cette section, nous allons rendre un article unique qui est cliqué par l'utilisateur dans une nouvelle route.

Nous allons également utiliser un outil appelé rehype pour personnaliser l'apparence de notre article de blog. Rehype est un pré-processeur HTML qui est alimenté par des plugins. Nous allons utiliser certains de ces plugins dans cette section, alors installons-les maintenant.

```bash
npm i rehype-highlight rehype-autolink-headings rehype-code-titles rehype-slug

```

`rehype-highlight` nous permet d'ajouter une coloration syntaxique à nos blocs de code.

`rehype-autolink-headings` est un plugin qui ajoute des liens aux titres de h1 à h6.

`rehype-code-titles` ajoute des titres de langage/fichier à votre code.

`rehype-slug` est un plugin qui ajoute des attributs `id` aux titres.

Maintenant que nous avons vu les rôles que chaque plugin joue, commençons à travailler sur le fichier `[slug].js`. Dans ce fichier, nous allons utiliser deux méthodes de récupération de données de Next.js — `getStaticProps` et `getStaticPaths`.

Nous utilisons ces deux méthodes car nous allons récupérer des données (articles) qui sont uniques au chemin (slugs) vers lequel l'utilisateur est redirigé.

```jsx
// générer dynamiquement les slugs pour chaque article(s)
export async function getStaticPaths() {
  // obtenir tous les chemins de chaque article sous forme de tableau d'
  // objets avec leurs slugs uniques
  const paths = (await getSlug()).map((slug) => ({ params: { slug } }))

  return {
    paths,
    // dans les situations où vous essayez d'accéder à un chemin
    // qui n'existe pas. il retournera une page 404
    fallback: false,
  }
}

```

Lorsque vous regardez l'extrait ci-dessus, vous verrez que nous obtenons la liste des `paths` des articles et que nous mappons cette liste d'éléments (paths) à un tableau. Cela peut être accessible avec la variable `params` dans la méthode de récupération de données `getStaticProps`.

```js
import { getArticleFromSlug } from "../../src/utils/mdx"

export async function getStaticProps({ params }) {
  //fetch the particular file based on the slug
  const { slug } = params
  const { content, frontmatter } = await getArticleFromSlug(slug)

  const mdxSource = await serialize(content, {
    mdxOptions: {
      rehypePlugins: [
        rehypeSlug,
        [
          rehypeAutolinkHeadings,
          {
            properties: { className: ['anchor'] },
          },
          { behaviour: 'wrap' },
        ],
        rehypeHighlight,
        rehypeCodeTitles,
      ],
    },
  })

  return {
    props: {
      post: {
        source: mdxSource,
        frontmatter,
      },
    },
  }
}`

```

Dans l'extrait ci-dessus, nous déstructurons `content` et `frontmatter` — qui sont les métadonnées de l'article — et les assignons à la fonction `getArticleFromSlug` qui reçoit le slug de l'article comme argument.

Nous continuons en sérialisant le contenu de l'article avec la fonction `serialize()` de next-mdx-remote, et passons les plugins rehype nécessaires dans l'objet `mdxOptions` :

```js
const mdxSource = await serialize(content, {
  mdxOptions: {
    rehypePlugins: [
      rehypeSlug,
      [
        rehypeAutolinkHeadings,
        {
          properties: { className: ['anchor'] },
        },
        { behaviour: 'wrap' },
      ],
      rehypeHighlight,
      rehypeCodeTitles,
    ],
  },
})

```

Pour conclure, nous retournons le `content` de l'article et le `frontmatter` en tant que props qui seront accessibles par le composant slug.

```js
return {
  props: {
    post: {
      source: mdxSource,
      frontmatter,
    },
  },
}

```

Les props que nous avons retournés dans les extraits précédents peuvent être accessibles via le composant ci-dessous.

Vous remarquerez que le composant `<MDXRemote />` reçoit le `{...source}` et les props de composants React personnalisés que nous pouvons utiliser dans nos fichiers MDX. Cela élimine le processus d'avoir à écrire du code répétitif encore et encore.

```jsx
import dayjs from 'dayjs'
import React from 'react'
import Head from 'next/head'
import Image from 'next/image'
import rehypeSlug from 'rehype-slug'
import { MDXRemote } from 'next-mdx-remote'
import rehypeHighlight from 'rehype-highlight'
import rehypeCodeTitles from 'rehype-code-titles'
import { serialize } from 'next-mdx-remote/serialize'
import 'highlight.js/styles/atom-one-dark-reasonable.css'
import rehypeAutolinkHeadings from 'rehype-autolink-headings'
import { getSlug, getArticleFromSlug } from '../../src/utils/mdx'
import { SectionTitle, Text } from '../../data/components/mdx-components'

export default function Blog({ post: { source, frontmatter } }) {
  return (
    <React.Fragment>
      <Head>
        <title>{frontmatter.title} | Mon blog</title>
      </Head>
      <div className="article-container">
        <h1 className="article-title">{frontmatter.title}</h1>
        <p className="publish-date">
          {dayjs(frontmatter.publishedAt).format('MMMM D, YYYY')} &mdash;{' '}
          {frontmatter.readingTime}
        </p>
        <div className="content">
          <MDXRemote {...source} components={{ Image, SectionTitle, Text }} />
        </div>
      </div>
    </React.Fragment>
  )
}

```

Dans l'extrait ci-dessus, vous remarquerez comment nous avons déstructuré les props de l'article en `{ source, frontmatter }`. Au lieu de faire cela, dans le composant `<MDXRemote>` ci-dessous, nous pouvons simplement étendre la variable source directement en tant que prop.

```jsx
<MDXRemote {...post.source} />

```

Remarquez comment nous rendons également dynamiquement le titre de la page avec le titre de l'article au lieu du titre normal ? Cela est obtenu à partir du frontmatter.

```jsx
<Head>
  <title>{frontmatter.title} | Mon blog</title>
</Head>

```

## Réflexions finales

Chaque développeur aime avoir ses thèmes fantaisistes appliqués à ses éditeurs. Nous ne allons donc pas laisser cela de côté dans ce blog.

J'utilise actuellement le thème `"atom-one-dark-reasonable"` pour ma coloration syntaxique. Vous pouvez l'importer depuis la bibliothèque `"highlight.js"` — puisque le plugin `rehype-highlight` l'utilise sous le capot — comme ceci :

```js
import 'highlight.js/styles/atom-one-dark-reasonable.css'

```

Il existe de nombreux autres thèmes [ici](https://highlightjs.org/static/demo/), vous pouvez donc choisir celui avec lequel vous êtes à l'aise.

Vous avez peut-être remarqué en lisant cet article qu'il y a certains composants comme celui dans l'image ci-dessous — et vous vous êtes peut-être demandé comment il a été créé.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/tooltip-1.png)

Vous pouvez décider d'avoir de nombreux composants MDX personnalisés que vous pouvez utiliser dans vos articles. Mais j'ai décidé de cibler tout élément que je souhaite styliser dans cet article en lui attribuant une classe générique. Ainsi, chaque fois que je veux l'utiliser, je fais simplement référence à ce style dans l'élément.

Le SEO est l'une des choses importantes lorsqu'il s'agit de créer un blog, et heureusement pour nous, Next.js a déjà cela couvert pour nous. Vous pouvez consulter cet article qui vous guide à travers [Comment ajouter des balises méta SEO dans vos applications Next.js](https://seven.hashnode.dev/seo-in-nextjs-apps) et [Comment j'ai corrigé une erreur de pré-rendu de balises méta dans Next.js](https://meje.dev/blog/meta-tags-error-in-nextjs)

Il y a une chose importante que vous ne devez pas oublier, et c'est le fichier `next.config.js`. Vous devez vous assurer qu'il est correctement configuré pour éviter l'une des erreurs de compatibilité de version de la dernière version de React — v18.0.0 — avec next-mdx-remote.

Bien que l'équipe Hashicorp ait déclaré avoir corrigé [cela](https://github.com/hashicorp/next-mdx-remote/pull/250) dans leur dernière version, cela n'a pas fonctionné pour moi. Une façon de contourner cette erreur est d'installer next-mdx-remote en tant que dépendance peer legacy, comme suit :

```bash
npm i next-mdx-remote --legacy-peer-deps

```

Et assurez-vous d'avoir un fichier `next.config` qui ressemble à ce que vous voyez ci-dessous.

```js
module.exports = {
  reactStrictMode: true,

  images: {
    loader: 'akamai',
    path: '',
  },

  webpack: (config) => {
    config.resolve.alias = {
      ...config.resolve.alias,
      'react/jsx-runtime.js': require.resolve('react/jsx-runtime'),
    }

    config.resolve = {
      ...config.resolve,

      fallback: {
        ...config.resolve.fallback,
        child_process: false,
        fs: false,
        // 'builtin-modules': false,
        // worker_threads: false,
      },
    }

    return config
  },
}

```

L'objet `resolve.alias` dans la config ci-dessus aide en tant que solution de contournement pour corriger l'erreur ci-dessous

#### Que faire si vous obtenez une erreur de serveur

Erreur : Le sous-chemin du package "./jsx-runtime.js" n'est pas défini par "exports" dans "path-to-node_modules/react/package.json"

Parfois, vous pouvez également rencontrer une erreur liée aux modules "builtin" de Node.js lors du déploiement de votre projet. L'objet `config.resolve` avec la clé `fallback` aide à supprimer cette erreur.

Vous remarquerez qu'il y a un objet `image` dans la config.

```js
  images: {
    loader: 'akamai',
    path: '',
  },

```

Son rôle est de garantir que le processus d'optimisation des images approprié est utilisé lors du processus de construction. Vous pouvez consulter un article que j'ai écrit sur la façon dont vous pouvez corriger l'[erreur d'optimisation d'image Next.js sur Netlify](https://meje.dev/blog/image-optimization-error-in-nextjs)

Merci beaucoup d'avoir lu cet article. J'espère que vous l'avez trouvé utile.