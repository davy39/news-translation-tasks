---
title: Imperative vs Declarative Programming – the Difference Explained in Plain English
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-08T18:32:24.000Z'
originalURL: https://freecodecamp.org/news/imperative-vs-declarative-programming-difference
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/imperative-vs-declarative-programming-difference.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Mike Zetlow

  As a coding instructor, it’s my duty to send programmers out into the world thinking
  in new ways. A major shift in thinking occurs when we switch from imperative to
  declarative programming.

  Once my students have learned basic JavaScrip...'
---

By Mike Zetlow

As a coding instructor, it’s my duty to send programmers out into the world thinking in new ways. A major shift in thinking occurs when we switch from imperative to declarative programming.

Once my students have learned basic JavaScript, we go over functional programming and the array methods used in a declarative coding style. This is where their brains start to pop and sizzle and melt like marshmallows over a fire.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/marshmellows-on-grill-crop-1.jpg)

## What is Imperative Programming?

As a beginner, you've probably mostly coded in an imperative style: you give the computer a set of instructions to follow and the computer does what you want in an easy-to-follow sequence.

Imagine we have a list of the world’s most commonly-used passwords:

```javascript
const passwords = [
   "123456",
   "password",
   "admin",
   "freecodecamp",
   "mypassword123",
];
```

Our app is going to check the user’s password on sign up and not allow them to create a password that is from this list.

But before we do that, we want to refine this list. We already have code that doesn’t allow the user to sign up with a password less than 9 characters long. So we can reduce this list to just passwords that are 9 characters or more to speed up our check.

Imperatively, we would write:

```javascript
// using the passwords constant from above

let longPasswords = [];
for (let i = 0; i < passwords.length; i++) {
   const password = passwords[i];
   if (password.length >= 9) {
      longPasswords.push(password);
   }
}

console.log(longPasswords); // logs ["freecodecamp", "mypassword123"];
```

1. We create an empty list called `longPasswords`.
2. Then we write a loop that will run as many times as there are passwords in the original `passwords` list.
3. Then we get the password at the index of the loop iteration we are presently on.
4. Then we check if that password is greater than or equal to 9 characters long.
5. If it is, we put it into the `longPasswords` list.

One of imperative programming’s strengths is the fact that it is easy to reason about. Like a computer, we can follow along step by step.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/steps-crop.jpg)

## What is Declarative Programming?

But there's another way of thinking about coding – as a process of constantly defining what things are. This is referred to as declarative programming.

Imperative and declarative programming achieve the same goals. They are just different ways of thinking about code. They have their benefits and drawbacks and there are times to use both.

Though imperative programming is easier to reason about for beginners, declarative programming allows us to write more readable code that reflects what exactly we want to see. Combined with [good variable names](https://github.com/10xcodecamp/javascript-conventions-and-code-style), it can be a powerful tool.

So instead of giving the computer step by step instructions, we declare what it is we want and we assign this to the result of some process.

```javascript
// using the passwords constant from above

const longPasswords = passwords.filter(password => password.length >= 9);

console.log(longPasswords); // logs ["freecodecamp", "mypassword123"];
```

The list of `longPasswords` is defined (or declared) as the list of `passwords` filtered for only passwords greater than or equal to 9 characters.

The functional programming methods in JavaScript enable us to cleanly declare things.

* **This is a list of passwords.**
* **This is a list of only long passwords.** (After running `filter`.)
* **This is a list of passwords with ids.** (After running `map`.)
* **This is a single password.** (After running `find`.)

One of declarative programming’s strengths is that it forces us to ask what we want first. It is in the naming of these new things that our code becomes expressive and explicit. 

And when our fellow developers come along and look at our code, they can find bugs more easily:

“You call this variable ‘index’ which makes me expect a number, but I see it is the result of `filter` which returns an array. What’s up with that?”

![Image](https://www.freecodecamp.org/news/content/images/2020/10/women-coding-at-home-crop.jpg)

I encourage learners to write declarative code as often as possible, constantly defining (and refactoring to redefine) what things are. 

Rather than hold an entire imperative process in your head, you can hold a more tangible **thing** in your head with a clear definition.

_Mike Zetlow is the Lead Instructor at_ [_10x Code Camp_](https://www.10xcodecamp.com/)_._

