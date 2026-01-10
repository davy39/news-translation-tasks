---
title: Comment héberger une application Blazor sur Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T22:10:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-host-a-blazor-application-on-firebase-67c4ee956a22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dhtbZon7OPebZuUO9-yyjw.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Blazor
  slug: blazor
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment héberger une application Blazor sur Firebase
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will learn how to deploy a Blazor application on Firebase. We
  will create a basic calculator app using Blazor and host it on Firebase. This application
  will not have any server-side code or web API log...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons apprendre comment déployer une application Blazor sur Firebase. Nous allons créer une application de calculatrice basique en utilisant Blazor et l'héberger sur Firebase. Cette application n'aura aucun code côté serveur ou logique d'API web. Nous allons utiliser Visual Studio 2017 pour construire et publier l'application. Nous allons utiliser la CLI pour déployer l'application sur Firebase.

### Prérequis

Vous devez installer les prérequis suivants pour créer une application Blazor.

* Installer le SDK .NET Core 2.1 ou supérieur depuis [ici](https://www.microsoft.com/net/learn/get-started-with-dotnet-tutorial#windowscmd)
* Installer la dernière version de Visual Studio 2017 depuis [ici](https://www.visualstudio.com/downloads/)
* Installer l'extension ASP.NET Core Blazor Language Services depuis [ici](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)

### Création d'une application Blazor

Nous allons créer une application de calculatrice basique pour cette démonstration. Puisque c'est une calculatrice basique, elle prendra deux opérandes et supportera quatre fonctions arithmétiques — addition, soustraction, multiplication et division.

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet. Après avoir sélectionné le projet, une boîte de dialogue « Nouveau Projet » s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche. Sélectionnez ensuite « Application Web ASP.NET Core » parmi les types de projets disponibles. Donnez le nom du projet comme « SampleCalculator » et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/HuinX8HUzvMpywjRLq-bk-6cvRBxJEDEAniC)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez observer deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez « .NET Core » et « ASP.NET Core 2.1 » dans ces menus déroulants. Ensuite, sélectionnez le modèle « Blazor » et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/xZ-fGQWc75D0gQ3UGMipKHlDFuDZv0Q02m93)

Cela créera votre application Blazor. Nous allons maintenant créer notre composant de calculatrice.

### Création du composant Calculatrice

Pour cette application, nous allons utiliser la structure de composant à page unique. La logique et l'interface utilisateur seront dans le même fichier.

Pour créer notre composant, faites un clic droit sur le dossier `SampleCalculator/Pages` puis sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue Ajouter un nouvel élément s'ouvrira, vous demandant de sélectionner le modèle d'élément souhaité dans la liste fournie. Sélectionnez ASP.NET Core dans le panneau de gauche, puis sélectionnez Vue Razor dans le panneau des modèles. Donnez le nom du fichier comme `Calculator.cshtml` et cliquez sur Ajouter.

Voir la capture d'écran suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/IOK1Vg6Pr1FX2dXJfCkmNSKtsCFQ2r7FWRTo)

Ouvrez le fichier `Calculator.cshtml` et placez le code suivant à l'intérieur :

```
@page "/calculator"
<h1>Calculatrice Basique Utilisant Blazor</h1>
<hr />
<div>
    <div class="row">
        <div class="col-sm-3">
            <label class="control-label">Premier Nombre</label>
        </div>
        <div class="col-sm-4">
            <input class="form-control" type="text" placeholder="Entrez le Premier Nombre" bind="@operand1" />
        </div>
    </div>
    <br />
    <div class="row">
        <div class="col-sm-3">
            <label class="control-label">Deuxième Nombre</label>
        </div>
        <div class="col-sm-4">
            <input class="form-control" type="text" placeholder="Entrez le Deuxième Nombre" bind="@operand2" />
        </div>
    </div>
    <br />
    <div class="row">
        <div class="col-sm-3">
            <label class="control-label">Résultat</label>
        </div>
        <div class="col-sm-4">
            <input readonly class="form-control" bind="@finalResult" />
        </div>
    </div>
    <br />
    <div class="row">
        <div class="col-md-3">
            <button onclick="@AddNumbers" class="btn btn-primary">
                Ajouter
                (+)
            </button>
        </div>
        <div class="col-md-3">
            <button onclick="@SubtractNumbers" class="btn btn-warning">Soustraire (─)</button>
        </div>
        <div class="col-md-3">
            <button onclick="@MultiplyNumbers" class="btn btn-success">Multiplier (X)</button>
        </div>
        <div class="col-md-3">
            <button onclick="@DivideNumbers" class="btn btn-info">Diviser (/)</button>
        </div>
    </div>
</div>

@functions {
    double operand1 { get; set; }
    double operand2 { get; set; }
    string finalResult { get; set; }

    void AddNumbers() {
        finalResult = (operand1 + operand2).ToString();
    }

    void SubtractNumbers() {
        finalResult = (operand1 - operand2).ToString();
    }

    void MultiplyNumbers() {
        finalResult = (operand1 * operand2).ToString();
    }

    void DivideNumbers() {
        if (operand2 != 0) {
            finalResult = (operand1 / operand2).ToString();
        } else {
            finalResult = "Impossible de diviser par zéro";
        }
    }
}
```

