---
title: Pourquoi utiliser GatsbyJS pour construire des sites statiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-04T22:31:57.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-use-gatsbyjs-to-build-static-sites-4f90eb6d1a7b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c4wjZPrF_3AnRMUZd5tlpw.png
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Pourquoi utiliser GatsbyJS pour construire des sites statiques
seo_desc: 'By Ajay NS

  Gatsby has been growing over time, and I’m glad to see it in use by a huge number
  of sites like marketing sites, blogs, and generated static pages.

  What attracted me in the first place was the smooth development experience, incredible
  resu...'
---

Par Ajay NS

Gatsby a connu une croissance au fil du temps, et je suis heureux de le voir utilisé par un grand nombre de sites comme des sites marketing, des blogs et des pages statiques générées.

Ce qui m'a attiré en premier lieu, c'est l'expérience de développement fluide, les résultats incroyables et la communauté chaleureuse. En approfondissant un peu son fonctionnement, son écosystème et en discutant de son potentiel avec d'autres développeurs, j'ai réalisé à quel point il est puissant — bien plus que je ne l'avais initialement présumé.

Cet article vise à vous faire comprendre pourquoi il a gagné en popularité. Si vous l'utilisez déjà, vous aurez une meilleure idée des fonctionnalités que vous pourriez utiliser pour une expérience de développement encore plus grande.

Notez bien que cela fonctionne pour moi, et je partage simplement mes opinions. Je ne dis pas que votre configuration actuelle, qui fonctionne pour vous, est obsolète, mais j'essaie simplement de partager comment Gatsby a été formidable pour moi.

### Qu'est-ce que Gatsby ?

C'est un autre générateur de sites statiques comme Hugo, Jekyll et autres. Alors, qu'est-ce qui le rend spécial ? Pourquoi en parlons-nous spécifiquement ?

Gatsby peut être utilisé pour construire des sites statiques qui sont des Applications Web Progressives (PWA), qui suivent les dernières normes du web et qui sont optimisés pour être hautement performants. Il utilise les dernières technologies populaires, y compris ReactJS, Webpack, GraphQL, JavaScript moderne ES6+ et CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yCPN-lvsZ7k2WcRsPQYjqA.png)
_GraphQL + React + Webpack = ❤️_

Cela signifie que de nombreux développeurs peuvent se lancer sans une courbe d'apprentissage trop raide, car ils connaissent déjà ou ont au moins utilisé une partie de cette stack technologique sur laquelle Gatsby est construit.

De plus, j'aimerais ajouter quelque chose que j'ai remarqué en travaillant avec des développeurs qui n'avaient aucune idée des derniers frameworks et bibliothèques et qui étaient simplement habitués à la méthode traditionnelle de construction de sites avec des fichiers HTML, JavaScript et CSS.

#### Approche du développement

D'un côté, nous avons des utilisateurs qui s'attendent à une expérience fluide comme une application sur le web. De l'autre côté, il y a des développeurs habitués à des sites ayant des pages, chacune étant des fichiers HTML ou peut-être utilisant un peu de templating — à la base, des _sites comme des pages avec des liens internes_.

Si vous commencez avec l'un des derniers frameworks, prenons le cas de React. Vous pourriez avoir une application opérationnelle avec une configuration minimale grâce à [create-react-app](https://github.com/facebook/create-react-app). Mais si vous regardez la structure du projet, cela peut ne pas avoir beaucoup de sens pour un débutant ou même pour certains développeurs venant d'autres stacks technologiques. Le modèle est assez différent de ce que vous avez vu auparavant.

C'est parce que, sans configuration supplémentaire, ils visent à construire des Applications à Page Unique (SPA). Pour ajouter le routage, des pages ou optimiser pour le SEO, cela nécessitera plus d'outils et de configuration.

Cela ne semble pas très pratique lorsque vous voulez des sites statiques, n'est-ce pas ? Alors voici Gatsby, optimisé pour ce cas d'utilisation spécifique. Cela pourrait être plus intuitif pour les développeurs, car il y a des pages créées à partir de composants qui suivent l'idée de base que les sites sont des pages avec des liens internes.

### Fonctionnalités

