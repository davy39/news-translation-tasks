---
title: How to Use the TypeScript satisfies Operator
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-10T17:12:59.000Z'
originalURL: https://freecodecamp.org/news/typescript-satisfies-operator
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Copy-of-Typescript-satisfies-Operator.png
tags:
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Satyam Tripathi

  In TypeScript, the satisfies operator is a very useful tool. It was introduced in
  TypeScript v4.9 as an effective way to ensure type safety.

  The satisfies operator tells you whether a given type satisfies a particular condition
  – a...'
---

By Satyam Tripathi

In TypeScript, the `satisfies` operator is a very useful tool. It was introduced in [TypeScript v4.9](https://github.com/microsoft/TypeScript/issues/50457) as an effective way to ensure type safety.

The `satisfies` operator tells you whether a given type satisfies a particular condition – and it provides this information before running your code. Also, when you're using it, you can declare a new variable to verify if an expression's type matches another type. 

In this article, you will learn all about this useful TypeScript operator. I'll explain how things were before this operator was available, and why we need it. We'll also explore real-life scenarios where you can use `satisfies` and the benefits it offers.

## What is the TypeScript `satisfies` Operator?

The TypeScript `satisfies` operator checks if a given type satisfies a specific condition or interface. It is a new and effective way to ensure type safety in TypeScript. 

`satisfies` ensures that all variables fit the definition and have all the required properties of a specific type or interface.

## Why Do You Need the `satisfies` Operator?

Let's take a look at life before the TypeScript `satisfies` operator and the problem it solves. We'll start by considering a simple example.

Let's create a type called `personInfo`, which is a union of `personName` and `otherDetails`.

```typescript
type personInfo = personName | otherDetails;

```

`personInfo` will be either `personName` or `otherDetails`. Now, we will define `personName` as a string with three possible values: '_John_', '_Jack_', and '_Justin_'.

```typescript
type personName = "John" | "Jack" | "Justin";

```

Now, we will define the `otherDetails`.

```typescript
type otherDetails = {
  id: number;
  age: number;
};

```

The `otherDetails` is an object that has two properties, `id` and `age`, which are going to be numbers. So we can say that our `personInfo` type is a union of a `string` and an `object`. Now let's create the `Person` type.

```typescript
type Person = {
  myInfo: personInfo;
  myOtherInfo: personInfo;
};

```

The `Person` type has two properties, `myInfo` and `myOtherInfo`, both of which will be of type `personInfo`. This indicates that both properties can either be `personName` or `otherDetails`. Now, let's create the variable `applicant`.

```typescript
const applicant: Person = {
  myInfo: "John",
  myOtherInfo: { id: 123, age: 22 },
};

```

As shown in the code above, the applicant `myInfo` is set to "_John_" (one of the values of the `personName` type). The `myOtherInfo` property is set to an object with the property `id` having the value `123`, and `age` having the value `22`. Now, let's imagine we want to access `myInfo` and convert it to uppercase.

```typescript
applicant.myInfo.toUpperCase();

```

Now, if we hover our mouse over the `toUpperCase()` function, we will see an error message: `Property 'toUpperCase' does not exist on type 'personInfo' and Property 'toUpperCase' does not exist on type 'otherDetails'`.

This error occurs because TypeScript is unsure whether the value of `myInfo` or `myOtherInfo` is a string or an object since we have defined our `personInfo` as a union of string and object.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_145501157f840023f204935d54e49de1.png)
_Error message because TypeScript is unsure whether the value of `myInfo` or `myOtherInfo` is a string or an object._

In order to remove this error, we have to manually validate the property as shown below:

```typescript
if (typeof applicant.myInfo === "string") {
  applicant.myInfo.toUpperCase();
}

```

Here, we first validate whether the `applicant` type is a string or not. If it is a string, we will use the string method to ensure TypeScript does not throw any error messages.

Now, suppose we have a lot of properties, and it becomes hectic to validate each and every property. In such cases, the `satisfies` operator comes in handy.

## How to Use the `satisfies` Operator

Now, developers are happy because the `satisfies` operator has come into the picture. Before this operator, we always needed to pre-validate, and it could become hectic. Now, with the help of this operator, you don't need to do all this.

Instead of defining `Person` again, we can replace it with the `satisfies` operator, as shown below:

```typescript
const applicant = {
  myInfo: "John",
  myOtherInfo: { id: 123, age: 22 },
} satisfies Person;

applicant.myInfo.toUpperCase();

```

The satisfies operator determines that the `myInfo` variable is a string and not an object. This is because, before executing the code, it checks all the values of the `Person` type. This operator ensures that we assign any value that satisfies the `Person` type to the `applicant` variable.

See the complete code below:

```typescript
type personInfo = personName | otherDetails;

type personName = "John" | "Jack" | "Justin";

type otherDetails = {
  id: number;
  age: number;
};

type Person = {
  myInfo: personInfo;
  myOtherInfo: personInfo;
};

const applicant = {
  myInfo: "John",
  myOtherInfo: { id: 123, age: 22 },
} satisfies Person;

```

**Note:** If we try to add something to the `myInfo` property that does not correspond to the defined type, an error will occur. For example, in this case, `myInfo` should be a string, but if we assign a boolean value, an error will be generated.

You may get an error if you are not using the TypeScript `satisfies` operator and you define an object with a different property. For example, in our scenario the age is a `boolean` value, so it does not satisfy the requirement (data should be either a `string` or an `object`).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_6eb976f68482f623c0db89fb5130c0b6.png)
_Red line in age and in the toUpperCase() shows you are not using the satisfies operator._

You can see that there is a red line in `age` and in the `toUpperCase()` function. This shows that if you are not using the `satisfies` operator and you are trying to make changes to other objects, you will get an error.

