---
title: Comment ajouter le stockage local à vos applications Blazor avec Blazored.LocalStorage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-07-29T13:55:34.000Z'
originalURL: https://freecodecamp.org/news/use-local-storage-in-blazor-apps
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/pexels-pixabay-236698.jpg
tags:
- name: Blazor
  slug: blazor
- name: C
  slug: c
- name: localstorage
  slug: localstorage
- name: .NET
  slug: net
seo_title: Comment ajouter le stockage local à vos applications Blazor avec Blazored.LocalStorage
seo_desc: "By FADAHUNSI SEYI SAMUEL\nOne critical feature of modern web applications\
  \ is their ability to store and retrieve data on the client side. This is where\
  \ local storage comes into play. \nIn this article, we'll explore how to leverage\
  \ the power of the Bla..."
---

Par FADAHUNSI SEYI SAMUEL

Une fonctionnalité critique des applications web modernes est leur capacité à stocker et récupérer des données sur le [côté client](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/). C'est là que le [stockage local](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) entre en jeu. 

Dans cet article, nous explorerons comment tirer parti de la puissance du [package NuGet Blazored LocalStorage](https://www.nuget.org/packages/Blazored.LocalStorage) pour intégrer de manière transparente les capacités de `stockage local` dans vos applications Blazor.

## Table des matières

* [Prérequis](#heading-prerequisites)
* [Comprendre le stockage local](#heading-comprendre-le-stockage-local)
* [Présentation de Blazored.LocalStorage](#heading-presentation-de-blazoredlocalstorage)
* [Avantages de l'utilisation de Blazored.LocalStorage dans les applications Blazor](#heading-avantages-de-lutilisation-de-blazoredlocalstorage-dans-les-applications-blazor)
* [Comment installer Blazored.LocalStorage](#heading-comment-installer-blazoredlocalstorage)
* [Installation avec le gestionnaire de packages NuGet](#heading-installation-avec-le-gestionnaire-de-packages-nuget)
* [Installation avec l'interface de ligne de commande .NET](#heading-installation-avec-linterface-de-ligne-de-commande-net)
* [Comment utiliser Blazored.LocalStorage](#heading-comment-utiliser-blazoredlocalstorage)
* [Fonctionnalités avancées et techniques](#heading-fonctionnalites-avancees-et-techniques)
* [Conclusion](#heading-conclusion)

### Prérequis

Assurez-vous d'avoir les outils nécessaires installés sur votre ordinateur avant de continuer avec ce guide :

* Pour construire et mettre à jour des projets [Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/?view=aspnetcore-8.0), vous aurez besoin de [Visual Studio](https://visualstudio.microsoft.com/downloads/), un environnement de développement intégré (IDE) riche en fonctionnalités que vous pouvez télécharger depuis le site officiel [Microsoft ici](https://visualstudio.microsoft.com/downloads/).
* Le [SDK .NET](https://dotnet.microsoft.com/en-us/download) (Software Development Kit) contient tout ce dont vous avez besoin pour créer et exécuter des applications [.NET](https://dotnet.microsoft.com/en-us/learn/dotnet/what-is-dotnet), et il est requis pour les projets Blazor. Assurez-vous que votre ordinateur a le `.NET SDK` installé.
* Connaissance de base de [C#](https://learn.microsoft.com/en-us/dotnet/csharp/) et de Blazor.

Avec ces outils installés, vous serez prêt à suivre ce guide.

## Comprendre le stockage local

Le stockage local est un mécanisme de stockage de paires `clé-valeur` pris en charge par les navigateurs web modernes. Il offre un moyen simple de stocker des données de manière persistante sur l'appareil de l'utilisateur. Contrairement au `stockage de session`, qui est effacé lorsque la session du navigateur se termine, le `stockage local` reste intact même après la fermeture de la fenêtre du navigateur.

[Blazored.LocalStorage](https://www.nuget.org/packages/Blazored.LocalStorage) est une bibliothèque puissante qui simplifie le travail avec l'API de stockage local du navigateur dans les applications Blazor. Elle fournit une API pratique pour stocker, récupérer et gérer des données dans le stockage local.

En abstraisant les complexités de l'interaction directe avec l'API `localStorage`, ce package offre une interface intuitive et sécurisée. Il vous permet de vous concentrer sur la création d'applications Blazor riches en fonctionnalités sans vous soucier des mécanismes de stockage sous-jacents.

## Présentation de Blazored.LocalStorage

`Blazored.LocalStorage` est une bibliothèque open-source conçue pour fournir une gestion facile et accessible du stockage local dans les applications Blazor. Cette bibliothèque est compatible avec les projets [Blazor WebAssembly](https://www.pragimtech.com/blog/blazor-webAssembly/what-is-blazor-webassembly/) et [Blazor Server](https://www.c-sharpcorner.com/article/understanding-server-side-blazor/). Cela en fait un choix polyvalent pour les développeurs Blazor cherchant à améliorer leurs applications avec des capacités de stockage persistantes côté client.

Au cœur de `Blazored.LocalStorage`, il facilite le stockage et la récupération de données dans le stockage local du navigateur, permettant aux données de persister entre les sessions du navigateur. 

Cela est particulièrement utile pour stocker les préférences de l'utilisateur, l'état de l'application et d'autres données qui doivent persister entre les rechargements de page sans avoir besoin d'une base de données ou d'une solution de stockage backend.


### Avantages de l'utilisation de Blazored.LocalStorage dans les applications Blazor

L'inclusion de `Blazored.LocalStorage` dans les applications Blazor apporte de nombreux avantages, notamment :

* Gestion d'état simplifiée : En utilisant le stockage local, les applications peuvent maintenir l'état plus efficacement entre les sessions utilisateur, améliorant ainsi l'expérience utilisateur.
* Amélioration des performances : Le stockage des données localement réduit le besoin de requêtes fréquentes au serveur, conduisant à des performances d'application plus rapides et à une charge serveur réduite.
* Expérience utilisateur améliorée : Les préférences et les états de l'application peuvent être conservés, ce qui signifie que les utilisateurs n'ont pas besoin de reconfigurer les paramètres ou de perdre leur place dans l'application lors de leur retour.
* Intégration facile : L'API fournie par `Blazored.LocalStorage` est conçue pour être intuitive et simple, garantissant que les développeurs peuvent intégrer les capacités de stockage local dans leurs applications avec un effort minimal.
* Persistance entre les sessions : Contrairement au stockage de session ou au stockage de données en mémoire, le stockage local garantit que les données persistent entre les sessions du navigateur et les fermetures d'onglets, offrant une expérience utilisateur plus cohérente.


## Comment installer Blazored.LocalStorage

L'intégration de `Blazored.LocalStorage` dans votre projet Blazor est simple, avec une prise en charge de l'installation via le `Gestionnaire de packages NuGet` ou l'interface de ligne de commande `.NET CLI`.


### Installation avec le gestionnaire de packages NuGet

En utilisant `Visual Studio`, vous pouvez facilement ajouter `Blazored.LocalStorage` en suivant ces étapes :

* Ouvrez votre projet Blazor dans Visual Studio.
* Accédez à l'"Explorateur de solutions", faites un clic droit sur "Dépendances" et sélectionnez "Gérer les packages NuGet".

![Annotation 2024-04-07 181852](https://hackmd.io/_uploads/S1ckU8ll0.png)

* Dans le gestionnaire de packages NuGet, cliquez sur l'onglet "Parcourir" et recherchez "Blazored.LocalStorage".

![2024-04-07_18-22-49](https://hackmd.io/_uploads/HkBjUUxxC.png)

* Trouvez le package dans la liste, sélectionnez-le et cliquez sur "Installer".

Visual Studio se chargera du reste, ajoutant le package à votre projet ainsi que toutes les dépendances.

### Installation avec l'interface de ligne de commande .NET

Pour ceux qui préfèrent utiliser la ligne de commande ou qui travaillent dans un environnement de développement autre que Visual Studio, l'interface de ligne de commande `.NET CLI` fournit une méthode simple pour ajouter `Blazored.LocalStorage` :

```csharp
dotnet add package Blazored.LocalStorage
```

Exécutez la commande ci-dessus dans votre `terminal` ou `invite de commande` à partir du répertoire racine de votre projet Blazor. Le CLI téléchargera et installera `Blazored.LocalStorage` ainsi que toutes les dépendances nécessaires.


## Comment utiliser Blazored.LocalStorage

Plongeons dans quelques exemples de base de l'utilisation de Blazored.LocalStorage dans une application Blazor.

### Comment enregistrer Blazored.LocalStorage dans votre application Blazor

Nous allons enregistrer `Blazored.LocalStorage` à la racine de l'application, afin qu'il soit disponible pour une utilisation partout dans l'application.

Dans le fichier `program.cs`, qui est notre fichier racine, nous allons enregistrer le service `Blazored.LocalStorage` en faisant ce qui suit :

```csharp
builder.Services.AddBlazoredLocalStorage();
```

L'extrait de code ci-dessus enregistre `Blazored.LocalStorage` dans l'application. Pour que cela fonctionne, assurez-vous d'ajouter le code ci-dessous en haut du fichier `program.cs` :

```csharp
using Blazored.LocalStorage;
```

L'extrait de code ci-dessus garantit que `Blazored.LocalStorage` est importé pour être utilisé dans le fichier. Si vous avez tout ajouté correctement, votre fichier `program.cs` devrait ressembler à ceci :

```csharp
using BlazorApp9.Components;
using Blazored.LocalStorage;

namespace BlazorApp9;

public class Program
{
    public static void Main(string[] args)
    {
        var builder = WebApplication.CreateBuilder(args);

        builder.Services.AddRazorComponents()
            .AddInteractiveServerComponents();

        builder.Services.AddBlazoredLocalStorage();

        var app = builder.Build();

        if (!app.Environment.IsDevelopment())
        {
            app.UseExceptionHandler("/Error");
            app.UseHsts();
        }

        app.UseHttpsRedirection();

        app.UseStaticFiles();
        app.UseAntiforgery();

        app.MapRazorComponents<App>()
            .AddInteractiveServerRenderMode();

        app.Run();
    }
}
```

Le code ci-dessus est le code complet qui doit se trouver dans votre fichier `program.cs`. Avec cela, vous pouvez maintenant utiliser `Blazored.LocalStorage` n'importe où dans l'application pour stocker et recevoir des données.


### Comment stocker et récupérer des données dans Blazored.LocalStorage
 
Considérons un scénario simple où nous voulons stocker et récupérer une donnée en utilisant le stockage local. Nous allons créer une page Blazor avec deux boutons : un pour stocker les données et un autre pour les récupérer.

```csharp
@page "/"

@inject Blazored.LocalStorage.ILocalStorageService localStorage
@rendermode RenderMode.InteractiveServer

<h3>Exemple de stockage local</h3>

<input @bind-value="@inputData" />

<button @onclick="StoreData">Stocker les données</button>
<button @onclick="RetrieveData">Récupérer les données</button>

<p>Les données récupérées du LocalStorage : @storedData </p>

@code {
    private const string dataKey = "localStorageKey";

    private string? storedData;
    private string? inputData;

    private async Task StoreData()
    {
        if(!string.IsNullOrWhiteSpace(inputData))
        {
            await localStorage.SetItemAsync(dataKey, inputData);
            inputData = "";
        }
    }

    protected override async Task OnAfterRenderAsync(bool firstRender)
    {
        if (firstRender)
        {
            await RetrieveData();
        }
    }

    private async Task RetrieveData()
    {
        storedData = await localStorage.GetItemAsync<string>(dataKey);
    }
}
```

Dans l'extrait de code ci-dessus, `@inject Blazored.LocalStorage.ILocalStorageService localStorage` injecte le service de stockage local pour interagir avec le stockage local du navigateur. Le `@rendermode RenderMode.InteractiveServer` spécifie que la page doit être rendue comme un composant interactif côté serveur. Sans le serveur interactif, la page ne sera pas interactive.

Le champ de saisie se lie à `inputData` en utilisant l'attribut `@bind-value`, permettant aux utilisateurs de saisir les données qu'ils souhaitent stocker. La `dataKey` est une variable constante utilisée pour stocker et récupérer des données du stockage local. Les variables `storedData` et `inputData` sont utilisées pour contenir les données à stocker et à récupérer.

La méthode `StoreData` vérifie si `inputData` n'est pas vide. Si ce n'est pas le cas, elle le stocke dans le stockage local en utilisant `dataKey`, et efface le champ de saisie. 

`OnAfterRenderAsync` est déclenché après le premier rendu du composant. Il récupère les données du stockage local pour s'assurer que les données persistent même après le rechargement de la page. 

`RetrieveData` récupère les données du stockage local et les attribue à `storedData` pour affichage.

![2024-04-15_00-52-31 (1) (1) (1) (1)](https://hackmd.io/_uploads/H1DGRAL-0.gif)

La vidéo ci-dessus explique comment stocker et récupérer des données stockées dans le stockage local côté client.

## Fonctionnalités avancées et techniques

Dans cette section, nous allons parler de la manière dont vous pouvez définir une date d'expiration pour vos données, et comment les données stockées peuvent être chiffrées et déchiffrées pour la sécurité.

### Comment gérer l'expiration des données stockées

Pour gérer l'expiration de vos données stockées, vous allez créer une classe d'assistance qui stocke les données avec un horodatage d'expiration. Créez un fichier appelé `StorageItem.cs` qui contiendra le code suivant :

```csharp
public class StorageItem<T>
{
    public required T Data { get; set; }
    public DateTime Expiry { get; set; }
}
```

L'extrait de code ci-dessus est une classe `StorageItem<T>`, qui est une classe générique pouvant contenir des données de n'importe quel type `T` et une date d'expiration `DateTime`. La propriété Data doit être définie lors de la création ou de l'initialisation d'une instance de `StorageItem`, garantissant qu'elle a toujours une valeur valide. La propriété `Expiry` représente la date d'expiration des données stockées.

Ensuite, vous allez créer un fichier qui sera une classe contenant des méthodes pour définir et obtenir des éléments du LocalStorage, avec un temps d'expiration. Créez un fichier appelé `LocalStorageHelper.cs` :

```csharp
using Blazored.LocalStorage;

namespace BlazorApp9.Components.Helpers;

public static class LocalStorageHelper
{
    public static async Task SetItemAsyncWithExpiry<T>(ILocalStorageService localStorageService, string key, TimeSpan expiry, T data)
    {
        StorageItem<T> storageItem = new StorageItem<T>
        {
            Data = data,
            Expiry = DateTime.UtcNow.Add(expiry)
        };

        await localStorageService.SetItemAsync(key, storageItem);
    }

    public static async Task<T?> GetItemAsyncWithExpiry<T>(ILocalStorageService localStorageService, string key)
    {
         var storageItem = await localStorageService.GetItemAsync<StorageItem<T>>(key);

        if(storageItem is null) {
            return default;
        }

        if (storageItem.Expiry < DateTime.UtcNow)
        {
            await localStorageService.RemoveItemAsync(key);
            return default;
        }
        return storageItem.Data;
    }
}
```

Dans le code ci-dessus, vous pouvez voir la directive `using` nécessaire pour la bibliothèque `Blazored.LocalStorage`. Elle fournit un accès facile au stockage local du navigateur depuis les applications Blazor. 

Cela est suivi par la déclaration de l'espace de noms `BlazorApp9.Components.Helpers`. Cela organise le code et indique que cet assistant fait partie des assistants de composants spécifiques dans l'application Blazor.

Ensuite, la classe `LocalStorageHelper` est définie comme une classe `static`. Une classe statique est une classe qui ne peut pas être instanciée et ne peut contenir que des membres statiques (l'utilisation de méthodes ou de propriétés non statiques ne sera pas acceptée). 

Dans la classe `LocalStorageHelper`, deux méthodes `static` asynchrones sont définies : `SetItemAsyncWithExpiry` et `GetItemAsyncWithExpiry`.

La méthode `SetItemAsyncWithExpiry` est responsable du stockage d'un élément dans le stockage local avec un temps d'expiration associé. Elle accepte une instance `ILocalStorageService` pour interagir avec le stockage local, une `clé` `string` pour identifier l'élément stocké, une valeur `TimeSpan` représentant la durée d'expiration, et les données réelles à stocker. 

À l'intérieur de la méthode, un objet `StorageItem<T>` est créé, où `T` est le type de données stockées. Cet objet inclut les données et le temps d'expiration, qui est calculé en ajoutant le `TimeSpan` spécifié à l'heure [UTC](https://www.space.com/what-is-utc.html) actuelle. 

Cet objet `StorageItem` est ensuite sérialisé et sauvegardé dans le stockage local sous la clé donnée en utilisant la méthode `SetItemAsync` de `ILocalStorageService`.

La méthode `GetItemAsyncWithExpiry` est responsable de la récupération d'un élément du stockage local et de la vérification de son expiration. Elle accepte également une instance `ILocalStorageService` et une `clé` `string`. 

Cette méthode tente de récupérer l'objet `StorageItem<T>` stocké en utilisant la `clé`. Si l'élément récupéré est `null`, elle retourne la valeur par défaut pour le type `T` (généralement `null` pour les types de référence et zéro ou équivalent pour les types de valeur). 

Si l'élément est trouvé mais que son temps d'expiration est antérieur à l'heure UTC actuelle, cela signifie que l'élément a expiré. Dans ce cas, l'élément est supprimé du stockage local en utilisant la méthode `RemoveItemAsync` de `ILocalStorageService`, et la méthode retourne la valeur par défaut pour `T`. Si l'élément est valide et n'a pas expiré, la méthode retourne les données stockées.

### Comment implémenter le chiffrement et le déchiffrement

Dans cette section, nous allons explorer un fichier utilitaire qui fournit des fonctionnalités de chiffrement et de déchiffrement pour une application Blazor. 

La classe `EncryptionHelper.cs` inclut des méthodes pour chiffrer et déchiffrer des chaînes, ainsi que des méthodes pour sérialiser des objets en [JSON (JavaScript Object Notation)](https://www.w3schools.com/whatis/whatis_json.asp) et ensuite les chiffrer. Cela garantit que les données sensibles peuvent être stockées et transmises de manière sécurisée. 

Plongeons dans le code pour comprendre comment ces méthodes fonctionnent et comment vous pouvez les utiliser. Ajoutez le code suivant pour ce fichier :

```csharp
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;

namespace BlazorApp9.Components.Helpers;

public static class EncryptionHelper
{
    private static readonly string EncryptionKey = "votre-cle-de-chiffrement";

    private static byte[] GetKeyBytes(string key)
    {

        byte[] keyBytes = Encoding.UTF8.GetBytes(key);
        Array.Resize(ref keyBytes, 32);
        return keyBytes;
    }

    public static string Encrypt(string plainText)
    {
        byte[] iv = new byte[16];
        byte[] array;

        using (Aes aes = Aes.Create())
        {
            aes.Key = GetKeyBytes(EncryptionKey);
            aes.IV = iv;

            ICryptoTransform encryptor = aes.CreateEncryptor(aes.Key, aes.IV);

            using (MemoryStream memoryStream = new MemoryStream())
            {
                using (CryptoStream cryptoStream = new CryptoStream((Stream)memoryStream, encryptor, CryptoStreamMode.Write))
                {
                    using (StreamWriter streamWriter = new StreamWriter((Stream)cryptoStream))
                    {
                        streamWriter.Write(plainText);
                    }

                    array = memoryStream.ToArray();
                }
            }
        }

        return Convert.ToBase64String(array);
    }

    public static string Decrypt(string cipherText)
    {
        byte[] iv = new byte[16];
        byte[] buffer = Convert.FromBase64String(cipherText);

        using (Aes aes = Aes.Create())
        {
            aes.Key = GetKeyBytes(EncryptionKey);
            aes.IV = iv;

            ICryptoTransform decryptor = aes.CreateDecryptor(aes.Key, aes.IV);

            using (MemoryStream memoryStream = new MemoryStream(buffer))
            {
                using (CryptoStream cryptoStream = new CryptoStream((Stream)memoryStream, decryptor, CryptoStreamMode.Read))
                {
                    using (StreamReader streamReader = new StreamReader((Stream)cryptoStream))
                    {
                        return streamReader.ReadToEnd();
                    }
                }
            }
        }
    }

    public static string SerializeAndEncrypt<T>(T data)
    {
        var jsonString = JsonSerializer.Serialize(data);
        return Encrypt(jsonString);
    }

    public static T DecryptAndDeserialize<T>(string cipherText)
    {
        var json = Decrypt(cipherText);
        return JsonSerializer.Deserialize<T>(json);
    }
}
```

La classe `EncryptionHelper` est une classe d'assistance statique conçue pour chiffrer et déchiffrer des données. Cela est particulièrement utile pour sécuriser les informations sensibles dans une application Blazor. 

La classe ci-dessus définit un champ `static` `readonly` `EncryptionKey` qui contient la clé de chiffrement. Cette clé est cruciale pour les processus de chiffrement et de déchiffrement. Il est important d'utiliser une clé forte et stockée de manière sécurisée.

La méthode `GetKeyBytes` convertit la clé de chaîne en un tableau d'octets et garantit que sa longueur est de 32 octets. Cela est dû au fait que [l'algorithme de chiffrement AES](https://www.techtarget.com/searchsecurity/definition/Advanced-Encryption-Standard) nécessite une clé de 256 bits, qui fait 32 octets de long.

La méthode `Encrypt` chiffre une chaîne de `texte en clair` en utilisant le chiffrement `AES`. Elle crée d'abord un vecteur d'initialisation (IV) de 16 octets, qui est requis par l'algorithme `AES`. La méthode configure ensuite un objet `AES` avec la clé de chiffrement et l'IV, et utilise un `CryptoStream` pour écrire les données chiffrées dans un flux mémoire. Ces données chiffrées sont ensuite converties en une chaîne `base64` pour un stockage et une transmission faciles.

La méthode `Decrypt` effectue l'opération inverse. Elle convertit une chaîne `base64` en un tableau d'octets, configure l'objet `AES` avec la même clé et le même IV, et utilise un `CryptoStream` pour lire les données déchiffrées à partir du flux mémoire. Le résultat est la chaîne de texte en clair originale.

La classe `EncryptionHelper` fournit deux méthodes pour gérer les structures de données complexes : `SerializeAndEncrypt` et `DecryptAndDeserialize`. La méthode `SerializeAndEncrypt` sérialise d'abord un objet en une chaîne `JSON` en utilisant `JsonSerializer.Serialize`, puis chiffre cette chaîne `JSON` en utilisant la méthode `Encrypt`. Cela permet de stocker des objets complexes de manière sécurisée dans un format chiffré.

La méthode `DecryptAndDeserialize` déchiffre une chaîne `JSON` chiffrée pour la ramener à sa forme originale, puis la désérialise en un objet de type T en utilisant `JsonSerializer.Deserialize`. Cette combinaison de déchiffrement et de désérialisation garantit que les données complexes peuvent être récupérées et utilisées de manière sécurisée au sein de l'application.


### Comment connecter l'expiration et le chiffrement à l'interface utilisateur

Maintenant, nous allons passer en revue un composant Blazor (`Home.razor`) qui permet aux utilisateurs de stocker et de récupérer des données chiffrées dans le stockage local du navigateur. Cela garantit que les informations sensibles sont protégées et expirent automatiquement lorsqu'elles ne sont plus nécessaires. 

Cette approche combine la facilité du stockage local avec la sécurité du chiffrement, offrant une solution robuste pour gérer les données utilisateur dans les applications web. Plongeons dans le code pour voir comment cela fonctionne.

```csharp
 @page "/"
@using BlazorApp9.Components.Helpers

@inject Blazored.LocalStorage.ILocalStorageService localStorage
@rendermode RenderMode.InteractiveServer

<h3>Exemple de stockage local</h3>

<input @bind-value="@inputData" />

<button @onclick="StoreData">Stocker les données</button>
<button @onclick="RetrieveData">Récupérer les données</button>

<p>Les données récupérées du LocalStorage : @storedData </p>

@code {
    private const string dataKey = "localStorageKey";

    private string? storedData;
    private string? inputData;

    bool isDataLoaded = false;

    private async Task StoreData()
    {
        if (!string.IsNullOrWhiteSpace(inputData))
        {
            string encryptData = EncryptionHelper.SerializeAndEncrypt(inputData);
            await LocalStorageHelper.SetItemAsyncWithExpiry(localStorage, dataKey, TimeSpan.FromMinutes(30), encryptData);
            inputData = "";
        }
    }

    protected override async Task OnAfterRenderAsync(bool firstRender)
    {
        if (firstRender && !isDataLoaded)
        {
            await RetrieveData();
            isDataLoaded = true;
            StateHasChanged();
        }
    }

    private async Task RetrieveData()
    {
        string encryptData = await LocalStorageHelper.GetItemAsyncWithExpiry<string>(localStorage, dataKey);
        storedData = encryptData != null ? EncryptionHelper.DecryptAndDeserialize<string>(encryptData) : "Données non trouvées ou expirées.";
    }
}
```

Dans le code ci-dessus, la méthode `StoreData` vérifie si `inputData` est valide, le chiffre en utilisant `EncryptionHelper.SerializeAndEncrypt`, et le stocke dans le stockage local avec une expiration de trente minutes en utilisant `LocalStorageHelper.SetItemAsyncWithExpiry`. Le champ de saisie est ensuite effacé.

La méthode `OnAfterRenderAsync` récupère les données du stockage local après le rendu initial du composant. Cela garantit que les données précédemment stockées sont chargées lorsque la page s'affiche pour la première fois. Elle s'exécute une fois, définissant `isDataLoaded` sur vrai et appelant `StateHasChanged` pour mettre à jour l'interface utilisateur (UI).

La méthode `RetrieveData` récupère les données du stockage local en utilisant `LocalStorageHelper.GetItemAsyncWithExpiry`. Si les données sont trouvées et valides, elle les déchiffre et les désérialise en utilisant `EncryptionHelper.DecryptAndDeserialize`. Si ce n'est pas le cas, elle définit `storedData` sur "`Données non trouvées ou expirées.`"

![2024-05-30_11-18-37 (1) (2) (1)](https://hackmd.io/_uploads/BJRDqJUNR.gif)

La vidéo ci-dessus démontre comment vous pouvez implémenter les concepts discutés dans ce guide dans une application web.

## Conclusion

`Blazored.LocalStorage` offre une solution puissante et facile à utiliser pour gérer les informations utilisateur dans les applications Blazor. Son intégration apporte de nombreux avantages, notamment une gestion d'état améliorée, des performances accrues et une meilleure expérience utilisateur.

Après avoir lu cet article et essayé le code par vous-même, vous devriez être en mesure d'incorporer des capacités de stockage local dans n'importe quel projet Blazor. Cela vous aidera à déverrouiller tout le potentiel du stockage côté client dans vos applications web.