---
title: Qu'est-ce qu'une API REST ? Exemple de requête de point de terminaison d'API
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-02-10T16:39:44.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-rest-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-life-of-pix-42408.jpg
tags:
- name: api
  slug: api
- name: REST API
  slug: rest-api
seo_title: Qu'est-ce qu'une API REST ? Exemple de requête de point de terminaison
  d'API
seo_desc: 'An API (short for Application Programming Interface) allows for two or
  more applications to communicate with one another and send data back and forth.

  APIs operated based on a standardized set of rules and they''re an integral component
  of modern-day ...'
---

Une API (abréviation de Application Programming Interface) permet à deux applications ou plus de communiquer entre elles et d'échanger des données.

Les API fonctionnent sur la base d'un ensemble standardisé de règles et elles sont un composant intégral du développement logiciel moderne.

Il existe différents styles d'API, et chacun a son architecture unique. L'un des styles les plus courants est REST.

Dans cet article, vous apprendrez les bases des API REST. Vous verrez un aperçu de ce qu'elles sont et de leur fonctionnement. Vous apprendrez également ce qui rend une API RESTful.

Commençons !

## Qu'est-ce qu'une API REST ?

REST (abréviation de REpresentational State Transfer) est un style d'architecture logicielle créé par le scientifique informatique Roy Fielding en 2000.

Avec les API REST, un client demande une ressource. Ensuite, le serveur répond au client avec une représentation de l'état actuel de cette ressource et toutes les informations pertinentes à son sujet dans un format standardisé, tel que JSON ou XML.

## Aperçu des concepts de l'API REST

Dans la section précédente, j'ai mentionné les termes client, ressource et serveur. Que signifient-ils ?

Un **client** est un programme qui s'exécute sur l'ordinateur d'un utilisateur.

Ce programme pourrait être un navigateur web, qui initie la communication et fait des requêtes à l'API.

Le rôle du client est uniquement de récupérer ou de modifier des informations au sein de l'application.

Une **ressource** est toute information que l'API peut fournir - un document, un fichier texte, une image, une vidéo, ou tout autre objet.

Chaque ressource a un identifiant unique, connu sous le nom d'Identifiant de Ressource Universel (ou URI), qui est une chaîne de caractères qui fait référence à cette ressource spécifique.

Un **serveur** est un système qui stocke la ressource que le client demande.

Le rôle du serveur est d'écouter et de recevoir les requêtes des clients pour ses ressources et de répondre à ces requêtes avec les informations demandées.

Le serveur envoie une représentation de l'état de la ressource et n'accorde pas un accès complet au client.

## Comment fonctionne une API REST ?

Un client envoie une requête HTTP au serveur pour effectuer une opération CRUD. CRUD est un acronyme pour `Create`, `Read`, `Update`, et `Delete`.

Le serveur répond avec une ressource dans un format standardisé tel que JSON (JavaScript Object Notation) ou XML, JSON étant le format le plus populaire utilisé aujourd'hui.

### Aperçu des requêtes d'API REST

Une requête d'API REST doit inclure les éléments suivants :

- Une opération
- Un point de terminaison
- Les paramètres/corps
- Les en-têtes HTTP

Tout d'abord, chaque requête doit inclure l'**opération/action** que vous souhaitez que le serveur effectue sur la ressource.

Dans la section ci-dessus, j'ai mentionné que le client envoie une requête au serveur pour effectuer une opération CRUD.

Chaque opération CRUD est équivalente à une méthode/verbe HTTP qui définit l'opération :

- L'équivalent de l'opération `Create` est une requête `POST` qui indique que vous souhaitez créer une nouvelle ressource.
- L'équivalent de l'opération `Read` est une requête `GET` qui indique que vous souhaitez récupérer une ressource.
- L'équivalent de l'opération `Update` est une requête `PUT` qui indique que vous souhaitez modifier ou mettre à jour une ressource existante spécifique.
- L'équivalent de l'opération `Delete` est une requête `DELETE` qui indique que vous souhaitez supprimer une ressource spécifique.

Ensuite, la requête doit également inclure un **point de terminaison**.

Un point de terminaison est une URL (abréviation de Uniform Resource Locator) qui contient l'URI (Uniform Resource Identifier), qui est l'emplacement où l'API peut trouver et interagir avec la ressource spécifique.

Vous pouvez consulter une liste de points de terminaison dans la documentation de l'API spécifique que vous utilisez.

