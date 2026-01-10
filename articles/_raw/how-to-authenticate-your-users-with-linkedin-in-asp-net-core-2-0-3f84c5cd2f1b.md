---
title: How to authenticate your users with LinkedIn in ASP.NET Core 2.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T18:56:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-authenticate-your-users-with-linkedin-in-asp-net-core-2-0-3f84c5cd2f1b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RRYg2jQ-11JV9ToXthgI5Q.png
tags:
- name: authentication
  slug: authentication
- name: JavaScript
  slug: javascript
- name: LinkedIn
  slug: linkedin
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ankit Sharma

  Introduction

  Sometimes, we want our users to log in using their existing credentials from third-party
  applications, such as Facebook, Twitter, Google, LinkedIn, and so on. In this article,
  we are going to look into the authentication ...'
---

By Ankit Sharma

### Introduction

Sometimes, we want our users to log in using their existing credentials from third-party applications, such as Facebook, Twitter, Google, LinkedIn, and so on. In this article, we are going to look into the authentication of an ASP.NET Core app using a LinkedIn account.

### Prerequisites

* Install .NET Core 2.0.0 or above SDK from [here](https://www.microsoft.com/net/core#windowscmd).
* Install the latest version of Visual Studio 2017 from [here](https://www.visualstudio.com/downloads/).

### Create MVC Web Application

Open Visual Studio and select File >> New >> Project. After selecting the project, a “New Project” dialog will open.

Select .NET Core inside the Visual C# menu from the left panel. Then, select “ASP.NET Core Web Application” from the available project types.

Name the project **LinkdinAuth** and press OK.

![Image](https://cdn-media-1.freecodecamp.org/images/E79vbhBT7QoeX-w-PTjHfS3zfY9-p4X1-lRr)

After clicking on OK, a new dialog will open asking you to select the project template. You can see two drop-down menus at the top left of the template window. Select “.NET Core” and “ASP.NET Core 2.0” from these dropdowns.

Then, select “Web application(Model-View-Controller)” template.

Click on Change Authentication button, and a “Change Authentication” dialog box will open.

Select “Individual User Account” and click OK. Now click OK again to create our web app.

![Image](https://cdn-media-1.freecodecamp.org/images/na6nloJuhfcQn5O87p4zcnDujh1cWqbeRpqZ)

Before running the application, we need to apply migrations to our app.

Navigate to Tools >> Nuget Package Manager >> Package Manager Console.

It will open the Package Manager Console. Put in the **Update-Database** command and hit enter. This will update the database using Entity Framework Code First Migrations.

![Image](https://cdn-media-1.freecodecamp.org/images/bmvIJTMzQbQAF0BViIyn44zHO3vXV15-XtF9)

Press F5 to run the application. You can see a Home page as shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/ySQg5QFxS2mDs0B1w7-t-2xft57vk3KKmFYN)

### Create the LinkedIn app

Navigate to [https://www.linkedin.com/developer/apps](https://www.linkedin.com/developer/apps) and sign in using your LinkedIn account. If you do not have a LinkedIn account, you need to create one, as you cannot proceed without one.

Once you have logged in, you will be redirected to the **My Applications** page similar to the one shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/0NTuW8X48p50EU4R9ID8jBNMAEMMqaV5VSKE)

Click on the **Create Application** button to navigate to the **Create a New Application** page. Here you need to fill in the details to create a new LinkedIn application.

* Company Name: — Give an appropriate name. Here we are using the name **DemoCompany**.
* Application Name: — This is the name of your LinkedIn application. Give a proper name of your choice.

Note: **Do not use the word ” LinkedIn ” in your product name**. You will be prompted with an error “_The application name cannot contain LinkedIn_” and you won’t be allowed to create the app. This means “LinkedinAuthDemo” is an invalid name. Refer to the below image.

* Application Description: Give a proper description of your application.
* Application Logo: you need to upload a logo for your application. If you do not have a logo, just upload any image. Please provide your application’s logo image in PNG or JPEG format. The image must be square and at least 80 x 80 pixels, and no larger than 5 MB in size.
* Application Use: Select an appropriate value from the drop-down.
* Website URL: Provide the URL for your public website. For this tutorial, we will use a dummy URL [http://demopage.com.](http://demopage.com.)

Note: If you use the URL format [_www.demopage.com_,](http://www.demopage.com,) you will get an error “_Please enter a_ _valid URL_.” Always use a URL format such as [_http://demopage.com_.](http://demopage.com.)

* Business Email: Give your email id. If you do not want to provide your personal email id, then you can also use any dummy email id such as _xyz@gmail.com_
* Business Phone: Provide your contact number. For this tutorial, I am using a dummy phone number 123456789.

![Image](https://cdn-media-1.freecodecamp.org/images/nrsaGLAUcu30hYK9cbm21yxF9Y6rzZs-3guA)

Do keep in mind that all the fields in this form are required, so you need to provide appropriate values to all of them. Once you have furnished all the details, click on the **Submit** button. If there is no error in the form, your LinkedIn app will be created successfully and you will be redirected to the application homepage.

Here you see the **Client ID** and **Client Secret** fields in Authentication Keys section. Take note of these values, as we will need them to configure LinkedIn authentication in our web app.

In the Authorized Redirect URLs field, provide the base URL of your application with **/signin-linkedin** appended to it. For this tutorial, the URL will be [_http://localhost:52676/signin-linkedin_.](http://localhost:52676/signin-linkedin.) After entering the URL, Press the **Add** button adjacent to it to add the value. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/M3IGu7qbkUcgohdAXfi4zVvV-irPJIgJoR8u)

### Configure your web wpp to use LinkedIn authentication

We will be using a third party Nuget package **AspNet.Security.OAuth.LinkedIn** to implement LinkedIn authentication in our Web app. Open NuGet package manager (Tools >> NuGet Package Manager >> Package Manager Console) and put in the following command. Hit enter to install it.

```
Install-Package AspNet.Security.OAuth.LinkedIn -Version 2.0.0-rc2-final
```

This NuGet package is maintained by aspnet-contrib. You can read more about this package [here](https://www.nuget.org/packages/AspNet.Security.OAuth.LinkedIn/2.0.0-rc2-final).

We need to store the **Client ID** and **Client Secret** field values in our application. We will use the Secret Manager tool for this purpose. The Secret Manager tool is a project tool that can be used to store secrets such as password, API Key, etc. for a .NET Core project during the development process. With the Secret Manager tool, we can associate app secrets with a specific project and can share them across multiple projects.

Open our web application once again and Right-click the project in Solution Explorer. Select “Manage User Secrets” from the context menu.

![Image](https://cdn-media-1.freecodecamp.org/images/qBERap-JaDEhvoaoYUwbzoUmBbaJFryXHuTh)

A **secrets.json** file will open. Put the following code in it.

```
{    "Authentication:LinkedIn:ClientId": "Your ClientId here",    "Authentication:LinkedIn:ClientSecret": "Your ClientSecret here"  }
```

Now, open the **Startup.cs** file and put the following code into the **ConfigureServices** method.

```
services.AddAuthentication().AddLinkedIn(options =>{    options.ClientId = Configuration["Authentication:LinkedIn:ClientId"];    options.ClientSecret = Configuration["Authentication:LinkedIn:ClientSecret"];    options.Events= new OAuthEvents()    {        OnRemoteFailure = loginFailureHandler =>        {            var authProperties = options.StateDataFormat.Unprotect(loginFailureHandler.Request.Query["state"]);            loginFailureHandler.Response.Redirect("/Account/login");            loginFailureHandler.HandleResponse();            return Task.FromResult(0);        }    };});
```

In this code section, we are reading the **Client ID** and **Client Secret** values from the **secrets.json** file for authentication purposes. We are also handling the event of “OnRemoteFailure” in this code section. Hence, if the user denies the access to their LinkedIn account, then they will be redirected back to the Login page.

So finally, **Startup.cs** will look like this.

```
using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;using Microsoft.AspNetCore.Builder;using Microsoft.AspNetCore.Identity;using Microsoft.EntityFrameworkCore;using Microsoft.AspNetCore.Hosting;using Microsoft.Extensions.Configuration;using Microsoft.Extensions.DependencyInjection;using LinkdinAuth.Data;using LinkdinAuth.Models;using LinkdinAuth.Services;using Microsoft.AspNetCore.Http;using Microsoft.AspNetCore.Authentication.OAuth;  namespace LinkdinAuth{    public class Startup    {        public Startup(IConfiguration configuration)        {            Configuration = configuration;        }          public IConfiguration Configuration { get; }          // This method gets called by the runtime. Use this method to add services to the container.        public void ConfigureServices(IServiceCollection services)        {            services.AddDbContext<ApplicationDbContext>(options =>                options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));              services.AddIdentity<ApplicationUser, IdentityRole>()                .AddEntityFrameworkStores<ApplicationDbContext>()                .AddDefaultTokenProviders();              services.AddAuthentication().AddLinkedIn(options =>            {                options.ClientId = Configuration["Authentication:LinkedIn:ClientId"];                options.ClientSecret = Configuration["Authentication:LinkedIn:ClientSecret"];                  options.Events= new OAuthEvents()                {                    OnRemoteFailure = loginFailureHandler =>                    {                        var authProperties = options.StateDataFormat.Unprotect(loginFailureHandler.Request.Query["state"]);                        loginFailureHandler.Response.Redirect("/Account/login");                        loginFailureHandler.HandleResponse();                        return Task.FromResult(0);                    }                };              });               // Add application services.            services.AddTransient<IEmailSender, EmailSender>();              services.AddMvc();        }          // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.        public void Configure(IApplicationBuilder app, IHostingEnvironment env)        {            if (env.IsDevelopment())            {                app.UseBrowserLink();                app.UseDeveloperExceptionPage();                app.UseDatabaseErrorPage();            }            else            {                app.UseExceptionHandler("/Home/Error");            }                          app.UseStaticFiles();              app.UseAuthentication();              app.UseMvc(routes =>            {                routes.MapRoute(                    name: "default",                    template: "{controller=Home}/{action=Index}/{id?}");            });        }    }}
```

And with this, our application is ready.

### Execution Demo

Launch the application and click Login in the top right corner of the homepage.

![Image](https://cdn-media-1.freecodecamp.org/images/vbFttzcLv92wHLH2-ygU4mR0VYpyf5GXYrQM)

You will be redirected to [_http://localhost:52676/Account/Login_](http://localhost:52676/Account/Login), where you can see the option to login using LinkedIn on the right side of page.

![Image](https://cdn-media-1.freecodecamp.org/images/Y0xfdJTNoKlRGBHQ80NlU4xEyx6pEMNXpCEK)

Clicking on the **LinkedIn** button will take you to the LinkedIn authorization page. There, you will be asked to fill in your LinkedIn credentials and authorize the LinkedIn app to use your LinkedIn account.

![Image](https://cdn-media-1.freecodecamp.org/images/pGsM2ZoAeJnvHXM5RFiD1ZaT5ChhAWZQ-aEa)

Put in your LinkedIn credentials and click on the **Allow access** button. The application will take few moments to authenticate your LinkedIn account. Upon successful authentication with LinkedIn, you will be redirected to a registration page inside your application where you need to fill in an email id to tag with your account.

![Image](https://cdn-media-1.freecodecamp.org/images/Lc6AxdswuS0k0rYbuqniUlMPlfNe2FHG2cYy)

Give an email id and click register, and you will be redirected to the homepage again. But this time, you can also see your registered email id at the top right corner. Hence, we have successfully logged in to our ASP .NET Core application using LinkedIn.

![Image](https://cdn-media-1.freecodecamp.org/images/gu9vHE9TEehppVZdX3DljEjonZx62Ycy7Uzq)

### Conclusion

We have successfully created a LinkedIn app and used it to authenticate our ASP.NET Core application.

You can get the source code from [GitHub](https://github.com/AnkitSharma-007/ASPCore.LinkedInAuth).

Please note that **secrets.json** file contains dummy values. You’ll need to replace the values with the keys of your LinkedIn app before executing it.

You can also find this article at [C# Corner](http://www.c-sharpcorner.com/article/authentication-using-linkedin-in-asp-net-core-2-0/).

You can check out my other articles on ASP .NET Core [here](http://ankitsharmablogs.com/category/asp-net-core/).

### See Also

* [Authentication Using Google In ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-google-asp-net-core-2-0/)
* [Authentication Using Twitter In ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-twitter-in-asp-net-core-2-0/)
* [Authentication Using Facebook In ASP.NET Core 2.0](http://ankitsharmablogs.com/authentication-using-facebook-in-asp-net-core-2-0/)
* [Cookie Authentication With ASP.NET Core 2.0](http://ankitsharmablogs.com/cookie-authentication-with-asp-net-core-2-0/)
* [ASP.NET Core — Two Factor Authentication Using Google Authenticator](http://ankitsharmablogs.com/asp-net-core-two-factor-authentication-using-google-authenticator/)

Originally published at [ankitsharmablogs.com](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)

