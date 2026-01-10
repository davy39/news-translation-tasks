---
title: Fall-Through in JavaScript Switch Statements – Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-02T17:42:59.000Z'
originalURL: https://freecodecamp.org/news/fall-through-in-javascript-switch-statements
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/14.-fall-through-2.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Dillion Megida

  Switch statements in JavaScript have a behavior called fall-through which can cause
  unexpected results. I will explain what this behavior is, how to avoid it, and use
  cases for it.

  Switch statements allow you to create conditional s...'
---

By Dillion Megida

Switch statements in JavaScript have a behavior called **fall-through** which can cause unexpected results. I will explain what this behavior is, how to avoid it, and use cases for it.

Switch statements allow you to create conditional statements in JavaScript. You have a conditional expression, and depending on the returned value of that expression, you can have different cases. The case that matches that expression will be executed.

Let's look at the fall-through behavior of switch statements.

## What is This Fall-through Behavior?

Take a look at this switch statement example:

```js
const expression = 10 - 5

switch (expression) {
  case 1:
    console.log("The result is 1")
    break

  case 5:
    console.log("The result is 5")
    break

  case 10:
    console.log("The result is 10")
    break

  default:
    console.log("The result does not exist")
}

// The result is 5
```

Here, we have the expression: `10 - 5`. Using the `switch` operator, we switch between different `case`s, one of which matches the expression's returned value.

In the example, `case 5` matches the expression so the code `console.log("The result is 5")` in this case will be executed.

As you can see, the logged result is "The result is 5".

If our expression was `10 - 1`, the result will be 9. Since there is no case for this value, the `default` case will be run and the logged result will be:

```js
// The result does not exist
```

One common statement you find in all cases is the `break` statement. What if that statement wasn't in those cases? Let's see what happens:

```js
const expression = 10 - 5

switch (expression) {
  case 1:
    console.log("The result is 1")

  case 5:
    console.log("The result is 5")

  case 10:
    console.log("The result is 10")

  default:
    console.log("The result does not exist")
}

// The result is 5
// The result is 10
// The result does not exist
```

What do you notice?

Case 5, case 10, and the default case are executed. This is the **fall-through behavior** at work.

When you have `case`s and an expression, the `switch` statement finds the first case that matches the expression. It starts from the first case, `case 1`. That case doesn't match, so the `switch` statement continues its search. Then it finds `case 5`. This case matches the expression.

When the `switch` statement finds this first case that matches the expression, it does a fall-through where it runs the remaining cases after the matched case. It doesn't matter if the remaining cases match the expression or not, they will be executed. 

