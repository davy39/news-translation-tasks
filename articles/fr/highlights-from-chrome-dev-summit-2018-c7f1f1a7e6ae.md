---
title: Points forts du Chrome Dev Summit 2018
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T16:53:21.000Z'
originalURL: https://freecodecamp.org/news/highlights-from-chrome-dev-summit-2018-c7f1f1a7e6ae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6QoOuhbOMjuUbJtzDXg-Dw.png
tags:
- name: Google Chrome
  slug: chrome
- name: Google
  slug: google
- name: performance
  slug: performance
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Points forts du Chrome Dev Summit 2018
seo_desc: 'By Chiamaka Ikeanyi

  Have you heard of Google Chrome Dev Summit? If you haven’t heard of it and the awesome
  cool things Chrome engineers have been working on lately, this article is for you.

  I’m a front-end engineer working on an application that serv...'
---

Par Chiamaka Ikeanyi

Avez-vous entendu parler du Google Chrome Dev Summit ? Si vous n'en avez pas entendu parler et des choses cool et géniales sur lesquelles les ingénieurs Chrome ont travaillé récemment, cet article est pour vous.

Je suis ingénieure front-end travaillant sur une application qui sert des millions d'utilisateurs. J'utilise également Chrome Dev Tools tous les jours pour déboguer et surveiller les performances. J'ai donc trouvé impératif d'apprendre les outils et technologies qui m'aideront à optimiser mes applications et à contribuer à la construction d'un meilleur web. Le débogage et les optimisations deviennent plus faciles lorsque vous connaissez les outils à utiliser et les métriques à surveiller.

Le Chrome Dev Summit m'a offert l'opportunité d'entendre parler des mises à jour de ces outils et technologies, et m'a montré des moyens de contribuer à l'amélioration de ces outils. J'ai beaucoup appris des ingénieurs Chrome lors du sommet, et je voudrais que vous profitiez de ces connaissances afin que nous puissions construire ensemble une expérience web géniale.

Le Chrome Dev Summit est une opportunité pour les ingénieurs de Google Chrome et les principaux développeurs web de célébrer la plateforme web, de fournir des mises à jour sur leurs derniers travaux et de recevoir des retours de la communauté.

Cette année, des développeurs du monde entier se sont réunis au Yerba Buena Center for the Arts à San Francisco, en Californie, pour une exploration de deux jours (12 et 13 novembre) des expériences web modernes. Il a été célébré en grande pompe alors que les ingénieurs Chrome marquent le 10e anniversaire de la sortie de Google Chrome, le navigateur web le plus utilisé.

L'événement s'est concentré sur ce que signifie construire une expérience web rapide et de haute qualité en utilisant les technologies web modernes et les meilleures pratiques, ainsi que sur l'examen des nouvelles capacités passionnantes à venir sur la plateforme web. Les principaux points forts sont résumés ci-dessous.

### Budgets de performance

Un nombre croissant de fonctionnalités dans les applications web aujourd'hui sont également accessibles via des appareils bas de gamme sur des réseaux à haute latence. Pour cette raison, JavaScript devient [coûteux](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4), nécessitant ainsi un [budget de performance](https://addyosmani.com/blog/performance-budgets/).

