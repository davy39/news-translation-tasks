---
title: Convertir le starter par défaut de Gatsby pour utiliser styled-components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-29T18:06:00.000Z'
originalURL: https://freecodecamp.org/news/convert-the-gatsby-default-starter-to-use-styled-components-2018
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/cover-3.png
tags:
- name: Gatsby
  slug: gatsby
- name: getting started
  slug: getting-started
- name: styled-components
  slug: styled-components
seo_title: Convertir le starter par défaut de Gatsby pour utiliser styled-components
seo_desc: 'By Scott Spence

  Let''s go through getting styled-components working with the Gatsby default starter.

  https://www.youtube.com/watch?v=O5sWySCr668

  In this example we''re going to use the Gatsby default starter you get with CodeSandbox
  and add in styled-c...'
---

Par Scott Spence

Passons en revue l'utilisation de styled-components avec le starter par défaut de Gatsby.

%[https://www.youtube.com/watch?v=O5sWySCr668]

Dans cet exemple, nous allons utiliser le starter par défaut de Gatsby que vous obtenez avec [CodeSandbox](https://codesandbox.io) et ajouter styled-components. Pour commencer, ouvrez un [nouveau CodeSandbox](https://codesandbox.io/s/) et sélectionnez Gatsby dans les SERVER TEMPLATES.

## 1. Dépendances

Dans la section des dépendances de l'éditeur CodeSandbox, vous devrez ajouter les éléments suivants :

```bash
gatsby-plugin-styled-components
styled-components
babel-plugin-styled-components

```

## 2. Configuration

Maintenant, nous devons modifier `gatsby-config.js` pour incorporer les nouvelles dépendances que nous venons d'ajouter. Il n'a pas d'options de configuration, donc il peut simplement être ajouté comme une ligne supplémentaire dans la configuration. Dans ce cas, je l'ajoute après le plugin `gatsby-plugin-sharp` :

```js
'gatsby-transformer-sharp',
'gatsby-plugin-sharp',
'gatsby-plugin-styled-components',

```

N'oubliez pas la virgule à la fin ?

## 3. Style Global

Maintenant que nous sommes prêts à utiliser styled-components, nous devons supprimer les styles actuellement appliqués dans le starter par défaut et appliquer les nôtres.

Dans le composant `src/components/layout.js`, il y a une importation pour `layout.css`. C'est la réinitialisation CSS pour le starter. Si nous supprimons l'importation de ici, nous verrons les styles pour la bordure et la police être réinitialisés. Nous pouvons maintenant supprimer le fichier `layout.css` et créer notre propre réinitialisation CSS en utilisant la fonction `createGlobalStyle` de styled-components.

Créez un nouveau dossier `theme`, dans cet exemple il se trouve dans `src/theme`, et ajoutez un fichier `globalStyle.js` dedans.

Cela exportera un composant `GlobalStyle` pour que nous puissions l'utiliser dans toute l'application.

Ajoutons une police Google et réinitialisons le `padding` et la `margin`. Pour un retour visuel, nous allons ajouter la police directement à l'élément body.

```js
import { createGlobalStyle } from 'styled-components';

export const GlobalStyle = createGlobalStyle`
  @import url('https://fonts.googleapis.com/css?family=Kodchasan:400,700');
  body {
    padding: 0;
    margin: 0;
    font-family: Kodchasan;
  }
  a {
    text-decoration: none;
  }
  ul {
    margin: 0 auto;
    list-style-type: none;
  }
`;

```

Ok, maintenant nous pouvons utiliser le composant exporté ici pour appliquer des styles globalement dans l'application. Nous devons donc l'avoir aussi haut que possible dans l'arborescence des composants. Dans ce cas, c'est dans le composant `layout.js` car il enveloppe toutes les pages de ce projet.

Dans `layout.js`, importez le composant `GlobalStyle`.

```js
import Header from './header';
import { GlobalStyle } from '../theme/globalStyle';

```

Ensuite, ajoutez-le avec les autres composants rendus.

```js
render={data => (
  <>
    <GlobalStyle />
    <Helmet
    ...

```

Ok ! Les styles globaux sont appliqués, nous devrions maintenant voir le changement de police et la marge autour du corps de la page changer.

Il est temps d'utiliser styled-components !

## 4. Utiliser styled-components

Maintenant, convertissons tous les styles en ligne utilisés dans le starter en styled-components.

C'est la partie styling proprement dite, qui consiste à déplacer les styles existants vers des composants stylisés, en travaillant de haut en bas de la structure des fichiers, en changeant :

```
src/components/header.js
src/components/layout.js
src/pages/index.js

```

**header.js**

```js
import React from 'react';
import { Link } from 'gatsby';
import styled from 'styled-components';

const HeaderWrapper = styled.div`
  background: rebeccapurple;
  margin-bottom: 1.45rem;
`;

const Headline = styled.div`
  margin: 0 auto;
  max-width: 960;
  padding: 1.45rem 1.0875rem;
  h1 {
    margin: 0;
  }
`;

const StyledLink = styled(Link)`
  color: white;
  textdecoration: none;
`;

const Header = ({ siteTitle }) => (
  <HeaderWrapper>
    <Headline>
      <h1>
        <StyledLink to="/">{siteTitle}</StyledLink>
      </h1>
    </Headline>
  </HeaderWrapper>
);

export default Header;

```

**layout.js**

```js
import React from 'react';
import PropTypes from 'prop-types';
import Helmet from 'react-helmet';
import { StaticQuery, graphql } from 'gatsby';

import styled from 'styled-components';

import Header from './header';
import { GlobalStyle } from '../theme/globalStyle';

const ContentWrapper = styled.div`
  margin: 0 auto;
  maxwidth: 960;
  padding: 0px 1.0875rem 1.45rem;
  paddingtop: 0;
`;

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
        <GlobalStyle />
        <Helmet title={data.site.siteMetadata.title} meta={[{ name: 'description', content: 'Sample' }, { name: 'keywords', content: 'sample, something' }]}>
          <html lang="en" />
        </Helmet>
        <Header siteTitle={data.site.siteMetadata.title} />
        <ContentWrapper>{children}</ContentWrapper>
      </>
    )}
  />
);

Layout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default Layout;

```

**index.js**

```js
import React from 'react';
import { Link } from 'gatsby';
import styled from 'styled-components';

import Layout from '../components/layout';
import Image from '../components/image';

const ImgWrapper = styled.div`
  max-width: 300px;
  margin-bottom: 1.45rem;
`;

const IndexPage = () => (
  <Layout>
    <h1>Salut les gens</h1>
    <p>Bienvenue sur votre nouveau site Gatsby.</p>
    <p>Maintenant, allez construire quelque chose de grand.</p>
    <ImgWrapper>
      <Image />
    </ImgWrapper>
    <Link to="/page-2/">Aller à la page 2</Link>
  </Layout>
);

export default IndexPage;

```

## 5. Terminé

**Merci d'avoir lu**

Voici le [code exemple](https://codesandbox.io/s/yp3z16yw11) sur lequel nous avons travaillé si vous avez besoin de référence.

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).**