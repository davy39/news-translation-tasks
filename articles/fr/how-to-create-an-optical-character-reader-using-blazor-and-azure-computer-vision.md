---
title: Comment créer un lecteur de caractères optiques en utilisant Blazor et Azure
  Computer Vision
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-03T18:48:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-optical-character-reader-using-blazor-and-azure-computer-vision
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c4c740569d1a4ca3143.jpg
tags:
- name: Aspnetcore
  slug: aspnetcore
- name: Azure
  slug: azure
- name: Blazor
  slug: blazor
- name: Computer Vision
  slug: computer-vision
seo_title: Comment créer un lecteur de caractères optiques en utilisant Blazor et
  Azure Computer Vision
seo_desc: "By Ankit Sharma\nIntroduction\nIn this article, we will create an optical\
  \ character recognition (OCR) application using Blazor and the Azure Computer Vision\
  \ Cognitive Service. \nComputer Vision is an AI service that analyzes content in\
  \ images. We will u..."
---

Par Ankit Sharma

## Introduction

Dans cet article, nous allons créer une application de reconnaissance optique de caractères (OCR) en utilisant Blazor et le service cognitif Azure Computer Vision. 

Computer Vision est un service d'IA qui analyse le contenu des images. Nous allons utiliser la fonctionnalité OCR de Computer Vision pour détecter le texte imprimé dans une image. 

L'application extraira le texte de l'image et détectera la langue du texte. Actuellement, l'API OCR prend en charge 25 langues.

Une démonstration de l'application est montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorComputerVision-1.gif)

## Prérequis

* Installer le dernier SDK .NET Core 3.1 depuis [https://dotnet.microsoft.com/download/dotnet-core/3.1](https://dotnet.microsoft.com/download/dotnet-core/3.1)
* Installer la dernière version de Visual Studio 2019 depuis [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)
* Un compte d'abonnement Azure. Vous pouvez créer un compte Azure gratuit à [https://azure.microsoft.com/en-in/free/](https://azure.microsoft.com/en-in/free/)

## Exigences de l'image

L'API OCR fonctionnera sur les images qui répondent aux exigences mentionnées ci-dessous :

* Le format de l'image doit être JPEG, PNG, GIF ou BMP.
* La taille de l'image doit être comprise entre 50 x 50 et 4200 x 4200 pixels.
* La taille du fichier image doit être inférieure à 4 Mo.
* Le texte dans l'image peut être tourné par un multiple de 90 degrés plus un petit angle allant jusqu'à 40 degrés.

## Code source

Vous pouvez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services).

## Créer la ressource du service cognitif Azure Computer Vision

Connectez-vous au portail Azure et recherchez les services cognitifs dans la barre de recherche, puis cliquez sur le résultat. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/CreateTextCogServ.png)

Sur l'écran suivant, cliquez sur le bouton Ajouter. Cela ouvrira la page du marketplace des services cognitifs. 

Recherchez Computer Vision dans la barre de recherche et cliquez sur le résultat de la recherche. Cela ouvrira la page de l'API Computer Vision. Cliquez sur le bouton Créer pour créer une nouvelle ressource Computer Vision. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/SelectComputerVisionCogServ-1.png)

Sur la page Créer, remplissez les détails comme indiqué ci-dessous.

* **Nom** : Donnez un nom unique à votre ressource.
* **Abonnement** : Sélectionnez le type d'abonnement dans la liste déroulante.
* **Niveau tarifaire** : Sélectionnez le niveau tarifaire selon votre choix.
* **Groupe de ressources** : Sélectionnez un groupe de ressources existant ou créez-en un nouveau.

Cliquez sur le bouton Créer. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorConfigureComputerVisionCogServ.png)

Après que votre ressource soit déployée avec succès, cliquez sur le bouton « Aller à la ressource ». Vous pouvez voir la clé et le point de terminaison pour la nouvelle ressource Computer Vision créée. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/ComputerVisionCogServKey.png)

Prenez note de la clé et du point de terminaison. Nous les utiliserons dans la suite de cet article pour invoquer l'API OCR Computer Vision depuis le code .NET. Les valeurs sont masquées ici pour des raisons de confidentialité.

