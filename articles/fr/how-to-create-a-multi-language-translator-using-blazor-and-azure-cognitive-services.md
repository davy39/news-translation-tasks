---
title: Comment créer un traducteur multilingue en utilisant Blazor et Azure Cognitive
  Services
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-09T14:14:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-multi-language-translator-using-blazor-and-azure-cognitive-services
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c3b740569d1a4ca30de.jpg
tags:
- name: Aspnetcore
  slug: aspnetcore
- name: Azure
  slug: azure
- name: Blazor
  slug: blazor
- name: translation
  slug: translation
seo_title: Comment créer un traducteur multilingue en utilisant Blazor et Azure Cognitive
  Services
seo_desc: "By Ankit Sharma\nIntroduction\nIn this article, we will create a multilanguage\
  \ translator using Blazor and the Translate Text Azure Cognitive Service. \nThis\
  \ translator will be able to translate between all the languages supported by the\
  \ Translate Text ..."
---

Par Ankit Sharma

## Introduction

Dans cet article, nous allons créer un traducteur multilingue en utilisant Blazor et le service Azure Cognitive Service Translate Text. 

Ce traducteur sera capable de traduire entre toutes les langues prises en charge par l'API Translate Text. Actuellement, l'API Translate Text prend en charge plus de 60 langues pour la traduction. 

L'application acceptera le texte à traduire et la langue cible comme entrée et retournera le texte traduit et la langue détectée pour le texte d'entrée comme sortie.

Jetez un œil à la sortie montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorTranslator.gif)

## Prérequis

* Installer le dernier SDK .NET Core 3.1 depuis [https://dotnet.microsoft.com/download/dotnet-core/3.1](https://dotnet.microsoft.com/download/dotnet-core/3.1)
* Installer la dernière version de Visual Studio 2019 depuis [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)
* Un compte d'abonnement Azure. Vous pouvez créer un compte Azure gratuit à l'adresse [https://azure.microsoft.com/en-in/free/](https://azure.microsoft.com/en-in/free/)

## Code source

Vous pouvez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services).

## Créer la ressource Azure Translator Text Cognitive Services

Connectez-vous au portail Azure et recherchez les services cognitifs dans la barre de recherche, puis cliquez sur le résultat. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/CreateTextCogServ-1.png)

Sur l'écran suivant, cliquez sur le bouton `Ajouter`. Cela ouvrira la page du marketplace des services cognitifs. Recherchez `Translator Text` dans la barre de recherche et cliquez sur le résultat de la recherche. Cela ouvrira la page de l'API Translator Text. Cliquez sur le bouton `Créer` pour créer une nouvelle ressource Translator Text. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/SelectTranslatorTextCogServ.png)

Sur la page `Créer`, remplissez les détails comme indiqué ci-dessous.

* Nom : Donnez un nom unique à votre ressource.
* Abonnement : Sélectionnez le type d'abonnement dans la liste déroulante.
* Niveau tarifaire : Sélectionnez le niveau tarifaire selon votre choix.
* Groupe de ressources : Sélectionnez un groupe de ressources existant ou créez-en un nouveau.

Cliquez sur le bouton `Créer`. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/ConfigureTranslatorTextCogServ.png)

Une fois votre ressource déployée avec succès, cliquez sur le bouton « Aller à la ressource ». Vous pouvez voir la clé et le point de terminaison pour la nouvelle ressource Translator Text créée. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/TextCogServKey.png)

Notez la clé, car nous l'utiliserons dans la suite de cet article pour demander les traductions à l'API Translator Text. Les valeurs sont masquées ici pour des raisons de confidentialité.

## Créer une application Blazor côté serveur

Ouvrez Visual Studio 2019 et cliquez sur « Créer un nouveau projet ». Sélectionnez « Application Blazor » et cliquez sur le bouton « Suivant ». Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/CreateProject-1.png)

Dans la fenêtre suivante, mettez le nom du projet comme `BlazorTranslator` et cliquez sur le bouton « Créer ». La fenêtre suivante vous demandera de sélectionner le type d'application Blazor. Sélectionnez `Application Blazor Server` et cliquez sur le bouton Créer pour créer une nouvelle application Blazor côté serveur. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorTemplate-1.png)

## Création des modèles

