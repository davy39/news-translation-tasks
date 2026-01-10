---
title: Création d'un Hook React Personnalisé pour les Métadonnées de Site Gatsby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-24T17:14:00.000Z'
originalURL: https://freecodecamp.org/news/creating-a-custom-react-hook-for-gatsby-site-metadata
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/cover-5.png
tags:
- name: Gatsby
  slug: gatsby
- name: metadata
  slug: metadata
- name: react hooks
  slug: react-hooks
seo_title: Création d'un Hook React Personnalisé pour les Métadonnées de Site Gatsby
seo_desc: 'By Scott Spence

  Hooks ahoy!

  Ok, let''s get it on with the new hotness in Reactland, React Hooks!This is a guide
  covering using the Gatsby custom React hook forStaticQuery which it is now replacing
  with useStaticQuery.

  If you haven''t used Gatsby before...'
---

Par Scott Spence

## Les Hooks à l'horizon !

D'accord, passons à la nouvelle tendance dans Reactland, les React Hooks ! 
Ce guide couvre l'utilisation du hook React personnalisé de Gatsby pour 
`StaticQuery` qu'il remplace désormais par `useStaticQuery`.

Si vous n'avez jamais utilisé Gatsby auparavant, `StaticQuery` est exactement cela, un moyen de 
requêter des données dans un composant Gatsby (c'est-à-dire un composant React) ou une page Gatsby où l'entrée de la requête ne change pas. C'est un excellent cas d'utilisation 
pour des données qui ne changent pas beaucoup, comme les métadonnées de votre site.

## tl;dr

Voici ma tentative de [m'équilibrer](https://youtu.be/8ruJBKFrRCk?t=93) avec [codesandbox.io](https://codesandbox.io) tout en convertissant une partie du démarreur par défaut de Gatsby qui se trouve sur [codesandbox.io](https://codesandbox.io) pour utiliser le 
hook personnalisé `useSiteMetadata`.

En utilisant [codesandbox.io](https://codesandbox.io), nous examinons l'implémentation d'un hook React personnalisé pour obtenir les métadonnées du site dans Gatsby.

**Voici une vidéo :**

%[https://www.youtube.com/watch?v=qWay-LjXwbk]

Le composant `StaticQuery` utilise le modèle [render props](https://reactjs.org/docs/render-props.html), ce qui 
signifie qu'il prend une fonction et retourne/rend en fonction de celle-ci.

J'ai détaillé ce modèle auparavant dans un article sur [l'utilisation de l'API de contexte React](http://localhost:8899/react-context-api-getting-started), c'est un composant auquel vous passez une fonction pour rendre 
un composant.

Pensez-y comme ceci :

```jsx
<Component>
 {() => ()}
</Component>

```

La première parenthèse est pour les arguments/variables et la seconde est 
ce qui est rendu, donc dans le cas du `StaticQuery` de Gatsby, vous 
passez une requête avec une balise `graphql` et ensuite les `data` qui reviennent 
de celle-ci sont utilisées dans le rendu de ce composant. Vous avez donc 
votre composant d'enveloppement qui retourne et rend un composant enfant, 
comme ceci.

```jsx
<WrappingComponent>
  {args => <ComponentToRender propsForComponent={args.propNeeded} />}
</WrappingComponent>

```

Voici une version réduite du composant `StaticQuery` utilisé dans 
le démarreur par défaut de Gatsby sur [codesandbox.io](https://codesandbox.io)

J'ai enlevé le style pour le rendre un peu plus court :

```js
const Layout = ({ children }) => (
  <StaticQuery
    query={graphql`
      query SiteTitleQuery {
        site {
          siteMetadata {
            title
          }
        }
      }
    `}
    render={data => (
      <>
        <Header siteTitle={data.site.siteMetadata.title} />
        <div>
          <main>{children}</main>
          <footer />
        </div>
      </>
    )}
  />
);

export default Layout;

```

Le `StaticQuery` prend deux props, la `query` et ce que vous voulez rendre avec `render`, c'est ici que vous pouvez déstructurer les données dont vous avez besoin à partir de la prop `data` retournée par la requête.

Je n'ai jamais vraiment aimé faire cela de cette manière, alors j'ai adopté un modèle similaire mais avec le composant contenu séparément et ensuite ajouté au `StaticQuery`. Comme ceci :

```js
const Layout = ({ children, data }) => (
  <>
    <Header siteTitle={data.site.siteMetadata.title} />
    <div>
      <main>{children}</main>
      <footer />
    </div>
  </>
);

export default props => (
  <StaticQuery
    query={graphql`
      query SiteTitleQuery {
        site {
          siteMetadata {
            title
          }
        }
      }
    `}
    render={data => <Layout data={data} {...props} />}
  />
);

```

J'ai trouvé cela plus acceptable car vous n'aviez pas à avoir tout le 
code regroupé dans le composant `StaticQuery`.

**Tout cela est-il clair ?**

Bien, maintenant oubliez tout cela ! Il est temps d'utiliser la nouvelle 
`useStaticQuery` dans Gatsby. ?

## Versions :

**Ce guide est utilisé avec les versions de dépendances suivantes.**

* gatsby : 2.1.31
* react : 16.8.4
* react-dom : 16.8.4

Vous pouvez également consulter le [code exemple](https://codesandbox.io/s/1vnvko0zqj).

---

La [documentation de Gatsby](https://www.gatsbyjs.org/docs/use-static-query/) couvre son utilisation et explique également comment créer 
votre propre hook React personnalisé pour utiliser `useStaticQuery`, voici celui que 
j'utilise dans la vidéo.

_useSiteMetadata.js_

```js
import { graphql, useStaticQuery } from 'gatsby';

const useSiteMetadata = () => {
  const { site } = useStaticQuery(
    graphql`
      query SITE_METADATA_QUERY {
        site {
          siteMetadata {
            title
            description
            author
          }
        }
      }
    `
  );
  return site.siteMetadata;
};

export default useSiteMetadata;

```

Cela peut maintenant être implémenté dans le reste du code comme un appel de fonction :

```js
const { title, description, author } = useSiteMetadata();

```

## Implémentons-le !

Dans le composant `layout`, importez le hook `useSiteMetadata`, puis nous 
pouvons supprimer le composant `StaticQuery` et déstructurer 
`title` à partir du hook `useSiteMetadata`.

Cela devrait ressembler à quelque chose comme ceci, j'ai enlevé le style pour 
plus de concision :

```js
import React from 'react';
import PropTypes from 'prop-types';
import useSiteMetadata from './useSiteMetadata';

import Header from './header';
import './layout.css';

const Layout = ({ children }) => {
  const { title } = useSiteMetadata();
  return (
    <>
      <Header siteTitle={title} />
      <div>
        <main>{children}</main>
        <footer>
          
9 {new Date().getFullYear()}, Construit avec
          {` `}
          <a href="https://www.gatsbyjs.org">Gatsby</a>
        </footer>
      </div>
    </>
  );
};
Layout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default Layout;

```

Voici la comparaison :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/compareLayout.png)

Passons maintenant au composant `seo`, même chose, supprimez `StaticQuery` et 
utilisez `useSiteMetadata` à sa place.

Voici la comparaison :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/compareSEO.png)

Si vous souhaitez consulter le code, l'exemple est disponible ici : 
[code exemple](https://codesandbox.io/s/1vnvko0zqj)

## Conclusion !

C'est tout ! Nous sommes passés de l'utilisation du modèle de props de rendu `StaticQuery` utilisé dans Gatsby à l'utilisation encore plus géniale 
du hook React `useStaticQuery`.

**Merci d'avoir lu** ?

Veuillez consulter mes autres contenus si vous avez aimé celui-ci.

Suivez-moi sur [Twitter](https://twitter.com/spences10) ou [Posez-moi une question](https://github.com/spences10/ama) sur GitHub.

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).**