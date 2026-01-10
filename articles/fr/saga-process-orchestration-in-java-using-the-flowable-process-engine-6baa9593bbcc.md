---
title: Orchestration de processus Saga en Java à l'aide du moteur de processus Flowable
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-01T22:05:19.000Z'
originalURL: https://freecodecamp.org/news/saga-process-orchestration-in-java-using-the-flowable-process-engine-6baa9593bbcc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Hcv7JuT-UuVxnTO2TkRoUg.jpeg
tags:
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: workflow
  slug: workflow
seo_title: Orchestration de processus Saga en Java à l'aide du moteur de processus
  Flowable
seo_desc: 'By Felix Kuestahler

  Define a Saga Process Controller in Flowable by using the Camel Task for system
  integration

  Introduction

  In this tutorial, I did an assessment of the capability of Flowable to act as a
  Saga Process Controller.


  _Photo by [Unsplash...'
---

Par Felix Kuestahler

#### Définir un contrôleur de processus Saga dans Flowable en utilisant la tâche Camel pour l'intégration de systèmes

### Introduction

Dans ce tutoriel, j'ai évalué la capacité de Flowable à agir en tant que contrôleur de processus Saga.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hcv7JuT-UuVxnTO2TkRoUg.jpeg)
_Photo de [Unsplash](https://unsplash.com/photos/uYkdJEYNwSM?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Geran de Klerk</a> sur <a href="https://unsplash.com/collections/1988198/integrous?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> Flowable fournit un ensemble de moteurs de processus métier open source, compacts et hautement efficaces. Ils offrent une plateforme de workflow et de gestion des processus métier (BPM) pour les développeurs, les administrateurs système et les utilisateurs métier. En son cœur se trouve un moteur de processus BPMN dynamique, ultra-rapide et éprouvé, accompagné de tables de décision DMN et de moteurs de gestion de cas CMMN, le tout écrit en Java. Ils sont sous licence open source Apache 2.0, avec une communauté engagée. ([Lien](https://www.flowable.org/))

Comme on peut le voir, Flowable se positionne comme une plateforme de workflow et de gestion des processus métier. Ce que nous voulons comprendre, c'est la faisabilité de Flowable dans le contexte de l'orchestration de services de bas niveau, définie comme l'orchestration Saga.

Consultez l'excellent article suivant de Bernd Rücker pour obtenir un aperçu de la manière d'aborder les « [Transactions commerciales sans validation en deux phases](https://blog.bernd-ruecker.com/saga-how-to-implement-complex-business-transactions-without-two-phase-commit-e00aa41a1b1b) »

> Le modèle Saga décrit comment résoudre les transactions (commerciales) distribuées sans validation en deux phases (two-phase-commit), car celle-ci ne passe pas à l'échelle dans les systèmes distribués. L'idée de base est de décomposer la transaction globale en plusieurs étapes ou activités. Seules les étapes internes peuvent être effectuées dans des transactions atomiques, mais la cohérence globale est prise en charge par la Saga. La Saga a la responsabilité soit de mener à bien la transaction commerciale globale, soit de laisser le système dans un état de terminaison connu. ([Lien](https://blog.bernd-ruecker.com/saga-how-to-implement-complex-business-transactions-without-two-phase-commit-e00aa41a1b1b))

Dans cet article, je ne traite pas de la transaction de compensation. Je me concentrerai sur le squelette de base nécessaire pour exécuter l'orchestration de processus Saga. Il s'agit principalement d'une combinaison de la capacité de workflow fournie par Flowable combinée à la puissance d'Apache Camel (un framework d'intégration Java basé sur les [modèles EIP](https://www.enterpriseintegrationpatterns.com/)). Apache Camel est un citoyen de première classe dans Flowable via ce qu'on appelle la « Tâche Camel ».

### Framework d'application Spring Boot

Flowable est par nature une application basée sur Spring Boot. Elle bénéficie de toutes les fonctionnalités fournies par Spring Boot.

> Spring Boot facilite la création d'applications basées sur Spring, autonomes et de qualité production, que vous pouvez « juste exécuter ».

> Nous adoptons une approche tranchée de la plateforme Spring et des bibliothèques tierces afin que vous puissiez commencer avec un minimum de tracas. La plupart des applications Spring Boot nécessitent très peu de configuration Spring. ([Lien](https://spring.io/projects/spring-boot))

Spring Boot repose sur le principe de la convention plutôt que la configuration. Notre fichier _build.gradle_ ressemble à ceci :

Le fichier de build gradle est assez compact et se compose des dépendances suivantes :

* Dépendances du framework Spring Boot
* Dépendances du framework intégré Flowable Spring Boot
* Dépendances du framework intégré Camel Boot
* Ainsi que H2, une base de données en mémoire requise pour le moteur de traitement avec état de Flowable

C'est tout, c'est plutôt simple.

#### Spring Boot et Flowable

En introduisant les dépendances Flowable ci-dessus (consultez la [Documentation de l'application Flowable Spring Boot](https://www.flowable.org/docs/userguide/index.html#springSpringBoot)) et en utilisant l'annotation _@SpringBootApplication_, beaucoup de choses se sont passées en coulisses :

* Une source de données en mémoire est créée automatiquement (car le pilote H2 est dans le classpath). Elle est transmise à la configuration du moteur de processus Flowable
* Les beans Flowable ProcessEngine, CMMNEngine, DMNEngine, FormEngine, ContentEngine et IdmEngine ont été créés et exposés
* Tous les services Flowable sont exposés en tant que beans Spring
* L'exécuteur de tâches Spring (Job Executor) est créé

Vous pouvez affiner l'application Flowable — par exemple, au cas où vous n'auriez besoin que d'un sous-ensemble des moteurs fournis, reportez-vous à la [Liste des starters Flowable](https://www.flowable.org/docs/userguide/index.html#springBootFlowableStarter) suivante.

#### Spring Boot et Camel

Le framework d'intégration Apache Camel est inclus via les deux dépendances suivantes :

```
implementation 'org.apache.camel:camel-spring-boot-starter:2.23.0'implementation 'org.flowable:flowable-camel:6.4.1'
```

* La première dépendance lie Camel au framework de l'application Spring Boot,
* La deuxième dépendance lie Camel au moteur de processus Flowable, via la tâche dite Camel Task, qui permet de déléguer toute intégration de système tiers dans un modèle de processus Flowable à une route Camel (plus de détails à ce sujet plus tard)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gXYo1XbpKyBN8UNIvYOD-w.png)

### Initialisation de l'application Flowable Boot

Pour faire fonctionner une application Spring Flowable minimale, suivez ces étapes :

Introduisez un fichier application.properties avec les propriétés suivantes.

```
management.endpoints.web.exposure.include=*management.endpoint.health.show-details=when_authorizedflowable.idm.password-encoder=spring_delegating
```

Fournissez une classe SecurityConfiguration.

Et chargez trois utilisateurs de test au démarrage.

Enfin, nous fournissons un contrôleur REST pour effectuer une vérification initiale de notre application Spring Boot Flowable de base.

Démarrez l'application Flowable via la commande

```
gradle bootApp
```

Et ouvrez le navigateur sur [http://localhost:8080](http://localhost:8080). Un nom d'utilisateur et un mot de passe vous seront demandés. Indiquez `flowfest` et le mot de passe `test`. Vous devriez maintenant être connecté et le message d'accueil devrait s'afficher.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7bxOg44MynsRr-IJXanD3A.png)

Ok, bien joué, notre puissante application Spring est prête et nous pouvons continuer.

### Flowable Modeler

Notre processus Saga sera modélisé dans le Flowable Modeler en utilisant la fonctionnalité de modèle BPM. Une introduction rapide est donnée dans ce [tutoriel Flowable](https://paulhh.wordpress.com/2017/01/31/flowable-6-instant-gratification/).

Via la [page d'accueil de Flowable](https://www.flowable.org/), téléchargez la dernière version (version actuelle de Flowable v4.6.1) qui est un fichier zip contenant un répertoire war avec 5 fichiers WAR.

Déployez ces 5 fichiers war par exemple sur un serveur de test Tomcat et lancez :

[http://localhost:8080/flowable-modeler](http://cloudburo2:8080/flowable-modeler/#/processes)/ il vous sera demandé de vous connecter, indiquez `admin` avec le mot de passe `test`

![Image](https://cdn-media-1.freecodecamp.org/images/1*S7UF3czTzNRQv_anLYkjQQ.png)
_Page de connexion Flowable_

Après une connexion réussie, vous serez dirigé vers le tableau de bord des modèles de processus métier (qui sera vide au départ).

![Image](https://cdn-media-1.freecodecamp.org/images/1*c6uVzhNkBfCqr8Othmb4QQ.png)

Vous êtes prêt à tester. La configuration par défaut de Flowable introduit une base de données persistante. Cela garantit que vos artefacts de modèle seront stockés et disponibles après le redémarrage du serveur d'application.

Une modification manuelle mineure a été nécessaire sur un serveur d'application Tomcat standard Ubuntu pour que le chargement du Flowable Modeler réussisse. Dans le répertoire des artefacts tomcat (/var/lib/tomcat8), j'ai dû créer un répertoire `flowable-db` avec les droits utilisateur/groupe `tomcat8:tomcat8`, sinon le démarrage de l'application échouait (du fait que les paquets apt tomcat8 sont installés par root).

![Image](https://cdn-media-1.freecodecamp.org/images/1*L8s7nstYSmTa_Eqi88fTHw.png)

### Flowable Saga : Processus Hello World

Dans Flowable, nous modélisons notre processus hello world, qui se compose de 4 étapes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hrwfgxuel0FA_xOl329uqQ.png)
_Le Flowable Modeler open source (BPMN, CMN, DMN et formulaires UI)_

* La tâche _Initialize Variables_ définit une variable d'entrée que nous voulons traiter dans notre tâche Camel
* La tâche _Async Camel_ déléguera le processus à une route Camel, qui traite la variable d'entrée. Nous utiliserons des routes Camel pour tout type d'intégration de système externe. Cette tâche est appelée de manière asynchrone, c'est-à-dire qu'après avoir délégué le traitement à la route Camel, la tâche est terminée et passe à la…
* La tâche _Receive Process Response_ est une tâche de réception asynchrone, qui attend la fin du traitement de la route Camel. Après le déclenchement de l'événement, les données traitées seront remises à la…
* La tâche _Save Variable_, qui extrait le résultat du processus.

Comme vous le verrez plus tard en utilisant la puissance de Camel pour l'intégration, nous pouvons introduire élégamment un comportement asynchrone dans notre flux de processus Saga avec une seule ligne de code.

La structure du projet est simple. Nous avons besoin de trois classes pour implémenter ce flux de processus, ainsi que du modèle de processus BPMN :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WN4qRXB1JLaw5G9trAzBQg.png)

Compte tenu du fait que nous pouvons avoir plusieurs flux de processus Saga dans une application Spring Flowable, nous nous efforçons d'établir une règle de packaging claire :

* Chaque modèle de processus BPMN a un identifiant unique, dans notre cas l'identifiant est `saga1Process`. Par conséquent
* tout type de tâche référencée dans le modèle de processus se trouve dans un package `task.saga1`
* tout type de route Camel référencée dans le modèle de processus se trouve dans un package `route.saga1`

### InitVariablesTask

Nous simulons ici la récupération de certaines données d'entrée fournies par une application appelante. Nous définissons la variable `name` sur `Hello World`. Cette variable fait maintenant partie du contexte du processus.

Dans le modèle, nous associons notre classe à notre tâche de service :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tIfsbnYIFpsI1_y-QAjbeA.png)

### Route Camel

Passons maintenant à la tâche Camel qui est une tâche de service Camel, que nous configurons comme asynchrone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MMTOI93toIg528lJ9UTJUA.png)

Comme on peut le voir, la seule chose que nous configurons dans notre tâche Camel est l'ID de la tâche de service et nous activons le flag Asynchronous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uzQyWtOi9haOaNVfNdY2Gg.png)

La liaison de la tâche de service à la route Camel se fait dans la classe de route, via des conventions de nommage. L'ID global du processus est `saga1Process` et l'ID de la tâche est `camelAsyncTask`. Regardons donc la classe Camel Route. Nous établissons la route entrante à la ligne 17 vers notre tâche de service Camel

```
from("flowable:saga1Process:camelAsyncTask")
```

et nous placerons le message reçu dans le composant Camel seda (ligne 18), qui découplera la tâche de service Camel du traitement de manière asynchrone (comme dit, avec une seule ligne de code)

```
.to("seda:continueAsync")
```

#### Une brève introduction au composant SEDA

Nous utiliserons le composant Camel **seda:**. Celui-ci fournit un comportement asynchrone [SEDA](https://en.wikipedia.org/wiki/Staged_event-driven_architecture). Les messages sont échangés sur une [BlockingQueue](http://java.sun.com/j2se/1.5.0/docs/api/java/util/concurrent/BlockingQueue.html) et les consommateurs sont invoqués dans un thread séparé de celui du producteur.

> L'**architecture pilotée par événements par étapes** (**SEDA**) fait référence à une approche de l'[architecture logicielle](https://en.wikipedia.org/wiki/Software_architecture) qui décompose une [application](https://en.wikipedia.org/wiki/Computer_program) complexe pilotée par événements en un ensemble d'étapes connectées par des files d'attente. Elle évite les frais généraux élevés associés aux [modèles de concurrence](https://en.wikipedia.org/wiki/Concurrency_(computer_science)) basés sur les [threads](https://en.wikipedia.org/wiki/Thread_(computer_science)) (c'est-à-dire le verrouillage, le déverrouillage et l'interrogation des verrous), et découple la planification des événements et des threads de la logique de l'application.

Comme nous pouvons le voir après la récupération du message, nous simulons un certain traitement

```
.log(LoggingLevel.INFO, logger, "External System Processing...").transform().simple("Processed: ${property.input}, { Result: OK }");
```

Enfin, nous renvoyons le résultat à notre processus Saga

```
from("seda:continueAsync")        .to("flowable:saga1Process:receiveAsyncTask");
```

C'est tout. Ainsi, tout type d'intégration de système externe peut être délégué à des routes Camel, qui fournissent des concepts d'intégration puissants. Par exemple, au lieu d'implémenter un mécanisme de nouvelle tentative dans le cadre du processus Saga, on peut utiliser un gestionnaire d'exceptions avec une politique de relivraison (également connue sous le nom de `RedeliveryErrorHandler` dans Camel). Ce gestionnaire d'erreurs vous permettra de définir le nombre de tentatives ainsi que des éléments tels que le délai entre les tentatives, etc.

```
public void configure()  {    // ExceptionHandler with RedliveryPolicy    errorHandler(defaultErrorHandler()            .maximumRedeliveries(3)            .backOffMultiplier(4)            .retryAttemptedLogLevel(LoggingLevel.WARN));
```

### Tâche Receive Async Response

Cette tâche de réception de service servira de pont de retour depuis Camel, comme expliqué ci-dessus.

### Tâche Save Output

Enfin, nous affichons le message Camel produit qui a été transmis.

### Application Spring Boot

Dans la classe `_SpringBootApplication_`, nous introduisons un `CommandLineRunner` qui déclenchera notre modèle de processus.

Si nous redémarrons notre application :

```
gradle bootApp
```

nous pouvons voir sur la console le résultat du traitement de notre processus Saga.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q0AWYjlWCTdhWr2gV6zH5A.png)

Enfin, vous pouvez également exécuter des tests unitaires via

```
gradle test
```

Pour résumer : comme on peut le voir, Flowable permet, avec le concept de tâche Camel, une intégration puissante de systèmes tiers dans un flux de processus BPMN. Cette approche garantit que le flux d'orchestration ne sera pas surchargé par la logique d'intégration d'entreprise qui est déportée vers les routes Camel.

Vous pouvez consulter le code ici :

[**talfco/tutorial-flowable-saga**](https://github.com/talfco/tutorial-flowable-saga)  
[_Un tutoriel qui décrit l'approche pour utiliser Flowable et Camel pour un gestionnaire de processus Saga… github.com](https://github.com/talfco/tutorial-flowable-saga)

Bon codage !