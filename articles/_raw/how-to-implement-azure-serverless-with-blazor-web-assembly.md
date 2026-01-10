---
title: How to Implement Azure Serverless with Blazor WebAssembly
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
seo_title: null
seo_desc: "By Ankit Sharma\nIntroduction\nIn this article, we will learn how to implement\
  \ Azure serverless with Blazor web assembly. And to do that, we will create an app\
  \ that lists out some Frequently Asked Questions (FAQ) on Covid-19. \nHere's what\
  \ we will cover..."
---

By Ankit Sharma

## **Introduction**

In this article, we will learn how to implement Azure serverless with Blazor web assembly. And to do that, we will create an app that lists out some Frequently Asked Questions (FAQ) on Covid-19. 

Here's what we will cover:

* We will create an Azure Cosmos DB which will act as our primary database to store questions and answers. 
* We will use an Azure function app to fetch data from cosmos DB. 
* We will deploy the function app to Azure to expose it globally via an API endpoint. 
* And lastly, we will consume the API in a Blazor web assembly app. 

The FAQs will be displayed in a card layout with the help of Bootstrap.

The Covid-19 FAQ app is deployed on Azure. See it in action at [https://covid19-faq.azurewebsites.net/](https://covid19-faq.azurewebsites.net/)

## **What is a serverless architecture?**

In traditional applications such as a 3-tier app, a client requests resources from the server, and the server processes the request and responds with the appropriate data.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ServerArchi.png)

However, there are some issues with this architecture. We need a server running continuously. Even if there are no requests, the server is present 24X7, ready to process the request. Maintaining server availability is cost-intensive. 

Another problem is scaling. If the traffic is huge, we need to scale out all the servers which can be a cumbersome process.

An effective solution to this problem is serverless web architecture. The client makes a request to a file storage account instead of a server. The storage account returns the `index.html` page along with some code that needs to be rendered on the browser. 

Since there is no server to render the page, we are relying on the browser to render the page. All the logic to draw the element or update the element will run in the browser. We do not have any server on backend – we just have a storage account with a static asset.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ServerLessArchi.png)

This is a cost-effective solution as we do not have any server, just some static files in a storage account. It is also very easy to scale out for heavy load websites.

## **What is an Azure function?**

Making the browser run all the logic to render the page seems exciting, but it has some limitations. 

We do not want the browser to make database calls. We need some part of our code to run on the server-side such as connecting to a database. 

This is where Azure functions come in handy. In a serverless architecture, if we want some code to run the server-side, then we use an Azure function.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ServerLessArchiAZFunc.png)

Azure functions are an event-driven serverless compute platform. You need to pay only when execution happens. They are also easy to scale. Hence, we get both the scaling and the cost benefits with Azure functions. 

