---
title: Comment résoudre une grille de Sudoku en utilisant Azure AI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-06T16:30:17.000Z'
originalURL: https://freecodecamp.org/news/solve-sudoku-using-azure-ai
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6065634f9618b008528ab1f6.jpg
tags:
- name: Angular
  slug: angular
- name: Azure
  slug: azure
- name: puzzles
  slug: puzzles
seo_title: Comment résoudre une grille de Sudoku en utilisant Azure AI
seo_desc: "By Ankit Sharma\nIn this article, we are going to create a sudoku solver\
  \ with the help of Azure Form Recognizer, an AI-powered document extraction service.\
  \ \nThe application will allow users to upload an image of the sudoku table. We\
  \ will extract the d..."
---

Par Ankit Sharma

Dans cet article, nous allons créer un solveur de sudoku à l'aide d'Azure Form Recognizer, un service d'extraction de documents alimenté par l'IA. 

L'application permettra aux utilisateurs de télécharger une image de la grille de sudoku. Nous extrairons les données de l'image, puis nous implémenterons l'algorithme de résolution de sudoku sur celle-ci.

Nous utiliserons .NET pour le backend, Angular pour le front end, et Angular Material pour le style de l'application.

Vous pouvez voir une démonstration fonctionnelle de l'application ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/SudokuSolver.gif)

## Prérequis

* Installer la dernière version LTS de Node.JS depuis [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
* Installer l'Angular CLI depuis [https://cli.angular.io/](https://cli.angular.io/)
* Un compte d'abonnement Azure. Vous pouvez créer un compte Azure gratuit à [https://azure.microsoft.com/en-in/free/](https://azure.microsoft.com/en-in/free/)
* Installer le SDK .NET Core 5.0 depuis [https://dotnet.microsoft.com/download/dotnet/5.0](https://dotnet.microsoft.com/download/dotnet/5.0)
* Installer la dernière version de Visual Studio 2019 depuis [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)

## Code Source

Vous pouvez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/Azure-AI-Sudoku-solver).

## Qu'est-ce que le service cognitif Azure Form Recognizer ?

Le service cognitif [Azure Form Recognizer](https://azure.microsoft.com/en-in/services/cognitive-services/form-recognizer/) nous permet de créer des logiciels de traitement automatique des données en utilisant la technologie d'apprentissage automatique. Il nous permet d'extraire du texte, des paires clé/valeur, des marques de sélection, des tableaux et des structures à partir de nos documents. 

Nous pouvons facilement invoquer les modèles Form Recognizer à l'aide d'une API REST ou des SDK de bibliothèque cliente.

Le service cognitif Form Recognizer fournit les fonctionnalités suivantes :

* **Modèles préconstruits** : Nous pouvons utiliser les modèles préconstruits pour extraire des données à partir de types de documents uniques tels que des factures, des reçus, des cartes d'identité et des cartes de visite.
* **Modèles personnalisés** : nous pouvons extraire du texte, des paires clé/valeur, des marques de sélection et des données de tableau à partir de formulaires en utilisant les modèles personnalisés. Cependant, nous devons entraîner les modèles personnalisés en utilisant nos données afin qu'ils répondent à nos besoins personnalisés.
* **API de mise en page** : Elle nous permet d'extraire du texte, des marques de sélection et des structures de tableau à partir des documents.

Dans cet article, nous allons utiliser l'API de mise en page pour extraire le contenu de l'image de la grille de sudoku que l'utilisateur télécharge.

## Comment créer la ressource du service cognitif Azure Form Recognizer

Connectez-vous au portail Azure et recherchez les services cognitifs dans la barre de recherche, puis cliquez sur le résultat. Sur l'écran suivant, cliquez sur le bouton Créer. Cela ouvrira la page du marketplace des services cognitifs. Recherchez Form Recognizer dans la barre de recherche et cliquez sur la carte « Form Recognizer » dans le résultat de la recherche. 

Cela ouvrira la page de l'API Form Recognizer. Cliquez sur le bouton Créer pour créer une nouvelle ressource Form Recognizer. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/CreateFR.png)

Sur la page Créer Form Recognizer, remplissez les détails comme indiqué ci-dessous.

* **Abonnement** : Sélectionnez le type d'abonnement dans la liste déroulante.
* **Groupe de ressources** : Sélectionnez un groupe de ressources existant ou créez-en un nouveau.
* **Région** : Choisissez la région qui vous convient.
* **Nom** : Donnez un nom unique à votre ressource.
* **Niveau tarifaire** : Sélectionnez le niveau tarifaire que vous souhaitez.

Cliquez sur le bouton « Vérifier + Créer ». Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/ConfigureFR.png)

Sur la page suivante, vérifiez les conditions d'utilisation, vérifiez les informations que vous avez fournies, puis cliquez sur le bouton « Créer ».

Une fois votre ressource déployée avec succès, cliquez sur le bouton « Accéder à la ressource ». Cliquez sur le lien « Clés et point de terminaison » dans le menu de gauche. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/FRKeys.png)

