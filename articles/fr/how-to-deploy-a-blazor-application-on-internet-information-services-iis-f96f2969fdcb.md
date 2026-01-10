---
title: Comment déployer une application Blazor sur Internet Information Services (IIS)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T15:12:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-blazor-application-on-internet-information-services-iis-f96f2969fdcb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qZqIAFSLGBjADpNTsnu9Pw.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Blazor
  slug: blazor
- name: Microsoft
  slug: microsoft
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment déployer une application Blazor sur Internet Information Services
  (IIS)
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will learn how to deploy an ASP.NET Core hosted Blazor application
  with the help of IIS 10 on a Windows 10 machine. We will be using Visual Studio
  2017 to publish the app and SQL Server 2014 to handle ...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons apprendre comment déployer une application Blazor hébergée par ASP.NET Core à l'aide d'IIS 10 sur une machine Windows 10. Nous utiliserons Visual Studio 2017 pour publier l'application et SQL Server 2014 pour gérer les opérations de base de données. Nous allons également résoudre certains des problèmes d'hébergement courants pour une application Blazor.

### Prérequis

* Installer IIS sur votre machine
* Installer le module URL Rewrite depuis [ici](https://www.iis.net/downloads/microsoft/url-rewrite)

Veuillez vous référer à mon article précédent, [Comment créer une liste déroulante en cascade dans Blazor en utilisant EF Core](https://medium.freecodecamp.org/how-to-create-a-cascading-dropdownlist-in-blazor-using-ef-core-d230bb5bff5f), pour créer l'application que nous allons déployer dans ce tutoriel.

### **Installation du bundle d'hébergement .NET Core**

Puisque nous allons déployer une application Blazor hébergée par ASP.NET Core, la première étape consiste à installer le bundle d'hébergement .NET Core sur notre machine.

Suivez les étapes ci-dessous pour télécharger le bundle d'hébergement .NET Core :

#### **Étape 1**

Ouvrez [https://www.microsoft.com/net/download/all](https://www.microsoft.com/net/download/all)

#### **Étape 2**

Sélectionnez la dernière version non préversion de .NET Core Runtime dans la liste. Pour ce tutoriel, nous sélectionnerons .NET Core Runtime 2.0.7.

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/yP2moxch5u2x6B6mUdKoT4PRFIKtScQSZgqp)

#### **Étape 3**

Sur la page de téléchargement de .NET Core Runtime, faites défiler jusqu'à la section Windows, sélectionnez le lien « Hosting Bundle Installer » pour télécharger le « .NET Core Hosting Bundle ». Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/blMT51CVhgidICtzTNRUxy3XfyyHMysiXuSN)

Une fois le téléchargement terminé, double-cliquez pour commencer l'installation. Vous verrez une fenêtre similaire à celle ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/jWrEFc9edDlLk9VwB8yRaXKDUiSUQHPRQj-7)

#### **Note Importante**

1. Le bundle d'hébergement .NET Core doit être installé uniquement après l'installation d'IIS. Si vous installez le bundle avant IIS, vous devez réparer le bundle après l'installation d'IIS afin qu'il mette à jour ses dépendances pour IIS.
2. Redémarrez la machine après l'installation du bundle d'hébergement .NET Core.

### Publication de l'application Blazor

Une fois l'installation du bundle d'hébergement .NET Core réussie et que vous avez redémarré votre machine, ouvrez la solution de l'application Blazor avec VS 2017.

Faites un clic droit sur le projet Serveur de votre solution et cliquez sur publier. Dans ce cas, ce sera BlazorDDL.Server >> Publier.

![Image](https://cdn-media-1.freecodecamp.org/images/9SX4ook9WusBea8tm8oajC4uxAsxZJ5cGcye)

Vous verrez un écran similaire à celui ci-dessous. Sélectionnez Dossier dans le menu de gauche et fournissez un chemin de dossier. Vous pouvez fournir n'importe quel chemin de dossier où vous souhaitez publier votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/p7U2FgDb0YjAqkvO-obPuDhbqfrSOf1VrDlT)

Cliquez sur publier. Visual Studio commencera à publier votre application. Si aucune erreur de build n'est présente, votre application sera publiée avec succès dans le dossier que vous avez mentionné.

Après la publication réussie, nous passerons à la configuration d'IIS.

### Configuration d'IIS

Ouvrez IIS et faites un clic droit sur Sites >> Ajouter un site Web.

Une boîte de dialogue « Ajouter un site Web » s'ouvrira. Ici, nous devons fournir des détails dans trois champs :

1. Nom du site : Mettez un nom de votre choix. Ici, je mettrai « ankitsite ».
2. Chemin physique : Le chemin vers le dossier où vous avez publié votre application.
3. Nom d'hôte : C'est le nom que nous mettons dans le navigateur pour accéder à notre application. Nous mettrons **ankitsite.com** pour cette démonstration.

Cliquez sur OK pour créer le site Web. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/gYvAyWLMlngmRpVgIDgAW0j7ZOcZHtVEDGyR)

L'étape suivante consiste à configurer le « Application Pool » pour notre site. Le nom du pool d'applications sera le même que le « Nom du site » que nous avons fourni à l'étape précédente. Par conséquent, dans ce cas, le nom du pool d'applications sera « ankitsite ».

Cliquez sur « Application Pools » dans le panneau de gauche et double-cliquez sur le pool « ankitsite ». Cela ouvrira une fenêtre « modifier le pool d'applications ». Sélectionnez « No Managed Code » dans la liste déroulante de la version .NET CLR. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/6Vzduhtg1YwMvYQUBDZuX6VSaHiSWhwa7Ako)

Voici l'ensemble du processus de configuration d'IIS expliqué dans une image gif.

![Image](https://cdn-media-1.freecodecamp.org/images/dNoMZnLndfBk7e1Elct13SB0ovTqhMUb136h)

### Configuration de l'hôte DNS

La dernière étape consiste à configurer notre fichier hôte DNS.

Accédez au chemin **C:\Windows\System32\drivers\etc** sur votre machine et ouvrez le fichier « hosts » avec n'importe quel éditeur de texte.

![Image](https://cdn-media-1.freecodecamp.org/images/R9jJHC5-mkBuAYjO0Lk17QlzeFxSVyFNFBiQ)

Nous devons ajouter le nom d'hôte que nous avons fourni dans IIS contre l'adresse IP localhost. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/U1dOrUOXwAcK6EhDnbSOJJja7ex9n7QBrTL-)

Et maintenant, nous avons réussi à héberger une application Blazor sur IIS.

### Démonstration d'exécution

Ouvrez n'importe quel navigateur sur votre machine et entrez le nom d'hôte que vous avez configuré. Vous pouvez voir que l'application s'ouvrira dans la fenêtre du navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/Vcb7-n8EFzMdE9H9MWDQZU8-seObr43fOGPs)

### Résolution des problèmes d'hébergement courants

Dans cette section, nous allons examiner certains des problèmes courants que vous pouvez rencontrer lors de l'hébergement d'une application Blazor.

1. Vous ne pouvez pas ouvrir le site Web et obtenez une erreur DNS non trouvé

Vérifiez si le nom d'hôte est correctement configuré dans le fichier hôte. Assurez-vous que votre machine n'est pas connectée à un serveur VPN. De plus, si vous utilisez un proxy Web, désactivez-le.

2. Erreur HTTP 500.19 — Erreur interne du serveur — La page demandée ne peut pas être accessible car les données de configuration associées à la page sont invalides.

Ce message d'erreur est clair. Le dossier de publication est inaccessible en raison de permissions insuffisantes. Accordez l'autorisation de lecture au groupe IIS_IUSRS sur le dossier de publication afin qu'il puisse accéder au fichier Web.config.

3. Le site Web se charge mais les données ne sont pas peuplées, et vous obtenez une erreur 500 du serveur interne

Assurez-vous que votre chaîne de connexion est au bon format. L'identifiant utilisateur que vous avez spécifié dans votre chaîne de connexion doit avoir les permissions db_datareader et db_datawriter. Si le problème persiste, accordez à l'utilisateur la permission db_owner.

4. Les données ne sont pas peuplées et vous obtenez une exception « opération non autorisée ».

Ce problème apparaît généralement lorsque vous essayez d'effectuer une opération PUT, POST ou DELETE dans votre API Web. Pour atténuer ce problème, nous devons modifier la configuration de l'installation IIS.

Accédez au Panneau de configuration >> Activer ou désactiver des fonctionnalités Windows. Ensuite, accédez à Services d'information Internet >> Services Web >> Fonctionnalités HTTP courantes et décochez l'option « Publication WebDAV » et cliquez sur OK. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/YA0t4fAfl53A7-LJfqT2ovgkXX1FQmH9PqpL)

5. « Échec du chargement de <web API> : Aucun en-tête 'Access-Control-Allow-Origin' n'est présent sur la ressource demandée. »

La cause de cette erreur est que le client et le serveur de l'application ne sont pas sur le même port. Le navigateur restreindra l'application à effectuer des appels d'API Web en raison de la politique de même origine. Pour résoudre ce problème, vous devez activer les requêtes Cross-Origin (CORS) dans votre application. Veuillez vous référer aux documents Microsoft sur [Activer les requêtes Cross-Origin (CORS) dans ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/security/cors?view=aspnetcore-2.1).

Lorsque vous republiez l'application, n'oubliez pas d'actualiser votre site Web ainsi que le pool d'applications dans IIS.

### Conclusion

Dans cet article, nous avons appris comment déployer une application Blazor sur IIS sur une machine Windows. Nous avons également appris comment résoudre certains des problèmes d'hébergement courants lors du déploiement d'une application Blazor.

Obtenez mon livre [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) pour en savoir plus sur Blazor.

Vous pouvez consulter mes autres articles sur Blazor [ici](http://ankitsharmablogs.com/category/blazor/).

Vous pouvez également trouver cet article sur [C# Corner](https://www.c-sharpcorner.com/article/deploying-a-blazor-application-on-iis/).

### Voir aussi

* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [ASP.NET Core — CRUD Using Angular 5 And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [ASP.NET Core — CRUD With React.js And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-with-react-js-and-entity-framework-core/)
* [ASP.NET Core — Using Highcharts With Angular 5](http://ankitsharmablogs.com/asp-net-core-using-highcharts-with-angular-5/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)