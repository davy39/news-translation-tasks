---
title: Comment créer un lecteur de caractères optiques en utilisant Angular et Azure
  Computer Vision
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-15T19:03:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-optical-character-reader-using-angular-and-azure-computer-vision
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aff740569d1a4ca2913.jpg
tags:
- name: AI
  slug: ai
- name: Angular
  slug: angular
- name: Azure
  slug: azure
- name: 'OCR '
  slug: ocr
seo_title: Comment créer un lecteur de caractères optiques en utilisant Angular et
  Azure Computer Vision
seo_desc: "By Ankit Sharma\nIntroduction\nIn this article, we will create an optical\
  \ character recognition (OCR) application using Angular and the Azure Computer Vision\
  \ Cognitive Service. \nComputer Vision is an AI service that analyzes content in\
  \ images. We will ..."
---

Par Ankit Sharma

## Introduction

Dans cet article, nous allons créer une application de reconnaissance optique de caractères (OCR) en utilisant Angular et le service cognitif Azure Computer Vision. 

Computer Vision est un service d'IA qui analyse le contenu des images. Nous allons utiliser la fonctionnalité OCR de Computer Vision pour détecter le texte imprimé dans une image. L'application extraira le texte de l'image et détectera la langue du texte. 

Actuellement, l'API OCR prend en charge 25 langues.

## Prérequis

* Installer la dernière version LTS de Node.JS depuis [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
* Installer l'interface de ligne de commande Angular depuis [https://cli.angular.io/](https://cli.angular.io/)
* Installer le SDK .NET Core 3.1 depuis [https://dotnet.microsoft.com/download/dotnet-core/3.1](https://dotnet.microsoft.com/download/dotnet-core/3.1)
* Installer la dernière version de Visual Studio 2019 depuis [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)
* Un compte d'abonnement Azure. Vous pouvez créer un compte Azure gratuit à l'adresse [https://azure.microsoft.com/en-in/free/](https://azure.microsoft.com/en-in/free/)

## Code source

Vous pouvez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services).

> Nous utiliserons un backend ASP.NET Core pour cette application. Le backend ASP.NET Core fournit un processus d'authentification direct pour accéder aux services cognitifs Azure. Cela garantira également que l'utilisateur final n'aura pas d'accès direct aux services cognitifs.

## Créer la ressource du service cognitif Azure Computer Vision

Connectez-vous au portail Azure et recherchez les services cognitifs dans la barre de recherche, puis cliquez sur le résultat. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/CreateCVCogServ.png)

Sur l'écran suivant, cliquez sur le bouton Ajouter. Cela ouvrira la page du marketplace des services cognitifs. Recherchez Computer Vision dans la barre de recherche et cliquez sur le résultat de la recherche. Cela ouvrira la page de l'API Computer Vision. Cliquez sur le bouton Créer pour créer une nouvelle ressource Computer Vision. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/SelectComputerVisionCogServ.png)

Sur la page Créer, remplissez les détails comme indiqué ci-dessous.

* **Nom** : Donnez un nom unique à votre ressource.
* **Abonnement** : Sélectionnez le type d'abonnement dans la liste déroulante.
* **Niveau tarifaire** : Sélectionnez le niveau tarifaire selon votre choix.
* **Groupe de ressources** : Sélectionnez un groupe de ressources existant ou créez-en un nouveau.

Cliquez sur le bouton Créer. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/ConfigureComputerVisionCogServ.png)

Une fois votre ressource déployée avec succès, cliquez sur le bouton "Aller à la ressource". Vous pouvez voir la clé et le point de terminaison pour la nouvelle ressource Computer Vision créée. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/ComputerVisionCogServKey-1.png)

Prenez note de la clé et du point de terminaison. Nous les utiliserons dans la suite de cet article pour invoquer l'API OCR Computer Vision depuis le code .NET. Les valeurs sont masquées ici pour des raisons de confidentialité.

## Création de l'application ASP.NET Core

Ouvrez Visual Studio 2019 et cliquez sur "Créer un nouveau projet". Une boîte de dialogue "Créer un nouveau projet" s'ouvrira. Sélectionnez "Application Web ASP.NET Core" et cliquez sur Suivant. Vous serez alors sur l'écran "Configurer votre nouveau projet", donnez le nom de votre application comme `ngComputerVision` et cliquez sur créer. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/CreateProject_1.png)

