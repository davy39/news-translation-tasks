---
title: How TypeScript Helps You Write Better Code
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2023-11-03T15:16:26.000Z'
originalURL: https://freecodecamp.org/news/benefits-of-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/thumbnail.001.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: "TypeScript is taking over the web. In this article I'll give you a high-level\
  \ overview of the benefits of TypeScript and how can it help you create websites\
  \ with fewer bugs. \nYou'll learn how TypeScript helps with handling edge cases,\
  \ catching typos,..."
---

TypeScript is taking over the web. In this article I'll give you a high-level overview of the benefits of TypeScript and how can it help you create websites with fewer bugs. 

You'll learn how TypeScript helps with handling edge cases, catching typos, refactoring code, and how types make code easier to understand. 

The latest [State of JavaScript survey](https://2022.stateofjs.com/en-US/usage/) found that developers spend more time writing TypeScript than JavaScript code. [GitHub’s own survey](https://octoverse.github.com/2022/top-programming-languages) states a more modest claim, saying that TypeScript is only the 4th most used language on the platform – behind JavaScript – yet its usage grew by almost 40% in a year. Why is this shift happening?

![Image](https://www.freecodecamp.org/news/content/images/2023/11/part0.png)
_Graph showing percentage of their time devs spend writing JavaScript vs TypeScript_

If you prefer video format you can also [watch this article as a video](https://youtu.be/3nmQj450zk0?si=1HLg0pHnSL5lUe-t) with a bit more content.

## What are Types?

You may know that in JavaScript (as in other programming languages), there are various data types like strings, numbers, arrays, objects, functions, booleans, undefined and null values. These are all types. 

But JavaScript is dynamically typed, which means that variables can change types. You can set the value of a variable to a string in one line and set the same variable to a number in another line, for example:

```javascript
let value = 'Hello';
value = 3;
```

On the one hand, this is a benefit of the language. It means that it's simple and very flexible. You don't have to restrict yourself by setting types. 

On the other hand, you can easily shoot yourself in the foot if you are not careful enough. When you write JavaScript, it is your responsibility to use the right type of value in your code. 

If you accidentally use the wrong types, you will run into errors. Have you tried getting the length of undefined? Don't try, it throws you an error. But maybe you had an edge case that changed your value and you didn't realize it:

```javascript
value = 3;
...
console.log(value.length); // TypeError: Cannot read properties of undefined
```

Because the variables can change type at any time, JavaScript only checks if your code will work when you run it. You don't know you have an error until you run the code. 

And if you only have an error in a very rare edge case, maybe you don't even realize that your code might fail for a very long time. When you write the code, JavaScript doesn't warn you that you might have an issue.

TypeScript, on the other hand, is statically typed. This means that variables can't change type. This makes the code more predictable and it allows TypeScript to analyze the code as you write it and spot mistakes as they occur (so they don't show up as errors in your code later).

Alright, now that you have a basic understanding of what types are and how JavaScript and TypeScript differ in how they handle them, let's dive into the main partf of the tutorial.

## You're Already Using TypeScript

Let’s review the basics: TypeScript gives you type information. It tells you the types of your variables, the type of the arguments you need to pass on to your functions, and what kind of data they will return. 

But what if I tell you that you're already using TypeScript, even in plain JavaScript?

Let’s take this quick example. This is a plain JavaScript file in VS Code. Because VS Code and TypeScript are both made by Microsoft, VS Code already comes with built-in TypeScript features.

![Screen recording of VS Code with a simple JavaScript code. In one line there is a variable called 'input' that is set to a string value. The recording shows that when you hover over the variable name, in an information popup its type is correctly revealed as a string. It also shows that another variable named 'greeting' is set to the return value of a function. When hovering over this variable name, it also shows that its type is a string. Finally, a third variable named 'greetingLength' is assigned to the length of greeting. When hovering over it is revealed that its value is a number.](https://www.freecodecamp.org/news/content/images/2023/11/part1-1.gif)
_When you hover over your variables, VS Code will tell their type whenever possible_

```javascript
function getGreeting(str) {
	return `Hello ${str}!`;
}

let input = 'Bob'; // Type: string
let greeting = getGreeting(input); // Type: string
let greetingLength = greeting.length; // Type: number

console.log(greeting, greetingLength);
```

If you hover over the `input` variable, VS Code will tell you that its type is a `string`. This is quite clear, as we've assigned a string to it in the very same line.

But if we go further and check the type of `greeting` it also says it’s a `string`. This is a bit more interesting. Greeting’s value comes from a function. How do we know that it’s a string?

VS Code, with the help of TypeScript, analyses the function, checks every possible return path, and concludes that the only thing that this function can return is a `string`.

Of course, this is a very simple example. But even if we had a more complex logic, with multiple different return statements, TypeScript would still analyze every different path and would tell you what the possible return values are.

To stick a little longer with this example, if we hover over the `length` variable we are going to see that its type is a `number`. This might seem obvious again, but the logic behind it is smarter than it looks. 

The `length` property of a `string` is a number. But this is only true if we are looking at a `string`. In this case, we know that it is a `string` because TypeScript already figured out that the return type of our function is a `string`. There are multiple steps here behind the scenes.

So the first reason why TypeScript is awesome: you can see the types of values just by hovering over them. And this even works to some extent in plain JavaScript.

### Checking the required arguments for built-in functions

Let’s see another example. This code is still in JavaScript, we still don’t define types explicitly, but the TypeScript parser can still derive the types.

Here we have an input value, again we hardcode it to ‘bob’, and then we capitalize the string. We take the first character, make it upper case, then add the rest of the string in lower case.

![Screen recording of VS Code with a simple JavaScript code. In the code we define an 'input' variable, capitalize it, and then get the length of the capitalized variable. The recording shows, that when you hover over the used functions like charAt and toUpperCase functions, their signature is revealed. ](https://www.freecodecamp.org/news/content/images/2023/11/part2.gif)
_You can check the signature of JavaScript functions in VS Code_

```javascript
let input = 'bob';
let formattedInput = 
	input.charAt(0).toUpperCase() + input.slice(1).toLowerCase();
let formattedLength = formattedInput.length;

console.log(greeting, greetingLength);
```

We can check the function signature of these functions. We can see that `charAt` requires a number parameter, `toUpperCase` does not require any parameters, and the `slice` function has two optional parameters that can be either a `number` or `undefined`. 

These are TypeScript annotations. The question marks mean that a value is optional, and the pipe characters mean that a type could be either this or that.

In summary, we know that our formatted input is of type `string`.

### Where JavaScript can’t figure out the types anymore

Let’s extract the logic that capitalizes our input into a function. The types should remain the same, right? Well, not exactly. Now our capitalized input is of type `any`.

![VS Code with a simple JavaScript code. First, we define a simple function that capitalizes a string, then we use this function to capitalize a string. The image shows that when you hover over the returned value, now its type is of type 'any'.](https://www.freecodecamp.org/news/content/images/2023/11/part3.png)
_After we extracted the logic that capitalizes the input, the return value is now of type 'any'_

```javascript
function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput = capitalize(input); // Type: any
let formattedLength = formattedInput.length;
```

Interesting! What happened? Our function should always return a string, right? If you look at the entire code base in this specific case, then yes. It should return a string. 

But we have to look at the function in isolation. We can’t assume what it will receive. We could also pass on a number to it and in that case, it would fail. You can’t read the first character of a number or turn it to lower or upper case.

In JavaScript we can’t state that we need a string here, so we can’t be sure that the function returns a string. In TypeScript we are going to specify the type of this parameter to avoid any confusion.

You might notice that the previous example with the `getGreeting` function was different. There, no matter what the input was, the function always returned a `string`. Here, however, the output depends on the input.

## What About Edge Cases in JavaScript?

Could we avoid getting an error in case we get the wrong input in JavaScript? Yes.

Checking the type early and returning before the function can fail is one way to make our function fail-safe. This is still JavaScript, and the `typeof` operator is part of JavaScript.

Now this function won't fail. But I introduced a bug.

![VS Code with the same simple JavaScript file as we had earlier. Except that now our capitalize function simply returns if its argument is not a string. The image shows that now the type of the returned value changed from any to string or undefined.](https://www.freecodecamp.org/news/content/images/2023/11/part4.png)
_After adding an early return statement to our capitalize function, the type of the returned value changed from any to string or undefined_

```javascript
function capitalize(str) {
    if (typeof str !== 'string') return;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput = capitalize(input); // Type: string or undefined
let formattedLength = formattedInput.length;
```

If we check the function signature or the type of the new value, it has changed from `any` to `string | undefined`. 

In one way that is very neat. We limited the possible return values and we have a better understanding of what the function does, just by looking at the returned value. On the other hand, in case it returns `undefined`, the application will fail in the very next line. You can’t check the length of `undefined`.

Of course, we could have also returned an empty string as a fallback and then we wouldn’t have this problem. We're working with strings here. But this is a great example of a topic that is very easy to overlook in JavaScript and which can cause you a lot of headaches later: edge cases.

What if you didn’t write the capitalize function and you didn’t know how exactly it works? 

Maybe it is also located in a different file and you simply assumed that it would always return a string. Maybe the function you use is much longer and much more complicated. 

Maybe you checked the function, but only the last line of it and say ‘Okay, this function returns a string’. And you completely miss that in a different line – that can also be in the middle of the function – there is another return statement that returns a different type of value.

The point here is that edge cases can happen and it’s very easy to miss them. It’s a typical source of bugs when developers cover the happy path of an application, but they are less attentive when covering edge cases. 

In JavaScript, you need to be mindful of edge cases, test different scenarios and user inputs, and write thorough unit tests to make sure your logic doesn’t fail.

Wouldn’t it be nice if the editor would tell you that you have a problem?

## Turn the Code into TypeScript

So after all this introduction, let’s finally turn this code into TypeScript. To do so, let’s simply change the extension from `.js` to `.ts` and see what happens. 

Right away, we'll see an error saying that our `formattedInput` might be `undefined`. And that doesn’t work well with getting the length of the value. We already caught the bug that caused trouble earlier and we didn’t even invest any time in adding types to our code.

![VS Code with the same file as we had earlier. Except now we changed the file extension to TypeScript. The image shows that a new error appears.](https://www.freecodecamp.org/news/content/images/2023/11/part-5.png)
_After changing the extension to .ts an error is revealing that our capitalized value might be undefined_

```typescript
function capitalize(str) {
    if (typeof str !== 'string') return;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput = capitalize(input);
let formattedLength = formattedInput.length; // Error
```

Before fixing this error, let’s turn on `strict` mode. By default, TypeScript can be very permissive, but we also get less value out of it without `strict` mode. 

For this, we need a `tsconfig.json` file at the root of our project. This might seem a bit scary now, but this file is most probably generated for you automatically when you create a project with any of the frameworks. What’s important for now is that we have `strict` mode set to true.

```json
{
    "compilerOptions": {
      "target": "ESNext",
      "module": "ESNext",
      "strict": true,
      "esModuleInterop": true,
      "skipLibCheck": true,
      "forceConsistentCasingInFileNames": true,
      "lib": ["DOM", "ESNext"],
      "moduleResolution": "node",
      "noImplicitAny": true,
      "allowSyntheticDefaultImports": true,
      "baseUrl": "./src",
      "paths": {
        "*": ["src/*"]
      },
      "outDir": "./dist",
      "rootDir": "./src",
      "strictPropertyInitialization": false,
      "noEmit": false,
    },
    "include": ["src/**/*.ts", "src/index.js"],
    "exclude": ["node_modules"]
  }

```

This will show more errors because with this setting we have to define the types of our function arguments.

![VS Code with the same TypeScript file as before. Now with strict mode, another error shows up that states that we need to set the type of our function argument.](https://www.freecodecamp.org/news/content/images/2023/11/part-6.png)
_After turning on strict mode, we have to set the type of function arguments_

```typescript
function capitalize(str) { // Error
    if (typeof str !== 'string') return;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput = capitalize(input);
let formattedLength = formattedInput.length; // Error
```

So let’s specify that our capitalize function requires a `string` by setting the argument to `str: string`. And that’s all the types we need to add in this case because that’s the only one TypeScript couldn’t figure out itself.

![VS Code with the same TypeScript file as before. Except we set the type of the function argument to string.](https://www.freecodecamp.org/news/content/images/2023/11/part-7.png)
_Setting the type of the function's argument to string_

```typescript
function capitalize(str: string) {
    if (typeof str !== 'string') return;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput = capitalize(input);
let formattedLength = formattedInput.length; // Error
```

One misconception about TypeScript is that you have to add types to everything. While that’s not a bad practice it is not strictly necessary. TypeScript is very smart. It analyses the code and figures out the types of as many things as possible.

We can of course specify types at other places. We can specify that we need our `formattedInput` value to be a `string` by setting `let formattedInput: string`. This is our whole problem here. We thought it was a string, but in some cases, it wasn’t.

![VS Code with the same TypeScript file as before. Except, that now the variable we set to the returned value of our capitalize function has to be a string. This revealed that there might be a type mismatch because the capitalize function might return undefined.](https://www.freecodecamp.org/news/content/images/2023/11/part-8.png)
_After setting the type of the 'formattedInput' variable, the error changed_

```typescript
function capitalize(str: string) {
    if (typeof str !== 'string') return;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput: string = capitalize(input); // Error
let formattedLength = formattedInput.length;
```

This highlights our problem right away. We want it to be a `string`, but our function might return `undefined`. We can read in the popover that `undefined` cannot be assigned to type `string`.

We can go further, by saying we want this function to return a `string`. This again will change the error. Now the problem is not that we can’t assign the returned value to a `string` variable, but that the function itself returns an incorrect value.

![VS Code with the same TypeScript file as before. Except, that now we set the return type of our capitalize function to string. This changes our error because the function might return undefined.](https://www.freecodecamp.org/news/content/images/2023/11/part-9.png)
_After setting the return type of the capitalize function, the error changed again_

```typescript
function capitalize(str: string): string {
    if (typeof str !== 'string') return; // Error
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput: string = capitalize(input);
let formattedLength = formattedInput.length;
```

To solve this, let’s delete this whole line. Earlier we added this line for type checking, but now, we let TypeScript do the whole type checking for us. The function signature already states that this property has to be a `string`, there’s no need to check it again. Our code got simpler, and at the same time safer.

So another reason why TypeScript is amazing is that it forces you to think of edge cases. Not just to think of them, but also to handle them. Something that’s very easy to overlook in JavaScript.

## Refactoring the Code

Now that we've got the basics, let’s go on to our third topic: refactoring. Let’s update our greeting function a bit, and let’s say it now takes two arguments: a first name and a last name. Imagine that this is a utility function that is used in many places in a huge, complex project:

![VS Code with a simple TypeScript file. In this file, we define a 'getGreeting' function that receives two arguments, a first name, and a last name. The type of both of these arguments is a string.](https://www.freecodecamp.org/news/content/images/2023/11/part10-1.png)
_Our new updated 'getGreeting' function that receives a first name and a last name_

```typescript
export function getGreeting(firstName: string, lastName: string) {
    const formattedFirstName = capitalize(firstName);
    const formattedLastName = capitalize(lastName);
    return `Hello ${formattedFirstName} ${formattedLastName}!`;
}

function capitalize(str: string): string {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}
```

What if we decide that we need to refactor this code? Instead of passing on two strings, we want to pass in an object that has the first name and last name properties.

In TypeScript, we can precisely define the shape of an object. We can define that we have to pass on a `person` parameter that should be an object with a `firstName` and a `lastName` property, that both have to be `strings`.

We can define a type for this argument. We say that we have a `Person` type with capital P by convention. This type describes an object with the `firstName` and `lastName` properties that are both strings. 

We can even add more things if we want, like adding a `birthday` property that has a type `Date`. But let’s make this optional because we don’t want to deal with it for now. 

Adding a question mark here makes this property optional. We can set it, but we don’t have to. But when we try to use it, we also can’t assume that it does exist.

![VS Code with the same TypeScript file. Except now we define a custom person type like this: `type Person = { firstName: string, lastName: string, birthday?: Date }`. Then we change the two function arguments to a single 'person' argument with type 'Person'. As a result, the editor shows errors in this file and it also highlights in the file explorer that the other files have errors as well.](https://www.freecodecamp.org/news/content/images/2023/11/part-10.png)
_After changing the function argument type, the editor highlights the parts we need to change_

```typescript
type Person = {
    firstName: string,
    lastName: string,
    birthDay?: Date
}

export function getGreeting(person: Person) {
    const formattedFirstName = capitalize(firstName);
    const formattedLastName = capitalize(lastName);
    return `Hello ${formattedFirstName} ${formattedLastName}!`;
}

function capitalize(str: string): string {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}
```

Now we can set that our `person` argument is of type `Person`.

As we do this change the editor lights up in red. It says that I’m trying to use variables that don’t exist. In this function, I’m referring to `firstName` and `lastName`, and there’s only a `person` object now. 

Even more, the other files in the file explorer light up as well, saying that I called the function with two arguments even though it expects only one.

Let’s fix the error in this file and replace `firstName` and `lastName` with `person.firstName` and `person.lastName`. TypeScript is very picky about using variables that don’t exist. 

To give you an even better example: What if I made a typo here? What if I miss a letter from `firstName`? This could be a very easily overlooked problem in JavaScript. Here, though, it’s not only highlighted that there’s no such property on a `Person`, but it even suggests that you might want to use `firstName` instead.

![VS Code with the same TypeScript file. Except now we updated the function to use the new function argument. By mistake, we made a typo. The editor highlights the typo and it makes a suggestion.](https://www.freecodecamp.org/news/content/images/2023/11/part-11.png)
_If we make a typo, the editor suggests corrections_

```typescript
type Person = {
    firstName: string,
    lastName: string,
    birthDay?: Date
}

export function getGreeting(person: Person) {
    const formattedFirstName = capitalize(person.frstName);
    const formattedLastName = capitalize(person.lastName);
    return `Hello ${formattedFirstName} ${formattedLastName}!`;
}

function capitalize(str: string): string {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}
```

Then, let’s fix the errors in the other files. As you can see the files with an error are already highlighted in the file explorer. This is of course a very simple example, but imagine you have a huge project and this function is called in a hundred different places. Of course, you can be thorough and fix all of them one by one, but in JavaScript, it would be very easy to miss one of them.

![VS Code with another TypeScript file calling our previously defined function. As we update the function call from the previous two-argument signature to our new one, TypeScript gives relevant errors if we make mistakes.](https://www.freecodecamp.org/news/content/images/2023/11/part-12.gif)
_When updating the function calls, TypeScipt gives you errors if we make mistakes_

```typescript
import { getGreeting } from "./utils";

let greeting = getGreeting({ firstName: 'bob', lastName:  'marley' });

console.log(greeting);

```

Now here, the error says that we pass on two parameters, but only one is expected. If we simply delete the second argument it says we pass on a string, but it expected an object of type `Person`. If we pass on an object with the first name only, it will still complain that we're missing the last name. If we add the last name, but again with a typo, then again it will say that we have a wrong property and it even suggests that we might have made a typo here.

TypeScript is very precise about what our issue is, and we can easily figure out how to fix it.

Now let’s fix the other file. Instead of inlining the argument, we can also define it as a variable and TypeScript will recognize that an object of this shape fits the criteria of this function. 

If we want to be sure that our variable is of type Person, we can also import the type and set it to this object. First, we need to export it, in the utility file, and then can import it just as our function, then assign it to our object.

![VS Code with yet another TypeScript file calling our previously defined function. This time we don't inline the function argument, but create a new variable for it. When setting the type of this argument, we reuse the previously defined 'Person' type.](https://www.freecodecamp.org/news/content/images/2023/11/part-13.png)
_We can also use our Person type in other files_

```typescript
import { Person, getGreeting } from "./utils";

let person: Person = {
    firstName: 'bob',
    lastName: 'dylan'
}

let greeting = getGreeting(person);

console.log(greeting);
```

## Summary

TypeScript can be much more complicated than this. But that’s the gist of it. For the most part you define your own types and TypeScript makes sure that you use them correctly.

In summary, there are three main reasons you want to consider using TypeScript:

1. You get type information about functions
2. You know what they return
3. You know what they expect from you, even without looking at the function itself

TypeScript makes sure that you wire together your application correctly. It forces you to call functions with the right arguments and it forces you to think about edge cases.

TypeScript helps a lot during refactoring. It doesn’t let you miss any part of your code that you need to change and it doesn’t let you get away with typos.

%[https://youtu.be/3nmQj450zk0?si=hLgdKiFrveP3e6eQ]

### Subscribe for more tutorials on Web Development:

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]


