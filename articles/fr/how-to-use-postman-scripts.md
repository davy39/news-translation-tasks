---
title: Comment utiliser les scripts Postman pour simplifier votre processus d'authentification
  API
subtitle: ''
author: Orim Dominic Adah
co_authors: []
series: null
date: '2025-09-08T14:24:49.555Z'
originalURL: https://freecodecamp.org/news/how-to-use-postman-scripts
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757341168209/dc77dc00-a0a6-40f7-b766-ce07d0d8a637.png
tags:
- name: authentication
  slug: authentication
- name: APIs
  slug: apis
- name: automation
  slug: automation
seo_title: Comment utiliser les scripts Postman pour simplifier votre processus d'authentification
  API
seo_desc: Postman is a platform used by developers, API testers, technical writers
  and DevOps teams for testing, documenting and collaborating on API development.
  It provides a user-friendly interface for making different types of API requests
  (HTTP, GraphQL, ...
---

Postman est une plateforme utilisée par les développeurs, les testeurs d'API, les rédacteurs techniques et les équipes DevOps pour tester, documenter et collaborer sur le développement d'API. Elle offre une interface conviviale pour effectuer différents types de requêtes API (HTTP, GraphQL, gRPC), inspecter les réponses et organiser les appels API en collections pour la collaboration et l'automatisation.

Effectuer des tâches répétitives lors du test d'API est stressant et fait perdre du temps. Par exemple, le processus de récupération, de copie et de collage de nouveaux jetons d'authentification pour une utilisation dans Postman est répétitif. Vous pouvez simplifier ce processus en utilisant des scripts Postman pour stocker les jetons d'authentification, puis les réutiliser sans répéter les étapes de copier-coller.

Pour suivre ce guide, vous devriez avoir :

* Le [client API Postman](https://www.postman.com/downloads/) installé sur votre ordinateur
    
* De l'expérience dans la réalisation de requêtes API avec Postman
    
* Une application backend qui utilise l'authentification JWT et dont la documentation se trouve dans votre client Postman
    

Si vous n'avez pas de configuration d'application backend, j'en ai créé une que vous pouvez cloner depuis GitHub à l'adresse [orimdominic/freeCodeCamp-postman-api-jwt](https://github.com/orimdominic/freeCodeCamp-postman-api-jwt).

À la fin de cet article, vous devriez être en mesure de simplifier le processus d'obtention et de réutilisation des jetons d'authentification à travers vos requêtes API. Vous devriez également avoir une compréhension pratique de certains scripts nécessaires pour une utilisation dans d'autres domaines du test logiciel avec Postman.

## Table des matières

* [Table des matières](#heading-table-des-matieres)
    
* [Que sont les scripts Postman ?](#heading-que-sont-les-scripts-postman)
    
* [Comment simplifier votre processus d'authentification JWT](#heading-comment-simplifier-votre-processus-d-authentification-jwt)
    
    * [S'authentifier pour obtenir le jeton](#heading-s-authentifier-pour-obtenir-le-jeton)
        
    * [Comment enregistrer le jeton dans une variable avec un script Postman](#heading-comment-enregistrer-le-jeton-dans-une-variable-avec-un-script-postman)
        
    * [Comment utiliser la variable dans une requête](#heading-comment-utiliser-la-variable-dans-une-requete)
        
* [Étapes suivantes](#heading-etapes-suivantes)
    

## Que sont les scripts Postman ?

Les [scripts Postman](https://learning.postman.com/docs/tests-and-scripts/tests-and-scripts/) sont des blocs de code JavaScript que vous pouvez écrire et exécuter dans le client API Postman pour automatiser et améliorer les flux de test d'API. Vous pouvez utiliser les scripts Postman pour ajouter du code à exécuter avant et après les requêtes API. Ces scripts peuvent être utilisés pour :

* Ajouter de la logique et traiter les données des requêtes API
    
* Écrire des assertions de test pour les réponses API
    
* Exécuter des tests automatisés sur les points de terminaison d'API
    

![L'onglet des scripts Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1756577771526/161bd327-fbf7-48cb-acab-317ab1cad4c5.jpeg align="center")

Vous pouvez trouver les scripts Postman sous l'onglet **Scripts** d'une requête API. Le code écrit dans l'onglet **Pre-request** s'exécute avant que la requête ne soit effectuée et le code écrit dans l'onglet **Post-response** s'exécute après que la réponse a été reçue.

## Comment simplifier votre processus d'authentification JWT

En résumé, vous allez effectuer les étapes suivantes pour atteindre l'objectif de ce tutoriel :

1. S'authentifier pour obtenir le jeton
    
2. Enregistrer le jeton dans une variable de collection avec les scripts Postman
    
3. Utiliser la variable dans une requête API
    

### S'authentifier pour obtenir le jeton

Pour commencer, effectuez les étapes suivantes :

1. Démarrez votre application backend et assurez-vous qu'elle fonctionne correctement.
    
2. Ouvrez votre application Postman et allez sur la requête API de connexion pour obtenir un JWT.
    
3. Effectuez une requête API vers le point de terminaison de connexion et notez le schéma de la réponse JSON.
    

![Réponse à la requête d'authentification](https://cdn.hashnode.com/res/hashnode/image/upload/v1756573137191/b5aad14c-5094-4a84-8876-1bbbb869064c.jpeg align="center")

La partie surlignée de l'image ci-dessus montre la réponse JSON d'une requête de connexion réussie. Dans le schéma de réponse, le jeton d'authentification à utiliser pour l'autorisation se trouve dans le champ `data.token`. Vous utiliserez des scripts Postman pour stocker ce jeton dans une variable, puis vous utiliserez cette variable dans l'en-tête `Authorization` des requêtes qui nécessitent une autorisation.

### Comment enregistrer le jeton dans une variable avec un script Postman

![Ajouter de la logique dans le script Post-response de Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1756575948975/2b43493d-2803-45cd-aefe-0ca5694f75e8.jpeg align="center")

Dans Postman, cliquez sur l'onglet **Scripts** à côté de l'onglet **Body**. Si la fenêtre de l'application Postman est petite, vous devrez peut-être cliquer sur un menu déroulant pour le voir. Ensuite, cliquez sur l'onglet **Post-response**. Dans la zone de texte à droite, vous écrirez le script pour capturer le jeton d'authentification de la réponse et le stocker dans une variable Postman. Copiez le code JavaScript ci-dessous et collez-le dans la zone de texte.

```javascript
if (pm.response.code == 200) {
    const token = pm.response.json().data.token
    pm.collectionVariables.set("auth_token", token)
}
```

Les scripts Postman utilisent l'identifiant [`pm`](https://learning.postman.com/docs/tests-and-scripts/write-scripts/postman-sandbox-api-reference/) pour accéder et modifier les informations dans l'environnement Postman. Le script ci-dessus utilise `pm` pour s'assurer d'abord que la requête a réussi en vérifiant si le code d'état de la réponse est `200`.

À l'intérieur de l'instruction conditionnelle, `pm.response.json().data.token` est utilisé pour obtenir le jeton d'authentification à partir de la réponse JSON et le stocker dans une variable de collection appelée `auth_token`. Si `auth_token` n'existe pas déjà, elle est créée et sa valeur est définie sur la valeur de `token`. Si elle existe déjà, sa valeur est remplacée.

![Variable de collection Postman définie par un script](https://cdn.hashnode.com/res/hashnode/image/upload/v1756581970294/bed1fe89-9c00-4b94-9f71-173ea3bf1cd1.png align="center")

Pour confirmer que `auth_token` a été défini, cliquez sur le nom de la collection (marqué 1 dans la capture d'écran ci-dessus), puis cliquez sur l'onglet **Variables** (marqué 2 dans la capture d'écran ci-dessus). Ensuite, au lieu de copier à plusieurs reprises le jeton et de le coller dans l'en-tête `Authorization` de vos requêtes, vous utiliserez `auth_token` dans l'en-tête `Authorization` de vos requêtes.

### Comment utiliser la variable dans une requête

![Utiliser la variable dans une requête](https://cdn.hashnode.com/res/hashnode/image/upload/v1756583915681/d3bf0f56-c406-4d3e-b7f1-df4cbc2a3cfc.png align="center")

Référencez la variable de collection dans l'en-tête `Authorization` en l'entourant de doubles accolades `{{auth_token}}`. Lorsque vous effectuez une requête API, Postman utilisera la valeur référencée par `{{auth_token}}` comme en-tête `Authorization`.

Si une autre requête d'authentification entraîne la mise à jour de la valeur de `auth_token`, vous n'avez plus besoin de copier le nouveau jeton d'authentification. Le script dans l'onglet post-response mettra à jour la valeur de `auth_token` et vous pourrez continuer à effectuer vos requêtes API sans interruption. Plus besoin de copier-coller répétitifs - **Don’t Repeat Yourself (DRY)**.

## Étapes suivantes

Dans ce tutoriel, vous avez appris à utiliser les scripts Postman pour définir des variables d'environnement dans Postman. Vous avez également appris à éliminer le processus de copier-coller répétitif des jetons d'authentification pour une utilisation dans les requêtes API.

Pour des guides sur l'écriture de tests d'assertion pour vos API, consultez le guide [Tester la fonctionnalité et la performance des API dans Postman](https://learning.postman.com/docs/tests-and-scripts/test-apis/test-apis/) par Postman.