---
title: Meilleures pratiques pour les API REST – Exemples de conception de points de
  terminaison REST
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-16T17:50:22.000Z'
originalURL: https://freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/api.png
tags:
- name: api
  slug: api
- name: best practices
  slug: best-practices
- name: REST API
  slug: rest-api
seo_title: Meilleures pratiques pour les API REST – Exemples de conception de points
  de terminaison REST
seo_desc: "In Web Development, REST APIs play an important role in ensuring smooth\
  \ communication between the client and the server. \nYou can think of the client\
  \ as the front end and the server as the back end. \nCommunication between the client\
  \ (frontend) and th..."
---

Dans le développement Web, les API REST jouent un rôle important en assurant une communication fluide entre le client et le serveur. 

Vous pouvez considérer le client comme le front-end et le serveur comme le back-end. 

La communication entre le client (front-end) et le serveur (back-end) n'est généralement pas très directe. Nous utilisons donc une interface appelée Interface de Programmation d'Application (ou API) pour servir d'intermédiaire entre le client et le serveur.

Étant donné que l'API joue un rôle crucial dans cette communication client-serveur, nous devons toujours concevoir des API en gardant à l'esprit les meilleures pratiques. Cela aide les développeurs qui les maintiennent, ainsi que ceux qui les consomment, à ne pas rencontrer de problèmes lors de l'exécution de ces tâches.

Dans cet article, je vais vous présenter 9 meilleures pratiques à suivre lors de la création d'API REST. Cela vous aidera à créer les meilleures API possibles et facilitera également la vie des consommateurs de votre API.

## D'abord, qu'est-ce qu'une API REST ?

REST signifie Representational State Transfer. C'est un style d'architecture logicielle créé par Roy Fielding en 2000 pour guider la conception de l'architecture du web. 

