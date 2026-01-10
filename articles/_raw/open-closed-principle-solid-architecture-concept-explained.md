---
title: Open-Closed Principle – SOLID Architecture Concept Explained
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-02-22T15:50:42.000Z'
originalURL: https://freecodecamp.org/news/open-closed-principle-solid-architecture-concept-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/chests-34153_1280.png
tags:
- name: software development
  slug: software-development
- name: solid
  slug: solid
seo_title: null
seo_desc: 'The Open-Closed principle (OCP) is one the 5 SOLID design principles. It
  was popularized by the American computer scientist and instructor, Robert C. Martin
  (aka Uncle Bob) in a paper he published in 2000.

  The other 4 SOLID design principles are:


  Si...'
---

The Open-Closed principle (OCP) is one the 5 SOLID design principles. It was popularized by the American computer scientist and instructor, Robert C. Martin (aka Uncle Bob) in a paper he published in 2000.

The other 4 SOLID design principles are:
- Single Responsibility Principle (SRP)
- Liskov Substitution Principle (LSP)
- Interface Segregation Principle (ISP)
- Dependency Inversion Principle (DIP).

If you want to learn about all these principles, you can read my tutorial on the [SOLID principles here](https://www.freecodecamp.org/news/solid-design-principles-in-software-development/).

In this article, I’ll show you what the open-closed principle (OCP) means, why you should use it, and its implementation in JavaScript.

## What We'll Cover
- [What is the Open-Closed Principle?](#heading-what-is-the-open-closed-principle)
- [Why should you use the Open-Closed Principle?](#heading-why-should-you-use-the-open-closed-principle)
- [How to implement the Open-Closed Principle in JavaScript](#heading-how-to-implement-the-open-closed-principle-in-javascript)
- [Conclusion](#heading-conclusion)

## What is the Open-Closed Principle?
The open-closed principle states that software entities (classes, modules, functions, and so on) should be open for extension, but closed for modification. 

You are probably wondering why that statement sounds like a contradiction. Like why would something be opened and be closed at the same time? 

Well, in the land of software development, it’s possible for an item to be opened for extension and be closed for modification. It means you or your team members should be able to add new functionalities to an existing software system without changing the existing code.

The open-closed principle encourages software engineers to focus on what’s necessary when it’s time to add new functionalities. 

If you want to add new functionality to your existing code and you have to modify it before you add the new functionality, then you are not following the open-closed principle.


## Why Should You Use the Open-Closed Principle?
Here are some reasons why you should be using the open-closed principle:

- **You don’t need to re-invent the wheel**: as the principle states, the code you and your team are working on is closed for extension. This means if you’re following the open-closed principle, you don’t need to reinvent the wheel (and rebuild everything) when you want to add new features.

- **You focus on what is necessary**: as the OCP states, your code is closed for modification. It means you can add new features without performing too much editing on the existing code, or none at all. This can help you and your team members focus on what is necessary when it’s time to implement new functionalities.

- **You can avoid bugs**: since you don’t have to edit the existing code before adding new features, you can avoid introducting unnecessary bugs.

-**Your code is more maintainable, testable, and flexible**: following the OCP will make your codebase loosely coupled. With this the code is more flexible and maintainable. And if you want, you can unit test each class successfully. 

## How to Implement the Open-Closed Principle in JavaScript
The first example of the open-closed principle I will show is a class using a switch or multiple if statements. That’s because in code like this, there’s a very real possibility you will modify the class using the switch or if statements. And that violates the open-closed principle in the process.

```js
class Footballer {
  constructor(name, age, role) {
    this.name = name;
    this.age = age;
    this.role = role;
  }

  getFootballerRole() {
    switch (this.role) {
      case 'goalkeeper':
        console.log(`The footballer, ${this.name} is a goalkeeper`);
        break;
      case 'defender':
        console.log(`The footballer, ${this.name} is a defender`);
        break;
      case 'midfielder':
        console.log(`The footballer, ${this.name} is a midfielder`);
        break;
      case 'forward':
        console.log(`The footballer, ${this.name} plays in the forward line`);
        break;
      default:
        throw new Error(`Unsupported animal type: ${this.type}`);
    }
  }
}

const kante = new Footballer('Ngolo Kante', 31, 'midfielder');
const hazard = new Footballer('Eden Hazard', 32, 'forward');

kante.getFootballerRole(); // The footballer, Ngolo Kante is a midfielder
hazard.getFootballerRole(); // The footballer, Eden Hazard plays in the forward line
``` 

There are more football roles like winger, defensive midfielder, and more. So, in the code above, what do you think would happen if you had to add another footballer role on the pitch? You would have to modify the `switch` statement. That violates the open-closed principle because you have to modify the existing code.

To fix the violation, you have to create a separate role `class` to consume the method that gets the player role from the super `class`. But it doesn’t end there. You then need to create a different `class` for each role that extends the class which gets the player role.

This will make more sense in code:

```js
class Footballer {
  constructor(name, age, role) {
    this.name = name;
    this.age = age;
    this.role = role;
  }

  getRole() {
    return this.role.getRole();
  }
}

// PlayerRole class uses the getRole method
class PlayerRole {
  getRole() {}
}

// Sub classes for different roles extend the PlayerRole class
class GoalkeeperRole extends PlayerRole {
  getRole() {
    return 'goalkeeper';
  }
}

class DefenderRole extends PlayerRole {
  getRole() {
    return 'defender';
  }
}

class MidfieldRole extends PlayerRole {
  getRole() {
    return 'midfielder';
  }
}

class ForwardRole extends PlayerRole {
  getRole() {
    return 'forward';
  }
}

// Putting all of them together
const hazard = new Footballer('Hazard', 32, new ForwardRole());
console.log(`${hazard.name} plays in the ${hazard.getRole()} line`); // Hazard plays in the forward line

const kante = new Footballer('Ngolo Kante', 31, new MidfieldRole());
console.log(`${kante.name} is the best ${kante.getRole()} in the world!`); //Ngolo Kante is the best midfielder in the world!
```


Here’s another example that uses functions instead of JavaScript classes:

```js
function calculatePrice(price, discount) {
  if (discount === '10%') {
    return price * 0.9;
  } else if (discount === '20%') {
    return price * 0.8;
  } else if (discount === '30%') {
    return price * 0.7;
  } else {
    throw new Error('Invalid discount');
  }
}

const discountedPrice = calculatePrice(100, '10%');
console.log(`Your discounted price is ${discountedPrice}`); //  The discount you get is 90
```

The code above violates the open-closed principle because you have to add another `if…else` statement if you want to add a new discount.

To fix it, you can extract all your discounts to an object and use it in the function this way:

```js
const discounts = {
  '10%': 0.9,
  '20%': 0.8,
  '30%': 0.7,
};

function calculatePrice(price, discountType) {
  const discount = discounts[discountType];
  if (discount === undefined) {
    throw new Error('Invalid discount');
  }
  return price * discount;
}

const discountedPrice = calculatePrice(100, '30%');
console.log(`Your discounted price is $${discountedPrice}`);
```

Now if you want to add new discounts, you only need to add to the discount object, not the existing function that calculates the discount.


## Conclusion
In this article, you learned about the open-closed principle, its benefits, and how to implement it.

To carry out the implementation, we used JavaScript classes to illustrate how you can get it done with JavaScript object-oriented programming. First I showed how the code violates the principle, and how to refactor it so it doesn't. 

Since function is also a software entity, we also looked at how you can implement the open-closed principle with JavaScript functions.

Keep coding!