Notez le point de terminaison et l'une des clés fournies. Nous les utiliserons dans la suite de cet article pour invoquer l'API de mise en page du service Form Recognizer depuis le code .NET.

## Comment créer l'application ASP.NET Core

Ouvrez Visual Studio 2019 et cliquez sur « Créer un nouveau projet ». Une boîte de dialogue « Créer un nouveau projet » s'ouvrira. Sélectionnez « ASP.NET Core avec Angular » et cliquez sur Suivant. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/CreateProj.png)

Vous serez maintenant sur l'écran « Configurer votre nouveau projet ». Donnez le nom de votre application comme `ngSudokuSolver`, et cliquez sur Suivant. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/CreateProj_1.png)

Sur la page d'informations supplémentaires, sélectionnez le framework cible comme .NET 5.0 et définissez le type d'authentification sur aucun comme indiqué dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/CreateProj_2.png)

Cela créera notre projet. La structure des dossiers de l'application ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Sol_Exp.png)

Le dossier `ClientApp` contient le code Angular de notre application. Le dossier Controllers contiendra nos contrôleurs d'API. Les composants Angular sont présents dans le dossier `ClientApp\src\app`. 

Le modèle par défaut contient quelques composants Angular. Ces composants n'affecteront pas notre application, mais pour simplifier, nous supprimerons les dossiers `fetchdata` et `counter` du dossier `ClientApp/src/app`. Supprimez également la référence de ces deux composants du fichier `app.module.ts`.

## Comment installer les packages NuGet requis

Pour installer le package, accédez à Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages. Cela ouvrira la Console du gestionnaire de packages dans Visual Studio.

