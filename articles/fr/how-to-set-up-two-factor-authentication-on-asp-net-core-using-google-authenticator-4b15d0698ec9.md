---
title: Comment configurer l'authentification à deux facteurs dans ASP.NET Core en
  utilisant Google Authenticator
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T23:11:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-two-factor-authentication-on-asp-net-core-using-google-authenticator-4b15d0698ec9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C2BqpQrShhPXLSSx7UTwmQ.jpeg
tags:
- name: Google
  slug: google
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: technology
  slug: technology
seo_title: Comment configurer l'authentification à deux facteurs dans ASP.NET Core
  en utilisant Google Authenticator
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we are going to learn how to perform two-factor authentication
  in an ASP.NET Core application using the Google Authenticator app.

  To use it, you need to configure the Google Authenticator app on your smar...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons apprendre comment effectuer l'authentification à deux facteurs dans une application ASP.NET Core en utilisant l'application Google Authenticator.

Pour l'utiliser, vous devez configurer l'application Google Authenticator sur votre smartphone en utilisant le code QR généré dans l'application web. Lorsque vous vous connectez à l'application web, vous devez entrer un code PIN à six chiffres qui sera généré dans l'application pour terminer l'authentification à deux facteurs. La clé générée dans l'application sera unique à votre identifiant utilisateur et est un mot de passe à usage unique basé sur le temps (TOTP) — c'est-à-dire qu'il expirera après un certain temps.

### Prérequis