To learn more you can refer to the [Azure function official docs](https://azure.microsoft.com/en-in/services/functions/).

## **Why should you use Azure serverless?**

An Azure serverless solution can add value to your product by minimizing the time and resources you spend on infrastructure-related requirements. 

You can increase developer productivity, optimize resources and accelerate the time to market with the help of a fully managed, end-to-end Azure serverless solution.

To learn more, see the [Azure serverless official doc](https://azure.microsoft.com/en-in/solutions/serverless/).

## **What is Blazor?**

Blazor is a .NET web framework for creating client-side applications using C#/Razor and HTML. 

Blazor runs in the browser with the help of [WebAssembly](http://webassembly.org/). It can simplify the process of creating a single page application (SPA). It also provides a full-stack web development experience using .NET.

Using .NET for developing Client-side application has multiple advantages:

* .NET offers a range of API and tools across all platforms that are stable and easy to use.
* The modern languages such as C# and F# offer a lot of features that make programming easier and interesting for developers.
* The availability of one of the best IDE in the form of Visual Studio provides a great .NET development experience across multiple platforms such as Windows, Linux, and macOS.
* .NET provides features such as speed, performance, security, scalability, and reliability in web development that makes full-stack development easier.

## **Why should you use Blazor?**

Blazor supports a wide array of features to make web development easier for us. Some of the prominent features of Blazor are:

* **Component-based architecture**: Blazor provides us with a component-based architecture to create rich and composable UI.
* **Dependency injection**: This allows us to use services by injecting them into components.
* **Layouts**: We can share common UI elements (for example, menus) across pages using the layouts feature.
* **Routing**: We can redirect the client request from one component to another with the help of routing.
* **JavaScript interop**: This allows us to invoke a C# method from JavaScript, and we can call a JavaScript function or API from C# code.
* **Globalization and localization**: The application can be made accessible to users in multiple cultures and languages
* **Live reloading**: Live reloading of the app in the browser during development.
* **Deployment**: We can deploy the Blazor application on IIS and Azure Cloud.

To learn more about Blazor, please refer to the [official Blazor docs](http://blazor.net/).

## **Prerequisites**

To get started with the application, we need to fulfill these prerequisites:

* An Azure subscription account. You can create a free Azure account at [https://azure.microsoft.com/en-in/free/](https://azure.microsoft.com/en-in/free/)
* Install the latest version of Visual Studio 2019 from [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)

While installing the VS 2019, please make sure you select the Azure development and ASP.NET and web development workload.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/VSInstall.png)

## **Source Code**

You can get the source code from [GitHub here](https://github.com/AnkitSharma-007/azure-serverless-with-blazor).

## **Create Azure Cosmos DB account**

Log in to the Azure portal and search for the “Azure Cosmos DB” in the search bar and click on the result. On the next screen, click on the Add button. 

This will open a “Create Azure Cosmos DB Account” page. You need to fill in the required information to create your database. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateCosmosDBAccount.png)

You can fill in the details like this:

* **Subscription**: Select your Azure subscription name from the drop-down.
* **Resource Group**: Select an existing Resource Group or create a new one.
* **Account Name**: Enter a unique name for your Azure Cosmos DB account. The name can contain only lowercase letters, numbers, and the ‘-‘ character, and must be between 3 and 44 characters.
* **API**: Select Core (SQL)
* **Location**: Select a location to host your Azure Cosmos DB account.

Keep the other fields to its default value and click on the “Review+ Create” button. In the next screen, review all your configurations and click on the “Create” button. After a few minutes, the Azure Cosmos DB account will be created. Click on “Go to resource” to navigate to the Azure Cosmos DB account page.

## **Set up the Database**

On the Azure Cosmos DB account page, click on “Data Explorer” on the left navigation, and then select “New Container”. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateContainer.png)

An “Add Container” pane will open. You need to fill in the details to create a new container for your Azure Cosmos DB. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ConfigureContainer.png)

You can fill in the details as indicated below.

* **Database ID:** You can give any name to your database. Here I am using FAQDB.
* **Throughput:** Keep it at the default value of 400
* **Container ID:** Enter the name for your container. Here I am using FAQContainer.
* **Partition key:** The Partition key is used to automatically partition data among multiple servers for scalability. Put the value as “/id”.

Click on the “OK” button to create the database.

## **Add Sample data to the Cosmos DB**

In the Data Explorer, expand the FAQDB database then expand the FAQContainer. Select Items, and then click on New Item on the top. An editor will open on the right side of the page. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/AddItem.png)

Put the following JSON data in the editor and click on the Save button at the top.

```json
{
    "id": "1",
    "question": "What is corona virus?",
    "answer": "Corona viruses are a large family of viruses which may cause illness in animals or humans. The most recently discovered coronavirus causes coronavirus disease COVID-19."
}

```

We have added a set of questions and answer along with a unique id.

Follow the process described above to insert five more sets of data.

```json
{
    "id": "2",
    "question": "What is COVID-19?",
    "answer": "COVID-19 is the infectious disease caused by the most recently discovered corona virus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019."
}
{
    "id": "3",
    "question": "What are the symptoms of COVID-19?",
    "answer": "The most common symptoms of COVID-19 are fever, tiredness, and dry cough. Some patients may have aches and pains, nasal congestion, runny nose, sore throat or diarrhea. These symptoms are usually mild and begin gradually. Some people become infected but don’t develop any symptoms and don't feel unwell."
}
{
    "id": "4",
    "question": "How does COVID-19 spread?",
    "answer": "People can catch COVID-19 from others who have the virus. The disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with COVID-19 coughs or exhales. These droplets land on objects and surfaces around the person. Other people then catch COVID-19 by touching these objects or surfaces, then touching their eyes, nose or mouth."
}
{
    "id": "5",
    "question": "What can I do to protect myself and prevent the spread of disease?",
    "answer": "You can reduce your chances of being infected or spreading COVID-19 by taking some simple precaution. Regularly and thoroughly clean your hands with an alcoholbased hand rub or wash them with soap and water. Maintain at least 1 metre (3 feet) distance between yourself and anyone who is coughing or sneezing. Make sure you, and the people around you, follow good respiratory hygiene. This means covering your mouth and nose with your bent elbow or tissue when you cough or sneeze. Stay home if you feel unwell. If you have a fever, cough and difficulty breathing, seek medical attention and call in advance."
}
{
    "id": "6",
    "question": "Are antibiotics effective in preventing or treating the COVID-19?",
    "answer": "No. Antibiotics do not work against viruses, they only work on bacterial infections. COVID-19 is caused by a virus, so antibiotics do not work."
}

```

## **Get the connection string**

Click on “keys” on the left navigation, navigate to the “Read-write Keys” tab. The value under `PRIMARY CONNECTION STRING` is our required connection string. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CosmosDBContString.png)

