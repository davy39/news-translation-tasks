---
title: 3 façons d'éditer Markdown avec TinaCMS + Gatsby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-09T18:27:17.000Z'
originalURL: https://freecodecamp.org/news/3-ways-to-edit-markdown-with-tina-gatsby
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/tinacms.jpg
tags:
- name: Gatsby
  slug: gatsby
seo_title: 3 façons d'éditer Markdown avec TinaCMS + Gatsby
seo_desc: 'By Thomas Weibenfalk

  Supercharge your static site with real-time content editing! ?

  In this post, I will explore the three different methods Tina offers to edit Markdown
  on your Gatsby site. You’ll learn how to set up Tina with both Page Queries and
  ...'
---

Par Thomas Weibenfalk

**Boostez votre site statique avec l'édition de contenu en temps réel !** 💡

Dans cet article, je vais explorer _les trois méthodes différentes_ que Tina offre pour éditer Markdown sur votre site Gatsby. Vous apprendrez comment configurer Tina avec les requêtes de page et les requêtes statiques.

_Cet article ne couvrira pas les bases de l'utilisation de Tina avec Gatsby. Veuillez consulter la [documentation](https://tinacms.org/docs/gatsby/manual-setup) sur la façon de configurer initialement Tina avec Gatsby._

## Quelle est la différence entre les requêtes de page et les requêtes statiques ?

Avant de plonger dans l'édition de Markdown avec Tina, nous devons comprendre comment Gatsby gère les requêtes de données avec GraphQL.

Vous pouvez sourcer des données de presque n'importe où dans Gatsby. Dans notre cas, nous utilisons _Markdown_. Lorsque vous construisez votre site, Gatsby crée un schéma GraphQL pour toutes les données. Ensuite, vous utilisez [GraphQL](https://graphql.org/learn/) dans vos composants React pour interroger vos données sourcées.

Gatsby vous permet d'interroger vos données de deux manières : [_Requêtes de page et requêtes statiques_](https://www.gatsbyjs.org/docs/static-vs-normal-queries/).
Depuis la sortie de l'[API React Hooks](https://reactjs.org/docs/hooks-intro.html) et du hook [`useStaticQuery`](https://www.gatsbyjs.org/docs/use-static-query/) dans Gatsby, il est très facile d'interroger vos données.

Il y a des cas où vous ne pouvez pas utiliser une requête statique. Commençons par explorer les différences.

### Les deux principales différences sont :

- Les requêtes de page peuvent accepter des variables GraphQL. Les requêtes statiques ne le peuvent pas.
- Les requêtes de page ne peuvent être ajoutées qu'aux composants de page. Les requêtes statiques peuvent être utilisées dans tous les composants.

Alors, pourquoi ne pouvons-nous pas utiliser des variables GraphQL dans une requête statique ? La raison est qu'une requête statique n'a pas accès au contexte de la page comme une requête de page. Le résultat est qu'une requête statique ne pourra pas accéder aux variables définies dans le contexte de la page.

Vous pouvez définir le contexte de la page dans votre fichier `gatsby-node.js` dans votre fonction `createPage`. Ici, vous pouvez fournir à votre page différentes variables qui seront injectées dans votre page au moment de la construction.

J'utilise les requêtes statiques autant que possible car j'adore l'API des hooks et la facilité des possibilités de composition qu'elle apporte. Par exemple, vous pouvez créer des hooks personnalisés et les réutiliser dans plusieurs composants.

Supposons que vous avez une requête GraphQL qui récupère des métadonnées que vous souhaitez sur plusieurs pages. Créez un hook React personnalisé avec le hook `useStaticQuery` de Gatsby à l'intérieur. Ensuite, vous pouvez utiliser votre hook personnalisé où vous le souhaitez et toujours obtenir facilement ces données dans votre composant. Lorsque vous devez avoir des variables dans votre composant, vous devez utiliser une requête de page. Les requêtes de page ne peuvent pas être utilisées avec l'API des hooks et doivent être uniques et attachées au composant de page spécifique.