Faites un clic droit sur le projet `BlazorTranslator` et sélectionnez Ajouter >> Nouveau dossier. Nommez le dossier Models. Ensuite, faites un clic droit sur le dossier Models et sélectionnez Ajouter >> Classe pour ajouter un nouveau fichier de classe. Mettez le nom de votre classe comme `LanguageDetails.cs` et cliquez sur Ajouter.

Ouvrez `[LanguageDetails.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/LanguageDetails.cs)` et mettez le code suivant à l'intérieur.

```c#
namespace BlazorTranslator.Models
{
    public class LanguageDetails
    {
        public string Name { get; set; }
        public string NativeName { get; set; }
        public string Dir { get; set; }
    }
}
```

De même, ajoutez un nouveau fichier de classe `[TextResult.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/TextResult.cs)` et mettez le code suivant à l'intérieur.

```c#
using System;
namespace BlazorTranslator.Models
{
    public class TextResult
    {
        public string Text { get; set; }
        public string Script { get; set; }
    }
}
```

Ajoutez un nouveau fichier de classe `[Translation.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/Translation.cs)` et mettez le code suivant à l'intérieur.

```c#
namespace BlazorTranslator.Models
{
    public class Translation
    {
        public string Text { get; set; }
        public TextResult Transliteration { get; set; }
        public string To { get; set; }
    }
}
```

Créez un fichier de classe `[DetectedLanguage.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/DetectedLanguage.cs)` et mettez le code suivant à l'intérieur.

```c#
namespace BlazorTranslator.Models
{
    public class DetectedLanguage
    {
        public string Language { get; set; }
        public float Score { get; set; }
    }
}
```

Créez un fichier de classe `[TranslationResult.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/TranslationResult.cs)` et mettez le code suivant à l'intérieur.

```c#
namespace BlazorTranslator.Models
{
    public class TranslationResult
    {
        public DetectedLanguage DetectedLanguage { get; set; }
        public TextResult SourceText { get; set; }
        public Translation[] Translations { get; set; }
    }
}
```

Enfin, créez le fichier de classe `[AvailableLanguage.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/AvailableLanguage.cs)` et mettez le code suivant à l'intérieur.

```c#
using System.Collections.Generic;

namespace BlazorTranslator.Models
{
    public class AvailableLanguage
    {
      public Dictionary<string, LanguageDetails> Translation { get; set; }
    }
}
```

## Créer le service de traduction

Faites un clic droit sur le dossier `BlazorTranslator/Data` et sélectionnez Ajouter >> Classe pour ajouter un nouveau fichier de classe. Mettez le nom du fichier comme `TranslationService.cs` et cliquez sur Ajouter. Ouvrez le fichier `[TranslationService.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Data/TranslationService.cs)` et mettez le code suivant à l'intérieur.

```c#
using BlazorTranslator.Models;
using Newtonsoft.Json;
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace BlazorTranslator.Data
{
    public class TranslationService
    {
        public async Task<TranslationResult[]> GetTranslatation(string textToTranslate, string targetLanguage)
        {
            string subscriptionKey = "af19d996a3cb4a70a808567aad5bc41a";
            string apiEndpoint = "https://api.cognitive.microsofttranslator.com/";
            string route = $"/translate?api-version=3.0&to={targetLanguage}";
            string requestUri = apiEndpoint + route;
            TranslationResult[] translationResult = await TranslateText(subscriptionKey, requestUri, textToTranslate);
            return translationResult;
        }

        async Task<TranslationResult[]> TranslateText(string subscriptionKey, string requestUri, string inputText)
        {
            object[] body = new object[] { new { Text = inputText } };
            var requestBody = JsonConvert.SerializeObject(body);

            using (var client = new HttpClient())
            using (var request = new HttpRequestMessage())
            {
                request.Method = HttpMethod.Post;
                request.RequestUri = new Uri(requestUri);
                request.Content = new StringContent(requestBody, Encoding.UTF8, "application/json");
                request.Headers.Add("Ocp-Apim-Subscription-Key", subscriptionKey);

                HttpResponseMessage response = await client.SendAsync(request).ConfigureAwait(false);
                string result = await response.Content.ReadAsStringAsync();
                TranslationResult[] deserializedOutput = JsonConvert.DeserializeObject<TranslationResult[]>(result);

                return deserializedOutput;
            }
        }

        public async Task<AvailableLanguage> GetAvailableLanguages()
        {
            string endpoint = "https://api.cognitive.microsofttranslator.com/languages?api-version=3.0&scope=translation";
            var client = new HttpClient();
            using (var request = new HttpRequestMessage())
            {
                request.Method = HttpMethod.Get;
                request.RequestUri = new Uri(endpoint);
                var response = await client.SendAsync(request).ConfigureAwait(false);
                string result = await response.Content.ReadAsStringAsync();

                AvailableLanguage deserializedOutput = JsonConvert.DeserializeObject<AvailableLanguage>(result);

                return deserializedOutput;
            }
        }
    }
}
```

