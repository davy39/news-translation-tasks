---
title: Authentification avec Google dans ASP.NET Core 2.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-09T23:11:56.000Z'
originalURL: https://freecodecamp.org/news/authentication-using-google-in-asp-net-core-2-0-5ec32c803e23
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CXNQW2ZhXOKhjBHMqxPT0A.jpeg
tags:
- name: authentication
  slug: authentication
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Authentification avec Google dans ASP.NET Core 2.0
seo_desc: 'By Ankit Sharma

  Introduction

  Sometimes, we want our users to log in using their existing credentials from third-party
  applications, such as Facebook, Twitter, Google, and so on. In this article, we
  are going to look into authentication of an ASP.NET ...'
---

Par Ankit Sharma

### Introduction

Parfois, nous voulons que nos utilisateurs se connectent en utilisant leurs identifiants existants à partir d'applications tierces, telles que Facebook, Twitter, Google, etc. Dans cet article, nous allons examiner l'authentification d'une application ASP.NET Core à l'aide d'un compte Google.

### Prérequis

* Installer le SDK .NET Core 2.0.0 ou supérieur depuis [ici](https://www.microsoft.com/net/core#windowscmd).
* Installer la dernière version de Visual Studio 2017 depuis [ici](https://www.visualstudio.com/downloads/).

### Créer une application Web MVC

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet. Après avoir sélectionné le projet, une boîte de dialogue "Nouveau Projet" s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche. Ensuite, sélectionnez "Application Web ASP.NET Core" parmi les types de projets disponibles. Donnez le nom du **projet** comme GoogleAuth et appuyez sur OK. Référez-vous à cette image.

![Image](https://cdn-media-1.freecodecamp.org/images/bj60EpFTyp-HFWKLB7DmC4wMquHcIloOg-1X)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez observer deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez ".NET Core" et "ASP.NET Core 2.0" dans ces menus déroulants. Ensuite, sélectionnez le modèle "Application Web (Modèle-Vue-Contrôleur)". Cliquez sur le bouton Changer l'authentification, et une boîte de dialogue "Changer l'authentification" s'ouvrira. Sélectionnez "Compte d'utilisateur individuel" et cliquez sur OK. Maintenant, cliquez à nouveau sur OK pour créer notre application web.

![Image](https://cdn-media-1.freecodecamp.org/images/GNw22x0TBogwDhIK2M4IYygdIXX4rLckERlm)

Avant d'exécuter l'application, nous devons appliquer les migrations à notre application.

Accédez à Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages.

Cela ouvrira la Console du gestionnaire de packages. Entrez la commande **Update-Database** et appuyez sur Entrée. Cela mettra à jour la base de données en utilisant les migrations Entity Framework Code First.

![Image](https://cdn-media-1.freecodecamp.org/images/07TaK6SUF3S202GzqF9Nbq6J3r2e7OQjiSQw)

Appuyez sur F5 pour exécuter l'application. Vous verrez une page d'accueil, comme illustré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/JY4-SU8LbJTlccEjz90WLH0xCij1XKsLDPsk)

Notez l'URL de la barre d'adresse du navigateur. Dans ce cas, l'URL est [http://localhost:51792/.](http://localhost:51792/.) Nous avons besoin de cette URL pour configurer notre application Google, que nous allons faire dans la section suivante.

### Créer l'application Google

Nous devons créer une nouvelle application Google sur la console de l'API Google. Accédez à [https://console.developers.google.com/projectselector/apis/library](https://console.developers.google.com/projectselector/apis/library) et connectez-vous en utilisant votre compte Google. Si vous n'avez pas de compte Google, vous devez en créer un. Vous ne pouvez pas continuer sans un compte Google. Une fois connecté, vous serez redirigé vers la page de la bibliothèque du gestionnaire d'API, similaire à celle illustrée ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/a1xEVPx9r5yvKP6zB6zECOORArngmXpd7Xh9)

Cliquez sur le bouton Créer pour accéder à la page "Nouveau Projet" où vous devez créer un nouveau projet. Le champ "Nom du projet" sera automatiquement rempli avec un nom par défaut fourni par Google. Si vous le souhaitez, vous pouvez le remplacer par votre propre nom personnalisé. Pour ce tutoriel, nous utiliserons le nom par défaut. Acceptez les conditions d'utilisation, puis cliquez sur le bouton **Créer**_._

![Image](https://cdn-media-1.freecodecamp.org/images/PmA1mwOOv-NpLgOVnpGpcMjpjffw2gqa8ytD)

Votre projet sera créé avec succès et vous serez redirigé vers la page de la bibliothèque d'API, similaire à celle illustrée ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/ZGibyBmIl89AeIXJ8Z3efwMFaD8IYwxeYZc-)

Recherchez l'API Google+ dans la barre de recherche et sélectionnez l'API Google+ dans les résultats de recherche. Référez-vous à l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/hEYfCuIhx4BZ99pCcKSR2ely7wW8dCEzld96)

Après avoir sélectionné l'option API Google+, vous serez redirigé vers une page comme illustré ci-dessous, où vous devez cliquer sur le bouton **Activer**.

![Image](https://cdn-media-1.freecodecamp.org/images/Gny-yyUfUwRhCbYngaTgplBh544fkBANWnev)

Après cela, l'API Google+ sera activée et vous serez redirigé vers la page d'accueil de l'API. Cliquez sur le bouton **Créer des identifiants** sur le côté droit de la page pour configurer les secrets de votre API.

![Image](https://cdn-media-1.freecodecamp.org/images/oEi6OKokWaFdE1s4BuwwNtu3VWBmAEbleUxb)

Vous verrez un formulaire "Ajouter des identifiants à votre projet".

![Image](https://cdn-media-1.freecodecamp.org/images/bhrrKkJfLUUk8Elx6Zb85zyFy-jeTrNXN7Rq)

Ce formulaire comporte trois sections.

Remplissez les détails des sections comme décrit ci-dessous.

#### Section 1 — Découvrez de quel type d'identifiants vous avez besoin

* Quelle API utilisez-vous ? — API Google+
* Depuis où allez-vous appeler l'API ? — Serveur web (par exemple, Node.js, Tomcat)
* Quelles données allez-vous accéder ? — Données utilisateur

Et cliquez sur le bouton **De quels identifiants ai-je besoin** ? Vous serez redirigé vers la section 2.

![Image](https://cdn-media-1.freecodecamp.org/images/jqgmfBYceZPa9-tRIgnVRex3vkhRhsqYC3ZF)

#### Section 2 — Créer un ID client OAuth 2.0

* Nom — La valeur par défaut fournie par Google.
* Origines JavaScript autorisées — Laissez-le vide.
* URIs de redirection autorisées — Donnez l'URL de base de votre application avec **/signin-google** ajouté à celle-ci. Pour ce tutoriel, l'URL sera [http://localhost:51792/signin-google.](http://localhost:51792/signin-google.) Après avoir entré l'URL, appuyez sur TAB pour ajouter la valeur.

Après cela, cliquez sur le bouton **Créer un ID client**. Vous serez redirigé vers la section 3.

![Image](https://cdn-media-1.freecodecamp.org/images/lexZ2KQD32HEh0doFARzIfxu5kXgGGwEiRhz)

#### Section 3 — Configurer l'écran de consentement OAuth 2.0

* Adresse e-mail — Sélectionnez votre adresse e-mail dans le menu déroulant. Cette valeur est masquée dans l'image ci-dessus pour des raisons de confidentialité.
* Nom du produit affiché aux utilisateurs — Entrez un nom de produit. Ici, nous utilisons "AuthDemo" comme nom de produit.

**Remarque** : N'utilisez pas le mot "Google" dans le nom de votre produit. Vous recevrez une erreur et vous ne pourrez pas créer l'application. Cela signifie que "GoogleAuthDemo" est un nom invalide.

Cliquez sur continuer.

![Image](https://cdn-media-1.freecodecamp.org/images/IumxI-6hzLont2cozVITaaQweJVhKtxP4yRD)

Vos identifiants ont été créés avec succès. Cliquez sur **Télécharger** pour télécharger un fichier JSON sur votre machine locale avec tous les secrets de votre application, puis cliquez sur **Terminé** pour compléter le processus.

Ouvrez le fichier **client_id.json** que vous venez de télécharger et notez les champs **ClientId** et **ClientSecret**. Nous aurons besoin de ces valeurs pour configurer l'authentification Google dans notre application web.

### Configurer votre application Web pour utiliser l'authentification Google

Nous devons stocker les valeurs des champs ClientId et ClientSecret dans notre application. Nous utiliserons l'outil Secret Manager à cette fin. L'outil Secret Manager est un outil de projet qui peut être utilisé pour stocker des secrets tels que des mots de passe, des clés API, etc. pour un projet .NET Core pendant le processus de développement. Avec l'outil Secret Manager, nous pouvons associer des secrets d'application à un projet spécifique et les partager entre plusieurs projets.

Ouvrez à nouveau votre application web et faites un clic droit sur le projet dans l'Explorateur de solutions. Sélectionnez **Gérer les secrets utilisateur** dans le menu contextuel.

![Image](https://cdn-media-1.freecodecamp.org/images/YooMRhsrDBiWW3UV4C1oZoT5NnsWBpcDZi2R)

Un fichier **secrets.json** s'ouvrira. Placez le code suivant dans celui-ci :

```json
{  
  "Authentication:Google:ClientId": "Votre ClientId Google ici",  
  "Authentication:Google:ClientSecret": "Votre ClientSecret Google ici"  
}
```

Ouvrez maintenant le fichier **Startup.cs** et placez le code suivant dans la méthode **ConfigureServices** :

```cs
services.AddAuthentication().AddGoogle(googleOptions =>  
{  
    googleOptions.ClientId = Configuration["Authentication:Google:ClientId"];  
    googleOptions.ClientSecret = Configuration["Authentication:Google:ClientSecret"];  
});
```

Dans cette section de code, nous lisons ClientId et ClientSecret à des fins d'authentification. Ainsi, finalement, **Startup.cs** ressemblera à ceci :

```cs
using System;  
using System.Collections.Generic;  
using System.Linq;  
using System.Threading.Tasks;  
using Microsoft.AspNetCore.Builder;  
using Microsoft.AspNetCore.Identity;  
using Microsoft.EntityFrameworkCore;  
using Microsoft.AspNetCore.Hosting;  
using Microsoft.Extensions.Configuration;  
using Microsoft.Extensions.DependencyInjection;  
using GoogleAuth.Data;  
using GoogleAuth.Models;  
using GoogleAuth.Services;  
  
namespace GoogleAuth  
{  
    public class Startup  
    {  
        public Startup(IConfiguration configuration)  
        {  
            Configuration = configuration;  
        }  
  
        public IConfiguration Configuration { get; }  
  
        // Cette méthode est appelée par le runtime. Utilisez cette méthode pour ajouter des services au conteneur.  
        public void ConfigureServices(IServiceCollection services)  
        {  
            services.AddDbContext<ApplicationDbContext>(options =>  
                options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));  
  
            services.AddIdentity<ApplicationUser, IdentityRole>()  
                .AddEntityFrameworkStores<ApplicationDbContext>()  
                .AddDefaultTokenProviders();  
  
            services.AddAuthentication().AddGoogle(googleOptions =>  
            {  
                googleOptions.ClientId = Configuration["Authentication:Google:ClientId"];  
                googleOptions.ClientSecret = Configuration["Authentication:Google:ClientSecret"];  
            });  
  
            // Ajouter des services d'application.  
            services.AddTransient<IEmailSender, EmailSender>();  
  
            services.AddMvc();  
        }  
  
        // Cette méthode est appelée par le runtime. Utilisez cette méthode pour configurer le pipeline de requête HTTP.  
        public void Configure(IApplicationBuilder app, IHostingEnvironment env)  
        {  
            if (env.IsDevelopment())  
            {  
                app.UseBrowserLink();  
                app.UseDeveloperExceptionPage();  
                app.UseDatabaseErrorPage();  
            }  
            else  
            {  
                app.UseExceptionHandler("/Home/Error");  
            }  
  
            app.UseStaticFiles();  
  
            app.UseAuthentication();  
  
            app.UseMvc(routes =>  
            {  
                routes.MapRoute(  
                    name: "default",  
                    template: "{controller=Home}/{action=Index}/{id?}");  
            });  
        }  
    }  
}
```

Et avec cela, notre application est prête.

### Démo d'exécution

Lancez l'application et cliquez sur Connexion en haut à droite de la page d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/23zs7ahiIW7wMaRAB5d-UeoCU1AXrgI6b0gN)

Vous serez redirigé vers la page [http://localhost:51792/Account/Login](http://localhost:51792/Account/Login), où vous pouvez voir l'option de connexion avec Google sur le côté droit de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/Pez9fV-RzqpnMBb4hxL0ZFAW83df481uVutu)

En cliquant sur le bouton **Google**, vous serez redirigé vers la page de connexion Google. Là, vous serez invité à remplir vos identifiants Google et à autoriser l'application Google à utiliser votre compte Google.

Après une authentification réussie avec Google, vous serez redirigé vers une page d'inscription dans votre application où vous devrez remplir une adresse e-mail à associer à votre compte. L'identifiant Gmail que vous avez utilisé pour vous connecter sera déjà rempli dans le champ d'adresse e-mail. Si vous souhaitez utiliser une autre adresse e-mail, vous pouvez la modifier ici.

![Image](https://cdn-media-1.freecodecamp.org/images/IKLOYBbeGQG-wi1ll5YPFgIVfBaT31iFLDr9)

Cliquez sur s'inscrire, vous serez redirigé vers la page d'accueil. Mais cette fois, vous pouvez également voir que votre e-mail enregistré est en haut à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/rUdpYiZfpO5I-2M7P0qwoZ3Bq2zHwpkUcplV)

### Conclusion

Nous avons créé et configuré avec succès une application Google+ et l'avons utilisée pour authentifier notre application ASP.NET Core.

Vous pouvez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/ASPCore.GoogleAuth).

Veuillez noter que le fichier **secrets.json** contient des valeurs factices. Vous devrez remplacer les valeurs par les clés de votre application Google avant de l'exécuter.

Vous pouvez également trouver cet article sur [C# Corner](http://www.c-sharpcorner.com/article/authentication-using-google-in-asp-net-core-2-0/).

Vous pouvez consulter mes autres articles sur ASP .NET Core [ici](http://ankitsharmablogs.com/category/asp-net-core/)

### Voir aussi

* [Authentification avec LinkedIn dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-linkedin-asp-net-core-2-0/)
* [Authentification avec Twitter dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-twitter-in-asp-net-core-2-0/)
* [Authentification avec Facebook dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-facebook-in-asp-net-core-2-0/)
* [Authentification par cookie avec ASP.NET Core 2.0](http://ankitsharmablogs.com/cookie-authentication-with-asp-net-core-2-0/)
* [ASP.NET Core — Authentification à deux facteurs avec Google Authenticator](http://ankitsharmablogs.com/asp-net-core-two-factor-authentication-using-google-authenticator/)

Publié à l'origine sur [ankitsharmablogs.com](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)