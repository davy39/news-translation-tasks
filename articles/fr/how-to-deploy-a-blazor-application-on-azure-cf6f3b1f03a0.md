---
title: Comment déployer une application Blazor sur Azure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T19:48:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-blazor-application-on-azure-cf6f3b1f03a0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q_9GcuoDUbWGTSFjdIkduA.jpeg
tags:
- name: Azure
  slug: azure
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment déployer une application Blazor sur Azure
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will learn how to deploy an ASP.NET Core hosted Blazor application
  on Azure. We will use Visual Studio 2017 to publish the app. We will create a SQL
  database server on Azure to handle DB operations.

  Pr...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons apprendre comment déployer une application Blazor hébergée par ASP.NET Core sur Azure. Nous utiliserons Visual Studio 2017 pour publier l'application. Nous créerons un serveur de base de données SQL sur Azure pour gérer les opérations de base de données.

### Prérequis

* Installer le SDK .NET Core 2.1 ou supérieur depuis [ici](https://www.microsoft.com/net/learn/dotnet/hello-world-tutorial#windowscmd)
* Installer Visual Studio 2017 v15.7 ou supérieur depuis [ici](https://visualstudio.microsoft.com/downloads/)
* Installer l'extension ASP.NET Core Blazor Language Services depuis [ici](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)
* Un compte d'abonnement Azure. Vous pouvez créer un compte Azure gratuit [ici](https://azure.microsoft.com/en-in/free/)

Veuillez vous référer à mon article précédent [Cascading DropDownList in Blazor Using EF Core](https://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/) pour créer l'application que nous allons déployer dans ce tutoriel.

### Créer un groupe de ressources sur le portail Azure

Nous allons créer un groupe de ressources sur le portail Azure pour contenir toutes nos ressources sur Azure.

Connectez-vous au portail Azure et cliquez sur `Groupes de ressources` dans le menu de gauche, puis cliquez sur Ajouter. Une fenêtre "Groupe de ressources" s'ouvrira comme illustré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/20T1IWmzWvOLuzHR1enxqFy0-7bq2BtIKbUf)

Dans cette fenêtre, nous devons remplir les détails suivants :

* **Nom du groupe de ressources** : Donnez un nom unique à votre groupe de ressources. Ici, nous utiliserons le nom `BlazorDDLGroup`.
* **Abonnement** : Sélectionnez votre type d'abonnement dans la liste déroulante. Ici, nous sélectionnons l'abonnement "essai gratuit".
* **Emplacement du groupe de ressources** : Sélectionnez un emplacement pour votre groupe de ressources dans la liste déroulante.

### Création d'une base de données SQL et d'un serveur de base de données sur Azure

Nous allons créer la base de données SQL et un serveur de base de données sur le portail Azure pour gérer nos opérations de base de données.

Cliquez sur `Bases de données SQL` dans le menu de gauche de votre portail Azure, puis cliquez sur Ajouter. Une fenêtre "Base de données SQL" s'ouvrira comme illustré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/38Z5Qh737F4cvXYy5tmwFw1hIbOozmawjBUX)

Ici, vous devez remplir les détails suivants :

* **Nom de la base de données** : Donnez un nom à votre base de données. Ici, nous utiliserons `DDLDemodb` comme nom de notre base de données.
* **Abonnement** : Sélectionnez votre type d'abonnement dans la liste déroulante. Ici, nous sélectionnons l'abonnement "essai gratuit".
* **Groupe de ressources** : Sélectionnez le nom du groupe de ressources que nous avons créé dans l'étape précédente.
* **Sélectionner la source** : Cette liste déroulante contient une liste de bases de données avec des données prédéfinies fournies par Azure. Comme nous créons notre base de données personnalisée, sélectionnez `Base de données vide` dans cette liste déroulante.
* **Niveau tarifaire** : Sélectionnez un niveau tarifaire pour votre base de données.

Avant de créer la base de données, nous devons créer un serveur de base de données pour la base de données SQL. Cliquez sur "Configurer les paramètres requis du serveur" puis cliquez sur `Créer un nouveau serveur`. Une fenêtre "Nouveau serveur" s'ouvrira comme illustré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/r6hMMqOkb0djwPQN42D3UI5nznTp72qdhhou)

Ici, nous devons fournir les détails suivants :

* **Nom du serveur** : Fournissez un nom pour votre serveur de base de données. Ici, nous utiliserons `ddldemoserver`. Le serveur de base de données sera créé en ajoutant `.database.windows.net` au nom de serveur fourni par l'utilisateur. Ainsi, le nom du serveur sera `ddldbserver.database.windows.net` dans ce cas.
* **Connexion admin du serveur** : Mettez un nom de connexion admin pour votre serveur de base de données.
* **Mot de passe** : Mettez le mot de passe de connexion correspondant à la connexion admin de votre serveur de base de données.
* **Emplacement** : Sélectionnez un emplacement pour votre serveur dans la liste déroulante.

Cochez la case "Autoriser les services Azure à accéder au serveur" et cliquez sur `Sélectionner` pour créer votre serveur de base de données.

**Note :** Le mot "admin" est restreint pour le nom d'utilisateur administrateur du serveur de base de données. Utilisez un autre nom d'utilisateur que "admin".

Une fois le serveur de base de données créé, vous serez redirigé vers la fenêtre "Base de données SQL". Vous devez cliquer sur le bouton "Créer" pour créer votre base de données.

Voici tout le processus expliqué dans un gif.

![Image](https://cdn-media-1.freecodecamp.org/images/6D4EPQq3NvDVgHHYLyldCYjHAf-rv2aRYlWH)

### Création des tables de la base de données

La base de données `DDLDemodb` ne contient pas les tables que nous utilisons dans notre application. Nous allons nous connecter à la base de données Azure en utilisant SQL Server Management Studio (SSMS) pour créer nos objets de base de données.

Ouvrez SSMS sur votre machine et mettez le nom du serveur comme `ddldbserver.database.windows.net`. Fournissez l'identifiant de l'utilisateur admin et le mot de passe que vous avez configurés dans la section précédente. Ensuite, cliquez sur "Connecter".

Vous obtiendrez une fenêtre contextuelle pour configurer la règle de pare-feu afin d'accéder à la base de données Azure. Connectez-vous avec vos identifiants de compte Azure et ajoutez l'adresse IP de votre machine sous `Règle de pare-feu`. Cliquez sur OK pour vous connecter au serveur de base de données Azure. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/3EZsH1Q0JygMDppF3q9vfDrDo4P4FL9sfOiC)

Une fois la connexion réussie, vous pouvez voir la base de données `DDLDemodb` sur le serveur. Voir mon article précédent [Cascading DropDownList in Blazor Using EF Core](https://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/). Exécutez les commandes SQL pour créer et insérer des données d'exemple dans les tables Country et Cities que nous utilisons dans notre application.

### Définition de la chaîne de connexion de la base de données

Après avoir créé les objets de la base de données, nous devons remplacer la chaîne de connexion de la base de données locale dans notre application par la chaîne de connexion de la base de données Azure.

Ouvrez le portail Azure et cliquez sur `Bases de données SQL` dans le menu de gauche. Une fenêtre s'ouvrira affichant la liste de toutes les bases de données que vous avez créées sur le portail Azure. Cliquez sur la base de données `DDLDemodb` et sélectionnez `Chaînes de connexion` dans le menu. Sélectionnez l'onglet `ADO.NET` et copiez la chaîne de connexion. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/TyolX9Lz7LWJaCjPWslSDToB1sxtKguXBfNp)

Vous devez mettre l'identifiant de l'utilisateur admin et le mot de passe pour le serveur de base de données que vous avez configurés précédemment dans cette chaîne de connexion.

Ouvrez l'application `BlazorDDL` en utilisant Visual Studio, naviguez jusqu'à `BlazorDDL.Shared/Models/myTestDBContext.cs` et remplacez la chaîne de connexion locale par cette nouvelle chaîne de connexion.

Lancez votre application depuis Visual Studio pour vérifier si la nouvelle chaîne de connexion est configurée correctement et si vous êtes en mesure d'accéder à la base de données Azure.

Si l'application ne fonctionne pas et que vous ne pouvez pas vous connecter à la base de données, vérifiez si votre chaîne de connexion est correcte ou non. Une fois que l'application fonctionne comme prévu sur votre machine locale, passez à la section suivante pour la publier sur Azure.

### Publication de l'application Blazor sur Azure

Pour publier l'application Blazor sur Azure, faites un clic droit sur le projet Serveur de votre solution et cliquez sur publier. Dans ce cas, ce sera `BlazorDDL.Server >> P`ublier.

La fenêtre `Choisir une cible de publication` s'ouvrira. Sélectionnez `Service d'application` dans le menu de gauche. Sélectionnez le bouton radio `Créer un nouveau` et cliquez sur le bouton "Créer un profil". Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/gUBsJCxOAcKBI4MT3gklIr4NAgVeF2UhYCB6)

La fenêtre suivante vous demandera de vous connecter à votre compte Azure si vous n'êtes pas connecté. Une fois la connexion réussie, une fenêtre `Créer un service d'application` s'ouvrira. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/XhCbINl98SIiBYISo1rWwho10j6RcQSi2VtM)

Les champs de cette fenêtre ont des valeurs par défaut selon la configuration de votre compte Azure. Cependant, vous pouvez changer ces valeurs en fonction de vos besoins.

Vous pouvez remplir les détails comme mentionné ci-dessous :

* **Nom de l'application** : Fournissez un nom d'application pour votre application. Le nom de l'application est soumis à disponibilité. Si le nom de l'application que vous avez fourni est déjà utilisé, vous devez donner un nouveau nom d'application. L'URL publique du site Web sera le nom de l'application suivi de `.azurewebsites.net`. Ici, nous utilisons le nom `BlazorDDLDemo`, donc l'URL de notre site Web sera `BlazorDDLDemo.azurewebsites.net`.
* **Abonnement** : Sélectionnez votre type d'abonnement dans la liste déroulante.
* **Groupe de ressources** : Sélectionnez le nom de votre groupe de ressources, qui est `BlazorDDLGroup` dans ce cas.
* **Plan d'hébergement** : Vous pouvez soit utiliser le plan existant, soit sélectionner un nouveau plan en cliquant sur le lien "Nouveau...".
* **Application Insights** : Vous pouvez choisir une valeur dans la liste déroulante. Cela fournira des analyses pour votre site Web.

Cliquez sur le bouton "Créer" pour démarrer le déploiement de l'application sur Azure. Cela prendra quelques minutes selon la vitesse de votre connexion Internet.

Une fois le déploiement réussi, cliquez sur le bouton "Publier" pour publier l'application sur Azure. Une fois l'application publiée avec succès, le site Web sera lancé automatiquement dans le navigateur par défaut de votre machine. Vous pouvez également accéder au site Web en utilisant l'URL `BlazorDDLDemo.azurewebsites.net`.

Vous pouvez voir l'application dans votre navigateur comme illustré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/awDc-mIvjrILWDsq7X4lhTMlA9iAAH9UcJKd)

### Conclusion

Dans cet article, nous avons appris comment déployer et publier une application Blazor sur Azure. Nous avons créé une base de données SQL et un serveur de base de données sur Azure et les avons utilisés dans notre application pour gérer les opérations de base de données.

Obtenez mon livre [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) pour en savoir plus sur Blazor.

Vous pouvez également lire mes autres articles [ici](https://ankitsharmablogs.com/).

### Voir aussi

* [Déployer une application Blazor sur IIS](https://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)
* [Blazor — CRUD avec MongoDB](https://ankitsharmablogs.com/crud-using-blazor-with-mongodb/)
* [Interopérabilité JavaScript dans Blazor](https://ankitsharmablogs.com/javascript-interop-in-blazor/)
* [Comprendre Blazor côté serveur](https://ankitsharmablogs.com/understanding-server-side-blazor/)
* [Application monopage utilisant Blazor côté serveur](https://ankitsharmablogs.com/single-page-application-using-server-side-blazor/)
* [ASP.NET Core — CRUD utilisant Blazor et Entity Framework Core](https://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)