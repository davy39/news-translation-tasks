---
title: A quick introduction to Server-side Blazor apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-09T23:29:28.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-server-side-blazor-apps-c991e59c90de
coverImage: https://cdn-media-1.freecodecamp.org/images/1*INENIFhB5lJNvVrYuxXX4w.png
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: null
seo_desc: 'By Ankit Sharma

  Introduction

  We all know that the Blazor framework is a client-side web framework. But is it
  possible to run a Blazor application separate from a UI thread? The latest version
  0.5.0 of Blazor gives us the flexibility to run it in a se...'
---

By Ankit Sharma

### Introduction

We all know that the Blazor framework is a client-side web framework. But is it possible to run a Blazor application separate from a UI thread? The latest version 0.5.0 of Blazor gives us the flexibility to run it in a separate process from the rendering process. We are going to explore server-side Blazor in this article.

### What is Server-Side Blazor?

Since Blazor is a client-side web framework, the component logic and DOM interaction both happens in the same process.

![Image](https://cdn-media-1.freecodecamp.org/images/SE8WnGMv3amme5Z6z5vClAJiTPXhzNUq1h5E)

However, the design of the Blazor framework is smart and flexible enough to run the application separate from the rendering process. For example, we can run Blazor in a web worker thread separately from the UI thread.

In this scenario, the UI thread will push the events to the Blazor worker thread, and Blazor will push UI updates to the UI thread as needed. Although Blazor does not support this functionality yet, but the Blazor framework is designed to handle such scenarios and is expected to support it in future releases.

![Image](https://cdn-media-1.freecodecamp.org/images/0o-zbwSglIvnNx8gUvHA37oJWSf5OMj1kCkt)

Starting from Blazor 0.5.0, we can run a Blazor application on the server. This means that we can run a Blazor component server-side on .NET Core while other functionalities, such as the UI, update. Event handling and JavaScript interop calls are handled by a SignalR connection over the network. The .NET part runs under CoreCLR instead of WebAssembly, which provides us the access to the complete .NET ecosystem, debugging, JIT compilation, and so on. This adds extensibility to the Blazor framework, as the server-side Blazor uses the same component model as running a client-side Blazor app.

![Image](https://cdn-media-1.freecodecamp.org/images/eWgI2AVm7-gGqD0B9fxWq5QlQ0wHiB06glT4)

Let us create our first server-side Blazor app and explore it to get a better understanding of this new feature.

### Prerequisites

* Install the .NET Core 2.1 or above SDK from [here](https://www.microsoft.com/net/learn/get-started-with-dotnet-tutorial#windowscmd)
* Install Visual Studio 2017 v15.7 or above from [here](https://visualstudio.microsoft.com/downloads/)
* Install ASP.NET Core Blazor Language Services extension from [here](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)

Visual Studio 2017 versions below v15.7 does not support the Blazor framework.

### Creating a server-side Blazor application

Open Visual Studio and select File >> New >> Project.

After selecting the project, a “New Project” dialog will open. Select .NET Core inside the Visual C# menu from the left panel. Then, select “ASP.NET Core Web Application” from the available project types. Name the project **ServerSideBlazor** and press OK.

![Image](https://cdn-media-1.freecodecamp.org/images/PVahH9QmYcbo2PgExBUIPugyXrOr-qxbCQho)

After clicking on OK, a new dialog will open asking you to select the project template. You can see two drop-down menus at the top left of the template window. Select “.NET Core” and “ASP.NET Core 2.1” from these dropdowns. Then, select the “Blazor (Server-side in ASP.NET Core)” template and press OK.

![Image](https://cdn-media-1.freecodecamp.org/images/apVoM-bwspujj5zLwGZ1bNJdWNelcHQSdXEd)

This will create our server-side Blazor solution. You can see the folder structure in Solution Explorer, as shown in the below image:

![Image](https://cdn-media-1.freecodecamp.org/images/cuCSqzS3yfGhGWLsjFrd0xsE0ijhORI2zvxi)

The solution has two project files:

1. ServerSideBlazor.App: this is our ASP.NET core hosted project.
2. ServerSideBlazor.Server: this contains our server-side Blazor app.

All of our component logic lies in the server-side Blazor app. However, this logic does not run on the client-side in browser — instead, it runs server-side in the ASP.NET Core host application. This application uses **blazor.server.js** for bootstrapping instead of blazor.webassembly.js which is used by normal Blazor apps. This allows the app to establish a SignalR connection over the network to handle UI updates and event forwarding. The **blazor.server.js** is present in the “\ServerSideBlazor.App\bin\Debug\netstandard2.0\dist\_framework” folder, and the <script> tag to include it in the project is present i**n the wwwroot/inde**x.html file.

![Image](https://cdn-media-1.freecodecamp.org/images/tC8zrjwd8WrCeS9hAiPxoqTmLmHU3HVJPenZ)

The **blazor.server.js** is the only component that separates a server-side Blazor app from a client-side Blazor app. If we provide a reference of **blazor.webassembly.js** instead of **blazor.server.js** inside the index.html file, then this application will behave like a client-side Blazor app.

The Blazor app is hosted by the ASP.NET Core app, which also sets up the SignalR endpoint. Since the Blazor app is running on the server, the event handling logic can directly access the server resources and services.

For example, if we want to fetch any data, we no longer need to issue an HTTP request. Instead, we can configure a service on the server and use it to retrieve the data.

In the sample application that we have created, the **WeatherForecastService** is defined inside the “ServerSideBlazor.App/Services” folder.

```
using System;using System.Linq;using System.Threading.Tasks;namespace ServerSideBlazor.App.Services{    public class WeatherForecastService    {        private static string[] Summaries = new[]        {            "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"        };        public Task<WeatherForecast[]> GetForecastAsync(DateTime startDate)        {            var rng = new Random();            return Task.FromResult(Enumerable.Range(1, 5).Select(index => new WeatherForecast            {                Date = startDate.AddDays(index),                TemperatureC = rng.Next(-20, 55),                Summary = Summaries[rng.Next(Summaries.Length)]            }).ToArray());        }    }}
```

Further, we need to configure the service inside the **ConfigureServices** method in the ServerSideBlazor.App/startup.cs” file.

```
public void ConfigureServices(IServiceCollection services){    services.AddSingleton<WeatherForecastService>();}
```

We will then inject the service into the **FetchData.cshtml** view page, where the method **GetForecastAsync** is invoked to fetch the data.

```
@using ServerSideBlazor.App.Services@page "/fetchdata"@inject WeatherForecastService ForecastService// HTML DOM here.@functions {    WeatherForecast[] forecasts;    protected override async Task OnInitAsync()    {        forecasts = await ForecastService.GetForecastAsync(DateTime.Now);    }}
```

Go ahead and launch the application in Google Chrome. It will open a browser window and the app will look like a normal Blazor app. Open Chrome DevTools. Navigate to the “Network” tab and you can see that the application has not downloaded any .NET runtime or the app assembly.

![Image](https://cdn-media-1.freecodecamp.org/images/jjiNmnaV4euLEWb1OFxiqAAf9IM7jbeKMngv)

This is because the app is running sever-side on .NET Core. Since the dependencies are not downloaded on application boot up, the size of the app is smaller. It will also load faster compared to a normal Blazor app.

### Advantages of server-side Blazor

Server-side Blazor applications provide us many benefits:

1. Since the UI update is handled over a SignalR connection, we can avoid the unnecessary page refreshes.
2. The app download size is smaller and the initial app load is faster.
3. The Blazor component can take full advantage of server capabilities such as using .NET Core compatible APIs.
4. It will also support existing .NET tooling like debugging the application and JIT compilation.
5. Since server-side Blazor runs under a native .NET Core process and not under Mono WebAssembly, it is also supported on the browsers that have no WebAssembly support.

But there are also few drawbacks for server-side blazor apps:

1. Since UI interaction involves SignalR communication, it adds one extra step in network calls which results in some latency.
2. Scalability of the apps (handling multiple client connections) is also a challenge.

### Conclusion

We have learned about the latest server-side Blazor application introduced with the Blazor 0.5.0 release, and we now understand how it is different from the normal client-side Blazor app. We’ve also discussed the pros and cons of using a server-side Blazor app over a client-side blazor app.

Get my book [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) to learn more about Blazor.

You can check out my other articles on Blazor [here](http://ankitsharmablogs.com/category/blazor/).

Preparing for interviews? Read my article on [C# Coding Questions For Technical Interviews](http://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/)

### See Also

* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [Cascading DropDownList In Blazor Using EF Core](http://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/)
* [Creating a SPA Using Razor Pages With Blazor](http://ankitsharmablogs.com/creating-a-spa-using-razor-pages-with-blazor/)
* [Deploying a Blazor Application on IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)
* [JavaScript Interop in Blazor](http://ankitsharmablogs.com/javascript-interop-in-blazor/)

Originally published at [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)