Dans la partie HTML du code, nous avons défini deux zones de texte pour lire les opérandes saisis par l'utilisateur. Nous avons une zone de texte pour afficher le résultat des opérations arithmétiques. Nous avons également défini quatre boutons, un pour chaque opération arithmétique. L'événement onclick des boutons appellera les méthodes qui fourniront le résultat. Une fois l'opération correspondante effectuée sur les deux opérandes.

Dans la section @functions, nous avons défini deux propriétés pour lier les valeurs d'entrée de l'utilisateur, et une autre propriété pour afficher le résultat du calcul. Pour gérer nos opérations arithmétiques, nous avons défini quatre méthodes qui effectueront les opérations souhaitées sur les opérandes et définiront la valeur de finalResult qui sera ensuite liée au champ Résultat sur l'interface utilisateur.

Ajoutez le lien de navigation pour ce composant dans le fichier `Shared/NavMenu.cshtml`. Appuyez sur F5 pour exécuter l'application et vous pouvez voir l'écran de sortie comme montré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/bKgUV3hORWxMnSk2UnoIEukeUIMiWcRJMYir)

Cette application est encore dans un environnement de développement. Avant de l'héberger sur Firebase, nous devons la publier.

### Publication de l'application Blazor

Faites un clic droit sur le projet et cliquez sur publier. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/ZjihqY84OTyVvaJzaqyVe5ey42SyGeE8j1iT)

Vous verrez un écran similaire à celui ci-dessous. Sélectionnez Dossier dans le menu de gauche et fournissez un chemin de dossier. Vous pouvez fournir n'importe quel chemin de dossier où vous souhaitez publier votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/aXzPfCQwg7P7ju9Pv8nwP9h2M4m-1VdGuokg)

Cliquez sur publier. Visual Studio commencera à publier votre application. Si il n'y a pas d'erreurs de construction, votre application sera publiée avec succès dans le dossier que vous avez mentionné.

Après la publication réussie, nous allons procéder à l'hébergement de cette application sur Firebase.

### Ajout du projet sur Firebase

La première étape pour héberger une application sur Firebase est d'ajouter un nouveau projet sur la console Firebase.

