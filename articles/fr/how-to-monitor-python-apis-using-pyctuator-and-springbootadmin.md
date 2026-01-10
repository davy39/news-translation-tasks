---
title: Comment surveiller les API Python à l'aide de Pyctuator et SpringBootAdmin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-02T15:02:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-monitor-python-apis-using-pyctuator-and-springbootadmin
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-01-at-12.18.52-AM.png
tags:
- name: api
  slug: api
- name: Python
  slug: python
- name: spring-boot
  slug: spring-boot
seo_title: Comment surveiller les API Python à l'aide de Pyctuator et SpringBootAdmin
seo_desc: "By Sameer Shukla\nActuator endpoints help us monitor our services. By using\
  \ actuators, we can gain a lot of information about what’s going on. \nSpringBoot\
  \ has a number of in-built actuators, and it also allows us to create our own Actuator\
  \ Endpoint. \n..."
---

Par Sameer Shukla

Les endpoints Actuator nous aident à surveiller nos services. En utilisant les actuators, nous pouvons obtenir beaucoup d'informations sur ce qui se passe. 

SpringBoot dispose de plusieurs actuators intégrés et permet également de créer notre propre endpoint Actuator. 

Pour les frameworks écrits en Python comme Flask ou FastAPI, nous pouvons incorporer des actuators en intégrant une bibliothèque appelée Pyctuator. 

Dans cet article, je vais expliquer comment surveiller des applications écrites en FastAPI en utilisant la bibliothèque Pyctuator. Je vais également vous montrer comment gérer les endpoints Actuator à l'aide du serveur SpringBootAdmin.

## Qu'est-ce que les Actuators ?

Nous utilisons les actuators pour surveiller et gérer l'utilisation des applications en production. Ces informations d'utilisation nous sont exposées via des endpoints REST. 

Par exemple, nous pouvons accéder aux logs de l'application en production, aux détails de l'environnement et aux traces HTTP. Et si quelque chose ne va pas dans l'application, nous pouvons même accéder au "threaddump" de l'application à des fins de débogage.

Voici quelques exemples d'endpoints Actuator importants :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-16.png)
_Actuators_

## Qu'est-ce que Pyctuator ?

Les Actuators sont devenus populaires grâce à SpringBoot, mais vous pouvez les implémenter dans des frameworks comme FastAPI ou Flask en intégrant un module appelé Pyctuator.

Pyctuator est un module Python, qui est une implémentation partielle des Actuators de SpringBoot. Pyctuator est géré par SolarEdge.

Certains des actuators pris en charge par Pyctuator sont :

* /health : Cet endpoint dans Pyctuator a une surveillance intégrée pour Redis et MySQL
* /env
* /metrics 
* /logfile
* /threaddump 
* /httptrace 
* /loggers

## Qu'est-ce que SpringBootAdmin ?

Imaginez un service ayant tous ces actuators pour vérifier les métriques, les traces HTTP, les threaddumps, etc. Il serait assez fastidieux d'invoquer chacun d'eux individuellement pour vérifier ce qui se passe dans le service. Et si nous avons plusieurs services et que chacun d'eux a ses propres endpoints Actuator, cela rend la surveillance encore plus difficile.

C'est là que vous pouvez utiliser SpringBootAdmin pour gérer et surveiller les applications.

En résumé, SpringBootAdmin fournit un tableau de bord pratique pour tous les endpoints Actuator en un seul endroit.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-30.png)
_Tableau de bord Admin_

## Cas d'utilisation pour Pyctuator

Le cas d'utilisation est simple : nous allons développer un service RESTful en utilisant le framework FastAPI et configurer les actuators dans le service en utilisant le module Pyctuator. 

Le service a 3 endpoints comme montré dans la documentation de l'API (Swagger) ci-dessous

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-31.png)
_Documentation de l'API_

* GET /users : Retourne tous les utilisateurs existants dans le système. 
* POST /users : Crée un utilisateur
* GET /users/{id} : Retourne un utilisateur avec un identifiant donné

Vous pouvez trouver le code [ici](https://github.com/sameershukla/fastapi-pyctuator).

Dans le service User-Service, nous allons activer les actuators en utilisant Pyctuator et les surveiller en utilisant le tableau de bord SpringBootAdmin. Nous allons également explorer comment nous pouvons améliorer l'actuator /health pour surveiller Redis.

Pour configurer les Actuators, nous devons d'abord installer "pyctuator". Vous pouvez le faire en utilisant la commande "pip install pyctuator". 

Après l'installation, l'instantiation de l'objet Pyctuator est le point d'entrée pour voir les actuators intégrés dans un framework web. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-47.png)
_Constructeur Pyctuator_

Avant d'instancier Pyctuator, si vous accédez à l'endpoint /pyctuator, vous obtiendrez le message "Not Found" :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-91.png)
_Sans configuration Pyctuator_

Après l'instantiation, en accédant à l'endpoint /pyctuator, vous verrez tous les actuators activés par défaut. Cela est dû au fait que nous avons défini "pyactuator_endpoint_url" dans Pyctuator. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-93.png)
_Après configuration Pyctuator_

Je vous recommande vivement de consulter l'objet Pyctuator car il explique quels sont les arguments obligatoires et facultatifs que nous devons fournir.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-114.png)
_Comprendre les paramètres du constructeur_

Les paramètres obligatoires sont :

* app – instance de FastAPI ou Flask 
* le nom de l'application – affiché dans la section info dans SpringBootAdmin 
* "pyctuator_endpoint_url" – ce que nous avons vu qui retourne tous les endpoints Actuator   
* "registration_url" – vous comprendrez celui-ci bientôt.

## Comment améliorer l'endpoint /health

Vous pouvez améliorer l'endpoint /health dans Pyctuator pour surveiller les bases de données Redis ou MySQL. Supposons que vous utilisiez Redis dans votre application – alors nous devons utiliser RedisHealthProvider et lui passer l'instance redis.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-174.png)
_Santé Redis_

## Comment démarrer le serveur SpringBootAdmin

Pour exécuter le serveur SpringBootAdmin en local, nous avons deux options : premièrement, nous pouvons le faire en créant manuellement SpringBootAdmin en allant sur start.spring.io et en ajoutant des bibliothèques.

Spring Web & Spring Boot Admin (Server) :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-175.png)
_Création de SpringBootAdmin_

La deuxième option est d'exécuter une image Docker :

```docker 
docker run --rm --name spring-boot-admin -p 8080:8080 michayaak/spring-boot-admin:2.2.3-1



```

Une fois le serveur admin démarré, nous devons fournir l'"registration_url" au constructeur Pyctuator comme discuté précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-178.png)
_Enregistrement de l'URL dans SpringBootAdmin_

Le serveur Admin est en cours d'exécution sur localhost:8080 et cela devrait enregistrer notre application dans SpringBootAdmin. Nous pouvons accéder à tous les endpoints Actuator en un seul endroit :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-181.png)
_Tableau de bord_

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-182.png)
_Tous les endpoints Actuator configurés_

J'ai exécuté l'endpoint /users plusieurs fois et maintenant les traces HTTP du côté Admin montrent tous les détails des échanges requête-réponse.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-191.png)
_Traces HTTP_

## Conclusion

Les Actuators sont extrêmement utiles pour surveiller et déboguer les applications en production. En accédant aux endpoints, nous pouvons obtenir des détails sur les thread dumps, les heap dumps, les traces HTTP, etc.

Pyctuator simplifie grandement l'utilisation des actuators dans les API Python. En important simplement la bibliothèque et en définissant un objet, tous les actuators sont prêts à être utilisés dans notre application.