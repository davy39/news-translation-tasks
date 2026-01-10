---
title: Comment implémenter JavaScript Interop dans Blazor
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T18:30:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-javascript-interop-in-blazor-9f91d263ec51
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RijhIwu_gn98_W_QnYcGAA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Comment implémenter JavaScript Interop dans Blazor
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will learn about JavaScript Interop in Blazor. We will understand
  what JavaScript Interop is and how we can implement it in Blazor with the help of
  a sample application.

  We will be using Visual Studio ...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons apprendre à propos de JavaScript Interop dans Blazor. Nous allons comprendre ce qu'est JavaScript Interop et comment nous pouvons l'implémenter dans Blazor avec l'aide d'une application d'exemple.

Nous allons utiliser Visual Studio Code pour notre démonstration.

### Qu'est-ce que JavaScript Interop ?

Blazor utilise JavaScript pour démarrer le runtime .NET. Il est capable d'utiliser n'importe quelle bibliothèque JS. Le code C# peut appeler une fonction/API JS et le code JS peut appeler n'importe quelle méthode C#. Cette propriété d'appeler une méthode JS à partir du code C# et vice versa est appelée JavaScript Interop. Blazor utilise JavaScript Interop pour gérer la manipulation du DOM et les appels d'API de navigateur.

JavaScript Interop est la fonctionnalité fournie par WebAssembly, puisque Blazor s'exécute sur Mono et Mono est compilé en WebAssembly. Par conséquent, Blazor peut également implémenter cette fonctionnalité.

### Prérequis

* Installer le SDK .NET Core 2.1 ou supérieur depuis [ici](https://www.microsoft.com/net/learn/get-started/windows#windowscmd).
* Installer Visual Studio Code depuis [ici](https://code.visualstudio.com/).

### Code Source

Obtenez le code source depuis [Github](https://github.com/AnkitSharma-007/Blazor-JSInterop).

### Création de l'application Blazor

Nous allons créer une application Blazor en utilisant Windows PowerShell.

#### **Étape 1**

Tout d'abord, nous allons installer les modèles de framework Blazor sur notre machine.

Ouvrez le dossier où vous souhaitez créer votre projet. Ouvrez Windows PowerShell avec shift + clic droit >> Ouvrir la fenêtre PowerShell ici.

Tapez la commande suivante :

```
dotnet new -i Microsoft.AspNetCore.Blazor.Templates
```

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/xyduFrvvobk8FKc3R4BRiAuZXmiJf6kNSv-0)

#### **Étape 2**

Tapez la commande suivante pour créer notre application Blazor :

```
dotnet new blazor -o BlazorJSDemo
```

Cela créera une application Blazor avec le nom **BlazorJSDemo**. Voir l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/oInrxVk6aoBMy6u9enSL3XjGiKUrSZy9augG)

### Ajout de la page Razor à notre application

Ouvrez l'application **BlazorJSDemo** avec VS Code. Vous pouvez observer la structure des dossiers dans l'Explorateur de solutions, comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/yD2TqOZ31I3GFMavWBRJ5FeVs13NOe2xU0Di)

Nous allons ajouter notre page Razor dans le dossier **Pages**.

Créez un nouveau fichier en cliquant avec le bouton droit sur le dossier Pages et sélectionnez Nouveau Fichier. Nommez le fichier **JSDemo.cshtml**. Ce fichier contiendra le code HTML pour gérer l'interface utilisateur de notre application.

De même, ajoutez un autre fichier **JSDemo.cshtml.cs**. Ce fichier contiendra le code C# pour gérer notre logique métier.

Maintenant, notre dossier **Pages** aura la structure suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/7uGmB3024FB7kaSQo-ZLMEnikX4CbA-tjEWa)

### Appel d'une fonction JavaScript depuis C#

Tout d'abord, nous allons écrire nos fonctions JavaScript dans le **fichier index.html**. Ouvrez le fichier **wwwroot/index.html** et mettez le code suivant :

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width">
    <title>BlazorJSDemo</title>
    <base href="/" />
    <link href="css/bootstrap/bootstrap.min.css" rel="stylesheet" />
    <link href="css/site.css" rel="stylesheet" />

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

</head>

<body>
    <app>Chargement...</app>

    <script src="_framework/blazor.webassembly.js"></script>

    <script>
        function JSMethod() {
            $("#demop").text("Méthode JavaScript invoquée");
        }
    </script>

