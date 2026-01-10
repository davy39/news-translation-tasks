---
title: 'How to Hide Your Angular Properties – # vs private Explained'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-20T20:39:45.000Z'
originalURL: https://freecodecamp.org/news/javascript-vs-typescript-private-in-angular-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/hash-v-private-thumbnail.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Deborah Kurata

  Have you noticed a hash symbol showing up in Angular code samples? If not, you may
  see it soon. What is the purpose of the # and when should you use it?

  The # symbol was recently added to JavaScript to denote private class propertie...'
---

By Deborah Kurata

Have you noticed a hash symbol showing up in Angular code samples? If not, you may see it soon. What is the purpose of the `#` and when should you use it?

The `#` symbol was recently added to JavaScript to denote private class properties. Making a class variable private means that the variable can only be accessed within its class. That allows us to encapsulate data we only want to access within a service.

But don't we already have a private accessor for our class fields? Yep!

Then why do we need the new hash syntax?

Let's take a look at the private accessor first, then examine the `#` syntax and why it is a better choice in our Angular applications.

You can watch the associated video here for a demonstration:

%[https://youtu.be/487iCAnhxCM]

## The Danger of Public Class Properties

Let's start by creating a property in a service and attempt to access it from our component. For this example, we have a Product service and a Product component. 

In the Product service, we create a property for the URL that we'll use to get our product data. And a `products` property to hold our retrieved array of products.

```typescript
// Product Service
@Injectable({
  providedIn: 'root'
})
export class ProductService {
  productUrl = 'api/products';
  products = [];

}
```

To verify the value of the URL, let's create a method to log it:

```typescript
// Product Service
logUrl() {
  console.log('Url:', this.productUrl);
}
```

Then we'll call that method in the Product service constructor:

```typescript
// Product Service
constructor() {
  this.logUrl();
}
```

By default, variables we define in a class are public, meaning that any other code in our application can access them. So we should be able to access our Product service properties from our component.

Let's give it a try. In the Product component, we first inject the service. In this example, we use the new `inject` function for dependency injection instead of the constructor. And add `inject` to the import statement from `@angular/core`.

Then we add a constructor. And because by default any property or method of a class is public, we can change the URL that we defined in the service. For confirmation, we'll call the service method to log the URL.

```typescript
// Product Component
productService = inject(ProductService);

constructor() {
  this.productService.productUrl = `api/nefarious`;

  this.productService.logUrl();
}
```

If we run the application and open the developer tools, we first see the service log the URL, then we see the component's changed URL (Figure 1).

![Console log includes api/products and api/nefarious](https://www.freecodecamp.org/news/content/images/2023/06/image-191.png)
_Figure 1. Resulting console output._

Well...that's not good. Our component was able to change the URL defined in our service.

## TypeScript's Private Accessibility Feature

To better protect our service properties from being modified outside of the service, we use **private accessibility**. 

Private accessibility is a feature of TypeScript. It marks a class property or method so that it is only accessible from within the class. The property or method is not available from any other component or service. 

To use private accessibility, we add the `private` keyword in front of the variable name.

```typescript
// Product Service
private productUrl = 'api/products';
```

Since we are currently modifying this property in the component, the component code now generates an error: `Property 'productUrl' is private and only accessible within class 'ProductService'.` Great! Our component can no longer access the private property from our service.

By adding the TypeScript private accessibility keyword in front of a property in the service, the variable is only accessible from that service.

But, going back to the component, what if we try to do something like this:

```typescript
// Product Component
constructor() {
  for (let i in this.productService) {
    console.log('properties:', i);
  }

  this.productService.logUrl();
}
```

The `for...in` loop iterates over the properties of an object. In this example, we display each property to the console. The result is shown in Figure 2:

![Console log includes productUrl and products](https://www.freecodecamp.org/news/content/images/2023/06/image-192.png)
_Figure 2. Resulting console output_

Notice that it displays both our public and private properties. Now that we can see the name of the private property, we can use it to update that private property.

```typescript
// Product Component
constructor() {
  for (let i in this.productService) {
    console.log('properties:', i);
  }

  this.productService['productUrl']= 'api/nefarious';
  this.productService.logUrl();
}
```

Oops! We've again modified our service property from our component. Our private property isn't so private.

Why is that? It's because the `private` keyword is part of TypeScript, not JavaScript. That means that the private accessibility is only enforced during development, as part of type checking, and during compilation. We get notifications during development and compilation that we can't access the private property from outside its class.

But when our TypeScript code is transpiled to JavaScript and executed, the private keyword is gone. That means the JavaScript runtime constructs such as our `for...in` loop or simple property lookup, can still access a property or method defined with the `private` keyword. In other words, the component can access the private properties in our service at runtime. Yikes!

## **JavaScript's Private Class Members (#)**

Using the JavaScript `#` syntax solves that problem. Recently, JavaScript added private class properties and methods, denoted with a `#`. Since the `#` is part of JavaScript, it denotes our properties and methods as private during development, compilation, and at runtime.

In the Product service, let's remove the `private` keyword and add `#`. The `#` is a prefix on the variable itself, and becomes part of the variable name. So we need to change the variable name wherever we access it, such as in our `logUrl` method.

```typescript
// Product Service
@Injectable({
  providedIn: 'root'
})
export class ProductService {
  #productUrl = 'api/products';
  products = [];

  constructor() { 
    this.logUrl();
  }

  logUrl() {
    console.log('Url:',this.#productUrl);
  }
}
```

We now see an error where we access the property in the Product component: `Property 'productUrl' does not exist on type 'ProductService'. Did you mean '#productUrl'?`

We can try changing our property lookup code in the component to include a `#` as well.

```typescript
// Product Component
constructor() {
  for (let i in this.productService) {
    console.log('properties:', i);
  }

  this.productService['#productUrl']= 'api/nefarious';
  this.productService.logUrl();
}
```

But the property is still not found: `Property '#productUrl' does not exist on type 'ProductService'`. The private property in our service is now correctly hidden from our component. We'll need to delete the property lookup line that accesses `#productUrl` for our code to compile successfully.

Looking at the console (Figure 3), notice that our `for...in loop` now finds the public `products` property, but not the private `productsUrl` property. Our private property is private and hidden, correctly encapsulated in our service.

![Console log includes products, not productUrl](https://www.freecodecamp.org/news/content/images/2023/06/image-193.png)
_Figure 3. Resulting console output_

## Wrapping Up

As Angular developers, we've been using the Typescript `private` accessibility keyword to make properties or methods private. But that only protects the property at development and compile type, not runtime.

Now we can use the JavaScript private class property syntax (denoted with the `#` symbol) to make private properties and methods truly private and hidden from other parts of our code.

To see these concepts in action, check out the demo provided in this video:

%[https://youtu.be/487iCAnhxCM]