#### Composants

Les composants sont une fonctionnalité clé de React, et maintenant c'est un modèle de conception web couramment suivi. Avec le niveau actuel de complexité des interfaces utilisateur, il est presque impossible d'écrire du code maintenable dans de longues pages HTML ou d'utiliser des moteurs de templating et de s'attendre à de la cohérence.

Alors, au lieu de cela, nous construisons des composants réutilisables et nous les utilisons pour construire des vues. De cette manière, nous avons des modules séparés qui gèrent des choses séparées, et il est plus facile de gérer et de maintenir. Le composant contient simplement toutes les informations dont il a besoin, et Gatsby, puisqu'il utilise React, suit le même modèle.

Le design atomique est une approche qui est une bonne façon de gérer des interfaces complexes, et nous pourrions l'utiliser ici avec des composants React. Brad Frost a un article de blog incroyable [blog post](http://bradfrost.com/blog/post/atomic-web-design/) décrivant ce que c'est et comment cela fonctionne.

#### **Bundling Webpack et outils modernes**

Webpack crée des bundles optimisés et minifiés de HTML, JavaScript et CSS. Lorsqu'il est pré-configuré avec Babel et plus de plugins, il vous permet d'utiliser le dernier JavaScript ES6+ et GraphQL.

La cerise sur le gâteau : nous avons le rechargement à chaud et le code splitting intégrés, offrant une meilleure expérience de développement et de meilleures performances du site. Cela vise à faire en sorte que le développeur écrive une configuration minimale d'outils et se concentre davantage sur le développement réel du site.

#### **Plugins Gatsby, starters et packages React**

Vous pouvez utiliser n'importe quel package que vous avez déjà utilisé avec NPM, en particulier ceux de React puisqu'il est construit sur la même base. Mais ce n'est pas tout : il existe un grand nombre de plugins, de starters et de transformateurs en constante croissance par la communauté Gatsby.

Vous n'arrivez presque jamais au point où vous devez réellement construire votre propre outil ou module, la communauté offre déjà un grand nombre pour répondre à chaque besoin.

En utilisant ceux-ci, Gatsby peut être étendu avec des fonctionnalités supplémentaires. Par exemple, quelques exemples incluent des images réactives, des fonctionnalités hors ligne, des données sources provenant de CMS et des formats de balisage de données, l'ajout de services tiers (Google Analytics, etc.), et ainsi de suite.

#### Styling

Encore une fois, des interfaces utilisateur complexes signifient des modèles de style complexes, et il n'est qu'une question de temps avant que les feuilles de style ne deviennent surchargées. Vous obtenez des problèmes de spécificité, vous faites défiler des centaines de lignes de code en essayant de comprendre les choses, et vous finissez par utiliser `!important` pour voir le style que vous avez ajouté.

Gatsby prend en charge SCSS, les bibliothèques CSS-in-JavaScript, vous permettant de gérer les styles plus facilement et avec facilité. Même la configuration pour cela est assez facile à gérer avec l'installation d'un plugin ou d'un package.

#### Images réactives

Redimensionner des images pour la réactivité sur différents appareils, le chargement paresseux, l'utilisation de `srcsets` et de `picture`... Cela semble déjà fastidieux lorsque cela doit être fait manuellement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yhkSz2qqhyRZ-HpATSQx6Q.png)
_Différentes versions de la même image pour la réactivité_

Bien que ce soit une exigence pour la performance et les interfaces optimisées comme des applications de nos jours, nous ne voyons pas beaucoup d'outils que nous pouvons utiliser directement.

