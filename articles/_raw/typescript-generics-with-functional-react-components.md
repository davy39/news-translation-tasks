---
title: How to Use TypeScript Generics with Functional React Components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-27T18:53:32.000Z'
originalURL: https://freecodecamp.org/news/typescript-generics-with-functional-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/federico-beccari-ahi73ZN5P0Y-unsplash.jpg
tags:
- name: generics
  slug: generics
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: "By Olasunkanmi Balogun\nIn this article, we will explore the powerful synergy\
  \ between TypeScript generics and functional React components. \nGenerics allow\
  \ you to define flexible components that can adapt to different data structures\
  \ and enforce type s..."
---

By Olasunkanmi Balogun

In this article, we will explore the powerful synergy between TypeScript generics and functional React components. 

Generics allow you to define flexible components that can adapt to different data structures and enforce type safety throughout your codebase. 

By leveraging Generics in functional components, you can create highly reusable and adaptable UI elements that can seamlessly handle varying data requirements.

In this tutorial, we'll begin by understanding the concept of generics in TypeScript and how they can be beneficial in the context of React development. 

We will then dive into practical examples, demonstrating how to define generic functional components in React using TypeScript. 

We'll also discuss various use cases where generic props shine, enabling us to build versatile and scalable React applications.

## What are Generics in TypeScript?

In order to explore functional components with generics, you need to grasp the fundamentals of generic functions in TypeScript – including their definition and implementation. 

In this section, you'll get a concise overview of what generics are and how to implement them in TypeScript. This should equip you with the necessary knowledge to delve deeper into the realm of functional components.

### How to declare a generic function in TypeScript

To declare a generic function in TypeScript, we place a generic type parameter, denoted as `<T>`, at the beginning of the function signature. This `<T>` represents a type that will be passed when the function is used. It serves as a placeholder for a specific type that will be determined during runtime, similar to how parameters behave in regular functions. 

For instance, consider the following function:

```ts
function func<T>(value: T):T[] {
   return [value];
}

func('Hello John');
```

In this example, the generic type parameter `T` is used to denote that the value parameter and the return type will be of the same type. 

When the `func` function is called with the argument `'Hello John'`, the inferred type for `T` becomes `string`. As a result, the return type of the function is `string[]`, indicating that an array containing the provided string value will be returned.

### How to define generics with arrow functions in TypeScript

The syntax for defining a generic function with arrow functions is slightly different from that of the function declaration we've seen before:

```ts	
export const func = <T>(value: T):T[] => {
   return [value];
}

func('Hello John');
```

From the above, we see that when using arrow functions to define generic functions in TypeScript, we employ the `<T>` syntax before the parameter list to indicate a generic type parameter.

Moving on, it's important to note that the generic type parameter `T` used in the previous examples is merely a descriptive name and can be replaced with any other valid identifier. For example:

```ts
export const func = <K>(value: K):K[] => {
   return [value];
}

func('Hello John');
```

The generic type parameter `T` has been replaced with `K`, showcasing that the choice of name for the generic type is flexible and can be customized to match the context or developer preference. 

The function `func` remains generic, capable of accepting any type specified during usage and returning an array of that same type.

Now that you know how to implement generic functions and understand their flexibility in returning any passed type, we'll now learn how to implement generic components in React. 

In the following section, I'll provide a step-by-step walkthrough of how to create and utilize generic components. This will help you harness the power of generics in React development.


## How to Define and Use Generic Components in React

Just like with generic functions, you can take component reusability to the next level by designing generic components with the integration of TypeScript generics. 

Declaring the generic props that a generic component will accept is the initial step in designing the component. We can build a parameterized props interface that supports different data types by using TypeScript generics.

```ts
interface MyComponentProps<T> {
  data: T;
  // Add additional props specific to your component
}
```

Once the generic props interface is defined, you can then implement the generic component itself. This involves using the declared generic props and integrating them into the component's structure. 

Similar to the TypeScript function description in the previous section, it has the same implementation.

```tsx
function MyComponent<T>({ data }: MyComponentProps<T>) {

  return (
    <div>
      {/* JSX content */}
    </div>
  );
}
```

Following this, you can also define generic components using arrow function syntax. But this is different when you are writing your code in a `JSX.Element` file.

To avoid ambiguity between generic type parameters and a `jsx` component, you add a trailing comma to the type parameter to differentiate it from a `JSX.Element`. For example:

```tsx
interface MyComponentProps<T> {
  data: T;
}
// notice the trailing comma after <T
const MyComponent = <T,>({ data }: MyComponentProps<T>) => {
  return (
  <div>{JSX content}</div>;
  )
};
export default MyComponent;
```

### Example Use Case Of Generic Components