Make a note of the `PRIMARY CONNECTION STRING` value. We will use it in the latter part of this article, when we will access the Azure Cosmos DB from an Azure function.

## **Create an Azure function app**

Open Visual Studio 2019, click on “Create a new project”. Search “Functions” in the search box. Select the Azure Functions template and click on Next. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateAzFunction.png)

In “Configure your new project” window, enter a Project name as `FAQFunctionApp`. Click on the Create button. Refer to the image below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateAzFunction_1.png)

A new “Create a new Azure Function Application settings” window will open. Select “Azure Functions v3 (.NET Core)”from the dropdown at the top. Select the function template as “HTTP trigger”. Set the authorization level to “Anonymous” from the drop-down on the right. Click on the Create button to create the function project and HTTP trigger function. 

Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateAzFunction_2.png)

## **Install package for Azure Cosmos DB**

To enable the Azure function App to bind to the Azure Cosmos DB, we need to install the `Microsoft.Azure.WebJobs.Extensions.CosmosDB` package. Navigate to Tools >> NuGet Package Manager >> Package Manager Console and run the following command:

```
Install-Package Microsoft.Azure.WebJobs.Extensions.CosmosDB

```

Refer to the image shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/InstallNuget.png)

You can learn more about this package at the [NuGet gallery](https://www.nuget.org/packages/Microsoft.Azure.WebJobs.Extensions.CosmosDB).

## **Configure the Azure Function App**

The Azure function project contains a default file called `Function1.cs`. You can safely delete this file as we won’t be using this for our project.

Right-click on the `FAQFunctionApp` project and select Add >> New Folder. Name the folder as Models. Again, right-click on the Models folder and select Add >> Class to add a new class file. Put the name of your class as `FAQ.cs` and click Add.

Open `[FAQ.cs](https://github.com/AnkitSharma-007/azure-serverless-with-blazor/blob/master/FAQFunctionApp/FAQFunctionApp/Models/FAQ.cs)` and put the following code inside it.

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

The class has the same structure as the JSON data we have inserted in the cosmos DB.

Right-click on the `FAQFunctionApp` project and select Add >> Class. Name your class as `[CovidFAQ.cs](https://github.com/AnkitSharma-007/azure-serverless-with-blazor/blob/master/FAQFunctionApp/FAQFunctionApp/CovidFAQ.cs)`. Put the following code inside it.

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

We have created a class `CovidFAQ` and added an Azure function to it. The attribute `FunctionName` is used to specify the name of the function. We have used the `HttpTrigger` attribute which allows the function to be triggered via an HTTP call. The attribute `CosmosDB` is used to connect to the Azure Cosmos DB. We have defined three parameters for this attribute as described below:

* **databaseName**: the name for the cosmos DB
* **collectionName**: the collecting inside the cosmos DB we want to access
* **ConnectionStringSetting**: the connection string to connect to Cosmos DB. We will configure it in the next section.

We have decorated the parameter `questionSet`, which is of type `IEnumerable<FAQ>` with the `CosmosDB` attribute. When the app is executed, the parameter `questionSet` will be populated with the data from Cosmos DB. The function will return the data using a new instance of `OkObjectResult`.

## **Add the connection string to the Azure Function**

Remember the Azure cosmos DB connection string you noted earlier? Now we will configure it for our app. Open the `local.settings.json` file and add your connection string as shown below:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "dotnet",
    "DBConnectionString": "your connectionn string"
  }
}

