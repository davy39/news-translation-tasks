---
title: Comment créer un blog alimenté par React et Gatsby en environ 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-28T15:35:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-react-and-gatsby-powered-blog-in-about-10-minutes-625c35c06481
coverImage: https://cdn-media-1.freecodecamp.org/images/1*P54PpELlIRgiGNSgLDBwNQ.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer un blog alimenté par React et Gatsby en environ 10 minutes
seo_desc: 'By Emmanuel Yusufu


  Disclaimer: This was written for Gatsby Version 1, version 2 was just released and
  has some changes made. I’ll work on another tutorial for that.


  Gatsby is a blazing fast static site generator based on ReactJS.

  A static site gene...'
---

Par Emmanuel Yusufu

> Avertissement : Ceci a été écrit pour Gatsby Version 1, la version 2 vient d'être publiée et comporte quelques changements. Je travaillerai sur un autre tutoriel pour cela.

**Gatsby** est un générateur de site statique ultra-rapide basé sur ReactJS.

Un **générateur de site statique** (SSG) est un compromis entre un site **statique** codé en dur en HTML et un CMS complet (Système de Gestion de Contenu), comme Wordpress.

Un SSG peut être utilisé pour générer des pages HTML pour des sites web axés sur le contenu (comme les blogs). Tout ce dont il a besoin, ce sont des données pour le contenu des pages et le modèle à remplir avec le contenu.

Cet article sera divisé en cinq sections :

1. **_Premiers pas._**
2. **_Création de composants de mise en page._**
3. **_Création de billets de blog._**
4. **_Génération de nouvelles pages à partir des données des billets de blog._**
5. **_Créer une liste de nos fichiers markdown du site sur la page d'accueil._**

Nous allons plonger profondément dans Gatsby et certaines de ses fonctionnalités en créant un blog statique imaginaire appelé **_CodeStack._** La maquette est montrée ci-dessous. C'est parti ! ✌️

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q4cYG_J2ZPLBkIH2G_N6xA.png)
_Une page de liste de blog / Un seul billet de blog_

### 1. Premiers pas

#### Prérequis

Tout d'abord, assurez-vous d'avoir Node.js installé sur votre système. Si ce n'est pas le cas, rendez-vous sur [**nodejs.org**](https://nodejs.org/) et installez une version récente pour votre système d'exploitation.

De plus, cet article suppose que vous avez une compréhension de ReactJS.

#### Installer l'interface en ligne de commande

Gatsby dispose d'un outil en ligne de commande qui fournit des commandes utiles telles que :

* `gatsby new` : pour échafauder un nouveau projet Gatsby.
* `gatsby develop` : pour lancer un serveur de développement web avec rechargement à chaud.
* `gatsby build` : pour construire une version du projet prête pour la production.

Pour installer, tapez ce qui suit dans votre terminal et appuyez sur Entrée :

```
npm install --global gatsby-cli
```

Créons un dossier de projet `codestack-blog` et naviguons vers celui-ci dans le terminal.

```
gatsby new codestack-blog && cd $_
```

Si vous exécutez `gatsby develop` dans le dossier du projet, le site échafaudé devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*H7QRzPcg28qxiUb-YvOeNA.gif)

### Ajout de plugins

Gatsby dispose d'un large ensemble de plugins [en croissance](https://www.gatsbyjs.org/docs/plugins/#official-plugins). Ce sont essentiellement des packages Node.js qui interfacent avec les API de Gatsby.

Ils peuvent être installés via NPM (Node Package Manager) dans le terminal, et ont généralement trois catégories : **_fonctionnels_**, **_source_** et **_transformateurs_**.

#### **Plugins fonctionnels**

Ces plugins fournissent des fonctionnalités supplémentaires dans un site Gatsby ou dans son environnement de développement. Pour notre application, nous aurons besoin de :

* `gatsby-plugin-react-helmet` : permet la modification des balises `head`. Remarquez qu'il est déjà installé dans notre projet échafaudé.
* `gatsby-plugin-catch-links` : Intercepte les liens locaux provenant de markdown et d'autres pages non-react, et effectue un pushState côté client pour éviter que le navigateur n'ait à rafraîchir la page.

Installez les plugins, ou simplement le deuxième plugin seulement.

```
npm install gatsby-plugin-react-helmet gatsby-plugin-catch-links
```

