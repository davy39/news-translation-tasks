---
title: Pourquoi je crois que Gatsby.js possède les meilleurs outils de JavaScript
  pour l'optimisation d'images — et comment les utiliser
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-16T10:22:28.000Z'
originalURL: https://freecodecamp.org/news/why-i-believe-gatsby-js-has-javascripts-best-tools-for-image-optimisation-and-how-to-use-them-939c82d05395
coverImage: https://cdn-media-1.freecodecamp.org/images/1*imOlCXHKx-yhN1S3i423SQ.jpeg
tags:
- name: GatsbyJS
  slug: gatsbyjs
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Pourquoi je crois que Gatsby.js possède les meilleurs outils de JavaScript
  pour l'optimisation d'images — et comment les utiliser
seo_desc: 'By Bret Cameron

  A beginner’s guide to using Gatsby.js and GraphQL for image optimisation


  _Image Credit: [Ryan Searle / Unsplash](https://unsplash.com/photos/BnTRzW95mnw"
  rel="noopener" target="blank" title=")

  Like so many developers, my first fully-...'
---

Par Bret Cameron

#### Un guide pour débutants sur l'utilisation de Gatsby.js et GraphQL pour l'optimisation d'images

![Image](https://cdn-media-1.freecodecamp.org/images/1*imOlCXHKx-yhN1S3i423SQ.jpeg)
_Crédit image : [Ryan Searle / Unsplash](https://unsplash.com/photos/BnTRzW95mnw" rel="noopener" target="_blank" title=")_

Comme tant de développeurs, mon premier site entièrement fonctionnel était un blog. Je l'ai construit en tant que thème WordPress personnalisé, et j'avais de grands projets pour une page d'accueil remplie d'images de haute qualité des articles.

Lorsque j'ai mis le site en ligne pour la première fois, j'ai tapé l'URL et… j'ai attendu. Ce fut un anti-climax majeur. Bien trop de secondes se sont écoulées alors que les images s'affichaient lentement.

Jusqu'à ce point, je n'avais pas fait d'optimisations significatives des images. Ce fut une leçon importante pour un développeur relativement nouveau, et je me suis mis à apprendre comment faire autant d'optimisations que possible. Mais optimiser les tailles d'images, configurer différentes tailles et résolutions pour chaque image selon les écrans, et mettre en place le chargement paresseux avec une belle animation de "fade in" était beaucoup de travail. Essayer de résoudre ces problèmes manuellement était bon pour l'apprentissage, mais ce n'était certainement pas quelque chose que je voulais refaire encore et encore.

Heureusement, il existe une meilleure façon. Maintenant, en tant que développeur React, j'ai rencontré de nombreux systèmes et modules différents de traitement d'images qui rendent l'optimisation des images simple. Mais — jusqu'à présent — rien de ce que j'ai rencontré ne se rapproche de Gatsby.js.

En utilisant plusieurs composants de Gatsby, vous pouvez facilement optimiser la livraison de vos images — avec des animations de "blur up" ou des placeholders SVG tracés — plus des optimisations supplémentaires, comme l'utilisation du format d'image WebP pour les navigateurs qui les supportent. Elles se chargent rapidement, de manière fluide, à la résolution idéale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qz1vQPsgbVratlVCUUQNTg.png)
_Une combinaison puissante : React, GraphQL et Gatsby_

### Présentation de l'optimisation d'images avec Gatsby

Gatsby.js rend l'optimisation des images facile, sauf pour une chose : si vous n'avez jamais utilisé GraphQL auparavant, le processus peut prendre un peu de temps pour s'y habituer. Il m'a fallu quelques essais pour maîtriser Gatsby image, principalement à cause de ma méconnaissance de GraphQL.

J'ai également senti que de nombreux tutoriels (y compris les officiels) étaient insuffisants lorsqu'il s'agissait d'expliquer comment gérer plus d'une image. Le starter officiel de Gatsby contient un composant image, et cela fonctionnerait bien si votre site n'avait qu'une poignée d'images. Mais que faire s'il en avait des dizaines ou des centaines ?

C'est ce que cet article vise à répondre. Nous allons adopter une approche étape par étape pour combiner les puissances de Gatsby et GraphQL pour l'optimisation d'images. Nous commencerons par rendre trois images, et dans la section finale, je discuterai de quelques façons de passer à l'échelle.

### Guide étape par étape

#### Étape 1 : Installer les dépendances

Gatsby dispose de deux principaux composants d'image : `gatsby-image` et `gatsby-background-image`.

Pour utiliser l'un d'eux, vous aurez besoin de plusieurs composants supplémentaires pour votre projet Gatsby. (Si vous êtes nouveau dans Gatsby, vous pouvez découvrir [comment démarrer un projet ici](https://www.gatsbyjs.org/docs/quick-start/)). Une fois votre projet Gatsby configuré, vous pouvez installer tous les plugins nécessaires liés aux images via npm, en tapant :

```
npm i gatsby-image gatsby-background-image gatsby-source-filesystem gatsby-plugin-sharp gatsby-transformer-sharp -s
```

Cela peut sembler beaucoup, mais chaque plugin fait plus ou moins un seul travail :

* `gatsby-image` est utilisé pour afficher les images
* `gatsby-background-image` est utilisé pour afficher les images de fond
* `gatsby-source-filesystem` vous permet d'interroger les fichiers dans le système de fichiers de votre site en utilisant GraphQL
* `gatsby-transformer-sharp` est le plugin qui vous permet de créer plusieurs images des bonnes tailles et résolutions via des requêtes
* et `gatsby-plugin-sharp` connecte les plugins Sharp et Gatsby ensemble

#### Étape 2 : Configurer Gatsby

Une fois installés, vous devez vous assurer que certains des plugins ci-dessus sont présents dans votre fichier `gatsby-config.js` dans le répertoire racine de votre application web.

Dans l'exemple ci-dessous, j'ai identifié deux répertoires, `images` et `pages`, où je souhaite pouvoir interroger mon système de fichiers. Dans cet article, nous nous concentrerons uniquement sur `images`, mais il est courant d'interroger également votre répertoire `pages` !

```
module.exports = {  plugins: [    `gatsby-transformer-sharp`,    `gatsby-plugin-sharp`,    {      resolve: `gatsby-source-filesystem`,      options: {        name: `images`,        path: `${__dirname}/src/images`,      },    },    {      resolve: `gatsby-source-filesystem`,      options: {        name: `pages`,        path: `${__dirname}/src/pages`,      },    },  ],}
```

Si vous êtes habitué à installer et importer des packages npm, jusqu'à présent cela peut sembler assez simple. À ce stade, les choses commencent à paraître un peu plus inhabituelles.

#### Étape 3A : Tester les requêtes dans GraphQL

Maintenant, nous allons accéder à l'interface GraphiQL. Par défaut, les applications Gatsby s'exécutent sur `localhost:8000`. Nous pouvons accéder à l'interface GraphiQL en ajoutant `/___graphql` à la fin du domaine (c'est 3 tirets bas de suite).

Ici, nous pouvons essayer différentes requêtes sur nos données avant de les intégrer dans notre code. Cela nous fera gagner du temps de débogage plus tard, car nous savons que les requêtes récupèrent les données que nous voulons.

Tout d'abord, vérifions que notre fichier `gatsby-config.js` fonctionne correctement. Tapez le code suivant dans l'interface GraphiQL et appuyez sur l'icône de lecture (ou `CTRL/CMD` + `ENTER`) :

```
{  allDirectory {    edges {      node {        name      }    }  }}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*HrHWozx4cHLjprCXEjfeJg.png)
_J'ai également un sous-répertoire "icons" dans mon dossier images, donc il a été retourné également._

Si vous voyez quelque chose de similaire à l'image ci-dessus, cela fonctionne. Maintenant, interrogeons le contenu de notre dossier images, en tapant :

```
{  allFile(filter:{ sourceInstanceName:{eq: "images"} }){    edges{      node{        relativePath        childImageSharp {          id        }      }    }  }}
```

Si la propriété "childImageSharp" retourne un ID, cela signifie que nous pouvons utiliser les optimisations d'images de Gatsby dessus. Cela retournera `null` pour des fichiers comme les SVGs, car ils ne peuvent pas être davantage optimisés, mais cela devrait vous donner une chaîne pour chaque `jpg` et `png`.

#### Étape 3B : Préparer nos requêtes d'images spécifiques

Maintenant, attrapons une poignée d'images spécifiques. Lorsque vous effectuez des requêtes sur une image, vous devez indiquer à Gatsby si cette image est `fixed` ou `fluid`. Les images `fixed` ont des dimensions connues et nécessitent moins de processus pour être optimisées. Les images `fluid` ont des dimensions qui changent en fonction de la taille de la fenêtre et d'autres facteurs contextuels.

Je construis un portfolio et j'ai des images pour chacun de mes services. Supposons donc que nous voulons attraper trois images appelées `webdev.jpg`, `design.jpg` et `writing.jpg`, et nous savons que leurs dimensions sont `fluid`.

```
{   webdev:file(relativePath:{eq:"webdev.jpg"}) {    childImageSharp {      fluid(maxWidth: 1600) {        base64      }    }  }    design:file(relativePath:{eq:"design.jpg"}) {    childImageSharp {      fluid(maxWidth: 1600) {        base64      }    }  }    writing:file(relativePath:{eq:"writing.jpg"}) {    childImageSharp {      fluid(maxWidth: 1600) {        base64      }    }  }  }
```

Notez que les termes avant chaque deux-points peuvent être n'importe quoi. Ici, il est logique de rester sur le nom du fichier. Nous définissons également une propriété max-width de 1600 pixels, afin que Gatsby sache qu'il n'a pas besoin de préparer des versions de chaque image plus grandes que cela.

`base64` est la propriété qui contient une version minuscule et floue de notre image qui se chargera presque immédiatement, puis sera remplacée en douceur par une version haute résolution. Si notre requête retourne une valeur pour `base64`, alors tout fonctionne. Nous sommes prêts à inclure cette requête dans notre code !

#### Étape 4 : Importer les composants et rendre

Naviguez vers n'importe quel composant où vous souhaitez afficher les images. Tout d'abord, vous devez importer les composants `StaticQuery` et `graphql` depuis `"gatsby"` en haut de votre fichier, ainsi que `Img` ou `BackgroundImage`, comme ceci :

```
import { StaticQuery, graphql } from "gatsby"import Img from "gatsby-image"import BackgroundImage from "gatsby-background-image"
```

Notre composant React devrait retourner une balise `<StaticQuery>`, qui possède une propriété `query` et une propriété `render`.

```
<StaticQuery query={  graphql`{    # nos requêtes GraphQL vont ici  `}   render={(data) => (    <>      {/* notre JSX va ici */}    </>  )}/>
```

Nous pouvons coller nos requêtes d'images ci-dessus dans la propriété `query`, mais cette fois nous remplacerons `base64` par le fragment que nous voulons rendre pour nos images. Dans ce cas, nous utiliserons `...GatsbyImageSharpFluid`.

Mais supposons que nous décidions plus tard que nous voulions l'effet SVG tracé, et que nous voulions utiliser le format WebP lorsque cela est possible. Nous pouvons simplement échanger notre fragment avec `...GatsbyImageSharpFluid_withWebp_tracedSVG`.

Notre code devrait maintenant ressembler à ceci :

```
<StaticQuery query={  graphql`{    webdev:file(relativePath:{eq:"webdev.jpg"}) {    childImageSharp {      fluid(maxWidth: 1600) {        ...GatsbyImageSharpFluid      }    }  }    design:file(relativePath:{eq:"design.jpg"}) {    childImageSharp {      fluid(maxWidth: 1600) {        ...GatsbyImageSharpFluid      }    }  }    writing:file(relativePath:{eq:"writing.jpg"}) {    childImageSharp {      fluid(maxWidth: 1600) {        ...GatsbyImageSharpFluid      }    }  }  `}   render={(data) => (    <>      {/* notre JSX va ici */}    </>  )}/>
```

Enfin, nous devons simplement inclure l'image dans notre JSX.

Le composant `Img` prend une propriété `fluid` (où vous mettez la référence des données de la requête) et une propriété `alt`.

```
<Img   fluid={data.webdev.childImageSharp.fluid}  alt=""/>
```

Le composant `BackgroundImage` prend une propriété `tag` (si elle est laissée vide, elle rend un `div`), une propriété `fluid`, et une propriété `backgroundColor`.

```
<BackgroundImage  tag="section"  fluid={data.webdev.childImageSharp.fluid}  backgroundColor={`#000`}>  {/* les éléments enfants qui vont au-dessus de l'arrière-plan */}</BackgroundImage>
```

#### Mettre le tout ensemble

Voici un composant Gatsby complet qui prend trois images de notre dossier `images` et les rend :

### Stratégies pour passer à l'échelle

Alors, comment faire pour que cela fonctionne lorsque nous devons traiter un plus grand nombre d'images ? Voici quelques idées pour vous lancer.

#### Parcourir un dossier

Supposons que nous avions une liste d'icônes que nous voulions afficher. Plutôt que de les interroger toutes séparément, nous pourrions les mettre dans leur propre répertoire, et utiliser une boucle pour parcourir les résultats de la requête. Par exemple, nous pourrions interroger l'ensemble du répertoire "icons" :

```
{  icons:allFile(filter:{ relativeDirectory:{eq: "icons"} }){    edges{      node{        name        relativePath        childImageSharp {          id        }      }    }  }}
```

Ensuite, si nous enregistrons `data.icons.edges` dans la console, nous pouvons voir un tableau d'éléments que nous pourrions parcourir. Voici un exemple de ce à quoi cela pourrait ressembler.

```
data.icons.edges.map(item => (  <Img     fluid={item.node.childImageSharp.fluid}     alt={item.node.name}   />))
```

#### Passer des données dynamiques

Une méthode importante consiste à ajouter des variables dynamiques à nos requêtes. GraphQL a une syntaxe spécifique pour cela.

Pour ce faire, donnons un nom à notre requête, `findFile`, en utilisant le mot-clé `query`. Ensuite, entre parenthèses, nous pouvons nommer n'importe quel nombre de nouvelles variables.

Dans GraphQL, toutes les variables doivent être précédées de `$`. Après le nom de la variable, nous utilisons un deux-points et spécifions ensuite le type : ici, une `String`. Enfin, nous pouvons utiliser `=` pour passer une valeur de secours par défaut, et cela nous permettra de tester la requête dans GraphiQL.

```
query findFile($relativePath: String = "webdev.jpg") {  file(relativePath: {eq: $relativePath}) {    id    relativePath    publicURL  }}
```

Il est possible d'ajouter une logique supplémentaire à ces requêtes en utilisant les directives `@include(if: Boolean)` et `@skip(if: Boolean)`.

Les variables GraphQL sont particulièrement utiles si nous voulons que nos utilisateurs puissent filtrer dynamiquement les données. Mais elles sont également pratiques pour toute raison pour laquelle nous pourrions vouloir séparer certaines données de notre requête réelle, par exemple, si nous devons les modifier d'une certaine manière d'abord.

#### Créer des fragments personnalisés

Vous vous souvenez de `...GatsbyImageSharpFluid` ci-dessus ? C'est un fragment, qui est essentiellement un raccourci pour un ensemble réutilisable de champs de requête. Nous pouvons également définir nos propres fragments.

Même si nous n'appelons que trois champs de requête — `id`, `relativePath` et `publicURL` — cela peut ajouter de nombreuses lignes de code supplémentaires si nous les utilisons de manière répétée. Au lieu de répéter la description de la documentation officielle sur la façon de procéder, je vous recommande de [la consulter](https://graphql.org/learn/queries/#fragments).

### Conclusion

Dans l'ensemble, j'espère que cet article vous a ouvert les yeux sur les puissants outils d'optimisation d'images qui accompagnent Gatsby.js, et vous a donné quelques idées sur la façon de les appliquer à des projets à plus grande échelle.

Pour comprendre pleinement et maximiser ces outils puissants, vous devez maîtriser à la fois React et GraphQL. Lorsque j'ai commencé à utiliser Gatsby, j'ai sauté GraphQL, sans réaliser qu'une compréhension de celui-ci — au moins à un niveau basique — était essentielle pour tirer le meilleur parti des fonctionnalités d'optimisation d'images de Gatsby.