---
title: Comment exploiter vos compétences React avec le générateur de site statique
  Gatsby.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T17:53:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-leverage-your-react-skills-with-static-site-generator-gatsby-js-81843e928606
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0I74xPQNi5ngVIpsTxsLhg.jpeg
tags:
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Software Engineering
  slug: software-engineering
- name: Web Development
  slug: web-development
seo_title: Comment exploiter vos compétences React avec le générateur de site statique
  Gatsby.js
seo_desc: 'By Amber Wilkie

  Sometimes a dynamic single-page app is overkill. You just need to get some attractive
  information on the internet. Welcome back to static sites. With the Gatsby.js framework,
  you don’t have to leave your React skills behind in the pur...'
---

Par Amber Wilkie

Parfois, une application dynamique à page unique est excessive. Vous avez simplement besoin de mettre des informations attrayantes sur Internet. Bienvenue dans le monde des sites statiques. Avec le framework [Gatsby.js](https://www.gatsbyjs.org), vous n'avez pas à laisser vos compétences React derrière vous dans la quête de sites plus rapides, meilleurs et plus légers.

![Image](https://cdn-media-1.freecodecamp.org/images/pkzXfmIaK3a42p1iIbTQ1BUzFcMAbUE2IkPK)
_Randonnée au-dessus de la limite des arbres dans les Bucegi, Roumanie — totalement sans rapport avec le développement web, mais joli_

### Qu'est-ce qu'un site statique et pourquoi en voulez-vous un ?

Un site statique, contrairement à un site dynamique, est un site qui a) n'interagit pas avec une base de données, et b) a la même apparence pour tout le monde. Chaque page d'un site statique existe en tant que fichier séparé.

Si vous avez travaillé avec React ou la plupart des autres frameworks front-end, vous reconnaîtrez que cela est différent de notre modèle actuel préféré de "site à page unique" — vous pouvez cliquer sur des liens, mais vous restez toujours "sur la même page". Chaque site React sur Internet est rendu presque entièrement dans la div `app` d'une page HTML très basique. Tout ce qui se trouve à l'intérieur de la div est généré dynamiquement. Souvent très spécifiquement pour l'utilisateur devant l'ordinateur.

Il peut être utile de comprendre certaines des choses qu'un site statique ne peut pas faire :

* Rendre les pages dynamiquement en fonction des informations de la base de données (afficher les informations utilisateur à `/user/<user-id>`, par exemple)
* Générer et utiliser des connexions / authentification utilisateur
* Être assuré de toute persistance des données (vous pouvez utiliser des cookies, bien sûr, mais vos utilisateurs sont toujours libres de les supprimer)

#### Avantages

Les sites statiques sont **rapides**, car ils n'ont pas besoin de communiquer avec une base de données pour obtenir leurs informations. Ils sont également déjà rendus et construits lorsque l'utilisateur demande la page depuis son navigateur, donc elle est disponible instantanément (chargement des images non compris, bien sûr). Tout le code nécessaire pour exécuter votre site web est fourni au navigateur et il s'exécute localement.

Les sites statiques peuvent être **hébergés simplement**. Pas de Heroku qui s'endort, pas de démarrage de serveurs. Il va sans dire que c'est le moyen le moins cher de mettre votre contenu en ligne. La plupart des gens seront satisfaits des options gratuites pour les sites simples.

Les sites statiques sont **stables**. La seule barrière à de plus en plus d'utilisateurs chargeant votre site est le serveur d'hébergement où vous avez vos fichiers. Pas de soucis concernant les charges de la base de données ou le traitement. Il s'agit simplement d'envoyer des fichiers HTML, CSS et Javascript, et cela peut le faire aussi rapidement que votre hébergeur le permet.

#### Inconvénients

Tous les inconvénients majeurs sont intégrés dans le concept même d'un site statique : la difficulté de mettre à jour le contenu et le manque de réponse aux utilisateurs. Si votre projet nécessite des connexions, un site statique n'est pas la bonne chose pour vous. Si vous avez beaucoup de contenu, ou un contenu similaire que vous voulez afficher de manière similaire, cela peut également être le mauvais outil.

Je ne pense pas personnellement qu'un blog soit un bon candidat pour un outil comme celui-ci, car il nécessite trop d'étapes pour passer de la création à la publication. Si vous avez utilisé quelque chose comme Wordpress, cela va sembler une corvée pour mettre les choses en ligne. En revanche, vous contrôlez votre contenu de bout en bout, et c'est très attrayant pour beaucoup de gens.

Le reste de cet article abordera le comment faire un site statique. Il y a quelques années, si vous en vouliez un, vous deviez tout écrire à partir de zéro. Puis potentiellement le déployer via FTP ou similaire. Mais je suis là pour dire : vous pouvez construire des sites web statiques en utilisant vos compétences React. Plongeons-nous.

### Mon Projet

![Image](https://cdn-media-1.freecodecamp.org/images/zJzT8hbhT-93qBRD8n8R4Fthpn-pQO7dkD9R)
_Mon site portfolio, construit avec Gatsby.js_

La raison pour laquelle je me suis lancée dans [Gatsby.js](https://www.gatsbyjs.org) en premier lieu est que je voulais refaire mon site portfolio. J'utilisais un modèle modifié que je téléchargeais sur mon site d'hébergement via FTP. C'était tellement pénible à mettre à jour que je n'y avais pas touché depuis des années. Je ne voulais pas le construire en React car alors je devrais l'héberger sur Heroku. Heroku met ses applications gratuites en veille si personne ne les utilise — un délai que je trouve inacceptable. Je savais qu'un site statique serait beaucoup plus rapide et n'aurait jamais besoin de se mettre en veille.

J'ai été ravie de trouver des générateurs de sites statiques construits en React ! Je pouvais mettre mes compétences React à profit pour construire quelque chose que je pourrais déployer sur les pages Github. Score !

Si vous êtes du genre à vouloir plonger directement dans le code, vous êtes les bienvenus dans le [dépôt github](https://github.com/AmberWilkie/portfolio) de mon [portfolio](http://www.amberwilkie.com).

### Gatsby.js vs. Next.js

En cours de recherche pour cet article, j'ai trouvé beaucoup de gens pointant vers [Next.js](http://www.nextjs.org). Il a une option pour [exporter du contenu statique](https://nextjs.org/docs/#static-html-export), mais il est plus couramment exécuté sur un serveur (entrez Heroku en veille) et est typiquement utilisé pour les personnes qui veulent employer le rendu côté serveur. Je ne peux pas en parler en tant qu'outil pour cela, mais cela semble bien et si vous avez besoin de faire du SSR, vous devriez y jeter un coup d'œil.

Pour moi, divers sites web recommandaient [Gatsby.js](https://www.gatsbyjs.org/). Je suis instantanément tombée amoureuse lorsque j'ai commencé à travailler sur mon propre portfolio.

### Pourquoi Gatsby ?

En un mot : **React**. Je sais déjà comment construire des choses en React et Gatsby exploite cet ensemble de compétences pour moi. Mais il y a plus. Beaucoup plus.

#### Communauté

Gatsby a une communauté fidèle et des tonnes de personnes développant des bibliothèques pour une utilisation avec le framework. Au moment de la rédaction de cet article, il y a [545 plugins pour Gatsby](https://www.gatsbyjs.org/plugins/). De plus, vous pouvez utiliser un grand nombre des bibliothèques React standard pour construire votre site.

#### GraphQL, API et toutes les données que l'internet possède

Au moment de la construction (lorsque vous, le développeur, construisez le site, et non lorsque l'utilisateur le visite), Gatsby peut atteindre l'internet et récupérer toutes les informations que votre cœur pourrait désirer, où que vous souhaitiez les obtenir. Ici, vous pouvez accéder à n'importe quelle API, y compris celles que vous avez construites. Gatsby intègre ensuite ces données dans le HTML qu'il génère, et crée les pages en fonction de ces données.

GraphQL est intégré directement dans le package de construction, vous pouvez donc utiliser un outil que vous connaissez peut-être déjà. Si vous préférez utiliser quelque chose comme `fetch` (ou `axios`, plus largement supporté), c'est bien aussi. Parce que vous écrivez plus ou moins du React, vous pouvez utiliser n'importe quel package React qui vous plaît.

Bien sûr, parce qu'il n'y a pas d'interaction avec le serveur lorsque le site est en ligne, Gatsby déverse les données dans des fichiers JSON. Gatsby extrait les données de là pour le rendu.

#### Chargement paresseux intégré des images

Si vous avez déjà redimensionné des images pour le web, vous savez à quel point il peut être ennuyeux de traiter l'affichage des images à une vitesse raisonnable. Entrez `gatsby-image`. Ce plugin vous permet de pré-charger vos images et de les livrer dans la taille appropriée pour le navigateur, à ce moment-là.

#### Ultra-rapide

Gatsby inclut la division de code et de données prête à l'emploi, donc votre site explosera dès le départ. Il pré-récupère également les données pour les parties du site que vous ne regardez pas. Lorsque le moment sera venu, il sera prêt à lancer de nouvelles informations à vos utilisateurs.

### Fonctionnalités intégrées

Gatsby facilite le démarrage. Après être construit sur React, ma partie préférée de Gatsby est le routage automatique.

#### Routage

Il y a un dossier `pages`, et vous y placez tous les liens de votre site. Vous pouvez donc avoir une page d'index, que vous nommerez par convention `index.js`. Vous pouvez également avoir une page `about` et peut-être une page `contact`. Gatsby veut que vous **nommiez les fichiers dans votre dossier `pages` de la même manière que les liens de votre site**.

![Image](https://cdn-media-1.freecodecamp.org/images/lLYlwCiC19Ewq61oT1fx4SQYMNDGQ9hoLMGo)
_Structure de dossier dans un projet Gatsby.js_

Ainsi, lorsque vous créez un `About.js` et un `Contact.js`, vous générerez automatiquement le routage vers `/about` et `/contact`. Dans ces composants parents, vous placerez tout code que vous souhaitez, y compris des composants supplémentaires, qui iront et vivront quelque part autre que votre dossier `pages`.

Si vous avez déjà configuré React Router, cela semble être une révélation. Il n'y a littéralement aucun travail à faire. Vous placez les composants parents correctement nommés (vous les auriez peut-être appelés `containers` dans vos projets React) dans le dossier `pages`. Gatsby fait tout le travail pour vous.

Pour lier les pages, utilisez un simple `<Link to='/contact'>Contact</Link>`.

#### Outillage

L'autre grande chose à propos de Gatsby est la facilité incroyable avec laquelle il est possible de se lancer. Il y a un outil CLI, bien sûr, donc c'est une simple question de :

```
npm install --global gatsby-cli
gatsby new site-name
gatsby develop
```

Gatsby s'occupe de tout, tout comme `create-react-app`. Vous avez le rechargement à chaud dès la sortie de la boîte. Lorsque vous avez terminé et êtes prêt à envoyer le site à votre hébergeur, il suffit de faire `gatsby build` et d'envoyer ce contenu statique où vous voulez.

#### Bibliothèques de démarrage

Une autre grande chose à propos de la communauté est le grand nombre de [bibliothèques de démarrage](https://www.gatsbyjs.org/starters/?v=2) disponibles afin que vous n'ayez pas à commencer chaque projet à partir de zéro. Si vous savez que vous voulez un blog, ou un site de présentation de type powerpoint, ou même quelque chose qui vient avec un design intégré, Gatsby peut vous envoyer sur cette voie rapidement et efficacement.

(Assurez-vous de choisir un démarreur basé sur la version 2 de Gatsby ! Je l'ai appris à la dure : la mise à niveau n'était pas agréable.)

### Le code

Alors, jetons un coup d'œil à ce que ressemble le code d'un projet Gatsby.

#### layouts/index.js

Nous commençons là où l'application commence : notre `components/layout.js`. Voici à quoi ressemble le mien, après avoir supprimé un peu de code de démarrage que je n'ai pas particulièrement besoin ou envie :

```
import React from 'react'
import '../assets/scss/main.scss'

import Header from '../components/Header'
import Footer from '../components/Footer'

class Template extends React.Component {
  render() {
    return (
      <div className='body'>
        <Header/>
        {this.props.children}
        <Footer/>
      </div>
    )
  }
}

export default Template;
```

Par convention, nous enveloppons toute page dans ce composant `Template`. Si nous avons besoin de différents templates, nous pouvons bien sûr les utiliser où nous le souhaitons.

(Note : Gatsby v1 récupérait automatiquement le code de votre `layouts/index.js` et l'appliquait à toutes les pages. Gatsby v2 s'attend à ce que vous gériez vos layouts manuellement.)

Nous devons importer notre feuille de style. Et regardez — nous pouvons utiliser Sass ! Vous devrez ajouter `node-sass` et `gatsby-plugin-sass`, mais sinon, écrivez votre sass, importez-le en haut de votre site et soyez heureux.

#### pages/index.js

`pages/index.js` est là où notre application "commence" vraiment.

Voici l'intégralité du composant pour mon site. J'ai abrégé les textes avec des ..., mais sinon j'ai tout laissé ici pour que vous puissiez voir que le code Gatsby ressemble exactement au code React, car c'en est.

```js
import React from 'react'
import me from '../assets/images/main/me.png'
import Helmet from 'react-helmet'
import Template from '../components/layout'
import Photography from '../components/Photography'
import Miscellaneous from '../components/Miscellaneous'

class IndexPage extends React.Component {
  state = {}

  ChevronLink = () => [...]

  render() {
    const { showMiscellaneous, showPhotography } = this.state

    return (
      <Template>
        <div>
          <Helmet>
            <meta charSet="utf-8"/>
            <title>Amber Wilkie, Software Engineer</title>
          </Helmet>

          <section id="aboutMe" className="main style1">
            <div className="grid-wrapper">
              <div className="col-6">
                <header className="major">
                  <h2>About Me</h2>
                </header>
                <p>Hi, it's me...</p>
                <div className='about-me-links' >
                  <a href='http://www.medium.com/@heyamberwilkie'>Tech Blog</a>
                  {this.ChevronLink('showPhotography', 'Photography')}
                  {this.ChevronLink('showMiscellaneous', 'Etc')}
                </div>
              </div>
              <div className="col-6">
                <span className="image fit">
                   <img src={me} alt="Amber near Dresden, Germany"/> 
                </span>
              </div>
            </div>
          </section>
          {showPhotography && <Photography />}
          {showMiscellaneous && <Miscellaneous/>}
        </div>
      </Template>
    )
  }
}

export default IndexPage;
```

Tout est assez basique ici : quelques spans qui basculent des sections du site, des imports/exports, vous connaissez tout cela. La seule chose à laquelle vous devez prêter attention est que nous devons importer puis référencer les éléments importés. Je ne peux pas "lier" une image locale : au moment de la construction, ces références sont générées dynamiquement. Si vous voulez référencer l'un de vos actifs, vous devrez les importer.

### Récupération de données

Le composant le plus intéressant de mon site est `Photography`. Encore une fois, j'ai supprimé un peu de code et abrégé d'autres pour faire de la place pour les parties importantes.

```js
import React, { Component } from 'react'
import { StaticQuery, graphql } from 'gatsby'
import Img from 'gatsby-image'
import { CSSTransition } from 'react-transition-group'
import { travelDescriptions } from '../utilities/constants'

class Photography extends Component {
  state = {
    currentImage: this.props.data.Images.edges[0].node,
    imageIndex: 0,
  }

  changeImage = () => [...]

  render() {
    const { currentImage } = this.state
    const imageSizes = currentImage.childImageSharp.sizes
    const imageName = currentImage.name

    return (
      <section id="photography" className="main style2">
       <div className="grid-wrapper">
         <div className='col-3'>
           <header className="major">
             <h2>Photography</h2>
           </header>
           <CSSTransition>
             [... photo descriptions ...]
           </CSSTransition>
         </div>
         <div className="col-9 image-holder">
           <div key={imageName}>
             <div className='left' onClick={() => this.changeImage(-1)}/>
           <Img
            title={imageName}
            alt={imageName}
            sizes={imageSizes}
            className="border-radius"
           />
          <div className='right' onClick={() => this.changeImage(1)}/>
        </div>
      </div>
    </div>
  </section>
)
  }
}

const query = graphql`
    query imagesQuery {
        Images: allFile(
            sort: {order: ASC, fields: [absolutePath]}
            filter: {relativePath: {regex: "/travel/"}}
        ) {
            edges {
                node {
                    relativePath
                    name
                    childImageSharp {
                        sizes(maxWidth: 1500) {
                            ...GatsbyImageSharpSizes
                        }
                    }
                }
            }
        }
    }
`
export default () => <StaticQuery
  query={query}
  render={data => <Photography data={data}/>}
/>
```

```
export default () => <StaticQuery  query={query}  render={data => <Photography data={data}/>}/>
```

#### Récupération de données GraphQL

Regardons la dernière partie de ce composant. Bien que votre site sera statique à l'exécution, il peut récupérer toutes sortes de données au moment de la construction. C'est là que notre récupération GraphQL intervient, incluse dans la bibliothèque principale de Gatsby. Parce que je travaille dans un composant, je suis obligé d'utiliser `StaticQuery` de Gatsby, qui passera les résultats de ma requête dans `this.props.data`.

Si je faisais cette requête sur une _page_, je pourrais simplement déverser ma requête dans le code. Elle passerait automatiquement les résultats à `this.props.data`. Notez que `StaticQuery` ne peut pas recevoir de props, mais les requêtes anonymes sur les pages le peuvent.

Cela fait la même chose ici. Si vous avez une structure de données plus compliquée, vous pouvez préférer créer une couche de données qui peut transmettre les props `data`. Ici, nous aurons besoin de la requête GraphQL sur la page pour obtenir `data` dans les props.

Ce n'est qu'un exemple de la manière dont Gatsby peut récupérer des données à partir de vos dossiers locaux. Pour plus d'informations, consultez la référence GraphQL des [docs Gatsby](https://www.gatsbyjs.org/docs/graphql-reference/). Il existe un certain nombre d'outils de capture d'images, également intégrés directement dans le framework. Plus d'exemples [dans les docs](https://www.gatsbyjs.org/docs/working-with-images/) sur ce sujet également.

![Image](https://cdn-media-1.freecodecamp.org/images/ckRx134SZdwgeIjBLBovcGJ6gVdhuRfayBdI)
_chargement progressif de gatsby-image_

Mais ici, nous allons simplement parler de ce que je fais. Je cherche tous les fichiers dans mon dossier `travel`. Ensuite, `childImageSharp` créera un tableau de tailles, que nous passons dans le composant `Img` (du plugin très populaire `gatsby-image`). `Img` créera un espace réservé flou pour nous et fournira également des tailles d'image efficaces en fonction de la taille de notre navigateur. Plutôt sympa, non ?

Enfin, n'oubliez pas la `key` de l'image. Vous ne mappez rien, mais `gatsby-image` s'attend à ce que vous lui disiez où l'image se charge afin qu'il puisse créer cet espace réservé flou.

### Bonus : déployer sur Netlify

Il est encore plus facile de mettre votre code sur Internet avec [Netlify](https://www.netlify.com). Ces gars vous permettent de sauter l'étape de construction et de simplement télécharger votre contenu sur Github. Netlify prendra votre code du dépôt et le rendra disponible en ligne, et le niveau de base est gratuit et inclut SSL. Il y a même un [guide étape par étape (ridiculement facile) pour mettre en place des pages Gatsby](https://www.netlify.com/blog/2016/02/24/a-step-by-step-guide-gatsby-on-netlify/). Chaque fois que vous faites un commit sur la branche master de Github, une construction Netlify sera déclenchée. Parce que Gatsby récupère les données des sources internes et externes au moment de la construction, vous obtiendrez de nouvelles données chaque fois qu'une construction est exécutée.

### Bonus : déploiement automatique avec IFTTT

En tant qu'étape supplémentaire, vous pourriez envisager de créer un déploiement automatique de votre site, afin de pouvoir récupérer du nouveau contenu à partir de vos sources externes. Par exemple, il est possible d'ajouter des résumés d'articles Medium via le plugin `gatsby-source-medium` (que je peux attester être magiquement facile à configurer).

Netlify vous fournira une URL pour faire des requêtes POST. Lorsque vous le faites, cela déclenchera une reconstruction et un déploiement de votre site. Vous pouvez conditionner cela à ce que vous voulez, en utilisant l'outil que vous préférez.

Je peux recommander [IFTTT](http://www.ifttt.com), un service qui rendra votre journée si vous n'en avez jamais entendu parler auparavant. If This Then That crée des webhooks pour vous. Vous pouvez donc conditionner une construction à, par exemple, la publication d'un nouvel article Medium. IFTTT gérera l'écouteur et l'action. Si vous publiez sur Medium, il enverra cette requête POST. Votre site Gatsby récupérera le nouveau contenu via sa requête GraphQL à Medium. Votre site sera redéployé avec le résumé de votre nouvel article.

Allez l'attraper, les amis.

### Références

* [Définition d'un site web statique](https://techterms.com/definition/staticwebsite)
* [Qu'est-ce qu'un générateur de site statique ?](https://wsvincent.com/what-is-a-static-site-generator/)
* [Gatsby vs. Next](http://blog.jakoblind.no/gatsby-vs-next/)
* [Documentation Gatsby](https://www.gatsbyjs.org/docs)
* Un grand merci à [Maribel Duran](https://www.freecodecamp.org/news/how-to-leverage-your-react-skills-with-static-site-generator-gatsby-js-81843e928606/undefined) pour [la création d'un si bon tutoriel](https://medium.freecodecamp.org/how-i-made-my-portfolio-website-blazing-fast-with-gatsby-82ccddc2f671). Faites attention, cependant : elle fait référence à un démarreur Gatsby v1. Vous détesterez la vie si vous l'utilisez, car la mise à niveau de Gatsby v1 à v2 est un énorme PITA. Je vous recommande vivement de trouver quelque chose construit en v2 pour commencer.