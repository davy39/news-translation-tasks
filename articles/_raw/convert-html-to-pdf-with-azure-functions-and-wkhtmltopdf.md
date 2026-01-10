---
title: How to Convert HTML to PDF with Azure Functions and wkhtmltopdf
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
seo_title: null
seo_desc: "By Arjav Dave\nIn this article, we are going to use Azure Functions and\
  \ the wkhtmltopdf tool to generate a PDF file from an HTML file. \nYou might want\
  \ to create a PDF file for a great many reasons, such as generating invoices for\
  \ sales, medical report..."
---

By Arjav Dave

In this article, we are going to use Azure Functions and the [wkhtmltopdf](https://wkhtmltopdf.org/) tool to generate a PDF file from an HTML file. 

You might want to create a PDF file for a great many reasons, such as generating invoices for sales, medical reports for your patients, insurance forms for your clients, and so on. And there are a few ways to do this.

Firstly, you can use [Adobe](https://www.adobe.com/in/acrobat/online/sign-pdf.html)'s fill and sign tool to fill out forms. But this mostly requires a human interaction and so it’s not scalable or convenient.

The second option is that you directly create a PDF file. Based on the platform you are working on you will have tools to do this. If it’s a very simple PDF you can take this approach.

This brings us to our final and most convenient option, [wkhtmltopdf](https://wkhtmltopdf.org/). This is a really great tool that lets you convert your HTML to PDF. Since it is free, open source, and can be compiled for almost all platforms, it is our best choice.

## Prerequisites

* VS Code editor installed
* An account on [Azure Portal](https://portal.azure.com/)
* Linux Basic (B1) App Service Plan. If you already have a Windows Basic (B1) App Service Plan you can use that.
* Azure Storage Account.

## How to Use Azure Functions

Since converting HTML to a PDF is a time consuming task, we shouldn’t run it on our main web server. Otherwise it may start blocking other important requests. Azure Functions are the best way to delegate such tasks.

In order to create a function you will first need to install Azure Functions on your machine. Based on your OS install the [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Ccsharp%2Cbash#install-the-azure-functions-core-tools). 

Once installed open your command line tool to fire the below command. `html2pdf` is the project’s name here, but you can replace it with any name.

```func init html2pdf```

When you execute the command it will ask for a worker runtime. Here select option 1, dotnet since it's a Microsoft’s product and provides great support for dotnet. 

This will generate a folder name `html2pdf` in your current directory. Since Visual Studio Code allows to directly publish to Azure Functions, we will use it to code and deploy.

After you open your project in VS Code, create a file named `Html2Pdf.cs`. Azure Functions provides a wide variety of [triggers](https://www.serverless360.com/blog/azure-functions-triggers-and-bindings) to execute the function. For now we will start with the HTTP trigger, that is the function can be called directly via the HTTP protocol. 

In our newly created file, paste the below content:

```
using System;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.Extensions.Logging;

namespace Html2Pdf
{
    public class Html2Pdf
    {
        // The name of the function
        [FunctionName("Html2Pdf")]
        
        // The first arugment tells that the functions can be triggerd by a POST HTTP request. 
        // The second argument is mainly used for logging information, warnings or errors
        public void Run([HttpTrigger(AuthorizationLevel.Function, "POST")] Html2PdfRequest Request, ILogger Log)
        {
        }
    }
}
```

We have created the skeleton and now we will fill in the details. As you might have noticed the type of request variable is `Html2PdfRequest`. So let’s create a model `Html2PdfRequest.cs` class as below:

```
namespace Html2Pdf
{
    public class Html2PdfRequest
    {
        // The HTML content that needs to be converted.
        public string HtmlContent { get; set; }
      
        // The name of the PDF file to be generated
        public string PDFFileName { get; set; }
    }
}
```

## How to Add DinkToPdf to Your Project

In order to invoke wkhtmltopdf from our managed code, we use a technology called P/Invoke.

In short [P/Invoke](https://docs.microsoft.com/en-us/dotnet/standard/native-interop/pinvoke) allows us to access structs, callbacks, and functions in unmanaged libraries. There is a nice P/Invoke wrapper named [DinkToPdf](https://github.com/rdvojmoc/DinkToPdf) that allows us to abstract away the technicalities.

You can add DinkToPdf to your project via [nuget](https://www.nuget.org/packages/DinkToPdf/). Simply run the command from your root folder.

```
dotnet add package DinkToPdf --version 1.0.8
```

Time to add some code at the top of our class `Html2Pdf`:

```
// Read more about converter on: https://github.com/rdvojmoc/DinkToPdf
// For our purposes we are going to use SynchronizedConverter
IPdfConverter pdfConverter = new SynchronizedConverter(new PdfTools());

// A function to convert html content to pdf based on the configuration passed as arguments
// Arguments:
// HtmlContent: the html content to be converted
// Width: the width of the pdf to be created. e.g. "8.5in", "21.59cm" etc.
// Height: the height of the pdf to be created. e.g. "11in", "27.94cm" etc.
// Margins: the margis around the content
// DPI: The dpi is very important when you want to print the pdf.
// Returns a byte array of the pdf which can be stored as a file
private byte[] BuildPdf(string HtmlContent, string Width, string Height, MarginSettings Margins, int? DPI = 180)
{
  // Call the Convert method of SynchronizedConverter "pdfConverter"
  return pdfConverter.Convert(new HtmlToPdfDocument()
            {
                // Set the html content
                Objects =
                {
                    new ObjectSettings
                    {
                        HtmlContent = HtmlContent
                    }
                },
                // Set the configurations
                GlobalSettings = new GlobalSettings
                {
                    // PaperKind.A4 can also be used instead PechkinPaperSize
                    PaperSize = new PechkinPaperSize(Width, Height),
                    DPI = DPI,
                    Margins = Margins
                }
            });
}
```

I have added inline comments so that the code is self-explanatory. If you have any questions you can ask me on Twitter. Let’s call the above created function from our `Run` method.

```
// PDFByteArray is a byte array of pdf generated from the HtmlContent 
var PDFByteArray = BuildPdf(Request.HtmlContent, "8.5in", "11in", new MarginSettings(0, 0, 0,0));
```

Once the byte array is generated, let’s store that as a blob in Azure Storage. Before you upload the blob, make sure you create a container. Once you do that, add the below code after `PDFByteArray`.

```
// The connection string of the Storage Account to which our PDF file will be uploaded
// Make sure to replace with your connection string.
var StorageConnectionString = "DefaultEndpointsProtocol=https;AccountName=<YOUR ACCOUNT NAME>;AccountKey=<YOUR ACCOUNT KEY>;EndpointSuffix=core.windows.net";

// Generate an instance of CloudStorageAccount by parsing the connection string
var StorageAccount = CloudStorageAccount.Parse(StorageConnectionString);

// Create an instance of CloudBlobClient to connect to our storage account
CloudBlobClient BlobClient = StorageAccount.CreateCloudBlobClient();

// Get the instance of CloudBlobContainer which points to a container name "pdf"
// Replace your own container name
CloudBlobContainer BlobContainer = BlobClient.GetContainerReference("pdf");

// Get the instance of the CloudBlockBlob to which the PDFByteArray will be uploaded
CloudBlockBlob Blob = BlobContainer.GetBlockBlobReference(Request.PDFFileName);

// Upload the pdf blob
await Blob.UploadFromByteArrayAsync(PDFByteArray, 0, PDFByteArray.Length);
```

You will see some errors and warnings after you add this code. To fix those, first add the missing import statements. Second, change the return type from `void` to `async Task` for the `Run` function. Here is what the final `Html2Pdf.cs` file will look like:

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
        // Read more about converter on: https://github.com/rdvojmoc/DinkToPdf
        // For our purposes we are going to use SynchronizedConverter
        IPdfConverter pdfConverter = new SynchronizedConverter(new PdfTools());

        // A function to convert html content to pdf based on the configuration passed as arguments
        // Arguments:
        // HtmlContent: the html content to be converted
        // Width: the width of the pdf to be created. e.g. "8.5in", "21.59cm" etc.
        // Height: the height of the pdf to be created. e.g. "11in", "27.94cm" etc.
        // Margins: the margis around the content
        // DPI: The dpi is very important when you want to print the pdf.
        // Returns a byte array of the pdf which can be stored as a file
        private byte[] BuildPdf(string HtmlContent, string Width, string Height, MarginSettings Margins, int? DPI = 180)
        {
            // Call the Convert method of SynchronizedConverter "pdfConverter"
            return pdfConverter.Convert(new HtmlToPdfDocument()
            {
                // Set the html content
                Objects =
                {
                    new ObjectSettings
                    {
                        HtmlContent = HtmlContent
                    }
                },
                // Set the configurations
                GlobalSettings = new GlobalSettings
                {
                    // PaperKind.A4 can also be used instead of width & height
                    PaperSize = new PechkinPaperSize(Width, Height),
                    DPI = DPI,
                    Margins = Margins
                }
            });
        }

        // The name of the function
        [FunctionName("Html2Pdf")]

        // The first arugment tells that the functions can be triggerd by a POST HTTP request. 
        // The second argument is mainly used for logging information, warnings or errors
        public async Task Run([HttpTrigger(AuthorizationLevel.Function, "POST")] Html2PdfRequest Request, ILogger Log)
        {
            // PDFByteArray is a byte array of pdf generated from the HtmlContent 
            var PDFByteArray = BuildPdf(Request.HtmlContent, "8.5in", "11in", new MarginSettings(0, 0, 0, 0));

            // The connection string of the Storage Account to which our PDF file will be uploaded
            var StorageConnectionString = "DefaultEndpointsProtocol=https;AccountName=<YOUR ACCOUNT NAME>;AccountKey=<YOUR ACCOUNT KEY>;EndpointSuffix=core.windows.net";
            
            // Generate an instance of CloudStorageAccount by parsing the connection string
            var StorageAccount = CloudStorageAccount.Parse(StorageConnectionString);

            // Create an instance of CloudBlobClient to connect to our storage account
            CloudBlobClient BlobClient = StorageAccount.CreateCloudBlobClient();

            // Get the instance of CloudBlobContainer which points to a container name "pdf"
            // Replace your own container name
            CloudBlobContainer BlobContainer = BlobClient.GetContainerReference("pdf");
            
            // Get the instance of the CloudBlockBlob to which the PDFByteArray will be uploaded
            CloudBlockBlob Blob = BlobContainer.GetBlockBlobReference(Request.PDFFileName);
            
            // Upload the pdf blob
            await Blob.UploadFromByteArrayAsync(PDFByteArray, 0, PDFByteArray.Length);
        }
    }
}
```

This concludes the coding part of this tutorial!

## How to Add wkhtmltopdf to Your Project

We will still need to add the wkhtmltopdf library in our project. There are a few caveats when you're selecting a particular Azure App Plan. Based on the plan, we will have to get the wkhtmltopdf library. 

For our purposes we have selected the Linux Basic (B1) App Service Plan since Windows Basic (B1) App Service Plan is five times more expensive.

At the time of writing this blog, the Azure App Service Plan was using Debian 10 with amd64 architecture. Luckily for us, DinkToPdf provides [precompiled libraries](https://github.com/rdvojmoc/DinkToPdf/tree/master/v0.12.4/64%20bit) for Linux, Windows, and MacOS. 

Download the .so library for Linux and put it in your project’s root folder. I am working on MacOS so I downloaded libwkhtmltox.dylib as well. 

If you are using Windows or if you have hosted the Azure Functions on the Windows App Service Plan you must download the libwkhtmltox.dll. Here is how our project structure will look now:

![Image](https://i2.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-21-at-4.41.20-PM.png?resize=676%2C546&ssl=1)
_Project Structure_

When we create a build we need to include the .so library. In order to do that, open your csproj file and add the below content to the ItemGroup.

```
<None Update="./libwkhtmltox.so">
    <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    <CopyToPublishDirectory>Always</CopyToPublishDirectory>
</None>
```

Here is the whole csproj file:

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

## How to Create the Azure Functions App

Before we deploy to Azure Functions we will have to create it in Azure Portal. You can go to Azure Portal and start creating the _Azure Functions_ resource. Follow the below screenshots for clarity.

![Image](https://i2.wp.com/arjavdave.com/wp-content/uploads/2021/03/Untitled-1.jpg?resize=750%2C724&ssl=1)
_Instance Details_

In the below screenshot, make sure to select or create at least the _Basic_ Plan here. Secondly, in the Operating System select _Linux_.

![Image](https://i2.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-10.30.48-AM.png?resize=750%2C784&ssl=1)
_Plan Details_

It’s good to have _Application Insights_ since you will be able to see logs and monitor functions. Besides, it hardly costs anything. As shown in the screenshot below, select _Yes_ if you want to enable it.

![Image](https://i1.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-10.31.11-AM.png?resize=750%2C798&ssl=1)
_Application Insights_

Select Next: Tags and again click Next and click _Create_ to create your resource. It might take a few minutes to create the _Azure Functions_ resource.

## How to Deploy to Azure Functions

Once created, we will deploy our code directly to Azure Functions via VS Code. For that you will have to go to the extensions and install the _Azure Functions_ extension. With its help we will be able to login and manage Azure Functions.

![Image](https://i1.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-10.03.00-AM.png?resize=750%2C433&ssl=1)
_Azure Functions in Marketplace_

Once installed you will see the Azure icon on the side bar. When you click it, it will open a panel with an option to _Sign In to Azure_.

![Image](https://i1.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-10.19.08-AM.png?resize=750%2C846&ssl=1)
_Azure Functions Extension_

Select _Sign in to Azure_ which will open a browser where you can login with your account. Once logged in, you can go back to VS Code and see the list of Azure Functions in your side panel.

![Image](https://i0.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-10.43.07-AM.png?resize=670%2C656&ssl=1)
_List of Azure Functions_

For me there are four function apps. Since you might have created just one it will show one. Now it's time to deploy the app.

Press _F1_ to open a menu with a list of actions. Select _Azure Functions: Deploy to Function App…_ which will open a list of Azure Functions to which you can deploy. 

Select our newly created Azure Funtions App. This will ask for a confirmation pop-up, so go ahead and deploy it. It will take a few minutes to deploy your App.

## How to Configure wkhtmltopdf

Once you have deployed to Azure Functions there is still one last thing to do. We will need to add `libwkhtmltox.so` to a proper location on our Azure Functions App. 

Login to Azure portal and navigate to our Azure Functions App. On the side panel search for SSH and click the _Go_ button.

![Image](https://i2.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-12.14.03-PM.png?resize=750%2C219&ssl=1)
_Search SSH for Azure Functions_

This will open a SSH console in new tab. Our site is located at /home/site/wwwroot. So navigate to that folder by typing in the below command:

```
cd /home/site/wwwroot/bin
```

When you execute the `ls` command to view the contents of the file you won’t see the `libwkhtmltox.so` file. It is actually located at /home/site/wwwroot.

That is not the correct position. We need to copy it into the bin folder. To do that, execute the below command:

```
cp ../libwkhtmltox.so libwkhtmltox.so
```

If you know a better way to include the file in the bin folder, please let me know.

That’s it! You have a fully functional Azure Functions App. Time to call it from our demo dotnet project.

## How to Invoke the Azure Function

All said and done, we still need to test and call our function. Before we do that we need to get ahold of _Code_ which is required to call the Function. 

The _Code_ is a secret that needs to be included to call the Function securely. To get the _Code_ navigate to Azure Portal and open your Function App. In the side panel search for _Functions._

![Image](https://i0.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-12.28.21-PM.png?resize=750%2C418&ssl=1)
_Search Functions_

You will see _Html2Pdf_ in the list. Click on that function which will open the details view. In the side panel there will be an option for _Function Keys_. Select that option to view a hidden default _Code_ already added for you.

![Image](https://i1.wp.com/arjavdave.com/wp-content/uploads/2021/03/Screenshot-2021-03-22-at-12.29.55-PM.png?resize=750%2C374&ssl=1)

Copy the code and keep it handy since we will need it in the code. In order to test the function I have created a sample console app for you. Replace the base URL and the code is as below:

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
        // The HTML content that needs to be converted.
        public string HtmlContent { get; set; }

        // The name of the PDF file to be generated
        public string PDFFileName { get; set; }
    }

}
```

Again the code should be pretty self-explanatory. If you have any feedback or questions just let me know. Once you run the above console app, it will create a _hello-world.pdf_ file in your _pdf_ container in Azure Storage.

## Conclusion

That concludes our tutorial on how to convert HTML to PDF using Azure Functions. Though it might be a bit difficult to setup, it is one of the cheapest solutions for going serverless. 

Read some of my other articles here:

* [Learning Integration Tests in .NET with .TDD](https://itnext.io/learn-tdd-with-integration-tests-in-net-5-0-937f126e7220)
* [Provide a password-less way to login using .NET](https://www.freecodecamp.org/news/how-to-go-passwordless-with-dotnet-identity/)
* [How to Authenticate & Authorise with .NET Identity](https://itnext.io/net-5-how-to-authenticate-authorise-apis-correctly-34b09d132d84)
* [How to speed up your site with Azure CDN](https://www.freecodecamp.org/news/how-to-speed-up-your-website-with-azure-cdn/)

  

