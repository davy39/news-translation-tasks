---
title: Tests de régression de performance de site web automatiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-12T17:26:43.000Z'
originalURL: https://freecodecamp.org/news/automatic-website-performance-regression-testing-4e30e6bf5cd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fQwuGPiTj7IpbUE2ddk0hA.jpeg
tags:
- name: performance
  slug: performance
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Testing
  slug: software-testing
- name: technology
  slug: technology
seo_title: Tests de régression de performance de site web automatiques
seo_desc: 'By Adam Henson

  Using a post deploy step to automate performance regression testing in a continuous
  delivery workflow


  In another post I went over how to analyze website performance using Lighthouse,
  and specifically how we can automate performance mo...'
---

Par Adam Henson

#### Utilisation d'une étape post-déploiement pour automatiser les tests de régression de performance dans un flux de travail de livraison continue

![Image](https://cdn-media-1.freecodecamp.org/images/uteQY9zjTMzvFakiU7GdR0OoDXKGTuvvhJlG)

Dans un autre article, j'ai expliqué [comment analyser la performance d'un site web en utilisant Lighthouse](https://medium.freecodecamp.org/three-ways-to-analyze-website-performance-with-lighthouse-8d100966c04b), et plus précisément comment nous pouvons automatiser la surveillance des performances avec Foo. Dans cet article, je vais démontrer comment nous pouvons passer à la vitesse supérieure en testant la régression des performances... automatiquement ?.

### Qu'est-ce que le test de régression ?

Le test de régression est un type de test logiciel visant à confirmer qu'une modification récente du programme ou du code n'a pas affecté négativement les fonctionnalités existantes. Le respect des meilleures pratiques pourrait inclure les éléments suivants.

* **Maintenir un calendrier de test strict** : Maintenez toujours un calendrier de test continu tout au long du cycle de vie du développement logiciel. Non seulement cela obligera rapidement l'équipe à s'adapter à un régime de test fréquent, mais cela garantira également que le produit final est aussi bien testé que possible.
* **Utiliser un logiciel de gestion des tests** : À moins que votre projet logiciel actuel ne soit un simple projet secondaire auto-développé, il est probable que vous ayez une telle abondance de tests que le suivi de chacun dépassera largement les capacités d'un individu ou d'une feuille de calcul. Heureusement, il existe de nombreux outils de gestion des tests sur le marché conçus pour simplifier le processus de création, de gestion, de suivi et de reporting de tous les tests de votre suite de tests.
* **Catégoriser vos tests** : Imaginez une suite de tests de centaines ou de milliers de tests qui sont simplement identifiés par un seul champ `name` ou `id`. Comment quelqu'un pourrait-il trier cette liste massive pour identifier les tests qui sont liés ? La solution consiste à catégoriser les tests en groupes plus petits en fonction des critères appropriés pour votre équipe. La plupart des outils de gestion des tests fourniront les moyens de catégoriser ou d'étiqueter les tests, ce qui facilitera pour tout le monde dans l'équipe d'identifier et de référencer un certain _type_ de test.
* **Prioriser les tests en fonction des besoins des clients** : Une façon utile de prioriser les tests est de considérer les besoins du client ou de l'utilisateur. Considérez comment un cas de test donné impacte l'expérience de l'utilisateur final ou les exigences commerciales du client.

Consultez cet article pour plus d'informations : « [Regression Testing: What It Is and How to Use It](https://airbrake.io/blog/what-is/regression-testing) »

### Que signifie réellement « Performance du site web » ?

> Les temps de chargement varient considérablement d'un utilisateur à l'autre, en fonction des capacités de leur appareil et des conditions du réseau. Les métriques de performance **traditionnelles** comme le temps de chargement ou le temps DOMContentLoaded sont extrêmement peu fiables, car leur occurrence peut ou non correspondre au moment où l'utilisateur pense que l'application est chargée.

> ~ [User-centric Performance Metrics | Web Fundamentals | Google Developers](https://developers.google.com/web/fundamentals/performance/user-centric-performance-metrics)

De nos jours, le cycle de vie du chargement d'une page web peut être pensé de manière plus granulaire. Nous pouvons considérer les métriques de performance d'un site web comme étant « centrées sur l'utilisateur ». Lorsqu'un utilisateur accède à une page web, il recherche généralement un retour visuel pour le rassurer que tout fonctionne comme prévu.

Les métriques ci-dessous représentent des points importants du cycle de vie du chargement de la page. Chacune répond à des questions sur l'expérience utilisateur.

* **First Contentful Paint** : Est-ce que cela se produit ? La navigation a-t-elle démarré avec succès ? Le serveur a-t-il répondu ?
* **First Meaningful Paint** : Est-ce utile ? Suffisamment de contenu a-t-il été rendu pour que les utilisateurs puissent interagir avec ?
* **Time to Interactive** : Est-ce utilisable ? Les utilisateurs peuvent-ils interagir avec la page, ou est-elle encore occupée à charger ?
* **Long Tasks (absence de)** : Est-ce agréable ? Les interactions sont-elles fluides et naturelles, sans lag ni saccades ?

Nous pouvons exécuter des audits de performance manuellement ou par programmation en utilisant des outils comme [Lighthouse pour fournir des valeurs aux métriques](https://developers.google.com/web/tools/lighthouse/) similaires à celles ci-dessus. Nous pouvons utiliser une [intégration Lighthouse](https://github.com/GoogleChrome/lighthouse#lighthouse-integrations) comme [Foo pour surveiller automatiquement la performance du site web](https://www.foo.software) au fil du temps. Dans l'exemple ci-dessous, vous pouvez voir la performance de Twitter se dégrader et la corréler à un jour et une heure exacts ! Et si nous pouvions identifier cela à une version exacte ? Dans la section suivante, j'explique comment faire cela.

![Image](https://cdn-media-1.freecodecamp.org/images/XGra1-Mms-pMto7BezMFT6et1dqdoe1DaWv4)
_Dégradation de la performance de Twitter_

### Comment pouvons-nous tester automatiquement la régression des performances ?

Nous pouvons accomplir des tests de performance automatiques intégrés comme une étape post-déploiement dans un pipeline de livraison continue. Nous pouvons le faire en créant un compte **gratuit** avec Foo et en utilisant son API REST publique. Suivez les étapes ci-dessous.

1. [Créez un compte gratuit avec Foo](https://www.foo.software/register). Vérifiez votre email en cliquant sur le lien envoyé.
2. [Créez une page sur Foo](https://www.foo.software/account/pages) où vous pouvez ajouter l'URL de la page que vous souhaitez tester en performance.
3. Cliquez sur l'élément de la liste de votre page à partir de l'écran ci-dessus. Cela vous dirigera vers le tableau de bord reflétant votre page.
4. Obtenez le jeton API de la page en faisant défiler jusqu'en bas de la page ci-dessus.
5. Déclenchez une exécution de test en demandant l'endpoint comme détaillé dans [la documentation de l'API de Foo](https://www.foo.software/docs/api/Methods.html#additems). Une commande curl ressemblerait à quelque chose comme `curl -X POST "https://www.foo.software/api/v1/queue/items" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"pages\": \"pagetoken1,pagetoken2\", \"tag\": \"My Tag\" }"`.
6. Ajoutez la commande ci-dessus comme une étape post-déploiement dans votre pipeline CD. Vous pouvez trouver un [exemple complet sur GitHub](https://github.com/foo-software/website-performance-monitoring/blob/master/.circleci/config.yml). Ci-dessous un extrait de [circleci](https://circleci.com/) qui définit réellement cette étape.

Dans l'exemple lié ci-dessus, nos étapes de pipeline s'exécutent à chaque commit sur notre branche `master`.

![Image](https://cdn-media-1.freecodecamp.org/images/oXvAl0fsY-qFQvP95SU1r0KSuPtiqSTOIPaw)
_Étapes de livraison continue_

Et voilà, nous déployons maintenant une version à chaque commit sur `master` et exécutons un audit de performance automatiquement ✨!

![Image](https://cdn-media-1.freecodecamp.org/images/uBhpSn6stxtkC8hr5RPVmIXkSNyelsU8CAcz)
_Foo CD Exemple de résultats automatiques de régression de performance_

### Conclusion

[Foo offre de nombreuses fonctionnalités pour surveiller et analyser les performances](https://www.foo.software/features). Dans cet article, nous avons examiné comment nous pouvons l'utiliser pour exécuter des tests de régression de performance Lighthouse automatiquement. Voici d'autres fonctionnalités — la plupart sont **gratuites** !

* Audits de performance automatiques, une visualisation chronologique et des vues détaillées des résultats.
* Notifications par email, Slack et PagerDuty lorsque les performances ont chuté, se sont améliorées ou sont revenues à la normale.
* Vérifications de santé automatiques et notifications.