Une autre grande chose avec les requêtes statiques est que vous pouvez récupérer les données dans le composant qui en a besoin. Cela évite le [_prop drilling_](https://kentcdodds.com/blog/prop-drilling) et vos données sont plus étroitement couplées au composant où elles sont utilisées.

## Vue d'ensemble de React

Pour obtenir des données, nous pouvons utiliser les options de requête de Gatsby. Pour structurer nos composants, React offre également quelques options. Vous pouvez créer votre composant soit comme un [composant de classe ou un composant fonctionnel](https://reactjs.org/docs/components-and-props.html). Avant l'API React Hooks, vous deviez utiliser des composants de classe pour avoir un état dans vos composants. Maintenant, avec les hooks, vous pouvez le faire avec des composants fonctionnels. ✨

## Trois façons d'éditer Markdown avec Tina

Étant donné toutes les options de création de composants et de sourçage de données dans Gatsby, nous devons choisir l'approche la plus adaptée au projet. Tina peut fonctionner avec toutes ces options, offrant **trois approches différentes** pour éditer Markdown avec Gatsby comme décrit ci-dessous.

- **remarkForm** - Un [composant d'ordre supérieur](https://reactjs.org/docs/higher-order-components.html) utilisé lorsque vous sourcez des données à partir d'une requête de page dans Gatsby. Ce composant peut être utilisé avec des composants fonctionnels et de classe. Veuillez noter la différence subtile ici ! La seule différence de nom avec le composant render props est le "r" minuscule.
- **useLocalRemarkForm** - Un [hook React](https://reactjs.org/docs/hooks-overview.html) destiné aux composants fonctionnels sourçant des données à partir d'une requête statique ou de page. Si le composant source des données statiques, le hook `useStaticQuery` de Gatsby serait appelé.
- **RemarkForm** - Un [composant Render Props](https://reactjs.org/docs/render-props.html) que vous pouvez utiliser dans les composants de classe sourçant des données à partir d'une requête statique ou de page. Les données statiques seraient sourcées via le composant render props `StaticQuery` de Gatsby.

### remarkForm - Comment l'utiliser et pourquoi cela ne fonctionne pas avec les requêtes statiques.

Tout d'abord, plongeons dans la façon de connecter TinaCMS avec une requête de page.
Le composant `remarkForm` dans TinaCMS est un [composant d'ordre supérieur](https://reactjs.org/docs/higher-order-components.html), un HOC en abrégé. Cela signifie qu'il s'agit d'une fonction qui prend un autre composant et retournera un nouveau composant qui a une fonctionnalité ajoutée.

Si vous n'êtes pas familier avec les HOC, je vous suggère de lire à leur sujet dans la <a href="https://reactjs.org/docs/higher-order-components.html"><b>documentation officielle de React</b></a>. Ils sont considérés comme un "usage avancé" dans le monde React.

Le composant `remarkForm` veut un autre composant comme argument et est destiné aux requêtes de page. Une requête de page injecte les données en tant que prop au composant et nous accédons aux données à partir de cette prop. Avec un hook `useStaticQuery`, les données sont collectées dans une variable, que vous choisissez, à l'intérieur du composant lui-même. Cela signifie que si vous utilisez le hook `useStaticQuery` dans Gatsby, vous n'aurez pas de composant à donner au HOC `remarkForm`. Dommage ! 😕 C'est pourquoi vous ne pouvez utiliser le composant `remarkForm` qu'avec les requêtes de page.

Alors **comment utilisez-vous ce composant avec une requête de page** dans Gatsby ? Tout d'abord, consultez le composant fictif Star Wars ci-dessous. Il montrera les trois étapes nécessaires pour tout connecter :

```javascript
// 1. Importer le HOC `remarkForm`
import { remarkForm } from 'gatsby-tinacms-remark'

const StarWarsMovie = ({ data: { markdownRemark } }) => {
  return <h1>{markdownRemark.frontmatter.title}</h1>
}

// 2. Envelopper votre composant avec `remarkForm`
export default remarkForm(StarWarsMovie)

// 3. Ajouter le fragment requis ...TinaRemark à votre requête de page
export const pageQuery = graphql`
  query StarWarsMovieById($id: String!) {
    markdownRemark(fields: { id: { eq: $id } }) {
      id
      html
      frontmatter {
        title
        releaseDate
        crawl
      }
      ...TinaRemark
    }
  }
`
```

Le code ci-dessus est un composant qui affiche des informations sur les films Star Wars. Pour l'instant, il affiche simplement un titre, mais il pourrait également afficher la date de sortie et le texte de défilement dans l'introduction du film. Mais c'est une autre histoire dans une galaxie lointaine, très lointaine... ⭐

La première étape dans cet exemple est d'importer le hook `remarkForm` depuis le plugin Gatsby 'gatsby-tinacms-remark'. C'est le plugin qui _fait fonctionner TinaCMS avec les fichiers Markdown_.

Il n'est pas nécessaire de faire des ajouts au code à l'intérieur du composant lui-même. Il pourrait s'agir de n'importe quel composant — fonctionnel ou de classe — structuré de la manière que vous souhaitez. La seule chose que vous devez faire avec le composant lui-même est d'envelopper votre composant avec le HOC `remarkForm` lorsque vous l'export.

Une autre chose que vous devez faire avant de pouvoir y aller est d'ajouter le fragment GraphQL `...TinaRemark` dans votre requête. Cela est nécessaire pour que TinaCMS reconnaisse vos données et crée les champs d'édition requis dans la barre latérale de TinaCMS. Après cela, vous n'avez plus qu'à démarrer votre serveur de développement pour afficher le site et la barre latérale de Tina.

Assez facile, n'est-ce pas ? Juste trois petites étapes et vous aurez une belle barre latérale pour éditer votre contenu sur votre site. 😊

_Mais que faire si vous souhaitez utiliser une requête statique et non une requête de page ?_

### useLocalRemarkForm à la rescousse !

Nous avons appris que le HOC `remarkForm` ne fonctionnera pas sur les requêtes statiques. Nous devons donc trouver une autre solution pour utiliser les requêtes statiques avec TinaCMS.

**Bonne nouvelle !**

Le composant `remarkForm` est essentiellement un "wrapper" pour le hook `useLocalRemarkForm`. 💡 Il prend un composant comme argument, appelle `useLocalRemarkForm` avec les données de la requête de page et retourne un nouveau composant avec les données de la requête et TinaCMS connecté.

Nous pouvons utiliser le hook `useLocalRemarkForm` directement, sans utiliser le HOC `remarkForm`. Cela peut être utile avec les requêtes statiques ou si nous préférons simplement travailler avec des hooks !

Jetez un coup d'œil à l'exemple de code ci-dessous pour avoir une idée de comment `useLocalRemarkForm` fonctionne.

```javascript
// 1. Importer le hook useLocalRemarkForm
import React from 'react';
import { useLocalRemarkForm } from 'gatsby-tinacms-remark';
import { useStaticQuery } from 'gatsby';

const StarWarsMovie = () => {
  // 2. Ajouter le fragment requis TinaCMS à la requête GrahpQL
    const data = useStaticQuery(graphql`
      query StarWarsMovieById {
        markdownRemark(fields: { id: { eq: "sw-01" } }) {
          id
          html
          frontmatter {
            title
            releaseDate
            crawl
          }
          ...TinaRemark
        }
      }
    `);
  // 3. Appeler le hook useLocalRemarkForm et passer les données
  const [markdownRemark] = useLocalRemarkForm(data.markdownRemark);
  return <h1>{markdownRemark.frontmatter.title}</h1>
}

export default StarWarsMovie;
```

Ce n'est qu'un exemple de composant illustrant comment `useLocalRemarkForm` fonctionne. Dans le monde réel, ce ne serait pas une solution optimale d'utiliser une requête statique pour cela. C'est parce que, comme vous pouvez le voir, vous ne pouvez pas utiliser de variables à l'intérieur du hook `useStaticQuery` pour le rendre dynamique. Vous devez coder en dur l'ID du film. Donc cette requête fonctionnera pour ce film spécifique uniquement, ce qui n'est pas bon.

Décomposons ce qui se passe ici :

1. Nous importons le hook personnalisé `useLocalRemarkForm` pour pouvoir l'utiliser dans notre composant.
2. Tout comme avant, le fragment `...TinaRemark` est nécessaire dans la requête GraphQL. Nous l'ajoutons donc là.
3. Lorsque nous avons récupéré nos données du hook `useStaticQuery` de Gatsby, nous pouvons appeler le hook `useLocalRemarkForm` de TinaCMS avec ces données. Ce hook retournera un tableau avec deux éléments. Le premier élément est pratiquement les données avec lesquelles nous avons appelé le hook. Il a la même forme et est prêt pour nous à utiliser dans notre composant. Le deuxième élément est une référence au formulaire Tina. Nous n'en avons pas besoin, donc nous ne le déstructurons pas comme nous le faisons avec `markdownRemark`.

Si vous vous demandez à propos de cette ligne :

```javascript
const [markdownRemark] = useLocalRemarkForm(heroData.markdownRemark)
```

C'est un exemple de [déstructuration ES6](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment). Comme nous obtenons un tableau avec deux éléments en retour, je déstructure le premier élément (qui est nos données) et le nomme `markdownRemark`. Vous pouvez le nommer comme vous le souhaitez.

### RemarkForm - Le composant Render Prop

Vous ne pouvez pas utiliser les hooks React sur les composants de classe. C'est pourquoi Tina fournit un composant [`RemarkForm`](https://tinacms.org/docs/gatsby/markdown/#2-the-render-props-component-remarkform) qui utilise le modèle [Render Props](https://reactjs.org/docs/render-props.html).

Ce composant fonctionne avec les requêtes de page et les requêtes statiques. Je vais montrer comment l'utiliser avec une requête de page ci-dessous.

Jetez un coup d'œil à l'exemple ci-dessous :

```javascript
// 1. Importer le composant render prop RemarkForm
import { RemarkForm } from '@tinacms/gatsby-tinacms-remark'

class StarWarsMovie extends React.Component {
  render() {
    /*
     ** 2. Retourner RemarkForm, passer markdownRemark
     **    à la prop remark et passer ce que vous
     **    voulez rendre à la prop render
     */
    return (
      <RemarkForm
        remark={this.props.data.markdownRemark}
        render={({ markdownRemark }) => {
          return <h1>{markdownRemark.frontmatter.title}</h1>
        }}
      />
    )
  }
}

export default StarWarsMovie

// 3. Ajouter le fragment requis ...TinaRemark à votre requête de page
export const pageQuery = graphql`
  query StarWarsMovieById($id: String!) {
    markdownRemark(fields: { id: { eq: $id } }) {
      id
      html
      frontmatter {
        title
        releaseDate
        crawl
      }
      ...TinaRemark
    }
  }
`
```

D'accord, encore une fois, voyons ce qui se passe ici :

1. Nous importons le composant `RemarkForm` pour l'utiliser dans notre code.
2. Dans notre instruction return, nous retournons le composant `RemarkForm` et passons ses props prédéfinies et requises. La prop remark fournit à `RemarkForm` les données markdown sourcées à partir de la requête de page. La prop render obtient le JSX que nous voulons rendre via une fonction, ou une prop render. `RemarkForm` connectera Tina pour éditer les données puis rendra ce qui est spécifié dans la fonction de la prop render.
3. Tout comme avant, nous devons ajouter le fragment `...TinaRemark` à la requête de page.

## Prochaines étapes

**C'est tout !** Trois façons d'utiliser Tina pour éditer des fichiers Markdown dans Gatsby. 🎉

Dans cet article, nous avons appris comment _configurer Tina avec les requêtes statiques et les requêtes de page dans Gatsby_. Nous avons également appris trois façons différentes d'éditer Markdown avec Tina en fonction de votre type de composant React.

Ce ne sont que les bases pour vous lancer. Si vous aimez Tina et souhaitez en savoir plus, vous devriez consulter la [documentation officielle](https://tinacms.org/docs/). Il y a beaucoup plus de choses à lire et quelques cas d'utilisation intéressants.

Par exemple, vous pouvez apprendre comment appliquer l'[édition en ligne](https://tinacms.org/docs/gatsby/inline-editing) et aussi comment [personnaliser les champs de formulaire](https://tinacms.org/docs/gatsby/markdown#customizing-remark-forms) dans la barre latérale de Tina.

Tina est un excellent ajout à l'écosystème React et aux générateurs de sites statiques comme Gatsby. Il offre à votre site une manière agréable et facile d'éditer et d'interagir avec votre contenu.
Je suis ravi de voir à quel point TinaCMS sera grand et ce qu'il pourra faire à mesure qu'il évoluera !

> Publié à l'origine sur [TinaCMS.org](https://tinacms.org/blog/three-ways-to-edit-md/)

## Plus de lectures et d'apprentissages

[Documentation officielle de Tina](https://tinacms.org/docs/)

[Communauté Tina](https://community.tinacms.org/)

Tina sur Twitter : [@tina_cms](https://twitter.com/tina_cms)

---
N'hésitez pas à me rendre visite sur ces liens :

Regardez le tutoriel de Weibenfalk pour [Tina & Gatsby](https://www.youtube.com/watch?v=eZWJ9ZtF61A&t=265s).
Twitter — [@weibenfalk](https://twitter.com/weibenfalk),
Weibenfalk sur [Youtube](https://www.youtube.com/c/weibenfalk),
Site web des [Cours Weibenfalk](https://www.weibenfalk.com).