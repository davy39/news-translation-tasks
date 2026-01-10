---
title: 'Comment structurer les dépôts de code : Multi, Mono ou Organique ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T11:26:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-structure-code-repositories-multi-mono-or-organic-eda67b397d38
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bk93-RBsMVGgEhYozK2SgQ.jpeg
tags:
- name: engineering
  slug: engineering
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Comment structurer les dépôts de code : Multi, Mono ou Organique ?'
seo_desc: 'By Chetan Sharma

  The newest debate in town is whether you should keep your services in a single repository
  or multiple small repositories.

  The idea of multiple small repositories is that code for each of your app’s micro
  service is kept in a reposito...'
---

Par Chetan Sharma

Le nouveau débat en ville est de savoir si vous devez garder vos services dans un seul dépôt ou dans plusieurs petits dépôts.

L'idée de plusieurs petits dépôts est que le code pour chaque micro-service de votre application est conservé dans un dépôt qui lui est propre. Avec un mono-dépôt, vous gardez tout le code dans un seul dépôt et déployez le code en tant que micro-services.

Alors, lequel devez-vous utiliser ? Être trop rigide sur une approche sans considérer le but et les utilisations de chaque approche peut conduire à des résultats négatifs à long terme. Si vous êtes conscient de quand utiliser chacune, cela peut augmenter votre productivité et améliorer votre projet.

### Pour enfreindre les règles, nous devons d'abord comprendre pourquoi elles existent.

Une recommandation courante est d'avoir un dépôt indépendant pour chaque application/service. Mais pourquoi ? Parce qu'en ayant un dépôt pour chaque micro-service, nous gagnons :

* **Liberté** d'écrire du code différemment et indépendamment de tous les autres services.
* **Vitesse** dans la réalisation des changements de code tout en corrigeant des bugs, en faisant des mises à jour, des tests et des déploiements. Puisque les changements n'ont à être testés que dans un seul dépôt, le déploiement du code est plus rapide et plus fiable.
* **Séparation du code** en unités indépendantes, ce qui prévient les fuites de bugs et les goulots d'étranglement de performance entre les services.
* **Propriété claire** de chaque dépôt et service, ce qui est particulièrement utile pour les grandes équipes.

### Mais pourquoi le besoin de mono-dépôts est-il apparu ?

Clairement, l'approche multi-dépôts a ses avantages. Mais elle vient aussi avec ses propres défis, surtout dans les projets avec un grand nombre de micro-services qui utilisent les mêmes frameworks, langages, piles technologiques, etc.

Quelques-uns de ces défis sont :

* **Appliquer des standards et des meilleures pratiques** à travers tous les dépôts. Avec un multi-dépôt, les changements dans les standards de code et les meilleures pratiques doivent être répliqués à travers les dépôts. Avec un mono-dépôt, tous les changements peuvent être faits en un seul endroit.
* L'effort de **maintenir des composants partagés ou communs**. Les correctifs de sécurité, les mises à jour de version et les corrections de bugs impliquent de s'assurer que ces changements sont faits à travers tous les dépôts et qu'ils fonctionnent de manière transparente partout. (En aparté, le code répété dans chaque service alourdit également sa taille.) Dans un mono-dépôt, nous pouvons faire des mises à jour en un seul endroit, économisant ainsi du temps et des maux de tête.
* **Tests de bout en bout** en tandem avec des services étroitement liés ou dépendants directement depuis la machine du développeur. En ayant tout le code en un seul endroit, nous facilitons le processus de démarrage de tous les services liés et l'exécution des tests de bout en bout.
* **Déploiements sur site** de code pour d'autres entreprises. En déployant un mono-dépôt en tant que micro-services, nous économisons du temps et réduisons l'effort redondant de démarrage de chaque dépôt.

Clairement, il y a des avantages et des inconvénients aux deux approches, et chaque approche aura ses propres bénéfices dans différentes circonstances.

Par conséquent, nous avons adopté l'approche de rester flexibles et d'utiliser à la fois des multi-dépôts et des mono-dépôts, mais seulement après avoir complètement compris pourquoi nous avons choisi d'utiliser chacun pour chaque service. Cela nous a conduit à avoir plusieurs dépôts contenant plusieurs micro-services, séparés de manière à ce que cela ait rendu :

* La maintenance et les mises à jour à la fois faciles et rapides.
* La localisation du code à déboguer ou à changer beaucoup plus structurée.
* L'intégration de nouveaux coéquipiers plus facile.

### Comment nous décidons du type de dépôt à utiliser

Les considérations suivantes nous ont aidé à décider quand utiliser des mono-dépôts par rapport aux multi-dépôts.