![Image](https://cdn-media-1.freecodecamp.org/images/6SHRW7kkfPoPjCqDLD2Jjy3C-exGXkSjt76n)
_Un budget de performance est un cadre qui permet de déterminer quels changements représentent un progrès et quels changements représentent une régression, en tenant compte d'un ensemble de métriques partagées et de budgets pour chaque action rendue actionnable_

Cependant, nous devons avoir des métriques en place pour mesurer avant de pouvoir nous améliorer, car il est impossible de mesurer ce que nous ne suivons pas. Lorsque nous nous soucions de l'expérience utilisateur exceptionnelle, indépendamment des conditions de l'appareil ou du réseau, [la construction d'une PWA](https://developers.google.com/web/progressive-web-apps/) avec la performance à l'esprit devient une priorité.

Pour construire une expérience web de haute qualité, Google a développé des outils comme Lighthouse, PageSpeed Insights et Chrome User Experience Report (CrUX) pour aider les développeurs à surveiller et à améliorer la plateforme web. Une nouvelle interface utilisateur de Lighthouse a été annoncée lors de l'événement avec PWA Refactor, une réduction du temps d'exécution de Lighthouse et un nouveau système de notation.

![Image](https://cdn-media-1.freecodecamp.org/images/5bUg2is4JueISZ1rZOyjz8p3DXl2WtfYfom1)
_Le nouveau système de notation de Lighthouse_

Nous pouvons également [intégrer Lighthouse](https://github.com/ebidel/lighthouse-ci) à notre flux de développement afin qu'il s'exécute à chaque commit. Cela nous aide à garder un œil sur les performances.

![Image](https://cdn-media-1.freecodecamp.org/images/eLG9CubQr2dDiVYrSjRcGIa1HDjYg-geIqd-)
_Exécution de Lighthouse en CI_

Outils pour aider à surveiller le coût des packages :

* [Webpack Bundle Analyzer](https://www.npmjs.com/package/webpack-bundle-analyzer) qui crée une visualisation en treemap du contenu de vos bundles. Il aide à déterminer les modules qui composent la majeure partie de sa taille.
* [Bundlephobia](https://bundlephobia.com/) aide à découvrir le coût de l'ajout d'un package npm à votre bundle.
* [Bundlesize](https://www.npmjs.com/package/bundlesize) aide à garder la taille de votre bundle sous contrôle. Vous pouvez l'intégrer de manière à ce que les PR ne puissent pas être fusionnées une fois que la taille du bundle est supérieure à la taille maximale cible.

![Image](https://cdn-media-1.freecodecamp.org/images/WBTc5rwOOoi7FlOIChBRQVNhfL2DGhg9Hw-U)
_Vérifications de la taille du bundle dans le processus CI_

### PageSpeed Insights alimenté par Lighthouse

En raison des résultats d'analyse variables obtenus de PageSpeed Insights et Lighthouse lors de la mesure des performances des sites web, l'équipe Chrome a introduit PageSpeed API v5. Il s'agit essentiellement de Lighthouse API v1 pour alimenter PageSpeed Insights. Cela signifie que les résultats divergents seront de l'histoire ancienne. PageSpeed Insights intègre également les données de terrain fournies par le [CrUX](https://developers.google.com/web/tools/chrome-user-experience-report/).

```
await fetch(`https://www.googleapis.com/pagespeedonline/v5/runPagespeed?&url=${url}`)
```

![Image](https://cdn-media-1.freecodecamp.org/images/f33Kx7eVWw0tMDTIXVoDXbuUUzhpcYLRLhCv)
_Par [Paul Irish](undefined" rel="noopener" target="_blank" title=") et Elizabeth Sweeny au Chrome Dev Summit_

### Premier délai d'entrée

Nous sommes familiers avec la mesure de l'indice de vitesse (SI), de la première peinture de contenu (FCP), du temps jusqu'à l'interactivité (TTI), du premier temps d'inactivité du CPU (FCPI) et d'autres métriques que vous avez peut-être vues en utilisant [Lighthouse](https://developers.google.com/web/tools/lighthouse) ou [WebPageTest](https://www.webpagetest.org). Pour aider à mesurer la première impression d'un utilisateur sur l'interactivité et la réactivité de votre site, une nouvelle métrique a été introduite appelée Premier délai d'entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/9yJDWbSpxsXxr3CQntqCXbyPTMafsfYH1lGl)
_Par [Paul Irish](undefined" rel="noopener" target="_blank" title=") au Chrome Dev Summit_

Le premier délai d'entrée (FID) mesure le temps entre le moment où un utilisateur interagit pour la première fois avec votre site (c'est-à-dire lorsqu'il clique sur un lien, appuie sur un bouton ou utilise un contrôle personnalisé alimenté par JavaScript) et le moment où le thread principal est libre de la tâche longue qu'il effectue, rendant possible pour le navigateur de répondre à l'interaction de l'utilisateur.

N'est-ce pas la même chose que TTI, pourriez-vous demander ? Eh bien, non, ce n'est pas le cas. Le temps jusqu'à l'interactivité (TTI) mesure le temps nécessaire à votre application pour se charger et devenir capable de répondre rapidement aux interactions de l'utilisateur. En revanche, le premier délai d'entrée (FID) est une métrique qui mesure le délai que les utilisateurs subissent lorsqu'ils interagissent avec la page alors qu'elle n'est pas encore interactive.

![Image](https://cdn-media-1.freecodecamp.org/images/8RwMGUnZmRP25fv5Zdit8gihaZO2KsRtZmIQ)
_Le navigateur reçoit l'entrée lorsque le thread principal est occupé, il doit donc attendre qu'il ne soit plus occupé pour répondre à l'entrée. Le temps qu'il doit attendre est la valeur FID pour cet utilisateur sur cette page._

Le [FID](https://github.com/GoogleChromeLabs/first-input-delay) est une métrique de terrain, ce qui signifie qu'elle peut être observée lorsque de vrais utilisateurs interagissent réellement avec l'application web, tandis que le TTI est une métrique de laboratoire. Les métriques de terrain capturent un large éventail de conditions réseau réelles et d'appareils utilisés par les utilisateurs de Chrome. Cela peut être bien mesuré en utilisant des outils de surveillance des utilisateurs réels (RUM) comme le [Rapport d'expérience utilisateur Chrome](https://developers.google.com/web/tools/chrome-user-experience-report/).

Les applications et sites JavaScript rendus côté serveur avec des iframes tierces doivent être particulièrement attentifs au suivi de cette métrique. Ils sont susceptibles d'avoir des valeurs FID élevées, en particulier sur les appareils bas de gamme qui prennent plus de temps pour analyser et exécuter JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/l-Kpu7dcufzgptE5uyJzRAGOPeOR1-OyieZ3)
_Où recueillir ces métriques_

### Format d'image WebP

Les images ne deviennent pas performantes du jour au lendemain — il y a des mesures appropriées à mettre en place pour y parvenir. Vous devez envisager d'utiliser le bon format, des techniques de compression et le chargement paresseux des images. Avec l'introduction de [WebP](https://developers.google.com/speed/webp/), un nouveau format d'image qui permet une économie moyenne de 30 %, le coût de la diffusion des images — qui est le plus grand composant de la plupart des sites — est réduit.

WebP offre une compression avec et sans perte supérieure pour les images sur le web avec support de la transparence, rendant le web plus rapide. Étant donné que WebP n'est pas encore supporté par tous les navigateurs, il est conseillé d'utiliser l'élément `<picture>` pour fournir des solutions de repli. Le format d'image serait alors utilisé sur les navigateurs supportés tandis que les navigateurs web qui ne supportent pas encore WebP utiliseront l'image dans le format qu'ils supportent.

![Image](https://cdn-media-1.freecodecamp.org/images/aBAOa1f4ODx6im4sRF8r5gZif0zrdohww8E6)
_Statistiques de support de WebP sur [caniuse.com](https://caniuse.com/" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/7obCuyaIAxHyCH2U4cM9kciX-9JbWnXF8TAg)
_Statistiques de support de WebP par Katie Hempenius au Chrome Dev Summit_

```
<picture>  <source type="image/webp" srcset="imagename.webp">  <source type="image/jpeg" srcset="imagename.jpeg">  <img src="imagename.jpeg" alt="description de l'image"></picture>
```

Pour compresser les images vers et depuis le format WebP, les outils en ligne de commande `[cwebp](https://developers.google.com/speed/webp/docs/cwebp)` et `[dwebp](https://developers.google.com/speed/webp/docs/dwebp)` peuvent être utilisés respectivement. Allez essayer ce format d'image sur [squoosh](https://squoosh.app/) (téléchargez votre image et voyez le taux de compression).

### Chargement paresseux natif

Pour améliorer l'expérience utilisateur sur le web, le chargement paresseux natif arrivera sur Chrome. Lorsqu'il est ajouté aux balises d'image et aux iframes cross-origin, cela retarde le chargement de la ressource jusqu'à ce que la page soit défilée près d'elles. Il est supporté sur toutes les plateformes Chrome — Mac, Windows, Linux, Chrome OS, Android.

Pour charger paresseusement les ressources, utilisez l'attribut `lazyload` avec la valeur "on" ou "off". Si aucune valeur n'est spécifiée, le navigateur décide quelle ressource charger paresseusement.

```
<img src="imagename.png" lazyload="on">
```

### Navigation sans friction sur le Web

La navigation sur le web n'a pas été aussi fluide que l'expérience avec les applications natives. C'est une expérience douloureuse, surtout lorsque l'on navigue sur le web en utilisant des appareils bas de gamme sur des réseaux lents, laissant les utilisateurs fixer un écran blanc en attendant que le contenu soit affiché à l'écran. Pour venir en aide à ces utilisateurs web, les ingénieurs Chrome ont annoncé **Web Packaging et Portals.**

![Image](https://cdn-media-1.freecodecamp.org/images/83-0VN2Zyz4DxfaIhndbzbdUmP8yTor8tM4A)
_Disponible uniquement sur les appareils mobiles. L'icône identifie les sites qui ont implémenté AMP_

Basé sur le modèle des Accelerated Mobile Pages (AMP) et réalisé grâce aux [échanges signés](https://developers.google.com/web/updates/2018/11/signed-exchanges), [Web Packaging](https://github.com/WICG/webpackage) introduit la capacité de signer une page web avec une clé de chiffrement spéciale qui prouve le domaine d'origine de la page. Il crée ensuite un package qui peut être servi de n'importe où, qui sera utilisé par le navigateur pour représenter le domaine, permettant des navigations instantanées préservant la confidentialité.

Les [Portals](https://github.com/KenjiBaheux/portals) fonctionnent comme un iframe mais peuvent être navigables, permettant aux utilisateurs de passer au contenu du portail. Ils abstraient la navigation entre les pages, donnant à l'utilisateur l'impression d'être sur une application à page unique.

```
<portal src="https://mywebsite.com"></portal>
```

Lorsque la vue créée est cliquée, ajoutez quelques animations et déclenchez l'événement activate :

```
portal.activate();
```

Les deux propositions combinées permettent des transitions de page sans friction sur le web. Cela est encore en phase de développement précoce et est donc sujet à changement.

### Web.dev

Une plateforme web construite pour aider les développeurs à apprendre à construire pour le web et à s'assurer que le site web répond aux objectifs des bonnes pratiques. [Web.dev](https://web.dev/) se concentre sur les raisons pour lesquelles les développeurs doivent se soucier d'un concept donné, et donne des conseils pour aider les développeurs à construire un meilleur web en le gardant rapide, découvrable, accessible, sûr et résilient.

![Image](https://cdn-media-1.freecodecamp.org/images/tA9MC830sETVhFxsuvj5xe9fNQTCznIueVwy)

### VisBug

Conçu avec l'accessibilité à l'esprit, [VisBug](https://chrome.google.com/webstore/detail/visbug/cdockenadnadldjbbgcallicgledbeoc) est un outil qui peut être utile pour les ingénieurs. Avec cette extension, vous pouvez explorer et ajuster votre site directement dans le navigateur pour voir les blocs de construction et à quoi il ressemble s'il est conçu différemment.

![Image](https://cdn-media-1.freecodecamp.org/images/jwnTD3kNW9BmZCkLGqVN7TQc75PhgYkUBfPQ)
_Utilisation de VisBug sur mon site_

### Squoosh

Squoosh est une application web progressive de 15 ko pilotée par JavaScript pour la compression d'images, écrite en C. Elle est compilée à l'aide de [**emscripten**](https://github.com/kripken/emscripten) en web assembly avec des codecs de pointe directement dans le navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/Yvs8MDF29mIMbnT64FMxccL9n7whzeR5W-Ce)
_Une taille d'image originale de **163 ko** : Remarquez le taux de compression de WebP par rapport à MozJPEG_

Ayant la performance à l'esprit, l'équipe a utilisé des technologies appropriées en suivant les meilleures pratiques de codage et de performance pour obtenir une application performante :

* Preact (une bibliothèque de 3 ko) pour orchestrer le DOM
* WebPack pour le bundling et le code splitting
* Web workers pour le chargement paresseux et la concurrency
* Importations dynamiques de modules
* Web components (une primitive de bas niveau utilisée par Polymer) pour le polyfill d'élément personnalisé sur Edge

Comme le dirait [Jake Archibald](https://www.freecodecamp.org/news/highlights-from-chrome-dev-summit-2018-c7f1f1a7e6ae/undefined), [allez squoosh](https://squoosh.app/) quelques images.

### Points clés

* Les décisions de performance doivent être basées sur des données. Respectez l'utilisateur, ses données et ses préférences.
* En tant que développeurs, nous devons tester en utilisant des appareils bas de gamme sur des connexions réseau lentes. Lorsque nous développons pour le web en utilisant des appareils rapides sur des connexions réseau rapides, nous ne pouvons pas vraiment ressentir ce que nos utilisateurs ressentent et penser que nous avons atteint nos objectifs de performance.
* La performance n'est pas une priorité d'ingénierie. Le succès des initiatives de performance dépend de l'adhésion multifonctionnelle. Il devrait y avoir un alignement organisationnel dans toutes les équipes qui affectent le site web (marketing, design, ingénierie, etc.).
* Comprenez comment les service workers affectent la performance de votre site. Ils peuvent l'affecter positivement ou négativement en fonction de la mise en œuvre.
* Les utilisateurs apprécient un parcours utilisateur cohérent. Essayez donc de réduire les frictions sur vos applications web.
* Mesurez les applications en utilisant le modèle RAIL — Réponse, Animation, Inactivité et Chargement.
* Utilisez le cadre HEART (Bonheur, Engagement, Adoption, Rétention, Succès de la tâche) pour déterminer la qualité de l'interface utilisateur de votre application web.
* Certaines de ces fonctionnalités annoncées ici et d'autres sont derrière les flags de Chrome — chrome://flags/

### Conclusion

Ce n'est que la partie émergée de l'iceberg — vous ne voudriez pas manquer les détails. L'avenir est sur le web et la performance en est la racine. Toutes les sessions enregistrées tout au long de l'événement sont disponibles sur la [Chaîne des développeurs Google Chrome](https://www.youtube.com/playlist?list=PLNYkxOF6rcIDjlCx1PcphPpmf43aKOAdF). Le code est disponible sur [GitHub](https://github.com/GoogleChromeLabs).

Construisons un meilleur web 💡