---
title: APIs avec Node.js et Express – Cours en espagnol pour débutants
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2024-05-22T08:11:16.247Z'
originalURL: https://freecodecamp.org/news/apis-with-nodejs-and-express-course-in-spanish-for-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1715802086520/639186b7-74e2-4ad0-bafb-9b8aa63cc5ba.png
tags:
- name: APIs
  slug: apis
- name: Node.js
  slug: nodejs
- name: Express
  slug: express
seo_title: APIs avec Node.js et Express – Cours en espagnol pour débutants
seo_desc: 'An application programming interface (API) is software that acts as an
  intermediary, allowing two applications to communicate. This project will teach
  you how to develop an API step by step and connect it to a database.

  We just published a course on ...'
---

Une interface de programmation d'applications (API) est un logiciel qui agit comme un intermédiaire, permettant à deux applications de communiquer. Ce projet vous apprendra à développer une API étape par étape et à la connecter à une base de données.

Nous venons de publier un cours sur la [chaîne YouTube freeCodeCamp.org en espagnol](https://www.youtube.com/freecodecampespanol) conçu pour vous apprendre à développer des APIs REST étape par étape. Vous apprendrez également à les connecter à des bases de données.

Vous développerez votre API avec TypeScript, Node.js, Express, MySQL et TypeORM, et vous la testerez avec Postman, une plateforme pour tester les APIs.

Vous commencerez par les bases de Node.js et Express et plongerez progressivement dans des concepts plus avancés qui vous prépareront à connecter votre API à une base de données. À la fin du cours, vous serez capable de créer vos propres APIs avec Node.js et Express.

Si vous avez des amis hispanophones, vous êtes invité à partager la [**version espagnole de cet article**](https://www.freecodecamp.org/espanol/news/aprende-a-crear-apis-desde-cero-con-node-js-y-express-curso-desde-cero/) avec eux.

Ce cours a été créé par Leonardo José Castillo. Leonardo est un développeur logiciel et créateur de contenu qui aime enseigner la programmation et partager ses connaissances.

Êtes-vous prêt ? Voici un aperçu rapide des APIs et de ce que vous apprendrez pendant le cours.

## **Qu'est-ce qu'une API ?**

Si vous devez faire communiquer deux applications entre elles, les APIs sont exactement ce dont vous avez besoin. Ce sont des logiciels que vous pouvez utiliser pour envoyer des données entre deux applications via des requêtes et des réponses.

**💡 Astuce :** API signifie Application Programming Interface.

![](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-14-at-6.23.02-PM.png align="left")

Les développeurs de l'application qui **enverra** les données à l'autre application implémenteront une API et documenteront ses fonctionnalités et ses endpoints, afin que d'autres développeurs puissent l'utiliser et accéder à ses ressources et données.

💡 **Astuce :** Un endpoint est un emplacement dans l'API qui accepte des requêtes et envoie des réponses.

Les développeurs de l'application qui **recevra** les données de l'API écriront du code pour effectuer ces requêtes, en spécifiant les endpoints et en traitant la réponse reçue de l'API de manière appropriée.

## Exemple d'API météo

Par exemple, une application météo peut accéder à une API pour obtenir les données météo actuelles d'un lieu saisi par l'utilisateur.

Les développeurs de l'application météo écrivent du code pour faire des requêtes à l'API météo, en suivant ses directives et sa documentation. L'API accédera ensuite aux données d'une base de données et les enverra au client qui a fait la requête.

![](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-14-at-6.32.00-PM.png align="left")

Tel est le rôle des APIs. C'est un rôle très important dans le monde du développement web back-end.

Vous pouvez les implémenter avec de nombreuses technologies différentes, y compris Node.js et Express.

Voyons ce qu'ils sont :

* **Node.js** est un environnement d'exécution JavaScript qui vous permet d'exécuter du code JavaScript en dehors du navigateur.

* **Express** est un framework Node.js qui facilite grandement le développement de serveurs et d'APIs.

Apprendre à concevoir et à implémenter des APIs peut vous ouvrir de nombreuses opportunités de carrière.

## **Opportunités de carrière**

En parlant d'opportunités de carrière – TypeScript, Node.js, Express et MySQL, les technologies que vous pratiquerez dans ce projet, sont très populaires et très demandées dans l'industrie de la programmation.

Pour vous montrer à quel point elles sont importantes, voici les résultats de l'[enquête des développeurs Stack Overflow 2023](https://survey.stackoverflow.co/2023/#most-popular-technologies-language-prof).

Node.js et Express étaient les premier et quatrième frameworks et technologies web les plus populaires :

![Résultats pour tous les répondants de la catégorie Web Frameworks and Technologies de l'enquête des développeurs Stack Overflow 2023.](https://www.freecodecamp.org/news/content/images/2024/05/node.png align="left")

MySQL était également très bien classé. C'était la deuxième base de données la plus populaire :

![Résultats de tous les répondants pour la catégorie base de données de l'enquête des développeurs Stack Overflow 2023.](https://www.freecodecamp.org/news/content/images/2024/05/mysql-survey-1.png align="left")

TypeScript était le cinquième langage le plus populaire parmi tous les répondants :

![Résultats des technologies les plus populaires de l'enquête des développeurs Stack Overflow 2023 pour tous les répondants.](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot-2024-04-29-at-2.56.30-PM.png align="left")

Ces résultats vous montrent à quel point ces technologies sont pertinentes et le seront pour le développement web en 2024 et au-delà.

💡 **Astuce :** Pendant le projet, vous utiliserez également TypeORM, un outil de mappage objet-relationnel qui vous aide à travailler avec des bases de données en JavaScript, TypeScript et autres langages de programmation.

## **Cours sur les APIs avec Node.js et Express**

Très bien. Maintenant que vous savez pourquoi les APIs sont si importantes, examinons les sujets que vous apprendrez pendant le cours :

* Introduction à Node.js et Express

* Architecture d'application

* Routage dynamique

* Contrôleurs

* Structure de la base de données

* Connexion de l'API à une base de données

* Implémentation des opérations CRUD en TypeScript

* Modélisation avec TypeORM

* Implémentation des contrôleurs avec TypeORM

Et plus encore !

![Capture d'écran du cours. Implémentation des endpoints de l'API avec Node.js et Express](https://www.freecodecamp.org/news/content/images/2024/05/frame.png align="left")

**💡 Astuce :** Pour construire ce projet, il est recommandé d'avoir une compréhension de base de TypeScript et du développement web. Si vous devez réviser ces sujets, nous avons ces cours sur la chaîne :

* [Aprende Node.js y Express - Curso desde cero](https://www.youtube.com/watch?v=1hpc70_OoAg)

* [Aprende TypeScript - Curso desde cero](https://www.youtube.com/watch?v=T7uaEZ3ZoZE)

Si vous êtes prêt à commencer à construire cette API, consultez le cours en espagnol sur la [chaîne YouTube freeCodeCamp.org en espagnol](https://www.youtube.com/freecodecampespanol) :

%[https://www.youtube.com/watch?v=yd_QpXWrbtQ]

✍️ Cours créé par Leonardo José Castillo.

* YouTube : [@LeonardoCastillo79](https://www.youtube.com/leonardocastillo79)

* LinkedIn : [Leonardo José Castillo Lacruz](https://www.linkedin.com/in/leonardo-castillo-4911571a/)

* Twitter : [@ljcl79](https://twitter.com/ljcl79)

* GitHub : [@ljcl79](https://github.com/ljcl79)