Vous serez redirigé vers l'écran "Créer une nouvelle application web ASP.NET Core". Sélectionnez ".NET Core" et "ASP.NET Core 3.1" dans les listes déroulantes en haut. Ensuite, sélectionnez le modèle de projet "Angular" et cliquez sur `Créer`. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/CreateProject_2.png)

Cela créera notre projet. La structure des dossiers de l'application est montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Sol_Exp-1.png)

Le dossier `ClientApp` contient le code Angular de notre application. Le dossier Controllers contiendra nos contrôleurs d'API. Les composants Angular sont présents dans le dossier `ClientApp\src\app`. 

Le modèle par défaut contient quelques composants Angular. Ces composants n'affecteront pas notre application, mais pour des raisons de simplicité, nous allons supprimer les dossiers fetchdata et counter du dossier `ClientApp/app/components`. Supprimez également la référence à ces deux composants dans le fichier `app.module.ts`.

## Installation de la bibliothèque de l'API Computer Vision

Nous allons installer la bibliothèque de l'API Azure Computer Vision qui nous fournira les modèles prêts à l'emploi pour gérer la réponse de l'API REST Computer Vision. Pour installer le package, naviguez vers Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages. Cela ouvrira la Console du gestionnaire de packages. Exécutez la commande comme indiqué ci-dessous.

```
Install-Package Microsoft.Azure.CognitiveServices.Vision.ComputerVision -Version 5.0.0
```

Vous pouvez en savoir plus sur ce package sur la [galerie NuGet](https://www.nuget.org/packages/Microsoft.Azure.CognitiveServices.Vision.ComputerVision/).

## Créer les Modèles

Faites un clic droit sur le projet `ngComputerVision` et sélectionnez Ajouter >> Nouveau Dossier. Nommez le dossier Models. Ensuite, faites un clic droit sur le dossier Models et sélectionnez Ajouter >> Classe pour ajouter un nouveau fichier de classe. Donnez le nom de votre classe comme `LanguageDetails.cs` et cliquez sur Ajouter.

Ouvrez [LanguageDetails.cs](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/Models/LanguageDetails.cs) et mettez le code suivant à l'intérieur.

```csharp
namespace ngComputerVision.Models
{
    public class LanguageDetails
    {
        public string Name { get; set; }
        public string NativeName { get; set; }
        public string Dir { get; set; }
    }
}
```

De même, ajoutez un nouveau fichier de classe [AvailableLanguage.cs](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/Models/AvailableLanguage.cs) et mettez le code suivant à l'intérieur.

```csharp
using System.Collections.Generic;

namespace ngComputerVision.Models
{
    public class AvailableLanguage
    {
        public Dictionary<string, LanguageDetails> Translation { get; set; }
    }
}
```

Nous allons également ajouter deux classes en tant que DTO (Data Transfer Object) pour envoyer des données au client.

Créez un nouveau dossier et nommez-le DTOModels. Ajoutez le nouveau fichier de classe [AvailableLanguageDTO.cs](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/DTOModels/AvailableLanguageDTO.cs) dans le dossier DTOModels et mettez le code suivant à l'intérieur.

```csharp
namespace ngComputerVision.DTOModels
{
    public class AvailableLanguageDTO
    {
        public string LanguageID { get; set; }
        public string LanguageName { get; set; }
    }
}
```

Ajoutez le fichier [OcrResultDTO.cs](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/DTOModels/OcrResultDTO.cs) et mettez le code suivant à l'intérieur.

```csharp
namespace ngComputerVision.DTOModels
{
    public class OcrResultDTO
    {
        public string Language { get; set; }
        public string DetectedText { get; set; }
    }
}
```

## Ajout du contrôleur OCR

Nous allons ajouter un nouveau contrôleur à notre application. Faites un clic droit sur le dossier Controllers et sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue "Ajouter un nouvel élément" s'ouvrira. Sélectionnez "Visual C#" dans le panneau de gauche, puis sélectionnez "Classe de contrôleur d'API" dans le panneau des modèles et donnez le nom `OCRController.cs`. Cliquez sur Ajouter. 

Reportons-nous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/AddController-1.png)

