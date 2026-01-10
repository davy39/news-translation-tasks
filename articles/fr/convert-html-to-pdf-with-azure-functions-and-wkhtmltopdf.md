---
title: Comment convertir HTML en PDF avec Azure Functions et wkhtmltopdf
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-20T16:02:01.000Z'
originalURL: https://freecodecamp.org/news/convert-html-to-pdf-with-azure-functions-and-wkhtmltopdf
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/html-to-pdf.jpeg
tags:
- name: Azure Functions
  slug: azure-functions
- name: HTML
  slug: html
- name: pdf
  slug: pdf
seo_title: Comment convertir HTML en PDF avec Azure Functions et wkhtmltopdf
seo_desc: "By Arjav Dave\nIn this article, we are going to use Azure Functions and\
  \ the wkhtmltopdf tool to generate a PDF file from an HTML file. \nYou might want\
  \ to create a PDF file for a great many reasons, such as generating invoices for\
  \ sales, medical report..."
---

Par Arjav Dave

Dans cet article, nous allons utiliser Azure Functions et l'outil [wkhtmltopdf](https://wkhtmltopdf.org/) pour générer un fichier PDF à partir d'un fichier HTML. 

Vous pourriez vouloir créer un fichier PDF pour de nombreuses raisons, telles que générer des factures pour les ventes, des rapports médicaux pour vos patients, des formulaires d'assurance pour vos clients, et ainsi de suite. Et il existe plusieurs façons de procéder.

Tout d'abord, vous pouvez utiliser l'outil de remplissage et de signature d'[Adobe](https://www.adobe.com/in/acrobat/online/sign-pdf.html) pour remplir des formulaires. Mais cela nécessite principalement une interaction humaine et n'est donc pas évolutif ou pratique.

La deuxième option consiste à créer directement un fichier PDF. Selon la plateforme sur laquelle vous travaillez, vous aurez des outils pour le faire. Si c'est un PDF très simple, vous pouvez adopter cette approche.

