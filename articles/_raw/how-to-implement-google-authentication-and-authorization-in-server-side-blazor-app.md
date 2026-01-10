---
title: How to Implement Google Authentication and Authorization in a Server-Side Blazor
  App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-11T06:13:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-google-authentication-and-authorization-in-server-side-blazor-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca187740569d1a4ca4f1d.jpg
tags:
- name: authentication
  slug: authentication
- name: autherization
  slug: autherization
- name: Blazor
  slug: blazor
- name: Google
  slug: google
seo_title: null
seo_desc: 'By Ankit Sharma

  Introduction

  The latest preview for .NET Core 3 (preview-6) has introduced the functionality
  to add authentication and authorization in a server-side Blazor application. In
  this article, we will learn how to implement authentication a...'
---

By Ankit Sharma

## **Introduction**

The latest preview for .NET Core 3 (preview-6) has introduced the functionality to add authentication and authorization in a server-side Blazor application. In this article, we will learn how to implement authentication and authorization using Google in a server-side Blazor application. You can refer to my previous article [Understanding Server-side Blazor](https://ankitsharmablogs.com/understanding-server-side-blazor/) to get in-depth knowledge on server-side Blazor.

## **Prerequisites**

* Install the latest .NET Core 3.0 Preview SDK from [here](https://dotnet.microsoft.com/download/dotnet-core/3.0).
* Install the latest preview of Visual Studio 2019 from [here](https://visualstudio.com/preview).
* Install ASP.NET Core Blazor Language Services extension from [here](https://go.microsoft.com/fwlink/?linkid=870389).

## **Source Code**

Get the source code from [GitHub](https://github.com/AnkitSharma-007/Google-Authentication-with-server-side-Blazor)

## **Create Server Side Blazor Application**

To create a server-side Blazor app, open Visual Studio 2019 and follow the steps mentioned below.

1. Click on “Create a new project”.
2. Select “ASP.NET Core Web Application” from available project types. Click on Next.
3. A new “Configure your new project” screen will open. Put the name of the project as `BlazorGoogleAuth` and click Create.
4. In the next screen, select “.NET Core” and “ASP.NET Core 3.0” from dropdowns on the top left.
5. Select “Blazor (server-side)” from the list of available templates.
6. Click on Change Authentication button, a “Change Authentication” dialog box will open. Select “Individual User Account” and click OK. Click on `Create` button to create the application.

These steps are shown in the GIF image below.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/BlazorGoogleAuth.gif)

Before running the application, we need to apply migrations to our app. Navigate to Tools >> NuGet Package Manager >> Package Manager Console.

It will open the Package Manager Console. Put in `Update-Database` command and hit enter. This will update the database using Entity Framework Code First Migrations.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/DBrestore.png)

Open project properties by right clicking on the project in solution explorer and select properties. Select Debug from left side menu then scroll to the bottom of the page. Note the SSL enabled URL. In this case, the URL is `https://localhost:44327/`. We need this URL to configure the Google API Console project which we will be doing in our next section. Refer to the image below:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/ProjectProperties.png)

## **Create a Google API Console project**

We need to create a Google API console project and obtain a client ID and client secret to configure the Google authentication in our application.

Navigate to [https://developers.google.com/identity/sign-in/web/sign-in#before_you_begin](https://developers.google.com/identity/sign-in/web/sign-in#before_you_begin). Login with your Google account. Follow the steps mentioned below.

1. Click on “Configure a Project” button.
2. A “Configure a project for Google Sign-in” dialog box will open asking you to select or create a new project.
3. Select “Create a new project” from the dropdown. Name your project “BlazorAuthDemo” and click on Next.
4. In the “Configure your OAuth client” screen, put your product name. You can use any name of your choice. Here we will put “BlazorAuth” as the product name.
5. In the next screen, select “Web server” from the “Where are you calling from” dropdown.
6. It will then ask you to put the “Authorized redirect URIs”. Give the base URL of your application with `/signin-google` appended to it. For this tutorial, the URL will be `https://localhost:44327/signin-google`.
7. Click on Create. The dialog box will now prompt you with the client ID and client secret. Make a note of `ClientId` and `ClientSecret` field. We will need these values to configure Google authentication in our web app

Refer to the GIF below for a better understanding.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/GoogleAuthProject.gif)

> * Do not use the word “Google” in your product name. You will be prompted with an error and you will not be allowed to create the app. This means “BlazorGoogleAuth” is an invalid project name.
> * Project names must be between 4 and 30 characters and may only contain letters, numbers, spaces, and hyphens.

## **Installing Google authentication middleware NuGet package**

To configure the ASP.NET Core middleware for Google authentication we need to install the `Microsoft.AspNetCore.Authentication.Google` nuget package in our application. The version of this nuget package must match the version of .NET Core 3 which we are using in our project.

Open [https://www.nuget.org/packages/Microsoft.AspNetCore.Authentication.Google/](https://www.nuget.org/packages/Microsoft.AspNetCore.Authentication.Google/). Select the version of .NET Core 3 from the “Version History”. Copy the command from the “package manager” tab. Run this command in the NuGet package manager console of our application.

For this application, we are using `.NET Core 3.0.0-preview6.19307.2`. Therefore, we will run the following command in the package manager console of our application.

```
Install-Package Microsoft.AspNetCore.Authentication.Google -Version 3.0.0-preview6.19307.2
```

Refer to the image below:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/NugetInstall.png)

## **Configure the server-side Blazor app to use Google authentication**

We need to store `ClientId` and `ClientSecret` field values in our application. We will use Secret Manager tool for this purpose. The Secret Manager tool is a project tool that can be used to store secrets such as password, API Key, etc. for a .NET Core project during the development process. With the Secret Manager tool, we can associate app secrets with a specific project and can share them across multiple projects.

Open our web application once again and Right-click the project in the Solution Explorer. Select Manage User Secrets from the context menu. A `secrets.json` file will open. Put the following code in it.

```
{
  "Authentication:Google:ClientId": "Your Google ClientId here",
  "Authentication:Google:ClientSecret": "Your Google ClientSecret here"
}
```

Now open `Startup.cs` file and put the following code into `ConfigureServices` method.

```
services.AddAuthentication().AddGoogle(googleOptions =>
{
  googleOptions.ClientId = Configuration["Authentication:Google:ClientId"];
  googleOptions.ClientSecret = Configuration["Authentication:Google:ClientSecret"];
});
```

This code will read the `ClientId` and `ClientSecret` from the `secrets.json` file. The `AddGoogle()`method is an extension method and it is used to configure the Google Authentication options for our application.

## **Adding authorization to Blazor pages**

Blazor has added a new built-in component called `AuthorizeView`, which is used to display different content based on the authentication state of the application. This component will display the child component only when the user is authorized.  The `AuthorizeView` component is configured in `\Shared\LoginDisplay.razor` file.

To implement authorization to a specific page, we need to use the `[Authorize]` attribute. Blazor has introduced a new directive `@attribute`, which is used to include the `[Authorize]` attribute for a page. In this application, we will apply `[Authorize]` to the FetchData component. This will prohibit unauthorized access to this component. Open `FetchData.razor` page and add the following lines at the top of the page.

```
@using Microsoft.AspNetCore.Authorization
@attribute [Authorize]
```

## **Execution Demo**

Launch the application. Navigate to Fetch Data component by clicking on the “Fetch data” link on the menu on the left. You will see a “Not authorized” message displayed on the screen. Click “Log In” on the menu at the top. In the next page click on the “Google” button to login with Google. Once you are logged in successfully, you will be able to access the Fetch Data component.

Refer to the GIF below for a better understanding.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/BlazorGoogleauthExecution.gif)

## **Conclusion**

We learned how to implement Google authentication and authorization in a server-side Blazor application. We have created and configured a Google API console project to implement Google authentication. To implement authorization for a specific component in Blazor, we have used the [Authorize] attribute. We have used `Microsoft.AspNetCore.Authentication.Google` nuget package to configure the middleware for Google authentication.

Please get the source code from [GitHub](https://github.com/AnkitSharma-007/Google-Authentication-with-server-side-Blazor) and play around to get a better understanding.

Get my book [Blazor Quick Start Guide](https://amzn.to/2OToEji) to learn more about Blazor.

Preparing for interviews !!! Read my article on [C# Coding Questions For Technical Interviews](https://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/)

## **See Also**

* [BlazorGrid – A Reusable Grid Component For Blazor](https://ankitsharmablogs.com/blazorgrid-reusable-grid-component-for-blazor/)
* [Publishing A Blazor Component To Nuget Gallery](https://ankitsharmablogs.com/publishing-blazor-component-to-nuget-gallery/)
* [Deploying A Blazor Application On Azure](https://ankitsharmablogs.com/deploying-a-blazor-application-on-azure/)
* [Hosting A Blazor Application on Firebase](https://ankitsharmablogs.com/hosting-a-blazor-application-on-firebase/)
* [Blazor CRUD Using Google Cloud Firestore](https://ankitsharmablogs.com/blazor-crud-using-google-cloud-firestore/)
* [CRUD Using Blazor with MongoDB](https://ankitsharmablogs.com/crud-using-blazor-with-mongodb/)
* [Single Page Application Using Server-Side Blazor](https://ankitsharmablogs.com/single-page-application-using-server-side-blazor/)

_Originally published at [https://ankitsharmablogs.com/google-authentication-and-authorization-in-server-side-blazor-app/](https://ankitsharmablogs.com/google-authentication-and-authorization-in-server-side-blazor-app/)_

