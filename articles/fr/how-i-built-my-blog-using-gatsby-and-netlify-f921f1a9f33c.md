---
title: Comment j'ai construit mon blog avec Gatsby et Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-28T19:11:29.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-my-blog-using-gatsby-and-netlify-f921f1a9f33c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5TRuG7tG0KrZJXKoFtHlSg.jpeg
tags:
- name: GatsbyJS
  slug: gatsbyjs
- name: Netlify
  slug: netlify
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment j'ai construit mon blog avec Gatsby et Netlify
seo_desc: 'By Pav Sidhu

  Can you name a more iconic duo? ?

  Years ago, whenever I built a static website, I didn’t use any fancy frameworks
  or build tools. The only thing I brought into my projects was jQuery, or if I was
  feeling extra fancy, I used Sass.

  Nowaday...'
---

Par Pav Sidhu

#### Pouvez-vous nommer un duo plus iconique ? 😉

Il y a des années, chaque fois que je construisais un site web statique, je n'utilisais aucun framework sophistiqué ou outil de build. La seule chose que j'apportais dans mes projets était jQuery, ou si je me sentais particulièrement sophistiqué, j'utilisais Sass.

De nos jours, nous avons des outils comme Gatsby et Netlify, qui améliorent grandement l'expérience de construction de sites web statiques. Plutôt que de penser au code boilerplate et à la configuration (je vous regarde, Webpack), vous pouvez simplement vous concentrer sur votre application.

Je n'hésiterais pas à dire que le flux Gatsby et Netlify est la meilleure expérience de programmation que j'ai jamais eue. Laissez-moi expliquer pourquoi.

### Gatsby

Gatsby est un générateur de site statique qui utilise React. Tout est configuré dès le départ, y compris React, Webpack, Prettier, et plus encore.

Puisque Gatsby est basé sur React, vous bénéficiez de tous les avantages de React, tels que ses performances, ses composants, JSX, l'écosystème de la bibliothèque React, et une grande communauté (React approche les 100 000 étoiles sur GitHub 🌟).

