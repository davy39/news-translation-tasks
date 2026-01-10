---
title: Qu'est-ce que Gatsby et pourquoi il est temps de monter dans le train de la
  hype
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-09-25T14:54:54.000Z'
originalURL: https://freecodecamp.org/news/what-is-gatsby-and-why-its-time-to-get-on-the-hype-train
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/gatsby-train.jpg
tags:
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React
  slug: reactjs
seo_title: Qu'est-ce que Gatsby et pourquoi il est temps de monter dans le train de
  la hype
seo_desc: 'Frameworks come and go, and while Gatsby may eventually drift as tech does,
  the performance and productivity boosts are strong arguments for diving in right
  away.

  Wait up, what is Gatsby?


  Gatsby is a free and open source framework based on React tha...'
---

Les frameworks viennent et partent, et bien que Gatsby puisse éventuellement dériver comme le fait la technologie, les gains de performance et de productivité sont de solides arguments pour plonger dès maintenant.

## **Attendez, qu'est-ce que Gatsby ?**

> [Gatsby](https://www.gatsbyjs.org/) est un framework gratuit et open source basé sur React qui aide les développeurs à créer des **sites web** et des **applications** ultra-rapides.

Leur emphase (je vais expliquer plus tard). J'aime le décrire comme [Create React App](https://facebook.github.io/create-react-app/) sur stéroïdes, où c'est un moyen facile de démarrer une application React et de se concentrer sur les parties vraiment différentes de votre application. Au cœur, c'est une application [Webpack](https://webpack.js.org/) glorifiée, où tout est construit sur ce même pipeline Webpack que vous avez eu du mal à écrire et à comprendre pleinement jusqu'à ce jour (ou peut-être que c'est juste moi).

La beauté, cependant, est que ce qu'il produit est un site web statique (un simple fichier HTML) avec votre application pré-rendue pour une livraison optimale. Cela signifie qu'il peut essentiellement fonctionner n'importe où, comme simplement le déposer dans [S3](https://aws.amazon.com/s3/) et [le servir comme une page web statique](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html) ou encore plus facile, avoir [Netlify](https://www.netlify.com/) [le construire et le servir pour vous](https://www.netlify.com/blog/2016/02/24/a-step-by-step-guide-gatsby-on-netlify/).

### **Tout est dans les scripts**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/chubbs-happy-gilmore.jpg)
_Chubbs avec Happy Gilmore_

Gatsby est l'un des nombreux outils disponibles qui supportent l'architecture [JAMstack](https://jamstack.org/). Pour les non-initiés, JAM signifie Javascript, APIs et Markup, ou en gros un site web statique HTML qui utilise javascript pour faire la magie.

Les applications JAMstack ont beaucoup d'avantages dès la sortie de la boîte, notamment :

* Facile à héberger
* Peu coûteux à héberger
* Il se charge super rapidement (la plupart du temps)

Cela signifie généralement plus souvent qu'autrement, vous allez avoir un site rapide qui ne vous coûte pas beaucoup d'argent à la fois pour l'hébergement et la maintenance.

### **Ça vous semble un peu familier ?**

Il est facile de comparer cela à [Rails](https://rubyonrails.org/), comme je l'entends souvent de la part des autres membres de mon équipe, et à juste titre. Il y a beaucoup de magie derrière les scènes dans Gatsby !

Mais à moins que vous ne vous appuiiez purement sur des plugins et des thèmes (ce qui est bien), à la fin de la journée, vous construisez toujours une application React comme vous le feriez ailleurs. Votre application peut _presque_ être portée vers n'importe quel autre framework (à l'exception de la partie sourcing de données et génération de pages). Les composants sont des composants, les styles sont des styles.

```jsx
const Nav = () => {
  return (
    <nav>Un composant nav normal dans une application Gatsby normale.</nav>
  )
}
```

Gatsby est opinionné sur de nombreux aspects, mais ces opinions tombent principalement en dehors de l'idée que vous construisez toujours une application webpack et que ces conventions sont celles de webpack et de la configuration derrière lui, pas nécessairement celles de Gatsby.

## **Alors, qu'est-ce qui le rend si génial ?**

### **Littéralement démarrer en moins d'une minute**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/literally.gif)
_Parks and Recreation "Littéralement"_

Sérieusement. Lancer un nouveau site Gatsby est la définition littérale de tous ces articles clickbait disant que vous pouvez faire quelque chose en 5 minutes. [Installez le CLI](https://www.gatsbyjs.org/tutorial/part-zero/#using-the-gatsby-cli) et vous êtes à 3 commandes de votre application lancée localement ou construite statiquement.

Par exemple, si vous voulez lancer un nouveau projet barebones avec [Sass](https://sass-lang.com/) :

```shell
$ gatsby new my-cool-gatsby-project https://github.com/colbyfayock/gatsby-starter-sass
$ cd my-cool-gatsby-project
$ yarn develop
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/gatsby-bootstrap-app.gif)
_Démarrage d'une application Gatsby_

Une communauté de Starters fournit un point d'entrée facile pour votre nouvelle application (ou la totalité de ce que vous voulez).

_Note : le "en moins d'une minute" dépend du type de connexion que vous avez, car vous devrez attendre que les dépendances se téléchargent et s'installent._

### **Tout rassembler dans le content mesh**

L'un des concepts derrière Gatsby est l'idée du "[content mesh](https://www.gatsbyjs.org/blog/2018-10-04-journey-to-the-content-mesh/)" et Gatsby étant la solution pour tout rassembler. De nombreuses applications, et de plus en plus, sont construites avec l'architecture JAMstack, ce qui aide à l'idée que nous pouvons sourcer autant de notre contenu à partir de nombreux endroits que nous voulons et l'intégrer dans une application performante.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/content-mesh.jpg)
_[https://www.gatsbyjs.org/blog/2018-10-04-journey-to-the-content-mesh/](https://www.gatsbyjs.org/blog/2018-10-04-journey-to-the-content-mesh/)_

Quand tout est dit et fait, vous pouvez intégrer des données de nombreuses sources dans une application compilée statiquement. C'est effectivement ultra-rapide. ?

### **Boost de performance gratuit !**

Dès la sortie de la boîte, vous obtenez votre configuration webpack superchargée incluant [le code splitting](https://developers.google.com/web/fundamentals/performance/optimizing-javascript/code-splitting/), [le prefetching](https://developers.google.com/web/fundamentals/performance/resource-prioritization), les styles en ligne, la minification des assets, et [une tonne d'autres grandes fonctionnalités](https://www.gatsbyjs.org/docs/gatsby-internals/). Améliorez cela facilement avec une multitude de plugins faciles à configurer comme la configuration de votre application en tant que [PWA](https://www.gatsbyjs.org/docs/progressive-web-app/) ([progressive web app](https://developers.google.com/web/progressive-web-apps/)) et fournissant la capacité pour le [mode hors ligne](https://www.gatsbyjs.org/packages/gatsby-plugin-offline/%3E)

Beaucoup de buzzwords là-dedans, mais à la fin de la journée, cela signifie que votre site web devrait être réactif basé sur les meilleures pratiques qui optimisent tous les assets de votre site pour la vitesse et la livraison, tout en le rendant aussi accessible que possible en [transpilant pour les anciens navigateurs](https://www.gatsbyjs.org/docs/babel/) et en s'assurant que les connexions lentes ne gaspillent pas de ressources précieuses. Il est difficile de confirmer comme une statistique dure, mais [Kyle Mathews](https://twitter.com/kylemathews) (fondateur de Gatsby) affirme que [les sites Gatsby sont 2-3x plus rapides que des types de sites similaires](https://www.gatsbyjs.org/blog/2017-09-13-why-is-gatsby-so-fast/).

### **Productivité accrue !**

Vous n'avez plus à vous soucier des complexités de vous assurer que votre application est performante en réécrivant et en ajustant votre configuration webpack selon les nouvelles meilleures pratiques pour chaque nouvelle application que vous démarrez. Gatsby fait tout cela pour vous. Il vous permet de vous concentrer sur les parties importantes qui rendent votre application spéciale, pas sur l'échafaudage.

Cela est poussé plus loin avec les [plugins](https://www.gatsbyjs.org/plugins/) de Gatsby et l'ajout de [Thèmes](https://www.gatsbyjs.org/docs/themes/). Les thèmes ne sont pas ce à quoi vous vous attendez dans le sens traditionnel, ou ce à quoi vous vous attendez de [Wordpress](https://wordpress.org/), mais ils fournissent un moyen d'abstraire n'importe quelle partie de votre application Gatsby afin que vous puissiez la réutiliser d'une application à l'autre.

Avez-vous une bibliothèque de composants de base que vous utilisez à chaque fois ? Faites-en un thème. Avez-vous [une configuration particulière pour le sourcing de données](https://www.gatsbyjs.org/packages/gatsby-source-wordpress/) que vous ne voulez pas réécrire à chaque fois ? Faites-en un plugin. Pouvoir abstraire ces pièces clés de votre application vous fait gagner du temps et du stress sur chaque nouveau projet que vous lancez, sans parler de la capacité à maintenir ces pièces en un seul endroit, en corrigeant les bugs et les améliorations avec une simple mise à jour de package.

### **Grande communauté**

Gatsby lui-même a déjà une communauté assez grande, mais en plus de cela, vous avez Webpack et React, qui existent depuis un moment. React est le [framework UI le plus populaire](https://2018.stateofjs.com/front-end-frameworks/overview/) en ce moment, ce qui rend le débogage via une simple recherche Google beaucoup plus facile. Il est difficile de trouver un problème que vous êtes le premier et le seul à rencontrer.

Si vous avez une question particulière sur Gatsby, leur Github Issues est rempli de personnes prêtes à vous aider à déboguer ou à résoudre le prochain bug. Tout ce qu'ils demandent, c'est que vous leur fournissiez poliment un moyen de reproduire, ce qui rend simplement plus facile pour eux de vous aider en premier lieu !

### **Ami de Hackerman**

Vous aimez retrousser vos manches et tweaker le pipeline vous-même ? Gatsby fournit des moyens faciles de patcher dans le traitement, qu'il s'agisse de [s'accrocher au cycle de vie de la construction](https://www.gatsbyjs.org/docs/node-apis/) ou de tweaker la [configuration webpack](https://www.gatsbyjs.org/docs/add-custom-webpack-config/). Cela permet au cœur de votre application d'être aussi facile ou avancé que vous le souhaitez, bien que si vous êtes aussi avancé, peut-être [aidez à écrire un plugin](https://www.gatsbyjs.org/docs/creating-plugins/) ou deux !

![Image](https://www.freecodecamp.org/news/content/images/2019/09/hackerman.gif)
_Hackerman_

## **Les peut-être pas si géniaux...**

### **Construire rapidement entraîne plus de bugs**

Vous devriez vous attendre à rencontrer quelques obstacles ici et là en restant sur la dernière et la meilleure version, après tout, il s'agit de logiciels open source en développement pour plus que juste votre site individuel.

L'équipe Gatsby a été [en train de construire très rapidement](https://github.com/gatsbyjs/gatsby/pulse/monthly), ce qui est génial, mais aller vite est sujet à négliger des choses en cours de route. Heureusement, ils commencent à pousser les tests automatisés partout pour aider à renforcer le code et ils essaient intentionnellement d'éviter de se précipiter sur le travail pour répondre à ce type de préoccupation.

Assurez-vous simplement d'être minutieux sur les tests de vos mises à jour de packages et n'ayez pas peur de rétrograder et de verrouiller votre version de package si vous rencontrez des problèmes.

### **Les sites statiques sont de première classe, pas les applications web**

Gatsby se présente comme une solution tout compris pour les applications statiques et non statiques, mais est-ce le cas ? La prise en charge des routes client uniquement nécessite un [plugin](https://www.gatsbyjs.org/packages/gatsby-plugin-create-client-paths/) ou [un ajustement de création de page](https://www.gatsbyjs.org/docs/client-only-routes-and-user-authentication/) ce qui est bien, mais leur [ton](https://github.com/gatsbyjs/gatsby/issues/15398) sur les [problèmes](https://github.com/gatsbyjs/gatsby/issues/16097) tend à suggérer qu'ils ne sont pas toujours également concentrés sur les deux.

Vraiment, le seul argument ici est pourquoi utiliseriez-vous Gatsby plutôt que Create React App pour ce cas d'utilisation ? Bien que cela ne soit peut-être pas de première classe, c'est toujours assez fonctionnel avec un bonus des avantages sous-jacents standard de Gatsby, mais clairement les bugs et les fonctionnalités ne vont pas être priorisés vers cet objectif.

## **Essayez-le déjà !**

Mon opinion ou celle de tout autre ne compte pas jusqu'à ce que vous l'essayiez. Dans le pire des cas, vous avez littéralement perdu 5 minutes entre l'installation des dépendances et la suppression du dossier avec le projet, ce qui, sur une note positive, est une expérience d'apprentissage. Dans le meilleur des cas, vous venez de découvrir un outil génial qui va vous aider à faire de grandes choses.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/lego-build.gif)
_Lego - nous pourrions construire un vaisseau spatial !_

Allez construire, allez expérimenter, et partagez les grandes choses que vous faites !

_Edit : Changé « ralentir » en « éviter de se précipiter » pour clarifier l'intention de la déclaration, car ils ne ralentissent pas la quantité de travail réel effectué, mais essaient d'être plus prudents avec celui-ci._

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f3a8 Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e8f3fb Inscription à ma newsletter</a>
    </li>
  </ul>
</div>

_Publié à l'origine_ sur [https://www.colbyfayock.com/2019/09/what-is-gatsby-and-why-its-time-to-get-on-the-hype-train](https://www.colbyfayock.com/2019/09/what-is-gatsby-and-why-its-time-to-get-on-the-hype-train)