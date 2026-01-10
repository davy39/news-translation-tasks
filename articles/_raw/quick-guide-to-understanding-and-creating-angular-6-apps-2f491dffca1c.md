---
title: A Quick Guide to Help you Understand and Create Angular 6 Apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-10T16:14:17.000Z'
originalURL: https://freecodecamp.org/news/quick-guide-to-understanding-and-creating-angular-6-apps-2f491dffca1c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*NJiF_4tVYO3O5EhM
tags:
- name: Angular
  slug: angular
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Aditya Sridhar

  This post is divided into two parts:

  The first part demonstrates how to create a simple Angular 6 App using Angular CLI
  and explains the project structure.

  The second part explains existing code that I have posted in GitHub. This co...'
---

By Aditya Sridhar

This post is divided into two parts:

The first part demonstrates how to create a simple Angular 6 App using Angular CLI and explains the project structure.

The second part explains existing code that I have posted in GitHub. This code demonstrates the use of components, services, HTTP client, and communication between components.

### Part 1

#### Install Node.js if not already present

You need Node.js, since the libraries required for Angular are downloaded using node package manager (npm) . Refer to [https://nodejs.org/en/](https://nodejs.org/en/) to install Node.js.

#### Install Angular CLI

Angular CLI is a command line interface for Angular, and is very useful in quickly creating an Angular 6 project template. Install the Angular CLI npm package globally using the following command:

```bash
npm install -g @angular/cli
```

#### Create the Project

Angular CLI helps in creating a project very easily. In order to create the project, use the following command.

```bash
ng new simple-angular6-app
```

**simple-angular6-app** is the name of the project. Now you will notice that you see a folder named **simple-angular6-app.** The folder is the project which has been created. In order to test if everything has been set properly, go into the project folder and run the application using the following commands:

```bash
cd simple-angular6-app
npm start
```

Go to your browser and go the following URL: **localhost:4200.** You should be able to see that your application is running.

The application would look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/HBxcPkVdbdA0Bt0XLfs7cnnpuyyOU4DUIG0Z)

#### Basic Folder Structure Explained

When you create the project, you’ll notice that it creates a bunch of files. Here I will list out some of the important files and folders that you should be aware of:

1. **package.json:** This file has the list of node dependencies which are needed.
2. **src/styles.css**: This file has the global CSS available throughout the application.
3. **src/main.ts**: This is the main file which starts the Angular Application (AppModule is bootstrapped here as seen in the code ). Here the Extension .ts stands for TypeScript.
4. **src/index.html**: This the first file which executes alongside main.ts when the page loads.
5. **src/app/app.module.ts**: This is the file where all the components, providers, and modules are defined. Without defining them here, they can’t be used elsewhere in the code.
6. **src/app/app.component.html:** This is the main component of an angular app, and all other components are usually present within this component. **src/app/app.component.ts** is the logic for this component, and **src/app/app.component.css** is the CSS for this component. This component itself does not do any important logic, but acts as a container for other components.
7. **dist**: This folder is where the built files are present. TypeScript is basically converted to JavaScript and the resulting files are stored here after bundling and minification. (This Folder appears only if the application is built. A simple “npm start” will not create this folder. ) Since web browsers understand only JavaScript (at least for now), it is therefore necessary to convert TypeScript to JavaScript before deploying the code. To see this folder, you can type the following in the command prompt:

```bash
npm run build
```

There are several other files as well, but knowing these basic ones is good for a start

#### TypeScript

Angular 6 uses TypeScript for implementing the logic. Those of you who have worked in Java will find TypeScript very easy. TypeScript is a language built on top of JavaScript but which is type safe, and TypeScript in turn compiles to JavaScript

#### Creating Components and Services

1. **Component**: A component in Angular does a specific function. An Angular application is built by using various components. Angular CLI can be used to create components easily. The syntax is **ng generate component [name].** Use the following command to create a component called “customers”.

```bash
ng generate component customers
```

2. The above command creates a folder called **customers** inside **src/app**. The component created has:

* a **customers.component.html** file to decide the template (how the component UI should look )
* a **customers.component.ts** file which is where the logic is present
* a **customers.component.css** file which has CSS content
* and a **customers.component.spec.ts** file which is used for unit testing (the spec wont be explained in this post).

3. **Service**: A service basically provides functionality which can be used by any component. The service can be shared across all components, or it can be restricted to a particular component (any reusable logic can be put in a service). Angular CLI can be used to create services as well. The syntax is **ng generate service [name].** Use the following command to create a service called “data”:

```bash
ng generate service data
```

4. The service is created inside **src/app.** The service created has a **data.service.ts** file which has the logic and a **data.service.spec.ts** file for unit testing.

### **Congrats** ?

