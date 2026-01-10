---
title: Comment implémenter Azure Serverless avec Blazor WebAssembly
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-06T13:32:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-azure-serverless-with-blazor-web-assembly
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99da740569d1a4ca220f.jpg
tags:
- name: Azure
  slug: azure
- name: Azure Functions
  slug: azure-functions
- name: Blazor
  slug: blazor
- name: C#
  slug: csharp
seo_title: Comment implémenter Azure Serverless avec Blazor WebAssembly
seo_desc: "By Ankit Sharma\nIntroduction\nIn this article, we will learn how to implement\
  \ Azure serverless with Blazor web assembly. And to do that, we will create an app\
  \ that lists out some Frequently Asked Questions (FAQ) on Covid-19. \nHere's what\
  \ we will cover..."
---

Par Ankit Sharma

## **Introduction**

Dans cet article, nous allons apprendre comment implémenter Azure serverless avec Blazor WebAssembly. Pour cela, nous allons créer une application qui liste quelques questions fréquemment posées (FAQ) sur le Covid-19. 

Voici ce que nous allons couvrir :

* Nous allons créer une base de données Azure Cosmos DB qui servira de base de données principale pour stocker les questions et les réponses. 
* Nous allons utiliser une application Azure Function pour récupérer les données de Cosmos DB. 
* Nous allons déployer l'application de fonction sur Azure pour l'exposer globalement via un point de terminaison API. 
* Et enfin, nous allons consommer l'API dans une application Blazor WebAssembly. 

Les FAQ seront affichées dans une disposition de carte à l'aide de Bootstrap.

L'application Covid-19 FAQ est déployée sur Azure. Voir son fonctionnement à l'adresse [https://covid19-faq.azurewebsites.net/](https://covid19-faq.azurewebsites.net/)

## **Qu'est-ce qu'une architecture serverless ?**

Dans les applications traditionnelles telles qu'une application à 3 niveaux, un client demande des ressources au serveur, et le serveur traite la demande et répond avec les données appropriées.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ServerArchi.png)

Cependant, il y a quelques problèmes avec cette architecture. Nous avons besoin d'un serveur qui fonctionne en continu. Même s'il n'y a pas de demandes, le serveur est présent 24h/24 et 7j/7, prêt à traiter la demande. Maintenir la disponibilité du serveur est coûteux. 

Un autre problème est l'évolutivité. Si le trafic est énorme, nous devons mettre à l'échelle tous les serveurs, ce qui peut être un processus fastidieux.

Une solution efficace à ce problème est l'architecture web serverless. Le client fait une demande à un compte de stockage de fichiers au lieu d'un serveur. Le compte de stockage renvoie la page `index.html` ainsi que du code qui doit être rendu dans le navigateur. 

Puisqu'il n'y a pas de serveur pour rendre la page, nous nous appuyons sur le navigateur pour rendre la page. Toute la logique pour dessiner l'élément ou mettre à jour l'élément s'exécutera dans le navigateur. Nous n'avons aucun serveur en backend – nous avons simplement un compte de stockage avec un actif statique.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ServerLessArchi.png)

C'est une solution rentable car nous n'avons aucun serveur, juste quelques fichiers statiques dans un compte de stockage. Il est également très facile de mettre à l'échelle pour les sites web à forte charge.

## **Qu'est-ce qu'une fonction Azure ?**

Faire fonctionner le navigateur avec toute la logique pour rendre la page semble excitant, mais cela a quelques limitations. 

Nous ne voulons pas que le navigateur effectue des appels à la base de données. Nous avons besoin d'une partie de notre code pour s'exécuter côté serveur, comme la connexion à une base de données. 

C'est là que les fonctions Azure sont utiles. Dans une architecture serverless, si nous voulons qu'une partie du code s'exécute côté serveur, nous utilisons une fonction Azure.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ServerLessArchiAZFunc.png)

