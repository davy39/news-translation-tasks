---
title: How to implement JavaScript Interop in Blazor
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T18:30:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-javascript-interop-in-blazor-9f91d263ec51
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RijhIwu_gn98_W_QnYcGAA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will learn about JavaScript Interop in Blazor. We will understand
  what JavaScript Interop is and how we can implement it in Blazor with the help of
  a sample application.

  We will be using Visual Studio ...'
---

By Ankit Sharma

### Introduction

In this article, we will learn about JavaScript Interop in Blazor. We will understand what JavaScript Interop is and how we can implement it in Blazor with the help of a sample application.

We will be using Visual Studio code for our demo.

### What is JavaScript Interop?

Blazor uses JavaScript to bootstrap the .NET runtime. It is able to use any JS library. C# code can call a JS function/API and JS code can call any C# methods. This property of calling a JS method from C# code and vice versa is referred as JavaScript Interop. Blazor uses JavaScript Interop to handle DOM manipulation and browser API calls.

JavaScript Interop is the feature provided by WebAssembly, since Blazor runs on Mono and mono is compiled to WebAssembly. Hence, Blazor can also implement this feature.

### Prerequisites

* Install the .NET Core 2.1 or above SDK from [here](https://www.microsoft.com/net/learn/get-started/windows#windowscmd).
* Install visual Studio Code from [here](https://code.visualstudio.com/).

### Source Code

Get the source code from [Github](https://github.com/AnkitSharma-007/Blazor-JSInterop).

### Creating the Blazor application

We will create a Blazor application using Windows PowerShell.

#### **Step 1**

First, we will install the Blazor framework templates in our machine.

Open the folder where you want to create your project. Open Windows PowerShell with shift + right click >> Open PowerShell window Here.

Type in the following command:

```
dotnet new -i Microsoft.AspNetCore.Blazor.Templates
```

Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/xyduFrvvobk8FKc3R4BRiAuZXmiJf6kNSv-0)

#### **Step 2**

Type in the following command to create our Blazor application:

```
dotnet new blazor -o BlazorJSDemo
```

This will create a Blazor application with the name **BlazorJSDemo**. Refer to the image below.

![Image](https://cdn-media-1.freecodecamp.org/images/oInrxVk6aoBMy6u9enSL3XjGiKUrSZy9augG)

### Adding the Razor Page to our application

Open the **BlazorJSDemo** app using VS code. You can observe the folder structure in Solution Explorer, as shown in the below image.

![Image](https://cdn-media-1.freecodecamp.org/images/yD2TqOZ31I3GFMavWBRJ5FeVs13NOe2xU0Di)

We will add our Razor page in the **Pages** folder.

Create a new file by right clicking on the Pages folder and select New File. Name the file **JSDemo.cshtml**. This file will contain HTML code to handle the UI of our application.

Similarly, add one more file **JSDemo.cshtml.cs**. This file will contain the C# code to handle our business logic.

Now our **Pages** folder will have the following structure:

![Image](https://cdn-media-1.freecodecamp.org/images/7uGmB3024FB7kaSQo-ZLMEnikX4CbA-tjEWa)

### Calling a JavaScript function from C#

First, we will write our JavaScript functions in **index.html file**. Open the **wwwroot/index.html** file and put in the following code:

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width">
    <title>BlazorJSDemo</title>
    <base href="/" />
    <link href="css/bootstrap/bootstrap.min.css" rel="stylesheet" />
    <link href="css/site.css" rel="stylesheet" />

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

</head>

<body>
    <app>Loading...</app>

    <script src="_framework/blazor.webassembly.js"></script>

    <script>
        function JSMethod() {
            $("#demop").text("JavaScript Method invoked");
        }
    </script>

</body>

</html>
```

Here we have included the CDN reference to JQuery library inside <head> section so that we can handle the DOM manipulation.

Inside the <body> section, we have defined our JS function. The function na_me is JS_Method and it is not accepting any arguments. When triggered it will set the text of a <p> tag having id “demop” to “JavaScript Method invoked”.

**Important Note**

1. Do not write your JS code in the **.cshtml** file. This is not allowed in Blazor and the compiler will throw an error. Always put your JS code in the **wwwroot/index.html** file.
2. Always add your custom <script> tag after “ <script src=”_framework/blazor.webassembly.js”></script>” in the **<body&g**t; section of index.html file. This is to ensure that your custom script will execute after loading the “ blazor.webassembly.js” script.

Open **JSDemo.cshtml.cs** and put in the following code:

```cs
using Microsoft.AspNetCore.Blazor.Components;
using Microsoft.JSInterop;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorJSDemo.Pages
{
    public class JSDemoModel : BlazorComponent
    {
        protected static string message { get; set; }

        protected void CallJSMethod()
        {
            JSRuntime.Current.InvokeAsync<bool>("JSMethod");
        }
    }
}
```

The method **CallJSMethod** will call our JS function “JSMethod” by using “JSRuntime.Current.InvokeAsync” method. This method can take two parameters — the JS function name and any parameter that needed to be supplied to theJS function. In this case, we are not passing any parameter to JS function.

Open **JSDemo.cshtml** and put in the following code:

```cs
@page "/demo"
@using BlazorJSDemo.Pages

@inherits JSDemoModel  

<h1>JavaScript Interop Demo</h1>

<hr />

<button class="btn btn-primary" onclick="@CallJSMethod">Call JS Method</button>

<br />
<p id="demop"></p>
```

Here we have defined the route of the page at the top. So, in this application, if we append “/demo” to the base URL, then we will be redirected to this page. We are also inheriting the **JSDemoModel** class, which is defined in the **JSDemo.cshtml.cs** file. This will allow us to use the methods defined in the **JSDemoModel** class.

After this, we have defined a button. This button will invoke the “CallJSMethod” method when clicked. The <p> element with id “demop” is also defined, and its value will be set by the JS function “JSMethod”.

### Calling a C#/.NET method from JavaScript

Now we will define our JS Method in the **wwwroot/index.html** file, which will call our C# method in the **JSDemo.cshtml.cs** file.

The syntax of calling a C# method from JavaScript is as follows:

```cs
DotNet.invokeMethodAsync('C# method assembly name', 'C# Method Name');
```

Therefore, we will follow the same method calling syntax. Open the **wwwroot/index.html** file and add the following script section to it:

```cs
<script>
  function CSMethod() {
    DotNet.invokeMethodAsync('BlazorJSDemo', 'CSCallBackMethod');
  }
</script>
```

Here we are defining a JS function “CSMethod”. This function will have a call back to our C# method “CSCallBackMethod” which is defined in **JSDemoModel** class.

To invoke a C#/.NET method from JavaScript, the target .NET method must meet the following criterias:

1. The method needs to be Static.
2. It must be Non-generic.
3. The method should have no overloads.
4. It has concrete JSON serializable parameter types.
5. It must be decorated with [JSInvokable] attribute.

Open **JSDemo.cshtml.cs** file and add the following code inside the **JSDemoModel** class.

```cs
protected static string message { get; set; }

[JSInvokable]
public static void CSCallBackMethod()
{
  message = "C# Method invoked";
}

protected void CallCSMethod()
{
  JSRuntime.Current.InvokeAsync<bool>("CSMethod");
}
```

Here we have defined two methods:

1. **CallCSMethod**: This will call our JS function “CSMethod”
2. **CSCallBackMethod**: This is a static method and it will be invoked from the JavaScript function “CSMethod”. Hence it is decorated with[JSInvokable] attribute. This method will set the value of a string variable **message**, which will be displayed on the UI.

Open the **JSDemo.cshtml** file and add the following code to it:

```html
<button class="btn btn-primary" onclick="@CallCSMethod">Call C# Method</button>
<br />
<p>@message</p>
```

Here we have defined a button which will call the “CallCSMethod” method on the “onclick” event. The value of the variable message is set on the button click.

### Adding Link to Navigation menu

Open **\BlazorJSDemo\Shared\NavMenu.cshtml** page and put the following code into it. This will include a link to our **JSDemo.cshtml** page in the navigation menu.

```html
<div class="top-row pl-4 navbar navbar-dark">
    <a class="navbar-brand" href="">BlazorJSDemo</a>
    <button class="navbar-toggler" onclick=@ToggleNavMenu>
        <span class="navbar-toggler-icon"></span>
    </button>
</div>

<div class=@(collapseNavMenu ? "collapse" : null) onclick=@ToggleNavMenu>
    <ul class="nav flex-column">
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="" Match=NavLinkMatch.All>
                <span class="oi oi-home" aria-hidden="true"></span> Home
            </NavLink>
        </li>
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="counter">
                <span class="oi oi-plus" aria-hidden="true"></span> Counter
            </NavLink>
        </li>
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="fetchdata">
                <span class="oi oi-list-rich" aria-hidden="true"></span> Fetch data
            </NavLink>
        </li>
         <li class="nav-item px-3">
            <NavLink class="nav-link" href="demo">
                <span class="oi oi-list-rich" aria-hidden="true"></span> JS Demo
            </NavLink>
        </li>
    </ul>
</div>

@functions {
    bool collapseNavMenu = true;

    void ToggleNavMenu()
    {
        collapseNavMenu = !collapseNavMenu;
    }
}
```

### Execution demo

Navigate to View >> Integrated Terminal to open the terminal window.

Type the command **dotnet run** to start the application. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/qPRwkQvalkfUx3ITH-tg6aG3TBMNscnWerVB)

You can observe that the application is listening on [_http://localhost:5000._](http://localhost:5000.) Open any browser on your machine and navigate to this URL. You can see the application home page. Click on the “JS Demo” link in the navigation menu to open the **JSdemo** view. Notice the URL has “/demo” appended to it.

Click on the buttons to invoke the JS functions and C# method.

Refer to the GIF below.

![Image](https://cdn-media-1.freecodecamp.org/images/J1P95jKUa8BulGL6f1qvan-kmMqn6XorEnaH)

### Conclusion

In this article, we have learned about JavaScript Interop. We have also created a sample application to demonstrate how JavaScript Interop works with the Blazor framework.

Please get the source code from [Github](https://github.com/AnkitSharma-007/Blazor-JSInterop) and play around to get a better understanding.

Get my book [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) to learn more about Blazor.

You can check out my other articles on ASP .NET Core [here](http://ankitsharmablogs.com/category/asp-net-core/).

### See Also

* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [Creating a SPA Using Razor Pages With Blazor](http://ankitsharmablogs.com/creating-a-spa-using-razor-pages-with-blazor/)
* [Cascading DropDownList In Blazor Using EF Core](http://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/)
* [Deploying A Blazor Application On IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)

Originally published at [ankitsharmablogs.com](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)