Cela nous amène à notre dernière et meilleure option, [wkhtmltopdf](https://wkhtmltopdf.org/). C'est un outil vraiment génial qui vous permet de convertir votre HTML en PDF. Puisqu'il est gratuit, open source et peut être compilé pour presque toutes les plateformes, c'est notre meilleur choix.

## Prérequis

* Éditeur VS Code installé
* Un compte sur [Azure Portal](https://portal.azure.com/)
* Plan de service d'application Linux Basic (B1). Si vous avez déjà un plan de service d'application Windows Basic (B1), vous pouvez l'utiliser.
* Compte de stockage Azure.

## Comment utiliser Azure Functions

Puisque la conversion de HTML en PDF est une tâche chronophage, nous ne devrions pas l'exécuter sur notre serveur web principal. Sinon, cela pourrait commencer à bloquer d'autres requêtes importantes. Azure Functions est le meilleur moyen de déléguer de telles tâches.

Pour créer une fonction, vous devrez d'abord installer Azure Functions sur votre machine. Selon votre système d'exploitation, installez les [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Ccsharp%2Cbash#install-the-azure-functions-core-tools). 

Une fois installé, ouvrez votre outil de ligne de commande pour exécuter la commande suivante. `html2pdf` est le nom du projet ici, mais vous pouvez le remplacer par n'importe quel nom.

```func init html2pdf```

Lorsque vous exécutez la commande, elle vous demandera un runtime de worker. Ici, sélectionnez l'option 1, dotnet puisque c'est un produit Microsoft et qu'il offre un excellent support pour dotnet. 

Cela générera un dossier nommé `html2pdf` dans votre répertoire actuel. Puisque Visual Studio Code permet de publier directement sur Azure Functions, nous allons l'utiliser pour coder et déployer.

Après avoir ouvert votre projet dans VS Code, créez un fichier nommé `Html2Pdf.cs`. Azure Functions propose une grande variété de [déclencheurs](https://www.serverless360.com/blog/azure-functions-triggers-and-bindings) pour exécuter la fonction. Pour l'instant, nous allons commencer avec le déclencheur HTTP, c'est-à-dire que la fonction peut être appelée directement via le protocole HTTP. 

Dans notre fichier nouvellement créé, collez le contenu suivant :

```
using System;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.Extensions.Logging;

namespace Html2Pdf
{
    public class Html2Pdf
    {
        // Le nom de la fonction
        [FunctionName("Html2Pdf")]
        
        // Le premier argument indique que les fonctions peuvent être déclenchées par une requête HTTP POST. 
        // Le deuxième argument est principalement utilisé pour les informations de journalisation, les avertissements ou les erreurs
        public void Run([HttpTrigger(AuthorizationLevel.Function, "POST")] Html2PdfRequest Request, ILogger Log)
        {
        }
    }
}
```

Nous avons créé le squelette et maintenant nous allons remplir les détails. Comme vous l'avez peut-être remarqué, le type de variable de requête est `Html2PdfRequest`. Alors créons un modèle de classe `Html2PdfRequest.cs` comme suit :

```
namespace Html2Pdf
{
    public class Html2PdfRequest
    {
        // Le contenu HTML qui doit être converti.
        public string HtmlContent { get; set; }
      
        // Le nom du fichier PDF à générer
        public string PDFFileName { get; set; }
    }
}
```

## Comment ajouter DinkToPdf à votre projet

Pour invoquer wkhtmltopdf depuis notre code géré, nous utilisons une technologie appelée P/Invoke.

En bref, [P/Invoke](https://docs.microsoft.com/en-us/dotnet/standard/native-interop/pinvoke) nous permet d'accéder aux structures, aux rappels et aux fonctions dans les bibliothèques non gérées. Il existe un wrapper P/Invoke nommé [DinkToPdf](https://github.com/rdvojmoc/DinkToPdf) qui nous permet d'abstraire les détails techniques.

Vous pouvez ajouter DinkToPdf à votre projet via [nuget](https://www.nuget.org/packages/DinkToPdf/). Exécutez simplement la commande depuis votre dossier racine.

```
dotnet add package DinkToPdf --version 1.0.8
```

Il est temps d'ajouter du code en haut de notre classe `Html2Pdf` :

```
// Lire plus sur le convertisseur sur : https://github.com/rdvojmoc/DinkToPdf
// Pour nos besoins, nous allons utiliser SynchronizedConverter
IPdfConverter pdfConverter = new SynchronizedConverter(new PdfTools());

// Une fonction pour convertir le contenu html en pdf en fonction de la configuration passée en arguments
// Arguments :
// HtmlContent : le contenu html à convertir
// Width : la largeur du pdf à créer. ex. "8.5in", "21.59cm" etc.
// Height : la hauteur du pdf à créer. ex. "11in", "27.94cm" etc.
// Margins : les marges autour du contenu
// DPI : Le dpi est très important lorsque vous voulez imprimer le pdf.
// Retourne un tableau d'octets du pdf qui peut être stocké comme un fichier
private byte[] BuildPdf(string HtmlContent, string Width, string Height, MarginSettings Margins, int? DPI = 180)
{
  // Appeler la méthode Convert de SynchronizedConverter "pdfConverter"
  return pdfConverter.Convert(new HtmlToPdfDocument()
            {
                // Définir le contenu html
                Objects =
                {
                    new ObjectSettings
                    {
                        HtmlContent = HtmlContent
                    }
                },
                // Définir les configurations
                GlobalSettings = new GlobalSettings
                {
                    // PaperKind.A4 peut également être utilisé au lieu de PechkinPaperSize
                    PaperSize = new PechkinPaperSize(Width, Height),
                    DPI = DPI,
                    Margins = Margins
                }
            });
}
```

J'ai ajouté des commentaires en ligne pour que le code soit explicite. Si vous avez des questions, vous pouvez me les poser sur Twitter. Appelons la fonction créée ci-dessus depuis notre méthode `Run`.

```
// PDFByteArray est un tableau d'octets de pdf généré à partir du HtmlContent 
var PDFByteArray = BuildPdf(Request.HtmlContent, "8.5in", "11in", new MarginSettings(0, 0, 0,0));
```

Une fois le tableau d'octets généré, stockons-le sous forme de blob dans Azure Storage. Avant de télécharger le blob, assurez-vous de créer un conteneur. Une fois cela fait, ajoutez le code suivant après `PDFByteArray`.

```
// La chaîne de connexion du compte de stockage vers lequel notre fichier PDF sera téléchargé
// Assurez-vous de remplacer par votre chaîne de connexion.
var StorageConnectionString = "DefaultEndpointsProtocol=https;AccountName=<YOUR ACCOUNT NAME>;AccountKey=<YOUR ACCOUNT KEY>;EndpointSuffix=core.windows.net";

// Générer une instance de CloudStorageAccount en analysant la chaîne de connexion
var StorageAccount = CloudStorageAccount.Parse(StorageConnectionString);

// Créer une instance de CloudBlobClient pour se connecter à notre compte de stockage
CloudBlobClient BlobClient = StorageAccount.CreateCloudBlobClient();

// Obtenir l'instance de CloudBlobContainer qui pointe vers un conteneur nommé "pdf"
// Remplacez par votre propre nom de conteneur
CloudBlobContainer BlobContainer = BlobClient.GetContainerReference("pdf");

// Obtenir l'instance de CloudBlockBlob vers laquelle le PDFByteArray sera téléchargé
CloudBlockBlob Blob = BlobContainer.GetBlockBlobReference(Request.PDFFileName);

// Télécharger le blob pdf
await Blob.UploadFromByteArrayAsync(PDFByteArray, 0, PDFByteArray.Length);
```

Vous verrez quelques erreurs et avertissements après avoir ajouté ce code. Pour les corriger, ajoutez d'abord les instructions d'importation manquantes. Ensuite, changez le type de retour de `void` à `async Task` pour la fonction `Run`. Voici à quoi ressemblera le fichier final `Html2Pdf.cs` :

```
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.Extensions.Logging;
using DinkToPdf;
using IPdfConverter = DinkToPdf.Contracts.IConverter;
using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Blob;
using System.Threading.Tasks;

namespace Html2Pdf
{
    public class Html2Pdf
    {
        // Lire plus sur le convertisseur sur : https://github.com/rdvojmoc/DinkToPdf
        // Pour nos besoins, nous allons utiliser SynchronizedConverter
        IPdfConverter pdfConverter = new SynchronizedConverter(new PdfTools());

        // Une fonction pour convertir le contenu html en pdf en fonction de la configuration passée en arguments
        // Arguments :
        // HtmlContent : le contenu html à convertir
        // Width : la largeur du pdf à créer. ex. "8.5in", "21.59cm" etc.
        // Height : la hauteur du pdf à créer. ex. "11in", "27.94cm" etc.
        // Margins : les marges autour du contenu
        // DPI : Le dpi est très important lorsque vous voulez imprimer le pdf.
        // Retourne un tableau d'octets du pdf qui peut être stocké comme un fichier
        private byte[] BuildPdf(string HtmlContent, string Width, string Height, MarginSettings Margins, int? DPI = 180)
        {
            // Appeler la méthode Convert de SynchronizedConverter "pdfConverter"
            return pdfConverter.Convert(new HtmlToPdfDocument()
            {
                // Définir le contenu html
                Objects =
                {
                    new ObjectSettings
                    {
                        HtmlContent = HtmlContent
                    }
                },
                // Définir les configurations
                GlobalSettings = new GlobalSettings
                {
                    // PaperKind.A4 peut également être utilisé au lieu de la largeur et de la hauteur
                    PaperSize = new PechkinPaperSize(Width, Height),
                    DPI = DPI,
                    Margins = Margins
                }
            });
        }

        // Le nom de la fonction
        [FunctionName("Html2Pdf")]

        // Le premier argument indique que les fonctions peuvent être déclenchées par une requête HTTP POST. 
        // Le deuxième argument est principalement utilisé pour les informations de journalisation, les avertissements ou les erreurs
        public async Task Run([HttpTrigger(AuthorizationLevel.Function, "POST")] Html2PdfRequest Request, ILogger Log)
        {
            // PDFByteArray est un tableau d'octets de pdf généré à partir du HtmlContent 
            var PDFByteArray = BuildPdf(Request.HtmlContent, "8.5in", "11in", new MarginSettings(0, 0, 0, 0));

            // La chaîne de connexion du compte de stockage vers lequel notre fichier PDF sera téléchargé
            var StorageConnectionString = "DefaultEndpointsProtocol=https;AccountName=<YOUR ACCOUNT NAME>;AccountKey=<YOUR ACCOUNT KEY>;EndpointSuffix=core.windows.net";
            
            // Générer une instance de CloudStorageAccount en analysant la chaîne de connexion
            var StorageAccount = CloudStorageAccount.Parse(StorageConnectionString);

            // Créer une instance de CloudBlobClient pour se connecter à notre compte de stockage
            CloudBlobClient BlobClient = StorageAccount.CreateCloudBlobClient();

            // Obtenir l'instance de CloudBlobContainer qui pointe vers un conteneur nommé "pdf"
            // Remplacez par votre propre nom de conteneur
            CloudBlobContainer BlobContainer = BlobClient.GetContainerReference("pdf");
            
            // Obtenir l'instance de CloudBlockBlob vers laquelle le PDFByteArray sera téléchargé
            CloudBlockBlob Blob = BlobContainer.GetBlockBlobReference(Request.PDFFileName);
            
            // Télécharger le blob pdf
            await Blob.UploadFromByteArrayAsync(PDFByteArray, 0, PDFByteArray.Length);
        }
    }
}
```

Cela conclut la partie codage de ce tutoriel !

## Comment ajouter wkhtmltopdf à votre projet

Nous devons encore ajouter la bibliothèque wkhtmltopdf à notre projet. Il y a quelques mises en garde lors de la sélection d'un plan Azure App spécifique. Selon le plan, nous devrons obtenir la bibliothèque wkhtmltopdf. 

Pour nos besoins, nous avons sélectionné le plan de service d'application Linux Basic (B1) puisque le plan de service d'application Windows Basic (B1) est cinq fois plus cher.

Au moment de la rédaction de ce blog, le plan de service d'application Azure utilisait Debian 10 avec une architecture amd64. Heureusement pour nous, DinkToPdf fournit des [bibliothèques précompilées](https://github.com/rdvojmoc/DinkToPdf/tree/master/v0.12.4/64%20bit) pour Linux, Windows et MacOS. 

Téléchargez la bibliothèque .so pour Linux et placez-la dans le dossier racine de votre projet. Je travaille sur MacOS, donc j'ai également téléchargé libwkhtmltox.dylib. 

Si vous utilisez Windows ou si vous avez hébergé les Azure Functions sur le plan de service d'application Windows, vous devez télécharger le fichier libwkhtmltox.dll. Voici à quoi ressemblera la structure de notre projet maintenant :

![Image](https://i2.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-21-at-4.41.20-PM.png?resize=676%2C546&ssl=1)
_Structure du projet_

Lorsque nous créons une build, nous devons inclure la bibliothèque .so. Pour ce faire, ouvrez votre fichier csproj et ajoutez le contenu suivant à l'ItemGroup.

```
<None Update="./libwkhtmltox.so">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    <CopyToPublishDirectory>Always</CopyToPublishDirectory>
</None>
```

Voici le fichier csproj complet :

```
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>netcoreapp3.1</TargetFramework>
    <AzureFunctionsVersion>v3</AzureFunctionsVersion>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="DinkToPdf" Version="1.0.8" />
    <PackageReference Include="Microsoft.NET.Sdk.Functions" Version="3.0.11" />
  </ItemGroup>
  <ItemGroup>
    <None Update="host.json">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
    <None Update="local.settings.json">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
      <CopyToPublishDirectory>Never</CopyToPublishDirectory>
    </None>
    <None Update="./libwkhtmltox.so">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
      <CopyToPublishDirectory>Always</CopyToPublishDirectory>
    </None>
  </ItemGroup>
</Project>
```

## Comment créer l'application Azure Functions

Avant de déployer sur Azure Functions, nous devons la créer dans le portail Azure. Vous pouvez aller sur le portail Azure et commencer à créer la ressource _Azure Functions_. Suivez les captures d'écran ci-dessous pour plus de clarté.

![Image](https://i2.wp.com/arjavdave.com/wp-content/uploads/2021/03/Untitled-1.jpg?resize=750%2C724&ssl=1)
_Détails de l'instance_

Dans la capture d'écran ci-dessous, assurez-vous de sélectionner ou de créer au moins le plan _Basic_. Deuxièmement, dans le système d'exploitation, sélectionnez _Linux_.

![Image](https://i2.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-10.30.48-AM.png?resize=750%2C784&ssl=1)
_Détails du plan_

Il est bon d'avoir _Application Insights_ puisque vous pourrez voir les journaux et surveiller les fonctions. De plus, cela coûte à peine quelque chose. Comme le montre la capture d'écran ci-dessous, sélectionnez _Oui_ si vous souhaitez l'activer.

![Image](https://i1.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-10.31.11-AM.png?resize=750%2C798&ssl=1)
_Application Insights_

Sélectionnez Suivant : Balises et cliquez à nouveau sur Suivant et sur _Créer_ pour créer votre ressource. Cela peut prendre quelques minutes pour créer la ressource _Azure Functions_.

## Comment déployer sur Azure Functions

Une fois créée, nous allons déployer notre code directement sur Azure Functions via VS Code. Pour cela, vous devrez aller dans les extensions et installer l'extension _Azure Functions_. Avec son aide, nous pourrons nous connecter et gérer Azure Functions.

![Image](https://i1.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-10.03.00-AM.png?resize=750%2C433&ssl=1)
_Azure Functions dans le Marketplace_

Une fois installée, vous verrez l'icône Azure dans la barre latérale. Lorsque vous cliquez dessus, elle ouvre un panneau avec une option pour _Se connecter à Azure_.

![Image](https://i1.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-10.19.08-AM.png?resize=750%2C846&ssl=1)
_Extension Azure Functions_

Sélectionnez _Se connecter à Azure_, ce qui ouvrira un navigateur où vous pourrez vous connecter avec votre compte. Une fois connecté, vous pouvez revenir à VS Code et voir la liste des Azure Functions dans votre panneau latéral.

![Image](https://i0.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-10.43.07-AM.png?resize=670%2C656&ssl=1)
_Liste des Azure Functions_

Pour moi, il y a quatre applications de fonction. Puisque vous n'en avez peut-être créé qu'une, elle en affichera une. Il est maintenant temps de déployer l'application.

Appuyez sur _F1_ pour ouvrir un menu avec une liste d'actions. Sélectionnez _Azure Functions : Déployer vers Function App..._ ce qui ouvrira une liste d'Azure Functions vers lesquelles vous pouvez déployer. 

Sélectionnez notre nouvelle application Azure Functions. Cela demandera une confirmation, alors allez-y et déployez-la. Cela prendra quelques minutes pour déployer votre application.

## Comment configurer wkhtmltopdf

Une fois que vous avez déployé sur Azure Functions, il reste encore une dernière chose à faire. Nous devons ajouter `libwkhtmltox.so` à un emplacement approprié sur notre application Azure Functions. 

Connectez-vous au portail Azure et accédez à notre application Azure Functions. Dans le panneau latéral, recherchez SSH et cliquez sur le bouton _Go_.

![Image](https://i2.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-12.14.03-PM.png?resize=750%2C219&ssl=1)
_Recherche SSH pour Azure Functions_

Cela ouvrira une console SSH dans un nouvel onglet. Notre site est situé à /home/site/wwwroot. Accédez donc à ce dossier en tapant la commande suivante :

```
cd /home/site/wwwroot/bin
```

Lorsque vous exécutez la commande `ls` pour afficher le contenu du fichier, vous ne verrez pas le fichier `libwkhtmltox.so`. Il est en fait situé à /home/site/wwwroot.

Ce n'est pas la bonne position. Nous devons le copier dans le dossier bin. Pour ce faire, exécutez la commande suivante :

```
cp ../libwkhtmltox.so libwkhtmltox.so
```

Si vous connaissez une meilleure façon d'inclure le fichier dans le dossier bin, faites-le moi savoir.

C'est tout ! Vous avez une application Azure Functions entièrement fonctionnelle. Il est temps de l'appeler depuis notre projet dotnet de démonstration.

## Comment invoquer la fonction Azure

Tout est dit et fait, nous devons encore tester et appeler notre fonction. Avant de le faire, nous devons obtenir le _Code_ qui est nécessaire pour appeler la fonction. 

Le _Code_ est un secret qui doit être inclus pour appeler la fonction de manière sécurisée. Pour obtenir le _Code_, accédez au portail Azure et ouvrez votre application de fonction. Dans le panneau latéral, recherchez _Functions_.

![Image](https://i0.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-12.28.21-PM.png?resize=750%2C418&ssl=1)
_Recherche de fonctions_

Vous verrez _Html2Pdf_ dans la liste. Cliquez sur cette fonction qui ouvrira la vue des détails. Dans le panneau latéral, il y aura une option pour _Function Keys_. Sélectionnez cette option pour voir un _Code_ par défaut masqué déjà ajouté pour vous.

![Image](https://i1.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-12.29.55-PM.png?resize=750%2C374&ssl=1)

Copiez le code et gardez-le à portée de main car nous en aurons besoin dans le code. Pour tester la fonction, j'ai créé une application console d'exemple pour vous. Remplacez l'URL de base et le code comme suit :

```
using System;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Demo.ConsoleApp
{
    public class Program
    {
        public static async Task Main(string[] args)
        {
            string AzureFunctionsUrl = "https://<Your Base Url>/api/Html2Pdf?code=<Replace with your Code>";


            using (HttpClient client = new HttpClient())
            {
                var Request = new Html2PdfRequest
                {
                    HtmlContent = "<h1>Hello World</h1>",
                    PDFFileName = "hello-world.pdf"
                };
                string json = JsonConvert.SerializeObject(Request);
                var buffer = System.Text.Encoding.UTF8.GetBytes(json);
                var byteContent = new ByteArrayContent(buffer);

                byteContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");


                using (HttpResponseMessage res = await client.PostAsync(AzureFunctionsUrl, byteContent))
                {
                    if (res.StatusCode != HttpStatusCode.NoContent)
                    {
                        throw new Exception("There was an error uploading the pdf");
                    }
                }
            }
        }
    }

    public class Html2PdfRequest
    {
        // Le contenu HTML qui doit être converti.
        public string HtmlContent { get; set; }

        // Le nom du fichier PDF à générer
        public string PDFFileName { get; set; }
    }

}
```

Encore une fois, le code devrait être assez explicite. Si vous avez des commentaires ou des questions, faites-le moi savoir. Une fois que vous exécutez l'application console ci-dessus, elle créera un fichier _hello-world.pdf_ dans votre conteneur _pdf_ dans Azure Storage.

## Conclusion

Cela conclut notre tutoriel sur la conversion de HTML en PDF en utilisant Azure Functions. Bien que cela puisse être un peu difficile à configurer, c'est l'une des solutions les moins chères pour passer au serverless. 

Lisez quelques-uns de mes autres articles ici :

* [Apprendre les tests d'intégration dans .NET avec .TDD](https://itnext.io/learn-tdd-with-integration-tests-in-net-5-0-937f126e7220)
* [Fournir un moyen de se connecter sans mot de passe en utilisant .NET](https://www.freecodecamp.org/news/how-to-go-passwordless-with-dotnet-identity/)
* [Comment authentifier et autoriser avec .NET Identity](https://itnext.io/net-5-how-to-authenticate-authorise-apis-correctly-34b09d132d84)
* [Comment accélérer votre site avec Azure CDN](https://www.freecodecamp.org/news/how-to-speed-up-your-website-with-azure-cdn/)