Les fonctions Azure sont une plateforme de calcul serverless basée sur les événements. Vous ne payez que lorsque l'exécution a lieu. Elles sont également faciles à mettre à l'échelle. Ainsi, nous obtenons à la fois les avantages de l'évolutivité et du coût avec les fonctions Azure. 

Pour en savoir plus, vous pouvez consulter la [documentation officielle des fonctions Azure](https://azure.microsoft.com/en-in/services/functions/).

## **Pourquoi devriez-vous utiliser Azure serverless ?**

Une solution Azure serverless peut ajouter de la valeur à votre produit en minimisant le temps et les ressources que vous consacrez aux exigences liées à l'infrastructure. 

Vous pouvez augmenter la productivité des développeurs, optimiser les ressources et accélérer le temps de mise sur le marché avec l'aide d'une solution Azure serverless entièrement gérée et de bout en bout.

Pour en savoir plus, consultez la [documentation officielle d'Azure serverless](https://azure.microsoft.com/en-in/solutions/serverless/).

## **Qu'est-ce que Blazor ?**

Blazor est un framework web .NET pour créer des applications côté client en utilisant C#/Razor et HTML. 

Blazor s'exécute dans le navigateur avec l'aide de [WebAssembly](http://webassembly.org/). Il peut simplifier le processus de création d'une application monopage (SPA). Il offre également une expérience de développement web full-stack en utilisant .NET.

L'utilisation de .NET pour développer des applications côté client présente plusieurs avantages :

* .NET offre une gamme d'API et d'outils sur toutes les plateformes qui sont stables et faciles à utiliser.
* Les langages modernes tels que C# et F# offrent de nombreuses fonctionnalités qui rendent la programmation plus facile et plus intéressante pour les développeurs.
* La disponibilité de l'un des meilleurs IDE sous la forme de Visual Studio offre une excellente expérience de développement .NET sur plusieurs plateformes telles que Windows, Linux et macOS.
* .NET fournit des fonctionnalités telles que la vitesse, la performance, la sécurité, l'évolutivité et la fiabilité dans le développement web qui facilitent le développement full-stack.

## **Pourquoi devriez-vous utiliser Blazor ?**

Blazor prend en charge une large gamme de fonctionnalités pour faciliter le développement web. Certaines des fonctionnalités les plus importantes de Blazor sont :

* **Architecture basée sur les composants** : Blazor nous fournit une architecture basée sur les composants pour créer des interfaces utilisateur riches et composables.
* **Injection de dépendances** : Cela nous permet d'utiliser des services en les injectant dans les composants.
* **Dispositions** : Nous pouvons partager des éléments d'interface utilisateur communs (par exemple, des menus) entre les pages à l'aide de la fonctionnalité de dispositions.
* **Routage** : Nous pouvons rediriger la demande du client d'un composant à un autre à l'aide du routage.
* **Interopérabilité JavaScript** : Cela nous permet d'invoquer une méthode C# à partir de JavaScript, et nous pouvons appeler une fonction ou une API JavaScript à partir du code C#.
* **Globalisation et localisation** : L'application peut être rendue accessible aux utilisateurs dans plusieurs cultures et langues.
* **Rechargement en direct** : Rechargement en direct de l'application dans le navigateur pendant le développement.
* **Déploiement** : Nous pouvons déployer l'application Blazor sur IIS et Azure Cloud.

Pour en savoir plus sur Blazor, veuillez consulter la [documentation officielle de Blazor](http://blazor.net/).

## **Prérequis**

Pour commencer avec l'application, nous devons remplir ces prérequis :

* Un compte d'abonnement Azure. Vous pouvez créer un compte Azure gratuit à l'adresse [https://azure.microsoft.com/en-in/free/](https://azure.microsoft.com/en-in/free/)
* Installez la dernière version de Visual Studio 2019 à partir de [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)

Lors de l'installation de VS 2019, assurez-vous de sélectionner la charge de travail de développement Azure et ASP.NET et le développement web.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/VSInstall.png)

## **Code Source**

Vous pouvez obtenir le code source à partir de [GitHub ici](https://github.com/AnkitSharma-007/azure-serverless-with-blazor).

## **Créer un compte Azure Cosmos DB**

Connectez-vous au portail Azure et recherchez "Azure Cosmos DB" dans la barre de recherche, puis cliquez sur le résultat. Sur l'écran suivant, cliquez sur le bouton Ajouter. 

Cela ouvrira une page "Créer un compte Azure Cosmos DB". Vous devez remplir les informations requises pour créer votre base de données. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateCosmosDBAccount.png)

Vous pouvez remplir les détails comme suit :

* **Abonnement** : Sélectionnez le nom de votre abonnement Azure dans la liste déroulante.
* **Groupe de ressources** : Sélectionnez un groupe de ressources existant ou créez-en un nouveau.
* **Nom du compte** : Entrez un nom unique pour votre compte Azure Cosmos DB. Le nom ne peut contenir que des lettres minuscules, des chiffres et le caractère -, et doit comporter entre 3 et 44 caractères.
* **API** : Sélectionnez Core (SQL)
* **Emplacement** : Sélectionnez un emplacement pour héberger votre compte Azure Cosmos DB.

Conservez les autres champs à leur valeur par défaut et cliquez sur le bouton "Vérifier + Créer". Dans l'écran suivant, passez en revue toutes vos configurations et cliquez sur le bouton "Créer". Après quelques minutes, le compte Azure Cosmos DB sera créé. Cliquez sur "Aller à la ressource" pour accéder à la page du compte Azure Cosmos DB.

## **Configurer la base de données**

Sur la page du compte Azure Cosmos DB, cliquez sur "Explorateur de données" dans la navigation de gauche, puis sélectionnez "Nouveau conteneur". Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateContainer.png)

Un volet "Ajouter un conteneur" s'ouvrira. Vous devez remplir les détails pour créer un nouveau conteneur pour votre Azure Cosmos DB. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ConfigureContainer.png)

Vous pouvez remplir les détails comme indiqué ci-dessous.

* **ID de la base de données** : Vous pouvez donner n'importe quel nom à votre base de données. Ici, j'utilise FAQDB.
* **Débit** : Laissez-le à la valeur par défaut de 400
* **ID du conteneur** : Entrez le nom de votre conteneur. Ici, j'utilise FAQContainer.
* **Clé de partition** : La clé de partition est utilisée pour partitionner automatiquement les données entre plusieurs serveurs pour l'évolutivité. Mettez la valeur à /id.

Cliquez sur le bouton "OK" pour créer la base de données.

## **Ajouter des données d'exemple à Cosmos DB**

Dans l'Explorateur de données, développez la base de données FAQDB, puis développez le conteneur FAQContainer. Sélectionnez Éléments, puis cliquez sur Nouveau élément en haut. Un éditeur s'ouvrira sur le côté droit de la page. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/AddItem.png)

Placez les données JSON suivantes dans l'éditeur et cliquez sur le bouton Enregistrer en haut.

```json
{
    "id": "1",
    "question": "Qu'est-ce que le coronavirus ?",
    "answer": "Les coronavirus sont une grande famille de virus qui peuvent provoquer des maladies chez les animaux ou les humains. Le coronavirus récemment découvert provoque la maladie à coronavirus COVID-19."
}

```

Nous avons ajouté un ensemble de questions et de réponses avec un identifiant unique.

Suivez le processus décrit ci-dessus pour insérer cinq autres ensembles de données.

```json
{
    "id": "2",
    "question": "Qu'est-ce que le COVID-19 ?",
    "answer": "Le COVID-19 est la maladie infectieuse causée par le coronavirus récemment découvert. Ce nouveau virus et cette maladie étaient inconnus avant le début de l'épidémie à Wuhan, en Chine, en décembre 2019."
}
{
    "id": "3",
    "question": "Quels sont les symptômes du COVID-19 ?",
    "answer": "Les symptômes les plus courants du COVID-19 sont la fièvre, la fatigue et la toux sèche. Certains patients peuvent avoir des douleurs, une congestion nasale, un écoulement nasal, un mal de gorge ou une diarrhée. Ces symptômes sont généralement légers et commencent progressivement. Certaines personnes deviennent infectées mais ne développent aucun symptôme et ne se sentent pas malades."
}
{
    "id": "4",
    "question": "Comment le COVID-19 se propage-t-il ?",
    "answer": "Les personnes peuvent attraper le COVID-19 d'autres personnes qui ont le virus. La maladie peut se propager d'une personne à l'autre par de petites gouttelettes du nez ou de la bouche qui sont propagées lorsqu'une personne atteinte de COVID-19 tousse ou expire. Ces gouttelettes se déposent sur les objets et les surfaces autour de la personne. D'autres personnes attrapent ensuite le COVID-19 en touchant ces objets ou surfaces, puis en touchant leurs yeux, leur nez ou leur bouche."
}
{
    "id": "5",
    "question": "Que puis-je faire pour me protéger et prévenir la propagation de la maladie ?",
    "answer": "Vous pouvez réduire vos chances d'être infecté ou de propager le COVID-19 en prenant quelques précautions simples. Nettoyez régulièrement et soigneusement vos mains avec une solution hydroalcoolique ou lavez-les avec du savon et de l'eau. Maintenez une distance d'au moins 1 mètre (3 pieds) entre vous et toute personne qui tousse ou éternue. Assurez-vous que vous et les personnes autour de vous suivez une bonne hygiène respiratoire. Cela signifie couvrir votre bouche et votre nez avec votre coude plié ou un mouchoir lorsque vous toussez ou éternuez. Restez à la maison si vous ne vous sentez pas bien. Si vous avez de la fièvre, de la toux et des difficultés à respirer, cherchez une attention médicale et appelez à l'avance."
}
{
    "id": "6",
    "question": "Les antibiotiques sont-ils efficaces pour prévenir ou traiter le COVID-19 ?",
    "answer": "Non. Les antibiotiques n'agissent pas contre les virus, ils n'agissent que sur les infections bactériennes. Le COVID-19 est causé par un virus, donc les antibiotiques n'agissent pas."
}

```

## **Obtenir la chaîne de connexion**

Cliquez sur "clés" dans la navigation de gauche, accédez à l'onglet "Clés de lecture-écriture". La valeur sous `PRIMARY CONNECTION STRING` est notre chaîne de connexion requise. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CosmosDBContString.png)

Notez la valeur de `PRIMARY CONNECTION STRING`. Nous l'utiliserons dans la partie suivante de cet article, lorsque nous accéderons à Azure Cosmos DB à partir d'une fonction Azure.

## **Créer une application de fonction Azure**

Ouvrez Visual Studio 2019, cliquez sur "Créer un nouveau projet". Recherchez "Functions" dans la boîte de recherche. Sélectionnez le modèle Azure Functions et cliquez sur Suivant. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateAzFunction.png)

Dans la fenêtre "Configurer votre nouveau projet", entrez un nom de projet comme `FAQFunctionApp`. Cliquez sur le bouton Créer. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateAzFunction_1.png)

Une nouvelle fenêtre "Créer une nouvelle application Azure Function" s'ouvrira. Sélectionnez "Azure Functions v3 (.NET Core)" dans la liste déroulante en haut. Sélectionnez le modèle de fonction comme "HTTP trigger". Définissez le niveau d'autorisation sur "Anonyme" dans la liste déroulante à droite. Cliquez sur le bouton Créer pour créer le projet de fonction et la fonction de déclenchement HTTP. 

Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateAzFunction_2.png)