À chaque fois que nous ajoutons un nouveau plugin, nous devons mettre à jour le fichier `gatsby-config.js` avec le nouveau plugin afin que Gatsby le reconnaisse et l'utilise. Nous utilisons des **_back-ticks_**.

```
module.exports = {  siteMetadata: {    title: `Gatsby Default Starter`,  },  plugins: [    `gatsby-plugin-react-helmet`,    `gatsby-plugin-catch-links`,  ],}
```

#### Plugins source

Ces plugins "sourcent" des données à partir d'emplacements distants ou locaux dans ce que Gatsby appelle [**nodes**](https://www.gatsbyjs.org/docs/node-interface/). Pour écrire nos posts en Markdown sur notre disque local, nous avons besoin de :

* `gatsby-source-filesystem` : source des données sur les fichiers à partir du système de fichiers de votre ordinateur.

```
npm install gatsby-source-filesystem
```

Mettez à jour le fichier `gatsby-config.js` :

```
module.exports = {  siteMetadata: {    title: `Gatsby Default Starter`,  },  plugins: [    `gatsby-plugin-react-helmet`,    `gatsby-plugin-catch-links`,    {      resolve: `gatsby-source-filesystem`,      options: {        path: `${__dirname}/src/pages`,        name: 'pages',      },    }  ],}
```

