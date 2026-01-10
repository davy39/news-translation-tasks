---
title: Comment obtenir votre URL MongoDB pour vous connecter à votre application Node.js
  – Un guide étape par étape
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2024-08-12T21:21:39.500Z'
originalURL: https://freecodecamp.org/news/get-mongodb-url-to-connect-to-a-nodejs-application
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723497228942/b766b557-8230-4bef-8392-d3f4f020c1f4.png
tags:
- name: Node.js
  slug: nodejs
- name: MongoDB
  slug: mongodb
- name: Web Development
  slug: web-development
- name: Developer
  slug: developer
seo_title: Comment obtenir votre URL MongoDB pour vous connecter à votre application
  Node.js – Un guide étape par étape
seo_desc: 'In my previous article about building a Node.js application, I didn’t fully
  explain how to obtain the MongoDB URL, as I wanted to keep the article concise.
  However, I realized that this information is essential for saving data to MongoDB.

  In this art...'
---

Dans mon [article précédent sur la création d'une application Node.js](https://www.freecodecamp.org/news/how-to-build-an-event-app-with-node-js/), je n'ai pas entièrement expliqué comment obtenir l'URL MongoDB, car je voulais garder l'article concis. Cependant, j'ai réalisé que cette information est essentielle pour sauvegarder des données dans MongoDB.

Dans cet article, je vais vous guider à travers le processus d'obtention de votre URL MongoDB afin que vous puissiez connecter votre application efficacement. À la fin de ce tutoriel, vous aurez une compréhension claire de la manière de récupérer votre URL MongoDB.

## Commençons ! 🚀

![Un tambour indiquant commençons](https://www.freecodecamp.org/news/content/images/2024/08/drum-roll-3.gif align="left")

## Étape 1 : Recherchez MongoDB ou visitez leur site web

Pour commencer, rendez-vous sur le site [MongoDB](https://www.mongodb.com).

![Site web de MongoDB](https://www.freecodecamp.org/news/content/images/2024/08/mongodb-website.png align="left")

## Étape 2 : Cliquez sur le bouton Se connecter sur leur site web.

Cela vous redirigera vers la page de connexion de MongoDB. Si vous n'avez pas encore de compte, vous pouvez en créer un en sélectionnant l'option **S'inscrire**. Comme je possède déjà un compte, je vais me connecter pour accéder à mon tableau de bord MongoDB.

![Redirection vers la page de connexion ou d'inscription de MongoDB](https://www.freecodecamp.org/news/content/images/2024/08/sigin-mongodb.gif align="left")

## Étape 3 : Accéder au tableau de bord

Une fois connecté, vous aurez accès au tableau de bord. Mais d'abord, vous devez créer un dossier de projet.

### Pourquoi avez-vous besoin d'un dossier de projet ?

Cela sert à des fins d'organisation, vous aidant à garder une trace des projets sur lesquels vous travaillez.

**Pour créer un dossier de projet**

* Cliquez sur la section **Projets** en haut, indiquée par une icône de dossier. Cela révèlera un menu déroulant.

* Dans le menu déroulant, cliquez sur **Nouveau projet**. Cela vous redirigera vers une page où vous pourrez créer votre nouveau projet.

![Créer un nouveau projet](https://www.freecodecamp.org/news/content/images/2024/08/use-mongodb.gif align="left")

* Cliquez sur le bouton **Suivant** pour passer à la page de création du projet.

![La création d'un projet continue](https://www.freecodecamp.org/news/content/images/2024/08/create-project.png align="left")

Après avoir créé votre projet, vous serez redirigé vers votre tableau de bord, où vous verrez votre dossier de projet nouvellement créé. Vous pouvez maintenant commencer à travailler sur ce projet spécifique.

![Retour au tableau de bord](https://www.freecodecamp.org/news/content/images/2024/08/project-created-mongodb-1.png align="left")

## Étape 4 : Création d'un cluster

Pour obtenir l'URL de connexion MongoDB, il est essentiel de créer un **cluster**.

### Qu'est-ce qu'un cluster ?

Un cluster dans MongoDB est un groupe de serveurs qui travaillent ensemble pour stocker et gérer vos données, offrant une haute disponibilité et une scalabilité.

**Pour créer un cluster :**

1. Sur votre tableau de bord, cliquez sur le bouton **Clusters** comme indiqué dans l'image de l'**Étape 3** ci-dessus.

2. Ensuite, cela vous dirigera vers une page intitulée "**Déployer votre cluster**" où vous pourrez créer votre cluster.

![Création d'un cluster](https://www.freecodecamp.org/news/content/images/2024/08/cluster-mongoDB.gif align="left")

## Étape 5 : Créer un nom d'utilisateur pour votre URL de connexion

Après avoir créé un cluster, vous serez dirigé vers une page où vous devez créer un nom d'utilisateur et un mot de passe pour l'URL de connexion. Le mot de passe peut être généré automatiquement, ou vous pouvez créer le vôtre.

![Création d'un nom d'utilisateur et d'un mot de passe](https://www.freecodecamp.org/news/content/images/2024/08/creating-a-username-for-mongodb.png align="left")

### Pourquoi dois-je créer un nom d'utilisateur ?

Créer un nom d'utilisateur est essentiel pour gérer l'accès à votre cluster MongoDB. Un nom d'utilisateur, associé à un mot de passe, garantit que seuls les utilisateurs autorisés peuvent accéder à votre base de données. Cela ajoute une couche de sécurité, protégeant vos données contre les accès non autorisés.

### Avantages de la création d'un nom d'utilisateur :

* **Sécurité :** Garantit que votre base de données n'est accessible qu'à ceux qui disposent des identifiants corrects.

* **Gestion :** Vous pouvez suivre qui accède à votre base de données et gérer les permissions.

* **Responsabilité :** Aide à l'audit et à la surveillance des activités au sein de votre base de données.

## Étape 6 : Génération automatique de l'URL de connexion MongoDB

Une fois que vous cliquez sur le bouton **Créer un utilisateur**, vous serez redirigé vers une page où votre URL de connexion est générée automatiquement. Copiez cette URL et collez-la dans votre fichier `.env` pour établir une connexion à votre base de données. Alternativement, vous pouvez la coller directement dans votre fichier `app.js` ou `server.js`, comme je [l'ai expliqué dans mon article précédent](https://www.freecodecamp.org/news/how-to-build-an-event-app-with-node-js/).

N'hésitez pas à me faire savoir si vous avez besoin d'aide !

![Génération automatique de l'URL](https://www.freecodecamp.org/news/content/images/2024/08/getting-the-strringt-fot-conn.png align="left")

## Conclusion

En suivant les étapes décrites dans cet article, vous devriez maintenant comprendre comment obtenir votre URL de connexion MongoDB. N'oubliez pas, créer un nom d'utilisateur et un mot de passe pour l'accès à votre base de données est crucial pour assurer la sécurité et la gestion de vos données.

Si vous rencontrez des difficultés en cours de route, n'hésitez pas à vous référer à ce guide, à poser des questions ou mieux encore, à consulter la [documentation officielle de MongoDB](https://www.mongodb.com/resources/products/fundamentals/basics) pour obtenir de l'aide supplémentaire.

Si vous avez trouvé cet article utile, partagez-le avec d'autres personnes qui pourraient également le trouver intéressant.

Restez informé de mes projets en me suivant sur [Twitter](https://https//twitter.com/ijaydimples), [LinkedIn](https://www.linkedin.com/in/ijeoma-igboagu/) et [GitHub](https://github.com/ijayhub).

Merci d'avoir lu 💖.