Nous avons défini une méthode `GetTranslatation` qui acceptera deux paramètres - le texte à traduire et la langue cible. Nous allons définir la clé d'abonnement pour le service cognitif Azure Translator Text et définir une variable pour le point de terminaison global pour Translator Text. L'URL de la requête contient le point de terminaison de l'API ainsi que la langue cible.

À l'intérieur de la méthode `TranslateText`, nous allons créer un nouveau `HttpRequestMessage`. Cette requête HTTP est une requête Post. Nous allons passer la clé d'abonnement dans l'en-tête de la requête. L'API Translator Text retourne un objet JSON, qui sera désérialisé en un tableau de type `TranslationResult`. La sortie contient le texte traduit ainsi que la langue détectée pour le texte d'entrée.

La méthode `GetAvailableLanguages` retournera la liste de toutes les langues prises en charge par l'API Translate Text. Nous allons définir l'URI de la requête et créer un `HttpRequestMessage` qui sera une requête Get. Cette URL de requête retournera un objet JSON qui sera désérialisé en un objet de type `AvailableLanguage`.

## Configuration du service

Pour rendre le service disponible pour les composants, nous devons le configurer dans l'application côté serveur. Ouvrez le fichier `Startup.cs`. Ajoutez la ligne suivante à l'intérieur de la méthode `[ConfigureServices](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Startup.cs#L28)` de la classe Startup.

```
services.AddSingleton<TranslationService>();
```

## Création du composant UI Blazor

Nous allons ajouter la page Razor dans le dossier `BlazorTranslator/Pages`. Par défaut, nous avons les pages « Counter » et « Fetch Data » fournies dans notre application. Ces pages par défaut n'affecteront pas notre application, mais pour les besoins de ce tutoriel, nous allons supprimer les pages fetchdata et counter du dossier `BlazorTranslator/Pages`.

Faites un clic droit sur le dossier `BlazorTranslator/Pages`, puis sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira, sélectionnez « Visual C# » dans le panneau de gauche, puis sélectionnez « Composant Razor » dans le panneau des modèles, mettez le nom comme `Translator.razor`. Cliquez sur `Ajouter`. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/AddRazorComp-1.png)

Ouvrez le fichier `[Translator.razor](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Pages/Translator.razor)` et ajoutez le code suivant en haut.

```
@page "/translator"
@using BlazorTranslator.Models
@using BlazorTranslator.Data
@inject TranslationService translationService
```

Nous avons défini la route pour ce composant. Nous injectons également le `TranslationService` dans ce composant.

Maintenant, nous allons ajouter le code HTML suivant dans ce fichier.

```html
<h3>Traducteur multilingue utilisant le service cognitif Microsoft Translator API</h3>
<hr />

<div class="container">
    <div class="row">
        <div class="col-md-6">
            <select class="form-control" @bind="inputLanguage">
                <option value="">-- Sélectionner la langue d'entrée --</option>
                @foreach (KeyValuePair<string, LanguageDetails> lang in LanguageList)
                {
                    <option value="@lang.Key">@lang.Value.Name</option>
                }
            </select>
            <textarea placeholder="Entrez le texte à traduire" class="form-control translation-box" rows="5" @bind="@inputText"></textarea>
        </div>
        <div class="col-md-6">
            <select class="form-control" @onchange="SelectLanguage">
                <option value="">-- Sélectionner la langue cible --</option>
                @foreach (KeyValuePair<string, LanguageDetails> lang in LanguageList)
                {
                    <option value="@lang.Key">@lang.Value.Name</option>
                }
            </select>
            <textarea disabled class="form-control translation-box" rows="5">@outputText</textarea>
        </div>
    </div>
    <div class="text-center">
        <button class="btn btn-primary btn-lg" @onclick="Translate">Traduire</button>
    </div>
</div>
```

