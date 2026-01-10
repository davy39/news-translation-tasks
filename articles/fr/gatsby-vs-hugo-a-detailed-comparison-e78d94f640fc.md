---
title: Gatsby vs Hugo, une comparaison détaillée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-28T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/gatsby-vs-hugo-a-detailed-comparison-e78d94f640fc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Qrk2M5aQ_J6Gtt-WZBrnGA.jpeg
tags:
- name: GatsbyJS
  slug: gatsbyjs
- name: Hugo
  slug: hugo
- name: React
  slug: react
- name: Static Site Generators
  slug: static-site-generators
- name: Web Development
  slug: web-development
seo_title: Gatsby vs Hugo, une comparaison détaillée
seo_desc: 'By David

  In this article, I compare two static site generators, Gatsby and Hugo. I discuss
  framework familiarity, stability, security, tooling, build speed, performance and
  the community surrounding both. So let’s get started.

  About a year ago, I cha...'
---

Par David

Dans cet article, je compare deux générateurs de sites statiques, Gatsby et Hugo. Je discute de la familiarité avec le framework, de la stabilité, de la sécurité, des outils, de la vitesse de construction, des performances et de la communauté entourant les deux. Alors commençons.

Il y a environ un an, j'ai changé [mon site web](https://learnitmyway.com/) de Wordpress à [Hugo](http://gohugo.io/), qui est un générateur de site statique écrit en Go utilisant les bibliothèques de modèles de Go pour les templates. J'ai récemment fait une évaluation de la viabilité de [Gatsby](https://www.gatsbyjs.org/), un autre générateur de site statique écrit en React utilisant React pour les templates.

Dans cet article, je compare les différences entre Hugo v0.42 et Gatsby v1.93. Pour la comparaison, j'ai utilisé [ce site Hugo](https://learnitmyway-hugo.netlify.com/) et [ce site Gatsby](http://learnitmyway-gatsby.netlify.com/). Le code pour chacun peut être trouvé sur Github pour [le site Hugo](https://github.com/DeveloperDavo/learnitmyway/tree/gatsby-vs-hugo) et pour [le site Gatsby](https://github.com/DeveloperDavo/learnitmyway-gatsby).

#### Familiarité avec le framework

Si vous n'êtes pas familier avec React et que vous ne prévoyez pas d'apprendre React, alors vous devriez probablement choisir Hugo. Si vous connaissez et aimez React, devriez-vous choisir Gatsby ? Eh bien, pas nécessairement.

Je soutiendrais que vous avez besoin d'une compréhension décente de React (voir [Apprendre React avec ces ressources](https://learnitmyway.com/learn-react-with-these-resources/)) si vous voulez utiliser Gatsby. Et afin de comprendre React, vous avez besoin d'une compréhension décente de JavaScript (voir [Apprendre JavaScript avec ces ressources](https://learnitmyway.com/learn-javascript-with-these-resources/)).

Même si j'utilise Hugo depuis presque un an, il n'a pas été nécessaire pour moi de comprendre Go. J'ai également seulement dû apprendre un peu sur les bibliothèques de modèles de Go. Cependant, j'ai trouvé que je devais me référer à la documentation plus souvent avec Hugo en raison de mon manque de familiarité. Gatsby nécessite une compréhension plus approfondie de React que ce que Hugo attend de Go. Néanmoins, si la familiarité avec le framework était le seul critère, je choisirais Gatsby car c'est agréable de ne pas avoir à se référer à la documentation tout en ajoutant de nouvelles fonctionnalités à mon site web.

#### Stabilité

Une façon d'évaluer la stabilité serait de comparer [les problèmes de Hugo sur GitHub](https://github.com/gohugoio/hugo/issues) avec [les problèmes de Gatsby sur GitHub](https://github.com/gatsbyjs/gatsby/issues). Vous verrez que Gatsby a plus de fonctionnalités (ce qui est excitant), mais aussi plus de bugs (ce qui est moins excitant). Initialement, je n'ai pas considéré la stabilité comme un critère jusqu'à ce que je trouve [ce bug](https://github.com/gatsbyjs/gatsby/issues/6392) et cela m'a fait réaliser l'importance de la stabilité dans les logiciels. Je prends peut-être cela personnellement à cause du temps et des efforts que j'ai consacrés à essayer de trouver ce bug, mais je pense toujours que Hugo est plus stable que Gatsby.

#### Sécurité

Gatsby utilise JavaScript, et les applications JavaScript sont notoires pour nécessiter beaucoup de modules Node pour fonctionner. Il existe même un module Node qui [envoie des tweets sur Hot Pocket](https://medium.com/@jdan/i-peeked-into-my-node-modules-directory-and-you-wont-believe-what-happened-next-b89f63d21558) et un autre qui [récolte des numéros de carte de crédit](https://hackernoon.com/im-harvesting-credit-card-numbers-and-passwords-from-your-site-here-s-how-9a8cb347c5b5) :D. Les sites statiques tendent à être plus sécurisés par nature, mais je pense qu'il vaut la peine de mentionner que plus de dépendances entraînent plus de code auquel vous ne faites peut-être pas confiance.

#### Outils

Gatsby a tous les avantages de la [chaîne d'outils JavaScript](https://www.npmjs.com/search?q=Gatsby) et tous les inconvénients de la [fatigue JavaScript](https://medium.com/@ericclemmons/javascript-fatigue-48d4011b6fc4). En plus de cela, Gatsby a une bibliothèque de plugins vraiment agréable. En particulier, [gatsby-plugin-offline](https://github.com/gatsbyjs/gatsby/tree/master/packages/gatsby-plugin-offline) m'a permis d'ajouter facilement des capacités hors ligne à mon site web, ce que je n'ai pas encore réussi à faire avec Hugo.

D'un autre côté, certaines choses qui nécessitent un plugin avec Gatsby sont simplement disponibles avec Hugo. Par exemple, [gatsby-plugin-react-helmet](https://github.com/gatsbyjs/gatsby/tree/master/packages/gatsby-plugin-react-helmet) est nécessaire pour éditer la balise head, alors que cela peut être fait avec du simple HTML dans Hugo. Comme j'ai apprécié utiliser les outils qui accompagnent Gatsby, je donne ce point à Gatsby.

#### Vitesse de construction

Hugo est capable de construire mon site web sans aucun outil supplémentaire en moins de 100 ms. Gatsby est capable de construire mon site web en environ 15 secondes, mais cela inclut beaucoup d'outils supplémentaires. L'ajout de [PostCSS](https://github.com/postcss/postcss) et [Imagemin](https://github.com/imagemin/imagemin) à la construction de Hugo porte le temps de construction à environ 5 secondes. La surveillance des changements pendant le développement était également plus rapide avec Hugo. Je pense que Hugo est le gagnant ici.

#### Documentation

Gatsby et Hugo ont tous deux une documentation vraiment agréable. Hugo a un [Guide de démarrage rapide](https://gohugo.io/getting-started/quick-start/) et Gatsby a une section [Premiers pas](https://www.gatsbyjs.org/docs/). Gatsby a également un [tutoriel](https://www.gatsbyjs.org/tutorial/) vraiment agréable, ce qui compense la courbe d'apprentissage plus raide. Personnellement, j'ai trouvé plus facile de commencer avec Gatsby, mais c'est parce que je comprenais déjà React. Je pense qu'il est juste de dire que Hugo et Gatsby ont tous deux une excellente documentation.

#### Performance

En utilisant [Lighthouse](https://developers.google.com/web/tools/lighthouse/), le score de performance était de 100 pour mon site en Hugo et de 95 pour mon site en Gatsby. Le First Contentful Paint pour une connexion 3G était d'environ 1 seconde pour le site Hugo et de 1,5 seconde pour le site Gatsby. En utilisant [Web Page Test](https://www.webpagetest.org/), le temps de chargement sur une connexion 2G était de [8,7 secondes en Hugo](https://www.webpagetest.org/result/180722_Y6_19710626850f2326f4610b156398dbf0/) et de [11,7 secondes en Gatsby](https://www.webpagetest.org/result/180722_PJ_fa010df1c51f603586ee9c04f2abd558/).

Cependant, en effectuant un simple test manuel pour voir quel site se charge en premier, Gatsby était nettement plus rapide, donc je ne comprends pas vraiment ce que Lighthouse ou Web Page Test mesuraient. De plus, comme Gatsby est une application monopage, la navigation au sein du site web ne nécessite pas de demande au serveur. Les pages sont simplement réaffichées avec JavaScript. En tout cas, je peux dire avec certitude que Hugo et Gatsby sont tous deux rapides. Je serais intéressé d'entendre vos réflexions dans les commentaires ci-dessous.

#### Communauté

Gatsby gagne rapidement en popularité, ce qui s'accompagne d'une communauté florissante. Cela ne signifie pas que la communauté de Hugo est ennuyeuse. Si les étoiles GitHub sont un indicateur, Hugo en a plus de 27 mille et Gatsby plus de 23 mille. Sur Twitter, Gatsby semble être plus actif que Hugo.

#### Réflexions finales

Alors, lequel devriez-vous choisir ? Gatsby utilise React, avec lequel je suis plus familier, il a de meilleurs outils et une communauté florissante. D'un autre côté, Hugo est plus stable et passe moins de temps à construire. Pour les sites web plus grands, les vitesses de construction deviennent plus importantes et certains d'entre vous pourraient ne pas du tout aimer React. Dans mon cas, la stabilité était le critère le plus important, donc j'ai décidé de rester avec Hugo. Je suis très enthousiaste de voir ce que l'avenir nous réserve dans cet espace.

---

**Avant de partir...** Merci d'avoir lu l'article ! J'écris sur mes expériences professionnelles et éducatives en tant que développeur logiciel autodidacte, alors consultez [mon blog](https://www.learnitmyway.com/) ou abonnez-vous à [ma newsletter](https://learnitmyway.com/newsletter) pour plus de contenu.

**Vous pourriez aussi aimer :**

* [Comment je publie des mises à jour sur mon site personnel](https://learnitmyway.com/how-i-release-updates-to-my-personal-website/)
* [Matériel d'apprentissage — développement logiciel](https://www.learnitmyway.com/2016/11/11/learning-material-software-development/) (une liste de ressources d'apprentissage, commençant par l'Introduction à l'informatique)
* [Le développement web full-stack vaut-il la peine d'être appris ?](https://learnitmyway.com/opinion-full-stack/)