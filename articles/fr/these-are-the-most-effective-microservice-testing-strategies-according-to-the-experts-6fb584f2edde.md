---
title: Voici les stratégies de test de microservices les plus efficaces, selon les
  experts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T20:15:24.000Z'
originalURL: https://freecodecamp.org/news/these-are-the-most-effective-microservice-testing-strategies-according-to-the-experts-6fb584f2edde
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OufjerPy6FKelc0l
tags:
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: Voici les stratégies de test de microservices les plus efficaces, selon
  les experts
seo_desc: 'By Jake Lumetta

  Testing microservices is hard. More specifically, end-to-end testing is hard, and
  that’s something we’ll discuss in greater detail in this article.

  But first, a quick story.

  I learned just how hard microservice testing could be when I...'
---

Par Jake Lumetta

Tester les microservices est difficile. Plus précisément, les tests de bout en bout sont difficiles, et c'est quelque chose que nous allons discuter plus en détail dans cet article.

Mais d'abord, une petite histoire.

J'ai appris à quel point les tests de microservices pouvaient être difficiles lorsque j'ai plongé pour la première fois dans une pile technologique avec sept microservices distincts. Chacun avait sa propre base de code, sa gestion des dépendances, ses branches de fonctionnalités et son schéma de base de données – qui avait également un ensemble unique de migrations.

Parlez d'un environnement chaotique.

L'approche que nous avons adoptée était de tout exécuter localement. Cela signifiait que, à tout moment où je voulais exécuter des tests de bout en bout, je devais suivre les cinq étapes suivantes pour chacun des sept microservices :

1. M'assurer que j'étais sur la bonne branche de code (soit master, soit feature_xyz)
2. Télécharger le dernier code pour cette branche
3. M'assurer que toutes les dépendances étaient à jour
4. Exécuter les nouvelles migrations de base de données
5. Démarrer le service

C'était juste une exigence de base pour permettre l'exécution des tests. Souvent, j'oubliais d'effectuer l'une de ces étapes pour un service et je passais 10 à 15 minutes à déboguer le problème. Une fois que j'avais enfin tous les services en cours d'exécution, je pouvais alors commencer à lancer la suite de tests. Cette expérience m'a certainement fait regretter les jours où je testais un grand monolithe.

Donc oui, j'ai découvert que les tests de bout en bout des microservices sont difficiles – et deviennent exponentiellement plus difficiles avec chaque nouveau service que vous introduisez. Mais ne craignez rien, car il existe des moyens de faciliter les tests de microservices. J'ai parlé à plusieurs CTO de la manière dont ils ont trouvé leurs propres façons créatives de résoudre ce problème complexe.

### Méthodes courantes de test de microservices

#### Tests unitaires