Le `OCRController` gérera les demandes de reconnaissance d'image de l'application cliente. Ce contrôleur retournera également la liste de toutes les langues prises en charge par l'API OCR.

Ouvrez le fichier [OCRController.cs](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/Controllers/OCRController.cs) et mettez le code suivant à l'intérieur.

```csharp
using System;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Net.Http.Headers;
using Newtonsoft.Json.Linq;
using System.IO;
using Newtonsoft.Json;
using System.Text;
using ngComputerVision.Models;
using System.Collections.Generic;
using Microsoft.Azure.CognitiveServices.Vision.ComputerVision.Models;
using ngComputerVision.DTOModels;

namespace ngComputerVision.Controllers
{
    [Produces("application/json")]
    [Route("api/[controller]")]
    public class OCRController : Controller
    {
        static string subscriptionKey;
        static string endpoint;
        static string uriBase;

        public OCRController()
        {
            subscriptionKey = "b993f3afb4e04119bd8ed37171d4ec71";
            endpoint = "https://ankitocrdemo.cognitiveservices.azure.com/";
            uriBase = endpoint + "vision/v2.1/ocr";
        }

        [HttpPost, DisableRequestSizeLimit]
        public async Task<OcrResultDTO> Post()
        {
            StringBuilder sb = new StringBuilder();
            OcrResultDTO ocrResultDTO = new OcrResultDTO();
            try
            {
                if (Request.Form.Files.Count > 0)
                {
                    var file = Request.Form.Files[Request.Form.Files.Count - 1];

                    if (file.Length > 0)
                    {
                        var memoryStream = new MemoryStream();
                        file.CopyTo(memoryStream);
                        byte[] imageFileBytes = memoryStream.ToArray();
                        memoryStream.Flush();

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
                    }
                }
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

        [HttpGet]
        public async Task<List<AvailableLanguageDTO>> GetAvailableLanguages()
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

                List<AvailableLanguageDTO> availableLanguage = new List<AvailableLanguageDTO>();

                foreach (KeyValuePair<string, LanguageDetails> translation in deserializedOutput.Translation)
                {
                    AvailableLanguageDTO language = new AvailableLanguageDTO();
                    language.LanguageID = translation.Key;
                    language.LanguageName = translation.Value.Name;

                    availableLanguage.Add(language);
                }
                return availableLanguage;
            }
        }
    }
}

```

Dans le constructeur de la classe, nous avons initialisé la clé et l'URL du point de terminaison pour l'API OCR.

La méthode Post recevra les données de l'image sous forme de collection de fichiers dans le corps de la requête et retournera un objet de type `OcrResultDTO`. Nous allons convertir les données de l'image en un tableau d'octets et invoquer la méthode `ReadTextFromStream`. Nous allons désérialiser la réponse en un objet de type `OcrResult`. Nous allons ensuite former la phrase en itérant sur l'objet `OcrWord`.

À l'intérieur de la méthode `ReadTextFromStream`, nous allons créer un nouveau `HttpRequestMessage`. Cette requête HTTP est une requête Post. Nous allons passer la clé d'abonnement dans l'en-tête de la requête. L'API OCR retournera un objet JSON contenant chaque mot de l'image ainsi que la langue détectée du texte.

La méthode `GetAvailableLanguages` retournera la liste de toutes les langues prises en charge par l'API Translate Text. Nous allons définir l'URI de la requête et créer un `HttpRequestMessage` qui sera une requête Get. Cet URI de requête retournera un objet JSON qui sera désérialisé en un objet de type `AvailableLanguage`.

### **Pourquoi devons-nous récupérer la liste des langues prises en charge ?**

L'API OCR retourne le code de la langue (par exemple, en pour l'anglais, de pour l'allemand, etc.) de la langue détectée. Mais nous ne pouvons pas afficher le code de la langue sur l'interface utilisateur car il n'est pas convivial. Par conséquent, nous avons besoin d'un dictionnaire pour rechercher le nom de la langue correspondant au code de la langue.