Exécutez la commande suivante pour installer la bibliothèque [Polly](https://www.nuget.org/packages/Polly). Cette bibliothèque vous permet d'exprimer des politiques de résilience et de gestion des pannes transitoires telles que la nouvelle tentative, le disjoncteur, le délai d'attente, l'isolement des cloisonnements et le repli de manière fluide et thread-safe.

```Install-Package Polly -Version 7.2.1```

Exécutez la commande suivante pour installer le package [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/).

```Install-Package Newtonsoft.Json -Version 13.0.1```

## Comment créer le gestionnaire RetryMessage

Faites un clic droit sur le projet `ngSudokuSolver` et sélectionnez Ajouter >> Nouveau dossier. Nommez le dossier Models. 

Encore une fois, faites un clic droit sur le dossier Models et sélectionnez Ajouter >> Classe pour ajouter un nouveau fichier de classe. Donnez le nom de votre classe comme `HttpRetryMessageHandler.cs` et cliquez sur "Ajouter". 

Mettez le code suivant à l'intérieur de cette classe.

```C#

using Newtonsoft.Json;
using Polly;
using System;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;

namespace ngSudokuSolver.Models
{
    public class HttpRetryMessageHandler : DelegatingHandler
    {
        public HttpRetryMessageHandler(HttpClientHandler handler) : base(handler) { }

        protected override Task<HttpResponseMessage> SendAsync(
            HttpRequestMessage request,
            CancellationToken cancellationToken) =>
            Policy
                .Handle<HttpRequestException>()
                .Or<TaskCanceledException>()
                .OrResult<HttpResponseMessage>(x =>
                {
                    string result = x.Content.ReadAsStringAsync().GetAwaiter().GetResult();
                    dynamic array = JsonConvert.DeserializeObject(result);

                    if (array["status"] == "running")
                    {
                        return true;
                    }
                    else
                    {
                        return false;
                    }
                })
                .WaitAndRetryAsync(7, retryAttempt => TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)))
                .ExecuteAsync(() => base.SendAsync(request, cancellationToken));
    }
}

```

Nous utiliserons le RetryMessageHandler pour réessayer l'appel `sendAsync`. Nous réessaierons l'appel HTTP si le statut du HttpResponseMessage est "running". 

Le nombre maximal de tentatives de réessai est défini à 7. À chaque réessai, nous augmenterons la durée du temps d'attente par une puissance de 2. Si le nombre maximal de réessais a été épuisé et que le HttpResponseMessage n'est pas encore réussi, nous retournerons false.

## Comment ajouter le contrôleur FormRecognizer

Nous allons maintenant ajouter un nouveau contrôleur à notre application. 

Faites un clic droit sur le dossier Controllers et sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue "Ajouter un nouvel élément" s'ouvrira. 

Sélectionnez "Visual C#" dans le panneau de gauche, puis sélectionnez "Contrôleur d'API - Vide" dans le panneau des modèles et donnez le nom `FormRecognizerController.cs`. Cliquez sur Ajouter. Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/AddController.png)

Mettez le code suivant à l'intérieur de cette classe.

```C#
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using ngSudokuSolver.Models;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace ngSudokuSolver.Controllers
{
    [Produces("application/json")]
    [Route("api/[controller]")]
    public class FormRecognizerController : ControllerBase
    {
        static string endpoint;
        static string apiKey;

        public FormRecognizerController()
        {
            endpoint = "https://sudokusolver.cognitiveservices.azure.com/";
            apiKey = "a9f75796b3ba49bdade48eb3b905cb0e";
        }

        [HttpPost, DisableRequestSizeLimit]
        public async Task<string[][]> Post()
        {
            try
            {
                string[][] sudokuArray = GetNewSudokuArray();

                if (Request.Form.Files.Count > 0)
                {
                    var file = Request.Form.Files[Request.Form.Files.Count - 1];

                    if (file.Length > 0)
                    {
                        var memoryStream = new MemoryStream();
                        file.CopyTo(memoryStream);
                        byte[] imageFileBytes = memoryStream.ToArray();
                        memoryStream.Flush();

                        string SudokuLayoutJSON = await GetSudokuBoardLayout(imageFileBytes);
                        if (SudokuLayoutJSON.Length > 0)
                        {
                            sudokuArray = GetSudokuBoardItems(SudokuLayoutJSON);
                        }
                    }
                }

                return sudokuArray;
            }
            catch
            {
                throw;
            }
        }

        static async Task<string> GetSudokuBoardLayout(byte[] byteData)
        {
            HttpClient client = new();
            client.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", apiKey);
            string uri = endpoint + "formrecognizer/v2.1-preview.3/layout/analyze";
            string LayoutJSON = string.Empty;

            using (ByteArrayContent content = new(byteData))
            {
                HttpResponseMessage response;
                content.Headers.ContentType = new MediaTypeHeaderValue("image/png");
                response = await client.PostAsync(uri, content);

                if (response.IsSuccessStatusCode)
                {
                    HttpHeaders headers = response.Headers;

                    if (headers.TryGetValues("Operation-Location", out IEnumerable<string> values))
                    {
                        string OperationLocation = values.First();
                        LayoutJSON = await GetJSON(OperationLocation);
                    }
                }
            }
            return LayoutJSON;
        }

        static async Task<string> GetJSON(string endpoint)
        {
            using var client = new HttpClient(new HttpRetryMessageHandler(new HttpClientHandler()));
            var request = new HttpRequestMessage();
            request.Method = HttpMethod.Get;
            request.RequestUri = new Uri(endpoint);

            client.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", apiKey);

            var response = await client.SendAsync(request);
            var result = response.Content.ReadAsStringAsync().GetAwaiter().GetResult();

            return result;
        }

        static string[][] GetSudokuBoardItems(string LayoutData)
        {
            string[][] sudokuArray = GetNewSudokuArray();
            dynamic array = JsonConvert.DeserializeObject(LayoutData);
            int countOfCells = ((JArray)array?.analyzeResult?.pageResults[0]?.tables[0]?.cells).Count;

            for (int i = 0; i < countOfCells; i++)
            {
                int rowIndex = array.analyzeResult.pageResults[0].tables[0].cells[i].rowIndex;
                int columnIndex = array.analyzeResult.pageResults[0].tables[0].cells[i].columnIndex;

                sudokuArray[rowIndex][columnIndex] = array.analyzeResult.pageResults[0].tables[0].cells[i]?.text;
            }
            return sudokuArray;
        }

        static string[][] GetNewSudokuArray()
        {
            string[][] sudokuArray = new string[9][];

            for (int i = 0; i < 9; i++)
            {
                sudokuArray[i] = new string[9];
            }

            return sudokuArray;
        }
    }
}
```

