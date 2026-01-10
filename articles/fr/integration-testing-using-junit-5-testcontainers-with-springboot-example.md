---
title: Comment effectuer des tests d'intégration en utilisant JUnit 5 et TestContainers
  avec SpringBoot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-26T15:46:39.000Z'
originalURL: https://freecodecamp.org/news/integration-testing-using-junit-5-testcontainers-with-springboot-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/testcontainers-logo.png
tags:
- name: Docker
  slug: docker
- name: Software Testing
  slug: software-testing
- name: spring-boot
  slug: spring-boot
- name: Testing
  slug: testing
seo_title: Comment effectuer des tests d'intégration en utilisant JUnit 5 et TestContainers
  avec SpringBoot
seo_desc: "By Sameer Shukla\nTestContainers is a library that helps you run module-specific\
  \ Docker containers to simplify Integration Testing. \nThese Docker containers are\
  \ lightweight, and once the tests are finished the containers get destroyed.\nIn\
  \ the article ..."
---

Par Sameer Shukla

TestContainers est une bibliothèque qui vous aide à exécuter des conteneurs Docker spécifiques à un module pour simplifier les tests d'intégration. 

Ces conteneurs Docker sont légers, et une fois les tests terminés, les conteneurs sont détruits.

Dans cet article, nous allons comprendre ce qu'est TestContainers et comment il vous aide à écrire des tests plus fiables. 

Nous allons également comprendre les composants importants (annotations et méthodes) de la bibliothèque qui vous aident à écrire les tests. 

Enfin, nous apprendrons également à écrire un test d'intégration propre dans SpringBoot en utilisant la bibliothèque TestContainers et ses composants. 

## Limites des tests avec une base de données H2 en mémoire

L'approche la plus courante pour les tests d'intégration aujourd'hui est d'utiliser une base de données H2 en mémoire. Mais cette méthode présente certaines limites.

Tout d'abord, disons que nous utilisons la version 8.0 de MySQL en production, mais que nos tests d'intégration utilisent H2. Nous ne pourrons jamais exécuter nos tests pour la version de la base de données en production.       

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-303.png)
_Application SpringBoot avec MySQL DB et H2_

Deuxièmement, les cas de test sont moins fiables car en production nous utilisons une base de données complètement différente et les tests pointent vers H2. L'application peut rencontrer des problèmes en production, mais les tests d'intégration peuvent réussir. 

J'essayais d'accéder à mon service RESTful en local et j'ai rencontré cette erreur : 

"**Caused by: org.postgresql.util.PSQLException: FATAL: database "example_db" does not exist**". 

Cela est arrivé à cause d'un problème de permission, mais les tests en local ont fonctionné correctement.

Et enfin, comme documenté [ici](http://h2database.com/html/features.html#compatibility), H2 est compatible avec d'autres bases de données seulement jusqu'à un certain point. Il y a quelques domaines où H2 est incompatible. Si vous devez utiliser des "nativeQueries" dans une application SpringBoot, par exemple, alors utiliser H2 peut causer des problèmes.

## Entrée de la bibliothèque TestContainers

En utilisant TestContainers, nous pouvons surmonter les limites de H2.

* Les tests d'intégration pointeront vers la même version de la base de données que celle en production. Ainsi, nous pouvons lier notre image de base de données TestContainer à la même version en production.
* Les tests d'intégration sont beaucoup plus fiables car à la fois l'application et les tests utilisent le même type et la même version de base de données et il n'y aura pas de problèmes de compatibilité dans les cas de test.

## Qu'est-ce que TestContainers ?

La bibliothèque TestContainers est une API wrapper sur Docker. Lorsque nous écrivons du code pour créer un conteneur, cela peut être traduit en une commande Docker, par exemple :                                    

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-283.png)
_Création de MySQLContainer_

Ce code peut être traduit en quelque chose comme ceci :

```docker 
docker run -d --env MYSQL_DATABASE=example_db --env MYSQL_USER=test --env MYSQL_PASSWORD=test 'mysql:latest' 
```

