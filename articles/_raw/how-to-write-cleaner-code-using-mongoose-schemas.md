---
title: How to Write Cleaner Code Using Mongoose Schemas
subtitle: ''
author: ِAya Nabil Othman
co_authors: []
series: null
date: '2024-09-06T13:44:56.627Z'
originalURL: https://freecodecamp.org/news/how-to-write-cleaner-code-using-mongoose-schemas
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725431278897/86823d79-7b9c-4512-a834-edcdd4e11ac3.jpeg
tags:
- name: mongoose
  slug: mongoose
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: dry
  slug: dry
- name: APIs
  slug: apis
seo_title: null
seo_desc: 'If you are used to building NodeJS applications using the Mongoose ORM,
  this article is for you. In it, we''ll discuss some cool features of Mongoose schemas
  that''ll help you write more organized and maintainable code.

  To get the most out of this guid...'
---

If you are used to building NodeJS applications using the Mongoose ORM, this article is for you. In it, we'll discuss some cool features of Mongoose schemas that'll help you write more organized and maintainable code.

To get the most out of this guide, you should have a background in JavaScript, understand how Mongoose works, and know Object-Oriented Programming basics.

### Here's what we'll cover:

1. [What is a Mongoose Schema?](#heading-what-is-a-mongoose-schema)
    
2. [Discriminator](#heading-discriminator)
    
3. [Statics](#heading-statics)
    
4. [Methods](#heading-methods)
    
5. [Query Builder](#heading-query-builder)
    
6. [Hooks](#heading-hooks)
    
7. [Summary](#heading-summary)
    

## W**hat is a Mongoose Schema?**

Mongoose schemas provide a structured way to model data in a MongoDB database, allowing you to define the properties and behavior of the documents. Schemas serve as a blueprint for a document that gets saved in the database. They enables developers to enforce data integrity and work with MongoDB in a more intuitive and organized manner.

Within a MongoDB collection, a schema outlines the fields of the documents, their data types, validation rules, default values, constraints, and more.

Programmatically, a Mongoose schema is a JavaScript object. Actually, it is an instance of a built-in class called `Schema` inside the `mongoose` module. For this reason, you can add more methods to its prototype. This will help you implement many features as middleware, methods, statics, and more. You will learn about some of them in this tutorial.

### **Features you'll learn how to implement:**

* [Discriminator](#discriminator)
    
* [Statics](#statics)
    
* [Methods](#methods)
    
* [Query Builder](#query-builder)
    
* [Hooks](#hooks)
    

## Discriminator

A discriminator is a feature that enables you to create multiple models (subtypes) that inherit from a base model (parent). This happens by defining a base schema and then extending it with extra fields specific to each subtype or each child schema.

All documents, regardless of their specific model, are stored in the same MongoDB collection. This keeps your data organized in a single collection while allowing for flexible querying and data management. Also, each document includes a special field that indicates its specific model type, allowing Mongoose to distinguish between the different subtypes.

**How to use** `discriminator`**:**

1. Start by defining a base schema, which will have the common fields among the subtypes. After that, create a model from it.
    
    ```javascript
    import mongoose from 'mongoose';
    
    const baseSchema = new mongoose.Schema({
        name: { type: String, required: true },
    }, { discriminatorKey: 'kind' }; // defaults to '__t');
    
    const BaseModel = mongoose.model('Base', baseSchema);
    ```
    
2. Create the subtypes that extend the base schema by defining the `discriminator` for each one.
    
    ```javascript
    const catSchema = new mongoose.Schema({
        meow: { type: Boolean, default: true }
    });
    // subtype
    const Cat = BaseModel.discriminator('Cat', catSchema);
    
    const dogSchema = new mongoose.Schema({
        bark: { type: Boolean, default: true }
    });
    // subtype
    const Dog = BaseModel.discriminator('Dog', dogSchema);
    ```
    
3. You can then create documents in the regular way. All the documents will be stored in the same collection, but each has its own type depending on its subtype model.
    
    ```javascript
    const fluffy = await Cat.create({ name: 'Fluffy' });
    const rover = await Dog.create({ name: 'Rover' });
    ```
    

### `discriminator` use case:

Let's say that you're building a multi-user Ecommerce web application which accommodates three main user roles: *admins*, *clients*, and *sellers*. Each of these roles plays a crucial part in the ecosystem of online shopping.

If you try to build a class for each role, you'll find that all the three have common fields and methods. You may decide to create a parent schema (user) and some other children schemas (client, seller, admin) that inherit from it.

You can use the `discriminator` to achieve this.

In your `user.model.js` file, add the following code:

```javascript
import mongoose from "mongoose";

const userSchema = mongoose.Schema(
  {
    name: String,
    profilePic: String,
    email: String,
    password: String,
    birthDate: Date,
    accountAcctivated: { type: Boolean, default: false },
  },
  {
    timestamps: true,
    discriminatorKey: "role",
  }
);

const User = mongoose.model("User", userSchema);
export default User;
```

Now you have the base model (`User`) from which other subtypes will inherit. In this parent schema, you define the common fields that all users will share regardless of their roles.

In your `client.model.js` file:

```javascript
import mongoose from "mongoose";
import User from "./user.model.js";

const clientSchema = mongoose.Schema(
  {
    products: Array,
    address: String,
    phone: String,
  }
);

const Client = User.discriminator("Client", clientSchema);
export default Client;
```

In your `seller.model.js` file:

```javascript
import mongoose from "mongoose";
import User from "./user.model.js";

export const sellerSchema = mongoose.Schema(
  {
    rating: Number,
    businessType: { type: String, enum: ["individual", "corporation"] },
  }
);

const Seller = User.discriminator("Seller", sellerSchema);
export default Seller;
```

In your `admin.model.js` file:

```javascript
import mongoose from "mongoose";
import User from "./user.model.js";

export const adminSchema = mongoose.Schema(
  {
    permissions: Array,
    assignedTasks: Array,
    department: String,
  }
);

const Admin = User.discriminator("Admin", adminSchema);
export default Admin;
```

The subtypes or children will be the `Client`, `Seller`, and `Admin`. In each subtype schema, you should add any extra fields or behaviors specific to this subtype only. By creating the child model using the discriminator, the child model will inherit all the fields and methods of its parent model `User`.  
  
So the previous code will create a `user` collection in the database with each document having a `role` field either Client, or Seller, or Admin. All documents are now sharing the parent (`user`) fields, and depending on the `role` of each document, each has another extra field.

Although all the documents will be saved in one single collection, models are fully separated while coding. What does this mean?

For instance, If you need to retrieve all clients from the `User` collection, you should write `Client.find({})`. This statement uses the discriminator key to find all documents whose `role` is `Client`. This way, any operations or queries that refer to one of the child models will still be written separately from the parent model.

**Note:** Before diving into the next sections, just keep in mind that any statics, methods, query builders, or hooks should be defined before creating the model itself (that is, before `const User = mongoose.model("User", userSchema);`).

## Statics

Statics are useful for defining functions that operate on the model level. They allow you to define reusable functions for operations related to the entire model. They help encapsulate logic that applies to the model rather than individual documents, making your code cleaner, more organized and maintainable

Methods like `find`, `findOne`, `findById` and others all are methods attached to the model. By using the `statics` property of Mongoose schemas, you will be able to build your own model method.  
  
Statics are powerful. By using them, you can encapsulate complex queries that you might want to reuse. Also, you can create statics for operations that modify or aggregate data, such as counting documents or finding documents based on specific criteria.

### `statics` use case

Statics are easy to build. You define a static method on your schema using the `statics` object.

In your `user.model.js` file, add these static methods, `countUsers` and `findByEmail`:

```javascript
// model method
userSchema.statics.countUsers = function () {
    return this.countDocuments({});
};

// model method
userSchema.statics.findByEmail = async function (email) {
  return await this.findOne({ email });
};
```

Inside any static method, `this` refers to the **model** itself. In this example, `this` in `this.findOne({ email })` refers to the `User` model.

Example usage:

```javascript
const user = await User.findByEmail("foo@bar.com");
//or
const client = await Client.findByEmail("foo@bar.com");
//or
const seller = await Seller.findByEmail("foo@bar.com");
//or
const admin = await Admin.findByEmail("foo@bar.com");
```

When you call the static method on your model, the method gets called and `this` is replaced by the model you called the statics on. This line performs a query to find a single document in the MongoDB collection where the `email` field matches the provided `email` argument.

## Methods

Methods are functions that you can define on a schema and that can be called on instances of documents created from this schema. They help encapsulate logic within the document itself, making your code cleaner and more modular.

By using instance methods, you can easily interact with and manipulate the data associated with specific documents.

### `methods` use case

You can define methods on the schema using the `methods` object.

In your `user.model.js` file, add a document method through which you can check the password of a user:

```javascript
// instance or document method
userSchema.methods.getProfile = function () {
    return `${this.name} (${this.email})`;
};

// instance or document method
userSchema.methods.checkPassword = function (password) {
    return password === this.password ? true : false;
};
```

Inside any document method, `this` refers to the **document** itself. In this example, `this` in `this.password` refers to the `user` document at which the method will get called on. This means that you can access all the fields of this document. This is so valuable because you can retrieve, modify, and check for anything related to this document.

Example usage:

```javascript
const client = await Client.findById(...)
client.checkPassword("12345")
//or
const seller = await Seller.findById(...)
seller.checkPassword("12345")
//or
const admin = await Admin.findById(...)
admin.checkPassword("12345")
```

Since methods are instance-level functions, they are called on the documents. `await Client.findById(...)` will return a document that has all the built-in methods as well as your own predefined methods `checkPassword` and `getProfile`. So by calling, for example `client.checkPassword("12345")`, the `this` keyword in the `checkPassword` function definition will get replaced with the `client` document. This in turn will compare the user password with the password saved earlier in the database.

## Query Builder

A query builder in Mongoose is a custom method that you can define on the query object to simplify and encapsulate common query patterns. These query builders allow you to create reusable and readable query logic, making it easier to work with your data.

One of the most valuable usages of query builders is chaining. They can be chained with other query builders that you've built or with standard query methods like find, sort, and so on.

### Query builder use case

You define query builders by adding them to the `query` property of a Mongoose schema.

In your `user.model.js` file, add a query helper method that lets you implement pagination.

```javascript
// query helper
userSchema.query.paginate = function ({ page, limit }) {
    // some code
    const skip = limit * (page - 1);
    return this.skip(skip).limit(limit);
};
```

To implement pagination, you need two important variables: first, the page number, and second, the number of items you will retrieve per page.

To query the database for a specific count of documents, you will always use the `skip` and `limit` built-in query methods in `mongoose`. `skip` is used to set a cursor after a certain number of documents, after which the query will get implemented. `limit` is used to retrieve a specific number of documents.

Inside any query builder method, `this` refers to the **query** itself. And since query builders are chainable, you can call any of them after each other.

Finally, any query builder method should return a `mongoose query object`, which is why you must write `return this.skip(skip).limit(limit)`.

Example usage:

```javascript
const results = await Client.find().paginate({ page: 2, limit: 5 });
//or
const results = await Seller.find().paginate({ page: 2, limit: 5 });
//or
const results = await Admin.find().paginate({ page: 2, limit: 5 });
```

You can then call it on any query, and `await Client.find().paginate({ page: 2, limit: 5 })` will invoke the `paginate` function and replace the `this` keyword with `Client.find()` using the query builder.

You can implement pagination with certain conditions, but you'll always call `skip` and `limit`. By defining the `paginate` query builder you won't repeat yourself and you'll be able to encapsulate the logic in one single function.

## Hooks

Hooks (also known as middleware) are functions that are executed at specific points in the lifecycle of a document. They allow you to add custom behavior before or after certain operations, such as saving, updating, or removing documents.

Types of Hooks

* Pre Hooks: Executed before an operation.
    
* Post Hooks: Executed after an operation.
    

### Hooks use case

In your `user.model.js` file, add a `post` save middleware through which you can send an email for account activation once the user document is saved in the database.

```javascript
// post hook
userSchema.post("save", async function (doc, next) {
  // send email logic
  // if succeeded
  return next();
  // if failed
  return next(new Error("Failed to send email!"));
});
```

The callback function will get invoked once you create a user through `model.create()` or any time you call `save()` method on the user document.

In this this example, if you need to avoid sending emails on save, you should write a condition to be sure that this `save` is for a new user only. You can write something like `if (doc.createdAt.getTime() === doc.updatedAt.getTime())`.

### **Summary**

In this overview of Mongoose features, we've explored four key concepts: discriminators, statics, methods, and hooks.

**Discriminators** allow you to create multiple models that share a common schema enabling different document types to be stored in a single collection. This facilitates data management and querying.  
  
**Statics** are model-level methods that provide reusable functionality applicable to the entire model. They encapsulate complex queries and data manipulation logic, helping to keep your codebase clean and maintainable.  
  
**Methods** are instance-level functions that operate on individual document instances. They allow for custom behaviors and data manipulations specific to each document, so you can modify the document’s data in a specific way, such as formatting or calculating values based on its fields.  
  
**Hooks** (or middleware) enable you to run functions at specific points in the document lifecycle, such as before or after saving, updating or deleting a document. This is useful for implementing validation, logging, or any other side effects related to database operations.  
  
Together, these features enhance the versatility and organization of your Mongoose models, making it easier to build robust and maintainable applications with MongoDB.

[Here](https://github.com/Ayanabilothman/mongoose-schema-features) can will find a repository where you can learn more about Mongoose schemas and use cases.
