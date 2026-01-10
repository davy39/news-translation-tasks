---
title: Comment créer votre blog de codage à partir de zéro en utilisant Gatsby et
  MDX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-31T19:45:00.000Z'
originalURL: https://freecodecamp.org/news/build-a-developer-blog-from-scratch-with-gatsby-and-mdx
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/cover-2.jpg
tags:
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: mdx
  slug: mdx
- name: React
  slug: react
seo_title: Comment créer votre blog de codage à partir de zéro en utilisant Gatsby
  et MDX
seo_desc: "By Scott Spence\nI have been a Gatsby user since around version 0 back\
  \ in May 2017. \nBack then, I was using a template called Lumen. It was just what\
  \ I needed at the time. Since then I have gone from using a template to creating\
  \ my blog.\nOver the year..."
---

Par Scott Spence

J'utilise Gatsby depuis environ [la version 0 en mai 2017](https://github.com/spences10/blog.scottspence.me/tree/a470e8563e1a040527cf2094fc1b377550a88c77).

À l'époque, j'utilisais un modèle appelé [Lumen](https://github.com/alxshelepenok/gatsby-starter-lumen). C'était exactement ce dont j'avais besoin à ce moment-là. Depuis, je suis passé de l'utilisation d'un modèle à la création de mon propre blog.

Au fil des ans, j'ai construit ma propre [Divulgation Progressive de la Complexité](https://lengstorf.com/progressive-disclosure-of-complexity/) avec Gatsby jusqu'à aujourd'hui.

## Que signifie cela ?

Cela signifie que bien qu'il existe une quantité impressionnante de modèles et de thèmes Gatsby pour vous aider à démarrer en quelques minutes, cet article va se concentrer sur ce que vous devez faire pour construire votre propre blog. En commençant par le plus basique "Hello World!" jusqu'au déploiement de votre code en production.

## Ce que vous allez construire

Vous allez construire un blog de développeur avec support MDX (pour certains composants React dans Markdown), afin de pouvoir ajouter vos propres composants React dans vos articles Markdown.

**Il y aura :**

* Ajout d'une mise en page
* Stylisation de base avec styled-components
* Blocs de code avec surlignage de syntaxe
* Copier un extrait de code dans le presse-papiers
* Images de couverture pour les articles
* Configuration d'un composant SEO
* Déploiement sur Netlify

## À qui s'adresse ce guide ?

Aux personnes qui ont peut-être utilisé Gatsby auparavant comme modèle et qui souhaitent maintenant s'impliquer davantage dans la manière d'apporter des modifications.

Si vous souhaitez avoir un surlignage de syntaxe de code.

Si vous souhaitez utiliser styled-components dans une application.

**Je veux vraiment éviter cela !**

%[https://twitter.com/ossia/status/588389121053200385]

## Prérequis

Vous aurez besoin d'une configuration de développement web de base : node, terminal (bash, zsh ou fish) et un éditeur de texte.

J'aime utiliser [codesandbox.io](https://codesandbox.io/) pour ce type de guides afin de réduire la barrière à l'entrée, mais dans ce cas, j'ai trouvé qu'il y avait certaines limitations à commencer à partir de zéro sur [codesandbox.io](https://codesandbox.io/) qui ne rendent pas cela possible.

J'ai créé un guide pour se configurer pour le développement web avec [Windows Web-Dev Bootstrap](http://blog.scottspence.me/wsl-bootstrap-2019) et j'ai couvert le même processus dans [Ubuntu également](https://www.youtube.com/watch?v=eSAsdQuQ-1o).

D'accord ? Il est temps de commencer !

## Hello World

Pour commencer avec le "hello world" de Gatsby, vous devrez initialiser le projet avec :

```bash
npm init -y
git init
```

Je suggère de commiter ce code dans un dépôt git, vous devriez donc commencer avec un fichier `.gitignore`.

```bash
touch .gitignore

echo "# Project dependencies
.cache
node_modules

# Build directory
public

# Other
.DS_Store
yarn-error.log" > .gitignore
```

Maintenant est un bon moment pour faire un `git init` et si vous utilisez VSCode, vous verrez les changements reflétés dans la barre latérale.

### hello world basique

Un hello world Gatsby, commencez avec le strict minimum ! Installez ce qui suit :

```bash
yarn add gatsby react react-dom
```

Vous allez devoir créer un répertoire pages et ajouter un fichier index. Vous pouvez faire cela dans le terminal en tapant ce qui suit :

```bash
# -p est pour créer les répertoires parents aussi si nécessaire
mkdir -p src/pages
touch src/pages/index.js
```

Maintenant vous pouvez commencer l'incantation hello word ! Dans le fichier `index.js` nouvellement créé, entrez ce qui suit :

```js
import React from 'react';

export default () => {
  return <h1>Hello World!</h1>;
};
```

Maintenant vous devez ajouter le script de développement Gatsby au fichier `package.json`, `-p` spécifie le port sur lequel vous voulez exécuter le projet et `-o` ouvre un nouvel onglet sur votre navigateur par défaut, donc dans ce cas `localhost:9988` :

```json
"dev": "gatsby develop -p 9988 -o"
```

Et maintenant il est temps d'exécuter le code ! Depuis le terminal, tapez la commande npm script que vous venez de créer :

```bash
yarn dev
```

> Notez que j'utilise Yarn pour installer toutes mes dépendances et exécuter des scripts. Si vous préférez, vous pouvez utiliser npm, gardez simplement à l'esprit que le contenu ici utilise yarn, donc remplacez les commandes si nécessaire.

Et avec cela, l'incantation "Hello World" est complète ?!

%[https://youtu.be/2vP3ZTDbN1g]

## Ajouter du contenu

Maintenant que vous avez la base de votre blog, vous allez vouloir ajouter du contenu. Commençons par établir la convention. Pour ce guide, le format de date sera logique - la manière la plus logique pour un format de date est **AAAAMMJJ**, combattez-moi !

Vous allez donc structurer le contenu de vos articles par années. Dans chacune d'entre elles, vous aurez un autre dossier relatif à l'article avec le format de date (correct) pour le début du fichier suivi du titre de l'article.

Vous pourriez approfondir cela en séparant les mois et les jours. Selon le volume d'articles que vous avez, cela peut être une bonne approche. Dans ce cas et dans les exemples fournis, la convention détaillée sera utilisée.

```bash
# créer plusieurs répertoires en utilisant des accolades
mkdir -p posts/2019/{2019-06-01-hello-world,2019-06-10-second-post,2019-06-20-third-post}
touch posts/2019/2019-06-01-hello-world/index.mdx
touch posts/2019/2019-06-10-second-post/index.mdx
touch posts/2019/2019-06-20-third-post/index.mdx
```

D'accord, c'est ainsi que vous configurez vos articles. Maintenant, vous devez ajouter du contenu à ceux-ci, donc chaque fichier que vous avez ici doit avoir un frontmatter. Le frontmatter est un moyen d'assigner des propriétés au contenu, dans ce cas un `title`, une date de `publication` et un indicateur `published` (`true` ou `false`).

```md
---
title: Hello World - from mdx!
date: 2019-06-01
published: true
---

# h1 Heading

My first post!!

## h2 Heading

### h3 Heading
```

```md
---
title: Second Post!
date: 2019-06-10
published: true
---

This is my second post!

#### h4 Heading

##### h5 Heading

###### h6 Heading
```

```md
---
title: Third Post!
date: 2019-06-20
published: true
---

This is my third post!

> with a block quote!
```

## API de configuration de Gatsby

Ensuite, vous allez configurer Gatsby pour qu'il puisse lire votre super contenu que vous venez de créer. Tout d'abord, vous devez créer le fichier `gatsby-config.js`. Dans le terminal, créez le fichier :

```bash
touch gatsby-config.js
```

## Plugins

Et maintenant vous pouvez ajouter les plugins dont Gatsby a besoin pour utiliser les fichiers que vous venez de créer.

### Gatsby source filesystem

Le [gatsby-source-filesystem](https://www.gatsbyjs.org/packages/gatsby-source-filesystem/) collecte les fichiers sur le système de fichiers local pour les utiliser dans Gatsby une fois configuré.

### Gatsby plugin MDX

Le [gatsby-plugin-mdx](https://www.gatsbyjs.org/packages/gatsby-plugin-mdx/) est ce qui nous permettra d'écrire du JSX dans nos documents Markdown et le cœur de la manière dont le contenu est affiché dans le blog.

Maintenant est un bon moment pour ajouter également les packages dépendants pour le plugin Gatsby MDX qui sont `@mdx-js/mdx` et `@mdx-js/react`.

Dans le terminal, installez les dépendances :

```bash
yarn add gatsby-plugin-mdx @mdx-js/mdx @mdx-js/react gatsby-source-filesystem
```

Maintenant, il est temps de configurer `gatsby-config.js` :

```js
module.exports = {
  siteMetadata: {
    title: `The Localhost Blog`,
    description: `This is my coding blog where I write about my coding journey.`,
  },
  plugins: [
    {
      resolve: `gatsby-plugin-mdx`,
      options: {
        extensions: [`.mdx`, `.md`],
      },
    },
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        path: `${__dirname}/posts`,
        name: `posts`,
      },
    },
  ],
};
```

## Interroger les données depuis GraphQL

Maintenant, vous pouvez voir ce que [gatsby-source-filesystem](https://www.gatsbyjs.org/packages/gatsby-source-filesystem/) et [gatsby-plugin-mdx](https://www.gatsbyjs.org/packages/gatsby-plugin-mdx/) ont fait pour nous. Vous pouvez maintenant aller à l'explorateur Gatsby GraphQL GraphiQL et vérifier les données :

```graphql
{
  allMdx {
    nodes {
      frontmatter {
        title
        date
      }
    }
  }
}
```

%[https://youtu.be/MPNJu24ad_s]

## Métadonnées du site

Lorsque vous souhaitez réutiliser des morceaux de données courants sur le site (par exemple, le titre de votre site), vous pouvez stocker ces données dans `siteMetadata`. Vous avez abordé cela lors de la définition du `gatsby-config.js`, et maintenant vous allez séparer cela de `module.exports`. Pourquoi ? Il sera plus agréable de raisonner une fois que la configuration est remplie de plugins.

En haut de `gatsby-config.js`, ajoutez un nouvel objet variable pour les métadonnées du site :

```js
const siteMetadata = {
  title: `The Localhost Blog`,
  description: `This is my coding blog where I write about my coding journey.`,
};
```

Maintenant, interrogez les métadonnées du site avec GraphQL.

```graphql
{
  site {
    siteMetadata {
      title
      description
    }
  }
}
```

## Hook des métadonnées du site

D'accord, c'est cool et tout, mais comment suis-je censé l'utiliser ? Nous allons faire un peu de code et créer un hook React pour que vous puissiez obtenir vos données de site dans n'importe quel composant dont vous avez besoin.

Créez un dossier pour garder tous vos hooks et créez un fichier pour notre hook. Dans le terminal, faites :

```bash
mkdir src/hooks
touch src/hooks/useSiteMetadata.js
```

D'accord, et dans votre fichier nouvellement créé, nous allons utiliser le hook `useStaticQuery` de Gatsby pour créer votre propre hook :

```js
import { graphql, useStaticQuery } from 'gatsby';

export const useSiteMetadata = () => {
  const { site } = useStaticQuery(
    graphql`
      query SITE_METADATA_QUERY {
        site {
          siteMetadata {
            title
            description
          }
        }
      }
    `
  );
  return site.siteMetadata;
};
```

Maintenant, vous pouvez utiliser ce hook n'importe où dans votre site, alors faites-le maintenant dans `src/pages/index.js` :

```js
import React from 'react';
import { useSiteMetadata } from '../hooks/useSiteMetadata';

export default () => {
  const { title, description } = useSiteMetadata();
  return (
    <>
      <h1>{title}</h1>
      <p>{description}</p>
    </>
  );
};
```

%[https://youtu.be/TfycpV4yyqY]

## Stylisation

Vous allez utiliser styled-components pour le style. Styled-components (pour moi) aide à la portée des styles dans vos composants. Il est temps de passer en revue les bases maintenant.

### installer styled-components

```bash
yarn add gatsby-plugin-styled-components styled-components babel-plugin-styled-components
```

Alors, qu'est-ce que tout cela que je viens d'installer ?

Le plugin babel est pour le nommage automatique des composants afin d'aider au débogage.

Le plugin Gatsby est pour le support de rendu côté serveur intégré.

### Configurer

D'accord, avec cette explication détaillée hors du chemin, configurez-les dans `gatsby-config.js` :

```js
const siteMetadata = {
  title: `The Localhost Blog`,
  description: `This is my coding blog where I write about my coding journey.`,
};

module.exports = {
  siteMetadata: siteMetadata,
  plugins: [
    `gatsby-plugin-styled-components`,
    {
      resolve: `gatsby-plugin-mdx`,
      options: {
        extensions: [`.mdx`, `.md`],
      },
    },
    {
      resolve: `gatsby-source-filesystem`,
      options: { path: `${__dirname}/posts`, name: `posts` },
    },
  ],
};
```

Il est temps de passer en revue un composant stylisé. Dans `index.js`, vous allez `importer styled depuis 'styled-components'` et créer une variable `StyledH1`.

Donc, vous utilisez la variable pour envelopper votre `{title}` que vous déstructurez depuis le hook `useSiteMetadata` que vous avez créé précédemment.

Pour cet exemple, faites-le en violet iconique de Gatsby `rebeccapurple`.

```js
import React from 'react';
import styled from 'styled-components';
import { useSiteMetadata } from '../hooks/useSiteMetadata';

const StyledH1 = styled.h1`
  color: rebeccapurple;
`;

export default () => {
  const { title, description } = useSiteMetadata();
  return (
    <>
      <StyledH1>{title}</StyledH1>
      <p>{description}</p>
    </>
  );
};
```

C'est styled-components à un niveau très basique. Basiquement, créez le style que vous voulez pour les éléments de page que vous créez dans le JSX.

%[https://youtu.be/41aNkb2tLyg]

## Mise en page

Gatsby n'applique aucune mise en page par défaut mais utilise plutôt la manière dont vous pouvez composer des composants React pour la mise en page. Cela signifie que c'est à vous de décider comment vous voulez disposer ce que vous construisez avec Gatsby.

Dans ce guide, nous allons initialement créer un composant de mise en page de base que vous ajouterez au fur et à mesure. Pour plus de détails sur les composants de mise en page, consultez la page des composants de mise en page de Gatsby [layout components](https://www.gatsbyjs.org/docs/layout-components/).

Maintenant, vous allez refactoriser la page d'accueil (`src/pages/index.js`) un peu et créer quelques composants pour la mise en page et l'en-tête de votre blog. Dans le terminal, créez un répertoire de composants et un composant `Header` et `Layout` :

```bash
mkdir src/components
touch src/components/Header.js src/components/Layout.js
```

Maintenant, déplacez le titre et la description de `src/pages/index.js` vers le composant nouvellement créé `src/components/Header.js`, en déstructurant les props pour le `siteTitle` et `siteDescription`, que vous passerez depuis le composant `Layout` ici. Vous allez ajouter Gatsby Link à cela pour que les utilisateurs puissent cliquer sur l'en-tête pour revenir à la page d'accueil.

```js
import { Link } from 'gatsby';
import React from 'react';

export const Header = ({ siteTitle, siteDescription }) => (
  <Link to="/">
    <h1>{siteTitle}</h1>
    <p>{siteDescription}</p>
  </Link>
);
```

Maintenant, pour le composant Layout : ceci sera un composant wrapper basique pour l'instant. Vous allez utiliser votre hook de métadonnées de site pour le titre et la description et les passer au composant d'en-tête et retourner les enfants du wrapper (`Layout`).

```js
import React from 'react';
import { useSiteMetadata } from '../hooks/useSiteMetadata';
import { Header } from './Header';

export const Layout = ({ children }) => {
  const { title, description } = useSiteMetadata();
  return (
    <>
      <Header siteTitle={title} siteDescription={description} />
      {children}
    </>
  );
};
```

Maintenant, pour ajouter le plus léger des styles pour un peu d'alignement pour `src/components/Layout.js`, créez un composant `AppStyles` stylisé et faites-en le wrapper principal de votre `Layout`.

```js
import React from 'react';
import styled from 'styled-components';
import { useSiteMetadata } from '../hooks/useSiteMetadata';
import { Header } from './Header';

const AppStyles = styled.main`
  width: 800px;
  margin: 0 auto;
`;

export const Layout = ({ children }) => {
  const { title, description } = useSiteMetadata();
  return (
    <AppStyles>
      <Header siteTitle={title} siteDescription={description} />
      {children}
    </AppStyles>
  );
};
```

D'accord, maintenant refactorisez votre page d'accueil (`src/pages/index.js`) avec `Layout`.

```js
import React from 'react';
import { Layout } from '../components/Layout';

export default () => {
  return (
    <>
      <Layout />
    </>
  );
};
```

%[https://youtu.be/Ase7bjxtQ3w]

## Requête des articles de la page d'index

Maintenant, vous pouvez jeter un coup d'œil à l'ajout de certains des articles que vous avez créés à la page d'index de votre blog. Vous allez le faire en créant une requête GraphQL pour lister les articles par titre, les trier par date et ajouter un extrait de l'article.

La requête ressemblera à ceci :

```graphql
{
  allMdx {
    nodes {
      id
      excerpt(pruneLength: 250)
      frontmatter {
        title
        date
      }
    }
  }
}
```

Si vous mettez cela dans l'interface graphique GraphiQL, vous remarquerez que les articles ne sont pas dans un ordre donné. Ajoutez donc un tri à cela - et vous allez également ajouter un filtre pour les articles marqués comme publiés ou non.

```graphql
{
  allMdx(
    sort: { fields: [frontmatter___date], order: DESC }
    filter: { frontmatter: { published: { eq: true } } }
  ) {
    nodes {
      id
      excerpt(pruneLength: 250)
      frontmatter {
        title
        date
      }
    }
  }
}
```

Sur la page d'accueil (`src/pages/index.js`), vous allez utiliser la requête que nous venons d'assembler pour obtenir une liste d'articles publiés dans l'ordre des dates ; ajoutez ce qui suit au fichier `index.js` :

```js
import { graphql } from 'gatsby';
import React from 'react';
import { Layout } from '../components/Layout';

export default ({ data }) => {
  return (
    <>
      <Layout>
        {data.allMdx.nodes.map(({ excerpt, frontmatter }) => (
          <>
            <h1>{frontmatter.title}</h1>
            <p>{frontmatter.date}</p>
            <p>{excerpt}</p>
          </>
        ))}
      </Layout>
    </>
  );
};

export const query = graphql`
  query SITE_INDEX_QUERY {
    allMdx(
      sort: { fields: [frontmatter___date], order: DESC }
      filter: { frontmatter: { published: { eq: true } } }
    ) {
      nodes {
        id
        excerpt(pruneLength: 250)
        frontmatter {
          title
          date
        }
      }
    }
  }
`;
```

Woah ! WTF était tout ça yo ?!

D'accord, vous parcourez les données passées dans le composant via la requête GraphQL. Gatsby `graphql` exécute la requête (`SITE_INDEX_QUERY`) au moment de l'exécution et nous donne les résultats en tant que props à votre composant via la prop `data`.

%[https://youtu.be/2GDbxZ0mHbM]

## Slugs et chemins

Gatsby source filesystem aidera à la création de slugs (chemins d'URL pour les articles que vous créez). Dans le nœud Gatsby, vous allez créer les slugs pour vos articles.

Tout d'abord, vous allez devoir créer un fichier `gatsby-node.js` :

```bash
touch gatsby-node.js
```

Cela créera le chemin du fichier (URL) pour chacun des articles du blog.

Vous allez utiliser l'API Gatsby Node `onCreateNode` et déstructurer `node`, `actions` et `getNode` pour les utiliser dans la création des emplacements de fichiers et de la valeur associée.

```ja
const { createFilePath } = require(`gatsby-source-filesystem`);

exports.onCreateNode = ({ node, actions, getNode }) => {
  const { createNodeField } = actions;
  if (node.internal.type === `Mdx`) {
    const value = createFilePath({ node, getNode });
    createNodeField({
      name: `slug`,
      node,
      value,
    });
  }
};
```

Maintenant, pour aider à visualiser certaines des données transmises aux composants, vous allez utiliser [Dump.js](https://github.com/wesbos/dump) pour déboguer les données. Merci à Wes Bos pour le super pratique composant [Dump.js](https://github.com/wesbos/dump).

Pour configurer le composant, créez un fichier `Dump.js` dans votre dossier `src\components` et copiez-collez le code de la page GitHub liée.

```bash
touch /src/components/Dump.js
```

```js
import React from 'react';

const Dump = props => (
  <div
    style={{
      fontSize: 20,
      border: '1px solid #efefef',
      padding: 10,
      background: 'white',
    }}>
    {Object.entries(props).map(([key, val]) => (
      <pre key={key}>
        <strong style={{ color: 'white', background: 'red' }}>
          {key} ?
        </strong>
        {JSON.stringify(val, '', ' ')}
      </pre>
    ))}
  </div>
);

export default Dump;
```

Maintenant, vous pouvez utiliser le composant `Dump` n'importe où dans votre projet. Pour démontrer, utilisez-le avec la `data` de la page d'index pour voir le résultat.

Donc dans le `src/pages/index.js`, vous allez importer le composant Dump et passer la prop `data` et voir à quoi ressemble la sortie.

```js
import { graphql } from 'gatsby';
import React from 'react';
import Dump from '../components/Dump';
import { Layout } from '../components/Layout';

export default ({ data }) => {
  return (
    <>
      <Layout>
        <Dump data={data} />
        {data.allMdx.nodes.map(({ excerpt, frontmatter }) => (
          <>
            <h1>{frontmatter.title}</h1>
            <p>{frontmatter.date}</p>
            <p>{excerpt}</p>
          </>
        ))}
      </Layout>
    </>
  );
};

export const query = graphql`
  query SITE_INDEX_QUERY {
    allMdx(
      sort: { fields: [frontmatter___date], order: DESC }
      filter: { frontmatter: { published: { eq: true } } }
    ) {
      nodes {
        id
        excerpt(pruneLength: 250)
        frontmatter {
          title
          date
        }
      }
    }
  }
`;
```

%[https://youtu.be/7eZZk7aJnUU]

## Chemins de lien

Maintenant que vous avez créé les chemins, vous pouvez les lier avec Gatsby Link. Tout d'abord, vous devrez ajouter le slug à votre `SITE_INDEX_QUERY`. Ensuite, vous pouvez ajouter le `Link` de Gatsby à `src/pages/index.js`.

Vous allez également créer quelques styled-components pour envelopper la liste des articles ainsi que chaque article individuel.

```js
import { graphql, Link } from 'gatsby';
import React from 'react';
import styled from 'styled-components';
import { Layout } from '../components/Layout';

const IndexWrapper = styled.main``;

const PostWrapper = styled.div``;

export default ({ data }) => {
  return (
    <Layout>
      <IndexWrapper>
        {data.allMdx.nodes.map(
          ({ id, excerpt, frontmatter, fields }) => (
            <PostWrapper key={id}>
              <Link to={fields.slug}>
                <h1>{frontmatter.title}</h1>
                <p>{frontmatter.date}</p>
                <p>{excerpt}</p>
              </Link>
            </PostWrapper>
          )
        )}
      </IndexWrapper>
    </Layout>
  );
};

export const query = graphql`
  query SITE_INDEX_QUERY {
    allMdx(
      sort: { fields: [frontmatter___date], order: DESC }
      filter: { frontmatter: { published: { eq: true } } }
    ) {
      nodes {
        id
        excerpt(pruneLength: 250)
        frontmatter {
          title
          date
        }
        fields {
          slug
        }
      }
    }
  }
`;
```

## Ajout d'un modèle de blog

Maintenant que vous avez les liens pointant vers les articles du blog, vous n'avez actuellement aucun fichier associé au chemin. Cela signifie que cliquer sur un lien vous donnera une erreur 404 et le 404 intégré de Gatsby listera toutes les pages disponibles dans le projet, actuellement seulement l'index `/` ou la page d'accueil.

Donc, pour chacun de vos articles de blog, vous allez utiliser un modèle qui contiendra les informations nécessaires pour composer votre article de blog. Pour commencer, créez un répertoire `templates` et un fichier de modèle pour cela avec :

```bash
mkdir -p src/templates
touch src/templates/blogPostTemplate.js
```

Pour l'instant, vous allez créer un modèle de base (vous allez ajouter des données à cela sous peu) :

```js
import React from 'react';

export default () => {
  return (
    <>
      <p>post here</p>
    </>
  );
};
```

Pour remplir le modèle, vous devrez utiliser Gatsby node pour créer vos pages.

Gatsby Node dispose de nombreuses API internes disponibles pour nous. Pour cet exemple, vous allez utiliser l'API `createPages`.

Plus d'informations sur l'API Gatsby `createPages` peuvent être trouvées dans la documentation de Gatsby, détails ici : [https://www.gatsbyjs.org/docs/node-apis/#createPages](https://www.gatsbyjs.org/docs/node-apis/#createPages)

Dans votre fichier `gatsby-node.js`, vous allez ajouter ce qui suit en plus de l'export `onCreateNode` que vous avez fait précédemment.

```js
const { createFilePath } = require(`gatsby-source-filesystem`);
const path = require(`path`);

exports.createPages = ({ actions, graphql }) => {
  const { createPage } = actions;
  const blogPostTemplate = path.resolve(
    'src/templates/blogPostTemplate.js'
  );

  return graphql(`
    {
      allMdx {
        nodes {
          fields {
            slug
          }
          frontmatter {
            title
          }
        }
      }
    }
  `).then(result => {
    if (result.errors) {
      throw result.errors;
    }

    const posts = result.data.allMdx.nodes;

    // create page for each mdx file
    posts.forEach(post => {
      createPage({
        path: post.fields.slug,
        component: blogPostTemplate,
        context: {
          slug: post.fields.slug,
        },
      });
    });
  });
};

exports.onCreateNode = ({ node, actions, getNode }) => {
  const { createNodeField } = actions;
  if (node.internal.type === `Mdx`) {
    const value = createFilePath({ node, getNode });
    createNodeField({
      name: `slug`,
      node,
      value,
    });
  }
};
```

La partie à laquelle vous devez prêter une attention particulière pour l'instant est la boucle `.forEach` où vous utilisez la fonction `createPage` que nous avons déstructurée de l'objet `actions`.

C'est ici que vous passez les données nécessaires par `blogPostTemplate` que vous avez défini précédemment. Vous allez ajouter plus de données au `context` pour la navigation des articles bientôt.

```js
// create page for each mdx node
posts.forEach(post => {
  createPage({
    path: post.fields.slug,
    component: blogPostTemplate,
    context: {
      slug: post.fields.slug,
    },
  });
});
```

%[https://youtu.be/OyQfIvXr4YA]

## Construire le modèle de blog

Maintenant, vous allez utiliser les informations de contexte passées à `blogPostTemplate.js` pour créer la page de l'article de blog.

Cela est similaire à la page d'accueil `index.js`, où des données GraphQL sont utilisées pour créer la page. Mais dans ce cas, le modèle utilise une variable (également connue sous le nom de paramètre ou d'identifiant) afin que vous puissiez interroger des données spécifiques à cette variable donnée.

Maintenant, plongez rapidement dans cela avec une démonstration. Dans l'interface graphique GraphiQL, créez une requête nommée et définissez la variable que vous allez passer :

```graphql
query PostBySlug($slug: String!) {
  mdx(fields: { slug: { eq: $slug } }) {
    frontmatter {
      title
      date(formatString: "YYYY MMMM Do")
    }
  }
}
```

Ici, vous définissez la variable comme slug avec le `$` indiquant qu'il s'agit d'une variable. Vous devez également définir le type de variable comme (dans ce cas) `String!`. Le point d'exclamation après le type signifie qu'il doit s'agir d'une chaîne de caractères passée dans la requête.

En utilisant `mdx`, vous allez filtrer sur `fields` où le `slug` correspond à la variable passée dans la requête.

L'exécution de la requête maintenant affichera une erreur car aucune variable n'est alimentée dans la requête. Si vous regardez en bas du panneau de requête, vous devriez remarquer `QUERY VARIABLES`. Cliquez dessus pour faire apparaître le panneau des variables.

C'est ici que vous pouvez ajouter l'un des chemins de publication que vous avez créés précédemment. Si vous avez votre serveur de développement en cours d'exécution, allez à l'un des articles et prenez le chemin et collez-le entre les guillemets `""` et essayez d'exécuter la requête à nouveau.

```graphql
{
  "slug": "/2019/2019-06-20-third-post/"
}
```

Il est temps d'utiliser ces données pour créer le post. Vous allez ajouter `body` à la requête et l'avoir en bas de votre fichier de page.

Pour l'instant, vous allez créer un simple composant react qui affichera les données que vous avez interrogées.

En déstructurant le `frontmatter` et le `body` de la requête GraphQL, vous obtiendrez le titre et la date du frontmatter et envelopperez le `body` dans le `MDXRenderer`.

```js
import { graphql } from 'gatsby';
import { MDXRenderer } from 'gatsby-plugin-mdx';
import React from 'react';
import { Layout } from '../components/Layout';

export default ({ data }) => {
  const { frontmatter, body } = data.mdx;
  return (
    <Layout>
      <h1>{frontmatter.title}</h1>
      <p>{frontmatter.date}</p>
      <MDXRenderer>{body}</MDXRenderer>
    </Layout>
  );
};

export const query = graphql`
  query PostsBySlug($slug: String!) {
    mdx(fields: { slug: { eq: $slug } }) {
      body
      frontmatter {
        title
        date(formatString: "YYYY MMMM Do")
      }
    }
  }
`;
```

Si vous ne l'avez pas encore fait, maintenant serait un bon moment pour redémarrer votre serveur de développement.

Maintenant, vous pouvez cliquer sur l'un des liens des articles et voir votre modèle de blog dans toute sa gloire basique !

%[https://youtu.be/S7cnkRoCjsc]

## Navigation Précédent et Suivant

Coolio ! Maintenant que vous avez votre blog de base où vous pouvez lister les articles disponibles et cliquer sur un lien pour voir l'article complet dans un modèle prédéfini. Une fois que vous êtes dans un article, vous devez naviguer vers la page d'accueil pour choisir un nouvel article à lire. Dans cette section, vous allez travailler sur l'ajout d'une navigation précédent et suivant.

Vous vous souvenez de l'extrait `.forEach` que vous avez regardé plus tôt ? C'est là que vous allez passer un contexte supplémentaire à la page en sélectionnant les articles précédent et suivant.

```js
// create page for each mdx node
posts.forEach((post, index) => {
  const previous =
    index === posts.length - 1 ? null : posts[index + 1];
  const next = index === 0 ? null : posts[index - 1];

  createPage({
    path: post.fields.slug,
    component: blogPostTemplate,
    context: {
      slug: post.fields.slug,
      previous,
      next,
    },
  });
});
```

Cela devrait maintenant correspondre à la requête que vous avez sur la page d'accueil (`src/pages/index.js`) sauf que vous n'avez actuellement aucun filtre ou tri appliqué ici. Donc faites cela maintenant dans `gatsby-node.js` et appliquez les mêmes filtres que sur la requête de la page d'accueil :

```js
const { createFilePath } = require(`gatsby-source-filesystem`);
const path = require(`path`);

exports.createPages = ({ actions, graphql }) => {
  const { createPage } = actions;
  const blogPostTemplate = path.resolve(
    'src/templates/blogPostTemplate.js'
  );

  return graphql(`
    {
      allMdx(
        sort: { fields: [frontmatter___date], order: DESC }
        filter: { frontmatter: { published: { eq: true } } }
      ) {
        nodes {
          fields {
            slug
          }
          frontmatter {
            title
          }
        }
      }
    }
  `).then(result => {
    if (result.errors) {
      throw result.errors;
    }

    const posts = result.data.allMdx.nodes;

    // create page for each mdx node
    posts.forEach((post, index) => {
      const previous =
        index === posts.length - 1 ? null : posts[index + 1];
      const next = index === 0 ? null : posts[index - 1];

      createPage({
        path: post.fields.slug,
        component: blogPostTemplate,
        context: {
          slug: post.fields.slug,
          previous,
          next,
        },
      });
    });
  });
};

exports.onCreateNode = ({ node, actions, getNode }) => {
  const { createNodeField } = actions;
  if (node.internal.type === `Mdx`) {
    const value = createFilePath({ node, getNode });
    createNodeField({
      name: `slug`,
      node,
      value,
    });
  }
};
```

Maintenant, vous pourrez exposer les objets `previous` et `next` passés en contexte depuis le nœud Gatsby.

Vous pouvez déstructurer `previous` et `next` depuis `pageContext` et pour l'instant les placer dans votre super pratique composant `Dump` pour voir leur contenu.

```js
import { graphql } from 'gatsby';
import { MDXRenderer } from 'gatsby-plugin-mdx';
import React from 'react';
import Dump from '../components/Dump';
import { Layout } from '../components/Layout';

export default ({ data, pageContext }) => {
  const { frontmatter, body } = data.mdx;
  const { previous, next } = pageContext;
  return (
    <Layout>
      <Dump previous={previous} />
      <Dump next={next} />
      <h1>{frontmatter.title}</h1>
      <p>{frontmatter.date}</p>
      <MDXRenderer>{body}</MDXRenderer>
    </Layout>
  );
};

export const query = graphql`
  query PostsBySlug($slug: String!) {
    mdx(fields: { slug: { eq: $slug } }) {
      body
      frontmatter {
        title
        date(formatString: "YYYY MMMM Do")
      }
    }
  }
`;
```

Ajoutez la navigation précédent et suivant, il s'agit de quelques opérations ternaires. Si la variable est vide, alors retournez `null`, sinon rendez un composant `Link` de Gatsby avec le slug de la page et le titre du frontmatter :

```js
import { graphql, Link } from 'gatsby';
import { MDXRenderer } from 'gatsby-plugin-mdx';
import React from 'react';
import Dump from '../components/Dump';
import { Layout } from '../components/Layout';

export default ({ data, pageContext }) => {
  const { frontmatter, body } = data.mdx;
  const { previous, next } = pageContext;
  return (
    <Layout>
      <Dump previous={previous} />
      <Dump next={next} />
      <h1>{frontmatter.title}</h1>
      <p>{frontmatter.date}</p>
      <MDXRenderer>{body}</MDXRenderer>
      {previous === false ? null : (
        <>
          {previous && (
            <Link to={previous.fields.slug}>
              <p>{previous.frontmatter.title}</p>
            </Link>
          )}
        </>
      )}
      {next === false ? null : (
        <>
          {next && (
            <Link to={next.fields.slug}>
              <p>{next.frontmatter.title}</p>
            </Link>
          )}
        </>
      )}
    </Layout>
  );
};

export const query = graphql`
  query PostsBySlug($slug: String!) {
    mdx(fields: { slug: { eq: $slug } }) {
      body
      frontmatter {
        title
        date(formatString: "YYYY MMMM Do")
      }
    }
  }
`;
```

%[https://youtu.be/AjLimYEwDOk]

## Blocs de code

Maintenant, pour ajouter une coloration syntaxique pour ajouter des blocs de code à vos pages de blog. Pour cela, vous allez ajouter des dépendances pour [prism-react-renderer](https://github.com/FormidableLabs/prism-react-renderer) et [react-live](https://github.com/FormidableLabs/react-live). Vous allez également créer les fichiers dont vous aurez besoin pour les utiliser :

```bash
yarn add prism-react-renderer react-live
touch root-wrapper.js gatsby-ssr.js gatsby-browser.js
```

Vous en viendrez à `react-live` bientôt. Pour l'instant, vous allez faire fonctionner `prism-react-render` pour la coloration syntaxique de tout code que vous allez ajouter au blog. Mais avant cela, vous allez passer en revue le concept de wrapper racine.

Donc, pour changer le rendu d'un élément de page, comme un titre ou un bloc de code, vous allez devoir utiliser le `MDXProvider`. Le `MDXProvider` est un composant que vous pouvez utiliser n'importe où plus haut dans l'arbre des composants React que le contenu MDX que vous souhaitez rendre.

Gatsby browser et Gatsby SSR ont tous deux `wrapRootElement` disponible pour eux et c'est aussi haut dans l'arbre que vous pouvez aller. Donc vous allez créer le fichier `root-wrapper.js` et ajouter les éléments que vous souhaitez remplacer là et l'importer dans `gatsby-browser.js` et `gatsby-ssr.js` pour ne pas dupliquer le code.

Avant d'aller plus loin, je veux ajouter qu'il existe une ressource de qualité supérieure [playlist egghead.io](https://egghead.io/lessons/vue-js-introduction-to-mdx?pl=building-websites-with-mdx-and-gatsby-161e9529) pour utiliser MDX avec Gatsby par Chris [Chris Biscardi](https://twitter.com/chrisbiscardi). Il y a une tonne d'informations utiles là-bas sur MDX dans Gatsby.

D'accord, commencez par importer le fichier `root-wrapper.js` dans `gatsby-browser.js` et `gatsby-ssr.js`. Dans les deux modules de code, collez ce qui suit :

```js
import { wrapRootElement as wrap } from './root-wrapper';

export const wrapRootElement = wrap;
```

D'accord, maintenant vous pouvez travailler sur le code qui sera utilisé dans les deux modules. MDX vous permet de contrôler le rendu des éléments de page dans votre markdown. `MDXProvider` est utilisé pour donner des composants React pour remplacer les éléments de page markdown.

Démonstration rapide, dans `root-wrapper.js`, ajoutez ce qui suit :

```js
import { MDXProvider } from '@mdx-js/react';
import React from 'react';

const components = {
  h2: ({ children }) => (
    <h2 style={{ color: 'rebeccapurple' }}>{children}</h2>
  ),
  'p.inlineCode': props => (
    <code style={{ backgroundColor: 'lightgray' }} {...props} />
  ),
};

export const wrapRootElement = ({ element }) => (
  <MDXProvider components={components}>{element}</MDXProvider>
);
```

Vous remplacez maintenant tout `h2` dans votre markdown rendu ainsi que tout bloc de `code` (c'est-à-dire les mots enveloppés dans des ``backticks``).

%[https://youtu.be/kN8ld7iLQso]

D'accord, maintenant pour la coloration syntaxique, créez un article avec un bloc de code dedans :

```bash
mkdir posts/2019-07-01-code-blocks
touch posts/2019-07-01-code-blocks/index.mdx
```

Collez un peu de contenu :

```markdown
---
title: Code Blocks
date: 2019-07-01
published: true
---

## Yes! Some code!

Here is the `Dump` component!

```jsx
import React from 'react';

const Dump = props => (
  <div
    style={{
      fontSize: 20,
      border: '1px solid #efefef',
      padding: 10,
      background: 'white',
    }}>
    {Object.entries(props).map(([key, val]) => (
      <pre key={key}>
        <strong style={{ color: 'white', background: 'red' }}>
          {key} ?
        </strong>
        {JSON.stringify(val, '', ' ')}
      </pre>
    ))}
  </div>
);

export default Dump;
```
```

Allez sur la page GitHub de [prism-react-renderer](https://github.com/FormidableLabs/prism-react-renderer) et copiez le code d'exemple dans `root-wrapper.js` pour l'élément `pre`.

Vous allez copier le code fourni pour la coloration afin de valider qu'il fonctionne.

```js
import { MDXProvider } from '@mdx-js/react';
import Highlight, { defaultProps } from 'prism-react-renderer';
import React from 'react';

const components = {
  h2: ({ children }) => (
    <h2 style={{ color: 'rebeccapurple' }}>{children}</h2>
  ),
  'p.inlineCode': props => (
    <code style={{ backgroundColor: 'lightgray' }} {...props} />
  ),
  pre: props => (
    <Highlight
      {...defaultProps}
      code={`
        (function someDemo() {
          var test = "Hello World!";
          console.log(test);
        })();

        return () => <App />;
      `}
      language="jsx">
      {({
        className,
        style,
        tokens,
        getLineProps,
        getTokenProps,
      }) => (
        <pre className={className} style={style}>
          {tokens.map((line, i) => (
            <div {...getLineProps({ line, key: i })}>
              {line.map((token, key) => (
                <span {...getTokenProps({ token, key })} />
              ))}
            </div>
          ))}
        </pre>
      )}
    </Highlight>
  ),
};

export const wrapRootElement = ({ element }) => (
  <MDXProvider components={components}>{element}</MDXProvider>
);
```

Cool, cool ! Maintenant, vous voulez remplacer l'exemple de code collé par les props de l'élément enfant du composant pre. Vous pouvez faire cela avec `props.children.props.children.trim()` ?.

```js
import { MDXProvider } from '@mdx-js/react';
import Highlight, { defaultProps } from 'prism-react-renderer';
import React from 'react';

const components = {
  pre: props => (
    <Highlight
      {...defaultProps}
      code={props.children.props.children.trim()}
      language="jsx">
      {({
        className,
        style,
        tokens,
        getLineProps,
        getTokenProps,
      }) => (
        <pre className={className} style={style}>
          {tokens.map((line, i) => (
            <div {...getLineProps({ line, key: i })}>
              {line.map((token, key) => (
                <span {...getTokenProps({ token, key })} />
              ))}
            </div>
          ))}
        </pre>
      )}
    </Highlight>
  ),
};

export const wrapRootElement = ({ element }) => (
  <MDXProvider components={components}>{element}</MDXProvider>
);
```

Ensuite, pour faire correspondre la langue, pour l'instant, vous allez ajouter une fonction `matches` pour faire correspondre la classe de langue assignée au bloc de code.

```js
import { MDXProvider } from '@mdx-js/react';
import Highlight, { defaultProps } from 'prism-react-renderer';
import React from 'react';

const components = {
  h2: ({ children }) => (
    <h2 style={{ color: 'rebeccapurple' }}>{children}</h2>
  ),
  'p.inlineCode': props => (
    <code style={{ backgroundColor: 'lightgray' }} {...props} />
  ),
  pre: props => {
    const className = props.children.props.className || '';
    const matches = className.match(/language-(?<lang>.*)/);
    return (
      <Highlight
        {...defaultProps}
        code={props.children.props.children.trim()}
        language={
          matches && matches.groups && matches.groups.lang
            ? matches.groups.lang
            : ''
        }>
        {({
          className,
          style,
          tokens,
          getLineProps,
          getTokenProps,
        }) => (
          <pre className={className} style={style}>
            {tokens.map((line, i) => (
              <div {...getLineProps({ line, key: i })}>
                {line.map((token, key) => (
                  <span {...getTokenProps({ token, key })} />
                ))}
              </div>
            ))}
          </pre>
        )}
      </Highlight>
    );
  },
};

export const wrapRootElement = ({ element }) => (
  <MDXProvider components={components}>{element}</MDXProvider>
);
```

[prism-react-renderer](https://github.com/FormidableLabs/prism-react-renderer) propose des thèmes supplémentaires en plus du thème par défaut qui est [duotoneDark](https://github.com/FormidableLabs/prism-react-renderer/blob/master/themes/duotoneDark.js). Vous allez utiliser [nightOwl](https://github.com/FormidableLabs/prism-react-renderer/blob/master/themes/nightOwl.js) dans cet exemple, mais n'hésitez pas à jeter un coup d'œil aux [autres exemples](https://github.com/FormidableLabs/prism-react-renderer/blob/master/themes) si vous le souhaitez.

Importez le `theme` puis utilisez-le dans les props du composant `Highlight`.

```js
import { MDXProvider } from '@mdx-js/react';
import Highlight, { defaultProps } from 'prism-react-renderer';
import theme from 'prism-react-renderer/themes/nightOwl';
import React from 'react';

const components = {
  pre: props => {
    const className = props.children.props.className || '';
    const matches = className.match(/language-(?<lang>.*)/);

    return (
      <Highlight
        {...defaultProps}
        code={props.children.props.children.trim()}
        language={
          matches && matches.groups && matches.groups.lang
            ? matches.groups.lang
            : ''
        }
        theme={theme}>
        {({
          className,
          style,
          tokens,
          getLineProps,
          getTokenProps,
        }) => (
          <pre className={className} style={style}>
            {tokens.map((line, i) => (
              <div {...getLineProps({ line, key: i })}>
                {line.map((token, key) => (
                  <span {...getTokenProps({ token, key })} />
                ))}
              </div>
            ))}
          </pre>
        )}
      </Highlight>
    );
  },
};

export const wrapRootElement = ({ element }) => (
  <MDXProvider components={components}>{element}</MDXProvider>
);
```

%[https://youtu.be/k6gI3jVxjKg]

D'accord, maintenant il est temps d'abstraire cela dans son propre composant pour que votre `root-wrapper.js` ne soit pas si encombré.

Créez un composant `Code.js`, et déplacez le code de `root-wrapper.js` dedans :

```bash
touch src/components/Code.js
```

Vous vous souvenez de ceci ?

> Cool, cool ! Maintenant, vous voulez remplacer l'exemple de code collé par les props de l'élément enfant du composant pre. Vous pouvez faire cela avec `props.children.props.children.trim()` ?.

Si cela ne fait pas vraiment sens pour vous (j'ai dû le lire de nombreuses, nombreuses fois moi-même), ne vous inquiétez pas : maintenant vous allez approfondir cela un peu plus pour la création du composant de bloc de code.

Donc, pour l'instant dans les `components` que vous ajoutez dans le `MDXProvider`, regardez les `props` entrant dans l'élément `pre`.

Commentez le code que vous avez ajouté précédemment et ajoutez un `console.log` :

```js
pre: props => {
  console.log('=====================');
  console.log(props);
  console.log('=====================');
  return <pre />;
};
```

Maintenant, si vous ouvrez les outils de développement de votre navigateur, vous pouvez voir la sortie.

```json
{children: {}}
  children:
    $$typeof: Symbol(react.element)
    key: null
    props: {parentName: "pre", className: "language-jsx", originalType: "code", mdxType: "code", children: "import React from 'react'		const Dump = props => (  </pre>	    ))}	  </div>	)		export default Dump	"}
    ref: null
    type:  (re....
```

Si vous approfondissez les props de cette sortie, vous pouvez voir les `children` de ces props. Si vous regardez le contenu de cela, vous verrez que c'est la chaîne de code pour votre bloc de code. C'est ce que vous allez passer dans le composant `Code` que vous êtes sur le point de créer. D'autres propriétés à noter ici sont le `className` et le `mdxType`.

Donc, prenez le code que vous avez utilisé précédemment pour `Highlight`, tout ce qui est à l'intérieur et y compris l'instruction `return`, et collez-le dans le module `Code.js` que vous avez créé précédemment.

`Highlight` nécessite plusieurs props :

```jsx
<Highlight
  {...defaultProps}
  code={codeString}
  language={language}
  theme={theme}
>
```

Le module `Code` devrait maintenant ressembler à ceci :

```js
import Highlight, { defaultProps } from 'prism-react-renderer';
import theme from 'prism-react-renderer/themes/nightOwl';
import React from 'react';

const Code = ({ codeString, language }) => {
  return (
    <Highlight
      {...defaultProps}
      code={codeString}
      language={language}
      theme={theme}>
      {({
        className,
        style,
        tokens,
        getLineProps,
        getTokenProps,
      }) => (
        <pre className={className} style={style}>
          {tokens.map((line, i) => (
            <div {...getLineProps({ line, key: i })}>
              {line.map((token, key) => (
                <span {...getTokenProps({ token, key })} />
              ))}
            </div>
          ))}
        </pre>
      )}
    </Highlight>
  );
};

export default Code;
```

Retournez au `root-wrapper` où vous allez passer les `props` nécessaires au composant `Code`.

La première vérification que vous allez faire est si le `mdxType` est `code`, alors vous pouvez obtenir les props supplémentaires dont vous avez besoin pour passer à votre composant `Code`.

Vous allez obtenir `defaultProps` et le `theme` de `prism-react-renderer`, donc tout ce dont vous avez besoin est le `code` et le `language`.

Le `codeString` que vous pouvez obtenir à partir des `props`, et les `children` en les déstructurant des `props` passés dans l'élément `pre`. Le `language` peut être soit le tag assigné à la propriété meta des backticks, comme `js`, `jsx`, soit également vide. Donc vous vérifiez cela avec un peu de JavaScript et supprimez également le préfixe `language-`, puis passez les éléments `{...props}` :

```js
pre: ({ children: { props } }) => {
  if (props.mdxType === 'code') {
    return (
      <Code
        codeString={props.children.trim()}
        language={
          props.className && props.className.replace('language-', '')
        }
        {...props}
      />
    );
  }
};
```

%[https://youtu.be/m0tWxa9Ip5E]

D'accord, maintenant vous êtes de retour là où vous étiez avant d'abstraire le composant `Highlight` dans son propre module. Ajoutez quelques styles supplémentaires avec `styled-components` et remplacez le `pre` par un `Pre` stylisé. Vous pouvez également ajouter quelques numéros de ligne avec un span stylisé et le styliser également.

```js
import Highlight, { defaultProps } from 'prism-react-renderer';
import theme from 'prism-react-renderer/themes/nightOwl';
import React from 'react';
import styled from 'styled-components';

export const Pre = styled.pre`
  text-align: left;
  margin: 1em 0;
  padding: 0.5em;
  overflow-x: auto;
  border-radius: 3px;

  & .token-line {
    line-height: 1.3em;
    height: 1.3em;
  }
  font-family: 'Courier New', Courier, monospace;
`;

export const LineNo = styled.span`
  display: inline-block;
  width: 2em;
  user-select: none;
  opacity: 0.3;
`;

const Code = ({ codeString, language, ...props }) => {
  return (
    <Highlight
      {...defaultProps}
      code={codeString}
      language={language}
      theme={theme}>
      {({
        className,
        style,
        tokens,
        getLineProps,
        getTokenProps,
      }) => (
        <Pre className={className} style={style}>
          {tokens.map((line, i) => (
            <div {...getLineProps({ line, key: i })}>
              <LineNo>{i + 1}</LineNo>
              {line.map((token, key) => (
                <span {...getTokenProps({ token, key })} />
              ))}
            </div>
          ))}
        </Pre>
      )}
    </Highlight>
  );
};

export default Code;
```

%[https://youtu.be/PPH153kWpqc]

### Copier le code dans le presse-papiers

Et si vous aviez un moyen d'obtenir cette chaîne de props de code dans le presse-papiers ?

J'ai regardé autour de moi et j'ai trouvé que la majorité des composants disponibles pour ce genre de chose s'attendaient à une entrée jusqu'à [ceci](https://github.com/gatsbyjs/gatsby/blob/master/www/src/utils/copy-to-clipboard.js) dans le code source de Gatsby. Qui crée l'entrée pour vous ?

Donc, créez un répertoire `utils` et le fichier `copy-to-clipboard.js` et ajoutez le code du code source de Gatsby.

```bash
mkdir src/utils
touch src/utils/copy-to-clipboard.js
```

```js
// https://github.com/gatsbyjs/gatsby/blob/master/www/src/utils/copy-to-clipboard.js

export const copyToClipboard = str => {
  const clipboard = window.navigator.clipboard;
  /*
   * fallback to older browsers (including Safari)
   * if clipboard API not supported
   */
  if (!clipboard || typeof clipboard.writeText !== `function`) {
    const textarea = document.createElement(`textarea`);
    textarea.value = str;
    textarea.setAttribute(`readonly`, true);
    textarea.setAttribute(`contenteditable`, true);
    textarea.style.position = `absolute`;
    textarea.style.left = `-9999px`;
    document.body.appendChild(textarea);
    textarea.select();
    const range = document.createRange();
    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    textarea.setSelectionRange(0, textarea.value.length);
    document.execCommand(`copy`);
    document.body.removeChild(textarea);

    return Promise.resolve(true);
  }

  return clipboard.writeText(str);
};
```

Maintenant, vous allez vouloir un moyen de déclencher la copie du code dans le presse-papiers.

Créons un bouton stylisé. Mais d'abord, ajoutez un `position: relative;` au composant `Pre` qui nous permettra de positionner le bouton stylisé :

```js
const CopyCode = styled.button`
  position: absolute;
  right: 0.25rem;
  border: 0;
  border-radius: 3px;
  margin: 0.25em;
  opacity: 0.3;
  &:hover {
    opacity: 1;
  }
`;
```

Et maintenant, vous devez utiliser la fonction `copyToClipboard` dans le `onClick` du bouton :

```js
import Highlight, { defaultProps } from 'prism-react-renderer';
import theme from 'prism-react-renderer/themes/nightOwl';
import React from 'react';
import styled from 'styled-components';
import { copyToClipboard } from '../utils/copy-to-clipboard';

export const Pre = styled.pre`
  text-align: left;
  margin: 1rem 0;
  padding: 0.5rem;
  overflow-x: auto;
  border-radius: 3px;

  & .token-lline {
    line-height: 1.3rem;
    height: 1.3rem;
  }
  font-family: 'Courier New', Courier, monospace;
  position: relative;
`;

export const LineNo = styled.span`
  display: inline-block;
  width: 2rem;
  user-select: none;
  opacity: 0.3;
`;

const CopyCode = styled.button`
  position: absolute;
  right: 0.25rem;
  border: 0;
  border-radius: 3px;
  margin: 0.25em;
  opacity: 0.3;
  &:hover {
    opacity: 1;
  }
`;

const Code = ({ codeString, language }) => {
  const handleClick = () => {
    copyToClipboard(codeString);
  };

  return (
    <Highlight
      {...defaultProps}
      code={codeString}
      language={language}
      theme={theme}>
      {({
        className,
        style,
        tokens,
        getLineProps,
        getTokenProps,
      }) => (
        <Pre className={className} style={style}>
          <CopyCode onClick={handleClick}>Copy</CopyCode>
          {tokens.map((line, i) => (
            <div {...getLineProps({ line, key: i })}>
              <LineNo>{i + 1}</LineNo>
              {line.map((token, key) => (
                <span {...getTokenProps({ token, key })} />
              ))}
            </div>
          ))}
        </Pre>
      )}
    </Highlight>
  );
};

export default Code;
```

%[https://youtu.be/j-EINXVe2WA]

## React live

Avec React Live, vous devez ajouter deux extraits à votre composant `Code.js`.

Vous allez importer les composants :

```js
import {
  LiveEditor,
  LiveError,
  LivePreview,
  LiveProvider,
} from 'react-live';
```

Ensuite, vous allez vérifier si `react-live` a été ajouté à la balise de langue sur votre fichier mdx via les props :

```js
if (props['react-live']) {
  return (
    <LiveProvider code={codeString} noInline={true} theme={theme}>
      <LiveEditor />
      <LiveError />
      <LivePreview />
    </LiveProvider>
  );
}
```

Voici le composant complet :

```js
import Highlight, { defaultProps } from 'prism-react-renderer';
import theme from 'prism-react-renderer/themes/nightOwl';
import React from 'react';
import {
  LiveEditor,
  LiveError,
  LivePreview,
  LiveProvider,
} from 'react-live';
import styled from 'styled-components';
import { copyToClipboard } from '../../utils/copy-to-clipboard';

const Pre = styled.pre`
  position: relative;
  text-align: left;
  margin: 1em 0;
  padding: 0.5em;
  overflow-x: auto;
  border-radius: 3px;

  & .token-lline {
    line-height: 1.3em;
    height: 1.3em;
  }
  font-family: 'Courier New', Courier, monospace;
`;

const LineNo = styled.span`
  display: inline-block;
  width: 2em;
  user-select: none;
  opacity: 0.3;
`;

const CopyCode = styled.button`
  position: absolute;
  right: 0.25rem;
  border: 0;
  border-radius: 3px;
  margin: 0.25em;
  opacity: 0.3;
  &:hover {
    opacity: 1;
  }
`;

export const Code = ({ codeString, language, ...props }) => {
  if (props['react-live']) {
    return (
      <LiveProvider code={codeString} noInline={true} theme={theme}>
        <LiveEditor />
        <LiveError />
        <LivePreview />
      </LiveProvider>
    );
  }

  const handleClick = () => {
    copyToClipboard(codeString);
  };

  return (
    <Highlight
      {...defaultProps}
      code={codeString}
      language={language}
      theme={theme}>
      {({
        className,
        style,
        tokens,
        getLineProps,
        getTokenProps,
      }) => (
        <Pre className={className} style={style}>
          <CopyCode onClick={handleClick}>Copy</CopyCode>
          {tokens.map((line, i) => (
            <div {...getLineProps({ line, key: i })}>
              <LineNo>{i + 1}</LineNo>
              {line.map((token, key) => (
                <span {...getTokenProps({ token, key })} />
              ))}
            </div>
          ))}
        </Pre>
      )}
    </Highlight>
  );
};
```

Pour tester cela, ajoutez `react-live` à côté de la langue sur votre composant `Dump`, donc vous avez ajouté à l'article de blog que vous avez fait :

```markdown
```jsx react-live
```

Maintenant, vous pouvez éditer le code directement. Essayez de changer quelques choses comme ceci :

```js
const Dump = props => (
  <div
    style={{
      fontSize: 20,
      border: '1px solid #efefef',
      padding: 10,
      background: 'white',
    }}>
    {Object.entries(props).map(([key, val]) => (
      <pre key={key}>
        <strong style={{ color: 'white', background: 'red' }}>
          {key} ?
        </strong>
        {JSON.stringify(val, '', ' ')}
      </pre>
    ))}
  </div>
);

render(<Dump props={['One', 'Two', 'Three', 'Four']} />);
```

%[https://youtu.be/AlOdd-TvqHE]

## Image de couverture

Maintenant, pour ajouter une image de couverture à chaque article, vous devrez installer quelques packages pour gérer les images dans Gatsby.

installer :

```bash
yarn add gatsby-transformer-sharp gatsby-plugin-sharp gatsby-remark-images gatsby-image
```

Maintenant, vous devriez configurer `gatsby-config.js` pour inclure les packages nouvellement ajoutés. N'oubliez pas d'ajouter `gatsby-remark-images` à `gatsby-plugin-mdx` à la fois comme option `gatsbyRemarkPlugins` et comme option `plugins`.

config :

```js
module.exports = {
  siteMetadata: siteMetadata,
  plugins: [
    `gatsby-plugin-styled-components`,
    `gatsby-transformer-sharp`,
    `gatsby-plugin-sharp`,
    {
      resolve: `gatsby-plugin-mdx`,
      options: {
        extensions: [`.mdx`, `.md`],
        gatsbyRemarkPlugins: [
          {
            resolve: `gatsby-remark-images`,
            options: {
              maxWidth: 590,
            },
          },
        ],
        plugins: [
          {
            resolve: `gatsby-remark-images`,
            options: {
              maxWidth: 590,
            },
          },
        ],
      },
    },
    {
      resolve: `gatsby-source-filesystem`,
      options: { path: `${__dirname}/posts`, name: `posts` },
    },
  ],
};
```

Ajoutez l'image à la requête d'index dans `src/pages.index.js` :

```graphql
cover {
  publicURL
  childImageSharp {
    sizes(
      maxWidth: 2000
      traceSVG: { color: "#639" }
    ) {
      ...GatsbyImageSharpSizes_tracedSVG
    }
  }
}
```

Corrigez également la date dans la requête :

```graphql
date(formatString: "YYYY MMMM Do")
```

Cela affichera la date comme année complète, mois complet et le jour comme 'st', 'nd', 'rd' et 'th'. Donc si la date d'aujourd'hui était 1970/01/01, elle se lirait 1970 January 1st.

Ajoutez `gatsby-image` utilisez cela dans un composant stylisé :

```js
const Image = styled(Img)`
  border-radius: 5px;
`;
```

Ajoutez un peu de JavaScript pour déterminer s'il y a quelque chose à rendre :

```
{
  !!frontmatter.cover ? (
    <Image sizes={frontmatter.cover.childImageSharp.sizes} />
  ) : null;
}
```

Voici à quoi devrait ressembler le module complet maintenant :

```js
import { Link } from 'gatsby';
import Img from 'gatsby-image';
import React from 'react';
import styled from 'styled-components';
import { Layout } from '../components/Layout';

const IndexWrapper = styled.main``;

const PostWrapper = styled.div``;

const Image = styled(Img)`
  border-radius: 5px;
`;

export default ({ data }) => {
  return (
    <Layout>
      <IndexWrapper>
        {/* <Dump data={data}></Dump> */}
        {data.allMdx.nodes.map(
          ({ id, excerpt, frontmatter, fields }) => (
            <PostWrapper key={id}>
              <Link to={fields.slug}>
                {!!frontmatter.cover ? (
                  <Image
                    sizes={frontmatter.cover.childImageSharp.sizes}
                  />
                ) : null}
                <h1>{frontmatter.title}</h1>
                <p>{frontmatter.date}</p>
                <p>{excerpt}</p>
              </Link>
            </PostWrapper>
          )
        )}
      </IndexWrapper>
    </Layout>
  );
};

export const query = graphql`
  query SITE_INDEX_QUERY {
    allMdx(
      sort: { fields: [frontmatter___date], order: DESC }
      filter: { frontmatter: { published: { eq: true } } }
    ) {
      nodes {
        id
        excerpt(pruneLength: 250)
        frontmatter {
          title
          date(formatString: "YYYY MMMM Do")
          cover {
            publicURL
            childImageSharp {
              sizes(maxWidth: 2000, traceSVG: { color: "#639" }) {
                ...GatsbyImageSharpSizes_tracedSVG
              }
            }
          }
        }
        fields {
          slug
        }
      }
    }
  }
`;
```

%[https://youtu.be/9S5GNtql02w]

**Ressources supplémentaires :**

* cela m'a aidé pour mon propre blog : [https://juliangaramendy.dev/custom-open-graph-images-in-gatsby-blog/](https://juliangaramendy.dev/custom-open-graph-images-in-gatsby-blog/)
* et la documentation de Gatsby : [https://www.gatsbyjs.org/docs/working-with-images/](https://www.gatsbyjs.org/docs/working-with-images/)

## Création d'un composant SEO avec React Helmet

Il y a une PR GitHub de Gatsby sur le SEO avec [d'excellentes notes d'Andrew Welch](https://github.com/gatsbyjs/gatsby/pull/10780#issuecomment-451048608) sur le SEO et un lien vers une présentation qu'il a faite en 2017.

**Crafting Modern SEO avec Andrew Welch :**

%[https://www.youtube.com/watch?v=I9qQslUJknw]

**Crafting Modern SEO avec Andrew Welch :**

%[https://vimeo.com/246846978]

Dans les commentaires suivants de cette PR, [LekoArts](https://github.com/LekoArts) de Gatsby détaille [sa propre implémentation](https://github.com/LekoArts/gatsby-starter-prismic/blob/master/src/components/SEO/SEO.jsx) que j'ai implémentée [en tant que composant React](https://github.com/spences10/react-seo-component). Vous allez le configurer maintenant dans ce guide.

Tout d'abord, installez et configurez `gatsby-plugin-react-helmet`. Cela est utilisé pour le rendu côté serveur des données ajoutées avec React Helmet.

```bash
yarn add gatsby-plugin-react-helmet
```

Vous devrez ajouter le plugin à votre `gatsby-config.js`. Si vous ne l'avez pas encore fait, maintenant est un bon moment pour configurer également `gatsby-plugin-styled-components`.

### Configurer le composant SEO pour la page d'accueil

Pour visualiser les données que vous allez obtenir dans le composant SEO, utilisez le composant `Dump` pour commencer à valider les données.

La majorité des informations nécessaires pour `src/pages/index.js` peuvent d'abord être ajoutées à l'objet `siteMetadata` de `gatsby-config.js`, puis interrogées avec le hook `useSiteMetadata`. Certaines des données ajoutées ici peuvent ensuite être utilisées dans `src/templates/blogPostTemplate.js` - plus d'informations à ce sujet dans la section suivante.

Pour l'instant, ajoutez ce qui suit :

```js
const siteMetadata = {
  title: `The Localhost Blog`,
  description: `This is my coding blog where I write about my coding journey.`,
  image: `/default-site-image.jpg`,
  siteUrl: `https://thelocalhost.blog`,
  siteLanguage: `en-GB`,
  siteLocale: `en_gb`,
  twitterUsername: `@spences10`,
  authorName: `Scott Spence`,
}

module.exports = {
  siteMetadata: siteMetadata,
  plugins: [
    ...
```

Vous n'êtes pas obligé d'abstraire le `siteMetadata` dans son propre composant ici. Ce n'est qu'une suggestion sur la façon de le gérer.

L'`image` sera l'image par défaut de votre site. Vous devriez créer un dossier `static` à la racine du projet et y ajouter une image que vous souhaitez voir lorsque la page d'accueil de votre site est partagée sur les réseaux sociaux.

Pour `siteUrl`, à ce stade, il n'est pas nécessairement valide. Vous pouvez ajouter une URL factice pour l'instant et la changer plus tard.

Le `siteLanguage` est votre langue de choix pour le site. Consultez les [balises de langue w3](https://www.w3.org/International/articles/language-tags/) pour plus d'informations.

Facebook OpenGraph est le seul endroit où `siteLocale` est utilisé et il est différent des balises de langue.

Ajoutez votre `twitterUsername` et votre `authorName`.

Mettez à jour le hook `useSiteMetadata` maintenant pour refléter les nouvelles propriétés ajoutées :

```js
import { graphql, useStaticQuery } from 'gatsby';

export const useSiteMetadata = () => {
  const { site } = useStaticQuery(
    graphql`
      query SITE_METADATA_QUERY {
        site {
          siteMetadata {
            description
            title
            image
            siteUrl
            siteLanguage
            siteLocale
            twitterUsername
            authorName
          }
        }
      }
    `
  );
  return site.siteMetadata;
};
```

Commencez par importer le composant `Dump` dans `src/pages/index.js`, puis branchez les props comme elles sont détaillées dans la documentation du [`react-seo-component`](https://github.com/spences10/react-seo-component).

```js
import Dump from '../components/Dump'
import { useSiteMetadata } from '../hooks/useSiteMetadata'

export default ({ data }) => {
  const {
    description,
    title,
    image,
    siteUrl,
    siteLanguage,
    siteLocale,
    twitterUsername,
  } = useSiteMetadata()
  return (
    <Layout>
      <Dump
        title={title}
        description={description}
        image={`${siteUrl}${image}`}
        pathname={siteUrl}
        siteLanguage={siteLanguage}
        siteLocale={siteLocale}
        twitterUsername={twitterUsername}
      />
      <IndexWrapper>
        {data.allMdx.nodes.map(
          ...
```

Vérifiez que toutes les props affichent des valeurs valides. Ensuite, vous pouvez remplacer le composant `Dump` par le composant `SEO`.

Le `src/pages/index.js` complet devrait maintenant ressembler à ceci :

```js
import { graphql, Link } from 'gatsby';
import Img from 'gatsby-image';
import React from 'react';
import SEO from 'react-seo-component';
import styled from 'styled-components';
import { Layout } from '../components/Layout';
import { useSiteMetadata } from '../hooks/useSiteMetadata';

const IndexWrapper = styled.main``;

const PostWrapper = styled.div``;

const Image = styled(Img)`
  border-radius: 5px;
`;

export default ({ data }) => {
  const {
    description,
    title,
    image,
    siteUrl,
    siteLanguage,
    siteLocale,
    twitterUsername,
  } = useSiteMetadata();
  return (
    <Layout>
      <SEO
        title={title}
        description={description || `nothin`}
        image={`${siteUrl}${image}`}
        pathname={siteUrl}
        siteLanguage={siteLanguage}
        siteLocale={siteLocale}
        twitterUsername={twitterUsername}
      />
      <IndexWrapper>
        {/* <Dump data={data}></Dump> */}
        {data.allMdx.nodes.map(
          ({ id, excerpt, frontmatter, fields }) => (
            <PostWrapper key={id}>
              <Link to={fields.slug}>
                {!!frontmatter.cover ? (
                  <Image
                    sizes={frontmatter.cover.childImageSharp.sizes}
                  />
                ) : null}
                <h1>{frontmatter.title}</h1>
                <p>{frontmatter.date}</p>
                <p>{excerpt}</p>
              </Link>
            </PostWrapper>
          )
        )}
      </IndexWrapper>
    </Layout>
  );
};

export const query = graphql`
  query SITE_INDEX_QUERY {
    allMdx(
      sort: { fields: [frontmatter___date], order: DESC }
      filter: { frontmatter: { published: { eq: true } } }
    ) {
      nodes {
        id
        excerpt(pruneLength: 250)
        frontmatter {
          title
          date(formatString: "YYYY MMMM Do")
          cover {
            publicURL
            childImageSharp {
              sizes(maxWidth: 2000, traceSVG: { color: "#639" }) {
                ...GatsbyImageSharpSizes_tracedSVG
              }
            }
          }
        }
        fields {
          slug
        }
      }
    }
  }
`;
```

%[https://www.youtube.com/watch?v=O0jk9AqM_ls]

### Configurer le composant SEO pour les articles de blog

Cela sera la même approche que pour la page d'accueil. Importez le composant `Dump` et validez les props avant de remplacer le composant `Dump` par le composant `SEO`.

```js
import Dump from '../components/Dump'
import { useSiteMetadata } from '../hooks/useSiteMetadata'

export default ({ data, pageContext }) => {
  const {
    image,
    siteUrl,
    siteLanguage,
    siteLocale,
    twitterUsername,
    authorName,
  } = useSiteMetadata()
  const { frontmatter, body, fields, excerpt } = data.mdx
  const { title, date, cover } = frontmatter
  const { previous, next } = pageContext
  return (
    <Layout>
      <Dump
        title={title}
        description={excerpt}
        image={
          cover === null
            ? `${siteUrl}${image}`
            : `${siteUrl}${cover.publicURL}`
        }
        pathname={`${siteUrl}${fields.slug}`}
        siteLanguage={siteLanguage}
        siteLocale={siteLocale}
        twitterUsername={twitterUsername}
        author={authorName}
        article={true}
        publishedDate={date}
        modifiedDate={new Date(Date.now()).toISOString()}
      />
      <h1>{frontmatter.title}</h1>
      ...
```

Ajoutez `fields.slug`, `excerpt` et `cover.publicURL` à la requête `PostsBySlug` et déstructurez-les depuis `data.mdx` et `frontmatter`, respectivement.

Pour l'image, vous devrez faire un peu de logique pour savoir si la `cover` existe et par défaut utiliser l'image du site par défaut si ce n'est pas le cas.

Le `src/templates/blogPostTemplate.js` complet devrait maintenant ressembler à ceci :

```js
import { graphql, Link } from 'gatsby';
import { MDXRenderer } from 'gatsby-plugin-mdx';
import React from 'react';
import SEO from 'react-seo-component';
import { Layout } from '../components/Layout';
import { useSiteMetadata } from '../hooks/useSiteMetadata';

export default ({ data, pageContext }) => {
  const {
    image,
    siteUrl,
    siteLanguage,
    siteLocale,
    twitterUsername,
    authorName,
  } = useSiteMetadata();
  const { frontmatter, body, fields, excerpt } = data.mdx;
  const { title, date, cover } = frontmatter;
  const { previous, next } = pageContext;
  return (
    <Layout>
      <SEO
        title={title}
        description={excerpt}
        image={
          cover === null
            ? `${siteUrl}${image}`
            : `${siteUrl}${cover.publicURL}`
        }
        pathname={`${siteUrl}${fields.slug}`}
        siteLanguage={siteLanguage}
        siteLocale={siteLocale}
        twitterUsername={twitterUsername}
        author={authorName}
        article={true}
        publishedDate={date}
        modifiedDate={new Date(Date.now()).toISOString()}
      />
      <h1>{frontmatter.title}</h1>
      <p>{frontmatter.date}</p>
      <MDXRenderer>{body}</MDXRenderer>
      {previous === false ? null : (
        <>
          {previous && (
            <Link to={previous.fields.slug}>
              <p>{previous.frontmatter.title}</p>
            </Link>
          )}
        </>
      )}
      {next === false ? null : (
        <>
          {next && (
            <Link to={next.fields.slug}>
              <p>{next.frontmatter.title}</p>
            </Link>
          )}
        </>
      )}
    </Layout>
  );
};

export const query = graphql`
  query PostBySlug($slug: String!) {
    mdx(fields: { slug: { eq: $slug } }) {
      frontmatter {
        title
        date(formatString: "YYYY MMMM Do")
        cover {
          publicURL
        }
      }
      body
      excerpt
      fields {
        slug
      }
    }
  }
`;
```

%[https://www.youtube.com/watch?v=a2fcgYIQRIU]

### Construire le site et valider les balises méta

Ajoutez le script de construction à `package.json` ainsi qu'un script pour servir le site construit localement.

```json
"scripts": {
  "dev": "gatsby develop -p 9988 -o",
  "build": "gatsby build",
  "serve": "gatsby serve -p 9500 -o"
},
```

Maintenant, il est temps d'exécuter :

```bash
yarn build && yarn serve
```

Cela construira le site et ouvrira un onglet de navigateur pour que vous puissiez voir le site tel qu'il apparaîtra lorsqu'il sera sur Internet. Validez que les balises méta ont été ajoutées à la construction en sélectionnant "Afficher la source de la page" (Crtl+u sous Windows et Linux) sur la page. Vous pouvez faire un Ctrl+f pour les trouver.

%[https://www.youtube.com/watch?v=c6bB9ddAgjc]

## Ajout du projet à GitHub

Ajoutez votre code à GitHub en sélectionnant l'icône plus (+) à côté de votre avatar sur GitHub ou en allant directement sur [https://github.com/new](https://github.com/new)

Nommez votre dépôt et cliquez sur créer un dépôt. Ensuite, vous recevrez les instructions pour lier votre code local au dépôt que vous avez créé via la ligne de commande.

La manière dont vous vous authentifiez avec GitHub dépendra de l'apparence de la commande.

Quelques bonnes ressources pour s'authentifier avec GitHub via SSH sont la vidéo Egghead.io de [Kent Dodds](https://egghead.io/lessons/javascript/how-to-authenticate-with-github-using-ssh) et aussi un guide [sur CheatSheets.xyz](https://www.cheatsheets.xyz/git/#how-to-authenticate-with-github-using-ssh).

%[https://www.youtube.com/watch?v=r2eiJ8E_YT0]

## Déploiement sur Netlify

Pour déployer votre site sur Netlify, si vous ne l'avez pas déjà fait, vous devrez ajouter l'intégration GitHub à votre profil GitHub. Si vous allez sur [app.netlify.com](https://egghead.io/lessons/javascript/how-to-authenticate-with-github-using-ssh), l'assistant vous guidera tout au long du processus.

À partir de là, vous pouvez ajouter le dossier `public` de votre site construit en le glissant et en le déposant directement sur les CDN mondiaux de Netlify.

Vous, cependant, allez charger votre site via le CLI de Netlify ! Dans votre terminal, si vous n'avez pas encore installé le CLI, exécutez :

```bash
yarn global add netlify-cli
```

Ensuite, une fois le CLI installé :

```bash
# authentifiez-vous via le CLI
netlify login
# initialisez le site
netlify init
```

Entrez les détails pour votre équipe : le nom du site est facultatif, la commande de construction sera `yarn build`, et le répertoire à déployer est `public`.

Vous serez invité à commiter les changements et à les pousser vers GitHub (avec `git push`). Une fois que vous aurez fait cela, votre site sera publié et prêt à être vu par tous !

%[https://www.youtube.com/watch?v=voWeHvIGB0g]

## Valider les métadonnées avec Heymeta

Enfin, il s'agit de valider les métadonnées pour les champs OpenGraph. Pour cela, vous devrez vous assurer que le `siteUrl` reflète ce que vous avez dans votre tableau de bord Netlify.

Si vous avez dû changer l'URL, vous devrez commiter et pousser les changements vers GitHub à nouveau.

Une fois que votre site est construit avec une URL valide, vous pouvez alors tester la page d'accueil et une page de blog pour les balises méta correctes avec [heymeta.com](http://heymeta.com/).

%[https://www.youtube.com/watch?v=JH1AVanYhwo]

**Outils de vérification OpenGraph :**

* [https://www.heymeta.com/](https://www.heymeta.com/)
* [https://opengraphcheck.com/](https://opengraphcheck.com/)
* [https://cards-dev.twitter.com/validator](https://cards-dev.twitter.com/validator)
* [https://developers.facebook.com/tools/debug/sharing](https://developers.facebook.com/tools/debug/sharing)
* [https://www.linkedin.com/post-inspector/](https://www.linkedin.com/post-inspector/)

**Ressources supplémentaires :**

* [Les balises méta essentielles pour les réseaux sociaux](https://css-tricks.com/essential-meta-tags-social-media/)

**Le code exemple pour ce blog peut être trouvé [ici](https://codesandbox.io/s/the-localhost-blog-3bn45) :**

%[https://codesandbox.io/s/the-localhost-blog-3bn45]

**Ou [ici](https://github.com/spences10/the-localhost-blog/tree/blog-post-code).**

## Merci d'avoir lu ?

C'est tout pour aujourd'hui ! Si j'ai oublié quelque chose ou s'il y a une meilleure façon de faire quelque chose, faites-le moi savoir.

Suivez-moi sur [Twitter](https://twitter.com/spences10) ou [Ask Me Anything](https://github.com/spences10/ama) sur GitHub.

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon jardin numérique](https://scottspence.com/garden).**