Let's say you want to develop a data visualization dashboard capable of presenting data from diverse sources, each with its unique structures and properties. But you want to create a reusable component that can generate a summary of any data object, focusing on a specific property.

This scenario provides an opportunity to delve into a practical application of a generic component in React. 

By extending the type parameter to an `object` and utilizing the `keyof` operator within the interfaces, you can construct a component that offers both flexibility and type safety. 

This approach harnesses the capabilities of TypeScript's robust type system, empowering you to work with a variety of objects seamlessly.

To achieve this, define a generic component called `Summary<T>` that accepts a type parameter `T` extending an object. You'll also use the `keyof` operator to specify the property of the object that you want to display in the summary:

```ts
interface SummaryProps<T extends object, K extends keyof T> {
  data: T;
  property: K;
}

export function Summary<T extends object, K extends keyof T>({
  data,
  property,
}: SummaryProps<T, K>) {
  const value = data[property] as string;

  return (
    <div>
      {(typeof property === "string") ? (
        <p>
          {property}: {value}{" "}
        </p>
      ) : (
        ""
      )}
    </div>
  );
}
```

In the `Summary` component, we defined a generic type parameter `T` that extends `object`, ensuring that data passed to the component is an `object` type. 

The second type parameter `K` uses the `keyof` `T` notation, indicating that it must be a key of the `T` object type. This way, you can access a specific property of the data object based on the provided property value.

Within the component, we extracted the value from the data `object` using the `property` as the key. To ensure the value is treated as a `string`, we used the `as` keyword to perform a type assertion: `data[property] as string` to avoid assignment errors. This type assertion tells TypeScript to treat the value as a `string`.

The component then returns a `<div>` element containing a conditional rendering of a `<p>` element. The code then checks if the `property` is of type `string` using `typeof property === "string"`. In this way, it also prevents assignment mistakes.

If it evaluates to `true`, the code renders the `<p>` element, displaying the `property` and `value`. Otherwise, an empty `string` gets returned.

Having defined the component, let's consider an example where you have two different data sources: `User` and `Product`. Each data source has its own properties, but you want to display a summary based on a specific property.

You can start by defining the `User` interface to represent user data, specifying properties such as `id`, `name`, and `email`. Similarly, create the `Product` interface to represent product data, including properties like `id`, `name`, and `price`, like this:

```tsx
interface User {
  id: number;
  name: string;
  email: string;
}

interface Product {
  id: number;
  name: string;
  price: number;
}
```

Next, you can create instances of these data objects. For example, `userData` can represent a `user` and `productData` can represent a `product`, with their respective properties filled with sample data:

```ts
const userData: User = {
  id: 1,
  name: "John Doe",
  email: "johndoe@example.com"
};

const productData: Product = {
  id: 1,
  name: "Smartphone",
  price: 999
};
```

To utilize the `Summary` component, provide it with different data sources and specify the property you want to display in the summary. 

For instance, you can use `<Summary<User, "name">>` to render a summary of the user's name, and `<Summary<Product, "price">>` to display the price of the product:

```ts
<Summary<User, "name"> data={userData} property="name" />
<Summary<Product, "price"> data={productData} property="price" />
```

The full code looks like this:

```ts
interface User {
  id: number;
  name: string;
  email: string;
}

interface Product {
  id: number;
  name: string;
  price: number;
}

const userData: User = {
  id: 1,
  name: "John Doe",
  email: "johndoe@example.com"
};

const productData: Product = {
  id: 1,
  name: "Smartphone",
  price: 999
};

// Usage of Summary component with different data sources and properties
<Summary<User, "name"> data={userData} property="name" />
<Summary<Product, "price"> data={productData} property="price" />
```

TypeScript's powerful type inference mechanism comes into play in this scenario. When you provide the `data` and `property` to the `Summary` component, TypeScript ensures that the specified property is valid for the corresponding data source. 

If you mistakenly attempt to use an invalid property, such as providing `"email"` as the property for the `Product` data, the TypeScript compiler will raise a type error. This ensures type safety and helps prevent potential runtime issues.

By leveraging TypeScript's static type checking, we gain the benefits of type safety and validation when working with generic components like `Summary`. This also helps catch errors early in the development process and ensures that the provided `data` and `property` combinations are correct.

## Conclusion

In this guide, we have explored the concept of generics in TypeScript and how they can be applied to create powerful and reusable components in React. 

Generics allow us to define components that are flexible enough to work with various data types while maintaining type safety.

Throughout this article, you learned generics fundamentals, including the implementation of generic functions. We then delved into the world of generic components in React, demonstrating how to define and implement them using both `arrow` and `named` function methods.

As you continue your journey with TypeScript, I encourage you to explore further the power and flexibility of generic props. By utilizing generics, you can unlock new possibilities in creating reusable and type-safe components that empower your React applications. Happy coding! 


