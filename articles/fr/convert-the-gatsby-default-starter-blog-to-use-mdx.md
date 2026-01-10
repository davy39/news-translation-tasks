---
title: Convertir le blog de démarrage par défaut de Gatsby pour utiliser MDX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T17:18:00.000Z'
originalURL: https://freecodecamp.org/news/convert-the-gatsby-default-starter-blog-to-use-mdx
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/cover-6.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: blog
  slug: blog
- name: Gatsby
  slug: gatsby
- name: mdx
  slug: mdx
seo_title: Convertir le blog de démarrage par défaut de Gatsby pour utiliser MDX
seo_desc: 'By Scott Spence

  In this guide we''re going to cover converting the Gatsby default blog starter to
  use MDX.

  All the cool kids are using Gatsby and MDX in their blogs these days. If you already
  have a blog that uses Gatsby but want to move onto the new ...'
---

Par Scott Spence

Dans ce guide, nous allons couvrir la conversion du blog de démarrage par défaut de Gatsby pour utiliser MDX.

Tous les jeunes branchés utilisent Gatsby et MDX dans leurs blogs ces jours-ci. Si vous avez déjà un blog qui utilise Gatsby mais que vous souhaitez passer à la nouvelle tendance, ce guide est fait pour vous.

%[https://www.youtube.com/watch?v=gck4RjaX5D4]

## Versions :

**Ce guide est utilisé avec les versions de dépendances suivantes.**

* gatsby : 2.3.5
* react : 16.8.6
* react-dom : 16.8.6
* gatsby-mdx : 0.4.5
* @mdx-js/mdx : 0.20.3
* @mdx-js/tag : 0.20.3

Vous pouvez également consulter le [code exemple](https://codesandbox.io/s/lqp6p647q).

---

Nous allons avoir besoin de quelques liens, qui sont :

[Documentation CodeSandbox pour importer des projets](https://codesandbox.io/docs/importing)

[Assistant d'importation CodeSandbox](https://codesandbox.io/s/github)

[Blog de démarrage Gatsby](https://github.com/gatsbyjs/gatsby-starter-blog)

## Importer vers CodeSandbox

Pour cet exemple, je vais utiliser le [blog de démarrage Gatsby](https://github.com/gatsbyjs/gatsby-starter-blog) et l'importer dans CodeSandbox. En consultant la documentation, il est indiqué que vous pouvez faire cela avec l'[assistant d'importation CodeSandbox](https://codesandbox.io/s/github) lié, collez le lien là-bas et CodeSandbox ouvrira la représentation du code sur GitHub.

Maintenant, nous pouvons procéder au passage de l'utilisation de Gatsby transformer remark à MDX.

Examinons ce que nous allons changer pour cet exemple. Mais d'abord, nous allons devoir importer quelques dépendances pour faire fonctionner MDX dans notre projet Gatsby.

Avec le bouton d'ajout de dépendance dans CodeSandbox, ajoutez les dépendances suivantes :

* `gatsby-mdx`
* `@mdx-js/mdx`
* `@mdx-js/tag`

Nous devrons également ajouter des dépendances pour styled-components, alors autant les ajouter maintenant aussi :

* `gatsby-plugin-styled-components`
* `styled-components`
* `babel-plugin-styled-components`

Fichiers à modifier :

* `gatsby-node.js`
* `gatsby-config.js`
* `index.js`
* `blog-post.js`

## `gatsby-node.js`

Tout d'abord, nous allons devoir modifier `gatsby-node.js`, c'est là que toutes les pages et les nœuds de données sont générés.

Remplacez toutes les occurrences de markdown remark par MDX, c'est la requête GraphQL initiale dans create pages, puis à nouveau dans le résultat.

![initial gatsby node changes](https://www.freecodecamp.org/news/content/images/2019/06/initialGatsbyNode.png)

Ensuite, changez le `node.internal.type` dans `onCreateNode` de `MarkdownRemark` à `Mdx`.

![last gatsby node changes](https://www.freecodecamp.org/news/content/images/2019/06/lastGatsbyNode.png)

## `gatsby-config.js`

Ici, nous allons remplacer `gatsby-transformer-remark` par `gatsby-mdx`

![replace transformer remark with gatsby-mdx](https://www.freecodecamp.org/news/content/images/2019/06/gatsbyConfig.png)

## `index.js`

Ici, nous allons modifier la variable `posts` pour prendre les `Mdx` edges.

![replace all markdown edges](https://www.freecodecamp.org/news/content/images/2019/06/indexPageEdges.png)

Les `Mdx` edges sont pris à partir de la requête de page, qui est également modifiée pour utiliser `allMdx` à la place de `allMarkdownRemark`.

![index page query](https://www.freecodecamp.org/news/content/images/2019/06/indexPageQuery.png)

## `blog-post.js`

Maintenant, le dernier de la liste pour faire fonctionner MDX est le modèle de blog, nous allons devoir importer `MDXRenderer` depuis `gatsby-mdx`, nous allons remplacer `dangerouslySetInnerHTML` par cela sous peu.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/importMdxRenderer.png)

Voici où nous l'utilisons, nous allons aborder `post.code.body`.

![replace dangerously set html](https://www.freecodecamp.org/news/content/images/2019/06/replaceDangerHtml.png)

Encore une fois dans la requête, nous remplaçons `markdownRemark` par `mdx` et cette fois, nous supprimons également `html` de la requête et ajoutons `code` pour `body` que nous utilisons dans notre méthode de rendu.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/blogPostQuery-1.png)

## Maintenant nous utilisons MDX !

Donc maintenant nous pouvons créer un post `.mdx`, faisons cela.

Importez les dépendances de styled-components :

```bash
gatsby-plugin-styled-components
styled-components
babel-plugin-styled-components

```

Ensuite, configurez-les dans `gatsby-config.js` :

```js
module.exports = {
  siteMetadata: {
    title: `Gatsby Starter Blog`,
    ...
    },
  },
  plugins: [
    `gatsby-plugin-styled-components`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
  ...

```

Maintenant, nous pouvons utiliser styled-components, dans `src/components`, créez un nouveau composant, j'ai appelé le mien `butt.js`, appelez le vôtre comme vous voulez.

Nous allons utiliser ce composant dans un document `.mdx`, d'abord le composant :

```js
import styled from 'styled-components';

export const Butt = styled.button`
  background-color: red;
  height: 40px;
  width: 80px;
`;

```

Épicé, non ?

Maintenant, nous pouvons inclure ce composant dans un document `.mdx`, alors allons-y et créons cela, dans `content/blog`, créez un nouveau répertoire, je donne à le mien le nom imaginatif `first-mdx-post`, créez-y un fichier `index.mdx` et utilisez le frontmatter de l'un des autres posts comme exemple de ce qu'il faut utiliser :

```mdx
---
title: Mon premier post MDX !
date: '2019-04-07T23:46:37.121Z'
---

# faites un site, ils ont dit, ce sera amusant, ils ont dit

plus de contenu yo !

```

Cela rendra un `h1` et un `p` et nous devrions le voir s'afficher dans notre aperçu CodeSandbox.

Maintenant, nous pouvons aller de l'avant et importer notre bouton magnifiquement conçu :

```mdx
---
title: Mon premier post MDX !
date: '2019-04-07T23:46:37.121Z'
---

import { Butt } from '../../../src/components/button';

# faites un site, ils ont dit, ce sera amusant, ils ont dit

plus de contenu yo !

<Butt>yoyoyo</Butt>

```

## Conclusion !

Donc, c'est tout, nous avons converti le blog de démarrage Gatsby de l'utilisation de Markdown Remark à l'utilisation de MDX.

J'espère que vous l'avez trouvé utile.

**Merci d'avoir lu.**

Veuillez consulter mon autre contenu si vous avez aimé cela.

Suivez-moi sur [Twitter](https://twitter.com/spences10) ou [Ask Me Anything](https://github.com/spences10/ama) sur GitHub.

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).**