---
title: Comment sourcer du contenu avec Gatsby.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T18:22:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-source-content-with-gatsby-js-c220dde97e7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MWjcgB371nkD9_yAPY3qDQ.png
tags:
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment sourcer du contenu avec Gatsby.js
seo_desc: 'By Dimitri Ivashchuk

  Gatsby.js is a powerful static site generator (with dynamic capabilities) which
  can be used to build super performant web-sites. It has a very rich plug-in functionality
  and is perfect for your next personal blog, product landing...'
---

Par Dimitri Ivashchuk

Gatsby.js est un générateur de site statique puissant (avec des capacités dynamiques) qui peut être utilisé pour construire des sites web ultra-performants. Il dispose d'une fonctionnalité de plug-in très riche et est parfait pour votre prochain _blog personnel_, _page de destination de produit_, _page de portfolio_ ou _petite application e-commerce_.

### Sourcing de contenu

Il est assez évident que lorsque vous construisez votre site web, outre la logique métier, la performance, la sécurité et les styles, vous vous souciez du contenu réel présenté à l'utilisateur final.

Le cas peut être assez simple : disons que vous avez une page produit avec des sections qui doivent être éditées par l'équipe marketing qui ne veut pas éditer ces _h1_ et _p_ fantaisistes dans l'éditeur de code.

Un autre scénario peut être une page de blog personnel qui contient de nombreux articles, chaque article ayant son propre titre, contenu et tonnes d'autres informations que vous pourriez vouloir afficher.

Grâce à de nombreux plugins écrits par la communauté et les mainteneurs de Gatsby, nous avons la chance de choisir parmi une large gamme d'options pour obtenir notre contenu sur la page.

### Sourcing depuis le dossier du projet avec `gatsby-source-filesystem` et `gatsby-markdown-remark`

L'une des façons les plus simples de récupérer notre contenu est de le sourcer directement depuis notre dossier de projet. Nous pouvons récupérer des actifs comme des images, et des types de contenu plus complexes comme des articles de blog écrits en markdown.

> Scénario 1 : Accéder aux images du dossier assets pour les afficher sur la page

Tout d'abord, nous devons installer `gatsby-source-filesystem` et le configurer dans `gatsby-config.js`.

`npm install gatsby-source-filesystem`

Dans `gatsby-config.js` :

```javascript
module.exports = {
  plugins: [
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `assets`,
        path: `${__dirname}/src/assets/`,
      },
    },
  ],
}
```

Avec les lignes ci-dessus, nous disons à Gatsby que nous voulons permettre à GraphQL d'interroger tout le contenu du dossier `assets` de notre projet situé au chemin spécifié `path`.

Maintenant que le plugin est prêt, nous pouvons effectivement interroger notre dossier assets avec la requête GraphQL suivante (`sourceInstanceName` est un paramètre de filtre qui correspond au `name` dans la configuration ci-dessus) :

```graphql
query {
  allFile(filter: { sourceInstanceName: { eq: "assets" } }) {
    edges {
      node {
        id
        childImageSharp {
          fluid {
            ...GatsbyImageSharpFluid
          }
        }
      }
    }
  }
}
```

Notez que pour pouvoir utiliser les images retournées par cette requête à l'intérieur d'un `component` plutôt qu'à l'intérieur d'une `page`, nous devons utiliser `StaticQuery` disponible depuis `Gatsby`.

`StaticQuery` accepte la propriété `query` où nous pouvons utiliser notre requête GraphQL ci-dessus et la propriété `render` qui rend ce que nous lui fournissons et qui a accès à `data` qui n'est rien de plus qu'un wrapper pour nos fichiers interrogés.

Si vous interrogez les mêmes images mais que vous voulez les utiliser à l'intérieur de l'une de vos `pages`, vous pouvez y accéder directement depuis `props.data`

> Scénario 2 : Accéder à une image particulière pour l'afficher sur la page

Pour accéder à une image particulière par son nom, nous devons adapter un peu notre requête GraphQL. Sinon, nous pouvons l'utiliser de la manière décrite ci-dessus dans le premier scénario en utilisant `StaticQuery` dans le composant et `props.data` dans la page.

Spécifions le chemin absolu vers le fichier et utilisons une regex pour sélectionner l'image souhaitée.

```graphql
query {
  file(absolutePath: { regex: "/assets/your-image-name.png/" }) {
    childImageSharp {
      fluid {
        ...GatsbyImageSharpFluid
      }
    }
  }
}
```