I have a [video version explaining this behavior](https://youtu.be/huQAwJIkYwk) which you can check out.

You're probably thinking "what's the benefit of this behavior?". We'll look at that later in this article.

## The Break Keyword in Switch Statements

The `break` keyword, as you saw in the first example, is a way to inform the `switch` statement, **do not fall through; stop here**. Without this statement, a fall-through happens, which means the case which matches the expression will be executed, as well as every other case that follows.

Let's say we have a `break` in our `case 10`:

```js
const expression = 10 - 5

switch (expression) {
  case 1:
    console.log("The result is 1")

  case 5:
    console.log("The result is 5")

  case 10:
    console.log("The result is 10")
    break

  default:
    console.log("The result does not exist")
}

// The result is 5
// The result is 10
```

From the logs, what do you notice here? Case 5, the matching case, is executed. We have "The result is 5" logged. There's no `break` statement, so `switch` continues with the cases that follow.

Case 10, the next case after case 5, is executed. We have "The result is 10" logged. Then, the `switch` statement encounters a `break` which is its signal to stop. Therefore, the remaining cases are not executed.

Now, you see why we had a `break` in every case:

```js
const expression = 10 - 5

switch (expression) {
  case 1:
    console.log("The result is 1")
    break

  case 5:
    console.log("The result is 5")
    break

  case 10:
    console.log("The result is 10")
    break

  default:
    console.log("The result does not exist")
}

// The result is 5
```

Its relevance is so we can execute only the case that matches our expression.

## Does the Default Case Need a Break?

In our example, every case has a `break`, but the `default` case doesn't. Does the default case need one? Well, it depends on the location where the default case is placed.

In our example, the `default` case is the last. When this case is executed (as there is no matched case for the expression), a fall-through is expected to happen as there's no `break` statement. 

But since the default case comes last, there's no other case that follows it in which the `switch` statement would fall through.

But let's say we had a different order for the `default` case:

```js
const expression = 10 - 1

switch (expression) {
  case 1:
    console.log("The result is 1")

  default:
    console.log("The result does not exist")

  case 5:
    console.log("The result is 5")

  case 10:
    console.log("The result is 10")
}

// The result does not exist
// The result is 5
// The result is 10
```

Here, the expression is `10 - 1`, and we've removed all the `break`s. The `default` case is the second in the `switch` statement. What do you notice in the logs?

As there's no case that matches the expression, the `default` case is executed. But this case does not have a `break` and there are other cases below it. So, the cases (5 and 10) after the `default` case are also executed.

That's why I stated that it depends on the location the `default` case is placed. In this example, it would be important to add a `break` to `default`. And then, we can skip a `break` in case 10, as that is the last case:

```js
const expression = 10 - 1

switch (expression) {
  case 1:
    console.log("The result is 1")
    break

  default:
    console.log("The result does not exist")
    break

  case 5:
    console.log("The result is 5")
    break

  case 10:
    console.log("The result is 10")
}

// The result does not exist
```

## Benefits of the Fall-through Behavior

This behavior might look like a bug, but it's actually not. It has its benefit. You can take advantage of this behavior to group related cases. Here's an example:

```js
const expression = 10 - 2

switch (expression) {
  case 2:
    console.log("The result is less than 8")
    break;

  case 5:
    console.log("The result is less than 8")
    break;

  case 8:
    console.log("The result is 8")
    break;

  default:
    console.log("The result does not exist")
}

// The result is 8
```

Here, we have a condition of `10 - 2`. Case 8 matches this expression, so we have "The result is 8" in the console.

If we change the condition to `10 - 8`, case 2 will match the expression, and we will have "The result is less than 8" in the console. 

If we change the condition to `10 - 5`, case 5 will match the expression, and we will have "The result is less than 8" in the console. 

Notice that the code for this case is similar to case 2? Then instead of writing them separately, we can group them together.

Here's how:

```js
const expression = 10 - 5

switch (expression) {
  case 2:

  case 5:
    console.log("The result is less than 8")
    break;

  case 8:
    console.log("The result is 8")
    break;

  default:
    console.log("The result does not exist")
}

// The result is less than 8
```

By removing the code and `break` keyword from case 2, we're able to combine case 2 and case 5. With a condition of `10 - 5`, case 5 matches, and we have "The result is less than 8" in the console.

With a condition of `10 - 8`, case 2 will match. There's no code in case 2, so nothing will be executed. Also, there's no `break` so fall-through happens, which means the next case, case 5, will be executed. 

After execution, we have "The result is less than 8" printed to the console. The `switch` statement encounters a `break` keyword here, so it knows to stop.

We have been able to group case 2 and case 5, since they are related, by taking advantage of the fall-through behavior. There are so many scenarios where you can use this behavior.

## Wrap up

In this article, we've looked at the fall-through behavior in switch statements. This behavior involves executing other cases after the matched case of an expression. It happens by default, but can be prevented with the `break` keyword as we have seen in different examples.

We've also seen the benefit of this behavior, as it helps to group related cases.

When I started learning JavaScript, I learned to always use `break` in my switch cases, but I never fully understood why. I thought it was just the syntax of switch statements. 

But only after some time, I came to understand what the `break` statement was doing – preventing fall-throughs.

Maybe you have a similar story, or not, but I hope this article teaches you something about switch statements. Please share it if you found it helpful.