L'API OCR Azure Computer Vision prend en charge 25 langues. Pour connaître toutes les langues prises en charge par l'API OCR, consultez la liste des [langues prises en charge](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/language-support). Ces langues sont un sous-ensemble des langues prises en charge par l'API Azure Translate Text. 

Puisqu'il n'existe pas de point de terminaison d'API dédié pour récupérer la liste des langues prises en charge par l'API OCR, nous utilisons le point de terminaison de l'API Translate Text pour récupérer la liste des langues. Nous allons créer le dictionnaire de recherche de langue en utilisant la réponse JSON de cet appel d'API et filtrer le résultat en fonction du code de langue retourné par l'API OCR.

## Travailler sur le côté client de l'application

Le code pour le côté client est disponible dans le dossier ClientApp. Nous allons utiliser Angular CLI pour travailler avec le code client.

> L'utilisation d'Angular CLI n'est pas obligatoire. J'utilise Angular CLI ici car il est convivial et facile à utiliser. Si vous ne souhaitez pas utiliser CLI, vous pouvez créer les fichiers pour les composants et les services manuellement.

Accédez au dossier ngComputerVision\ClientApp sur votre machine et ouvrez une fenêtre de commande. Nous allons exécuter toutes nos commandes Angular CLI dans cette fenêtre.

## Créer les modèles côté client

Créez un dossier appelé models à l'intérieur du dossier `ClientApp\src\app`. Maintenant, nous allons créer un fichier [availablelanguage.ts](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/ClientApp/src/app/models/availablelanguage.ts) dans le dossier models. Mettez le code suivant à l'intérieur.

```typescript
export class AvailableLanguage {
    languageID: string;
    languageName: string;
}
```

De même, créez un autre fichier à l'intérieur du dossier models appelé [ocrresult.ts](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/ClientApp/src/app/models/ocrresult.ts). Mettez le code suivant à l'intérieur.

```typescript
export class OcrResult {
    language: string;
    detectedText: string
}
```

Vous pouvez observer que ces deux classes ont la même définition que les classes DTO que nous avons créées côté serveur. Cela nous permettra de lier les données retournées par le serveur directement à nos modèles.

## Créer le service Computervision

Nous allons créer un service Angular qui invoquera les points de terminaison de l'API Web, convertira la réponse de l'API Web en JSON et la transmettra à notre composant. Exécutez la commande suivante.

```
ng g s services\Computervision
```

Cette commande créera un dossier nommé services et créera ensuite les deux fichiers suivants à l'intérieur.

* computervision.service.ts

 le fichier de classe de service.
* computervision.service.spec.ts

 le fichier de test unitaire pour le service.

Ouvrez le fichier [computervision.service.ts](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/ClientApp/src/app/services/computervision.service.ts) et mettez le code suivant à l'intérieur.

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ComputervisionService {

  baseURL: string;

  constructor(private http: HttpClient) {
    this.baseURL = '/api/OCR';
  }

  getAvailableLanguage() {
    return this.http.get(this.baseURL)
      .pipe(response => {
        return response;
      });
  }

  getTextFromImage(image: FormData) {
    return this.http.post(this.baseURL, image)
      .pipe(response => {
        return response;
      });
  }
}

```

Nous avons défini une variable baseURL qui contiendra l'URL du point de terminaison de notre API. Nous allons initialiser baseURL dans le constructeur et le définir sur le point de terminaison du `OCRController`.

La méthode `getAvailableLanguage` enverra une requête Get à la méthode `GetAvailableLanguages` du `OCRController` pour récupérer la liste des langues prises en charge par OCR.

La méthode `getTextFromImage` enverra une requête Post au `OCRController` et fournira le paramètre de type `FormData`. Elle récupérera le texte détecté dans l'image et le code de langue du texte.

### **Créer le composant Ocr**

Exécutez la commande suivante dans l'invite de commande pour créer le `OcrComponent`.

```
ng g c ocr --module app
```

Le drapeau `--module` garantira que ce composant sera enregistré dans `app.module.ts`.

Ouvrez [ocr.component.html](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/ClientApp/src/app/ocr/ocr.component.html) et mettez le code suivant à l'intérieur.

```html
<h2>Reconnaissance optique de caractères (OCR) en utilisant Angular et les services cognitifs Azure Computer Vision</h2>