* Installer le SDK .NET Core 2.0.0 ou supérieur depuis [ici](https://www.microsoft.com/net/core#windowscmd).
* Installer la dernière version de Visual Studio 2017 Community Edition depuis [ici](https://www.visualstudio.com/downloads/).

### Code Source

Avant de continuer, je vous recommande de récupérer le code source depuis [GitHub](https://github.com/AnkitSharma-007/ASPCore.Two-Factor-Authentication)

### Créer l'Application Web MVC

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet. Après avoir sélectionné le projet, une boîte de dialogue "Nouveau Projet" s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche. Ensuite, sélectionnez "Application Web ASP.NET Core" parmi les types de projets disponibles. Nommez le projet "TwoFactAuth" et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/5IZr6oGLiJEBiaR440jXpogP1cjJZGSg0fcs)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez voir deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez ".NET Core" et "ASP.NET Core 2.0" dans ces menus déroulants. Ensuite, sélectionnez le modèle "Application Web (Modèle-Vue-Contrôleur)". Cliquez sur le bouton "Changer l'Authentification". Une boîte de dialogue "Changer l'Authentification" s'ouvrira. Sélectionnez "Compte d'utilisateur individuel" et cliquez sur OK. Maintenant, cliquez à nouveau sur OK pour créer votre application web.

![Image](https://cdn-media-1.freecodecamp.org/images/ec4V1Smjem3XvQmvmEa8Ajx0cVKtQO73Eqer)

### Ajout de Codes QR pour configurer l'authentification à deux facteurs

Nous allons utiliser un code QR pour configurer et synchroniser l'application Google Authenticator avec notre application web. Téléchargez la bibliothèque JavaScript qrcode.js depuis [https://davidshimjs.github.io/qrcodejs/](https://davidshimjs.github.io/qrcodejs/) et placez-la dans le dossier "wwwroot\lib" de votre application. Maintenant, votre dossier "wwwroot" aura la structure suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/NzN3wSvkRdHO8fbbgqhzMGDb0TU6EiAelb-t)

Ouvrez le fichier "Views\Manage\EnableAuthenticator.cshtml". Vous trouverez _@section Scripts_ à la fin du fichier. Placez le code suivant dedans.

```
@section Scripts {      @await Html.PartialAsync("_ValidationScriptsPartial")      <script src="~/lib/qrcodejs/qrcode.js"></script>      <script type="text/javascript">          new QRCode(document.getElementById("qrCode"),              {                  text: "@Html.Raw(Model.AuthenticatorUri)",                  width: 200,                  height: 200              });      </script>  }
```

Ce fichier "EnableAuthenticator.cshtml" a déjà une div avec l'id "qrCode" (voir l'extrait de code ci-dessous). Nous générons un code QR à l'intérieur de cette div en utilisant la bibliothèque **qrcode.js**. Nous définissons également les dimensions du code QR en termes de largeur et de hauteur.

Ainsi, votre fichier "EnableAuthenticator.cshtml" ressemblera à ceci.

```
@model EnableAuthenticatorViewModel  @{      ViewData["Title"] = "Activer l'authentificateur";      ViewData.AddActivePage(ManageNavPages.TwoFactorAuthentication);  }    <h4>@ViewData["Title"]</h4>  <div>      <p>Pour utiliser une application d'authentification, suivez les étapes suivantes :</p>      <ol class="list">          <li>              <p>                  Téléchargez une application d'authentification à deux facteurs comme Microsoft Authenticator pour                  <a href="https://go.microsoft.com/fwlink/?Linkid=825071">Windows Phone</a>,                  <a href="https://go.microsoft.com/fwlink/?Linkid=825072">Android</a> et                  <a href="https://go.microsoft.com/fwlink/?Linkid=825073">iOS</a> ou                  Google Authenticator pour                  <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en">Android</a> et                  <a href="https://itunes.apple.com/us/app/google-authenticator/id388497605?mt=8">iOS</a>.              </p>          </li>          <li>              <p>Scannez le code QR ou entrez cette clé <kbd>@Model.SharedKey</kbd> dans votre application d'authentification à deux facteurs. Les espaces et la casse n'ont pas d'importance.</p>              <div class="alert alert-info">Pour activer la génération de codes QR, veuillez lire notre <a href="https://go.microsoft.com/fwlink/?Linkid=852423">documentation</a>.</div>              <div id="qrCode"></div>              <div id="qrCodeData" data-url="@Model.AuthenticatorUri"></div>          </li>          <li>              <p>                  Une fois que vous avez scanné le code QR ou entré la clé ci-dessus, votre application d'authentification à deux facteurs vous fournira                  un code unique. Entrez le code dans la boîte de confirmation ci-dessous.              </p>              <div class="row">                  <div class="col-md-6">                      <form method="post">                          <div class="form-group">                              <label asp-for="Code" class="control-label">Code de Vérification</label>                              <input asp-for="Code" class="form-control" autocomplete="off" />                              <span asp-validation-for="Code" class="text-danger"></span>                          </div>                          <button type="submit" class="btn btn-default">Vérifier</button>                          <div asp-validation-summary="ModelOnly" class="text-danger"></div>                      </form>                  </div>              </div>          </li>      </ol>  </div>  @section Scripts {      @await Html.PartialAsync("_ValidationScriptsPartial")      <script src="~/lib/qrcodejs/qrcode.js"></script>      <script type="text/javascript">          new QRCode(document.getElementById("qrCode"),              {                  text: "@Html.Raw(Model.AuthenticatorUri)",                  width: 200,                  height: 200              });      </script>  }
```

Lorsque nous exécutons le programme, un code QR sera généré dans cette vue. Vous pouvez ensuite configurer l'authentification à deux facteurs en utilisant Google Authenticator avec l'aide de ce code QR.

### Configurer l'authentification à deux facteurs

Avant d'exécuter l'application, nous devons appliquer les migrations à notre application. Accédez à Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages. Cela ouvrira la Console du gestionnaire de packages. Entrez la commande "Update-Database" et appuyez sur Entrée. Cela mettra à jour la base de données en utilisant les migrations Entity Framework Code First.

![Image](https://cdn-media-1.freecodecamp.org/images/tDY3UBG3ufUbbw0LAA01N0c9hAxPMQ-5-cav)

Appuyez sur F5 pour lancer l'application et cliquez sur "S'inscrire" dans le coin supérieur droit de la page d'accueil. Vous pouvez voir une page d'inscription d'utilisateur. Remplissez les détails et cliquez sur le bouton "S'inscrire" comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/tWrSzu0RRYMDBjFhNieFzwmYJwblB7hPYpkt)

Après une inscription réussie, vous serez connecté à l'application et redirigé vers la page d'accueil. Ici, vous pouvez voir votre identifiant de messagerie enregistré dans le coin supérieur droit de la page. Cliquez dessus pour accéder à la page "Gérer votre compte". Sélectionnez "TwoFactorAuthentication" dans le menu de gauche. Vous verrez une page similaire à celle montrée ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/qh4Kyd-XETDCOuiTsNAo4XuKBiP8kX26woY8)

Cliquez sur le bouton "Configurer l'application d'authentification". Vous pouvez voir un code QR généré sur votre écran — il demande un "Code de Vérification", comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/RK22LzdtmJ1Nx-sxWyeIAaH8cStx9VmMsoSY)

Vous devez installer l'application Google Authenticator sur votre smartphone. Cela vous permettra de scanner ce code QR afin de générer un Code de Vérification et de compléter la configuration de l'authentification à deux facteurs.

Téléchargez et installez Google Authenticator depuis le [Play Store](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en) pour Android et depuis l'[App Store](https://itunes.apple.com/us/app/google-authenticator/id388497605?mt=8) pour iOS. Nous utilisons un appareil Android pour cette démonstration.

Lancez l'application sur votre smartphone. Vous pouvez voir l'écran de bienvenue comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/tEJqq53r4dFXOA097u94Y0fZGGSvSWTjyX2J)

