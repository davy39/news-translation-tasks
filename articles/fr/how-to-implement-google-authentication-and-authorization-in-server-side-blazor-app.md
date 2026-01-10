---
title: Comment implémenter l'authentification et l'autorisation Google dans une application
  Blazor côté serveur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-11T06:13:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-google-authentication-and-authorization-in-server-side-blazor-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca187740569d1a4ca4f1d.jpg
tags:
- name: authentication
  slug: authentication
- name: autherization
  slug: autherization
- name: Blazor
  slug: blazor
- name: Google
  slug: google
seo_title: Comment implémenter l'authentification et l'autorisation Google dans une
  application Blazor côté serveur
seo_desc: 'By Ankit Sharma

  Introduction

  The latest preview for .NET Core 3 (preview-6) has introduced the functionality
  to add authentication and authorization in a server-side Blazor application. In
  this article, we will learn how to implement authentication a...'
---

Par Ankit Sharma

## **Introduction**

La dernière version préliminaire de .NET Core 3 (preview-6) a introduit la fonctionnalité d'ajouter l'authentification et l'autorisation dans une application Blazor côté serveur. Dans cet article, nous allons apprendre comment implémenter l'authentification et l'autorisation en utilisant Google dans une application Blazor côté serveur. Vous pouvez vous référer à mon article précédent [Comprendre Blazor côté serveur](https://ankitsharmablogs.com/understanding-server-side-blazor/) pour obtenir des connaissances approfondies sur Blazor côté serveur.

## **Prérequis**

* Installez le dernier SDK .NET Core 3.0 Preview depuis [ici](https://dotnet.microsoft.com/download/dotnet-core/3.0).
* Installez la dernière version préliminaire de Visual Studio 2019 depuis [ici](https://visualstudio.com/preview).
* Installez l'extension ASP.NET Core Blazor Language Services depuis [ici](https://go.microsoft.com/fwlink/?linkid=870389).

## **Code Source**

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/Google-Authentication-with-server-side-Blazor)

## **Créer une application Blazor côté serveur**

Pour créer une application Blazor côté serveur, ouvrez Visual Studio 2019 et suivez les étapes mentionnées ci-dessous.

1. Cliquez sur « Créer un nouveau projet ».
2. Sélectionnez « Application Web ASP.NET Core » parmi les types de projets disponibles. Cliquez sur Suivant.
3. Un nouvel écran « Configurer votre nouveau projet » s'ouvrira. Mettez le nom du projet comme `BlazorGoogleAuth` et cliquez sur Créer.
4. Dans l'écran suivant, sélectionnez « .NET Core » et « ASP.NET Core 3.0 » dans les menus déroulants en haut à gauche.
5. Sélectionnez « Blazor (côté serveur) » dans la liste des modèles disponibles.
6. Cliquez sur le bouton Changer l'authentification, une boîte de dialogue « Changer l'authentification » s'ouvrira. Sélectionnez « Compte d'utilisateur individuel » et cliquez sur OK. Cliquez sur le bouton `Créer` pour créer l'application.

Ces étapes sont montrées dans l'image GIF ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/BlazorGoogleAuth.gif)

Avant d'exécuter l'application, nous devons appliquer les migrations à notre application. Naviguez vers Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages.

Cela ouvrira la Console du gestionnaire de packages. Entrez la commande `Update-Database` et appuyez sur Entrée. Cela mettra à jour la base de données en utilisant les migrations Entity Framework Code First.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/DBrestore.png)

Ouvrez les propriétés du projet en cliquant avec le bouton droit sur le projet dans l'explorateur de solutions et sélectionnez propriétés. Sélectionnez Debug dans le menu de gauche, puis faites défiler jusqu'en bas de la page. Notez l'URL avec SSL activé. Dans ce cas, l'URL est `https://localhost:44327/`. Nous avons besoin de cette URL pour configurer le projet Google API Console que nous allons faire dans notre prochaine section. Référez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/ProjectProperties.png)

## **Créer un projet Google API Console**

Nous devons créer un projet de console Google API et obtenir un identifiant client et un secret client pour configurer l'authentification Google dans notre application.

