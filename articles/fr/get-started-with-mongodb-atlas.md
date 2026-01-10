---
title: Tutoriel MongoDB Atlas – Comment commencer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-04T08:12:37.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-mongodb-atlas
coverImage: https://cdn-media-2.freecodecamp.org/w1280/601ba92a0a2838549dcbe68a.jpg
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: freeCodeCamp Curriculum
  slug: freecodecamp-curriculum
- name: mongo
  slug: mongo
- name: MongoDB
  slug: mongodb
seo_title: Tutoriel MongoDB Atlas – Comment commencer
seo_desc: 'For the following challenges, you are going to use MongoDB to store data.
  To simplify the configuration, you''ll use a service called MongoDB Atlas.

  Create a MongoDB Atlas Account

  MongoDB Atlas is a MongoDB Database-as-a-Service platform, which means ...'
---

Pour les défis suivants, vous allez utiliser MongoDB pour stocker des données. Pour simplifier la configuration, vous utiliserez un service appelé MongoDB Atlas.

## Créer un compte MongoDB Atlas

MongoDB Atlas est une plateforme MongoDB Database-as-a-Service, ce qui signifie qu'ils configurent et hébergent la base de données pour vous. Votre seule responsabilité sera alors de peupler votre base de données avec ce qui compte : des données.

* [Allez ici](https://account.mongodb.com/account/register) pour vous inscrire à un nouveau compte MongoDB Atlas.
* Remplissez le formulaire d'inscription avec vos informations et cliquez sur **S'inscrire**.

## Créer un nouveau cluster

* Sur la page suivante, remplissez le nom de votre organisation, le nom de votre projet, sélectionnez JavaScript comme langage de programmation préféré, puis cliquez sur le bouton vert **Continuer**.
* Une fois que vous avez créé et vérifié votre compte, répondez aux questions d'intégration (votre objectif, le type d'application que vous construisez, votre langage de programmation préféré, etc.) et cliquez sur le bouton vert **Terminer**.
* Sur la page "Déployer une base de données cloud", cliquez sur le bouton **Créer** sous le type de cluster Partagé. Il s'agit de la seule option gratuite :

![La page "Déployer une base de données cloud" montrant le type de cluster Partagé gratuit comme dernière option à l'extrême droite, après les types de clusters Serverless et Dédié.](https://www.freecodecamp.org/news/content/images/2022/05/image-120.png)

* Dans le menu déroulant **Fournisseur cloud et région**, laissez tout par défaut. Votre valeur dépendra probablement de la région dans laquelle vous vous trouvez.
* Dans le menu déroulant **Niveau de cluster**, laissez cela par défaut, M0 Sandbox (RAM partagée, 512 Mo de stockage).
* Dans le menu déroulant **Nom du cluster**, vous pouvez donner un nom à votre cluster ou le laisser par défaut, Cluster0.
* Cliquez sur le bouton vert **Créer un cluster** en bas de l'écran.
* Vous devriez maintenant voir le message "Approvisionnement du cluster M0... Ce processus prendra 3 à 5 minutes." Attendez que le cluster soit créé avant de passer à l'étape suivante.

## Créer un nouvel utilisateur pour la base de données

* Sur le côté gauche de l'écran, sous **SÉCURITÉ**, cliquez sur **Accès à la base de données**.
* Cliquez sur le bouton vert **Ajouter un nouvel utilisateur de base de données**.
* Sous **Méthode d'authentification**, assurez-vous que **Mot de passe** est sélectionné, puis entrez un nom d'utilisateur et un mot de passe pour votre utilisateur.
* Sous **Privilèges de l'utilisateur de la base de données**, laissez cela comme option par défaut s'il y en a une – il devrait s'agir de **Lecture et écriture sur n'importe quelle base de données**. Vous devrez peut-être sélectionner cela manuellement si le défaut est vide. Vous pouvez sélectionner "Lecture et écriture sur n'importe quelle base de données" à partir du bouton "Ajouter un rôle intégré" comme montré ici :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image--6-.png)
_Cliquez sur "Ajouter un rôle intégré" pour sélectionner "Lecture et écriture sur n'importe quelle base de données"._

* Cliquez sur le bouton **Ajouter un utilisateur** pour créer votre nouvel utilisateur.

## Autoriser l'accès depuis toutes les adresses IP

* Sur le côté gauche de l'écran, sous **SÉCURITÉ**, cliquez sur **Accès réseau**.
* Cliquez sur le bouton vert **Ajouter une adresse IP**.
* Dans la fenêtre modale, cliquez sur le bouton **AUTORISER L'ACCÈS DE N'IMPORTE OÙ**. Vous devriez voir `0.0.0.0/0` dans le champ Entrée de la liste d'accès.
* Cliquez sur le bouton vert **Confirmer**.

## Se connecter à votre cluster

* Sur le côté gauche de l'écran, sous **DÉPLOIEMENT**, cliquez sur **Base de données**.
* Cliquez sur le bouton **Se connecter** pour votre cluster :

![Le bouton Se connecter pour votre cluster, Cluster0 si vous avez laissé le nom par défaut.](https://www.freecodecamp.org/news/content/images/2022/05/image-122.png)

* Dans la fenêtre modale contextuelle, cliquez sur **Connecter votre application**.
* Vous devriez voir la chaîne URI que vous utiliserez pour vous connecter à votre base de données, similaire à celle-ci : `mongodb+srv://<username>:<password>@<cluster-name>.prx1c.mongodb.net/<db-name>?retryWrites=true&w=majority`.
* Cliquez sur le bouton **Copier** pour copier votre URI dans votre presse-papiers.

Remarquez que les champs `<username>` et `<cluster-name>` de l'URI que vous avez copiée sont déjà remplis pour vous. Tout ce que vous avez à faire est de remplacer le champ `<password>` par celui que vous avez créé à l'étape précédente, et assurez-vous d'ajouter le nom de votre base de données avant la chaîne de requête (`?retryWrites=true&w=majority`).

Vous pouvez appeler votre base de données comme vous le souhaitez, mais il est bon de lui donner un nom mémorable pour votre projet. Par exemple, si vous travaillez sur les défis "MongoDB et Mongoose", vous pourriez remplacer `<db-name>` par `fcc-mongodb-et-mongoose` ou quelque chose de similaire.

## Se connecter à une base de données existante

Si vous avez déjà créé un cluster et une base de données et que vous souhaitez les connecter à une nouvelle application, suivez ces étapes :

* Sur le côté gauche de l'écran, sous **DÉPLOIEMENT**, cliquez sur **Base de données**.
* Trouvez votre cluster et cliquez sur le bouton **Parcourir les collections** pour voir une liste des bases de données et collections existantes.
* Copiez le nom de la base de données à laquelle vous souhaitez vous connecter et remplacez `<db-name>` par celui-ci dans la chaîne URI ci-dessus.

Et voilà — vous avez maintenant l'URI à ajouter à votre application et à vous connecter à votre base de données. Conservez cet URI en lieu sûr afin de pouvoir l'utiliser plus tard.