<div class="row">
  <div class="col-md-5">
    <textarea disabled class="form-control" rows="10" cols="15">{{ocrResult?.detectedText}}</textarea>
    <hr />
    <div class="row">
      <div class="col-sm-5">
        <label><strong> Langue détectée :</strong></label>
      </div>
      <div class="col-sm-6">
        <input disabled type="text" class="form-control" value={{DetectedTextLanguage}} />
      </div>
    </div>
  </div>
  <div class="col-md-5">
    <div class="image-container">
      <img class="preview-image" src={{imagePreview}}>
    </div>
    <input type="file" (change)="uploadImage($event)" />
    <p>{{status}}</p>
    <hr />
    <button [disabled]="loading" class="btn btn-primary btn-lg" (click)="GetText()">
      <span *ngIf="loading" class="spinner-border spinner-border-sm mr-1"></span>Extraire le texte
    </button>
  </div>
</div>

```

Nous avons défini une zone de texte pour afficher le texte détecté et une zone de texte pour afficher la langue détectée. Nous avons défini un contrôle de téléchargement de fichier qui nous permettra de télécharger une image. Après avoir téléchargé l'image, l'aperçu de l'image sera affiché à l'aide d'un élément `<img>`.

Ouvrez [ocr.component.ts](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/ClientApp/src/app/ocr/ocr.component.ts) et mettez le code suivant à l'intérieur.

```typescript
import { Component, OnInit } from '@angular/core';
import { ComputervisionService } from '../services/computervision.service';
import { AvailableLanguage } from '../models/availablelanguage';
import { OcrResult } from '../models/ocrresult';

@Component({
  selector: 'app-ocr',
  templateUrl: './ocr.component.html',
  styleUrls: ['./ocr.component.css']
})
export class OcrComponent implements OnInit {

  loading = false;
  imageFile;
  imagePreview;
  imageData = new FormData();
  availableLanguage: AvailableLanguage[];
  DetectedTextLanguage: string;
  ocrResult: OcrResult;
  DefaultStatus: string;
  status: string;
  maxFileSize: number;
  isValidFile = true;

  constructor(private computervisionService: ComputervisionService) {
    this.DefaultStatus = "La taille maximale autorisée pour l'image est de 4 Mo";
    this.status = this.DefaultStatus;
    this.maxFileSize = 4 * 1024 * 1024; // 4MB
  }

  ngOnInit() {
    this.computervisionService.getAvailableLanguage().subscribe(
      (result: AvailableLanguage[]) => this.availableLanguage = result
    );
  }

  uploadImage(event) {
    this.imageFile = event.target.files[0];
    if (this.imageFile.size > this.maxFileSize) {
      this.status = `La taille du fichier est de ${this.imageFile.size} octets, ce qui dépasse la limite autorisée de ${this.maxFileSize} octets.`;
      this.isValidFile = false;
    } else if (this.imageFile.type.indexOf('image') == -1) {
      this.status = "Veuillez télécharger un fichier image valide";
      this.isValidFile = false;
    } else {
      const reader = new FileReader();
      reader.readAsDataURL(event.target.files[0]);
      reader.onload = () => {
        this.imagePreview = reader.result;
      };
      this.status = this.DefaultStatus;
      this.isValidFile = true;
    }
  }

  GetText() {
    if (this.isValidFile) {

      this.loading = true;
      this.imageData.append('imageFile', this.imageFile);

      this.computervisionService.getTextFromImage(this.imageData).subscribe(
        (result: OcrResult) => {
          this.ocrResult = result;
          if (this.availableLanguage.find(x => x.languageID === this.ocrResult.language)) {
            this.DetectedTextLanguage = this.availableLanguage.find(x => x.languageID === this.ocrResult.language).languageName;
          } else {
            this.DetectedTextLanguage = "inconnu";
          }
          this.loading = false;
        });
    }
  }
}