```

> The local.settings.json will not be published to Azure when we publish the Azure Function app. Therefore, we need to configure the connections string separately while publishing the app to Azure. We will see this in action in the latter part of this article.

## **Test the Azure Function locally**

Press F5 to execute the function. Copy the URL of your function from the Azure Functions runtime output. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ExecuteLocal-1.png)

Open the browser and paste the URL in the browser’s address bar. You can see the output as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ExecuteLocal-2.png)

Here you can see the data we have inserted into our Azure Cosmos DB.

## **Publish the Function app to Azure**

We have successfully created the Function app, but it is still running in the localhost. Let’s publish the app to make it available globally.

Right-click on the `FAQFunctionApp` project and select Publish. Select the Publish target as Azure.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/DeploytoAZ_1.png)

Select the specific target as “Azure Function App (windows)”.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/DeploytoAZ_2.png)

In the next window, click on the “Create a new Azure Function…” button. A new Function App window will open. Refer to the image as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/DeploytoAZ_3.png)

You can fill in the details as indicated below:

* **Name:** A globally unique name for your function app.
* **Subscription**: Select your Azure subscription name from the drop-down.
* **Resource Group**: Select an existing Resource Group or create a new one.
* **Plan Type**: Select Consumption. It will make sure that you pay only for executions of your functions app.
* **Location:** Select a location for your function.
* **Azure Storage**: Keep the default value.

Click on the “Create” button to create the Function App and return to the previous window. Make sure the option “Run from package file” is checked. Click on the Finish button.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/DeploytoAZ_4.png)

Now you are at the Publish page. Click on the “Manage Azure App Service Settings” button.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ManageAZappSetting.png)

You will see a “Application Settings” window as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/SetConnString.png)

At this point, we will configure the Remote value for the “DBConnectionString” key. This value is used when the app is deployed on Azure. Since the key for Local and Remote environment is the same in our case, click on the “Insert value from Local” button to copy the value from the Local field to the Remote field. Click on the OK button.

You are navigated back to the Publish page. We are done with all the configurations. Click on the Publish button to publish your Azure function app. After the app is published, get the site URL value, append `/api/covidFAQ` to it and open it in the browser. You can see the output as shown below.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ExecuteGlobally.png)

This is the same dataset that we got while running the app locally. This proves that our serverless Azure function is deployed and able to access the Azure Cosmos DB successfully.

## **Enable CORS for the Azure app service**

We will use the Function app in a Blazor UI project. To allow the Blazor app to access the Azure Function, we need to enable CORS for the Azure app service.

Open the Azure portal. Navigate to “All resources”. Here, you can see the App service which we have created while Publishing the app the in previous section. Click on the resource to navigate to the resource page. Click on CORS on the left navigation. A CORS details pane will open.

Now we have two options here:

1. Enter the specific origin URL to allow them to make cross-origin calls.
2. Remove all origin URL from the list, and use “*” wildcard to allow all the URL to make cross-origin calls.

We will use the second option for our app. Remove all the previously listed URL and enter a single entry as “*” wildcard. Click on the Save button at the top. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/AZFuncCors.png)

## **Create the Blazor Web assembly project**

Open Visual Studio 2019, click on “Create a new project”. Select “Blazor App” and click on the “Next” button. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateBlazorProj_1.png)

On the “Configure your new project” window, put the project name as `FAQUIApp` and click on the “Create” button as shown in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateBlazorProj_2.png)

On the “Create a new Blazor app” window, select the “Blazor WebAssmebly App” template. Click on the Create button to create the project. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateBlazorProj_3.png)

To create a new razor component, right-click on the Pages folder, select Add >>Razor Component.An “Add New Item” dialog box will open, put the name of your component as `CovidFAQ.razor` and click on the Add button. Refer to the image shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/CreateRazorComp.png)

Open `[CovidFAQ.razor](https://github.com/AnkitSharma-007/azure-serverless-with-blazor/blob/master/FAQUIApp/FAQUIApp/Pages/CovidFAQ.razor)` and put the following code into it.

```
@page "/covidfaq"
@inject HttpClient Http

<div class="d-flex justify-content-center">
    <img src="../Images/COVID_banner.jpg" alt="Image" style="width:80%; height:300px" />
</div>
<br />
<div class="d-flex justify-content-center">
    <h1>Frequently asked Questions on Covid-19</h1>
</div>
<hr />

@if (questionList == null)
{
    <p><em>Loading...</em></p>
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

In the `@code` section, we have created a class called FAQ. The structure of this class is the same as that of the FAQ class we created earlier in the Azure function app**.** Inside the `OnInitializedAsync` method, we are hitting the API endpoint of our function app. The data returned from the API will be stored in a variable called `questionList` which is an array of type `FAQ`.

In the HTML section of the page, we have set a banner image at the top of the page. The image is available in the `/wwwroot/Images` folder. We will use a foreach loop to iterate over the `questionList` array and create a bootstrap card to display the question and answer.

## **Adding Link to Navigation menu**

The last step is to add the link of our CovidFAQ component in the navigation menu. Open `[/Shared/NavMenu.razor](https://github.com/AnkitSharma-007/azure-serverless-with-blazor/blob/master/FAQUIApp/FAQUIApp/Shared/NavMenu.razor#L15-L19)` file and add the following code into it.

```html
<li class="nav-item px-3">
  <NavLink class="nav-link" href="covidfaq">
    <span class="oi oi-plus" aria-hidden="true"></span> Covid FAQ
  </NavLink>
</li>

```

Remove the navigation links for Counter and Fetch-data components as they are not required for this application.

## **Execution Demo**

Press F5 to launch the app. Click on the Covid FAQ button on the nav menu on the left. You can see all the questions and answers in a beautiful card layout as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/BlazorExecution.png)

You can also check the live app at [https://covid19-faq.azurewebsites.net/](https://covid19-faq.azurewebsites.net/)

## **Summary**

In this article, we learned about serverless and its advantage over the traditional 3-tier web architecture. We also learned how the Azure function fits in serverless web architecture. 

To demonstrate the practical implementation of these concepts, we have created a Covid-19 FAQ app using the Blazor web assembly and Azure serverless. The questions and answers are displayed in the card layout using Bootstrap. 

We have used the Azure cosmos DB as the primary database to store the questions and answers for our FAQ app. An Azure function is used to fetch data from the cosmos DB. We deployed the function app on Azure to make it available globally via an API endpoint.

## **See Also**

* [Optical Character Reader Using Blazor And Computer Vision](https://ankitsharmablogs.com/optical-character-reader-using-blazor-and-computer-vision/)
* [Multi-Language Translator Using Blazor And Azure Cognitive Services](https://ankitsharmablogs.com/multi-language-translator-using-blazor-and-azure-cognitive-services/)
* [Facebook Authentication And Authorization In Server-Side Blazor App](https://ankitsharmablogs.com/facebook-authentication-and-authorization-in-server-side-blazor-app/)
* [Continuous Deployment For Angular App Using Heroku And GitHub](https://ankitsharmablogs.com/continuous-deployment-for-angular-app-using-heroku-and-github/)
* [Google Authentication And Authorization In Server-Side Blazor App](https://ankitsharmablogs.com/google-authentication-and-authorization-in-server-side-blazor-app/)
* [Blazor CRUD Using Google Cloud Firestore](https://ankitsharmablogs.com/blazor-crud-using-google-cloud-firestore/)

If you like the article, share with you friends. You can also connect with me on [Twitter](https://twitter.com/ankitsharma_007) and [LinkedIn](https://www.linkedin.com/in/ankitsharma-007/).

Originally published at [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)

