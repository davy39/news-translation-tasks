---
title: How to Create a Multi-Language Translator Using Blazor and Azure Cognitive
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
seo_title: null
seo_desc: "By Ankit Sharma\nIntroduction\nIn this article, we will create a multilanguage\
  \ translator using Blazor and the Translate Text Azure Cognitive Service. \nThis\
  \ translator will be able to translate between all the languages supported by the\
  \ Translate Text ..."
---

By Ankit Sharma

## Introduction

In this article, we will create a multilanguage translator using Blazor and the Translate Text Azure Cognitive Service. 

This translator will be able to translate between all the languages supported by the Translate Text API. Currently, the Translate Text API supports more than 60 languages for translation. 

The application will accept the text to translate and the target language as the input and returns the translated text and the detected language for the input text as the output.

Take a look at the output shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorTranslator.gif)

## Prerequisites

* Install the latest .NET Core 3.1 SDK from [https://dotnet.microsoft.com/download/dotnet-core/3.1](https://dotnet.microsoft.com/download/dotnet-core/3.1)
* Install the latest version of Visual Studio 2019 from [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)
* An Azure subscription account. You can create a free Azure account at [https://azure.microsoft.com/en-in/free/](https://azure.microsoft.com/en-in/free/)

## Source Code

You can get the source code from [GitHub](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services).

## Create the Azure Translator Text Cognitive Services resource

Log in to the Azure portal and search for the cognitive services in the search bar and click on the result. Refer to the image shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/CreateTextCogServ-1.png)

On the next screen, click on the `Add` button. It will open the cognitive services marketplace page. Search for the `Translator Text` in the search bar and click on the search result. It will open the Translator Text API page. Click on the `Create` button to create a new Translator Text resource. Refer to the image shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/SelectTranslatorTextCogServ.png)

On the `Create` page, fill in the details as indicated below.

* Name: Give a unique name for your resource.
* Subscription: Select the subscription type from the dropdown.
* Pricing tier: Select the pricing tier as per your choice.
* Resource group: Select an existing resource group or create a new one.

Click on the `Create` button. Refer to the image shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/ConfigureTranslatorTextCogServ.png)

After your resource is successfully deployed, click on the “Go to resource” button. You can see the Key and the endpoint for the newly created Translator Text resource. Refer to the image shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/TextCogServKey.png)

Make a note of the key, as we will be using this in the latter part of this article to request the translations from the Translator Text API. The values are masked here for privacy.

## Create a Server-Side Blazor Application

Open Visual Studio 2019 and click on “Create a new project”. Select “Blazor App” and click on the “Next” button. Refer to the image shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/CreateProject-1.png)

On the next window, put the project name as `BlazorTranslator` and click on the “Create” button. The next window will ask you to select the type of Blazor app. Select `Blazor Server App` and click on the Create button to create a new server-side Blazor application. Refer to the image shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorTemplate-1.png)

## Creating the Models

Right-click on `BlazorTranslator` project and select Add >> New Folder. Name the folder as Models. Again, right-click on the Models folder and select Add >> Class to add a new class file. Put the name of your class as `LanguageDetails.cs` and click Add.

Open `[LanguageDetails.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/LanguageDetails.cs)` and put the following code inside it.

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

Similarly, add a new class file `[TextResult.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/TextResult.cs)` and put the following code inside it.

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

Add a new class file `[Translation.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/Translation.cs)` and put the following code inside it.

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

Create a class file `[DetectedLanguage.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/DetectedLanguage.cs)` and put the following code inside it.

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

Create a class file `[TranslationResult.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/TranslationResult.cs)` and put the following code inside it.

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

Finally, create the class file `[AvailableLanguage.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Models/AvailableLanguage.cs)` and put the following code inside it.

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

## Create the Translation service

Right-click on the `BlazorTranslator/Data` folder and select Add >> Class to add a new class file. Put the name of the file as `TranslationService.cs` and click on Add. Open `[TranslationService.cs](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Data/TranslationService.cs)` file and put the following code inside it.

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

We have defined a `GetTranslatation` method which will accept two parameters – the text to translate and the target language. We will set the subscription key for the Azure Translator Text cognitive service and define a variable for the global endpoint for Translator Text. The request URL contains the API endpoint along with the target language.

Inside the `TranslateText` method, we will create a new `HttpRequestMessage`. This HTTP request is a Post request. We will pass the subscription key in the header of the request. The Translator Text API returns a JSON object, which will be deserialized to an array of type `TranslationResult`. The output contains the translated text as well as the language detected for the input text.

The `GetAvailableLanguages` method will return the list of all the language supported by the Translate Text API. We will set the request URI and create a `HttpRequestMessage` which will be a Get request. This request URL will return a JSON object which will be deserialized to an object of type `AvailableLanguage`.

## Configuring the Service

To make the service available to the components we need to configure it on the server-side app. Open the `Startup.cs` file. Add the following line inside the `[ConfigureServices](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Startup.cs#L28)` method of Startup class.

```
services.AddSingleton<TranslationService>();
```