Dans le constructeur de la classe, nous avons initialisé la clé et l'URL du point de terminaison pour l'API formrecognizer.

La méthode Post recevra les données d'image sous forme de collection de fichiers dans le corps de la requête et retournera un tableau à deux dimensions. Nous convertirons les données d'image en un tableau d'octets et invoquerons la méthode `GetSudokuBoardLayout`. Si nous obtenons une réponse réussie et que le résultat JSON n'est pas vide, nous invoquerons la méthode `GetSudokuBoardItems`.

À l'intérieur de la méthode `GetSudokuBoardLayout`, nous instancierons un nouveau HttpClient. Nous passerons la clé d'abonnement dans l'en-tête de la requête. 

Lorsque nous utilisons l'API formrecognizer, nous obtiendrons un code de statut 202. Cela indique que le service a accepté la requête et commencera le traitement plus tard. 

La réponse inclut un en-tête "Operation-Location". Le champ "Operation-Location" contient l'URL que nous devons utiliser pour obtenir le résultat de l'opération formrecognizer. L'URL mentionnée dans l'en-tête expirera dans 48 heures.

Pour que le résultat du service formrecognizer soit disponible, cela nécessite une certaine quantité de temps qui dépend de la longueur du texte. 

C'est là que notre RetryMessageHandler sera utilisé. Nous récupérerons l'URL de l'en-tête et invoquerons la méthode `GetJSON` pour récupérer le résultat JSON. 

À l'intérieur de la méthode `GetJSON`, nous créons le HttpClient et l'initialisons avec notre `HttpRetryMessageHandler` personnalisé. Cette méthode retournera la réponse JSON sous forme de chaîne.

La méthode `GetSudokuBoardItems` acceptera la chaîne JSON. Elle itérera ensuite sur la propriété tables de la chaîne JSON pour préparer le tableau à deux dimensions `sudokuArray`.

## Maintenant, travaillons sur le côté client de l'application

Le code pour le côté client est disponible dans le dossier ClientApp. Nous utiliserons Angular CLI pour travailler avec le code client.

> L'utilisation d'Angular CLI n'est pas obligatoire. J'utilise Angular CLI ici car il est convivial et simple. Si vous ne souhaitez pas utiliser CLI, vous pouvez créer les fichiers pour les composants et les services manuellement.