Pendant ce temps, dans Gatsby, avec juste un plugin, en particulier [gatsby-plugin-sharp](https://www.gatsbyjs.org/packages/gatsby-plugin-sharp/), vous pouvez directement générer des images fluides, ajouter des filtres, changer les formats, flouter au chargement et bien plus encore. Cela économise beaucoup de travail et de temps pour redimensionner manuellement les images et écrire du code boilerplate explicite pour les images réactives. Cela vous donne également de bien meilleures performances ainsi qu'une expérience utilisateur plus fluide.

#### **Expérience comme une application**

Avec le boost de performance et les fonctionnalités qui ajoutent à la fluidité de l'expérience utilisateur, Gatsby vise une expérience complète comme une application, empruntant aux PWAs complètes. Il n'y a pas de rechargements entre les pages lorsque vous utilisez [gatsby-link](https://www.gatsbyjs.org/docs/gatsby-link/) au lieu de liens hypertextes, et l'application reste fluide et performante grâce au chargement paresseux des images et au code-splitting.

Pour les sites suivant les normes que vous souhaitez également performants, nous avons beaucoup de choses à faire et de guides à suivre : minification et bundling, mise en cache du navigateur et chargement asynchrone des scripts ou fichiers, et ainsi de suite. Lorsque vous travaillez avec un framework comme React, vous avez plus de choses à vous soucier même s'il résout quelques problèmes : code-splitting, SEO, routage si nécessaire, images réactives, et la liste est longue.

Gatsby vise à résoudre tous ces problèmes, avec moins de temps passé sur les outils, la configuration et l'environnement, et plus de temps pour concevoir et développer le site.

### L'écosystème Gatsby

#### Plugins

Gatsby a été construit pour être extensible et flexible — utiliser des plugins est un moyen de le rendre ainsi. Ils peuvent être installés directement et utilisés pour une variété de fonctionnalités, y compris rendre le site hors ligne, ajouter Google Analytics, ajouter la prise en charge des SVGs en ligne, vous l'appelez — la liste est presque sans fin.

Parmi les différents types de plugins Gatsby, les plugins gatsby-source en particulier récupèrent des données à partir d'une source locale ou distante et permettent de les utiliser via GraphQL. Ces sources pourraient être des CMS tels que WordPress, Drupal, Plone, des fichiers markdown locaux, XML ou similaires, des bases de données, des APIs et des formats de données tels que JSON, CSV.

Cela implique que presque n'importe quoi peut être utilisé comme source pour travailler avec Gatsby et générer des sites statiques.

> Note : GraphQL est un langage de requête pour les APIs qui fonctionne sur la philosophie de demander exactement ce dont vous avez besoin. Contrairement aux APIs REST, vous ne cherchez pas des endpoints pour fournir vos données et les traiter à partir de la structure donnée, mais vous demandez ce que vous voulez et utilisez directement ces données. Lisez plus sur son fonctionnement et comment l'utiliser dans leur [docs](https://graphql.org/).

Après l'installation, certains plugins peuvent être utilisés directement en les listant simplement dans `gatsby-config.js` et les autres configurés avec un objet d'options.

Allez consulter la [bibliothèque de plugins Gatsby](https://www.gatsbyjs.org/plugins/), elle contient déjà un grand nombre de plugins et d'autres sont encore ajoutés par la communauté active.

#### Starters

Ce sont essentiellement des sites Gatsby boilerplate qui vous aident à démarrer rapidement le développement en fonction du type de site. Ils vous aident à vous lancer directement dans le développement d'un site, la configuration et les fonctionnalités de base dont vous avez besoin étant déjà prises en charge. Ce qui signifie, moins de temps sur les outils, plus de temps pour le développement.

Les plugins Gatsby ont souvent leurs starters correspondants qui montrent ou servent de moyen rapide pour commencer à les utiliser. Ils servent également de référence couvrant toutes les fonctionnalités et montrent les configurations du plugin en cours d'utilisation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0EB7BqFJb70XAGAqt0LgRw.png)
_[Bibliothèque de starters Gatsby](https://www.gatsbyjs.org/starters/?" rel="noopener" target="_blank" title=")_

_Gatsby themes est une fonctionnalité encore en développement qui vous permet d'emballer et de réutiliser ces fonctionnalités et modèles similaires à ce que l'on voit dans les starters. Lisez plus sur ce qui se prépare dans le [blog Gatsby](https://www.gatsbyjs.org/blog/2018-11-11-introducing-gatsby-themes/)._

#### Sites statiques

Tout d'abord, jetons un coup d'œil à la façon dont Gatsby fonctionne en interne. Contrairement aux SPAs qui font des requêtes API lorsque vous exécutez l'application, Gatsby effectue toutes les récupérations de données, y compris les données provenant de fichiers locaux, lors de la construction. Toutes ces données sont ensuite utilisées pour générer des fichiers HTML, JavaScript et CSS statiques. Ce rendu statique est ce qui rend les choses plus rapides.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8JLlG_T6onoeW2mVjVT_Gw.png)
_Comment fonctionne Gatsby_

Cela en était beaucoup sur Gatsby, son écosystème et comment il vous aide à créer des sites statiques incroyables. Mais pourquoi voudrions-nous des sites statiques ? Cela ne semble-t-il pas être un retour en arrière par rapport aux sites dynamiques ?

* Ils ne nécessitent pas de configuration complexe de serveur avec des bases de données, de maintenance et n'ont aucun problème de mise à l'échelle.
* Les données sont entièrement sécurisées. Les CMS et les APIs ont des fonctionnalités privées, mais les données sont toujours présentes sur le serveur et peuvent être exploitées. Gatsby ne prend que les données nécessaires à afficher à partir de la source, et les données privées ou sécurisées ne sont même pas présentes dans la version finale. Ce qui est le plus sûr possible.
* Plutôt que de dépendre des serveurs pour générer des pages dynamiquement, pré-rendre toutes les pages lors de la construction et utiliser des CDNs pour une expérience ultra-rapide et fluide pour les utilisateurs du monde entier.
* Gatsby fait du rendu statique. Ce qui rend le contenu disponible en HTML et optimisé pour les moteurs de recherche, sans long temps de chargement initial.

#### Essayez-le !

Cela devrait avoir éclairé ce qui est toute cette hype autour et pourquoi certaines grandes entreprises choisissent de l'utiliser sur leurs sites. La [vitrine des sites Gatsby](https://www.gatsbyjs.org/showcase/) semble simplement croître avec de nombreuses additions incroyables ces derniers temps.

Peut-être est-il temps que vous mettiez la main à la pâte et que vous jetiez un coup d'œil autour !

Grâce à [CodeSandbox](https://codesandbox.io), nous pouvons faire cela tout de suite, dans le navigateur lui-même.

Si vous souhaitez l'exécuter localement, vous devriez consulter [gatsby-cli](https://www.gatsbyjs.org/docs/). C'est le moyen le plus rapide et le plus facile de commencer. Ils ont également une documentation et des tutoriels incroyables pour vous lancer dans le développement de sites sur [gatsbyjs.org](https://www.gatsbyjs.org/docs/).

_J'espère que vous avez apprécié cet article et que vous l'avez trouvé utile. Vous pouvez consulter tous mes projets sur [Github](http://github.com/ajayns/) ou [Dribbble](https://dribbble.com/ajayns) et n'hésitez pas à me contacter sur [Twitter](https://twitter.com/ajayns08) !_

_Vous pourriez également aimer consulter mes autres articles :_

[**Progressive Web Apps: Bridging the gap between web and mobile apps**](https://medium.freecodecamp.org/progressive-web-apps-bridging-the-gap-between-web-and-mobile-apps-a08c76e3e768)  
[_Unless youve been living under a rock, youve probably heard of PWAs or Progressive Web Apps. Its a hot topic rightmedium.freecodecamp.org](https://medium.freecodecamp.org/progressive-web-apps-bridging-the-gap-between-web-and-mobile-apps-a08c76e3e768)[**Hackathon Report: What can you code in 30 hours? Quite a lot!**](https://medium.freecodecamp.org/hackathon-report-what-can-you-code-in-30-hours-quite-a-lot-ffd7224c9745)  
[_What can you build in 30 hours straight? As a group of second year college students with a growing portfolio of workmedium.freecodecamp.org](https://medium.freecodecamp.org/hackathon-report-what-can-you-code-in-30-hours-quite-a-lot-ffd7224c9745)[**ACM Month Of Code 2k17: Building Moodify**](https://hackernoon.com/acm-month-of-code-2k17-building-moodify-d5d9e0c52ca7)  
[_March was a pretty productive month, all thanks to this major event hosted by Association for Computing Machinery, NIThackernoon.com](https://hackernoon.com/acm-month-of-code-2k17-building-moodify-d5d9e0c52ca7)