Here, the problem was only with the `age`, but we are also getting an error while changing the `myInfo`.

If you use the `satisfies` operator, you will not encounter errors in other objects. In this case, the issue is with the `age`, which should be either a `string` or an `object` but is instead a `boolean`. Therefore, the error is specific to the `age` variable and does not affect the other objects.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_e1066360bb78289236ec5574be935af0.png)
_Error is specific to age variable and does not affect the other objects._

When you hover over the age, you will see the following error message:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_3bba64495ec8e5783fcb92eb78f1afa5.png)
_When you hover over the age, you will see the error message._

Thanks to the TypeScript `satisfies` operator for pre-validation.

**Note:** To resolve the above error, you can modify the the `age` property of the `otherDetails` object. You can inlcude the boolean in the age as shown below:

```typescript
type otherDetails = {
  id: number;
  age: number | boolean;
};

```

Now, the below code will not throw any error because we have already mentioned that our age could be either a `number` or `boolean`.

```typescript
type personInfo = personName | otherDetails;

type personName = "John" | "Jack" | "Justin";

type otherDetails = {
  id: number;
  age: number | boolean;
};

type Person = {
  myInfo: personInfo;
  myOtherInfo: personInfo;
};

const applicant = {
  myInfo: "John",
  myOtherInfo: { id: 123, age: true },
} satisfies Person;

applicant.myInfo.toUpperCase();

```

### Property Name Constraining

We can use the `satisfies` operator to ensure that only a subset of the keys are included. In the below code, we have 5 keys and our code states that the person object should satisfy the `Partial<Record<Keys, string | number>>` type.

```typescript
type Keys = "personID" | "personName" | "personEmail" | "personAge" | "personPhone";

const person = {
  personID: 12345,
  personName: "Jacky",
  personEmail: "jacky@testing.com",
  personAge: 22,
} satisfies Partial<Record<Keys, string | number>>;

person.personName.toUpperCase();
person.personAge.toFixed();

```

`Partial<Record<Keys, string | number>>` will create an object that will have all five keys and values (which can be a `string` or a `number`). Currently, our person object has only four properties: `personID`, `personName`, `personEmail`, and `personAge`. All the properties of the person object satisfy the properties of the partial type.

### Property Name Fulfillment

Here, we are checking if all properties of the person object satisfy the `Record<Keys, string | number>`.

`Record<Keys, string | number>` will create a record type that has 4 properties, each of which can be either a `string` or a `number`.

```typescript
type Keys = "personID" | "personName" | "personEmail" | "personAge";

const person = {
  personID: 12345,
  personName: "Jacky",
  personEmail: "jacky@testing.com",
  personAge: 22,
} satisfies Record<Keys, string | number>;

person.personName.toUpperCase();
person.personAge.toFixed();

```

Now, if we remove one property from the `person` object, then the code will throw an error, this is because the `person` object will remain only 3 properties which will not satisfy the `record` type.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_159790f137c6c0b380a6beff3201231b.jpg)
_`person` object has only 3 properties which will not satisfy record type._

### Property Value Conformance

As discussed in the `property name constraining`, the `satisfies` operator was able to restrict the names of properties in an object. However, it can also restrict the values of those properties.

Let's consider the example below. We have defined an object called `pcStore` which contains various pcs. Each pc in the `pcStore` object follows the properties defined in the `PC` type.

In `pc4`, we have mistakenly represented the `price` as a `string`, which is incorrect. The `PC` object specifies that the `price` property should be a `number`. 

To identify and catch this error, we can use the `satisfies` operator. It will determine whether all the properties in `pcStore` following the `PC` type or not.

```typescript
type PC = { name: string; ram: string; price: number };

const pcStore = {
  pc1: { name: "Dell", ram: "10 GB", price: 12000 },
  pc2: { name: "HP", ram: "8 GB", price: 11000 },
  pc3: { name: "Asus", ram: "6 GB", price: 13000 },
  pc4: { name: "Mac", ram: "20 GB", price: "21000" },
} satisfies Record<string, PC>;

```

If we hover the mouse over the price, TypeScript throws an error indicating that the `string cannot be assigned to a variable of type number`. This error occurs because the `price` variable is declared as a `number`, but we are trying to assign it a `string` value.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/upload_2a7a4636ae3870ac3c9e48825f9416b7.jpg)
_We are trying to assign the string to the price object, but a string is not assignable to a number._

The `satisfies` operator will catch the error before you run the code.

## Benefits of TypeScript's `satisfies` Operator

The `satisfies` operator allows us to check if an object has a specific property. The It can help with type safety, code correctness, validation, code reusability, and code organization.

### Type Safety

You can use the `satisfies` operator to check if an object satisfies a particular type or not. This can make your code more reliable and decrease the chances of errors in the code.

### Validation

You can also use the `satisfies` operator to validate user input. It enables us to verify if an expression type matches another type. For example, you can use it to check if the user's email matches the string type or not.

### Code Correctness

The `satisfies` operator also lets you check if the code is correct or not. It verifies if a particular object satisfies all the required properties.

### Code Reusability

The `satisfies` operator helps make code more reusable. It ensures that different blocks of code can work with the same types of data and follow the same properties.

### Code Organization

Based on the type of value, you can divide your code into different blocks, which can make the code easier to read and manage.

## Conclusion

The `satisfies` operator can make your code reusable and maintainable. The best thing about the satisfies operator is that it pre-validates the values and provides the best type-checking experience. 

You can also use the satisfies operator to restrict the names and values of any property, as we have discussed in the section Property Name Constraining and Property Value Conformance.

Thank you for reading!