Toute API (Interface de Programmation d'Application) qui suit le principe de conception REST est dite RESTful. 

En termes simples, une API REST est un moyen pour deux ordinateurs de communiquer via HTTP (Hypertext Transfer Protocol), de la même manière que les clients et les serveurs communiquent.

## Meilleures pratiques pour la conception d'API REST

### 1. Utiliser JSON comme format pour l'envoi et la réception de données 

Par le passé, l'acceptation et la réponse aux requêtes API se faisaient principalement en XML et même en HTML. Mais de nos jours, JSON (JavaScript Object Notation) est largement devenu le format de facto pour l'envoi et la réception de données API. 

Cela est dû au fait que, avec XML par exemple, il est souvent un peu fastidieux de décoder et d'encoder les données – donc XML n'est plus largement supporté par les frameworks.

JavaScript, par exemple, dispose d'une méthode intégrée pour analyser les données JSON via l'API fetch car JSON a été principalement conçu pour cela. Mais si vous utilisez un autre langage de programmation tel que Python ou PHP, ils disposent désormais tous de méthodes pour analyser et manipuler les données JSON. 

Par exemple, Python fournit `json.loads()` et `json.dumps()` pour travailler avec les données JSON. 

Pour vous assurer que le client interprète correctement les données JSON, vous devez définir le type `Content-Type` dans l'en-tête de réponse sur `application/json` lors de la requête. 

Pour les frameworks côté serveur, en revanche, beaucoup d'entre eux définissent le `Content-Type` automatiquement. Express, par exemple, dispose désormais du middleware `express.json()` à cet effet. Le package NPM `body-parser` fonctionne toujours pour le même usage.

### 2. Utiliser des noms au lieu de verbes dans les points de terminaison

Lorsque vous concevez une API REST, vous ne devez pas utiliser de verbes dans les chemins des points de terminaison. Les points de terminaison doivent utiliser des noms, indiquant ce que chacun d'eux fait. 

Cela est dû au fait que les méthodes HTTP telles que `GET`, `POST`, `PUT`, `PATCH` et `DELETE` sont déjà sous forme de verbes pour effectuer des opérations CRUD (Create, Read, Update, Delete) de base.

`GET`, `POST`, `PUT`, `PATCH` et `DELETE` sont les verbes HTTP les plus courants. Il en existe également d'autres tels que `COPY`, `PURGE`, `LINK`, `UNLINK`, et ainsi de suite.

Ainsi, par exemple, un point de terminaison ne devrait pas ressembler à ceci : 

`https://mysite.com/getPosts` ou `https://mysite.com/createPost`

Au lieu de cela, il devrait être quelque chose comme ceci : `https://mysite.com/posts`

En bref, vous devriez laisser les verbes HTTP gérer ce que font les points de terminaison. Ainsi, `GET` récupérera les données, `POST` créera des données, `PUT` mettra à jour les données et `DELETE` supprimera les données.

### 3. Nommer les collections avec des noms pluriels

Vous pouvez considérer les données de votre API comme une collection de différentes ressources pour vos consommateurs. 

Si vous avez un point de terminaison comme `https://mysite.com/post/123`, cela peut être acceptable pour supprimer un article avec une requête `DELETE` ou mettre à jour un article avec une requête `PUT` ou `PATCH`, mais cela n'indique pas à l'utilisateur qu'il pourrait y avoir d'autres articles dans la collection. C'est pourquoi vos collections doivent utiliser des noms pluriels. 

Ainsi, au lieu de `https://mysite.com/post/123`, cela devrait être `https://mysite.com/posts/123`.

### 4. Utiliser les codes de statut dans la gestion des erreurs 

Vous devez toujours utiliser les codes de statut HTTP réguliers dans les réponses aux requêtes faites à votre API. Cela aidera vos utilisateurs à savoir ce qui se passe – que la requête soit réussie, ou si elle échoue, ou autre chose.

Ci-dessous, un tableau montrant les différentes plages de codes de statut HTTP et leurs significations :

| Plage de codes de statut | Signification |
| ----------- | ----------- |
| 100 – 199 | Réponses informatives. <br> Par exemple, 102 indique que la ressource est en cours de traitement |
| 300 – 399   | Redirections <br> Par exemple, 301 signifie Déplacé définitivement        |
| 400 – 499   | Erreurs côté client <br> 400 signifie mauvaise requête et 404 signifie ressource non trouvée        |
| 500 – 599   | Erreurs côté serveur <br> Par exemple, 500 signifie une erreur interne du serveur        |

### 5. Utiliser la imbrication dans les points de terminaison pour montrer les relations

Souvent, différents points de terminaison peuvent être interconnectés, vous devriez donc les imbriquer pour qu'il soit plus facile de les comprendre.

Par exemple, dans le cas d'une plateforme de blogging multi-utilisateurs, différents articles pourraient être écrits par différents auteurs, donc un point de terminaison tel que `https://mysite.com/posts/author` constituerait une imbrication valide dans ce cas. 

De la même manière, les articles peuvent avoir leurs propres commentaires, donc pour récupérer les commentaires, un point de terminaison comme `https://mysite.com/posts/postId/comments` aurait du sens. 

Vous devriez éviter les imbrications de plus de 3 niveaux de profondeur, car cela peut rendre l'API moins élégante et lisible. 

### 6. Utiliser le filtrage, le tri et la pagination pour récupérer les données demandées

Parfois, la base de données d'une API peut devenir incroyablement grande. Si cela se produit, la récupération de données à partir d'une telle base de données pourrait être très lente. 

Le filtrage, le tri et la pagination sont toutes des actions qui peuvent être effectuées sur la collection d'une API REST. Cela permet de ne récupérer, trier et organiser que les données nécessaires en pages afin que le serveur ne soit pas trop occupé par les requêtes. 

Un exemple de point de terminaison filtré est celui ci-dessous : 
`https://mysite.com/posts?tags=javascript`
Ce point de terminaison récupérera tout article ayant une balise JavaScript.

### 7. Utiliser SSL pour la sécurité 

SSL signifie Secure Socket Layer. Il est crucial pour la sécurité dans la conception d'API REST. Cela sécurisera votre API et la rendra moins vulnérable aux attaques malveillantes. 

D'autres mesures de sécurité que vous devriez prendre en considération incluent : rendre la communication entre le serveur et le client privée et vous assurer que toute personne consommant l'API n'obtient pas plus que ce qu'elle demande.

Les certificats SSL ne sont pas difficiles à charger sur un serveur et sont disponibles gratuitement la plupart du temps pendant la première année. Ils ne sont pas chers à acheter dans les cas où ils ne sont pas disponibles gratuitement. 

La différence claire entre l'URL d'une API REST qui s'exécute sur SSL et celle qui ne l'est pas est le "s" dans HTTP :
`https://mysite.com/posts` s'exécute sur SSL.
`http://mysite.com/posts` ne s'exécute pas sur SSL.
 
### 8. Être clair avec la versioning

Les API REST doivent avoir différentes versions, afin de ne pas forcer les clients (utilisateurs) à migrer vers de nouvelles versions. Cela pourrait même casser l'application si vous n'êtes pas prudent.

L'un des systèmes de versioning les plus courants dans le développement web est le versioning sémantique. 

Un exemple de versioning sémantique est 1.0.0, 2.1.2 et 3.3.4. Le premier nombre représente la version majeure, le deuxième nombre représente la version mineure et le troisième représente la version de correctif.

De nombreuses API RESTful des géants de la technologie et des particuliers sont généralement présentées comme suit : 
`https://mysite.com/v1/` pour la version 1
`https://mysite.com/v2` pour la version 2

Facebook versionne ses API de cette manière :
![facebook-versioning](https://www.freecodecamp.org/news/content/images/2021/09/facebook-versioning.jpg)

Spotify fait de même pour ses versions :
![spotify-versioning](https://www.freecodecamp.org/news/content/images/2021/09/spotify-versioning.jpg)

Ce n'est pas le cas pour toutes les API. Mailchimp versionne son API différemment : 
![mailchimp-versioning](https://www.freecodecamp.org/news/content/images/2021/09/mailchimp-ersioning.jpg)

Lorsque vous rendez les API REST disponibles de cette manière, vous ne forcez pas les clients à migrer vers les nouvelles versions au cas où ils choisiraient de ne pas le faire.

### 9. Fournir une documentation précise de l'API

Lorsque vous créez une API REST, vous devez aider les clients (consommateurs) à apprendre et à comprendre comment l'utiliser correctement. La meilleure façon de le faire est de fournir une bonne documentation pour l'API. 

La documentation doit contenir :
- les points de terminaison pertinents de l'API
- des exemples de requêtes pour les points de terminaison
- l'implémentation dans plusieurs langages de programmation
- les messages listés pour différentes erreurs avec leurs codes de statut 

L'un des outils les plus courants que vous pouvez utiliser pour la documentation des API est Swagger. Vous pouvez également utiliser Postman, l'un des outils de test d'API les plus courants dans le développement logiciel, pour documenter vos API.

## Conclusion

Dans cet article, vous avez appris les plusieurs meilleures pratiques à garder à l'esprit lors de la création d'API REST. 

Il est important de mettre ces meilleures pratiques et conventions en pratique afin de pouvoir créer des applications hautement fonctionnelles qui fonctionnent bien, sont sécurisées et, en fin de compte, facilitent la vie des consommateurs de votre API.

Merci d'avoir lu. Maintenant, allez créer des API avec ces meilleures pratiques.