TestContainers a une méthode nommée "withCommand". Vous l'utilisez pour définir la commande qui doit être exécutée à l'intérieur du conteneur Docker, ce qui confirme que TestContainers est une API wrapper sur Docker.

TestContainers télécharge les images MySQL, Postgres, Kafka, Redis et les exécute dans un conteneur. Le MySQLContainer exécutera une base de données MySQL dans un conteneur et les cas de test pourront s'y connecter sur la machine locale. Une fois l'exécution terminée, la base de données sera supprimée - elle est simplement effacée de la machine. Dans les cas de test, nous pouvons démarrer autant d'images de conteneurs que nous le souhaitons.

TestContainers prend en charge JUnit 4, JUnit 5 et Spock. Si vous allez sur le site TestContainers.org, visitez simplement la section QuickStart qui explique comment l'utiliser :                    

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-284.png)
_TestContainers.org comment démarrer avec Test Framework_

TestContainers prend en charge presque toutes les bases de données, de MySQL et Postgres à CockroachDB. Vous pouvez trouver plus d'informations à ce sujet sur le site TestContainers.org sous la section Modules :                                              

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-285.png)
_Prise en charge des modules de base de données par TestContainers_

TestContainers prend également en charge les modules Cloud comme GCloud Module et Azure Module. Si votre application s'exécute sur Google Cloud, alors TestContainers prend en charge Cloud Spanner, Firestore, Datastore et ainsi de suite. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-286.png)
_Prise en charge du module GCloud par TestContainers_

Dans cet article jusqu'à présent, nous n'avons discuté que des bases de données, mais TestContainers prend en charge divers autres composants comme Kafka, SOLR, Redis, et plus encore.

## Comment utiliser la bibliothèque TestContainers

Dans cet article, nous allons explorer TestContainers avec JUnit 5. Pour implémenter TestContainers, nous devons comprendre quelques annotations, méthodes et bibliothèques importantes de TestContainers que nous devons implémenter dans notre projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-288.png)
_Bibliothèques TestContainers_

### Annotations dans TestContainers

Deux annotations importantes sont requises dans nos tests pour que TestContainers fonctionne : @TestContainers et @Container.

@TestContainer est une extension JUnit-Jupiter qui démarre et arrête automatiquement les conteneurs utilisés dans les tests. Cette annotation trouve les champs marqués avec @Container et appelle les méthodes spécifiques du cycle de vie du conteneur. Ici, les méthodes du cycle de vie de MySQLContainer seront invoquées.                                              

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-289.png)
_MySQLContainer_

Le MySQLContainer est déclaré comme statique car si nous déclarons Container comme statique, alors un seul conteneur est démarré et il sera partagé entre toutes les méthodes de test.

Si c'est une variable d'instance, alors un nouveau conteneur est créé pour chaque méthode de test.

## Méthodes de la bibliothèque TestContainers

Il y a quelques méthodes importantes dans la bibliothèque TestContainers que vous utiliserez dans les tests. Il est bon de les connaître avant d'utiliser la bibliothèque.

* **withInitScript** : En utilisant 'withInitScript', nous pouvons exécuter le .SQL pour définir le schéma, les tables, et plus encore ajouter les données dans la base de données. En bref, cette méthode est utilisée pour exécuter le .SQL pour remplir la base de données.
* **withReuse** (true) : En utilisant la méthode 'withReuse', nous pouvons activer la réutilisation des conteneurs. Cette méthode fonctionne bien en conjonction avec l'activation de la propriété 'testcontainers.reuse.enable:true' dans le fichier '.testcontainers.properties'.
* **start** : nous utilisons cela pour démarrer le conteneur.
* **withClasspathResourceMapping** : Cela mappe une ressource (fichier ou répertoire) sur le classpath à un chemin à l'intérieur du conteneur. Cela ne fonctionnera que si vous exécutez vos tests en dehors d'un conteneur Docker.
* **withCommand** : Définit la commande qui doit être exécutée à l'intérieur du conteneur Docker.
* **withExposedPorts** : Utilisé pour définir le port sur lequel le conteneur écoute.
* **withFileSystemBind** : Utilisé pour mapper un fichier / répertoire du système de fichiers local dans le conteneur.

