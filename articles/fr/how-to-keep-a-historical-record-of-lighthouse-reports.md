---
title: Comment conserver un historique des rapports Lighthouse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-28T13:02:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-a-historical-record-of-lighthouse-reports
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/lighthouse-logo-in-water-1.png
tags:
- name: Lighthouse
  slug: lighthouse
- name: SEO
  slug: seo
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: web performance
  slug: web-performance
- name: website development,
  slug: website-development
seo_title: Comment conserver un historique des rapports Lighthouse
seo_desc: "By Adam Henson\nLighthouse is an open-source project from the Google Chrome\
  \ team. It's used to analyze web page quality based on a set of modern, \"user-centric\"\
  \ metrics. \nWhen supporting websites that rely on organic search results for revenue,\
  \ qualit..."
---

Par Adam Henson

Lighthouse est un projet open-source de l'équipe Google Chrome. Il est utilisé pour analyser la qualité des pages web en fonction d'un ensemble de métriques modernes et "centrées sur l'utilisateur". 

Lors de la maintenance de sites web qui dépendent des résultats de recherche organique pour leurs revenus, la qualité est cruciale. La performance, l'accessibilité et les bonnes pratiques SEO générales sont des facteurs majeurs dans le classement des moteurs de recherche. 

Lighthouse fournit un ensemble granulaire de métriques représentant ces facteurs ainsi que des suggestions d'amélioration dans les rapports. 

Il existe [de nombreuses façons d'exécuter Lighthouse](https://developers.google.com/web/tools/lighthouse), mais dans le monde réel, vous pourriez vouloir comparer les rapports régulièrement, surtout dans les flux de travail en changement continu. Cela dit, vous vous demandez peut-être - **comment puis-je suivre les changements SEO, de performance et d'accessibilité au fil du temps** ?

Cet article explique comment utiliser [Automated Lighthouse Check](https://www.foo.software/lighthouse) pour analyser la qualité d'un site web au fil du temps. Mais gardez à l'esprit qu'il existe de nombreuses autres [intégrations Lighthouse](https://github.com/GoogleChrome/lighthouse#lighthouse-integrations) parmi lesquelles choisir.

## Sauvegarde des rapports et visualisation des résultats dans une timeline

Le [système de notation Lighthouse](https://developers.google.com/web/tools/lighthouse/v3/scoring) est un aspect intéressant de l'outil qui peut sembler un peu obscur au début. Néanmoins, il peut être très utile pour comparer des données historiques. 

La catégorie performance en particulier est assez complexe dans son calcul de score et vous pouvez trouver beaucoup de [lectures intéressantes sur le sujet parmi d'autres sur web.dev](https://web.dev/performance-scoring/).

Automated Lighthouse Check offre un moyen de déclencher manuellement des audits ou d'établir un calendrier pour qu'ils s'exécutent automatiquement tout au long de la journée. Ces audits sont sauvegardés dans une base de données afin que vous puissiez visualiser et analyser les résultats à un niveau historique. Vous pouvez en fait examiner n'importe quel rapport dans le temps pour voir les détails complets ([voir un exemple ici](https://www.foo.software/dashboard/page/5d1d459641e33a002f256efc)).

Pour un guide sur la prise en main d'Automated Lighthouse Check, [consultez la documentation](https://www.foo.software/automated-lighthouse-check-getting-started/).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/automated-ligthouse-check-timeline.png)
_Vue en timeline des scores Lighthouse_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-28-at-8.15.32-AM.png)
_Une liste historique des audits Lighthouse_

## Automatisation de Lighthouse dans DevOps

Non seulement il existe de nombreux outils Lighthouse basés sur le cloud, mais il existe également de nombreux projets open-source qui peuvent être implémentés dans une variété de flux de travail DevOps. Certaines de ces solutions prennent en charge la persistance des données sous une forme ou une autre, pour un suivi historique. 

Voici quelques exemples auxquels j'ai contribué.

* [Cet article explique comment utiliser Lighthouse dans CircleCI](https://www.freecodecamp.org/news/how-to-use-lighthouse-in-circleci/). Vous pouvez sauvegarder les rapports en tant qu'"artifacts" dans CircleCI ou les télécharger automatiquement sur AWS S3.
* [Cet article explique comment utiliser Lighthouse dans GitHub Actions](https://www.freecodecamp.org/news/how-to-use-lighthouse-in-github-actions/). Cette solution offre également un moyen de sauvegarder les rapports en tant qu'"artifacts" (dans GitHub) ou de les télécharger automatiquement sur AWS S3.
* [Lighthouse Persist est un package NPM](https://www.npmjs.com/package/@foo-software/lighthouse-persist) qui expose l'API native de Lighthouse avec des options supplémentaires pour définir les identifiants AWS S3 afin qu'il puisse être utilisé pour télécharger des rapports automatiquement.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-28-at-8.34.59-AM.png)
_Quelques amis - Octocat, Jenkins, CircleCI_

## Conclusion

J'espère que cet article vous a été utile en fournissant des solutions pour analyser historiquement la qualité des sites web. Aidez à soutenir vos développeurs locaux en achetant leur logiciel ?

Mais plus sérieusement, j'adorerais recevoir vos commentaires sur Automated Lighthouse Check... commentaires, suggestions, demandes de fonctionnalités, etc. Il a environ un an au moment de la rédaction de cet article et a récemment été migré vers Kubernetes pour une haute disponibilité. 

Automated Lighthouse Check propose [des plans gratuits et premium](https://www.foo.software/pricing).