Nous avons défini deux listes déroulantes, une pour la langue d'entrée et une pour la langue cible. L'API Azure Translate Text détectera la langue d'entrée et nous utiliserons cette valeur pour remplir la liste déroulante de la langue d'entrée. Nous avons également défini deux zones de texte pour le texte d'entrée et le texte traduit.

Enfin, ajoutez le code suivant dans la section `@code` de la page.

```c#
@code {
    private TranslationResult[] translations;
    private AvailableLanguage availableLanguages;

    private string outputLanguage { get; set; }
    private string inputLanguage { get; set; }

    string inputText { get; set; }
    string outputText { get; set; }

    private Dictionary<string, LanguageDetails> LanguageList = new Dictionary<string, LanguageDetails>();

    protected override async Task OnInitializedAsync()
    {
        availableLanguages = await translationService.GetAvailableLanguages();
        LanguageList = availableLanguages.Translation;
    }

    private void SelectLanguage(ChangeEventArgs langEvent)
    {
        this.outputLanguage = langEvent.Value.ToString();
    }

    private async Task Translate()
    {
        if (!string.IsNullOrEmpty(outputLanguage))
        {
            translations = await translationService.GetTranslatation(this.inputText, this.outputLanguage);
            outputText = translations[0].Translations[0].Text;
            inputLanguage = translations[0].DetectedLanguage.Language;
        }
    }
}
```

Nous appelons la méthode `GetAvailableLanguages` de notre service à l'intérieur de `OnInitializedAsync`. Cette méthode `OnInitializedAsync` est une méthode de cycle de vie qui sera appelée lors de l'initialisation du composant. Cela garantira que la liste déroulante des langues sera remplie lors du chargement de la page.

La méthode `SelectLanguage` définira la `outputLanguage` pour la traduction. La méthode Translate appellera la méthode `GetTranslatation` du service. Nous définirons le `outputText` et la langue détectée pour le `inputLanguage` comme retourné par le service.

## Ajouter le style pour le composant Translator

Accédez au fichier `[BlazorTranslator\wwwroot\css\site.css](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/wwwroot/css/site.css#L185-L187)` et mettez la définition de style suivante à l'intérieur.

```css
.translation-box {
    margin: 15px 0px;
}

```

## Ajout du lien au menu de navigation

La dernière étape consiste à ajouter le lien de notre composant Translator dans le menu de navigation. Ouvrez le fichier `[BlazorTranslator/Shared/NavMenu.razor](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Shared/NavMenu.razor#L15-L19)` et ajoutez le code suivant à l'intérieur.

```html
<li class="nav-item px-3">
	<NavLink class="nav-link" href="translator">
		<span class="oi oi-list-rich" aria-hidden="true"></span> Traducteur
	</NavLink>
</li>
```

Supprimez les liens de navigation pour les composants Counter et Fetch-data car ils ne sont pas nécessaires pour cette application.

## Démonstration d'exécution

Appuyez sur F5 pour lancer l'application. Cliquez sur le bouton Traducteur dans le menu de navigation à gauche. Vous pouvez effectuer la traduction multilingue comme montré dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorTranslator-1.gif)

## Résumé

Nous avons créé une ressource Translator Text Cognitive Services sur Azure. Nous avons utilisé l'API Translator Text pour créer un traducteur multilingue en utilisant Blazor. Ce traducteur prend en charge plus de 60 langues pour la traduction. Nous avons récupéré la liste des langues prises en charge pour la traduction depuis le point de terminaison global de l'API Translator Text.

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services) et jouez avec pour mieux comprendre.

## Voir aussi

* [Lecteur de caractères optiques utilisant Blazor et Computer Vision](https://ankitsharmablogs.com/optical-character-reader-using-blazor-and-computer-vision/)
* [Authentification et autorisation Facebook dans une application Blazor côté serveur](https://ankitsharmablogs.com/facebook-authentication-and-authorization-in-server-side-blazor-app/)
* [Authentification et autorisation Google dans une application Blazor côté serveur](https://ankitsharmablogs.com/google-authentication-and-authorization-in-server-side-blazor-app/)
* [CRUD Blazor utilisant Google Cloud Firestore](https://ankitsharmablogs.com/blazor-crud-using-google-cloud-firestore/)
* [Hébergement d'une application Blazor sur Firebase](https://ankitsharmablogs.com/hosting-a-blazor-application-on-firebase/)
* [Localisation dans Angular en utilisant les outils i18n](https://ankitsharmablogs.com/localization-in-angular-using-i18n-tools/)