Un microservice peut être plus petit par définition, mais avec les tests unitaires, vous pouvez aller encore plus loin dans le détail. Un test unitaire se concentre sur la plus petite partie d'un logiciel testable pour déterminer si ce composant fonctionne comme il le devrait. L'ingénieur logiciel renommé, auteur et conférencier international Martin Fowler [décompose les tests unitaires](https://martinfowler.com/articles/microservice-testing/#testing-unit-introduction) en deux catégories :

1. **Tests unitaires sociables** : Cette méthode de test unitaire teste le comportement des modules en observant les changements dans leur état.
2. **Tests unitaires solitaires** : Cette méthode se concentre sur les interactions et les collaborations entre un objet et ses dépendances, qui sont remplacées par des doublures de test.

Bien que ces stratégies de test unitaire soient distinctes, Fowler soutient qu'elles ne sont pas en compétition – elles peuvent être utilisées en tandem pour résoudre différents problèmes de test.

Lors d'une discussion avec David Strauss, CTO de Pantheon, David m'a dit que « l'opportunité est que les microservices sont très simples pour effectuer des tests unitaires. »

#### Tests d'intégration

Avec les tests d'intégration, vous faites ce que cela semble être : tester les chemins de communication et les interactions entre les composants pour détecter les problèmes. [Selon Fowler](https://martinfowler.com/articles/microservice-testing/#testing-integration-introduction), un test d'intégration « exerce les chemins de communication à travers le sous-système pour vérifier toute hypothèse incorrecte que chaque module a sur la façon d'interagir avec ses pairs. »

Un test d'intégration teste généralement les interactions entre le microservice et les services externes, comme un autre microservice ou un datastore.

Pawel Ledwon, Platform Lead chez Pusher, m'a informé que son équipe « penche vers les tests d'intégration. Les tests unitaires sont encore utiles pour certaines abstractions, mais pour les fonctionnalités orientées utilisateur, ils sont difficiles à simuler ou à sauter des parties importantes du système. »

Tout le monde à qui j'ai parlé n'était pas fan du processus. L'opinion de Mosquera sur le sujet des tests d'intégration, par exemple, vaut la peine d'être notée :

> Les tests d'intégration sont très sujets aux erreurs et coûteux, en termes d'heures de travail. Le retour sur investissement n'est tout simplement pas là. Chaque test d'intégration individuel apporte une petite couverture marginale des cas d'utilisation.

#### Tests de bout en bout

Enfin, mais non des moindres, les tests de bout en bout, qui – comme mentionné précédemment – peuvent être une tâche difficile. Cela est dû au fait qu'ils impliquent de tester chaque partie mobile du microservice, en s'assurant qu'il peut atteindre les objectifs pour lesquels vous l'avez construit.

[Fowler a écrit](https://martinfowler.com/articles/microservice-testing/#testing-end-to-end-tips) ce qui suit :

> les tests de bout en bout peuvent également devoir tenir compte de l'asynchronisme dans le système, qu'il soit dans l'interface graphique ou dû à des processus backend asynchrones entre les services.

Il explique ensuite comment ces facteurs peuvent entraîner des « instabilités, des temps d'exécution excessifs des tests et des coûts supplémentaires de maintenance de la suite de tests. »

Le meilleur conseil que je puisse donner en matière de tests de bout en bout est de limiter le nombre de fois où vous essayez de les effectuer par service. Un équilibre sain entre les autres stratégies de test de microservices mentionnées – comme les tests unitaires et les tests d'intégration – vous aidera à éliminer les petits problèmes.

Un test de bout en bout est, par définition, plus grand, prend plus de temps et peut être beaucoup plus facile à mal faire. Pour garder vos coûts bas et éviter de perdre du temps, limitez les tests de bout en bout lorsque tous les autres moyens de test ont été épuisés, et comme un dernier sceau d'assurance qualité.

### Les défis des tests de microservices

Les microservices (par rapport à un monolithe) nécessitent des étapes supplémentaires, comme la gestion de plusieurs dépôts et branches, chacun avec ses propres schémas de base de données. Mais les défis peuvent aller plus loin que cela.

Voici quelques défis clés associés aux tests de microservices :

* **Disponibilité** : Puisque différentes équipes peuvent gérer leurs propres microservices, sécuriser la disponibilité d'un microservice (ou, pire encore, essayer de trouver un moment où tous les microservices sont disponibles en même temps), est difficile.
* **Tests fragmentés et holistiques** : Les microservices sont conçus pour fonctionner seuls et ensemble avec d'autres services faiblement couplés. Cela signifie que les développeurs doivent tester chaque composant isolément, ainsi que tout tester ensemble.
* **Lacunes de connaissances** : Particulièrement avec les tests d'intégration (que nous aborderons plus tard dans cet article), la personne qui effectue les tests devra avoir une forte compréhension de chaque service afin de rédiger des cas de test efficaces.

Selon Oleksiy Kovyrin, Head of Swiftype SRE chez Elastic,

> Un problème important que nous devons garder à l'esprit en travaillant avec des microservices est la stabilité de l'API et la versioning de l'API. Pour éviter de casser les applications dépendant d'un service, nous devons nous assurer que nous avons un solide ensemble de tests d'intégration pour les API de microservices et, en cas de changement cassant, nous devons fournir un moyen rétrocompatible pour que les clients migrent vers une nouvelle version à leur propre rythme afin d'éviter de grandes mises à jour d'API inter-services.

Stefan Zier, Chief Architect chez Sumo Logic, m'a également réitéré que les tests de microservices sont effectivement « très, très difficiles ».

« Surtout une fois que vous passez à un déploiement plus continu. Nous avons investi et continuons à investir assez lourdement dans les tests d'intégration, les tests unitaires, et nous en ferions beaucoup plus si nous avions les personnes pour le faire », m'a dit Zier.

Cela dit, il a admis que, à certains stades, lorsque Sumo Logic veut tester leurs services de manière holistique, « plus ou moins toute l'entreprise devient une équipe d'assurance qualité en un sens. »

### Solution : Cinq stratégies de test de microservices pour les startups

Oui, tester les microservices peut être difficile, mais [étant donné tous les avantages des microservices](https://buttercms.com/books/microservices-for-startups/should-you-always-start-with-a-monolith), y renoncer à cause des défis de test n'est pas la bonne voie. Pour relever ces défis, j'ai obtenu des informations de plusieurs CTO et distillé cinq stratégies qu'ils ont utilisées pour aborder avec succès les tests de microservices.

#### 1. La stratégie de documentation d'abord

Chris McFadden, VP of Engineering chez Sparkpost, a résumé la stratégie de documentation d'abord assez bien lors de notre discussion :

> Nous suivons une approche de documentation d'abord, donc toute notre documentation est en markdown sur GitHub. Nos documents d'API sont open source, donc tout est public. Ensuite, ce que nous ferons, c'est que avant que quiconque n'écrive des changements d'API ou soit une nouvelle API ou des changements à une API, ils mettront à jour la documentation d'abord, feront examiner ce changement pour s'assurer qu'il est conforme à nos conventions et normes d'API qui sont toutes documentées, et s'assurer qu'aucun changement cassant n'est introduit ici. Assurez-vous qu'il est conforme à nos conventions de nommage et ainsi de suite.

Si vous êtes prêt à aller plus loin, vous pourriez vous essayer au test de contrat d'API, qui – comme mentionné précédemment – implique d'écrire et d'exécuter des tests qui garantissent que le contrat explicite et implicite d'un microservice fonctionne comme il le devrait.

#### 2. La stratégie de pile complète dans une boîte

La stratégie de pile complète dans une boîte implique de répliquer un environnement cloud localement et de tout tester dans une seule instance vagrant (« $ vagrant up »). Le problème ? C'est extrêmement délicat, comme l'a expliqué l'ingénieur logiciel Cindy Sridharan d'Imgix dans un [article de blog](https://medium.com/@copyconstruct/testing-microservices-the-sane-way-9bb31d158c16) :

> J'ai eu une expérience directe avec ce sophisme dans une entreprise précédente où j'ai travaillé et où nous avons essayé de lancer toute notre pile dans une boîte vagrant [locale]. L'idée, comme vous pouvez l'imaginer, était qu'un simple vagrant up devrait permettre à n'importe quel ingénieur de l'entreprise (même les développeurs frontend et mobile) de pouvoir lancer la pile dans son intégralité sur leurs ordinateurs portables.

Sridharan continue en détaillant comment l'entreprise n'avait que deux microservices, un serveur API basé sur gevent et quelques travailleurs Python asynchrones en arrière-plan. Une configuration relativement simple, à tous égards.

« Je me souviens avoir passé toute ma première semaine dans cette entreprise à essayer de lancer avec succès la VM localement pour tomber sur une pléthore d'erreurs. Finalement, vers 16h00 le vendredi de ma première semaine, j'avais réussi à faire fonctionner la configuration Vagrant et tous les tests passaient localement. Je me souviens m'être senti incroyablement épuisé », a-t-elle raconté.

En outre, Stefan Zier, Chief Architect chez Sumo Logic, m'a expliqué que – en plus d'être difficile à réaliser – cette stratégie de test localisé ne s'adapte tout simplement pas :

« [Avec] un déploiement local, nous exécutons la plupart des services là-bas, donc vous obtenez un système entièrement fonctionnel et cela étire même les machines avec 16 Go de RAM assez dur. Donc cela ne s'adapte pas vraiment », a-t-il dit.

#### 3. La stratégie de test AWS

Cette troisième stratégie implique de lancer une infrastructure Amazon Web Services (AWS) pour chaque ingénieur afin de déployer et d'exécuter des tests. C'est une approche plus évolutive que la stratégie de pile complète dans une boîte discutée ci-dessus.

Zier a appelé cela une stratégie de « déploiement personnel, où tout le monde ici a son propre compte AWS ».

« Vous pouvez pousser le code qui est sur votre ordinateur portable vers AWS en environ dix minutes et simplement l'exécuter comme un vrai système », a-t-il dit.

#### 4. La stratégie des instances de test partagées

J'aime penser à cette quatrième stratégie comme un hybride entre la pile complète dans une boîte et le test AWS. Cela est dû au fait qu'elle implique des développeurs travaillant depuis leur propre station locale, tout en utilisant une instance séparée et partagée d'un microservice pour pointer leur environnement local lors des tests.

Steven Czerwinski, Head of Engineering chez Scaylr, a expliqué comment cela peut fonctionner en pratique :

> Certains de [nos] développeurs exécutent une instance séparée d'un microservice juste pour être utilisée pour tester les builds locaux. Imaginez que vous êtes un développeur, vous développez sur votre station de travail locale, et vous n'avez pas de moyen facile de lancer le parseur d'images. Cependant, votre constructeur local pointerait simplement vers un parseur d'images de test qui s'exécute dans l'infrastructure Google.

#### 5. La stratégie des services simulés

Et enfin, nous avons la stratégie de test des services simulés.

Zier a exposé l'approche de SumoLogic pour les tests de services simulés en me disant comment, « la simulation vous permet d'écrire ces marques ou 'simulations' de microservices qui se comportent comme s'ils étaient le bon service et ils s'annoncent dans notre découverte de service comme s'ils étaient un vrai service, mais ils ne sont qu'une imitation factice », a-t-il expliqué.

Par exemple, tester un service peut nécessiter que le service prenne conscience qu'un utilisateur effectue un ensemble de tâches. Avec les services simulés, vous pouvez prétendre que l'utilisateur (et ses tâches) a eu lieu sans les complexités habituelles qui accompagnent cela. Cette approche est beaucoup plus légère par rapport à l'exécution des services dans leur intégralité.

### Outils pour vous aider à tester les microservices

Voici une liste d'outils qui m'ont été bénéfiques lors de mes propres expériences de test de microservices, renforcée par quelques recommandations de la [communauté de CTO et de développeurs seniors](https://buttercms.com/books/microservices-for-startups/#contributors) :

* [Hoverfly](https://hoverfly.io/) : simuler la latence et les échecs de l'API.
* [Vagrant](https://www.vagrantup.com/) : construire et maintenir des environnements de développement logiciel virtuels portables
* [VCR](https://github.com/vcr/vcr) : un outil de test unitaire
* [Pact](https://docs.pact.io/) : frameworks de test de contrats pilotés par le consommateur.
* [Apiary](https://apiary.io/) : outil de documentation d'API
* [API Blueprint](https://apiblueprint.org/) : concevoir et prototyper des API
* [Swagger](https://swagger.io/) : concevoir et prototyper des API

### Tests de microservices : difficiles, mais ça en vaut la peine

Tester vos microservices ne sera pas une promenade de santé, mais le travail supplémentaire en vaut la peine pour les avantages d'avoir une architecture de microservices.

De plus, les stratégies de test de microservices adoptées par des entreprises comme SumoLogic et Scaylr devraient aider à simplifier le processus. Voici un bref récapitulatif de ces stratégies :

1. La stratégie de documentation d'abord
2. La stratégie de pile complète dans une boîte
3. La stratégie de test AWS
4. La stratégie des instances de test partagées
5. La stratégie des services simulés

Naturellement, vous devrez peut-être ajuster chaque stratégie pour correspondre à vos circonstances uniques, mais avec un bon vieux essai et erreur, votre stratégie de test de microservices devrait se concrétiser.

*Si vous avez aimé cet article, aidez-le à se diffuser en applaudissant ci-dessous ! Pour plus de contenu comme celui-ci, suivez-nous sur [Twitter](https://twitter.com/ButterCMS) et [abonnez-vous](https://buttercms.com/blog/) à notre blog.*

*Jake Lumetta est le PDG de [ButterCMS](https://buttercms.com/), et publie [Microservices for Startups](https://buttercms.com/books/microservices-for-startups/).*

*Et si vous voulez ajouter un blog ou un CMS à votre site web sans vous embêter avec Wordpress, [vous devriez essayer Butter CMS](https://buttercms.com/).*