Naviguez vers [https://developers.google.com/identity/sign-in/web/sign-in#before_you_begin](https://developers.google.com/identity/sign-in/web/sign-in#before_you_begin). Connectez-vous avec votre compte Google. Suivez les étapes mentionnées ci-dessous.

1. Cliquez sur le bouton « Configurer un projet ».
2. Une boîte de dialogue « Configurer un projet pour Google Sign-in » s'ouvrira vous demandant de sélectionner ou de créer un nouveau projet.
3. Sélectionnez « Créer un nouveau projet » dans le menu déroulant. Nommez votre projet « BlazorAuthDemo » et cliquez sur Suivant.
4. Dans l'écran « Configurer votre client OAuth », mettez le nom de votre produit. Vous pouvez utiliser n'importe quel nom de votre choix. Ici, nous mettrons « BlazorAuth » comme nom de produit.
5. Dans l'écran suivant, sélectionnez « Serveur Web » dans le menu déroulant « D'où appelez-vous ».
6. Il vous demandera ensuite de mettre les « URIs de redirection autorisés ». Donnez l'URL de base de votre application avec `/signin-google` ajouté à celle-ci. Pour ce tutoriel, l'URL sera `https://localhost:44327/signin-google`.
7. Cliquez sur Créer. La boîte de dialogue vous présentera maintenant l'identifiant client et le secret client. Prenez note des champs `ClientId` et `ClientSecret`. Nous aurons besoin de ces valeurs pour configurer l'authentification Google dans notre application web.

Référez-vous au GIF ci-dessous pour une meilleure compréhension.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/GoogleAuthProject.gif)

> * Ne pas utiliser le mot « Google » dans le nom de votre produit. Vous recevrez une erreur et vous ne serez pas autorisé à créer l'application. Cela signifie que « BlazorGoogleAuth » est un nom de projet invalide.
> * Les noms de projet doivent comporter entre 4 et 30 caractères et ne peuvent contenir que des lettres, des chiffres, des espaces et des traits d'union.

## **Installation du package NuGet du middleware d'authentification Google**

Pour configurer le middleware ASP.NET Core pour l'authentification Google, nous devons installer le package nuget `Microsoft.AspNetCore.Authentication.Google` dans notre application. La version de ce package nuget doit correspondre à la version de .NET Core 3 que nous utilisons dans notre projet.

Ouvrez [https://www.nuget.org/packages/Microsoft.AspNetCore.Authentication.Google/](https://www.nuget.org/packages/Microsoft.AspNetCore.Authentication.Google/). Sélectionnez la version de .NET Core 3 dans l'« Historique des versions ». Copiez la commande de l'onglet « gestionnaire de packages ». Exécutez cette commande dans la console du gestionnaire de packages NuGet de notre application.

Pour cette application, nous utilisons `.NET Core 3.0.0-preview6.19307.2`. Par conséquent, nous exécuterons la commande suivante dans la console du gestionnaire de packages de notre application.

```
Install-Package Microsoft.AspNetCore.Authentication.Google -Version 3.0.0-preview6.19307.2
```

Référez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/NugetInstall.png)

## **Configurer l'application Blazor côté serveur pour utiliser l'authentification Google**

Nous devons stocker les valeurs des champs `ClientId` et `ClientSecret` dans notre application. Nous utiliserons l'outil Secret Manager à cette fin. L'outil Secret Manager est un outil de projet qui peut être utilisé pour stocker des secrets tels que des mots de passe, des clés API, etc. pour un projet .NET Core pendant le processus de développement. Avec l'outil Secret Manager, nous pouvons associer des secrets d'application à un projet spécifique et les partager entre plusieurs projets.

Ouvrez notre application web une fois de plus et cliquez avec le bouton droit sur le projet dans l'Explorateur de solutions. Sélectionnez Gérer les secrets utilisateur dans le menu contextuel. Un fichier `secrets.json` s'ouvrira. Mettez le code suivant dedans.

```
{
  "Authentication:Google:ClientId": "Votre ClientId Google ici",
  "Authentication:Google:ClientSecret": "Votre ClientSecret Google ici"
}
```

Ouvrez maintenant le fichier `Startup.cs` et mettez le code suivant dans la méthode `ConfigureServices`.

