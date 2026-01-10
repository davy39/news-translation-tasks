---
title: Comment votre site Gatsby peut obtenir un score parfait sur Google Lighthouse
  après la mise à jour de la version 6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-28T14:24:10.000Z'
originalURL: https://freecodecamp.org/news/gatsby-perfect-lighthouse-score
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/header-image.png
tags:
- name: Gatsby
  slug: gatsby
- name: Lighthouse
  slug: lighthouse
- name: React
  slug: react
- name: SEO
  slug: seo
- name: web performance
  slug: web-performance
seo_title: Comment votre site Gatsby peut obtenir un score parfait sur Google Lighthouse
  après la mise à jour de la version 6
seo_desc: "By Erik Larsson\nGoogle Lighthouse is the free, go-to SEO tool for determining\
  \ your website's overall health. \nEnter your URL, and Google Lighthouse will score\
  \ the performance metrics of your website, including page-speed, accessibility,\
  \ best-practice..."
---

Par Erik Larsson

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) est l'outil SEO gratuit et incontournable pour déterminer la santé globale de votre site web. 

Entrez votre URL, et Google Lighthouse évaluera les *métriques de performance* de votre site web, y compris la vitesse de la page, l'accessibilité, les meilleures pratiques et le SEO sur la page.

Avec la sortie de **Lighthouse version 6** plus tôt cette année, de nombreux développeurs ont **observé une baisse drastique** des métriques de performance de leurs sites web.

Cela a été particulièrement choquant pour la communauté de développeurs utilisant le framework populaire basé sur React, GatsbyJS, loué pour sa vitesse et ses performances.

En tant que développeur GatsbyJS moi-même, j'ai également été perplexe. Nous avions l'habitude de voir ces belles notes vertes de performance de 90+, sans beaucoup d'efforts de notre part.