Cliquez sur "Commencer". Il vous demandera d'ajouter un compte en fournissant deux options :

1. Scanner un code-barres
2. Entrez une clé fournie

![Image](https://cdn-media-1.freecodecamp.org/images/bryFzQGbXD7oC7ieexuK6sNXMDlfzEDXjIEK)

Cliquez sur "Scanner un code-barres" et scannez le code QR généré par l'application web. Cela ajoutera un nouveau compte à Google Authenticator et générera un code PIN à six chiffres sur l'écran de votre mobile. C'est notre code d'authentification à deux facteurs. Il s'agit d'un TOTP (mot de passe à usage unique basé sur le temps). Vous pouvez observer qu'il change fréquemment (durée de vie de 30 secondes).

Maintenant, vous pouvez voir le nom de l'application ainsi que votre identifiant de messagerie enregistré dans l'application, comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/WXpRAzi07uMytCK2YS6BrT563wDJvMGcFFso)

Entrez ce code PIN dans la zone de texte Code de Vérification et cliquez sur vérifier. Après une vérification réussie, vous verrez un écran similaire à celui montré ci-dessous. Cela vous donnera les codes de récupération pour votre compte qui vous aideront à récupérer votre compte en cas de blocage. Prenez note de ces codes et conservez-les dans un endroit sûr.

![Image](https://cdn-media-1.freecodecamp.org/images/kjzE1nDGYby1Tiy2LRwPesYMixgKJ396JtUK)

Ainsi, la configuration de l'authentification à deux facteurs est complète. Vérifions si notre authentification à deux facteurs fonctionne correctement ou non.

### Démonstration d'Exécution

Déconnectez-vous de l'application et cliquez à nouveau sur connexion. Entrez votre identifiant de messagerie enregistré et votre mot de passe et cliquez sur connexion.

![Image](https://cdn-media-1.freecodecamp.org/images/-9fvzE-9jFdLLYYp1kWJoomjOW7jo9YhGYuU)

Maintenant, vous pouvez voir un écran d'authentification à deux facteurs demandant le code de l'authentificateur. Entrez le code qui est généré dans votre application Google Authenticator et cliquez sur Connexion. Vous serez connecté avec succès à l'application et redirigé vers la page d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/1opsb7gnoKI56CVI5jrSJA8Yy6ahWu7U3BK7)

Si vous cochez l'option "Se souvenir de cette machine", alors il ne demandera pas le code de l'authentificateur sur la même machine à nouveau. Vous pouvez sauter l'authentification à deux facteurs dans ce cas.

### Conclusion

Nous avons généré avec succès un code QR en utilisant la bibliothèque JavaScript [qrcode.js](https://davidshimjs.github.io/qrcodejs/) et l'avons utilisé pour configurer l'application Google Authenticator. Cette application générera un TOTP à six chiffres que vous devez entrer lors de la connexion à l'application web. Cela implémente l'authentification à deux facteurs dans une application ASP.NET Core.

Vous pouvez également trouver cet article sur [C# Corner](https://www.c-sharpcorner.com/article/asp-net-core-two-factor-authentication-using-google-authenticator/).

Vous pouvez consulter mes autres articles sur ASP .NET Core [ici](http://ankitsharmablogs.com/category/asp-net-core/).

### Voir Aussi

* [Authentification par Cookie Avec ASP.NET Core 2.0](http://ankitsharmablogs.com/cookie-authentication-with-asp-net-core-2-0/)
* [Authentification En Utilisant Facebook Dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-facebook-in-asp-net-core-2-0/)
* [Authentification En Utilisant Google Dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-google-asp-net-core-2-0/)
* [Authentification En Utilisant Twitter Dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-twitter-in-asp-net-core-2-0/)
* [Authentification En Utilisant LinkedIn Dans ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-linkedin-asp-net-core-2-0/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)