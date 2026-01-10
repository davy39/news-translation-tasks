---
title: Comment authentifier vos utilisateurs avec LinkedIn dans ASP.NET Core 2.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T18:56:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-authenticate-your-users-with-linkedin-in-asp-net-core-2-0-3f84c5cd2f1b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RRYg2jQ-11JV9ToXthgI5Q.png
tags:
- name: authentication
  slug: authentication
- name: JavaScript
  slug: javascript
- name: LinkedIn
  slug: linkedin
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment authentifier vos utilisateurs avec LinkedIn dans ASP.NET Core 2.0
seo_desc: 'By Ankit Sharma

  Introduction

  Sometimes, we want our users to log in using their existing credentials from third-party
  applications, such as Facebook, Twitter, Google, LinkedIn, and so on. In this article,
  we are going to look into the authentication ...'
---

Par Ankit Sharma

### Introduction

Parfois, nous voulons que nos utilisateurs se connectent en utilisant leurs identifiants existants à partir d'applications tierces, telles que Facebook, Twitter, Google, LinkedIn, etc. Dans cet article, nous allons examiner l'authentification d'une application ASP.NET Core à l'aide d'un compte LinkedIn.

### Prérequis

* Installez le SDK .NET Core 2.0.0 ou supérieur depuis [ici](https://www.microsoft.com/net/core#windowscmd).
* Installez la dernière version de Visual Studio 2017 depuis [ici](https://www.visualstudio.com/downloads/).

### Créer une application Web MVC

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet. Après avoir sélectionné le projet, une boîte de dialogue "Nouveau Projet" s'ouvrira.

Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche. Ensuite, sélectionnez "Application Web ASP.NET Core" parmi les types de projets disponibles.

Nommez le projet **LinkdinAuth** et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/E79vbhBT7QoeX-w-PTjHfS3zfY9-p4X1-lRr)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez voir deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez ".NET Core" et "ASP.NET Core 2.0" dans ces menus déroulants.

Ensuite, sélectionnez le modèle "Application Web (Modèle-Vue-Contrôleur)".

Cliquez sur le bouton Changer l'authentification, et une boîte de dialogue "Changer l'authentification" s'ouvrira.

Sélectionnez "Compte d'utilisateur individuel" et cliquez sur OK. Cliquez à nouveau sur OK pour créer notre application web.

![Image](https://cdn-media-1.freecodecamp.org/images/na6nloJuhfcQn5O87p4zcnDujh1cWqbeRpqZ)

Avant d'exécuter l'application, nous devons appliquer les migrations à notre application.

Accédez à Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages.

Cela ouvrira la Console du gestionnaire de packages. Entrez la commande **Update-Database** et appuyez sur Entrée. Cela mettra à jour la base de données en utilisant les migrations Entity Framework Code First.

![Image](https://cdn-media-1.freecodecamp.org/images/bmvIJTMzQbQAF0BViIyn44zHO3vXV15-XtF9)

Appuyez sur F5 pour exécuter l'application. Vous pouvez voir une page d'accueil comme illustré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/ySQg5QFxS2mDs0B1w7-t-2xft57vk3KKmFYN)

### Créer l'application LinkedIn

Accédez à [https://www.linkedin.com/developer/apps](https://www.linkedin.com/developer/apps) et connectez-vous en utilisant votre compte LinkedIn. Si vous n'avez pas de compte LinkedIn, vous devez en créer un, car vous ne pouvez pas continuer sans.

Une fois connecté, vous serez redirigé vers la page **Mes Applications** similaire à celle illustrée ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/0NTuW8X48p50EU4R9ID8jBNMAEMMqaV5VSKE)

Cliquez sur le bouton **Créer une Application** pour accéder à la page **Créer une Nouvelle Application**. Ici, vous devez remplir les détails pour créer une nouvelle application LinkedIn.

* Nom de l'entreprise : donnez un nom approprié. Ici, nous utilisons le nom **DemoCompany**.
* Nom de l'application : c'est le nom de votre application LinkedIn. Donnez un nom approprié de votre choix.

Note : **Ne pas utiliser le mot "LinkedIn" dans le nom de votre produit**. Vous recevrez une erreur "Le nom de l'application ne peut pas contenir LinkedIn" et vous ne serez pas autorisé à créer l'application. Cela signifie que "LinkedinAuthDemo" est un nom invalide. Voir l'image ci-dessous.

* Description de l'application : donnez une description appropriée de votre application.
* Logo de l'application : vous devez télécharger un logo pour votre application. Si vous n'avez pas de logo, téléchargez simplement une image. Veuillez fournir l'image du logo de votre application au format PNG ou JPEG. L'image doit être carrée et d'au moins 80 x 80 pixels, et ne pas dépasser 5 Mo en taille.
* Utilisation de l'application : sélectionnez une valeur appropriée dans le menu déroulant.
* URL du site web : fournissez l'URL de votre site web public. Pour ce tutoriel, nous utiliserons une URL fictive [http://demopage.com.](http://demopage.com.)

Note : Si vous utilisez le format d'URL [_www.demopage.com_,](http://www.demopage.com,) vous recevrez une erreur "Veuillez entrer une URL valide". Utilisez toujours un format d'URL tel que [_http://demopage.com_.](http://demopage.com.)

* Email professionnel : donnez votre adresse email. Si vous ne souhaitez pas fournir votre adresse email personnelle, vous pouvez également utiliser une adresse email fictive telle que _xyz@gmail.com_
* Téléphone professionnel : fournissez votre numéro de contact. Pour ce tutoriel, j'utilise un numéro de téléphone fictif 123456789.

![Image](https://cdn-media-1.freecodecamp.org/images/nrsaGLAUcu30hYK9cbm21yxF9Y6rzZs-3guA)

Gardez à l'esprit que tous les champs de ce formulaire sont obligatoires, vous devez donc fournir des valeurs appropriées à tous. Une fois que vous avez rempli tous les détails, cliquez sur le bouton **Soumettre**. Si le formulaire ne contient aucune erreur, votre application LinkedIn sera créée avec succès et vous serez redirigé vers la page d'accueil de l'application.

Ici, vous voyez les champs **Client ID** et **Client Secret** dans la section Clés d'authentification. Notez ces valeurs, car nous en aurons besoin pour configurer l'authentification LinkedIn dans notre application web.

Dans le champ URL de redirection autorisées, fournissez l'URL de base de votre application avec **/signin-linkedin** ajouté à celle-ci. Pour ce tutoriel, l'URL sera [_http://localhost:52676/signin-linkedin_.](http://localhost:52676/signin-linkedin.) Après avoir entré l'URL, appuyez sur le bouton **Ajouter** adjacent pour ajouter la valeur. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/M3IGu7qbkUcgohdAXfi4zVvV-irPJIgJoR8u)

### Configurer votre application web pour utiliser l'authentification LinkedIn

Nous allons utiliser un package NuGet tiers **AspNet.Security.OAuth.LinkedIn** pour implémenter l'authentification LinkedIn dans notre application web. Ouvrez le gestionnaire de packages NuGet (Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages) et entrez la commande suivante. Appuyez sur Entrée pour l'installer.

```
Install-Package AspNet.Security.OAuth.LinkedIn -Version 2.0.0-rc2-final
```

Ce package NuGet est maintenu par aspnet-contrib. Vous pouvez en savoir plus sur ce package [ici](https://www.nuget.org/packages/AspNet.Security.OAuth.LinkedIn/2.0.0-rc2-final).

Nous devons stocker les valeurs des champs **Client ID** et **Client Secret** dans notre application. Nous allons utiliser l'outil Secret Manager à cette fin. L'outil Secret Manager est un outil de projet qui peut être utilisé pour stocker des secrets tels que des mots de passe, des clés API, etc. pour un projet .NET Core pendant le processus de développement. Avec l'outil Secret Manager, nous pouvons associer des secrets d'application à un projet spécifique et les partager entre plusieurs projets.

Ouvrez à nouveau notre application web et faites un clic droit sur le projet dans l'Explorateur de solutions. Sélectionnez "Gérer les secrets utilisateur" dans le menu contextuel.

![Image](https://cdn-media-1.freecodecamp.org/images/qBERap-JaDEhvoaoYUwbzoUmBbaJFryXHuTh)

Un fichier **secrets.json** s'ouvrira. Mettez le code suivant dans celui-ci.

```
{    "Authentication:LinkedIn:ClientId": "Votre ClientId ici",    "Authentication:LinkedIn:ClientSecret": "Votre ClientSecret ici"  }
```

Maintenant, ouvrez le fichier **Startup.cs** et mettez le code suivant dans la méthode **ConfigureServices**.

```
services.AddAuthentication().AddLinkedIn(options =>{    options.ClientId = Configuration["Authentication:LinkedIn:ClientId"];    options.ClientSecret = Configuration["Authentication:LinkedIn:ClientSecret"];    options.Events= new OAuthEvents()    {        OnRemoteFailure = loginFailureHandler =>        {            var authProperties = options.StateDataFormat.Unprotect(loginFailureHandler.Request.Query["state"]);            loginFailureHandler.Response.Redirect("/Account/login");            loginFailureHandler.HandleResponse();            return Task.FromResult(0);        }    };});
```

Dans cette section de code, nous lisons les valeurs **Client ID** et **Client Secret** du fichier **secrets.json** à des fins d'authentification. Nous gérons également l'événement "OnRemoteFailure" dans cette section de code. Ainsi, si l'utilisateur refuse l'accès à leur compte LinkedIn, ils seront redirigés vers la page de connexion.

Ainsi, finalement, **Startup.cs** ressemblera à ceci.

```
using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;using Microsoft.AspNetCore.Builder;using Microsoft.AspNetCore.Identity;using Microsoft.EntityFrameworkCore;using Microsoft.AspNetCore.Hosting;using Microsoft.Extensions.Configuration;using Microsoft.Extensions.DependencyInjection;using LinkdinAuth.Data;using LinkdinAuth.Models;using LinkdinAuth.Services;using Microsoft.AspNetCore.Http;using Microsoft.AspNetCore.Authentication.OAuth;  namespace LinkdinAuth{    public class Startup    {        public Startup(IConfiguration configuration)        {            Configuration = configuration;        }          public IConfiguration Configuration { get; }          // Cette méthode est appelée par le runtime. Utilisez cette méthode pour ajouter des services au conteneur.        public void ConfigureServices(IServiceCollection services)        {            services.AddDbContext<ApplicationDbContext>(options =>                options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));              services.AddIdentity<ApplicationUser, IdentityRole>()                .AddEntityFrameworkStores<ApplicationDbContext>()                .AddDefaultTokenProviders();              services.AddAuthentication().AddLinkedIn(options =>            {                options.ClientId = Configuration["Authentication:LinkedIn:ClientId"];                options.ClientSecret = Configuration["Authentication:LinkedIn:ClientSecret"];                  options.Events= new OAuthEvents()                {                    OnRemoteFailure = loginFailureHandler =>                    {                        var authProperties = options.StateDataFormat.Unprotect(loginFailureHandler.Request.Query["state"]);                        loginFailureHandler.Response.Redirect("/Account/login");                        loginFailureHandler.HandleResponse();                        return Task.FromResult(0);                    }                };              });               // Ajouter des services d'application.            services.AddTransient<IEmailSender, EmailSender>();              services.AddMvc();        }          // Cette méthode est appelée par le runtime. Utilisez cette méthode pour configurer le pipeline de requête HTTP.        public void Configure(IApplicationBuilder app, IHostingEnvironment env)        {            if (env.IsDevelopment())            {                app.UseBrowserLink();                app.UseDeveloperExceptionPage();                app.UseDatabaseErrorPage();            }            else            {                app.UseExceptionHandler("/Home/Error");            }                          app.UseStaticFiles();              app.UseAuthentication();              app.UseMvc(routes =>            {                routes.MapRoute(                    name: "default",                    template: "{controller=Home}/{action=Index}/{id?}");            });        }    }}
```

Et avec cela, notre application est prête.

### Démo d'exécution

Lancez l'application et cliquez sur Connexion dans le coin supérieur droit de la page d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/vbFttzcLv92wHLH2-ygU4mR0VYpyf5GXYrQM)

Vous serez redirigé vers [_http://localhost:52676/Account/Login_](http://localhost:52676/Account/Login), où vous pouvez voir l'option de connexion en utilisant LinkedIn sur le côté droit de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/Y0xfdJTNoKlRGBHQ80NlU4xEyx6pEMNXpCEK)

En cliquant sur le bouton **LinkedIn**, vous serez redirigé vers la page d'autorisation LinkedIn. Là, vous serez invité à remplir vos identifiants LinkedIn et à autoriser l'application LinkedIn à utiliser votre compte LinkedIn.

![Image](https://cdn-media-1.freecodecamp.org/images/pGsM2ZoAeJnvHXM5RFiD1ZaT5ChhAWZQ-aEa)

Entrez vos identifiants LinkedIn et cliquez sur le bouton **Autoriser l'accès**. L'application prendra quelques instants pour authentifier votre compte LinkedIn. Une fois l'authentification réussie avec LinkedIn, vous serez redirigé vers une page d'inscription dans votre application où vous devrez fournir une adresse email à associer à votre compte.

![Image](https://cdn-media-1.freecodecamp.org/images/Lc6AxdswuS0k0rYbuqniUlMPlfNe2FHG2cYy)

Donnez une adresse email et cliquez sur s'inscrire, et vous serez redirigé vers la page d'accueil. Mais cette fois, vous pouvez également voir votre adresse email enregistrée dans le coin supérieur droit. Ainsi, nous nous sommes connectés avec succès à notre application ASP .NET Core en utilisant LinkedIn.

![Image](https://cdn-media-1.freecodecamp.org/images/gu9vHE9TEehppVZdX3DljEjonZx62Ycy7Uzq)

### Conclusion

Nous avons créé avec succès une application LinkedIn et l'avons utilisée pour authentifier notre application ASP.NET Core.

Vous pouvez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/ASPCore.LinkedInAuth).

Veuillez noter que le fichier **secrets.json** contient des valeurs fictives. Vous devrez remplacer les valeurs par les clés de votre application LinkedIn avant de l'exécuter.

Vous pouvez également trouver cet article sur [C# Corner](http://www.c-sharpcorner.com/article/authentication-using-linkedin-in-asp-net-core-2-0/).

Vous pouvez consulter mes autres articles sur ASP .NET Core [ici](http://ankitsharmablogs.com/category/asp-net-core/).

### Voir aussi

* [Authentification avec Google dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-google-asp-net-core-2-0/)
* [Authentification avec Twitter dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-twitter-in-asp-net-core-2-0/)
* [Authentification avec Facebook dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-facebook-in-asp-net-core-2-0/)
* [Authentification par cookie avec ASP.NET Core 2.0](http://ankitsharmablogs.com/cookie-authentication-with-asp-net-core-2-0/)
* [ASP.NET Core — Authentification à deux facteurs avec Google Authenticator](http://ankitsharmablogs.com/asp-net-core-two-factor-authentication-using-google-authenticator/)

Publié à l'origine sur [ankitsharmablogs.com](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)