---
title: Authentification avec Twitter dans ASP.NET Core 2.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-09T23:22:50.000Z'
originalURL: https://freecodecamp.org/news/authentication-using-twitter-in-asp-net-core-2-0-c7e02be30678
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NtO_nq3H7lfuDd9nL9pRWg.jpeg
tags:
- name: authentication
  slug: authentication
- name: Microsoft
  slug: microsoft
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Twitter
  slug: twitter
seo_title: Authentification avec Twitter dans ASP.NET Core 2.0
seo_desc: 'By Ankit Sharma

  Introduction

  Sometimes, we want our users to log in using their existing credentials from third-party
  applications such as Facebook, Twitter, Google and so on. In this article, we are
  going to look into authentication of an ASP.NET Co...'
---

Par Ankit Sharma

### Introduction

Parfois, nous voulons que nos utilisateurs se connectent en utilisant leurs identifiants existants à partir d'applications tierces telles que Facebook, Twitter, Google, etc. Dans cet article, nous allons examiner l'authentification d'une application ASP.NET Core à l'aide de Twitter.

### Prérequis

* Installer le SDK .NET Core 2.0.0 ou supérieur depuis [ici](https://www.microsoft.com/net/learn/get-started/windows#windowscmd).
* Installer la dernière version de Visual Studio 2017 Community Edition depuis [ici](https://www.visualstudio.com/downloads/).

### Créer une application Web MVC

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet. Après avoir sélectionné le projet, une boîte de dialogue "Nouveau Projet" s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche. Ensuite, sélectionnez "Application Web ASP.NET Core" parmi les types de projets disponibles. Donnez le nom du **projet comme Dem**_o_TwitterAuth et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/cq-CFz1g6xYXEsBVwGl0TAeFcTop50eW8-J9)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez observer deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez ".NET Core" et "ASP.NET Core 2.0" dans ces menus déroulants. Ensuite, sélectionnez le modèle "Application Web (Model-View-Controller)". Cliquez sur le bouton "Changer l'authentification", et une boîte de dialogue "Changer l'authentification" s'ouvrira. Sélectionnez "Compte d'utilisateur individuel" et cliquez sur OK. Maintenant, cliquez à nouveau sur OK pour créer votre application web.

![Image](https://cdn-media-1.freecodecamp.org/images/XTWNNIJlmrRbktYzfCqgKubRHB0CRDH298Z-)

Avant d'exécuter l'application, nous devons appliquer les migrations à notre application. Accédez à Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages.

Cela ouvrira la Console du gestionnaire de packages. Entrez la commande **Update-Database** et appuyez sur Entrée. Cela mettra à jour la base de données en utilisant les migrations Entity Framework Code First.

![Image](https://cdn-media-1.freecodecamp.org/images/oXXyV-TDBUPTbFPH0J8tgKm0qqlVqLuJivpK)

Appuyez sur F5 pour exécuter l'application. Vous pouvez voir une page d'accueil comme illustré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/ZD8J4FfPJlG7f7y3AYurYUWQ1H2i4KFu4SSC)

Notez l'URL depuis la barre d'adresse du navigateur. Dans ce cas, l'URL est [http://localhost:51763/](http://localhost:51763/). Nous avons besoin de cette URL pour configurer notre application Twitter, que nous allons faire dans la section suivante.

### Créer l'application Twitter

Avant de commencer à construire notre application ASP.NET Core 2.0, nous devons créer et configurer l'application Twitter afin de pouvoir l'utiliser pour authentifier notre application.

Accédez à [https://apps.twitter.com/](https://apps.twitter.com/) et connectez-vous en utilisant votre compte Twitter existant. Si vous n'avez pas de compte Twitter, vous devez en créer un. Vous ne pouvez pas continuer sans un compte Twitter. Une fois connecté, vous serez redirigé vers une page de gestion des applications similaire à celle illustrée ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/DhLIHOx6mS78mT2H-PsVCz5l7lDLfIiaZ8hc)

Elle affichera toutes vos applications Twitter configurées. Comme j'ai déjà configuré une application Twitter, elle est affichée. Si vous en créez une pour la première fois, elle n'affichera rien. Cliquez sur le bouton "Créer une nouvelle application" dans le coin supérieur droit. Cela ouvrira un formulaire et vous demandera de remplir les détails pour créer une nouvelle application.

![Image](https://cdn-media-1.freecodecamp.org/images/o6WpTlQrLxwkuJFormFZzQKCIDGJF56B4yZ6)

Vous pouvez remplir le formulaire avec les détails comme mentionné ci-dessous.

* **Nom**
Donnez un nom de votre choix. Mais il doit être universellement unique. Cela signifie que personne n'aurait dû utiliser ce nom auparavant pour créer une application Twitter. Cela fonctionne de la même manière qu'une adresse e-mail. Deux personnes ne peuvent pas avoir la même adresse e-mail. J'utilise le nom "DemoTwitterAuth" pour ce tutoriel. Si vous utilisez un nom déjà existant, vous obtiendrez une erreur "_L'application cliente a échoué à la validation : <votre nom entré> est déjà pris pour le Nom._"
* **Description**
Donnez une description appropriée.
* **Site Web**
Donnez l'URL de votre site web public. Mais pour ce but de démonstration, nous utiliserons une URL factice [http://demopage.com](http://demopage.com).

Si vous utilisez le format d'URL comme [_www.demopage.com_](http://www.demopage.com), vous obtiendrez une erreur "_L'application cliente a échoué à la validation : Format d'URL non valide._" Utilisez toujours le format d'URL comme [http://demopage.com](http://demopage.com).

* **URL de rappel**
Donnez l'URL de base de votre application avec _/signin-twitter_ ajouté à celle-ci. Pour ce tutoriel, l'URL sera [http://localhost:51763/signin-twitter](http://localhost:51763/signin-twitter).

Acceptez l'accord de développeur en cochant la case et cliquez sur le bouton "Créer votre application Twitter". Vous serez redirigé vers la page de votre nouvelle application Twitter, et vous verrez également un message de succès comme illustré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/YnVKPlP1oLmzvsIMT-SxN0qNaV823gRGQUAN)

Accédez à l'onglet "Clés et jetons d'accès" et notez les valeurs des champs Consumer Key (Clé API) et Consumer Secret (Secret API). Nous utiliserons ces valeurs dans l'application ASP.NET Core.

Les champs sont masqués dans cette image pour des raisons de sécurité.

![Image](https://cdn-media-1.freecodecamp.org/images/iTBe1Ka428jg0MbRF0sLIfVu5ZWCXll8QOx8)

Notre application Twitter a été créée avec succès.

### Configurer l'application Web pour utiliser l'authentification Twitter

Nous devons stocker les valeurs des champs Consumer Key (Clé API) et Consumer Secret (Secret API) dans notre application. Nous utiliserons l'outil Secret Manager à cette fin.

L'outil Secret Manager est un outil de projet qui peut être utilisé pour stocker des secrets tels que des mots de passe, des clés API, etc. pour un projet .NET Core pendant le processus de développement. Avec l'outil Secret Manager, nous pouvons associer des secrets d'application à un projet spécifique et les partager entre plusieurs projets.

Ouvrez votre application web une fois de plus et faites un clic droit sur le projet dans l'Explorateur de solutions. Sélectionnez "Gérer les secrets utilisateur" dans le menu contextuel.

![Image](https://cdn-media-1.freecodecamp.org/images/o1hmnNs6pwY1RQAW3dxtkxfEKL0T1KuDV5bY)

Un fichier **secrets.json** s'ouvrira. Mettez le code suivant dans celui-ci.

```json
{
    "Authentication:Twitter:ConsumerKey": "Votre Consumer Key ici",
    "Authentication:Twitter:ConsumerSecret": "Votre Consumer Secret ici"
}
```

Ouvrez maintenant le fichier **Startup.cs** et mettez le code suivant dans la méthode **ConfigureServices**.

```cs
services.AddAuthentication().AddTwitter(twitterOptions => {
    twitterOptions.ConsumerKey = Configuration["Authentication:Twitter:ConsumerKey"];
    twitterOptions.ConsumerSecret = Configuration["Authentication:Twitter:ConsumerSecret"];
});
```

Dans cette section de code, nous lisons ConsumerKey et ConsumerSecret à des fins d'authentification. Ainsi, finalement, **Startup.cs** ressemblera à ceci.

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
using DemoTwitterAuth.Data;
using DemoTwitterAuth.Models;
using DemoTwitterAuth.Services;
namespace DemoTwitterAuth {
    public class Startup {
        public Startup(IConfiguration configuration) {
            Configuration = configuration;
        }
        public IConfiguration Configuration {
            get;
        }
        // Cette méthode est appelée par le runtime. Utilisez cette méthode pour ajouter des services au conteneur.
        public void ConfigureServices(IServiceCollection services) {
            services.AddDbContext<ApplicationDbContext>(options => options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));
            services.AddIdentity<ApplicationUser, IdentityRole>().AddEntityFrameworkStores<ApplicationDbContext>().AddDefaultTokenProviders();
            services.AddAuthentication().AddTwitter(twitterOptions => {
                twitterOptions.ConsumerKey = Configuration["Authentication:Twitter:ConsumerKey"];
                twitterOptions.ConsumerSecret = Configuration["Authentication:Twitter:ConsumerSecret"];
            });
            // Ajouter des services d'application.
            services.AddTransient<IEmailSender, EmailSender>();
            services.AddMvc();
        }
        // Cette méthode est appelée par le runtime. Utilisez cette méthode pour configurer le pipeline de requête HTTP.
        public void Configure(IApplicationBuilder app, IHostingEnvironment env) {
            if (env.IsDevelopment()) {
                app.UseBrowserLink();
                app.UseDeveloperExceptionPage();
                app.UseDatabaseErrorPage();
            } else {
                app.UseExceptionHandler("/Home/Error");
            }
            app.UseStaticFiles();
            app.UseAuthentication();
            app.UseMvc(routes => {
                routes.MapRoute(name: "default", template: "{controller=Home}/{action=Index}/{id?}");
            });
        }
    }
}
```

Et avec cela, notre application est prête.

### Démo d'exécution

Lancez l'application et cliquez sur "Connexion" dans le coin supérieur droit de la page d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/aHMNgaRPh0NMXgIW4s2mrJtJk5vKqVV8XJ0H)

Vous serez redirigé vers la page [http://localhost:51763/Account/Login](http://localhost:51763/Account/Login), où vous pouvez voir l'option de connexion avec Twitter sur le côté droit de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/eZDBIjX9Pk8wsz60GqbiWDROIR13orQOBnjB)

En cliquant sur le bouton **Twitter**, vous serez redirigé vers la page d'autorisation de Twitter. Là, vous serez invité à remplir vos identifiants Twitter et à autoriser l'application Twitter à utiliser votre compte Twitter.

![Image](https://cdn-media-1.freecodecamp.org/images/WEHZKMOVfDrG3IoFe-LRxKRJSjetvTM3nQpN)

Une fois que vous cliquez sur Autoriser l'application, l'application prendra quelques instants pour authentifier votre compte Twitter. Après une authentification réussie, vous serez redirigé vers une page d'inscription dans votre application où vous devrez fournir une adresse e-mail à associer à votre compte.

![Image](https://cdn-media-1.freecodecamp.org/images/Bzg-YBfpHwWEkhTZMElngLxQQNo7K382MyWs)

Donnez une adresse e-mail et cliquez sur "S'inscrire". Vous serez redirigé vers la page d'accueil, mais cette fois, vous verrez également votre e-mail enregistré dans le coin supérieur droit.

![Image](https://cdn-media-1.freecodecamp.org/images/i1ajB6q3LxCN4Sl8MA511219WG1bgB5SsPpW)

### Conclusion

Nous avons créé avec succès une application Twitter et l'avons utilisée pour authentifier notre application ASP.NET Core.

Vous pouvez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/ASPCore.TwitterAuth).

Veuillez noter que dans le code source, le fichier **secrets.json** contient des valeurs factices. Vous devrez donc remplacer les valeurs par les clés de votre application Twitter avant de l'exécuter.

Vous pouvez également trouver cet article sur [C# Corner](http://www.c-sharpcorner.com/article/authentication-using-twitter-in-asp-net-core-2-0/).

Vous pouvez consulter mes autres articles sur ASP .NET Core [ici](http://ankitsharmablogs.com/category/asp-net-core/)

### Voir aussi

* [Authentification avec Facebook dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-facebook-in-asp-net-core-2-0/)
* [Authentification avec Google dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-google-asp-net-core-2-0/)
* [Authentification avec LinkedIn dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-linkedin-asp-net-core-2-0/)
* [Authentification par cookie avec ASP.NET Core 2.0](http://ankitsharmablogs.com/cookie-authentication-with-asp-net-core-2-0/)
* [ASP.NET Core — Authentification à deux facteurs avec Google Authenticator](http://ankitsharmablogs.com/asp-net-core-two-factor-authentication-using-google-authenticator/)

Publié à l'origine sur [ankitsharmablogs.com](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)