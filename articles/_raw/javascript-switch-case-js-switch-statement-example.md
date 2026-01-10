---
title: JavaScript Switch Case – JS Switch Statement Example
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-08-06T15:18:55.000Z'
originalURL: https://freecodecamp.org/news/javascript-switch-case-js-switch-statement-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/karl-pawlowicz-QUHuwyNgSA0-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "There are times in JavaScript where you might consider using a switch statement\
  \ instead of an if else statement.  \nswitch statements can have a cleaner syntax\
  \ over complicated if else statements. \nTake a look at the example below – instead\
  \ of using t..."
---

There are times in JavaScript where you might consider using a `switch` statement instead of an `if else` statement.  

`switch` statements can have a cleaner syntax over complicated `if else` statements. 

Take a look at the example below – instead of using this long `if else` statement, you might choose to go with an easier to read `switch` statement. 

```js
const pet = "dog";

if (pet === "lizard") {
  console.log("I own a lizard");
} else if (pet === "dog") {
  console.log("I own a dog");
} else if (pet === "cat") {
  console.log("I own a cat");
} else if (pet === "snake") {
  console.log("I own a snake");
} else if (pet === "parrot") {
  console.log("I own a parrot");
} else {
  console.log("I don't own a pet");
}
```

```js
const pet = "dog";
 
switch (pet) {
  case "lizard":
    console.log("I own a lizard");
    break;
  case "dog":
    console.log("I own a dog");
    break;
  case "cat":
    console.log("I own a cat");
    break;
  case "snake":
    console.log("I own a snake");
    break;
  case "parrot":
    console.log("I own a parrot");
    break;
  default:
    console.log("I don't own a pet");
    break;
}
```

In this article, I'll explain what switch statements are and how they work. I'll also help you figure out if they're a good option to use in your code.

## What is a Switch Statement?  

In programming, a `switch` statement is a control-flow statement that tests the value of an `expression` against multiple cases. 

This is the basic syntax for a `switch` statement:

```js
switch (expression) {
  case 1:
   //this code will execute if the case matches the expression
    break;
  case 2:
   //this code will execute if the case matches the expression
    break;
  case 3:
   //this code will execute if the case matches the expression
    break;
  default:
    //this code will execute if none of the cases match the expression
    break;
}
```

The computer will go through  the `switch` statement and check for strict equality `===` between the `case` and `expression`.  If one of the cases matches the `expression`, then the code inside that `case` clause will execute. 

```js
switch (expression) {
  case 1:
   //this code will execute if the case matches the expression
    break;
  case 2:
   //this code will execute if the case matches the expression
    break;
}
```

If none of the cases match the expression, then the `default` clause will be executed. 

```js
  default:
    //this code will execute if none of the cases match the expression
    break;
```

If multiples cases match the `switch` statement, then the first `case` that matches the `expression` will be used. 

`break` statements will break out of the `switch` when the `case` is matched. If `break` statements are not present, then the computer will continue through the `switch` statement even if a match is found. 

If `return` statements are present in the `switch`, then you don't need a `break` statement. 

## Example of Switch Statements in JavaScript

In this example, we are comparing `"oboe"` to the cases. `"oboe"` would match the third `case` clause and would print to the console "I play the oboe". 

```js
switch ("oboe") {
  case "trumpet":
    console.log("I play the trumpet");
    break;
  case "flute":
    console.log("I play the flute");
    break;
  case "oboe":
    console.log("I play the oboe");
    break;
  default:
    console.log("I don't play an instrument. Sorry");
    break;
}
```

If I were to change the expression to `"no instrument"`, then the `default` clause would execute and the message printed to the console would be "I don't play an instrument. Sorry".

```js
switch ("no instrument") {
  case "trumpet":
    console.log("I play the trumpet");
    break;
  case "flute":
    console.log("I play the flute");
    break;
  case "oboe":
    console.log("I play the oboe");
    break;
  default:
    console.log("I don't play an instrument. Sorry");
    break;
}
```

## Missing Break Statements 

In this example, the match would be `case` 2. But without a `break` statement, the computer will continue onto `case` 3 and the `default` clause. 

You should see three `console.log` statements because a `break` statement was not included. 

```js
switch (2) {
  case 1:
    console.log("Number 1 was chosen");
  case 2:
    console.log("Number 2 was chosen");
  case 3:
    console.log("Number 3 was chosen");
  default:
    console.log("No number was chosen");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-04-at-10.20.10-PM.png)

## Where to Place the Default Clause

Standard convention is to place the `default` as the last clause. But you can place it before other cases too.

```js
const food = "nuts";

switch (food) {
  case "cake":
    console.log("I like cake");
    break;
  case "pizza":
    console.log("I like pizza");
    break;
  default:
    console.log("I like all foods");
    break;
  case "ice cream":
    console.log("I like ice cream");
    break;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-04-at-11.22.42-PM.png)

The computer will still go through each of the cases and find a match. Since the variable `food` does not match any of the cases, then the `default` case will be executed. 

## Multiple Cases for One Operation

There may be times where you have one operation that will be the same for multiple cases. 

Instead of writing out the same `console.log` for each case, we can omit the `break` statements and place a singular operation after the group of cases. 

The message, "This country is in Europe." will print to the console if `country` matches any of the cases of `"France"`, `"Spain"`, `"Ireland"` or `"Poland"`. 

```js
const country = "Ireland";
switch (country) {
  case "France":
  case "Spain":
  case "Ireland":
  case "Poland":
    console.log("This country is in Europe.");
    break;
  case "United States":
  default:
    console.log("This country is not in Europe.");
}
```

## Block Scope and Switch Statements

This example will produce an error message, because the `message` variable has already been declared and you cannot have the same variable name in the same block scope. 

```js
const errand = "Going Shopping";
switch (errand) {
  case "Going to the Dentist":
    let message = "I hate going to the dentist";
    console.log(message);
    break;
  case "Going Shopping":
    let message = "I love to shop";
    console.log(message);
    break;
  default:
    console.log("No errands");
    break;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-05-at-12.45.29-AM.png)

In order to get rid of that error message, the cases need to be wrapped in a set of curly braces. 

```js
const errand = "Going Shopping";
switch (errand) {
  case "Going to the Dentist": {
    let message = "I hate going to the dentist";
    console.log(message);
    break;
  }
  case "Going Shopping": {
    let message = "I love to shop";
    console.log(message);
    break;
  }
  default: {
    console.log("No errand");
    break;
  }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-05-at-12.51.50-AM.png)

## Conclusion

Using a `switch` statement can be an alternative to an `if else` statement. A `switch` statement compares the value of an `expression` to multiple cases. 

`switch` statements will check for strict equality. In this example, since  `"2"!== 2`, the `default` clause will execute.

```js
switch (2) {
  case "2":
    console.log("Number 2 in a string");
    break;
  case "3":
    console.log("Number 3 in a string");
    break;
  default:
    console.log("Number not present");
    break;
}
```

`break` statements will break out of the `switch` when the `case` is matched. If `break` statements are not present, then the computer will continue through the `switch` statement even if a match is found. 

I hope you enjoyed this article on `switch` statements. 