Que se passe-t-il ici ? Un objet `options` peut être passé à un plugin pour plus de configuration. Nous passons le `path` du système de fichiers (c'est-à-dire où nos fichiers Markdown seront situés), et ensuite un `name` pour les fichiers source, afin que Gatsby sache où se trouvent nos fichiers source et où appliquer les plugins de transformation.

#### Plugins de transformation

Ces plugins transforment les données brutes des [**nodes**](https://www.gatsbyjs.org/docs/node-interface/) en formats de données utilisables. Par exemple, nous aurons besoin de :

* `gatsby-transformer-remark` : cela transforme les billets de blog écrits en fichiers markdown `.md` sur le disque local en HTML pour le rendu.

```
npm install gatsby-transformer-remark
```

Mettez à jour le fichier `gatsby-config.js` à nouveau.

```
module.exports = {  siteMetadata: {    title: `Gatsby Default Starter`,  },  plugins: [    `gatsby-plugin-react-helmet`,    `gatsby-plugin-catch-links`,    {      resolve: `gatsby-source-filesystem`,      options: {        path: `${__dirname}/src/pages`,        name: 'pages',      },    },    `gatsby-transformer-remark`,  ],}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*mXNH_xEpSXWMZmPfDoqcZg.gif)
_Bien joué ! / Crédit : [Nigel Payne](https://dribbble.com/nigelpayne" rel="noopener" target="_blank" title=")_

### 2. Création de composants de mise en page

Gatsby vous permet de créer facilement des "composants de mise en page". Les composants de mise en page sont des sections de votre site que vous souhaitez partager sur plusieurs pages. Pour le blog que nous construisons, ce sont **l'en-tête** et **les barres latérales**.

À partir du dossier racine, jetez un coup d'œil à `src/layouts`. Vous découvrirez un fichier `index.js` où nous définissons les composants de mise en page. `index.css` est déjà fourni avec des styles.

Après avoir exploré le fichier `index.js`, vous verrez que deux composants ont déjà été créés : `Header` et `TemplateWrapper`. Dans `TemplateWrapper`, nous enveloppons le contenu de notre site avec des composants de mise en page que nous voulons voir présents sur plusieurs pages.

Cela est rendu possible par les props `children()`. Il rendra tous les composants non-mise en page de notre site où il est placé. Remarquez que contrairement aux props children de React, le prop children passé aux composants de mise en page est une fonction et doit être exécuté.

Tout d'abord, créez un nouveau dossier et un fichier CSS à `src/styles/layout-overide.css`. Ajoutez-le à la liste des imports dans le fichier `index.js`. Nous devons **_l'importer après `index.css`_** pour remplacer certaines règles de style existantes.

```
import React from 'react'import PropTypes from 'prop-types'import Link from 'gatsby-link'import Helmet from 'react-helmet'
```

```
import './index.css'import "../styles/layout-overide.css";
```

Ouvrez `layout-overide.css` et collez les règles de style suivantes. Pas besoin de les comprendre.

```
* {    background: #f5f5f5;    color: black;}html {    height: 100%;}
```

```
body {    height: 100%;    border: 5px solid #ffdb3a;}
```

```
h1 {    font-size: 1.5rem;    line-height: 0.5rem;}
```

```
p, div {    font-size: 16px;}
```

Mettez à jour le composant d'en-tête.

```
const Header = () => (  <div    style={{      background: '#f5f5f5',      marginBottom: '3rem',      borderBottom: '2px solid #e6e6e6',    }}  >    <div      style={{        margin: '0 auto',        maxWidth: 980,        padding: '1.45rem 1.0875rem',      }}   >     <h1 style={{margin: 0, textAlign: 'center',fontSize: '18px'}}>        <Link to="/"          style={{            color: 'black',            textDecoration: 'none',          }}        >          CodeStack        </Link>      </h1>    </div>  </div>);
```

Créez également un composant `Sidebar`.

```
const Sidebar = (props) => (
```

```
<div    style={{      border: '2px solid #e6e6e6',      maxWidth: 960,      padding: '0.5rem',      marginBottom: '25px'    }}    >    <strong>{props.title}.</strong> {props.description}</div>
```

```
);
```

Nous voulons que les composants `Sidebar` et `{children()}` se comportent de manière responsive comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mNhoGQ6xZEWX5O3XWmvc0Q.gif)

Comme il n'y a pas de moyen facile de définir des media queries dans React, j'ai trouvé une bibliothèque appelée `[react-media](https://github.com/ReactTraining/react-media)`, **_un composant de media query CSS pour React._** Installez-le.

```
npm install --save react-media
```

Il fournit un composant `<Media>` **qui écoute les correspondances à une media query CSS et rend des éléments en fonction de si la query correspond ou non.**

Ajoutez-le à la liste des imports dans notre fichier.

```
import Media from 'react-media'
```

Organisons tout (composants `Header`, `Sidebar`, et `children()`) comme nous le souhaitons dans `TemplateWrapper`. Apportez les modifications suivantes (désolé pour l'auto-promotion de mon nom) :

```
const TemplateWrapper = ({ children }) => (  <div>    <Helmet      title="Gatsby Default Starter"      meta={[        { name: "description", content: "Sample" },        { name: "keywords", content: "sample, something" }      ]}    />    <Header />    <div      style={{        margin: "0 auto",        maxWidth: 980,        display: "flex",        flexDirection: "row",        justifyContent: "space-between",        height: "100%"      }}    >      <Media query={{ maxWidth: 848 }}>        {matches =>          matches ? (            <div              style={{                margin: "0 auto",                maxWidth: 980,                display: "flex",                flexDirection: "row",                justifyContent: "space-between",                height: "100%",                padding: "25px"              }}            >              <div style={{ flex: 1 }}>{children()}</div>            </div>          ) : (            <div              style={{                margin: "0 auto",                maxWidth: 980,                display: "flex",                flexDirection: "row",                justifyContent: "space-between",                height: "100%",                padding: "25px"              }}            >              <div style={{ flex: 2.5, paddingRight: "30px" }}>                {children()}              </div>
```

```
<div style={{ flex: 1 }}>                <Sidebar                  title="Codestack"                  description="Articles sur React et Node.js. Tous les articles sont écrits par Moi. Développement Web Fullstack."                />                <Sidebar                  title="À propos de l'auteur"                  description="Je suis un Développeur Web Full-stack spécialisé dans React et Node.js basé au Nigeria."                />              </div>            </div>          )        }      </Media>    </div>  </div>);
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*zpeuBlfmSvz-bpJ5Lm86Vg.gif)
_Vous avez compris ! 💪 / Crédit : L[evon ](https://dribbble.com/Uzunyan" rel="noopener" target="_blank" title=")_

Que se passe-t-il dans ce bloc de code monolithique ? React media utilise une **opération ternaire** pour déterminer ce qu'il faut rendre en fonction d'une _largeur maximale de 848px_. Lorsque l'écran correspond à la largeur, seuls les composants `Header` et `children()` sont rendus.

```
<Media query={{ maxWidth: 848 }}>        {matches =>          matches ? (            ...stuff to render...          ) : (            ...stuff to render...          )        }      </Media>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*NaYcfuNoAVZ790Wxu6r9jQ.png)
_Un rappel sur l'opérateur ternaire. Si `condition` est `**vrai**`, l'opérateur retourne la valeur de `**expr1**`; sinon, il retourne la valeur de `**expr2**`._

Si vous avez remarqué, nous avons également utilisé Flexbox pour organiser les positions des composants `children()` et `Sidebar`.

Exécutez `gatsby develop` dans le terminal et notre blog statique devrait maintenant ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CGGelk1wXkOT8MrezuODGw.gif)
_Prenant forme 💪_

### 3. **Création de billets de blog**

Maintenant, passons à la création de véritables billets de blog. Gatsby utilise GraphQL pour récupérer des données à partir d'une ou plusieurs sources telles que votre disque local, l'API Wordpress, etc.

Personnellement, j'aime le fait que je puisse créer un blog statique et récupérer du contenu à partir d'une API WordPress. Mon client a accès à l'éditeur Wordpress où il crée des posts, et j'évite de devoir gérer toutes les difficultés du développement d'un site Wordpress.

Dans cet article, nous chargerons les données à partir de fichiers Markdown que nous créerons sur notre disque local. Le plugin `gatsby-source-filesystem` que nous avons configuré précédemment s'attend à ce que notre contenu se trouve dans `src/pages`, c'est donc exactement là que nous allons le mettre !

Une pratique typique pour les billets de blog est de nommer le dossier quelque chose comme MM-DD-YYYY-titre. Vous pouvez le nommer comme vous le souhaitez ou simplement placer un fichier markdown à l'intérieur du dossier `/pages`.

Créons un dossier `src/pages/12–22–2017-first-post`, et plaçons un `index.md` à l'intérieur. Écrivez :

```
---path: "/hello-world"date: "2017-07-12T17:12:33.962Z"title: "Mon premier billet Gatsby"---
```

```
Oooooh-weeee, mon premier billet de blog !
```

```
Premier post Ipsum est une clé majeure du succès. Félicitations, vous vous êtes joué. Entourez-vous d'anges. Célébrez le succès correctement, la seule façon, la pomme. La clé est de boire de la noix de coco, de la noix de coco fraîche, faites-moi confiance. Blancs d'œufs, saucisse de dinde, toast de blé, eau. Bien sûr, ils ne veulent pas que nous mangions notre petit-déjeuner, alors nous allons profiter de notre petit-déjeuner. 
```

Le bloc entouré de tirets est appelé `frontmatter`. Les données que nous spécifions ici, ainsi que d'autres fichiers Markdown, seront reconnues par le plugin `[**gatsby-transformer-remark**](https://www.gatsbyjs.org/packages/gatsby-transformer-remark/)`.

Le plugin convertira la partie métadonnées du frontmatter de votre fichier markdown en `frontmatter` et la partie contenu (Yippeeee, mon premier billet de blog !) en HTML.

Lorsque nous commencerons à générer des pages de blog directement à partir de fichiers markdown dans **_la section 4_** (section suivante), `path` sera utilisé pour spécifier le chemin URL pour rendre le fichier. Par exemple, le fichier markdown ci-dessus sera rendu à `localhost:8000/hello-world`.

Avant cela, créons un modèle qui rendra n'importe quel fichier markdown dans sa propre page de blog. Créez le fichier `src/templates/blog-post.js` (veuillez créer le dossier `src/templates`).

```
import React from "react";import Helmet from "react-helmet";
```

```
export default function Template({  data }) {  const post = data.markdownRemark;   return (    <div className="blog-post-container">     <Helmet title={`CodeStack - ${post.frontmatter.title}`} />      <div className="blog-post">        <h1>{post.frontmatter.title}</h1>        <div          className="blog-post-content"          dangerouslySetInnerHTML={{ __html: post.html }}        />      </div>    </div>  );}
```

Nous avons configuré le composant `Template` pour recevoir un objet `data` qui proviendra de la requête GraphQL que nous allons écrire.

Encore une fois, la requête GraphQL est nécessaire pour récupérer les données dans le composant. Le résultat de la requête est injecté par Gatsby dans le composant Template en tant que `data` et `markdownRemark`.

Nous constaterons que la propriété `markdownRemark` contient tous les détails du fichier Markdown.

Faisons maintenant la requête. Elle doit être placée sous le composant `Template` :

```
export const pageQuery = graphql`  query BlogPostByPath($path: String!) {    markdownRemark(frontmatter: { path: { eq: $path } }) {      html      frontmatter {        date(formatString: "MMMM DD, YYYY")        path        title      }    }  }`;
```

Si vous n'êtes pas familier avec GraphQL, je vais essayer de décomposer ce qui se passe ici. _Pour en savoir plus sur GraphQL, envisagez cette [**excellente ressource**](https://www.howtographql.com/)**.**_

GraphQL est simplement l'idée de Facebook d'un certain type de serveur. Ils ont écrit une spécification sur le type de requêtes qui peuvent être envoyées à ce serveur et comment le serveur doit répondre. L'API de GraphQL est meilleure que REST, car vous décrivez les données exactes dont le client a besoin, il n'y a donc plus de sous-récupération ou de sur-récupération de données.

Cela signifie que vous devez créer votre propre serveur GraphQL. Heureusement pour nous, GatsbyJS vient avec son propre serveur GraphQL intégré.

Dans le code ci-dessus, `BlogPostByPath` est la requête sous-jacente qui aboutira au retour d'un billet de blog. Il sera retourné en tant que `data` pour être injecté dans le composant `Template`.

Nous passons à `BlogPostByPath` l'argument `$path` pour retourner un billet de blog lié au chemin que nous consultons actuellement.

De plus, rappelez-vous que `markdownRemark` a transformé nos fichiers markdown. Il sera traité comme une propriété dont le contenu sera disponible via `data.markdownRemark`.

Nous pourrions accéder au HTML via `data.markdownRemark.html`. De plus, le contenu `frontmatter` que nous avons créé avec un bloc de tirets peut être accessible via `data.markdownRemark.title`, etc.

L'ensemble du fichier `blog-template.js` devrait ressembler à ceci :

```
import React from "react";import Helmet from "react-helmet";
```

```
export default function Template({  data }) {  const post = data.markdownRemark;   return (    <div className="blog-post-container">     <Helmet title={`CodeStack - ${post.frontmatter.title}`} />      <div className="blog-post">        <h1>{post.frontmatter.title}</h1>        <div          className="blog-post-content"          dangerouslySetInnerHTML={{ __html: post.html }}        />      </div>    </div>  );}
```

```
export const pageQuery = graphql`  query BlogPostByPath($path: String!) {    markdownRemark(frontmatter: { path: { eq: $path } }) {      html      frontmatter {        date(formatString: "MMMM DD, YYYY")        path        title      }    }  }`;
```

À ce stade :

* Nous avons installé un ensemble de plugins pour effectuer certaines utilités ainsi que pour charger des fichiers depuis le disque et transformer le Markdown en HTML.
* Nous avons un seul fichier Markdown solitaire qui sera rendu en tant que billet de blog.
* Nous avons un modèle React pour rendre les billets de blog dans une mise en page, ainsi qu'un GraphQL configuré pour interroger les données des billets de blog et injecter le modèle React avec les données interrogées.

Super !

### 4. Génération de nouvelles pages à partir des données des billets de blog.

Gatsby fournit une API Node, qui offre des fonctionnalités pour créer des pages dynamiques à partir de billets de blog. Cette API est exposée dans le fichier `gatsby-node.js` dans le répertoire racine de votre projet. Ce fichier pourrait exporter plusieurs API Node, mais nous nous intéressons à l'API `createPages`.

Utilisez le bloc de code suivant tel que [fournis dans la documentation officielle](https://www.gatsbyjs.org/docs/creating-and-modifying-pages/#creating-pages-in-gatsby-nodejs) (**_Notez que le chemin blogPostTemplate a été défini pour refléter le nôtre_**):

```
const path = require('path');
```

```
exports.createPages = ({ boundActionCreators, graphql }) => {  const { createPage } = boundActionCreators;
```

```
const blogPostTemplate = path.resolve(`src/templates/blog-post.js`);
```

```
return graphql(`{    allMarkdownRemark(      sort: { order: DESC, fields: [frontmatter___date] }      limit: 1000    ) {      edges {        node {          excerpt(pruneLength: 250)          html          id          frontmatter {            date            path            title          }        }      }    }  }`)    .then(result => {      if (result.errors) {        return Promise.reject(result.errors);      }
```

```
result.data.allMarkdownRemark.edges        .forEach(({ node }) => {          createPage({            path: node.frontmatter.path,            component: blogPostTemplate,            context: {} // additional data can be passed via context          });        });    });}
```

Vérifiez si cela fonctionne. Je recommande de fermer votre fenêtre de navigateur, d'arrêter le serveur `gatsby develop` depuis le terminal en utilisant `ctrl c`. Maintenant, exécutez à nouveau `gatsby develop` et ouvrez `[http://localhost:8000/hello-world](http://localhost:8000/hello-world)`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l9T2DuLWH0Cq-XSYkaZRFg.gif)
_oui 💪_

Créez un autre fichier `src/pages/24–12–2017-learning-grid/index.md`

```
---path: "/another-one"date: "2017-07-12T17:12:33.962Z"title: "Mon deuxième billet Gatsby"---
```

```
Dans la vie, il y aura des obstacles, mais nous les surmonterons. Alerte vêtements spéciaux. Ne vous jouez jamais. La clé pour plus de succès est de se faire masser une fois par semaine, très important, clé majeure, parler de vêtements.
```

```
<pre><code>// some css grid code </code></pre>
```

Encore une fois, fermez votre fenêtre de navigateur, arrêtez le serveur `gatsby develop`. Exécutez à nouveau `gatsby develop` et ouvrez `[http://localhost:8000/another-](http://localhost:8000/hello-world)one`. Cela est montré :

![Image](https://cdn-media-1.freecodecamp.org/images/1*de5Txh2KOcrUWUXDWdAqqA.gif)

Continuez si vous le souhaitez et créez vos propres pages. ✌️

### **5.** Créer une liste de nos fichiers markdown du site sur la page d'accueil.

La page d'accueil par défaut qui vient avec le site Gatsby échafaudé se trouve à `src/pages/index.js`. C'est là que nous définirions un modèle, et ferions une requête pour l'injecter avec des données pour la liste des fichiers `.md`. Faites ceci :

```
import React from "react";import Link from "gatsby-link";import Helmet from "react-helmet";
```

```
import '../styles/blog-listing.css';
```

```
export default function Index({ data }) {  const { edges: posts } = data.allMarkdownRemark;  return (    <div className="blog-posts">      {posts        .filter(post => post.node.frontmatter.title.length > 0)        .map(({ node: post }) => {          return (            <div className="blog-post-preview" key={post.id}>              <h1>                <Link to={post.frontmatter.path}>{post.frontmatter.title}</Link>              </h1>              <h2>{post.frontmatter.date}</h2>              <p>{post.excerpt}</p>            </div>          );        })}    </div>  );}
```

```
export const pageQuery = graphql`  query IndexQuery {    allMarkdownRemark(sort: { order: DESC, fields: [frontmatter___date] }) {      edges {        node {          excerpt(pruneLength: 250)          id          frontmatter {            title            date(formatString: "MMMM DD, YYYY")            path          }        }      }    }  }`;
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*vN_FXKB4LsdkItnNAWoaMg.png)

Je fais confiance que vous êtes un pro à ce stade et déjà familier avec ce qui se passe. Notez que nous avons écrit un `import` ci-dessus qui n'existe pas. Maintenant, créez le fichier `/styles/blog-listing.css` :

```
div.blog-post-preview {    border-bottom: 2px solid #e6e6e6;    padding-top: 1rem;    padding-bottom: 1rem;    margin-bottom: 1rem;}
```

```
h1 > * {    font-size: 1.2rem;    text-decoration-line: none;}
```

```
h2 {    font-size: 0.8rem !important;    font-weight: 100 !important;}
```

Redémarrez le serveur, visitez la page d'accueil, et vous devriez voir la liste en action :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DfQpVy0rjFurPHGoGvDhgg.gif)

### Conclusion

Nous sommes arrivés à la fin de ce tutoriel. Merci d'avoir lu jusqu'ici.

Cet article n'est que la partie émergée de l'iceberg compte tenu de la quantité de choses que vous pourriez faire avec Gatsby. N'hésitez pas à explorer comment vous pourriez implémenter :

* Fonctionnalité de recherche
* L'utilisation de tags pour catégoriser les billets de blog
* [Déployer](https://www.gatsbyjs.org/docs/deploy-gatsby/) votre site Gatsby

Vous pouvez récupérer le code source final [ici](https://github.com/emmyyusufu/codestack-gatsby-blog). N'hésitez pas à me soutenir ([devapparel.co](http://www.devapparel.co)) et à avoir l'air bien en le faisant. De plus, commentez ou partagez cet article. Merci d'avoir lu !

P.S. Je travaille sur un livre React avec [Ohans Emmanuel](https://www.freecodecamp.org/news/how-to-build-a-react-and-gatsby-powered-blog-in-about-10-minutes-625c35c06481/) qui vous fera maîtriser React en construisant 30 petits projets en 30 jours. Si vous voulez rester informé de cela, rejoignez [la liste de diffusion](http://eepurl.com/dfEESD). Merci !