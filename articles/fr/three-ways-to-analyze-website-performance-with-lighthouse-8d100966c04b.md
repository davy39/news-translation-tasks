---
title: Comment analyser les performances d'un site web avec Lighthouse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T14:11:19.000Z'
originalURL: https://freecodecamp.org/news/three-ways-to-analyze-website-performance-with-lighthouse-8d100966c04b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ydkP__0WxXbUl9Jy8D67DA.jpeg
tags:
- name: 'automation testing '
  slug: automation-testing
- name: Productivity
  slug: productivity
- name: SEO
  slug: seo
- name: 'tech '
  slug: tech
- name: Website performance
  slug: website-performance
seo_title: Comment analyser les performances d'un site web avec Lighthouse
seo_desc: 'By Adam Henson

  Audit website performance manually, programmatically, or automatically


  Cityscape Birds Eye View

  Lighthouse is an open-source project by Google that gives you a way to measure web
  page performance. It has configurable settings for repr...'
---

Par Adam Henson

#### Auditer les performances d'un site web manuellement, par programmation ou automatiquement

![Image](https://cdn-media-1.freecodecamp.org/images/KZlzVvOb9fZcuBwmwxqRHgrrZyct4MCKNB4X)
_Vue aérienne d'une ville_

Lighthouse est un projet open-source de Google qui vous offre un moyen de mesurer les performances des pages web. Il dispose de paramètres configurables pour reproduire diverses conditions. Vous pouvez définir le type de réseau et de périphérique à simuler, par exemple.

> Vous donnez à Lighthouse une URL à auditer, il exécute une série d'audits sur la page, puis génère un rapport sur la performance de la page. À partir de là, utilisez les audits échoués comme indicateurs pour améliorer la page. Chaque audit dispose d'une documentation de référence expliquant pourquoi l'audit est important, ainsi que la manière de le corriger. [Lighthouse](https://developers.google.com/web/tools/lighthouse/)

Il existe de nombreuses raisons pour lesquelles vous souhaiteriez mesurer les performances, mais l'une des plus importantes concerne l'impact sur le référencement (SEO). Je vais plus en détail sur ce sujet et sur la manière d'aborder certaines métriques dans [cet article](https://medium.freecodecamp.org/taming-performance-in-todays-web-app-with-lighthouse-webpack-and-react-loadable-components-b2d3fa04e0ab).

### Exécuter Lighthouse avec Chrome DevTools

Vous pouvez exécuter des audits de performance manuellement avec [l'extension navigateur Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/). Il suffit de lancer l'extension depuis la page web que vous souhaitez tester et de sélectionner le panneau « Audits ».

![Image](https://cdn-media-1.freecodecamp.org/images/CoSD1b8oLEO5ahFg4E4dRazNeo7c5L5y5sHo)
_Panneau « Audits » de Chrome DevTools_

Parmi une variété d'audits, vous pouvez choisir « performance ». Vous pouvez également choisir de simuler le type de périphérique et la limitation du réseau. Certaines informations spécifiques sur la limitation peuvent être trouvées dans le [dépôt Github du projet Lighthouse](https://github.com/GoogleChrome/lighthouse/blob/master/docs/throttling.md).

Cliquez sur « Exécuter les audits » ensuite. Une fois terminé, Lighthouse fournit un rapport dans l'interface utilisateur de l'extension.

![Image](https://cdn-media-1.freecodecamp.org/images/rQqYaIzYRyX4kCF5-V4m7sr0MncTgrI9sJf9)
_Rapport de performance de Lighthouse_

Ce rapport est un aperçu général des métriques importantes, des opportunités et du score de performance global. Des vignettes illustrent le cycle de vie du chargement de la page. Que signifie tout cela ? Google fournit une multitude de [documentation décrivant chaque métrique](https://developers.google.com/web/tools/lighthouse/audits), comment les aborder et le [score de performance global](https://developers.google.com/web/tools/lighthouse/v3/scoring).

Dans le coin supérieur gauche du panneau Chrome DevTools se trouve une icône de téléchargement que vous pouvez utiliser pour télécharger le rapport complet au format JSON. Vous pouvez ensuite l'utiliser pour créer un rapport PDF via [Lighthouse Report Viewer](https://github.com/GoogleChrome/lighthouse#using-the-node-cli).

En raison du grand nombre de facteurs jouant sur le cycle de vie du chargement de la page, il est important de comparer les résultats par lots. Prendre une moyenne de 5 exécutions, par exemple, fournira une meilleure vision.

### Exécuter Lighthouse par programmation

Pour nos situations standard « courantes », ce qui précède devrait suffire. Une autre façon d'exécuter Lighthouse consiste à installer le package open-source via NPM et à suivre les instructions dans la [documentation CLI](https://github.com/GoogleChrome/lighthouse#using-the-node-cli). Cela peut être bénéfique si vous souhaitez exécuter des audits par programmation dans un pipeline de build, par exemple.

De manière similaire à ce qui précède, vous pouvez également exécuter Lighthouse en code en suivant la [documentation pour utiliser le module Node de manière programmatique](https://github.com/GoogleChrome/lighthouse/blob/master/docs/readme.md#using-programmatically). Vous pourriez créer une application Node.js complète avec Lighthouse !

### Exécuter Lighthouse automatiquement au fil du temps

Maintenant que nous sommes des pros, passons au niveau supérieur. Il existe de nombreuses [intégrations listées dans la documentation de Lighthouse](https://github.com/GoogleChrome/lighthouse#lighthouse-integrations), alors jetons un coup d'œil à l'une d'entre elles.

#### Utiliser « Foo » pour exécuter Lighthouse et comparer les résultats au fil du temps

Dans un environnement d'ingénierie où de nombreux développeurs déploient des modifications d'application de manière régulière, il peut être important de surveiller les performances du site web au fil du temps pour associer les ensembles de modifications à la dégradation ou à l'amélioration des performances. Un autre exemple serait les équipes qui ont des initiatives pour améliorer les performances pour le classement SEO ou d'autres raisons. Dans ces situations, il est crucial de surveiller les performances du site web sur des jours, des semaines, des mois, etc.

Vous pouvez ajouter des URLs à suivre sur [www.foo.software](https://www.foo.software) et surveiller les changements de performance. Foo fournit également des notifications par email, Slack ou PagerDuty lorsque les performances ont chuté en dessous d'un seuil défini par l'utilisateur, lorsqu'elles sont revenues à la normale et lorsque des améliorations sont identifiées automatiquement !

Le meilleur dans tout cela, c'est que vous pouvez [créer un compte gratuitement](https://www.foo.software/register) ! Une fois inscrit et connecté, cliquez sur le lien « Pages » dans la navigation supérieure. C'est ici que vous pouvez ajouter des URLs à surveiller. Foo sauvegarde les résultats et affiche un graphique chronologique fournissant une visualisation des métriques importantes. Vous pouvez naviguer à travers les jours, les semaines, les mois et approfondir les rapports détaillés.

![Image](https://cdn-media-1.freecodecamp.org/images/aMrCtx3sHKfiNW4UbN32f5y7WwUejkJqEKYg)
_Exemple de graphique chronologique Lighthouse Foo pour Amazon_

### Conclusion

Lighthouse devient une norme industrielle dans la mesure des performances des sites web. Il existe des livres de [documentation sur Lighthouse qui fournissent des détails sur les métriques importantes](https://developers.google.com/web/tools/lighthouse/).