#### 1. Pensez au code qui servira de fondation au service.

> _Commencez par identifier les similitudes dans le code, la maintenance et les mises à jour. Si plusieurs dépôts ont un code identique, il serait préférable de les regrouper dans un seul dépôt._

La liberté d'écrire du code différemment et indépendamment dans un service est l'un des avantages de plusieurs petits dépôts. Mais souvent, les services auront beaucoup de structures identiques s'ils utilisent le même langage, framework, journalisation, scripts de démarrage, middlewares, etc. Réutiliser ces structures partagées fait gagner du temps.

Par exemple, [Collect](http://socialcops.com/collect) — notre outil principal de collecte de données — a plusieurs micro-services construits sur un framework identique. Ces services sont construits sur [Node.js](https://nodejs.org/en/), [Express](https://expressjs.com/) et [Parse Server](https://parseplatform.org/). Ils partagent beaucoup de bibliothèques comme [Winston](https://github.com/winstonjs/winston), [Mongoose](https://mongoosejs.com/) et d'autres intégrations tierces. Auparavant, lorsque chacun de ces services avait son propre dépôt, la mise à jour ou la correction d'un bug dans l'un de ces modules partagés signifiait mettre à jour et tester chaque dépôt séparément. Cela était lent et fastidieux.

Cependant, lorsque nous les avons regroupés dans un mono-dépôt, les tests et les mises à jour des modules partagés sont devenus plus faciles et plus rapides. L'application des correctifs de sécurité et l'application des standards sont devenues plus faciles puisque les développeurs peuvent faire toutes les modifications en un seul endroit.

Le risque potentiel d'un mono-dépôt est qu'un développeur peut réutiliser du code initialement écrit pour un module sans rapport. Lorsque les deux modules partagent du code, un changement dans ce code commun peut entraîner des bugs. Si ces bugs passent inaperçus, ils peuvent affecter les pipelines CI/CD (Intégration Continue et Livraison) de micro-services sans rapport. Pour éviter de tels problèmes, il est important d'avoir une suite de tests solide en place.

#### 2. Vérifiez si vous avez des modules très distincts des autres.

> _Développez-vous un module qui demande une technologie, un langage, un framework ou une persistance très différents ? Alors le séparer dans un dépôt séparé sera meilleur._

Dans Collect, il y a des services qui gèrent le traitement des événements en masse. Ils maintiennent des files d'attente, exécutent des scripts personnalisés et ont un mécanisme de gestion des erreurs complètement différent. Ces services sont écrits en Python, et assez souvent, ils doivent effectuer des tâches intensives en CPU.

Ainsi, lorsque nous pensions à restructurer le code pour Collect, garder ces services dans un dépôt séparé est apparu comme une évidence. Ces services étaient très différents du dépôt principal de Collect (décrit ci-dessus). Alors que le dépôt principal était pour les requêtes orientées utilisateur, ce dépôt était tout à fait axé sur les tâches et les exécutions en arrière-plan. De plus, la gestion des changements dans ces services allait être différente et isolée du dépôt principal.

Penser à la maintenance du code et à son évolution au fil du temps nous a conduit à regrouper ces services dans un dépôt séparé. En faisant cela, nous avons pu mettre en place un système de gestion des changements complètement différent, ce qui s'est avéré très utile et plus productif.

#### 3. Considérez l'incertitude et donc la fréquence des changements qu'un service pourrait subir.

Lorsque vous commencez à travailler sur quelque chose de très incertain (soit en termes de portée du problème, soit de l'implémentation elle-même), alors avoir un dépôt différent peut vous donner la vitesse et la liberté dont vous avez besoin pour tester des choses.

Par exemple, disons que vous voulez tester une nouvelle façon de traiter des images pour identifier des objets. Vous voulez vous essayer à l'apprentissage automatique, mais vous n'êtes toujours pas sûr de son évolution ou si l'énoncé du problème changera radicalement. Dans ce cas, il serait clairement préférable d'avoir un dépôt séparé et d'atteindre un point de certitude. À l'inverse, si vous pensez que l'API a atteint la stabilité et restera inchangée pendant une longue période, vous pouvez décider de la fusionner avec l'un de vos dépôts principaux.

Le blog a été initialement publié sur [blog.socialcops.com](https://blog.socialcops.com/). Ce qui précède est la façon dont nous gérons nos décisions de dépôt. J'espère que cela peut vous aider à penser à partir des premiers principes si vous abordez ce problème. Abonnez-vous à notre newsletter pour plus de mises à jour de l'équipe d'ingénierie et de science des données de [SocialCops](http://www.socialcops.com).