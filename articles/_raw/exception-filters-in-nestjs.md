---
title: How to Use Exception Filters to Catch Bugs in Nest.js
subtitle: ''
author: Okoye Chukwuebuka Victor
co_authors: []
series: null
date: '2023-06-23T21:38:23.000Z'
originalURL: https://freecodecamp.org/news/exception-filters-in-nestjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/brett-jordan-XWar9MbNGUY-unsplash.jpg
tags:
- name: debugging
  slug: debugging
- name: error handling
  slug: error-handling
- name: JavaScript
  slug: javascript
- name: nestjs
  slug: nestjs
seo_title: null
seo_desc: "It's common to find errors and bugs in your code if you're a software developer.\
  \ They might occur because of incorrect input, from passing the wrong data types,\
  \ or because of delays or response timeouts. \nAnd even though errors and bugs are\
  \ a part of..."
---

It's common to find errors and bugs in your code if you're a software developer. They might occur because of incorrect input, from passing the wrong data types, or because of delays or response timeouts. 

And even though errors and bugs are a part of life, they can stress you out and decrease your productivity. Fortunately, you can limit the number of pests in your code by taking proactive measures to prevent and fix them. 

In this article, you will learn how best to utilize exception filters to limit disruptions in your code implementations.

## What Are Exception Filters?

Exception filters are constructs of a programming language that help you handle exceptions or errors found in services or controller classes. Using these filters improves the efficiency of your codebase and makes errors more traceable, which helps you resolve them.

### What are Exception Filters in Nest.js?

Nest.js has an inbuilt exception filter interface that you import from the `@nestjs/common package`. This interface gives you precise information about exceptions you may encounter so that you can know how to fix them. 

Some built-in exception filters include `NotFoundException`, `UnauthorizedException`, and `RequestTimeOutException`, among others.

## How to Create a Custom Exception Filter

To create a custom exception filter class, you define it with a `@Catch` decorator that takes in the type of exception the filter should catch. This class then implements the `ExceptionFilter` interface. This way you will have access to the `catch` method that the interface provides. 

NestJS allows you to create your own exception filters so you can define what sort of information it should return.

```typescript
@Catch(HttpException)
export class TestExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();
    const request = ctx.getRequest<Request>();
    const status = exception.getStatus();

    response
      .status(status)
      .json({
        statusCode: status,
        timestamp: new Date().toISOString(),
        path: request.url,
      });
  }
}
```

As you can see above, the catch method takes in two argument inputs: the `exception:HttpException` and the `host:argumentsHost`. 

`HttpException` is the exception thrown when an `HTTP` request fails and returns the appropriate Error Message with a status code as a response to the client. 

The `argumentsHost` parameter provides information about the current request and response cycle. Here the code extracts the Response and Request objects from the `ArgumentsHost` object using the `switchToHttp` method. It then calls the `getStatus` method from the `HttpException` object in order to retrieve the `HTTP` status code of the error.

 A `JSON` object gets returned. It contains the status code, the error timestamp, and the request URL, setting the `HTTP` response status code to be the error status code.

Another exciting thing to note is that you can modify the status code and error message of existing exception filters like `NotFoundException` so that they display your own custom error message and status code. Here is an illustration below:

```typescript
export class NotFoundException extends HttpException {
  constructor(message: string) {
    super(message || 'Not Found', HttpStatus.NOT_FOUND);
  }
}
```

The example above shows that the `NotFoundException` class was modified to accept a `message` parameter in the constructor method or give a default value of 'Not Found'. 

By doing this you are now able to customize an error message for your `NotFoundException` class and return a `404` status code.

## How to Bind Exception Filters in Nest.js

You might be wondering how you can implement the custom or modified exception you've created for your application. Well, you use something called **binding**. 

There are several ways in which you can bind exception filters to your application. Here are three major ways you can do it:

1. Global Scope
2. Controller Scope
3. Method Scope

### **Binding using Global Scope**

Just like the name “Global” implies, it covers the entirety of a thing – in this case the application. The custom exception filter is **bonded** to the entirety of your web application by using the `useGlobalFilters()` function. An instance of your custom exception filter gets passed in before starting up the server. 

Here is an example of what that looks like:

```typescript
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalFilters(new TestExceptionFilter());
  await app.listen(3000);
}
bootstrap();
```

If you bind the exception filter to the global scope, it means that any exceptions of type `HttpException` thrown from any controller or method within the application will be handled by the `TestExceptionFilter`.

### **Binding using Controller Scope**

If you want to handle an exception that not only covers the specific methods in your application but also the entire controller with the methods in it, you can the `@UseFilters` to bind the custom exception to the controller. Check out the below is example:

```typescript
@UseFilters(TestExceptionFilter)
@Controller('users')
export class UsersController {
  @Get()
  async findUsers() {
    // ...
  }
}
```

In this example, the custom exception filter is bonded to the controller by putting it ahead of the `@Controller` decorator. This way it handles any error that comes from the routes in this controller.

### **Binding using Method Scope**

In this form of binding, you make use of the `@UseFilters` decorator to apply the Custom ExceptionFilter you defined to a method in your application. Here is an example:

```typescript
@Controller()
export class UsersController {
  @Get()
  @UseFilters(TestExceptionFilter)
  async findUsers() {
    // ...
  }
}
```

In this example, you're using the `@UseFilters` decorator to bind the `TestExceptionFilter` exception filter to the `findUsers` method. This means that if any exception occurs within the `findUsers()` method, the `TestExceptionFilter` will catch and handle it.

## Debugging Made Easier

In this tutorial, you learned about exception filters in Nest.js, and how to create custom exception filters. You also saw some different ways in which you can implement them in your applications.

All the methods discussed are good ways to handle exceptions. By implementing these techniques, you can ensure smoother application performance and provide a better user experience.

If you enjoyed reading this article, you can share and follow me on [Twitter](https://twitter.com/okoyevictorr) and [Linkedin](https://www.linkedin.com/in/officalrajdeepsingh/).