Après la mise à jour de la version 6, cependant, notre site est passé dans l'orange, descendant à 60 points ! Et certains d'entre nous ont même connu des scores rouges, [inférieurs à 40 points](https://github.com/gatsbyjs/gatsby/issues/24332).

Je souhaite partager avec vous **les étapes que j'ai suivies afin de retrouver un score parfait de 100 sur Google Lighthouse**.

## Étape 1. La solution rapide et facile : passer à Preact
Avec la [sortie de Lighthouse version 6](https://web.dev/lighthouse-whats-new-6.0/), trois nouvelles métriques de performance ont été introduites : Largest Contentful Paint (LCP), Cumulative Layout Shift (CLS) et Total Blocking Time (TBT).

Après avoir parcouru le [dépôt GitHub de Gatsby](https://github.com/gatsbyjs/gatsby), ainsi que la documentation de Lighthouse, il est devenu clair que le *Total Blocking Time* (TBT) était le principal responsable de la baisse des scores de performance pour de nombreux sites.

Le [Total Blocking Time](https://web.dev/tbt/) (TBT) est défini comme le *temps total entre le First Contentful Paint (FCP) et le Time to Interactive (TTI)*. 

En termes simples, le TBT est une mesure de la durée pendant laquelle le *thread principal* du navigateur est bloqué par des tâches longues, telles que l'analyse de JavaScript (JS).

Cela dit, toute mesure prise pour réduire la quantité de JS, ainsi que le temps d'exécution de JS, aura un impact positif sur les performances du site en réduisant le TBT.

Preact est une alternative petite (3 ko) et [rapide à React](https://preactjs.com/). Et grâce à [gatsby-plugin-preact](https://www.gatsbyjs.com/plugins/gatsby-plugin-preact/), passer votre site Gatsby de React à Preact est incroyablement facile.

Accédez à la racine de votre projet et installez les packages suivants en utilisant NPM :

    npm install --save gatsby-plugin-preact preact preact-render-to-string

...ou Yarn :

    yarn add gatsby-plugin-preact preact preact-render-to-string

Ensuite, ajoutez simplement

    ...
    `gatsby-plugin-preact`,
    ...
    
à votre fichier gatsby-config.js

Ensuite, exécutez

    yarn gatsby build
    
Si vous utilisez le [webpack bundle analyzer](https://www.gatsbyjs.com/plugins/gatsby-plugin-webpack-bundle-analyser-v2/), vous devriez maintenant voir une taille de bundle réduite d'environ 100 ko ! Pas mal, n'est-ce pas.

Découvrez la différence que ce changement a apportée à la taille de notre bundle dans l'image ci-dessous.

![La différence de taille de bundle entre React et Preact](https://www.freecodecamp.org/news/content/images/2020/09/preact-2.PNG)
_Une diminution de 8 pour cent de la taille du bundle pour une ligne de code - pas mal !_

Passer à Preact devrait augmenter votre score de performance d'environ **5 à 10 points**.

## Étape 2. Reconsidérez la nécessité de l'*image héroïque*
Une autre métrique qui a fait baisser les performances de notre site, [SmartRate](https://www.smartrate.se/), était le [Largest Contentful Paint](https://web.dev/lcp/) (LCP).

Le LCP est une métrique pour mesurer la *vitesse de chargement perçue*. Et avec le Total Blocking Time, le LCP et le TBT représentent 50 % du score total de performance de Lighthouse.

Avec cela en tête, ce n'est pas une grande surprise qu'une image couvrant 80 pour cent de la partie visible de la page ait un impact négatif sur la métrique LCP, même lorsqu'elle est optimisée en utilisant le format webp.

Nous avons ajusté l'image héroïque et obtenu un succès partiel en désactivant le fondu et en changeant le chargement du paramètre par défaut (lazy) à eager :

    <Img fadeIn="false" loading="eager" src={heroImage} />

Cependant, les améliorations étaient seulement marginales et à peine perceptibles dans Lighthouse (environ 2 à 4 points), nous avons donc décidé de nous regrouper et de repenser.

Quel était *vraiment* le but de notre image héroïque ?

L'image héroïque est couramment utilisée pour attirer l'attention de l'utilisateur et transmettre un message central pour renforcer votre marque. 

Dans notre cas, cependant, ce n'est pas ainsi que nous utilisons *la partie visible de la page*.

![Une capture d'écran de la page d'accueil de SmartRate](https://www.freecodecamp.org/news/content/images/2020/09/www.smartrate.se_-Desktop-monitor--1.png)
_Une capture d'écran de la partie visible de la page telle qu'elle apparaît aujourd'hui, montrant l'unité héroïque et la zone de saisie utilisateur._

Comme vous pouvez le voir sur l'image, *la partie visible de la page* est dédiée à la *saisie utilisateur*. Et l'image héroïque que nous utilisions avant celle actuelle était simplement une photo floue afin de donner une certaine ambiance à la partie visible de la page.

Après un peu de réflexion, nous avons réalisé que nous ne pouvions pas justifier l'utilisation d'une image héroïque, étant donné l'impact négatif qu'elle avait sur nos métriques de performance.

Au lieu de cela, inspirés par des sites tels que [Spotify.com](https://www.spotify.com), nous avons décidé d'opter pour un fond SVG.

**Cette seule décision a réduit la taille du chargement initial de la page de 65 ko !**

D'une image webp optimisée de ~67 ko à un simple SVG de 2 ko pour le même espace.

En découvrant que cette solution résolvait complètement nos problèmes avec la métrique LCP, nous avons rapidement abandonné l'idée d'utiliser une *image héroïque* sur notre page secondaire la plus importante, [f6retagsl5n](https://www.smartrate.se/foretagslan/) - prêts aux entreprises - également.

![Une capture d'écran de la sous-page SmartRate j4mf6r f6retagsl5n](https://www.freecodecamp.org/news/content/images/2020/09/www.smartrate.se_foretagslan_-Desktop-monitor--1.png)
_Conception actuelle de la sous-page utilisant une unité héroïque (bien que pas une image héroïque)_

Pour cela, et nos autres sous-pages, nous avons opté pour un dégradé CSS subtil à trois couleurs, pour faire ressortir le *message héroïque*.

Cette solution n'était peut-être pas aussi élégante que l'utilisation d'une image sur mesure, mais elle a fait l'affaire et a grandement amélioré le LCP pour nos sous-pages également.

Ce qui m'amène à...

### Considérations clés si votre site utilise une image héroïque
Abandonner l'image héroïque au profit d'un fond SVG ou CSS résoudra, selon notre expérience, les problèmes causés par un faible score LCP.

Cependant, selon le but de votre unité héroïque, cette solution peut ne pas être optimale pour vous.

Alors, avant de décider quoi faire, vous devriez considérer quelques points :

- L'image héroïque est-elle **personnalisée** pour votre site **ou une photo de stock** ?
- L'image héroïque **ajoute-t-elle de la valeur** à votre marque ?
- Quel est le but de la partie visible de la page sur **votre site** ?

Si votre image héroïque ajoute une grande valeur de marque à votre site, peut-être que le compromis pour de meilleures performances n'en vaut simplement pas la peine.

Cependant, si vous êtes prêt à essayer mes suggestions, vous serez heureux d'apprendre les ressources suivantes.

### Excellentes ressources pour les fonds SVG
Ci-dessous, j'ai compilé une courte liste de ressources et d'outils précieux pour quiconque souhaite passer de l'utilisation d'une image héroïque à l'utilisation de motifs SVG/CSS :

- [Hero Patterns](https://www.heropatterns.com/) par Steve Schoger
   Un excellent outil fournissant plusieurs motifs SVG personnalisables.

- [SVG Patterns](https://philiprogers.com/svgpatterns/) par Philip Rogers
   Une autre galerie de motifs SVG gratuits.

- [SVGOMG](https://jakearchibald.github.io/svgomg/) par Jake Archibald
   Une excellente ressource gratuite pour minifier les fichiers SVG. Tout est question de réduire ces ko, n'est-ce pas ?

L'étape suivante est un peu plus situationnelle, mais sera, pour ceux d'entre vous qui utilisent une bibliothèque d'interface utilisateur, toujours *très pertinente*. Pour nous, cette étape était tout aussi importante que les deux premières étapes pour améliorer nos métriques.

## Étape 3. Abandonner Material UI pour TailwindCSS
Permettez-moi de dire, d'emblée, que je suis un grand, grand fan de [Material UI](https://material-ui.com/). Et je ne suis pas le seul à penser ainsi. Jusqu'à récemment, MUI a été la bibliothèque d'interface utilisateur React la plus populaire sur GitHub (actuellement en deuxième position).

Lorsque nous avons commencé à développer notre site, la conception était entièrement basée sur les composants MUI.

Le seul problème était, *qu'il ralentissait les performances du site*.

Beaucoup.

Surtout pour les utilisateurs mobiles.

Après la sortie de Lighthouse version 6, nous n'avons tout simplement pas pu obtenir des notes de performance mobile supérieures à 70 points, en raison d'un *Total Blocking Time* (TBT) très élevé. 

Au début, rien de ce que nous avons fait ne semblait avoir d'importance. Nous avons même essayé le fractionnement de code en utilisant [Loadable Components](https://loadable-components.com/docs/code-splitting/), et le chargement paresseux des charges utiles non essentielles.

Cependant, après quelques recherches, **nous avons identifié Material UI comme la source de la baisse de performance**.

Lors du rendu de la page, les calculs de mise en page (et les recalculs) semblaient se produire partout, ce qui contribuait à un TBT accru.

Nous avons commencé à supprimer les composants MUI, *un par un*, mais cela a peu amélioré les performances.

Enfin, nous n'avions plus qu'un seul composant MUI, et un site web presque propre.

Et nous avions toujours des notes de performance faibles.

**Comment cela pouvait-il être ?**

Eh bien, comme il s'est avéré, importer un seul composant MUI ferait entrer toute la bibliothèque Material UI dans le bundle. Et le chargement de la page d'accueil nécessiterait que l'utilisateur télécharge l'intégralité du CSS et du JS de Material UI.

**Mais qu'en est-il du [tree-shaking](https://webpack.js.org/guides/tree-shaking/) ?**

Eh bien, à cela, je ne peux répondre que nous avons suivi [les recommandations de MUI](https://material-ui.com/guides/minimizing-bundle-size/) pour minimiser la taille du bundle. Nos efforts, cependant, n'ont pas porté leurs fruits.

En supprimant la dernière importation de MUI, nous avons remarqué **une baisse impressionnante de ~170 ko de la taille du bundle !**

Enfin, les performances de notre site ont grimpé dans le vert, à plus de 90 points, *même sur mobile !*

Le TBT était maintenant inexistant, mais il en était de même pour la mise en page de notre site web.

Nous avons donc commencé à chercher des alternatives, et je me suis souvenu d'avoir [lu sur l'intégration de TailwindCSS dans Gatsby](https://www.gatsbyjs.com/docs/tailwind-css/) quelque temps plus tôt.

Une phrase a attiré mon attention : *"Purger votre CSS"*.

[PurgeCSS](https://purgecss.com/), qui est maintenant intégré à TailwindCSS, fait exactement ce que vous pensez qu'il fait - il supprime le CSS inutilisé !

Parfait.

![Image illustrant le passage de Material UI à TailwindCSS](https://www.freecodecamp.org/news/content/images/2020/09/muitotailwindpostcss-1.png)
_En passant de Material UI à TailwindCSS, nous avons pu obtenir un design de type material avec un excellent score de performance._

Suivre simplement le [guide d'installation de Tailwind dans la documentation de Gatsby](https://www.gatsbyjs.com/docs/tailwind-css/) a suffi pour nous lancer. Nous avons lentement commencé à concevoir des composants de type material en utilisant Tailwind via PostCSS.

Pas tout à fait aussi beaux que les composants MUI, mais pas loin. Étant donné l'énorme boost de performance, *cela en valait totalement la peine*.

Pour des débutants complets, je dois dire que concevoir des composants en utilisant **Tailwind est surprenamment intuitif**. On s'y habitue rapidement.

### Reconnexion à la première étape
Un autre petit avantage d'utiliser Preact plutôt que React est la possibilité d'utiliser le paramètre class au lieu du paramètre className (qui fonctionne toujours). Cela rend la conception des composants un peu plus rapide - surtout lors de la copie de markdown depuis leur [site officiel](https://tailwindcss.com/docs/installation).

Si vous décidez d'abandonner Material UI, Bootstrap, ou toute autre bibliothèque d'interface utilisateur basée sur React en faveur de Tailwind, vous serez heureux d'apprendre les ressources suivantes :

- [Tailwind UI](https://tailwindui.com/preview) Créé par les créateurs de TailwindCSS, Tailwind UI est un dépôt où vous pouvez trouver de beaux composants préconçus. Certains d'entre eux peuvent être utilisés gratuitement.
- [Tailwind Components](https://tailwindcomponents.com/) est un dépôt de composants Tailwind gratuits créés par la communauté.

## Conseil bonus : Gérez la taille de votre bundle à l'avenir
Comme vous pouvez probablement l'imaginer, optimiser la taille du bundle et reconstruire l'intégralité de l'interface utilisateur de notre site a été assez éprouvant. Si j'ai appris une leçon importante pendant ce processus, c'est celle-ci :

**Surveillez la taille du bundle !**

Alors que nous devenions de plus en plus conscients de l'impact de la taille du bundle sur les performances de notre site, nous avons découvert un outil appelé **[bundlephobia](https://bundlephobia.com/)**.

![Une capture d'écran de la page d'accueil de Bundlephobia](https://www.freecodecamp.org/news/content/images/2020/09/bundlephobia1-1.PNG)
_Page d'accueil de Bundlephobia._

Cet excellent outil vous permettra de *"trouver le coût de l'ajout d'un package npm à votre bundle"*. Non seulement cela, mais il vous montrera des packages similaires, et comment ils se comparent en taille à celui que vous consultez actuellement.

Cela a été vraiment utile pour nous lorsque nous avons développé la sous-page [bol5n](https://www.smartrate.se/bolan/) (taux hypothécaires). Nous avions besoin d'une bibliothèque de graphiques qui nous permettrait d'assembler plusieurs graphiques en ligne, montrant les taux hypothécaires moyens des plus grandes banques de Suède au cours des douze derniers mois.

Nous n'avons pas trouvé d'autre site faisant cela, nous avons donc pensé que ce serait un excellent service gratuit à offrir à nos visiteurs.

Cependant, plus sages des expériences précédentes, nous n'étions pas enthousiastes à l'idée d'utiliser simplement la première bibliothèque de graphiques qui se présentait à nous.

En utilisant bundlephobia, nous avons comparé la taille du bundle de différentes bibliothèques de graphiques et avons découvert que, selon nos besoins, [chartist.js](https://gionkunz.github.io/chartist-js/) serait suffisant pour nous.

![Une capture d'écran de Bundlephobia montrant des bibliothèques similaires à Chartist.js](https://www.freecodecamp.org/news/content/images/2020/09/bundlephobia2.PNG)
_Bundlephobia montrant des bibliothèques similaires (et leur taille de package respective) à chartist.js_

![Un graphique en ligne](https://www.freecodecamp.org/news/content/images/2020/09/bolaneranta-genomsnitt.png)
_Et une image des graphiques en ligne résultants montrant les taux hypothécaires historiques._

Si notre besoin était simplement d'afficher des graphiques en ligne interactifs, pourquoi payer plus que nécessaire ?

En d'autres termes, si nous avons la possibilité d'obtenir la fonction souhaitée avec un impact minimal sur les performances, cette option devrait être notre choix par défaut.

Cependant, il est également important de reconnaître que les décisions entre le design et les performances impliquent presque toujours un compromis. *Et ce compromis devrait être considéré avec sagesse*.

**Notre priorité était la performance, comme le montrent les résultats ci-dessous :**

![Image montrant un score presque parfait sur Lighthouse](https://www.freecodecamp.org/news/content/images/2020/09/100perfectscore-1.PNG)
_Un score presque parfait sur Google Lighthouse ! Seulement deux points de moins sur l'accessibilité en raison d'un ratio de contraste trop faible sur certains boutons. Mais après tout, le design doit prévaloir quelque part, n'est-ce pas ?_

Dans cet article, nous avons couvert **les étapes que nous avons suivies afin d'obtenir un score presque parfait sur Google Lighthouse**, en :
- Améliorant la métrique *Total Blocking Time* en passant de React à Preact 
- Améliorant la métrique *Largest Contentful Paint* en optimisant les paramètres de l'image héroïque, ou en remplaçant l'image héroïque par un motif SVG
- Améliorant la métrique *Total Blocking Time* en passant de Material UI à TailwindCSS, et en supprimant le CSS inutilisé en utilisant PurgeCSS
- Réduisant la taille globale du bundle

J'espère vraiment que les leçons que nous avons apprises vous inspireront et vous bénéficieront également !