```

Nous allons injecter le `ComputervisionService` dans le constructeur du `OcrComponent` et définir un message et la valeur pour la taille maximale de l'image autorisée à l'intérieur du constructeur.

Nous allons invoquer la méthode `getAvailableLanguage` de notre service dans `ngOnInit` et stocker le résultat dans un tableau de type `AvailableLanguage`.

La méthode `uploadImage` sera invoquée lors du téléchargement d'une image. Nous allons vérifier si le fichier téléchargé est une image valide et dans la limite de taille autorisée. Nous allons traiter les données de l'image en utilisant un objet `FileReader`. La méthode `readAsDataURL` lira le contenu du fichier téléchargé. 

À la fin réussie de l'opération de lecture, l'événement `reader.onload` sera déclenché. La valeur de `imagePreview` sera définie sur le résultat retourné par l'objet fileReader, qui est de type `ArrayBuffer`.

À l'intérieur de la méthode `GetText`, nous allons ajouter le fichier image à une variable de type `FormData`. Nous allons invoquer `getTextFromImage` du service et lier le résultat à un objet de type `OcrResult`. Nous allons rechercher le nom de la langue dans le tableau `availableLanguage`, en fonction du code de langue retourné par le service. Si le code de langue n'est pas trouvé, nous définirons la langue comme inconnue.

Nous allons ajouter le style pour la zone de texte dans [ocr.component.css](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/ClientApp/src/app/ocr/ocr.component.css) comme indiqué ci-dessous.

```css
.preview-image {
    max-height: 300px;
    max-width: 300px;
}

.image-container{
  display: flex;
  padding: 15px;
  align-content: center;
  align-items: center;
  justify-content: center;
  border: 2px dashed skyblue;
}

```

## Ajout des liens dans le menu de navigation

Nous allons ajouter les liens de navigation pour nos composants dans le menu de navigation. Ouvrez [nav-menu.component.html](https://github.com/AnkitSharma-007/Angular-Computer-Vision-Azure-Cognitive-Services/blob/master/ngComputerVision/ClientApp/src/app/nav-menu/nav-menu.component.html#L14-L16) et supprimez les liens pour les composants Counter et Fetch data. Ajoutez les lignes suivantes dans la liste des liens de navigation.

```html
<li class="nav-item" [routerLinkActive]="['link-active']">
 <a class="nav-link text-dark" routerLink='/computer-vision-ocr'>Computer Vision</a>
</li>

```

## Démo d'exécution

Appuyez sur F5 pour lancer l'application. Cliquez sur le bouton Computer Vision dans le menu de navigation en haut. Vous pouvez télécharger une image et extraire le texte de l'image comme montré dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/ngComputerVision.gif)
_Démo d'exécution_

## Résumé

Nous avons créé une application de reconnaissance optique de caractères (OCR) en utilisant Angular et le service cognitif Azure Computer Vision. L'application est capable d'extraire le texte imprimé de l'image téléchargée et de reconnaître la langue du texte. L'API OCR de Computer Vision est utilisée et peut reconnaître le texte dans 25 langues.

Je viens de publier un eBook gratuit sur Angular et Firebase. Vous pouvez télécharger le livre gratuitement depuis [Créer une application Web Full-Stack en utilisant Angular & Firebase](https://www.c-sharpcorner.com/ebooks/build-a-full-stack-web-application-using-angular-and-firebase)

## Voir aussi

* [Validation de formulaire pilotée par modèle dans Angular](https://ankitsharmablogs.com/template-driven-form-validation-in-angular/)
* [Validation de formulaire réactive dans Angular](https://ankitsharmablogs.com/reactive-form-validation-in-angular/)
* [Déploiement continu pour une application Angular en utilisant Heroku et GitHub](https://ankitsharmablogs.com/continuous-deployment-for-angular-app-using-heroku-and-github/)
* [Autorisation basée sur les stratégies dans Angular en utilisant JWT](https://ankitsharmablogs.com/policy-based-authorization-in-angular-using-jwt/)
* [Lecteur de caractères optiques en utilisant Blazor et Computer Vision](https://ankitsharmablogs.com/optical-character-reader-using-blazor-and-computer-vision/)

Si vous aimez l'article, partagez-le avec vos amis. Vous pouvez également me suivre sur [Twitter](https://twitter.com/ankitsharma_007) et [LinkedIn](https://www.linkedin.com/in/ankitsharma-007/).