## Creating the Blazor UI Component

We will add the Razor page in `BlazorTranslator/Pages` folder. By default, we have “Counter” and “Fetch Data” pages provided in our application. These default pages will not affect our application but for the sake of this tutorial, we will delete fetchdata and counter pages from `BlazorTranslator/Pages` folder.

Right-click on `BlazorTranslator/Pages` folder and then select Add >> New Item. An “Add New Item” dialog box will open, select “Visual C#” from the left panel, then select “Razor Component” from the templates panel, put the name as `Translator.razor`. Click `Add`. Refer to the image shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/AddRazorComp-1.png)

Open the `[Translator.razor](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Pages/Translator.razor)` file and add the following code at the top.

```
@page "/translator"
@using BlazorTranslator.Models
@using BlazorTranslator.Data
@inject TranslationService translationService
```

We have defined the route for this component. We are also injecting the `TranslationService` in this component.

Now we will add the following HTML code in this file.

```html
<h3>Multilanguage translator using Microsoft Translator API Cognitive Service</h3>
<hr />

<div class="container">
    <div class="row">
        <div class="col-md-6">
            <select class="form-control" @bind="inputLanguage">
                <option value="">-- Select input language --</option>
                @foreach (KeyValuePair<string, LanguageDetails> lang in LanguageList)
                {
                    <option value="@lang.Key">@lang.Value.Name</option>
                }
            </select>
            <textarea placeholder="Enter text to translate" class="form-control translation-box" rows="5" @bind="@inputText"></textarea>
        </div>
        <div class="col-md-6">
            <select class="form-control" @onchange="SelectLanguage">
                <option value="">-- Select target language --</option>
                @foreach (KeyValuePair<string, LanguageDetails> lang in LanguageList)
                {
                    <option value="@lang.Key">@lang.Value.Name</option>
                }
            </select>
            <textarea disabled class="form-control translation-box" rows="5">@outputText</textarea>
        </div>
    </div>
    <div class="text-center">
        <button class="btn btn-primary btn-lg" @onclick="Translate">Translate</button>
    </div>
</div>
```

We have defined two dropdown lists, one each for input language and the target language. The Azure Translate Text API will detect the input language and we will use that value to populate the dropdown for input language. We have also defined two text areas for the input and the translated text.

Finally, add the following code in the `@code` section of the page.

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

We are invoking the `GetAvailableLanguages` method from our service inside the `OnInitializedAsync`. This `OnInitializedAsync` is a lifecycle method that will be invoked upon component initialization. This will make sure that the language dropdown will be populated as the page loads.

The `SelectLanguage` method will set the `outputLanguage` for the translation. The Translate method will invoke the `GetTranslatation` method from the service. We will set the `outputText` and the language detected for the `inputLanguage` as returned from the service.

## Add styling for the Translator component

Navigate to `[BlazorTranslator\wwwroot\css\site.css](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/wwwroot/css/site.css#L185-L187)` file and put the following style definition inside it.

```css
.translation-box {
    margin: 15px 0px;
}

```

## Adding Link to Navigation menu

The last step is to add the link of our Translator component in the navigation menu. Open `[BlazorTranslator/Shared/NavMenu.razor](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services/blob/master/BlazorTranslator/Shared/NavMenu.razor#L15-L19)` file and add the following code into it.

```html
<li class="nav-item px-3">
	<NavLink class="nav-link" href="translator">
		<span class="oi oi-list-rich" aria-hidden="true"></span> Translator
	</NavLink>
</li>
```

Remove the navigation links for Counter and Fetch-data components as they are not required for this application.

## Execution Demo

Press F5 to launch the application. Click on the Translator button on the nav menu in the left. You can perform the multilanguage translation as shown in the image below.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorTranslator-1.gif)

## Summary

We have created a Translator Text Cognitive Services resource on Azure. We have used the Translator Text API to create a multilanguage translator using Blazor. This translator supports more than 60 languages for translation. We fetched the list of supported languages for translation from the global API endpoint for Translator Text.

Get the Source code from [GitHub](https://github.com/AnkitSharma-007/Blazor-Translator-Azure-Cognitive-Services) and play around to get a better understanding.

## See Also

* [Optical Character Reader Using Blazor And Computer Vision](https://ankitsharmablogs.com/optical-character-reader-using-blazor-and-computer-vision/)
* [Facebook Authentication And Authorization In Server-Side Blazor App](https://ankitsharmablogs.com/facebook-authentication-and-authorization-in-server-side-blazor-app/)
* [Google Authentication And Authorization In Server-Side Blazor App](https://ankitsharmablogs.com/google-authentication-and-authorization-in-server-side-blazor-app/)
* [Blazor CRUD Using Google Cloud Firestore](https://ankitsharmablogs.com/blazor-crud-using-google-cloud-firestore/)
* [Hosting A Blazor Application on Firebase](https://ankitsharmablogs.com/hosting-a-blazor-application-on-firebase/)
* [Localization In Angular Using i18n Tools](https://ankitsharmablogs.com/localization-in-angular-using-i18n-tools/)