> Scénario 3 : Accéder à un article de blog écrit en markdown avec son frontmatter

Comme Gatsby est souvent utilisé comme modèle de blog, il offre un moyen très pratique de travailler avec des articles de blog écrits en `markdown`. Pour accéder aux articles en markdown, nous devons d'abord modifier un peu notre configuration afin que Gatsby sache où se trouvent nos fichiers `markdown`.

Nous utilisons `gatsby-source-filesystem` pour y parvenir :

```javascript
module.exports = {
  plugins: [
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `markdown`,
        path: `${__dirname}/src/blog/`,
      },
    },
  ],
}
```

Pour pouvoir travailler avec les fichiers `markdown` de manière vraiment pratique, nous devons également configurer le plugin `gatsby-transformer-remark`. Notez comment nous ajoutons d'autres plugins à l'intérieur de `gatsby-transformer-remark` comme `gatsby-remark-images` ou `gatsby-remark-prismjs`. Ceux-ci sont là pour que nous puissions directement intégrer des images dans notre `markdown` et mettre en évidence des morceaux de code avec `prismjs`, respectivement.

```javascript
module.exports = {
  plugins: [
    {
      resolve: `gatsby-transformer-remark`,
      options: {
        plugins: [
          `gatsby-remark-images`,
          `gatsby-remark-prismjs`,
        ],
      },
    },
  ],
}
```