Accédez à [https://console.firebase.google.com](https://console.firebase.google.com/) et connectez-vous avec votre compte Google. Cliquez sur le lien `Ajouter un projet`. Une fenêtre pop-up s'ouvrira comme montré dans l'image ci-dessous. Fournissez le nom de votre projet et cliquez sur le bouton `Créer un projet` en bas.

![Image](https://cdn-media-1.freecodecamp.org/images/e88YyTpLOYUyMPWNlt7BRm9D9SGKJQ1pE1zz)

Notez l'identifiant du projet ici. Les identifiants de projet Firebase sont globalement uniques. Vous pouvez modifier l'identifiant de votre projet lors de la création d'un nouveau projet. Une fois le projet créé, vous ne pouvez pas changer l'identifiant de votre projet. Nous utiliserons cet identifiant de projet dans la section suivante lors de l'initialisation de notre application.

### Déploiement avec Firebase

Ouvrez le dossier où vous avez publié votre application Blazor. Ici, vous pouvez voir un dossier « SampleCalculator » et un fichier web.config. À l'intérieur de « SampleCalculator », nous aurons un autre dossier nommé « dist ». Nous allons publier le contenu de ce dossier « dist ».

Ouvrez une fenêtre d'invite de commande/PowerShell à l'intérieur du dossier « SampleCalculator ». Suivez maintenant les étapes mentionnées ci-dessous :

**Étape 1** : Connexion avec Firebase

Exécutez la commande suivante :

```
firebase login
```

Cela ouvrira une fenêtre de navigateur et vous demandera de vous connecter à Firebase. Connectez-vous avec votre compte Google. Après une connexion réussie, revenez à votre CLI.

**Étape 2** : Initialisation de votre application

Exécutez la commande suivante :

```
firebase init
```

Cette commande initialisera un projet firebase. Vous serez invité à répondre à une série de questions. Répondez-y comme indiqué ci-dessous :

* Êtes-vous prêt à continuer ? — Appuyez sur Y
* Quelles fonctionnalités de l'interface de ligne de commande Firebase souhaitez-vous configurer pour ce dossier ? — Sélectionnez Hébergement
* Sélectionnez un projet Firebase par défaut pour ce répertoire : — Si le projet que vous avez ajouté dans la dernière section apparaît dans la liste, sélectionnez-le, sinon sélectionnez « ne pas configurer de projet par défaut ».
* Que souhaitez-vous utiliser comme répertoire public ? — dist
* Configurer comme une application à page unique (réécrire toutes les URL vers /index.html) ? — y
* Le fichier dist/index.html existe déjà. Écraser ? — N

Vous recevrez un message « Initialisation de Firebase terminée ! ».

**Étape 3** : Ajout d'un projet par défaut

Si vous avez déjà sélectionné un projet par défaut à l'étape 2, vous pouvez ignorer cette étape.

Si vous n'avez pas sélectionné de projet par défaut, vous devez l'ajouter manuellement ici. Exécutez la commande suivante :

```
firebase use --add yourProjectId
```

Dans ce cas, ce sera :

```
firebase use --add blazorcalc
```

Vous recevrez un message de succès comme « Utilisation du projet blazorcalc ».

**Étape 4** : Déploiement sur Firebase

Enfin, exécutez la commande suivante pour déployer votre application sur Firebase.

```
firebase deploy
```

Cette commande déployera votre application Blazor sur Firebase et, en cas de succès, elle vous fournira une URL d'hébergement.

Toutes les étapes mentionnées ci-dessus sont montrées dans le GIF ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/8LWcAiWcrmbuU2TeTFCkUG2yEpQSR0LxJxzR)

### Démonstration d'exécution

Ouvrez l'URL d'hébergement. Vous pouvez voir l'application dans votre navigateur comme montré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Yc-a1ikqx961hS2NN8u9WAnXmQt0ojPO0Id1)

### Extension de l'article

Nous pouvons suivre les mêmes étapes pour héberger une application Angular sur Firebase.

Exécutez la commande suivante pour construire une application Angular pour la production.

```
ng build --prod
```

Cela créera le dossier « dist » dans le dossier racine de votre application. Une fois que vous avez le dossier « dist », suivez les mêmes étapes que mentionnées ci-dessus.

### Conclusion

Nous avons appris comment créer une application de calculatrice échantillon en utilisant Blazor. Nous avons également appris comment déployer cette application sur Firebase.

Vous pouvez trouver le code de cette application de calculatrice échantillon sur [Github](https://github.com/AnkitSharma-007/ASPCore.BlazorDemo).

Obtenez mon livre [Blazor Quick Start Guide](https://amzn.to/2OToEji) pour en apprendre davantage sur Blazor.

Préparation aux entretiens ? Lisez mon article sur [C# Coding Questions For Technical Interviews](https://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/)

### Voir aussi

* [BlazorGrid — Un composant de grille réutilisable pour Blazor](https://ankitsharmablogs.com/blazorgrid-reusable-grid-component-for-blazor/)
* [Publier un composant Blazor sur la galerie Nuget](https://ankitsharmablogs.com/publishing-blazor-component-to-nuget-gallery/)
* [Déployer une application Blazor sur IIS](https://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)
* [Déployer une application Blazor sur Azure](https://ankitsharmablogs.com/deploying-a-blazor-application-on-azure/)
* [CRUD avec Blazor et MongoDB](https://ankitsharmablogs.com/crud-using-blazor-with-mongodb/)
* [Application à page unique utilisant Blazor côté serveur](https://ankitsharmablogs.com/single-page-application-using-server-side-blazor/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)