</body>

</html>
```

Ici, nous avons inclus la référence CDN à la bibliothèque JQuery dans la section <head> afin de pouvoir gérer la manipulation du DOM.

Dans la section <body>, nous avons défini notre fonction JS. Le nom de la fonction est JSMethod et elle n'accepte aucun argument. Lorsqu'elle est déclenchée, elle définira le texte d'une balise <p> ayant l'id "demop" à "Méthode JavaScript invoquée".

**Note Importante**

1. N'écrivez pas votre code JS dans le fichier **.cshtml**. Cela n'est pas autorisé dans Blazor et le compilateur générera une erreur. Placez toujours votre code JS dans le fichier **wwwroot/index.html**.
2. Ajoutez toujours votre balise <script> personnalisée après "<script src='_framework/blazor.webassembly.js'></script>" dans la section **<body>** du fichier index.html. Cela garantit que votre script personnalisé s'exécutera après le chargement du script "blazor.webassembly.js".

Ouvrez **JSDemo.cshtml.cs** et mettez le code suivant :

```cs
using Microsoft.AspNetCore.Blazor.Components;
using Microsoft.JSInterop;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorJSDemo.Pages
{
    public class JSDemoModel : BlazorComponent
    {
        protected static string message { get; set; }

        protected void CallJSMethod()
        {
            JSRuntime.Current.InvokeAsync<bool>("JSMethod");
        }
    }
}
```

La méthode **CallJSMethod** appellera notre fonction JS "JSMethod" en utilisant la méthode "JSRuntime.Current.InvokeAsync". Cette méthode peut prendre deux paramètres — le nom de la fonction JS et tout paramètre nécessaire à fournir à la fonction JS. Dans ce cas, nous ne passons aucun paramètre à la fonction JS.

Ouvrez **JSDemo.cshtml** et mettez le code suivant :

```cs
@page "/demo"
@using BlazorJSDemo.Pages

@inherits JSDemoModel  

<h1>Démonstration de JavaScript Interop</h1>

<hr />

<button class="btn btn-primary" onclick="@CallJSMethod">Appeler la méthode JS</button>

