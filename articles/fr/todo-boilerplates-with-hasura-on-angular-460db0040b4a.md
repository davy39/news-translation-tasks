---
title: Comment commencer avec les modèles Angular-Hasura
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-10T17:39:05.000Z'
originalURL: https://freecodecamp.org/news/todo-boilerplates-with-hasura-on-angular-460db0040b4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*z01LoM6jNxhND7Nc5OLP4A.jpeg
tags:
- name: Angular
  slug: angular
- name: GraphQL
  slug: graphql
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment commencer avec les modèles Angular-Hasura
seo_desc: 'By Siddhant Srivastav

  This blogpost gives you an idea of how to start with GraphQL with the help of Hasura
  and Angular. I will give you information about the boilerplate apps on Angular configured
  to use with Hasura’s deployed GraphQL engine on Herok...'
---

Par Siddhant Srivastav

Cet article de blog vous donne une idée de la façon de commencer avec GraphQL à l'aide de Hasura et Angular. Je vais vous fournir des informations sur les applications modèles Angular configurées pour être utilisées avec le moteur GraphQL déployé de Hasura sur Heroku.

L'idée derrière cet article est de vous donner un coup de pouce dans le processus de création de l'application et une idée de l'approche utilisée pour cela. Nous n'entrerons pas trop dans le code, juste la partie dont nous avons besoin pour faire fonctionner l'application.

Commençons !

### Aperçu

Nous avons 3 genres de modèles :

#### hello-world

Ce modèle est simplement une application Angular qui a les paramètres pour GraphQL et les en-têtes déjà configurés. En utilisant ce modèle, vous pouvez cloner directement l'application et commencer à créer votre application !

#### basic

Ce modèle est construit sur le modèle **hello-world** et introduit les fonctionnalités de base des mutations/requêtes et vous montre comment les écrire et les fonctions qui les utilisent.

#### advanced

Ce modèle est construit sur l'application **basic** et est entièrement équipé de mutations, de requêtes et d'authentification avec Auth0 déjà configurés ! Ce modèle est une application idéale pour vous permettre de commencer et de créer de nouvelles applications en un temps record.

### Woah ! Stop ! Des choses importantes ici...

Pour utiliser ces modèles, certains paramètres importants sont requis. Les voici :

* Créez une instance sur Heroku. Pour cela, rendez-vous sur [https://hasura.io](https://hasura.io)
* Configurez les variables d'environnement : dirigez-vous vers le fichier `environments/environment.ts` et changez les valeurs pour le point de terminaison et les autres champs requis. Dans l'application avancée, vous devrez utiliser les identifiants fournis par Auth0.

### Les Modèles

Les trois modèles qui permettent à Angular d'interagir avec le moteur GraphQL de Hasura peuvent être clonés à partir du [dépôt du moteur Hasura](https://github.com/hasura/graphql-engine). Les étapes communes aux trois modèles sont :

* Clonez l'application.
* `cd <nom-du-modèle>` et
* exécutez `npm install` pour installer toutes les dépendances.

#### Hello World

Le modèle hello-world n'est rien d'autre qu'une simple application Angular avec le module GraphQL configuré et le client apollo déjà configuré également. 
La structure du répertoire pour l'application est montrée ci-dessous.

L'application hello world a un module hello qui importe le `graph-ql.module.ts`. Former cette structure de répertoire nous aide à initialiser le module GraphQL une fois que le module Hello est activé.

Mais pourquoi devons-nous faire cela ? Le module GraphQL initialise les en-têtes et crée un client Apollo. Les en-têtes contiennent des jetons d'autorisation et d'autres informations. Nous voulons initialiser ce module uniquement lorsque les jetons d'autorisation sont définis, sinon nous devrions actualiser l'application une fois de plus pour définir les valeurs des jetons dans le module. Ce modèle est suivi dans tous les modèles.

Le module Hello est activé à partir du module App.

Maintenant, apprenons à mieux connaître le module GraphQL. Ce module est le même dans les trois modèles avec quelques ajustements mineurs pour les jetons.

#### L'Application de Base

Le modèle d'application de base est construit sur le modèle Hello World. Les ajouts à l'application sont les requêtes et les mutations écrites pour vous donner des exemples de la façon dont les requêtes et les mutations sont écrites.

Les requêtes sont écrites dans `app/shared/operations.ts`. Le module partagé est importé dans le module de base qui contient le HTML et les fonctions écrites pour effectuer des requêtes.

![Image](https://cdn-media-1.freecodecamp.org/images/fuSvefGpnVXkOMFT8qkj1wFk6I88S2PaG88k)
_Page de Connexion_

Dans l'application **basic**, la connexion est gérée par un authentificateur fictif qui définit une session codée en dur et vous permet de vous connecter avec n'importe quel nom d'utilisateur et mot de passe.

![Image](https://cdn-media-1.freecodecamp.org/images/6a7CPXsHoGNACnyEJsCKKgmheqR8Eu2CLYTq)
_Liste de Tâches_

![Image](https://cdn-media-1.freecodecamp.org/images/UL9C10qClyfeghorIYwNnUF4C5cn1MVF3lRb)
_Élément Complété_

#### Le Modèle Avancé

Ce modèle est construit sur le modèle de base et ajoute la fonctionnalité d'authentification à l'application.

**Authentification via Auth0**

* Rendez-vous sur [https://auth0.com](https://auth0.com) et connectez-vous.
* Une fois connecté, créez une nouvelle application et obtenez les identifiants pour l'application.
* Ouvrez les paramètres de l'application et ajoutez une URL de rappel. Pour le développement : utilisez l'URL [http://localhost:4200](http://localhost:4200), et pour la production, utilisez l'URL de votre site web.

Maintenant, dirigez-vous vers le fichier `environments/environment.prod.ts` et remplacez les variables d'environnement. Vous êtes maintenant prêt à utiliser le modèle avancé !

### Bon Codage !

### À Propos de Moi

Je m'appelle **Siddhant Srivastav**, et je suis un étudiant de premier cycle à l'**Indian Institute of Information Technology, Allahabad.**

J'aime créer. J'aime coder en **Python et JS.** J'aime l'**Open source** et contribuer à des projets que je trouve intéressants.

Vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/siddhant-s-45065182/), [Twitter](http://twitter.com/siddhantsme) et [GitHub](https://github.com/WickedBrat).