## **Installer le package pour Azure Cosmos DB**

Pour permettre à l'application Azure Function de se lier à Azure Cosmos DB, nous devons installer le package `Microsoft.Azure.WebJobs.Extensions.CosmosDB`. Accédez à Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages et exécutez la commande suivante :

```
Install-Package Microsoft.Azure.WebJobs.Extensions.CosmosDB

```

Reportez-vous à l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/InstallNuget.png)

Vous pouvez en savoir plus sur ce package à la [galerie NuGet](https://www.nuget.org/packages/Microsoft.Azure.WebJobs.Extensions.CosmosDB).

## **Configurer l'application Azure Function**

Le projet Azure Function contient un fichier par défaut appelé `Function1.cs`. Vous pouvez supprimer ce fichier en toute sécurité car nous ne l'utiliserons pas pour notre projet.

Faites un clic droit sur le projet `FAQFunctionApp` et sélectionnez Ajouter >> Nouveau dossier. Nommez le dossier Models. Ensuite, faites un clic droit sur le dossier Models et sélectionnez Ajouter >> Classe pour ajouter un nouveau fichier de classe. Donnez le nom de votre classe comme `FAQ.cs` et cliquez sur Ajouter.

Ouvrez `[FAQ.cs](https://github.com/AnkitSharma-007/azure-serverless-with-blazor/blob/master/FAQFunctionApp/FAQFunctionApp/Models/FAQ.cs)` et placez le code suivant à l'intérieur.

```c#
namespace FAQFunctionApp.Models
{
    class FAQ
    {
        public string Id { get; set; }
        public string Question { get; set; }
        public string Answer { get; set; }
    }
}

```

La classe a la même structure que les données JSON que nous avons insérées dans la base de données Cosmos.

Faites un clic droit sur le projet `FAQFunctionApp` et sélectionnez Ajouter >> Classe. Nommez votre classe comme `[CovidFAQ.cs](https://github.com/AnkitSharma-007/azure-serverless-with-blazor/blob/master/FAQFunctionApp/FAQFunctionApp/CovidFAQ.cs)`. Placez le code suivant à l'intérieur.

```c#
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Microsoft.Azure.WebJobs;
using FAQFunctionApp.Models;
using Microsoft.Azure.WebJobs.Extensions.Http;
using System.Threading.Tasks;

namespace FAQFunctionApp
{
    class CovidFAQ
    {
        [FunctionName("covidFAQ")]
        public static async Task<IActionResult> Run(
        [HttpTrigger(AuthorizationLevel.Anonymous, "get", Route = null)] HttpRequest req,
        [CosmosDB(
            databaseName:"FAQDB",
            collectionName:"FAQContainer",
            ConnectionStringSetting = "DBConnectionString"
            )] IEnumerable<FAQ> questionSet, 
        ILogger log)
        {
            log.LogInformation("Data fetched from FAQContainer");
            return new OkObjectResult(questionSet);
        }
    }
}

```

Nous avons créé une classe `CovidFAQ` et ajouté une fonction Azure à celle-ci. L'attribut `FunctionName` est utilisé pour spécifier le nom de la fonction. Nous avons utilisé l'attribut `HttpTrigger` qui permet à la fonction d'être déclenchée via un appel HTTP. L'attribut `CosmosDB` est utilisé pour se connecter à Azure Cosmos DB. Nous avons défini trois paramètres pour cet attribut comme décrit ci-dessous :

* **databaseName** : le nom de la base de données Cosmos DB
* **collectionName** : la collection à l'intérieur de la base de données Cosmos DB que nous voulons accéder
* **ConnectionStringSetting** : la chaîne de connexion pour se connecter à Cosmos DB. Nous allons la configurer dans la section suivante.

Nous avons décoré le paramètre `questionSet`, qui est de type `IEnumerable<FAQ>` avec l'attribut `CosmosDB`. Lorsque l'application est exécutée, le paramètre `questionSet` sera rempli avec les données de Cosmos DB. La fonction retournera les données en utilisant une nouvelle instance de `OkObjectResult`.

## **Ajouter la chaîne de connexion à l'application Azure Function**

Vous vous souvenez de la chaîne de connexion Azure Cosmos DB que vous avez notée précédemment ? Maintenant, nous allons la configurer pour notre application. Ouvrez le fichier `local.settings.json` et ajoutez votre chaîne de connexion comme indiqué ci-dessous :

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "dotnet",
    "DBConnectionString": "votre chaîne de connexion"
  }
}

