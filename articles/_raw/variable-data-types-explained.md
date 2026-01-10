---
title: Variable Data Types Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-07T16:54:47.000Z'
originalURL: https://freecodecamp.org/news/variable-data-types-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/data-types-thumbnail2.jpg
tags:
- name: arrays
  slug: arrays
- name: object
  slug: object
- name: General Programming
  slug: programming
- name: variables
  slug: variables
seo_title: null
seo_desc: "By Deborah Kurata\nWalking into a hardware store, it's not enough to say:\
  \ \"I need a tool\". You need to be specific about the type of tool you need. \n\
  Each tool type has its particular purpose: A hammer to drive a nail into wood, a\
  \ paint brush to paint,..."
---

By Deborah Kurata

Walking into a hardware store, it's not enough to say: "I need a tool". You need to be specific about the type of tool you need. 

Each tool type has its particular purpose: A hammer to drive a nail into wood, a paint brush to paint, and a wrench tightens or loosens nuts and bolts.

The same goes for the variables we use to hold data in our code. Regardless of the programming language you use, when building a website or app you'll want to use the appropriate type of variable for a particular purpose. We'll look at basic types and more complex types such as arrays (lists) and objects.

You can also watch the associated video here which walks through the key variable data types.

%[https://youtu.be/8cTu_RrkiME]

## **Basic Data Types**

The most common basic data types available in most programming languages include:

**numbers**: we use this for any data that is numeric or should be worked with as a number for addition or other math operations. 

In some programming languages, there are multiple data types for numbers, depending on whether the number is an integer, decimal, or currency, for example. 

If we were building a number guessing game, we would hold the guessed number in a numeric data type, like this:

```code
usersGuess = 3
```

**string**: we use this for any data that is text. For example, a name or address or message. In most programming languages, strings require quotes. Notice that the text inside of the quotes can include spaces and other special characters.

```code
usersName = "Jack Harkness"
```

**date**: we use this for data that is a date or time, such as a birthday.

```code
usersBirthday = April 14, 2001
```

**Boolean**: we use this for data that only has the value `true` or `false`. In a number guessing game, the user's guess was either correct or it wasn't. There is no other value.

```code
correctGuess = true
```

For programming languages that are considered to be "strongly typed", such as C# and TypeScript, the data type defines the kind of data that can be assigned to that variable. You'll see an error if you try to put the wrong type of data into a variable.

```typescript
pageTitle = 'Pet List';	// Variable is a string.

pageTitle = 42;			// Error
						// Can't put a number into a string variable
```

With "dynamically typed" languages such as JavaScript and Python, the data type defines the kind of data currently assigned to that variable. That type can change if you put a different type of data into that variable. So the type dynamically changes based on the currently assigned value.

```javascript
pageTitle = 'Pet List';			// Variable type is a string

pageTitle = 42;					// Variable type is now a number
```

## **Array (List) Data Type**

Another important data type in programming is an array, which in some programming languages is called a list.

Let's say we add a feature to our website or app so the user can provide the name of each of their pets. We could hold each name in a separate variable like shown in Figure 1.

![Pictures of three cats with three variables to hold the name of each cat.](https://www.freecodecamp.org/news/content/images/2023/03/array1.jpg)
_Figure 1. Using separate string variables to hold multiple items._

But we'd then have to limit how many pets we could allow based on how many variables we'd defined.

Arrays solve this problem. An **array** is a collection or set of data items. You can think of an array as a list of items.

The data items in an array are often of the same type, so you may have an array of numbers, of strings, or of dates.

In some programming languages, including C#, TypeScript, JavaScript, and Python, arrays are defined with square brackets: [ ] and each value in the array is separated with commas.

```code
petNames = ["Yoyo", "Vanny", "Cali"]
```

Here we define an array of strings. Recall that strings must be enclosed in quotation marks. 

![Pictures of three cats with a single array to hold the name of each cat.](https://www.freecodecamp.org/news/content/images/2023/03/array2.jpg)
_Figure 2. Using an array to hold multiple items._

With arrays, the user can have an almost limitless number of items, such as names, because we can keep appending to the array.

```code
petNames = ["Yoyo", "Vanny", "Cali", "Ben", "Maki"]
```

## **Object Data Type (Custom Data Type)**

What about data that represent things in our application? Things like those shown in Figure 3:

* A pet
* A customer
* A product
* Or post, and I actually mean a social media post here, but close enough.

![Four icons representing pet, customer, product, and post](https://www.freecodecamp.org/news/content/images/2023/03/object1.jpg)
_Figure 3. Custom data type (object) examples._

We can hold detailed information about a thing, such as a pet or customer or blog post, in a set of string, number, and date variables. But to keep that set of variables for a particular thing together as one variable, we want a custom data type that describes that thing. 

Think of an object as a custom data type that groups a set of related variables for a particular thing.

Let's walk through how to define an object as a custom data type.

### Step 1: Identify Properties (Characteristics)

To define an object data type, we first identify the data we want to hold for the object. These are often characteristics of the object, like a pet's name, type, and age. In programming, we call each of these characteristics a **property** of the object.

Let's look at some examples.

![Four icons representing pet, customer, product, and post and their characteristics](https://www.freecodecamp.org/news/content/images/2023/03/object2.jpg)
_Figure 4. Identify the data to store (or hold) for each object._

For a customer, the properties might be the customer's name, shipping address, and default payment method. 

A product may have a product name, description, and a Boolean value defining whether the product is currently in stock.

And for a blog post, we may want to hold the user's name, the post text, and the date.

Each of these are properties of our object.

At this point, we have the list of properties for the object. We want to hold data for each of these properties.

### Step 2: Assign a Property Name

Once we have the properties defined, we assign a name to each property as shown in Figure 5. 

![Four icons representing pet, customer, product, and post and their property names](https://www.freecodecamp.org/news/content/images/2023/03/object3.jpg)
_Figure 5. Define a variable name for each object property._

The names follow the conventions for the programming language you are using. In general, property names cannot have spaces or special characters in them. They are often defined using camel case, with the first letter lower case and each additional word capitalized.

Each property also has a basic data type. `petName`, `customerName`, `productName`, and `userName` are strings. `age` is a number, `inStock` is a Boolean value (true or false), and `postDate` is a date.

We could keep track of separate variables for each of these pet properties and each of these customer properties and each of these post properties. But we'd end up with lots of unorganized variables.

Let's instead group each set of related properties into an object.

### Step 3: Group the Properties for the Object

We group the properties of an object together using object literal syntax. This keeps the data for an object together and makes it easier to work with it as a set.

The syntax used to group the properties depends on the programming language you use. In languages such as JavaScript, TypeScript, and C#, object properties are grouped within curly braces ({ }).

```code
pet = {
	petName: "Yoyo",
    petType: "cat",
    age: 11
}
```

![Four icons representing pet, customer, product, and post and a sample object.](https://www.freecodecamp.org/news/content/images/2023/03/object4.jpg)
_Figure 6. Group the properties for each object_

For each object, the variable on the left of the equal sign is the object variable and represents a specific pet, customer, product, or post. On the right of the equal sign, inside the curly braces, we list each property name, a colon, and the data (often called a value). We separate properties with a comma.

To say that another way, you can think of an object as a collection of name and value pairs. The name is the property name and the value is the data you want to store for that property. 

In Figure 6, we defined a pet object with a specific set of properties, and a value for each property. Same with the customer, and so on.

## Try It Yourself!

Let's stop here for a moment and think about objects. What's your favorite hobby? If you built a website or an app to support that hobby, what objects might you define?

Maybe you like to bake, so you'd build a recipe app with your favorite recipes. You work with the data for each recipe using an object with properties such as ingredients, recipe steps, baking temperature, and time.

Or say you like sports. You'd track the data for each player using an object with properties such as name, position, and stats. And you'd track the data for each game using another object with properties such as teams and score.

What objects did you define for your hobby?

## **Wrapping Up**

A variable has a data type such as number, string (for text), date, and Boolean (for true or false).

An array stores a set of data items, often of the same type.

An object represents something in the website or app, like a pet, a customer, or a blog post. The object groups related properties holding the data for the object.

Now that you know all about data types, you can create variables of the appropriate type to hold any data you need for your website or app.

If you are self-taught or new to programming and want more information about general programming concepts, check out this course:

%[https://youtu.be/yO4JaMVMerA]