Accédez au dossier `ngSudokuSolver\ClientApp` sur votre machine et ouvrez une fenêtre de commande. Nous exécuterons toutes nos commandes Angular CLI dans cette fenêtre.

## Comment installer Angular Material

Exécutez la commande suivante pour ajouter Angular Material au projet.

```ng add @angular/material```

Cette commande installera Angular Material dans votre projet, puis posera les questions suivantes pour déterminer quelles fonctionnalités inclure :

* Choisissez un nom de thème préconstruit, ou "custom" pour un thème personnalisé : Nous sélectionnerons le thème Indigo/Pink.
* Configurer les styles de typographie globale Angular Material ? (Y/n) : Y
* Configurer les animations du navigateur pour Angular Material ? (Y/n) : Y

Reportons-nous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/ngMaterial.png)

## Comment ajouter le module pour Angular Material

Exécutez la commande suivante pour créer un nouveau module.

```ng g m ng-material```

Ouvrez le fichier `src\app\ng-material\ng-material.module.ts` et mettez le code suivant à l'intérieur.

```typescript
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatDividerModule } from '@angular/material/divider';
import { MatIconModule } from '@angular/material/icon';

const materialModules = [
  MatButtonModule,
  MatCardModule,
  MatInputModule,
  MatToolbarModule,
  MatDividerModule,
  MatIconModule,
];

@NgModule({
  declarations: [],
  imports: [CommonModule, ...materialModules],
  exports: [...materialModules],
})
export class NgMaterialModule {}
```

Nous importons tous les modules requis pour les composants Angular Material que nous utiliserons dans cette application. Un module séparé pour Angular Material rendra l'application facile à maintenir.

Importez le `NgMaterialModule` dans le fichier `app.module.ts` comme indiqué ci-dessous :

```
import { NgMaterialModule } from './ng-material/ng-material.module';

@NgModule({
	...
	imports: [
		...
		NgMaterialModule,
	],
})
```

## Comment configurer la barre de navigation de l'application

Ouvrez `nav-menu.component.html` et mettez le code suivant à l'intérieur.

```html
<mat-toolbar color="primary" class="mat-elevation-z2">
  <mat-toolbar-row>
    <div>
      <button mat-button [routerLink]='["/"]'>
        <mat-icon>book</mat-icon> Solveur de Sudoku
      </button>
    </div>
  </mat-toolbar-row>
</mat-toolbar>
```

Nous avons ajouté la barre d'outils material et un bouton qui liera à la route de base de l'application.

## Comment créer le service Form Recognizer

Nous allons créer un service Angular qui invoquera les points de terminaison de l'API Web et transmettra la réponse à notre composant. Exécutez la commande suivante.

```ng g s services\form-recognizer```

Cette commande créera un dossier nommé services et créera ensuite les deux fichiers suivants à l'intérieur :

* form-recognizer.service.ts

 le fichier de classe de service.
* form-recognizer.service.spec.ts

 le fichier de test unitaire pour le service.