```

> Le fichier local.settings.json ne sera pas publié sur Azure lorsque nous publierons l'application Azure Function. Par conséquent, nous devons configurer la chaîne de connexion séparément lors de la publication de l'application sur Azure. Nous verrons cela en action dans la partie suivante de cet article.

## **Tester la fonction Azure localement**

Appuyez sur F5 pour exécuter la fonction. Copiez l'URL de votre fonction à partir de la sortie d'exécution des fonctions Azure. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ExecuteLocal-1.png)

Ouvrez le navigateur et collez l'URL dans la barre d'adresse du navigateur. Vous pouvez voir la sortie comme indiqué ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ExecuteLocal-2.png)

Ici, vous pouvez voir les données que nous avons insérées dans notre base de données Azure Cosmos DB.

## **Publier l'application de fonction sur Azure**

Nous avons créé avec succès l'application de fonction, mais elle s'exécute toujours en localhost. Publions l'application pour la rendre disponible globalement.

Faites un clic droit sur le projet `FAQFunctionApp` et sélectionnez Publier. Sélectionnez la cible de publication comme Azure.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/DeploytoAZ_1.png)

Sélectionnez la cible spécifique comme "Azure Function App (windows)".

![Image](https://www.freecodecamp.org/news/content/images/2020/07/DeploytoAZ_2.png)

Dans la fenêtre suivante, cliquez sur le bouton "Créer une nouvelle fonction Azure...". Une nouvelle fenêtre d'application de fonction s'ouvrira. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/DeploytoAZ_3.png)

Vous pouvez remplir les détails comme indiqué ci-dessous :

* **Nom** : Un nom globalement unique pour votre application de fonction.
* **Abonnement** : Sélectionnez le nom de votre abonnement Azure dans la liste déroulante.
* **Groupe de ressources** : Sélectionnez un groupe de ressources existant ou créez-en un nouveau.
* **Type de plan** : Sélectionnez Consommation. Cela garantira que vous ne payez que pour les exécutions de votre application de fonctions.
* **Emplacement** : Sélectionnez un emplacement pour votre fonction.
* **Stockage Azure** : Conservez la valeur par défaut.

Cliquez sur le bouton "Créer" pour créer l'application de fonction et revenir à la fenêtre précédente. Assurez-vous que l'option "Exécuter à partir du fichier package" est cochée. Cliquez sur le bouton Terminer.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/DeploytoAZ_4.png)

Vous êtes maintenant sur la page de publication. Cliquez sur le bouton "Gérer les paramètres du service d'application Azure".

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ManageAZappSetting.png)

Vous verrez une fenêtre "Paramètres de l'application" comme indiqué ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/SetConnString.png)

À ce stade, nous allons configurer la valeur distante pour la clé "DBConnectionString". Cette valeur est utilisée lorsque l'application est déployée sur Azure. Puisque la clé pour les environnements local et distant est la même dans notre cas, cliquez sur le bouton "Insérer la valeur depuis le local" pour copier la valeur du champ local vers le champ distant. Cliquez sur le bouton OK.

Vous êtes redirigé vers la page de publication. Nous avons terminé toutes les configurations. Cliquez sur le bouton Publier pour publier votre application de fonction Azure. Après la publication de l'application, obtenez la valeur de l'URL du site, ajoutez `/api/covidFAQ` à celle-ci et ouvrez-la dans le navigateur. Vous pouvez voir la sortie comme indiqué ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ExecuteGlobally.png)

Il s'agit du même ensemble de données que nous avons obtenu lors de l'exécution de l'application localement. Cela prouve que notre fonction Azure serverless est déployée et capable d'accéder à Azure Cosmos DB avec succès.

## **Activer CORS pour le service d'application Azure**

Nous allons utiliser l'application de fonction dans un projet d'interface utilisateur Blazor. Pour permettre à l'application Blazor d'accéder à la fonction Azure, nous devons activer CORS pour le service d'application Azure.

Ouvrez le portail Azure. Accédez à "Toutes les ressources". Ici, vous pouvez voir le service d'application que nous avons créé lors de la publication de l'application dans la section précédente. Cliquez sur la ressource pour accéder à la page de la ressource. Cliquez sur CORS dans la navigation de gauche. Un volet de détails CORS s'ouvrira.

Nous avons maintenant deux options ici :

1. Entrez l'URL d'origine spécifique pour leur permettre de faire des appels cross-origin.
2. Supprimez toutes les URL d'origine de la liste et utilisez le caractère générique "*" pour permettre à toutes les URL de faire des appels cross-origin.

Nous utiliserons la deuxième option pour notre application. Supprimez toutes les URL précédemment listées et entrez une seule entrée comme caractère générique "*" . Cliquez sur le bouton Enregistrer en haut. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/AZFuncCors.png)

## **Créer le projet Blazor WebAssembly**

Ouvrez Visual Studio 2019, cliquez sur "Créer un nouveau projet". Sélectionnez "Application Blazor" et cliquez sur le bouton "Suivant". Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateBlazorProj_1.png)

Dans la fenêtre "Configurer votre nouveau projet", mettez le nom du projet comme `FAQUIApp` et cliquez sur le bouton "Créer" comme indiqué dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateBlazorProj_2.png)

Dans la fenêtre "Créer une nouvelle application Blazor", sélectionnez le modèle "Application Blazor WebAssembly". Cliquez sur le bouton Créer pour créer le projet. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateBlazorProj_3.png)

Pour créer un nouveau composant Razor, faites un clic droit sur le dossier Pages, sélectionnez Ajouter >> Composant Razor. Une boîte de dialogue "Ajouter un nouvel élément" s'ouvrira, mettez le nom de votre composant comme `CovidFAQ.razor` et cliquez sur le bouton Ajouter. Reportez-vous à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateRazorComp.png)

Ouvrez `[CovidFAQ.razor](https://github.com/AnkitSharma-007/azure-serverless-with-blazor/blob/master/FAQUIApp/FAQUIApp/Pages/CovidFAQ.razor)` et placez le code suivant à l'intérieur.

```
@page "/covidfaq"
@inject HttpClient Http

<div class="d-flex justify-content-center">
    <img src="../Images/COVID_banner.jpg" alt="Image" style="width:80%; height:300px" />
</div>
<br />
<div class="d-flex justify-content-center">
    <h1>Questions fréquemment posées sur le Covid-19</h1>
</div>
<hr />

@if (questionList == null)
{
    <p><em>Chargement...</em></p>
}
else
{
    @foreach (var question in questionList)
    {
        <div class="card">
            <h3 class="card-header">
                @question.Question
            </h3>
            <div class="card-body">
                <p class="card-text">@question.Answer</p>
            </div>
        </div>
        <br />
    }
}

@code {

    private FAQ[] questionList;

    protected override async Task OnInitializedAsync()
    {
        questionList = await Http.GetFromJsonAsync<FAQ[]>("https://faqfunctionapp20200611160123.azurewebsites.net/api/covidFAQ");
    }

    public class FAQ
    {
        public string Id { get; set; }
        public string Question { get; set; }
        public string Answer { get; set; }
    }
}

```

Dans la section `@code`, nous avons créé une classe appelée FAQ. La structure de cette classe est la même que celle de la classe FAQ que nous avons créée précédemment dans l'application de fonction Azure. À l'intérieur de la méthode `OnInitializedAsync`, nous appelons le point de terminaison de l'API de notre application de fonction. Les données retournées par l'API seront stockées dans une variable appelée `questionList` qui est un tableau de type `FAQ`.

Dans la section HTML de la page, nous avons défini une image de bannière en haut de la page. L'image est disponible dans le dossier `/wwwroot/Images`. Nous allons utiliser une boucle foreach pour itérer sur le tableau `questionList` et créer une carte Bootstrap pour afficher la question et la réponse.

## **Ajout de lien au menu de navigation**

La dernière étape consiste à ajouter le lien de notre composant CovidFAQ dans le menu de navigation. Ouvrez le fichier `[/Shared/NavMenu.razor](https://github.com/AnkitSharma-007/azure-serverless-with-blazor/blob/master/FAQUIApp/FAQUIApp/Shared/NavMenu.razor#L15-L19)` et ajoutez le code suivant à l'intérieur.

```html
<li class="nav-item px-3">
  <NavLink class="nav-link" href="covidfaq">
    <span class="oi oi-plus" aria-hidden="true"></span> Covid FAQ
  </NavLink>
</li>

```

Supprimez les liens de navigation pour les composants Counter et Fetch-data car ils ne sont pas nécessaires pour cette application.

## **Démonstration d'exécution**

Appuyez sur F5 pour lancer l'application. Cliquez sur le bouton Covid FAQ dans le menu de navigation à gauche. Vous pouvez voir toutes les questions et réponses dans une belle disposition de carte comme indiqué ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/BlazorExecution.png)

Vous pouvez également vérifier l'application en direct à l'adresse [https://covid19-faq.azurewebsites.net/](https://covid19-faq.azurewebsites.net/)

## **Résumé**

Dans cet article, nous avons appris ce qu'est le serverless et ses avantages par rapport à l'architecture web traditionnelle à trois niveaux. Nous avons également appris comment la fonction Azure s'intègre dans l'architecture web serverless. 

Pour démontrer la mise en œuvre pratique de ces concepts, nous avons créé une application FAQ sur le Covid-19 en utilisant Blazor WebAssembly et Azure serverless. Les questions et réponses sont affichées dans une disposition de carte en utilisant Bootstrap. 

Nous avons utilisé Azure Cosmos DB comme base de données principale pour stocker les questions et réponses de notre application FAQ. Une fonction Azure est utilisée pour récupérer les données de Cosmos DB. Nous avons déployé l'application de fonction sur Azure pour la rendre disponible globalement via un point de terminaison API.

## **Voir aussi**

* [Lecteur de caractères optiques utilisant Blazor et la vision par ordinateur](https://ankitsharmablogs.com/optical-character-reader-using-blazor-and-computer-vision/)
* [Traduction multilingue utilisant Blazor et les services cognitifs Azure](https://ankitsharmablogs.com/multi-language-translator-using-blazor-and-azure-cognitive-services/)
* [Authentification et autorisation Facebook dans une application Blazor côté serveur](https://ankitsharmablogs.com/facebook-authentication-and-authorization-in-server-side-blazor-app/)
* [Déploiement continu pour une application Angular utilisant Heroku et GitHub](https://ankitsharmablogs.com/continuous-deployment-for-angular-app-using-heroku-and-github/)
* [Authentification et autorisation Google dans une application Blazor côté serveur](https://ankitsharmablogs.com/google-authentication-and-authorization-in-server-side-blazor-app/)
* [CRUD Blazor utilisant Google Cloud Firestore](https://ankitsharmablogs.com/blazor-crud-using-google-cloud-firestore/)

Si vous aimez l'article, partagez-le avec vos amis. Vous pouvez également me contacter sur [Twitter](https://twitter.com/ankitsharma_007) et [LinkedIn](https://www.linkedin.com/in/ankitsharma-007/).

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)