---
title: How Type Aliases work in TypeScript – Explained with Code Examples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-21T14:14:40.000Z'
originalURL: https://freecodecamp.org/news/how-typescript-type-aliases-work
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-1--2.png
tags:
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'One of TypeScript''s powerful features is type aliases, which allow developers
  to create custom names for types, enhancing code readability and maintainability.
  In this article, we''ll explore TypeScript type aliases through examples.

  Table of Contents...'
---

One of TypeScript's powerful features is type aliases, which allow developers to create custom names for types, enhancing code readability and maintainability. In this article, we'll explore TypeScript type aliases through examples.

## Table of Contents

* [TypeScript Type Aliases](#typescript-type-aliases)
* [Examples](#examples)
* [Conclusion](#heading-conclusion)

## What are Type Aliases in TypeScript?

Type aliases in TypeScript offer a streamlined approach to defining custom names for existing types, thereby bolstering code clarity and maintainability. The syntax is straightforward:

```typescript
type AliasName = TypeDefinition;

```

Here, `AliasName` denotes the custom name assigned to the type, while `TypeDefinition` delineates the underlying type structure. Type aliases are versatile, accommodating various types, including primitives, object types, union types, and function signatures.

## TypeScript Type Aliases Examples

### How to use the User ID Alias

```typescript
// Alias for User ID
type UserID = number;

// Usage
function getUserByID(id: UserID): User {
    // Implementation to fetch user by ID
    console.log("Fetching user with ID:", id);
    return {} as User; // Dummy return for demonstration
}

// Test
const user = getUserByID(123);
console.log("Fetched user:", user);

```

In this example, `UserID` serves as a type alias representing numerical identifiers for users. By employing the alias `UserID` instead of `number` directly, the code becomes inherently more self-descriptive. 

When declaring functions like `getUserByID`, developers immediately discern that the function anticipates a user ID as an argument, thereby augmenting code readability and conveying intent effectively.

### How to use the Post Alias

```typescript
// Alias for Post
type Post = {
    title: string;
    content: string;
    author: Username;
};

// Usage
const newPost: Post = {
    title: "Introduction to TypeScript Type Aliases",
    content: "In this article, we explore TypeScript type aliases...",
    author: "dev_guru_123",
};

// Test
console.log("New post:", newPost);

```

In this example, the `Post` type alias encapsulates the structure of a post, comprising `title`, `content`, and `author`. By leveraging the `Post` alias, the code transparently communicates the structure of a post object. Upon encountering variables like `newPost`, developers intuitively grasp the anticipated properties.

### How to use the Math Operation Alias

```typescript
// Alias for MathOperation
type MathOperation = (x: number, y: number) => number;

// Usage
const add: MathOperation = (x, y) => x + y;
const subtract: MathOperation = (x, y) => x - y;

// Test
console.log("Addition result:", add(5, 3));
console.log("Subtraction result:", subtract(8, 3));

```

Here, the `MathOperation` alias represents a function accepting two numbers (`x` and `y`) as input parameters and yielding a number as output. 

By employing the `MathOperation` alias, the code distinctly communicates the expected signature of mathematical operations. When defining functions like `add` or `subtract`, developers promptly grasp the input-output expectations, thereby streamlining function declaration.

### How to use the Union Type Alias

```typescript
// Alias for Result
type Result = Success | Error;

// Define Success and Error types (for demonstration purposes)
class Success {
    constructor(public data: any) {}
}

class Error {
    constructor(public message: string) {}
}

// Usage
const successResult: Result = new Success("Data loaded successfully");
const errorResult: Result = new Error("Failed to load data");

// Test
function handleResult(result: Result) {
    if (result instanceof Success) {
        console.log("Success:", result.data);
    } else {
        console.error("Error:", result.message);
    }
}

handleResult(successResult); // Output: Success: Data loaded successfully
handleResult(errorResult);   // Output: Error: Failed to load data

```

In this example, the `Result` alias denotes a union type encompassing `Success` and `Error`. The `handleResult` function expects a parameter of type `Result`, which may manifest as either a `Success` or an `Error`. By utilizing the `Result` alias, the code distinctly delineates the potential outcomes of an operation, fostering code comprehension, reusability, and maintenance.

### How to Extend Type Aliases

```typescript
// Base Alias for User
type BaseUser = {
    id: UserID;
    username: string;
    email: string;
};

// Extended Alias for Admin User
type AdminUser = BaseUser & {
    role: "admin";
};

// Usage
const admin: AdminUser = {
    id: 1,
    username: "admin",
    email: "admin@example.com",
    role: "admin",
};

// Test
console.log("Admin user:", admin);

```

In this example, the `BaseUser` alias encapsulates common user properties. By extending the `BaseUser` alias, we create an `AdminUser` type, augmenting it with a specific `role` property. This extension enables the definition of specialized type definitions while upholding code consistency and clarity.

## Conclusion

TypeScript type aliases improve code readability and maintainability by providing custom names for types. By clarifying code intent and simplifying structure, they streamline development and enhance overall software quality. Embrace type aliases to create cleaner, more maintainable codebases.

If you have any feedback, then DM me on [Twitter](https://twitter.com/introvertedbot) or [LinkedIn](https://www.linkedin.com/analytics/profile-views/).

