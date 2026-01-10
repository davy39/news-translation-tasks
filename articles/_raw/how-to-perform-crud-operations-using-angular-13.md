---
title: How to Perform CRUD Operations using Angular 13
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-14T19:49:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-crud-operations-using-angular-13
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/How-to-Build-a-Weather-Application-using-React--82-.png
tags:
- name: Angular
  slug: angular
- name: crud
  slug: crud
seo_title: null
seo_desc: "By Nishant Kumar\nBuilding a full-stack application can be tough. And the\
  \ base of building such an application is learning how to perform CRUD operations\
  \ – Create, Read, Update, and Delete. \nIt's by using these operations that we manage\
  \ the data flow ..."
---

By Nishant Kumar

Building a full-stack application can be tough. And the base of building such an application is learning how to perform CRUD operations – Create, Read, Update, and Delete. 

It's by using these operations that we manage the data flow between the client application and the server.

So, in this article, you'll learn how to perform CRUD operations in Angular using Angular Services.

Let's dive in.

## But What are Angular Services?

Angular Services are methods that are triggered when we want to perform a certain operation in an Angular Application. In our case, they are the methods that will perform CRUD Operations. In other words, we will have a service that will Create data in the database. Just like that, we will have difference services for Reading Data from the server, Updating data in the server, as well as deleting data.

## Base Setup

Create a folder called Angular CRUD in your system. And inside that folder, create two files. One is the client, and the other is the server.

The **client** will contain our Angular Application, and the **server** will have the backend code for the server, built using Node, Express, and MongoDB.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-185153.jpeg)

