---
title: Comment créer un journal consultable avec Gatsby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-16T17:23:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-searchable-log-with-gatsby-d624bf3a05af
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jxvEoOYeWq64HVZAVNoI7g.jpeg
tags:
- name: GatsbyJS
  slug: gatsbyjs
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Comment créer un journal consultable avec Gatsby
seo_desc: 'By Amber Wilkie

  For all your developer note-taking needs

  Taking notes is key to remembering most things in our lives. How many times have
  you worked on a project, then three months later needed to get back in the code,
  and it took you hours to come b...'
---

Par Amber Wilkie

#### Pour tous vos besoins de prise de notes de développeur

Prendre des notes est essentiel pour se souvenir de la plupart des choses dans nos vies. Combien de fois avez-vous travaillé sur un projet, puis trois mois plus tard, avez eu besoin de revenir dans le code, et cela vous a pris des heures pour vous remettre à niveau ? Si vous aviez pris quelques minutes pour noter quelques éléments de documentation, vous auriez pu aller droit au but.

![Image](https://cdn-media-1.freecodecamp.org/images/d-mmUTctxFHT7pg572F9k2oihMmBZ2Yvh74f)

Personnellement, je garde mes notes un peu partout — principalement dans des carnets, mais aussi ici sur ce blog. De nombreuses fois, lorsque je termine une fonctionnalité grande et difficile, j'aime bloguer les éléments clés afin de pouvoir revenir plus tard et comprendre comment j'ai fait ce que j'ai fait. De plus, cela pourrait aider quelqu'un d'autre en cours de route. Cependant, il y a des tonnes de choses que j'apprends chaque jour et qui s'échappent simplement. Je continue d'apprendre et de réapprendre, et ce n'est pas efficace.

Récemment, je voulais un moyen de noter rapidement les choses que j'apprends tout au long de la journée, ou les leçons que je veux garder à l'esprit. Mais ce n'est pas suffisant — je dois également pouvoir _rechercher_ ces journaux afin de trouver exactement ce que je cherche immédiatement. C'est exactement ce que je vais vous montrer comment construire aujourd'hui. Ce projet, de bout en bout, m'a pris peut-être une heure et demie.

### Gatsby

Ce projet est construit en utilisant [Gatsby](https://www.gatsbyjs.org), le framework front-end extrêmement populaire pour créer des sites web statiques. Je vais sauter toutes les parties de discours commercial et passer directement au code, mais si vous voulez revenir en arrière, j'ai écrit un [long article de blog sur pourquoi j'aime tant Gatsby](https://medium.freecodecamp.org/how-to-leverage-your-react-skills-with-static-site-generator-gatsby-js-81843e928606). En bref : c'est génial si vous connaissez React, et cela vaut probablement la peine de l'apprendre de toute façon si vous avez besoin d'un site statique.

### Étape 1 : Créer un nouveau site Gatsby en utilisant le beau modèle "Julia"

En supposant que vous avez le CLI Gatsby qui fonctionne, exécutez ceci pour récupérer le modèle [Julia](https://github.com/niklasmtj/gatsby-starter-julia) épuré mais magnifiquement conçu :

```
gatsby new <nom-du-site> https://github.com/niklasmtj/gatsby-starter-julia
```

Ouvrez le fichier `gatsby-config.js` et remplacez vos détails par ceux de "Julia Doe" sous `siteMeta`. Vous êtes à moitié là.

### Étape 2 : Ajouter la journalisation

Maintenant, nous voulons ajouter quelques fonctionnalités au site. Dans le répertoire `content`, ajoutez un fichier markdown ou vingt. Imbriquez-les comme vous le souhaitez. Vous suivrez ce format :

```
---
title: "Quel que soit le titre que vous voulez"
date: "2019-05-010"
draft: false
path: "/logs/quelque-slug-pour-le-fichier"
tags: test, documentation
---

# Lundi 6 mai 2019
* Ajouté de la documentation ....
```

Notez que le `path` doit être unique pour chaque fichier. J'ai nommé les miens par date (chaque semaine ayant un fichier) mais évidemment vous pouvez faire ce que vous voulez.

#### Étape 2A : suivre la documentation de Gatsby pour créer des pages à partir de Markdown

Je pourrais répéter, mais la [documentation de Gatsby elle-même](https://www.gatsbyjs.org/docs/adding-markdown-pages/) est incroyablement simple et facile à suivre. Vous installerez les plugins requis, les configurerez dans `gatsby-config.js`, créerez un modèle pour l'apparence de vos publications, et configurerez `gatsby-node.js` pour construire des pages à partir de vos fichiers markdown.

Pour voler un conseil quelque part sur Internet : si vous allez sur une page localhost que vous savez ne vous mène nulle part (je préfère `localhost:8000/garbage`), vous pouvez voir tous les liens disponibles pour votre page. C'est un moyen rapide de vérifier que Gatsby a créé toutes vos pages markdown de manière appropriée.

![Image](https://cdn-media-1.freecodecamp.org/images/Eg7SMq2ZN2jaiO7ZMShIE9vT0UIlKYMcLXdl)

#### Gardez-le propre

J'ai appris en travaillant sur ce projet que vous pouvez assigner plusieurs dossiers à scanner par le plugin du système de fichiers de Gatsby :

```
{
  resolve: `gatsby-source-filesystem`,
  options: {
    name: `images`,
    path: `${__dirname}/src/images`,
  },
},
{
  resolve: `gatsby-source-filesystem`,
  options: {
    name: `markdown-pages`,
    path: `${__dirname}/src/content`,
  },
},
```

Donc, aucun problème si vous utilisez déjà `gatsby-source-filesystem` pour lire, par exemple, vos fichiers image. J'ai également testé l'imbrication, et Gatsby attrapera tout dans votre dossier `content` de manière récursive — vous pouvez donc organiser comme vous le souhaitez.

Bons moments ! Si vous avez fait ce détour vers les docs de Gatsby, vous devriez maintenant avoir un système de journalisation entièrement fonctionnel.

### Étape 3 : Ajouter la recherche

Maintenant, la partie amusante. Nous allons ajouter la capacité de rechercher dans nos journaux en utilisant le [plugin de recherche élastique Gatsby lunr](https://github.com/gatsby-contrib/gatsby-plugin-elasticlunr-search).

#### Configurer

D'abord, `yarn add @gatsby-contrib/gatsby-plugin-elasticlunr-search`, puis nous ajouterons à `gatsby-config.js` :

```js
{
  resolve: `@gatsby-contrib/gatsby-plugin-elasticlunr-search`,
  options: {
    // Champs à indexer
    fields: [`title`, `tags`, `html`],
    resolvers: {
      MarkdownRemark: {
        title: node => node.frontmatter.title,
        tags: node => node.frontmatter.tags,
        path: node => node.frontmatter.path,
        html: node => node.internal.content,
      },
    },
  },
},
```

Notez que j'ai ajouté un champ non inclus dans les docs lunr : `html`. Nous en aurons besoin pour la recherche en texte intégral des journaux, plutôt que de simplement rechercher par tags.

#### Ajouter une barre de recherche

Évidemment, la vôtre peut aller n'importe où. J'ai mis la mienne directement sur l'index sous mon nom.

**Le composant de la barre de recherche :**

```js
import React from "react"
import { graphql, StaticQuery } from "gatsby"
import Search from "./search"

export default () => {
  return (
    <StaticQuery
      query={graphql`
          query SearchIndexQuery {
            siteSearchIndex {
              index
            }
          }
        `}
      render={data => (
        <Search searchIndex={data.siteSearchIndex.index}/>
      )}
    />
  )
}
```

Rien de bien compliqué ici — nous récupérons simplement l'index de recherche à partir des données de recherche élastique.

Le composant de recherche, essentiellement copié directement des docs lunr :

```js
import React, { Component } from "react"
import { Index } from "elasticlunr"
import { Link } from "gatsby"
import styled from "@emotion/styled"
export default class Search extends Component {
  state = {
    query: ``,
    results: []
 }

  render() {
    return (
      <div>
        <input type="text" value={this.state.query} onChange={this.search} />
        <ul>
          {this.state.results.map(page => (
            <li key={page.id}>
              <Link to={"/" + page.path}>{page.title}</Link>
              {': ' + page.tags}
            </li>
          ))}
        </ul>
      </div>
    )
  }

  getOrCreateIndex = () => {
    return this.index
      ? this.index
      : // Créer un index élastique lunr et hydrater avec les résultats de la requête graphql
      Index.load(this.props.searchIndex)
  }

  search = evt => {
    const query = evt.target.value
    this.index = this.getOrCreateIndex()
    this.setState({
      query,
      // Interroger l'index avec la chaîne de recherche pour obtenir un [] d'IDs
      results: this.index
        .search(query, { expand: true })
        // Map sur chaque ID et retourner le document complet
        .map(({ ref }) => {
          return this.index.documentStore.getDoc(ref)
        }),
    })
  }
}

```

Vous construisez un index de recherche, récupérez des résultats basés sur une chaîne partielle, hydratez ces résultats en fonction de ce que l'index retourne, puis mappez dessus pour les afficher.

Et c'est sérieusement tout. Vos pages markdown seront construites lorsque Gatsby `build` s'exécute et votre recherche indexera la première fois que vous essayez de rechercher.

![Image](https://cdn-media-1.freecodecamp.org/images/5RGRv6C7VR-i5sbunBvW3KwM5GjcjUagU7Hv)

### Étape 4 : Ajouter la sécurité

Je ne mets aucun secret d'État ou variable `env` dans ces journaux, mais je préférerais qu'un employeur potentiel ne tombe pas dessus, principalement parce que je veux être libre de parler de mes luttes ou être très clair sur ce que je ne sais pas. Si je dois me censurer, cela affectera la qualité de mes journaux.

En même temps, je ne peux pas me soucier d'une connexion ou de quoi que ce soit de trop fantaisiste. J'ai donc opté pour la sécurité la plus simple, la plus lâche et la plus facile que j'ai pu imaginer : un jeton `localStorage` basique. Si vous l'avez, vous voyez les journaux, et si ce n'est pas le cas, tant pis. Voici comment cela fonctionne.

Dans `landing-bio.js` et partout ailleurs où je veux protéger :

```js
const isBrowser = () => typeof window !== "undefined"
const isAuthenticated = isBrowser() && window.localStorage.getItem('authenticated');
[...]
{isAuthenticated ? <SearchBar /> : <div>Vous n'êtes pas Amber, donc vous ne pouvez pas lire ses journaux.</div>}
```

Je n'utiliserais jamais cela pour des informations réellement sensibles, mais c'est idéal pour un peu de tranquillité d'esprit que mes collègues ne fouineront pas dans mes journaux personnels.

![Image](https://cdn-media-1.freecodecamp.org/images/6JvxsRvmiIdc76U5xZhkmhOhQMhepUSeJgUm)

Notez que la vérification du navigateur (première ligne) est nécessaire pour que cela passe les tests sur Netlify — cela fonctionne bien sans cela sinon.

### Bonus : Déployer avec Netlify

J'ai parlé de combien j'aime [Netlify](https://www.netlify.com) dans mon [précédent article de blog sur Gatsby](https://medium.freecodecamp.org/how-to-leverage-your-react-skills-with-static-site-generator-gatsby-js-81843e928606), et je les aime toujours. C'est tellement facile de mettre vos trucs en ligne.

Tout ce que vous avez à faire est de vous rendre sur Netlify, de les autoriser à accéder au Github où vos journaux sont stockés, et ils surveilleront Github et créeront de nouvelles versions pour vous chaque fois que vous pousserez vers master. Ils créeront également des aperçus de déploiement lorsque vous ferez des PR ! C'est vraiment merveilleux et je les super-recommande.

![Image](https://cdn-media-1.freecodecamp.org/images/ET0qPPLGcm14zLGqyImUUCGIq8i4SBsQ9wiw)

Si vous allez créer des journaux en markdown, je vous recommande vivement un système de déploiement aussi facile que celui-ci, et je ne connais pas un autre qui soit aussi fluide.