Par exemple, lors de l'utilisation de [l'API de Spotify](https://developer.spotify.com/documentation/web-api/), le point de terminaison pour obtenir un [album d'un artiste spécifique](https://developer.spotify.com/console/get-artist-albums/) ressemble à quelque chose comme ceci :

```
https://api.spotify.com/v1/artists/{id}/albums
```

La requête inclut également facultativement les **paramètres/corps**, qui sont des données et messages supplémentaires que vous pourriez envoyer au serveur.

Enfin, la requête inclut également des en-têtes HTTP, qui sont des données d'authentification telles qu'une clé API.

### Aperçu des réponses de l'API REST

Après avoir reçu la requête, le serveur renverra des informations sur la ressource demandée.

La réponse est une représentation de l'état de la ressource demandée - et non la ressource elle-même.

Typiquement, la réponse est sous la forme de données JSON - un format lisible pour le client qui a fait la requête.

Il y a également un code de statut HTTP approprié renvoyé dans l'en-tête de la réponse pour informer le client si l'opération a réussi ou non.

Certains des codes de statut les plus couramment utilisés sont les suivants :

- `200 OK` signifie que la requête a réussi
- `201 Created` signifie que la requête a réussi et qu'une ressource a été créée
- `204 No Content` signifie que la requête a réussi, mais qu'il n'est pas nécessaire de retourner un corps de message
- `400 Bad Request` signifie que le serveur ne peut pas traiter la requête en raison d'une erreur du côté du client
- `401 Unauthorized` signifie que le serveur ne peut pas traiter la requête en raison d'un manque de credentials d'authentification
- `403 Forbidden` signifie que le client n'a pas la permission d'accéder à la ressource
- `404 Not Found` signifie que le serveur ne peut pas trouver la ressource (cela peut être dû à sa suppression)
- `500 Internal Server Error` signifie que le serveur a rencontré une erreur inattendue

## Ce qui rend une API RESTful

Pour qu'une API soit considérée comme RESTful, elle doit suivre certaines meilleures pratiques, également connues sous le nom de contraintes architecturales.

Les six contraintes de l'architecture REST sont :

- Séparation client-serveur
- Une interface uniforme
- Sans état
- Système en couches
- Cacheable
- Code exécutable

Examinons chacun d'eux un peu plus en détail dans les sections suivantes.


### Séparation Client-Serveur

Dans l'architecture des API REST, le client et le serveur doivent fonctionner indépendamment.

Un client n'initie que la communication et envoie une requête au serveur, et un serveur attend les requêtes d'un client et répond de manière appropriée.

Cette séparation des préoccupations garantit la fiabilité et la scalabilité du système.

Lorsque vous séparez le client du serveur, vous pouvez changer le code côté client sans affecter le serveur. Et vous pouvez modifier les ressources stockées dans le serveur sans affecter le client.

### Une Interface Uniforme

Toutes les requêtes et réponses doivent suivre un format et un protocole - il doit y avoir un langage commun standardisé.

Ce langage commun est HTTP (abréviation de HyperText Transfer Protocol).

Notez que HTTP n'a pas été conçu pour les API REST - REST a adopté le protocole de communication.


### Sans État

Les API REST sont sans état, ce qui signifie que l'API traite chaque requête d'un client indépendamment, et la requête doit inclure toutes les informations nécessaires.

Le serveur interprète chaque requête comme nouvelle - c'est-à-dire qu'il ne se souvient pas des informations passées sur le client. Par exemple, il ne se souvient pas si le client a déjà demandé la même ressource.

Cette contrainte améliore les performances, la scalabilité et la fiabilité.

### Système en Couches

L'architecture RESTful a une structure en couches, et chaque couche fonctionne indépendamment - les requêtes et les réponses passent par des couches hiérarchiques séparées.

Le client et le serveur ne savent pas s'ils communiquent avec un intermédiaire. Il peut y avoir plusieurs autres serveurs au milieu qui ne affectent pas les interactions client-serveur.

Ces couches peuvent ajouter de la sécurité et gérer et distribuer le trafic, ce qui améliore la sécurité et la scalabilité du système.

### Cacheable

Les API REST sont conçues en tenant compte de la mise en cache. La réponse du serveur doit indiquer si une ressource est cacheable ou non.

Si la ressource est cacheable, le client peut stocker et réutiliser les données fréquemment consultées au lieu de les demander encore et encore au serveur.

Lorsque une ressource est cacheable, elle réduit le temps de chargement d'une page puisque le client récupère les données depuis le stockage local et fait moins d'appels au serveur. Le serveur, à son tour, a moins de latence.


### Code Exécutable

La dernière contrainte est facultative.

Au lieu d'envoyer une représentation d'une ressource statique en JSON, le serveur peut retourner un code informatique sous la forme d'un script que le client peut exécuter.

Cela dit, une API est RESTful même si elle ne fournit pas de code exécutable.

## Conclusion

Espérons que cet article a été utile et vous a donné un aperçu de ce qu'est une API REST, comment elle fonctionne et ce qui rend une API RESTful.

Si vous souhaitez approfondir l'utilisation des API REST, voici un [guide pour vous aider à commencer](https://www.freecodecamp.org/news/how-to-use-rest-api/).

Et si vous souhaitez essayer de concevoir votre propre API REST, ce [manuel complet vous guidera à travers le processus](https://www.freecodecamp.org/news/rest-api-design-best-practices-build-a-rest-api/).

Merci d'avoir lu, et bon codage !