If you want to learn how to design and develop a RESTful API, you can watch my video on [RESTful APIs - Build a RESTful API using Node, Express, and MongoDB](https://youtu.be/paxagc55loU). You can also refer my blog on [How to Build a RESTful API Using Node, Express, and MongoDB](https://www.freecodecamp.org/news/build-a-restful-api-using-node-express-and-mongodb/).

But if you want just the code, you can just get it from [GitHub](https://github.com/nishant-666/Rest-Api-Express-MongoDB).

Add this backend code in the server folder, and then run it using **npm start**. Don't forget the use **npm install** to install the packages first.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-185814.jpeg)

Now, in the client folder, add the starter code for the Angular Project from the repository below. It's just a form that prints the name and age in the console. 

Do an **`npm i`** here as well before running the project. And to run the project, just do **`ng serve`**.

Angular Stater Code: [https://github.com/nishant-666/Angular-crud/tree/Stater-Code](https://github.com/nishant-666/Angular-crud/tree/Stater-Code)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-190334.jpeg)

And here is our output which has two inputs and a submit button.

## How to Write Services for CRUD Operations

Now, let's write services for the CRUD Operations. But we need to generate a service component first. Let's call this services **users**.

To generate a new service, simply type the following command in a new terminal:

```
ng g s users
```

Here, **g** is short for generate and **s** is short for service, followed by the service name, which is users.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-190732.jpeg)

And the service has now been created. You can check the newly created service into the **app** folder.

```
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  constructor() { }
}

```

Now, let's write the code for the read service that gets data from the database. For that, we need the **HttpClientModule**, in order to send or receive **http requests.**

We will do it into the **app.module.ts**, because that's where all the imports are.

```
import { HttpClientModule } from '@angular/common/http';
```

And then add this **HttpClientModule** in the list of imports:

```
imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
 ],
```

Here is the whole **app.module.ts** for your reference:

```
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

```

Now, we can send **http** requests from our application.

To receive data from the backend, let's create a service. Into the users.service.ts, import **HttpClient** and **Observable.** 

```
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
```

So, we will send requests to the backend API using this **HttpClient**, and we will receive the incoming data using an **observable.**

Now, let's create an instance of HttpClient in the constructor.

```
constructor(private http: HttpClient) { }
```

Let's also define the base URL for the backend API. If you check the server folder, you will see a file called **index.js.** And here, we have this base endpoint **/api**.

```
private baseURL = `http://localhost:3000/api`
```

```
app.use('/api', routes)
```

## How to Create a Service for Getting the Data

Create a function that will run every time we send a **GET** request to the server.

```
getAllData(): Observable<any> {
   return this.http.get(`${this.baseURL}/getAll`)
}
```

This **getAll** is the route for the getting all the data. So, we are appending the **baseURL** with the route path.

Now, we have to call this function wherever we want to show the incoming data. Let's do it in the **app.component.ts.**

First, import the service.

```
import { UsersService } from './users.service';
```

Then, create an instance of this service in the constructor.

```
constructor(
    private userService: UsersService
  ) { }
```

Then, in **ngOnInit**, call the function in the **userService**. Also, subscribe to the incoming data using **subscribe**.

```
ngOnInit() {
    this.userService.getAllData()
      .subscribe(data => {
        console.log(data)
      })
  }
```

So, this **ngOnInit** runs when the page loads, which is the equivalent of the **useEffect Hook** and **componentDidMount** in React.

And this subscribe returns us the incoming data from the backend server.

Now, let's check the console.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-192702.jpeg)

We don't have any data in the database, that's why we are getting an empty array.

## How to Create a Service for Adding Data

Now, let's create a service for adding some data to the backend database using the backend server.

```
postData(data: any): Observable<any> {
    return this.http.post(`${this.baseURL}/post`, data)
}
```

This is very similar to the read service. The only difference is that it takes two arguments, not one. One is the endpoint, and the other is the data which we are going to post. And we will pass this data from our **app.component.ts.**

In the **app.component.ts** file, create a function submitData. It should contain a body object that will be sent.

```
 submitData(value: any) {
    let body = {
      name: value.name,
      age: value.age
    }
  }
```

Then, we will post this body like this:

```
this.userService.postData(body)
  .subscribe(response => {
    	console.log(response)
})
```

So, think about it like this. We are sending the body in the userService.postData function, and it's getting received on the other end as **data** arguments, in the services. And then, we are simply posting it.

```
postData(data: any): Observable<any> {
    return this.http.post(`${this.baseURL}/post`, data)
}
```

Here is the whole submitData function for your reference:

```
submitData(value: any) {
    let body = {
      name: value.name,
      age: value.age
    }

    this.userService.postData(body)
      .subscribe(response => {
        console.log(response)
      })
  }
```

Now, let's add some data.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-193534.jpeg)

Add some name and age, and click Add Data.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-193610.jpeg)

And it will be added. Refresh the page, and you will see that the read data service is working as well, because we will be getting the incoming data.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-193645.jpeg)

## How to Create a Service for Updating and Deleting Data

Now, let's create the services for updating and deleting data.

```
updateData(data: any, id: string): Observable<any> {
    return this.http.patch(`${this.baseURL}/update/${id}`, data)
}
```

So, this **updateData** service takes two arguments. One is the id of the document we are going to update, and the second is the new data that will replace the previous data. The **updateData** uses the patch method to update the data.

We will use the id as path parameters. It will be appended in the **http.patch** method. And we will pass the new data, too.

Similarly, we have the **deleteData** service. This only takes the id as arguments, and it will be removed. The **deleteData** uses the `delete` method to delete the data.

```
deleteData(id: string): Observable<any> {
    return this.http.delete(`${this.baseURL}/delete/${id}`)
}
```

Import the updateData function into the **app.component.ts** file.

```
updateData(value: any) {
    let body = {
      name: value.name,
      age: value.age
    }

    this.userService.updateData(body, `622ca8c59f6c668226f74f52`)
      .subscribe(response => {
        console.log(response)
      })
  }
```

Here, we're passing the new updated body and the id of the document that we want to update.

```
<form #loginForm="ngForm" (ngSubmit)="updateData(loginForm.value)">
  <div class="main">
    <div class="input-fields">
      <input name="name" ngModel placeholder="Name" id="name" type="text" class="input-field" />
    </div>
    <div class="input-fields">
      <input name="age" ngModel placeholder="Age" id="age" type="number" class="input-field" />
    </div>
    <button>Update Data </button>
  </div>
</form>
```

Also, change the function in **app.component.html** as well, in the form tags.

So, if we add some new data in the input fields, it will replace the old data for the id **622ca8c59f6c668226f74f52.** Because that is the data and id we are passing.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-194634.jpeg)

Let's add this new data in the form, and click the Update Data button. You will see that the data will be updated and it will be in the console.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-194708.jpeg)

To delete data, create a function in app.component.ts called **delete,** and add the **deleteData** service inside it. 

```
delete() {
    this.userService.deleteData(`622c573cf23ce54e445b2bed`)
      .subscribe(response => {
        console.log(response);
      })
  }
```

Also, change the HTML button text and the function. 

```
<form #loginForm="ngForm" (ngSubmit)="delete()">
  <div class="main">
    <div class="input-fields">
      <input name="name" ngModel placeholder="Name" id="name" type="text" class="input-field" />
    </div>
    <div class="input-fields">
      <input name="age" ngModel placeholder="Age" id="age" type="number" class="input-field" />
    </div>
    <button>Delete Data </button>
  </div>
</form>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-195125.jpeg)

Open the Newtork tab in Chrome Dev Tools, and click the Delete Data button. It will delete the document with the id of **622ca8c59f6c668226f74f52,** because that is what we are passing to the **deleteData** service.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-12-195807.jpeg)

And we will get this confirmation message.

## Wrapping Up

So, that is how we do **CRUD operations** in Angular 13 using Services.

You can also check my video on [Let's perform CRUD Operations with Angular 13 - Full Tutorial for Beginners](https://youtu.be/O-MAtagUJjM)

Get the full code here: [https://github.com/nishant-666/Angular-crud/tree/Finished-Code](https://github.com/nishant-666/Angular-crud/tree/Finished-Code)