## Créer une application Blazor côté serveur

Ouvrez Visual Studio 2019, cliquez sur « Créer un nouveau projet ». Sélectionnez « Application Blazor » et cliquez sur le bouton « Suivant ». Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/CreateProject.png)

Dans la fenêtre suivante, mettez le nom du projet comme `BlazorComputerVision` et cliquez sur le bouton « Créer ». 

La fenêtre suivante vous demandera de sélectionner le type d'application Blazor. Sélectionnez `Blazor Server App` et cliquez sur le bouton Créer pour créer une nouvelle application Blazor côté serveur. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorTemplate.png)

## Installation de la bibliothèque de l'API Computer Vision

Nous allons installer la bibliothèque de l'API Azure Computer Vision qui nous fournira les modèles prêts à l'emploi pour gérer la réponse de l'API REST Computer Vision. 

Pour installer le package, accédez à Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages. Cela ouvrira la Console du gestionnaire de packages. Exécutez la commande comme montré ci-dessous.

```
Install-Package Microsoft.Azure.CognitiveServices.Vision.ComputerVision -Version 5.0.0
```

Vous pouvez en savoir plus sur ce package à la [galerie NuGet](https://www.nuget.org/packages/Microsoft.Azure.CognitiveServices.Vision.ComputerVision/).

## Créer les modèles

Faites un clic droit sur le projet `BlazorComputerVision` et sélectionnez Ajouter >> Nouveau dossier. Nommez le dossier `Models`. Ensuite, faites un clic droit sur le dossier `Models` et sélectionnez Ajouter >> Classe pour ajouter un nouveau fichier de classe. Donnez le nom de votre classe comme `LanguageDetails.cs` et cliquez sur Ajouter.

Ouvrez `[LanguageDetails.cs](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/Models/LanguageDetails.cs)` et mettez le code suivant à l'intérieur.

```c#
namespace BlazorComputerVision.Models
{
    public class LanguageDetails
    {
        public string Name { get; set; }
        public string NativeName { get; set; }
        public string Dir { get; set; }
    }
}
```

De même, ajoutez un nouveau fichier de classe `[AvailableLanguage.cs](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/Models/AvailableLanguage.cs)` et mettez le code suivant à l'intérieur.

```c#
using System.Collections.Generic;

namespace BlazorComputerVision.Models
{
    public class AvailableLanguage
    {
        public Dictionary<string, LanguageDetails> Translation { get; set; }
    }
}
```

Enfin, nous allons ajouter une classe en tant que DTO (Data Transfer Object) pour envoyer des données au client. Ajoutez un nouveau fichier de classe `[OcrResultDTO.cs](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/Models/OcrResultDTO.cs)` et mettez le code suivant à l'intérieur.

```c#
namespace BlazorComputerVision.Models
{
    public class OcrResultDTO
    {
        public string Language { get; set; }

        public string DetectedText { get; set; }
    }
}
```

## Créer le service Computer Vision

Faites un clic droit sur le dossier `BlazorComputerVision/Data` et sélectionnez Ajouter >> Classe pour ajouter un nouveau fichier de classe. Donnez le nom du fichier comme `ComputerVisionService.cs` et cliquez sur Ajouter.

Ouvrez le fichier `[ComputerVisionService.cs](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/Data/ComputerVisionService.cs)` et mettez le code suivant à l'intérieur.

```c#
using BlazorComputerVision.Models;
using Microsoft.Azure.CognitiveServices.Vision.ComputerVision.Models;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace BlazorComputerVision.Data
{
    public class ComputerVisionService
    {
        static string subscriptionKey;
        static string endpoint;
        static string uriBase;

        public ComputerVisionService()
        {
            subscriptionKey = "b993f3afb4e04119bd8ed37171d4ec71";
            endpoint = "https://ankitocrdemo.cognitiveservices.azure.com/";
            uriBase = endpoint + "vision/v2.1/ocr";
        }

        public async Task<OcrResultDTO> GetTextFromImage(byte[] imageFileBytes)
        {
            StringBuilder sb = new StringBuilder();
            OcrResultDTO ocrResultDTO = new OcrResultDTO();
            try
            {
                string JSONResult = await ReadTextFromStream(imageFileBytes);

                OcrResult ocrResult = JsonConvert.DeserializeObject<OcrResult>(JSONResult);

                if (!ocrResult.Language.Equals("unk"))
                {
                    foreach (OcrLine ocrLine in ocrResult.Regions[0].Lines)
                    {
                        foreach (OcrWord ocrWord in ocrLine.Words)
                        {
                            sb.Append(ocrWord.Text);
                            sb.Append(' ');
                        }
                        sb.AppendLine();
                    }
                }
                else
                {
                    sb.Append("Cette langue n'est pas prise en charge.");
                }
                ocrResultDTO.DetectedText = sb.ToString();
                ocrResultDTO.Language = ocrResult.Language;
                return ocrResultDTO;
            }
            catch
            {
                ocrResultDTO.DetectedText = "Une erreur s'est produite. Veuillez réessayer";
                ocrResultDTO.Language = "unk";
                return ocrResultDTO;
            }
        }

        static async Task<string> ReadTextFromStream(byte[] byteData)
        {
            try
            {
                HttpClient client = new HttpClient();
                client.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
                string requestParameters = "language=unk&detectOrientation=true";
                string uri = uriBase + "?" + requestParameters;
                HttpResponseMessage response;

                using (ByteArrayContent content = new ByteArrayContent(byteData))
                {
                    content.Headers.ContentType = new MediaTypeHeaderValue("application/octet-stream");
                    response = await client.PostAsync(uri, content);
                }

                string contentString = await response.Content.ReadAsStringAsync();
                string result = JToken.Parse(contentString).ToString();
                return result;
            }
            catch (Exception e)
            {
                return e.Message;
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

Dans le constructeur de la classe, nous avons initialisé la clé et l'URL du point de terminaison pour l'API OCR.

À l'intérieur de la méthode `ReadTextFromStream`, nous allons créer un nouveau `HttpRequestMessage`. Cette requête HTTP est une requête Post. Nous allons passer la clé d'abonnement dans l'en-tête de la requête. L'API OCR retournera un objet JSON contenant chaque mot de l'image ainsi que la langue détectée du texte.

La méthode `GetTextFromImage` acceptera les données de l'image sous forme de tableau d'octets et retournera un objet de type `OcrResultDTO`. Nous allons invoquer la méthode `ReadTextFromStream` et désérialiser la réponse dans un objet de type `OcrResult`. Nous allons ensuite former la phrase en itérant sur l'objet `OcrWord`.

La méthode `GetAvailableLanguages` retournera la liste de toutes les langues prises en charge par l'API Translate Text. Nous allons définir l'URI de la requête et créer un `HttpRequestMessage` qui sera une requête Get. Cette URL de requête retournera un objet JSON qui sera désérialisé en un objet de type `AvailableLanguage`.

## Pourquoi devons-nous récupérer la liste des langues prises en charge ?

L'API OCR retourne le code de la langue (par exemple, en pour l'anglais, de pour l'allemand, etc.) de la langue détectée. Mais nous ne pouvons pas afficher le code de la langue sur l'interface utilisateur car il n'est pas convivial. Par conséquent, nous avons besoin d'un dictionnaire pour rechercher le nom de la langue correspondant au code de la langue.

L'API OCR Azure Computer Vision prend en charge 25 langues. Pour connaître toutes les langues prises en charge par l'API OCR, voir la liste des [langues prises en charge](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/language-support). 

Ces langues sont un sous-ensemble des langues prises en charge par l'API Azure Translate Text. Puisqu'il n'existe pas de point de terminaison d'API dédié pour récupérer la liste des langues prises en charge par l'API OCR, nous utilisons donc le point de terminaison de l'API Translate Text pour récupérer la liste des langues. 

Nous allons créer le dictionnaire de recherche de langue en utilisant la réponse JSON de cet appel d'API et filtrer le résultat en fonction du code de langue retourné par l'API OCR.

## Installer le package NuGet BlazorInputFile

[BlazorInputFile](https://www.nuget.org/packages/BlazorInputFile/) est un composant d'entrée de fichier pour les applications Blazor. Il permet de télécharger un ou plusieurs fichiers vers une application Blazor.

Ouvrez le fichier `[BlazorComputerVision.csproj](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/BlazorComputerVision.csproj#L8)` et ajoutez une dépendance pour le package `BlazorInputFile` comme montré ci-dessous :

```xhtml
<ItemGroup>
    <PackageReference Include="BlazorInputFile" Version="0.1.0-preview-00002" />
</ItemGroup>
```

Ouvrez le fichier `[BlazorComputerVision\Pages\_Host.cshtml](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/Pages/_Host.cshtml#L17)` et ajoutez la référence pour le fichier JavaScript du package en ajoutant la ligne suivante dans la section `<head>`.

```js
<script src="_content/BlazorInputFile/inputfile.js"></script>
```

Ajoutez la ligne suivante dans le fichier `[_Imports.razor](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/_Imports.razor#L10)`.

```
@using BlazorInputFile
```

## **Configuration du service**

Pour rendre le service disponible pour les composants, nous devons le configurer dans l'application côté serveur. Ouvrez le fichier Startup.cs. Ajoutez la ligne suivante à l'intérieur de la méthode `[ConfigureServices](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/Startup.cs#L31)` de la classe Startup.

```c#
 services.AddSingleton<ComputerVisionService>();
```

## Création du composant d'interface utilisateur Blazor

Nous allons ajouter la page Razor dans le dossier `BlazorComputerVision/Pages`. Par défaut, nous avons les pages « Counter » et « Fetch Data » fournies dans notre application. Ces pages par défaut n'affecteront pas notre application, mais pour simplifier ce tutoriel, nous allons supprimer les pages fetchdata et counter du dossier `BlazorComputerVision/Pages`.

Faites un clic droit sur le dossier `BlazorComputerVision/Pages`, puis sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira, sélectionnez « Visual C# » dans le panneau de gauche, puis sélectionnez « Composant Razor » dans le panneau des modèles, donnez le nom `OCR.razor`. Cliquez sur Ajouter. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorOCRComponent.png)

Nous allons ajouter un fichier de code-behind pour cette page Razor afin de séparer le code et la présentation. Cela permettra une maintenance facile de l'application. 

Faites un clic droit sur le dossier `BlazorComputerVision/Pages`, puis sélectionnez Ajouter >> Classe. Nommez la classe `OCR.razor.cs`. Le framework Blazor est suffisamment intelligent pour associer ce fichier de classe au fichier Razor. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/BlazorCodeBehind.png)

## Code-behind du composant d'interface utilisateur Blazor

Ouvrez le fichier `[OCR.razor.cs](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/Pages/OCR.razor.cs)` et mettez le code suivant à l'intérieur.

```c#
using Microsoft.AspNetCore.Components;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.IO;
using BlazorComputerVision.Models;
using BlazorInputFile;
using BlazorComputerVision.Data;

namespace BlazorComputerVision.Pages
{
    public class OCRModel : ComponentBase
    {
        [Inject]
        protected ComputerVisionService computerVisionService { get; set; }

        protected string DetectedTextLanguage;
        protected string imagePreview;
        protected bool loading = false;
        byte[] imageFileBytes;

        const string DefaultStatus = "La taille maximale autorisée pour l'image est de 4 Mo";
        protected string status = DefaultStatus;

        protected OcrResultDTO Result = new OcrResultDTO();
        private AvailableLanguage availableLanguages;
        private Dictionary<string, LanguageDetails> LanguageList = new Dictionary<string, LanguageDetails>();
        const int MaxFileSize = 4 * 1024 * 1024; // 4MB

        protected override async Task OnInitializedAsync()
        {
            availableLanguages = await computerVisionService.GetAvailableLanguages();
            LanguageList = availableLanguages.Translation;
        }

        protected async Task ViewImage(IFileListEntry[] files)
        {
            var file = files.FirstOrDefault();
            if (file == null)
            {
                return;
            }
            else if (file.Size > MaxFileSize)
            {
                status = $"La taille du fichier est de {file.Size} octets, ce qui est plus que la limite autorisée de {MaxFileSize} octets.";
                return;
            }
            else if (!file.Type.Contains("image"))
            {
                status = "Veuillez télécharger un fichier image valide";
                return;
            }
            else
            {
                var memoryStream = new MemoryStream();
                await file.Data.CopyToAsync(memoryStream);
                imageFileBytes = memoryStream.ToArray();
                string base64String = Convert.ToBase64String(imageFileBytes, 0, imageFileBytes.Length);

                imagePreview = string.Concat("data:image/png;base64,", base64String);
                memoryStream.Flush();
                status = DefaultStatus;
            }
        }

        protected private async Task GetText()
        {
            if (imageFileBytes != null)
            {
                loading = true;
                Result = await computerVisionService.GetTextFromImage(imageFileBytes);
                if (LanguageList.ContainsKey(Result.Language))
                {
                    DetectedTextLanguage = LanguageList[Result.Language].Name;
                }
                else
                {
                    DetectedTextLanguage = "Inconnu";
                }
                loading = false;
            }
        }
    }
}
```

Nous injectons le `ComputerVisionService` dans cette classe.

La méthode `OnInitializedAsync` est une méthode de cycle de vie de Blazor qui est invoquée lorsque le composant est initialisé. Nous invoquons la méthode `GetAvailableLanguages` de notre service à l'intérieur de la méthode `OnInitializedAsync`. Nous allons ensuite initialiser la variable LanguageList qui est un dictionnaire pour contenir les détails des langues disponibles.

À l'intérieur de la méthode `ViewImage`, nous allons vérifier si le fichier téléchargé est une image uniquement et si la taille est inférieure à 4 Mo. Nous allons transférer l'image téléchargée vers le flux de mémoire. Nous allons ensuite convertir ce flux de mémoire en un tableau d'octets. 

Pour définir l'aperçu de l'image, nous allons convertir l'image du tableau d'octets en une chaîne encodée en base64. La méthode `GetText` invoquera la méthode `GetTextFromImage` du service et passera le tableau d'octets de l'image comme argument. Nous allons rechercher le nom de la langue dans le dictionnaire en fonction du code de langue retourné par le service. Si aucun code de langue n'est disponible, nous définirons la langue comme inconnue.

## Modèle de composant d'interface utilisateur Blazor

Ouvrez le fichier `[OCR.razor](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/Pages/OCR.razor)` et mettez le code suivant à l'intérieur.

```html
@page "/computer-vision-ocr"
@inherits OCRModel

<h2>Reconnaissance optique de caractères (OCR) en utilisant Blazor et le service cognitif Azure Computer Vision</h2>

<div class="row">
    <div class="col-md-5">
        <textarea disabled class="form-control" rows="10" cols="15">@Result.DetectedText</textarea>
        <hr />
        <div class="row">
            <div class="col-sm-5">
                <label><strong> Langue détectée :</strong></label>
            </div>
            <div class="col-sm-6">
                <input disabled type="text" class="form-control" value="@DetectedTextLanguage" />
            </div>
        </div>
    </div>
    <div class="col-md-5">
        <div class="image-container">
            <img class="preview-image" src=@imagePreview>
        </div>
        <InputFile OnChange="ViewImage" />
        <p>@status</p>
        <hr />
        <button disabled="@loading" class="btn btn-primary btn-lg" @onclick="GetText">
            @if (loading)
            {
                <span class="spinner-border spinner-border-sm mr-1"></span>
            }
            Extraire le texte
        </button>
    </div>
</div>
```

Nous avons défini la route pour ce composant. Nous avons hérité de la classe `OCRModel` qui nous permet d'accéder aux propriétés et méthodes de cette classe depuis le modèle. Bootstrap est utilisé pour concevoir l'interface utilisateur. Nous avons une zone de texte pour afficher le texte détecté et une boîte de texte pour afficher la langue détectée. La balise image est utilisée pour montrer l'aperçu de l'image après avoir téléchargé l'image. Le composant `<InputFile>` nous permettra de télécharger un fichier image et d'invoquer la méthode `ViewImage` lorsque nous téléchargeons l'image.

## Ajouter le style pour le composant

Accédez au fichier `[BlazorComputerVision\wwwroot\css\site.css](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/wwwroot/css/site.css#L185-L197)` et ajoutez la définition de style suivante à l'intérieur.

```css
.preview-image {
    max-height: 300px;
    max-width: 300px;
}
.image-container {
    display: flex;
    padding: 15px;
    align-content: center;
    align-items: center;
    justify-content: center;
    border: 2px dashed skyblue;
}
```

## **Ajout du lien au menu de navigation**

La dernière étape consiste à ajouter le lien de notre composant OCR dans le menu de navigation. Ouvrez le fichier `[BlazorComputerVision/Shared/NavMenu.razor](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services/blob/master/BlazorComputerVision/Shared/NavMenu.razor#L15-L19)` et ajoutez le code suivant à l'intérieur.

```html
<li class="nav-item px-3">
	<NavLink class="nav-link" href="computer-vision-ocr">
		<span class="oi oi-list-rich" aria-hidden="true"></span> Computer Vision
	</NavLink>
</li>
```

Supprimez les liens de navigation pour les composants Counter et Fetch-data car ils ne sont pas nécessaires pour cette application.

## Démonstration d'exécution

Appuyez sur F5 pour lancer l'application. Cliquez sur le bouton Computer Vision dans le menu de navigation à gauche. Sur la page suivante, téléchargez une image avec du texte et cliquez sur le bouton « Extraire le texte ». Vous verrez le texte extrait dans la zone de texte à gauche ainsi que la langue détectée pour le texte. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Execution_English.png)

Maintenant, nous allons essayer de télécharger une image avec du texte en français, vous pouvez voir le texte extrait et la langue détectée comme étant le français. Reportez-vous à l'image montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Execution_French.png)

Si nous essayons de télécharger une image avec une langue non prise en charge, nous obtiendrons une erreur. Reportez-vous à l'image montrée ci-dessous où une image avec du texte écrit en hindi est téléchargée.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Execution_Hindi.png)

## **Résumé**

Nous avons créé une application de reconnaissance optique de caractères (OCR) en utilisant Blazor et le service cognitif Azure Computer Vision. Nous avons ajouté la fonctionnalité de téléchargement d'un fichier image en utilisant le composant `BlazorInputFile`. L'application est capable d'extraire le texte imprimé de l'image téléchargée et de reconnaître la langue du texte. L'API OCR de Computer Vision est utilisée, qui peut reconnaître le texte dans 25 langues.

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-Computer-Vision-Azure-Cognitive-Services) et jouez avec pour obtenir une meilleure compréhension.

## Voir aussi

* [Traduction multilingue en utilisant Blazor et les services cognitifs Azure](https://ankitsharmablogs.com/multi-language-translator-using-blazor-and-azure-cognitive-services/)
* [Authentification et autorisation Facebook dans une application Blazor côté serveur](https://ankitsharmablogs.com/facebook-authentication-and-authorization-in-server-side-blazor-app/)
* [Authentification et autorisation Google dans une application Blazor côté serveur](https://ankitsharmablogs.com/google-authentication-and-authorization-in-server-side-blazor-app/)
* [Autorisation basée sur les politiques dans Angular en utilisant JWT](https://ankitsharmablogs.com/policy-based-authorization-in-angular-using-jwt/)
* [Déploiement continu pour une application Angular en utilisant Heroku et GitHub](https://ankitsharmablogs.com/continuous-deployment-for-angular-app-using-heroku-and-github/)
* [Hébergement d'une application Blazor sur Firebase](https://ankitsharmablogs.com/hosting-a-blazor-application-on-firebase/)
* [Déploiement d'une application Blazor sur Azure](https://ankitsharmablogs.com/deploying-a-blazor-application-on-azure/)