Ouvrez le fichier `form-recognizer.service.ts` et mettez le code suivant à l'intérieur.

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class FormRecognizerService {
  baseURL: string;

  constructor(private http: HttpClient) {
    this.baseURL = '/api/FormRecognizer';
  }

  getSudokuTableFromImage(image: FormData) {
    return this.http.post(this.baseURL, image);
  }
}
```

Nous avons défini une variable baseURL qui contiendra l'URL du point de terminaison de notre API. Nous initialiserons le baseURL dans le constructeur et le définirons sur le point de terminaison du `FormRecognizerController`.

La méthode `getSudokuTableFromImage` enverra une requête Post au `FormRecognizerController` et fournira le paramètre de type FormData. Elle récupérera un tableau à deux dimensions qui désigne les éléments dans la grille de sudoku.

## Comment mettre à jour le composant Home

Ouvrez `home.component.html` et mettez le code suivant à l'intérieur.

```html
<div class="container">
  <h1 class="display-4">Résoudre le Sudoku en utilisant Azure AI</h1>
  <mat-divider></mat-divider>
  <div class="row mt-3">
    <div class="col-md-6">
      <mat-card class="mat-elevation-z4">
        <mat-card-content>
          <table>
            <tr *ngFor="let row of gameBoard">
              <td *ngFor="let col of gameBoard">
                {{game[row][col]}}
              </td>
            </tr>
          </table>
        </mat-card-content>
        <mat-card-actions>
          <button type="button" mat-raised-button color="primary" (click)="SolveSudoku()"> Résoudre le Sudoku </button>
        </mat-card-actions>
      </mat-card>
    </div>
    <div class="col-md-6">
      <div class="image-container">
        <img class="preview-image" src={{imagePreview}}>
      </div>
      <input type="file" (change)="uploadImage($event)" />
      <hr />
      <button mat-raised-button color="accent" (click)="GetSudokuTable()">
        <span *ngIf="loading" class="spinner-border spinner-border-sm mr-1"></span>Extraire la grille de Sudoku
      </button>
    </div>
  </div>
