---
title: How to Create Serverless Logic with Azure Functions
subtitle: ''
author: Salim Oyinlola
co_authors: []
series: null
date: '2022-09-26T22:35:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-serverless-logic-with-azure-functions
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-sagui-andrea-618833.jpg
tags:
- name: Azure
  slug: azure
- name: Azure Functions
  slug: azure-functions
- name: serverless
  slug: serverless
seo_title: null
seo_desc: "What is Serverless Computing?\nServerless computing is a cloud computing\
  \ model where backend services are provided on a pay-as-you-use basis. \nIn this\
  \ model, developers get to create and run development code without having to manage\
  \ or provision serve..."
---

## **What is Serverless Computing?**

Serverless computing is a cloud computing model where backend services are provided on a pay-as-you-use basis. 

In this model, developers get to create and run development code without having to manage or provision servers. As such, they get to focus solely on writing the business logic (or front-end development) code instead. 

Microsoft Azure provides a wide range of options for designing this kind of architecture. However, the most frequently used methods are Azure Logic Apps and Azure Functions which will be the main focus of this article. 

## **What are Azure Functions?**

Azure Functions is the serverless computing model on Microsoft Azure platform for creating serverless applications. It enables developers to host their business logics without the need for infrastructure. 

The code for Azure functions can be written in a wide range of programming languages including C#, JavaScript, and Python, amongst others. Like other cloud services, it operates on a pay-per-use basis, where you only pay for the resources you consume. 

By the end of this tutorial, you will be able to:

* Create an Azure function app in the Azure portal.
* Exercise a function using triggers.
* Monitor and test your Azure function from the Azure portal.

### **Prerequisites**

You will need a valid and active Microsoft Azure account to follow along with this tutorial. You can use either:

* [Free Azure Trial](https://azure.microsoft.com/en-us/free/): With this option, you will start with $200 Azure credit and will have 30 days to use it, in addition to free services.
* [Azure for Students](https://azure.microsoft.com/en-us/free/students/): This offer is available for students only. With this option, you will start with $100 Azure credit with no credit card required and access to popular services for free whilst you have your credit.

## **Step 1 – Create your Azure Function App**

To establish a serverless computing resource for your business logic using Azure Functions, it is essential to create an Azure Function application. Having created a valid and active Microsoft Azure account, navigate to the [portal](https://portal.azure.com/). 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-128.png)

* Select `Create a resource` 
* Select the `Create` button underneath the `Function App` pane. 
* On clicking the button, a page where you enter the details of your project appears as shown below. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-129.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-130.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-131.png)

Enter the configuration details for this tutorial under the `Basics` tab before clicking the `Review + create` button

* Enter the `Subscription` available on your account. Note that your subscription might not be `Visual Studio Enterprise Subscription` as shown in mine. 
* For the `Resource group`, if you have created one before, you could use it. However, if you have not created one or are not familiar with Azure resource group, create a new one by using the `Create new` button. 

At its core, a resource group is used to group similar Azure services on your Azure subscription together to make managing them easier. 

* For the `Function App name` option, enter a globally unique app name. It is important to note that this name is will become part of the base URL for your service. 
* For the `Publish` option, select `Code`. 
* Choose `Node.js` for the `Runtime Slack` option since this tutorial's function examples were implemented using that language.
* Leave the `Version` option as default.
* Select the region that is geographically nearest to you when filling out the `Region` choice. A region is a collection of physical server data centers. Given that my base of operations is in Lagos, Nigeria, I chose `South Africa North`.
* For the `Operating System`, select one that conforms with your selection of runtime.
* For the `Plan` option, select `Consumption (Serverless)`. The plan you choose will determine how your app scales and what features are enabled.  
* At this point, you can then click the `Review + create` button.

The validation and deployment process usually takes up to three minutes. When the validation and deployment processes are both completed for the Azure Function set up, you can then verify that your Azure function app is running.

## **Step 2 – Verify that your Azure Function App is Running**

Once the deployment process is done, select `Go to resource`. Your function's App pane will now appear. To open it in a browser, select the `URL` link in the `Essentials` section. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-132.png)

With the message above, you will see a standard Azure functions web app page appear: _Your Function 4.0 app is up and running._ 

## **Step 3 – Run your Code On-Demand with Azure Functions**

With the function app created, the next step is to build and configure the function. To do this, you have to understand what Triggers and Bindings are. 

> Triggers cause a function to run. A trigger defines how a function is invoked and a function must have exactly one trigger. Triggers have associated data, which is often provided as the payload of the function. Binding to a function is a way of declaratively connecting another resource to the function; bindings may be connected as _input bindings_, _output bindings_, or both. Data from bindings is provided to the function as parameters. – [Microsoft Learn Documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings?tabs=csharp)

In general, Azure Functions run in response to an event. This event is known as a **Trigger** and **Bindings** are used to connect resources to a function. The typical triggers on Azure range from a blob storage that runs a function when a blob is created or updated to a timer that runs a function on a schedule.

To run your code on Azure Functions, you need to first create your function to run your code within the function app using the template. 

To do this, click the `Function` tag on the menu bar on the left of your functions app's home page. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-134.png)

* Click the `+ Create` button to create the function. 
* Select the `Azure Queue Storage trigger` template. This trigger runs the functions app when it detects that a message has been added to an Azure storage queue. 
* Leave everything else as its default value. 
* Click the `Create` button to create the function. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-135.png)

Given that the function was created with a template, several other files will be created automatically. These files comprises of a source code and a configuration file. 

* Click on the `Code + Test` button on the left pane and open the `function.json` file by selecting it from the dropdown. 
* Replace the block of code it shows with the one below. 

```python
{
  "bindings": [
    {
      "name": "order",
      "type": "queueTrigger",
      "direction": "in",
      "queueName": "myqueue-items",
      "connection": "MY_STORAGE_ACCT_APP_SETTING"
    },
    {
      "name": "$return",
      "type": "table",
      "direction": "out",
      "tableName": "outTable",
      "connection": "MY_TABLE_STORAGE_ACCT_APP_SETTING"
    }
  ]
}
```

This block of code sets the trigger for the function as **when a message is added to the queue named `myqueue-items`.** Furthermore, it sends the return value to the `outTable`. 

* Save and _Test/Run_ the function whilst leaving the testing details as their default values and run the function app. 
* You will see the output shown below.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-136.png)

The fact that the outcome automatically displays on the **Output tab** suggests that the function app functions well. Because there isn't any business logic applied to the function, the graphic above is blank.

## **Conclusion**

In this tutorial, you have seen that serverless computing is a great option for hosting business logic code in the cloud. You have seen that with serverless offers such as Azure Functions, you can write your business logic in the language of your choice.

Also, it is important to note that not only does the use of serverless computing solutions avoid the over-allocation of infrastructure (because they can be created and destroyed on demand), but they are also event driven. Event driven in the sense that they run only in response to an event (called a 'trigger'), such as a message being added to a queue, or receiving an HTTP request.

Finally, I share my writings on [Twitter](https://twitter.com/SalimOyinlola) if you enjoyed this article and want to see more.