You have successfully created your first Angular 6 app and have also learned how to create components and services. Also now you have learned the basic folder structure of an Angular 6 project. The next part will explain the existing GitHub code to demonstrate how to use components, services, HTTP client, and communication between components.

### Part 2

#### Code

[This code](https://github.com/aditya-sridhar/simple-angular6-app) is being explained here, so clone the repo onto your local machine. The repo has instructions on how to clone it and set it up.

#### Application URL

To see how the final application looks, you can click on [this URL](https://aditya-sridhar.github.io/simple-angular6-app/). This will give you a good idea as to what the application is trying to do.

The application would look like this on a mobile screen:

![Image](https://cdn-media-1.freecodecamp.org/images/r31wXEDd34foI8fcVwbjw7xv16jQ6RcfVUlM)

#### What Does This Application Do?

The goal of the application is to display a list of customers in the form of cards. When the customer data is clicked, then the application switches to a new page which then displays the details of the selected customer.

#### Application Structure Explained

**The Components Created are:**

1. **CustomersComponent**: This corresponds to the **src/app/customers** folder. This component is to display the list of customers. The **customers.component.ts** file has a function called **ngOnInit()**. This function is called whenever the component is loaded. So this function can be used to load the data for the component. That data is loaded by calling the **getCustomerList()** function. **getCustomerList()** in turn calls the data service to get the data needed.
2. **CustomerdetailsComponent**: This corresponds to the **src/app/customerdetails** folder. This component displays the details for a single selected customer. The **customerdetails.component.ts** file has the **ngOnInit()** function which can be used to load the data. To load data, the **getCustomerDetails()** function is called. This function makes a call to the data service to get the data needed. But here you will also notice the use of **routeParams.id** which is sent to the service. **routeParams** is used to get parameters from the application URL, and the **id** parameter is used to find out for which customer the details need to be loaded. This will become more clear when I get to the routing part.
3. **DisplayComponent**: This corresponds to the **src/app/display** folder. This component displays the customer name clicked in the **CustomersComponent.** (The whole point for this component is to demonstrate parent to child component communication.) This is a child component of **CustomersComponent**_._ In **customers.component.html** you will notice that **<app-display [customer] = selectedCustomer> </app-display>**. This makes DisplayComponent a child component of **CustomersComponent**. Data is passed from **CustomerComponent** to **DisplayComponent** using the **[customer]** attribute.

#### **The Sample Data**

The sample data is present in the **src/assets/samplejson** folder.

**The services created are:**

1. **DataService**: This corresponds to **src/app/data.service.ts**. All the JSON used in the application is stored in the **src/assets/samplejson** folder. DataService helps in getting the JSON from the **src/assets/samplejson** folder using an HTTP request. In real applications, the service helps get the data from a Rest API or any other API by making an HTTP Request. This service is used by both the **CustomersComponent** and **CustomerdetailsComponent.**

**Model classes used are:**

1. **Customer**: This corresponds to **src/app/customer.ts**. This is the model class used for the **CustomersComponent** to define the structure of each customer in the list.
2. **CustomerDetails**: This corresponds to **src/app/customerdetails.ts**. This is the model class used for **CustomerdetailsComponent** to define the structure containing all the customer details.

#### **Routing Module**

The routing module is defined in **src/app/app-routing.module.ts _._** This module is then applied to the application by add `<router-outlet></router-outlet>` in app.component.html.

There are 2 routes present in the application:

1. **/customers**: This URL displays the customer list and points to **CustomersComponent.**
2. **/customerdetails/:id**: This URL displays the details for each customer and points to **CustomerdetailsComponent_._** The **id** which is present in this URL is the routeParam. This **id** in turn is used by the **CustomerdetailsComponent** to know which customer’s details to display. For Example **/customerdetails/1** will display the details of the first customer, **/customerdetails/3** will display the details of the 3rd customer, and so on.

### **Congrats again** ?

Now you know how to use components and services. Also you know how to make HTTP calls, how to use routing, and how to pass routeParams.

The basic concepts have been covered in this post, and hope it was helpful.

### References:

1. To know more about Angular you can check the documentation [https://angular.io/guide/quickstart](https://angular.io/guide/quickstart) . The Documentation is very good to understand further concepts of angular

#### About the author

I love technology and follow the advancements in technology. I also like helping others with any knowledge I have in the technology space.

Feel free to connect with me on my LinkdIn account [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

You can also follow me on twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

My Website: [https://adityasridhar.com/](https://adityasridhar.com/)

#### Other related posts by me

[A quick guide to help you understand and create ReactJS apps](https://medium.freecodecamp.org/quick-guide-to-understanding-and-creating-reactjs-apps-8457ee8f7123)

[A quick introduction to Vue.js](https://medium.freecodecamp.org/a-quick-introduction-to-vue-js-72937ee8880d)