Si vous n'avez jamais utilisé React auparavant, il y a une courbe d'apprentissage. Mais il existe de nombreux tutoriels bien écrits qui rendent React très accessible. La [documentation officielle de React](https://reactjs.org/) est également très bien écrite.

Pour de nombreux sites web statiques comme mon blog, j'ai besoin d'utiliser des sources de données externes (mes articles de blog réels) pendant le processus de build. Gatsby prend en charge de nombreuses formes de données, y compris Markdown, les API, les bases de données et les CMS comme WordPress. Pour accéder à ces données, Gatsby utilise GraphQL.

![Image](https://cdn-media-1.freecodecamp.org/images/iM2OGEJL6tZLVWstXJ6YLcYnxcQaMCPt4Bz-)
_Tirée directement du site web de Gatsby_

Tous mes articles de blog sont en Markdown, donc j'utilise un plugin Gatsby ([gatsby-transformer-remark](https://www.gatsbyjs.org/packages/gatsby-transformer-remark/?=gatsby-transformer-remark)) qui me permet d'interroger mes fichiers Markdown en utilisant GraphQL. Il convertit également un fichier Markdown en HTML directement, comme par magie. Je dois simplement utiliser la requête GraphQL suivante pour accéder à un article spécifique :

```
query BlogPostByPath($path: String!) {  markdownRemark(frontmatter: { path: { eq: $path } }) {    frontmatter {      title      date(formatString: "Do MMMM YYYY")    }    html  }}
```

En utilisant cette requête, j'accède aux données via mes props comme suit :

```
const BlogPost = ({ props: { data: { markdownRemark } } }) => (  <div>    <h1>{markdownRemark.title}</h1>    <p>{markdownRemark.date}<p>    <div dangerouslySetInnerHTML={{ __html: markdownRemark.html }} />  </div>)
```

Si vous comprenez GraphQL, l'accès aux données à partir de Markdown en utilisant Gatsby semble naturel. Si GraphQL est nouveau pour vous, cela ajoute une autre chose à apprendre. Mais la documentation sur l'utilisation de GraphQL avec Gatsby contient beaucoup d'informations et d'extraits de code que vous pouvez utiliser.

Si vous construisez un blog simple avec seulement une ou deux requêtes, il existe des kits de démarrage Gatsby qui configurent gatsby-transformer-remark et toutes les requêtes pour vous. Pour accélérer le développement, j'ai utilisé celui appelé [gatsby-starter-blog-no-styles](https://github.com/noahg/gatsby-starter-blog-no-styles/).

Je suis un grand fan de styled-components, donc j'ai essayé de l'utiliser lors de la construction de ce blog. J'ai rencontré un problème, car il n'y avait aucun moyen pour moi de spécifier à gatsby-transformer-remark comment styliser mes composants. Au lieu de cela, j'ai dû utiliser du CSS simple pour le style. J'adorerais voir quelque chose comme ce qui suit dans `gatsby-config.js` :

```
import styled from 'styled-components'
```

```
const Header = styled.h1`  font-size: 24px;  color: #333333;`
```

```
module.exports = {  plugins: [    {      resolve: 'gatsby-transformer-remark',      options: {        h1: Header      }    }  ]}
```

En plus de la facilité d'utilisation de Gatsby, la [documentation officielle](https://www.gatsbyjs.org/docs/) est très bien écrite et à jour. Chaque guide dans les docs explique si bien les concepts de Gatsby qu'il est probable que dans la plupart des cas, vous n'aurez pas besoin de consulter une source d'information tierce.

La seule difficulté que j'ai eue avec Gatsby était lors du déploiement de mon site web. J'avais un FOUC (flash de contenu non stylisé). J'ai découvert que la mise à jour de Gatsby de 1.8.12 à 1.9.250 a résolu le problème. Je ne suis pas trop sûr de pourquoi cela l'a résolu, et j'imagine que cela devait être un problème interne avec Gatsby.

![Image](https://cdn-media-1.freecodecamp.org/images/ifD3he8pRN4CLuiN9dYw4MxLxZdVe5KmKqH4)
_Je veux dire, qui veut vraiment voir mon front ?_

### Netlify

Habituellement, lors de la construction d'un site web statique, j'utilise GitHub Pages car c'est gratuit et assez facile à configurer. Bien que je pense toujours que GitHub Pages est un excellent outil, Netlify va plus loin pour rendre l'expérience du développeur encore plus efficace.

Une fois que vous avez [connecté Netlify à votre dépôt](https://www.netlify.com/blog/2016/02/24/a-step-by-step-guide-gatsby-on-netlify/), chaque push vers votre dépôt GitHub construit automatiquement votre site web, selon le générateur de site statique que vous utilisez, et le déploie en production.

J'utilise actuellement Netlify uniquement pour l'hébergement de sites statiques. Mais il prend également en charge les fonctions cloud, la gestion de domaine (avec SSL), les soumissions de formulaires, les tests A/B, et plus encore.

L'interface web de Netlify est également propre et facile à utiliser. La différence avec AWS est comme le jour et la nuit. Bien qu'AWS soit hautement configurable, de nombreux développeurs n'utilisent pas cette fonctionnalité. Lorsque j'ai utilisé S3 ou Lambda (les services de fichiers statiques et de fonctions cloud d'Amazon) pour la première fois, j'ai passé un temps considérable à chercher la documentation difficile et parfois obsolète d'Amazon. Il y a beaucoup de complexité inutile et de jargon Amazon lorsque vous utilisez AWS. En comparaison, Netlify est un bol d'air frais. C'est l'un de ces services qui fonctionne simplement.

Le meilleur aspect de Netlify est qu'il est gratuit. Si vous faites partie d'une grande équipe ou avez besoin de plus de ressources pour les fonctions cloud, les soumissions de formulaires, et plus encore, ils ont des options payantes. Si vous prévoyez de construire un petit blog comme le mien, il est peu probable que vous deviez payer pour quoi que ce soit.

### TL;DR

Gatsby et Netlify sont les moyens les plus faciles de construire et de publier un site web statique. Point final.

Si vous souhaitez un exemple de la construction d'un blog en utilisant Gatsby, le code de mon blog est [disponible sur GitHub](https://github.com/pavsidhu/blog).

Cet article a été initialement publié sur mon blog : [Comment j'ai construit mon blog en utilisant Gatsby et Netlify](https://blog.pavsidhu.com/how-i-built-my-blog-using-gatsby-and-netlify)

Merci d'avoir lu, n'hésitez pas à ❤️ si vous avez trouvé cela utile ! J'adorerais entendre vos réflexions sur Gatsby et Netlify dans les commentaires.