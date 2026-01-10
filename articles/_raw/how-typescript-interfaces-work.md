---
title: How TypeScript Interfaces Work – Explained with Examples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-23T10:59:53.000Z'
originalURL: https://freecodecamp.org/news/how-typescript-interfaces-work
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-2--1.png
tags:
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'TypeScript, a superset of JavaScript, has gained widespread adoption among
  developers due to its ability to provide static typing, enhancing code robustness
  and maintainability.

  One of TypeScript''s key features is interfaces, which play a pivotal rol...'
---

TypeScript, a superset of JavaScript, has gained widespread adoption among developers due to its ability to provide static typing, enhancing code robustness and maintainability.

One of TypeScript's key features is interfaces, which play a pivotal role in defining the shape of objects, enabling type checking and facilitating better code organization. In this article, we'll delve deep into TypeScript interfaces, exploring their syntax and use cases.

You can get all the source code from [here](https://github.com/dotslashbit/fcc-article-resources/blob/main/ts-interfaces/index.ts).

## What are TypeScript Interfaces?

At its core, an interface in TypeScript is a syntactical contract that defines the expected structure of an object. It provides a way to describe the shape of objects, including their properties and methods, without implementing any functionality. Interfaces solely focus on the structure and type-checking aspects, allowing for better code understanding and validation during development.

## Syntax of TypeScript Interfaces

The syntax of a TypeScript interface is straightforward:

```typescript
interface InterfaceName {
    property1: type;
    property2: type;
    // Additional properties and methods can be defined here
}

```

Here's a breakdown of the syntax elements:

* `interface`: Keyword used to define an interface.
* `InterfaceName`: Name of the interface following TypeScript naming conventions.
* `property1`, `property2`: Properties of the interface.
* `type`: TypeScript type annotation defining the type of each property.

## TypeScript Interfaces Use Cases

### How to define Object Structures

A fundamental application of TypeScript interfaces is seen in defining object structures. Imagine a scenario where you're tasked with managing various shapes within a project. Here, you can employ an interface to represent a generic geometric shape:

```typescript
interface Shape {
  name: string;
  color: string;
  area(): number;
}

console.log("Use Case 1: Defining Object Structures");
console.log("-----------------------------------------");

// Define a function to calculate the area of a shape
function calculateArea(shape: Shape): void {
  console.log(`Calculating area of ${shape.name}...`);
  console.log(`Area: ${shape.area()}`);
}

// Define a circle object
const circle: Shape = {
  name: "Circle",
  color: "Red",
  area() {
    return Math.PI * 2 * 2;
  },
};

// Calculate and log the area of the circle
calculateArea(circle);

```

Output:

```
Use Case 1: Defining Object Structures
-----------------------------------------
Calculating area of Circle...
Area: 12.566370614359172

```

In this use case, we define an interface called `Shape` to represent the structure of geometric shapes. The `Shape` interface contains properties `name` and `color`, both of type `string`, and a method `area()` that returns a `number`. We then define a circle object that adheres to the `Shape` interface, specifying its properties and implementing the `area()` method to calculate its area.

### How to Type-Check Function Parameters

Another pivotal role of interfaces is in type-checking function parameters during compile-time. Consider a function tasked with calculating the perimeter of a shape:

```typescript
function calculatePerimeter(shape: Shape): number {
  // Implementation
}

console.log("\nUse Case 2: Type-Checking Function Parameters");
console.log("----------------------------------------------");

// Attempt to call the function with a shape object
console.log("Calculating perimeter of a shape...");
console.log(`Perimeter: ${calculatePerimeter(circle)}`); // Compiler error: Argument of type 'Shape' is not assignable to parameter of type 'Shape'.

```

Output:

```
Use Case 2: Type-Checking Function Parameters
----------------------------------------------
Calculating perimeter of a shape...

```

```
Error: Argument of type 'Shape' is not assignable to parameter of type 'Shape'.

```

Here, we demonstrate how interfaces enable type-checking of function parameters. We have a function `calculatePerimeter()` that takes an object of type `Shape` as a parameter. When we attempt to call this function with a `circle` object, TypeScript raises a compiler error because the `circle` object does not precisely match the expected `Shape` interface, ensuring type safety during development.

### How to Implement Class Contracts

Interfaces also serve as effective means to enforce contracts on classes, ensuring they adhere to specific properties and methods. Let's exemplify this by creating a `Circle` class that implements the `Shape` interface:

```typescript
class Circle implements Shape {
  constructor(public name: string, public color: string, public radius: number) {}

  area(): number {
    return Math.PI * this.radius * this.radius;
  }
}

console.log("\nUse Case 3: Implementing Class Contracts");
console.log("------------------------------------------");

// Create an instance of the Circle class
const myCircle = new Circle("My Circle", "Blue", 3);

// Log the area of the circle
console.log(`Area of ${myCircle.name}: ${myCircle.area()}`);

```

Output:

```
Use Case 3: Implementing Class Contracts
------------------------------------------
Area of My Circle: 28.274333882308138

```

Here, we demonstrate how interfaces enable type-checking of function parameters. We have a function `calculatePerimeter()` that takes an object of type `Shape` as a parameter. When we attempt to call this function with a `circle` object, TypeScript raises a compiler error because the `circle` object does not precisely match the expected `Shape` interface, ensuring type safety during development.

### How to Extend Interfaces

Interfaces can extend other interfaces, enabling composition and reuse of interface definitions. Let's extend the `Shape` interface to encompass additional properties for 3D shapes:

```typescript
interface ThreeDShape extends Shape {
  volume(): number;
}

console.log("\nUse Case 4: Extending Interfaces");
console.log("----------------------------------");

// Define a function to calculate the volume of a 3D shape
function calculateVolume(shape: ThreeDShape): void {
  console.log(`Calculating volume of ${shape.name}...`);
  console.log(`Volume: ${shape.volume()}`);
}

// Define a class for a 3D shape
class Sphere implements ThreeDShape {
  constructor(public name: string, public color: string, public radius: number) {}

  area(): number {
    return 4 * Math.PI * this.radius ** 2;
  }

  volume(): number {
    return (4 / 3) * Math.PI * this.radius ** 3;
  }
}

// Create an instance of the Sphere class
const mySphere = new Sphere("My Sphere", "Green", 4);

// Calculate and log the volume of the sphere
calculateVolume(mySphere);

```

Output:

```
Use Case 4: Extending Interfaces
----------------------------------
Calculating volume of My Sphere...
Volume: 268.082573106329

```

Here, we demonstrate how interfaces enable type-checking of function parameters. We have a function `calculatePerimeter()` that takes an object of type `Shape` as a parameter. When we attempt to call this function with a `circle` object, TypeScript raises a compiler error because the `circle` object does not precisely match the expected `Shape` interface, ensuring type safety during development.

## Conclusion

In conclusion, TypeScript interfaces emerge as potent tools for defining contracts within your codebase, ensuring type safety, and fostering code maintainability. By harnessing interfaces, you can establish clear expectations for object structures, function parameters, class contracts, and more. 

Whether you're working on a modest application or an extensive enterprise project, mastering interfaces is indispensable for crafting clean, dependable, and maintainable TypeScript code.

If you have any feedback, DM me on [Twitter](https://twitter.com/introvertedbot) or [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).

