---
title: Mocking dynamique avec Kakapo.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-25T08:11:07.000Z'
originalURL: https://freecodecamp.org/news/dynamic-mocking-with-kakapo-js-bdbd3d7b58e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AWc9hdd-JQUromU-wYWeDA.jpeg
tags:
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: Web Development
  slug: web-development
seo_title: Mocking dynamique avec Kakapo.js
seo_desc: 'By zzarcon

  3 months after the first commit, Kakapo.js reaches the first release and we are
  proud to announce that now it is ready to use. Let us introduce you Kakapo.


  Kakapo - The next generation mocking framework in Javascript


  Kakapo is just a set...'
---

Par zzarcon

3 mois après le premier commit, [Kakapo.js](http://github.com/devlucky/Kakapo.js) atteint la première version et nous sommes fiers d'annoncer qu'il est maintenant prêt à être utilisé. Permettez-nous de vous présenter Kakapo.

> Kakapo - Le framework de mocking de nouvelle génération en JavaScript

Kakapo est simplement un ensemble d'outils qui tente de faciliter votre vie lors de la création d'applications web, notamment lors de la création de **mocks côté client**. Il fournit des composants et des API qui vous permettent de répliquer facilement la logique et les réponses de votre backend côté client.

Ce n'est rien de nouveau et je suis assez sûr que vous êtes familier avec des outils comme [jquery-mockjax](https://github.com/jakerella/jquery-mockjax), [FakeXMLHttpRequest](https://github.com/pretenderjs/FakeXMLHttpRequest) ou [fetch-mock](https://github.com/wheresrhys/fetch-mock), ces outils sont excellents et existent depuis longtemps, mais à mon avis, ils ne sont qu'une partie de la solution à un grand problème.

Pourquoi devriez-vous vous soucier du mocking côté client ? Pour résoudre le _goulot d'étranglement du backend_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UJ2ClAEKWpWAM_QF5kj9Kg.jpeg)

### Goulot d'étranglement du backend

Lors de la dernière rétrospective de sprint, après le troisième sprint consécutif où plus de 50 % des points prévus n'ont pas été atteints, nous avons commencé à nous demander ce qui n'allait pas. Certains développeurs backend disaient :

* _Oui, nous pensions que c'était une tâche facile, mais nous avons dû passer une semaine à refactoriser la fonctionnalité actuelle pour qu'elle fonctionne comme prévu…_
* _Trop de choses non prévues sont apparues et nous avons dû nous occuper de ces problèmes en production…_
* _Les serveurs de staging ne fonctionnaient pas du tout et nous avons dû redéployer le service plus de 5 fois…_

De l'autre côté, les développeurs frontend :

* _J'ai passé toute la journée de lundi à essayer de comprendre pourquoi le endpoint retournait un code de statut 500 au lieu d'obtenir la réponse attendue…_
* _Nous construisions le profil utilisateur, mais le endpoint de création n'était pas documenté, donc nous n'avons pas pu le faire pour la release…_
* _Hier, j'ai dû basculer trop de fois entre différents environnements de staging que je n'ai pas eu le temps de travailler sur la fonctionnalité…_

J'étais très frustré par la situation actuelle et, surtout, par le fait de ne pas pouvoir livrer une petite fonctionnalité dans le temps estimé. Il m'a fallu un certain temps pour réaliser que ce n'était pas un problème de backend ou de client : le problème était plus profond et nécessiterait plus de temps et d'efforts pour être résolu.

> Et si, au lieu de traiter les problèmes de backend et les environnements de staging, nous construisions la fonctionnalité basée sur une réponse JSON convenue avec l'équipe backend au préalable ?

Voyons un exemple de base pour avoir une idée de son fonctionnement :

Dans l'exemple ci-dessus, nous définissons simplement quelques endpoints et une factory, puis nous définissons une logique métier à l'intérieur des gestionnaires de requêtes afin de retourner les réponses fictives. Pour ce faire, nous utilisons trois éléments clés de Kakapo :

* [**Router**](http://devlucky.github.io/kakapo-js#router) : Le routeur de Kakapo reconnaît les URL (routes) et les achemine vers les gestionnaires associés. Il fournit également un objet **request** en tant qu'argument qui vous donne des informations utiles sur la requête entrante.
* [**Database**](http://devlucky.github.io/kakapo-js#database) : Cette classe, ainsi que les **factories** et les **relationships**, vous permet de définir comment vos entités doivent être représentées et leurs comportements.
* [**Server**](http://devlucky.github.io/kakapo-js#server) : Il connecte tous les autres composants et vous permet de les activer ou de les désactiver ; cette fonctionnalité vous donne la possibilité de basculer entre plusieurs bases de données et routeurs, nous appelons cela des [scenarios](http://devlucky.github.io/kakapo-js#scenarios).

#### Mocking côté client dans la vie réelle

Habituellement, le mocking des API est réalisé en créant un **JSON statique** pour chaque requête et en testant contre celui-ci. Créer et maintenir le JSON est une tâche répétitive et sujette aux erreurs.

Kakapo, en revanche, vous permet de **mocker dynamiquement** vos réponses en définissant comment elles doivent apparaître et en les sérialisant automatiquement en JSON.

Par exemple, essayons de faire un CRUD.

C'est à quel point il est facile de répliquer un CRUD avec Kakapo, vous pouvez également consulter [fake data](http://devlucky.github.io/kakapo-js#fake-data) et [serializers](http://devlucky.github.io/kakapo-js#serializers) pour voir quelques fonctionnalités de Kakapo.

### Défis techniques

Outre tout ce que nous avons appris lors de la création de la bibliothèque, je voudrais souligner certains des défis les plus difficiles auxquels nous avons dû faire face :

#### Intercepteurs

Les composants [interceptor](http://devlucky.github.io/kakapo-js#interceptors) sont ceux qui sont responsables de l'_interception_ de la requête de l'utilisateur, de la vérification si elle correspond à l'une des routes et de l'application du mock. Ils sont conçus de manière si modulaire que l'utilisateur peut définir les siens. Actuellement, nous supportons les API de réseau du navigateur, [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) et [fetch](https://developer.mozilla.org/en/docs/Web/API/Fetch_API), mais nous supporterons bientôt Node.js ?.

> Réinventer la roue n'est pas implicitement mauvais. Vous pouvez apprendre beaucoup en le faisant.

J'ai trouvé ce composant compliqué car vous devez répliquer la même fonctionnalité que les API du navigateur fournissent. Dès que vous vous comportez un peu différemment, l'application peut se casser car elle dépend du comportement natif. Vous pouvez apprendre beaucoup en construisant ce genre de choses directement avec les API natives au lieu d'utiliser des wrappers comme jQuery, car vous comprendrez vraiment comment cela fonctionne en interne.

Lors de l'implémentation des intercepteurs, nous avons dû nous assurer de ne pas casser les bibliothèques de réseau populaires comme [jQuery](http://api.jquery.com/jquery.ajax/) et [Superagent](http://visionmedia.github.io/superagent/). Nous avons créé des [_tests d'intégration_](https://github.com/devlucky/Kakapo.js/tree/master/test/specs/integration) pour nous assurer que Kakapo continuera à fonctionner comme prévu après l'introduction de nouveaux changements.

#### Tests

Les tests sont une nécessité lors du développement de logiciels, mais ils sont encore plus critiques dans les projets open source que d'autres développeurs utiliseront potentiellement. Nous avons toujours gardé cela à l'esprit lors de la création de Kakapo et ce fut le premier projet que j'ai jamais réalisé en suivant strictement la méthode **TDD**. Je dois admettre que le sentiment que j'avais au début était très différent de celui que j'ai maintenant. Parfois, j'avais l'impression que l'écriture de tant de tests nous ralentissait, mais maintenant, avec une [couverture de code élevée](https://codecov.io/github/devlucky/Kakapo.js?branch=master), je me sens vraiment confiant lorsque je dois refactoriser un composant critique ou ajouter une nouvelle fonctionnalité à la bibliothèque.

C'est quelque chose que vous devez introduire dans votre flux de travail de manière incrémentielle et définir avec l'équipe. Comme il s'agissait du plus grand projet open source sur lequel j'ai jamais travaillé, j'ai appris à coordonner et à travailler avec une équipe. Parfois, les choses doivent être discutées [deux fois ou plus](https://github.com/devlucky/devlucky.github.io/issues/4) juste pour s'assurer que tous les membres sont sur la même longueur d'onde, mais à la fin, cela va fonctionner.

### Importance de la documentation

Les développeurs _détestent_ écrire de la documentation. Malheureusement, c'est aussi important que d'avoir une bonne bibliothèque et ce sera la première chose que vos utilisateurs et contributeurs verront.

Pensez-y de cette manière : vous avez construit votre bibliothèque pendant quelques mois et maintenant elle est enfin prête, ne pensez-vous pas qu'il vaut la peine de passer quelques jours à [construire un site web](https://pages.github.com/) et à écrire quelques bons exemples ?

Voici une conférence de React Europe 2016 dans laquelle [Christopher Chedeau](https://twitter.com/Vjeux) explique comment Facebook gère la diffusion des bibliothèques open source.

#### Jekyll

[Jekyll](https://jekyllrb.com/) nous a littéralement sauvés, il a amélioré la façon dont nous écrivons la documentation et la rapidité. Avant de choisir Jekyll, j'avais l'habitude de construire des sites web statiques avec un peu de css et de html pour ensuite y placer la documentation. Cependant, certains développeurs pourraient ne pas être fluides et manquer la simplicité de [Markdown](https://en.wikipedia.org/wiki/Markdown). C'est pourquoi nous avons décidé d'utiliser Jekyll, qui vous permet d'écrire vos pages en [Kramdown](http://kramdown.gettalong.org/) (markdown avec des stéroïdes) et est intégré avec Github Pages.

Une fois que nous nous sommes sentis à l'aise avec l'état de la documentation et des exemples, nous avons également voulu donner une bonne première impression aux nouveaux arrivants. Nous avons créé un [script](https://github.com/devlucky/Kakapo.js/blob/master/create-readme.js) qui récupère le **fichier md** de la [page github](https://github.com/devlucky/devlucky.github.io), ajoute du contenu et génère le [readme](https://github.com/devlucky/Kakapo.js/blob/master/README.md) ?

#### Applications de démonstration

Tout le monde aime les démos, elles montrent ce que fait votre bibliothèque et comment elle le fait. Cela peut sembler étrange, mais cela vous aidera également à apprendre à utiliser votre propre bibliothèque, ainsi qu'à trouver des bugs ou des fonctionnalités manquantes.

Jusqu'à ce que nous construisions notre première [application todo](https://kakapo-todo-app.firebaseapp.com/) en utilisant Kakapo, nous n'avons pas réalisé les principaux points de douleur et comment les résoudre, c'est pourquoi nous avons ensuite construit notre deuxième application de démonstration, un [explorateur github](https://kakapo-github-explorer.firebaseapp.com/).

> Avoir une bonne bibliothèque sans documentation, c'est comme avoir une fusée que personne ne sait utiliser.

### FEUILLE DE ROUTE

Le projet vient de commencer, mais nous avons des plans ambitieux pour lui ; n'hésitez pas à consulter les [problèmes ouverts](https://github.com/devlucky/Kakapo.js/issues) ou à en ouvrir de nouveaux, nous l'apprécierons vraiment ! Voici quelques-uns des plus importants :

* Support complet du **JSON API**
* Support des intercepteurs **Node.js**
* Support des **Async handlers**

Nous travaillons également dur pour terminer [la version Swift de Kakapo](https://github.com/devlucky/Kakapo), qui est presque prête pour la phase bêta, et nous pensons qu'elle va être un game changer pour la construction d'applications iOS : restez à l'écoute ! ?