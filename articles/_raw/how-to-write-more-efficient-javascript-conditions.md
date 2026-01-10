---
title: How to Write More Efficient JavaScript Conditions
subtitle: ''
author: Eesa Zahed
co_authors: []
series: null
date: '2023-05-03T17:44:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-more-efficient-javascript-conditions
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/image3-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "When you're coding in JavaScript, conditions are important for developing\
  \ a functional application. \nConditional statements are important because you use\
  \ them as \"validators\" which can either return truth or false. You can then use\
  \ them to trigger fu..."
---

When you're coding in JavaScript, conditions are important for developing a functional application. 

Conditional statements are important because you use them as "validators" which can either return truth or false. You can then use them to trigger further actions within the program.

But with many long, messy `if` statements in the program, it can cause confusion for developers and heavily reduce readability. This is why it's important for developers to implement more efficient conditions.

## Conditional Statement Example

Imagine you are creating a polling app. Each user has to choose their favorite color, but the only options are red, green, and blue.

Clearly there aren't many choices for users, but let's stick to a simple solution for now.

The function for voting may look something like this:

```js
const vote = (color) => {
  // code goes here
}

```

But what if a user votes for a color that isn't a valid option? They might have used a dropdown you forgot to remove some colors from, or the user could have manipulated the client-side JavaScript.

Try to imagine if a user voted for the color orange. You would need to use some JavaScript logic to prevent this.

How would you do this? You could create a simple condition where a user can only choose red:

```js
const vote = (color) => {
  if (color !== "red") {
    return "invalid color";
  }

  return "valid color";
}

```

This is great! Now, the first condition the function checks is: "Is the color NOT red? Well, that’s not allowed", and returns accordingly.

```js
vote("orange"); // "invalid color"

```

Now, how can you make it so that the color blue is also accepted? All you need to do is add another condition:

```js
const vote = (color) => {
  if (color !== "red" && color !== "blue") {
    return "invalid color";
  }

  return "valid color";
}

```

This works, too. But what if you want to verify that the color is red, orange, yellow, green, blue, or purple? Then the code would look like this:

```js
const vote = (color) => {
  if (color !== "red" && color !== "orange"  && color !== "yellow"  && color !== "green"  && color !== "blue"  && color !== "purple") {
    return "invalid color";
  }

  return "valid color";
}

vote("cyan"); // "invalid color"

```

As you can see, this definitely works. But the code is long, messy, and is less readable now. To implement this efficiently, you need to use an array.

### How to Do this Using an Array

First, define the array. A good variable name is `validColors`:

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

```

You can use the `array.includes()` method here. The syntax for this is:

```js
array.includes(item) // returns a boolean

```

To implement this in the code, the syntax looks like this:

```js
!validColors.includes(color)

```

The exclamation point (!) at the beginning is there because you want to know if the color is NOT in the `validColors` array.

The full code for this is:

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

const vote = (color) => {
  if (!validColors.includes(color)) {
    return "invalid color";
  }

  return "valid color";
}

```

This code is far easier to read and to edit. And it will be much easier to add new colors to the `validColors` array.

And you can test the code to make sure it works:

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

const vote = (color) => {
  if (!validColors.includes(color)) {
    return "invalid color" ;
  }

  return "valid color";
}

console.log(vote("red")); // "valid color"
console.log(vote("orange")); // "valid color"
console.log(vote("yellow")); // "valid color"
console.log(vote("green")); // "valid color"
console.log(vote("blue")); // "valid color"
console.log(vote("purple")); // "valid color"

console.log(vote("cyan")); // "invalid color"
console.log(vote("black")); // "invalid color"

```

Now, this implementation uses much less code and is more readable. 

### Why Arrays are More Efficient Than Switch Cases

This is much easier than using a switch case, which would look like this:

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

const vote = (color) => {
  switch (color) {
    case "red":
        console.log("you voted red");
        break;
    case "orange":
        console.log("you voted orange");
        break;
    case "yellow":
        console.log("you voted yellow");
        break;
    case "green":
        console.log("you voted green");
        break;
    case "blue":
        console.log("you voted blue");
        break;
    case "purple":
        console.log("you voted purple");
        break;
    default:
        console.log("invalid color");
    }
}

```

As you can see, this uses a lot more code. Another issue would arise if you needed to add another color as a valid option. Instead of just updating an array, you would need to carefully edit a switch case, which has a higher potential to break something in the code.

### The Issue with Nested Conditional Statements

For another example, let's try to add the user's name when voting. The name must be less than or equal to 15 characters.

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

const vote = (name, color) => {
  if (!validColors.includes(color)) {
    return "invalid color" ;
  } else {
    if (name.length > 15) {
      return "name is too long";
    }
  }

  return "valid name and color";
}

console.log(vote("bob", "red")); // "valid name and color"

```

The code works correctly, but is difficult to read, and can cause confusion if more code is added. You can clean this up by not nesting conditions.

```js
const validColors = ["red", "orange", "yellow", "green", "blue", "purple"];

const vote = (name, color) => {
  if (!validColors.includes(color)) {
    return "invalid color" ;
  }
    
  if (name.length > 15) {
    return "name is too long";
  }

  return "valid name and color";
}

console.log(vote("bob", "red")); // "valid name and color"

```

This works well, as the code first checks if the color is valid, and then it checks if the name is valid. The code is also much easier to read now.

It’s looking good! I hope this has helped you understand how to write more efficient conditions in JavaScript.

## Conclusion

Feel free to check out my [GitHub](https://github.com/eesazahed) and [Replit](https://replit.com/@eesazahed) to view my projects.

If you'd like to reach out, my email address is eszhd1 (at) gmail.com