```
services.AddAuthentication().AddGoogle(googleOptions =>
{
  googleOptions.ClientId = Configuration["Authentication:Google:ClientId"];
  googleOptions.ClientSecret = Configuration["Authentication:Google:ClientSecret"];
});
```

Ce code lira le `ClientId` et le `ClientSecret` depuis le fichier `secrets.json`. La méthode `AddGoogle()` est une méthode d'extension et elle est utilisée pour configurer les options d'authentification Google pour notre application.

## **Ajout de l'autorisation aux pages Blazor**

Blazor a ajouté un nouveau composant intégré appelé `AuthorizeView`, qui est utilisé pour afficher différents contenus en fonction de l'état d'authentification de l'application. Ce composant affichera le composant enfant uniquement lorsque l'utilisateur est autorisé. Le composant `AuthorizeView` est configuré dans le fichier `\Shared\LoginDisplay.razor`.

Pour implémenter l'autorisation pour une page spécifique, nous devons utiliser l'attribut `[Authorize]`. Blazor a introduit une nouvelle directive `@attribute`, qui est utilisée pour inclure l'attribut `[Authorize]` pour une page. Dans cette application, nous appliquerons `[Authorize]` au composant FetchData. Cela empêchera l'accès non autorisé à ce composant. Ouvrez la page `FetchData.razor` et ajoutez les lignes suivantes en haut de la page.

```
@using Microsoft.AspNetCore.Authorization
@attribute [Authorize]
```

## **Démonstration d'exécution**

Lancez l'application. Naviguez vers le composant Fetch Data en cliquant sur le lien « Fetch data » dans le menu à gauche. Vous verrez un message « Non autorisé » affiché à l'écran. Cliquez sur « Log In » dans le menu en haut. Dans la page suivante, cliquez sur le bouton « Google » pour vous connecter avec Google. Une fois que vous êtes connecté avec succès, vous pourrez accéder au composant Fetch Data.

Référez-vous au GIF ci-dessous pour une meilleure compréhension.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/BlazorGoogleauthExecution.gif)

## **Conclusion**

Nous avons appris comment implémenter l'authentification et l'autorisation Google dans une application Blazor côté serveur. Nous avons créé et configuré un projet de console Google API pour implémenter l'authentification Google. Pour implémenter l'autorisation pour un composant spécifique dans Blazor, nous avons utilisé l'attribut [Authorize]. Nous avons utilisé le package nuget `Microsoft.AspNetCore.Authentication.Google` pour configurer le middleware pour l'authentification Google.

Veuillez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/Google-Authentication-with-server-side-Blazor) et jouez avec pour une meilleure compréhension.

Obtenez mon livre [Blazor Quick Start Guide](https://amzn.to/2OToEji) pour en apprendre davantage sur Blazor.

Préparation aux entretiens !!! Lisez mon article sur [C# Coding Questions For Technical Interviews](https://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/)

## **Voir aussi**

* [BlazorGrid – Un composant de grille réutilisable pour Blazor](https://ankitsharmablogs.com/blazorgrid-reusable-grid-component-for-blazor/)
* [Publier un composant Blazor sur la galerie Nuget](https://ankitsharmablogs.com/publishing-blazor-component-to-nuget-gallery/)
* [Déployer une application Blazor sur Azure](https://ankitsharmablogs.com/deploying-a-blazor-application-on-azure/)
* [Héberger une application Blazor sur Firebase](https://ankitsharmablogs.com/hosting-a-blazor-application-on-firebase/)
* [Blazor CRUD utilisant Google Cloud Firestore](https://ankitsharmablogs.com/blazor-crud-using-google-cloud-firestore/)
* [CRUD utilisant Blazor avec MongoDB](https://ankitsharmablogs.com/crud-using-blazor-with-mongodb/)
* [Application monopage utilisant Blazor côté serveur](https://ankitsharmablogs.com/single-page-application-using-server-side-blazor/)

_Publié à l'origine sur [https://ankitsharmablogs.com/google-authentication-and-authorization-in-server-side-blazor-app/](https://ankitsharmablogs.com/google-authentication-and-authorization-in-server-side-blazor-app/)_