## Cas d'utilisation de TestContainers

Dans l'exemple que nous allons examiner maintenant, l'application communiquera uniquement avec la base de données et écrira les tests d'intégration pour celle-ci en utilisant TestContainers. Ensuite, nous étendrons le cas d'utilisation en implémentant Redis entre les deux.

Si les données existent dans le cache Redis, elles seront retournées, sinon elles seront sauvegardées et récupérées dans la base de données en fonction de la clé.              

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-308.png)
_Cas d'utilisation_

Le service est simple. Il a 2 endpoints - le premier est pour créer un utilisateur et le second est pour trouver un utilisateur par email. Si l'utilisateur est trouvé, il est retourné, sinon nous obtenons un 404. Le code de la classe de service ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-291.png)
_Composant de service_

Nous allons écrire des tests pour cette classe. Vous pouvez trouver l'ensemble du code source [ici](https://github.com/sameershukla/testcontainers_demo ) :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-292.png)
_Classe de test_

La classe de test est marquée avec l'annotation @TestContainers qui démarre/arrête le conteneur. Nous utilisons l'annotation @Container pour appeler les méthodes spécifiques du cycle de vie du conteneur. 

De plus, le 'MySQLContainer' est déclaré comme statique car alors un seul conteneur est démarré. Ensuite, il est partagé entre toutes les méthodes de test (nous avons déjà discuté de l'importance de ces annotations).                             

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-293.png)
_BeforeAll_

Ensuite, nous devons écrire une méthode de configuration marquée avec @BeforeAll, où nous avons activé la méthode 'withReuse'. Cela nous aide à réutiliser les conteneurs existants. Nous utilisons la méthode 'withInitScript' pour exécuter le fichier '.sql' puis démarrer le conteneur.                                              

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-294.png)
_Surcharge des propriétés_

@DynamicPropertySource nous aide à remplacer les propriétés déclarées dans le fichier de propriétés. Nous écrivons cette méthode pour permettre à TestContainers de créer l'URL, le nom d'utilisateur et le mot de passe par lui-même - sinon nous pourrions rencontrer des erreurs. 

Par exemple, en supprimant le nom d'utilisateur et le mot de passe, nous pourrions rencontrer une erreur 'Access denied' qui pourrait nous confondre. Il est donc préférable de permettre à TestContainer d'assigner ces propriétés dynamiquement par lui-même.

C'est tout - nous sommes prêts à exécuter les cas de test :       

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-295.png)
_Cas de test_

Exécutez @AfterAll pour arrêter le conteneur, sinon il peut continuer à s'exécuter sur votre machine locale si vous ne l'arrêtez pas explicitement.                                               

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-296.png)

## Comment utiliser GenericContainer

GenericContainer est le conteneur le plus flexible. Il facilite l'exécution de n'importe quelle image de conteneur dans GenericContainer.

Maintenant que nous avons Redis en place, tout ce que nous devons faire dans notre cas de test est de démarrer un GenericContainer avec l'image Redis.        

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-297.png)
_GenericContainer pour Redis_

Ensuite, nous démarrons le conteneur Redis générique dans @BeforeAll et l'arrêtons avec la méthode de démontage @AfterAll.                     

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-298.png)
_Démarrage des conteneurs_

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-299.png)
_Arrêt des conteneurs_

## Conclusion

Il est extrêmement facile d'utiliser TestContainers dans notre application pour écrire de meilleurs tests. La courbe d'apprentissage n'est pas trop raide et il prend en charge divers modules différents, allant de diverses bases de données comme Kafka, Redis et autres. 

Écrire des tests en utilisant TestContainers rend nos tests beaucoup plus fiables. Le seul inconvénient est que les tests sont lents par rapport à H2. Cela est dû au fait que H2 est en mémoire et que TestContainers prend du temps pour télécharger l'image, exécuter le conteneur et mettre en place l'ensemble de la configuration que nous avons discutée dans cet article.