<br />
<p id="demop"></p>
```

Ici, nous avons défini la route de la page en haut. Donc, dans cette application, si nous ajoutons "demo" à l'URL de base, nous serons redirigés vers cette page. Nous héritons également de la classe **JSDemoModel**, qui est définie dans le fichier **JSDemo.cshtml.cs**. Cela nous permettra d'utiliser les méthodes définies dans la classe **JSDemoModel**.

Après cela, nous avons défini un bouton. Ce bouton invoquera la méthode "CallJSMethod" lorsqu'il sera cliqué. L'élément <p> avec l'id "demop" est également défini, et sa valeur sera définie par la fonction JS "JSMethod".

### Appel d'une méthode C#/.NET depuis JavaScript

Maintenant, nous allons définir notre méthode JS dans le fichier **wwwroot/index.html**, qui appellera notre méthode C# dans le fichier **JSDemo.cshtml.cs**.

La syntaxe pour appeler une méthode C# depuis JavaScript est la suivante :

```cs
DotNet.invokeMethodAsync('Nom de l'assembly de la méthode C#', 'Nom de la méthode C#');
```

Par conséquent, nous allons suivre la même syntaxe d'appel de méthode. Ouvrez le fichier **wwwroot/index.html** et ajoutez la section de script suivante :

```cs
<script>
  function CSMethod() {
    DotNet.invokeMethodAsync('BlazorJSDemo', 'CSCallBackMethod');
  }
</script>
```

Ici, nous définissons une fonction JS "CSMethod". Cette fonction aura un rappel vers notre méthode C# "CSCallBackMethod" qui est définie dans la classe **JSDemoModel**.

Pour invoquer une méthode C#/.NET depuis JavaScript, la méthode .NET cible doit répondre aux critères suivants :

1. La méthode doit être statique.
2. Elle doit être non générique.
3. La méthode ne doit pas avoir de surcharges.
4. Elle doit avoir des types de paramètres JSON sérialisables concrets.
5. Elle doit être décorée avec l'attribut [JSInvokable].

Ouvrez le fichier **JSDemo.cshtml.cs** et ajoutez le code suivant à l'intérieur de la classe **JSDemoModel**.

```cs
protected static string message { get; set; }

[JSInvokable]
public static void CSCallBackMethod()
{
  message = "Méthode C# invoquée";
}

protected void CallCSMethod()
{
  JSRuntime.Current.InvokeAsync<bool>("CSMethod");
}
```

Ici, nous avons défini deux méthodes :

1. **CallCSMethod** : Cela appellera notre fonction JS "CSMethod"
2. **CSCallBackMethod** : Il s'agit d'une méthode statique et elle sera invoquée depuis la fonction JavaScript "CSMethod". Par conséquent, elle est décorée avec l'attribut [JSInvokable]. Cette méthode définira la valeur d'une variable de chaîne **message**, qui sera affichée sur l'interface utilisateur.

Ouvrez le fichier **JSDemo.cshtml** et ajoutez le code suivant :

```html
<button class="btn btn-primary" onclick="@CallCSMethod">Appeler la méthode C#</button>
<br />
<p>@message</p>
```

Ici, nous avons défini un bouton qui appellera la méthode "CallCSMethod" lors de l'événement "onclick". La valeur de la variable message est définie lors du clic sur le bouton.

### Ajout d'un lien au menu de navigation

Ouvrez la page **\BlazorJSDemo\Shared\NavMenu.cshtml** et mettez le code suivant. Cela inclura un lien vers notre page **JSDemo.cshtml** dans le menu de navigation.

```html
<div class="top-row pl-4 navbar navbar-dark">
    <a class="navbar-brand" href="">BlazorJSDemo</a>
    <button class="navbar-toggler" onclick=@ToggleNavMenu>
        <span class="navbar-toggler-icon"></span>
    </button>
</div>

<div class=@(collapseNavMenu ? "collapse" : null) onclick=@ToggleNavMenu>
    <ul class="nav flex-column">
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="" Match=NavLinkMatch.All>
                <span class="oi oi-home" aria-hidden="true"></span> Accueil
            </NavLink>
        </li>
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="counter">
                <span class="oi oi-plus" aria-hidden="true"></span> Compteur
            </NavLink>
        </li>
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="fetchdata">
                <span class="oi oi-list-rich" aria-hidden="true"></span> Récupérer les données
            </NavLink>
        </li>
         <li class="nav-item px-3">
            <NavLink class="nav-link" href="demo">
                <span class="oi oi-list-rich" aria-hidden="true"></span> Démo JS
            </NavLink>
        </li>
    </ul>
</div>

@functions {
    bool collapseNavMenu = true;

    void ToggleNavMenu()
    {
        collapseNavMenu = !collapseNavMenu;
    }
}
```

### Démonstration d'exécution

Accédez à Affichage >> Terminal intégré pour ouvrir la fenêtre du terminal.

Tapez la commande **dotnet run** pour démarrer l'application. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/qPRwkQvalkfUx3ITH-tg6aG3TBMNscnWerVB)

Vous pouvez observer que l'application écoute sur [_http://localhost:5000._](http://localhost:5000.) Ouvrez un navigateur sur votre machine et accédez à cette URL. Vous pouvez voir la page d'accueil de l'application. Cliquez sur le lien "Démo JS" dans le menu de navigation pour ouvrir la vue **JSdemo**. Remarquez que l'URL a "demo" ajouté à la fin.

Cliquez sur les boutons pour invoquer les fonctions JS et la méthode C#.

Voir le GIF ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/J1P95jKUa8BulGL6f1qvan-kmMqn6XorEnaH)

### Conclusion

Dans cet article, nous avons appris à propos de JavaScript Interop. Nous avons également créé une application d'exemple pour démontrer comment JavaScript Interop fonctionne avec le framework Blazor.

Veuillez obtenir le code source depuis [Github](https://github.com/AnkitSharma-007/Blazor-JSInterop) et jouez avec pour obtenir une meilleure compréhension.

Obtenez mon livre [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) pour en apprendre davantage sur Blazor.

Vous pouvez consulter mes autres articles sur ASP .NET Core [ici](http://ankitsharmablogs.com/category/asp-net-core/).

### Voir aussi

* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [Creating a SPA Using Razor Pages With Blazor](http://ankitsharmablogs.com/creating-a-spa-using-razor-pages-with-blazor/)
* [Cascading DropDownList In Blazor Using EF Core](http://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/)
* [Deploying A Blazor Application On IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)

Publié à l'origine sur [ankitsharmablogs.com](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)