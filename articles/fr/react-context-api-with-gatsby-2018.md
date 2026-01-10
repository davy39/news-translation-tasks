---
title: Utiliser l'API de Contexte React avec Gatsby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-22T16:40:00.000Z'
originalURL: https://freecodecamp.org/news/react-context-api-with-gatsby-2018
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/cover.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Gatsby
  slug: gatsby
seo_title: Utiliser l'API de Contexte React avec Gatsby
seo_desc: 'By Scott Spence

  I''m a bit late to the party using the new React Context API, I did get to use it
  the other day at work, I also made a snippet to scaffold out a component for it.

  I had followed a couple of guides explaining how to use it and neither o...'
---

Par Scott Spence

Je suis un peu en retard pour utiliser la nouvelle [API de Contexte React](https://reactjs.org/docs/context.html), je l'ai utilisée l'autre jour au travail, j'ai également [créé un extrait](https://github.com/spences10/settings/blob/35ba1ca3e9871c3ea6344ca2274ebbd327a18bed/globalVs.code-snippets#L74-L112) pour échafauder un composant pour cela.

J'avais suivi quelques guides expliquant comment l'utiliser et aucun d'entre eux n'était aussi bon que cette excellente explication de [comment l'utiliser](https://www.youtube.com/watch?v=yzQ_XulhQFw) de [@leighchalliday](https://twitter.com/leighchalliday), merci Leigh ? C'est un excellent cas d'utilisation qui m'a aidé à comprendre comment l'utiliser.

Donc, après avoir fait cela dans un projet CRA, j'ai décidé de l'utiliser sur l'un de mes projets Gatsby. Avec Gatsby, la mise en page est légèrement différente où vous pouvez avoir plusieurs mises en page pour différentes sections de votre application, ce qui se prête bien à la transmission de contexte.

Une chose à garder à l'esprit est que cela concerne mon cas d'utilisation spécifique, donc je m'excuse à l'avance si cela est confus, j'essaie de documenter cela pour m'aider à comprendre aussi ?

Avec Gatsby, si vous souhaitez utiliser React 16.3, vous devrez installer le plugin Gatsby React next :

```js
npm install gatsby-plugin-react-next

```

Gatsby utilise React 16.2 je crois, donc vous devrez utiliser ce plugin.

Une autre chose que vous devrez peut-être faire est :

```bash
npm i react react-dom
npm un react react-dom

```

Cela peut être dû au fait que j'essayais de l'utiliser dans un ancien projet, j'ai dû faire cela sur trois projets maintenant car j'avais des erreurs `createContext` n'est pas une fonction jusqu'à ce que je fasse cela.

Une autre chose que vous pourriez vouloir considérer si rien ne semble fonctionner, essayez d'utiliser la commande `npm ci`. Il s'agit de la version npm 6+ de la suppression de votre dossier `node_modules` et de la réinstallation. ?

Donc, passons en revue l'un de mes cas d'utilisation préférés en ce moment et ajoutons la prise en charge des thèmes à un site Gatsby et utilisons l'API de contexte React pour gérer le thème.

Vous pouvez voir comment thématiser une application React sans l'API de contexte React dans mon article [styled-components ? getting started](https://scottspence.me/styled-components-getting-started).

Pour illustration, je vais en parler ici maintenant, vous ajoutez le `ThemeProvider` au niveau le plus élevé dans la structure de l'application afin que tous les descendants/enfants de l'application puissent y accéder.

J'ai déjà fait cela pour mon [site personnel](https://scottspence.me) et maintenant je vais le faire ici, alors passons en revue cela ensemble.

## Créons un composant !

D'accord, donc tout dans React est un composant, c'est pourquoi je l'aime tant - alors créons un composant `SomethingContext.js`, car je veux faire des choses avec les styled-components ?

Commençons par lui donner un nom imaginatif :

```js
touch src/layouts/components/BlogThemeContext.js

```

Nous y voilà ?

D'accord, les "choses" que je veux faire avec l'API de Contexte sont :

1. changer le `ThemeProvider` de styled-components
2. faire tourner les motifs du héros du site

Maintenant, pour échafauder le composant de contexte, j'ai déjà mentionné le [snippet VS Code](https://github.com/spences10/settings/blob/71dc76fb8e11c176f4517431be57c021fb72411a/globalVs.code-snippets#L74-L111) pour mon usage personnel qui est la structure de base pour le `Context` qui est en deux parties, un `Provider` et un `Consumer`

Créons le `Context` et le `Consumer` dans ce composant.

**En utilisant le snippet, cela devrait ressembler à quelque chose comme ceci :**

###### `src/layouts/components/BlogThemeContext.js`

```js
import React from 'react';
// Le Contexte est composé de deux choses
// Provider - Unique aussi proche du niveau supérieur que possible
// Consumer - Multiple peut avoir plusieurs consommateurs
export const BlogThemeContext = React.createContext();

export class BlogThemeProvider extends React.Component {
  state = {
    item1: 1,
    item2: 2,
  };

  // ajouter une fonction ici
  functionHere = () => {
    this.setState({
      item1: 2,
      item2: 3,
    });
  };
  render() {
    return (
      <BlogThemeContext.Provider
        value={{
          ...this.state,
          functionHere: this.functionHere,
        }}>
        {this.props.children}
      </BlogThemeContext.Provider>
    );
  }
}

```

Donc, les `props` passées dans le `<BlogThemeContext.Provider>` sont l'état et les méthodes contenues dans `BlogThemeProvider`, celles-ci peuvent ensuite être accessibles dans toute l'application en utilisant le `<BlogThemeContext.Consumer>`.

Maintenant, ajoutons le `BlogThemeProvider` au niveau supérieur de notre application afin que l'état et les fonctions du provider soient accessibles pour les enfants de `layout/index.js`.

Voici à quoi cela ressemble avant d'ajouter le provider de contexte, vous remarquerez que le `ThemeProvider` de styled-components est un composant de niveau supérieur ici.

###### `src/layouts/index.js`

```js
const TemplateWrapper = ({ children }) => (
  <ThemeProvider theme={theme}>
    <PageContainer>
      <Helmet title={nameContent} meta={siteMeta} />
      <Header />
      <Main>{children()}</Main>
      <Footer />
    </PageContainer>
  </ThemeProvider>
);

```

Nous avons déjà le `ThemeProvider` de styled-components qui reçoit un objet `theme`, et nous voulons gérer le thème dans notre provider de contexte. Donc, importons le thème existant du module `globalStyle` dans `BlogThemeContext` et ajoutons `theme` à l'état du `BlogThemeProvider` :

```js
import React from 'react';
import PropTypes from 'prop-types';

import { theme } from '../../theme/globalStyle';

// Le Contexte est composé de deux choses
// Provider - Unique aussi proche du niveau supérieur que possible
// Consumer - Multiple peut avoir plusieurs consommateurs
export const BlogThemeContext = React.createContext();

export class BlogThemeProvider extends React.Component {
  state = {
    theme,
  };

  // ajouter une fonction ici
  functionHere = () => {
    this.setState({
      item1: 2,
      item2: 3,
    });
  };
  render() {
    return (
      <BlogThemeContext.Provider
        value={{
          ...this.state,
          functionHere: this.functionHere,
        }}>
        {this.props.children}
      </BlogThemeContext.Provider>
    );
  }
}

BlogThemeProvider.propTypes = {
  children: PropTypes.any,
};

```

Pendant que nous y sommes, ajoutons également la fonction pour gérer le changement de thème en remplaçant la fonction factice `functionHere` dans le snippet et importons également les thèmes entre lesquels nous voulons basculer.

```js
import React from 'react';
import PropTypes from 'prop-types';

import { theme1, theme2 } from '../../theme/globalStyle';

export const BlogThemeContext = React.createContext();

export class BlogThemeProvider extends React.Component {
  state = {
    theme,
  };

  handleThemeChange = e => {
    let theme = e.target.value;
    theme === 'theme1' ? (theme = theme1) : (theme = theme2);
    this.setState({ theme });
  };
  render() {
    return (
      <BlogThemeContext.Provider
        value={{
          ...this.state,
          handleThemeChange: this.handleThemeChange,
        }}>
        {this.props.children}
      </BlogThemeContext.Provider>
    );
  }
}

BlogThemeProvider.propTypes = {
  children: PropTypes.any,
};

```

## Utiliser le `Context.Consumer`

Donc, maintenant, utilisons-le, n'est-ce pas ? La façon de l'utiliser est très similaire à celle du `ThemeProvider` de styled-component, importez votre `<ThemeSelectProvider>` puis vous pouvez utiliser le `<ThemeSelectContext.Consumer>` pour accéder aux fonctions et à l'état du `BlogThemeContext` via le `<ThemeSelectProvider>`

L'enfant d'un consommateur est une fonction, donc plutôt que d'avoir votre application retournée comme vous le feriez avec un composant React normal comme ceci :

```js
<Wrapper>
  <Child />
</Wrapper>

```

Donc, vous devez intégrer une fonction comme ceci :

```js
<Wrapper>{() => <Child />}</Wrapper>

```

Donc, vous retournez l'application (dans cet exemple, `<Child />`) comme résultat de la fonction `<Context.Consumer>`, ici nous pouvons également obtenir toutes les propriétés ou l'état du Contexte, dans mon cas d'utilisation ici, je veux obtenir la prop `theme` du provider de Contexte `value` (`<BlogThemeProvider>`) donc nous utiliserons la destructuration ES6 pour extraire l'objet `theme`.

Le `ThemeProvider` de styled-components peut maintenant utiliser l'objet `theme` fourni par le `<BlogThemeContext.Consumer>` donc il est sûr de supprimer l'import de `globalStyle`.

```js
const TemplateWrapper = ({ children }) => (
  <BlogThemeProvider>
    <BlogThemeContext.Consumer>
      {({ theme }) => (
        <ThemeProvider theme={theme}>
          <PageContainer>
            <Helmet title={nameContent} meta={siteMeta} />
            <Header />
            <Main>{children()}</Main>
            <Footer />
          </PageContainer>
        </ThemeProvider>
      )}
    </BlogThemeContext.Consumer>
  </BlogThemeProvider>
);

```

Il y a aussi un modèle `src/template/blog-posts.js` que Gatsby utilise pour générer les articles dans ce blog, faisons de même, enveloppons l'application dans la fonction de retour pour le consommateur de contexte, avant cela ressemblait à ceci :

```js
const Template = ({ data, pathContext }) => {
  const { markdownRemark: post } = data
  const { frontmatter, html } = post
  const { title, date } = frontmatter
  const { next, prev } = pathContext

  return (
    <PostWrapper border={({ theme }) => theme.primary.light}>
      <Helmet title={`${title} - blog.scottspence.me`} />
      <Title>{title}</Title>
      <TitleDate>{date}</TitleDate>
      ....

```

Maintenant, cela ressemble à ceci :

```js
const Template = ({ data, pathContext }) => {
  const { markdownRemark: post } = data
  const { frontmatter, html } = post
  const { title, date } = frontmatter
  const { next, prev } = pathContext

  return (
    <BlogThemeProvider>
      <BlogThemeContext.Consumer>
        {({ theme }) => (
          <PostWrapper border={({ theme }) => theme.primary.light}>
            <Helmet title={`${title} - blog.scottspence.me`} />
            <Title>{title}</Title>
            <TitleDate>{date}</TitleDate>
            ....

```

## Ajouter un composant ThemeSelect

Le composant `ThemeSelect` est un composant de sélection que j'ai utilisé plusieurs fois maintenant, [voici la source](https://github.com/spences10/scottspence.me/blob/master/src/components/ThemeSelect.js) de mon site personnel, c'est ce que nous allons utiliser pour gérer le changement de thème, il utilisera la méthode `handleThemeChange` dans le `BlogThemeContext` donc nous ferions mieux d'utiliser un consommateur de Contexte pour accéder à la méthode :

###### `src/layouts/components/Footer.js`

```js
<BlogThemeContext.Consumer>
  {({ handleThemeChange }) => (
    <ThemeSelectWrapper>
      <ThemeSelect handleThemeChange={handleThemeChange} />
    </ThemeSelectWrapper>
  )}
</BlogThemeContext.Consumer>

```

Maintenant, si nous regardons le `state` dans les outils de développement React, nous pouvons voir la police changer avec la sélection du changement de thème, comme dans l'article [styled-components ? getting started](https://scottspence.me/styled-components-getting-started).

![Image](https://thepracticaldev.s3.amazonaws.com/i/r1b8qgu6lm5xjjondse7.gif)

D'accord, succès ? ? maintenant passons à la chose de commutation/transition d'arrière-plan.

## Changer le héros (motifs d'arrière-plan)

Donc, actuellement, pour basculer entre les [motifs de héros](http://www.heropatterns.com/) géniaux de [Steve Schoger](https://twitter.com/steveschoger), j'ai une fonction qui se trouve dans le module `globalStyle` qui retourne un motif HERO aléatoire :

```js
export const randoHero = () => {
  const keys = Object.keys(HERO);
  return HERO[keys[(keys.length * Math.random()) << 0]];
};

```

Cette fonction définit l'arrière-plan sur le `body` à chaque rechargement avec une clé aléatoire de l'objet `HERO`, maintenant je vais déplacer cela vers le `componentDidMount()` de `BlogThemeContext.Provider` afin que (pour l'instant) il sélectionne une clé aléatoire de l'objet toutes les dix secondes :

```js
export class BlogThemeProvider extends React.Component {
  state = {
    theme: theme1,
    background: HERO[0]
  }

  handleThemeChange = e => {
    let theme = e.target.value
    theme === 'theme1' ? (theme = theme1) : (theme = theme2)
    this.setState({ theme })
  }

  componentDidMount() {
    this.interval = setInterval(() => {
      const keys = Object.keys(HERO)
      const background =
        HERO[keys[(keys.length * Math.random()) << 0]]

      this.setState({ background })
    }, 10 * 1000)
  }

  render() {
  ....

```

Maintenant, trouvons un endroit dans l'application qui peut changer l'arrière-plan ! Comme je l'ai mentionné précédemment, l'arrière-plan de la page était défini sur le `body` via `injectGlobal` de styled-components, je veux maintenant accéder à la prop `background` du Contexte, donc je l'ai déplacé vers `src/layouts/index.js`. J'ai déjà ajouté le consommateur de Contexte pour le `theme`, donc déstructurons également la prop `background` :

```js
const TemplateWrapper = ({ children }) => (
  <BlogThemeProvider>
    <BlogThemeContext.Consumer>
      {({ theme, background }) => (
        <ThemeProvider theme={theme}>
          <PageContainer background={background}>
            <Helmet title={nameContent} meta={siteMeta} />
            <Header />
            <Main>{children()}</Main>
            <Footer />
          </PageContainer>
          ....

```

Maintenant, utilisons la prop `background` dans le conteneur principal `PageContainer`

Nous passons à la fois l'image et la couleur d'arrière-plan en tant que props de styled-component maintenant.

```js
const PageContainer = styled.div`
  background-color: ${props => props.theme.background};
  background-image: url("${props => props.background}");
  background-attachment: fixed;

```

C'est tout ! Nous avons utilisé l'API de Contexte React pour accéder à l'état et l'utiliser à (deux) points différents dans l'application.

## Merci d'avoir lu

Merci d'avoir regardé tous les murs de code !

Si vous avez des commentaires [n'hésitez pas à me contacter](https://scottspence.me/contact)

Vous pouvez trouver tout le code source de cela sur mon dépôt pour ce blog ici : [https://blog.scottspence.me](https://blog.scottspence.me)

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).**