Avec tout ce qui est configuré ci-dessus, nous pouvons maintenant interroger nos articles en markdown avec `query` (nous pouvons utiliser `sort` pour obtenir nos articles de blog dans l'ordre chronologique et filtrer pour être sûr que nous interrogeons uniquement les markdowns qui sont situés dans le dossier `blog` de notre projet) :

```graphql
query {
  allMarkdownRemark(
    sort: { fields: [frontmatter___date], order: DESC }
    filter: { fileAbsolutePath: { regex: "/blog/" } }
  ) {
    edges {
      node {
        frontmatter {
          title
          date
        }
        html
      }
    }
  }
}
```

Nous savons déjà que nous pouvons maintenant accéder à nos articles de blog `markdown` dans n'importe quelle `page` simplement via `this.props.data.allMarkdownRemark.edges`, les mapper et afficher toutes les données nécessaires générées pour nous par le plugin.

Par exemple, nous avons accès à `frontmatter` qui n'est rien de plus qu'une structure de type JSON que nous incluons dans notre `markdown`.

Voici un exemple rapide :

```markdown
---
title: "Mon premier article de blog"
date: "2019-05-04"
---

# Mon premier article de blog

Ceci est mon premier article de blog.
```

Nous avons inclus le titre et la date, mais vous pouvez ajouter librement tout autre paramètre que vous voulez rendre accessible depuis la requête (comme des tags sous forme de tableau) :

```markdown
---
title: "Mon premier article de blog"
date: "2019-05-04"
tags: ["gatsby", "blog", "tutoriel"]
---

# Mon premier article de blog

Ceci est mon premier article de blog.
```

### CMS Headless

Parfois, il n'est pas vraiment pratique de changer tous les types de contenu comme les images ou les articles de blog dans l'éditeur de code. De plus, votre utilisateur final peut ne pas savoir comment naviguer dans le code et peut nécessiter une solution plus directe.

> Scénario 4 : Accéder à un modèle de contenu complexe depuis un CMS et afficher le contenu sur la page

C'est là qu'intervient le CMS headless. Imaginez un scénario où vous créez une page produit statique avec Gatsby et la passez au département marketing qui est responsable de la rédaction et des images sur la page. Vous l'avez construit avec du code — ils interagissent avec une interface utilisateur conviviale qui facilite la modification de tout contenu. Génial !

Explorons comment nous pourrions le faire avec Gatsby.js !

#### Sourcing depuis Contentful

Pour pouvoir sourcer quelque chose depuis Contentful, vous aurez besoin d'un compte sur [https://www.contentful.com/](https://www.contentful.com/). Après l'inscription, vous obtiendrez un exemple de projet simple que nous utiliserons à des fins d'apprentissage.

Pour l'instant, commençons par installer `gatsby-source-contentful` et l'ajouter à notre configuration.

`npm install --save gatsby-source-contentful`

Dans `gatsby-config.js`, nous devons ajouter le plugin et fournir notre `spaceId` et `accessToken` qui peuvent tous deux être trouvés dans les paramètres -> clés API de notre tableau de bord de projet :

![Image](https://cdn-media-1.freecodecamp.org/images/1*xyys4cd2XaBOSKjLUWXjAA.png)
_Tableau de bord Contentful_

Notez qu'il n'est pas judicieux d'exposer votre `accessToken` directement dans le fichier de configuration afin qu'il soit visible par tous sur GitHub. À des fins de formation, je l'inclurai dans le code pour ce tutoriel, mais essayez d'utiliser des variables d'environnement pour protéger vos clés comme cela peut être vu dans l'exemple ci-dessus. Si c'est la première fois que vous voyez le terme `variable d'environnement`, ne vous inquiétez pas, vous pouvez comprendre le concept à partir de [cet article](https://dev.to/deammer/loading-environment-variables-in-js-apps-1p7p).

Avant d'aller plus loin, je veux vous montrer comment nous pouvons résoudre un petit conflit venant du fait que certains fichiers Contentful sont traités comme `markdown` par Gatsby.

Notre `gatsby-node.js` est responsable de la création programmatique de pages à partir de nos articles de blog en markdown qui sont situés dans le dossier blog. Par défaut, il utilise la requête `allMarkdownRemark`, qui sourcerait également le markdown de Contentful dont nous n'avons pas besoin. Adaptons notre requête pour sourcer uniquement les fichiers qui sont situés dans notre dossier de projet :

Dans `gatsby-node.js`, nous avons ajouté `filter` et l'avons défini sur `/blog/` :

```javascript
exports.createPages = async ({ graphql, actions }) => {
  const { createPage } = actions
  const result = await graphql(`
    query {
      allMarkdownRemark(
        filter: { fileAbsolutePath: { regex: "/blog/" } }
      ) {
        edges {
          node {
            frontmatter {
              path
            }
          }
        }
      }
    }
  `)
  // ... reste du code
}
```

Maintenant, nous sommes prêts à sourcer notre contenu depuis Contentful. Dans une nouvelle page nommée `contentful.js`, nous voulons d'abord interroger nos actifs que Contentful a créés pour nous. À l'heure actuelle, nous avons un type de contenu particulièrement intéressant appelé `Course` qui contient tous les éléments nécessaires pour nous entraîner.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AbIn1ZFV9jIdIoJlcMWXvQ.png)
_Type de contenu — Course_

Il est simple d'interroger les actifs de Contentful avec GraphQL, et tout ce que nous devons faire pour obtenir toutes les entrées qui sont de type `Course` est d'exécuter la requête `allContentfulCourse`.

Vous avez peut-être déjà deviné que nous pouvons interroger `yourCustomType` de contenu avec `allContentfulYourCustomType`. Notez comment nous filtrons nos cours sur une base linguistique, sinon nous obtiendrions des doublons de chaque cours dans chaque langue spécifiée dans Contentful. Cela est assez spécifique à ce cas, car chaque cours a une traduction :

```graphql
query {
  allContentfulCourse(filter: { node_locale: { eq: "en-US" } }) {
    edges {
      node {
        title
        duration
        shortDescription
        image {
          fluid {
            ...GatsbyContentfulFluid
          }
        }
      }
    }
  }
}
```

En explorant notre contenu sur Contentful, nous pouvons voir que chaque Course a un titre, une durée, une description courte et une image. Nous avons inclus ceux-ci dans notre requête et pouvons maintenant y accéder dans notre composant via `this.props.data`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YqwONdTKDFPfpTqFf6KlmA.png)
_Modèle de contenu de Course_

### Récapitulatif

Dans ce petit tutoriel, vous avez appris plusieurs façons de sourcer différents types de contenu dans _Gatsby_. Vous avez également appris comment les combiner dans un seul projet, en évitant les conflits de sourcing possibles en spécifiant précisément ce que nous voulons interroger depuis quelle source.

Merci d'avoir lu ! J'espère que vous avez apprécié la lecture de cet article autant que j'ai apprécié l'écrire ! Si vous avez des questions ou souhaitez engager une discussion, n'hésitez pas à me contacter sur [twitter](https://twitter.com/DivDev_). Je serais heureux si vous cliquiez sur ce bouton `follow` pour ne pas manquer les futurs articles que je publierai ?

Comme toujours, vous pouvez trouver le code de ce tutoriel [ici sur github](https://github.com/d-ivashchuk/blog-gatsby-sourcing)

_Publié à l'origine sur [divdev.io](http://divdev.io)_