</div>
```

Nous avons créé un tableau 9x9 qui désigne une grille de sudoku. Nous avons défini un contrôle de téléchargement de fichier qui nous permettra de télécharger une image. Après avoir téléchargé l'image, l'aperçu de l'image sera affiché à l'aide d'un élément `<img>`.

En cliquant sur le bouton "Extraire la grille de Sudoku" récupérera le contenu du sudoku à partir de l'image et remplira partiellement le tableau. En cliquant sur "Résoudre le Sudoku" résoudra le sudoku et mettra à jour le tableau avec le résultat.

Ouvrez le fichier `home.component.ts` et mettez le code suivant à l'intérieur.

```typescript
import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subject } from 'rxjs';
import { FormRecognizerService } from '../services/form-recognizer.service';
import { takeUntil } from 'rxjs/operators';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnDestroy {
  gameBoard = [0, 1, 2, 3, 4, 5, 6, 7, 8];
  loading = false;
  imageFile;
  imagePreview;
  maxFileSize: number;
  isValidFile = true;
  status: string;
  DefaultStatus: string;
  imageData = new FormData();
  game = new Array(9);
  private unsubscribe$ = new Subject();

  constructor(private formRecognizerService: FormRecognizerService) {
    this.DefaultStatus = 'La taille maximale autorisée pour l\'image est de 4 Mo';
    this.status = this.DefaultStatus;
    this.maxFileSize = 4 * 1024 * 1024; // 4MB

    for (var i = 0; i < this.game.length; i++) {
      this.game[i] = new Array(9);
    }
  }

  uploadImage(event) {
    this.imageFile = event.target.files[0];
    if (this.imageFile.size > this.maxFileSize) {
      this.status = `La taille du fichier est de ${this.imageFile.size} octets, ce qui est plus que la limite autorisée de ${this.maxFileSize} octets.`;
      this.isValidFile = false;
    } else if (this.imageFile.type.indexOf('image') == -1) {
      this.status = 'Veuillez télécharger un fichier image valide';
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

  GetSudokuTable() {
    if (this.isValidFile) {
      this.loading = true;
      this.imageData.append('imageFile', this.imageFile);

      this.formRecognizerService
        .getSudokuTableFromImage(this.imageData)
        .pipe(takeUntil(this.unsubscribe$))
        .subscribe(
          (result: any) => {
            this.game = result;
            this.loading = false;
          },
          () => {
            console.error();
            this.loading = false;
          }
        );
    }
  }

  SolveSudoku() {
    this.sudokuSolver(this.game);
  }

  ngOnDestroy() {
    this.unsubscribe$.next();
    this.unsubscribe$.complete();
  }

  private sudokuSolver(data) {
    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        if (data[i][j] == '') {
          for (let k = 1; k <= 9; k++) {
            if (this.isSudokuValid(data, i, j, k)) {
              data[i][j] = `${k}`;
              if (this.sudokuSolver(data)) {
                return true;
              } else {
                data[i][j] = '';
              }
            }
          }
          return false;
        }
      }
    }
    return true;
  }

  private isSudokuValid(board, row, col, k) {
    for (let i = 0; i < 9; i++) {
      const m = 3 * Math.floor(row / 3) + Math.floor(i / 3);
      const n = 3 * Math.floor(col / 3) + (i % 3);
      if (board[row][i] == k || board[i][col] == k || board[m][n] == k) {
        return false;
      }
    }
    return true;
  }
}
```

Nous allons injecter le formRecognizerService dans le constructeur du `HomeComponent` et définir un message et la valeur pour la taille maximale de l'image autorisée à l'intérieur du constructeur. Nous allons également initialiser le tableau à deux dimensions pour contenir la valeur du sudoku.

La méthode `uploadImage` sera invoquée lors du téléchargement d'une image. Nous vérifierons si le fichier téléchargé est une image valide et est dans la limite de taille autorisée. Nous traiterons les données de l'image à l'aide d'un objet FileReader. La méthode readAsDataURL lira le contenu du fichier téléchargé. 

Lorsque l'opération de lecture se termine avec succès, l'événement reader.onload sera déclenché. La valeur de imagePreview sera définie sur le résultat retourné par l'objet fileReader, qui est de type ArrayBuffer.

À l'intérieur de la méthode `GetSudokuTable`, nous ajouterons le fichier image à une variable de type FormData. Nous invoquerons le `getSudokuTableFromImage` du service et lierons le résultat au tableau game.

La méthode `sudokuSolver` acceptera la grille de Sudoku comme paramètre. Nous résoudrons ensuite la grille de sudoku à l'aide de l'algorithme de backtracking.

## Démonstration d'exécution

Appuyez sur F5 pour lancer l'application. Téléchargez l'image d'une grille de sudoku. Cliquez sur le bouton "Extraire la grille de Sudoku". Cela extraira le contenu de l'image et remplira le tableau du côté gauche. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/ExecDemo1.png)

Cliquez sur le bouton "Résoudre le Sudoku". Vous pouvez voir le résultat final du sudoku sur l'interface utilisateur. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/ExecDemo2.png)

## **Résumé**

Nous avons créé une application de résolution de sudoku en utilisant Angular et le service Azure Form Recognizer. L'application peut extraire les données de l'image d'une grille de sudoku téléchargée par l'utilisateur. Nous implémentons ensuite le backtracking pour résoudre le sudoku. Nous avons utilisé Angular Material pour styliser l'application.

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/Azure-AI-Sudoku-solver) et jouez avec pour mieux comprendre.

## Voir aussi

* [Lecteur de caractères optiques utilisant Angular et Azure Computer Vision](https://ankitsharmablogs.com/optical-character-reader-using-angular-and-azure-computer-vision/)
* [Traduction multilingue utilisant Blazor et Azure Cognitive Services](https://ankitsharmablogs.com/multi-language-translator-using-blazor-and-azure-cognitive-services/)
* [Authentification et autorisation Facebook dans une application Blazor côté serveur](https://ankitsharmablogs.com/facebook-authentication-and-authorization-in-server-side-blazor-app/)
* [Déploiement continu pour une application Angular utilisant Heroku et GitHub](https://ankitsharmablogs.com/continuous-deployment-for-angular-app-using-heroku-and-github/)
* [Aller sans serveur avec Blazor](https://ankitsharmablogs.com/going-serverless-with-blazor/)

Si vous aimez l'article, veuillez le partager avec vos amis. Vous pouvez également me suivre sur [Twitter](https://twitter.com/ankitsharma_007) et [LinkedIn](https://www.linkedin.com/in/ankitsharma-007/).

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)