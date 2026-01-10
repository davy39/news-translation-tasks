---
title: How to Add Local Storage to Your Blazor Apps with Blazored.LocalStorage
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
seo_title: null
seo_desc: "By FADAHUNSI SEYI SAMUEL\nOne critical feature of modern web applications\
  \ is their ability to store and retrieve data on the client side. This is where\
  \ local storage comes into play. \nIn this article, we'll explore how to leverage\
  \ the power of the Bla..."
---

By FADAHUNSI SEYI SAMUEL

One critical feature of modern web applications is their ability to store and retrieve data on the [client side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/). This is where [local storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) comes into play. 

In this article, we'll explore how to leverage the power of the [Blazored LocalStorage NuGet package](https://www.nuget.org/packages/Blazored.LocalStorage) to seamlessly integrate `local storage` capabilities into your Blazor applications.

## Table of Contents

* [Prerequisites](#heading-prerequisites)
* [Understanding Local Storage](#heading-understanding-local-storage)
* [Introducing Blazored.LocalStorage](#heading-introducing-blazoredlocalstorage)
* [Advantages of Using Blazored.LocalStorage in Blazor Applications](#heading-advantages-of-using-blazoredlocalstorage-in-blazor-applications)
* [How to Install Blazored.LocalStorage](#heading-how-to-install-blazoredlocalstorage)
* [Install Using Nuget Package Manager](#heading-install-using-the-nuget-package-manager)
* [Install Using the .NET CLI](#heading-install-using-the-net-cli)
* [How to Use Blazored.LocalStorage](#heading-how-to-use-blazoredlocalstorage)
* [Advanced Features and Techniques](#heading-advanced-features-and-techniques)
* [Conclusion](#heading-conclusion)

### Prerequisites

Make sure you have the necessary tools installed on your computer before continuing with this guide:

* To build and update [Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/?view=aspnetcore-8.0) projects, you'll need [Visual Studio](https://visualstudio.microsoft.com/downloads/), a feature-rich Integrated Development Environment (IDE) which you can download from the official [Microsoft website here](https://visualstudio.microsoft.com/downloads/).
* The [.NET SDK](https://dotnet.microsoft.com/en-us/download) (Software Development Kit) has everything you need to create and execute [.NET](https://dotnet.microsoft.com/en-us/learn/dotnet/what-is-dotnet) apps, and it's required for Blazor projects. Make sure your computer has the `.NET SDK` installed.
* Basic knowledge of [C#](https://learn.microsoft.com/en-us/dotnet/csharp/) and Blazor.

With these installed, will be ready to follow along.

## Understanding Local Storage

Local storage is a `key-value` pair storage mechanism supported by modern web browsers. It provides a simple way to store data persistently on the user's device. Unlike `session storage`, which is cleared when the browser session ends, `local storage` remains intact even after closing the browser window.

[Blazored.LocalStorage](https://www.nuget.org/packages/Blazored.LocalStorage) is a powerful library that simplifies working with the browser's local storage `API` (Application Programming Interface) within Blazor applications. It provides a convenient `API` for storing, retrieving, and managing data in local storage.

By abstracting away the complexities of directly interacting with the `localStorage` API, this package provides an intuitive and type-safe interface. It lets you focus on building feature-rich Blazor applications without worrying about the underlying storage mechanisms.

## Introducing Blazored.LocalStorage

`Blazored.LocalStorage` is an open-source library designed to provide easy and accessible local storage management in Blazor applications. This library is compatible with both [Blazor WebAssembly](https://www.pragimtech.com/blog/blazor-webAssembly/what-is-blazor-webassembly/) and [Blazor Server](https://www.c-sharpcorner.com/article/understanding-server-side-blazor/) projects. This makes it a versatile choice for Blazor developers looking to enhance their applications with persistent, client-side storage capabilities.

At its core, `Blazored.LocalStorage` facilitates the storage and retrieval of data in the browser's local storage, allowing data to persist across browser sessions. 

This is particularly useful for storing user preferences, application state, and other data that needs to persist between page reloads without the need for a database or backend storage solution.


### Advantages of Using Blazored.LocalStorage in Blazor Applications

The inclusion of `Blazored.LocalStorage` in Blazor applications comes with a host of benefits, including:

* Simplified State Management: By leveraging local storage, applications can maintain state more effectively across user sessions, enhancing the user experience.
* Performance Improvements: Storing data locally reduces the need for frequent server requests, leading to faster application performance and reduced server load.
* Enhanced User Experience: Preferences and application states can be preserved, meaning users do not need to reconfigure settings or lose their place in the application upon returning.
* Easy Integration: The `API` provided by `Blazored.LocalStorage` is designed to be intuitive and straightforward, ensuring that developers can integrate local storage capabilities into their applications with minimal effort.
* Cross-Session Persistence: Unlike session storage or in-memory data storage, local storage ensures that data persists across browser sessions and tab closures, providing a more consistent user experience.


## How to Install Blazored.LocalStorage

Integrating `Blazored.LocalStorage` into your Blazor project is straightforward, with support for installation via the `NuGet Package Manager` or the `.NET CLI` (Command Line Interpreter).


### Install Using the NuGet Package Manager

Using `Visual Studio`, you can easily add `Blazored.LocalStorage` by following these steps:

* Open your Blazor project in Visual Studio.
* Navigate to the “Solution Explorer”, right-click on "Dependencies", and select “Manage NuGet Packages”.

![Annotation 2024-04-07 181852](https://hackmd.io/_uploads/S1ckU8ll0.png)

* In the NuGet Package Manager, click on the “Browse” tab and search for “Blazored.LocalStorage”.

![2024-04-07_18-22-49](https://hackmd.io/_uploads/HkBjUUxxC.png)

* Find the package in the list, select it, and click “Install”.

Visual Studio will handle the rest, adding the package to your project along with any dependencies.

### Install Using the .NET CLI

For those who prefer using the command line or are working within a development environment other than Visual Studio, the `.NET CLI` provides a simple method to add `Blazored.LocalStorage`:

```csharp
dotnet add package Blazored.LocalStorage
```

Run the command above in your `terminal` or `command prompt` from the root directory of your Blazor project. The CLI will download and install `Blazored.LocalStorage` along with any necessary dependencies.


## How to Use Blazored.LocalStorage

Let's dive into some basic examples of using Blazored.LocalStorage in a Blazor application.

### How to Register Blazored.LocalStorage in your Blazor Application

We will register`Blazored.LocalStorage` into the root of the application, so that it will be available to use everywhere in the application.

In the `program.cs` file, which is our root file, we will register the `Blazored.LocalStorage` service by doing the following:

```csharp
builder.Services.AddBlazoredLocalStorage();
```

The code snippet above registers the `Blazored.LocalStorage` into the application. For this to work, make sure you add the code below to the top of the `program.cs` file:

```csharp
using Blazored.LocalStorage;
```

The code snippet above makes sure that the `Blazored.LocalStorage` is being imported to be used in the file. If you've added everything correctly, your `program.cs` file should look like this:

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

The above is the full code that should be in your `program.cs` file. With this, you can now use `Blazored.LocalStorage` anywhere in the application to store and receive data.


### How to Store and Retrieve Data in Blazored.LocalStorage
 
Let's consider a simple scenario where we want to store and retrieve a piece of data using local storage. We'll create a Blazor page with two buttons: one to store data and another to retrieve it.

```csharp
@page "/"

@inject Blazored.LocalStorage.ILocalStorageService localStorage
@rendermode RenderMode.InteractiveServer

<h3>Local Storage Example</h3>

<input @bind-value="@inputData" />

<button @onclick="StoreData">Store Data</button>
<button @onclick="RetrieveData">Retrieve Data</button>

<p>The retrieved data from the LocalStorage: @storedData </p>

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

In the code snippet above, the `@inject Blazored.LocalStorage.ILocalStorageService localStorage` injects the local storage service to interact with the browser's local storage. The `@rendermode RenderMode.InteractiveServer` specifies that the page should be rendered as an interactive server-side component. Without the interactive server, the page will not be interactive.

The input field binds to `inputData` using the `@bind-value` attribute, allowing users to enter data they wish to store. The `dataKey` is a constant variable used to store and retrieve data from local storage. The `storedData` and `inputData` variables are used to hold the data to be stored and retrieved.

The `StoreData` method checks to see if `inputData` is not empty. If not, it stores it in local storage using `dataKey`, and clears the input field. 

`OnAfterRenderAsync` is triggered after the component's first render. It retrieves data from local storage to ensure that data persists even after the page is reloaded. 

`RetrieveData` retrieves data from local storage and assigns it to `storedData` for display.

![2024-04-15_00-52-31 (1) (1) (1) (1)](https://hackmd.io/_uploads/H1DGRAL-0.gif)

The video above explains how to store and retrieve data stored in localstorage on the client-side.

## Advanced Features and Techniques

In this section, we'll talk about how you can set an expiration date on your data, and how the stored data can be encrypted and decrypted for security.

### How to Manage the Expiration of Stored Data

To manage the expiration of your stored data, you will create a helper class that stores data along with an expiration timestamp. Create a file called `StorageItem.cs` which will contain the code below:

```csharp
public class StorageItem<T>
{
    public required T Data { get; set; }
    public DateTime Expiry { get; set; }
}
```

The code snippet above is a `StorageItem<T>` class, which is a generic class that can hold data of any type `T` and an expiry date `DateTime`. The Data property is required to be set when an instance of `StorageItem` is created or initialized, ensuring that it always has a valid value. The `Expiry` property represents the expiration date of the stored data.

Next, you'll create a file which will be a class that contains methods to set and get from the LocalStorage, with an expiration time. Create a file called `LocalStorageHelper.cs`:

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

In the code above, you can see the necessary `using` directive for the `Blazored.LocalStorage` library. It provides easy access to the browser's local storage from Blazor applications. 

This is followed by the declaration of the namespace `BlazorApp9.Components.Helpers`. This organizes the code and indicates that this helper is part of a specific component's helpers within the Blazor application.

Next, the `LocalStorageHelper` class is defined as a `static` class. A static class is one that cannot be instantiated and can only contain static members (using non static methods or properties will not be accepted). 

Within the `LocalStorageHelper` class, two `static` asynchronous methods are defined: `SetItemAsyncWithExpiry` and `GetItemAsyncWithExpiry`.

The `SetItemAsyncWithExpiry` method is responsible for storing an item in the local storage with an associated expiry time. It accepts an `ILocalStorageService` instance for interacting with local storage, a `key` `string` to identify the stored item, a `TimeSpan` value representing the expiry duration, and the actual data to be stored. 

Inside the method, a `StorageItem<T>` object is created, where `T` is the type of data being stored. This object includes the data and the expiry time, which is calculated by adding the specified `TimeSpan` to the current [UTC time](https://www.space.com/what-is-utc.html). 

This `StorageItem` object is then serialized and saved in local storage under the given key using the `SetItemAsync` method of `ILocalStorageService`.

The `GetItemAsyncWithExpiry` method is responsible for retrieving an item from local storage and checking if it has expired. It also accepts an `ILocalStorageService` instance and a `key` `string`. 

This method attempts to retrieve the stored `StorageItem<T>` object using the `key`. If the retrieved item is `null`, it returns the default value for the type `T` (typically `null` for reference types and zero or equivalent for value types). 

If the item is found but its expiry time is earlier than the current UTC time, it means the item has expired. In this case, the item is removed from the local storage using the `RemoveItemAsync` method of `ILocalStorageService`, and the method returns the default value for `T`. If the item is valid and has not expired, the method returns the stored data.

### How to Implement Encryption and Decryption

In this section, we will explore a utility file that provides encryption and decryption functionalities for a Blazor application. 

The `EncryptionHelper.cs` class includes methods for encrypting and decrypting strings, as well as methods for serializing objects to [JSON (Javascript Object Notation)](https://www.w3schools.com/whatis/whatis_json.asp) and then encrypting them. This ensures that sensitive data can be securely stored and transmitted. 

Let’s dive into the code to understand how these methods work and how you can use them. Add the following code for this file:

```csharp
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;

namespace BlazorApp9.Components.Helpers;

public static class EncryptionHelper
{
    private static readonly string EncryptionKey = "your-encryption-key";

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

The `EncryptionHelper` class is a static helper class designed for encrypting and decrypting data. This is particularly useful for securing sensitive information in a Blazor application. 

The class above defines a `static` `readonly` field `EncryptionKey` which holds the encryption key. This key is crucial for both the encryption and decryption processes. It's important to use a strong and securely stored key.

The `GetKeyBytes` method converts the string key into a byte array and ensures its length is 32 bytes. This is because [the AES encryption](https://www.techtarget.com/searchsecurity/definition/Advanced-Encryption-Standard) algorithm requires a 256-bit key, which is 32 bytes long.

The `Encrypt` method encrypts a `plaintext` string using `AES` encryption. It first creates an initialization vector (IV) of 16 bytes, which is required by the `AES` algorithm. The method then sets up an `AES` object with the encryption key and IV, and uses a `CryptoStream` to write the encrypted data to a memory stream. This encrypted data is then converted to a `base64` string for easy storage and transmission.

The `Decrypt` method performs the reverse operation. It converts a `base64` string back to a byte array, sets up the `AES` object with the same key and IV, and uses a `CryptoStream` to read the decrypted data from the memory stream. The result is the original plaintext string.

The `EncryptionHelper` class provides two methods for handling complex data structures: `SerializeAndEncrypt` and `DecryptAndDeserialize`. The `SerializeAndEncrypt` method first serializes an object to a `JSON` string using `JsonSerializer.Serialize`, and then encrypts this `JSON` string using the `Encrypt` method. This allows complex objects to be securely stored in an encrypted format.

The `DecryptAndDeserialize` method decrypts an encrypted `JSON` string back into its original form and then deserializes it into an object of type T using `JsonSerializer.Deserialize`. This combination of decryption and deserialization ensures that complex data can be securely retrieved and used within the application.


### How to Connect the Expiration and Encryption to the User Interface

Now we'll walk through a Blazor component (`Home.razor`) that allows users to store and retrieve encrypted data in the browser's local storage. This ensures that sensitive information is protected and automatically expires when no longer needed. 

This approach combines the ease of local storage with the security of encryption, providing a robust solution for managing user data in web applications. Let's dive into the code to see how it works.

```csharp
 @page "/"
@using BlazorApp9.Components.Helpers

@inject Blazored.LocalStorage.ILocalStorageService localStorage
@rendermode RenderMode.InteractiveServer

<h3>Local Storage Example</h3>

<input @bind-value="@inputData" />

<button @onclick="StoreData">Store Data</button>
<button @onclick="RetrieveData">Retrieve Data</button>

<p>The retrieved data from the LocalStorage: @storedData </p>

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
        storedData = encryptData != null ? EncryptionHelper.DecryptAndDeserialize<string>(encryptData) : "Data not found or expired.";
    }
}
```

In the code above, the `StoreData` method checks if `inputData` is valid, encrypts it using `EncryptionHelper.SerializeAndEncrypt`, and stores it in local storage with a thirty-minute expiry using `LocalStorageHelper.SetItemAsyncWithExpiry`. The input field is then cleared.

The `OnAfterRenderAsync` method retrieves data from local storage after the component's initial render. This ensures previously stored data is loaded when the page first displays. It runs once, setting `isDataLoaded` to true and calling `StateHasChanged` to update the user interface (UI).

The `RetrieveData` method fetches data from local storage using `LocalStorageHelper.GetItemAsyncWithExpiry`. If the data is found and valid, it decrypts and deserializes it using `EncryptionHelper.DecryptAndDeserialize`. If not, it sets `storedData` to "`Data not found or expired.`"

![2024-05-30_11-18-37 (1) (2) (1)](https://hackmd.io/_uploads/BJRDqJUNR.gif)

The video above demonstrates how you can implement the concepts discussed in this guide in a web application.

## Conclusion

`Blazored.LocalStorage` offers a powerful and easy-to-use solution for managing user information in Blazor applications. Its integration brings numerous benefits, including enhanced state management, improved performance, and a better user experience.

After reading through this article and trying out the code for yourself, you should be able to incorporate local storage capabilities into any Blazor project. This will help you unlock the full potential of client-side storage in your web applications.


